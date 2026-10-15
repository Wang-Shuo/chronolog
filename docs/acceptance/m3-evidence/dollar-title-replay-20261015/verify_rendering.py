"""Check a replay against its baseline and inspect literal-dollar HTML/index labels.

Run from the repository root after operations generation, before committing:
  python docs/acceptance/m3-evidence/dollar-title-replay-20261015/verify_rendering.py
"""
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import frontmatter

BASE = '0940c9a8bd832b8a029e0fa6ea0e988cba45921e'
OUT = Path('_pipeline/dollar-title-replay-20261015')
SITE = OUT / 'site'
DIRECTORIES = ['Changes', 'Releases', 'Products', 'Themes', 'Alerts', '_review']

class Labels(HTMLParser):
    def __init__(self):
        super().__init__()
        self.labels = []
        self.active = []
    def handle_starttag(self, tag, attrs):
        if tag in {'a', 'title'}:
            self.active.append([tag, dict(attrs).get('href'), ''])
    def handle_data(self, data):
        for label in self.active:
            label[2] += data
    def handle_endtag(self, tag):
        if self.active and tag == self.active[-1][0]:
            self.labels.append(self.active.pop())

names = subprocess.check_output(['git', 'diff', '--name-only', BASE, '--', *DIRECTORIES, 'index.md'], text=True).splitlines()
assert names, 'No regenerated changes found'
# Reversing the dollar conversion and dropping only the derived machine hash
# must recover each old page semantically, allowing YAML line reflow.
# Source records and all metadata other than title/hash remain byte-value identical.
def normalized(text):
    post = frontmatter.loads(text)
    post.metadata.pop('machine_hash', None)
    if 'title' in post.metadata:
        post.metadata['title'] = post.metadata['title'].replace('USD ', '$')
    return post.metadata, post.content.replace('USD ', '$')
for name in names:
    before = subprocess.check_output(['git', 'show', f'{BASE}:{name}'], text=True)
    assert normalized(before) == normalized(Path(name).read_text()), name

index = json.loads((SITE / 'static/contentIndex.json').read_text())
checks = []
for directory in DIRECTORIES:
    for path in sorted(Path(directory).rglob('*.md')):
        slug = path.with_suffix('').as_posix().replace(' ', '-')
        if slug not in index:
            continue
        text = path.read_text()
        post = frontmatter.loads(text)
        title = post.get('title', '')
        aliases = re.findall(r'\[\[[^\]|]+\|([^\]]*\$[^\]]*)\]\]', text)
        if '$' not in title and not aliases:
            continue
        parser = Labels()
        parser.feed((SITE / (slug + '.html')).read_text())
        if '$' in title:
            assert index[slug]['title'] == title, slug
            assert any(tag == 'title' and label == title for tag, _, label in parser.labels), slug
        for alias in aliases:
            assert any(tag == 'a' and href and label.replace('’', "'") == alias.replace('\\$', '$').replace('’', "'") for tag, href, label in parser.labels), (slug, alias)
        checks.append({'slug': slug, 'title': title, 'dollar_link_labels': aliases})
assert any('$.prompt.media' in item['title'] for item in checks)
assert any('$.ui.view' in item['title'] for item in checks)
assert any(label.count('$') > 1 for item in checks for label in item['dollar_link_labels'])
result = {'status': 'passed', 'baseline_commit': BASE, 'input_kind': 'replay',
          'scope': 'Changed pages differ only by literal-dollar restoration and derived machine_hash; active dollar titles match HTML title and index; dollar wiki aliases render as anchors. Global target checks are in publication.json.',
          'changed_files': names, 'changed_file_count': len(names), 'pages_checked': len(checks),
          'dollar_link_labels_checked': sum(len(item['dollar_link_labels']) for item in checks),
          'content_index_sha256': hashlib.sha256((SITE / 'static/contentIndex.json').read_bytes()).hexdigest(),
          'checks': checks}
(OUT / 'dollar-rendering.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k:v for k,v in result.items() if k not in {'checks','changed_files'}}, ensure_ascii=False, indent=2))
