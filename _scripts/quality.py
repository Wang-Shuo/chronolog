"""Inspectable per-run facts and Markdown summaries for the operations gate."""
from __future__ import annotations
import hashlib
import html
import json
from pathlib import Path
import re
import frontmatter
from _scripts.transaction import files
from _scripts.validate import ROOT_PAGES


def normalized_page(path: Path) -> str:
    post = frontmatter.load(path)
    post.metadata.pop('machine_hash', None)
    coverage = post.get('coverage')
    if isinstance(coverage, dict):
        for key in ('acquired_at', 'last_successful_fetch', 'snapshot_captured_at', 'snapshot_sha256'):
            coverage.pop(key, None)
    # A healthy fetch with unchanged source facts should not open a timestamp-only PR.
    # Preserve all other text, including source ranges, limitations and human notes.
    body = re.sub(r'(Last successful fetch: |Official browser snapshot captured: )[^\n]*?(?=\. (?:Imported|$)|\.\n|$)',
                  r'\1[acquisition recorded in run evidence]', post.content, flags=re.M)
    return json.dumps(post.metadata, sort_keys=True, default=str) + '\n' + body


def inventory(root: Path) -> dict:
    result = {}
    for name, path in files(root).items():
        post = frontmatter.load(path)
        result[name] = {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'semantic_sha256': hashlib.sha256(normalized_page(path).encode()).hexdigest(),
            'kind': name.split('/')[0], 'superseded': bool(post.get('superseded')),
            'id': post.get('card_id') or post.get('release_id')}
    return result


def changes(before: dict, after: dict) -> dict:
    groups = {key: [] for key in ('added', 'modified', 'retired', 'removed', 'acquisition_only')}
    for name in sorted(before.keys() | after.keys()):
        old, new = before.get(name), after.get(name)
        if old == new:
            continue
        if old is None:
            key = 'added'
        elif new is None:
            key = 'removed'
        elif not old['superseded'] and new['superseded']:
            key = 'retired'
        elif old['semantic_sha256'] == new['semantic_sha256']:
            key = 'acquisition_only'
        else:
            key = 'modified'
        groups[key].append(name)
    groups['content_changed'] = any(groups[k] for k in ('added', 'modified', 'retired', 'removed'))
    groups['counts'] = {k: len(v) for k, v in groups.items() if isinstance(v, list)}
    groups['by_kind'] = {kind: {key: sum(p.split('/')[0] == kind for p in groups[key])
                              for key in groups['counts']}
                         for kind in ('Releases', 'Changes', 'Products', 'Themes', 'Alerts', '_review', *ROOT_PAGES)}
    return groups


def markdown(report: dict) -> str:
    def safe(value):
        return html.escape(str(value)[:2000]).replace('|', '\\|').replace('\n', ' ')
    lines = ['# ChronoLog quality report', '', f"Run: `{report['run_id']}` · **{report['status']}**", '',
        f"Mode: {report['mode']}; input: {report.get('input_kind', 'not collected')}; base: `{report.get('commit', 'local')}`.",
        '', '| Source | Status | Acquisition | Acquired at | Release range |', '| --- | --- | --- | --- | --- |']
    for s in report.get('sources', []):
        lines.append('| ' + ' | '.join(safe(v) for v in (s.get('product'), s.get('status'),
            s.get('acquisition', 'none'), s.get('acquired_at', 'unknown'),
            f"{s.get('earliest')} → {s.get('latest')}")) + ' |')
    lines += ['', '## Changes', '', json.dumps(report.get('changes', {}).get('counts', {}), sort_keys=True), '',
        f"Pending themes: {report.get('pending_theme_review', 'not assessed')}; DLQ: {report.get('dlq_count', 'not assessed')}; conflicts: {len(report.get('conflicts', []))}.",
        '', '| Gate | Result | Evidence |', '| --- | --- | --- |']
    for gate, result in report.get('checks', {}).items():
        lines.append(f"| {safe(gate)} | {safe(result.get('status'))} | {safe(result.get('log', result.get('report', 'quality.json')))} |")
    if report.get('error'):
        lines += ['', '## Failure', '', safe(report['error'])]
    for s in report.get('sources', []):
        if s.get('error'):
            lines += ['', f"Source {safe(s['product'])}: {safe(s['error'])}"]
    if report.get('status') == 'no-change':
        lines += ['', 'No content PR is needed. Acquisition timestamps are preserved in this run artifact.']
    lines += ['', 'Detailed changed paths, source coverage, validation results and input hashes are in `quality.json` and `evidence-sha256.json`.',
        'Generated content requires PR review. A green engineering gate does not approve new semantic judgments.', '']
    return '\n'.join(lines)
