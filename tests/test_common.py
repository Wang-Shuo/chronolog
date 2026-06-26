from datetime import date
from pathlib import Path

from _scripts.common import (
    card_id_for,
    machine_hash,
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
