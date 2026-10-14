"""Production publication audit: M2 collection invariants plus RSS and deployment identity."""
from pathlib import Path
import json
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET
import importlib.util


def audit(vault: Path, site: Path, base_url: str, code_root: Path) -> dict:
    spec = importlib.util.spec_from_file_location('chronolog_publication_audit', code_root / 'tests/manual/check_m2_publication.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    report = module.audit(vault, site, base_url)
    index = json.loads((site / 'static/contentIndex.json').read_text())
    prefix = 'https://' + base_url.rstrip('/') + '/'
    rss = ET.parse(site / 'index.xml').getroot()
    items = rss.findall('./channel/item')
    if not items:
        raise ValueError('RSS is missing active content')
    if rss.findtext('./channel/link') != prefix.rstrip('/'):
        raise ValueError('RSS channel does not match deployment base URL')
    seen = set()
    for item in items:
        link = item.findtext('link') or ''
        if not link.startswith(prefix):
            raise ValueError(f'RSS URL outside configured site: {link}')
        slug = unquote(link[len(prefix):]).rstrip('/') or 'index'
        if slug not in index or slug in seen or item.findtext('guid') != link:
            raise ValueError(f'RSS includes duplicate or inactive page: {slug}')
        if not item.findtext('pubDate') or not item.findtext('title'):
            raise ValueError('RSS item missing title/date')
        seen.add(slug)
    sitemap = ET.parse(site / 'sitemap.xml').getroot()
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    for loc in sitemap.findall('s:url/s:loc', ns):
        if not (loc.text or '').startswith(prefix):
            raise ValueError('sitemap URL outside configured site')
    report.update(rss_items=len(items), base_url=base_url, rss_active_only=True)
    return report
