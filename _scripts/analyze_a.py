from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from collections.abc import Collection
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _scripts.common import PipelinePaths, read_json, write_json
from _scripts.extract import HOLDING_THEMES


def analyze_products(
    cards: list[dict[str, Any]],
    holding: Collection[str] = HOLDING_THEMES,
) -> dict[str, Any]:
    """Per-product summary. Cards of a holding theme count toward the verbosity baseline
    (they are published cards) but never rank among the product's themes."""
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for card in cards:
        grouped[card["product"]].append(card)

    products = {}
    evolves_from = {}
    for product, product_cards in grouped.items():
        ordered = sorted(product_cards, key=lambda card: (card["date"], card["card_id"]))
        releases = {card["source_release"] for card in ordered}
        theme_counts = Counter(card["theme"] for card in ordered if card["theme"] not in holding)
        baseline = round(len(ordered) / max(len(releases), 1), 2)

        # Chronology alone is not evidence of capability evolution. Product
        # narratives are curated separately with cited turning points.
        eras = []

        products[product] = {
            "product_name": ordered[0]["product_name"],
            "verbosity_baseline": baseline,
            "top_themes": [theme for theme, _ in theme_counts.most_common()],
            "eras": eras,
        }

    return {"products": products, "evolves_from": evolves_from}


def analyze_run(run_id: str) -> dict[str, Any]:
    paths = PipelinePaths(run_id)
    cards = read_json(paths.valid_cards)["change_cards"]
    result = analyze_products(cards)
    write_json(paths.analyze_a, result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    args = parser.parse_args()
    analyze_run(args.run_id)


if __name__ == "__main__":
    main()
