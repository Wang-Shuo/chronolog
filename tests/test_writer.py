from pathlib import Path

from _scripts.writer import (
    ensure_vault_dirs,
    render_change_markdown,
    render_theme_markdown,
    replace_machine_region,
    write_markdown_file,
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


def test_ensure_vault_dirs_creates_empty_alerts_directory(tmp_path: Path):
    ensure_vault_dirs(tmp_path)

    assert (tmp_path / "Products").is_dir()
    assert (tmp_path / "Changes").is_dir()
    assert (tmp_path / "Releases").is_dir()
    assert (tmp_path / "Themes").is_dir()
    assert (tmp_path / "Alerts").is_dir()
