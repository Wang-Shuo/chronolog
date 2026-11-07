import json
from pathlib import Path

import pytest

from _scripts import additional_feeds as feeds, collect
from _scripts.extract import extract_cards_from_release, load_theme_vocabulary

ROOT = Path(__file__).resolve().parents[1]


def product(name):
    return {'name': name, 'display_name': {'lm-studio':'LM Studio', 'wispr-flow':'Wispr Flow'}.get(name, name.title()),
            'feed_type': {'lm-studio':'lmstudio_changelog', 'wispr-flow':'wispr_flow_changelog'}.get(name, name+'_changelog'),
            'url':'https://official.example/changelog', 'markdown_url':'https://official.example/changelog.md',
            'api_url':'https://official.example/api/changelog'}


KREA = '**November 4, 2026**\n\nAccess Controls\n\n## Agent rules\n\nAdmins can now control agent access.\n\n**November 4, 2026**\n\nNew Image Model\n\n## Image model\n\nAdded a new image model.\n\nThis documentation is built and hosted on Mintlify.'


def test_dated_markdown_keeps_same_day_announcements_distinct_and_removes_footer():
    rows=feeds.parse_dated_markdown(product('krea'), KREA, 'https://official.example/changelog')
    assert len(rows)==2 and len({r['release_id'] for r in rows})==2
    assert {r['date'] for r in rows}=={'2026-11-04'}
    assert all('Mintlify' not in r['body'] and r['title'] not in r['body'] for r in rows)


@pytest.mark.parametrize('text', ['', KREA.replace('November 4, 2026','November 32, 2026'),
                                '**November 4, 2026**\n\nMissing body'])
def test_dated_markdown_rejects_empty_or_invalid_announcements(text):
    with pytest.raises(ValueError):
        feeds.parse_dated_markdown(product('krea'),text,'https://official.example/changelog')


def test_devin_uses_annual_text_and_verifies_recent_date_coverage(monkeypatch):
    p=product('devin')
    overview='**November 4, 2026**\n\n**Feature**\n\nOlder overview text.\n\n## All Release Notes\n\n[2026 Release Notes](https://official.example/release-notes/2026.md)'
    annual='# 2026\n\n**November 4, 2026**\n\n**Feature**:\n\nUpdated authoritative description.\n\n***\n'
    pages={p['markdown_url']:overview,'https://official.example/release-notes/2026.md':annual}
    monkeypatch.setattr(feeds,'get_text',pages.__getitem__)
    rows=feeds.fetch_devin(p,None)
    assert len(rows)==1 and rows[0]['body']=='### Feature\n\nUpdated authoritative description.'
    assert rows[0]['source_url']=='https://official.example/release-notes/2026'
    pages[p['markdown_url']]=overview.replace('November 4','November 5')
    with pytest.raises(ValueError,match='missing a recent'):
        feeds.fetch_devin(p,None)
    with pytest.raises(ValueError,match='year archive'):
        feeds.parse_dated_markdown(p,annual,'https://official.example/release-notes/2025','2025')


def raycast_page(version='2.1', next_href=None):
    return f'<article><div class="a_changelogMeta"><a href="/changelog/macos/{version}">v{version}</a><span class="a_changelogDate">November 4, 2026</span></div><div class="markdown a_changelogBody"><h2>New</h2><ul><li>Added voice commands.</li></ul></div></article>' + (f'<a title="Next Page" href="{next_href}">Next</a>' if next_href else '')


def test_raycast_exhausts_each_platform_and_does_not_merge_equal_versions(monkeypatch):
    p={**product('raycast'),'surfaces':['macos','windows']}
    pages={p['url']+'/macos':raycast_page(next_href='/changelog/macos/2'),
           p['url']+'/macos/2':raycast_page('2.0'),p['url']+'/windows':raycast_page()}
    monkeypatch.setattr(feeds,'get_text',pages.__getitem__)
    rows=feeds.fetch_raycast(p,None)
    assert {r['version'] for r in rows}=={'macos/2.1','macos/2.0','windows/2.1'}
    pages[p['url']+'/macos/2']=raycast_page()
    with pytest.raises(ValueError,match='repeated'):
        feeds.fetch_raycast(p,None)


@pytest.mark.parametrize('href',['https://outside.example/page','/changelog/windows/2','/changelog/macos/0'])
def test_raycast_rejects_wrong_archive_pagination(href):
    with pytest.raises(ValueError):
        feeds.parse_raycast(product('raycast'),'macos',raycast_page(next_href=href))


def superwhisper_page(label='macOS',date='Nov 6, 2026'):
    return f'<button class="text-trigray-100">{label}</button><div class="space-y-12"><div><div><p>3.2.1</p><span>{date}</span></div><div><b>Fixes</b><ul><li>Fixed clipboard pasting.</li></ul></div></div></div>'


def test_superwhisper_verifies_selected_platform_and_preserves_fix_section():
    rows=feeds.parse_superwhisper(product('superwhisper'),'macos',superwhisper_page())
    assert rows[0]['version']=='macos/3.2.1'
    assert rows[0]['body']=='### Fixes\n\n- Fixed clipboard pasting.'
    with pytest.raises(ValueError,match='wrong platform'):
        feeds.parse_superwhisper(product('superwhisper'),'windows',superwhisper_page())
    with pytest.raises(ValueError):
        feeds.parse_superwhisper(product('superwhisper'),'macos',superwhisper_page(date='November 2026'))


WISPR='<div id="older-anchor"><div class="release-item-grid-v2"><div class="release-date">October 30, 2026</div><div release-content="all-platforms"><div class="wn_body w-richtext"><h3>Meeting summary</h3><p>Meeting summaries now finish faster.</p></div></div></div></div>'


def test_wispr_uses_visible_date_and_carries_feature_platform_scope():
    row=feeds.parse_wispr_flow(product('wispr-flow'),WISPR)[0]
    assert row['date']=='2026-10-30' and row['source_url'].endswith('#older-anchor')
    assert '### Meeting summary (All platforms)' in row['body']
    with pytest.raises(ValueError,match='unknown platform'):
        feeds.parse_wispr_flow(product('wispr-flow'),WISPR.replace('all-platforms','new-platform'))


def lm_item(version='0.4.28'):
    return {'version':version,'build':2,'releaseDateIso':'2026-10-31T00:42:40.368Z',
            'releaseNotesMarkdownText':f'### {version} - Release Notes\n\n**Build 2**\n\n- Fixed chat reliability.'}


def test_lmstudio_exhausts_api_and_checks_total(monkeypatch):
    p=product('lm-studio')
    pages={p['api_url']+'?offset=0&limit=10':{'items':[lm_item()],'nextOffset':1,'totalCount':2,'errorMessage':None},
           p['api_url']+'?offset=1&limit=10':{'items':[lm_item('0.4.27')],'nextOffset':None,'totalCount':2,'errorMessage':None}}
    monkeypatch.setattr(feeds,'get_text',lambda url:json.dumps(pages[url]))
    rows=feeds.fetch_lmstudio(p,None)
    assert len(rows)==2 and all('### Build 2' in r['body'] and 'Release Notes' not in r['body'] for r in rows)
    assert rows[0]['source_url'].endswith('/lmstudio-v0.4.28')
    pages[p['api_url']+'?offset=1&limit=10']['items']=[lm_item()]
    with pytest.raises(ValueError,match='repeated'):
        feeds.fetch_lmstudio(p,None)


@pytest.mark.parametrize('changes', [{'nextOffset':None,'totalCount':2}, {'nextOffset':2,'totalCount':3},
                                    {'items':[]}, {'errorMessage':'partial backend failure'}, {'nextOffset':True}])
def test_lmstudio_rejects_partial_or_malformed_results(monkeypatch,changes):
    payload={'items':[lm_item()],'nextOffset':None,'totalCount':1,'errorMessage':None,**changes}
    monkeypatch.setattr(feeds,'get_text',lambda url:json.dumps(payload))
    with pytest.raises(ValueError):
        feeds.fetch_lmstudio(product('lm-studio'),None)


def test_new_feed_dispatch_preserves_full_collection_contract(tmp_path,monkeypatch):
    import yaml
    p=product('krea')
    config=tmp_path/'sources.yaml'
    config.write_text(yaml.safe_dump({'products':[p]}))
    monkeypatch.setattr(feeds,'get_text',lambda _:KREA)
    payload=collect.collect_live(config,tmp_path/'collection.json',None,'all')
    assert not payload['errors'] and len(payload['releases'])==2
    assert payload['sources'][0]['complete'] and payload['sources'][0]['coverage']=='available-endpoint'


@pytest.mark.parametrize('heading', ['Build 1', 'Features & Improvements', 'Features and Fixes', 'Other'])
def test_category_labels_do_not_become_feature_launches(heading):
    row = collect.normalize_release(product('lm-studio'), release_date='2026-10-31', version='0.4.28',
        title='LM Studio 0.4.28', body=f'### {heading}\n\n- Added support for new models.\n- Added MCP servers.\n- Fixed chat formatting.',
        source_url='https://official.example/changelog/0.4.28', source_type='lmstudio_changelog')
    cards = extract_cards_from_release(row, load_theme_vocabulary(ROOT / '_scripts/themes.yaml'))
    assert {c['theme'] for c in cards} == {'model-support', 'apps-integrations'}
    assert all(c['title'] != heading and c['kind'] != 'launch' for c in cards)
    row['body'] = '### Build 2\n\n- Fixed chat template parsing.\n\n### Build 1\n\n- Fixed the updater.'
    assert extract_cards_from_release(row, load_theme_vocabulary(ROOT / '_scripts/themes.yaml')) == []


def test_krea_generated_video_is_distinct_from_video_input():
    row = collect.normalize_release(product('krea'), release_date='2026-10-31', version=None,
        title='Kling for video', body='## Kling for video\n\nGenerate video with Kling. It supports text, image, and reference to video.',
        source_url='https://official.example/changelog', source_type='krea_changelog')
    themes = load_theme_vocabulary(ROOT / '_scripts/themes.yaml')
    assert extract_cards_from_release(row, themes)[0]['theme'] == 'video-generation'
    row['body'] = '## Video input\n\nAdded video input for analyzing uploaded recordings.'
    assert extract_cards_from_release(row, themes)[0]['theme'] == 'multimodal'
