"""Operations gates must keep the source Vault unchanged until all checks pass."""
from datetime import datetime, timezone, timedelta
import gzip
import hashlib
from pathlib import Path
import shutil

import pytest
import yaml

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
    # Curated narratives and key moments cite real archived releases and cards, which a
    # fixture run lacks; without them the fixture vault reports no editorial warnings.
    editorial = root / '_scripts/editorial.yaml'
    spec = yaml.safe_load(editorial.read_text())
    spec.pop('key_moments', None)
    spec.pop('themes', None)
    editorial.write_text(yaml.safe_dump(spec, sort_keys=False, allow_unicode=True))
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
    generate = workflows['generate']['jobs']
    assert generate['generate']['runs-on'] == 'ubuntu-24.04'
    assert generate['generate']['permissions'] == {'contents': 'read', 'pull-requests': 'read'}
    assert generate['publish']['needs'] == 'generate'
    assert generate['publish']['permissions'] == {'contents': 'write', 'pull-requests': 'write', 'actions': 'write'}
    assert 'default_branch' in generate['generate']['if']
    assert workflows['generate']['on']['workflow_dispatch']['inputs']['preview']['default'] == 'false'
    assert 'inputs.preview != true' in generate['publish']['if']
    assert 'default_branch' in generate['publish']['if']
    generation_steps = generate['generate']['steps']
    for step_name in ('Prepare managed review branch', 'Export gated candidate without writing to GitHub'):
        assert next(s for s in generation_steps if s.get('name') == step_name)['if'] == 'inputs.preview != true'
    collector = next(s for s in generation_steps if s.get('name') == 'Collect and gate isolated candidate')
    assert '--snapshot-bundle _inputs/chatgpt' not in collector['run']
    assert '--allow-partial' in collector['run'] and '--browser-fallback' in collector['run']
    assert 'if [ "$PREVIEW" != true ]; then args+=(--apply); fi' in collector['run']
    assert collector['env']['CHRONOLOG_BROWSER_HEADED'] == '1'
    publisher = generate['publish']['steps']
    checkout = next(s for s in publisher if s.get('uses') == 'actions/checkout@v4')
    assert checkout['with']['ref'] == '${{ github.sha }}'
    assert checkout['with']['persist-credentials'] == 'false'
    assert not any('pip install' in s.get('run', '') or 'npm' in s.get('run', '') for s in publisher)
    assert 'CHRONOLOG_BOT_TOKEN' not in (ROOT/'.github/workflows/generate.yml').read_text()
    assert 'expected_head' in workflows['quality']['on']['workflow_dispatch']['inputs']
    assert any('test "$GITHUB_SHA" = "$EXPECTED_HEAD"' in s.get('run', '') for s in workflows['quality']['jobs']['quality']['steps'])
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


def root_page_vault(root):
    """A minimal Vault with both root pages, a product page and archive pages, without
    wiki links."""
    for name, title in (('index.md', 'ChronoLog'), ('About.md', 'About the data'),
                        ('Products/Cursor.md', 'Cursor'), ('Archive/index.md', 'Archive'),
                        ('Archive/2026-10.md', 'October 2026')):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f'---\ntitle: {title}\n---\n\n# {title}\n')
    return root


def test_about_is_enumerated_wherever_index_is(tmp_path, monkeypatch):
    from _scripts import rolling_pr
    from _scripts.transaction import DIRECTORIES, copy_pages, files
    from _scripts.validate import ROOT_PAGES, VAULT_DIRECTORIES, vault_markdown_files
    assert ROOT_PAGES == ('index.md', 'About.md')
    assert 'Archive' in VAULT_DIRECTORIES
    vault = root_page_vault(tmp_path / 'vault')

    assert {'index.md', 'About.md', 'Archive/index.md', 'Archive/2026-10.md'} <= set(files(vault))
    assert {vault / 'index.md', vault / 'About.md', vault / 'Archive/index.md',
            vault / 'Archive/2026-10.md'} <= set(vault_markdown_files(vault))
    # Content scope of the rolling PR publisher (kept literal there).
    assert set(rolling_pr.VAULT) == {*VAULT_DIRECTORIES, '_review', *ROOT_PAGES}
    assert set(DIRECTORIES) == {*VAULT_DIRECTORIES, '_review'}
    # Pipeline stage and manual replays copy with copy_pages.
    stage = tmp_path / 'stage'
    stage.mkdir()
    copy_pages(vault, stage, create_missing=True)
    assert (stage / 'About.md').exists() and (stage / 'Releases').is_dir()
    assert (stage / 'Archive/index.md').exists() and (stage / 'Archive/2026-10.md').exists()
    # Candidate copy.
    source = root_page_vault(tmp_path / 'source')
    (source / '_scripts').mkdir()
    operations.copy_vault(source, tmp_path / 'candidate')
    assert (tmp_path / 'candidate/About.md').read_text() == (source / 'About.md').read_text()
    assert (tmp_path / 'candidate/Archive/2026-10.md').exists()
    # Quality report counts root pages by kind.
    before = inventory(vault)
    about = vault / 'About.md'
    about.write_text(about.read_text() + '\nChanged.\n')
    report = changes(before, inventory(vault))
    assert report['by_kind']['About.md']['modified'] == 1
    assert report['by_kind']['index.md']['modified'] == 0
    month = vault / 'Archive/2026-10.md'
    month.unlink()
    report = changes(before, inventory(vault))
    assert report['by_kind']['Archive']['removed'] == 1
    month.write_text('---\ntitle: October 2026\n---\n\n# October 2026\n')
    # The Quartz build copy of validate_site.
    built = {}

    def fake_command(args, root, out, name, report, env=None):
        if name == 'build':
            build_vault = Path(args[args.index('--directory') + 1])
            built.update({p.relative_to(build_vault).as_posix(): True for p in build_vault.rglob('*.md')})

    class Stop(Exception):
        pass

    def stop(*args):
        raise Stop()

    monkeypatch.setattr(operations, 'command', fake_command)
    monkeypatch.setattr(operations, 'audit', stop)
    out = tmp_path / 'out'
    out.mkdir()
    with pytest.raises(Stop):
        operations.validate_site(ROOT, vault, out, {'checks': {}}, 'localhost:8080')
    assert {'index.md', 'About.md', 'Archive/index.md', 'Archive/2026-10.md', 'Products/Cursor.md'} <= set(built)


def test_pipeline_stage_keeps_human_text_on_about(vault):
    run_pipeline(vault, 'seed', collection=payload(), today='2026-10-13')
    about = vault / 'About.md'
    assert '## Sources and coverage' in about.read_text()
    about.write_text(about.read_text() + '\nReviewer note kept outside the regions.\n')
    run_pipeline(vault, 'again', collection=payload(acquired='2026-10-14T10:00:00Z'), today='2026-10-14')
    text = about.read_text()
    assert 'Reviewer note kept outside the regions.' in text
    assert 'Last successful fetch: 2026-10-14T10:00:00Z.' in text


def test_publication_audit_expects_root_pages_and_the_archive_page(tmp_path):
    import importlib.util
    import json
    spec = importlib.util.spec_from_file_location('m2_audit', ROOT / 'tests/manual/check_m2_publication.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    vault = root_page_vault(tmp_path / 'vault')
    (vault / 'Products/Cursor.md').unlink()
    (vault / 'Archive/2026-10.md').unlink()
    site = tmp_path / 'site'
    (site / 'Archive').mkdir(parents=True)
    (site / 'static').mkdir()
    for slug in ('index', 'About', 'Archive/index'):
        (site / f'{slug}.html').write_text('<a href="https://elsewhere.example/">About the data</a>')
    index = {'index': {'content': '3 products · 0 tracked changes · 0 themes', 'links': []},
             'About': {'content': 'About the data', 'links': []},
             'Archive/index': {'content': 'No changes archived yet.', 'links': []}}
    (site / 'static/contentIndex.json').write_text(json.dumps(index))
    assert mod.audit(vault, site)['active_pages'] == 3
    for root_page in ('About', 'Archive/index'):
        reduced = {slug: page for slug, page in index.items() if slug != root_page}
        (site / 'static/contentIndex.json').write_text(json.dumps(reduced))
        with pytest.raises(AssertionError):
            mod.audit(vault, site)


def test_publication_audit_expects_one_archive_page_per_month_with_cards(tmp_path):
    import importlib.util
    import json
    spec = importlib.util.spec_from_file_location('m2_audit', ROOT / 'tests/manual/check_m2_publication.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # The Vault link check has its own tests; this one is about the page set.
    mod.read_history = lambda *args: ([], [], [])
    mod.validate_vault_links = lambda *args: {'errors': []}
    vault = root_page_vault(tmp_path / 'vault')
    card = vault / 'Changes/Cursor/2026-10-01-agent.md'
    card.parent.mkdir(parents=True)
    card.write_text("---\ntitle: Agent\ncard_id: cursor-2026-10-01-aaaaaa\nproduct: cursor\n"
                    "product_name: Cursor\ntheme: uncategorized\ndate: '2026-10-01'\ntype: change\n---\n")
    site = tmp_path / 'site'
    (site / 'static').mkdir(parents=True)
    slugs = ('index', 'About', 'Archive/index', 'Archive/2026-10', 'Products/Cursor',
             'Changes/Cursor/2026-10-01-agent')
    for slug in slugs:
        (site / f'{slug}.html').parent.mkdir(parents=True, exist_ok=True)
        (site / f'{slug}.html').write_text('<p>page</p>')
    index = {slug: {'content': '', 'links': []} for slug in slugs}
    index['index']['content'] = '1 tracked changes'
    index['Products/Cursor']['content'] = 'All tracked changes (1 card)'
    index['Archive/index']['links'] = ['Archive/2026-10']
    index['Archive/2026-10']['content'] = '1 tracked change · Cursor 1'

    def audit(**month):
        (site / 'static/contentIndex.json').write_text(json.dumps(
            {**index, 'Archive/2026-10': {**index['Archive/2026-10'], **month}}))
        return mod.audit(vault, site)

    assert audit()['archive_months'] == 1
    with pytest.raises(AssertionError):
        audit(content='2 tracked changes · Cursor 2')
    # A month page without active cards is not expected.
    (vault / 'Archive/2025-01.md').write_text('---\ntitle: January 2025\n---\n')
    (site / 'Archive/2025-01.html').write_text('<p>page</p>')
    index['Archive/2025-01'] = {'content': '', 'links': []}
    with pytest.raises(AssertionError):
        audit()


def test_pipeline_measures_cadence_to_the_archive_date_and_writes_the_archive(vault):
    manifest = run_pipeline(vault, 'seed', collection=payload(), today='2026-10-13')

    silence = read_json(vault / '_pipeline/seed/03c-silence/alerts.json')
    assert silence['alerts'] == []
    assert silence['cadence']['cursor']['as_of'] == '2026-10-01'  # newest release, not today
    assert silence['cadence']['cursor']['status'] == 'not-tracked'  # fewer than four releases
    assert manifest['editorial_warnings'] == []
    assert (vault / 'Archive/2026-10.md').exists() and (vault / 'Archive/index.md').exists()
    assert '## Release cadence' in (vault / 'Products/Cursor.md').read_text()
    assert 'Last release 2026-10-01 (the archive date)' in (vault / 'Products/Cursor.md').read_text()
    # The same archive regenerated on a later day renders the same pages.
    assert run_pipeline(vault, 'later', collection=payload(), today='2026-12-20')['status'] == 'no-change'


def test_pipeline_reports_unknown_editorial_key_moments_without_failing(vault):
    editorial = vault / '_scripts/editorial.yaml'
    editorial.write_text(editorial.read_text() + 'key_moments:\n  agent-mode:\n    - cursor-2020-01-01-ffffff\n')

    manifest = run_pipeline(vault, 'seed', collection=payload(), today='2026-10-13')

    assert manifest['status'] == 'published'
    assert manifest['editorial_warnings'] == [{'theme': 'agent-mode', 'card_id': 'cursor-2020-01-01-ffffff',
                                               'reason': 'not an active card of this theme; ignored'}]
