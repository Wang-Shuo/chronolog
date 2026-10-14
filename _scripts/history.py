"""Rebuild pipeline inputs from the durable Markdown vault, never old run JSON."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

import frontmatter

from _scripts.common import machine_hash, slugify
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
            record = {
                "release_id": meta["release_id"], "product": product,
                "product_name": meta["product_name"], "date": str(meta["date"]),
                "title": meta["source_release"], "version": meta.get("version", ""),
                "source_url": meta["source_url"], "source_type": meta.get("source_type", "unknown"),
                "source_summary": regions.get("summary", "").split("\n\n[Official release notes]")[0],
            }
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
            record.update(date=str(meta["date"]), source_release=source, title=title,
                          slug=slugify(title)[:80].strip("-"), description=regions["description"],
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


def merge_history(
    history: tuple[list[dict], list[dict], list[dict]],
    releases: list[dict], cards: list[dict], pending: list[dict],
    reconcile_products: set[str],
) -> tuple[list[dict], list[dict], list[dict]]:
    old_releases, old_cards, old_pending = history
    accepted_ids = {c["card_id"] for c in cards}
    queue = {c["card_id"]: c for c in old_pending if c["card_id"] not in accepted_ids}
    queue.update({c["card_id"]: c for c in pending})
    protected_releases = {c["source_release"] for c in queue.values()}
    release_map = {r["release_id"]: r for r in old_releases
                   if r["product"] not in reconcile_products or r["release_id"] in protected_releases}
    # Old records are kept for incremental batches, including changed release bodies.
    # Only an explicitly complete reconciliation can retire missing identities.
    card_map = {c["card_id"]: c for c in old_cards
                if c["product"] not in reconcile_products or c["card_id"] in queue}
    release_map.update({r["release_id"]: {k: v for k, v in r.items() if k != "body"} for r in releases})
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
