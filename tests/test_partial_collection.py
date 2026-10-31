"""Failed sources must never be re-extracted, retired or mistaken for fresh data."""
from copy import deepcopy

import frontmatter
import pytest

from _scripts.common import PipelinePaths, read_json
from _scripts.history import read_history
from _scripts.pipeline import check_collection
from _scripts.transaction import snapshot
from test_reliable_pipeline import vault, release, collection, run, PENDING_PROSE


def degraded(releases):
    data = collection(releases, requested=['chatgpt', 'cursor'])
    data['sources'][0].update(status='failed', count=0, complete=False, error='HTTP 403')
    data['errors'] = [{'product': 'chatgpt', 'error': 'HTTP 403'}]
    return data


def test_partial_preserves_failed_source_history_pending_and_human_notes(vault):
    chat = release('chatgpt')
    pending = release('chatgpt', date='2026-06-01', body=PENDING_PROSE, source_type='chatgpt_changelog')
    seed = collection([chat, pending, release()])
    seed['sources'][0].update(acquisition='http', acquired_at='2026-07-01T00:00:00Z')
    run(vault, 'seed', seed, reconcile=True)
    page = next((vault / 'Changes/ChatGPT').glob('*.md'))
    page.write_text(page.read_text() + '\nHuman research notes.\n')
    old = snapshot(vault)
    old_history = read_history(vault, {'chatgpt'})
    data = degraded([release(date='2026-07-02')])
    result = run(vault, 'partial', data, reconcile=True, allow_partial=True)
    assert result['reconcile_products'] == ['cursor']
    assert result['retained_products'] == ['chatgpt']
    assert result['collection_health'] == 'degraded'
    assert read_history(vault, {'chatgpt'}) == old_history
    new = snapshot(vault)
    for path in old:
        if path.startswith(('Releases/ChatGPT/', '_review/')):
            assert new[path] == old[path], path
        if path.startswith('Changes/ChatGPT/'):
            assert path in new
    # Nearby links can follow the healthy product's new cards; facts and human text stay.
    assert 'Human research notes.' in page.read_text()
    assert '2026-07-02' in (vault / 'Products/Cursor.md').read_text()
    coverage = frontmatter.load(vault / 'Products/ChatGPT.md')['coverage']
    assert coverage['last_successful_fetch'] == '2026-07-01T00:00:00Z'
    assert coverage['collection_status'] == 'delayed'
    assert 'Collection delayed' in (vault / 'index.md').read_text()
    silence = read_json(PipelinePaths('partial', vault).silence)
    assert not any(a['product'] == 'chatgpt' for a in silence['alerts'])
    assert silence['cadence']['chatgpt']['status'] == 'collection-delayed'
    assert any(p['product'] == 'chatgpt' and p['silence_tracking'] == 'collection-error'
               for p in silence['pending'])
    # New error text/time is evidence, not a daily modification of reader content.
    repeated = deepcopy(data)
    repeated['sources'][0].update(error='HTTP 503', collected_at='2026-07-29T02:00:00Z')
    assert run(vault, 'repeat', repeated, reconcile=True, allow_partial=True)['status'] == 'no-change'
    assert snapshot(vault) == new
    recovered = collection([chat, pending, release(date='2026-07-02')])
    recovered['sources'][0].update(acquisition='http', acquired_at='2026-07-29T03:00:00Z')
    result = run(vault, 'recovery', recovered, reconcile=True, allow_partial=True)
    assert result['collection_health'] == 'healthy'
    assert 'Collection delayed' not in (vault / 'index.md').read_text()
    assert 'collection_status' not in frontmatter.load(vault / 'Products/ChatGPT.md')['coverage']


def test_partial_without_failed_source_baseline_still_blocks(vault):
    run(vault, 'seed', collection([release()]))
    before = snapshot(vault)
    with pytest.raises(ValueError, match='historical source baseline'):
        run(vault, 'partial', degraded([release()]), reconcile=True, allow_partial=True)
    assert snapshot(vault) == before


def test_all_failed_never_claims_no_change(vault):
    run(vault, 'seed', collection([release('chatgpt'), release()]))
    before = snapshot(vault)
    data = degraded([])
    data['sources'][1].update(status='failed', complete=False, error='offline')
    with pytest.raises(ValueError, match='no successful sources'):
        run(vault, 'all-failed', data, reconcile=True, allow_partial=True)
    assert snapshot(vault) == before


@pytest.mark.parametrize('fault', ['failed-data', 'incomplete', 'unattributed', 'duplicate', 'missing-error'])
def test_partial_does_not_relax_input_integrity(fault):
    data = degraded([release()])
    if fault == 'failed-data':
        data['releases'].append(release('chatgpt'))
    elif fault == 'incomplete':
        data['sources'][1]['complete'] = False
    elif fault == 'unattributed':
        data['errors'].append({'product': 'cursor', 'error': 'bad'})
    elif fault == 'duplicate':
        data['sources'].append(data['sources'][0])
    else:
        data['sources'][0].pop('error')
    with pytest.raises(ValueError):
        check_collection(data, reconcile=True, allow_partial=True)
