"""Bounded official-page capture. No CAPTCHA handling, cookies or stealth plugins."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import os
from pathlib import Path
import time
from urllib.parse import urlsplit

from _scripts.collect import load_sources, parse_chatgpt_changelog
from _scripts.common import utc_timestamp, write_json
from _scripts.history import read_history
from _scripts.snapshot_bundle import SOURCE, create_bundle, load_bundle


def validate_coverage(releases: list[dict], baseline: set[str]) -> None:
    ids = [r['release_id'] for r in releases]
    if not ids or len(ids) != len(set(ids)):
        raise ValueError('empty or duplicate ChatGPT release identities')
    missing = baseline - set(ids)
    if missing:
        raise ValueError(f'ChatGPT coverage shrank: {len(missing)} archived release IDs missing; '
                         f'first IDs: {", ".join(sorted(missing)[:5])}')


def validate_document(html: str, url: str, product: dict, baseline: set[str]) -> list[dict]:
    actual, expected = urlsplit(url), urlsplit(SOURCE)
    if (actual.scheme, actual.netloc, actual.path.rstrip('/')) != (
            expected.scheme, expected.netloc, expected.path.rstrip('/')):
        raise ValueError('browser left the official release notes URL')
    if len(html.encode()) < 1000 or not html.rstrip().lower().endswith('</html>'):
        raise ValueError('browser document is empty or truncated')
    releases = parse_chatgpt_changelog(product, html, None)
    validate_coverage(releases, baseline)
    return releases


def capture(product: dict, output: Path, baseline: set[str], *, headed: bool = False,
            timeout_seconds: int = 45, channel: str | None = None) -> Path:
    """Create a fresh bundle only after two matching, complete parsed observations.

    Challenge/error pages are retained as failed evidence, never a usable bundle.
    Each invocation uses a new browser context; it does not import user sessions.
    """
    if output.exists():
        raise ValueError('browser evidence output must be a new directory')
    if not 5 <= timeout_seconds <= 120:
        raise ValueError('browser timeout must be between 5 and 120 seconds')
    channel = channel or os.environ.get('CHRONOLOG_BROWSER_CHANNEL') or None
    if channel not in {None, 'chrome', 'msedge'}:
        raise ValueError('browser channel must be chrome or msedge, or unset for bundled Chromium')
    headed = headed or os.environ.get('CHRONOLOG_BROWSER_HEADED') == '1'
    output.mkdir(parents=True)
    report = {'source_url': SOURCE, 'started_at': utc_timestamp(), 'status': 'running',
              'automation': 'playwright-chromium', 'browser_channel': channel or 'bundled-chromium',
              'headless': not headed, 'baseline_releases': len(baseline)}
    html = ''
    try:
        from playwright.sync_api import sync_playwright
        deadline = time.monotonic() + timeout_seconds
        with sync_playwright() as runtime:
            browser = runtime.chromium.launch(headless=not headed, timeout=15000, channel=channel)
            try:
                page = browser.new_page()
                response = page.goto(SOURCE, wait_until='domcontentloaded', timeout=30000)
                report['initial_http_status'] = response.status if response else None
                previous = None
                last_error = 'document has not stabilized'
                while time.monotonic() < deadline:
                    html = page.content()
                    report['final_url'] = page.url
                    try:
                        releases = validate_document(html, page.url, product, baseline)
                        # Ignore unrelated scripts/session state when checking stability.
                        fingerprint = repr(releases)
                        if fingerprint == previous:
                            captured_at = utc_timestamp()
                            raw = output / 'document.html'
                            raw.write_text(html, encoding='utf-8')
                            create_bundle(raw, captured_at, output / 'bundle')
                            raw.unlink()
                            _, meta = load_bundle(output / 'bundle')
                            report.update(status='success', captured_at=captured_at,
                                          release_count=len(releases), sha256=meta['sha256'])
                            return output / 'bundle'
                        previous = fingerprint
                    except ValueError as exc:
                        previous, last_error = None, str(exc)
                    page.wait_for_timeout(2000)
                raise ValueError(f'official browser capture did not become usable: {last_error}')
            finally:
                browser.close()
    except Exception as exc:
        report.update(status='failed', error=f'{type(exc).__name__}: {exc}')
        if html:
            raw = html.encode()
            (output / 'failed-document.html.gz').write_bytes(gzip.compress(raw, mtime=0))
            report['failed_document_sha256'] = hashlib.sha256(raw).hexdigest()
        raise
    finally:
        report['completed_at'] = utc_timestamp()
        write_json(output / 'browser-capture.json', report)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--headed', action='store_true')
    parser.add_argument('--channel', choices=['chrome', 'msedge'], help='Optional installed browser; still uses an isolated context')
    args = parser.parse_args()
    product = next(s for s in load_sources(args.root / '_scripts/sources.yaml') if s['name'] == 'chatgpt')
    baseline = {r['release_id'] for r in read_history(args.root, {'chatgpt'})[0]}
    try:
        bundle = capture(product, args.output, baseline, headed=args.headed, channel=args.channel)
        print(f'Captured official source: {bundle}')
    except Exception as exc:
        parser.exit(1, f'Capture failed: {exc}; evidence: {args.output}\n')


if __name__ == '__main__':
    main()
