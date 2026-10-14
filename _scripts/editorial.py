"""Cited editorial narratives, activated only when their evidence is in the run."""
from pathlib import Path
from typing import Any
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


def render_coverage(state: dict) -> str:
    if not state:
        return 'Source acquisition time has not been recorded.'
    lines = [f"Archived release dates: {state.get('earliest', 'unknown')} → {state.get('latest', 'unknown')}."]
    if state.get('acquisition') == 'browser-snapshot':
        lines.append(f"Official browser snapshot captured: {state.get('snapshot_captured_at', 'unknown')}. "
                     'Imported snapshot; this is not a successful automatic HTTP fetch.')
    else:
        lines.append(f"Last successful fetch: {state.get('last_successful_fetch', 'not recorded')}.")
    if state.get('url'):
        lines.append(f"[Source]({state['url']}).")
    if state.get('known_gaps'):
        lines.append(f"Coverage limits: {state['known_gaps']}")
    return '\n\n'.join(lines)
