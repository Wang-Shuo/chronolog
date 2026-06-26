from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _scripts.common import PipelinePaths, card_id_for, read_json, read_yaml, slugify, write_json


IMPACT_WORDS = {
    "paradigm-shift": ["agent", "autonomous", "pricing", "200k", "major"],
    "significant": ["support", "new", "expanded", "integration", "model"],
}


def load_theme_vocabulary(path: str | Path) -> dict[str, dict[str, Any]]:
    data = read_yaml(Path(path))
    vocab = {}
    for theme in data["themes"]:
        terms = {theme["slug"], theme["display_name"].lower(), *theme.get("aliases", [])}
        vocab[theme["slug"]] = {**theme, "terms": {term.lower() for term in terms}}
    return vocab


def split_release_lines(body: str) -> list[str]:
    lines = []
    for raw in body.splitlines():
        line = re.sub(r"^[-*#\s]+", "", raw).strip()
        if len(line) >= 12:
            lines.append(line)
    return lines


def choose_theme(text: str, themes: dict[str, dict[str, Any]]) -> tuple[str, str | None]:
    lowered = text.lower()
    for slug, theme in themes.items():
        if any(term in lowered for term in theme["terms"]):
            return slug, None
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9]+", text.lower())[:3]
    if words and words[0] in {"new"}:
        words = words[1:]
    return "__candidate__", slugify(" ".join(words) or "unclassified")


def choose_impact(text: str) -> str:
    lowered = text.lower()
    for impact, words in IMPACT_WORDS.items():
        if any(word in lowered for word in words):
            return impact
    return "incremental"


def extract_cards_from_release(release: dict[str, Any], themes: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    lines = split_release_lines(release.get("body", "")) or [release["title"]]
    cards = []
    seen_themes: set[str] = set()
    for line in lines[:5]:
        theme, suggestion = choose_theme(line, themes)
        identity_theme = suggestion if theme == "__candidate__" else theme
        if identity_theme in seen_themes:
            continue
        seen_themes.add(identity_theme)
        impact = choose_impact(line)
        card = {
            "type": "change",
            "card_id": card_id_for(release["product"], release["date"], line),
            "product": release["product"],
            "product_name": release["product_name"],
            "source_release": f"{release['product']}-{release['date']}-{slugify(release.get('version') or release['title'])}",
            "date": release["date"],
            "title": line[:80],
            "slug": slugify(line)[:80].strip("-"),
            "theme": theme,
            "impact": impact,
            "description": line,
            "comparison": "",
            "evidence": [{"source_release": release.get("source_url", ""), "quote": line}],
            "extractor_version": "fallback-v1",
        }
        if suggestion:
            card["theme_suggestion"] = suggestion
        if impact in {"significant", "paradigm-shift"}:
            card["ai_generated"] = True
            card["confidence"] = "low"
        cards.append(card)
    return cards


def extract_run(run_id: str) -> list[dict[str, Any]]:
    paths = PipelinePaths(run_id)
    themes = load_theme_vocabulary(ROOT / "_scripts/themes.yaml")
    releases = read_json(paths.collected)["releases"]
    cards = [card for release in releases for card in extract_cards_from_release(release, themes)]
    write_json(paths.extracted, {"run_id": run_id, "change_cards": cards})
    return cards


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    args = parser.parse_args()
    extract_run(args.run_id)


if __name__ == "__main__":
    main()
