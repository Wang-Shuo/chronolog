"""Cited editorial narratives, activated only when their evidence is in the run."""
from pathlib import Path
import re
from typing import Any
from urllib.parse import urlsplit
from _scripts.common import read_yaml


def load_editorial(root: Path) -> dict[str, Any]:
    path = root / '_scripts/editorial.yaml'
    return read_yaml(path) if path.exists() else {}


def attach_editorial(analysis: dict, releases: list[dict], editorial: dict) -> None:
    available = {r['release_id']: r for r in releases}
    for product, spec in editorial.get('products', {}).items():
        if product not in analysis['products']:
            continue
        eras = []
        for era in spec['eras']:
            ids = era['releases']
            if not all(key in available for key in ids):
                continue
            evidence = [available[key] for key in ids]
            eras.append({**era, 'evidence': [
                {'release_id': r['release_id'], 'title': r['title'], 'date': r['date'],
                 'url': r['source_url']} for r in evidence]})
        analysis['products'][product].update(
            eras=eras, narrative_summary=spec['summary'], narrative_limitations=spec['limitations'])


KEY_MOMENT_UNKNOWN = 'not an active card of this theme; ignored'
KEY_MOMENT_DUPLICATE = 'listed more than once; later entries ignored'
KEY_MOMENT_NOT_A_LIST = 'key_moments entry must be a list of card ids; ignored'


def key_moments(editorial: dict, cards: list[dict]) -> tuple[dict[str, list[str]], list[dict[str, str]]]:
    """Validated editorial ``key_moments`` (``{theme: [card_id, ...]}``, optional).

    A listed id must name an active card of that theme; unknown ids and repeats are
    dropped and returned as warnings (the pipeline records them in the run manifest as
    ``editorial_warnings``; they never block a run). A theme whose list keeps no id
    falls back to the auto-selected key moments.
    """
    spec = editorial.get('key_moments') or {}
    themes_of = {str(card['card_id']): card['theme'] for card in cards}
    curated: dict[str, list[str]] = {}
    warnings: list[dict[str, str]] = []
    if not isinstance(spec, dict):
        return {}, [{'theme': '', 'card_id': '', 'reason': KEY_MOMENT_NOT_A_LIST}]
    for theme, ids in spec.items():
        if not isinstance(ids, list):
            warnings.append({'theme': str(theme), 'card_id': '', 'reason': KEY_MOMENT_NOT_A_LIST})
            continue
        kept: list[str] = []
        for card_id in map(str, ids):
            if themes_of.get(card_id) != theme:
                warnings.append({'theme': str(theme), 'card_id': card_id, 'reason': KEY_MOMENT_UNKNOWN})
            elif card_id in kept:
                warnings.append({'theme': str(theme), 'card_id': card_id, 'reason': KEY_MOMENT_DUPLICATE})
            else:
                kept.append(card_id)
        if kept:
            curated[str(theme)] = kept
    return curated, warnings


def source_coverage(source: dict | None, releases: list[dict], previous: dict | None = None) -> dict:
    state = dict(previous or {})
    # A replay's processing time must not masquerade as a successful live fetch.
    if source and source.get('status') == 'success' and source.get('coverage') != 'no-change':
        state.update({key: source[key] for key in (
            'acquired_at', 'acquisition', 'url', 'coverage', 'known_gaps', 'snapshot_sha256'
        ) if key in source})
        if source.get('acquisition') == 'http':
            state['last_successful_fetch'] = source.get('acquired_at') or source['collected_at']
        elif source.get('acquisition') == 'browser-snapshot':
            state['snapshot_captured_at'] = source.get('acquired_at') or 'unknown'
    if releases:
        state.update(earliest=min(r['date'] for r in releases), latest=max(r['date'] for r in releases),
                     release_count=len(releases))
    return state


def acquisition_line(state: dict) -> str:
    """How the archive was last acquired, on one line.

    ``quality.normalized_page`` masks the timestamp after these exact prefixes, so a
    refresh that only moves the acquisition time is not a content change.
    """
    if state.get('acquisition') == 'browser-snapshot':
        return (f"Official browser snapshot captured: {state.get('snapshot_captured_at', 'unknown')}. "
                'Imported snapshot; this is not a successful automatic HTTP fetch.')
    return f"Last successful fetch: {state.get('last_successful_fetch', 'not recorded')}."


def render_coverage(state: dict) -> str:
    if not state:
        return 'Source acquisition time has not been recorded.'
    lines = [f"Archived release dates: {state.get('earliest', 'unknown')} → {state.get('latest', 'unknown')}.",
             acquisition_line(state)]
    if state.get('url'):
        lines.append(f"[Source]({state['url']}).")
    if state.get('known_gaps'):
        lines.append(f"Coverage limits: {state['known_gaps']}")
    return '\n\n'.join(lines)


GITHUB_RELEASES_API_RE = re.compile(r'^https://api\.github\.com/repos/([^/\s]+)/([^/\s]+)/releases/?$')


def reader_source_url(url: str) -> str:
    """Human-readable page for a source URL (the GitHub releases page, not its API)."""
    match = GITHUB_RELEASES_API_RE.match(str(url).strip())
    return f'https://github.com/{match.group(1)}/{match.group(2)}/releases' if match else str(url).strip()


def source_label(product_name: str, url: str) -> str:
    host = urlsplit(str(url)).netloc
    if host.endswith('github.com'):
        return f'{product_name} GitHub releases'
    if 'changelog' in str(url).lower():
        return f'{product_name} changelog'
    return f'{product_name} release notes'


def _releases(count: int) -> str:
    return f"{count} release" if count == 1 else f"{count} releases"


def render_coverage_summary(state: dict, release_count: int | None = None) -> str:
    """One reader-facing line: releases, release date range, source and known gaps.

    Acquisition timestamps are left to the About page and run artifacts.
    """
    state = state or {}
    count = release_count if release_count is not None else int(state.get('release_count') or 0)
    parts = [_releases(count)]
    if state.get('earliest') and state.get('latest'):
        parts.append(f"{state['earliest']} → {state['latest']}")
    if state.get('url'):
        parts.append(f"[official source]({reader_source_url(state['url'])})")
    line = ' · '.join(parts)
    if state.get('known_gaps'):
        line += ' · ' + ' '.join(str(state['known_gaps']).split())
    return line


def render_source_details(product_name: str, state: dict, release_count: int | None = None) -> str:
    """About-page block for one source; the acquisition sentence keeps its exact wording."""
    state = state or {}
    count = release_count if release_count is not None else int(state.get('release_count') or 0)
    lines = [f'### {product_name}']
    if state.get('url'):
        lines.append(f"- Official source: [{source_label(product_name, state['url'])}]"
                     f"({reader_source_url(state['url'])})")
    archived = f'- Archived releases: {count}'
    if state.get('earliest') and state.get('latest'):
        archived += f", dated {state['earliest']} → {state['latest']}"
    lines.append(archived)
    lines.append(f'- {acquisition_line(state)}' if state else
                 '- Source acquisition time has not been recorded.')
    if state.get('known_gaps'):
        lines.append(f"- Known gaps: {' '.join(str(state['known_gaps']).split())}")
    return '\n'.join(lines)
