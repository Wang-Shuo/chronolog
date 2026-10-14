"""Operations gates must keep the source Vault unchanged until all checks pass."""
from datetime import datetime, timezone, timedelta
import gzip
import hashlib
from pathlib import Path
import shutil

import pytest

from _scripts import operations
from _scripts.collect import normalize_release, source_result
from _scripts.common import read_json, write_json
from _scripts.pipeline import run_pipeline
from _scripts.quality import inventory, changes
from _scripts.snapshot_bundle import load_bundle, SOURCE
from _scripts.transaction import snapshot

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def vault(tmp_path):
    root = tmp_path / 'vault'
    shutil.copytree(ROOT / '_scripts', root / '_scripts', ignore=shutil.ignore_patterns('__pycache__'))
    return root


def payload(day='2026-10-01', acquired='2026-10-13T10:00:00Z'):
    release = normalize_release({'name':'cursor','display_name':'Cursor'}, release_date=day, version=day,
        title='Agent update', body='Agent can run shell commands after approval.',
        source_url=f'https://cursor.com/changelog/{day}', source_type='cursor_changelog')
    state = source_result('cursor', [release], complete=True, coverage='available-endpoint')
    state.update(acquisition='http', acquired_at=acquired)
    return {'source':'live','mode':'full','errors':[],'releases':[release],'sources':[state]}


def passed(root, candidate, out, report, base):
    report['checks']['test-gate'] = {'status':'passed'}


def failed(*args):
    raise operations.GateFailure('simulated build failure')


def run(vault, tmp_path, data, gate=passed, apply=False):
    return operations.run(vault, 'ops', tmp_path/'report', mode='generate', base_url='localhost:8080',
                          collection=data, gate=gate, apply=apply)


def test_candidate_is_only_applied_after_success(vault, tmp_path):
    before = snapshot(vault)
    result = run(vault,tmp_path,payload())
    assert result['status']=='ready'
    assert snapshot(vault)==before
    assert result['changes']['counts']['added']>0
    result = operations.run(vault,'apply',tmp_path/'apply',mode='generate',base_url='localhost:8080',
                            collection=payload(),gate=passed,apply=True)
    assert result['status']=='candidate-applied'
    assert snapshot(vault)!=before
    assert (tmp_path/'apply/quality.md').exists()


def test_failed_build_keeps_existing_vault_and_archives_failure(vault, tmp_path):
    run_pipeline(vault,'seed',collection=payload(),today='2026-10-13')
    before = snapshot(vault)
    result = run(vault,tmp_path,payload('2026-10-02'),gate=failed,apply=True)
    assert result['status']=='failed'
    assert snapshot(vault)==before
    assert 'simulated build failure' in (tmp_path/'report/quality.md').read_text()
    evidence=read_json(tmp_path/'report/evidence-sha256.json')
    assert 'collection.json.gz' in evidence and 'quality.json' in evidence


def test_fresh_acquisition_without_new_facts_does_not_open_pr(vault,tmp_path):
    run_pipeline(vault,'seed',collection=payload(),today='2026-10-13')
    before=snapshot(vault)
    result=run(vault,tmp_path,payload(acquired='2026-10-13T11:00:00Z'),apply=True)
    assert result['status']=='no-change'
    assert not result['changes']['content_changed']
    assert result['changes']['counts']['acquisition_only']>0
    assert snapshot(vault)==before
    assert result['sources'][0]['acquired_at']=='2026-10-13T11:00:00Z'


@pytest.mark.parametrize('all_failed',[False,True])
def test_failed_sources_keep_previous_content_and_source_status(vault,tmp_path,all_failed):
    run_pipeline(vault,'seed',collection=payload(),today='2026-10-13')
    before=snapshot(vault); data=payload()
    data['sources'].append(source_result('chatgpt',[],complete=False,coverage='available-endpoint',error='HTTP 403'))
    if all_failed:
        data['sources'][0].update(status='failed',error='HTTP 503')
    data['errors']=[{'product':s['product'],'error':s['error']} for s in data['sources'] if s['status']=='failed']
    result=run(vault,tmp_path,data,apply=True)
    assert result['status']=='failed' and snapshot(vault)==before
    assert len([s for s in result['sources'] if s['status']=='failed'])==(2 if all_failed else 1)


def test_machine_conflict_is_visible_and_never_overwritten(vault,tmp_path):
    run_pipeline(vault,'seed',collection=payload(),today='2026-10-13')
    p=next((vault/'Changes').rglob('*.md'))
    p.write_text(p.read_text().replace('Agent can run shell commands after approval.','Edited machine evidence.'))
    before=snapshot(vault)
    result=run(vault,tmp_path,payload(),apply=True)
    assert result['status']=='failed' and result['conflicts']
    assert snapshot(vault)==before


def test_concurrent_edit_during_gate_is_preserved(vault,tmp_path):
    def editing_gate(root,*_):
        (root/'index.md').write_text('# Concurrent human note\n')
    result=run(vault,tmp_path,payload(),gate=editing_gate,apply=True)
    assert result['status']=='failed'
    assert (vault/'index.md').read_text()=='# Concurrent human note\n'


def test_source_range_and_human_note_changes_are_content_changes(vault):
    run_pipeline(vault,'seed',collection=payload(),today='2026-10-13')
    before=inventory(vault)
    p=vault/'index.md';p.write_text(p.read_text()+'\nHuman research note.\n')
    assert changes(before,inventory(vault))['content_changed']


def test_snapshot_requires_actual_capture_date_and_matching_bytes(tmp_path):
    body=b'<html>'+b'official release body '*100+b'</html>'
    (tmp_path/'chatgpt.html.gz').write_bytes(gzip.compress(body))
    now=datetime(2026,10,13,12,tzinfo=timezone.utc)
    meta={'source_url':SOURCE,'acquisition':'browser-snapshot','captured_at':now.isoformat(),
          'sha256':hashlib.sha256(body).hexdigest()}
    write_json(tmp_path/'capture.json',meta)
    assert load_bundle(tmp_path,now=now)[0]==body
    with pytest.raises(ValueError,match='expired'):
        load_bundle(tmp_path,now=now+timedelta(days=2))
    with pytest.raises(ValueError,match='future'):
        load_bundle(tmp_path,now=now-timedelta(days=1))
    meta['sha256']='incorrect';write_json(tmp_path/'capture.json',meta)
    with pytest.raises(ValueError,match='digest'):
        load_bundle(tmp_path,now=now)


@pytest.mark.parametrize('bad',['https://example.org','user:pass@example.org','example.org?q=x','example.org/#x','localhost:8080','example.invalid','example.org/../private'])
def test_production_base_url_cannot_silently_publish_local_links(bad):
    with pytest.raises(ValueError):operations.validate_base_url(bad,production=True)


def test_github_pages_project_path_is_preserved():
    assert operations.validate_base_url('owner.github.io/chronolog/',production=True)=='owner.github.io/chronolog'


def test_deployment_requires_human_approval_on_exact_merged_head():
    from _scripts.review_gate import approved_merge
    pr={'merged_at':'2026-10-13','merge_commit_sha':'merge','base':{'ref':'main'},
        'head':{'sha':'head'},'user':{'login':'author'}}
    review={'state':'APPROVED','commit_id':'head','submitted_at':'2026-10-13T10:00:00Z',
            'user':{'login':'reviewer','type':'User'}}
    assert approved_merge(pr,[review],'merge','main')
    assert not approved_merge(pr,[{**review,'commit_id':'previous-head'}],'merge','main')
    assert not approved_merge(pr,[],'merge','main')
    assert not approved_merge(pr,[review],'different-commit','main')
    assert not approved_merge(pr,[{**review,'user':{'login':'bot','type':'Bot'}}],'merge','main')
    assert not approved_merge(pr,[review,{**review,'state':'DISMISSED','submitted_at':'2026-10-13T11:00:00Z'}],'merge','main')


def test_public_verification_rejects_stale_commit_and_mixed_artifacts():
    import json
    from _scripts.verify_public import verify
    base='https://owner.github.io/chronolog'
    index=json.dumps({'index':{},'Products/ChatGPT':{}}).encode()
    rss=f'<rss><channel><item><link>{base}/Products/ChatGPT</link></item></channel></rss>'.encode()
    identity={'commit':'abc','kind':'commit-build',
        'content_index_sha256':hashlib.sha256(index).hexdigest(),'rss_sha256':hashlib.sha256(rss).hexdigest()}
    pages={base+'/deployment.json':json.dumps(identity).encode(),base+'/static/contentIndex.json':index,
           base+'/index.xml':rss,base+'/':b'<html>Home</html>'}
    assert verify(base,'abc',pages.__getitem__)['status']=='passed'
    with pytest.raises(ValueError,match='commit'):verify(base,'stale',pages.__getitem__)
    pages[base+'/index.xml']=b'<rss>wrong version</rss>'
    with pytest.raises(ValueError,match='manifest'):verify(base,'abc',pages.__getitem__)


def test_untrusted_snapshot_rejection_does_not_hide_http_error(vault,tmp_path,monkeypatch):
    data=payload();data['sources'].append(source_result('chatgpt',[],complete=False,coverage='available-endpoint',error='HTTP 403'))
    data['errors']=[{'product':'chatgpt','error':'HTTP 403'}]
    monkeypatch.setattr(operations,'collect_live',lambda *a:data)
    result=operations.collect(vault,tmp_path,tmp_path/'missing-bundle')
    assert result['errors'] and result['sources'][-1]['status']=='failed'
    assert 'snapshot fallback rejected' in result['sources'][-1]['error']


def test_seven_replays_or_missing_days_do_not_satisfy_live_acceptance():
    from _scripts.verify_schedule import assess
    now=datetime(2026,10,13,12,tzinfo=timezone.utc)
    runs=[{'databaseId':i,'event':'schedule','status':'completed','conclusion':'success',
           'createdAt':(now-timedelta(days=i)).isoformat()} for i in range(7)]
    reports={i:{'input_kind':'live','status':'no-change',
                'sources':[{'product':p,'status':'success'} for p in ['chatgpt','claude-code','cursor']]} for i in range(7)}
    assert assess(runs,reports,now)['scheduled_runs']==7
    reports[0]['input_kind']='replay'
    with pytest.raises(ValueError,match='replay'):assess(runs,reports,now)
    reports[0]['input_kind']='live';runs[0]['createdAt']=(now-timedelta(days=10)).isoformat()
    with pytest.raises(ValueError,match='consecutive'):assess(runs,reports,now)


def test_workflows_keep_prs_unprivileged_and_deploy_behind_review_and_build():
    import yaml
    workflows={p.stem:yaml.load(p.read_text(),Loader=yaml.BaseLoader) for p in (ROOT/'.github/workflows').glob('*.yml')}
    assert 'pull_request' in workflows['quality']['on']
    assert 'pull_request_target' not in workflows['quality']['on']
    assert workflows['quality']['permissions']=={'contents':'read'}
    assert workflows['generate']['concurrency']['cancel-in-progress']=='false'
    deploy=workflows['deploy']['jobs']
    assert deploy['deploy']['needs']=='build'
    assert deploy['build']['permissions']=={'contents':'read','pull-requests':'read','pages':'read'}
    assert deploy['deploy']['permissions']['pages']=='write'
    steps=deploy['build']['steps']
    assert any('_scripts.review_gate' in s.get('run','') for s in steps)
    assert any('_scripts.operations' in s.get('run','') and '--production' in s['run'] for s in steps)
    assert any('_scripts.verify_public' in s.get('run','') for s in deploy['deploy']['steps'])


def test_html_audit_resolves_project_prefix_and_rejects_escaping_links(tmp_path):
    import importlib.util
    spec=importlib.util.spec_from_file_location('m2_audit',ROOT/'tests/manual/check_m2_publication.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    (tmp_path/'index.html').write_text('<a href="/chronolog">Home</a>')
    p=tmp_path/'Releases/Cursor/test.html';p.parent.mkdir(parents=True)
    p.write_text('<a href="../../index.html">Home</a>')
    assert mod.audit_html(tmp_path,'owner.github.io/chronolog')==2
    p.write_text('<a href="../../../tags/Heading">Wrong root</a>')
    with pytest.raises(AssertionError,match='escapes deployment path'):
        mod.audit_html(tmp_path,'owner.github.io/chronolog')
