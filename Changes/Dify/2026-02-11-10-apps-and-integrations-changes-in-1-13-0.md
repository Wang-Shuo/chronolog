---
card_id: dify-2026-02-11-2bcb3a
date: '2026-02-11'
description: 'Dify · 2026-02-11 · Apps and Integrations: 10 changes in 1.13.0 - Human-in-the-Loop
  and Workflow Execution Upgrades — Reduced backend load and console latency…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2616
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d49cee820e98ba0e9372552274f7e2bda138ae3ce987a466851c3877b42351ca
product: dify
product_name: Dify
record:
  card_id: dify-2026-02-11-2bcb3a
  comparison: ''
  date: '2026-02-11'
  description: 'Dify — 1.13.0 - Human-in-the-Loop and Workflow Execution Upgrades:
    10 Apps and Integrations changes'
  evidence:
  - quote: Reduced backend load and console latency with plugin manifest pre-caching
      and `AppListApi` query optimizations.
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.0
  - quote: Enhanced MCP Tool integration by extracting and reporting usage metadata
      (for example, token/cost fields) from MCP responses.
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.0
  - quote: '> [error] failed to initialize database, got error failed to connect to
      `host=db_postgres user=postgres database=dify_plugin`: hostname resolving error
      (lookup db_postgres on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.0
  - quote: '> 2025/11/26 11:37:57 init.go:99: [PANIC]failed to init dify plugin db:
      failed to connect to `host=db_postgres user=postgres database=postgres`: hostname
      resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.0
  - quote: '> panic: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres
      user=postgres database=postgres`: hostname resolving error (lookup db_postgres
      on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.0
  - quote: 'refactor: plugin detail panel components for better maintainability and
      code organization. by @CodingOnStar in https://github.com/langgenius/dify/pull/31870'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.0
  - quote: 'refactor(datasets): extract hooks and components with comprehensive tests
      by @CodingOnStar in https://github.com/langgenius/dify/pull/31707'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.0
  - quote: 'feat: pre-cache all the plugin manifests before checking updates by @Stream29
      in https://github.com/langgenius/dify/pull/31942'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.0
  - quote: 'feat: extract mcp tool usage by @fatelei in https://github.com/langgenius/dify/pull/31802'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.0
  - quote: 'refactor: extract sub-components and custom hooks from UpdateDSLModal
      and Metadata components by @CodingOnStar in https://github.com/langgenius/dify/pull/32045'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 10-apps-and-integrations-changes-in-1-13-0
  source_release: dify-2026-02-11-1-13-0-github-285073967-47691626
  source_type: github_releases
  theme: apps-integrations
  title: 10 Apps and Integrations changes in 1.13.0
  type: change
related_changes:
- '[[Changes/Microsoft 365 Copilot/2026-02-10-query-miro-boards-and-diagrams-with-copilot-connectors-web-microsoft-365-copilot|Query
  Miro boards and diagrams with Copilot connectors…]]'
- '[[Changes/OpenCode/2026-02-10-core-add-directory-parameter-to-plugin-client-for-multi-project-support|Core
  Add directory parameter to plugin client for multi-project support]]'
- '[[Changes/Codex CLI/2026-02-11-13-apps-and-integrations-changes-in-rust-v0-99-0|13
  Apps and Integrations changes in rust-v0.99.0]]'
source_release: '[[Releases/Dify/dify-2026-02-11-1-13-0-github-285073967-47691626|dify-2026-02-11-1-13-0-github-285073967-47691626]]'
source_type: github_releases
theme: apps-integrations
title: 10 Apps and Integrations changes in 1.13.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Apps and Integrations changes in 1.13.0

**Dify** · 2026-02-11 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.13.0) · from [[Releases/Dify/dify-2026-02-11-1-13-0-github-285073967-47691626|1.13.0 - Human-in-the-Loop and Workflow Execution Upgrades]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Reduced backend load and console latency with plugin manifest pre-caching and `AppListApi` query optimizations.

> Enhanced MCP Tool integration by extracting and reporting usage metadata (for example, token/cost fields) from MCP responses.

> > [error] failed to initialize database, got error failed to connect to `host=db_postgres user=postgres database=dify_plugin`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> > 2025/11/26 11:37:57 init.go:99: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres user=postgres database=postgres`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> > panic: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres user=postgres database=postgres`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> refactor: plugin detail panel components for better maintainability and code organization. by @CodingOnStar in https://github.com/langgenius/dify/pull/31870

> refactor(datasets): extract hooks and components with comprehensive tests by @CodingOnStar in https://github.com/langgenius/dify/pull/31707

> feat: pre-cache all the plugin manifests before checking updates by @Stream29 in https://github.com/langgenius/dify/pull/31942

> feat: extract mcp tool usage by @fatelei in https://github.com/langgenius/dify/pull/31802

> refactor: extract sub-components and custom hooks from UpdateDSLModal and Metadata components by @CodingOnStar in https://github.com/langgenius/dify/pull/32045

Source: https://github.com/langgenius/dify/releases/tag/1.13.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-02-11-3-reliability-and-performance-changes-in-1-13-0|3 Reliability and Performance changes in 1.13.0]] · Reliability and Performance
- [[Changes/Dify/2026-02-11-flexible-delivery-methods-human-input-forms-can-be-delivered-via-webapp-or-email|Flexible Delivery Methods: Human input forms can be delivered…]] · Agent Mode
- [[Changes/Dify/2026-02-11-to-support-the-stateful-pause-resume-mechanism-required-by-hitl-and-provide-even|To support the stateful pause/resume mechanism required by HITL and provide…]] · Pricing Model
- [[Changes/Dify/2026-02-11-review-edit-the-node-generates-a-ui-where-humans-can-review-ai-outputs-and-modif|Review & Edit: The node generates a UI where humans can review AI outputs…]] · Editor Experience
- [[Changes/Dify/2026-02-11-please-use-the-following-command-instead-for-details-please-read-this-https-gith| Please use the following command instead]] · Developer Workflow
- [[Changes/Dify/2026-02-11-2-model-support-changes-in-1-13-0|2 Model Support changes in 1.13.0]] · Model Support
- [[Changes/Dify/2026-02-11-2-files-and-data-changes-in-1-13-0|2 Files and Data changes in 1.13.0]] · Files and Data
- [[Changes/Dify/2026-02-11-added-dutch-nl-nl-language-support-across-backend-language-mapping-and-web-local|Added Dutch (nl-NL) language support across backend language mapping and web…]] · Accessibility and Localization
- [[Changes/Dify/2026-02-11-2-safety-and-privacy-changes-in-1-13-0|2 Safety and Privacy changes in 1.13.0]] · Safety and Privacy
- [[Changes/Dify/2026-02-11-97-other-changes-in-1-13-0|97 other changes in 1.13.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-02-11 · Codex CLI · [[Changes/Codex CLI/2026-02-11-13-apps-and-integrations-changes-in-rust-v0-99-0|13 Apps and Integrations changes in rust-v0.99.0]]
- Later: 2026-02-11 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-11-3-apps-and-integrations-changes-in-v0-0-407|3 Apps and Integrations changes in v0.0.407]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-02-11-2bcb3a&body=Card%3A%20Changes%2FDify%2F2026-02-11-10-apps-and-integrations-changes-in-1-13-0.md%0ACard%20ID%3A%20dify-2026-02-11-2bcb3a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.13.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->