from pathlib import Path

import httpx
import pytest
import yaml

from _scripts import collect, extended_feeds as feeds, trending_feeds
from _scripts.extract import extract_cards_from_release, load_theme_vocabulary


CATALOG = {p["name"]: p for p in collect.load_sources(Path("_scripts/sources.yaml"))}


def notion_row(slug="2026-11-01", date="November 1, 2026"):
    return (f'<article><div><time>{date}</time></div><a href="/releases/{slug}"><h2>Agent updates</h2></a>'
            '<article><p>The agent now searches your workspace.</p>'
            '<p>Coming soon: shared memory.<br><br>Your team will remember preferences.</p>'
            '<div role="alert"><p>Uh-oh! Video player failed.</p></div></article></article>')


def synthesia_row(slug="dubbing", date="10/27/2026"):
    return (f'<div class="w-dyn-item"><h2>New video dubbing</h2><p class="paragraph-small">'
            f'Dub videos in more languages.</p><p class="caption-medium">{date}</p>'
            f'<a href="/updates/{slug}">Read more</a></div>')


def heygen_row(slug="voice", timestamp="1793208900000"):
    return (f'<a href="/publications/{slug}"><article class="listing-post">'
            f'<span class="publication-time">{timestamp}</span><h1>New voice</h1></article></a>')


HEYGEN_POST = ('<article class="post"><header class="post-header"><h1>New voice</h1>'
               '<p class="publication-time">1793208900000</p></header><section class="post-content">'
               '<p>Voice cloning now preserves emotion.</p></section>'
               '<p>Did you like this update?</p></article>')
QODER = '<Update label="November 6, 2026" description="Qoder 0.5.6">\n    ### Improvements\n\n    - Supports MCP tools.\n</Update>'
KIMI = '## 2.5.2 (2026-11-06)\n\n### Bug Fixes\n\n- Fixed duplicate tool errors.\n\n## 2.5.1 (2026-11-06)\n\n- Added model support.'
ZAI = '**2026-08-26**\n\nGLM-5.3-Flash\n\n* Added native visual capabilities.\n\n**2026-08-18**\n\nGLM-5.3\n\n* Improved coding support.'


def m365_panel(body, panel="all"):
    return (f'<section role="tabpanel" id="tabpanel_1_{panel}"><h2 id="november-4-2026">'
            f'November 4, 2026</h2><h3>Excel</h3>{body}</section>')


M365_FEATURE = ('<ul><li><p><strong>Edit workbooks</strong> [Web]</p>'
                '<p>Copilot now edits your workbook.</p><p><strong>Details:</strong></p>'
                '<ul><li>Click a button to try this.</li></ul></li></ul>')


def test_notion_uses_publication_date_and_keeps_roadmap_out_of_cards():
    rows, next_url = feeds.parse_notion(CATALOG["notion"], notion_row() + '<a href="/releases/page/2">Next page</a>')
    assert len(rows) == 1 and rows[0]["date"] == "2026-11-01"
    assert next_url == "https://www.notion.com/releases/page/2"
    assert "Video player" not in rows[0]["body"]
    assert "Coming soon" in rows[0]["body"] and "remember preferences" in rows[0]["body"]
    cards = extract_cards_from_release(rows[0], load_theme_vocabulary(Path("_scripts/themes.yaml")))
    assert cards and all("Coming soon" not in str(card["evidence"]) for card in cards)
    assert all("remember preferences" not in str(card["evidence"]) for card in cards)


def test_synthesia_uses_dated_index_summaries_and_omits_separate_undated_hero():
    html = '<div class="w-dyn-item" hero-update><h2>Undated announcement</h2></div>' + synthesia_row()
    rows, url = feeds.parse_synthesia(CATALOG["synthesia"], html)
    assert len(rows) == 1 and url is None and rows[0]["date"] == "2026-10-27"
    assert rows[0]["source_url"] == "https://www.synthesia.io/updates/dubbing"
    assert rows[0]["body"] == "Dub videos in more languages."


@pytest.mark.parametrize("product", ["heygen", "synthesia", "descript"])
def test_video_products_classify_explicit_generation_as_video(product):
    row = feeds.release(CATALOG[product], "2026-11-01", "Generate videos from a text prompt.", CATALOG[product]["url"])
    cards = extract_cards_from_release(row, load_theme_vocabulary(Path("_scripts/themes.yaml")))
    assert len(cards) == 1 and cards[0]["theme"] == "video-generation"


@pytest.mark.parametrize("name,parser,html", [
    ("notion", feeds.parse_notion, notion_row(date="unknown")),
    ("notion", feeds.parse_notion, notion_row().replace('<article><p>', '<div><p>').replace('</p></div></article></article>', '</p></div></div></article>')),
    ("synthesia", feeds.parse_synthesia, synthesia_row(date="10/42/2026")),
    ("synthesia", feeds.parse_synthesia, synthesia_row().replace('class="paragraph-small"', 'class="changed"')),
])
def test_html_sources_fail_on_missing_schema_or_dates(name, parser, html):
    with pytest.raises(ValueError):
        parser(CATALOG[name], html)
    with pytest.raises(ValueError):
        parser(CATALOG[name], "<main>Format changed</main>")


@pytest.mark.parametrize("name,row,pager", [
    ("notion", notion_row, '<a href="/releases/page/2">Next page</a>'),
    ("synthesia", synthesia_row, '<a class="w-pagination-next" href="?b5ee831f_page=2">Load more</a>'),
])
def test_paginated_archives_reach_terminal_page_before_marking_complete(monkeypatch, name, row, pager):
    calls = []
    def get(url):
        calls.append(url)
        return row() + pager if len(calls) == 1 else row("older")
    monkeypatch.setattr(feeds, "get_text", get)
    rows = feeds.fetch_extended_releases(CATALOG[name], None)
    assert len(calls) == len(rows) == 2
    assert len({r["release_id"] for r in rows}) == 2


@pytest.mark.parametrize("failure", ["repeat", "loop", "foreign", "empty", "unavailable"])
def test_paginated_archives_reject_partial_or_repeated_history(monkeypatch, failure):
    def get(url):
        if url == CATALOG["notion"]["url"]:
            href = 'https://foreign.example/releases/page/2' if failure == "foreign" else '/releases/page/2'
            return notion_row() + f'<a href="{href}">Next page</a>'
        if failure == "unavailable":
            raise httpx.ConnectError("page unavailable")
        if failure == "empty":
            return "<main>No releases</main>"
        return notion_row("older") + '<a href="/releases/page/2">Next page</a>' if failure == "loop" else notion_row()
    monkeypatch.setattr(feeds, "get_text", get)
    with pytest.raises((ValueError, httpx.ConnectError)):
        feeds.fetch_extended_releases(CATALOG["notion"], None)


def test_heygen_follows_cursor_and_checks_article_publication_metadata(monkeypatch):
    def get(url):
        if "/publications/" in url:
            return HEYGEN_POST
        if "after=" in url:
            return heygen_row("older")
        return heygen_row() + '<a href="?after=abc_123">Older</a>'
    monkeypatch.setattr(feeds, "get_text", get)
    rows = feeds.fetch_extended_releases(CATALOG["heygen"], None)
    assert len(rows) == 2 and all(r["date"] == "2026-10-28" for r in rows)
    assert all("Did you like" not in r["body"] for r in rows)
    entry = {"date": "2026-10-28", "title": "New voice", "url": CATALOG["heygen"]["url"] + "publications/voice"}
    for html in [HEYGEN_POST.replace("1793208900000", "1793295300000"), HEYGEN_POST.replace("New voice", "Wrong title")]:
        with pytest.raises(ValueError):
            feeds.parse_heygen(CATALOG["heygen"], entry, html)
    with pytest.raises(ValueError):
        feeds.heygen_index(CATALOG["heygen"], heygen_row(timestamp="unknown"))


def test_qoder_uses_explicit_date_and_version_with_mdx_indentation_removed():
    rows = feeds.parse_qoder(CATALOG["qoder"], QODER)
    assert rows[0]["date"] == "2026-11-06" and rows[0]["version"] == "0.5.6"
    assert rows[0]["source_url"] == "https://changelog.qoder.com/app#0.5.6"
    assert "\n    -" not in rows[0]["body"]


def test_kimi_keeps_same_day_versions_and_ignores_unreleased_draft():
    rows = feeds.parse_kimi_code(CATALOG["kimi-code"], '## Unreleased\n- Future tools.\n\n' + KIMI)
    assert len({r["release_id"] for r in rows}) == 2
    assert {r["version"] for r in rows} == {"2.5.2", "2.5.1"}
    assert all("Future" not in r["body"] for r in rows)


def test_kimi_category_headings_are_not_published_as_features():
    row = feeds.parse_kimi_code(CATALOG["kimi-code"], '## 2.5.2 (2026-11-06)\n### Polish\n- Added support for Claude Sonnet models.')[0]
    cards = extract_cards_from_release(row, load_theme_vocabulary(Path("_scripts/themes.yaml")))
    assert cards and all(c["title"] != "Polish" for c in cards)


def test_zai_keeps_model_names_and_removes_hosting_metadata():
    rows = feeds.parse_zai(CATALOG["zai-api"], ZAI + '\n\nThis documentation is built and hosted on Mintlify.')
    assert rows[0]["title"] == "GLM-5.3-Flash" and rows[-1]["date"] == "2026-08-18"
    assert all("Mintlify" not in r["body"] for r in rows)


@pytest.mark.parametrize("name,parser,text", [
    ("qoder", feeds.parse_qoder, QODER.replace("November 6, 2026", "November 2026")),
    ("qoder", feeds.parse_qoder, QODER.replace("</Update>", "")),
    ("qoder", feeds.parse_qoder, QODER + QODER),
    ("kimi-code", feeds.parse_kimi_code, KIMI.replace("2026-11-06", "2026-02-30")),
    ("kimi-code", feeds.parse_kimi_code, KIMI.replace("2.5.1", "2.5.2")),
    ("zai-api", feeds.parse_zai, ZAI.replace("2026-08-26", "2026-08-99")),
    ("zai-api", feeds.parse_zai, ZAI.replace("2026-08-26", "August 2026")),
    ("zai-api", feeds.parse_zai, ZAI.replace("GLM-5.3-Flash", "")),
])
def test_markdown_sources_fail_closed(name, parser, text):
    with pytest.raises(ValueError):
        parser(CATALOG[name], text)
    with pytest.raises(ValueError):
        parser(CATALOG[name], "# Changelog\nFormat changed")


def test_m365_deduplicates_platform_tabs_and_excludes_setup_steps():
    html = m365_panel(M365_FEATURE) + m365_panel(M365_FEATURE, "win")
    rows = feeds.parse_m365_copilot(CATALOG["microsoft-365-copilot"], html)
    assert len(rows) == 1 and rows[0]["body"] == '### Edit workbooks [Web] (Excel)\n\nCopilot now edits your workbook.'
    assert rows[0]["source_url"].endswith("#november-4-2026")
    cards = extract_cards_from_release(rows[0], load_theme_vocabulary(Path("_scripts/themes.yaml")))
    assert cards and cards[0]["title"].startswith("Edit workbooks")


@pytest.mark.parametrize("body", [
    '<ul><li><strong>Edit workbooks</strong></li></ul><p>Copilot now edits your workbook.</p>',
    '<ul><li><p>**Edit workbooks ** [Web]</p><p>Copilot now edits your workbook.</p></li></ul>',
    '<ul><li><p><strong>Edit workbooks</strong> [Web] Copilot now edits your workbook.</p><p><strong>Details:</strong></p></li></ul>',
    M365_FEATURE.replace('<p>Copilot now', '<p><strong>Roadmap ID:</strong> 123</p><p>Copilot now'),
])
def test_m365_handles_official_summary_markup_variants(body):
    rows = feeds.parse_m365_copilot(CATALOG["microsoft-365-copilot"], m365_panel(body))
    assert 'Copilot now edits your workbook.' in rows[0]["body"]
    assert 'Roadmap ID:' not in rows[0]["body"]


def test_m365_requires_all_features_tab_and_real_summary():
    for html in [m365_panel(M365_FEATURE, "win"), m365_panel(M365_FEATURE.replace('<p>Copilot now edits your workbook.</p>', ''))]:
        with pytest.raises(ValueError):
            feeds.parse_m365_copilot(CATALOG["microsoft-365-copilot"], html)


def test_descript_reuses_published_canny_archive_without_gamma_source_type(monkeypatch):
    entry = {"_id": "a", "urlName": "new-tools", "title": "New tools", "status": "published",
             "types": ["new", "improved", "fixed"],
             "publishedAt": "2026-11-06", "details": "Video editing now supports new tools."}
    monkeypatch.setattr(trending_feeds, "post_json", lambda url, payload: {"result": {"entries": [entry], "hasNextPage": False}})
    rows = feeds.fetch_extended_releases(CATALOG["descript"], None)
    assert rows[0]["source_type"] == "canny_changelog"
    assert rows[0]["source_url"] == "https://feedback.descript.com/changelog/new-tools"


def test_descript_retains_official_titles_for_media_only_or_empty_notes(monkeypatch):
    entry = {"_id": "a", "urlName": "new-tools", "title": "New tools", "status": "published",
             "types": ["new", "improved", "fixed"],
             "publishedAt": "2026-11-06", "details": "Video editing now supports new tools."}
    media = {**entry, "_id": "b", "title": "Added subtitle export", "details": "![video](https://fast.wistia.net/embed/iframe/example)"}
    monkeypatch.setattr(trending_feeds, "post_json", lambda url, payload: {"result": {"entries": [entry, media], "hasNextPage": False}})
    rows = feeds.fetch_extended_releases(CATALOG["descript"], None)
    assert len(rows) == 2 and any(r["body"] == "Added subtitle export" for r in rows)
    media["details"] = ""
    assert len(feeds.fetch_extended_releases(CATALOG["descript"], None)) == 2
    media["details"] = "<div> </div>"
    with pytest.raises(ValueError):
        feeds.fetch_extended_releases(CATALOG["descript"], None)


@pytest.mark.parametrize("failure", [None, "wrong-type", "changed-content"])
def test_canny_type_partitions_are_complete_and_overlaps_must_agree(monkeypatch, failure):
    calls = []
    def post(url, query):
        calls.append(query)
        entry = {"_id": "shared", "urlName": "shared", "title": "New tools", "status": "published",
                 "types": ["new", "improved", "fixed"], "publishedAt": "2026-11-06",
                 "details": "Video editing now supports new tools."}
        if failure == "wrong-type":
            entry["types"] = ["private"]
        if failure == "changed-content" and query["type"] == "fixed":
            entry["details"] = "Changed source content during pagination."
        return {"result": {"entries": [entry], "hasNextPage": False}}
    monkeypatch.setattr(trending_feeds, "post_json", post)
    if failure:
        with pytest.raises(ValueError):
            feeds.fetch_extended_releases(CATALOG["descript"], None)
    else:
        rows = feeds.fetch_extended_releases(CATALOG["descript"], None)
        assert len(rows) == 1 and {q["type"] for q in calls} == {"new", "improved", "fixed"}
        assert all(q["status"] == ["published"] for q in calls)


def test_live_collection_never_labels_failed_archive_complete(tmp_path, monkeypatch):
    config = tmp_path / "sources.yaml"
    config.write_text(yaml.safe_dump({"products": [CATALOG["qoder"], CATALOG["notion"]]}))
    monkeypatch.setattr(feeds, "get_text", lambda url: QODER if url.endswith("app.md") else "Unavailable")
    payload = collect.collect_live(config, tmp_path / "collection.json", None, "all")
    states = {s["product"]: s for s in payload["sources"]}
    assert states["qoder"]["complete"] and states["qoder"]["coverage"] == "available-endpoint"
    assert not states["notion"]["complete"] and payload["errors"]
