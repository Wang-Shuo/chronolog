from __future__ import annotations

import argparse
from html import escape as escape_html
import math
import re
import sys
from collections import Counter, defaultdict
from datetime import date, timedelta
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlencode

import frontmatter

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _scripts.editorial import render_coverage_summary, render_source_details
from _scripts.common import (
    PipelinePaths,
    load_site,
    machine_hash,
    read_json,
    slugify,
    write_json,
    write_text,
)
from _scripts.extract import (
    GENERIC_HEADING_RE,
    HOLDING_THEMES,
    KIND_LABELS,
    UNCATEGORIZED_THEME,
    is_high_signal,
    load_theme_vocabulary,
    split_release_lines,
)


REGION_RE = re.compile(
    r"<!-- chronolog:begin region=\"(?P<name>[^\"]+)\" -->\n"
    r"(?P<content>.*?)\n"
    r"<!-- chronolog:end -->",
    re.S,
)
REGION_BLOCK_RE = re.compile(
    r"<!-- chronolog:begin region=\"[^\"]+\" -->.*?<!-- chronolog:end -->",
    re.S,
)
REGION_BEGIN = "<!-- chronolog:begin region="
MACHINE_FIELD_NAMES = {
    "tags",
    "type",
    "card_id",
    "release_id",
    "product",
    "product_name",
    "source_release",
    "source_url",
    "source_type",
    "version",
    "changes_count",
    "date",
    "created",
    "modified",
    "theme",
    "kind",
    "scope",
    "impact",
    "extractor_version",
    "related_changes",
    "diffusion",
    "evolves_from",
    "superseded",
    "status",
    "products_involved",
    "verbosity_baseline",
    "top_themes",
    "eras",
    "title",
    "record",
    "coverage",
    "publication",
    "description",
}
DESCRIPTION_MAX_CHARS = 160
# Static headings of the pre-W1 skeletons. A body holding only these, the generated H1
# and machine regions carries no human text and can be replaced by the new template.
SKELETON_HEADINGS = {
    "change": frozenset({"## Editor Notes"}),
    "release": frozenset({"## Summary", "## Change Cards"}),
    # Pre-W2 headings plus the current ones (Key moments, Timeline), so an untouched
    # legacy theme page is replaced and later renders stay idempotent.
    "theme": frozenset({
        "## Research summary", "## Cross-Product Timeline", "## Change Cards",
        "## Key moments", "## Timeline",
    }),
    # Archive pages (W2): every line is inside a machine region.
    "archive": frozenset(),
    # Product pages: the pre-W2 headings (including the inserted Research summary,
    # Source coverage and Release cadence sections) plus the current ones, so an
    # untouched legacy product page is replaced and later renders stay idempotent.
    "product": frozenset({
        "## Summary", "## Coverage", "## Source coverage", "## Capability turning points",
        "## Research summary", "## Eras", "## Release Archive", "## Change Timeline",
        "## Release cadence", "## Editor Notes", "## Themes", "## Recent releases",
    }),
    # Home page: the pre-W1 headings and lead paragraph, plus the current headings, so
    # an untouched legacy index is replaced and later renders stay idempotent.
    "index": frozenset({
        "## Source coverage", "## Start exploring", "## Overview", "## Products", "## Themes",
        "Research changes in ChatGPT, Claude Code, and Cursor through official release evidence. "
        "Counts cover accepted active records; fixtures, pending review, and superseded records "
        "are excluded.",
        "## Latest changes", "## About the data",
    }),
}
MIGRATION_PENDING_REASON = "legacy skeleton with human text; manual migration needed"
ARCHIVE_KEPT_REASON = "archive month without active cards; kept because it has human text"


def machine_region(region: str, content: str) -> str:
    return f"<!-- chronolog:begin region=\"{region}\" -->\n{content.rstrip()}\n<!-- chronolog:end -->"


def replace_machine_region(existing: str, region: str, content: str) -> str:
    rendered = machine_region(region, content)
    pattern = re.compile(
        rf"<!-- chronolog:begin region=\"{re.escape(region)}\" -->.*?<!-- chronolog:end -->",
        re.S,
    )
    if pattern.search(existing):
        return pattern.sub(lambda _match: rendered, existing)
    return existing.rstrip() + "\n\n" + rendered + "\n"


def extract_machine_regions(markdown_body: str) -> dict[str, str]:
    return {match.group("name"): match.group("content").rstrip() for match in REGION_RE.finditer(markdown_body)}


def machine_fields(metadata: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in metadata.items()
        if key in MACHINE_FIELD_NAMES
    }


def render_frontmatter(metadata: dict[str, Any], body: str) -> str:
    post = frontmatter.Post(body, **metadata)
    return frontmatter.dumps(post)


def content_machine_hash(markdown: str) -> str:
    post = frontmatter.loads(markdown)
    return machine_hash(machine_fields(dict(post.metadata)), extract_machine_regions(post.content))


def ensure_vault_dirs(root: Path) -> None:
    for name in ["Products", "Changes", "Releases", "Themes", "Alerts", "Archive"]:
        (root / name).mkdir(parents=True, exist_ok=True)


def page_type(metadata: dict[str, Any]) -> str | None:
    """Kind of page whose skeleton the writer migrates (About and alerts are not)."""
    tags = metadata.get("tags") or []
    if metadata.get("type") == "change":
        return "change"
    if metadata.get("release_id"):
        return "release"
    if metadata.get("theme") and "theme" in tags:
        return "theme"
    if "index" in tags:
        return "index"
    if "archive" in tags:
        return "archive"
    if "product" in tags:
        return "product"
    return None


def region_names(markdown_body: str) -> list[str]:
    return [match.group("name") for match in REGION_RE.finditer(markdown_body)]


def _first_heading(markdown_body: str) -> str:
    return next(
        (line.rstrip() for line in markdown_body.splitlines() if line.startswith("# ")), ""
    )


def _leading_heading(body: str) -> tuple[int, str] | None:
    """Line index and text of the first H1 that precedes every machine region.

    Legacy skeletons put the generated H1 there; the new templates keep it inside the
    ``header`` region, so a ``# `` line after the regions is human text.
    """
    first_region = body.find(REGION_BEGIN)
    head = body if first_region < 0 else body[:first_region]
    for index, line in enumerate(head.split("\n")):
        if line.startswith("# "):
            return index, line.rstrip()
    return None


def legacy_residue(body: str, page_type: str | None) -> str:
    """Return the text a person wrote outside the generated skeleton of a page.

    Removes every machine region, the first ``# `` line (the generated H1, which comes
    before the regions) and the static section headings of ``page_type``.
    """
    lines = body.split("\n")
    heading = _leading_heading(body)
    if heading is not None:
        del lines[heading[0]]
    text = REGION_BLOCK_RE.sub("", "\n".join(lines))
    skeleton = SKELETON_HEADINGS.get(page_type or "", frozenset())
    return "\n".join(
        line for line in text.split("\n") if line.rstrip() not in skeleton
    ).strip()


def _is_generated_heading(
    heading: str,
    metadata: dict[str, Any],
    kind: str | None,
    rendered_heading: str,
) -> bool:
    """Whether a leading H1 is still the text an earlier writer version produced."""
    if heading == rendered_heading:
        return True
    record = metadata.get("record") if isinstance(metadata.get("record"), dict) else {}
    if kind == "change":
        if record.get("title"):
            return heading == f"# {str(record['title']).rstrip()}"
        return bool(metadata.get("title")) and wiki_label(heading[2:]) == str(metadata["title"])
    if kind == "release":
        product_name = record.get("product_name") or metadata.get("product_name")
        title = record.get("title") or metadata.get("source_release")
        return heading == f"# {product_name} {title}".rstrip()
    if kind == "theme":
        return heading == f"# Theme: {metadata.get('theme')}"
    return False


def refresh_generated_heading(
    body: str,
    existing_metadata: dict[str, Any],
    rendered_body: str,
    kind: str | None = "change",
) -> str:
    """Replace a leading H1 that still equals the previously generated heading.

    In a legacy skeleton the H1 sits outside the machine regions, so it is human-owned
    once edited: it is refreshed only while it matches what the writer generated
    (``record.title`` for cards); any other heading is kept. It is not part of
    ``machine_hash``.
    """
    new_heading = _first_heading(rendered_body)
    heading = _leading_heading(body)
    if (
        not new_heading
        or heading is None
        or not _is_generated_heading(heading[1], existing_metadata, kind, new_heading)
    ):
        return body
    lines = body.split("\n")
    lines[heading[0]] = new_heading
    return "\n".join(lines)


def merge_page_body(
    target: Path,
    body: str,
    metadata: dict[str, Any],
    rendered_body: str,
    kind: str,
    migration_pending: list[dict[str, str]] | None = None,
) -> str:
    """Merge a change, release, theme or index page, migrating an untouched skeleton.

    Without human text outside the machine regions the whole body becomes the rendered
    body, so a legacy skeleton is replaced instead of receiving appended regions. With
    human text the existing structure is kept: only regions the file already has are
    replaced, and a file whose regions differ from the template is reported as pending
    manual migration (not a conflict).

    A legacy card H1 that no longer matches ``record.title`` was edited by a person
    (PR 1 refreshed generated card headings), so it counts as human text. Release and
    theme H1s were never refreshed and may be stale, so they are always generated; so
    are the H1s of superseded cards, which PR 1 did not refresh either and which a new
    card definition can bring back under the same identity.
    """
    heading = _leading_heading(body)
    edited_heading = (
        kind == "change"
        and metadata.get("superseded") is not True
        and heading is not None
        and not _is_generated_heading(heading[1], metadata, kind, _first_heading(rendered_body))
    )
    if not edited_heading and not legacy_residue(body, kind):
        return rendered_body
    merged = refresh_generated_heading(body, metadata, rendered_body, kind)
    present = set(region_names(merged))
    rendered_regions = extract_machine_regions(rendered_body)
    for region, content in rendered_regions.items():
        if region in present:
            merged = replace_machine_region(merged, region, content)
    if region_names(merged) != list(rendered_regions) and migration_pending is not None:
        migration_pending.append({"file": str(target), "reason": MIGRATION_PENDING_REASON})
    return merged


def merge_machine_regions(body: str, rendered_regions: dict[str, str]) -> str:
    """Replace the machine regions of a page the writer does not migrate (About,
    alerts); a region the page lacks is appended, keeping all human text."""
    for region, content in rendered_regions.items():
        body = replace_machine_region(body, region, content)
    return body


def write_markdown_file(
    target: Path,
    rendered: str,
    conflicts: list[dict[str, str]] | None = None,
    migration_pending: list[dict[str, str]] | None = None,
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
                    "merge_conflict": True,
                }
            )
        return False

    rendered_post = frontmatter.loads(rendered)
    kind = page_type(existing_post.metadata)
    if kind in SKELETON_HEADINGS:
        merged_body = merge_page_body(
            target,
            existing_post.content,
            existing_post.metadata,
            rendered_post.content,
            kind,
            migration_pending,
        )
    else:
        merged_body = merge_machine_regions(
            existing_post.content, extract_machine_regions(rendered_post.content)
        )

    merged_metadata = {
        key: value
        for key, value in existing_post.metadata.items()
        if key not in MACHINE_FIELD_NAMES and key != "machine_hash"
    }
    merged_metadata.update(rendered_post.metadata)
    merged_metadata["machine_hash"] = machine_hash(
        machine_fields(merged_metadata), extract_machine_regions(merged_body)
    )
    write_text(target, render_frontmatter(merged_metadata, merged_body))
    return True


def wiki_label(text: str) -> str:
    text = re.sub(r"[`*\[\]]", "", text)
    text = text.replace('|', ' / ').replace('<', '').replace('>', '')
    text = re.sub(r"https?://\S+", "(source link)", text)
    text = text.replace("#", "♯")
    return re.sub(r"(?<!\w)_|_(?!\w)", "", text)


def card_link(
    card: dict[str, Any],
    card_targets: dict[str, str] | None = None,
    label: str | None = None,
) -> str:
    target = (
        card_targets.get(card["card_id"])
        if card_targets and card["card_id"] in card_targets
        else f"{card['date']}-{card['slug']}"
    )
    # Markdown code/emphasis inside a wiki alias splits the parser's text node,
    # leaving literal [[...]] in Quartz instead of a navigable link.
    return f"[[{target}|{wiki_label(label or card['title'])}]]"


def relation_link(
    card_id: str,
    card_targets: dict[str, str] | None,
    card_titles: dict[str, str] | None = None,
) -> str:
    if card_targets and card_id in card_targets:
        title = (card_titles or {}).get(card_id)
        return f"[[{card_targets[card_id]}|{wiki_label(title) if title else card_id}]]"
    return card_id


def theme_label(theme: str, theme_labels: dict[str, str] | None = None) -> str:
    return (theme_labels or {}).get(theme) or theme.replace("-", " ").title()


def load_theme_labels(path: Path) -> dict[str, str]:
    """Map theme slugs to vocabulary display names; empty when the file is absent."""
    if not path.exists():
        return {}
    return {
        slug: str(theme["display_name"])
        for slug, theme in load_theme_vocabulary(path).items()
        if theme.get("display_name")
    }


def cap_text(text: str, limit: int = DESCRIPTION_MAX_CHARS) -> str:
    """Collapse whitespace and cap at ``limit`` characters on a word boundary."""
    text = " ".join(str(text).split())
    if len(text) <= limit:
        return text
    cut = text[: limit - 1]
    if text[limit - 1] != " " and " " in cut:
        cut = cut.rsplit(" ", 1)[0]
    return cut.rstrip(" ,;:.·—–-") + "…"


def markdown_url(url: str) -> str:
    return str(url).strip().replace(" ", "%20").replace("(", "%28").replace(")", "%29")


def plural(count: int, noun: str) -> str:
    return f"{count} {noun}" if count == 1 else f"{count} {noun}s"


def natural_join(items: list[str]) -> str:
    if len(items) <= 2:
        return " and ".join(items)
    return ", ".join(items[:-1]) + " and " + items[-1]


def feedback_url(repository: str, card_id: str, card_path: str, source_url: str) -> str:
    """Prefilled GitHub issue for one card; empty when no repository is configured."""
    if not repository:
        return ""
    body = (
        f"Card: {card_path}\n"
        f"Card ID: {card_id}\n"
        f"Source: {source_url}\n\n"
        "What should be corrected?\n"
    )
    query = urlencode({"title": f"Card feedback: {card_id}", "body": body}, quote_via=quote)
    return f"{repository.rstrip('/')}/issues/new?{query}"


def editorial_lead(editorial: str) -> str:
    """First paragraph of an editorial narrative as plain text."""
    first = editorial.strip().split("\n\n", 1)[0] if editorial else ""
    text = re.sub(r"!?\[([^\]]*)\]\((?:[^()\s]|\([^()\s]*\))*\)", r"\1", first)
    text = re.sub(r"\*\*|\*|`", "", text)
    # Underscore emphasis only at word boundaries, so snake_case names survive.
    text = re.sub(r"(?<!\w)(__|_)(?=\S)(.+?)(?<=\S)\1(?!\w)", r"\2", text)
    return " ".join(text.split())


SCOPE_NOTE = (
    "Scope: tracked-products-only. Entries show same-theme chronology; "
    "they do not establish equivalent capabilities, adoption, or causation."
)
# Kinds labelled in theme timelines; expansion, fix and plain changes are not.
TIMELINE_KINDS = ("launch", "pricing", "policy", "digest")
KEY_MOMENTS_PER_PRODUCT = 12
KEY_MOMENTS_TOTAL = 30
AUTO_MOMENTS_CAPTION = "Selected automatically from launches and standalone announcements."
# Themes up to this many entries show their timeline open; longer ones fold each year.
TIMELINE_OPEN_MAX = 12


def scope_callout() -> str:
    """The collapsed reading note shared by timeline pages (U6)."""
    return callout("How to read this timeline", SCOPE_NOTE)


def table_link(card: dict[str, Any], card_targets: dict[str, str] | None = None) -> str:
    """``card_link`` with the alias pipe escaped, for a Markdown table cell."""
    return card_link(card, card_targets).replace("|", "\\|", 1)


def entries(count: int) -> str:
    return f"{count:,} entry" if count == 1 else f"{count:,} entries"


def granularity_note(product_names: list[str], verbosity: dict[str, float] | None) -> str:
    """``Claude Code averages 6.9 cards per release, Cursor 4.0, ChatGPT 1.7``.

    Uses each product's ``verbosity_baseline`` (cards per release with cards), most
    granular first; products without a baseline are left out."""
    known = sorted(
        ((name, float((verbosity or {})[name])) for name in product_names
         if (verbosity or {}).get(name)),
        key=lambda item: (-item[1], item[0]),
    )
    if not known:
        return ""
    (name, value), rest = known[0], known[1:]
    return f"{name} averages {value:.1f} cards per release" + "".join(
        f", {other} {other_value:.1f}" for other, other_value in rest
    )


def moment_tier(card: dict[str, Any]) -> int | None:
    """Auto-selection rank of a card as a key moment; ``None`` when it is not one.

    0: kind ``launch``; 1: a standalone announcement (``high_signal`` when recorded,
    otherwise a title or first quote matching the B+ high-signal patterns). Digest, fix
    and holding-theme cards never qualify; the machine impact level is a keyword
    heuristic and is not used."""
    kind = str(card.get("kind") or "change")
    if kind in {"digest", "fix"} or card.get("theme") in HOLDING_THEMES:
        return None
    if kind == "launch":
        return 0
    quote = str(card["evidence"][0]["quote"]) if card.get("evidence") else ""
    if card.get("high_signal") is True or is_high_signal(str(card.get("title", ""))) \
            or is_high_signal(quote):
        return 1
    return None


def auto_key_moments(cards: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Key moments of one theme without an editorial list, spread over time.

    Candidates (``moment_tier``) keep one card per release. Per product, the best card
    of each quarter that has a candidate is taken, newest quarter first (best rank, then
    newest), up to ``KEY_MOMENTS_PER_PRODUCT``; remaining slots go to the next best
    candidates, newest first. Above ``KEY_MOMENTS_TOTAL`` overall, the oldest moment of
    the product with the most moments is dropped until the total fits."""
    def rank(card: dict[str, Any]) -> tuple[int, int, str]:
        return (
            moment_tier(card) or 0,  # only candidates are ranked
            -date.fromisoformat(card["date"]).toordinal(),
            card["card_id"],
        )

    best: dict[tuple[str, str], dict[str, Any]] = {}
    for card in cards:
        if moment_tier(card) is None:
            continue
        key = (card["product"], str(card.get("source_release", card["card_id"])))
        if key not in best or rank(card) < rank(best[key]):
            best[key] = card
    by_product: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for card in best.values():
        by_product[card["product"]].append(card)

    selected: dict[str, list[dict[str, Any]]] = {}
    for product, candidates in by_product.items():
        quarters: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for card in candidates:
            quarters[quarter_label(card["date"])].append(card)
        picks = [min(quarters[quarter], key=rank) for quarter in sorted(quarters, reverse=True)]
        picks = picks[:KEY_MOMENTS_PER_PRODUCT]
        chosen = {card["card_id"] for card in picks}
        rest = sorted((card for card in candidates if card["card_id"] not in chosen), key=rank)
        selected[product] = picks + rest[: KEY_MOMENTS_PER_PRODUCT - len(picks)]

    def oldest(card: dict[str, Any]) -> tuple[str, str]:
        return (card["date"], card["card_id"])

    while sum(len(moments) for moments in selected.values()) > KEY_MOMENTS_TOTAL:
        most = max(len(moments) for moments in selected.values())
        # Among products tied for the most moments, trim the one holding the oldest.
        product = min(
            (name for name, moments in selected.items() if len(moments) == most),
            key=lambda name: (min(map(oldest, selected[name])), name),
        )
        selected[product].remove(min(selected[product], key=oldest))
    return sorted(
        (card for moments in selected.values() for card in moments),
        key=lambda card: (card["date"], card["card_id"]),
        reverse=True,
    )


def quarter_label(day: str) -> str:
    return f"{day[:4]} Q{(int(day[5:7]) - 1) // 3 + 1}"


def key_moments_table(
    moments: list[dict[str, Any]],
    product_names: list[str],
    card_targets: dict[str, str] | None,
) -> str:
    """One row per quarter with a key moment, newest first; one column per product."""
    rows: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    for card in moments:
        rows[quarter_label(card["date"])][card["product_name"]].append(card)
    lines = [
        "| Quarter | " + " | ".join(product_names) + " |",
        "| --- |" + " --- |" * len(product_names),
    ]
    for quarter in sorted(rows, reverse=True):
        cells = []
        for name in product_names:
            items = sorted(rows[quarter][name], key=lambda card: (card["date"], card["card_id"]),
                           reverse=True)
            cells.append(
                "<br>".join(f"{card['date']} {table_link(card, card_targets)}" for card in items)
                or "·"
            )
        lines.append(f"| {quarter} | " + " | ".join(cells) + " |")
    return "\n".join(lines)


def theme_timeline(cards: list[dict[str, Any]], card_targets: dict[str, str] | None) -> str:
    """Every card of a theme, newest first: one callout per year titled with its counts,
    months as bold labels inside. Years fold unless the theme has at most
    ``TIMELINE_OPEN_MAX`` entries; the key moments above summarise a long timeline."""
    if not cards:
        return "No changes yet."
    blocks: list[str] = []
    for year in sorted({card["date"][:4] for card in cards}, reverse=True):
        year_cards = [card for card in cards if card["date"].startswith(year)]
        counts = Counter(card["product_name"] for card in year_cards)
        breakdown = " · ".join(f"{name} {counts[name]:,}" for name in sorted(counts))
        lines: list[str] = []
        for month in sorted({card["date"][:7] for card in year_cards}, reverse=True):
            month_cards = sorted(
                (card for card in year_cards if card["date"].startswith(month)),
                key=lambda card: (card["product_name"], card["card_id"]),
            )
            month_cards.sort(key=lambda card: card["date"], reverse=True)
            lines.extend([f"**{month}**", ""])
            for card in month_cards:
                kind = str(card.get("kind") or "change")
                label = f" · {KIND_LABELS[kind]}" if kind in TIMELINE_KINDS else ""
                lines.append(
                    f"- {card['date']} · **{card['product_name']}** · "
                    f"{card_link(card, card_targets)}{label}"
                )
            lines.append("")
        blocks.append(callout(
            f"{year} · {entries(len(year_cards))} ({breakdown})",
            "\n".join(lines),
            folded=len(cards) > TIMELINE_OPEN_MAX,
        ))
    return "\n\n".join(blocks)


def render_theme_markdown(
    theme: str,
    cards: list[dict[str, Any]],
    card_targets: dict[str, str] | None = None,
    editorial: str = "",
    theme_labels: dict[str, str] | None = None,
    *,
    verbosity: dict[str, float] | None = None,
    key_moments: list[str] | None = None,
) -> str:
    """Theme page: header with counts and granularity, research summary, key moments,
    a collapsed reading note and the full timeline grouped by year and month.

    ``verbosity`` maps product names to ``verbosity_baseline``; ``key_moments`` is the
    validated editorial list of card ids for this theme (auto-selected when absent)."""
    display = theme_label(theme, theme_labels)
    ordered = sorted(cards, key=lambda card: (card["date"], card["product_name"], card["card_id"]))
    products_involved = sorted({card["product_name"] for card in ordered})
    if ordered:
        where = "across" if len(products_involved) > 1 else "in"
        parts = [
            f"{counted(len(ordered), 'tracked change')} {where} {natural_join(products_involved)}",
            f"{ordered[0]['date']} → {ordered[-1]['date']}",
        ]
        note = granularity_note(products_involved, verbosity)
        header = f"# {display}\n\n" + " · ".join(parts + ([note] if note else []))
    else:
        header = f"# {display}\n\nNo tracked changes yet."
    by_id = {card["card_id"]: card for card in ordered}
    curated = [by_id[card_id] for card_id in dict.fromkeys(key_moments or []) if card_id in by_id]
    moments = curated or auto_key_moments(ordered)
    caption = "" if curated else AUTO_MOMENTS_CAPTION
    if moments:
        table = key_moments_table(moments, products_involved, card_targets)
        moments_text = f"{caption}\n\n{table}" if caption else table
    else:
        moments_text = "No key moments selected yet." + (f" {caption}" if caption else "")
    regions = {
        "header": header,
        "narrative": editorial or "Explore the dated evidence below.",
        "moments": moments_text,
        "scope": scope_callout(),
        "timeline": theme_timeline(ordered, card_targets),
    }
    lead = editorial_lead(editorial)
    if not lead:
        scope = f" in {natural_join(products_involved)}" if products_involved else ""
        lead = f"Cross-product timeline of {display} changes{scope}."
    fields = {
        "tags": ["theme", "moc"],
        "title": wiki_label(display),
        "description": cap_text(lead),
        "status": "official",
        "publication": "fixture" if ordered and all(c.get("source_type") == "fixture" for c in ordered) else "active",
        "theme": theme,
        "products_involved": products_involved,
    }
    if ordered:
        fields.update(date=ordered[-1]["date"], created=ordered[0]["date"], modified=ordered[-1]["date"])
    fields["machine_hash"] = machine_hash(fields, regions)
    body = (
        f"{machine_region('header', regions['header'])}\n\n"
        f"## Research summary\n{machine_region('narrative', regions['narrative'])}\n\n"
        f"## Key moments\n{machine_region('moments', regions['moments'])}\n\n"
        f"{machine_region('scope', regions['scope'])}\n\n"
        f"## Timeline\n{machine_region('timeline', regions['timeline'])}\n"
    )
    return render_frontmatter(fields, body)


def kind_label(card: dict[str, Any]) -> str:
    """Display label of a card's kind; empty for a plain change or a pre-W2 record."""
    kind = str(card.get("kind") or "change")
    return "" if kind == "change" else KIND_LABELS.get(kind, kind.title())


def change_description(
    card: dict[str, Any],
    theme_labels: dict[str, str] | None = None,
    release_title: str | None = None,
) -> str:
    quote_text = card["evidence"][0]["quote"] if card.get("evidence") else card["title"]
    display = theme_label(card["theme"], theme_labels)
    if card.get("kind") == "digest":
        where = f" in {release_title}" if release_title else ""
        return cap_text(
            f"{card['product_name']} · {card['date']} · {display}: "
            f"{plural(len(card['evidence']), 'change')}{where} — {quote_text}"
        )
    return cap_text(f"{card['product_name']} · {card['date']} · {display}: {quote_text}")


# A quote is source text, not HTML: a placeholder such as <pr-url> outside a code span
# would be parsed as a tag and vanish from the page.
TAG_LIKE_RE = re.compile(r"<(?=[A-Za-z/!?])")
CODE_SPAN_RE = re.compile(r"(`+[^`]*`+)")


def quote_markdown(quote: str) -> str:
    """A source quote with tag-like ``<`` escaped outside inline code spans."""
    return "".join(
        part if part.startswith("`") else TAG_LIKE_RE.sub(r"\\<", part)
        for part in CODE_SPAN_RE.split(str(quote))
    )


def render_evidence(card: dict[str, Any]) -> str:
    """Quoted source text: a digest lists each item; other cards quote one group."""
    evidence = card["evidence"]
    sources = list(dict.fromkeys(str(item["source_release"]) for item in evidence))
    if card.get("kind") == "digest":
        quotes = "\n\n".join(f"> {quote_markdown(item['quote'])}" for item in evidence)
        return f"## Changes in this digest\n\n{quotes}\n\n" + "\n".join(
            f"Source: {source}" for source in sources
        )
    if len(evidence) > 1 and len(sources) == 1:
        quotes = "\n>\n".join(f"> {quote_markdown(item['quote'])}" for item in evidence)
        return f"{quotes}\n>\n> Source: {sources[0]}"
    return "\n\n".join(
        f"> {quote_markdown(item['quote'])}\n>\n> Source: {item['source_release']}"
        for item in evidence
    )


def render_change_markdown(
    card: dict[str, Any],
    patch_a: dict[str, Any],
    patch_b: dict[str, Any],
    card_targets: dict[str, str] | None = None,
    release_target: str | None = None,
    *,
    release_title: str | None = None,
    cards_by_id: dict[str, dict[str, Any]] | None = None,
    siblings: list[dict[str, Any]] | None = None,
    earlier: dict[str, Any] | None = None,
    later: dict[str, Any] | None = None,
    theme_labels: dict[str, str] | None = None,
    repository: str = "",
) -> str:
    """Render a Change Card whose body consists of machine regions only.

    ``siblings`` are the other active cards of the same release; ``earlier``/``later``
    are the neighbouring cards of the same theme across products. Section headings
    live inside their regions, so a section without content renders nothing.
    """
    cards_by_id = cards_by_id or {}
    raw_diffusion = dict(patch_b.get("diffusion", {}))
    linked_ids = [
        *patch_a.get("evolves_from", []),
        *patch_b.get("related_changes", []),
        raw_diffusion.get("first_in_tracked"),
    ]
    card_titles = {
        card_id: cards_by_id[card_id]["title"] for card_id in linked_ids if card_id in cards_by_id
    }
    display = theme_label(card["theme"], theme_labels)
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
            "kind",
            "scope",
            "impact",
            "extractor_version",
            "source_type",
        ]
        if key in card
    }
    metadata["title"] = wiki_label(card["title"])
    metadata["description"] = change_description(card, theme_labels, release_title)
    metadata["record"] = {key: value for key, value in card.items() if not key.startswith("_")}
    if release_target:
        metadata["source_release"] = f"[[{release_target}|{card['source_release']}]]"
    evolves_from = [
        relation_link(card_id, card_targets, card_titles)
        for card_id in patch_a.get("evolves_from", [])
    ]
    related_changes = [
        relation_link(card_id, card_targets, card_titles)
        for card_id in patch_b.get("related_changes", [])
    ]
    diffusion = dict(raw_diffusion)
    if diffusion.get("first_in_tracked"):
        diffusion["first_in_tracked"] = relation_link(
            diffusion["first_in_tracked"],
            card_targets,
            card_titles,
        )
    metadata["evolves_from"] = evolves_from
    if related_changes:
        metadata["related_changes"] = related_changes
    if diffusion:
        metadata["diffusion"] = diffusion

    source_url = card["evidence"][0]["source_release"] if card.get("evidence") else ""
    # A holding theme ("Other changes") has no theme page, timeline or neighbours.
    holding = card["theme"] in HOLDING_THEMES
    meta_line = [
        f"**{card['product_name']}**",
        card["date"],
        wiki_label(display) if holding else f"[[Themes/{card['theme']}|{wiki_label(display)}]]",
    ]
    if kind_label(card):
        meta_line.append(kind_label(card))
    if card.get("scope"):
        meta_line.append(wiki_label(str(card["scope"])))
    if source_url:
        meta_line.append(f"[Official source]({markdown_url(source_url)})")
    if release_target and release_title:
        meta_line.append(f"from [[{release_target}|{wiki_label(release_title)}]]")
    evidence = render_evidence(card)
    context_lines = [
        f"- {card_link(other, card_targets)} · {theme_label(other['theme'], theme_labels)}"
        for other in sorted(
            siblings or [], key=lambda item: (item["theme"] in HOLDING_THEMES, item["card_id"])
        )
        if other["card_id"] != card["card_id"]
    ]
    nearby_lines = [
        f"- {label}: {other['date']} · {other['product_name']} · {card_link(other, card_targets)}"
        for label, other in (("Earlier", earlier), ("Later", later))
        if other
    ]
    relation_lines = [f"- Builds on: {link}" for link in evolves_from]
    role = raw_diffusion.get("role")
    if role == "later-observed":
        first = cards_by_id.get(str(raw_diffusion.get("first_in_tracked", "")))
        if first:
            relation_lines.append(
                "- Earliest same-theme entry in the tracked set: "
                f"{first['date']} · {first['product_name']} · {card_link(first, card_targets)}"
            )
    elif role == "first-observed":
        count = raw_diffusion.get("tracked_products_count")
        relation_lines.append(
            f"- Earliest same-theme entry among the {count} tracked products."
            if count
            else "- Earliest same-theme entry in the tracked set."
        )
    if holding:
        nearby_lines, relation_lines = [], []
    card_path = (
        (card_targets or {}).get(card["card_id"])
        or f"Changes/{card['product_name']}/{card['date']}-{card['slug']}"
    )
    report_url = feedback_url(repository, card["card_id"], f"{card_path}.md", source_url)

    def section(heading: str, lines: list[str]) -> str:
        return f"## {heading}\n\n" + "\n".join(lines) if lines else ""

    body_regions = {
        "header": f"# {card['title'].rstrip()}\n\n" + " · ".join(meta_line),
        "evidence": evidence,
        "context": section("Also in this release", context_lines),
        "nearby": section(f"Nearby in {wiki_label(display)}", nearby_lines),
        "relations": section("Related", relation_lines),
        "footer": f"[Report an issue with this card]({report_url})" if report_url else "",
    }
    metadata["machine_hash"] = machine_hash(metadata, body_regions)
    body = "\n\n".join(
        machine_region(name, content) for name, content in body_regions.items()
    )
    return render_frontmatter(metadata, body)


CADENCE_BAR_WIDTH = 20
CADENCE_STATUS_LABELS = {"not-tracked": "not tracked", "collection-delayed": "collection delayed"}


def cadence_status(cadence: dict[str, Any] | None) -> str:
    status = str((cadence or {}).get("status") or "")
    return CADENCE_STATUS_LABELS.get(status, status)


def cadence_bar(count: int, peak: int) -> str:
    """``▇`` repeated ``count / peak`` of ``CADENCE_BAR_WIDTH`` (at least one); ``·`` at 0."""
    if count <= 0 or peak <= 0:
        return "·"
    return "▇" * max(1, math.floor(count / peak * CADENCE_BAR_WIDTH + 0.5))


def render_cadence(cadence: dict[str, Any] | None) -> str:
    """Product cadence panel from ``silence_monitor.cadence_summary`` (measured to the
    archive date, the newest archived release, not the clock)."""
    if not cadence:
        return "Release cadence has not been measured yet."
    if not cadence.get("last_release_date"):
        return "No releases archived yet."
    days = int(cadence["days_since_last_release"])
    gap = "the archive date" if days == 0 else f"{plural(days, 'day')} before the archive date"
    monthly = cadence.get("monthly_counts", [])
    peak = max((int(item["count"]) for item in monthly), default=0)
    bars = "\n".join(
        f"- {item['month']} · not archived" if item.get("archived") is False
        else f"- {item['month']} {cadence_bar(int(item['count']), peak)} {item['count']}"
        for item in monthly
    )
    return (
        f"Last release {cadence['last_release_date']} ({gap}) · "
        f"{plural(int(cadence['releases_90d']), 'release')} in the last 90 days · "
        f"cadence: {cadence_status(cadence)}\n\n"
        f"Monthly releases, last {len(monthly)} months "
        f"(baseline {float(cadence['baseline_monthly_releases']):.1f} per month):\n\n{bars}"
    )


PRODUCT_THEMES_SHOWN = 8
THEME_BAR_WIDTH = 12
RECENT_RELEASES_SHOWN = 10
ERA_RELEASES_SHOWN = 3
NO_NARRATIVE = ("The release archive records announced changes; "
                "a reviewed phase narrative is not yet available.")


def theme_bar(count: int, peak: int) -> str:
    """``█`` repeated ``count / peak`` of ``THEME_BAR_WIDTH`` (at least one)."""
    if count <= 0 or peak <= 0:
        return ""
    return "█" * max(1, min(THEME_BAR_WIDTH, math.floor(count / peak * THEME_BAR_WIDTH + 0.5)))


def callout(title: str, content: str, *, folded: bool = True) -> str:
    """A native ``<details>`` disclosure, collapsed unless ``folded`` is false (then open
    but collapsible). Quartz's own callouts open with a click handler on a ``div``: a
    keyboard cannot reach them and their hidden links stay in the tab order (critique
    2026-10-31, P0). Blank lines around the content keep it Markdown, so lists and
    wikilinks inside still render; ``disclosure`` is styled in ``site_title.tsx``."""
    opened = "" if folded else " open"
    return (
        f'<details class="disclosure"{opened}>\n<summary>{escape_html(title, quote=False)}</summary>\n\n'
        f"{content.rstrip()}\n\n</details>"
    )


def counted_cards(count: int) -> str:
    return f"{count:,} card" if count == 1 else f"{count:,} cards"


def product_themes(cards: list[dict[str, Any]], theme_labels: dict[str, str] | None) -> str:
    """The product's top themes by active card count, with a bar scaled to the top
    theme; Other changes (holding themes) last, as plain text."""
    counts = Counter(card["theme"] for card in cards if card["theme"] not in HOLDING_THEMES)
    top = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:PRODUCT_THEMES_SHOWN]
    peak = top[0][1] if top else 0
    lines = [
        f"- [[Themes/{theme}|{wiki_label(theme_label(theme, theme_labels))}]] · "
        f"{counted_cards(count)} · {theme_bar(count, peak)}"
        for theme, count in top
    ]
    held = sum(1 for card in cards if card["theme"] in HOLDING_THEMES)
    if held:
        label = theme_label(UNCATEGORIZED_THEME, theme_labels)
        lines.append(f"- {label} · {counted_cards(held)}")
    return "\n".join(lines) or "No tracked changes yet."


def release_label(
    release: dict[str, Any], release_targets: dict[str, str] | None
) -> str:
    target = (release_targets or {}).get(release["release_id"])
    label = wiki_label(str(release.get("title") or release.get("version") or release["release_id"]))
    return f"[[{target}|{label}]]" if target else label


def render_product_markdown(
    product: str,
    product_info: dict[str, Any],
    cards: list[dict[str, Any]],
    card_targets: dict[str, str] | None = None,
    releases: list[dict[str, Any]] | None = None,
    release_targets: dict[str, str] | None = None,
    theme_labels: dict[str, str] | None = None,
    cadence: dict[str, Any] | None = None,
) -> str:
    """Product page: positioning header, release cadence, eras, top themes, recent
    releases, coverage, then the release archive and every tracked change inside
    collapsed callouts (design review P6)."""
    name = product_info["product_name"]
    ordered = sorted(cards, key=lambda item: (item["date"], item["card_id"]))
    ordered_releases = sorted(
        releases or [],
        key=lambda item: (item["date"], item["release_id"]),
    )
    positioning = " ".join(str(product_info.get("positioning") or "").split())
    header_parts = [positioning] if positioning else []
    if ordered_releases:
        header_parts += [
            plural(len(ordered_releases), "release"),
            f"{ordered_releases[0]['date']} → {ordered_releases[-1]['date']}",
        ]
    header_parts.append("[[About|coverage details]]")

    era_lines = []
    for era in product_info.get("eras", []):
        sparse = " · data sparse" if era.get("data_sparse") else ""
        block = [f"### {era['name']} ({era['from']} → {era.get('to') or 'present'}){sparse}",
                 "", " ".join(str(era["summary"]).split())]
        evidence = era.get("evidence", [])[:ERA_RELEASES_SHOWN]
        if evidence:
            block += ["", "Representative releases:", ""]
        for item in evidence:
            target = (release_targets or {}).get(item["release_id"])
            internal = f" · [[{target}|Archived release]]" if target else ""
            block.append(f"- {item['date']}: [{item['title']}]({item['url']}){internal}")
        era_lines.append("\n".join(block))
    limitations = " ".join(str(product_info.get("narrative_limitations") or "").split())
    if era_lines and limitations:
        era_lines.append(f"**Scope:** {limitations}")

    cards_per_release = Counter(card.get("source_release") for card in ordered)
    recent_lines = [
        f"- {release['date']} · {release_label(release, release_targets)} · "
        f"{counted_cards(cards_per_release[release['release_id']])}"
        for release in reversed(ordered_releases[-RECENT_RELEASES_SHOWN:])
    ] or ["No releases collected yet."]
    release_lines = [
        f"- {release['date']}: {release_label(release, release_targets)}"
        for release in reversed(ordered_releases)
    ] or ["No releases collected yet."]
    change_lines: list[str] = []
    for year in sorted({card["date"][:4] for card in ordered}, reverse=True):
        year_cards = [card for card in reversed(ordered) if card["date"].startswith(year)]
        change_lines += [f"**{year}** · {counted_cards(len(year_cards))}", ""]
        change_lines += [
            f"- {card['date']} · {theme_label(card['theme'], theme_labels)}: "
            f"{card_link(card, card_targets)}"
            for card in year_cards
        ]
        change_lines.append("")
    regions = {
        "header": f"# {name}\n\n" + " · ".join(header_parts),
        "cadence": render_cadence(cadence),
        "narrative": " ".join(str(product_info.get("narrative_summary") or "").split())
        or NO_NARRATIVE,
        "eras": "\n\n".join(era_lines)
        or "No reviewed eras assigned yet. The release archive below is chronological.",
        "themes": product_themes(ordered, theme_labels),
        "recent": "\n".join(recent_lines),
        "coverage": (
            render_coverage_summary(
                product_info.get("coverage", {}),
                len(ordered_releases) if releases is not None else None,
            )
            + "\n\nAcquisition details, how cards are made and known gaps: [[About]]."
        ),
        "releases": callout(
            f"Release archive ({plural(len(ordered_releases), 'release')})",
            "\n".join(release_lines),
        ),
        "changes": callout(
            f"All tracked changes ({counted_cards(len(ordered))})",
            "\n".join(change_lines) or "No tracked changes yet.",
        ),
    }
    timeline_dates = [item["date"] for item in ordered_releases] or [
        item["date"] for item in ordered
    ]
    description = positioning or (
        f"{name}: "
        + (f"{plural(len(ordered_releases), 'archived release')} and " if ordered_releases else "")
        + f"{plural(len(ordered), 'tracked change')}."
    )
    fields = {
        "tags": ["product"],
        "title": name,
        "description": cap_text(description),
        "product": product,
        "product_name": name,
        "verbosity_baseline": product_info["verbosity_baseline"],
        "top_themes": product_info.get("top_themes", []),
        "coverage": product_info.get("coverage", {}),
        "publication": "fixture" if ordered_releases and all(r.get("source_type") == "fixture" for r in ordered_releases) else "active",
    }
    if timeline_dates:
        fields.update(
            {
                "date": max(timeline_dates),
                "created": min(timeline_dates),
                "modified": max(timeline_dates),
            }
        )
    fields["machine_hash"] = machine_hash(fields, regions)
    body = (
        f"{machine_region('header', regions['header'])}\n\n"
        f"## Release cadence\n{machine_region('cadence', regions['cadence'])}\n\n"
        f"## Eras\n{machine_region('narrative', regions['narrative'])}\n\n"
        f"{machine_region('eras', regions['eras'])}\n\n"
        f"## Themes\n{machine_region('themes', regions['themes'])}\n\n"
        f"## Recent releases\n{machine_region('recent', regions['recent'])}\n\n"
        f"## Coverage\n{machine_region('coverage', regions['coverage'])}\n\n"
        f"{machine_region('releases', regions['releases'])}\n\n"
        f"{machine_region('changes', regions['changes'])}\n"
    )
    return render_frontmatter(fields, body)


def release_heading(release: dict[str, Any]) -> str:
    """``Product · Title``, without repeating a product name the title already starts with."""
    title = str(release["title"]).strip()
    product_name = str(release["product_name"])
    if title.casefold().startswith(product_name.casefold()):
        return title
    return f"{product_name} · {title}"


def candidate_line_count(release: dict[str, Any]) -> int | None:
    """Release lines eligible for extraction, from the body or the persisted record."""
    if release.get("body") is not None:
        return len(split_release_lines(str(release["body"])))
    stored = release.get("candidate_line_count")
    return int(stored) if isinstance(stored, int) and not isinstance(stored, bool) else None


def informative_summary(summary: Any, title: Any) -> bool:
    text = str(summary or "").strip()
    return (
        bool(text)
        and text.casefold() != str(title or "").strip().casefold()
        and not GENERIC_HEADING_RE.fullmatch(text)
    )


def tracked_line(count: int, candidates: int | None, pending_lines: int = 0) -> str:
    """``Tracked N cards from M candidate lines; K lines pending review.``"""
    if candidates is not None and candidates >= count:
        tracked = f"Tracked {plural(count, 'card')} from {plural(candidates, 'candidate line')}"
    else:
        tracked = f"Tracked {plural(count, 'card')}"
    if pending_lines:
        tracked += f"; {plural(pending_lines, 'line')} pending review"
    return tracked + "."


def release_cards_summary(
    count: int, theme_displays: list[str], other: int, other_label: str
) -> str:
    """``12 tracked changes across 11 themes: A, B; 1 in Other changes.``"""
    if not theme_displays:
        return f"{plural(count, 'tracked change')}, all in {other_label}."
    summary = (
        f"{plural(count, 'tracked change')} across {plural(len(theme_displays), 'theme')}: "
        f"{', '.join(theme_displays)}"
    )
    return summary + (f"; {other} in {other_label}." if other else ".")


def render_release_markdown(
    release: dict[str, Any],
    card_targets: dict[str, str] | None = None,
    theme_labels: dict[str, str] | None = None,
    *,
    pending_lines: int = 0,
) -> str:
    """Render a Release page. ``pending_lines`` counts this release's lines waiting in
    the theme review queue. Cards of a holding theme ("Other changes") are listed last
    and are not counted as a theme."""
    cards = sorted(
        release.get("cards", []),
        key=lambda card: (card["theme"] in HOLDING_THEMES, card["date"], card["card_id"]),
    )
    count = len(cards)
    theme_counts = Counter(card["theme"] for card in cards if card["theme"] not in HOLDING_THEMES)
    other = count - sum(theme_counts.values())
    other_label = theme_label(UNCATEGORIZED_THEME, theme_labels)
    theme_displays = [
        theme_label(theme, theme_labels)
        for theme, _ in sorted(
            theme_counts.items(),
            key=lambda item: (-item[1], theme_label(item[0], theme_labels)),
        )
    ]
    heading = release_heading(release)
    candidates = candidate_line_count(release)
    card_lines = [
        f"- {card_link(card, card_targets)} · {theme_label(card['theme'], theme_labels)}"
        + (f" · {kind_label(card)}" if kind_label(card) else "")
        for card in cards
    ]
    if informative_summary(release.get("source_summary"), release["title"]):
        summary = str(release["source_summary"]).strip()
    elif cards:
        summary = release_cards_summary(count, theme_displays, other, other_label)
    else:
        summary = "No change cards extracted."
    tracked = tracked_line(count, candidates, pending_lines)
    regions = {
        "header": (
            f"# {heading}\n\n"
            f"**{release['product_name']}** · {release['date']} · "
            f"[Official release notes]({markdown_url(release['source_url'])})"
        ),
        "summary": f"{summary}\n\n{tracked}",
        "cards": "\n".join(card_lines) or "No change cards extracted.",
    }
    description = (
        f"{release['product_name']} release {wiki_label(str(release['title']))} on {release['date']}: "
        + (
            f"{plural(count, 'tracked change')} across "
            + ", ".join(theme_displays + ([other_label] if other else []))
            if cards
            else "no tracked changes"
        )
    )
    record = {
        key: value for key, value in release.items()
        if key not in {"body", "cards"} and not key.startswith("_")
    }
    if candidates is not None:
        record["candidate_line_count"] = candidates
    fields = {
        "tags": ["release", release["product"]],
        "title": wiki_label(heading),
        "description": cap_text(description),
        "record": record,
        "release_id": release["release_id"],
        "product": release["product"],
        "product_name": release["product_name"],
        "source_release": release["title"],
        "version": release.get("version") or release["title"],
        "source_url": release["source_url"],
        "source_type": release.get("source_type", "unknown"),
        "changes_count": count,
        "date": release["date"],
    }
    fields["machine_hash"] = machine_hash(fields, regions)
    body = (
        f"{machine_region('header', regions['header'])}\n\n"
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


SITE_TITLE = "ChronoLog"
ABOUT_LINK = "[[About|About the data]]"
# Curated taglines; other themes with a research summary show its research question.
FEATURED_THEMES = (
    ("agent-mode", "From assisted edits to delegated work"),
    ("pricing-model", "Plans, allowances, and usage charging"),
)
RESEARCH_QUESTION_RE = re.compile(r"\*\*Research question:\s*(.+?)\*\*")
THEME_CATEGORY_ORDER = (
    "paradigm", "capability", "workflow", "platform", "ecosystem", "business", "trust", "quality",
)
RECENT_WINDOW_DAYS = 30
RECENT_PER_PRODUCT = 6
RECENT_THEMES_SHOWN = 3
# Home-page headline of a versioned release: a launch, then a standalone announcement
# (rank 1, see moment_tier), then pricing or policy, then an expansion. Plain changes,
# fixes and digests are not headlines.
HEADLINE_KIND_RANK = {"launch": 0, "pricing": 2, "policy": 2, "expansion": 3}
VERSION_TITLE_RE = re.compile(r"^v?\d+(?:\.\d+)+")
RELEASE_ACTIVITY_DAYS = 90
NUMBER_WORDS = ("no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten")


def number_word(count: int) -> str:
    return NUMBER_WORDS[count] if 0 <= count < len(NUMBER_WORDS) else str(count)


def counted(count: int, noun: str) -> str:
    """``plural`` with thousands separators, for headline counts."""
    return f"{count:,} {noun}" if count == 1 else f"{count:,} {noun}s"


def window_start(end: str, days: int) -> str:
    """First day of the ``days``-day window that ends on (and includes) ``end``."""
    return (date.fromisoformat(end) - timedelta(days=days - 1)).isoformat()


def site_lead(product_names: list[str]) -> str:
    scope = f" in {natural_join(product_names)}" if product_names else ""
    return f"Tracked changes{scope}, from official release notes."


def aggregate_publication(cards: list[dict[str, Any]]) -> str:
    return "fixture" if cards and all(c.get("source_type") == "fixture" for c in cards) else "active"


def aggregate_dates(cards: list[dict[str, Any]]) -> dict[str, str]:
    if not cards:
        return {}
    ordered_dates = sorted(card["date"] for card in cards)
    return {"date": ordered_dates[-1], "created": ordered_dates[0], "modified": ordered_dates[-1]}


def ordered_products(products: dict[str, dict[str, Any]]) -> list[tuple[str, dict[str, Any]]]:
    return sorted(products.items(), key=lambda item: (item[1]["product_name"], item[0]))


ARCHIVE_LINK = "All months: [[Archive/index|Archive]]"


def headline_rank(card: dict[str, Any]) -> int | None:
    """Rank of a card as its release's home-page headline, lower first; ``None`` when
    it is not a headline."""
    if moment_tier(card) == 1:
        return 1
    return HEADLINE_KIND_RANK.get(str(card.get("kind") or "change"))


def release_line(
    release: dict[str, Any] | None,
    release_cards: list[dict[str, Any]],
    card_targets: dict[str, str] | None,
    release_targets: dict[str, str] | None,
    theme_labels: dict[str, str] | None,
) -> str:
    """One home-page line for the cards of one release.

    A single card is listed as itself. A release with a descriptive title (ChatGPT,
    Cursor) is listed by that title; a versioned release (Claude Code) by its best
    headline card when it has one, otherwise by its version. Release lines name the
    themes with the most quoted items."""
    def card_line(card: dict[str, Any], suffix: str = "") -> str:
        return (f"- {card['date']} · {theme_label(card['theme'], theme_labels)}: "
                f"{card_link(card, card_targets)}{suffix}")

    def headline_key(card: dict[str, Any]) -> tuple[int, int, str]:
        rank = headline_rank(card)
        return (len(HEADLINE_KIND_RANK) + 1 if rank is None else rank,
                -len(card.get("evidence") or []), card["card_id"])

    if len(release_cards) == 1:
        return card_line(release_cards[0])
    if release is None:
        return card_line(min(release_cards, key=headline_key), f" · +{len(release_cards) - 1} more")
    title = str(release.get("title") or "")
    link = release_label(release, release_targets)
    if not title or VERSION_TITLE_RE.match(title):
        headlines = [card for card in release_cards if headline_rank(card) is not None]
        if headlines:
            return card_line(min(headlines, key=headline_key),
                             f" · +{len(release_cards) - 1} more in {link}")
    items: Counter = Counter()
    for card in release_cards:
        items[theme_label(card["theme"], theme_labels)] += max(1, len(card.get("evidence") or []))
    themes = [label for label, _ in sorted(items.items(), key=lambda item: (-item[1], item[0]))]
    shown = themes[:RECENT_THEMES_SHOWN]
    if len(themes) > len(shown):
        shown.append(f"+{len(themes) - len(shown)} more")
    return (f"- {release['date']} · {link} · {counted_cards(len(release_cards))}: "
            + ", ".join(shown))


def recent_changes(
    cards: list[dict[str, Any]],
    products: list[tuple[str, dict[str, Any]]],
    alerts: list[dict[str, Any]],
    card_targets: dict[str, str] | None,
    theme_labels: dict[str, str] | None,
    releases: dict[str, dict[str, Any]] | None = None,
    release_targets: dict[str, str] | None = None,
) -> str:
    """Newest releases per product in the window ending at the latest card date (not
    today), one line each (``release_line``), followed by a link to the monthly archive.

    Cards of a holding theme ("Other changes") are left out, including from the counts;
    ``releases`` maps release ids to releases."""
    cards = [card for card in cards if card["theme"] not in HOLDING_THEMES]
    warnings = [f"- ⚠ {alert['product_name']}: {alert['message']}" for alert in alerts]
    sections = ["\n".join(warnings)] if warnings else []
    if not cards:
        return "\n\n".join(sections + ["No changes archived yet.", ARCHIVE_LINK])
    anchor = max(card["date"] for card in cards)
    start = window_start(anchor, RECENT_WINDOW_DAYS)
    for product, info in products:
        name = info["product_name"]
        by_release: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for card in cards:
            if card["product"] == product and start <= card["date"] <= anchor:
                by_release[str(card.get("source_release") or card["card_id"])].append(card)
        newest = sorted(
            by_release.items(),
            key=lambda item: (max(card["date"] for card in item[1]), item[0]),
            reverse=True,
        )
        entries = [
            release_line((releases or {}).get(release_id), release_cards, card_targets,
                         release_targets, theme_labels)
            for release_id, release_cards in newest[:RECENT_PER_PRODUCT]
        ] or [f"- No changes archived between {start} and {anchor}."]
        remaining = len(newest) - RECENT_PER_PRODUCT
        if remaining > 0:
            entries.append(
                f"- {plural(remaining, 'more release')} in this window → [[Products/{name}|{name}]]"
            )
        sections.append(f"### {name}\n" + "\n".join(entries))
    return "\n\n".join(sections + [ARCHIVE_LINK])


def featured_themes(
    narratives: dict[str, str],
    theme_counts: Counter,
    theme_labels: dict[str, str] | None,
) -> str:
    """Every theme with a research summary and active cards: curated taglines first, in
    ``FEATURED_THEMES`` order, then the others by card count with their research question."""
    taglines = dict(FEATURED_THEMES)
    curated = list(taglines)
    themes = sorted(
        (theme for theme in narratives if theme_counts.get(theme)),
        key=lambda theme: (curated.index(theme) if theme in taglines else len(curated),
                           -theme_counts[theme], theme),
    )
    lines = []
    for theme in themes:
        label = taglines.get(theme, "")
        if not label:
            question = RESEARCH_QUESTION_RE.search(narratives[theme])
            label = question.group(1).strip() if question else ""
            label = label[:1].upper() + label[1:]
        link = f"[[Themes/{theme}|{wiki_label(theme_label(theme, theme_labels))}]]"
        lines.append(f"- {link} — {label}" if label else f"- {link}")
    return "\n".join(lines)


def product_activity(
    products: list[tuple[str, dict[str, Any]]],
    releases_by_product: dict[str, list[dict[str, Any]]],
    cadence: dict[str, dict[str, Any]] | None = None,
) -> str:
    """Release count, range, releases in the window ending at the latest release overall
    and the cadence status when it was measured."""
    all_dates = [release["date"] for releases in releases_by_product.values() for release in releases]
    latest = max(all_dates) if all_dates else None
    lines = []
    for product, info in products:
        name = info["product_name"]
        dates = sorted(release["date"] for release in releases_by_product.get(product, []))
        if not dates or latest is None:
            lines.append(f"- [[Products/{name}|{name}]] · No releases archived yet.")
            continue
        start = window_start(latest, RELEASE_ACTIVITY_DAYS)
        recent = sum(start <= value <= latest for value in dates)
        status = cadence_status((cadence or {}).get(product))
        lines.append(
            f"- [[Products/{name}|{name}]] · {plural(len(dates), 'release')} · "
            f"{dates[0]} → {dates[-1]} · {plural(recent, 'release')} in the last "
            f"{RELEASE_ACTIVITY_DAYS} days" + (f" · cadence: {status}" if status else "")
        )
    return "\n".join(lines)


def theme_groups(
    theme_counts: Counter,
    vocabulary: dict[str, dict[str, Any]] | None,
    theme_labels: dict[str, str] | None,
) -> str:
    """Themes with active cards, grouped by vocabulary category."""
    grouped: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for theme, count in theme_counts.items():
        category = str((vocabulary or {}).get(theme, {}).get("category") or "other")
        grouped[category].append((theme, count))

    def category_key(category: str) -> tuple[int, str]:
        known = category in THEME_CATEGORY_ORDER
        return (THEME_CATEGORY_ORDER.index(category) if known else len(THEME_CATEGORY_ORDER), category)

    lines = []
    for category in sorted(grouped, key=category_key):
        entries = sorted(
            grouped[category], key=lambda item: (-item[1], theme_label(item[0], theme_labels))
        )
        links = " · ".join(
            f"[[Themes/{theme}|{wiki_label(theme_label(theme, theme_labels))}]] ({count})"
            for theme, count in entries
        )
        lines.append(f"**{category.title()}** · {links}")
    return "\n\n".join(lines)


def release_count(releases_by_product: dict[str, list[dict[str, Any]]], product: str) -> int | None:
    return len(releases_by_product[product]) if product in releases_by_product else None


def render_index_markdown(
    cards: list[dict[str, Any]],
    analysis_a: dict[str, Any],
    analysis_b: dict[str, Any],
    silence: dict[str, Any],
    theme_labels: dict[str, str] | None = None,
    *,
    releases_by_product: dict[str, list[dict[str, Any]]] | None = None,
    vocabulary: dict[str, dict[str, Any]] | None = None,
    card_targets: dict[str, str] | None = None,
    release_targets: dict[str, str] | None = None,
) -> str:
    """Reader home page: latest changes, products, themes and a coverage summary.

    Every number is derived from the data (no clock): the latest-changes window ends at
    the newest card date and the release activity window at the newest release date.
    Acquisition timestamps and review counts live on the About page.
    """
    products = ordered_products(analysis_a.get("products", {}))
    releases_by_product = releases_by_product or {}
    releases_by_id = {
        release["release_id"]: release
        for releases in releases_by_product.values() for release in releases
    }
    # A holding theme is not a theme: no group, no page and not in the theme count.
    theme_counts = Counter(card["theme"] for card in cards if card["theme"] not in HOLDING_THEMES)
    release_dates = [r["date"] for releases in releases_by_product.values() for r in releases]
    archive_end = max(release_dates) if release_dates else max(
        (card["date"] for card in cards), default=None
    )
    stats = [
        counted(len(products), "product"),
        counted(len(cards), "tracked change"),
        counted(len(theme_counts), "theme"),
    ]
    if archive_end:
        stats.append(f"archive to {archive_end}")
    stats.append(ABOUT_LINK)
    product_names = [info["product_name"] for _, info in products]
    coverage_lines = [
        f"- {info['product_name']} · "
        + render_coverage_summary(info.get("coverage", {}), release_count(releases_by_product, product))
        for product, info in products
    ]
    regions = {
        "header": f"# {SITE_TITLE}\n\n{site_lead(product_names)} " + " · ".join(stats),
        "recent": recent_changes(
            cards, products, silence.get("alerts", []), card_targets, theme_labels,
            releases_by_id, release_targets,
        ),
        "featured": featured_themes(
            analysis_b.get("editorial", {}), theme_counts, theme_labels
        ) or "No featured themes yet.",
        "products": product_activity(
            products, releases_by_product, silence.get("cadence")
        ) or "No products yet.",
        "themes": theme_groups(theme_counts, vocabulary, theme_labels) or "No themes yet.",
        "coverage": (
            ("\n".join(coverage_lines) or "No sources recorded yet.")
            + f"\n\nAcquisition times, how cards are made, review status and glossary: {ABOUT_LINK}."
        ),
    }
    fields = {"tags": ["index"], "title": SITE_TITLE, "publication": aggregate_publication(cards)}
    fields.update(aggregate_dates(cards))
    fields["machine_hash"] = machine_hash(fields, regions)
    body = (
        f"{machine_region('header', regions['header'])}\n\n"
        f"## Latest changes\n{machine_region('recent', regions['recent'])}\n\n"
        f"## Start exploring\n{machine_region('featured', regions['featured'])}\n\n"
        f"## Products\n{machine_region('products', regions['products'])}\n\n"
        f"## Themes\n{machine_region('themes', regions['themes'])}\n\n"
        f"## About the data\n{machine_region('coverage', regions['coverage'])}\n"
    )
    return render_frontmatter(fields, body)


ABOUT_METHOD = "\n".join([
    "- Each archived release is read as headings, paragraphs and list items.",
    "- Version-only lines, availability notes, instructions and unclassified bug-fix lines "
    "are skipped.",
    "- A feature heading and the text under it become one Change Card, titled by the heading.",
    "- Consecutive paragraphs about one theme become one card. When a release yields a "
    "single card, the card takes the release title.",
    "- Items under a platform or plan heading (such as Web, iOS or Plus) and lists of up "
    "to eight items become one card each.",
    "- Longer lists, lists under headings such as \"What's changed\" or \"Bug fixes\", and "
    "GitHub release notes are read item by item. Items that announce something on their own "
    "(\"Introducing …\", a new slash command, a feature now on by default) stay separate "
    "cards; the other items of one theme are listed together on one digest card per release.",
    "- Every card has one theme from a fixed vocabulary and a kind: launch, expansion, "
    "pricing, policy, fix, digest or change.",
    "- Lines without a confident theme are published in an \"Other changes\" digest of their "
    "release and do not appear on theme pages or the home page; prose without a theme waits "
    "in a review queue. Each release page shows \"Tracked N cards from M candidate lines\" "
    "and how many lines wait for review.",
    "- Dates are announcement dates, not availability dates.",
    "- Cadence is measured to the newest archived release date, not the clock.",
    "- Relations between cards are same-theme chronology only; they never claim adoption "
    "or causation.",
])
ABOUT_GLOSSARY = "\n".join([
    "- **Change Card**: one announced change that can be understood on its own, taken from "
    "an official release, with a date, one theme, a kind and the quoted source text.",
    "- **Digest card**: the smaller changes of one theme in one release, quoted together on "
    "one card.",
    "- **Other changes**: the list items of one release without a confident theme, quoted "
    "together on one digest card (a single item keeps its own card); listed on release and "
    "product pages, not on theme pages or the home page.",
    "- **Release**: one archived entry of an official changelog or release page; its page "
    "lists the cards tracked from it.",
    "- **Theme**: a category from a fixed vocabulary that groups cards across products.",
    "- **Era**: a reviewed phase of one product's history, bounded by cited releases.",
    "- **Key moments**: on a theme page, the cards an editor selected; until then up to 12 "
    "per product are chosen automatically from launches and standalone announcements, one "
    "per quarter first and never two from one release.",
    "- **Cadence**: releases per month on a product page. *Quiet* means each of the last two "
    "months had fewer than half the product's average monthly releases; *silent* means no "
    "release in the last two months, which also raises a silence alert.",
    "- **Tracked products only**: comparisons and \"earliest\" statements cover only the "
    "tracked products, not the wider market.",
    "- **Candidate line**: a line of release text that could become part of a card; Markdown "
    "headings, code samples and very short lines are not counted. \"Tracked N cards from M "
    "candidate lines\" compares the cards kept with these lines.",
])


def render_about_markdown(
    cards: list[dict[str, Any]],
    products: dict[str, dict[str, Any]],
    releases_by_product: dict[str, list[dict[str, Any]]],
    silence: dict[str, Any],
    pending_theme_review: int = 0,
    repository: str = "",
) -> str:
    """``About.md``: sources, acquisition, method, review status, glossary and feedback.

    The only page that shows acquisition timestamps; their sentences use the exact
    ``editorial.acquisition_line`` wording that ``quality.normalized_page`` masks.
    """
    ordered = ordered_products(products)
    names = [info["product_name"] for _, info in ordered]
    scope = f"{number_word(len(names))} {'product' if len(names) == 1 else 'products'}"
    intro = (
        f"ChronoLog tracks announced changes in {scope}: {natural_join(names)}. "
        if names else "ChronoLog tracks announced product changes. "
    ) + (
        "It reads official release notes only, turns each release into dated Change Cards and "
        "groups them by theme. Every record is reviewed before it is published."
    )
    archived = sum(len(releases) for releases in releases_by_product.values())
    themes = len({card["theme"] for card in cards if card["theme"] not in HOLDING_THEMES})
    alerts = len(silence.get("alerts", []))
    issues = f"{repository.rstrip('/')}/issues" if repository else ""
    regions = {
        "intro": intro,
        "sources": "\n\n".join(
            render_source_details(
                info["product_name"], info.get("coverage", {}),
                release_count(releases_by_product, product),
            )
            for product, info in ordered
        ) or "No sources recorded yet.",
        "method": ABOUT_METHOD,
        "status": (
            f"{counted(len(names), 'product')} · {counted(archived, 'archived release')} · "
            f"{counted(len(cards), 'tracked change')} · {counted(themes, 'theme')}. "
            f"Pending theme review: {pending_theme_review:,}. Silence alerts: {alerts:,}. "
            "Every generated batch is reviewed in a pull request before it is published."
        ),
        "glossary": ABOUT_GLOSSARY,
        "feedback": (
            "Every card ends with a link that opens a prefilled issue. "
            f"For anything else, open an issue at [{issues}]({issues})."
        ) if issues else "",
    }
    fields = {
        "tags": ["about"],
        "title": "About the data",
        "description": cap_text(
            "Where ChronoLog's data comes from, how official release notes become reviewed "
            "Change Cards, what is grouped or skipped, and how to report a problem."
        ),
        "publication": aggregate_publication(cards),
    }
    fields.update(aggregate_dates(cards))
    fields["machine_hash"] = machine_hash(fields, regions)
    body = (
        "# About the data\n\n"
        f"{machine_region('intro', regions['intro'])}\n\n"
        f"## Sources and coverage\n{machine_region('sources', regions['sources'])}\n\n"
        f"## How cards are made\n{machine_region('method', regions['method'])}\n\n"
        f"## Review status\n{machine_region('status', regions['status'])}\n\n"
        f"## Glossary\n{machine_region('glossary', regions['glossary'])}\n\n"
        f"## Feedback\n{machine_region('feedback', regions['feedback'])}\n"
    )
    return render_frontmatter(fields, body)


MONTH_NAMES = (
    "January", "February", "March", "April", "May", "June", "July", "August", "September",
    "October", "November", "December",
)
ARCHIVE_DIRECTORY = "Archive"
# The archive's own page is the folder note ``Archive/index.md``: Quartz renders a folder
# note as the folder page, whereas a root ``Archive.md`` would also be rendered there with
# its links resolved from the wrong directory.
ARCHIVE_INDEX = "index"
ARCHIVE_MONTH_RE = re.compile(r"^\d{4}-\d{2}$")


def month_title(month: str) -> str:
    """``October 2026`` for ``2026-10``."""
    return f"{MONTH_NAMES[int(month[5:7]) - 1]} {month[:4]}"


def archive_months(cards: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """Active cards (holding themes included) by ``YYYY-MM`` of their date."""
    months: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for card in cards:
        months[str(card["date"])[:7]].append(card)
    return dict(months)


def product_breakdown(cards: list[dict[str, Any]], separator: str = " · ") -> str:
    """``ChatGPT 42 · Claude Code 86 · Cursor 14`` (products with cards, by name)."""
    counts = Counter(card["product_name"] for card in cards)
    return separator.join(f"{name} {counts[name]:,}" for name in sorted(counts))


def archive_month_link(month: str) -> str:
    return f"[[{ARCHIVE_DIRECTORY}/{month}|{month_title(month)}]]"


def render_archive_month_markdown(
    month: str,
    cards: list[dict[str, Any]],
    card_targets: dict[str, str] | None = None,
    theme_labels: dict[str, str] | None = None,
    *,
    previous: str | None = None,
    following: str | None = None,
) -> str:
    """``Archive/YYYY-MM.md``: the month's cards per product, newest first. On one date,
    cards of a holding theme ("Other changes") follow the themed ones."""
    title = month_title(month)
    navigation = " · ".join(
        part for part in (
            f"← {archive_month_link(previous)}" if previous else "",
            f"[[{ARCHIVE_DIRECTORY}/{ARCHIVE_INDEX}|All months]]",
            f"{archive_month_link(following)} →" if following else "",
        ) if part
    )
    sections = []
    for name in sorted({card["product_name"] for card in cards}):
        product_cards = sorted(
            (card for card in cards if card["product_name"] == name),
            key=lambda card: (
                card["theme"] in HOLDING_THEMES,
                theme_label(card["theme"], theme_labels),
                card["card_id"],
            ),
        )
        product_cards.sort(key=lambda card: card["date"], reverse=True)
        lines = [
            f"- {card['date']} · {wiki_label(theme_label(card['theme'], theme_labels))} · "
            f"{card_link(card, card_targets)}" + (f" · {kind_label(card)}" if kind_label(card) else "")
            for card in product_cards
        ]
        sections.append(f"### {name}\n\n" + "\n".join(lines))
    regions = {
        "header": (
            f"# {title}\n\n{counted(len(cards), 'tracked change')} · {product_breakdown(cards)}"
            f"\n\n{navigation}"
        ),
        "changes": "\n\n".join(sections) or "No changes archived in this month.",
    }
    fields = {
        "tags": ["archive"],
        "title": title,
        "description": cap_text(
            f"{counted(len(cards), 'tracked change')} announced in {title}: "
            f"{natural_join(product_breakdown(cards, '|').split('|'))}."
        ),
        "publication": aggregate_publication(cards),
    }
    fields.update(aggregate_dates(cards))
    fields["machine_hash"] = machine_hash(fields, regions)
    body = (
        f"{machine_region('header', regions['header'])}\n\n"
        f"{machine_region('changes', regions['changes'])}\n"
    )
    return render_frontmatter(fields, body)


def render_archive_markdown(cards: list[dict[str, Any]]) -> str:
    """``Archive/index.md``: every month with cards, newest first, grouped by year.

    Quartz shows it as the ``Archive/`` folder page, which prints the title itself, so the
    header region has no H1 (``_scripts/folder_content.tsx`` also drops the folder's
    automatic page list, which would repeat the months)."""
    months = archive_months(cards)
    ordered = sorted(months, reverse=True)
    if ordered:
        lead = (
            "Tracked changes by month of announcement, newest first: "
            f"{counted(len(cards), 'tracked change')} in {counted(len(ordered), 'month')}, "
            f"{month_title(ordered[-1])} → {month_title(ordered[0])}."
        )
    else:
        lead = "No changes archived yet."
    sections = []
    for year in sorted({month[:4] for month in ordered}, reverse=True):
        lines = [
            f"- {archive_month_link(month)} · {plural(len(months[month]), 'change')} "
            f"({product_breakdown(months[month])})"
            for month in ordered
            if month.startswith(year)
        ]
        sections.append(f"### {year}\n\n" + "\n".join(lines))
    regions = {
        "header": lead,
        "months": "\n\n".join(sections) or "No months archived yet.",
    }
    fields = {
        "tags": ["archive"],
        "title": "Archive",
        "description": cap_text(
            "Every tracked change by month of announcement, with the number of changes per "
            "product in each month."
        ),
        "publication": aggregate_publication(cards),
    }
    fields.update(aggregate_dates(cards))
    fields["machine_hash"] = machine_hash(fields, regions)
    body = (
        f"{machine_region('header', regions['header'])}\n\n"
        f"{machine_region('months', regions['months'])}\n"
    )
    return render_frontmatter(fields, body)


def remove_stale_archive_months(
    directory: Path,
    months: set[str],
    conflicts: list[dict[str, str]],
    migration_pending: list[dict[str, str]],
) -> list[str]:
    """Delete ``YYYY-MM.md`` month pages whose month has no active card any more.

    The staged deletion reaches the Vault through the transaction like any other change.
    A page with an edited machine region is a conflict; one with human text outside the
    regions is kept and reported as pending manual migration. Other files are left alone.
    """
    removed: list[str] = []
    if not directory.exists():
        return removed
    for path in sorted(directory.glob("*.md")):
        if path.stem in months or not ARCHIVE_MONTH_RE.match(path.stem):
            continue
        existing = path.read_text(encoding="utf-8")
        post = frontmatter.loads(existing)
        stored_hash = post.metadata.get("machine_hash")
        if stored_hash and content_machine_hash(existing) != stored_hash:
            conflicts.append({
                "file": str(path),
                "error": "machine_hash mismatch while removing an empty archive month",
                "merge_conflict": True,
            })
            continue
        if legacy_residue(post.content, "archive"):
            migration_pending.append({"file": str(path), "reason": ARCHIVE_KEPT_REASON})
            continue
        path.unlink()
        removed.append(path.stem)
    return removed


def change_card_paths(
    root: Path,
    cards: list[dict[str, Any]],
) -> tuple[dict[str, Path], list[dict[str, str]]]:
    existing: dict[str, Path] = {}
    duplicates: list[dict[str, str]] = []
    changes_root = root / "Changes"
    if changes_root.exists():
        for path in sorted(changes_root.rglob("*.md")):
            card_id = frontmatter.load(path).metadata.get("card_id")
            if not card_id:
                continue
            card_id = str(card_id)
            if card_id in existing:
                duplicates.append(
                    {
                        "file": str(path),
                        "error": f"duplicate card_id also found at {existing[card_id]}",
                        "merge_conflict": True,
                    }
                )
                continue
            existing[card_id] = path

    targets = dict(existing)
    used_paths = {path: card_id for card_id, path in existing.items()}
    for card in cards:
        card_id = card["card_id"]
        if card_id in existing:
            continue

        default_path = (
            root
            / "Changes"
            / card["product_name"]
            / f"{card['date']}-{card['slug']}.md"
        )
        target = default_path
        if target in used_paths:
            stable_suffix = card_id.rsplit("-", 1)[-1]
            target = default_path.with_name(
                f"{default_path.stem}-{stable_suffix}{default_path.suffix}"
            )
        if target in used_paths:
            target = default_path.with_name(
                f"{default_path.stem}-{slugify(card_id)}{default_path.suffix}"
            )

        targets[card_id] = target
        used_paths[target] = card_id
    return targets, duplicates


def release_page_paths(
    root: Path,
    releases: list[dict[str, Any]],
) -> tuple[dict[str, Path], list[dict[str, str]]]:
    existing: dict[str, Path] = {}
    duplicates: list[dict[str, str]] = []
    releases_root = root / "Releases"
    if releases_root.exists():
        for path in sorted(releases_root.rglob("*.md")):
            release_id = frontmatter.load(path).metadata.get("release_id")
            if not release_id:
                continue
            release_id = str(release_id)
            if release_id in existing:
                duplicates.append(
                    {
                        "file": str(path),
                        "error": f"duplicate release_id also found at {existing[release_id]}",
                        "merge_conflict": True,
                    }
                )
                continue
            existing[release_id] = path

    targets = dict(existing)
    for release in releases:
        default_path = (
            root
            / "Releases"
            / release["product_name"]
            / (
                f"{release['date']}-{release['release_id']}.md"
                if release.get("source_type") == "fixture"
                else f"{release['release_id']}.md"
            )
        )
        targets[release["release_id"]] = existing.get(
            release["release_id"],
            default_path,
        )
    return targets, duplicates


def reconcile_missing_change_cards(
    root: Path,
    active_card_ids: set[str],
    reconcile_products: set[str],
    conflicts: list[dict[str, str]],
) -> list[str]:
    superseded = []
    changes_root = root / "Changes"
    if not changes_root.exists():
        return superseded

    for path in sorted(changes_root.rglob("*.md")):
        existing = path.read_text(encoding="utf-8")
        post = frontmatter.loads(existing)
        card_id = str(post.metadata.get("card_id", ""))
        product = str(post.metadata.get("product", ""))
        if (
            not card_id
            or card_id in active_card_ids
            or product not in reconcile_products
            or post.metadata.get("superseded") is True
        ):
            continue

        stored_hash = post.metadata.get("machine_hash")
        if stored_hash and content_machine_hash(existing) != stored_hash:
            conflicts.append(
                {
                    "file": str(path),
                    "error": "machine_hash mismatch while marking card superseded",
                    "merge_conflict": True,
                }
            )
            continue

        metadata = dict(post.metadata)
        metadata["superseded"] = True
        regions = extract_machine_regions(post.content)
        metadata["machine_hash"] = machine_hash(machine_fields(metadata), regions)
        write_text(path, render_frontmatter(metadata, post.content))
        superseded.append(card_id)
    return superseded


def reconcile_missing_releases(
    root: Path,
    active_release_ids: set[str],
    reconcile_products: set[str],
    conflicts: list[dict[str, str]],
) -> list[str]:
    superseded = []
    releases_root = root / "Releases"
    if not releases_root.exists():
        return superseded

    for path in sorted(releases_root.rglob("*.md")):
        existing = path.read_text(encoding="utf-8")
        post = frontmatter.loads(existing)
        release_id = str(post.metadata.get("release_id", ""))
        product = str(post.metadata.get("product", "")) or slugify(
            str(post.metadata.get("product_name", path.parent.name))
        )
        if (
            (release_id and release_id in active_release_ids)
            or product not in reconcile_products
            or post.metadata.get("superseded") is True
        ):
            continue

        stored_hash = post.metadata.get("machine_hash")
        if stored_hash and content_machine_hash(existing) != stored_hash:
            conflicts.append(
                {
                    "file": str(path),
                    "error": "machine_hash mismatch while marking release superseded",
                    "merge_conflict": True,
                }
            )
            continue

        metadata = dict(post.metadata)
        metadata["superseded"] = True
        regions = extract_machine_regions(post.content)
        metadata["machine_hash"] = machine_hash(machine_fields(metadata), regions)
        write_text(path, render_frontmatter(metadata, post.content))
        superseded.append(release_id or path.stem)
    return superseded


def nearby_cards(
    theme_cards: list[dict[str, Any]],
) -> dict[str, tuple[dict[str, Any] | None, dict[str, Any] | None]]:
    """Earlier and later card of one theme for each card, across products.

    Cards are ordered by ``(date, product_name, card_id)``. Cards of the same release
    are skipped in both directions, since "Also in this release" already lists them.
    """
    ordered = sorted(
        theme_cards, key=lambda item: (item["date"], item["product_name"], item["card_id"])
    )

    def closest(index: int, step: int) -> dict[str, Any] | None:
        release = ordered[index]["source_release"]
        index += step
        while 0 <= index < len(ordered):
            if ordered[index]["source_release"] != release:
                return ordered[index]
            index += step
        return None

    return {
        card["card_id"]: (closest(index, -1), closest(index, 1))
        for index, card in enumerate(ordered)
    }


def relative_wiki_target(root: Path, path: Path) -> str:
    return path.relative_to(root).with_suffix("").as_posix()


def write_run(
    run_id: str,
    root: Path = ROOT,
    reconcile: bool = False,
    reconcile_products: set[str] | None = None,
    config_root: Path | None = None,
) -> list[dict[str, str]]:
    """Render every page of a run into ``root``.

    ``config_root`` holds ``_scripts/themes.yaml`` and ``_scripts/sources.yaml`` (the
    pipeline renders into a staging copy without them); it defaults to ``root``.
    """
    paths = PipelinePaths(run_id, root=root)
    ensure_vault_dirs(paths.root)
    config = config_root or root
    themes_path = config / "_scripts" / "themes.yaml"
    theme_labels = load_theme_labels(themes_path)
    vocabulary = load_theme_vocabulary(themes_path) if themes_path.exists() else {}
    repository = str(load_site(config / "_scripts" / "sources.yaml").get("repository") or "")
    migration_pending: list[dict[str, str]] = []
    valid_payload = read_json(paths.valid_cards)
    cards = valid_payload["change_cards"]
    pending_theme_review = valid_payload.get("pending_theme_review", [])
    analysis_a = read_json(paths.analyze_a)
    analysis_b = read_json(paths.analyze_b)
    silence = read_json(paths.silence) if paths.silence.exists() else {"alerts": []}
    collected = read_json(paths.collected)
    collected_releases = [
        {**release, "cards": []} for release in collected.get("releases", [])
    ]
    card_paths, conflicts = change_card_paths(paths.root, cards)
    release_paths, release_path_conflicts = release_page_paths(
        paths.root,
        collected_releases,
    )
    conflicts.extend(release_path_conflicts)
    card_targets = {
        card_id: relative_wiki_target(paths.root, path)
        for card_id, path in card_paths.items()
    }
    release_targets = {
        release_id: relative_wiki_target(paths.root, path)
        for release_id, path in release_paths.items()
    }

    cards_by_product: dict[str, list[dict[str, Any]]] = defaultdict(list)
    cards_by_theme: dict[str, list[dict[str, Any]]] = defaultdict(list)
    releases_by_product: dict[str, list[dict[str, Any]]] = defaultdict(list)
    releases_by_id: dict[str, dict[str, Any]] = {}

    for release in collected_releases:
        release_id = release["release_id"]
        if release_id in releases_by_id:
            conflicts.append(
                {
                    "file": str(paths.collected),
                    "error": f"duplicate collected release_id: {release_id}",
                    "merge_conflict": True,
                }
            )
            continue
        releases_by_id[release_id] = release
        releases_by_product[release["product"]].append(release)

    for card in cards:
        cards_by_product[card["product"]].append(card)
        cards_by_theme[card["theme"]].append(card)
        release = releases_by_id.get(card["source_release"])
        if release is None:
            conflicts.append(
                {
                    "file": str(paths.valid_cards),
                    "error": (
                        f"card {card['card_id']} references missing release "
                        f"{card['source_release']}"
                    ),
                    "merge_conflict": True,
                }
            )
            continue
        release["cards"].append(card)

    cards_by_id = {card["card_id"]: card for card in cards}
    theme_neighbours: dict[str, tuple[dict[str, Any] | None, dict[str, Any] | None]] = {}
    for theme, theme_cards in cards_by_theme.items():
        if theme not in HOLDING_THEMES:
            theme_neighbours.update(nearby_cards(theme_cards))

    for card in cards:
        if card["source_release"] not in release_paths:
            continue
        release = releases_by_id.get(card["source_release"])
        earlier, later = theme_neighbours.get(card["card_id"], (None, None))
        patch_a = {
            "evolves_from": analysis_a.get("evolves_from", {}).get(card["card_id"], [])
        }
        patch_b = analysis_b.get("cards", {}).get(card["card_id"], {})
        release_target = relative_wiki_target(
            paths.root,
            release_paths[card["source_release"]],
        )
        write_markdown_file(
            card_paths[card["card_id"]],
            render_change_markdown(
                card,
                patch_a,
                patch_b,
                card_targets=card_targets,
                release_target=release_target,
                release_title=release["title"] if release else None,
                cards_by_id=cards_by_id,
                siblings=release["cards"] if release else [],
                earlier=earlier,
                later=later,
                theme_labels=theme_labels,
                repository=repository,
            ),
            conflicts,
            migration_pending,
        )

    products_info = dict(analysis_a.get("products", {}))
    for product, product_releases in releases_by_product.items():
        if product in products_info:
            continue
        ordered_releases = sorted(
            product_releases,
            key=lambda release: (release["date"], release["release_id"]),
        )
        products_info[product] = {
            "product_name": ordered_releases[0]["product_name"],
            "verbosity_baseline": 0.0,
            "top_themes": [],
            "eras": [
                {
                    "name": "Official Release Archive",
                    "from": ordered_releases[0]["date"],
                    "to": None,
                    "summary": (
                        f"{len(ordered_releases)} official releases are archived; "
                        "no publishable change cards were extracted."
                    ),
                    "data_sparse": len(ordered_releases) < 3,
                }
            ],
        }
    analysis_for_render = {**analysis_a, "products": products_info}

    for product, product_info in products_info.items():
        target = paths.root / "Products" / f"{product_info['product_name']}.md"
        write_markdown_file(
            target,
            render_product_markdown(
                product,
                product_info,
                cards_by_product[product],
                card_targets,
                releases=releases_by_product[product],
                release_targets=release_targets,
                theme_labels=theme_labels,
                cadence=silence.get("cadence", {}).get(product),
            ),
            conflicts,
            migration_pending,
        )

    pending_lines: Counter = Counter()
    for card in pending_theme_review:
        pending_lines[card["source_release"]] += len(card.get("evidence") or [None])
    for release in collected_releases:
        write_markdown_file(
            release_paths[release["release_id"]],
            render_release_markdown(
                release,
                card_targets,
                theme_labels,
                pending_lines=pending_lines[release["release_id"]],
            ),
            conflicts,
            migration_pending,
        )

    # A complete reconciliation may retire the last card in a theme. Refresh that
    # existing aggregate too, preserving its human-owned sections and stable URL.
    if reconcile:
        managed_names = {info["product_name"] for info in products_info.values()}
        for path in (paths.root / "Themes").glob("*.md"):
            post = frontmatter.load(path)
            if (
                managed_names.intersection(post.get("products_involved", []))
                and post.get("theme")
                and post["theme"] not in HOLDING_THEMES
            ):
                cards_by_theme.setdefault(post["theme"], [])
    verbosity = {
        info["product_name"]: info.get("verbosity_baseline") for info in products_info.values()
    }
    key_moments = analysis_b.get("key_moments", {})
    for theme, theme_cards in cards_by_theme.items():
        # A holding theme ("Other changes") has no theme page.
        if theme in HOLDING_THEMES:
            continue
        target = paths.root / "Themes" / f"{theme}.md"
        write_markdown_file(
            target,
            render_theme_markdown(
                theme,
                theme_cards,
                card_targets,
                analysis_b.get("editorial", {}).get(theme, ""),
                theme_labels=theme_labels,
                verbosity=verbosity,
                key_moments=key_moments.get(theme),
            ),
            conflicts,
            migration_pending,
        )

    # Monthly archive: one page per month with an active card, regenerated every run;
    # a month left without cards (after a reconcile) loses its page.
    months = archive_months(cards)
    ordered_months = sorted(months)
    for index, month in enumerate(ordered_months):
        write_markdown_file(
            paths.root / ARCHIVE_DIRECTORY / f"{month}.md",
            render_archive_month_markdown(
                month,
                months[month],
                card_targets,
                theme_labels,
                previous=ordered_months[index - 1] if index else None,
                following=ordered_months[index + 1] if index + 1 < len(ordered_months) else None,
            ),
            conflicts,
            migration_pending,
        )
    remove_stale_archive_months(
        paths.root / ARCHIVE_DIRECTORY, set(months), conflicts, migration_pending
    )
    write_markdown_file(
        paths.root / ARCHIVE_DIRECTORY / f"{ARCHIVE_INDEX}.md",
        render_archive_markdown(cards),
        conflicts,
        migration_pending,
    )

    for alert in silence.get("alerts", []):
        target = paths.root / "Alerts" / f"{alert['date']}-{alert['product']}-silence.md"
        write_markdown_file(target, render_alert_markdown(alert), conflicts)

    write_markdown_file(
        paths.root / "index.md",
        render_index_markdown(
            cards,
            analysis_for_render,
            analysis_b,
            silence,
            theme_labels=theme_labels,
            releases_by_product=releases_by_product,
            vocabulary=vocabulary,
            card_targets=card_targets,
            release_targets=release_targets,
        ),
        conflicts,
        migration_pending,
    )
    write_markdown_file(
        paths.root / "About.md",
        render_about_markdown(
            cards,
            products_info,
            releases_by_product,
            silence,
            pending_theme_review=len(pending_theme_review),
            repository=repository,
        ),
        conflicts,
    )

    if reconcile:
        reconcile_products = reconcile_products if reconcile_products is not None else {
            str(release["product"]) for release in collected.get("releases", [])
        }
        active_card_ids = {card["card_id"] for card in cards}
        active_card_ids.update(card["card_id"] for card in pending_theme_review)
        reconcile_missing_change_cards(
            paths.root,
            active_card_ids,
            reconcile_products,
            conflicts,
        )
        reconcile_missing_releases(
            paths.root,
            {release["release_id"] for release in collected_releases},
            reconcile_products,
            conflicts,
        )

    conflict_path = paths.root / "_pipeline" / "dlq" / f"{run_id}-writer-conflicts.json"
    if conflicts:
        write_json(conflict_path, {"failed": conflicts})
    else:
        conflict_path.unlink(missing_ok=True)
    # Non-blocking: pages that keep a legacy skeleton because a person wrote in them.
    pending_path = paths.run_dir / "writer-migration-pending.json"
    if migration_pending:
        write_json(pending_path, [
            {**item, "file": Path(item["file"]).relative_to(paths.root).as_posix()}
            for item in migration_pending
        ])
    else:
        pending_path.unlink(missing_ok=True)
    return conflicts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    parser.add_argument("--reconcile", action="store_true")
    args = parser.parse_args()
    conflicts = write_run(args.run_id, reconcile=args.reconcile)
    if conflicts:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
