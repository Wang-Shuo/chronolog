"""Complete public histories for creative, meeting and agent products.

Archives are scoped by the catalog, not by a guessed launch date. Pagination must
terminate explicitly; a missing page or changed schema fails the entire source.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import os
import re
from urllib.parse import urljoin, urlsplit
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
import httpx

from _scripts.product_feeds import (
    body_from_blocks, clean_markdown, dated, get_text, html_blocks, ordered, plain, release,
)


FEED_TYPES = {f"{name}_changelog" for name in (
    "suno", "runway", "midjourney", "granola", "antigravity", "gamma", "manus",
    "openclaw", "opencode",
)}
MANUS_API = "https://api.manus.im/notifier.v1.NotificationPublicService/GetPublicUpdateNotifications"


def publication_date(value: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Missing publication date")
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        result = dated(value)
        if result:
            return result
        for fmt in ("%d %b %Y", "%d %B %Y"):
            try:
                return datetime.strptime(value.replace("Sept ", "Sep "), fmt).date().isoformat()
            except ValueError:
                pass
    raise ValueError(f"Invalid publication date: {value}")


def official_url(base: str, href: str) -> str:
    url = urljoin(base, href)
    parts = urlsplit(url)
    if parts.scheme != "https" or parts.netloc != urlsplit(base).netloc:
        raise ValueError("Archive link points outside the official host")
    return url


def post_json(url: str, payload: dict) -> dict:
    response = httpx.post(url, json=payload, timeout=45.0,
                          headers={"Connect-Protocol-Version": "1"})
    response.raise_for_status()
    result = response.json()
    if not isinstance(result, dict):
        raise ValueError("Expected a public changelog JSON object")
    return result


def parse_suno(product: dict, html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    releases = []
    for article in soup.select("article"):
        title, time = article.select_one("h2 a[href]"), article.find("time")
        parts = article.find_all("div", recursive=False)
        if title is None or time is None or len(parts) != 2 or not article.get("id"):
            raise ValueError("Suno entry is missing its title, date, identity or body")
        releases.append(release(product, publication_date(time.get("datetime", "")),
                                body_from_blocks(html_blocks(parts[1])),
                                official_url(product["url"], title["href"]),
                                plain(title), article["id"]))
    return ordered(releases, None)


def parse_runway(product: dict, html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    releases = []
    for heading in soup.select(".rw-h5"):
        row = heading.parent.parent
        time, body = row.select_one(".rw-bodycopy5"), row.select_one(".rw-bodycopy2")
        if time is None or body is None:
            raise ValueError("Runway entry is missing its publication date or description")
        title, date = plain(heading), publication_date(plain(time))
        releases.append(release(product, date, plain(body), product["url"], title,
                                f"{date}|{title}"))
    return ordered(releases, None)


def parse_granola(product: dict, html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    releases = []
    for link in soup.select("a[href]:has(h3)"):
        heading, body = link.find("h3"), link.find("p")
        # The update index includes dates and summaries, while its linked blog
        # articles may mix release information with longer marketing material.
        date = re.search(r"(\d{1,2} [A-Za-z]+ \d{4})$", plain(link))
        if date is None or body is None:
            raise ValueError("Granola update is missing its date or summary")
        url = official_url(product["url"], link["href"])
        releases.append(release(product, publication_date(date[1]), plain(body), url,
                                plain(heading), url))
    return ordered(releases, None)


def parse_antigravity(product: dict, html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    releases = []
    surfaces = product["surfaces"]
    for article in soup.select("article.release-entry"):
        identity = article.get("id", "")
        surface = next((s for s in surfaces if identity.startswith(f"rel-{s}-")
                        and not identity.startswith(f"rel-{s}-model-")), None)
        if surface is None:
            continue
        time, version = article.find("time"), article.select_one(".rn-version-tag[href]")
        card = article.select_one(".rn-card")
        if time is None or version is None or card is None:
            raise ValueError("Antigravity version is missing its date, permalink or notes")
        headline = card.select_one(".rn-headline")
        title = f"{surface.upper()} {plain(version)}"
        if headline:
            title += " — " + plain(headline)
        for summary in card.select("details > summary"):
            heading = soup.new_tag("h3")
            heading.string = summary.parent.get("data-item-title") or plain(summary)
            summary.replace_with(heading)
        item = release(product, publication_date(plain(time)),
                       body_from_blocks(html_blocks(card)),
                       official_url(product["url"], version["href"]), title, identity)
        item["version"] = f"{surface}/{plain(version)}"
        releases.append(item)
    # A removed/renamed surface must not silently reconcile away its history.
    if any(not any(r["version"].startswith(s + "/") for r in releases) for s in surfaces):
        raise ValueError("Antigravity is missing a configured product surface")
    return ordered(releases, None)


def midjourney_urls(product: dict, xml: str) -> list[str]:
    doc = ET.fromstring(xml)
    if doc.tag != "{http://www.sitemaps.org/schemas/sitemap/0.9}urlset":
        raise ValueError("Expected the Midjourney posts sitemap")
    urls = [official_url(product["url"], loc.text or "") for loc in doc.findall("{*}url/{*}loc")]
    if not urls or len(set(urls)) != len(urls):
        raise ValueError("Midjourney sitemap is empty or contains duplicate posts")
    return urls


def parse_midjourney(product: dict, url: str, html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    time = soup.select_one('meta[property="article:published_time"]')
    heading, body = soup.select_one("h1.single-title"), soup.select_one(".single-content.gh-content")
    if time is None or heading is None or body is None:
        raise ValueError(f"Midjourney post lacks publication metadata or content: {url}")
    for paragraph in body.find_all("p"):
        bold = paragraph.find(["strong", "b"], recursive=False)
        if bold:
            prefix = list(bold.previous_siblings)
            if not re.search(r"[A-Za-z0-9]", "".join(str(node) for node in prefix)):
                section = soup.new_tag("h3")
                section.string = plain(bold)
                paragraph.insert_before(section)
                for node in prefix:
                    node.extract()
                bold.decompose()
        if paragraph.contents and isinstance(paragraph.contents[0], str):
            first = paragraph.contents[0]
            first.replace_with(re.sub(r"^(?:hi|hey) everyone[!,.]\s*", "", str(first), flags=re.I))
    return release(product, publication_date(time.get("content", "")),
                   body_from_blocks(html_blocks(body)), url, plain(heading), url)


def fetch_gamma(product: dict, limit: int | None) -> list[dict]:
    previous = []
    for pages in range(1, 1001):
        payload = post_json(product["api_url"], {"pages": pages, "status": ["published"]})
        result = payload.get("result", {})
        entries, more = result.get("entries"), result.get("hasNextPage")
        if not isinstance(entries, list) or not isinstance(more, bool):
            raise ValueError("Gamma public changelog has an invalid pagination response")
        ids = [entry.get("_id") for entry in entries]
        if (not all(ids) or len(set(ids)) != len(ids) or len(ids) <= len(previous)
                or ids[:len(previous)] != previous):
            raise ValueError("Gamma cumulative pages contain duplicate, missing or shifted entries")
        releases = []
        for entry in entries:
            if entry.get("status") != "published" or entry.get("deleted"):
                raise ValueError("Gamma returned an unpublished entry from its public feed")
            if not entry.get("urlName") or not entry.get("title"):
                raise ValueError("Gamma entry has no public permalink or title")
            url = official_url(product["url"] + "/", entry["urlName"])
            body = clean_markdown(entry.get("details", ""), url)
            # Canny's editor puts bold headings on separate lines.
            body = re.sub(r"(?m)^\*\*\s*\n([^*\n]+)\s*\n\*\*\s*$", r"### \1", body)
            body = re.sub(r"(?m)^\*\*([^*\n]+)\*\*\s*$", r"### \1", body)
            releases.append(release(product, publication_date(entry.get("publishedAt", "")),
                                    body, url, entry["title"], entry["_id"]))
        if not more or (limit is not None and len(releases) >= limit):
            return ordered(releases, limit)
        previous = ids
    raise ValueError("Gamma pagination did not terminate")


def fetch_manus(product: dict, limit: int | None) -> list[dict]:
    releases, seen = [], set()
    cursor, total = None, None
    for _ in range(1000):
        query = {"limit": 20}
        if cursor:
            query["latestUid"] = cursor
        payload = post_json(MANUS_API, query)
        # Protobuf JSON encodes int64 as decimal strings and may omit a false
        # boolean at the terminal page.
        entries, more = payload.get("data"), payload.get("hasNext", False)
        reported_total = payload.get("total")
        if isinstance(reported_total, str) and re.fullmatch(r"\d+", reported_total):
            reported_total = int(reported_total)
        if (payload.get("success") is not True or not isinstance(entries, list)
                or not isinstance(more, bool) or type(reported_total) is not int):
            raise ValueError("Manus public updates has an invalid pagination response")
        if total is not None and reported_total != total:
            raise ValueError("Manus public update total changed during collection")
        total = reported_total
        if not entries:
            raise ValueError("Manus returned an empty archive page")
        for entry in entries:
            uid, detail = entry.get("uid"), entry.get("detail", {})
            if not uid or uid in seen or not detail.get("title"):
                raise ValueError("Manus update has a missing/duplicate identity or title")
            if entry.get("notificationCategory") != "CATEGORY_UPDATE":
                raise ValueError("Manus public feed returned a non-update notification")
            seen.add(uid)
            # Some entries have no permalink. Keep the official public index as
            # their source; never invent an anchor or include account-only URLs.
            target = detail.get("button", {}).get("target", "")
            parts = urlsplit(target)
            url = target if (parts.scheme == "https" and parts.netloc in {"manus.im", "www.manus.im"}
                             and parts.path.startswith("/blog/")) else product["url"]
            releases.append(release(product, publication_date(entry.get("createAt", "")),
                                    detail.get("content", ""), url, detail["title"].strip(), uid))
        if not more:
            if len(seen) != total:
                raise ValueError("Manus archive count disagrees with its reported total")
            return ordered(releases, limit)
        if len(seen) >= total:
            raise ValueError("Manus pagination continues beyond its reported total")
        if limit is not None and len(releases) >= limit:
            return ordered(releases, limit)
        cursor = entries[-1]["uid"]
    raise ValueError("Manus pagination did not terminate")


def openclaw_urls(product: dict, html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    urls = []
    for link in soup.select(".doc a[href]"):
        path = urlsplit(link["href"]).path
        if re.fullmatch(r"/releases/\d{4}\.\d+\.\d+", path):
            urls.append(official_url(product["url"], link["href"]))
    if not urls or len(set(urls)) != len(urls):
        raise ValueError("OpenClaw curated release index is empty or contains duplicates")
    return urls


def parse_openclaw(product: dict, url: str, html: str, metadata: dict) -> dict:
    version = "v" + urlsplit(url).path.rsplit("/", 1)[-1]
    if (metadata.get("tag_name") != version or metadata.get("draft")
            or metadata.get("prerelease")):
        raise ValueError("OpenClaw published tag disagrees with its curated release")
    soup = BeautifulSoup(html, "html.parser")
    body = soup.select_one(".doc")
    heading = (body.find("h1") or soup.select_one("main.article > header.article-header h1")) if body else None
    if heading is None or not re.match(r"^(?:OpenClaw )?" + re.escape(version) + r"(?:$|\s+\()", plain(heading)):
        raise ValueError("OpenClaw curated release is missing its matching version heading")
    for ignored in body.select("h1, .release-source-toggle, .docs-media-scene"):
        ignored.decompose()
    blocks = [block for block in html_blocks(body) if not block["text"].startswith((
        "AI agents and tools can read", "Release scale:", "The pull-request count includes",
    ))]
    # Calendar-looking versions are identifiers, not publication dates.
    item = release(product, publication_date(metadata.get("published_at", "")),
                   body_from_blocks(blocks), url, version, version)
    item["version"] = version
    return item


def fetch_openclaw(product: dict, limit: int | None) -> list[dict]:
    urls = openclaw_urls(product, get_text(product["url"]))
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("CHRONOLOG_GITHUB_READ_TOKEN", "").strip()
    if token:
        headers["Authorization"] = "Bearer " + token

    def fetch(url):
        version = "v" + url.rsplit("/", 1)[-1]
        response = httpx.get(f"https://api.github.com/repos/{product['repo']}/releases/tags/{version}",
                             headers=headers, timeout=45.0, follow_redirects=False)
        response.raise_for_status()
        return parse_openclaw(product, url, get_text(url), response.json())

    with ThreadPoolExecutor(max_workers=4) as pool:
        return ordered(list(pool.map(fetch, urls)), limit)


def parse_opencode(product: dict, html: str) -> tuple[list[dict], str | None]:
    soup = BeautifulSoup(html, "html.parser")
    releases = []
    for body in soup.select('[data-component="changelog-entry"]'):
        row = body.find_parent("li")
        time, version = row.find("time") if row else None, row.select_one('[data-slot="version"][href]') if row else None
        if time is None or version is None or not row.get("id"):
            raise ValueError("OpenCode entry is missing its publication date or version")
        for refs in body.select('[data-slot="refs"], [data-slot="copied"]'):
            refs.decompose()
        for heading in body.find_all(["h2", "h3", "h4"]):
            # Disclosure headings include a visual count ("Improvements 14").
            # Keep the generic section name so it cannot become a feature title.
            label = re.fullmatch(r"(Improvements|Fixes|Breaking changes)\s+\d+", plain(heading), re.I)
            if label:
                heading.clear()
                heading.string = label[1]
        item = release(product, publication_date(time.get("datetime", "")),
                       body_from_blocks(html_blocks(body)),
                       official_url(product["url"], version["href"]), plain(version), row["id"])
        item["version"] = plain(version)
        releases.append(item)
    older = [a for a in soup.select("a[href]") if plain(a).startswith("Older updates")]
    if len(older) > 1:
        raise ValueError("OpenCode has ambiguous archive pagination")
    next_url = official_url(product["url"], older[0]["href"]) if older else None
    if next_url and not re.fullmatch(r"/changelog\?page=\d+", urlsplit(next_url).path + "?" + urlsplit(next_url).query):
        raise ValueError("OpenCode archive has an unexpected pagination URL")
    return ordered(releases, None), next_url


def fetch_opencode(product: dict, limit: int | None) -> list[dict]:
    url, seen, releases = product["url"], set(), []
    while url:
        if url in seen or len(seen) >= 1000:
            raise ValueError("OpenCode archive pagination did not terminate")
        seen.add(url)
        entries, url = parse_opencode(product, get_text(url))
        releases.extend(entries)
        if limit is not None and len(releases) >= limit:
            break
    return ordered(releases, limit)


def fetch_trending_releases(product: dict, limit: int | None) -> list[dict]:
    kind = product["feed_type"].removesuffix("_changelog")
    if kind in {"suno", "runway", "granola", "antigravity"}:
        parser = {"suno": parse_suno, "runway": parse_runway,
                  "granola": parse_granola, "antigravity": parse_antigravity}[kind]
        return ordered(parser(product, get_text(product["url"])), limit)
    if kind == "midjourney":
        urls = midjourney_urls(product, get_text(product["index_url"]))
        with ThreadPoolExecutor(max_workers=4) as pool:
            # Sitemap order/lastmod do not establish publication order. Fetch all
            # posts before selecting a recent window.
            return ordered(list(pool.map(lambda url: parse_midjourney(product, url, get_text(url)), urls)), limit)
    fetcher = {"gamma": fetch_gamma, "manus": fetch_manus,
               "openclaw": fetch_openclaw, "opencode": fetch_opencode}.get(kind)
    if fetcher is None:
        raise ValueError(f"Unsupported trending product feed: {kind}")
    return fetcher(product, limit)
