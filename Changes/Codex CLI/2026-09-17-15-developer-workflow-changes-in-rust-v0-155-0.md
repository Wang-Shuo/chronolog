---
card_id: codex-cli-2026-09-17-a49a25
date: '2026-09-17'
description: 'Codex CLI · 2026-09-17 · Developer Workflow: 15 changes in 0.155.0 —
  Added task hiding, archiving, and deletion in the agents overview, plus worktree
  ownership…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2928
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f408a7dd58f83d1e8a3eaa584778a09d770245d5a793d028c3da34016d5079f8
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-17-a49a25
  comparison: ''
  date: '2026-09-17'
  description: 'Codex CLI — 0.155.0: 15 Developer Workflow changes'
  evidence:
  - quote: 'Added task hiding, archiving, and deletion in the agents overview, plus
      worktree ownership details and confirmed deletion of clean managed worktrees.
      (#43942, #44424, #44433)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: 'Blocked Windows-process escapes from restricted WSL sandboxes and hardened
      brokered shell snapshots against credential exposure. (#44286, #43909, #44040)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43562 Add an explicit app-server daemon update command @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43621 Add worktree classification to thread telemetry @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43876 Detach Unix hook commands from the controlling terminal @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43907 Preserve complete shell snapshot exports through filtering and
      replay @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43909 Protect shell snapshots when credential brokerage is enabled @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43937 Tag TUI startup metrics with terminal and multiplexer categories
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43942 Show worktree owner details and add confirmed deletion @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43954 Cache protected shell snapshots and harden capture cleanup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44038 Handle copied credentials in the broker and shell snapshots @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44040 Harden credential handling in shell snapshots and replay @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44072 Support configured credential providers across shell snapshots
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44286 Block WSL interop escapes from restricted filesystem sandboxes
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44297 Isolate the hook pipe I/O timeout test from shell startup files
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 15-developer-workflow-changes-in-rust-v0-155-0
  source_release: codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512
  source_type: github_releases
  theme: developer-workflow
  title: 15 Developer Workflow changes in rust-v0.155.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-17-7-developer-workflow-changes-in-v2-1-274|7 Developer
  Workflow changes in v2.1.274]]'
- '[[Changes/Claude Code/2026-09-17-2-developer-workflow-changes-in-v2-1-275|2 Developer
  Workflow changes in v2.1.275]]'
- '[[Changes/Cline/2026-09-17-2-developer-workflow-changes-in-v4-1-19|2 Developer
  Workflow changes in v4.1.19]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512|codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512]]'
source_type: github_releases
theme: developer-workflow
title: 15 Developer Workflow changes in rust-v0.155.0
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Developer Workflow changes in rust-v0.155.0

**Codex CLI** · 2026-09-17 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.155.0) · from [[Releases/Codex CLI/codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512|0.155.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added task hiding, archiving, and deletion in the agents overview, plus worktree ownership details and confirmed deletion of clean managed worktrees. (#43942, #44424, #44433)

> Blocked Windows-process escapes from restricted WSL sandboxes and hardened brokered shell snapshots against credential exposure. (#44286, #43909, #44040)

> #43562 Add an explicit app-server daemon update command @copyberry

> #43621 Add worktree classification to thread telemetry @copyberry

> #43876 Detach Unix hook commands from the controlling terminal @copyberry

> #43907 Preserve complete shell snapshot exports through filtering and replay @copyberry

> #43909 Protect shell snapshots when credential brokerage is enabled @copyberry

> #43937 Tag TUI startup metrics with terminal and multiplexer categories @copyberry

> #43942 Show worktree owner details and add confirmed deletion @copyberry

> #43954 Cache protected shell snapshots and harden capture cleanup @copyberry

> #44038 Handle copied credentials in the broker and shell snapshots @copyberry

> #44040 Harden credential handling in shell snapshots and replay @copyberry

> #44072 Support configured credential providers across shell snapshots @copyberry

> #44286 Block WSL interop escapes from restricted filesystem sandboxes @copyberry

> #44297 Isolate the hook pipe I/O timeout test from shell startup files @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.155.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-17-7-safety-and-privacy-changes-in-rust-v0-155-0|7 Safety and Privacy changes in rust-v0.155.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-17-43953-preserve-per-image-generation-ids-in-image-generation-analytics-copyberry|♯43953 Preserve per-image generation IDs in image generation analytics @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-09-17-7-memory-and-personalization-changes-in-rust-v0-155-0|7 Memory and Personalization changes in rust-v0.155.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-17-43846-include-completed-commentary-in-the-copy-picker-copyberry|♯43846 Include completed commentary in the /copy picker @copyberry]] · Interface Experience
- [[Changes/Codex CLI/2026-09-17-13-model-support-changes-in-rust-v0-155-0|13 Model Support changes in rust-v0.155.0]] · Model Support
- [[Changes/Codex CLI/2026-09-17-2-editor-experience-changes-in-rust-v0-155-0|2 Editor Experience changes in rust-v0.155.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-17-20-voice-and-audio-changes-in-rust-v0-155-0|20 Voice and Audio changes in rust-v0.155.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-17-2-mobile-and-desktop-changes-in-rust-v0-155-0|2 Mobile and Desktop changes in rust-v0.155.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-17-20-context-window-changes-in-rust-v0-155-0|20 Context Window changes in rust-v0.155.0]] · Context Window
- [[Changes/Codex CLI/2026-09-17-44354-extract-shared-footer-hint-wrapping-in-the-tui-copyberry|♯44354 Extract shared footer hint wrapping in the TUI @copyberry]] · Collaboration
- [[Changes/Codex CLI/2026-09-17-9-agent-mode-changes-in-rust-v0-155-0|9 Agent Mode changes in rust-v0.155.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-17-6-account-and-access-changes-in-rust-v0-155-0|6 Account and Access changes in rust-v0.155.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-17-24-apps-and-integrations-changes-in-rust-v0-155-0|24 Apps and Integrations changes in rust-v0.155.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-17-96-other-changes-in-rust-v0-155-0|96 other changes in rust-v0.155.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-17 · Cline · [[Changes/Cline/2026-09-17-2-developer-workflow-changes-in-v4-1-19|2 Developer Workflow changes in v4.1.19]]
- Later: 2026-09-17 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-17-the-status-row-now-says-it-is-waiting-for-background-shells-instead-of-working-w|The status row now says it is waiting for background shells, instead…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-17-a49a25&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-17-15-developer-workflow-changes-in-rust-v0-155-0.md%0ACard%20ID%3A%20codex-cli-2026-09-17-a49a25%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.155.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->