"""Shared delivery preserves resource bytes, URL context and Quartz event flags."""
import json
from pathlib import Path
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize('base,prefix', [('owner.github.io/chronolog', '/chronolog'),
                                       ('localhost:8080', ''), ('owner.example/nested/site/', '/nested/site')])
def test_shared_assets_preserve_behavior_and_bytes(tmp_path, base, prefix):
    bundle = tmp_path / 'resources.cjs'
    subprocess.run(['node', '--input-type=module', '-e', """
import { build } from 'esbuild';
await build({entryPoints: ['_scripts/shared_resources.ts'], bundle: true,
  platform: 'node', format: 'cjs', outfile: process.argv[1]});
""", str(bundle)], cwd=ROOT, check=True, capture_output=True)
    result = subprocess.run(['node', '-e', r"""
const fs = require('node:fs/promises');
const path = require('node:path');
const assert = require('node:assert/strict');
const { shareTransformerResources } = require(process.argv[1]);
const output = process.argv[2], prefix = process.argv[4];
const css = '.mermaid { color: red }\n';
const script = 'document.addEventListener("nav", () => {});\n';
const original = {
  css: [{inline: true, content: css, spaPreserve: true}, {inline: true, content: css},
        {inline: true, content: '.icon { background: url(../icon.svg) }'},
        {inline: true, content: '@import "theme.css";'}, {content: 'https://cdn.example/style.css'}],
  js: [{contentType: 'inline', script, loadTime: 'afterDOMReady', moduleType: 'module', spaPreserve: true},
       {contentType: 'inline', script: 'window.before = 1;', loadTime: 'beforeDOMReady'},
       ...['import.meta.url', 'document.currentScript.src', 'import("./module.js")',
           'import "./side-effect.js";', 'import { value } from "../module.js";'].map(script =>
          ({contentType: 'inline', script, loadTime: 'afterDOMReady'})),
       {contentType: 'external', src: 'https://cdn.example/script.js', loadTime: 'afterDOMReady'}],
  additionalHead: ['custom-head'],
};
const before = JSON.stringify(original);
const plugin = {name: 'Original', textTransform: () => 'unchanged', externalResources: () => original};
const shared = shareTransformerResources(plugin);
const ctx = {argv: {output}, cfg: {configuration: {baseUrl: process.argv[3]}}};
(async () => {
  const resources = shared.transformer.externalResources(ctx);
  assert.equal(shared.transformer.textTransform(), 'unchanged');
  assert.deepEqual(resources.additionalHead, original.additionalHead);
  assert.equal(resources.css[0].inline, false);
  assert.equal(resources.css[0].spaPreserve, true);
  assert.equal(resources.css[0].content, resources.css[1].content);
  assert.deepEqual(resources.css.slice(2), original.css.slice(2));
  assert.deepEqual(resources.js.slice(2), original.js.slice(2));
  assert.deepEqual({...resources.js[0], src: undefined},
    {contentType: 'external', src: undefined, loadTime: 'afterDOMReady', moduleType: 'module', spaPreserve: true});
  assert.equal(resources.js[1].loadTime, 'beforeDOMReady');
  const emitted = [];
  for await (const file of shared.emitter.emit(ctx, [], {})) emitted.push(file);
  assert.equal(emitted.length, 3); // Duplicate CSS has only one emitted file.
  for (const [url, bytes] of [[resources.css[0].content, css], [resources.js[0].src, script],
                             [resources.js[1].src, original.js[1].script]]) {
    assert.ok(url.startsWith(prefix + '/static/shared-'));
    const file = path.join(output, url.slice(prefix.length + 1));
    assert.equal(await fs.readFile(file, 'utf8'), bytes);
  }
  assert.equal(JSON.stringify(original), before);
  const repeat = shared.transformer.externalResources(ctx);
  assert.deepEqual(repeat, resources);
  await fs.rm(output, {recursive: true});
  const partial = [];
  for await (const file of shared.emitter.partialEmit(ctx, [], {}, [])) partial.push(file);
  assert.deepEqual(partial, emitted);
  console.log(JSON.stringify({files: emitted.length, prefix}));
})().catch(error => {console.error(error); process.exit(1)});
""", str(bundle), str(tmp_path / 'site'), base, prefix], cwd=ROOT, check=True,
        capture_output=True, text=True)
    assert json.loads(result.stdout) == {'files': 3, 'prefix': prefix}
