---
card_id: dify-2026-10-23-de7ffe
date: '2026-10-23'
description: 'Dify · 2026-10-23 · Reliability and Performance: 2 changes in v1.18.0
  — Smarter Agent Routing, Portable Apps, Deeper Workflow Visibility — **Knowledge…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2895
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 74d892b7f7f019091601e9545011a08d596521dc3bafeac06f297a4f02608df8
product: dify
product_name: Dify
record:
  card_id: dify-2026-10-23-de7ffe
  comparison: ''
  date: '2026-10-23'
  description: 'Dify — v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow
    Visibility: 2 Reliability and Performance changes'
  evidence:
  - quote: '**Knowledge performance:** dataset lists and indexing status use batched
      queries; segment imports avoid repeated position queries; retrieval and result
      post-processing reduce repeated lookups. (#42279, #42191, #42233, #42673, #43665)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Faster loading:** translations load by feature, workflow configuration
      panels load on demand, and chart, music, and SVG previews defer heavier work.
      Chat history no longer loads saved prompts that are not needed for display.
      (#42812, #42873, #42874, #42877, #42970, #42840, #42951, #44521)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 2-reliability-and-performance-changes-in-1-18-0
  source_release: dify-2026-10-23-1-18-0-github-421489030-879b0613
  source_type: github_releases
  theme: reliability-performance
  title: 2 Reliability and Performance changes in 1.18.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-22-restarting-the-same-official-docker-container-no-longer-copies-all-its-saved-sta|Restarting
  the same official Docker container no longer copies all its saved state…]]'
- '[[Changes/Claude Code/2026-10-23-improved-memory-use-of-non-interactive-sessions-p-agent-sdk-during-compaction-wh|Improved
  memory use of non-interactive sessions (-p, Agent SDK) during compaction…]]'
- '[[Changes/Codex CLI/2026-10-23-2-reliability-and-performance-changes-in-rust-v0-164-0|2
  Reliability and Performance changes in rust-v0.164.0]]'
source_release: '[[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|dify-2026-10-23-1-18-0-github-421489030-879b0613]]'
source_type: github_releases
theme: reliability-performance
title: 2 Reliability and Performance changes in 1.18.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Reliability and Performance changes in 1.18.0

**Dify** · 2026-10-23 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.18.0) · from [[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow Visibility]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Knowledge performance:** dataset lists and indexing status use batched queries; segment imports avoid repeated position queries; retrieval and result post-processing reduce repeated lookups. (#42279, #42191, #42233, #42673, #43665)

> **Faster loading:** translations load by feature, workflow configuration panels load on demand, and chart, music, and SVG previews defer heavier work. Chat history no longer loads saved prompts that are not needed for display. (#42812, #42873, #42874, #42877, #42970, #42840, #42951, #44521)

Source: https://github.com/langgenius/dify/releases/tag/1.18.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-10-23-respect-xforward-headers-enabled-standalone-api-default-remains-false-bundled-co| /  RESPECT_XFORWARD_HEADERS_ENABLED  /  Standalone API default remains false]] · Developer Workflow
- [[Changes/Dify/2026-10-23-3-memory-and-personalization-changes-in-1-18-0|3 Memory and Personalization changes in 1.18.0]] · Memory and Personalization
- [[Changes/Dify/2026-10-23-3-accessibility-and-localization-changes-in-1-18-0|3 Accessibility and Localization changes in 1.18.0]] · Accessibility and Localization
- [[Changes/Dify/2026-10-23-3-context-window-changes-in-1-18-0|3 Context Window changes in 1.18.0]] · Context Window
- [[Changes/Dify/2026-10-23-operations-archive-storage-supports-configurable-s3-addressing-style-the-api-ima|Operations: archive storage supports configurable S3 addressing style]] · Model Support
- [[Changes/Dify/2026-10-23-2-interface-experience-changes-in-1-18-0|2 Interface Experience changes in 1.18.0]] · Interface Experience
- [[Changes/Dify/2026-10-23-3-editor-experience-changes-in-1-18-0|3 Editor Experience changes in 1.18.0]] · Editor Experience
- [[Changes/Dify/2026-10-23-32-agent-mode-changes-in-1-18-0|32 Agent Mode changes in 1.18.0]] · Agent Mode
- [[Changes/Dify/2026-10-23-11-safety-and-privacy-changes-in-1-18-0|11 Safety and Privacy changes in 1.18.0]] · Safety and Privacy
- [[Changes/Dify/2026-10-23-14-apps-and-integrations-changes-in-1-18-0|14 Apps and Integrations changes in 1.18.0]] · Apps and Integrations
- [[Changes/Dify/2026-10-23-6-account-and-access-changes-in-1-18-0|6 Account and Access changes in 1.18.0]] · Account and Access
- [[Changes/Dify/2026-10-23-5-collaboration-changes-in-1-18-0|5 Collaboration changes in 1.18.0]] · Collaboration
- [[Changes/Dify/2026-10-23-8-files-and-data-changes-in-1-18-0|8 Files and Data changes in 1.18.0]] · Files and Data
- [[Changes/Dify/2026-10-23-2-automation-and-scheduling-changes-in-1-18-0|2 Automation and Scheduling changes in 1.18.0]] · Automation and Scheduling
- [[Changes/Dify/2026-10-23-81-other-changes-in-1-18-0|81 other changes in 1.18.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-10-23 · Codex CLI · [[Changes/Codex CLI/2026-10-23-2-reliability-and-performance-changes-in-rust-v0-164-0|2 Reliability and Performance changes in rust-v0.164.0]]
- Later: 2026-10-25 · Open WebUI · [[Changes/Open WebUI/2026-10-25-3-reliability-and-performance-changes-in-v0-12-4|3 Reliability and Performance changes in v0.12.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-10-23-de7ffe&body=Card%3A%20Changes%2FDify%2F2026-10-23-2-reliability-and-performance-changes-in-1-18-0.md%0ACard%20ID%3A%20dify-2026-10-23-de7ffe%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.18.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->