import shutil
import subprocess
import sys
from pathlib import Path
from uuid import uuid4

from _scripts.common import PipelinePaths, card_id_for, read_json, write_json
from _scripts.validate import validate_card, validate_cards_file, validate_vault_links


def valid_card(**overrides):
    card = {
        "type": "change",
        "card_id": "cursor-2026-03-15-a1b2c3",
        "product": "cursor",
        "product_name": "Cursor",
        "source_release": "cursor-2026-03-15-v1",
        "date": "2026-03-15",
        "title": "Agent mode",
        "slug": "agent-mode",
        "theme": "agent-mode",
        "impact": "significant",
        "description": "Agent mode can run commands.",
        "comparison": "",
        "evidence": [
            {"source_release": "https://example.com", "quote": "Agent mode can run commands."}
        ],
        "extractor_version": "fallback-v1",
        "ai_generated": True,
        "confidence": "low",
    }
    card.update(overrides)
    if "card_id" not in overrides and isinstance(card.get("evidence"), list) and card["evidence"]:
        first_evidence = card["evidence"][0]
        if isinstance(first_evidence, dict) and first_evidence.get("quote"):
            card["card_id"] = card_id_for(
                card["product"],
                card["date"],
                first_evidence["quote"],
            )
    return card


def test_validate_cards_file_splits_valid_and_invalid_records(tmp_path: Path):
    source = tmp_path / "cards.json"
    valid_output = tmp_path / "valid.json"
    dlq_output = tmp_path / "dlq.json"
    write_json(
        source,
        {
            "change_cards": [
                valid_card(),
                {"type": "change", "theme": "made-up", "impact": "huge"},
            ]
        },
    )

    result = validate_cards_file(source, valid_output, dlq_output, "_scripts/themes.yaml")

    assert result["passed"] == 1
    assert result["pending_theme_review"] == 0
    assert result["failed"] == 1
    assert valid_output.exists()
    assert dlq_output.exists()


def test_validate_card_accepts_candidate_theme_with_suggestion():
    card = valid_card(
        theme="__candidate__",
        theme_suggestion="mobile-companion",
        impact="incremental",
    )
    card.pop("ai_generated")
    card.pop("confidence")

    assert validate_card(card, {"agent-mode"}) == []


def test_validate_card_rejects_high_impact_without_ai_metadata():
    card = valid_card(ai_generated=False, confidence="unknown")

    assert "high impact cards require ai_generated and confidence" in validate_card(
        card,
        {"agent-mode"},
    )


def test_validate_card_rejects_malformed_evidence_item_without_crashing():
    card = valid_card(impact="incremental", evidence=["not-a-dict"])
    card.pop("ai_generated")
    card.pop("confidence")

    errors = validate_card(card, {"agent-mode"})

    assert "evidence requires source_release and quote" in errors


def test_validate_card_rejects_card_id_that_does_not_match_primary_evidence():
    card = valid_card(card_id="cursor-2026-03-15-a1b2c3")

    assert "card_id does not match primary evidence" in validate_card(
        card,
        {"agent-mode"},
    )


def test_validate_cards_file_writes_dlq_with_record_and_errors(tmp_path: Path):
    source = tmp_path / "cards.json"
    valid_output = tmp_path / "valid.json"
    dlq_output = tmp_path / "dlq.json"
    invalid = valid_card(theme="made-up", evidence=[])
    write_json(source, {"change_cards": [invalid]})

    result = validate_cards_file(source, valid_output, dlq_output, "_scripts/themes.yaml")

    dlq = read_json(dlq_output)
    assert result == {"passed": 0, "pending_theme_review": 0, "failed": 1}
    assert read_json(valid_output) == {"change_cards": [], "pending_theme_review": []}
    assert dlq["failed"][0]["record"] == invalid
    assert "theme must be official or candidate with suggestion" in dlq["failed"][0]["errors"]
    assert "evidence is required" in dlq["failed"][0]["errors"]


def test_validate_cards_file_removes_stale_dlq_when_current_run_has_no_failures(tmp_path: Path):
    source = tmp_path / "cards.json"
    valid_output = tmp_path / "valid.json"
    dlq_output = tmp_path / "dlq.json"
    write_json(source, {"change_cards": [valid_card()]})
    write_json(dlq_output, {"failed": [{"record": {"old": True}, "errors": ["old failure"]}]})

    result = validate_cards_file(source, valid_output, dlq_output, "_scripts/themes.yaml")

    assert result == {"passed": 1, "pending_theme_review": 0, "failed": 0}
    assert not dlq_output.exists()


def test_validate_cards_file_quarantines_candidate_theme_from_publishable_cards(tmp_path: Path):
    source = tmp_path / "cards.json"
    valid_output = tmp_path / "valid.json"
    dlq_output = tmp_path / "dlq.json"
    candidate = valid_card(
        theme="__candidate__",
        theme_suggestion="mobile-companion",
        impact="incremental",
        title="Mobile companion",
        description="Mobile companion is available for conversation review.",
        evidence=[
            {
                "source_release": "https://example.com/mobile",
                "quote": "Mobile companion is available for conversation review.",
            }
        ],
    )
    candidate.pop("ai_generated")
    candidate.pop("confidence")
    write_json(source, {"change_cards": [valid_card(), candidate]})

    result = validate_cards_file(source, valid_output, dlq_output, "_scripts/themes.yaml")

    assert result == {"passed": 1, "pending_theme_review": 1, "failed": 0}
    assert read_json(valid_output) == {
        "change_cards": [valid_card()],
        "pending_theme_review": [candidate],
    }


def test_validate_cards_file_rejects_duplicate_card_ids(tmp_path: Path):
    source = tmp_path / "cards.json"
    valid_output = tmp_path / "valid.json"
    dlq_output = tmp_path / "dlq.json"
    duplicate = valid_card()
    write_json(source, {"change_cards": [duplicate, duplicate]})

    result = validate_cards_file(source, valid_output, dlq_output, "_scripts/themes.yaml")

    assert result == {"passed": 1, "pending_theme_review": 0, "failed": 1}
    assert "duplicate card_id in extraction batch" in read_json(dlq_output)["failed"][0]["errors"]


def test_validate_vault_links_reports_missing_and_superseded_relation_targets(tmp_path: Path):
    changes = tmp_path / "Changes" / "Cursor"
    changes.mkdir(parents=True)
    (changes / "old.md").write_text(
        "---\ncard_id: cursor-2025-01-01-aaaaaa\ntype: change\nsuperseded: true\n---\n# Old\n",
        encoding="utf-8",
    )
    (changes / "current.md").write_text(
        "---\n"
        "card_id: cursor-2026-01-01-bbbbbb\n"
        "type: change\n"
        "evolves_from:\n"
        "  - '[[Changes/Cursor/old|cursor-2025-01-01-aaaaaa]]'\n"
        "---\n"
        "# Current\n"
        "See [[Themes/missing|missing theme]].\n",
        encoding="utf-8",
    )

    report = validate_vault_links(tmp_path)

    assert report["files_checked"] == 2
    assert {error["error"] for error in report["errors"]} == {
        "unresolved wikilink",
        "evolves_from points to superseded card",
    }


def test_validate_vault_links_requires_rendered_relation_wikilinks(tmp_path: Path):
    changes = tmp_path / "Changes" / "Cursor"
    changes.mkdir(parents=True)
    (changes / "current.md").write_text(
        "---\n"
        "card_id: cursor-2026-01-01-bbbbbb\n"
        "type: change\n"
        "source_release: cursor-2026-01-01-v1\n"
        "related_changes:\n"
        "  - cursor-2025-01-01-aaaaaa\n"
        "diffusion:\n"
        "  first_in_tracked: cursor-2025-01-01-aaaaaa\n"
        "---\n"
        "# Current\n",
        encoding="utf-8",
    )

    report = validate_vault_links(tmp_path)

    assert {error["error"] for error in report["errors"]} == {
        "source_release must be a wikilink",
        "related_changes must be a wikilink",
        "diffusion.first_in_tracked must be a wikilink",
    }


def test_direct_cli_invocation_writes_valid_cards_and_dlq_for_round_one():
    run_id = f"pytest-validate-{uuid4().hex}"
    paths = PipelinePaths(run_id)
    shutil.rmtree(paths.run_dir, ignore_errors=True)
    paths.dlq.unlink(missing_ok=True)

    try:
        write_json(
            paths.extracted,
            {"change_cards": [valid_card(), valid_card(theme="made-up")]},
        )

        result = subprocess.run(
            [sys.executable, "_scripts/validate.py", "--run-id", run_id, "--round", "1"],
            cwd=Path.cwd(),
            capture_output=True,
            text=True,
            check=False,
        )

        assert result.returncode == 0, result.stderr
        assert read_json(paths.valid_cards)["change_cards"] == [valid_card()]
        assert read_json(paths.dlq)["failed"][0]["record"]["theme"] == "made-up"
    finally:
        shutil.rmtree(paths.run_dir, ignore_errors=True)
        paths.dlq.unlink(missing_ok=True)
