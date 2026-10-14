"""Generate in an isolated Vault, run every gate, then optionally apply a PR candidate.

No command deploys a site or bypasses review. All runs retain quality.json/md,
including failed collection, conflict, regression and build runs.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Callable
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _scripts.collect import collect_live, load_sources, fetch_chatgpt_releases, source_result
from _scripts.common import PipelinePaths, read_json, write_json, utc_timestamp
from _scripts.history import read_history
from _scripts.pipeline import run_pipeline, check_machine_hashes
from _scripts.publication import audit
from _scripts.quality import inventory, changes, markdown
from _scripts.snapshot_bundle import load_bundle, SOURCE
from _scripts.transaction import DIRECTORIES, snapshot, publish, recover, vault_lock
from _scripts.validate import validate_vault_links


class GateFailure(RuntimeError):
    pass


def code_snapshot(root: Path) -> dict:
    paths = [p for directory in ('_scripts', 'tests', '.github') for p in (root / directory).rglob('*')
             if p.is_file() and p.suffix in {'.py', '.json', '.yaml', '.yml', '.ts', '.mjs'}]
    paths += [root / name for name in ('quartz.config.ts', 'quartz.layout.ts', 'pyproject.toml', 'package.json', 'package-lock.json')
              if (root / name).exists()]
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}


def validate_base_url(value: str, production: bool = False) -> str:
    value = value.rstrip('/')
    parsed = urlsplit('https://' + value)
    if not value or '://' in value or parsed.username or parsed.password or parsed.query or parsed.fragment or not parsed.hostname or any(c.isspace() for c in value) or '..' in parsed.path.split('/'):
        raise ValueError('base URL must be host[/path], without scheme, credentials, query or fragment')
    if production and (parsed.hostname in {'localhost', '127.0.0.1', '::1'} or parsed.hostname.endswith(('.invalid', '.example'))):
        raise ValueError('production needs a public deployment host')
    return value


def command(args: list[str], root: Path, out: Path, name: str, report: dict, env: dict | None = None) -> None:
    log = out / f'{name}.log'
    check = report['checks'][name] = {'status': 'running', 'command': args, 'log': log.name}
    try:
        with log.open('w') as handle:
            result = subprocess.run(args, cwd=root, env=env, stdout=handle, stderr=subprocess.STDOUT,
                                    timeout=1200, check=False)
        check.update(status='passed' if result.returncode == 0 else 'failed', exit_code=result.returncode)
        if result.returncode:
            raise GateFailure(f'{name} failed; see {log.name}')
    except subprocess.TimeoutExpired as exc:
        check.update(status='failed', error='timeout after 1200 seconds')
        raise GateFailure(f'{name} timed out') from exc


def validate_site(root: Path, vault: Path, out: Path, report: dict, base_url: str) -> None:
    command([sys.executable, '-m', 'pytest', '-q', '--tb=short'], root, out, 'tests', report)
    products = {s['name'] for s in load_sources(root / '_scripts/sources.yaml')}
    check_machine_hashes(vault)
    releases, cards, pending = read_history(vault, products)
    links = validate_vault_links(vault, releases, cards, pending)
    write_json(out / 'vault-validation.json', links)
    report['checks']['vault'] = {'status': 'failed' if links['errors'] else 'passed', 'report': 'vault-validation.json'}
    report['pending_theme_review'] = len(pending)
    if links['errors']:
        raise GateFailure('Vault links failed')
    env = dict(os.environ, CHRONOLOG_BASE_URL=base_url)
    # Quartz applies ignore globs to ancestor paths too. A candidate stored under
    # ignored _pipeline/ would otherwise silently build zero Markdown files.
    with tempfile.TemporaryDirectory(prefix='chronolog-build-') as temp:
        build_vault = Path(temp) / 'vault'
        build_vault.mkdir()
        for directory in DIRECTORIES:
            if (vault / directory).exists():
                shutil.copytree(vault / directory, build_vault / directory)
        shutil.copy2(vault / 'index.md', build_vault / 'index.md')
        command(['npm', 'run', 'build', '--', '--directory', str(build_vault), '--output', str(out / 'site')],
                root, out, 'build', report, env)
    report['checks']['publication'] = {'status': 'running'}
    try:
        publication = audit(vault, out / 'site', base_url, root)
        write_json(out / 'publication.json', publication)
        report['checks']['publication'] = {'status': 'passed', 'report': 'publication.json'}
    except Exception:
        report['checks']['publication']['status'] = 'failed'
        raise
    identity = {'commit': report.get('commit'), 'run_id': report['run_id'], 'built_at': utc_timestamp(),
                'base_url': base_url, 'kind': 'commit-build' if report['mode'] == 'check' else 'unreviewed-candidate'}
    identity['content_index_sha256'] = hashlib.sha256((out / 'site/static/contentIndex.json').read_bytes()).hexdigest()
    identity['rss_sha256'] = hashlib.sha256((out / 'site/index.xml').read_bytes()).hexdigest()
    write_json(out / 'site/deployment.json', identity)


def collect(root: Path, out: Path, bundle: Path | None) -> dict:
    payload = collect_live(root / '_scripts/sources.yaml', out / 'collection.json', None, 'all')
    failed = next((s for s in payload['sources'] if s['product'] == 'chatgpt' and s['status'] == 'failed'), None)
    if failed and bundle is not None:
        try:
            html, meta = load_bundle(bundle)
            captured = out / 'chatgpt.html'
            captured.write_bytes(html)
            product = next(s for s in load_sources(root / '_scripts/sources.yaml') if s['name'] == 'chatgpt')
            releases = fetch_chatgpt_releases(product, None, captured)
            if not releases:
                raise ValueError('snapshot contains no ChatGPT releases')
            state = source_result('chatgpt', releases, complete=True, coverage='available-endpoint')
            state.update(acquisition='browser-snapshot', acquired_at=meta['captured_at'],
                         snapshot_sha256=meta['sha256'], url=SOURCE, http_error=failed['error'])
            payload['sources'] = [state if s['product'] == 'chatgpt' else s for s in payload['sources']]
            payload['errors'] = [e for e in payload['errors'] if e['product'] != 'chatgpt']
            payload['releases'] = [r for r in payload['releases'] if r['product'] != 'chatgpt'] + releases
            write_json(out / 'snapshot-capture.json', meta)
        except Exception as exc:
            failed['error'] += f'; snapshot fallback rejected: {exc}'
    write_json(out / 'collection.json', payload)
    return payload


def copy_vault(root: Path, candidate: Path) -> None:
    candidate.mkdir()
    shutil.copytree(root / '_scripts', candidate / '_scripts', ignore=shutil.ignore_patterns('__pycache__'))
    for directory in DIRECTORIES:
        if (root / directory).exists():
            shutil.copytree(root / directory, candidate / directory)
    if (root / 'index.md').exists():
        shutil.copy2(root / 'index.md', candidate / 'index.md')


def run(root: Path, run_id: str, out: Path, *, mode: str, base_url: str,
        collection: dict | None = None, snapshot_bundle: Path | None = None, apply: bool = False,
        production: bool = False, gate: Callable = validate_site) -> dict:
    root, out = root.resolve(), out.resolve()
    PipelinePaths(run_id, root)  # validate identity before any filesystem mutation
    if out.exists() or out == root or root.is_relative_to(out):
        raise ValueError('report output must be a new directory and cannot contain the repository')
    if out.is_relative_to(root) and not out.is_relative_to(root / '_pipeline'):
        raise ValueError('in-repository output must be under ignored _pipeline/')
    if mode not in {'generate', 'check'} or (apply and mode != 'generate'):
        raise ValueError('apply is only supported for generation')
    out.mkdir(parents=True)
    report = {'schema_version': 1, 'run_id': run_id, 'mode': mode, 'status': 'running',
        'started_at': utc_timestamp(), 'checks': {}, 'sources': [], 'conflicts': [], 'dlq_count': 0,
        'input_kind': 'replay' if collection is not None else 'live' if mode == 'generate' else 'committed-vault',
        'commit': subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=root, text=True, capture_output=True).stdout.strip() or None}
    candidate = out / 'candidate'
    initial = snapshot(root)
    try:
        report['code_sha256'] = code_snapshot(root)
        report['sources'] = [{'product': s['name'], 'status': 'not-attempted'}
                             for s in load_sources(root / '_scripts/sources.yaml')]
        base_url = validate_base_url(base_url, production)
        report['base_url'] = base_url
        before = inventory(root)
        if mode == 'generate':
            copy_vault(root, candidate)
            payload = collection if collection is not None else collect(root, out, snapshot_bundle)
            report['sources'] = payload.get('sources', [])
            packed = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()
            (out / 'collection.json.gz').write_bytes(gzip.compress(packed, mtime=0))
            report['input_sha256'] = hashlib.sha256(packed).hexdigest()
            manifest = run_pipeline(candidate, run_id, collection=payload, reconcile=True)
            report['pipeline'] = manifest
            report['pending_theme_review'] = manifest['pending_theme_review']
            report['changes'] = changes(before, inventory(candidate))
        else:
            candidate = root
            report['changes'] = changes(before, before)
            report['sources'] = [{'product': p.stem, 'status': 'not-collected',
                **frontmatter_coverage(p)} for p in sorted((root / 'Products').glob('*.md')) if frontmatter_coverage(p)]
        gate(root, candidate, out, report, base_url)
        if snapshot(root) != initial:
            raise GateFailure('source Vault changed during checks; refusing to publish')
        if code_snapshot(root) != report['code_sha256']:
            raise GateFailure('source code changed during checks; rerun on a stable revision')
        report['status'] = 'passed' if mode == 'check' else 'ready' if report['changes']['content_changed'] else 'no-change'
        report['applied_files'] = 0
        if apply and report['status'] == 'ready':
            with vault_lock(root):
                recover(root)
                report['applied_files'] = publish(root, candidate, initial, run_id)
            report['status'] = 'candidate-applied'
    except Exception as exc:
        report.update(status='failed', error=f'{type(exc).__name__}: {exc}')
        if 'conflict' in str(exc).lower():
            report['conflicts'].append(str(exc))
    finally:
        paths = PipelinePaths(run_id, candidate)
        if mode == 'generate' and (paths.run_dir / 'manifest.json').exists():
            report['pipeline'] = read_json(paths.run_dir / 'manifest.json')
            report['sources'] = report['pipeline'].get('sources', report['sources'])
            if paths.dlq.exists():
                report['dlq_count'] = len(read_json(paths.dlq).get('failed', []))
        report['completed_at'] = utc_timestamp()
        write_json(out / 'quality.json', report)
        (out / 'quality.md').write_text(markdown(report))
        evidence = {}
        # The rendered site and staged copies are reproducible outputs, not run evidence.
        for p in sorted(out.rglob('*')):
            if not p.is_file() or p.relative_to(out).parts[0] in {'site', 'candidate'}:
                continue
            evidence[str(p.relative_to(out))] = hashlib.sha256(p.read_bytes()).hexdigest()
        write_json(out / 'evidence-sha256.json', evidence)
    return report


def frontmatter_coverage(path: Path) -> dict:
    import frontmatter
    return frontmatter.load(path).get('coverage', {})


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=ROOT)
    p.add_argument('--run-id', required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--mode', choices=['generate', 'check'], required=True)
    p.add_argument('--collection', type=Path, help='Explicit offline replay; never counted as live acquisition')
    p.add_argument('--snapshot-bundle', type=Path)
    p.add_argument('--base-url', default=os.environ.get('CHRONOLOG_BASE_URL', 'localhost:8080'))
    p.add_argument('--apply', action='store_true')
    p.add_argument('--production', action='store_true')
    a = p.parse_args()
    payload = None
    if a.collection:
        data = a.collection.read_bytes()
        payload = json.loads(gzip.decompress(data) if a.collection.suffix == '.gz' else data)
    report = run(a.root, a.run_id, a.output, mode=a.mode, base_url=a.base_url,
        collection=payload, snapshot_bundle=a.snapshot_bundle, apply=a.apply, production=a.production)
    print(f"{report['status']}: {a.output / 'quality.md'}")
    raise SystemExit(1 if report['status'] == 'failed' else 0)

if __name__ == '__main__':
    main()
