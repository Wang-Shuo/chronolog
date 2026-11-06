"""Product dates and complete archive traversal are publication boundaries."""
from pathlib import Path

import pytest
import yaml

from _scripts import collect, product_feeds as feeds
from _scripts.extract import extract_cards_from_release, load_theme_vocabulary


def product(name):
    return next(p for p in collect.load_sources(Path('_scripts/sources.yaml')) if p['name'] == name)


def test_claude_uses_entry_dates_not_updated_time_and_preserves_feature_headings():
    html = '''<main><time datetime="2026-11-06">Updated today</time><article>
    <h2>November 2026</h2><h3 id="november-5">November 5, 2026</h3>
    <p><b>Memory across chats</b></p><p>Added saved memory across conversations.</p>
    <p><b>New privacy controls</b></p><p>Added privacy controls for shared projects.</p>
    <h2>October 2026</h2><h3 id="october-1">October 1, 2026</h3>
    <p><b>Voice mode</b></p><p>Added voice conversations.</p>
    <p>Note: Refer to our docs for historical release notes.</p></article>
    <h3>Related Articles</h3><p>Not a release.</p></main>'''
    releases = feeds.parse_html(product('claude'), html)
    assert [r['date'] for r in releases] == ['2026-11-05', '2026-10-01']
    assert releases[0]['source_url'].endswith('#november-5')
    assert '### Memory across chats' in releases[0]['body']
    assert all('Related Articles' not in r['body'] and 'historical release notes' not in r['body'] for r in releases)
    cards = extract_cards_from_release(releases[0], load_theme_vocabulary('_scripts/themes.yaml'))
    assert {c['theme'] for c in cards} == {'memory', 'safety-privacy'}


def test_gemini_uses_dotted_dates_and_keeps_multiple_features_on_one_date():
    html = '''<nav><h2>2026.12.31</h2></nav><main><h1>Release Notes</h1>
    <h2>2026.10.13</h2><h3>New voice controls</h3><ul><li><p>What: Added voice controls.</p></li></ul>
    <h3>Image generation</h3><p>Generate images in conversations.</p>
    <h2>2026.09.01</h2><h3>Saved memory</h3><p>Added saved memory.</p></main>'''
    releases = feeds.parse_html(product('gemini'), html)
    assert [r['date'] for r in releases] == ['2026-10-13', '2026-09-01']
    assert releases[0]['body'].count('What: Added voice controls.') == 1
    assert '### Image generation' in releases[0]['body']
    assert feeds.parse_html(product('gemini'), html, 1) == releases[:1]


def test_deepseek_preserves_date_anchors_and_excludes_benchmark_tables():
    html = '''<article><h1>Change Log</h1><h2 id="date-2026-10-17">Date: 2026-10-17&#8203;</h2>
    <h3>Search API</h3><p>Added a web search API.</p><table><tr><td>99.9 benchmark score</td></tr></table>
    <h2 id="date-2025-12-01">Date: 2025-12-01</h2><h3>Model update</h3><p>Added a reasoning model.</p>
    </article>'''
    releases = feeds.parse_html(product('deepseek-api'), html)
    assert releases[0]['source_url'].endswith('#date-2026-10-17')
    assert '99.9' not in releases[0]['body'] and '\u200b' not in releases[0]['body']


def test_v0_keeps_distinct_same_day_articles_and_real_anchors():
    def article(anchor, title):
        return f'''<article id="{anchor}"><h2>{title}</h2><aside><time datetime="2026-10-19">Oct 19</time>
        <button>Copy link</button></aside><div class="prose"><p>Added MCP integrations.</p></div></article>'''
    releases = feeds.parse_html(product('v0'), article('slack', 'Slack integration') + article('linear', 'Linear integration'))
    assert len(releases) == 2 and len({r['release_id'] for r in releases}) == 2
    assert {r['source_url'].split('#')[-1] for r in releases} == {'slack', 'linear'}
    assert all('Copy link' not in r['body'] for r in releases)


@pytest.mark.parametrize('name,html', [
    ('claude', '<article><h3>November 41, 2026</h3><p>Added memory.</p></article>'),
    ('gemini', '<main><h2>2026.99.13</h2><p>Added voice.</p></main>'),
    ('deepseek-api', '<article><h2>Date: missing</h2><p>Added search.</p></article>'),
    ('v0', '<article id="item"><h2>Added MCP</h2><div class="prose">Notes</div></article>'),
    ('gemini', '<html><h1>Sign in</h1></html>'),
    ('claude', '<article><h3>November 5, 2026</h3></article>'),
])
def test_html_sources_fail_closed_on_changed_or_incomplete_markup(name, html):
    with pytest.raises(ValueError):
        feeds.parse_html(product(name), html)


def test_lovable_uses_explicit_years_and_cleans_docs_widgets_and_relative_links():
    markdown = '''> ## Documentation Index
> Ignore these hosting instructions.
# Lovable changelog
**Jan 2, 2026**
### Project memory
Added [saved memory](/features/memory) to projects.
<CardGroup><Card>Read another guide.</Card></CardGroup>
**Dec 30, 2025**
### Connectors
Added MCP connectors.
This documentation is built and hosted on a platform.
'''
    releases = feeds.parse_lovable(product('lovable'), markdown)
    assert [r['date'] for r in releases] == ['2026-01-02', '2025-12-30']
    assert '(https://docs.lovable.dev/features/memory)' in releases[0]['body']
    assert all('hosting instructions' not in r['body'] and 'Read another guide' not in r['body'] and 'hosted' not in r['body'] for r in releases)
    assert feeds.parse_lovable(product('lovable'), markdown, 1) == releases[:1]


@pytest.mark.parametrize('text', ['# Changelog', '**Jan 44, 2026**\n### Memory\nAdded memory.',
                                 '**Jan 2, 2026**\n<Card>Only navigation</Card>',
                                 '**Jan 2, 2026**\nAdded memory.\n**Jan 2, 2026**\nAdded voice.'])
def test_lovable_rejects_empty_invalid_and_duplicate_entries(text):
    with pytest.raises(ValueError):
        feeds.parse_lovable(product('lovable'), text)


ELEVEN_INDEX = '''# Changelog
## Entries
- [November 2, 2026](https://elevenlabs.io/docs/changelog/2026/11/2.md)
- [October 13, 2024](https://elevenlabs.io/docs/changelog/2024/10/13.md)
'''


def test_elevenlabs_follows_full_index_including_older_entries(monkeypatch):
    calls = []
    def get(url):
        calls.append(url)
        if url.endswith('llms.txt'): return ELEVEN_INDEX
        return '### Voice generation\nAdded a voice model.\n<Card>Guide link</Card>'
    monkeypatch.setattr(feeds, 'get_text', get)
    releases = feeds.fetch_product_releases(product('elevenlabs'), None)
    assert [r['date'] for r in releases] == ['2026-11-02', '2024-10-13']
    assert len(calls) == 3 and all(not r['source_url'].endswith('.md') for r in releases)
    calls.clear()
    assert feeds.fetch_product_releases(product('elevenlabs'), 1) == releases[:1]
    assert len(calls) == 2


@pytest.mark.parametrize('replacement', [
    'https://untrusted.example/docs/changelog/2026/11/2.md',
    'https://elevenlabs.io/docs/changelog/2026/11/3.md',
])
def test_index_rejects_foreign_hosts_or_mismatched_dates(replacement):
    with pytest.raises(ValueError):
        feeds.indexed_entries(product('elevenlabs'), ELEVEN_INDEX.replace('https://elevenlabs.io/docs/changelog/2026/11/2.md', replacement))


def test_failed_archive_entry_does_not_publish_an_incomplete_full_source(tmp_path, monkeypatch):
    def get(url):
        if url.endswith('llms.txt'): return ELEVEN_INDEX
        if '/2024/' in url: raise RuntimeError('Archive entry unavailable')
        return '### Voice generation\nAdded a voice model.'
    monkeypatch.setattr(feeds, 'get_text', get)
    config = tmp_path / 'sources.yaml'
    config.write_text(yaml.safe_dump({'products': [product('elevenlabs')]}))
    payload = collect.collect_live(config, tmp_path / 'collection.json', None, 'all')
    assert payload['releases'] == [] and payload['errors']
    assert not payload['sources'][0]['complete']


def test_replit_sitemap_filters_docs_and_validates_publication_date():
    sitemap = '''<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>https://docs.replit.com/updates/2026/10/30/changelog</loc><lastmod>2026-11-06</lastmod></url>
    <url><loc>https://docs.replit.com/build/publish-your-app</loc></url></urlset>'''
    entries = feeds.indexed_entries(product('replit'), sitemap)
    assert entries == [('2026-10-30', 'https://docs.replit.com/updates/2026/10/30/changelog.md')]
    markdown = '# October 30, 2026\n## What\'s new\n* [Agent](#agent)\n### Agent\nAdded cloud agents.'
    item = feeds.parse_indexed_entry(product('replit'), *entries[0], markdown)
    assert item['date'] == '2026-10-30' and '[Agent](#agent)' not in item['body']
    with pytest.raises(ValueError, match='date'):
        feeds.parse_indexed_entry(product('replit'), *entries[0], markdown.replace('30,', '29,'))
    # Early official entries have a dated H1 followed by bullets, without H2/H3.
    old_style = '# October 30, 2026\n* Added agent integrations.'
    assert 'Added agent integrations.' in feeds.parse_indexed_entry(product('replit'), *entries[0], old_style)['body']
    with pytest.raises(ValueError, match='no release notes'):
        feeds.parse_indexed_entry(product('replit'), *entries[0], '# October 30, 2026')


@pytest.mark.parametrize('markdown', ['<!DOCTYPE html><html>Unavailable</html>', 'No release notes found.'])
def test_indexed_entry_rejects_html_errors_and_empty_markdown(markdown):
    with pytest.raises(ValueError):
        feeds.parse_indexed_entry(product('elevenlabs'), '2026-11-02',
                                  'https://elevenlabs.io/docs/changelog/2026/11/2.md', markdown)


def test_gemini_app_name_does_not_turn_voice_and_memory_updates_into_model_changes():
    html = '''<main><h2>2026.10.13</h2><h3>Gemini Live voice conversations</h3>
    <p>Gemini now supports natural voice conversations.</p>
    <h3>Saved memory in Gemini</h3><p>Gemini remembers your preferences with saved memory.</p>
    <h3>Gemini 4 Argon</h3><p>Introducing our newest model.</p></main>'''
    item = feeds.parse_html(product('gemini'), html)[0]
    cards = extract_cards_from_release(item, load_theme_vocabulary('_scripts/themes.yaml'))
    assert {c['theme'] for c in cards} == {'voice', 'memory', 'model-support'}
    quotes = [e['quote'] for c in cards for e in c['evidence']]
    assert 'Gemini now supports natural voice conversations.' in quotes
    assert 'Gemini remembers your preferences with saved memory.' in quotes
    assert all('the app' not in quote for quote in quotes)


def test_html_audit_still_rejects_links_to_excluded_content(tmp_path):
    from tests.manual.check_m2_publication import audit_html
    (tmp_path / 'index.html').write_text('<a href="/Products/Fixture">Fixture</a>')
    (tmp_path / 'Products').mkdir()
    (tmp_path / 'Products/Fixture.html').write_text('<p>Fixture</p>')
    with pytest.raises(AssertionError, match='excluded content'):
        audit_html(tmp_path, 'example.com', ['Products/Fixture'])


def test_new_github_sources_ignore_release_automation_and_interpret_runtime_memory():
    vocabulary = load_theme_vocabulary('_scripts/themes.yaml')
    def github(name, body):
        return collect.normalize_release(product(name), release_date='2026-11-01', version='v1.0.0',
            title='v1.0.0', body=body, source_url='https://github.com/official/product/releases/tag/v1.0.0',
            source_type='github_releases')
    assert extract_cards_from_release(github('open-webui', 'Automatically created new release'), vocabulary) == []
    cards = extract_cards_from_release(github('ollama', '* Models stay loaded in memory between requests.'), vocabulary)
    assert len(cards) == 1 and cards[0]['theme'] == 'reliability-performance'
    cards = extract_cards_from_release(github('ollama', '* Added persistent memory to remember user preferences.'), vocabulary)
    assert len(cards) == 1 and cards[0]['theme'] == 'memory'


def test_deepseek_search_api_is_a_search_change():
    html = '<article><h2>Date: 2026-10-17</h2><h3>Opening up the in-house search API</h3><p>Added access to our search engine.</p></article>'
    cards = extract_cards_from_release(feeds.parse_html(product('deepseek-api'), html)[0],
                                      load_theme_vocabulary('_scripts/themes.yaml'))
    assert len(cards) == 1 and cards[0]['theme'] == 'search-browsing'


def test_double_underscore_directory_names_cannot_split_wiki_aliases():
    from _scripts.writer import card_link, wiki_label
    title = 'Reorganize specs into __tests__ and keep snake_case names'
    assert wiki_label(title) == 'Reorganize specs into tests and keep snake_case names'
    assert card_link({'card_id': 'dify-change', 'title': title},
                     {'dify-change': 'Changes/Dify/reorganize'}) == (
        '[[Changes/Dify/reorganize|Reorganize specs into tests and keep snake_case names]]')


@pytest.mark.parametrize('heading', ['Misc.', 'All changes'])
def test_generic_app_changelog_groups_do_not_become_feature_titles(heading):
    item = feeds.release(product('v0'), '2026-11-01',
        f'### {heading}\n\n- Added model support for Claude.\n- Added MCP integrations.',
        'https://v0.app/changelog#update')
    cards = extract_cards_from_release(item, load_theme_vocabulary('_scripts/themes.yaml'))
    assert len(cards) == 2
    assert {card['theme'] for card in cards} == {'model-support', 'apps-integrations'}
    assert all(card['title'] != heading for card in cards)
