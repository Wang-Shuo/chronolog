from copy import deepcopy
import gzip
import sys
from types import SimpleNamespace

import pytest

from _scripts import browser_capture, operations
from _scripts.collect import source_result
from _scripts.common import read_json
from _scripts.snapshot_bundle import SOURCE, create_bundle, load_bundle


PRODUCT = {'name': 'chatgpt', 'display_name': 'ChatGPT', 'url': SOURCE}
HTML = ('<!DOCTYPE html><html><body><article><h1>ChatGPT — Release Notes</h1>'
        '<h1>October 30, 2026</h1><h2>Agent tools</h2><p>Agent can use new tools.</p>'
        '</article>' + '<!-- padding -->' * 100 + '</body></html>')


def test_browser_requires_official_complete_document_and_full_history():
    releases = browser_capture.validate_document(HTML, SOURCE, PRODUCT, set())
    assert releases
    ids = {r['release_id'] for r in releases}
    assert browser_capture.validate_document(HTML, SOURCE, PRODUCT, ids) == releases
    for html, url, baseline in [(HTML, 'https://example.com', set()),
                                (HTML[:-8], SOURCE, set()),
                                ('<html>Just a moment</html>', SOURCE, set()),
                                (HTML, SOURCE, ids | {'missing-historical-release'})]:
        with pytest.raises(ValueError):
            browser_capture.validate_document(html, url, PRODUCT, baseline)


def install_browser(monkeypatch, html=HTML, url=SOURCE):
    class Page:
        def goto(self, *a, **kw): return SimpleNamespace(status=200)
        def content(self): return html
        def wait_for_timeout(self, ms): pass
    page = Page()
    page.url = url
    browser = SimpleNamespace(new_page=lambda: page, close=lambda: None)
    class Runtime:
        def __enter__(self): return SimpleNamespace(chromium=SimpleNamespace(launch=lambda **kw: browser))
        def __exit__(self, *a): pass
    monkeypatch.setitem(sys.modules, 'playwright.sync_api', SimpleNamespace(sync_playwright=Runtime))
    return page


@pytest.mark.parametrize('headed', [False, True])
def test_browser_bundle_has_actual_capture_time_digest_and_evidence(tmp_path, monkeypatch, headed):
    install_browser(monkeypatch)
    if headed:
        monkeypatch.setenv('CHRONOLOG_BROWSER_HEADED', '1')
    else:
        monkeypatch.delenv('CHRONOLOG_BROWSER_HEADED', raising=False)
    out = tmp_path / 'browser'
    bundle = browser_capture.capture(PRODUCT, out, set())
    raw, meta = load_bundle(bundle)
    assert raw == HTML.encode()
    report = read_json(out / 'browser-capture.json')
    assert report['status'] == 'success'
    assert report['headless'] is not headed
    assert meta['captured_at'] == report['captured_at']
    assert meta['sha256'] == report['sha256']


def test_challenge_is_failed_evidence_never_a_bundle(tmp_path, monkeypatch):
    install_browser(monkeypatch, html='<html>Just a moment</html>')
    ticks = iter([0, 1, 100])
    monkeypatch.setattr(browser_capture.time, 'monotonic', lambda: next(ticks))
    out = tmp_path / 'browser'
    with pytest.raises(ValueError, match='did not become usable'):
        browser_capture.capture(PRODUCT, out, set())
    assert read_json(out / 'browser-capture.json')['status'] == 'failed'
    assert not (out / 'bundle').exists()
    assert b'Just a moment' in gzip.decompress((out / 'failed-document.html.gz').read_bytes())


def test_operations_uses_fresh_browser_bundle_without_repository_input(tmp_path, monkeypatch):
    from _scripts.common import utc_timestamp
    html = tmp_path / 'page.html'; html.write_text(HTML)
    bundle = tmp_path / 'fresh'
    create_bundle(html, utc_timestamp(), bundle)
    failure = source_result('chatgpt', [], complete=False, coverage='available-endpoint', error='HTTP 403')
    payload = {'sources': [failure], 'errors': [{'product': 'chatgpt', 'error': 'HTTP 403'}], 'releases': []}
    monkeypatch.setattr(operations, 'collect_live', lambda *a: deepcopy(payload))
    monkeypatch.setattr(operations, 'read_history', lambda *a: ([], [], []))
    monkeypatch.setattr(operations, 'load_sources', lambda *a: [PRODUCT])
    monkeypatch.setattr(operations, 'capture_browser', lambda *a: bundle)
    result = operations.collect(tmp_path, tmp_path, None, browser_fallback=True)
    assert result['sources'][0]['status'] == 'success'
    assert result['sources'][0]['http_error'] == 'HTTP 403'
    assert result['sources'][0]['acquisition'] == 'browser-snapshot'
    assert not result['errors']
    def unavailable(*a): raise RuntimeError('browser unavailable')
    monkeypatch.setattr(operations, 'capture_browser', unavailable)
    result = operations.collect(tmp_path, tmp_path, None, browser_fallback=True)
    assert result['sources'][0]['status'] == 'failed'
    assert result['errors'][0]['error'] == result['sources'][0]['error']
    assert 'HTTP 403' in result['errors'][0]['error']
    assert 'browser unavailable' in result['errors'][0]['error']


def test_truncated_http_capture_cannot_reconcile_history(tmp_path, monkeypatch):
    releases = browser_capture.validate_document(HTML, SOURCE, PRODUCT, set())
    state = source_result('chatgpt', releases, complete=True, coverage='available-endpoint')
    monkeypatch.setattr(operations, 'collect_live', lambda *a: {'sources': [state], 'errors': [], 'releases': releases})
    monkeypatch.setattr(operations, 'read_history', lambda *a: ([{'release_id': 'missing'}], [], []))
    result = operations.collect(tmp_path, tmp_path, None)
    assert not result['releases']
    assert result['sources'][0]['complete'] is False
    assert result['sources'][0]['status'] == 'failed'
    assert 'coverage shrank' in result['errors'][0]['error']
