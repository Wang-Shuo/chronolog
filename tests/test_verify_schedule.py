"""Evidence downloads must follow GitHub's latest attempt, including failed retries."""
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys

import pytest

from _scripts import verify_schedule


@pytest.mark.parametrize('latest_conclusion', ['success', 'failure', 'in_progress'])
def test_selects_latest_attempt_without_mixing_old_artifacts(tmp_path, monkeypatch, latest_conclusion):
    now = datetime.now(timezone.utc)
    runs = [{'databaseId': i, 'event': 'schedule', 'status': 'completed',
             'conclusion': 'failure' if latest_conclusion == 'failure' else 'success',
             'createdAt': (now - timedelta(days=i)).isoformat(), 'headSha': 'abc'}
            for i in range(7)]
    downloaded = []

    def output(args, **kwargs):
        if args[:3] == ['gh', 'run', 'list']:
            return json.dumps(runs)
        assert args[:2] == ['gh', 'api']
        run_id = int(args[2].rsplit('/', 1)[1])
        return json.dumps({'id': run_id, 'event': 'schedule', 'head_sha': 'abc',
                           'status': 'in_progress' if latest_conclusion == 'in_progress' else 'completed',
                           'conclusion': runs[run_id]['conclusion'], 'run_attempt': 2})

    def download(args, **kwargs):
        assert args[:3] == ['gh', 'run', 'download']
        run_id = int(args[3])
        assert '--pattern' not in args
        assert args[args.index('--name') + 1] == f'generation-{run_id}-2'
        downloaded.append(run_id)
        destination = Path(args[args.index('--dir') + 1])
        destination.mkdir(parents=True)
        (destination / 'quality.json').write_text(json.dumps({
            'input_kind': 'live', 'status': 'failed' if latest_conclusion == 'failure' else 'no-change',
            'sources': [{'product': p, 'status': 'failed' if latest_conclusion == 'failure' else 'success'}
                        for p in ['chatgpt', 'claude-code', 'cursor']]}))

    out = tmp_path / 'evidence'
    monkeypatch.setattr(sys, 'argv', ['verify_schedule', '--repo', 'owner/repo', '--output', str(out)])
    monkeypatch.setattr(verify_schedule.subprocess, 'check_output', output)
    monkeypatch.setattr(verify_schedule.subprocess, 'run', download)
    if latest_conclusion == 'in_progress':
        with pytest.raises(ValueError, match='changed'):
            verify_schedule.main()
        assert not downloaded
        assert not (out / 'scheduled-runs.json').exists()
    else:
        verify_schedule.main()
        report = json.loads((out / 'scheduled-runs.json').read_text())
        assert len(downloaded) == 7
        assert all(r['selectedAttempt'] == 2 for r in report['runs'])
        assert report['assessment']['conclusions']['0'] == latest_conclusion
