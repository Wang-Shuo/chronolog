---
card_id: dify-2026-01-13-21ad1a
date: '2026-01-13'
description: 'Dify · 2026-01-13 · Apps and Integrations: 13 changes in v1.11.3 — **MCP
  Tool Enhancements**: Added support for `embeddedResource` and made MCP tools display…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1027
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 52a3b93a8c38921bc01c2f08ec04b74799d6152030df9cc166e9954251198f7d
product: dify
product_name: Dify
record:
  card_id: dify-2026-01-13-21ad1a
  comparison: ''
  date: '2026-01-13'
  description: 'Dify — v1.11.3: 13 Apps and Integrations changes'
  evidence:
  - quote: '**MCP Tool Enhancements**: Added support for `embeddedResource` and made
      MCP tools display directly for quicker access by @IthacaDream and @fatelei in
      #30261 and #30019.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  - quote: '> [error] failed to initialize database, got error failed to connect to
      `host=db_postgres user=postgres database=dify_plugin`: hostname resolving error
      (lookup db_postgres on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  - quote: '> 2025/11/26 11:37:57 init.go:99: [PANIC]failed to init dify plugin db:
      failed to connect to `host=db_postgres user=postgres database=postgres`: hostname
      resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  - quote: '> panic: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres
      user=postgres database=postgres`: hostname resolving error (lookup db_postgres
      on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  - quote: 'feat: add mcp tool display directly by @fatelei in https://github.com/langgenius/dify/pull/30019'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  - quote: 'chore(claude-code): migrate from legacy MCP configuration to official
      plugin system by @lyzno1 in https://github.com/langgenius/dify/pull/30265'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  - quote: 'chore(sdk/nodejs): update deps by @hyoban in https://github.com/langgenius/dify/pull/30291'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  - quote: 'feat: MCP tool adds support for embeddedResource by @IthacaDream in https://github.com/langgenius/dify/pull/30261'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  - quote: 'refactor(web): drop swr and migrate share/chat hooks to tanstack query
      by @lyzno1 in https://github.com/langgenius/dify/pull/30232'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  - quote: 'chore: integrate @tanstack/eslint-plugin-query and fix service layer lint
      errors by @lyzno1 in https://github.com/langgenius/dify/pull/30444'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  - quote: 'feat: add Ralph Wiggum plugin support by @lyzno1 in https://github.com/langgenius/dify/pull/30525'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  - quote: 'chore: rename ralph-wiggum plugin to ralph-loop by @lyzno1 in https://github.com/langgenius/dify/pull/30664'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  - quote: 'feat: implement step two of dataset creation with comprehensive UI components
      and hooks by @CodingOnStar in https://github.com/langgenius/dify/pull/30681'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 13-apps-and-integrations-changes-in-1-11-3
  source_release: dify-2026-01-13-1-11-3-github-276298566-1fe35168
  source_type: github_releases
  theme: apps-integrations
  title: 13 Apps and Integrations changes in 1.11.3
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-01-12-mcp-server|MCP Server]]'
- '[[Changes/ElevenLabs/2026-01-12-sdk-releases|SDK Releases]]'
- '[[Changes/Claude Code/2026-01-13-2-apps-and-integrations-changes-in-v2-1-6|2 Apps
  and Integrations changes in v2.1.6]]'
source_release: '[[Releases/Dify/dify-2026-01-13-1-11-3-github-276298566-1fe35168|dify-2026-01-13-1-11-3-github-276298566-1fe35168]]'
source_type: github_releases
theme: apps-integrations
title: 13 Apps and Integrations changes in 1.11.3
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Apps and Integrations changes in 1.11.3

**Dify** · 2026-01-13 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.11.3) · from [[Releases/Dify/dify-2026-01-13-1-11-3-github-276298566-1fe35168|v1.11.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **MCP Tool Enhancements**: Added support for `embeddedResource` and made MCP tools display directly for quicker access by @IthacaDream and @fatelei in #30261 and #30019.

> > [error] failed to initialize database, got error failed to connect to `host=db_postgres user=postgres database=dify_plugin`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> > 2025/11/26 11:37:57 init.go:99: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres user=postgres database=postgres`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> > panic: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres user=postgres database=postgres`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> feat: add mcp tool display directly by @fatelei in https://github.com/langgenius/dify/pull/30019

> chore(claude-code): migrate from legacy MCP configuration to official plugin system by @lyzno1 in https://github.com/langgenius/dify/pull/30265

> chore(sdk/nodejs): update deps by @hyoban in https://github.com/langgenius/dify/pull/30291

> feat: MCP tool adds support for embeddedResource by @IthacaDream in https://github.com/langgenius/dify/pull/30261

> refactor(web): drop swr and migrate share/chat hooks to tanstack query by @lyzno1 in https://github.com/langgenius/dify/pull/30232

> chore: integrate @tanstack/eslint-plugin-query and fix service layer lint errors by @lyzno1 in https://github.com/langgenius/dify/pull/30444

> feat: add Ralph Wiggum plugin support by @lyzno1 in https://github.com/langgenius/dify/pull/30525

> chore: rename ralph-wiggum plugin to ralph-loop by @lyzno1 in https://github.com/langgenius/dify/pull/30664

> feat: implement step two of dataset creation with comprehensive UI components and hooks by @CodingOnStar in https://github.com/langgenius/dify/pull/30681

Source: https://github.com/langgenius/dify/releases/tag/1.11.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-01-13-4-account-and-access-changes-in-1-11-3|4 Account and Access changes in 1.11.3]] · Account and Access
- [[Changes/Dify/2026-01-13-chore-deps-bump-scheduler-from-0-26-0-to-0-27-0-in-web-by-dependabot-bot-in-http|chore(deps): bump scheduler from 0.26.0 to 0.27.0 in /web…]] · Automation and Scheduling
- [[Changes/Dify/2026-01-13-8-model-support-changes-in-1-11-3|8 Model Support changes in 1.11.3]] · Model Support
- [[Changes/Dify/2026-01-13-5-developer-workflow-changes-in-1-11-3|5 Developer Workflow changes in 1.11.3]] · Developer Workflow
- [[Changes/Dify/2026-01-13-3-agent-mode-changes-in-1-11-3|3 Agent Mode changes in 1.11.3]] · Agent Mode
- [[Changes/Dify/2026-01-13-2-accessibility-and-localization-changes-in-1-11-3|2 Accessibility and Localization changes in 1.11.3]] · Accessibility and Localization
- [[Changes/Dify/2026-01-13-5-safety-and-privacy-changes-in-1-11-3|5 Safety and Privacy changes in 1.11.3]] · Safety and Privacy
- [[Changes/Dify/2026-01-13-4-reliability-and-performance-changes-in-1-11-3|4 Reliability and Performance changes in 1.11.3]] · Reliability and Performance
- [[Changes/Dify/2026-01-13-4-files-and-data-changes-in-1-11-3|4 Files and Data changes in 1.11.3]] · Files and Data
- [[Changes/Dify/2026-01-13-124-other-changes-in-1-11-3|124 other changes in 1.11.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-01-13 · Claude Code · [[Changes/Claude Code/2026-01-13-2-apps-and-integrations-changes-in-v2-1-6|2 Apps and Integrations changes in v2.1.6]]
- Later: 2026-01-14 · Codex CLI · [[Changes/Codex CLI/2026-01-14-10-apps-and-integrations-changes-in-rust-v0-81-0|10 Apps and Integrations changes in rust-v0.81.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-01-13-21ad1a&body=Card%3A%20Changes%2FDify%2F2026-01-13-13-apps-and-integrations-changes-in-1-11-3.md%0ACard%20ID%3A%20dify-2026-01-13-21ad1a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.11.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->