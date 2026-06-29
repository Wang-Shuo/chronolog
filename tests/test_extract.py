import shutil
import subprocess
import sys
from pathlib import Path
from uuid import uuid4

from _scripts.common import PipelinePaths, read_json, write_json
from _scripts.extract import extract_cards_from_release, extract_run, load_theme_vocabulary


def release_with_body(body: str) -> dict[str, str]:
    return {
        "product": "cursor",
        "product_name": "Cursor",
        "date": "2026-05-01",
        "version": "v1.2",
        "title": "Extractor fixture",
        "body": body,
        "source_url": "https://example.com",
    }


def test_extractor_normalizes_theme_alias_and_stable_card_id():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    release = {
        "product": "cursor",
        "product_name": "Cursor",
        "date": "2026-03-15",
        "version": "v1.0",
        "title": "Agent and context update",
        "body": "- Agent can run shell commands\n- Context window expanded to 200K tokens",
        "source_url": "https://example.com",
    }

    cards = extract_cards_from_release(release, themes)

    assert {card["theme"] for card in cards} >= {"agent-mode", "context-window"}
    assert cards[0]["card_id"] == extract_cards_from_release(release, themes)[0]["card_id"]
    assert cards[0]["evidence"][0]["quote"]


def test_extractor_marks_candidate_theme_when_no_alias_matches():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    release = {
        "product": "cursor",
        "product_name": "Cursor",
        "date": "2026-04-01",
        "version": "v1.1",
        "title": "Mobile companion",
        "body": "- New mobile companion app for reviewing conversations",
        "source_url": "https://example.com",
    }

    cards = extract_cards_from_release(release, themes)

    assert cards[0]["theme"] == "__candidate__"
    assert cards[0]["theme_suggestion"] == "mobile-companion"


def test_extractor_does_not_match_theme_or_impact_inside_words():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    release = release_with_body("- Stable planning remodel renewed workflow cleanup")

    cards = extract_cards_from_release(release, themes)

    assert cards[0]["theme"] == "__candidate__"
    assert cards[0]["theme_suggestion"] == "stable-planning-remodel"
    assert cards[0]["impact"] == "incremental"
    assert "ai_generated" not in cards[0]
    assert "confidence" not in cards[0]


def test_extractor_matches_hyphenated_alias_written_with_space():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    release = release_with_body("- Usage based metering controls are available")

    cards = extract_cards_from_release(release, themes)

    assert cards[0]["theme"] == "pricing-model"


def test_extractor_skips_markdown_headings_and_strips_numbered_bullets():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    release = release_with_body(
        "# Release Notes\n"
        "## Breaking Changes\n"
        "1. Added model support for Claude\n"
    )

    cards = extract_cards_from_release(release, themes)

    assert [card["title"] for card in cards] == ["Added model support for Claude"]
    assert cards[0]["theme"] == "model-support"


def test_extractor_dedupes_before_five_card_limit():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    release = release_with_body(
        "\n".join(
            [
                "- Agent can run task one",
                "- Agent can run task two",
                "- Agent can run task three",
                "- Agent can run task four",
                "- Agent can run task five",
                "- Context window expanded to 200K tokens",
            ]
        )
    )

    cards = extract_cards_from_release(release, themes)

    assert [card["theme"] for card in cards] == ["agent-mode", "context-window"]


def test_extractor_adds_ai_fields_only_for_high_impact_cards():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    release = release_with_body(
        "- Stable workflow polishing for command history\n"
        "- Added new model support for Claude"
    )

    cards = extract_cards_from_release(release, themes)

    incremental_card = cards[0]
    significant_card = cards[1]
    assert incremental_card["impact"] == "incremental"
    assert "ai_generated" not in incremental_card
    assert "confidence" not in incremental_card
    assert significant_card["impact"] == "significant"
    assert significant_card["ai_generated"] is True
    assert significant_card["confidence"] == "low"


def test_extract_run_writes_extracted_change_cards():
    run_id = f"pytest-extract-{uuid4().hex}"
    paths = PipelinePaths(run_id)
    shutil.rmtree(paths.run_dir, ignore_errors=True)

    try:
        write_json(
            paths.collected,
            {"releases": [release_with_body("- Agent can run shell commands")]},
        )

        cards = extract_run(run_id)

        output = read_json(paths.extracted)
        assert paths.extracted.exists()
        assert output == {"run_id": run_id, "change_cards": cards}
        assert output["change_cards"][0]["theme"] == "agent-mode"
    finally:
        shutil.rmtree(paths.run_dir, ignore_errors=True)


def test_direct_cli_invocation_writes_extracted_change_cards():
    run_id = f"pytest-direct-extract-{uuid4().hex}"
    paths = PipelinePaths(run_id)
    shutil.rmtree(paths.run_dir, ignore_errors=True)

    try:
        write_json(
            paths.collected,
            {"releases": [release_with_body("- Context window expanded to 200K tokens")]},
        )

        result = subprocess.run(
            [sys.executable, "_scripts/extract.py", "--run-id", run_id],
            cwd=Path.cwd(),
            capture_output=True,
            text=True,
            check=False,
        )

        assert result.returncode == 0, result.stderr
        output = read_json(paths.extracted)
        assert output["change_cards"][0]["theme"] == "context-window"
    finally:
        shutil.rmtree(paths.run_dir, ignore_errors=True)
