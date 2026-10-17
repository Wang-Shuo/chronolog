"""Rebuild pipeline inputs from the durable Markdown vault, never old run JSON."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

import frontmatter

from _scripts.common import machine_hash, normalize_text, slugify
from _scripts.extract import BULLET_MARKER_RE, clean_block_text, split_release_lines
from _scripts.validate import normalize_wikilink_target
from _scripts.writer import extract_machine_regions, machine_fields, render_frontmatter, write_markdown_file


def read_history(root: Path, products: set[str]) -> tuple[list[dict], list[dict], list[dict]]:
    releases, cards, pending = [], [], []
    release_targets = {}
    for path in sorted((root / "Releases").rglob("*.md")):
        post = frontmatter.load(path)
        meta = post.metadata
        product = str(meta.get("product") or slugify(str(meta.get("product_name", path.parent.name))))
        if product not in products or meta.get("superseded"):
            continue
        if not meta.get("release_id"):
            raise ValueError(f"historical release missing release_id: {path}")
        record = meta.get("record")
        if not record:
            regions = extract_machine_regions(post.content)
            summary = regions.get("summary", "")
            record = {
                "release_id": meta["release_id"], "product": product,
                "product_name": meta["product_name"], "date": str(meta["date"]),
                "title": meta["source_release"], "version": meta.get("version", ""),
                "source_url": meta["source_url"], "source_type": meta.get("source_type", "unknown"),
                "source_summary": historical_source_summary(summary),
            }
            candidates = re.search(
                r"^Tracked \d+ (?:of|cards? from) (\d+) candidate lines?(?:; [^\n]*)?\.$",
                summary,
                re.M,
            )
            if candidates:
                record["candidate_line_count"] = int(candidates.group(1))
        releases.append(dict(record))
        release_targets[path.relative_to(root).with_suffix("").as_posix()] = record["release_id"]

    for path in sorted((root / "Changes").rglob("*.md")):
        post = frontmatter.load(path)
        meta = post.metadata
        if meta.get("product") not in products or meta.get("superseded"):
            continue
        record = meta.get("record")
        if not record:
            regions = extract_machine_regions(post.content)
            source = str(meta["source_release"])
            if source.startswith("[["):
                source = release_targets.get(normalize_wikilink_target(source[2:-2]), "")
            if not source:
                raise ValueError(f"cannot resolve historical release: {path}")
            evidence = [
                {"quote": quote, "source_release": url}
                for quote, url in re.findall(
                    r"(?ms)^> (.*?)\n>\n> Source: ([^\n]+)(?:\n|$)", regions.get("evidence", "")
                )
            ]
            if not evidence:
                raise ValueError(f"cannot reconstruct historical evidence: {path}")
            title = next((line[2:] for line in post.content.splitlines() if line.startswith("# ")), "")
            record = {key: meta[key] for key in (
                "type", "card_id", "product", "product_name", "theme", "impact", "extractor_version"
            )}
            # Cards rendered since W1 no longer carry a description region.
            description = regions.get("description") or str(meta.get("description") or "")
            record.update(date=str(meta["date"]), source_release=source, title=title,
                          slug=slugify(title)[:80].strip("-"), description=description,
                          evidence=evidence, comparison="")
        cards.append(dict(record))

    for path in sorted((root / "_review").glob("*.md")):
        post = frontmatter.load(path)
        if post.get("product") in products:
            pending.append(dict(post["record"]))
    for records, key in ((releases, "release_id"), (cards, "card_id"), (pending, "card_id")):
        ids = [r[key] for r in records]
        if len(ids) != len(set(ids)):
            raise ValueError(f"duplicate historical {key}")
    return releases, cards, pending


def historical_source_summary(summary: str) -> str:
    """Official summary text of a Release ``summary`` region, without generated lines."""
    text = re.split(r"\n\n(?:\[Official release notes\]|Tracked )", summary, maxsplit=1)[0].strip()
    # A generated fallback is not an official summary; the writer recomputes it.
    if re.match(r"^(?:\d+ tracked changes? across |No change cards extracted\.$)", text):
        return ""
    return text


def without_body(release: dict) -> dict:
    """Drop a release body, keeping its candidate line count for later Release pages."""
    record = {key: value for key, value in release.items() if key != "body"}
    if release.get("body") is not None:
        record["candidate_line_count"] = len(split_release_lines(str(release["body"])))
    return record


def line_key(quote: str) -> str:
    """Comparable form of an evidence line, without list markers or invisible characters."""
    text = clean_block_text(str(quote))
    return normalize_text(BULLET_MARKER_RE.sub("", text, count=1))


def regrouped_lines(cards: list[dict]) -> dict[str, set[str]]:
    """Comparable evidence lines of freshly extracted cards, by source release."""
    lines: dict[str, set[str]] = {}
    for card in cards:
        lines.setdefault(card["source_release"], set()).update(
            line_key(item["quote"]) for item in card.get("evidence", [])
        )
    return lines


def is_regrouped(entry: dict, regrouped: dict[str, set[str]]) -> bool:
    """Whether every line of an old queue entry now sits in a card of its release.

    A changed card definition can move a pending line into a multi-line card (or a new
    queue entry) with another identity; the old entry is then resolved, not kept twice.
    """
    lines = regrouped.get(entry["source_release"])
    quotes = [line_key(item["quote"]) for item in entry.get("evidence", [])]
    return bool(lines and quotes) and all(quote in lines for quote in quotes)


def merge_history(
    history: tuple[list[dict], list[dict], list[dict]],
    releases: list[dict], cards: list[dict], pending: list[dict],
    reconcile_products: set[str],
) -> tuple[list[dict], list[dict], list[dict]]:
    old_releases, old_cards, old_pending = history
    accepted_ids = {c["card_id"] for c in cards}
    regrouped = regrouped_lines(cards + pending)
    # A complete reconciliation re-extracts every collected release of its products, so
    # their earlier queue entries are replaced by this batch's entries, like their cards.
    reextracted = {r["release_id"] for r in releases if r["product"] in reconcile_products}
    queue = {
        c["card_id"]: c for c in old_pending
        if c["card_id"] not in accepted_ids
        and c["source_release"] not in reextracted
        and not is_regrouped(c, regrouped)
    }
    queue.update({c["card_id"]: c for c in pending})
    protected_releases = {c["source_release"] for c in queue.values()}
    release_map = {r["release_id"]: r for r in old_releases
                   if r["product"] not in reconcile_products or r["release_id"] in protected_releases}
    # Old records are kept for incremental batches, including changed release bodies.
    # Only an explicitly complete reconciliation can retire missing identities.
    card_map = {c["card_id"]: c for c in old_cards
                if c["product"] not in reconcile_products or c["card_id"] in queue}
    release_map.update({r["release_id"]: without_body(r) for r in releases})
    card_map.update({c["card_id"]: c for c in cards})
    merged_cards = sorted(card_map.values(), key=lambda c: (c["date"], c["card_id"]))
    merged_releases = sorted(release_map.values(), key=lambda r: (r["date"], r["release_id"]))
    return merged_releases, merged_cards, sorted(queue.values(), key=lambda c: c["card_id"])


def write_pending(root: Path, pending: list[dict[str, Any]], products: set[str]) -> None:
    directory = root / "_review"
    wanted = {f"{card['card_id']}.md" for card in pending}
    for path in directory.glob("*.md"):
        if path.name not in wanted and frontmatter.load(path).get("product") in products:
            resolved = directory / "resolved" / path.name
            resolved.parent.mkdir(parents=True, exist_ok=True)
            if resolved.exists() and resolved.read_bytes() != path.read_bytes():
                suffix = hashlib.sha256(path.read_bytes()).hexdigest()[:12]
                resolved = resolved.with_name(f"{resolved.stem}-{suffix}.md")
            path.replace(resolved)
    for card in pending:
        fields = {"record": card, "product": card["product"], "draft": True}
        fields["machine_hash"] = machine_hash(machine_fields(fields), {})
        wrote = write_markdown_file(directory / f"{card['card_id']}.md", render_frontmatter(
            fields, "Pending theme review. Resolve via the theme vocabulary or review decisions."
        ))
        if not wrote:
            raise ValueError(f"pending review conflict: {card['card_id']}")
