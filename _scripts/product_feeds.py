"""Official app changelogs with dated HTML or indexed Markdown histories.

Only the configured first-party endpoints are fetched. A changed format, missing
date or failed archive entry fails the source rather than publishing a partial
history as a successful full backfill.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import re
from urllib.parse import urljoin, urlsplit
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup, Tag
import httpx

from _scripts.collect import normalize_release, normalize_space, source_summary_for


HTML_FEEDS = {"claude_changelog", "gemini_changelog", "deepseek_changelog", "v0_changelog"}
FEED_TYPES = HTML_FEEDS | {"lovable_changelog", "elevenlabs_changelog", "replit_changelog"}
DATE_FORMATS = ("%B %d, %Y", "%b %d, %Y", "%Y.%m.%d", "%Y-%m-%d")
INVISIBLE = re.compile(r"[\u200b-\u200d\ufeff]")


def dated(value: str) -> str | None:
    value = INVISIBLE.sub("", value).strip().removeprefix("Date: ")
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(value, fmt).date().isoformat()
        except ValueError:
            pass
    return None


def get_text(url: str) -> str:
    response = httpx.get(url, timeout=45.0, follow_redirects=True)
    response.raise_for_status()
    return response.text


def plain(node: Tag) -> str:
    return normalize_space(INVISIBLE.sub("", node.get_text(" ", strip=True)))


def html_blocks(root: Tag) -> list[dict]:
    for ignored in root.select("script, style, nav, footer, button, svg, pre, table, .hash-link"):
        ignored.decompose()
    blocks = []
    contained_list_items = {id(item) for item in root.find_all("li")} | ({id(root)} if root.name == "li" else set())
    for node in root.find_all(["h1", "h2", "h3", "h4", "p", "li"]):
        # A list item already contains its paragraphs; child list items are kept
        # separately so nested lists don't duplicate their parent text.
        if node.name == "p" and id(node.find_parent("li")) in contained_list_items:
            continue
        if node.name == "li":
            clone = BeautifulSoup(str(node), "html.parser").li
            for nested in clone.find_all(["ul", "ol"]):
                nested.decompose()
            text = plain(clone)
        else:
            text = plain(node)
        if not text:
            continue
        bold = node.find(["b", "strong"], recursive=False)
        blocks.append({"tag": node.name, "id": node.get("id", ""), "text": text,
                       "bold_heading": bool(bold and plain(bold) == text)})
    return blocks


def body_from_blocks(blocks: list[dict], *, bold_headings: bool = False) -> str:
    lines = []
    for block in blocks:
        text, tag = block["text"], block["tag"]
        if text.startswith("Note: Refer to our docs for historical release notes"):
            continue
        if tag in {"h1", "h2", "h3", "h4"} or (bold_headings and block["bold_heading"]):
            lines.append("### " + text)
        elif tag == "li":
            lines.append("- " + text)
        else:
            lines.append(text)
    return "\n\n".join(lines).strip()


def release(product: dict, date: str, body: str, source_url: str,
            title: str | None = None, identity: str | None = None) -> dict:
    if not body.strip() or not re.search(r"[A-Za-z]{3}", body):
        raise ValueError(f"{product['name']} {date} has no release notes")
    title = title or f"{product['display_name']} updates — {date}"
    result = normalize_release(product, release_date=date, version=date, title=title,
                               body=body, source_url=source_url,
                               source_type=product["feed_type"], identity=identity or date)
    result["source_summary"] = source_summary_for(re.sub(r"^#{1,6}.*$", "", body, flags=re.M), title)
    return result


def ordered(releases: list[dict], limit: int | None) -> list[dict]:
    if not releases:
        raise ValueError("Official changelog contained no dated release entries")
    ids = [item["release_id"] for item in releases]
    if len(ids) != len(set(ids)):
        raise ValueError("Official changelog contained duplicate dated identities")
    releases.sort(key=lambda item: (item["date"], item["release_id"]), reverse=True)
    return releases if limit is None else releases[:limit]


def parse_html(product: dict, html: str, limit: int | None = None) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    kind = product["feed_type"]
    if kind == "v0_changelog":
        releases = []
        for article in soup.select("article[id]"):
            heading, time = article.find("h2"), article.find("time")
            if not heading or not time or not dated(time.get("datetime", "")):
                raise ValueError("v0 article is missing its heading or publication date")
            title = plain(heading)
            content = article.select_one(".prose")
            if content is None:
                raise ValueError("v0 article is missing its release body")
            releases.append(release(product, dated(time["datetime"]),
                                    body_from_blocks(html_blocks(content)),
                                    product["url"] + "#" + article["id"], title, article["id"]))
        return ordered(releases, limit)

    root = soup.find("main" if kind == "gemini_changelog" else "article")
    if root is None:
        raise ValueError(f"{product['name']} changelog article is missing")
    date_tag = "h3" if kind == "claude_changelog" else "h2"
    blocks = html_blocks(root)
    sections = []
    current = None
    for block in blocks:
        date = dated(block["text"]) if block["tag"] == date_tag else None
        if date:
            current = {"date": date, "anchor": block["id"], "blocks": []}
            sections.append(current)
        elif block["tag"] == date_tag and (
                kind == "claude_changelog" or block["text"].startswith("Date:")
                or re.match(r"^\d{4}[.-]", block["text"])):
            raise ValueError(f"{product['name']} has an invalid publication date: {block['text']}")
        elif current is not None:
            # Claude's month labels are navigation between dated sections.
            if kind == "claude_changelog" and block["tag"] == "h2":
                continue
            current["blocks"].append(block)
    releases = []
    for section in sections:
        body = body_from_blocks(section["blocks"], bold_headings=kind == "claude_changelog")
        anchor = "#" + section["anchor"] if section["anchor"] else ""
        releases.append(release(product, section["date"], body, product["url"] + anchor))
    return ordered(releases, limit)


def clean_markdown(text: str, source_url: str) -> str:
    # Hosting directives, UI widgets and code examples aren't release claims.
    text = re.sub(r"```[^\n]*\n.*?```", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"<(CardGroup|Card|Frame|Video|YoutubeEmbed)\b[^>]*>.*?</\1>", "", text, flags=re.S)
    text = re.sub(r"<(?:img|YoutubeEmbed|Image|Video)\b[^>]*/?>", "", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if (stripped.startswith((">", "import ", "export ", "This documentation is built and hosted"))
                or re.fullmatch(r"[-*] \[[^\]]+\]\(#[^)]*\)", stripped)):
            continue
        # Markdown relative links must stay on the first-party documentation site.
        line = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)",
                      lambda m: f"[{m[1]}]({urljoin(source_url, m[2])})", line)
        lines.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def parse_lovable(product: dict, markdown: str, limit: int | None = None) -> list[dict]:
    markers = list(re.finditer(r"^\*\*([^\n*]+)\*\*\s*$", markdown, re.M))
    # Only top-level bold date lines delimit releases; inline emphasis is content.
    dates = [marker for marker in markers if re.match(r"[A-Za-z]+ \d{1,2}, \d{4}$", marker[1])]
    releases = []
    for index, marker in enumerate(dates):
        date = dated(marker[1])
        if date is None:
            raise ValueError(f"Lovable has an invalid publication date: {marker[1]}")
        end = dates[index + 1].start() if index + 1 < len(dates) else len(markdown)
        body = clean_markdown(markdown[marker.end():end], product["url"])
        releases.append(release(product, date, body, product["url"]))
    return ordered(releases, limit)


def indexed_entries(product: dict, index: str) -> list[tuple[str, str]]:
    host = urlsplit(product["url"]).netloc
    if product["feed_type"] == "elevenlabs_changelog":
        candidates = []
        for label, url in re.findall(r"^[-*] \[([^\]]+)\]\((https://[^)]+)\)", index, re.M):
            if not re.fullmatch(r"/docs/changelog/\d{4}/\d{1,2}/\d{1,2}\.md", urlsplit(url).path):
                continue
            if urlsplit(url).netloc != host:
                raise ValueError("Changelog index points outside the official host")
            date = dated(label)
            parts = urlsplit(url).path.removesuffix(".md").split("/")[-3:]
            path_date = datetime(*map(int, parts)).date().isoformat()
            if date != path_date:
                raise ValueError("Changelog date disagrees with its archive URL")
            candidates.append((date, url))
    else:
        doc = ET.fromstring(index)
        if doc.tag != "{http://www.sitemaps.org/schemas/sitemap/0.9}urlset":
            raise ValueError("Expected a complete Replit URL sitemap")
        candidates = []
        for loc in doc.findall("{*}url/{*}loc"):
            url = loc.text or ""
            path = urlsplit(url).path
            match = re.fullmatch(r"/updates/(\d{4})/(\d{2})/(\d{2})/changelog", path)
            if not match:
                continue
            if urlsplit(url).netloc != host:
                raise ValueError("Changelog sitemap points outside the official host")
            date = datetime(*map(int, match.groups())).date().isoformat()
            candidates.append((date, url + ".md"))
    if not candidates:
        raise ValueError("Official changelog index contained no dated entries")
    if len(candidates) != len(set(candidates)) or len({date for date, _ in candidates}) != len(candidates):
        raise ValueError("Official changelog index contains duplicate dates")
    return sorted(candidates, reverse=True)


def parse_indexed_entry(product: dict, date: str, url: str, markdown: str) -> dict:
    if re.match(r"\s*(?:<!doctype|<html)", markdown, re.I):
        raise ValueError("Expected Markdown release notes, received HTML")
    public_url = url.removesuffix(".md")
    if product["feed_type"] == "replit_changelog":
        title = re.search(r"^# ([^\n]+)$", markdown, re.M)
        if not title or dated(title[1]) != date:
            raise ValueError("Replit release heading disagrees with its indexed date")
        markdown = markdown[title.end():]
    body = clean_markdown(markdown, public_url)
    if product["feed_type"] == "elevenlabs_changelog" and not re.search(r"^#{2,4} ", body, re.M):
        raise ValueError("Indexed release has no feature sections")
    return release(product, date, body, public_url)


def fetch_product_releases(product: dict, limit: int | None) -> list[dict]:
    kind = product["feed_type"]
    if kind in HTML_FEEDS:
        return parse_html(product, get_text(product["url"]), limit)
    if kind == "lovable_changelog":
        return parse_lovable(product, get_text(product["markdown_url"]), limit)
    if kind not in {"elevenlabs_changelog", "replit_changelog"}:
        raise ValueError(f"Unsupported official product feed: {kind}")
    entries = indexed_entries(product, get_text(product["index_url"]))
    if limit is not None:
        entries = entries[:limit]

    def fetch(entry):
        date, url = entry
        try:
            return parse_indexed_entry(product, date, url, get_text(url))
        except Exception as exc:
            raise ValueError(f"Failed official archive entry {url}: {exc}") from exc

    with ThreadPoolExecutor(max_workers=4) as pool:
        return ordered(list(pool.map(fetch, entries)), limit)
