from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from collections.abc import Collection
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _scripts.common import PipelinePaths, read_json, write_json
from _scripts.extract import HOLDING_THEMES


def date_value(value: str) -> date:
    return date.fromisoformat(value)


def analyze_themes(
    cards: list[dict[str, Any]],
    holding: Collection[str] = HOLDING_THEMES,
) -> dict[str, Any]:
    """Same-theme chronology. A holding theme ("Other changes") groups lines without a
    confident theme, so its cards get no diffusion, related changes or theme entry."""
    cards = [card for card in cards if card["theme"] not in holding]
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    tracked_products = {card["product"] for card in cards}
    for card in cards:
        grouped[card["theme"]].append(card)

    patches = {}
    themes = {}
    for theme, theme_cards in grouped.items():
        ordered = sorted(theme_cards, key=lambda card: (card["date"], card["card_id"]))
        first = ordered[0]
        first_date = date_value(first["date"])
        themes[theme] = {
            "cards": [card["card_id"] for card in ordered],
            "products": sorted({card["product"] for card in ordered}),
        }
        for index, card in enumerate(ordered):
            previous = [other["card_id"] for other in ordered[max(0, index - 3) : index]]
            role = "first-observed" if card["card_id"] == first["card_id"] else "later-observed"
            patches[card["card_id"]] = {
                "related_changes": previous,
                "diffusion": {
                    "theme": theme,
                    "relation": "same-theme-chronology",
                    "inference": "No adoption, equivalence, or causation claim.",
                    "scope": "tracked-products-only",
                    "role": role,
                    "first_in_tracked": first["card_id"],
                    "lag_days": (date_value(card["date"]) - first_date).days,
                    "tracked_products_count": len(tracked_products),
                },
            }
    return {"themes": themes, "cards": patches}


def analyze_run(run_id: str) -> dict[str, Any]:
    paths = PipelinePaths(run_id)
    cards = read_json(paths.valid_cards)["change_cards"]
    result = analyze_themes(cards)
    write_json(paths.analyze_b, result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    args = parser.parse_args()
    analyze_run(args.run_id)


if __name__ == "__main__":
    main()
