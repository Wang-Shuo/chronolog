"""Additional official sources must survive collection and the public product filters."""
import json
import hashlib
from pathlib import Path
import subprocess

import pytest
import yaml

from _scripts import collect
from _scripts.extract import extract_cards_from_release, load_theme_vocabulary
from _scripts.writer import quote_markdown, theme_timeline
from _scripts.verify_public import verify

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("extra,missing", [(None,None), ('Products/Continue',None),
                                            ('Changes/Tabby/fixture',None), (None,'Products/OpenHands')])
def test_public_verifier_allows_real_reactivated_products_and_rejects_catalog_mismatches(extra, missing):
    base = 'https://owner.github.io/chronolog'
    pages = {'index':{}, 'Products/Aider':{}, 'Products/OpenHands':{},
             'Changes/Aider/real-change':{}, 'Releases/OpenHands/v1':{}}
    if extra: pages[extra] = {}
    if missing: del pages[missing]
    index = json.dumps(pages).encode()
    rss = f'<rss><channel><item><link>{base}/Changes/Aider/real-change</link></item></channel></rss>'.encode()
    identity = {'commit':'abc', 'kind':'commit-build',
                'product_slugs':['Products/Aider','Products/OpenHands'],
                'content_index_sha256':hashlib.sha256(index).hexdigest(),
                'rss_sha256':hashlib.sha256(rss).hexdigest()}
    files = {base+'/deployment.json':json.dumps(identity).encode(),
             base+'/static/contentIndex.json':index, base+'/index.xml':rss, base+'/':b'Home'}
    if extra or missing:
        with pytest.raises(ValueError, match='catalog'):
            verify(base, 'abc', files.__getitem__)
    else:
        assert verify(base, 'abc', files.__getitem__)['products'] == ['Products/Aider','Products/OpenHands']


def test_stable_github_scope_pages_past_previews_drafts_and_other_packages(monkeypatch):
    def item(tag, **extra):
        return {"tag_name": tag, "published_at": "2026-11-01T10:00:00Z",
                "body": "Added model support.", "html_url": f"https://github.com/org/tool/releases/tag/{tag}",
                **extra}

    pages = [
        [item("v1.2.0", prerelease=True), item("v1.1.0", draft=True, published_at=None)],
        [item("sdk/v1.0.0"), item("pr123-evidence")],
        [item("v1.0.0"), item("v0.9.0")],
    ]
    requested = []

    class Response:
        def __init__(self, items): self.items = items
        def raise_for_status(self): pass
        def json(self): return self.items

    def get(url, **kwargs):
        page = kwargs["params"]["page"]
        requested.append(page)
        assert kwargs["params"]["per_page"] == 2
        return Response(pages[page - 1])

    monkeypatch.setattr(collect.httpx, "get", get)
    releases = collect.fetch_github_releases({
        "name": "tool", "display_name": "Tool", "repo": "org/tool",
        "include_prereleases": False, "tag_pattern": r"^v\d+\.\d+\.\d+$",
    }, 2)
    assert requested == [1, 2, 3]
    assert [r["version"] for r in releases] == ["v1.0.0", "v0.9.0"]


def test_github_large_asset_feeds_can_use_smaller_complete_pages(monkeypatch):
    calls = []

    class Response:
        def raise_for_status(self): pass
        def json(self): return []

    def get(url, **kwargs):
        calls.append(kwargs["params"])
        return Response()

    monkeypatch.setattr(collect.httpx, "get", get)
    collect.fetch_github_releases({"name": "tool", "repo": "org/tool", "github_page_size": 20}, None)
    assert calls == [{"per_page": 20, "page": 1}]


WINDSURF = {
    "name": "windsurf", "display_name": "Windsurf", "feed_type": "windsurf_changelog",
    "url": "https://docs.devin.ai/desktop/changelog",
    "markdown_url": "https://docs.devin.ai/desktop/changelog.md",
    "known_gaps": "Stable desktop releases only; Next previews are excluded.",
}
WINDSURF_NOTES = """# Devin Desktop changelog

**v3.11.238**

October 30, 2026

**New**

* Members can now switch the program on or off from the model picker.

> [accordion] Download 3.11.238

**v3.11.234**

October 29, 2026

**Fixed**

* Reduced memory usage for large Devin Local sessions.

> [accordion] Download 3.11.234

This documentation is built and hosted on [Mintlify](https://mintlify.com).
"""


def test_windsurf_versions_dates_anchors_and_widget_removal():
    releases = collect.parse_windsurf_changelog(WINDSURF, WINDSURF_NOTES)
    assert [r["date"] for r in releases] == ["2026-10-30", "2026-10-29"]
    assert releases[0]["source_url"] == WINDSURF["url"] + "#v3-11-238"
    assert releases[0]["body"].startswith("### New\n")
    assert releases[0]["source_summary"].startswith("Members can now")
    assert all("Download" not in r["body"] and "Mintlify" not in r["body"] for r in releases)
    limited = collect.parse_windsurf_changelog(WINDSURF, WINDSURF_NOTES, 1)
    assert limited == releases[:1]


@pytest.mark.parametrize("text", ["# Changelog", "**v1.2.3**\n\nUnknown date\n\n* Model support.",
                                  "**v1.2.3**\n\nOctober 30, 2026\n\n> [accordion] Download 1.2.3"])
def test_windsurf_fails_closed_on_missing_entries_dates_or_notes(text):
    with pytest.raises(ValueError):
        collect.parse_windsurf_changelog(WINDSURF, text)


def test_windsurf_full_collection_preserves_coverage_and_acquisition(tmp_path, monkeypatch):
    class Response:
        text = WINDSURF_NOTES
        def raise_for_status(self): pass

    def get(url, **kwargs):
        assert url == WINDSURF["markdown_url"]
        return Response()

    monkeypatch.setattr(collect.httpx, "get", get)
    sources = tmp_path / "sources.yaml"
    sources.write_text(yaml.safe_dump({"products": [WINDSURF]}))
    payload = collect.collect_live(sources, tmp_path / "collection.json", None, "all")
    assert not payload["errors"]
    state = payload["sources"][0]
    assert state["complete"] and state["count"] == 2
    assert state["coverage"] == "available-endpoint" and state["acquisition"] == "http"
    assert state["known_gaps"] == WINDSURF["known_gaps"] and state["url"] == WINDSURF["url"]


def test_new_heading_does_not_merge_unrelated_windsurf_features():
    notes = WINDSURF_NOTES.replace(
        "* Members can now switch the program on or off from the model picker.",
        "* Added support for new models in the model picker.\n* Added MCP servers for external integrations.")
    release = collect.parse_windsurf_changelog(WINDSURF, notes)[0]
    cards = extract_cards_from_release(release, load_theme_vocabulary(ROOT / "_scripts/themes.yaml"))
    assert {c["theme"] for c in cards} == {"model-support", "apps-integrations"}
    assert all(c["title"] != "New" for c in cards)


def test_github_attribution_does_not_classify_every_gemini_pr_as_a_model_change():
    quote = "Added MCP servers for external integrations by @model-robot in https://github.com/google-gemini/gemini-cli/pull/123"
    release = collect.normalize_release(
        {"name": "gemini-cli", "display_name": "Gemini CLI"},
        release_date="2026-11-01", version="v1.0.0", title="v1.0.0",
        body=f"## What's Changed\n* {quote}\n\n## New Contributors\n* @model-robot made their first contribution in https://github.com/google-gemini/gemini-cli/pull/123\n\n**Full Changelog**: https://github.com/google-gemini/gemini-cli/compare/v0.9.0...v1.0.0",
        source_url="https://github.com/google-gemini/gemini-cli/releases/tag/v1.0.0", source_type="github_releases")
    cards = extract_cards_from_release(release, load_theme_vocabulary(ROOT / "_scripts/themes.yaml"))
    assert len(cards) == 1 and cards[0]["theme"] == "apps-integrations"
    assert cards[0]["evidence"][0]["quote"] == quote
    assert "by @" not in cards[0]["title"]


def test_theme_timeline_filters_all_twenty_products():
    cards = [{"card_id": f"c{i}", "product_name": f"Product {i:02}", "date": "2026-11-01",
              "title": "New model", "kind": "expansion", "theme": "model-support"}
             for i in range(1, 21)]
    result = theme_timeline(cards, {c["card_id"]: f"Changes/{c['card_id']}" for c in cards})
    assert 'id="tl-only-20"' in result and 'class="tl-product tl-p20"' in result


def test_source_links_without_scheme_are_external_but_code_quotes_stay_verbatim():
    quote = "Read [GPT-5.1](www.openai.com/index/gpt-5-1); code: `[example](www.example.com)`."
    assert quote_markdown(quote) == (
        "Read [GPT-5.1](https://www.openai.com/index/gpt-5-1); code: `[example](www.example.com)`."
    )


def test_publication_scope_comes_from_catalog_and_keeps_fixtures_private(tmp_path):
    # Execute the real Quartz filter with a new, arbitrary catalog entry. A second
    # run disables it without editing TypeScript or rebuilding the bundled code.
    bundle = tmp_path / "filter.cjs"
    subprocess.run(["node", "--input-type=module", "-e", """
import { build } from 'esbuild';
await build({entryPoints: ['_scripts/publication_filter.ts'], bundle: true,
  platform: 'node', format: 'cjs', outfile: process.argv[1]});
""", str(bundle)], cwd=ROOT, check=True, capture_output=True)
    (tmp_path / "_scripts").mkdir()
    config = tmp_path / "_scripts/sources.yaml"
    probe = """
const { ActiveChronolog } = require(process.argv[1]);
const publish = meta => ActiveChronolog().shouldPublish({}, [null, {data:{frontmatter:meta}}]);
console.log(JSON.stringify([
  publish({product:'future', product_name:'Future Tool'}),
  publish({product:'future', product_name:'Future Tool', source_type:'fixture'}),
  publish({product:'future', superseded:true}),
  publish({product:'unknown'}), publish({title:'About'})
]));
"""
    for enabled in (True, False):
        config.write_text(yaml.safe_dump({"products": [
            {"name": "future", "display_name": "Future Tool", "enabled": enabled}]}))
        result = subprocess.check_output(["node", "-e", probe, str(bundle)], cwd=tmp_path, text=True)
        assert json.loads(result) == [enabled, False, False, False, True]
