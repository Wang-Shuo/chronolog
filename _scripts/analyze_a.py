from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _scripts.common import PipelinePaths, read_json, write_json


def analyze_products(cards: list[dict[str, Any]]) -> dict[str, Any]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for card in cards:
        grouped[card["product"]].append(card)

    products = {}
    evolves_from = {}
    for product, product_cards in grouped.items():
        ordered = sorted(product_cards, key=lambda card: (card["date"], card["card_id"]))
        releases = {card["source_release"] for card in ordered}
        theme_counts = Counter(card["theme"] for card in ordered)
        baseline = round(len(ordered) / max(len(releases), 1), 2)

        cards_by_release: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for card in ordered:
            cards_by_release[card["source_release"]].append(card)
        release_groups = sorted(
            cards_by_release.values(),
            key=lambda group: (group[0]["date"], group[0]["source_release"]),
        )
        midpoint = max(len(release_groups) // 2, 1)
        era_groups = (
            [
                [card for release in release_groups[:midpoint] for card in release],
                [card for release in release_groups[midpoint:] for card in release],
            ]
            if len(release_groups) >= 2
            else [ordered]
        )
        eras = []
        for index, era_cards in enumerate(era_groups, start=1):
            dominant = Counter(card["theme"] for card in era_cards).most_common(1)[0][0]
            eras.append(
                {
                    "name": f"{dominant.replace('-', ' ').title()} Era",
                    "from": era_cards[0]["date"],
                    "to": era_cards[-1]["date"] if index < len(era_groups) else None,
                    "summary": (
                        f"{product} focused on {dominant} across "
                        f"{len(era_cards)} tracked changes."
                    ),
                    "dominant_theme": dominant,
                    "data_sparse": len(release_groups) < 3,
                }
            )

        previous_by_theme: dict[str, str] = {}
        for card in ordered:
            previous = previous_by_theme.get(card["theme"])
            if previous:
                evolves_from[card["card_id"]] = [previous]
            previous_by_theme[card["theme"]] = card["card_id"]

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
