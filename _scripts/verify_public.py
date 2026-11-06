"""Verify the public deployment identity, index and RSS after Pages publishes."""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


def verify(base: str, commit: str, fetch) -> dict:
    base=base.rstrip('/')
    identity=json.loads(fetch(base+'/deployment.json'))
    if identity.get('commit')!=commit or identity.get('kind')!='commit-build':
        raise ValueError('public site does not match the reviewed deployment commit')
    raw=fetch(base+'/static/contentIndex.json');rss=fetch(base+'/index.xml')
    if hashlib.sha256(raw).hexdigest()!=identity['content_index_sha256'] or hashlib.sha256(rss).hexdigest()!=identity['rss_sha256']:
        raise ValueError('public files do not match the built deployment manifest')
    index=json.loads(raw)
    if 'index' not in index or any(s.startswith(('_review/','_inputs/','docs/','tests/')) for s in index):
        raise ValueError('public index includes internal content or lacks home')
    declared = identity.get('product_slugs')
    if (not isinstance(declared, list) or not declared
            or any(not isinstance(slug, str) or not slug.startswith('Products/') for slug in declared)
            or len(set(declared)) != len(declared)):
        raise ValueError('deployment manifest is missing a valid product catalog')
    products = {slug for slug in index if slug.startswith('Products/')}
    names = {slug.removeprefix('Products/') for slug in declared}
    if products != set(declared) or any(
            slug.split('/')[1] not in names
            for slug in index if slug.startswith(('Changes/', 'Releases/'))):
        raise ValueError('public index products do not match the deployed catalog')
    items=ET.fromstring(rss).findall('./channel/item')
    if not items:raise ValueError('public RSS is empty')
    for item in items:
        link=item.findtext('link') or ''
        if not link.startswith(base+'/') or (unquote(link[len(base)+1:]).rstrip('/') or 'index') not in index:
            raise ValueError('RSS references inactive content or wrong deployment prefix')
    fetch(base+'/')
    return {'status':'passed','commit':commit,'base_url':base,'active_pages':len(index),
            'rss_items':len(items),'products':sorted(products)}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--url',required=True)
    p.add_argument('--commit',required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    def fetch(url):
        with urlopen(Request(url,headers={'Cache-Control':'no-cache'}),timeout=30) as response:return response.read()
    try:report=verify(a.url,a.commit,fetch)
    except Exception as exc:report={'status':'failed','commit':a.commit,'error':str(exc)}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(report,indent=2)+'\n')
    if report['status']!='passed':raise SystemExit(report['error'])

if __name__=='__main__':main()
