from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _scripts.common import PipelinePaths, read_json, read_yaml, write_json


REQUIRED_FIELDS = {
    "type",
    "card_id",
    "product",
    "product_name",
    "source_release",
    "date",
    "title",
    "slug",
    "theme",
    "impact",
    "description",
    "evidence",
    "extractor_version",
}
IMPACTS = {"incremental", "significant", "paradigm-shift"}
CARD_ID_RE = re.compile(r"^[a-z0-9-]+-\d{4}-\d{2}-\d{2}-[a-f0-9]{6}$")


def official_themes(themes_path: str | Path) -> set[str]:
    data = read_yaml(Path(themes_path))
    return {theme["slug"] for theme in data["themes"] if theme.get("status") == "official"}


def validate_card(card: dict[str, Any], themes: set[str]) -> list[str]:
    errors = []
    missing = sorted(REQUIRED_FIELDS - set(card))
    if missing:
        errors.append(f"missing fields: {', '.join(missing)}")
    if card.get("type") != "change":
        errors.append("type must be change")
    if not CARD_ID_RE.match(str(card.get("card_id", ""))):
        errors.append("card_id is not deterministic format")
    if card.get("theme") not in themes:
        if card.get("theme") != "__candidate__" or not card.get("theme_suggestion"):
            errors.append("theme must be official or candidate with suggestion")
    if card.get("impact") not in IMPACTS:
        errors.append("impact is invalid")
    evidence = card.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        errors.append("evidence is required")
    elif not evidence[0].get("source_release") or not evidence[0].get("quote"):
        errors.append("evidence requires source_release and quote")
    if not str(card.get("description", "")).strip():
        errors.append("description is required")
    if card.get("impact") in {"significant", "paradigm-shift"}:
        if card.get("ai_generated") is not True or card.get("confidence") not in {
            "low",
            "medium",
            "high",
        }:
            errors.append("high impact cards require ai_generated and confidence")
    return errors


def validate_cards_file(
    source: Path,
    valid_output: Path,
    dlq_output: Path,
    themes_path: str | Path,
) -> dict[str, int]:
    payload = read_json(source)
    themes = official_themes(themes_path)
    valid = []
    failed = []
    for card in payload.get("change_cards", []):
        errors = validate_card(card, themes)
        if errors:
            failed.append({"record": card, "errors": errors})
        else:
            valid.append(card)
    write_json(valid_output, {"change_cards": valid})
    if failed:
        write_json(dlq_output, {"failed": failed})
    return {"passed": len(valid), "failed": len(failed)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    parser.add_argument("--round", default="1")
    args = parser.parse_args()
    if args.round != "1":
        return
    paths = PipelinePaths(args.run_id)
    validate_cards_file(paths.extracted, paths.valid_cards, paths.dlq, ROOT / "_scripts/themes.yaml")


if __name__ == "__main__":
    main()
