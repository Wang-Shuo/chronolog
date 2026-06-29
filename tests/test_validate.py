import shutil
import subprocess
import sys
from pathlib import Path
from uuid import uuid4

from _scripts.common import PipelinePaths, read_json, write_json
from _scripts.validate import validate_card, validate_cards_file


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
    assert result["failed"] == 1
    assert valid_output.exists()
    assert dlq_output.exists()


def test_validate_card_accepts_candidate_theme_with_suggestion():
    card = valid_card(
        card_id="cursor-2026-03-15-d4e5f6",
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


def test_validate_cards_file_writes_dlq_with_record_and_errors(tmp_path: Path):
    source = tmp_path / "cards.json"
    valid_output = tmp_path / "valid.json"
    dlq_output = tmp_path / "dlq.json"
    invalid = valid_card(theme="made-up", evidence=[])
    write_json(source, {"change_cards": [invalid]})

    result = validate_cards_file(source, valid_output, dlq_output, "_scripts/themes.yaml")

    dlq = read_json(dlq_output)
    assert result == {"passed": 0, "failed": 1}
    assert read_json(valid_output) == {"change_cards": []}
    assert dlq["failed"][0]["record"] == invalid
    assert "theme must be official or candidate with suggestion" in dlq["failed"][0]["errors"]
    assert "evidence is required" in dlq["failed"][0]["errors"]


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
