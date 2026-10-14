"""Exercise real Git history with a local bare remote; mock only the GitHub API."""
import json
from pathlib import Path
import subprocess
import pytest
from _scripts import rolling_pr as rolling


def git(root,*args):
    return subprocess.check_output(['git',*args],cwd=root,text=True,stderr=subprocess.DEVNULL).strip()


@pytest.fixture
def repo(tmp_path,monkeypatch):
    remote=tmp_path/'remote.git';remote.mkdir();git(remote,'init','--bare')
    root=tmp_path/'repo';root.mkdir();git(root,'init','-b','main')
    git(root,'config','user.name','Test');git(root,'config','user.email','test@example.org')
    (root/'.gitignore').write_text('_pipeline/\n')
    (root/'index.md').write_text('# Home\n')
    git(root,'add','.');git(root,'commit','-m','baseline')
    git(root,'remote','add','origin',str(remote));git(root,'push','-u','origin','main')
    responses={'open':[],'calls':[]};original=rolling.cmd
    def command(path,*args):
        if args[0]!='gh':return original(path,*args)
        responses['calls'].append(args)
        if args[1:3]==('pr','list'):return json.dumps(responses['open'])
        return 'https://github.com/test/chronolog/pull/1'
    monkeypatch.setattr(rolling,'cmd',command)
    monkeypatch.setenv('GITHUB_REPOSITORY','test/chronolog');monkeypatch.setenv('GITHUB_RUN_ID','42')
    return root,remote,responses


def report(root,status='candidate-applied'):
    out=root/'_pipeline/report';out.mkdir(parents=True,exist_ok=True)
    (out/'quality.json').write_text(json.dumps({'status':status,'run_id':'daily-test'}))
    (out/'quality.md').write_text('# Passed\n')
    return out


def publish(root, state, report_dir):
    bundle = root / '_pipeline/publication'
    rolling.package(root, state, report_dir, bundle)
    publisher = root / '_pipeline/publisher'
    if not publisher.exists():
        subprocess.run(['git', 'clone', git(root, 'remote', 'get-url', 'origin'), str(publisher)], check=True, capture_output=True)
    git(publisher, 'fetch', 'origin', 'main')
    git(publisher, 'checkout', '--detach', state['base_head'])
    return rolling.publish_bundle(publisher, bundle, 'main')


def test_one_pr_is_reused_and_open_branch_human_notes_survive(repo):
    root,remote,responses=repo
    state=rolling.prepare(root,'main',root/'_pipeline/state.json')
    (root/'index.md').write_text('# Home\n\nFirst generated release.\n')
    assert publish(root,state,report(root))['status']=='review-required'
    responses['open']=[{'number':1,'url':'https://github.com/test/chronolog/pull/1'}]
    (root/'index.md').write_text((root/'index.md').read_text()+'\nHuman review note.\n')
    git(root,'add','index.md');git(root,'commit','-m','human review');git(root,'push','origin',rolling.BRANCH)
    git(root,'switch','main')
    (root/'README.md').write_text('Updated operating instructions.\n')
    git(root,'add','README.md');git(root,'commit','-m','new main docs');git(root,'push','origin','main')
    state=rolling.prepare(root,'main',root/'_pipeline/state.json')
    assert 'Human review note.' in (root/'index.md').read_text()
    assert (root/'README.md').exists()
    (root/'index.md').write_text((root/'index.md').read_text()+'\nSecond generated release.\n')
    publish(root,state,report(root))
    assert sum(c[1:3]==('pr','create') for c in responses['calls'])==1
    assert sum(c[1:3]==('pr','edit') for c in responses['calls'])==1
    before=git(remote,'rev-parse','refs/heads/'+rolling.BRANCH)
    state=rolling.prepare(root,'main',root/'_pipeline/state.json')
    result=publish(root,state,report(root,'no-change'))
    assert result['status']=='review-required'
    assert result['quality']=='dispatched'
    assert git(remote,'rev-parse','refs/heads/'+rolling.BRANCH)==before


def test_push_lease_rejects_a_concurrent_remote_edit(repo,tmp_path):
    root,remote,responses=repo
    state=rolling.prepare(root,'main',root/'_pipeline/state.json')
    (root/'index.md').write_text('# Initial candidate\n');publish(root,state,report(root))
    responses['open']=[{'number':1,'url':'https://github.com/test/chronolog/pull/1'}]
    state=rolling.prepare(root,'main',root/'_pipeline/state.json')
    other=tmp_path/'other';subprocess.run(['git','clone','-b',rolling.BRANCH,str(remote),str(other)],check=True,capture_output=True)
    git(other,'config','user.name','Other');git(other,'config','user.email','other@example.org')
    (other/'index.md').write_text('# Concurrent reviewer edit\n')
    git(other,'add','index.md');git(other,'commit','-m','concurrent human change');git(other,'push','origin',rolling.BRANCH)
    remote_sha=git(remote,'rev-parse','refs/heads/'+rolling.BRANCH)
    (root/'index.md').write_text('# Generated later\n')
    with pytest.raises(ValueError, match='remote branch changed'):publish(root,state,report(root))
    assert git(remote,'rev-parse','refs/heads/'+rolling.BRANCH)==remote_sha


def test_empty_candidate_never_creates_pr_or_dispatches_ci(repo):
    root, remote, responses = repo
    state = rolling.prepare(root, 'main', root/'_pipeline/state.json')
    result = publish(root, state, report(root, 'no-change'))
    assert result == {'status': 'no-change', 'pr': None}
    assert not git(remote, 'ls-remote', '--heads', str(remote), 'refs/heads/'+rolling.BRANCH)
    assert not any(c[1:3] in [('workflow', 'run'), ('pr', 'create')] for c in responses['calls'])


def test_failed_generation_never_exports_or_pushes(repo):
    root, remote, responses = repo
    state = rolling.prepare(root, 'main', root/'_pipeline/state.json')
    with pytest.raises(ValueError, match='did not pass'):
        publish(root, state, report(root, 'failed'))
    assert not (root/'_pipeline/publication/candidate.bundle').exists()


@pytest.mark.parametrize('path,mode', [('_scripts/evil.py', 'file'), ('Products/evil.md', 'symlink'), ('Products/evil.md', 'executable')])
def test_publisher_rejects_code_and_special_files_from_readonly_job(repo, path, mode):
    root, remote, responses = repo
    state = rolling.prepare(root, 'main', root/'_pipeline/state.json')
    target = root/path
    target.parent.mkdir(parents=True, exist_ok=True)
    if mode == 'symlink':
        target.symlink_to('../index.md')
    else:
        target.write_text('untrusted artifact content')
        if mode == 'executable':
            target.chmod(0o755)
    # Model a compromised read-only job: it may forge a commit, but cannot publish it.
    git(root, 'add', path); git(root, 'commit', '-m', 'invalid candidate')
    with pytest.raises(ValueError, match='scope|regular non-executable'):
        publish(root, state, report(root))
    assert not any(c[1:3] == ('pr', 'create') for c in responses['calls'])
    assert not git(remote, 'ls-remote', '--heads', str(remote), 'refs/heads/'+rolling.BRANCH)


def test_no_change_syncs_main_and_retries_failed_quality_dispatch(repo, monkeypatch):
    root, remote, responses = repo
    state = rolling.prepare(root, 'main', root/'_pipeline/state.json')
    (root/'index.md').write_text('# New candidate')
    original = rolling.cmd
    def fail_dispatch(path, *args):
        if args[:3] == ('gh', 'workflow', 'run'):
            raise subprocess.CalledProcessError(1, args)
        return original(path, *args)
    monkeypatch.setattr(rolling, 'cmd', fail_dispatch)
    with pytest.raises(subprocess.CalledProcessError):
        publish(root, state, report(root))
    responses['open'] = [{'number': 1, 'url': 'https://github.com/test/chronolog/pull/1'}]
    monkeypatch.setattr(rolling, 'cmd', original)
    git(root, 'switch', 'main')
    (root/'README.md').write_text('new main documentation')
    git(root, 'add', 'README.md');git(root, 'commit', '-m', 'advance main');git(root, 'push', 'origin', 'main')
    state = rolling.prepare(root, 'main', root/'_pipeline/state.json')
    result = publish(root, state, report(root, 'no-change'))
    assert result['quality'] == 'dispatched'
    assert git(remote, 'rev-parse', 'refs/heads/'+rolling.BRANCH) == result['head']
    assert responses['calls'][-1][-2:] == ('-f', 'expected_head='+result['head'])
    assert sum(c[1:3] == ('pr', 'create') for c in responses['calls']) == 1


def test_closed_pr_is_not_recreated_from_stale_candidate(repo):
    root, remote, responses = repo
    state = rolling.prepare(root, 'main', root/'_pipeline/state.json')
    (root/'index.md').write_text('# Candidate')
    publish(root, state, report(root))
    responses['open'] = [{'number': 1, 'url': 'https://github.com/test/chronolog/pull/1'}]
    state = rolling.prepare(root, 'main', root/'_pipeline/state.json')
    responses['open'] = []
    with pytest.raises(ValueError, match='PR changed'):
        publish(root, state, report(root, 'no-change'))


def test_deleted_content_is_preserved_in_bundle(repo):
    root, remote, responses = repo
    state = rolling.prepare(root, 'main', root/'_pipeline/state.json')
    (root/'index.md').unlink()
    result = publish(root, state, report(root))
    assert result['quality'] == 'dispatched'
    assert not git(remote, 'ls-tree', result['head'], '--', 'index.md')


def test_publisher_rejects_base_that_moved_during_generation(repo):
    root, remote, responses = repo
    state = rolling.prepare(root, 'main', root/'_pipeline/state.json')
    (root/'index.md').write_text('# Candidate')
    bundle = root/'_pipeline/publication'
    rolling.package(root, state, report(root), bundle)
    # A publisher running a different trusted workflow commit cannot accept this packet.
    with pytest.raises(ValueError, match='base changed'):
        rolling.publish_bundle(root, bundle, 'main')
