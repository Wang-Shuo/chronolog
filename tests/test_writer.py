from pathlib import Path

import frontmatter
import pytest

from _scripts.common import PipelinePaths, write_json
from _scripts.writer import (
    change_card_paths,
    ensure_vault_dirs,
    main,
    reconcile_missing_change_cards,
    render_change_markdown,
    render_release_markdown,
    render_theme_markdown,
    replace_machine_region,
    write_markdown_file,
    write_run,
)


def test_replace_machine_region_preserves_human_content():
    existing = """# Cursor

Human intro.

<!-- chronolog:begin region="eras" -->
old
<!-- chronolog:end -->

## Editor Notes
Keep this.
"""

    updated = replace_machine_region(existing, "eras", "new")

    assert "Human intro." in updated
    assert "Keep this." in updated
    assert "new" in updated
    assert "old" not in updated


def test_render_theme_markdown_contains_mermaid_timeline(tmp_path: Path):
    cards = [
        {
            "card_id": "aider-2025-01-01-aaaaaa",
            "product": "aider",
            "product_name": "Aider",
            "date": "2025-01-01",
            "title": "Agent mode",
            "theme": "agent-mode",
            "slug": "agent-mode",
        },
        {
            "card_id": "cursor-2025-02-01-bbbbbb",
            "product": "cursor",
            "product_name": "Cursor",
            "date": "2025-02-01",
            "title": "Agent shell",
            "theme": "agent-mode",
            "slug": "agent-shell",
        },
    ]

    markdown = render_theme_markdown("agent-mode", cards)

    assert "```mermaid" in markdown
    assert "timeline" in markdown
    assert "Aider" in markdown
    assert "Cursor" in markdown


def test_write_markdown_file_detects_machine_region_edits(tmp_path: Path):
    target = tmp_path / "change.md"
    card = {
        "type": "change",
        "card_id": "cursor-2025-02-01-aaaaaa",
        "product": "cursor",
        "product_name": "Cursor",
        "source_release": "cursor-2025-02-01-v1",
        "date": "2025-02-01",
        "title": "Agent shell",
        "slug": "agent-shell",
        "theme": "agent-mode",
        "impact": "incremental",
        "description": "Agent can run shell commands.",
        "comparison": "",
        "evidence": [{"source_release": "https://example.com", "quote": "Agent can run shell commands."}],
        "extractor_version": "fallback-v1",
    }
    rendered = render_change_markdown(card, {"evolves_from": []}, {})
    write_markdown_file(target, rendered, [])

    target.write_text(
        target.read_text(encoding="utf-8").replace(
            "Agent can run shell commands.",
            "Edited machine text.",
        ),
        encoding="utf-8",
    )
    conflicts: list[dict[str, str]] = []

    wrote = write_markdown_file(target, rendered, conflicts)

    assert wrote is False
    assert conflicts[0]["file"] == str(target)
    assert "Edited machine text." in target.read_text(encoding="utf-8")


def test_write_markdown_file_preserves_custom_human_frontmatter(tmp_path: Path):
    target = tmp_path / "change.md"
    card = change_card()
    rendered = render_change_markdown(card, {"evolves_from": []}, {})
    write_markdown_file(target, rendered, [])
    post = frontmatter.load(target)
    post.metadata["research_note"] = "keep this"
    target.write_text(frontmatter.dumps(post), encoding="utf-8")

    wrote = write_markdown_file(target, rendered, [])

    assert wrote is True
    assert frontmatter.load(target).metadata["research_note"] == "keep this"


def test_change_card_paths_reuses_existing_path_for_stable_card_id(tmp_path: Path):
    target = tmp_path / "Changes" / "Cursor" / "2025-02-01-original-slug.md"
    target.parent.mkdir(parents=True)
    target.write_text(
        render_change_markdown(change_card(), {"evolves_from": []}, {}),
        encoding="utf-8",
    )
    renamed_card = {**change_card(), "slug": "new-title-slug", "title": "A new title"}

    paths, duplicates = change_card_paths(tmp_path, [renamed_card])

    assert duplicates == []
    assert paths[renamed_card["card_id"]] == target


def test_reconcile_missing_change_cards_marks_superseded_without_deleting(tmp_path: Path):
    target = tmp_path / "Changes" / "Cursor" / "2025-02-01-agent-shell.md"
    target.parent.mkdir(parents=True)
    target.write_text(
        render_change_markdown(change_card(), {"evolves_from": []}, {}),
        encoding="utf-8",
    )
    conflicts: list[dict[str, str]] = []

    superseded = reconcile_missing_change_cards(
        tmp_path,
        active_card_ids=set(),
        reconcile_products={"cursor"},
        conflicts=conflicts,
    )

    assert superseded == [change_card()["card_id"]]
    assert conflicts == []
    assert target.exists()
    assert frontmatter.load(target).metadata["superseded"] is True


def test_writer_cli_returns_nonzero_when_machine_conflict_exists(monkeypatch):
    monkeypatch.setattr("_scripts.writer.write_run", lambda *_args, **_kwargs: [{"error": "conflict"}])
    monkeypatch.setattr("sys.argv", ["writer.py", "--run-id", "demo"])

    with pytest.raises(SystemExit) as error:
        main()

    assert error.value.code == 1


def test_ensure_vault_dirs_creates_empty_alerts_directory(tmp_path: Path):
    ensure_vault_dirs(tmp_path)

    assert (tmp_path / "Products").is_dir()
    assert (tmp_path / "Changes").is_dir()
    assert (tmp_path / "Releases").is_dir()
    assert (tmp_path / "Themes").is_dir()
    assert (tmp_path / "Alerts").is_dir()


def test_writer_creates_release_page_when_release_has_no_publishable_cards(tmp_path: Path):
    run_id = "zero-card-release"
    paths = PipelinePaths(run_id, root=tmp_path)
    release = {
        "release_id": "chatgpt-2023-01-09-updates-a1b2c3d4",
        "product": "chatgpt",
        "product_name": "ChatGPT",
        "date": "2023-01-09",
        "version": "Updates to ChatGPT",
        "title": "Updates to ChatGPT",
        "body": "Maintenance update.",
        "source_summary": "Maintenance update.",
        "source_url": "https://help.openai.com/release#update",
        "source_type": "chatgpt_changelog",
    }
    write_json(
        paths.valid_cards,
        {"change_cards": [], "pending_theme_review": []},
    )
    write_json(paths.analyze_a, {"products": {}, "evolves_from": {}})
    write_json(paths.analyze_b, {"themes": {}, "cards": {}})
    write_json(paths.silence, {"alerts": [], "pending": []})
    write_json(paths.collected, {"source": "fixture", "releases": [release]})

    conflicts = write_run(run_id, root=tmp_path)

    pages = list((tmp_path / "Releases" / "ChatGPT").glob("*.md"))
    assert conflicts == []
    assert len(pages) == 1
    post = frontmatter.load(pages[0])
    assert post.metadata["release_id"] == release["release_id"]
    assert post.metadata["changes_count"] == 0
    assert "No change cards extracted." in post.content


def change_card() -> dict[str, object]:
    return {
        "type": "change",
        "card_id": "cursor-2025-02-01-aaaaaa",
        "product": "cursor",
        "product_name": "Cursor",
        "source_release": "cursor-2025-02-01-v1",
        "date": "2025-02-01",
        "title": "Agent shell",
        "slug": "agent-shell",
        "theme": "agent-mode",
        "impact": "incremental",
        "description": "Agent can run shell commands.",
        "comparison": "",
        "evidence": [
            {"source_release": "https://example.com", "quote": "Agent can run shell commands."}
        ],
        "extractor_version": "fallback-v1",
    }
