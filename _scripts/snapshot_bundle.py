"""Dated official ChatGPT browser snapshot handoff; never infer capture time from mtime."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone, timedelta
import gzip
import hashlib
from pathlib import Path

from _scripts.common import read_json, write_json

SOURCE = 'https://help.openai.com/en/articles/6825453-chatgpt-release-notes'


def timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('capture time must include a timezone')
    return parsed.astimezone(timezone.utc)


def load_bundle(directory: Path, *, now: datetime | None = None, max_age_hours: int = 36) -> tuple[bytes, dict]:
    meta = read_json(directory / 'capture.json')
    if meta.get('source_url') != SOURCE or meta.get('acquisition') != 'browser-snapshot':
        raise ValueError('snapshot must identify the official ChatGPT changelog')
    if max_age_hours <= 0:
        raise ValueError('maximum snapshot age must be positive')
    captured = timestamp(meta['captured_at'])
    age = (now or datetime.now(timezone.utc)) - captured
    if age < timedelta(minutes=-5) or age > timedelta(hours=max_age_hours):
        raise ValueError('snapshot is future-dated or expired; capture the official page again')
    html = gzip.decompress((directory / 'chatgpt.html.gz').read_bytes())
    if hashlib.sha256(html).hexdigest() != meta['sha256']:
        raise ValueError('snapshot digest mismatch')
    if len(html) < 1000:
        raise ValueError('snapshot is empty or truncated')
    return html, meta


def create_bundle(html: Path, captured_at: str, output: Path) -> None:
    timestamp(captured_at)
    if output.exists():
        raise ValueError('output must be a new directory; preserve previous capture evidence')
    body = html.read_bytes()
    output.mkdir(parents=True)
    (output / 'chatgpt.html.gz').write_bytes(gzip.compress(body, mtime=0))
    write_json(output / 'capture.json', {'source_url': SOURCE, 'acquisition': 'browser-snapshot',
        'captured_at': captured_at, 'sha256': hashlib.sha256(body).hexdigest(),
        'note': 'Capture time supplied by the browser operator; not inferred from filesystem metadata.'})
    load_bundle(output)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--html', type=Path, required=True)
    p.add_argument('--captured-at', required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    create_bundle(a.html, a.captured_at, a.output)

if __name__ == '__main__':
    main()
