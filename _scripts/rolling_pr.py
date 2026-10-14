"""Transfer a gated content candidate from a read-only job to a trusted publisher."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re
import subprocess

BRANCH = 'codex/chronolog-updates'
VAULT = ['Products', 'Releases', 'Changes', 'Themes', 'Alerts', '_review', 'index.md']


def cmd(root: Path, *args: str) -> str:
    return subprocess.check_output(args, cwd=root, text=True).strip()


def prepare(root: Path, base: str, state_path: Path) -> dict:
    cmd(root, 'git', 'check-ref-format', '--branch', base)
    if cmd(root, 'git', 'status', '--porcelain'):
        raise ValueError('prepare requires a clean disposable CI checkout')
    cmd(root, 'git', 'fetch', 'origin', base)
    base_head = cmd(root, 'git', 'rev-parse', 'origin/' + base)
    prs = open_prs(root, base)
    remote = cmd(root, 'git', 'ls-remote', '--heads', 'origin', 'refs/heads/' + BRANCH)
    sha = remote.split()[0] if remote else ''
    if prs:
        if not sha:
            raise ValueError('open rolling PR has no remote branch')
        cmd(root, 'git', 'fetch', 'origin', BRANCH)
        cmd(root, 'git', 'switch', '-C', BRANCH, 'origin/' + BRANCH)
        cmd(root, 'git', 'merge', '--no-edit', 'origin/' + base)
    else:
        cmd(root, 'git', 'switch', '-C', BRANCH, 'origin/' + base)
    state = {'base': base, 'base_head': base_head, 'branch': BRANCH,
             'expected_remote_head': sha, 'pr': prs[0] if prs else None}
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, indent=2) + '\n')
    return state


def open_prs(root: Path, base: str) -> list:
    prs = json.loads(cmd(root, 'gh', 'pr', 'list', '--state', 'open', '--head', BRANCH,
                         '--base', base, '--json', 'number,url'))
    if len(prs) > 1:
        raise ValueError('multiple open rolling PRs; reconcile them before generation')
    return prs


def package(root: Path, state: dict, report_dir: Path, output: Path) -> dict:
    """Commit and export locally. This function never writes to GitHub."""
    report = json.loads((report_dir / 'quality.json').read_text())
    if report['status'] not in {'candidate-applied', 'no-change'}:
        raise ValueError('generation did not pass all gates')
    if cmd(root, 'git', 'branch', '--show-current') != BRANCH:
        raise ValueError('must package from the managed review branch')
    if report['status'] == 'candidate-applied':
        cmd(root, 'git', 'add', '-u')  # Include deleted content; reject other paths below.
        paths = [p for p in VAULT if (root / p).exists()]
        if paths:
            cmd(root, 'git', 'add', '--', *paths)
        staged = cmd(root, 'git', 'diff', '--cached', '--name-only').splitlines()
        if any(p.split('/')[0] not in VAULT for p in staged):
            raise ValueError('unexpected staged file outside generated Vault scope')
        if staged:
            cmd(root, 'git', 'commit', '-m', f"chore: refresh ChronoLog sources ({report['run_id']})")
    head = cmd(root, 'git', 'rev-parse', 'HEAD')
    packet = {**state, 'head': head, 'generation_status': report['status']}
    output.mkdir(parents=True, exist_ok=True)
    (output / 'candidate.json').write_text(json.dumps(packet, indent=2) + '\n')
    (output / 'quality.md').write_text((report_dir / 'quality.md').read_text())
    cmd(root, 'git', 'bundle', 'create', str((output / 'candidate.bundle').resolve()), 'HEAD')
    return packet


def validate_candidate(root: Path, packet: dict, expected_base: str) -> None:
    if packet['branch'] != BRANCH or packet['base'] != expected_base:
        raise ValueError('unexpected publication branch or base')
    for key in ('head', 'base_head', 'expected_remote_head'):
        value = packet[key]
        if key == 'expected_remote_head' and value == '':
            continue
        if not isinstance(value, str) or not re.fullmatch(r'[0-9a-f]{40}', value):
            raise ValueError('invalid candidate commit')
    if packet['generation_status'] not in {'candidate-applied', 'no-change'}:
        raise ValueError('generation did not pass all gates')
    # The publisher checked out the workflow's trusted commit, never the candidate.
    if cmd(root, 'git', 'rev-parse', 'HEAD') != packet['base_head']:
        raise ValueError('base changed since workflow checkout; regenerate')
    cmd(root, 'git', 'merge-base', '--is-ancestor', packet['base_head'], packet['head'])
    if packet['pr'] and packet['expected_remote_head']:
        cmd(root, 'git', 'merge-base', '--is-ancestor', packet['expected_remote_head'], packet['head'])
    # A read-only job may supply data, never executable code to the publishing job.
    changes = cmd(root, 'git', 'diff', '--no-renames', '--name-only',
                  packet['base_head'], packet['head']).splitlines()
    if any(p.split('/')[0] not in VAULT or not p.endswith('.md') for p in changes):
        raise ValueError('candidate changes files outside Markdown Vault scope')
    for path in changes:
        entry = cmd(root, 'git', 'ls-tree', packet['head'], '--', path)
        if entry and not entry.startswith('100644 blob '):
            raise ValueError('candidate content must be regular non-executable files')


def publish_bundle(root: Path, bundle_dir: Path, expected_base: str) -> dict:
    """Import objects without checkout, push with a lease, then dispatch exact-head CI."""
    packet = json.loads((bundle_dir / 'candidate.json').read_text())
    cmd(root, 'git', 'bundle', 'verify', str((bundle_dir / 'candidate.bundle').resolve()))
    cmd(root, 'git', 'fetch', str((bundle_dir / 'candidate.bundle').resolve()), 'HEAD')
    validate_candidate(root, packet, expected_base)
    if cmd(root, 'git', 'rev-parse', 'FETCH_HEAD') != packet['head']:
        raise ValueError('bundle head does not match candidate metadata')
    prs = open_prs(root, expected_base)
    pr = prs[0] if prs else None
    if pr != packet['pr']:
        raise ValueError('rolling PR changed during generation; regenerate')
    head = packet['head']
    # With no open PR and no content change, no branch or empty PR is created.
    if not pr and head == packet['base_head']:
        return {'status': 'no-change', 'pr': None}
    remote = cmd(root, 'git', 'ls-remote', '--heads', 'origin', 'refs/heads/' + BRANCH)
    remote_head = remote.split()[0] if remote else ''
    if remote_head != packet['expected_remote_head']:
        raise ValueError('remote branch changed during generation; regenerate')
    if head != remote_head:
        cmd(root, 'git', 'push', f'--force-with-lease=refs/heads/{BRANCH}:{remote_head}',
            'origin', f'{head}:refs/heads/{BRANCH}')
    body = bundle_dir / 'pr-body.md'
    body.write_text((bundle_dir / 'quality.md').read_text() +
        f"\nRun evidence: {os.environ.get('GITHUB_SERVER_URL', 'https://github.com')}/{os.environ['GITHUB_REPOSITORY']}/actions/runs/{os.environ['GITHUB_RUN_ID']}\n")
    title = 'chore: review ChronoLog source updates'
    if pr:
        url = pr['url']
        if packet['generation_status'] != 'no-change':
            cmd(root, 'gh', 'pr', 'edit', str(pr['number']), '--title', title, '--body-file', str(body))
    else:
        url = cmd(root, 'gh', 'pr', 'create', '--base', expected_base, '--head', BRANCH,
                  '--title', title, '--body-file', str(body))
    # GITHUB_TOKEN PR events do not trigger CI. workflow_dispatch is an exception.
    # Dispatch also on no-change, so a failed dispatch can recover on a rerun.
    cmd(root, 'gh', 'workflow', 'run', 'quality.yml', '--ref', BRANCH,
        '-f', f'expected_head={head}')
    return {'status': 'review-required', 'url': url, 'head': head,
            'quality': 'dispatched', 'generation_status': packet['generation_status']}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('action', choices=['prepare', 'package', 'publish-bundle'])
    p.add_argument('--root', type=Path, default=Path.cwd())
    p.add_argument('--base', default='main')
    p.add_argument('--state', type=Path)
    p.add_argument('--report', type=Path)
    p.add_argument('--bundle', type=Path)
    a = p.parse_args()
    if a.action == 'prepare':
        if not a.state:
            p.error('prepare requires --state')
        result = prepare(a.root, a.base, a.state)
    elif a.action == 'package':
        if not all((a.state, a.report, a.bundle)):
            p.error('package requires --state, --report and --bundle')
        result = package(a.root, json.loads(a.state.read_text()), a.report, a.bundle)
    else:
        if not a.bundle:
            p.error('publish-bundle requires --bundle')
        try:
            result = publish_bundle(a.root, a.bundle, a.base)
        except Exception as exc:
            (a.bundle / 'rolling-pr.json').write_text(json.dumps({'status': 'failed', 'error': str(exc)}, indent=2) + '\n')
            raise
        (a.bundle / 'rolling-pr.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
