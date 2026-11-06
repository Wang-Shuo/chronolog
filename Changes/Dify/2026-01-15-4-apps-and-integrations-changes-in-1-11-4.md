---
card_id: dify-2026-01-15-564168
date: '2026-01-15'
description: 'Dify · 2026-01-15 · Apps and Integrations: 4 changes in v1.11.4 — Dify
  now requires Node.js 24.13.0 to pick up the upstream fix for the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1029
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2e4a214aba4fc74a0380fb4c36f886d2a5b9716b84228e49005e27e8084dc078
product: dify
product_name: Dify
record:
  card_id: dify-2026-01-15-564168
  comparison: ''
  date: '2026-01-15'
  description: 'Dify — v1.11.4: 4 Apps and Integrations changes'
  evidence:
  - quote: 'Dify now requires Node.js 24.13.0 to pick up the upstream fix for the
      AsyncLocalStorage/async_hooks DoS CVE that can crash apps with deeply nested
      input. **All self-hosted deployments should upgrade Node.js**. Thanks to @hyoban
      in #30945.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.4
  - quote: '> [error] failed to initialize database, got error failed to connect to
      `host=db_postgres user=postgres database=dify_plugin`: hostname resolving error
      (lookup db_postgres on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.4
  - quote: '> 2025/11/26 11:37:57 init.go:99: [PANIC]failed to init dify plugin db:
      failed to connect to `host=db_postgres user=postgres database=postgres`: hostname
      resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.4
  - quote: '> panic: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres
      user=postgres database=postgres`: hostname resolving error (lookup db_postgres
      on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 4-apps-and-integrations-changes-in-1-11-4
  source_release: dify-2026-01-15-1-11-4-github-276958085-bf7e8274
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in 1.11.4
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-01-14-10-apps-and-integrations-changes-in-rust-v0-81-0|10
  Apps and Integrations changes in rust-v0.81.0]]'
- '[[Changes/Gemini CLI/2026-01-14-9-apps-and-integrations-changes-in-v0-24-0|9 Apps
  and Integrations changes in v0.24.0]]'
- '[[Changes/Codex CLI/2026-01-15-9207-propagate-mcp-disabled-reason-gt-oai|♯9207
  Propagate MCP disabled reason @gt-oai]]'
source_release: '[[Releases/Dify/dify-2026-01-15-1-11-4-github-276958085-bf7e8274|dify-2026-01-15-1-11-4-github-276958085-bf7e8274]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in 1.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in 1.11.4

**Dify** · 2026-01-15 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.11.4) · from [[Releases/Dify/dify-2026-01-15-1-11-4-github-276958085-bf7e8274|v1.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Dify now requires Node.js 24.13.0 to pick up the upstream fix for the AsyncLocalStorage/async_hooks DoS CVE that can crash apps with deeply nested input. **All self-hosted deployments should upgrade Node.js**. Thanks to @hyoban in #30945.

> > [error] failed to initialize database, got error failed to connect to `host=db_postgres user=postgres database=dify_plugin`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> > 2025/11/26 11:37:57 init.go:99: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres user=postgres database=postgres`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> > panic: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres user=postgres database=postgres`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

Source: https://github.com/langgenius/dify/releases/tag/1.11.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-01-15-please-use-the-following-command-instead-for-details-please-read-this-https-gith| Please use the following command instead]] · Developer Workflow
- [[Changes/Dify/2026-01-15-redirect-after-login-we-ve-sorted-out-the-login-redirects-to-bring-you-back-to-y|Redirect After Login]] · Account and Access
- [[Changes/Dify/2026-01-15-20-other-changes-in-1-11-4|20 other changes in 1.11.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-01-15 · Codex CLI · [[Changes/Codex CLI/2026-01-15-9207-propagate-mcp-disabled-reason-gt-oai|♯9207 Propagate MCP disabled reason @gt-oai]]
- Later: 2026-01-16 · Codex CLI · [[Changes/Codex CLI/2026-01-16-accepting-an-mcp-elicitation-now-sends-an-empty-json-payload-instead-of-null-to|Accepting an MCP elicitation now sends an empty JSON payload instead of null…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-01-15-564168&body=Card%3A%20Changes%2FDify%2F2026-01-15-4-apps-and-integrations-changes-in-1-11-4.md%0ACard%20ID%3A%20dify-2026-01-15-564168%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->