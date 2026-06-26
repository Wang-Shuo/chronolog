import shutil
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

from _scripts import collect
from _scripts.collect import (
    collect_fixture,
    collect_live,
    fetch_github_releases,
    fetch_rss_releases,
    load_sources,
)


def test_load_sources_returns_enabled_products():
    products = load_sources(Path("_scripts/sources.yaml"))
    assert len(products) >= 5
    assert all(product["feed_type"] in {"github_releases", "blog_rss"} for product in products)


def test_collect_fixture_writes_normalized_releases(tmp_path: Path):
    output = tmp_path / "releases.json"
    releases = collect_fixture(Path("tests/fixtures/releases.json"), output)

    assert output.exists()
    assert len(releases["releases"]) >= 10
    assert {"product", "product_name", "date", "title", "body", "source_url"} <= set(
        releases["releases"][0]
    )


def test_direct_cli_fixture_invocation_writes_output():
    run_id = "pytest-direct-collect-fixture"
    run_dir = Path("_pipeline") / run_id
    output = run_dir / "01-collected" / "releases.json"
    shutil.rmtree(run_dir, ignore_errors=True)

    try:
        result = subprocess.run(
            [sys.executable, "_scripts/collect.py", "--fixture", "--run-id", run_id],
            cwd=Path.cwd(),
            capture_output=True,
            text=True,
            check=False,
        )

        assert result.returncode == 0, result.stderr
        assert output.exists()
    finally:
        shutil.rmtree(run_dir, ignore_errors=True)


def test_fetch_github_releases_normalizes_api_items(monkeypatch):
    calls = {}

    class Response:
        def raise_for_status(self):
            calls["raised"] = True

        def json(self):
            return [
                {
                    "published_at": "2026-06-20T10:11:12Z",
                    "tag_name": "v1.2.3",
                    "name": "Release 1.2.3",
                    "body": "Ship the thing",
                    "html_url": "https://github.com/acme/tool/releases/tag/v1.2.3",
                }
            ]

    def fake_get(url, timeout, headers, params):
        calls.update({"url": url, "timeout": timeout, "headers": headers, "params": params})
        return Response()

    monkeypatch.setattr(collect.httpx, "get", fake_get)

    releases = fetch_github_releases(
        {"name": "tool", "display_name": "Tool", "repo": "acme/tool"},
        limit=100,
    )

    assert calls["url"] == "https://api.github.com/repos/acme/tool/releases"
    assert calls["params"] == {"per_page": 100}
    assert calls["raised"] is True
    assert releases == [
        {
            "product": "tool",
            "product_name": "Tool",
            "date": "2026-06-20",
            "version": "v1.2.3",
            "title": "Release 1.2.3",
            "body": "Ship the thing",
            "source_url": "https://github.com/acme/tool/releases/tag/v1.2.3",
            "source_type": "github_releases",
        }
    ]


def test_fetch_github_releases_rejects_limit_over_first_page(monkeypatch):
    def fake_get(*args, **kwargs):
        raise AssertionError("GitHub request should not be made for an invalid limit")

    monkeypatch.setattr(collect.httpx, "get", fake_get)

    with pytest.raises(ValueError, match="limit.*100"):
        fetch_github_releases(
            {"name": "tool", "display_name": "Tool", "repo": "acme/tool"},
            limit=101,
        )


def test_fetch_rss_releases_normalizes_feed_entries(monkeypatch):
    calls = {}

    class Response:
        content = b"<rss>release feed</rss>"

        def raise_for_status(self):
            calls["raised"] = True

    def fake_get(url, timeout):
        calls.update({"url": url, "timeout": timeout})
        return Response()

    feed = SimpleNamespace(
        bozo=False,
        status=200,
        entries=[
            SimpleNamespace(
                published="Fri, 26 Jun 2026 12:34:56 GMT",
                id="entry-1",
                title="RSS release",
                summary="RSS body",
                link="https://example.com/releases/1",
            )
        ],
    )

    def fake_parse(content):
        calls["parsed_content"] = content
        return feed

    monkeypatch.setattr(collect.httpx, "get", fake_get)
    monkeypatch.setattr(collect.feedparser, "parse", fake_parse)

    releases = fetch_rss_releases(
        {"name": "blog", "display_name": "Blog", "url": "https://example.com/feed.xml"},
        limit=10,
    )

    assert calls == {
        "url": "https://example.com/feed.xml",
        "timeout": 30.0,
        "raised": True,
        "parsed_content": b"<rss>release feed</rss>",
    }
    assert releases == [
        {
            "product": "blog",
            "product_name": "Blog",
            "date": "2026-06-26",
            "version": "entry-1",
            "title": "RSS release",
            "body": "RSS body",
            "source_url": "https://example.com/releases/1",
            "source_type": "blog_rss",
        }
    ]


def test_fetch_rss_releases_raises_for_bozo_feed(monkeypatch):
    class Response:
        content = b"<rss>broken"

        def raise_for_status(self):
            pass

    feed = SimpleNamespace(
        bozo=True,
        bozo_exception=ValueError("broken xml"),
        entries=[],
    )
    monkeypatch.setattr(collect.httpx, "get", lambda url, timeout: Response())
    monkeypatch.setattr(collect.feedparser, "parse", lambda url: feed)

    with pytest.raises(ValueError, match="broken xml"):
        fetch_rss_releases(
            {"name": "blog", "display_name": "Blog", "url": "https://example.com/feed.xml"},
            limit=10,
        )


def test_fetch_rss_releases_raises_for_http_error_status(monkeypatch):
    class Response:
        content = b"<rss></rss>"

        def raise_for_status(self):
            pass

    feed = SimpleNamespace(bozo=False, status=500, entries=[])
    monkeypatch.setattr(collect.httpx, "get", lambda url, timeout: Response())
    monkeypatch.setattr(collect.feedparser, "parse", lambda url: feed)

    with pytest.raises(ValueError, match="500"):
        fetch_rss_releases(
            {"name": "blog", "display_name": "Blog", "url": "https://example.com/feed.xml"},
            limit=10,
        )


def test_collect_live_writes_sorted_releases_and_errors(tmp_path: Path, monkeypatch):
    sources = tmp_path / "sources.yaml"
    sources.write_text(
        """
products:
  - name: later
    display_name: Later
    feed_type: github_releases
    repo: acme/later
  - name: blog
    display_name: Blog
    feed_type: blog_rss
    url: https://example.com/feed.xml
  - name: earlier
    display_name: Earlier
    feed_type: github_releases
    repo: acme/earlier
""",
        encoding="utf-8",
    )
    output = tmp_path / "releases.json"

    def fake_github(product, limit):
        return [
            {
                "product": product["name"],
                "product_name": product["display_name"],
                "date": "2026-06-20" if product["name"] == "later" else "2026-01-01",
                "title": product["display_name"],
                "body": "",
                "source_url": "https://example.com",
                "source_type": "github_releases",
            }
        ]

    def fake_rss(product, limit):
        raise RuntimeError("feed unavailable")

    monkeypatch.setattr(collect, "fetch_github_releases", fake_github)
    monkeypatch.setattr(collect, "fetch_rss_releases", fake_rss)

    payload = collect_live(sources, output, limit=5)

    assert output.exists()
    assert [release["date"] for release in payload["releases"]] == ["2026-01-01", "2026-06-20"]
    assert payload["errors"] == [{"product": "blog", "error": "feed unavailable"}]


def test_collect_live_records_unsupported_feed_type_error(tmp_path: Path):
    sources = tmp_path / "sources.yaml"
    sources.write_text(
        """
products:
  - name: docs
    display_name: Docs
    feed_type: webpage
    url: https://example.com
""",
        encoding="utf-8",
    )

    payload = collect_live(sources, tmp_path / "releases.json", limit=5)

    assert payload["releases"] == []
    assert payload["errors"] == [
        {"product": "docs", "error": "unsupported feed_type: webpage"}
    ]


def test_collect_live_backfill_filters_to_product(tmp_path: Path, monkeypatch):
    sources = tmp_path / "sources.yaml"
    sources.write_text(
        """
products:
  - name: cursor
    display_name: Cursor
    feed_type: github_releases
    repo: acme/cursor
  - name: aider
    display_name: Aider
    feed_type: github_releases
    repo: acme/aider
""",
        encoding="utf-8",
    )
    called_products = []

    def fake_github(product, limit):
        called_products.append(product["name"])
        return [
            {
                "product": product["name"],
                "product_name": product["display_name"],
                "date": "2026-01-01",
                "title": product["display_name"],
                "body": "",
                "source_url": "https://example.com",
                "source_type": "github_releases",
            }
        ]

    monkeypatch.setattr(collect, "fetch_github_releases", fake_github)

    payload = collect_live(sources, tmp_path / "releases.json", limit=5, backfill="aider")

    assert called_products == ["aider"]
    assert [release["product"] for release in payload["releases"]] == ["aider"]
    assert payload["errors"] == []


def test_collect_live_unknown_backfill_product_records_error(tmp_path: Path):
    sources = tmp_path / "sources.yaml"
    sources.write_text(
        """
products:
  - name: cursor
    display_name: Cursor
    feed_type: github_releases
    repo: acme/cursor
""",
        encoding="utf-8",
    )

    payload = collect_live(sources, tmp_path / "releases.json", limit=5, backfill="missing")

    assert payload["releases"] == []
    assert payload["errors"] == [{"product": "missing", "error": "unknown product: missing"}]


def test_main_uses_backfill_default_limit(monkeypatch):
    captured = {}

    def fake_collect_live(sources_path, output_path, limit, backfill=None):
        captured.update({"limit": limit, "backfill": backfill})
        return {"source": "live", "releases": [], "errors": []}

    monkeypatch.setattr(sys, "argv", ["collect.py", "--backfill", "cursor"])
    monkeypatch.setattr(collect, "collect_live", fake_collect_live)
    monkeypatch.setattr(
        collect,
        "PipelinePaths",
        lambda run_id: SimpleNamespace(collected=Path("unused.json")),
    )

    collect.main()

    assert captured == {"limit": 100, "backfill": "cursor"}


def test_main_keeps_explicit_limit_for_backfill(monkeypatch):
    captured = {}

    def fake_collect_live(sources_path, output_path, limit, backfill=None):
        captured.update({"limit": limit, "backfill": backfill})
        return {"source": "live", "releases": [], "errors": []}

    monkeypatch.setattr(sys, "argv", ["collect.py", "--backfill", "cursor", "--limit", "7"])
    monkeypatch.setattr(collect, "collect_live", fake_collect_live)
    monkeypatch.setattr(
        collect,
        "PipelinePaths",
        lambda run_id: SimpleNamespace(collected=Path("unused.json")),
    )

    collect.main()

    assert captured == {"limit": 7, "backfill": "cursor"}
