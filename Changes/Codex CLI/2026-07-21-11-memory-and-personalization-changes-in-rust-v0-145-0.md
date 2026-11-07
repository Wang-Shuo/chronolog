---
card_id: codex-cli-2026-07-21-c45468
date: '2026-07-21'
description: 'Codex CLI · 2026-07-21 · Memory and Personalization: 11 changes in 0.145.0
  — Added experimental paginated thread history with efficient resume, search…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1097
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 90d6b647cc3192722f784aa2b1e3387b2eb2aba9b733471ccc5f790539861ae3
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-21-c45468
  comparison: ''
  date: '2026-07-21'
  description: 'Codex CLI — 0.145.0: 11 Memory and Personalization changes'
  evidence:
  - quote: 'Added experimental paginated thread history with efficient resume, search,
      persisted names, sub-agent support, and memories. (#33364, #33907, #34085, #34229,
      #34386)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31362 core: route realtime and memories through HTTP client factory @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31804 Stabilize the memories feature flag @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32193 Validate memory consolidation artifacts before succeeding @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32197 Rebind memory consolidation workspace roots @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32274 Remove the personality migration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32277 Honor `personality = "none"` in model instructions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32744 Log missing personality messages at trace level @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33444 Add external agent memory migration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33683 Preserve scope and provenance for imported agent memory @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34386 Enable memories for paginated threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-memory-and-personalization-changes-in-rust-v0-145-0
  source_release: codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f
  source_type: github_releases
  theme: memory
  title: 11 Memory and Personalization changes in rust-v0.145.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-07-16-refresh-memory-context-after-30-minutes-in-long-lived-sessions|Refresh
  memory context after 30 minutes in long-lived sessions]]'
- '[[Changes/Dify/2026-07-17-perf-memory-batch-load-message-files-in-tokenbuffermemory-to-remove-n-1-queries|perf(memory):
  batch-load message files in TokenBufferMemory to remove N+1 queries]]'
- '[[Changes/Claude Code/2026-07-18-added-an-iso-modified-timestamp-to-memory-file-frontmatter|Added
  an ISO modified timestamp to memory file frontmatter]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f]]'
source_type: github_releases
theme: memory
title: 11 Memory and Personalization changes in rust-v0.145.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Memory and Personalization changes in rust-v0.145.0

**Codex CLI** · 2026-07-21 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.145.0) · from [[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|0.145.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added experimental paginated thread history with efficient resume, search, persisted names, sub-agent support, and memories. (#33364, #33907, #34085, #34229, #34386)

> #31362 core: route realtime and memories through HTTP client factory @bolinfest

> #31804 Stabilize the memories feature flag @jif-oai

> #32193 Validate memory consolidation artifacts before succeeding @copyberry

> #32197 Rebind memory consolidation workspace roots @copyberry

> #32274 Remove the personality migration @copyberry

> #32277 Honor `personality = "none"` in model instructions @copyberry

> #32744 Log missing personality messages at trace level @copyberry

> #33444 Add external agent memory migration @copyberry

> #33683 Preserve scope and provenance for imported agent memory @copyberry

> #34386 Enable memories for paginated threads @copyberry

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
- [[Changes/Codex CLI/2026-07-21-3-reliability-and-performance-changes-in-rust-v0-145-0|3 Reliability and Performance changes in rust-v0.145.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-07-21-33167-document-the-windows-exec-yield-time-range-copyberry|♯33167 Document the Windows exec yield time range @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-07-21-3-search-and-browsing-changes-in-rust-v0-145-0|3 Search and Browsing changes in rust-v0.145.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-21-9-account-and-access-changes-in-rust-v0-145-0|9 Account and Access changes in rust-v0.145.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-21-44-apps-and-integrations-changes-in-rust-v0-145-0|44 Apps and Integrations changes in rust-v0.145.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-21-18-interface-experience-changes-in-rust-v0-145-0|18 Interface Experience changes in rust-v0.145.0]] · Interface Experience
- [[Changes/Codex CLI/2026-07-21-161-other-changes-in-rust-v0-145-0|161 other changes in rust-v0.145.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-07-18 · Claude Code · [[Changes/Claude Code/2026-07-18-added-an-iso-modified-timestamp-to-memory-file-frontmatter|Added an ISO modified timestamp to memory file frontmatter]]
- Later: 2026-07-21 · v0 · [[Changes/v0/2026-07-21-design-systems-personal-scope-imports-save-to-your-own-memory-the-selector-reset|Design systems: personal-scope imports save to your own memory, the selector resets…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-21-c45468&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-21-11-memory-and-personalization-changes-in-rust-v0-145-0.md%0ACard%20ID%3A%20codex-cli-2026-07-21-c45468%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.145.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->