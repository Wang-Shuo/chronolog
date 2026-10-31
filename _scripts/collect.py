from __future__ import annotations

import argparse
import os
import re
import sys
from collections import Counter
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlsplit

import feedparser
import httpx

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _scripts.common import (
    PipelinePaths,
    parse_date,
    read_json,
    read_yaml,
    release_id_for,
    slugify,
    utc_timestamp,
    write_json,
)


CHATGPT_DATE_FORMATS = ("%B %d, %Y", "%b %d, %Y", "%B %d %Y", "%b %d %Y")
CHATGPT_CODEX_ONLY_RE = re.compile(r"\bcodex\b", re.I)
MARKDOWN_LINK_RE = re.compile(r"!?\[([^\]]+)\]\([^)]*\)")
HTML_TAG_RE = re.compile(r"<[^>]+>")


def load_sources(path: Path) -> list[dict[str, Any]]:
    data = read_yaml(path)
    return [product for product in data["products"] if product.get("enabled", True)]


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def source_summary_for(body: str, title: str, length: int = 320) -> str:
    text = MARKDOWN_LINK_RE.sub(r"\1", body)
    text = HTML_TAG_RE.sub(" ", text)
    candidates = []
    for raw in text.splitlines():
        line = re.sub(r"^(?:#{1,6}\s+|[-*]\s+|\d+[.)]\s+)", "", raw).strip()
        if line and line.casefold() not in {"changelog", "release notes", "what's new"}:
            candidates.append(line)
    summary = normalize_space(candidates[0] if candidates else title)
    if len(summary) <= length:
        return summary
    shortened = summary[: length + 1].rsplit(" ", 1)[0].rstrip(".,;: ")
    return f"{shortened}…"


def normalize_release(
    product: dict[str, Any],
    *,
    release_date: str,
    version: str,
    title: str,
    body: str,
    source_url: str,
    source_type: str,
    identity: str | None = None,
) -> dict[str, Any]:
    stable_identity = identity or version or title or source_url
    return {
        "release_id": release_id_for(product["name"], release_date, stable_identity),
        "product": product["name"],
        "product_name": product["display_name"],
        "date": release_date,
        "version": version or title or "release",
        "title": title or version or "Release",
        "body": body,
        "source_summary": source_summary_for(body, title or version or "Release"),
        "source_url": source_url,
        "source_type": source_type,
    }


def normalize_fixture_release(release: dict[str, Any]) -> dict[str, Any]:
    product = {
        "name": release["product"],
        "display_name": release["product_name"],
    }
    normalized = normalize_release(
        product,
        release_date=release["date"],
        version=release.get("version") or release["title"],
        title=release["title"],
        body=release.get("body", ""),
        source_url=release.get("source_url", ""),
        source_type=release.get("source_type", "fixture"),
        identity=release.get("release_id")
        or release.get("version")
        or release["title"],
    )
    normalized["release_id"] = (
        release.get("release_id")
        or f"{release['product']}-{release['date']}-{slugify(release.get('version') or release['title'])}"
    )
    return {**release, **normalized}


def collect_fixture(fixture_path: Path, output_path: Path) -> dict[str, Any]:
    data = read_json(fixture_path)
    releases = sorted(
        (normalize_fixture_release(release) for release in data["releases"]),
        key=lambda item: (item["product"], item["date"], item["release_id"]),
    )
    payload = {
        "source": "fixture", "releases": releases, "errors": [],
        "mode": "full",
        "sources": [
            source_result(product, [r for r in releases if r["product"] == product],
                          complete=True, coverage="fixture")
            for product in sorted({r["product"] for r in releases})
        ],
    }
    write_json(output_path, payload)
    return payload


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("value must be a positive integer")
    return parsed


def fetch_github_releases(
    product: dict[str, Any],
    limit: int | None,
) -> list[dict[str, Any]]:
    url = f"https://api.github.com/repos/{product['repo']}/releases"
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("CHRONOLOG_GITHUB_READ_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    releases: list[dict[str, Any]] = []
    page = 1
    per_page = 100 if limit is None else min(limit, 100)

    while True:
        response = httpx.get(
            url,
            timeout=30.0,
            headers=headers,
            params={"per_page": per_page, "page": page},
            # Authenticated requests stay on the fixed API endpoint. A renamed
            # repository must be corrected in sources.yaml, not followed with credentials.
            follow_redirects=not bool(token),
        )
        response.raise_for_status()
        items = response.json()
        if not isinstance(items, list):
            raise ValueError(f"GitHub response for {product['name']} is not a release list")

        for item in items:
            published = item.get("published_at") or item.get("created_at")
            if not published:
                raise ValueError(f"GitHub release for {product['name']} is missing a date")
            release_date = parse_date(published).isoformat()
            version = item.get("tag_name") or item.get("name") or "release"
            title = item.get("name") or item.get("tag_name") or "Release"
            body = item.get("body") or ""
            source_url = item.get("html_url") or url
            releases.append(
                normalize_release(
                    product,
                    release_date=release_date,
                    version=version,
                    title=title,
                    body=body,
                    source_url=source_url,
                    source_type="github_releases",
                    identity=f"{version}|github:{item.get('id') or source_url}",
                )
            )
            if limit is not None and len(releases) >= limit:
                return releases

        if len(items) < per_page:
            break
        page += 1
    return releases


def fetch_rss_releases(
    product: dict[str, Any],
    limit: int | None,
) -> list[dict[str, Any]]:
    response = httpx.get(product["url"], timeout=30.0, follow_redirects=True)
    response.raise_for_status()
    feed = feedparser.parse(response.content)
    if getattr(feed, "bozo", False):
        message = f"RSS parse failed for {product['name']}"
        bozo_exception = getattr(feed, "bozo_exception", None)
        if bozo_exception is not None:
            message = f"{message}: {bozo_exception}"
        raise ValueError(message)

    status = getattr(feed, "status", None)
    if status is not None and status >= 400:
        raise ValueError(f"RSS fetch failed for {product['name']}: HTTP {status}")

    releases = []
    entries = feed.entries if limit is None else feed.entries[:limit]
    for entry in entries:
        date_value = getattr(entry, "published", None) or getattr(entry, "updated", None)
        if not date_value:
            raise ValueError(f"RSS entry for {product['name']} is missing published/updated date")
        release_date = parse_date(date_value).isoformat()
        version = getattr(entry, "id", getattr(entry, "title", "release"))
        title = getattr(entry, "title", "Release")
        body = getattr(entry, "summary", "")
        source_url = getattr(entry, "link", product["url"])
        releases.append(
            normalize_release(
                product,
                release_date=release_date,
                version=version,
                title=title,
                body=body,
                source_url=source_url,
                source_type="blog_rss",
                identity=f"{version}|{source_url}",
            )
        )
    return releases


class CursorChangelogParser(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.releases: list[dict[str, str]] = []
        self.pagination_pages: set[int] = set()
        self.current: dict[str, Any] | None = None
        self.prose_depth = 0
        self.capturing_title = False
        self.capturing_label = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        href = values.get("href") or ""
        page_match = re.fullmatch(r"/changelog/page/(\d+)", urlsplit(href).path)
        if page_match:
            self.pagination_pages.add(int(page_match.group(1)))

        if tag == "article" and self.current is None:
            self.current = {
                "date": "",
                "version": "",
                "title_parts": [],
                "body_parts": [],
                "source_url": "",
            }
            return
        if self.current is None:
            return

        classes = set((values.get("class") or "").split())
        if tag == "time" and values.get("datetime"):
            self.current["date"] = str(values["datetime"])
        if (
            tag == "a"
            and href.startswith("/changelog/")
            and "/page/" not in href
            and not self.current["source_url"]
        ):
            self.current["source_url"] = urljoin(self.base_url, href)
        if tag == "h1":
            self.capturing_title = True
        if tag == "span" and "label" in classes:
            self.capturing_label = True
        if tag == "div" and "prose" in classes and self.prose_depth == 0:
            self.prose_depth = 1
        elif tag == "div" and self.prose_depth:
            self.prose_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if self.current is None:
            return
        if self.prose_depth:
            if tag in {"p", "li", "h2", "h3", "h4"}:
                self.current["body_parts"].append("\n")
            if tag == "div":
                self.prose_depth -= 1
        if tag == "h1":
            self.capturing_title = False
        if tag == "span" and self.capturing_label:
            self.capturing_label = False
        if tag == "article":
            self._finish_article()

    def handle_data(self, data: str) -> None:
        if self.current is None:
            return
        if self.capturing_title:
            self.current["title_parts"].append(data)
        if self.capturing_label:
            self.current["version"] += data
        if self.prose_depth:
            self.current["body_parts"].append(data)

    def _finish_article(self) -> None:
        if self.current is None:
            return
        title = normalize_space("".join(self.current["title_parts"]))
        body = "\n".join(
            normalize_space(line)
            for line in "".join(self.current["body_parts"]).splitlines()
            if normalize_space(line)
        )
        if title and self.current["date"] and self.current["source_url"]:
            self.releases.append(
                {
                    "date": self.current["date"],
                    "version": normalize_space(self.current["version"]) or title,
                    "title": title,
                    "body": body,
                    "source_url": self.current["source_url"],
                }
            )
        self.current = None
        self.prose_depth = 0
        self.capturing_title = False
        self.capturing_label = False


def parse_cursor_changelog_page(
    product: dict[str, Any],
    html: str,
) -> tuple[list[dict[str, Any]], set[int]]:
    parser = CursorChangelogParser(product["url"])
    parser.feed(html)
    releases = []
    seen_urls: set[str] = set()
    for item in parser.releases:
        if item["source_url"] in seen_urls:
            continue
        seen_urls.add(item["source_url"])
        release_date = parse_date(item["date"]).isoformat()
        releases.append(
            normalize_release(
                product,
                release_date=release_date,
                version=item["version"],
                title=item["title"],
                body=item["body"],
                source_url=item["source_url"],
                source_type="cursor_changelog",
                identity=f"{item['version']}|{item['source_url']}",
            )
        )
    return releases, parser.pagination_pages


def fetch_cursor_releases(
    product: dict[str, Any],
    limit: int | None,
) -> list[dict[str, Any]]:
    releases: list[dict[str, Any]] = []
    seen_release_ids: set[str] = set()
    page = 1
    while True:
        page_url = product["url"] if page == 1 else urljoin(product["url"], f"/changelog/page/{page}")
        response = httpx.get(page_url, timeout=30.0, follow_redirects=True)
        response.raise_for_status()
        page_releases, pagination_pages = parse_cursor_changelog_page(product, response.text)
        if not page_releases:
            raise ValueError(f"Cursor changelog page {page} contained no release entries")
        for release in page_releases:
            if release["release_id"] in seen_release_ids:
                continue
            seen_release_ids.add(release["release_id"])
            releases.append(release)
            if limit is not None and len(releases) >= limit:
                return releases
        if page + 1 not in pagination_pages:
            break
        page += 1
    return releases


class ArticleBlockParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_article = False
        self.active: dict[str, Any] | None = None
        self.blocks: list[dict[str, str]] = []
        self.ignored_depth = 0

    # DOM void elements do not have an end tag and must not extend a skipped subtree.
    VOID_TAGS = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
                 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "article" and not self.in_article:
            self.in_article = True
            return
        if not self.in_article:
            return
        if self.ignored_depth:
            if tag not in self.VOID_TAGS:
                self.ignored_depth += 1
            return
        # The Help Center injects this support widget inside <article>, after the
        # release body. Its h2 otherwise becomes a release on the final date.
        if 'ai-voice-help-contact' in (dict(attrs).get('class') or '').split():
            self.ignored_depth = 1
            return
        if self.active is not None:
            return
        if tag in {"h1", "h2", "h3", "h4", "p", "li"}:
            values = dict(attrs)
            self.active = {"tag": tag, "id": values.get("id") or "", "parts": []}

    def handle_endtag(self, tag: str) -> None:
        if not self.in_article:
            return
        if self.ignored_depth:
            if tag not in self.VOID_TAGS:
                self.ignored_depth -= 1
            return
        if self.active is not None and tag == self.active["tag"]:
            text = normalize_space("".join(self.active["parts"]))
            if text:
                self.blocks.append(
                    {
                        "tag": self.active["tag"],
                        "id": self.active["id"],
                        "text": text,
                    }
                )
            self.active = None
        if tag == "article":
            self.in_article = False

    def handle_data(self, data: str) -> None:
        if self.active is not None and not self.ignored_depth:
            self.active["parts"].append(data)


def parse_chatgpt_date(value: str) -> str | None:
    normalized = normalize_space(value)
    for date_format in CHATGPT_DATE_FORMATS:
        try:
            return datetime.strptime(normalized, date_format).date().isoformat()
        except ValueError:
            continue
    return None


def entry_body(blocks: list[dict[str, str]]) -> str:
    lines = []
    for block in blocks:
        if block["tag"] in {"h3", "h4"}:
            level = 3 if block["tag"] == "h3" else 4
            lines.append(f"{'#' * level} {block['text']}")
        elif block["tag"] == "li":
            lines.append(f"- {block['text']}")
        elif block["tag"] == "p":
            lines.append(block["text"])
    return "\n".join(lines)


def dated_chatgpt_entries(
    release_date: str,
    blocks: list[dict[str, str]],
) -> list[dict[str, str]]:
    heading_level = next(
        (level for level in (2, 3, 4) if any(block["tag"] == f"h{level}" for block in blocks)),
        None,
    )
    if heading_level is None:
        body = entry_body(blocks)
        if not body:
            return []
        first_sentence = re.split(r"(?<=[.!?])\s+", normalize_space(body), maxsplit=1)[0]
        return [
            {
                "date": release_date,
                "title": first_sentence[:120].rstrip() or "ChatGPT update",
                "anchor": "",
                "body": body,
            }
        ]

    marker = f"h{heading_level}"
    entries: list[dict[str, str]] = []
    preamble: list[dict[str, str]] = []
    current_heading: dict[str, str] | None = None
    current_blocks: list[dict[str, str]] = []
    for block in blocks:
        if block["tag"] == marker:
            if current_heading is not None:
                entries.append(
                    {
                        "date": release_date,
                        "title": current_heading["text"],
                        "anchor": current_heading["id"],
                        "body": entry_body(current_blocks),
                    }
                )
            current_heading = block
            current_blocks = preamble
            preamble = []
        elif current_heading is None:
            preamble.append(block)
        else:
            current_blocks.append(block)
    if current_heading is not None:
        entries.append(
            {
                "date": release_date,
                "title": current_heading["text"],
                "anchor": current_heading["id"],
                "body": entry_body(current_blocks),
            }
        )
    return [entry for entry in entries if entry["title"] and entry["body"]]


def is_chatgpt_entry(title: str) -> bool:
    normalized = title.casefold()
    return "chatgpt" in normalized or not CHATGPT_CODEX_ONLY_RE.search(title)


def parse_chatgpt_changelog(
    product: dict[str, Any],
    html: str,
    limit: int | None,
) -> list[dict[str, Any]]:
    parser = ArticleBlockParser()
    parser.feed(html)
    sections: list[tuple[str, list[dict[str, str]]]] = []
    current_date: str | None = None
    current_blocks: list[dict[str, str]] = []
    for block in parser.blocks:
        parsed_date = parse_chatgpt_date(block["text"]) if block["tag"] == "h1" else None
        if parsed_date:
            if current_date is not None:
                sections.append((current_date, current_blocks))
            current_date = parsed_date
            current_blocks = []
        elif current_date is not None:
            current_blocks.append(block)
    if current_date is not None:
        sections.append((current_date, current_blocks))

    raw_entries = [
        entry
        for release_date, blocks in sections
        for entry in dated_chatgpt_entries(release_date, blocks)
        if is_chatgpt_entry(entry["title"])
    ]
    raw_entries.sort(key=lambda entry: entry["date"], reverse=True)
    if limit is not None:
        raw_entries = raw_entries[:limit]

    occurrence_counts: Counter[tuple[str, str]] = Counter()
    releases = []
    for entry in raw_entries:
        key = (entry["date"], normalize_space(entry["title"]).casefold())
        occurrence_counts[key] += 1
        occurrence = occurrence_counts[key]
        identity = entry["title"] if occurrence == 1 else f"{entry['title']}|{occurrence}"
        anchor = f"#{entry['anchor']}" if entry["anchor"] else ""
        releases.append(
            normalize_release(
                product,
                release_date=entry["date"],
                version=entry["title"],
                title=entry["title"],
                body=entry["body"],
                source_url=f"{product['url']}{anchor}",
                source_type="chatgpt_changelog",
                identity=identity,
            )
        )
    return releases


def fetch_chatgpt_releases(
    product: dict[str, Any],
    limit: int | None,
    snapshot_path: Path | None = None,
) -> list[dict[str, Any]]:
    if snapshot_path is not None:
        html = snapshot_path.read_text(encoding="utf-8")
    else:
        response = httpx.get(
            product["url"],
            timeout=60.0,
            follow_redirects=True,
            headers={
                "Accept": "text/html,application/xhtml+xml",
                "User-Agent": "ChronoLog/0.1 (+official-release-archive)",
            },
        )
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 403:
                raise RuntimeError(
                    "ChatGPT Help Center blocked automated access; provide a browser-rendered "
                    "snapshot with --snapshot chatgpt=/path/to/page.html"
                ) from exc
            raise
        html = response.text
    releases = parse_chatgpt_changelog(product, html, limit)
    if not releases:
        raise ValueError("ChatGPT changelog contained no dated release entries")
    return releases


def parse_snapshot_args(values: list[str]) -> dict[str, Path]:
    snapshots: dict[str, Path] = {}
    for value in values:
        product, separator, raw_path = value.partition("=")
        if not separator or not product.strip() or not raw_path.strip():
            raise argparse.ArgumentTypeError("snapshot must use PRODUCT=/path/to/file")
        path = Path(raw_path).expanduser().resolve()
        if not path.is_file():
            raise argparse.ArgumentTypeError(f"snapshot file does not exist: {path}")
        snapshots[product.strip().casefold()] = path
    return snapshots


def source_result(
    product: str, releases: list[dict[str, Any]], *, complete: bool,
    coverage: str, error: str | None = None,
) -> dict[str, Any]:
    dates = sorted(r["date"] for r in releases)
    return {
        "product": product, "status": "failed" if error else "success",
        "collected_at": utc_timestamp(), "complete": complete and not error,
        "coverage": coverage, "count": len(releases),
        "earliest": dates[0] if dates else None,
        "latest": dates[-1] if dates else None, "error": error,
    }


def collect_live(
    sources_path: Path,
    output_path: Path,
    limit: int | None,
    backfill: str | None = None,
    snapshot_paths: dict[str, Path] | None = None,
) -> dict[str, Any]:
    releases: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    results: list[dict[str, Any]] = []
    products = load_sources(sources_path)
    if backfill and backfill != "all":
        requested = {item.strip().casefold() for item in backfill.split(",") if item.strip()}
        products = [
            product
            for product in products
            if product["name"].casefold() in requested
            or product["display_name"].casefold() in requested
        ]
        matched = {
            value
            for product in products
            for value in (product["name"].casefold(), product["display_name"].casefold())
        }
        missing = sorted(requested - matched)
        if missing:
            payload = {
                "source": "live",
                "releases": [],
                "errors": [
                    {"product": name, "error": f"unknown product: {name}"} for name in missing
                ],
                "mode": "full",
                "sources": [source_result(name, [], complete=False, coverage="unknown",
                                          error=f"unknown product: {name}")
                            for name in missing],
            }
            write_json(output_path, payload)
            return payload

    snapshots = snapshot_paths or {}
    for product in products:
        coverage = "feed-window" if product["feed_type"] == "blog_rss" else "available-endpoint"
        complete = bool(backfill) and limit is None and coverage != "feed-window"
        try:
            if product["feed_type"] == "github_releases":
                product_releases = fetch_github_releases(product, limit)
            elif product["feed_type"] == "blog_rss":
                product_releases = fetch_rss_releases(product, limit)
            elif product["feed_type"] == "cursor_changelog":
                product_releases = fetch_cursor_releases(product, limit)
            elif product["feed_type"] == "chatgpt_changelog":
                product_releases = fetch_chatgpt_releases(
                    product,
                    limit,
                    snapshot_path=snapshots.get(product["name"].casefold()),
                )
            else:
                raise ValueError(f"unsupported feed_type: {product['feed_type']}")
            release_ids = [release["release_id"] for release in product_releases]
            if len(release_ids) != len(set(release_ids)):
                raise ValueError(f"duplicate release_id for {product['name']}")
            if not product_releases:
                raise ValueError("unexpected empty source response; completeness cannot be established")
            releases.extend(product_releases)
            result = source_result(product["name"], product_releases, complete=complete,
                                   coverage=coverage)
            result["url"] = product.get("url") or f"https://api.github.com/repos/{product.get('repo')}/releases"
            result["acquisition"] = "http"
            result["acquired_at"] = result["collected_at"]
            if product["name"] in snapshots:
                snapshot = snapshots[product["name"]]
                result["acquisition"] = "browser-snapshot"
                result["acquired_at"] = "unknown"  # mtime is not proof of acquisition
                result["snapshot"] = str(snapshot)
                result["snapshot_mtime"] = datetime.fromtimestamp(
                    snapshot.stat().st_mtime).astimezone().isoformat()
            results.append(result)
        except Exception as exc:
            errors.append({"product": product["name"], "error": str(exc)})
            results.append(source_result(product["name"], [], complete=False,
                                         coverage=coverage, error=str(exc)))
    payload = {
        "source": "live",
        "releases": sorted(
            releases,
            key=lambda item: (item["date"], item["product"], item["release_id"]),
        ),
        "errors": errors,
        "mode": "full" if backfill else "incremental",
        "sources": results,
    }
    write_json(output_path, payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    parser.add_argument("--fixture", action="store_true")
    parser.add_argument("--backfill", nargs="?", const="all")
    parser.add_argument("--limit", type=positive_int)
    parser.add_argument(
        "--snapshot",
        action="append",
        default=[],
        metavar="PRODUCT=PATH",
        help="Use a browser-rendered official page snapshot for a blocked source.",
    )
    args = parser.parse_args()
    paths = PipelinePaths(args.run_id)
    if args.fixture:
        collect_fixture(ROOT / "tests/fixtures/releases.json", paths.collected)
    else:
        limit = args.limit if args.limit is not None else None if args.backfill else 30
        try:
            snapshots = parse_snapshot_args(args.snapshot)
        except argparse.ArgumentTypeError as exc:
            parser.error(str(exc))
        payload = collect_live(
            ROOT / "_scripts/sources.yaml",
            paths.collected,
            limit,
            backfill=args.backfill,
            snapshot_paths=snapshots,
        )
        if payload.get("errors"):
            raise SystemExit(1)


if __name__ == "__main__":
    main()
