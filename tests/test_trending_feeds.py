from pathlib import Path

import httpx
import pytest
import yaml

from _scripts import collect, trending_feeds as feeds
from _scripts.extract import extract_cards_from_release, load_theme_vocabulary


CATALOG = {p["name"]: p for p in collect.load_sources(Path("_scripts/sources.yaml"))}
SUNO = '<article id="song"><div><h2><a href="/release-notes/song">Song editor</a></h2><time datetime="2026-11-06T20:00:00Z"/><button>New feature</button></div><div><h3>Stem separation</h3><p>Separate your song into editable instrument stems.</p></div></article>'
RUNWAY = '<div><div class="rw-bodycopy5">Oct 27, 2026</div><div><div class="rw-bodycopy3">All plans</div><div class="rw-h5">Video generation</div><div class="rw-bodycopy2">Generate videos from images.</div></div></div>'
GRANOLA = '<a href="/updates/languages"><h3>More languages</h3><p>Meeting notes now support 32 languages.</p><span>Jack · 02 Sept 2026</span></a>'
MIDJOURNEY = '<meta property="article:published_time" content="2026-10-08T21:17:13Z"><h1 class="single-title">Alpha changelog 10/7/26</h1><div class="single-content gh-content"><p>Image generation now supports thinking mode.</p></div><footer><p>Subscribe for more</p></footer>'
OPENCLAW = '<div class="doc"><h1>v2026.11.1</h1><p>AI agents and tools can read these release notes as plain Markdown.</p><p>Release scale: 83 pull requests.</p><h2>Memory</h2><ul><li><p>Persistent memory remembers your preferences.</p><details class="release-source-toggle"><p>Thanks to contributors; see commit.</p></details></li></ul></div>'


def antigravity_row(surface, version="1.0.0"):
    return f'<article class="release-entry" id="rel-{surface}-{version}"><a class="rn-version-tag" href="/releases?tab={surface}&amp;version={version}">v{version}</a><time>November 3, 2026</time><div class="rn-card"><h3 class="rn-headline">New agent</h3><p>The agent can plan a project.</p><details data-item-title="Improvements"><summary>Improvements (1)</summary><ul><li>Supports new model connections.</li></ul></details></div></article>'


def opencode_row(version="v2.2.6", date="2026-11-06"):
    return f'<li id="{version}"><header><time datetime="{date}"/><a data-slot="version" href="/changelog/{version}">{version}</a></header><div data-component="changelog-entry"><h2>Shared MCP</h2><p>Share MCP connections across projects.<span data-slot="refs">#1234</span></p><h3>Fixes</h3><ul><li>Fixed terminal reconnects.</li></ul></div></li>'


def gamma_entry(uid="a", date="2026-11-01"):
    return {"_id": uid, "title": "New presentation tools", "publishedAt": date,
            "status": "published", "deleted": False, "urlName": "new-" + uid,
            "details": "**\nBetter slides\n\n**\nCreate presentations from your data.\n\n![Preview](https://example.com/image.png)"}


def manus_entry(uid="a", date="2026-11-01"):
    return {"uid": uid, "createAt": date, "notificationCategory": "CATEGORY_UPDATE",
            "detail": {"title": "New agent", "content": "The agent can build websites.",
                       "button": {"target": "https://manus.im/blog/new-agent"}}}


@pytest.mark.parametrize("text,expected", [
    ("2026-11-06T20:00:35.781Z", "2026-11-06"),
    ("November 3, 2026", "2026-11-03"), ("02 Sept 2026", "2026-09-02"),
])
def test_explicit_publication_date_formats(text, expected):
    assert feeds.publication_date(text) == expected


@pytest.mark.parametrize("text", ["", "yesterday", "2026-02-30", None])
def test_missing_or_invalid_dates_fail(text):
    with pytest.raises(ValueError):
        feeds.publication_date(text)


def test_single_page_sources_preserve_dates_and_remove_controls():
    suno = feeds.parse_suno(CATALOG["suno"], SUNO)[0]
    assert suno["source_url"] == "https://suno.com/release-notes/song"
    assert suno["date"] == "2026-11-06" and "New feature" not in suno["body"]
    assert suno["body"].startswith("### Stem separation")
    runway = feeds.parse_runway(CATALOG["runway"], RUNWAY + RUNWAY.replace("Video generation", "Image generation"))
    assert len({r["release_id"] for r in runway}) == 2
    assert all(r["date"] == "2026-10-27" and "All plans" not in r["body"] for r in runway)
    granola = feeds.parse_granola(CATALOG["granola"], GRANOLA)[0]
    assert granola["date"] == "2026-09-02" and "Jack" not in granola["body"]


@pytest.mark.parametrize("name,parser,html", [
    ("suno", feeds.parse_suno, SUNO.replace('datetime="2026-11-06T20:00:00Z"', "")),
    ("runway", feeds.parse_runway, RUNWAY.replace("Oct 27, 2026", "unknown")),
    ("granola", feeds.parse_granola, GRANOLA.replace("02 Sept 2026", "unknown")),
])
def test_single_page_sources_do_not_publish_partial_or_undated_entries(name, parser, html):
    with pytest.raises(ValueError):
        parser(CATALOG[name], html)
    with pytest.raises(ValueError):
        parser(CATALOG[name], "<main>Format changed</main>")


def test_antigravity_scope_keeps_surface_in_identity_and_requires_each_surface():
    html = antigravity_row("hub") + antigravity_row("ide") + antigravity_row("cli")
    html += '<article class="release-entry" id="rel-ide-model-gemini"><p>Undated model launch</p></article>'
    rows = feeds.parse_antigravity(CATALOG["google-antigravity"], html)
    assert len(rows) == len({r["release_id"] for r in rows}) == 2
    assert {r["version"] for r in rows} == {"hub/v1.0.0", "ide/v1.0.0"}
    assert all("### Improvements" in r["body"] for r in rows)
    with pytest.raises(ValueError):
        feeds.parse_antigravity(CATALOG["google-antigravity"], antigravity_row("hub"))
    with pytest.raises(ValueError):
        feeds.parse_antigravity(CATALOG["google-antigravity"], html.replace("November 3, 2026", "unknown"))


def test_midjourney_uses_article_publication_not_title_or_sitemap_lastmod(monkeypatch):
    product = CATALOG["midjourney"]
    url = product["url"] + "alpha/"
    xml = f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{url}</loc><lastmod>2026-11-07</lastmod></url></urlset>'
    monkeypatch.setattr(feeds, "get_text", lambda target: xml if target == product["index_url"] else MIDJOURNEY)
    rows = feeds.fetch_trending_releases(product, 1)
    assert rows[0]["date"] == "2026-10-08"
    assert "Subscribe" not in rows[0]["body"]
    with pytest.raises(ValueError):
        feeds.midjourney_urls(product, xml.replace("updates.midjourney.com", "foreign.example"))
    with pytest.raises(ValueError):
        feeds.parse_midjourney(product, url, MIDJOURNEY.replace("article:published_time", "article:modified_time"))


def test_midjourney_preserves_bold_section_boundaries_and_does_not_publish_roadmaps():
    html = MIDJOURNEY.replace("<p>Image generation now supports thinking mode.</p>",
        '<p>🆕 <strong>VIDEO GENERATION</strong>Generate videos from images.</p>'
        '<p><strong>UP NEXT</strong>We plan to add shared folders.</p>')
    row = feeds.parse_midjourney(CATALOG["midjourney"], CATALOG["midjourney"]["url"] + "video/", html)
    assert "### VIDEO GENERATION" in row["body"] and "### UP NEXT" in row["body"]
    cards = extract_cards_from_release(row, load_theme_vocabulary(Path("_scripts/themes.yaml")))
    assert len(cards) == 1 and cards[0]["theme"] == "video-generation"
    assert "UP NEXT" not in cards[0]["title"]


def test_gamma_traverses_cumulative_pages_with_published_filter(monkeypatch):
    calls = []
    def post(url, query):
        calls.append(query)
        return {"result": {"entries": [gamma_entry()] + ([gamma_entry("b", "2025-01-01")] if query["pages"] == 2 else []),
                           "hasNextPage": query["pages"] == 1}}
    monkeypatch.setattr(feeds, "post_json", post)
    rows = feeds.fetch_gamma(CATALOG["gamma"], None)
    assert len(rows) == 2 and len(calls) == 2
    assert all(query["status"] == ["published"] for query in calls)
    assert rows[1]["date"] == "2025-01-01"
    assert rows[0]["body"] == "### Better slides\nCreate presentations from your data."
    assert rows[0]["source_url"] == "https://ideas.gamma.app/changelog/new-a"


@pytest.mark.parametrize("failure", ["repeat", "shift", "draft", "deleted", "no-more-flag"])
def test_gamma_fails_on_incomplete_or_unpublished_response(monkeypatch, failure):
    def post(url, query):
        entry = gamma_entry()
        if failure in {"draft", "deleted"}:
            entry.update(status="draft" if failure == "draft" else "published", deleted=failure == "deleted")
        entries = [entry]
        if failure == "shift" and query["pages"] == 2:
            entries = [gamma_entry("b"), entry]
        return {"result": {"entries": entries, "hasNextPage": None if failure == "no-more-flag" else True}}
    monkeypatch.setattr(feeds, "post_json", post)
    with pytest.raises(ValueError):
        feeds.fetch_gamma(CATALOG["gamma"], None)


def test_manus_follows_public_cursor_checks_total_and_keeps_safe_source_links(monkeypatch):
    calls = []
    def post(url, query):
        assert url == feeds.MANUS_API
        calls.append(query)
        entry = manus_entry("b", "2025-06-01") if query.get("latestUid") else manus_entry()
        if query.get("latestUid"):
            entry["detail"]["button"]["target"] = "https://foreign.example/account"
        result = {"success": True, "data": [entry], "total": "2"}
        if len(calls) == 1:
            result["hasNext"] = True
        return result
    monkeypatch.setattr(feeds, "post_json", post)
    rows = feeds.fetch_manus(CATALOG["manus"], None)
    assert calls == [{"limit": 20}, {"limit": 20, "latestUid": "a"}]
    assert rows[0]["source_url"] == "https://manus.im/blog/new-agent"
    assert rows[1]["source_url"] == CATALOG["manus"]["url"]


@pytest.mark.parametrize("failure", ["repeat", "empty", "wrong-total", "private", "error"])
def test_manus_fails_on_incomplete_or_unexpected_response(monkeypatch, failure):
    def post(url, query):
        entry = manus_entry()
        if failure == "private":
            entry["notificationCategory"] = "CATEGORY_ACCOUNT"
        return {"success": failure != "error", "data": [] if failure == "empty" else [entry],
                "total": 3, "hasNext": failure != "wrong-total"}
    monkeypatch.setattr(feeds, "post_json", post)
    with pytest.raises(ValueError):
        feeds.fetch_manus(CATALOG["manus"], None)


def test_openclaw_dates_come_from_matching_public_release_not_version_number():
    product = CATALOG["openclaw"]
    url = product["url"] + "/2026.11.1"
    metadata = {"tag_name": "v2026.11.1", "published_at": "2026-11-05T10:00:00Z", "draft": False, "prerelease": False}
    row = feeds.parse_openclaw(product, url, OPENCLAW, metadata)
    assert row["date"] == "2026-11-05" and row["version"] == "v2026.11.1"
    assert all(text not in row["body"] for text in ["Thanks", "Release scale", "plain Markdown"])
    assert feeds.parse_openclaw(product, url, OPENCLAW.replace("<h1>v", "<h1>OpenClaw v"), metadata)["date"] == row["date"]
    legacy = '<main class="article"><header class="article-header"><h1>v2026.11.1</h1></header>' + OPENCLAW.replace('<h1>v2026.11.1</h1>', '') + '</main>'
    assert feeds.parse_openclaw(product, url, legacy, metadata)["date"] == row["date"]
    for changes in [{"published_at": ""}, {"tag_name": "v2026.11.2"}, {"draft": True}]:
        with pytest.raises(ValueError):
            feeds.parse_openclaw(product, url, OPENCLAW, {**metadata, **changes})


def test_openclaw_index_ignores_sidebar_duplicates_but_rejects_foreign_links():
    product = CATALOG["openclaw"]
    html = '<nav><a href="/releases/2026.11.1">Sidebar</a></nav><div class="doc"><a href="/releases/2026.11.1">Release</a></div>'
    assert feeds.openclaw_urls(product, html) == [product["url"] + "/2026.11.1"]
    with pytest.raises(ValueError):
        feeds.openclaw_urls(product, html.replace('href="/releases', 'href="https://foreign.example/releases'))


def test_openclaw_category_headings_do_not_become_feature_launches():
    row = feeds.release(CATALOG["openclaw"], "2026-11-05",
        "### Web UI\n\n- Added a sidebar for agent sessions.\n\n- Fixed a missing navigation button.",
        CATALOG["openclaw"]["url"], "v2026.11.1")
    cards = extract_cards_from_release(row, load_theme_vocabulary(Path("_scripts/themes.yaml")))
    assert cards and all(c["title"] != "Web UI" for c in cards)


def test_opencode_traverses_older_pages_and_keeps_same_day_versions(monkeypatch):
    product = CATALOG["opencode"]
    first = opencode_row() + '<a href="/changelog?page=2">Older updates →</a>'
    second = opencode_row("v2.2.5")
    monkeypatch.setattr(feeds, "get_text", lambda url: second if "?" in url else first)
    rows = feeds.fetch_opencode(product, None)
    assert len({r["release_id"] for r in rows}) == 2
    assert all("#1234" not in r["body"] for r in rows)
    assert all("Share MCP connections across projects." in r["body"] for r in rows)
    assert len(feeds.fetch_opencode(product, 1)) == 1


@pytest.mark.parametrize("failure", ["loop", "duplicate", "empty", "unavailable"])
def test_opencode_rejects_incomplete_archive(monkeypatch, failure):
    def get(url):
        if "?" not in url or failure == "loop":
            return opencode_row() + '<a href="/changelog?page=2">Older updates →</a>'
        if failure == "unavailable":
            raise httpx.ConnectError("unavailable")
        return "<main>Format changed</main>" if failure == "empty" else opencode_row()
    monkeypatch.setattr(feeds, "get_text", get)
    with pytest.raises((ValueError, httpx.ConnectError)):
        feeds.fetch_opencode(CATALOG["opencode"], None)


def test_live_collection_marks_only_complete_archives_successful(tmp_path, monkeypatch):
    config = tmp_path / "sources.yaml"
    config.write_text(yaml.safe_dump({"products": [CATALOG["suno"], CATALOG["runway"]]}))
    monkeypatch.setattr(feeds, "get_text", lambda url: SUNO if "suno" in url else "<main>Unavailable</main>")
    result = collect.collect_live(config, tmp_path / "collection.json", None, "all")
    states = {s["product"]: s for s in result["sources"]}
    assert states["suno"]["complete"] and states["suno"]["coverage"] == "available-endpoint"
    assert states["suno"]["known_gaps"] == CATALOG["suno"]["known_gaps"]
    assert not states["runway"]["complete"] and states["runway"]["count"] == 0
    assert {r["product"] for r in result["releases"]} == {"suno"}


@pytest.mark.parametrize("name,title,body,expected", [
    ("suno", "Stem separation", "Stem separation creates editable music tracks.", "music-generation"),
    ("runway", "Video generation", "Generate videos using image-to-video.", "video-generation"),
    ("gamma", "Better presentations", "Create presentations from your outline.", "presentation-creation"),
    ("granola", "Meeting notes", "Meeting notes now include citations.", "meeting-notes"),
    ("granola", "More languages", "Granola now supports 32 languages.", "accessibility-localization"),
    ("suno", "Daily song challenge", "Turn a favorite memory into a song.", "music-generation"),
])
def test_creative_and_meeting_changes_have_relevant_themes(name, title, body, expected):
    row = feeds.release(CATALOG[name], "2026-11-01", f"### {title}\n\n{body}", CATALOG[name]["url"])
    cards = extract_cards_from_release(row, load_theme_vocabulary(Path("_scripts/themes.yaml")))
    assert cards and cards[0]["theme"] == expected
