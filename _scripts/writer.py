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

from _scripts.common import PipelinePaths, machine_hash, read_json, slugify, write_json, write_text


REGION_RE = re.compile(
    r"<!-- chronolog:begin region=\"(?P<name>[^\"]+)\" -->\n"
    r"(?P<content>.*?)\n"
    r"<!-- chronolog:end -->",
    re.S,
)


def machine_region(region: str, content: str) -> str:
    return f"<!-- chronolog:begin region=\"{region}\" -->\n{content.rstrip()}\n<!-- chronolog:end -->"


def replace_machine_region(existing: str, region: str, content: str) -> str:
    rendered = machine_region(region, content)
    pattern = re.compile(
        rf"<!-- chronolog:begin region=\"{re.escape(region)}\" -->.*?<!-- chronolog:end -->",
        re.S,
    )
    if pattern.search(existing):
        return pattern.sub(rendered, existing)
    return existing.rstrip() + "\n\n" + rendered + "\n"


def extract_machine_regions(markdown_body: str) -> dict[str, str]:
    return {match.group("name"): match.group("content").rstrip() for match in REGION_RE.finditer(markdown_body)}


def machine_fields(metadata: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in metadata.items()
        if key not in {"machine_hash", "human_overrides"}
    }


def render_frontmatter(metadata: dict[str, Any], body: str) -> str:
    post = frontmatter.Post(body, **metadata)
    return frontmatter.dumps(post)


def content_machine_hash(markdown: str) -> str:
    post = frontmatter.loads(markdown)
    return machine_hash(machine_fields(dict(post.metadata)), extract_machine_regions(post.content))


def ensure_vault_dirs(root: Path) -> None:
    for name in ["Products", "Changes", "Releases", "Themes", "Alerts"]:
        (root / name).mkdir(parents=True, exist_ok=True)


def write_markdown_file(
    target: Path,
    rendered: str,
    conflicts: list[dict[str, str]] | None = None,
) -> bool:
    if not target.exists():
        write_text(target, rendered)
        return True

    existing = target.read_text(encoding="utf-8")
    existing_post = frontmatter.loads(existing)
    stored_hash = existing_post.metadata.get("machine_hash")
    if stored_hash and content_machine_hash(existing) != stored_hash:
        if conflicts is not None:
            conflicts.append(
                {
                    "file": str(target),
                    "error": "machine_hash mismatch",
                }
            )
        return False

    rendered_post = frontmatter.loads(rendered)
    rendered_regions = extract_machine_regions(rendered_post.content)
    merged_body = existing_post.content
    for region, content in rendered_regions.items():
        merged_body = replace_machine_region(merged_body, region, content)

    merged_metadata = dict(rendered_post.metadata)
    if "human_overrides" in existing_post.metadata:
        merged_metadata["human_overrides"] = existing_post.metadata["human_overrides"]
    merged_metadata["machine_hash"] = machine_hash(machine_fields(merged_metadata), rendered_regions)
    write_text(target, render_frontmatter(merged_metadata, merged_body))
    return True


def card_link(card: dict[str, Any]) -> str:
    return f"[[{card['date']}-{card['slug']}|{card['title']}]]"


def render_theme_markdown(theme: str, cards: list[dict[str, Any]]) -> str:
    ordered = sorted(cards, key=lambda card: (card["date"], card["product_name"], card["card_id"]))
    timeline = ["```mermaid", "timeline", f"    title {theme}"]
    for card in ordered:
        timeline.append(f"    {card['date']} : {card['product_name']} : {card['title']}")
    timeline.append("```")
    links = "\n".join(
        f"- {card['date']} {card['product_name']}: {card_link(card)}" for card in ordered
    )
    regions = {"timeline": "\n".join(timeline), "cards": links or "No changes yet."}
    fields = {
        "tags": ["theme", "moc"],
        "status": "official",
        "theme": theme,
        "products_involved": sorted({card["product_name"] for card in ordered}),
    }
    fields["machine_hash"] = machine_hash(fields, regions)
    body = (
        f"# Theme: {theme}\n\n"
        f"## Cross-Product Timeline\n{machine_region('timeline', regions['timeline'])}\n\n"
        f"## Change Cards\n{machine_region('cards', regions['cards'])}\n"
    )
    return render_frontmatter(fields, body)


def render_change_markdown(
    card: dict[str, Any],
    patch_a: dict[str, Any],
    patch_b: dict[str, Any],
) -> str:
    metadata = {
        key: card[key]
        for key in [
            "type",
            "card_id",
            "product",
            "product_name",
            "source_release",
            "date",
            "theme",
            "impact",
            "extractor_version",
        ]
        if key in card
    }
    metadata.update(patch_a)
    metadata.update(patch_b)
    evidence = "\n\n".join(
        f"> {item['quote']}\n>\n> Source: {item['source_release']}" for item in card["evidence"]
    )
    body_regions = {
        "description": card["description"],
        "evidence": evidence,
        "evolution": "\n".join(f"- {item}" for item in patch_a.get("evolves_from", []))
        or "No prior tracked change.",
        "diffusion": str(patch_b.get("diffusion", {"scope": "tracked-products-only"})),
    }
    metadata["machine_hash"] = machine_hash(metadata, body_regions)
    body = f"# {card['title']}\n\n" + "\n\n".join(
        machine_region(name, content) for name, content in body_regions.items()
    )
    body += "\n\n## Editor Notes\n"
    return render_frontmatter(metadata, body)


def render_product_markdown(
    product: str,
    product_info: dict[str, Any],
    cards: list[dict[str, Any]],
) -> str:
    ordered = sorted(cards, key=lambda item: (item["date"], item["card_id"]))
    era_lines = []
    for era in product_info.get("eras", []):
        date_range = f"{era['from']} to {era.get('to') or 'present'}"
        sparse = " data_sparse" if era.get("data_sparse") else ""
        era_lines.append(f"- **{era['name']}** ({date_range}){sparse}: {era['summary']}")
    change_lines = [
        f"- {card['date']} {card['theme']}: {card_link(card)}" for card in ordered
    ] or ["- No tracked changes yet."]
    regions = {
        "summary": (
            f"verbosity_baseline: {product_info['verbosity_baseline']}\n"
            f"top_themes: {', '.join(product_info.get('top_themes', []))}"
        ),
        "eras": "\n".join(era_lines) or "No eras yet.",
        "changes": "\n".join(change_lines),
    }
    fields = {
        "tags": ["product"],
        "product": product,
        "product_name": product_info["product_name"],
        "verbosity_baseline": product_info["verbosity_baseline"],
        "top_themes": product_info.get("top_themes", []),
    }
    fields["machine_hash"] = machine_hash(fields, regions)
    body = (
        f"# {product_info['product_name']}\n\n"
        f"## Summary\n{machine_region('summary', regions['summary'])}\n\n"
        f"## Eras\n{machine_region('eras', regions['eras'])}\n\n"
        f"## Change Timeline\n{machine_region('changes', regions['changes'])}\n\n"
        "## Editor Notes\n"
    )
    return render_frontmatter(fields, body)


def render_release_markdown(product_name: str, release: dict[str, Any]) -> str:
    cards = sorted(release["cards"], key=lambda card: (card["date"], card["card_id"]))
    card_lines = [f"- {card['theme']}: {card_link(card)}" for card in cards]
    regions = {
        "summary": f"Source release: {release['title']}\nTracked cards: {len(cards)}",
        "cards": "\n".join(card_lines) or "No change cards extracted.",
    }
    fields = {
        "tags": ["release"],
        "product_name": product_name,
        "source_release": release["title"],
        "date": release["date"],
    }
    fields["machine_hash"] = machine_hash(fields, regions)
    body = (
        f"# {product_name} {release['title']}\n\n"
        f"## Summary\n{machine_region('summary', regions['summary'])}\n\n"
        f"## Change Cards\n{machine_region('cards', regions['cards'])}\n"
    )
    return render_frontmatter(fields, body)


def render_alert_markdown(alert: dict[str, Any]) -> str:
    regions = {
        "details": (
            f"{alert['message']}\n\n"
            f"Baseline monthly releases: {alert['baseline_monthly_releases']}\n"
            f"Recent releases: {alert['recent_releases']}"
        )
    }
    fields = {
        "tags": ["alert", "silence"],
        "type": alert["type"],
        "product": alert["product"],
        "product_name": alert["product_name"],
        "date": alert["date"],
    }
    fields["machine_hash"] = machine_hash(fields, regions)
    body = f"# {alert['product_name']} Silence Alert\n\n{machine_region('details', regions['details'])}\n"
    return render_frontmatter(fields, body)


def render_index_markdown(
    cards: list[dict[str, Any]],
    analysis_a: dict[str, Any],
    analysis_b: dict[str, Any],
    silence: dict[str, Any],
) -> str:
    products = analysis_a.get("products", {})
    themes = analysis_b.get("themes", {})
    product_links = "\n".join(
        f"- [[Products/{info['product_name']}|{info['product_name']}]]"
        for _, info in sorted(products.items())
    )
    theme_links = "\n".join(f"- [[Themes/{theme}|{theme}]]" for theme in sorted(themes))
    regions = {
        "overview": (
            f"Product count: {len(products)}\n"
            f"Change count: {len(cards)}\n"
            f"Theme count: {len(themes)}\n"
            f"Alert count: {len(silence.get('alerts', []))}"
        ),
        "products": product_links or "No products yet.",
        "themes": theme_links or "No themes yet.",
    }
    fields = {"tags": ["index"], "title": "ChronoLog"}
    fields["machine_hash"] = machine_hash(fields, regions)
    body = (
        "# ChronoLog\n\n"
        f"## Overview\n{machine_region('overview', regions['overview'])}\n\n"
        f"## Products\n{machine_region('products', regions['products'])}\n\n"
        f"## Themes\n{machine_region('themes', regions['themes'])}\n"
    )
    return render_frontmatter(fields, body)


def write_run(run_id: str) -> list[dict[str, str]]:
    paths = PipelinePaths(run_id)
    ensure_vault_dirs(paths.root)
    cards = read_json(paths.valid_cards)["change_cards"]
    analysis_a = read_json(paths.analyze_a)
    analysis_b = read_json(paths.analyze_b)
    silence = read_json(paths.silence) if paths.silence.exists() else {"alerts": []}
    conflicts: list[dict[str, str]] = []

    cards_by_product: dict[str, list[dict[str, Any]]] = defaultdict(list)
    cards_by_theme: dict[str, list[dict[str, Any]]] = defaultdict(list)
    releases_by_product: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)

    for card in cards:
        patch_a = {"evolves_from": analysis_a.get("evolves_from", {}).get(card["card_id"], [])}
        patch_b = analysis_b.get("cards", {}).get(card["card_id"], {})
        cards_by_product[card["product"]].append(card)
        cards_by_theme[card["theme"]].append(card)
        target = paths.root / "Changes" / card["product_name"] / f"{card['date']}-{card['slug']}.md"
        write_markdown_file(target, render_change_markdown(card, patch_a, patch_b), conflicts)

        product_releases = releases_by_product[card["product_name"]]
        release = product_releases.setdefault(
            card["source_release"],
            {"date": card["date"], "title": card["source_release"], "cards": []},
        )
        release["cards"].append(card)
        release["date"] = min(release["date"], card["date"])

    for product, product_info in analysis_a["products"].items():
        target = paths.root / "Products" / f"{product_info['product_name']}.md"
        write_markdown_file(
            target,
            render_product_markdown(product, product_info, cards_by_product[product]),
            conflicts,
        )

    for product_name, releases in releases_by_product.items():
        for release in releases.values():
            target = paths.root / "Releases" / product_name / f"{release['date']}-{slugify(release['title'])}.md"
            write_markdown_file(target, render_release_markdown(product_name, release), conflicts)

    for theme, theme_cards in cards_by_theme.items():
        target = paths.root / "Themes" / f"{theme}.md"
        write_markdown_file(target, render_theme_markdown(theme, theme_cards), conflicts)

    for alert in silence.get("alerts", []):
        target = paths.root / "Alerts" / f"{alert['date']}-{alert['product']}-silence.md"
        write_markdown_file(target, render_alert_markdown(alert), conflicts)

    write_markdown_file(
        paths.root / "index.md",
        render_index_markdown(cards, analysis_a, analysis_b, silence),
        conflicts,
    )

    conflict_path = paths.root / "_pipeline" / "dlq" / f"{run_id}-writer-conflicts.json"
    if conflicts:
        write_json(conflict_path, {"failed": conflicts})
    else:
        conflict_path.unlink(missing_ok=True)
    return conflicts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    args = parser.parse_args()
    write_run(args.run_id)


if __name__ == "__main__":
    main()
