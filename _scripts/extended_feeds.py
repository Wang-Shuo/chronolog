"""Official dated histories for workspace, video and additional coding products.

Each collector exhausts the configured public archive. Missing dates, repeated
pages or a changed entry schema fail collection instead of reconciling a partial
history. Scope limitations (such as undated featured posts) live in the catalog.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import re
from urllib.parse import urlsplit

from bs4 import BeautifulSoup

from _scripts.product_feeds import (
    body_from_blocks, clean_markdown, get_text, html_blocks, ordered, plain, release,
)
from _scripts.trending_feeds import fetch_canny, official_url, publication_date


FEED_TYPES = {"canny_changelog", "heygen_changelog", "synthesia_changelog",
              "notion_changelog", "qoder_changelog", "kimi_code_changelog",
              "m365_copilot_changelog", "zai_changelog"}


def next_page(product: dict, links: list, pattern: str) -> str | None:
    if len(links) > 1:
        raise ValueError("Official archive has ambiguous pagination")
    if not links:
        return None
    url = official_url(product["url"], links[0]["href"])
    parts = urlsplit(url)
    path = parts.path + ("?" + parts.query if parts.query else "")
    if not re.fullmatch(pattern, path):
        raise ValueError("Official archive has an unexpected pagination URL")
    return url


def fetch_pages(product: dict, parser, limit: int | None) -> list[dict]:
    url, seen, identities, rows = product["url"], set(), set(), []
    while url:
        if url in seen or len(seen) >= 1000:
            raise ValueError("Official archive pagination did not terminate")
        seen.add(url)
        entries, url = parser(product, get_text(url))
        for entry in entries:
            identity = entry.get("release_id", entry.get("url"))
            if not identity or identity in identities:
                raise ValueError("Official archive repeated an entry across pages")
            identities.add(identity)
        if not entries:
            raise ValueError("Official archive returned an empty page")
        rows.extend(entries)
        if limit is not None and len(rows) >= limit:
            break
    return rows


def parse_synthesia(product: dict, html: str) -> tuple[list[dict], str | None]:
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for card in soup.select(".w-dyn-item:has(h2)"):
        # Featured hero announcements have no publication dates. They are a
        # separate list, explicitly outside this dated-index source's scope.
        if card.has_attr("hero-update"):
            continue
        title, summary = card.find("h2"), card.select_one("p.paragraph-small")
        time, link = card.select_one("p.caption-medium"), card.select_one('a[href^="/updates/"]')
        if summary is None or time is None or link is None:
            raise ValueError("Synthesia dated update lacks its summary, date or permalink")
        date = datetime.strptime(plain(time), "%m/%d/%Y").date().isoformat()
        url = official_url(product["url"], link["href"])
        rows.append(release(product, date, plain(summary), url, plain(title), url))
    url = next_page(product, soup.select("a.w-pagination-next[href]"), r"/updates\?b5ee831f_page=[1-9]\d*")
    return ordered(rows, None), url


def epoch_date(node) -> str:
    value = plain(node) if node else ""
    if not re.fullmatch(r"\d{13}", value):
        raise ValueError("HeyGen entry has no valid publication timestamp")
    return datetime.fromtimestamp(int(value) / 1000, tz=timezone.utc).date().isoformat()


def heygen_index(product: dict, html: str) -> tuple[list[dict], str | None]:
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for card in soup.select("article.listing-post"):
        link, title = card.find_parent("a", href=True), card.find("h1")
        if link is None or title is None:
            raise ValueError("HeyGen index entry has no title or permalink")
        url = official_url(product["url"], link["href"])
        if not urlsplit(url).path.startswith("/publications/"):
            raise ValueError("HeyGen index link is not a public update")
        rows.append({"url": url, "date": epoch_date(card.select_one(".publication-time")), "title": plain(title)})
    links = [a for a in soup.select("a[href]") if plain(a) == "Older"]
    url = next_page(product, links, r"/?\?after=[A-Za-z0-9_%=-]+")
    return rows, url


def parse_heygen(product: dict, entry: dict, html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    post = soup.select_one("article.post")
    title = post.select_one(".post-header h1") if post else None
    body = post.select_one("section.post-content") if post else None
    if title is None or body is None:
        raise ValueError("HeyGen public update is missing its title or body")
    date = epoch_date(post.select_one(".publication-time"))
    if date != entry["date"] or plain(title) != entry["title"]:
        raise ValueError("HeyGen update disagrees with its index metadata")
    return release(product, date, body_from_blocks(html_blocks(body), bold_headings=True),
                   entry["url"], plain(title), entry["url"])


def parse_notion(product: dict, html: str) -> tuple[list[dict], str | None]:
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for card in soup.select("article:has(time)"):
        time, title, body = card.find("time"), card.find("h2"), card.find("article")
        link = title.find_parent("a", href=True) if title else None
        if body is None or link is None:
            raise ValueError("Notion update is missing its title, permalink or body")
        date = publication_date(time.get("datetime") or plain(time))
        url = official_url(product["url"], link["href"])
        if not re.fullmatch(r"/releases/[^/]+", urlsplit(url).path):
            raise ValueError("Notion release has an unexpected permalink")
        for ignored in body.select('[hidden], [role="alert"], figure, iframe, video'):
            ignored.decompose()
        # Notion uses line breaks for individual feature/roadmap paragraphs.
        # Keep those boundaries so an announced future feature cannot attach to
        # the preceding shipped feature during extraction.
        for paragraph in body.find_all("p"):
            if (paragraph.find("br") and not paragraph.find_parent("li")
                    and not re.search(r"\bcoming soon\b", plain(paragraph), re.I)):
                for br in paragraph.find_all("br"):
                    br.replace_with("\n")
                for line in paragraph.get_text().splitlines():
                    if line.strip():
                        item = soup.new_tag("p")
                        item.string = line.strip().removeprefix("→ ")
                        paragraph.insert_before(item)
                paragraph.decompose()
        rows.append(release(product, date, body_from_blocks(html_blocks(body)), url, plain(title), url))
    links = [a for a in soup.select("a[href]") if plain(a) == "Next page"]
    return ordered(rows, None), next_page(product, links, r"/releases/page/[1-9]\d*")


def parse_qoder(product: dict, markdown: str) -> list[dict]:
    entries = list(re.finditer(r"<Update\b([^>]*)>(.*?)</Update>", markdown, re.S))
    if len(entries) != len(re.findall(r"<Update\b", markdown)):
        raise ValueError("Qoder contains an incomplete release block")
    rows = []
    for entry in entries:
        attrs = dict(re.findall(r'(\w+)="([^"\n]+)"', entry[1]))
        title = attrs.get("description", "")
        version = re.fullmatch(r"Qoder (\d+\.\d+\.\d+)", title)
        if version is None:
            raise ValueError("Qoder release is missing its version")
        date = publication_date(attrs.get("label", ""))
        body = clean_markdown(entry[2], product["url"])
        # MDX's layout indentation is not a Markdown code block.
        body = "\n".join(line[4:] if line.startswith("    ") else line for line in body.splitlines())
        row = release(product, date, body, product["url"] + "#" + version[1], title, version[1])
        row["version"] = version[1]
        rows.append(row)
    return ordered(rows, None)


def parse_kimi_code(product: dict, markdown: str) -> list[dict]:
    headings = list(re.finditer(r"^## (.+)$", markdown, re.M))
    rows = []
    for index, heading in enumerate(headings):
        match = re.fullmatch(r"(\d+\.\d+\.\d+) \((\d{4}-\d{2}-\d{2})\)(?: .+)?", heading[1])
        if match is None:
            # Unreleased drafts are not publication events.
            if heading[1].strip().casefold() == "unreleased":
                continue
            raise ValueError("Kimi Code has an invalid dated version heading")
        version, date = match[1], publication_date(match[2])
        end = headings[index + 1].start() if index + 1 < len(headings) else len(markdown)
        body = clean_markdown(markdown[heading.end():end], product["url"])
        row = release(product, date, body, product["url"], "Kimi Code " + heading[1], version)
        row["version"] = version
        rows.append(row)
    return ordered(rows, None)


def parse_zai(product: dict, markdown: str) -> list[dict]:
    markers = list(re.finditer(r"^\*\*(\d{4}-\d{2}-\d{2})\*\*\s*$", markdown, re.M))
    if len(markers) != len(re.findall(r"^\*\*[^*\n]+\*\*\s*$", markdown, re.M)):
        raise ValueError("Z.ai release has an invalid date boundary")
    rows = []
    for index, marker in enumerate(markers):
        end = markers[index + 1].start() if index + 1 < len(markers) else len(markdown)
        text = clean_markdown(markdown[marker.end():end], product["url"])
        lines = text.splitlines()
        title = lines[0].strip() if lines else ""
        if not title or not re.match(r"GLM[- ]", title):
            raise ValueError("Z.ai model release has no model name")
        date = publication_date(marker[1])
        rows.append(release(product, date, "\n".join(lines[1:]).strip(), product["url"], title, f"{date}|{title}"))
    return ordered(rows, None)


def parse_m365_copilot(product: dict, html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    panel = soup.select_one('section[role="tabpanel"][id="tabpanel_1_all"]')
    if panel is None:
        raise ValueError("Microsoft 365 Copilot all-features tab is missing")
    rows, current, surface = [], None, ""
    for node in panel.children:
        if getattr(node, "name", None) == "h2":
            surface = ""
            current = {"date": publication_date(plain(node)), "anchor": node.get("id"), "lines": []}
            if not current["anchor"]:
                raise ValueError("Microsoft 365 Copilot dated heading has no anchor")
            rows.append(current)
        elif getattr(node, "name", None) == "h3":
            surface = plain(node)
        elif getattr(node, "name", None) == "ul":
            if current is None or not surface:
                raise ValueError("Microsoft 365 Copilot feature lacks its date or app scope")
            previous = node.find_previous_sibling()
            supporting_list = bool(previous and previous.name == "p" and current["lines"])
            for item in node.find_all("li", recursive=False):
                # The first description is the official change summary. Nested
                # setup steps, roadmap IDs and business-impact boilerplate are
                # supporting documentation, not additional product changes.
                paragraphs = item.find_all("p", recursive=False)
                title_node = paragraphs[0] if paragraphs else item
                if not title_node.find("strong") and not plain(title_node).startswith("**"):
                    if supporting_list:
                        continue
                    raise ValueError("Microsoft 365 Copilot feature summary changed format")
                title = plain(title_node).replace("**", "").strip()
                description = ""
                bold = title_node.find("strong")
                if bold:
                    remainder = title.removeprefix(plain(bold)).strip()
                    platform = re.match(r"^(\[[^\]]+\])\s*(.*)$", remainder, re.S)
                    title = plain(bold) + (" " + platform[1] if platform else "")
                    description = platform[2] if platform else remainder
                if not description:
                    descriptions = [p for p in paragraphs[1:] if not plain(p).startswith("Roadmap ID:")]
                    description_node = descriptions[0] if descriptions else node.find_next_sibling()
                    if description_node is None or description_node.name != "p":
                        raise ValueError("Microsoft 365 Copilot feature has no change summary")
                    description = plain(description_node)
                if not description or description.startswith("Details:"):
                    raise ValueError("Microsoft 365 Copilot feature has no change summary")
                current["lines"].append(f"### {title} ({surface})\n\n{description}")
                supporting_list = True
    return ordered([release(product, r["date"], "\n\n".join(r["lines"]),
                            product["url"] + "#" + r["anchor"]) for r in rows], None)


def fetch_extended_releases(product: dict, limit: int | None) -> list[dict]:
    kind = product["feed_type"]
    if kind == "canny_changelog":
        return fetch_canny(product, limit)
    if kind in {"synthesia_changelog", "notion_changelog"}:
        parser = parse_synthesia if kind == "synthesia_changelog" else parse_notion
        return ordered(fetch_pages(product, parser, limit), limit)
    if kind == "heygen_changelog":
        entries = fetch_pages(product, heygen_index, limit)
        with ThreadPoolExecutor(max_workers=4) as pool:
            rows = list(pool.map(lambda entry: parse_heygen(product, entry, get_text(entry["url"])), entries))
        return ordered(rows, limit)
    parser = {"qoder_changelog": parse_qoder, "kimi_code_changelog": parse_kimi_code,
              "m365_copilot_changelog": parse_m365_copilot, "zai_changelog": parse_zai}.get(kind)
    if parser is None:
        raise ValueError(f"Unsupported extended product feed: {kind}")
    return ordered(parser(product, get_text(product.get("markdown_url", product["url"]))), limit)
