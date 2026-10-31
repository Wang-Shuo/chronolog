from datetime import datetime, timedelta, timezone
import json
from pathlib import Path

import pytest

from _scripts import pipeline_health
from _scripts.pipeline_health import ISSUE_TITLE, assess, last_acquired, sync_issue

NOW = datetime(2026, 10, 31, 6, 0, tzinfo=timezone.utc)
SOURCES = [
    {'name': 'chatgpt', 'display_name': 'ChatGPT', 'max_staleness_days': 8},
    {'name': 'claude-code', 'display_name': 'Claude Code', 'max_staleness_days': 2},
    {'name': 'cursor', 'display_name': 'Cursor'},  # default limit
]


def report(**statuses):
    return {'status': 'candidate-applied',
            'sources': [{'product': p, 'status': statuses.get(p, 'success'), 'error': None}
                        for p in ('chatgpt', 'claude-code', 'cursor')]}


def days_ago(days: float) -> datetime:
    return NOW - timedelta(days=days)


def test_a_healthy_run_needs_no_attention():
    result = assess(report(), SOURCES, {}, None, NOW)
    assert result == {'failing': False, 'attention': False, 'findings': []}


def test_a_failed_source_is_tolerated_until_its_reviewed_data_is_too_old():
    run = report(chatgpt='failed')
    run['sources'][0]['error'] = 'HTTP 403'
    within = assess(run, SOURCES, {'chatgpt': days_ago(5)}, None, NOW)
    assert not within['attention'] and not within['failing']
    assert within['findings'] == [{'severity': 'note', 'text': (
        'ChatGPT not collected this run (HTTP 403); reviewed data is 5 of 8 days old')}]

    stale = assess(run, SOURCES, {'chatgpt': days_ago(9)}, None, NOW)
    assert stale['failing'] and stale['attention']
    assert stale['findings'][0]['text'] == (
        'ChatGPT: reviewed data is 9 days old (limit 8 days); this run: HTTP 403')
    # Cursor has no explicit limit: the default applies; unknown acquisition is stale.
    cursor = assess(report(cursor='failed'), SOURCES, {'cursor': days_ago(3)}, None, NOW)
    assert cursor['failing'] and 'limit 2 days' in cursor['findings'][0]['text']
    unknown = assess(report(cursor='failed'), SOURCES, {}, None, NOW)
    assert unknown['findings'][0]['text'].startswith('Cursor: no reviewed acquisition')


def test_failed_runs_and_publication_fail_while_a_waiting_review_only_reminds():
    failed = assess({'status': 'failed', 'phase': 'setup', 'error': 'npm ci failed', 'sources': []},
                    SOURCES, {s['name']: days_ago(1) for s in SOURCES}, None, NOW, 'skipped')
    assert failed['failing'] and failed['findings'][0]['text'] == 'Generation failed (setup): npm ci failed'
    assert assess(report(), SOURCES, {}, None, NOW, 'failure')['failing']

    pr = {'number': 25, 'url': 'https://github.com/o/r/pull/25', 'createdAt': days_ago(4).isoformat()}
    waiting = assess(report(), SOURCES, {}, pr, NOW)
    assert waiting['attention'] and not waiting['failing']
    assert waiting['findings'] == [{'severity': 'reminder', 'text': (
        'Review PR #25 has waited 4 days: https://github.com/o/r/pull/25')}]
    fresh = {**pr, 'createdAt': days_ago(1).isoformat()}
    assert not assess(report(), SOURCES, {}, fresh, NOW)['attention']


def test_last_acquisition_comes_from_the_reviewed_product_page(tmp_path: Path):
    products = tmp_path / 'Products'
    products.mkdir()
    (products / 'ChatGPT.md').write_text(
        "---\ncoverage:\n  acquired_at: '2026-10-24T04:08:55Z'\n---\n# ChatGPT\n")
    (products / 'Cursor.md').write_text(
        "---\ncoverage:\n  last_successful_fetch: '2026-10-14T23:26:11+0800'\n---\n# Cursor\n")
    assert last_acquired(tmp_path, 'ChatGPT') == datetime(2026, 10, 24, 4, 8, 55, tzinfo=timezone.utc)
    assert last_acquired(tmp_path, 'Cursor') == datetime(2026, 10, 14, 15, 26, 11, tzinfo=timezone.utc)
    assert last_acquired(tmp_path, 'Claude Code') is None


class FakeGitHub:
    def __init__(self, open_issues):
        self.open_issues, self.calls = open_issues, []

    def __call__(self, root, *args):
        self.calls.append(args)
        return json.dumps(self.open_issues) if args[:3] == ('gh', 'issue', 'list') else ''


@pytest.mark.parametrize('attention, open_issues, action, verb', [
    (True, [], 'opened', 'create'),
    (True, [{'number': 7, 'title': ISSUE_TITLE}], 'commented', 'comment'),
    (False, [{'number': 7, 'title': ISSUE_TITLE}], 'closed', 'close'),
    (False, [{'number': 3, 'title': 'Unrelated'}], 'none', None),
])
def test_one_health_issue_is_opened_updated_and_closed(attention, open_issues, action, verb):
    gh = FakeGitHub(open_issues)
    findings = [{'severity': 'failure', 'text': 'x'}] if attention else []
    assessment = {'failing': attention, 'attention': attention, 'findings': findings}

    assert sync_issue(Path('.'), assessment, 'https://run', 'owner', run=gh) == action
    writes = [call for call in gh.calls if call[:3] != ('gh', 'issue', 'list')]
    assert [call[2] for call in writes] == ([verb] if verb else [])
    if verb == 'create':
        assert writes[0][3:7] == ('--title', ISSUE_TITLE, '--assignee', 'owner')
    if verb in {'comment', 'close'}:
        assert writes[0][3] == '7'


def test_main_treats_a_missing_report_as_a_failed_run(tmp_path, monkeypatch, capsys):
    calls = []

    def fake_cmd(root, *args):
        calls.append(args)
        return '[]'

    monkeypatch.setattr(pipeline_health, 'cmd', fake_cmd)
    monkeypatch.setattr(pipeline_health, 'sync_issue',
                        lambda root, assessment, run_url, owner: 'opened')
    monkeypatch.setattr('sys.argv', ['pipeline_health', '--quality', str(tmp_path / 'missing.json'),
                                     '--owner', 'owner', '--run-url', 'https://run'])
    monkeypatch.delenv('GITHUB_STEP_SUMMARY', raising=False)

    with pytest.raises(SystemExit) as exit_info:
        pipeline_health.main()

    assert exit_info.value.code == 1
    output = json.loads(capsys.readouterr().out)
    assert output['findings'][0]['text'] == (
        'Generation failed (setup): the run uploaded no generation report')
    assert calls[0][:4] == ('gh', 'pr', 'list', '--state')
