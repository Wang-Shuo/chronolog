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


def test_one_pr_is_reused_and_open_branch_human_notes_survive(repo):
    root,remote,responses=repo
    state=rolling.prepare(root,'main',root/'_pipeline/state.json')
    (root/'index.md').write_text('# Home\n\nFirst generated release.\n')
    assert rolling.publish(root,state,report(root))['status']=='review-required'
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
    rolling.publish(root,state,report(root))
    assert sum(c[1:3]==('pr','create') for c in responses['calls'])==1
    assert sum(c[1:3]==('pr','edit') for c in responses['calls'])==1
    before=git(remote,'rev-parse','refs/heads/'+rolling.BRANCH)
    result=rolling.publish(root,state,report(root,'no-change'))
    assert result['status']=='no-change'
    assert git(remote,'rev-parse','refs/heads/'+rolling.BRANCH)==before


def test_push_lease_rejects_a_concurrent_remote_edit(repo,tmp_path):
    root,remote,responses=repo
    state=rolling.prepare(root,'main',root/'_pipeline/state.json')
    (root/'index.md').write_text('# Initial candidate\n');rolling.publish(root,state,report(root))
    responses['open']=[{'number':1,'url':'https://github.com/test/chronolog/pull/1'}]
    state=rolling.prepare(root,'main',root/'_pipeline/state.json')
    other=tmp_path/'other';subprocess.run(['git','clone','-b',rolling.BRANCH,str(remote),str(other)],check=True,capture_output=True)
    git(other,'config','user.name','Other');git(other,'config','user.email','other@example.org')
    (other/'index.md').write_text('# Concurrent reviewer edit\n')
    git(other,'add','index.md');git(other,'commit','-m','concurrent human change');git(other,'push','origin',rolling.BRANCH)
    remote_sha=git(remote,'rev-parse','refs/heads/'+rolling.BRANCH)
    (root/'index.md').write_text('# Generated later\n')
    with pytest.raises(subprocess.CalledProcessError):rolling.publish(root,state,report(root))
    assert git(remote,'rev-parse','refs/heads/'+rolling.BRANCH)==remote_sha
