---
card_id: dify-2025-12-12-ae6242
date: '2025-12-12'
description: 'Dify · 2025-12-12 · Apps and Integrations: 6 changes in v1.11.1 — **Amplitude
  Integration**: We’ve integrated the Amplitude API key into our layout and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 995
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6fbda24f4cb12fc6b548619e164974cce2d83c5a88e224b3bef37c7091c9624e
product: dify
product_name: Dify
record:
  card_id: dify-2025-12-12-ae6242
  comparison: ''
  date: '2025-12-12'
  description: 'Dify — v1.11.1: 6 Apps and Integrations changes'
  evidence:
  - quote: '**Amplitude Integration**: We’ve integrated the Amplitude API key into
      our layout and provider components for enhanced analytics. Big thanks to @CodingOnStar
      in #29546.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.1
  - quote: '**Container Integration Tests**: Added integration tests for triggers
      to make sure everything runs smoothly in container environments by @Stream29
      in #29527.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.1
  - quote: '> [error] failed to initialize database, got error failed to connect to
      `host=db_postgres user=postgres database=dify_plugin`: hostname resolving error
      (lookup db_postgres on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.1
  - quote: '> 2025/11/26 11:37:57 init.go:99: [PANIC]failed to init dify plugin db:
      failed to connect to `host=db_postgres user=postgres database=postgres`: hostname
      resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.1
  - quote: '> panic: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres
      user=postgres database=postgres`: hostname resolving error (lookup db_postgres
      on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.1
  - quote: 'test(trigger): add container integration tests for trigger by @Stream29
      in https://github.com/langgenius/dify/pull/29527'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 6-apps-and-integrations-changes-in-1-11-1
  source_release: dify-2025-12-12-1-11-1-github-269775785-2add8858
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in 1.11.1
  type: change
related_changes:
- '[[Changes/Windsurf/2025-12-10-cascade-hooks-on-user-prompts|Cascade Hooks on User
  Prompts]]'
- '[[Changes/Cline/2025-12-11-7-apps-and-integrations-changes-in-v3-41-0|7 Apps and
  Integrations changes in v3.41.0]]'
- '[[Changes/Dify/2025-12-11-16-apps-and-integrations-changes-in-1-11-0|16 Apps and
  Integrations changes in 1.11.0]]'
source_release: '[[Releases/Dify/dify-2025-12-12-1-11-1-github-269775785-2add8858|dify-2025-12-12-1-11-1-github-269775785-2add8858]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in 1.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in 1.11.1

**Dify** · 2025-12-12 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.11.1) · from [[Releases/Dify/dify-2025-12-12-1-11-1-github-269775785-2add8858|v1.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Amplitude Integration**: We’ve integrated the Amplitude API key into our layout and provider components for enhanced analytics. Big thanks to @CodingOnStar in #29546.

> **Container Integration Tests**: Added integration tests for triggers to make sure everything runs smoothly in container environments by @Stream29 in #29527.

> > [error] failed to initialize database, got error failed to connect to `host=db_postgres user=postgres database=dify_plugin`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> > 2025/11/26 11:37:57 init.go:99: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres user=postgres database=postgres`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> > panic: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres user=postgres database=postgres`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> test(trigger): add container integration tests for trigger by @Stream29 in https://github.com/langgenius/dify/pull/29527

Source: https://github.com/langgenius/dify/releases/tag/1.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-12-12-3-reliability-and-performance-changes-in-1-11-1|3 Reliability and Performance changes in 1.11.1]] · Reliability and Performance
- [[Changes/Dify/2025-12-12-please-use-the-following-command-instead-for-details-please-read-this-https-gith| Please use the following command instead]] · Developer Workflow
- [[Changes/Dify/2025-12-12-perf-optimize-save-document-with-dataset-id-by-fatelei-in-https-github-com-langg|perf: optimize save_document_with_dataset_id]] · Files and Data
- [[Changes/Dify/2025-12-12-3-safety-and-privacy-changes-in-1-11-1|3 Safety and Privacy changes in 1.11.1]] · Safety and Privacy
- [[Changes/Dify/2025-12-12-25-other-changes-in-1-11-1|25 other changes in 1.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-12-11 · Dify · [[Changes/Dify/2025-12-11-16-apps-and-integrations-changes-in-1-11-0|16 Apps and Integrations changes in 1.11.0]]
- Later: 2025-12-12 · Replit · [[Changes/Replit/2025-12-12-agent-now-supports-custom-mcp-servers|Agent now supports custom MCP servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-12-12-ae6242&body=Card%3A%20Changes%2FDify%2F2025-12-12-6-apps-and-integrations-changes-in-1-11-1.md%0ACard%20ID%3A%20dify-2025-12-12-ae6242%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->