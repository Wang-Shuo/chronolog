---
card_id: codex-cli-2026-07-21-8b9b28
date: '2026-07-21'
description: 'Codex CLI · 2026-07-21 · Reliability and Performance: 3 changes in 0.145.0
  — #32106 Reduce startup latency for ancestor discovery @copyberry'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1314
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3ab7cad55fd2668708b7ef3fb5dd8fb5e89d06b7a3bc28c226766394e1477a03
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-21-8b9b28
  comparison: ''
  date: '2026-07-21'
  description: 'Codex CLI — 0.145.0: 3 Reliability and Performance changes'
  evidence:
  - quote: '#32106 Reduce startup latency for ancestor discovery @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34216 Speed up TUI Markdown layout @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34375 Extend second-based latency histogram buckets @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-reliability-and-performance-changes-in-rust-v0-145-0
  source_release: codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f
  source_type: github_releases
  theme: reliability-performance
  title: 3 Reliability and Performance changes in rust-v0.145.0
  type: change
related_changes:
- '[[Changes/Windsurf/2026-07-17-devin-cloud|Devin Cloud]]'
- '[[Changes/Claude Code/2026-07-18-added-a-periodic-progress-heartbeat-for-long-running-tool-calls-that-previously|Added
  a periodic progress heartbeat for long-running tool calls that previously went…]]'
- '[[Changes/Claude Code/2026-07-21-added-warnings-when-transcript-writes-are-failing-e-g-disk-full-or-when-session|Added
  warnings when transcript writes are failing (e.g. disk full) or when session…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f]]'
source_type: github_releases
theme: reliability-performance
title: 3 Reliability and Performance changes in rust-v0.145.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Reliability and Performance changes in rust-v0.145.0

**Codex CLI** · 2026-07-21 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.145.0) · from [[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|0.145.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #32106 Reduce startup latency for ancestor discovery @copyberry

> #34216 Speed up TUI Markdown layout @copyberry

> #34375 Extend second-based latency histogram buckets @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.145.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-21-4-collaboration-changes-in-rust-v0-145-0|4 Collaboration changes in rust-v0.145.0]] · Collaboration
- [[Changes/Codex CLI/2026-07-21-20-agent-mode-changes-in-rust-v0-145-0|20 Agent Mode changes in rust-v0.145.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-21-12-developer-workflow-changes-in-rust-v0-145-0|12 Developer Workflow changes in rust-v0.145.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-21-7-voice-and-audio-changes-in-rust-v0-145-0|7 Voice and Audio changes in rust-v0.145.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-07-21-12-context-window-changes-in-rust-v0-145-0|12 Context Window changes in rust-v0.145.0]] · Context Window
- [[Changes/Codex CLI/2026-07-21-4-editor-experience-changes-in-rust-v0-145-0|4 Editor Experience changes in rust-v0.145.0]] · Editor Experience
- [[Changes/Codex CLI/2026-07-21-17-safety-and-privacy-changes-in-rust-v0-145-0|17 Safety and Privacy changes in rust-v0.145.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-07-21-3-mobile-and-desktop-changes-in-rust-v0-145-0|3 Mobile and Desktop changes in rust-v0.145.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-21-3-image-generation-changes-in-rust-v0-145-0|3 Image Generation changes in rust-v0.145.0]] · Image Generation
- [[Changes/Codex CLI/2026-07-21-22-model-support-changes-in-rust-v0-145-0|22 Model Support changes in rust-v0.145.0]] · Model Support
- [[Changes/Codex CLI/2026-07-21-33201-branch-conversations-when-editing-earlier-tui-prompts-copyberry|♯33201 Branch conversations when editing earlier TUI prompts @copyberry]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-07-21-33167-document-the-windows-exec-yield-time-range-copyberry|♯33167 Document the Windows exec yield time range @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-07-21-11-memory-and-personalization-changes-in-rust-v0-145-0|11 Memory and Personalization changes in rust-v0.145.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-21-3-search-and-browsing-changes-in-rust-v0-145-0|3 Search and Browsing changes in rust-v0.145.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-21-9-account-and-access-changes-in-rust-v0-145-0|9 Account and Access changes in rust-v0.145.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-21-44-apps-and-integrations-changes-in-rust-v0-145-0|44 Apps and Integrations changes in rust-v0.145.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-21-18-interface-experience-changes-in-rust-v0-145-0|18 Interface Experience changes in rust-v0.145.0]] · Interface Experience
- [[Changes/Codex CLI/2026-07-21-161-other-changes-in-rust-v0-145-0|161 other changes in rust-v0.145.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-07-21 · Claude Code · [[Changes/Claude Code/2026-07-21-added-warnings-when-transcript-writes-are-failing-e-g-disk-full-or-when-session|Added warnings when transcript writes are failing (e.g. disk full) or when session…]]
- Later: 2026-07-29 · Windsurf · [[Changes/Windsurf/2026-07-29-devin-cloud|Devin Cloud]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-21-8b9b28&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-21-3-reliability-and-performance-changes-in-rust-v0-145-0.md%0ACard%20ID%3A%20codex-cli-2026-07-21-8b9b28%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.145.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->