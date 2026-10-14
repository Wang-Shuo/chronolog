"""Audit actual Quartz HTML and the shared search/graph index against the Vault."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit, unquote
import sys
import frontmatter

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from _scripts.history import read_history
from _scripts.validate import validate_vault_links


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.text = []
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            href = dict(attrs).get('href')
            if href:
                self.hrefs.append(href)
    def handle_data(self, value):
        self.text.append(value)


def audit_html(site, base_url=None):
    checked = 0
    errors = []
    base = urlsplit('https://' + base_url) if base_url else urlsplit('http://preview')
    prefix = base.path.rstrip('/')
    for file in site.rglob('*.html'):
        parser = Links()
        parser.feed(file.read_text())
        visible = ''.join(parser.text)
        # Only machine-authored link targets: quoted source code may contain [[ ]].
        if re.search(r'\[\[(?:Changes|Products|Releases|Themes)/', visible):
            errors.append((str(file.relative_to(site)), 'unrendered wiki link'))
        for href in parser.hrefs:
            if href.startswith(('#','mailto:','tel:','data:')):
                continue
            url = urlsplit(urljoin(f'{base.scheme}://{base.netloc}{prefix}/' + file.relative_to(site).as_posix(), href))
            if url.netloc != base.netloc:
                continue
            path = unquote(url.path)
            if prefix and path != prefix and not path.startswith(prefix + '/'):
                errors.append((str(file.relative_to(site)), f'link escapes deployment path: {href}'))
                continue
            target = site / path[len(prefix):].lstrip('/')
            checked += 1
            if not (target.is_file() or target.with_suffix('.html').is_file() or
                    Path(str(target) + '.html').is_file() or (target / 'index.html').is_file()):
                errors.append((str(file.relative_to(site)), href))
    assert not errors, errors[:30]
    return checked


def audit(vault, site, base_url=None):
    index = json.loads((site / 'static/contentIndex.json').read_text())
    active, excluded = {}, []
    for directory in ['Products','Changes','Releases','Themes','Alerts']:
        for path in (vault / directory).rglob('*.md'):
            meta = frontmatter.load(path)
            slug = path.relative_to(vault).with_suffix('').as_posix().replace(' ', '-')
            if meta.get('superseded') or meta.get('source_type') == 'fixture' or meta.get('publication') == 'fixture' or meta.get('product_name') not in (None,'ChatGPT','Claude Code','Cursor') or meta.get('product') not in (None,'chatgpt','claude-code','cursor'):
                excluded.append(slug)
            else:
                active[slug] = meta
    expected = set(active) | {'index'}
    assert set(index) == expected, (set(index)-expected, expected-set(index))
    for slug in excluded:
        assert not (site / (slug + '.html')).exists(), slug
    broken = [(slug,link) for slug,page in index.items() for link in page.get('links', [])
              if link not in expected and not (site / (link.rstrip('/') + '.html')).exists() and not (site / link / 'index.html').exists()]
    assert not broken, broken[:20]
    for slug in expected:
        assert (site / (slug + '.html')).exists(), slug
    html = '\n'.join(p.read_text() for p in site.rglob('*.html'))
    for excluded_slug in excluded:
        assert f'href="/{excluded_slug}"' not in html
    for name in ['Aider','Continue','Tabby','OpenHands']:
        assert not (site / 'Products' / (name+'.html')).exists()
        assert not any(f'/{name}/' in key or key == f'Products/{name}' for key in index)
    changes = {k:v for k,v in active.items() if k.startswith('Changes/')}
    releases = {k:v for k,v in active.items() if k.startswith('Releases/')}
    product_counts = Counter(v['product'] for v in changes.values())
    theme_counts = Counter(v['theme'] for v in changes.values())
    assert f'Change count: {len(changes)}' in index['index']['content']
    for product, count in product_counts.items():
        display = next(v['product_name'] for v in changes.values() if v['product']==product)
        content = index['Products/'+display.replace(' ','-')]['content']
        assert f'{count} tracked changes.' in content
    for theme,count in theme_counts.items():
        assert f'Active changes: {count}.' in index['Themes/'+theme]['content']
    rs,cs,pending = read_history(vault, {'chatgpt','claude-code','cursor'})
    links = validate_vault_links(vault,rs,cs,pending)
    assert not links['errors'], links['errors'][:10]
    html_links = audit_html(site, base_url)
    return {'html_links_checked':html_links,'active_pages':len(expected),'excluded_pages':len(excluded),'active_releases':len(releases),
            'active_changes':len(changes),'products':dict(product_counts),'themes':dict(theme_counts),
            'index_set_matches_vault':True,'broken_graph_edges':broken,'vault_validation':links,
            'html_checked':len(list(site.rglob('*.html'))),
            'scope':'Built HTML + search/contentIndex (also consumed by explorer and graph). No public archive is emitted; local superseded records retain provenance.'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--vault',type=Path,required=True);p.add_argument('--site',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    report=audit(args.vault,args.site)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in {'themes','vault_validation'}}))


if __name__ == '__main__': main()
