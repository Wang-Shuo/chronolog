---
card_id: codex-cli-2026-07-21-0e9d44
date: '2026-07-21'
description: 'Codex CLI · 2026-07-21 · Agent Mode: 20 changes in 0.145.0 — #32749
  Expose model overrides for multi-agent v2 spawns @copyberry'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1111
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 958c7b4f417e7112a32241f2ebea8ed15fb6ef682d28a2f0913ea7c49b7d1a1f
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-21-0e9d44
  comparison: ''
  date: '2026-07-21'
  description: 'Codex CLI — 0.145.0: 20 Agent Mode changes'
  evidence:
  - quote: '#32749 Expose model overrides for multi-agent v2 spawns @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32751 Restrict spawned-agent models to the active backend @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32822 Make explicit multi-agent mode override proactive delegation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32837 Restore V2 agent identities on root thread resume @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32884 Prepare external agent migration for source adapters @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33030 Remove task messages from `list_agents` output @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33076 Add an agent extension runner @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33156 Run detached reviews as review-agent turns @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33367 Respect final-answer boundaries for queued agent mail @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33432 Preserve paginated history for spawned subagents @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33456 Move external agent migration into its crate @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33550 Unify multi-agent settings under `agents` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33572 Expose spawn agent types only when roles are configured @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33657 Restore agent roles when reloading v2 sub-agents @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33841 Make parent-owned sub-agent threads read-only in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33862 Suppress empty multi-agent mode messages @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33883 Report CLI as the external agent config import source @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34234 Avoid redundant TUI subagent metadata requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34383 Mark multi-agent v2 as stable @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34413 Remove CSV-backed agent jobs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 20-agent-mode-changes-in-rust-v0-145-0
  source_release: codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f
  source_type: github_releases
  theme: agent-mode
  title: 20 Agent Mode changes in rust-v0.145.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-07-20-elevenagents|ElevenAgents]]'
- '[[Changes/GitHub Copilot CLI/2026-07-20-3-agent-mode-changes-in-v1-0-72|3 Agent
  Mode changes in v1.0.72]]'
- '[[Changes/Claude Code/2026-07-21-2-agent-mode-changes-in-v2-1-217|2 Agent Mode
  changes in v2.1.217]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f]]'
source_type: github_releases
theme: agent-mode
title: 20 Agent Mode changes in rust-v0.145.0
type: change
---

<!-- chronolog:begin region="header" -->
# 20 Agent Mode changes in rust-v0.145.0

**Codex CLI** · 2026-07-21 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.145.0) · from [[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|0.145.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #32749 Expose model overrides for multi-agent v2 spawns @copyberry

> #32751 Restrict spawned-agent models to the active backend @copyberry

> #32822 Make explicit multi-agent mode override proactive delegation @copyberry

> #32837 Restore V2 agent identities on root thread resume @copyberry

> #32884 Prepare external agent migration for source adapters @copyberry

> #33030 Remove task messages from `list_agents` output @copyberry

> #33076 Add an agent extension runner @copyberry

> #33156 Run detached reviews as review-agent turns @copyberry

> #33367 Respect final-answer boundaries for queued agent mail @copyberry

> #33432 Preserve paginated history for spawned subagents @copyberry

> #33456 Move external agent migration into its crate @copyberry

> #33550 Unify multi-agent settings under `agents` @copyberry

> #33572 Expose spawn agent types only when roles are configured @copyberry

> #33657 Restore agent roles when reloading v2 sub-agents @copyberry

> #33841 Make parent-owned sub-agent threads read-only in the TUI @copyberry

> #33862 Suppress empty multi-agent mode messages @copyberry

> #33883 Report CLI as the external agent config import source @copyberry

> #34234 Avoid redundant TUI subagent metadata requests @copyberry

> #34383 Mark multi-agent v2 as stable @copyberry

> #34413 Remove CSV-backed agent jobs @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.145.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-21-4-collaboration-changes-in-rust-v0-145-0|4 Collaboration changes in rust-v0.145.0]] · Collaboration
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
- [[Changes/Codex CLI/2026-07-21-11-memory-and-personalization-changes-in-rust-v0-145-0|11 Memory and Personalization changes in rust-v0.145.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-21-3-search-and-browsing-changes-in-rust-v0-145-0|3 Search and Browsing changes in rust-v0.145.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-21-9-account-and-access-changes-in-rust-v0-145-0|9 Account and Access changes in rust-v0.145.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-21-44-apps-and-integrations-changes-in-rust-v0-145-0|44 Apps and Integrations changes in rust-v0.145.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-21-18-interface-experience-changes-in-rust-v0-145-0|18 Interface Experience changes in rust-v0.145.0]] · Interface Experience
- [[Changes/Codex CLI/2026-07-21-161-other-changes-in-rust-v0-145-0|161 other changes in rust-v0.145.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-07-21 · Claude Code · [[Changes/Claude Code/2026-07-21-2-agent-mode-changes-in-v2-1-217|2 Agent Mode changes in v2.1.217]]
- Later: 2026-07-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-21-2-agent-mode-changes-in-v1-0-73|2 Agent Mode changes in v1.0.73]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-21-0e9d44&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-21-20-agent-mode-changes-in-rust-v0-145-0.md%0ACard%20ID%3A%20codex-cli-2026-07-21-0e9d44%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.145.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->