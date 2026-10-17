"""M1 acceptance regressions. Every test owns an isolated vault."""
from pathlib import Path
import shutil
import subprocess
import sys

import frontmatter
import pytest

from _scripts import pipeline
from _scripts.collect import normalize_release, source_result
from _scripts.common import PipelinePaths, read_json, write_json
from _scripts.history import read_history
from _scripts.transaction import recover, snapshot, vault_lock

ROOT = Path(__file__).resolve().parents[1]
DAY = "2026-07-29"


@pytest.fixture
def vault(tmp_path):
    shutil.copytree(ROOT / "_scripts", tmp_path / "_scripts", ignore=shutil.ignore_patterns("__pycache__"))
    return tmp_path


def release(product="cursor", date="2026-07-01", body="- Agent can run shell commands after approval",
            source_type="github_releases"):
    return normalize_release(
        {"name": product, "display_name": {"cursor": "Cursor", "chatgpt": "ChatGPT"}[product]},
        release_date=date, version=date, title=f"Release {date}", body=body,
        source_url=f"https://example.com/{product}/{date}", source_type=source_type,
    )


# List lines without a theme are published as "Other changes"; prose without a theme
# is what still waits in the review queue.
PENDING_PROSE = "New quasar renderer for geometric palettes."


def prose_release(date="2026-07-01", body=PENDING_PROSE):
    return release(date=date, body=body, source_type="cursor_changelog")


def collection(releases, *, mode="full", requested=None, complete=None):
    requested = requested or sorted({r["product"] for r in releases})
    return {
        "source": "live", "mode": mode, "releases": releases, "errors": [],
        "sources": [source_result(
            product, [r for r in releases if r["product"] == product],
            complete=mode == "full" if complete is None else complete,
            coverage="available-endpoint" if releases else "no-change",
        ) for product in requested],
    }


def run(vault, run_id, payload, **kwargs):
    return pipeline.run_pipeline(vault, run_id, collection=payload, today=DAY, **kwargs)


def cards(vault):
    return [frontmatter.load(p) for p in (vault / "Changes").rglob("*.md")]


def test_a1_full_then_incremental_uses_markdown_without_previous_run_json(vault):
    old, recent = release(date="2025-01-01"), release()
    full = collection([old, recent, release("chatgpt")])
    run(vault, "full", full, reconcile=True)
    shutil.rmtree(vault / "_pipeline")
    result = run(vault, "incremental", collection([recent], mode="incremental"))
    assert result["merged_cards"] == 3
    assert result["merged_releases"] == 3
    assert old["release_id"] in (vault / "Products/Cursor.md").read_text()
    assert "2025-01-01" in (vault / "Themes/agent-mode.md").read_text()
    assert "3 tracked changes" in (vault / "index.md").read_text()
    cursor = sorted((c for c in cards(vault) if c["product"] == "cursor"), key=lambda c: c["date"])
    assert cursor[1]["evolves_from"] == []
    earlier = next(p for p in (vault / "Changes").rglob("*.md")
                   if frontmatter.load(p)["card_id"] == cursor[0]["card_id"])
    target = earlier.relative_to(vault).with_suffix("").as_posix()
    # Relation links name the target card by its title, not its card_id.
    assert cursor[1]["related_changes"][0] == f"[[{target}|{cursor[0]['title']}]]"
    assert read_json(PipelinePaths("incremental", vault).validation_round2)["errors"] == []


def test_a2_repeat_preserves_ids_paths_human_regions_and_overrides(vault):
    payload = collection([release()])
    run(vault, "full", payload, reconcile=True)
    path = next((vault / "Changes").rglob("*.md"))
    post = frontmatter.load(path)
    post["human_overrides"] = {"title": "Research title"}
    post.content += "\n\nHuman research notes."
    path.write_text(frontmatter.dumps(post))
    before = snapshot(vault)
    result = run(vault, "repeat", payload, reconcile=True)
    assert result["status"] == "no-change"
    assert snapshot(vault) == before
    assert frontmatter.load(path)["human_overrides"] == {"title": "Research title"}


@pytest.mark.parametrize("all_failed", [False, True])
def test_a3_source_failures_preserve_vault_and_report_collection_error(vault, monkeypatch, all_failed):
    run(vault, "seed", collection([release(), release("chatgpt")]))
    before = snapshot(vault)
    payload = collection([] if all_failed else [release()], requested=["cursor", "chatgpt"])
    failed = {"cursor", "chatgpt"} if all_failed else {"chatgpt"}
    for source in payload["sources"]:
        if source["product"] in failed:
            source.update(status="failed", error="HTTP 503", complete=False)
    payload["errors"] = [{"product": p, "error": "HTTP 503"} for p in sorted(failed)]
    def collect(*args, **kwargs):
        write_json(args[1], payload)
        return payload
    monkeypatch.setattr(pipeline, "collect_live", collect)
    with pytest.raises(ValueError, match="collection failed"):
        pipeline.run_pipeline(vault, "failure", today=DAY)
    assert snapshot(vault) == before
    manifest = read_json(vault / "_pipeline/failure/manifest.json")
    assert manifest["status"] == "failed"
    assert {s["product"] for s in manifest["sources"] if s["status"] == "failed"} == failed
    silence = read_json(PipelinePaths("failure", vault).silence)
    assert silence["alerts"] == []
    assert {s["product"] for s in silence["pending"]} == failed


def test_a4_success_no_new_releases_is_no_change(vault):
    run(vault, "seed", collection([release()]))
    before = snapshot(vault)
    result = run(vault, "empty-delta", collection([], mode="incremental", requested=["cursor"]))
    assert result["status"] == "no-change"
    assert snapshot(vault) == before


def test_a5_scoped_reconcile_preserves_unselected_and_pending_history(vault):
    old, recent, other = release(date="2025-01-01"), release(), release("chatgpt")
    candidate = prose_release(date="2025-02-01")
    run(vault, "seed", collection([old, recent, other, candidate]))
    pending_id = next((vault / "_review").glob("*.md")).stem
    shutil.rmtree(vault / "_pipeline")
    result = run(vault, "reconcile", collection([recent]), reconcile=True)
    assert result["reconcile_products"] == ["cursor"]
    assert result["pending_theme_review"] == 1
    assert (vault / "_review" / f"{pending_id}.md").exists()
    old_card = next(c for c in cards(vault) if c["product"] == "cursor" and c["date"] == "2025-01-01")
    assert old_card["superseded"] is True
    assert not next(c for c in cards(vault) if c["product"] == "chatgpt").get("superseded")
    assert other["release_id"] in (vault / "Products/ChatGPT.md").read_text()
    assert candidate["release_id"] in (vault / "Products/Cursor.md").read_text()
    assert old["release_id"] not in (vault / "Products/Cursor.md").read_text()


@pytest.mark.parametrize("mode,complete", [("incremental", False), ("full", False)])
def test_a6_reconcile_rejects_incomplete_scope(vault, mode, complete):
    run(vault, "seed", collection([release()]))
    before = snapshot(vault)
    with pytest.raises(ValueError, match="complete full collection"):
        run(vault, "truncated", collection([release()], mode=mode, complete=complete), reconcile=True)
    assert snapshot(vault) == before


def test_a6_round1_dlq_prevents_superseding_existing_card(vault, monkeypatch):
    payload = collection([release()])
    run(vault, "seed", payload)
    before = snapshot(vault)
    original = pipeline.extract_run
    def invalid(run_id, root):
        original(run_id, root=root)
        paths = PipelinePaths(run_id, root)
        extracted = read_json(paths.extracted)
        extracted["change_cards"][0]["description"] = ""
        write_json(paths.extracted, extracted)
    monkeypatch.setattr(pipeline, "extract_run", invalid)
    with pytest.raises(ValueError, match="round 1 failed"):
        run(vault, "invalid", payload, reconcile=True)
    assert snapshot(vault) == before
    assert read_json(PipelinePaths("invalid", vault).dlq)["failed"]


def test_a6_round2_failure_keeps_published_files(vault, monkeypatch):
    run(vault, "seed", collection([release()]))
    before = snapshot(vault)
    original = pipeline.write_run
    def break_link(*args, **kwargs):
        result = original(*args, **kwargs)
        path = kwargs["root"] / "Products/Cursor.md"
        path.write_text(path.read_text() + "\n[[nonexistent-page]]\n")
        return result
    monkeypatch.setattr(pipeline, "write_run", break_link)
    with pytest.raises(ValueError, match="round 2 failed"):
        run(vault, "broken-links", collection([release(date="2026-07-02")]))
    assert snapshot(vault) == before
    assert read_json(PipelinePaths("broken-links", vault).validation_round2)["errors"]


def test_a6_machine_edit_is_preserved_and_blocks_run(vault):
    run(vault, "seed", collection([release()]))
    path = vault / "Products/Cursor.md"
    path.write_text(path.read_text().replace("verbosity_baseline: 1.0", "verbosity_baseline: 99.0"))
    before = snapshot(vault)
    with pytest.raises(ValueError, match="machine_hash conflict"):
        run(vault, "conflict", collection([release()]))
    assert snapshot(vault) == before


def test_a7_mid_commit_exception_rolls_back_new_and_existing_files(vault):
    run(vault, "seed", collection([release()]))
    before = snapshot(vault)
    seen = []
    def fail(index, path):
        seen.append(path)
        if index == 2:
            raise OSError("injected disk failure")
    with pytest.raises(OSError, match="injected disk failure"):
        run(vault, "interrupted", collection([release(date="2026-07-02")]), after_write=fail)
    assert len(seen) == 3
    assert snapshot(vault) == before
    assert not (vault / "_pipeline/transaction.json").exists()
    assert run(vault, "recovered", collection([release(date="2026-07-02")]))["status"] == "published"


def test_a7_process_death_recovers_from_journal_without_old_run_json(vault):
    run(vault, "seed", collection([release()]))
    before = snapshot(vault)
    payload_path = vault / "input.json"
    write_json(payload_path, collection([release(date="2026-07-02")]))
    script = '''
import os, sys
from pathlib import Path
from _scripts.pipeline import run_pipeline
from _scripts.common import read_json
root = Path(sys.argv[1])
def die(index, path):
    if index == 2:
        os._exit(73)
run_pipeline(root, "crashed", collection=read_json(root / "input.json"), today="2026-07-29", after_write=die)
'''
    result = subprocess.run([sys.executable, "-c", script, str(vault)], cwd=ROOT)
    assert result.returncode == 73
    assert snapshot(vault) != before
    assert (vault / "_pipeline/transaction.json").exists()
    result = subprocess.run([sys.executable, str(ROOT / "_scripts/run_pipeline.py"),
                             "--root", str(vault), "--recover-only"], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert snapshot(vault) == before
    assert not (vault / "_pipeline/transaction.json").exists()


def test_a8_execution_day_timezone_override_and_historical_silence(vault, monkeypatch):
    from datetime import datetime, timezone
    class Clock:
        @classmethod
        def now(cls, zone):
            return datetime(2026, 7, 29, 18, 0, tzinfo=timezone.utc).astimezone(zone)
        strptime = datetime.strptime
    monkeypatch.setattr(pipeline, "datetime", Clock)
    assert pipeline.execution_date("Asia/Shanghai") == "2026-07-30"
    assert pipeline.execution_date("UTC") == "2026-07-29"
    releases = [release(date=f"2025-0{m}-01") for m in range(1, 5)]
    pipeline.run_pipeline(vault, "seed", collection=collection(releases), today="2025-04-15")
    result = pipeline.run_pipeline(vault, "today", collection=collection([releases[-1]], mode="incremental"))
    assert result["today"] == "2026-07-30"
    assert read_json(PipelinePaths("today", vault).silence)["alerts"][0]["product"] == "cursor"
    pipeline.run_pipeline(vault, "replay", collection=collection([releases[-1]], mode="incremental"), today="2025-04-15")
    assert read_json(PipelinePaths("replay", vault).silence)["alerts"] == []


def test_cli_failure_returns_nonzero_and_leaves_vault(vault):
    run(vault, "seed", collection([release()]))
    before = snapshot(vault)
    bad = collection([], requested=["cursor"])
    bad["errors"] = [{"product": "cursor", "error": "offline"}]
    write_json(vault / "input.json", bad)
    result = subprocess.run([sys.executable, str(ROOT / "_scripts/run_pipeline.py"),
                             "--root", str(vault), "--run-id", "cli-error",
                             "--collection", str(vault / "input.json")], cwd="/tmp", capture_output=True, text=True)
    assert result.returncode == 1
    assert snapshot(vault) == before


def test_concurrent_run_and_reused_run_id_are_rejected(vault):
    payload = collection([release()])
    run(vault, "seed", payload)
    before = snapshot(vault)
    with pytest.raises(ValueError, match="run-id already exists"):
        run(vault, "seed", payload)
    with vault_lock(vault), pytest.raises(RuntimeError, match="vault lock"):
        run(vault, "locked", payload)
    assert snapshot(vault) == before


def test_reconcile_refreshes_theme_after_its_last_card_is_retired(vault):
    old = release(date="2025-01-01", body="- Context window expanded to 200K tokens")
    latest = release()
    run(vault, "seed", collection([old, latest]))
    assert "2025-01-01" in (vault / "Themes/context-window.md").read_text()
    run(vault, "remove", collection([latest]), reconcile=True)
    assert "No changes yet." in (vault / "Themes/context-window.md").read_text()
    assert "2025-01-01" not in (vault / "Themes/context-window.md").read_text()
    assert "Themes/context-window" not in (vault / "index.md").read_text()


def test_a1_new_release_extends_full_history_and_cross_product_relations(vault):
    run(vault, "seed", collection([release(), release("chatgpt")]))
    new = release(date="2026-07-02")
    result = run(vault, "new", collection([new], mode="incremental"))
    assert result["merged_cards"] == 3
    newest = next(c for c in cards(vault) if c["date"] == new["date"])
    assert newest["diffusion"]["tracked_products_count"] == 2
    assert newest["evolves_from"] == []
    assert newest["related_changes"]
    assert "2026-07-01" in (vault / "Products/Cursor.md").read_text()
    assert "2026-07-02" in (vault / "Products/Cursor.md").read_text()


def test_pending_promotion_survives_without_run_json_and_keeps_review_notes(vault):
    import yaml
    unknown = prose_release()
    run(vault, "seed", collection([unknown]))
    path = next((vault / "_review").glob("*.md"))
    path.write_text(path.read_text() + "\n\nHuman review notes.")
    shutil.rmtree(vault / "_pipeline")
    themes_path = vault / "_scripts/themes.yaml"
    themes = yaml.safe_load(themes_path.read_text())
    next(t for t in themes["themes"] if t["slug"] == "editor-experience")["aliases"].append("quasar")
    themes_path.write_text(yaml.safe_dump(themes))
    result = run(vault, "promote", collection([unknown]), reconcile=True)
    assert result["pending_theme_review"] == 0
    assert len(cards(vault)) == 1
    assert not path.exists()
    assert "Human review notes." in (vault / "_review/resolved" / path.name).read_text()


def test_legacy_markdown_without_record_field_can_be_merged(vault):
    from _scripts.writer import content_machine_hash
    run(vault, "seed", collection([release(), release("chatgpt")]))
    for directory in ("Changes", "Releases"):
        for path in (vault / directory).rglob("*.md"):
            post = frontmatter.load(path)
            del post["record"]
            post["machine_hash"] = content_machine_hash(frontmatter.dumps(post))
            path.write_text(frontmatter.dumps(post))
    shutil.rmtree(vault / "_pipeline")
    result = run(vault, "migrate", collection([release()], mode="incremental"))
    assert result["merged_cards"] == 2
    assert len(read_history(vault, {"cursor", "chatgpt"})[0]) == 2


def test_legacy_card_with_human_notes_is_reported_not_blocking(vault):
    from _scripts.writer import content_machine_hash, extract_machine_regions, machine_region
    run(vault, "seed", collection([release()]))
    path = next((vault / "Changes").rglob("*.md"))
    post = frontmatter.load(path)
    evidence = extract_machine_regions(post.content)["evidence"]
    post.content = (f"# {post['record']['title']}\n\n{machine_region('evidence', evidence)}\n\n"
                    "## Editor Notes\n\nHuman research notes.")
    post["machine_hash"] = content_machine_hash(frontmatter.dumps(post))
    path.write_text(frontmatter.dumps(post))
    result = run(vault, "legacy", collection([release()]), reconcile=True)
    assert result["writer_migration_pending"] == 1
    pending = read_json(vault / "_pipeline/legacy/writer-migration-pending.json")
    assert pending == [{"file": path.relative_to(vault).as_posix(),
                        "reason": "legacy skeleton with human text; manual migration needed"}]
    assert "Human research notes." in path.read_text()
    assert "Report an issue" not in path.read_text()
    result = run(vault, "clean", collection([release()]), reconcile=True)
    assert result["writer_migration_pending"] == 1
    path.write_text(path.read_text().replace("\n\nHuman research notes.", ""))
    post = frontmatter.load(path)
    post["machine_hash"] = content_machine_hash(frontmatter.dumps(post))
    path.write_text(frontmatter.dumps(post))
    result = run(vault, "migrated", collection([release()]), reconcile=True)
    assert result["writer_migration_pending"] == 0
    assert not (vault / "_pipeline/migrated/writer-migration-pending.json").exists()
    assert list(extract_machine_regions(frontmatter.load(path).content)) == [
        "header", "evidence", "context", "nearby", "relations", "footer"]


def test_fixture_cannot_overwrite_live_vault(vault):
    run(vault, "seed", collection([release()]))
    shutil.copytree(ROOT / "tests/fixtures", vault / "tests/fixtures")
    before = snapshot(vault)
    with pytest.raises(ValueError, match="separate vault"):
        pipeline.run_pipeline(vault, "fixture", fixture=True, today=DAY)
    assert snapshot(vault) == before


def test_concurrent_human_edit_during_preparation_is_not_overwritten(vault, monkeypatch):
    run(vault, "seed", collection([release()]))
    path = vault / "Products/Cursor.md"
    original = pipeline.validate_vault_links
    def edit_then_validate(*args, **kwargs):
        path.write_text(path.read_text() + "\n\nConcurrent human note.")
        return original(*args, **kwargs)
    monkeypatch.setattr(pipeline, "validate_vault_links", edit_then_validate)
    with pytest.raises(RuntimeError, match="vault changed during preparation"):
        run(vault, "concurrent-edit", collection([release(date="2026-07-02")]))
    assert "Concurrent human note." in path.read_text()
    assert len(cards(vault)) == 1


def test_source_completeness_empty_responses_and_rss_windows(vault, monkeypatch):
    from _scripts import collect
    import yaml
    sources = {"products": [
        {"name": "cursor", "display_name": "Cursor", "feed_type": "github_releases", "repo": "owner/repo"},
        {"name": "chatgpt", "display_name": "ChatGPT", "feed_type": "blog_rss", "url": "https://example.com/feed"},
    ]}
    path = vault / "sources.yaml"
    path.write_text(yaml.safe_dump(sources))
    monkeypatch.setattr(collect, "fetch_github_releases", lambda *_: [release()])
    monkeypatch.setattr(collect, "fetch_rss_releases", lambda *_: [release("chatgpt")])
    full = collect.collect_live(path, vault / "full.json", None, backfill="all")
    assert [s["complete"] for s in full["sources"]] == [True, False]
    assert full["sources"][1]["coverage"] == "feed-window"
    limited = collect.collect_live(path, vault / "limited.json", 1, backfill="all")
    assert not any(s["complete"] for s in limited["sources"])
    monkeypatch.setattr(collect, "fetch_github_releases", lambda *_: [])
    empty = collect.collect_live(path, vault / "empty.json", None, backfill="cursor")
    assert empty["sources"][0]["status"] == "failed"
    assert empty["errors"] and not empty["sources"][0]["complete"]


def test_recovery_manifest_and_restart_are_idempotent(vault):
    from _scripts.transaction import atomic_write
    run(vault, "seed", collection([release()]))
    old_path = vault / "index.md"
    old = old_path.read_bytes()
    import hashlib
    before_hash = hashlib.sha256(old).hexdigest()
    atomic_write(vault / "_pipeline/transaction-backup/index.md", old)
    atomic_write(old_path, b"interrupted new content")
    journal = {"run_id": "interrupted", "status": "applying", "files": [
        {"path": "index.md", "before": before_hash,
         "after": hashlib.sha256(b"interrupted new content").hexdigest()}
    ]}
    write_json(vault / "_pipeline/transaction.json", journal)
    write_json(vault / "_pipeline/interrupted/manifest.json", {"status": "preparing"})
    result = run(vault, "restart", collection([release()]))
    assert result["recovered_run"] == "interrupted"
    assert old_path.read_bytes() == old
    assert read_json(vault / "_pipeline/interrupted/manifest.json")["status"] == "recovered"
    assert recover(vault) is None


def test_snapshot_input_is_copied_and_hashed(vault, monkeypatch):
    import hashlib
    source = vault / "snapshot.html"
    source.write_text("<article>offline source evidence</article>")
    payload = collection([release("chatgpt")])
    def fake_collect(config, output, limit, backfill, snapshot_paths):
        saved = snapshot_paths["chatgpt"]
        assert saved != source and saved.read_bytes() == source.read_bytes()
        write_json(output, payload)
        return payload
    monkeypatch.setattr(pipeline, "collect_live", fake_collect)
    result = pipeline.run_pipeline(vault, "snapshot", snapshot_paths={"chatgpt": source}, today=DAY)
    assert result["snapshots"]["chatgpt"]["sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
    assert (vault / "_pipeline/snapshot/00-snapshots/chatgpt.html").exists()


def test_a6_existing_accepted_card_is_protected_when_reclassified_pending(vault, monkeypatch):
    payload = collection([release()])
    run(vault, "seed", payload)
    old_id = cards(vault)[0]["card_id"]
    original = pipeline.extract_run
    def candidate(run_id, root):
        original(run_id, root=root)
        paths = PipelinePaths(run_id, root)
        extracted = read_json(paths.extracted)
        extracted["change_cards"][0].update(theme="__candidate__", theme_suggestion="reconsider")
        write_json(paths.extracted, extracted)
    monkeypatch.setattr(pipeline, "extract_run", candidate)
    result = run(vault, "pending", payload, reconcile=True)
    assert result["pending_theme_review"] == 1
    assert cards(vault)[0]["card_id"] == old_id
    assert not cards(vault)[0].get("superseded")
    assert (vault / "_review" / f"{old_id}.md").exists()


def test_committed_journal_cleanup_does_not_rollback_published_content(vault):
    run(vault, "seed", collection([release()]))
    before = snapshot(vault)
    write_json(vault / "_pipeline/transaction.json", {
        "run_id": "seed", "status": "committed", "files": [],
    })
    assert recover(vault) == "seed"
    assert snapshot(vault) == before
    assert read_json(vault / "_pipeline/seed/manifest.json")["status"] == "published"


def test_recovery_conflict_preserves_external_edit_and_backup(vault):
    import hashlib
    run(vault, "seed", collection([release()]))
    path = vault / "index.md"
    old = path.read_bytes()
    backup = vault / "_pipeline/transaction-backup/index.md"
    backup.parent.mkdir(parents=True)
    backup.write_bytes(old)
    write_json(vault / "_pipeline/transaction.json", {
        "run_id": "seed", "status": "applying", "files": [{
            "path": "index.md", "before": hashlib.sha256(old).hexdigest(),
            "after": hashlib.sha256(b"new machine output").hexdigest(),
        }],
    })
    path.write_text("Human edit after interruption")
    with pytest.raises(RuntimeError, match="recovery conflict"):
        recover(vault)
    assert path.read_text() == "Human edit after interruption"
    assert backup.read_bytes() == old
    assert (vault / "_pipeline/transaction.json").exists()


def test_repeated_pending_resolution_preserves_earlier_review_notes(vault):
    from _scripts.history import write_pending
    from _scripts.extract import extract_cards_from_release, load_theme_vocabulary
    candidate = extract_cards_from_release(
        prose_release(), load_theme_vocabulary(vault / "_scripts/themes.yaml"),
    )[0]
    assert candidate["theme"] == "__candidate__"
    write_pending(vault, [candidate], {"cursor"})
    path = vault / "_review" / f"{candidate['card_id']}.md"
    path.write_text(path.read_text() + "\n\nFirst review notes.")
    write_pending(vault, [], {"cursor"})
    write_pending(vault, [candidate], {"cursor"})
    path.write_text(path.read_text() + "\n\nSecond review notes.")
    write_pending(vault, [], {"cursor"})
    archived = list((vault / "_review/resolved").glob("*.md"))
    assert len(archived) == 2
    assert any("First review notes." in p.read_text() for p in archived)
    assert any("Second review notes." in p.read_text() for p in archived)


def test_list_lines_without_a_theme_publish_as_other_changes_and_retire_old_queue_entries(vault):
    from _scripts.extract import extract_cards_from_release, load_theme_vocabulary
    from _scripts.history import write_pending
    listed = release(body="- New quasar renderer for geometric palettes\n"
                          "- Zephyr gauges round half values up")
    run(vault, "seed", collection([listed]))
    assert not list((vault / "_review").glob("*.md"))
    [card] = cards(vault)
    assert (card["theme"], card["kind"], card["title"]) == (
        "uncategorized", "digest", "2 other changes in 2026-07-01")
    assert not (vault / "Themes/uncategorized.md").exists()
    assert "Other changes · Digest" in next((vault / "Releases").rglob("*.md")).read_text()
    # Queue entries the previous card definition left for the same lines (one per line)
    # retire in an incremental run: their lines joined a card of the same release.
    themes = load_theme_vocabulary(vault / "_scripts/themes.yaml")
    official = {slug: theme for slug, theme in themes.items() if theme["status"] == "official"}
    old_entries = extract_cards_from_release(listed, official)
    assert [entry["theme"] for entry in old_entries] == ["__candidate__"] * 2
    write_pending(vault, old_entries, {"cursor"})
    shutil.rmtree(vault / "_pipeline")

    result = run(vault, "incremental", collection([listed], mode="incremental"))

    assert result["pending_theme_review"] == 0
    assert not list((vault / "_review").glob("*.md"))
    assert len(list((vault / "_review/resolved").glob("*.md"))) == 2
    assert [c["card_id"] for c in cards(vault)] == [card["card_id"]]
