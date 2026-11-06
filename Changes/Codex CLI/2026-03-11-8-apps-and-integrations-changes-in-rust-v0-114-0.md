---
card_id: codex-cli-2026-03-11-f7a1b1
date: '2026-03-11'
description: 'Codex CLI · 2026-03-11 · Apps and Integrations: 8 changes in 0.114.0
  — Added an experimental hooks engine with `SessionStart` and `Stop` hook events.
  (#13276)'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1084
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0b93bab9d7131b48bcb1d6f26a6500a0feb841345078a3d4aeb6f1b3846f6914
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-11-f7a1b1
  comparison: ''
  date: '2026-03-11'
  description: 'Codex CLI — 0.114.0: 8 Apps and Integrations changes'
  evidence:
  - quote: Added an experimental hooks engine with `SessionStart` and `Stop` hook
      events. (#13276)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: 'Improved the `$` mention picker by clearly labeling Skills, Apps, and
      Plugins, and by surfacing plugins first. (#14147, #14163)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: Laid the groundwork for the Python SDK’s generated v2 schema types and
      pinned platform-specific runtime binaries. (#13953)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#14147 make dollar-mention always clarify item category (skill, app, plugin)
      @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#13276 start of hooks engine @eternal-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#14011 [apps] Fix apps enablement condition. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#13953 python-sdk: generated type foundation (all v2 schemas) @shaqayeq-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#13603 Fix release-mode integration test compiler failure @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 8-apps-and-integrations-changes-in-rust-v0-114-0
  source_release: codex-cli-2026-03-11-rust-v0-114-0-github-295424880-aad043c8
  source_type: github_releases
  theme: apps-integrations
  title: 8 Apps and Integrations changes in rust-v0.114.0
  type: change
related_changes:
- '[[Changes/Windsurf/2026-03-09-mcp|MCP]]'
- '[[Changes/Claude Code/2026-03-10-3-apps-and-integrations-changes-in-v2-1-72|3 Apps
  and Integrations changes in v2.1.72]]'
- '[[Changes/Codex CLI/2026-03-10-11-apps-and-integrations-changes-in-rust-v0-113-0|11
  Apps and Integrations changes in rust-v0.113.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-11-rust-v0-114-0-github-295424880-aad043c8|codex-cli-2026-03-11-rust-v0-114-0-github-295424880-aad043c8]]'
source_type: github_releases
theme: apps-integrations
title: 8 Apps and Integrations changes in rust-v0.114.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Apps and Integrations changes in rust-v0.114.0

**Codex CLI** · 2026-03-11 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.114.0) · from [[Releases/Codex CLI/codex-cli-2026-03-11-rust-v0-114-0-github-295424880-aad043c8|0.114.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added an experimental hooks engine with `SessionStart` and `Stop` hook events. (#13276)

> Improved the `$` mention picker by clearly labeling Skills, Apps, and Plugins, and by surfacing plugins first. (#14147, #14163)

> Laid the groundwork for the Python SDK’s generated v2 schema types and pinned platform-specific runtime binaries. (#13953)

> #14147 make dollar-mention always clarify item category (skill, app, plugin) @sayan-oai

> #13276 start of hooks engine @eternal-openai

> #14011 [apps] Fix apps enablement condition. @mzeng-openai

> #13953 python-sdk: generated type foundation (all v2 schemas) @shaqayeq-oai

> #13603 Fix release-mode integration test compiler failure @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.114.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-11-14003-stabilize-split-pty-output-on-windows-aibrahim-oai|♯14003 Stabilize split PTY output on Windows @aibrahim-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-11-3-developer-workflow-changes-in-rust-v0-114-0|3 Developer Workflow changes in rust-v0.114.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-11-2-safety-and-privacy-changes-in-rust-v0-114-0|2 Safety and Privacy changes in rust-v0.114.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-11-14136-fix-core-use-dedicated-types-for-responsesapi-web-search-tool-config-owenl|♯14136 fix(core): use dedicated types for responsesapi web search tool config @owenlin0]] · Search and Browsing
- [[Changes/Codex CLI/2026-03-11-14135-tui-only-show-fast-status-for-gpt-5-4-pash-openai|♯14135 tui: only show fast status for gpt-5.4 @pash-openai]] · Model Support
- [[Changes/Codex CLI/2026-03-11-2-context-window-changes-in-rust-v0-114-0|2 Context Window changes in rust-v0.114.0]] · Context Window
- [[Changes/Codex CLI/2026-03-11-24-other-changes-in-rust-v0-114-0|24 other changes in rust-v0.114.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-10 · Codex CLI · [[Changes/Codex CLI/2026-03-10-11-apps-and-integrations-changes-in-rust-v0-113-0|11 Apps and Integrations changes in rust-v0.113.0]]
- Later: 2026-03-11 · Cursor · [[Changes/Cursor/2026-03-11-we-ve-added-more-than-30-new-plugins-from-partners-such-as-atlassian-datadog-git-901313|New Plugins on the Cursor Marketplace]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-11-f7a1b1&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-11-8-apps-and-integrations-changes-in-rust-v0-114-0.md%0ACard%20ID%3A%20codex-cli-2026-03-11-f7a1b1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.114.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->