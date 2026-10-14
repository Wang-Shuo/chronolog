import argparse
import shutil
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace
from uuid import uuid4

import pytest

from _scripts import collect
from _scripts.collect import (
    collect_fixture,
    collect_live,
    fetch_github_releases,
    fetch_rss_releases,
    load_sources,
    parse_chatgpt_changelog,
    parse_cursor_changelog_page,
    positive_int,
)


def test_load_sources_returns_enabled_products():
    products = load_sources(Path("_scripts/sources.yaml"))
    assert {product["name"] for product in products} == {
        "chatgpt",
        "claude-code",
        "cursor",
    }
    assert {product["feed_type"] for product in products} == {
        "chatgpt_changelog",
        "github_releases",
        "cursor_changelog",
    }


def test_collect_fixture_writes_normalized_releases(tmp_path: Path):
    output = tmp_path / "releases.json"
    releases = collect_fixture(Path("tests/fixtures/releases.json"), output)

    assert output.exists()
    assert len(releases["releases"]) >= 10
    assert {"product", "product_name", "date", "title", "body", "source_url"} <= set(
        releases["releases"][0]
    )


def test_direct_cli_fixture_invocation_writes_output():
    run_id = f"pytest-direct-collect-fixture-{uuid4().hex}"
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


def test_absolute_cli_fixture_invocation_from_other_cwd_writes_repo_output(tmp_path: Path):
    run_id = f"pytest-absolute-collect-fixture-{uuid4().hex}"
    repo_root = Path.cwd()
    run_dir = repo_root / "_pipeline" / run_id
    output = run_dir / "01-collected" / "releases.json"
    shutil.rmtree(run_dir, ignore_errors=True)

    try:
        result = subprocess.run(
            [
                sys.executable,
                str(repo_root / "_scripts" / "collect.py"),
                "--fixture",
                "--run-id",
                run_id,
            ],
            cwd=tmp_path,
            capture_output=True,
            text=True,
            check=False,
        )

        assert result.returncode == 0, result.stderr
        assert output.exists()
    finally:
        shutil.rmtree(run_dir, ignore_errors=True)


def test_positive_int_accepts_positive_numbers():
    assert positive_int("7") == 7


def test_positive_int_rejects_zero_and_negative_numbers():
    with pytest.raises(argparse.ArgumentTypeError, match="positive"):
        positive_int("0")
    with pytest.raises(argparse.ArgumentTypeError, match="positive"):
        positive_int("-1")


def test_main_rejects_non_positive_limit(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["collect.py", "--limit", "0"])

    with pytest.raises(SystemExit):
        collect.main()


def test_fetch_github_releases_normalizes_api_items(monkeypatch):
    monkeypatch.delenv("CHRONOLOG_GITHUB_READ_TOKEN", raising=False)
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

    def fake_get(url, timeout, headers, params, follow_redirects):
        calls.update(
            {
                "url": url,
                "timeout": timeout,
                "headers": headers,
                "params": params,
                "follow_redirects": follow_redirects,
            }
        )
        return Response()

    monkeypatch.setattr(collect.httpx, "get", fake_get)

    releases = fetch_github_releases(
        {"name": "tool", "display_name": "Tool", "repo": "acme/tool"},
        limit=100,
    )

    assert calls["url"] == "https://api.github.com/repos/acme/tool/releases"
    assert calls["params"] == {"per_page": 100, "page": 1}
    assert calls["follow_redirects"] is True
    assert "Authorization" not in calls["headers"]
    assert calls["raised"] is True
    assert len(releases) == 1
    assert releases[0] | {} == {
        "release_id": releases[0]["release_id"],
        "product": "tool",
        "product_name": "Tool",
        "date": "2026-06-20",
        "version": "v1.2.3",
        "title": "Release 1.2.3",
        "body": "Ship the thing",
        "source_summary": "Ship the thing",
        "source_url": "https://github.com/acme/tool/releases/tag/v1.2.3",
        "source_type": "github_releases",
    }
    assert releases[0]["release_id"].startswith("tool-2026-06-20-")


@pytest.mark.parametrize("token", ["", "read-token-for-test"])
def test_fetch_github_releases_paginates_beyond_first_page(monkeypatch, token):
    monkeypatch.setenv("CHRONOLOG_GITHUB_READ_TOKEN", token)
    calls = []

    class Response:
        def __init__(self, items):
            self.items = items

        def raise_for_status(self):
            pass

        def json(self):
            return self.items

    def item(index):
        return {
            "id": index,
            "published_at": "2026-06-20T10:11:12Z",
            "tag_name": f"v{index}",
            "name": f"Release {index}",
            "body": "Release body",
            "html_url": f"https://github.com/acme/tool/releases/tag/v{index}",
        }

    def fake_get(*args, **kwargs):
        assert args[0] == "https://api.github.com/repos/acme/tool/releases"
        assert kwargs["headers"].get("Authorization") == (f"Bearer {token}" if token else None)
        assert kwargs["follow_redirects"] is (not bool(token))
        page = kwargs["params"]["page"]
        calls.append(page)
        return Response([item(index) for index in range(100)] if page == 1 else [item(100)])

    monkeypatch.setattr(collect.httpx, "get", fake_get)

    releases = fetch_github_releases(
        {"name": "tool", "display_name": "Tool", "repo": "acme/tool"},
        limit=101,
    )

    assert calls == [1, 2]
    assert len(releases) == 101


def test_github_read_token_is_not_sent_to_rss(monkeypatch):
    monkeypatch.setenv("CHRONOLOG_GITHUB_READ_TOKEN", "read-token-for-test")

    def fake_get(url, **kwargs):
        assert url == "https://feed.example.org/releases.xml"
        assert "Authorization" not in kwargs.get("headers", {})
        return SimpleNamespace(raise_for_status=lambda: None,
            content=b'<rss version="2.0"><channel><title>Releases</title></channel></rss>')

    monkeypatch.setattr(collect.httpx, "get", fake_get)
    assert fetch_rss_releases({"name": "tool", "url": "https://feed.example.org/releases.xml"}, None) == []


def test_parse_cursor_changelog_page_extracts_release_and_next_page():
    product = {
        "name": "cursor",
        "display_name": "Cursor",
        "url": "https://cursor.com/changelog",
    }
    html = """
    <main>
      <article>
        <time dateTime="2026-07-10T00:00:00.000Z">Jul 10, 2026</time>
        <span class="label">3.11</span>
        <h1><a href="/changelog/side-chat">Side Chats</a></h1>
        <div class="prose prose--block"><p>Search agent transcripts from the editor.</p></div>
      </article>
      <a href="/changelog/page/2">Older posts</a>
    </main>
    """

    releases, pages = parse_cursor_changelog_page(product, html)

    assert pages == {2}
    assert len(releases) == 1
    assert releases[0]["date"] == "2026-07-10"
    assert releases[0]["version"] == "3.11"
    assert releases[0]["title"] == "Side Chats"
    assert releases[0]["source_url"] == "https://cursor.com/changelog/side-chat"


def test_parse_chatgpt_changelog_splits_same_day_entries_and_filters_codex_only():
    product = {
        "name": "chatgpt",
        "display_name": "ChatGPT",
        "url": "https://help.openai.com/en/articles/6825453-chatgpt-release-notes",
    }
    html = """
    <article>
      <h1>ChatGPT — Release Notes</h1>
      <h1>July 29, 2026</h1>
      <h2 id="researchers">ChatGPT for Academic Researchers</h2>
      <p>A dedicated ChatGPT workspace is available.</p>
      <h2 id="signin">Sign in with ChatGPT</h2>
      <p>Supported partners can use ChatGPT sign in.</p>
      <h2 id="codex">Updates to Codex</h2>
      <p>Codex received an update.</p>
      <h1>March 10, 2026</h1>
      <h3 id="learning">Interactive learning</h3>
      <p>Math and science lessons are interactive.</p>
    </article>
    """

    releases = parse_chatgpt_changelog(product, html, limit=None)

    assert [release["title"] for release in releases] == [
        "ChatGPT for Academic Researchers",
        "Sign in with ChatGPT",
        "Interactive learning",
    ]
    assert len({release["release_id"] for release in releases}) == 3
    assert releases[0]["source_url"].endswith("#researchers")


def test_fetch_rss_releases_normalizes_feed_entries(monkeypatch):
    calls = {}

    class Response:
        content = b"<rss>release feed</rss>"

        def raise_for_status(self):
            calls["raised"] = True

    def fake_get(url, timeout, follow_redirects):
        calls.update({"url": url, "timeout": timeout, "follow_redirects": follow_redirects})
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
        "follow_redirects": True,
        "raised": True,
        "parsed_content": b"<rss>release feed</rss>",
    }
    assert len(releases) == 1
    assert releases[0] == {
        "release_id": releases[0]["release_id"],
        "product": "blog",
        "product_name": "Blog",
        "date": "2026-06-26",
        "version": "entry-1",
        "title": "RSS release",
        "body": "RSS body",
        "source_summary": "RSS body",
        "source_url": "https://example.com/releases/1",
        "source_type": "blog_rss",
    }


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
    monkeypatch.setattr(
        collect.httpx, "get", lambda url, timeout, follow_redirects: Response()
    )
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
    monkeypatch.setattr(
        collect.httpx, "get", lambda url, timeout, follow_redirects: Response()
    )
    monkeypatch.setattr(collect.feedparser, "parse", lambda url: feed)

    with pytest.raises(ValueError, match="500"):
        fetch_rss_releases(
            {"name": "blog", "display_name": "Blog", "url": "https://example.com/feed.xml"},
            limit=10,
        )


def test_fetch_rss_releases_raises_for_missing_entry_date(monkeypatch):
    class Response:
        content = b"<rss></rss>"

        def raise_for_status(self):
            pass

    feed = SimpleNamespace(
        bozo=False,
        status=200,
        entries=[SimpleNamespace(id="entry-1", title="No date release")],
    )
    monkeypatch.setattr(
        collect.httpx, "get", lambda url, timeout, follow_redirects: Response()
    )
    monkeypatch.setattr(collect.feedparser, "parse", lambda content: feed)

    with pytest.raises(ValueError, match="blog.*date"):
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
                    "release_id": f"{product['name']}-release",
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
                    "release_id": f"{product['name']}-release",
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


def test_collect_live_backfill_matches_name_and_display_name_case_insensitively(
    tmp_path: Path, monkeypatch
):
    sources = tmp_path / "sources.yaml"
    sources.write_text(
        """
products:
  - name: cursor
    display_name: Cursor
    feed_type: github_releases
    repo: acme/cursor
  - name: openhands
    display_name: OpenHands
    feed_type: github_releases
    repo: acme/openhands
""",
        encoding="utf-8",
    )
    called_products = []

    def fake_github(product, limit):
        called_products.append(product["name"])
        return [
                {
                    "release_id": f"{product['name']}-release",
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

    cursor_payload = collect_live(
        sources, tmp_path / "cursor-releases.json", limit=5, backfill="Cursor"
    )
    openhands_payload = collect_live(
        sources, tmp_path / "openhands-releases.json", limit=5, backfill="OpenHands"
    )

    assert called_products == ["cursor", "openhands"]
    assert [release["product"] for release in cursor_payload["releases"]] == ["cursor"]
    assert [release["product"] for release in openhands_payload["releases"]] == ["openhands"]
    assert cursor_payload["errors"] == []
    assert openhands_payload["errors"] == []


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

    def fake_collect_live(sources_path, output_path, limit, backfill=None, snapshot_paths=None):
        captured.update({"sources_path": sources_path, "limit": limit, "backfill": backfill})
        return {"source": "live", "releases": [], "errors": []}

    monkeypatch.setattr(sys, "argv", ["collect.py", "--backfill", "cursor"])
    monkeypatch.setattr(collect, "collect_live", fake_collect_live)
    monkeypatch.setattr(
        collect,
        "PipelinePaths",
        lambda run_id: SimpleNamespace(collected=Path("unused.json")),
    )

    collect.main()

    assert captured == {
        "sources_path": collect.ROOT / "_scripts/sources.yaml",
        "limit": None,
        "backfill": "cursor",
    }


def test_main_keeps_explicit_limit_for_backfill(monkeypatch):
    captured = {}

    def fake_collect_live(sources_path, output_path, limit, backfill=None, snapshot_paths=None):
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
