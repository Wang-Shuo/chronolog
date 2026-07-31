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
AMBIGUITY_MARGIN = 25


def normalize_match_text(value: str) -> str:
    text = re.sub(r"[^a-z0-9]+", " ", value.lower())
    return re.sub(r"\s+", " ", text).strip()


def contains_phrase(normalized_text: str, normalized_phrase: str) -> bool:
    if not normalized_phrase:
        return False
    return f" {normalized_phrase} " in f" {normalized_text} "


def load_theme_vocabulary(path: str | Path) -> dict[str, dict[str, Any]]:
    data = read_yaml(Path(path))
    vocab = {}
    for theme in data["themes"]:
        canonical_terms = {
            normalize_match_text(theme["slug"]),
            normalize_match_text(theme["display_name"]),
        }
        alias_terms = {
            normalize_match_text(term) for term in theme.get("aliases", [])
        } - canonical_terms
        vocab[theme["slug"]] = {
            **theme,
            "canonical_terms": canonical_terms,
            "alias_terms": alias_terms,
            "terms": canonical_terms | alias_terms,
        }
    return vocab


def split_release_lines(body: str) -> list[str]:
    lines = []
    for raw in body.splitlines():
        stripped = raw.strip()
        if re.match(r"^#{1,6}(\s+|$)", stripped):
            continue
        line = re.sub(r"^(?:[-*]\s+|\d+[.)]\s+)", "", stripped).strip()
        if len(line) >= 12:
            lines.append(line)
    return lines


def rank_theme_matches(
    text: str,
    themes: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    normalized = normalize_match_text(text)
    matches = []
    for slug, theme in themes.items():
        canonical = sorted(
            term
            for term in theme.get("canonical_terms", set())
            if contains_phrase(normalized, term)
        )
        aliases = sorted(
            term
            for term in theme.get("alias_terms", theme.get("terms", set()))
            if term not in canonical and contains_phrase(normalized, term)
        )
        matched_terms = canonical + aliases
        if not matched_terms:
            continue
        score = sum(100 + 10 * len(term.split()) for term in canonical)
        score += sum(40 + 10 * len(term.split()) for term in aliases)
        matches.append(
            {
                "theme": slug,
                "score": score,
                "matched_terms": matched_terms,
            }
        )
    return sorted(matches, key=lambda match: (-match["score"], match["theme"]))


def candidate_suggestion(text: str) -> str:
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9]+", text.lower())[:3]
    if words and words[0] in {"new"}:
        words = words[1:]
    return slugify(" ".join(words) or "unclassified")


def classify_theme(text: str, themes: dict[str, dict[str, Any]]) -> dict[str, Any]:
    matches = rank_theme_matches(text, themes)
    if not matches:
        return {
            "theme": "__candidate__",
            "theme_suggestion": candidate_suggestion(text),
            "theme_review_reason": "no_match",
            "theme_matches": [],
        }

    top = matches[0]
    if len(matches) > 1 and top["score"] - matches[1]["score"] < AMBIGUITY_MARGIN:
        return {
            "theme": "__candidate__",
            "theme_suggestion": f"{top['theme']}-or-{matches[1]['theme']}",
            "theme_review_reason": "ambiguous_match",
            "theme_matches": matches,
        }

    result = {"theme": top["theme"]}
    if len(matches) > 1:
        result["theme_matches"] = matches
    return result


def choose_theme(text: str, themes: dict[str, dict[str, Any]]) -> tuple[str, str | None]:
    classification = classify_theme(text, themes)
    return classification["theme"], classification.get("theme_suggestion")


def choose_impact(text: str) -> str:
    normalized = normalize_match_text(text)
    for impact, words in IMPACT_WORDS.items():
        if any(contains_phrase(normalized, normalize_match_text(word)) for word in words):
            return impact
    return "incremental"


def extract_cards_from_release(release: dict[str, Any], themes: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    lines = split_release_lines(release.get("body", "")) or [release["title"]]
    cards = []
    seen_card_ids: set[str] = set()
    for line in lines:
        classification = classify_theme(line, themes)
        card_id = card_id_for(release["product"], release["date"], line)
        if card_id in seen_card_ids:
            continue
        seen_card_ids.add(card_id)
        impact = choose_impact(line)
        card = {
            "type": "change",
            "card_id": card_id,
            "product": release["product"],
            "product_name": release["product_name"],
            "source_release": f"{release['product']}-{release['date']}-{slugify(release.get('version') or release['title'])}",
            "date": release["date"],
            "title": line[:80],
            "slug": slugify(line)[:80].strip("-"),
            "theme": classification["theme"],
            "impact": impact,
            "description": line,
            "comparison": "",
            "evidence": [{"source_release": release.get("source_url", ""), "quote": line}],
            "extractor_version": "fallback-v1",
        }
        card.update({key: value for key, value in classification.items() if key != "theme"})
        if impact in {"significant", "paradigm-shift"}:
            card["ai_generated"] = True
            card["confidence"] = "low"
        cards.append(card)
        if len(cards) >= 5:
            break
    return cards


def extract_run(run_id: str) -> list[dict[str, Any]]:
    paths = PipelinePaths(run_id)
    themes = load_theme_vocabulary(ROOT / "_scripts/themes.yaml")
    releases = read_json(paths.collected)["releases"]
    cards = [card for release in releases for card in extract_cards_from_release(release, themes)]
    write_json(paths.extracted, {"run_id": run_id, "change_cards": cards})
    candidates = [
        {
            key: card[key]
            for key in [
                "card_id",
                "product",
                "product_name",
                "date",
                "title",
                "theme_suggestion",
                "theme_review_reason",
                "theme_matches",
                "evidence",
            ]
            if key in card
        }
        for card in cards
        if card["theme"] == "__candidate__"
    ]
    write_json(paths.theme_candidates, {"run_id": run_id, "candidates": candidates})
    return cards


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    args = parser.parse_args()
    extract_run(args.run_id)


if __name__ == "__main__":
    main()
