"""Curated editorial content (narratives, eras, positioning, key moments) against the
writing guide (docs/style-guide.md) and the archived vault."""
from datetime import date, timedelta
from pathlib import Path
import re

import frontmatter
import pytest

from _scripts.editorial import key_moments, load_editorial

ROOT = Path(__file__).resolve().parents[1]
EDITORIAL = load_editorial(ROOT)
PRODUCTS = {
    # name in prose: (official source prefix, archived release folder)
    'ChatGPT': ('https://help.openai.com/en/articles/6825453-chatgpt-release-notes', 'Releases/ChatGPT/'),
    'Cursor': ('https://cursor.com/changelog/', 'Releases/Cursor/'),
    'Claude Code': ('https://github.com/anthropics/claude-code/releases/tag/', 'Releases/Claude Code/'),
}
SCOPE_LABEL = '**Uncertainty and scope:** '
CAVEATS = ('does not establish', 'do not establish', 'cannot establish', 'not evidence')
WIKI_RE = re.compile(r'\[\[([^|\]]+)\|[^\]]+\]\]')
LINK_RE = re.compile(r'\]\((https?://[^)\s]+)\)')


def sentences(text: str) -> list[str]:
    """Split on a sentence end followed by a capitalised word (version numbers such as
    ``v2.1.32`` and decimals stay inside their sentence)."""
    return [part for part in re.split(r'(?<=[.!?])\s+(?=[A-Z“"])', text.strip()) if part]


def paragraphs(narrative: str) -> list[str]:
    return [part.strip() for part in narrative.strip().split('\n\n')]


def active_cards() -> list[dict]:
    cards = []
    for path in (ROOT / 'Changes').glob('*/*.md'):
        meta = frontmatter.load(path).metadata
        if meta.get('superseded') is True or meta.get('source_type') == 'fixture':
            continue
        cards.append({'card_id': str(meta['card_id']), 'theme': meta['theme'],
                      'product': meta.get('product')})
    return cards


def test_sentence_split_keeps_versions_and_splits_on_capitals():
    assert sentences('Claude Code v2.1.32 adds a. B follows, at $0.10 per Mtok.') == [
        'Claude Code v2.1.32 adds a.', 'B follows, at $0.10 per Mtok.']


@pytest.mark.parametrize('theme', sorted(EDITORIAL['themes']))
def test_narrative_shape_question_products_then_one_scope_sentence(theme):
    parts = paragraphs(EDITORIAL['themes'][theme])
    assert parts[0].startswith('**Research question: ') and parts[0].endswith('?**'), theme
    assert parts[-1].startswith(SCOPE_LABEL), theme
    assert len(sentences(parts[-1][len(SCOPE_LABEL):])) == 1, theme  # exactly one scope sentence
    body = parts[1:-1]
    assert body, theme
    for paragraph in parts:
        assert sum(paragraph.count(phrase) for phrase in ('does not establish',)) <= 1, theme
    for paragraph in body:
        prose = re.sub(r'\]\([^)\s]+\)|\[\[[^\]]+\]\]', ']', paragraph)  # drop link targets
        # Caveats live in the single scope sentence, not in evidence paragraphs (C4).
        assert not any(phrase in prose for phrase in CAVEATS), (theme, paragraph[:80])
        # Third person: no vendor or reader first/second person (C3).
        assert not re.search(r'\b(we|our|you|your)\b', prose, re.I), (theme, paragraph[:80])


@pytest.mark.parametrize('theme', sorted(EDITORIAL['themes']))
def test_each_product_paragraph_cites_its_official_source_and_archived_release(theme):
    narrative = EDITORIAL['themes'][theme]
    mentioned = [name for name in PRODUCTS if name in narrative]
    assert mentioned, theme
    for name in mentioned:
        official, folder = PRODUCTS[name]
        assert any(url.startswith(official) for url in LINK_RE.findall(narrative)), (theme, name)
        assert any(target.startswith(folder) for target in WIKI_RE.findall(narrative)), (theme, name)
    for paragraph in paragraphs(narrative)[1:-1]:
        name = next(name for name in PRODUCTS if paragraph.startswith(name))
        official, folder = PRODUCTS[name]
        assert any(url.startswith(official) for url in LINK_RE.findall(paragraph)), (theme, name)
        assert any(target.startswith(folder) for target in WIKI_RE.findall(paragraph)), (theme, name)


def test_every_archived_release_link_in_editorial_exists_in_the_vault():
    texts = list(EDITORIAL['themes'].values())
    targets = {target for text in texts for target in WIKI_RE.findall(text)}
    assert len(targets) > 40
    missing = sorted(target for target in targets if not (ROOT / f'{target}.md').exists())
    assert missing == []


@pytest.mark.parametrize('product', ['chatgpt', 'cursor', 'claude-code'])
def test_product_positioning_limitations_and_contiguous_eras(product):
    spec = EDITORIAL['products'][product]
    positioning = ' '.join(spec['positioning'].split())
    assert 0 < len(positioning) <= 160 and '\n' not in spec['positioning'].strip()
    assert len(sentences(' '.join(spec['limitations'].split()))) == 1, product
    assert not any(phrase in era['summary'] for era in spec['eras'] for phrase in CAVEATS), product
    eras = spec['eras']
    assert eras[-1]['to'] is None
    for era, following in zip(eras, eras[1:]):
        assert date.fromisoformat(era['to']) + timedelta(days=1) == date.fromisoformat(following['from'])
    for era in eras:
        assert 1 <= len(era['releases']) <= 3 and len(set(era['releases'])) == len(era['releases'])
        assert all(release.startswith(product + '-') for release in era['releases'])
        assert min(release[len(product) + 1:][:10] for release in era['releases']) == era['from']


def test_curated_key_moments_are_active_cards_of_their_theme_and_balanced():
    cards = active_cards()
    curated, warnings = key_moments(EDITORIAL, cards)
    assert warnings == []
    product_of = {card['card_id']: card['product'] for card in cards}
    for theme in ('agent-mode', 'pricing-model'):
        ids = curated[theme]
        assert 10 <= len(ids) <= 16, theme
        products = {product_of[card_id] for card_id in ids}
        years = {card_id.split('-')[-4] if card_id.startswith('claude-code') else card_id.split('-')[1]
                 for card_id in ids}
        assert products == {'chatgpt', 'cursor', 'claude-code'}, theme
        assert len(years) >= 3, theme


def test_theme_narratives_show_only_when_every_cited_release_is_in_the_run():
    from _scripts.editorial import NARRATIVE_MISSING_RELEASE, theme_narratives
    editorial = {'themes': {
        'agent-mode': 'Q\n\nCursor [r](https://cursor.com/changelog/1-0) ([[Releases/Cursor/cursor-a|archived]]).',
        'memory': 'Q\n\nCursor [r](https://cursor.com/changelog/1-2) ([[Releases/Cursor/cursor-b|archived]]).',
        'voice': 'No archived links.',
    }}
    shown, warnings = theme_narratives(editorial, [{'release_id': 'cursor-a'}])
    assert sorted(shown) == ['agent-mode', 'voice']
    assert warnings == [{'theme': 'memory', 'card_id': '', 'release_id': 'cursor-b',
                         'reason': NARRATIVE_MISSING_RELEASE}]
    # The curated narratives all resolve against the archived releases in the vault.
    releases = [{'release_id': path.stem} for path in (ROOT / 'Releases').glob('*/*.md')]
    shown, warnings = theme_narratives(EDITORIAL, releases)
    assert warnings == [] and sorted(shown) == sorted(EDITORIAL['themes'])
