"""Keep one GitHub issue that says whether the daily generation needs attention.

Reads the run's quality.json, the reviewed vault's last acquisition of each failed source
and the rolling review PR. While something needs attention the "ChronoLog pipeline health"
issue is opened (assigned to the owner) or commented on; on recovery it is closed. Exits 1
when the run failed or a source's reviewed data is older than its ``max_staleness_days``,
so a degraded run that stays degraded too long turns red.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
from typing import Callable

import frontmatter

from _scripts.collect import load_sources
from _scripts.rolling_pr import BRANCH

ROOT = Path(__file__).resolve().parents[1]
ISSUE_TITLE = 'ChronoLog pipeline health'
DEFAULT_MAX_STALENESS_DAYS = 2
REVIEW_REMINDER_DAYS = 3
RUNBOOK = 'docs/m3-operations.md'


def cmd(root: Path, *args: str) -> str:
    return subprocess.check_output(args, cwd=root, text=True).strip()


def timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def last_acquired(root: Path, product_name: str) -> datetime | None:
    """Acquisition time of the reviewed data on the product page; None when unknown."""
    page = root / 'Products' / f'{product_name}.md'
    coverage = frontmatter.load(page).get('coverage', {}) if page.exists() else {}
    for key in ('acquired_at', 'last_successful_fetch', 'snapshot_captured_at'):
        if coverage.get(key):
            return timestamp(coverage[key])
    return None


def assess(report: dict, sources: list[dict], last: dict[str, datetime | None], rolling_pr: dict | None,
           now: datetime, publish_result: str = 'success') -> dict:
    """Findings of one run: ``failure`` (the run turns red), ``reminder`` (the issue stays
    open) and ``note`` (reported only)."""
    findings: list[dict[str, str]] = []
    if report.get('status') == 'failed':
        stage = report.get('phase') or 'see quality.md'
        findings.append({'severity': 'failure',
                         'text': f"Generation failed ({stage}): {report.get('error') or 'no error recorded'}"})
    if publish_result == 'failure':
        findings.append({'severity': 'failure', 'text': 'Publishing the review PR failed; see rolling-pr.json.'})
    states = {s.get('product'): s for s in report.get('sources', [])}
    for source in sources:
        state = states.get(source['name'], {})
        if state.get('status') == 'success':
            continue
        name = source.get('display_name', source['name'])
        limit = int(source.get('max_staleness_days', DEFAULT_MAX_STALENESS_DAYS))
        acquired = last.get(source['name'])
        age = None if acquired is None else (now - acquired).total_seconds() / 86400
        reason = state.get('error') or state.get('status') or 'not collected'
        if age is None or age > limit:
            known = 'no reviewed acquisition' if age is None else f'reviewed data is {age:.0f} days old'
            findings.append({'severity': 'failure',
                             'text': f'{name}: {known} (limit {limit} days); this run: {reason}'})
        else:
            findings.append({'severity': 'note',
                             'text': f'{name} not collected this run ({reason}); reviewed data is '
                                     f'{age:.0f} of {limit} days old'})
    if rolling_pr:
        waited = (now - timestamp(rolling_pr['createdAt'])).total_seconds() / 86400
        if waited >= REVIEW_REMINDER_DAYS:
            findings.append({'severity': 'reminder',
                             'text': f"Review PR #{rolling_pr['number']} has waited {waited:.0f} days: "
                                     f"{rolling_pr['url']}"})
    return {'failing': any(f['severity'] == 'failure' for f in findings),
            'attention': any(f['severity'] in {'failure', 'reminder'} for f in findings),
            'findings': findings}


def render(assessment: dict, run_url: str) -> str:
    marks = {'failure': '✗', 'reminder': '⏳', 'note': '·'}
    lines = [f"- {marks[f['severity']]} {f['text']}" for f in assessment['findings']]
    head = 'Needs attention' if assessment['attention'] else 'Healthy'
    return '\n'.join([f'**{head}** in [this run]({run_url}).', '', *lines, '',
                      f'Recovery steps: `{RUNBOOK}`.'])


def sync_issue(root: Path, assessment: dict, run_url: str, owner: str,
               run: Callable[..., str] = cmd) -> str:
    """Open, comment on or close the health issue; returns the action taken."""
    issues = json.loads(run(root, 'gh', 'issue', 'list', '--state', 'open', '--limit', '200',
                            '--json', 'number,title'))
    issue = next((i for i in issues if i['title'] == ISSUE_TITLE), None)
    body = render(assessment, run_url)
    if not assessment['attention']:
        if issue is None:
            return 'none'
        run(root, 'gh', 'issue', 'close', str(issue['number']), '--comment', body)
        return 'closed'
    if issue is None:
        run(root, 'gh', 'issue', 'create', '--title', ISSUE_TITLE, '--assignee', owner, '--body', body)
        return 'opened'
    run(root, 'gh', 'issue', 'comment', str(issue['number']), '--body', body)
    return 'commented'


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=ROOT)
    p.add_argument('--quality', type=Path, required=True)
    p.add_argument('--publish-result', default='skipped')
    p.add_argument('--base', default='main')
    p.add_argument('--owner', required=True)
    p.add_argument('--run-url', required=True)
    a = p.parse_args()
    report = (json.loads(a.quality.read_text()) if a.quality.exists() else
              {'status': 'failed', 'phase': 'setup', 'error': 'the run uploaded no generation report'})
    sources = load_sources(a.root / '_scripts/sources.yaml')
    last = {s['name']: last_acquired(a.root, s.get('display_name', s['name'])) for s in sources}
    prs = json.loads(cmd(a.root, 'gh', 'pr', 'list', '--state', 'open', '--head', BRANCH,
                         '--base', a.base, '--json', 'number,url,createdAt'))
    assessment = assess(report, sources, last, prs[0] if prs else None,
                        datetime.now(timezone.utc), a.publish_result)
    action = sync_issue(a.root, assessment, a.run_url, a.owner)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
            summary.write(f'## Pipeline health ({action})\n\n{render(assessment, a.run_url)}\n')
    print(json.dumps({'action': action, **assessment}, indent=2))
    raise SystemExit(1 if assessment['failing'] else 0)


if __name__ == '__main__':
    main()
