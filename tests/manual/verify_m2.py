"""Reproduce M2 on an isolated copy using committed acquisition evidence."""
import argparse
import gzip
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from _scripts.pipeline import run_pipeline
from _scripts.transaction import copy_pages, snapshot


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    if out.exists() or out.is_relative_to(ROOT):
        parser.error('output must be a new directory outside the repository')
    before = snapshot(ROOT)
    vault = out / 'vault'
    shutil.copytree(ROOT / '_scripts', vault / '_scripts', ignore=shutil.ignore_patterns('__pycache__'))
    copy_pages(ROOT, vault)
    payload = json.loads(gzip.decompress((ROOT / 'docs/acceptance/m2-evidence/collection.json.gz').read_bytes()))
    result = run_pipeline(vault, 'm2-replay', collection=payload, reconcile=True, today='2026-10-13')
    assert snapshot(ROOT) == before
    (out / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k:result[k] for k in ('status','merged_releases','merged_cards','pending_theme_review','changed_files')}))


if __name__ == '__main__':
    main()
