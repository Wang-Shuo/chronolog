"""Fixed semantic expectations and publication regressions, not a human sign-off."""
import gzip
import json
import re
from collections import Counter
from pathlib import Path

from _scripts.analyze_a import analyze_products
from _scripts.analyze_b import analyze_themes
from _scripts.common import normalize_text
from _scripts.editorial import (attach_editorial, load_editorial, render_coverage,
                                render_coverage_summary, source_coverage)
from _scripts.extract import extract_cards_from_release, load_review_decisions, load_theme_vocabulary
from _scripts.validate import validate_card

ROOT = Path(__file__).resolve().parents[1]


def inputs():
    payload = json.loads(gzip.decompress((ROOT / 'docs/acceptance/m2-evidence/collection.json.gz').read_bytes()))
    themes = load_theme_vocabulary(ROOT / '_scripts/themes.yaml')
    review = load_review_decisions(ROOT / '_scripts/backfill_review.yaml', themes)
    review.update(load_review_decisions(ROOT / '_scripts/m2_review.yaml', themes))
    return payload, themes, review


def test_fixed_sixty_card_golden_set():
    # W2 card definition: a sample is located by (source_release, quote), since a quote
    # may now be one of several evidence lines of a feature, paragraph or digest card.
    payload, themes, review = inputs()
    releases = {r['release_id']: r for r in payload['releases']}
    samples = json.loads((ROOT / 'tests/golden/m2/cards.json').read_text())['cards']
    assert Counter(s['product'] for s in samples) == {'chatgpt':20, 'claude-code':20, 'cursor':20}
    retained = 0
    for sample in samples:
        release = releases[sample['source_release']]
        assert sample['source_url'] == release['source_url']
        quote = normalize_text(sample['quote'])
        assert quote in normalize_text(release['body'])
        cards = extract_cards_from_release(release, themes, review)
        published = [c for c in cards if c['theme'] != '__candidate__']
        holders = [c for c in published
                   if any(quote in normalize_text(e['quote']) for e in c['evidence'])]
        if sample['expected_theme'] == 'skip':
            assert not holders, sample['card_id']
            continue
        assert len(holders) == 1, sample['card_id']
        card = holders[0]
        assert not validate_card(card, set(themes)), sample['card_id']
        assert all(e['source_release'] == release['source_url'] for e in card['evidence'])
        if card['theme'] == sample['expected_theme']:
            retained += 1
    assert retained >= 55


def test_twenty_historical_edges_do_not_infer_semantics_from_chronology():
    cases = json.loads((ROOT / 'tests/golden/m2/relations.json').read_text())['cases']
    assert Counter(c['before_relation'] for c in cases) == {'evolves_from':10, 'cross_product':10}
    for case in cases:
        cards = [case['left'], case['right']]
        assert analyze_products(cards)['evolves_from'] == {}
        patches = analyze_themes(cards)['cards']
        for patch in patches.values():
            assert patch['diffusion']['role'] in {'first-observed', 'later-observed'}
            assert patch['diffusion']['relation'] == 'same-theme-chronology'
            assert patch['diffusion']['scope'] == 'tracked-products-only'


def test_specific_headings_and_duplicate_lines_are_not_independent_events():
    _, themes, _ = inputs()
    release = {'release_id':'cursor-2026-01-01-test','product':'cursor','product_name':'Cursor',
               'source_type':'cursor_changelog','date':'2026-01-01','title':'Agent update',
               'source_url':'https://cursor.com/changelog/test',
               'body':'#Background Agent\nAgent can now run tests in the background.\nAgent can now run tests in the background!'}
    cards = extract_cards_from_release(release, themes)
    assert len(cards) == 1
    assert cards[0]['description'].startswith('Cursor — Agent update:')
    assert not cards[0]['evidence'][0]['quote'].startswith('#')


def test_coverage_distinguishes_snapshot_acquisition_from_processing_and_release():
    release = {'date':'2026-09-29'}
    state = source_coverage({'status':'success','acquisition':'browser-snapshot',
                            'acquired_at':'2026-10-13T10:59:17Z','collected_at':'2026-11-01T00:00:00Z'},[release])
    text = render_coverage(state)
    assert '2026-10-13' in text and '2026-09-29' in text
    assert '2026-11-01' not in text
    assert 'not a successful automatic HTTP fetch' in text
    replay = source_coverage({'status':'success','coverage':'historical-snapshot','collected_at':'2027-01-01'},[release],state)
    assert replay['snapshot_captured_at'] == state['snapshot_captured_at']


def test_coverage_summary_is_one_reader_line_without_acquisition_times():
    state = source_coverage({'status':'success','acquisition':'http','acquired_at':'2026-10-15T01:55:15Z',
                             'url':'https://api.github.com/repos/anthropics/claude-code/releases',
                             'known_gaps':'GitHub Releases starts at v2.0.73.'},
                            [{'date':'2025-12-19'},{'date':'2026-10-14'}])
    line = render_coverage_summary(state, 2)
    assert line == ('2 releases · 2025-12-19 → 2026-10-14 · '
                    '[official source](https://github.com/anthropics/claude-code/releases) · '
                    'GitHub Releases starts at v2.0.73.')
    assert '\n' not in line and '01:55' not in line
    assert render_coverage_summary({}, 1) == '1 release'


def test_curated_eras_have_actual_announcement_evidence():
    payload, themes, review = inputs()
    cards = [c for r in payload['releases'] for c in extract_cards_from_release(r,themes,review)]
    analysis = analyze_products(cards)
    editorial = load_editorial(ROOT)
    attach_editorial(analysis, payload['releases'], editorial)
    # Every curated era of every product survives: all its releases are archived.
    for product, count in (('chatgpt', 5), ('cursor', 5), ('claude-code', 3)):
        eras = analysis['products'][product]['eras']
        assert len(eras) == count == len(editorial['products'][product]['eras']), product
        for era in eras:
            assert 1 <= len(era['evidence']) <= 3, era['name']
            assert all(e['url'].startswith(('https://help.openai.com/', 'https://cursor.com/changelog/',
                                            'https://github.com/anthropics/claude-code/releases/tag/'))
                       for e in era['evidence']), era['name']
            assert era['from'] == min(e['date'] for e in era['evidence']), era['name']
            assert era['to'] is None or max(e['date'] for e in era['evidence']) <= era['to'], era['name']
        assert analysis['products'][product]['positioning']
    empty = analyze_products(cards)
    attach_editorial(empty, [], editorial)
    assert not any(empty['products'][product]['eras'] for product in ('chatgpt', 'cursor', 'claude-code'))


def test_wiki_alias_keeps_code_titles_clickable():
    from _scripts.writer import card_link
    text = card_link({'card_id':'c','date':'2026-10-09','slug':'test',
                      'title':'Added `autoCompactWindow` and [Image #N] support | details'}, {'c':'Changes/Claude Code/test'})
    assert text == '[[Changes/Claude Code/test|Added autoCompactWindow and Image ♯N support  /  details]]'


def test_fixture_aggregates_are_marked_nonpublic_even_for_enabled_products():
    import frontmatter
    from _scripts.writer import render_theme_markdown, render_product_markdown, render_index_markdown
    card = {'card_id':'c','date':'2026-01-01','slug':'demo','product':'cursor','product_name':'Cursor',
            'title':'Demo agent','theme':'agent-mode','source_type':'fixture','source_release':'r'}
    info = {'product_name':'Cursor','verbosity_baseline':1,'eras':[],'top_themes':['agent-mode']}
    release = {'release_id':'r','date':card['date'],'title':'demo','source_type':'fixture'}
    pages = [render_theme_markdown('agent-mode',[card]),
             render_product_markdown('cursor',info,[card],releases=[release]),
             render_index_markdown([card],{'products':{'cursor':info}},{'themes':{'agent-mode':{}}},{})]
    assert all(frontmatter.loads(page)['publication'] == 'fixture' for page in pages)


def test_wiki_alias_preserves_currency_and_avoids_autolinks_and_heading_delimiters():
    from _scripts.writer import wiki_label
    assert wiki_label('C# $0.50/M at https://example.com/docs') == 'C♯ $0.50/M at (source link)'


def test_model_introduction_with_price_is_not_a_pricing_only_change():
    _, themes, _ = inputs()
    release = {'product':'claude-code','product_name':'Claude Code','release_id':'claude-release',
               'source_type':'github_releases','date':'2026-10-07','title':'v2.1.293',
               'body':'- Added Claude Haiku 5.5, now the default Haiku model — 1M context, $0.10/$0.50 per Mtok',
               'source_url':'https://github.com/anthropics/claude-code/releases/tag/v2.1.293'}
    assert extract_cards_from_release(release,themes)[0]['theme'] == 'model-support'
    release['body'] = '# New pricing model'
    assert extract_cards_from_release(release,themes) == []


def test_sdk_examples_are_not_changes_but_release_prose_survives():
    payload, themes, review = inputs()
    release = next(r for r in payload['releases'] if r['product'] == 'cursor' and r['date'] == '2026-04-29')
    cards = extract_cards_from_release(release, themes, review)
    assert cards
    assert not any(c['evidence'][0]['quote'].startswith(('import ', 'const ', 'for await', 'console.log')) for c in cards)
    assert any('introducing the Cursor SDK' in c['evidence'][0]['quote'] for c in cards)
    from _scripts.extract import split_release_lines
    assert split_release_lines('```typescript\nAgent.create({model: "test"});\n```\nAgent now supports remote execution.') == ['Agent now supports remote execution.']


# Vendor openings that card_title rewrites with an explicit rule. Other first-person
# openings ("We're retiring ...") intentionally keep the vendor's wording.
EXPLICIT_VENDOR_OPENING_RE = re.compile(
    r"^(?:good news!|you can now |this release (?:introduces|brings|adds|includes|makes) |"
    r"(?:today,? )?we(?:[’']re| are) (?:introducing|launching|rolling out|expanding|adding) |"
    r"(?:today,? )?we(?:[’']ve| have) (?:also )?added |"
    r"(?:today,? )?we[’']ve (?:also )?(?:improved|updated|fixed|made|expanded|changed) |"
    r"(?:today,? )?we(?:[’']re| are) (?:now )?(?:excited|happy|thrilled) to "
    r"(?:(?:announce|share) that|introduce|launch|announce|bring|expand) )",
    re.I,
)
COORDINATED_GERUND = re.compile(r" and (?:also )?\w+ing\b")


def test_every_m2_card_title_is_readable_and_bounded():
    from _scripts.extract import _first_sentence
    payload, themes, review = inputs()
    cards = [c for r in payload['releases'] for c in extract_cards_from_release(r, themes, review)]
    assert len(cards) > 1900
    for card in cards:
        title = card['title']
        assert len(title) <= 90, title
        assert title == title.strip(), title
        assert not title.endswith(('.', ':')), title
        if title.endswith('…'):
            assert title[-2].isalnum() or title[-2] in ")`'", title
        assert title.count('`') % 2 == 0, title
        if EXPLICIT_VENDOR_OPENING_RE.match(title):
            # Only a coordinated gerund ("introducing X and updating Y") blocks the rewrite.
            assert COORDINATED_GERUND.search(_first_sentence(card['evidence'][0]['quote'])), title
