"""Dated official histories for local AI, voice and creative products.

Pagination and platform/year boundaries are part of the source contract. An
incomplete archive must fail instead of authorizing history reconciliation.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import json
import re
from urllib.parse import urlsplit

from bs4 import BeautifulSoup

from _scripts.product_feeds import body_from_blocks, clean_markdown, get_text, html_blocks, ordered, plain, release
from _scripts.trending_feeds import official_url, publication_date


FEED_TYPES = {f"{name}_changelog" for name in (
    "krea", "devin", "raycast", "superwhisper", "wispr_flow", "lmstudio",
)}
MONTHS = r"(?:January|February|March|April|May|June|July|August|September|October|November|December)"
DATE_BOUNDARY = re.compile(r"^\*\*(" + MONTHS + r"[^*\n]*)\*\*[ \t]*$", re.M)


def parse_dated_markdown(product: dict, markdown: str, url: str, year: str | None = None) -> list[dict]:
    # The overview's year navigation and Mintlify footer are not release notes.
    markdown = markdown.split("\n## All Release Notes", 1)[0]
    markdown = markdown.split("\nThis documentation is built and hosted on", 1)[0]
    dates = list(DATE_BOUNDARY.finditer(markdown))
    rows = []
    for index, marker in enumerate(dates):
        date = publication_date(marker[1])
        if year and not date.startswith(year + "-"):
            raise ValueError("Dated release disagrees with its official year archive")
        end = dates[index + 1].start() if index + 1 < len(dates) else len(markdown)
        body = re.sub(r"(?m)^\*{3,}[ \t]*$", "", markdown[marker.end():end]).strip()
        title, identity = None, date
        if product["name"] == "krea":
            lines = body.splitlines()
            title = lines[0].strip() if lines else ""
            if not title or title.startswith(("#", "*", "<")):
                raise ValueError("Krea update has no descriptive title")
            body = "\n".join(lines[1:]).strip()
            identity = f"{date}|{title}"
        else:
            # Devin's bold standalone feature labels are real section headings.
            body = re.sub(r"(?m)^\*\*([^*\n]+)\*\*[:：]?[ \t]*$", r"### \1", body)
        rows.append(release(product, date, clean_markdown(body, url), url, title, identity))
    return ordered(rows, None)


def fetch_devin(product: dict, limit: int | None) -> list[dict]:
    overview = get_text(product["markdown_url"])
    links = re.findall(r"\[\d{4} Release Notes\]\(([^)]+)\)", overview)
    if not links or len(links) != len(set(links)):
        raise ValueError("Devin overview is missing its unique year archive links")
    urls = [official_url(product["url"], link) for link in links]
    if any(not re.fullmatch(r"/release-notes/\d{4}\.md", urlsplit(url).path) for url in urls):
        raise ValueError("Unexpected Devin year archive URL")
    recent_dates = {publication_date(marker[1]) for marker in DATE_BOUNDARY.finditer(overview)}
    if not recent_dates:
        raise ValueError("Devin overview contains no dated updates")
    rows = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        texts = list(pool.map(get_text, urls))
    for url, text in zip(urls, texts):
        year = urlsplit(url).path.rsplit("/", 1)[-1].removesuffix(".md")
        for row in parse_dated_markdown(product, text, url.removesuffix(".md"), year):
            rows.append(row)
    # The overview duplicates the permanent archives and can contain older text.
    # Use annual notes as the content authority, but reject a lagging archive.
    if not recent_dates <= {row["date"] for row in rows}:
        raise ValueError("Devin annual archives are missing a recent overview date")
    return ordered(rows, limit)


def parse_raycast(product: dict, surface: str, html: str) -> tuple[list[dict], str | None]:
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for card in soup.select("article"):
        meta, body = card.select_one('[class*="changelogMeta"]'), card.select_one('[class*="changelogBody"]')
        link = meta.select_one("a[href]") if meta else None
        time = meta.select_one('[class*="changelogDate"]') if meta else None
        if link is None or time is None or body is None:
            raise ValueError("Raycast update is missing its version, date or body")
        version = plain(link).removeprefix("v").strip()
        if not re.fullmatch(r"\d+(?:\.\d+){1,3}", version):
            raise ValueError("Raycast version has an unexpected format")
        url = official_url(product["url"], link["href"])
        if not urlsplit(url).path.startswith("/changelog/"):
            raise ValueError("Raycast entry does not link to an official changelog")
        row = release(product, publication_date(plain(time)), body_from_blocks(html_blocks(body)),
                      url, f"Raycast {surface} {version}", f"{surface}/{version}")
        row["version"] = f"{surface}/{version}"
        rows.append(row)
    links = soup.select('a[title="Next Page"][href]')
    if len(links) > 1:
        raise ValueError("Raycast archive has ambiguous pagination")
    next_url = official_url(product["url"], links[0]["href"]) if links else None
    if next_url and not re.fullmatch(r"/changelog/" + re.escape(surface) + r"/[1-9]\d*", urlsplit(next_url).path):
        raise ValueError("Raycast pagination left its configured platform archive")
    return ordered(rows, None), next_url


def fetch_raycast(product: dict, limit: int | None) -> list[dict]:
    def platform(surface):
        url = product["url"].rstrip("/") + "/" + surface
        seen, identities, rows = set(), set(), []
        while url:
            if url in seen or len(seen) >= 1000:
                raise ValueError("Raycast archive pagination did not terminate")
            seen.add(url)
            page, url = parse_raycast(product, surface, get_text(url))
            for row in page:
                if row["release_id"] in identities:
                    raise ValueError("Raycast repeated a release across archive pages")
                identities.add(row["release_id"])
            rows.extend(page)
            if limit is not None and len(rows) >= limit:
                break
        return rows
    with ThreadPoolExecutor(max_workers=4) as pool:
        pages = list(pool.map(platform, product["surfaces"]))
    return ordered([row for page in pages for row in page], limit)


def parse_superwhisper(product: dict, surface: str, html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    selected = [plain(button) for button in soup.select("button") if "text-trigray-100" in button.get("class", [])]
    labels = {"macos": "macOS", "windows": "Windows", "ios": "iOS", "android": "Android"}
    if selected != [labels[surface]]:
        raise ValueError("Superwhisper returned the wrong platform archive")
    containers = soup.select(".space-y-12")
    if len(containers) != 1 or any(plain(b).casefold() in {"load more", "next"} for b in soup.select("button")):
        raise ValueError("Superwhisper complete archive structure changed")
    rows = []
    for card in containers[0].find_all("div", recursive=False):
        parts = card.find_all("div", recursive=False)
        if len(parts) != 2:
            raise ValueError("Superwhisper entry is missing metadata or notes")
        version_node, time = parts[0].find("p"), parts[0].find("span")
        if version_node is None or time is None:
            raise ValueError("Superwhisper entry has no dated version")
        version = plain(version_node)
        if not re.fullmatch(r"\d+(?:\.\d+){1,3}", version):
            raise ValueError("Superwhisper version has an unexpected format")
        body = parts[1]
        for label in body.find_all(["b", "strong"]):
            if not label.find_parent(["li", "p"]):
                label.name = "h3"
        row = release(product, publication_date(plain(time)), body_from_blocks(html_blocks(body)),
                      product["url"] + "?platform=" + surface,
                      f"Superwhisper {labels[surface]} {version}", f"{surface}/{version}")
        row["version"] = f"{surface}/{version}"
        rows.append(row)
    return ordered(rows, None)


def parse_wispr_flow(product: dict, html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    dates, cards = soup.select(".release-date"), soup.select(".release-item-grid-v2")
    if len(dates) != len(cards) or soup.select(".w-pagination-next"):
        raise ValueError("Wispr Flow dated archive structure or pagination changed")
    labels = {"desktop": "Desktop", "ios": "iOS", "android": "Android", "notetaker": "Notetaker",
              "all-platforms": "All platforms"}
    rows = []
    for card in cards:
        time, anchor = card.select_one(".release-date"), card.find_parent(id=True)
        if time is None or anchor is None:
            raise ValueError("Wispr Flow entry lacks its date or public anchor")
        blocks = []
        for section in card.select("[release-content]"):
            surface = section["release-content"]
            if surface not in labels:
                raise ValueError("Wispr Flow added an unknown platform scope")
            body = section.select_one(".wn_body.w-richtext")
            if body is None:
                raise ValueError("Wispr Flow platform section is missing its release notes")
            parts = html_blocks(body)
            for part in parts:
                if part["tag"] in {"h1", "h2", "h3", "h4"}:
                    part["text"] += f" ({labels[surface]})"
            blocks.extend(parts)
        rows.append(release(product, publication_date(plain(time)), body_from_blocks(blocks),
                            product["url"] + "#" + anchor["id"]))
    return ordered(rows, None)


def fetch_lmstudio(product: dict, limit: int | None) -> list[dict]:
    offset, total, rows, versions = 0, None, [], set()
    for _ in range(1000):
        payload = json.loads(get_text(f"{product['api_url']}?offset={offset}&limit=10"))
        if not isinstance(payload, dict) or payload.get("errorMessage"):
            raise ValueError("LM Studio public changelog API returned an error")
        items, next_offset, count = payload.get("items"), payload.get("nextOffset"), payload.get("totalCount")
        if (not isinstance(items, list) or not items or type(count) is not int or count < 1
                or (next_offset is not None and type(next_offset) is not int)):
            raise ValueError("LM Studio changelog has an invalid pagination response")
        if total is not None and count != total:
            raise ValueError("LM Studio total changed during collection")
        total = count
        for item in items:
            version, body = item.get("version"), item.get("releaseNotesMarkdownText")
            if (not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version)
                    or version in versions or not isinstance(body, str) or type(item.get("build")) is not int):
                raise ValueError("LM Studio repeated or malformed a stable version")
            versions.add(version)
            body = re.sub(r"^#{1,3}\s*[\d.]+\s*-\s*Release Notes\s*", "", body)
            body = re.sub(r"(?m)^\*\*(Build \d+)\*\*[ \t]*$", r"### \1", body)
            url = product["url"].rstrip("/") + "/lmstudio-v" + version
            row = release(product, publication_date(item.get("releaseDateIso", "")),
                          clean_markdown(body, url), url, "LM Studio " + version, version)
            row["version"] = version
            rows.append(row)
        if next_offset is None:
            if len(rows) != total:
                raise ValueError("LM Studio terminal page does not match its reported total")
            return ordered(rows, limit)
        if next_offset != offset + len(items) or next_offset >= total:
            raise ValueError("LM Studio pagination skipped entries or continued past its total")
        if limit is not None and len(rows) >= limit:
            return ordered(rows, limit)
        offset = next_offset
    raise ValueError("LM Studio archive pagination did not terminate")


def fetch_additional_releases(product: dict, limit: int | None) -> list[dict]:
    kind = product["feed_type"]
    if kind == "krea_changelog":
        return ordered(parse_dated_markdown(product, get_text(product["markdown_url"]), product["url"]), limit)
    if kind == "devin_changelog":
        return fetch_devin(product, limit)
    if kind == "raycast_changelog":
        return fetch_raycast(product, limit)
    if kind == "superwhisper_changelog":
        def platform(surface):
            return parse_superwhisper(product, surface, get_text(product["url"] + "?platform=" + surface))
        with ThreadPoolExecutor(max_workers=4) as pool:
            pages = list(pool.map(platform, product["surfaces"]))
        return ordered([row for page in pages for row in page], limit)
    if kind == "wispr_flow_changelog":
        return ordered(parse_wispr_flow(product, get_text(product["url"])), limit)
    if kind == "lmstudio_changelog":
        return fetch_lmstudio(product, limit)
    raise ValueError(f"Unsupported additional product feed: {kind}")
