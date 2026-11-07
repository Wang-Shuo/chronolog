---
card_id: codex-cli-2026-07-21-ec9a8c
date: '2026-07-21'
description: 'Codex CLI · 2026-07-21 · Interface Experience: 18 changes in 0.145.0
  — Stabilized the opt-in multi-agent V2 experience with configurable sub-agent models…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2655
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 59dfb25e48898fb34323f3cbf2c0b57d810e951d13b799ca8f83e645febb63bb
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-21-ec9a8c
  comparison: ''
  date: '2026-07-21'
  description: 'Codex CLI — 0.145.0: 18 Interface Experience changes'
  evidence:
  - quote: 'Stabilized the opt-in multi-agent V2 experience with configurable sub-agent
      models, reasoning levels, concurrency, restored roles, and improved agent navigation.
      (#33550, #33631, #33657, #33841, #34383)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: 'Improved terminal responsiveness for long conversations and streamed output
      through incremental Markdown rendering, fewer redraws, caching, and bounded
      command output. (#34045, #34049, #34216, #34223, #34359)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32280 Include terminal errors in turn completion events @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32461 Expand tabs when rendering TUI diffs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32746 Make advanced reasoning selection explicit in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32761 Add shadow metrics for lexical skill selection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32768 Align shadow skill selection with observable sources @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32780 Enable skill search shadow selection by default @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33412 Refactor world-state rendering tests into snapshots @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33605 Add fielded BM25 to shadow skill selection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33613 Add character n-gram skill selection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33614 Add multi-query lexical skill selection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33921 Preserve sub-agent liveness in the agent picker @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33922 Allow selecting path-backed agents in the TUI picker @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34194 Avoid cloning thread data when rendering transcripts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34223 Cache finalized Markdown history rendering @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34224 Avoid cloning file changes in TUI diff rendering @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34366 Avoid cloning hyperlink text during TUI rendering @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 18-interface-experience-changes-in-rust-v0-145-0
  source_release: codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f
  source_type: github_releases
  theme: interface-experience
  title: 18 Interface Experience changes in rust-v0.145.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-07-20-desktop-preserve-command-drafts-in-the-command-menu|Desktop
  Preserve command drafts in the command menu]]'
- '[[Changes/Superwhisper/2026-07-20-you-can-now-transcribe-mov-video-files-directly-from-the-file-picker|Transcribe
  .mov video files directly from the file picker]]'
- '[[Changes/Superwhisper/2026-07-20-2-interface-experience-changes-in-superwhisper-macos-2-16-5|2
  Interface Experience changes in Superwhisper macOS 2.16.5]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f]]'
source_type: github_releases
theme: interface-experience
title: 18 Interface Experience changes in rust-v0.145.0
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Interface Experience changes in rust-v0.145.0

**Codex CLI** · 2026-07-21 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.145.0) · from [[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|0.145.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Stabilized the opt-in multi-agent V2 experience with configurable sub-agent models, reasoning levels, concurrency, restored roles, and improved agent navigation. (#33550, #33631, #33657, #33841, #34383)

> Improved terminal responsiveness for long conversations and streamed output through incremental Markdown rendering, fewer redraws, caching, and bounded command output. (#34045, #34049, #34216, #34223, #34359)

> #32280 Include terminal errors in turn completion events @copyberry

> #32461 Expand tabs when rendering TUI diffs @copyberry

> #32746 Make advanced reasoning selection explicit in the TUI @copyberry

> #32761 Add shadow metrics for lexical skill selection @copyberry

> #32768 Align shadow skill selection with observable sources @copyberry

> #32780 Enable skill search shadow selection by default @copyberry

> #33412 Refactor world-state rendering tests into snapshots @copyberry

> #33605 Add fielded BM25 to shadow skill selection @copyberry

> #33613 Add character n-gram skill selection @copyberry

> #33614 Add multi-query lexical skill selection @copyberry

> #33921 Preserve sub-agent liveness in the agent picker @copyberry

> #33922 Allow selecting path-backed agents in the TUI picker @copyberry

> #34194 Avoid cloning thread data when rendering transcripts @copyberry

> #34223 Cache finalized Markdown history rendering @copyberry

> #34224 Avoid cloning file changes in TUI diff rendering @copyberry

> #34366 Avoid cloning hyperlink text during TUI rendering @copyberry

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
- [[Changes/Codex CLI/2026-07-21-11-memory-and-personalization-changes-in-rust-v0-145-0|11 Memory and Personalization changes in rust-v0.145.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-21-3-search-and-browsing-changes-in-rust-v0-145-0|3 Search and Browsing changes in rust-v0.145.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-21-9-account-and-access-changes-in-rust-v0-145-0|9 Account and Access changes in rust-v0.145.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-21-44-apps-and-integrations-changes-in-rust-v0-145-0|44 Apps and Integrations changes in rust-v0.145.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-21-161-other-changes-in-rust-v0-145-0|161 other changes in rust-v0.145.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-07-20 · Superwhisper · [[Changes/Superwhisper/2026-07-20-2-interface-experience-changes-in-superwhisper-macos-2-16-5|2 Interface Experience changes in Superwhisper macOS 2.16.5]]
- Later: 2026-07-21 · Lovable · [[Changes/Lovable/2026-07-21-invite-people-outside-your-workspace-to-an-internally-published-app|Invite people outside your workspace to an internally published app]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-21-ec9a8c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-21-18-interface-experience-changes-in-rust-v0-145-0.md%0ACard%20ID%3A%20codex-cli-2026-07-21-ec9a8c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.145.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->