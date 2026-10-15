from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import frontmatter

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _scripts.common import (
    PipelinePaths,
    card_id_for,
    parse_date,
    read_json,
    read_yaml,
    write_json,
)


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
WIKILINK_RE = re.compile(r"!?\[\[([^\]]+)\]\]")
VAULT_DIRECTORIES = ("Products", "Changes", "Releases", "Themes", "Alerts")
# Machine-maintained pages at the Vault root, enumerated wherever VAULT_DIRECTORIES are.
ROOT_PAGES = ("index.md", "About.md")


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
    try:
        parse_date(str(card.get("date", "")))
    except (TypeError, ValueError):
        errors.append("date must be a valid ISO or feed date")
    if card.get("theme") not in themes:
        if card.get("theme") != "__candidate__" or not card.get("theme_suggestion"):
            errors.append("theme must be official or candidate with suggestion")
    if card.get("impact") not in IMPACTS:
        errors.append("impact is invalid")
    evidence = card.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        errors.append("evidence is required")
    elif any(
        not isinstance(item, dict)
        or not item.get("source_release")
        or not item.get("quote")
        for item in evidence
    ):
        errors.append("evidence requires source_release and quote")
    elif card.get("product") and card.get("date"):
        expected_card_id = card_id_for(
            str(card["product"]),
            str(card["date"]),
            str(evidence[0]["quote"]),
            source_release=(
                str(card.get("source_release", "")) or None
                if card.get("extractor_version") in {"fallback-v2", "fallback-v3", "fallback-v4"}
                else None
            ),
        )
        if card.get("card_id") != expected_card_id:
            errors.append("card_id does not match primary evidence")
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
    pending_theme_review = []
    failed = []
    seen_card_ids: set[str] = set()
    for card in payload.get("change_cards", []):
        errors = validate_card(card, themes)
        card_id = str(card.get("card_id", ""))
        if card_id and card_id in seen_card_ids:
            errors.append("duplicate card_id in extraction batch")
        seen_card_ids.add(card_id)
        if errors:
            failed.append({"record": card, "errors": errors})
        elif card.get("theme") == "__candidate__":
            pending_theme_review.append(card)
        else:
            valid.append(card)
    write_json(
        valid_output,
        {
            "change_cards": valid,
            "pending_theme_review": pending_theme_review,
        },
    )
    if failed:
        write_json(dlq_output, {"failed": failed})
    else:
        dlq_output.unlink(missing_ok=True)
    return {
        "passed": len(valid),
        "pending_theme_review": len(pending_theme_review),
        "failed": len(failed),
    }


def vault_markdown_files(root: Path) -> list[Path]:
    files = [root / name for name in ROOT_PAGES if (root / name).exists()]
    for directory in VAULT_DIRECTORIES:
        target = root / directory
        if target.exists():
            files.extend(target.rglob("*.md"))
    return sorted(set(files))


def normalize_wikilink_target(raw: str) -> str:
    target = raw.split("|", 1)[0].split("#", 1)[0].strip().lstrip("/")
    return target[:-3] if target.endswith(".md") else target


def validate_vault_links(
    root: Path,
    collected_releases: list[dict[str, Any]] | None = None,
    valid_cards: list[dict[str, Any]] | None = None,
    pending_cards: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    files = vault_markdown_files(root)
    relative_targets: dict[str, Path] = {}
    basename_targets: dict[str, list[Path]] = defaultdict(list)
    card_targets: dict[str, list[Path]] = defaultdict(list)
    release_targets: dict[str, list[Path]] = defaultdict(list)
    active_card_ids: set[str] = set()
    active_card_products: dict[Path, str] = {}
    active_release_ids: set[str] = set()
    active_release_products: dict[Path, str] = {}
    superseded_cards: set[str] = set()

    for path in files:
        relative = path.relative_to(root).with_suffix("").as_posix()
        relative_targets[relative] = path
        basename_targets[path.stem].append(path)
        post = frontmatter.load(path)
        card_id = post.metadata.get("card_id")
        if card_id:
            card_targets[str(card_id)].append(path)
            if post.metadata.get("superseded") is True:
                superseded_cards.add(str(card_id))
            else:
                active_card_ids.add(str(card_id))
                active_card_products[path] = str(post.metadata.get("product", ""))
        release_id = post.metadata.get("release_id")
        if release_id:
            release_targets[str(release_id)].append(path)
            if post.metadata.get("superseded") is not True:
                active_release_ids.add(str(release_id))
        if "release" in (post.metadata.get("tags") or []) and post.metadata.get("superseded") is not True:
            active_release_products[path] = str(post.metadata.get("product", ""))

    errors = [
        {
            "file": str(path.relative_to(root)),
            "link": card_id,
            "error": "duplicate card_id in Vault",
        }
        for card_id, paths in card_targets.items()
        if len(paths) > 1
        for path in paths
    ]
    errors.extend(
        {
            "file": str(path.relative_to(root)),
            "link": release_id,
            "error": "duplicate release_id in Vault",
        }
        for release_id, paths in release_targets.items()
        if len(paths) > 1
        for path in paths
    )
    if collected_releases is not None:
        expected_release_ids = {
            str(release["release_id"]) for release in collected_releases
        }
        expected_products = {
            str(release["product"]) for release in collected_releases
        }
        for release_id in sorted(expected_release_ids - active_release_ids):
            errors.append(
                {
                    "file": "Releases",
                    "link": release_id,
                    "error": "collected release has no active Release page",
                }
            )
        for path, product in active_release_products.items():
            if product not in expected_products:
                continue
            post = frontmatter.load(path)
            release_id = str(post.metadata.get("release_id", ""))
            if not release_id:
                errors.append(
                    {
                        "file": str(path.relative_to(root)),
                        "link": "",
                        "error": "active Release page is missing release_id",
                    }
                )
            elif release_id not in expected_release_ids:
                errors.append(
                    {
                        "file": str(path.relative_to(root)),
                        "link": release_id,
                        "error": "active Release page is absent from collected snapshot",
                    }
                )
    if valid_cards is not None:
        expected_card_ids = {str(card["card_id"]) for card in valid_cards}
        protected_card_ids = expected_card_ids | {
            str(card["card_id"]) for card in (pending_cards or [])
        }
        expected_products = {str(card["product"]) for card in valid_cards}
        expected_products.update(str(card["product"]) for card in (pending_cards or []))
        for card_id in sorted(expected_card_ids - active_card_ids):
            errors.append(
                {
                    "file": "Changes",
                    "link": card_id,
                    "error": "valid Change Card has no active Vault page",
                }
            )
        for path, product in active_card_products.items():
            if product not in expected_products:
                continue
            post = frontmatter.load(path)
            card_id = str(post.metadata.get("card_id", ""))
            if card_id not in protected_card_ids:
                errors.append(
                    {
                        "file": str(path.relative_to(root)),
                        "link": card_id,
                        "error": "active Change Card is absent from validated extraction",
                    }
                )
    links_checked = 0

    def resolve_target(target: str) -> Path | None:
        if target in relative_targets:
            return relative_targets[target]
        matches = basename_targets.get(Path(target).name, [])
        return matches[0] if len(matches) == 1 else None

    for path in files:
        markdown = path.read_text(encoding="utf-8")
        post = frontmatter.loads(markdown)
        for raw_link in WIKILINK_RE.findall(markdown):
            links_checked += 1
            target = normalize_wikilink_target(raw_link)
            if target and resolve_target(target) is None:
                errors.append(
                    {
                        "file": str(path.relative_to(root)),
                        "link": raw_link,
                        "error": "unresolved wikilink",
                    }
                )

        if post.metadata.get("superseded") is True:
            continue

        relation_values = {
            "evolves_from": post.metadata.get("evolves_from", []) or [],
            "related_changes": post.metadata.get("related_changes", []) or [],
        }
        diffusion = post.metadata.get("diffusion", {}) or {}
        if diffusion.get("first_in_tracked"):
            relation_values["diffusion.first_in_tracked"] = [
                diffusion["first_in_tracked"]
            ]
        if post.metadata.get("type") == "change" and post.metadata.get("source_release"):
            relation_values["source_release"] = [post.metadata["source_release"]]

        for field, values in relation_values.items():
            for relation in values:
                match = WIKILINK_RE.search(str(relation))
                if not match:
                    errors.append(
                        {
                            "file": str(path.relative_to(root)),
                            "link": str(relation),
                            "error": f"{field} must be a wikilink",
                        }
                    )
                    continue
                target_path = resolve_target(normalize_wikilink_target(match.group(1)))
                if target_path is None or field != "evolves_from":
                    continue
                target_card_id = frontmatter.load(target_path).metadata.get("card_id")
                if target_card_id in superseded_cards:
                    errors.append(
                        {
                            "file": str(path.relative_to(root)),
                            "link": str(relation),
                            "error": "evolves_from points to superseded card",
                        }
                    )

    expected_release_count = (
        len({str(release["release_id"]) for release in collected_releases})
        if collected_releases is not None
        else None
    )
    report = {
        "files_checked": len(files),
        "links_checked": links_checked,
        "errors": errors,
    }
    if expected_release_count is not None:
        report.update(
            {
                "expected_release_count": expected_release_count,
                "active_release_count": len(
                    active_release_ids
                    & {str(release["release_id"]) for release in collected_releases}
                ),
            }
        )
    if valid_cards is not None:
        expected_card_ids = {str(card["card_id"]) for card in valid_cards}
        report.update(
            {
                "expected_card_count": len(expected_card_ids),
                "active_card_count": len(active_card_ids & expected_card_ids),
            }
        )
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    parser.add_argument("--round", default="1")
    args = parser.parse_args()
    if args.round == "2":
        paths = PipelinePaths(args.run_id)
        collected = read_json(paths.collected)
        validated = read_json(paths.valid_cards)
        report = validate_vault_links(
            ROOT,
            collected.get("releases", []),
            validated.get("change_cards", []),
            validated.get("pending_theme_review", []),
        )
        write_json(paths.validation_round2, report)
        if report["errors"]:
            raise SystemExit(1)
        return
    if args.round != "1":
        raise SystemExit(f"unsupported validation round: {args.round}")
        return
    paths = PipelinePaths(args.run_id)
    validate_cards_file(paths.extracted, paths.valid_cards, paths.dlq, ROOT / "_scripts/themes.yaml")


if __name__ == "__main__":
    main()
