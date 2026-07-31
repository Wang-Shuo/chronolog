from datetime import date
from pathlib import Path

from _scripts.common import (
    PipelinePaths,
    card_id_for,
    machine_hash,
    parse_date,
    read_json,
    slugify,
    write_json,
)


def test_slugify_normalizes_text_for_paths():
    assert slugify("Cursor Agent Mode!") == "cursor-agent-mode"
    assert slugify("  GPT-4.1 / Claude  ") == "gpt-4-1-claude"


def test_card_id_is_stable_from_quote():
    first = card_id_for("Cursor", "2026-03-15", "Context window expanded to 200K tokens.")
    second = card_id_for("cursor", "2026-03-15", " context window expanded to 200k tokens ")
    assert first == second
    assert first.startswith("cursor-2026-03-15-")
    assert len(first.rsplit("-", 1)[-1]) == 6


def test_write_json_creates_parent_directories(tmp_path: Path):
    target = tmp_path / "nested" / "file.json"
    write_json(target, {"run_id": "demo", "day": date(2026, 6, 26).isoformat()})
    assert read_json(target)["run_id"] == "demo"


def test_machine_hash_excludes_machine_hash_field():
    fields = {"title": "Cursor", "machine_hash": "old"}
    regions = {"summary": "Hello"}
    assert machine_hash(fields, regions) == machine_hash({"title": "Cursor"}, regions)


def test_parse_date_accepts_iso_date():
    assert parse_date("2026-06-26") == date(2026, 6, 26)


def test_parse_date_accepts_iso_datetime():
    assert parse_date("2026-06-26T12:34:56Z") == date(2026, 6, 26)


def test_parse_date_accepts_rss_datetime():
    assert parse_date("Fri, 26 Jun 2026 12:34:56 GMT") == date(2026, 6, 26)


def test_pipeline_paths_collected_points_to_run_output():
    assert PipelinePaths("demo").collected.as_posix().endswith(
        "_pipeline/demo/01-collected/releases.json"
    )
    assert PipelinePaths("demo").theme_candidates.as_posix().endswith(
        "_pipeline/demo/02-extracted/theme_candidates.json"
    )
    assert PipelinePaths("demo").validation_round2.as_posix().endswith(
        "_pipeline/demo/04-validated/report.json"
    )
