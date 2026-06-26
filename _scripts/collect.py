from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import feedparser
import httpx

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _scripts.common import PipelinePaths, parse_date, read_json, read_yaml, write_json


def load_sources(path: Path) -> list[dict[str, Any]]:
    data = read_yaml(path)
    return [product for product in data["products"] if product.get("enabled", True)]


def collect_fixture(fixture_path: Path, output_path: Path) -> dict[str, Any]:
    data = read_json(fixture_path)
    releases = sorted(data["releases"], key=lambda item: (item["product"], item["date"]))
    payload = {"source": "fixture", "releases": releases}
    write_json(output_path, payload)
    return payload


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("value must be a positive integer")
    return parsed


def fetch_github_releases(product: dict[str, Any], limit: int) -> list[dict[str, Any]]:
    if limit > 100:
        raise ValueError("github_releases limit must be <= 100 for MVP")

    url = f"https://api.github.com/repos/{product['repo']}/releases"
    response = httpx.get(
        url,
        timeout=30.0,
        headers={"Accept": "application/vnd.github+json"},
        params={"per_page": min(limit, 100)},
        follow_redirects=True,
    )
    response.raise_for_status()
    releases = []
    for item in response.json()[:limit]:
        published = item.get("published_at") or item.get("created_at")
        releases.append(
            {
                "product": product["name"],
                "product_name": product["display_name"],
                "date": parse_date(published).isoformat(),
                "version": item.get("tag_name") or item.get("name") or "release",
                "title": item.get("name") or item.get("tag_name") or "Release",
                "body": item.get("body") or "",
                "source_url": item.get("html_url") or url,
                "source_type": "github_releases",
            }
        )
    return releases


def fetch_rss_releases(product: dict[str, Any], limit: int) -> list[dict[str, Any]]:
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
    for entry in feed.entries[:limit]:
        date_value = getattr(entry, "published", None) or getattr(entry, "updated", None)
        if not date_value:
            raise ValueError(f"RSS entry for {product['name']} is missing published/updated date")
        releases.append(
            {
                "product": product["name"],
                "product_name": product["display_name"],
                "date": parse_date(date_value).isoformat(),
                "version": getattr(entry, "id", getattr(entry, "title", "release")),
                "title": getattr(entry, "title", "Release"),
                "body": getattr(entry, "summary", ""),
                "source_url": getattr(entry, "link", product["url"]),
                "source_type": "blog_rss",
            }
        )
    return releases


def collect_live(
    sources_path: Path,
    output_path: Path,
    limit: int,
    backfill: str | None = None,
) -> dict[str, Any]:
    releases: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    products = load_sources(sources_path)
    if backfill and backfill != "all":
        backfill_key = backfill.casefold()
        products = [
            product
            for product in products
            if product["name"].casefold() == backfill_key
            or product["display_name"].casefold() == backfill_key
        ]
        if not products:
            payload = {
                "source": "live",
                "releases": [],
                "errors": [{"product": backfill, "error": f"unknown product: {backfill}"}],
            }
            write_json(output_path, payload)
            return payload

    for product in products:
        try:
            if product["feed_type"] == "github_releases":
                releases.extend(fetch_github_releases(product, limit))
            elif product["feed_type"] == "blog_rss":
                releases.extend(fetch_rss_releases(product, limit))
            else:
                raise ValueError(f"unsupported feed_type: {product['feed_type']}")
        except Exception as exc:
            errors.append({"product": product["name"], "error": str(exc)})
    payload = {
        "source": "live",
        "releases": sorted(releases, key=lambda item: item["date"]),
        "errors": errors,
    }
    write_json(output_path, payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    parser.add_argument("--fixture", action="store_true")
    parser.add_argument("--backfill", nargs="?", const="all")
    parser.add_argument("--limit", type=positive_int)
    args = parser.parse_args()
    paths = PipelinePaths(args.run_id)
    if args.fixture:
        collect_fixture(ROOT / "tests/fixtures/releases.json", paths.collected)
    else:
        limit = args.limit if args.limit is not None else 100 if args.backfill else 30
        collect_live(ROOT / "_scripts/sources.yaml", paths.collected, limit, backfill=args.backfill)


if __name__ == "__main__":
    main()
