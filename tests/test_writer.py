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


def test_render_theme_markdown_contains_navigable_year_timeline(tmp_path: Path):
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

    assert "### 2025" in markdown
    assert "same-theme chronology" in markdown
    assert "timeline" in markdown
    assert "Aider" in markdown
    assert "Cursor" in markdown


def test_render_theme_markdown_strips_trailing_timeline_whitespace():
    card = {**change_card(), "title": "Agent shell   "}

    markdown = render_theme_markdown("agent-mode", [card])

    assert not any(line.endswith(" ") for line in markdown.splitlines())


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


def _card_heading(path: Path) -> str:
    return next(line for line in frontmatter.load(path).content.splitlines() if line.startswith("# "))


def test_write_markdown_file_refreshes_generated_card_heading(tmp_path: Path):
    target = tmp_path / "change.md"
    legacy = {**change_card(), "title": "We're adding an agent shell so agents can run comma"}
    write_markdown_file(target, render_change_markdown(legacy, {"evolves_from": []}, {}), [])
    target.write_text(
        target.read_text(encoding="utf-8").replace("## Editor Notes", "## Editor Notes\n\nKeep me."),
        encoding="utf-8",
    )
    retitled = {**legacy, "title": "Cursor adds an agent shell so agents can run commands"}
    conflicts: list[dict[str, str]] = []

    wrote = write_markdown_file(
        target, render_change_markdown(retitled, {"evolves_from": []}, {}), conflicts
    )

    assert wrote is True and conflicts == []
    post = frontmatter.load(target)
    assert _card_heading(target) == "# Cursor adds an agent shell so agents can run commands"
    assert post["record"]["title"] == retitled["title"]
    assert post["title"] == retitled["title"]
    assert "Keep me." in post.content


def test_write_markdown_file_preserves_edited_card_heading(tmp_path: Path):
    target = tmp_path / "change.md"
    card = change_card()
    write_markdown_file(target, render_change_markdown(card, {"evolves_from": []}, {}), [])
    target.write_text(
        target.read_text(encoding="utf-8").replace("# Agent shell\n", "# Curated agent shell\n"),
        encoding="utf-8",
    )
    retitled = {**card, "title": "Agent can run shell commands"}
    conflicts: list[dict[str, str]] = []

    wrote = write_markdown_file(
        target, render_change_markdown(retitled, {"evolves_from": []}, {}), conflicts
    )

    assert wrote is True and conflicts == []
    assert _card_heading(target) == "# Curated agent shell"
    assert frontmatter.load(target)["record"]["title"] == "Agent can run shell commands"


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


def test_change_card_paths_disambiguates_same_date_and_slug(tmp_path: Path):
    first = change_card()
    second = {**change_card(), "card_id": "cursor-2025-02-01-bbbbbb"}

    paths, duplicates = change_card_paths(tmp_path, [first, second])

    assert duplicates == []
    assert paths[first["card_id"]].name == "2025-02-01-agent-shell.md"
    assert paths[second["card_id"]].name == "2025-02-01-agent-shell-bbbbbb.md"
    assert len(set(paths.values())) == 2


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


@pytest.mark.parametrize("source_title, visible_title", [
    ("Added `$.prompt.media` for managed mods", "Added $.prompt.media for managed mods"),
    ("Added `$.ui.view({ agentId })`", "Added $.ui.view({ agentId })"),
    ("Read `$SHELL`, `$1`, and `$(pwd)`", "Read $SHELL, $1, and $(pwd)"),
    ("Pricing: $0.10/$0.50 per Mtok", "Pricing: $0.10/$0.50 per Mtok"),
    ("Keep $$ and a trailing $", "Keep $$ and a trailing $"),
])
def test_dollar_symbols_survive_card_titles_and_navigation(source_title, visible_title):
    from _scripts.writer import card_link
    card = {**change_card(), "title": source_title}
    target = "Changes/Cursor/2025-02-01-agent-shell"
    targets = {card["card_id"]: target}
    post = frontmatter.loads(render_change_markdown(card, {}, {}, targets))
    assert post["title"] == visible_title
    assert post["record"]["title"] == source_title
    expected_link = f"[[{target}|{visible_title}]]"
    assert card_link(card, targets) == expected_link
    assert expected_link in render_theme_markdown("agent-mode", [card], card_targets=targets)
    release = {"release_id": "r", "product": "cursor", "product_name": "Cursor",
               "title": source_title, "date": card["date"],
               "source_url": "https://cursor.com/changelog/test", "cards": [card]}
    rendered_release = render_release_markdown(release, targets)
    assert frontmatter.loads(rendered_release)["title"] == "Cursor — " + visible_title
    assert expected_link in rendered_release
