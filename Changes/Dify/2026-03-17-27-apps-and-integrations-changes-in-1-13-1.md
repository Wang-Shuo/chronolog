---
card_id: dify-2026-03-17-a90d93
date: '2026-03-17'
description: 'Dify · 2026-03-17 · Apps and Integrations: 27 changes in v1.13.1 — Cleared
  stale provider credentials during plugin uninstall to reduce residual credential…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1090
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f37e485d4db2ee042878fdb640c3662178969bb4998b63aefc8132834424a873
product: dify
product_name: Dify
record:
  card_id: dify-2026-03-17-a90d93
  comparison: ''
  date: '2026-03-17'
  description: 'Dify — v1.13.1: 27 Apps and Integrations changes'
  evidence:
  - quote: Cleared stale provider credentials during plugin uninstall to reduce residual
      credential risk.
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: '> [error] failed to initialize database, got error failed to connect to
      `host=db_postgres user=postgres database=dify_plugin`: hostname resolving error
      (lookup db_postgres on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: '> 2025/11/26 11:37:57 init.go:99: [PANIC]failed to init dify plugin db:
      failed to connect to `host=db_postgres user=postgres database=postgres`: hostname
      resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: '> panic: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres
      user=postgres database=postgres`: hostname resolving error (lookup db_postgres
      on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test: add comprehensive unit and integration tests for dataset module
      by @CodingOnStar in https://github.com/langgenius/dify/pull/32187'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test(web): add comprehensive unit and integration tests for plugins and
      tools modules by @CodingOnStar in https://github.com/langgenius/dify/pull/32220'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test: add unit and integration tests for share, develop, and goto-anything
      modules by @CodingOnStar in https://github.com/langgenius/dify/pull/32246'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test: add comprehensive unit and integration tests for RAG Pipeline components
      by @CodingOnStar in https://github.com/langgenius/dify/pull/32237'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'feat(tests): add integration tests for explore app list, installed apps,
      and sidebar lifecycle flows by @CodingOnStar in https://github.com/langgenius/dify/pull/32248'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'feat: support config max size of plugin generated files by @bowenliang123
      in https://github.com/langgenius/dify/pull/30887'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'refactor(web): extract custom hooks from complex components and add comprehensive
      tests by @CodingOnStar in https://github.com/langgenius/dify/pull/32301'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test: Add unit tests for Data Source Integrations (Notion, Website) and
      Modals by @mahammadasim in https://github.com/langgenius/dify/pull/32313'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test: add unit tests for prompt editor''s component picker block plugin.
      by @mahammadasim in https://github.com/langgenius/dify/pull/32412'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test(web): increase coverage for files in folder plugin-page and model-provider-page
      by @akashseth-ifp in https://github.com/langgenius/dify/pull/32377'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test: unit test cases for controllers.files, controllers.mcp and controllers.trigger
      module by @rajatagarwal-oss in https://github.com/langgenius/dify/pull/32057'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test(workflow): add comprehensive hooks unit tests and refactor test infrastructure
      (Part 3) by @CodingOnStar in https://github.com/langgenius/dify/pull/32958'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'chore: add react refresh plugin for vinext by @hyoban in https://github.com/langgenius/dify/pull/32996'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'chore: prevent Storybook crash caused by vite-plugin-inspect by @lyzno1
      in https://github.com/langgenius/dify/pull/33039'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'chore: use react-grab to replace code-inspector-plugin by @hyoban in https://github.com/langgenius/dify/pull/33078'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'chore: bring back code-inspector-plugin and agentation by @hyoban in https://github.com/langgenius/dify/pull/33088'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'feat: enterprise plugin pre uninstall by @wylswz in https://github.com/langgenius/dify/pull/33158'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'feat: source for plugin tasks by @zyssyz123 in https://github.com/langgenius/dify/pull/33244'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test: unit test cases for core.app.apps module by @rajatagarwal-oss in
      https://github.com/langgenius/dify/pull/32482'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test: add UTs for api/ services.plugin by @cryptus-neoxys in https://github.com/langgenius/dify/pull/32588'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test: unit test cases for core.variables, core.plugin, core.prompt module
      by @rajatagarwal-oss in https://github.com/langgenius/dify/pull/32637'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'test: added for core logging and core mcp by @mahammadasim in https://github.com/langgenius/dify/pull/32478'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'chore: update plugin daemon version to 0.5.4-local in Docker compose files
      by @QuantumGhost in https://github.com/langgenius/dify/pull/33526'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 27-apps-and-integrations-changes-in-1-13-1
  source_release: dify-2026-03-17-1-13-1-github-297876307-84187197
  source_type: github_releases
  theme: apps-integrations
  title: 27 Apps and Integrations changes in 1.13.1
  type: change
related_changes:
- '[[Changes/Lovable/2026-03-16-chat-connectors-polar-and-sanity|Chat connectors:
  Polar and Sanity]]'
- '[[Changes/Claude Code/2026-03-17-3-apps-and-integrations-changes-in-v2-1-78|3 Apps
  and Integrations changes in v2.1.78]]'
- '[[Changes/Claude Code/2026-03-17-2-apps-and-integrations-changes-in-v2-1-77|2 Apps
  and Integrations changes in v2.1.77]]'
source_release: '[[Releases/Dify/dify-2026-03-17-1-13-1-github-297876307-84187197|dify-2026-03-17-1-13-1-github-297876307-84187197]]'
source_type: github_releases
theme: apps-integrations
title: 27 Apps and Integrations changes in 1.13.1
type: change
---

<!-- chronolog:begin region="header" -->
# 27 Apps and Integrations changes in 1.13.1

**Dify** · 2026-03-17 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.13.1) · from [[Releases/Dify/dify-2026-03-17-1-13-1-github-297876307-84187197|v1.13.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Cleared stale provider credentials during plugin uninstall to reduce residual credential risk.

> > [error] failed to initialize database, got error failed to connect to `host=db_postgres user=postgres database=dify_plugin`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> > 2025/11/26 11:37:57 init.go:99: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres user=postgres database=postgres`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> > panic: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres user=postgres database=postgres`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> test: add comprehensive unit and integration tests for dataset module by @CodingOnStar in https://github.com/langgenius/dify/pull/32187

> test(web): add comprehensive unit and integration tests for plugins and tools modules by @CodingOnStar in https://github.com/langgenius/dify/pull/32220

> test: add unit and integration tests for share, develop, and goto-anything modules by @CodingOnStar in https://github.com/langgenius/dify/pull/32246

> test: add comprehensive unit and integration tests for RAG Pipeline components by @CodingOnStar in https://github.com/langgenius/dify/pull/32237

> feat(tests): add integration tests for explore app list, installed apps, and sidebar lifecycle flows by @CodingOnStar in https://github.com/langgenius/dify/pull/32248

> feat: support config max size of plugin generated files by @bowenliang123 in https://github.com/langgenius/dify/pull/30887

> refactor(web): extract custom hooks from complex components and add comprehensive tests by @CodingOnStar in https://github.com/langgenius/dify/pull/32301

> test: Add unit tests for Data Source Integrations (Notion, Website) and Modals by @mahammadasim in https://github.com/langgenius/dify/pull/32313

> test: add unit tests for prompt editor's component picker block plugin. by @mahammadasim in https://github.com/langgenius/dify/pull/32412

> test(web): increase coverage for files in folder plugin-page and model-provider-page by @akashseth-ifp in https://github.com/langgenius/dify/pull/32377

> test: unit test cases for controllers.files, controllers.mcp and controllers.trigger module by @rajatagarwal-oss in https://github.com/langgenius/dify/pull/32057

> test(workflow): add comprehensive hooks unit tests and refactor test infrastructure (Part 3) by @CodingOnStar in https://github.com/langgenius/dify/pull/32958

> chore: add react refresh plugin for vinext by @hyoban in https://github.com/langgenius/dify/pull/32996

> chore: prevent Storybook crash caused by vite-plugin-inspect by @lyzno1 in https://github.com/langgenius/dify/pull/33039

> chore: use react-grab to replace code-inspector-plugin by @hyoban in https://github.com/langgenius/dify/pull/33078

> chore: bring back code-inspector-plugin and agentation by @hyoban in https://github.com/langgenius/dify/pull/33088

> feat: enterprise plugin pre uninstall by @wylswz in https://github.com/langgenius/dify/pull/33158

> feat: source for plugin tasks by @zyssyz123 in https://github.com/langgenius/dify/pull/33244

> test: unit test cases for core.app.apps module by @rajatagarwal-oss in https://github.com/langgenius/dify/pull/32482

> test: add UTs for api/ services.plugin by @cryptus-neoxys in https://github.com/langgenius/dify/pull/32588

> test: unit test cases for core.variables, core.plugin, core.prompt module by @rajatagarwal-oss in https://github.com/langgenius/dify/pull/32637

> test: added for core logging and core mcp by @mahammadasim in https://github.com/langgenius/dify/pull/32478

> chore: update plugin daemon version to 0.5.4-local in Docker compose files by @QuantumGhost in https://github.com/langgenius/dify/pull/33526

Source: https://github.com/langgenius/dify/releases/tag/1.13.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-03-17-test-add-comprehensive-unit-and-integration-tests-for-billing-components-by-codi|test: add comprehensive unit and integration tests for billing components]] · Pricing Model
- [[Changes/Dify/2026-03-17-refactor-web-split-share-text-generation-and-add-high-coverage-tests-by-codingon|refactor(web): split share text-generation and add high-coverage tests]] · Collaboration
- [[Changes/Dify/2026-03-17-16-files-and-data-changes-in-1-13-1|16 Files and Data changes in 1.13.1]] · Files and Data
- [[Changes/Dify/2026-03-17-3-safety-and-privacy-changes-in-1-13-1|3 Safety and Privacy changes in 1.13.1]] · Safety and Privacy
- [[Changes/Dify/2026-03-17-5-agent-mode-changes-in-1-13-1|5 Agent Mode changes in 1.13.1]] · Agent Mode
- [[Changes/Dify/2026-03-17-2-reliability-and-performance-changes-in-1-13-1|2 Reliability and Performance changes in 1.13.1]] · Reliability and Performance
- [[Changes/Dify/2026-03-17-ci-add-weekly-schedule-for-pip-and-uv-ecosystems-by-asukaminato0721-in-https-git|ci: Add weekly schedule for pip and uv ecosystems]] · Automation and Scheduling
- [[Changes/Dify/2026-03-17-9-context-window-changes-in-1-13-1|9 Context Window changes in 1.13.1]] · Context Window
- [[Changes/Dify/2026-03-17-18-model-support-changes-in-1-13-1|18 Model Support changes in 1.13.1]] · Model Support
- [[Changes/Dify/2026-03-17-7-interface-experience-changes-in-1-13-1|7 Interface Experience changes in 1.13.1]] · Interface Experience
- [[Changes/Dify/2026-03-17-8-editor-experience-changes-in-1-13-1|8 Editor Experience changes in 1.13.1]] · Editor Experience
- [[Changes/Dify/2026-03-17-4-memory-and-personalization-changes-in-1-13-1|4 Memory and Personalization changes in 1.13.1]] · Memory and Personalization
- [[Changes/Dify/2026-03-17-test-add-integration-tests-for-app-card-operations-list-browsing-and-create-app|test: add integration tests for app card operations, list browsing, and create app flows]] · Search and Browsing
- [[Changes/Dify/2026-03-17-8-developer-workflow-changes-in-1-13-1|8 Developer Workflow changes in 1.13.1]] · Developer Workflow
- [[Changes/Dify/2026-03-17-2-enterprise-and-administration-changes-in-1-13-1|2 Enterprise and Administration changes in 1.13.1]] · Enterprise and Administration
- [[Changes/Dify/2026-03-17-295-other-changes-in-1-13-1|295 other changes in 1.13.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-17 · Claude Code · [[Changes/Claude Code/2026-03-17-2-apps-and-integrations-changes-in-v2-1-77|2 Apps and Integrations changes in v2.1.77]]
- Later: 2026-03-17 · Gemini CLI · [[Changes/Gemini CLI/2026-03-17-4-apps-and-integrations-changes-in-v0-34-0|4 Apps and Integrations changes in v0.34.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-03-17-a90d93&body=Card%3A%20Changes%2FDify%2F2026-03-17-27-apps-and-integrations-changes-in-1-13-1.md%0ACard%20ID%3A%20dify-2026-03-17-a90d93%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.13.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->