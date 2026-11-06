---
card_id: codex-cli-2026-09-17-2d450a
date: '2026-09-17'
description: 'Codex CLI · 2026-09-17 · Memory and Personalization: 7 changes in 0.155.0
  — #43797 Add configurable memory versions with isolated storage @copyberry'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1155
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9dc8f3a68354bda89efc2690fa2dee273757f9c2135c20d24f81ef7968bcf5f5
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-17-2d450a
  comparison: ''
  date: '2026-09-17'
  description: 'Codex CLI — 0.155.0: 7 Memory and Personalization changes'
  evidence:
  - quote: '#43797 Add configurable memory versions with isolated storage @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43799 Prioritize human evidence in memory v2 extraction @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43800 Add summary-only extraction for memory v2 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43808 Move v2 extraction chunking into the memory writer @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43813 Add dedicated memory v2 consolidation and read prompts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43827 Add memory dual writing and v2 readiness reporting @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44298 Set turn triggers for guardian and memory requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-memory-and-personalization-changes-in-rust-v0-155-0
  source_release: codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512
  source_type: github_releases
  theme: memory
  title: 7 Memory and Personalization changes in rust-v0.155.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-09-16-3-memory-and-personalization-changes-in-v1-0-85|3
  Memory and Personalization changes in v1.0.85]]'
- '[[Changes/Claude Code/2026-09-17-vscode-added-viewing-editing-and-deleting-a-saved-memory-inside-the-memory-dialo|VSCode
  Added viewing, editing and deleting a saved memory inside the Memory dialog]]'
- '[[Changes/Claude Code/2026-09-17-vscode-added-memory-and-instructions-entries-to-the-customize-menu-memory-shows|VSCode
  Added Memory and Instructions entries to the Customize menu]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512|codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512]]'
source_type: github_releases
theme: memory
title: 7 Memory and Personalization changes in rust-v0.155.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Memory and Personalization changes in rust-v0.155.0

**Codex CLI** · 2026-09-17 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.155.0) · from [[Releases/Codex CLI/codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512|0.155.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #43797 Add configurable memory versions with isolated storage @copyberry

> #43799 Prioritize human evidence in memory v2 extraction @copyberry

> #43800 Add summary-only extraction for memory v2 @copyberry

> #43808 Move v2 extraction chunking into the memory writer @copyberry

> #43813 Add dedicated memory v2 consolidation and read prompts @copyberry

> #43827 Add memory dual writing and v2 readiness reporting @copyberry

> #44298 Set turn triggers for guardian and memory requests @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.155.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-17-7-safety-and-privacy-changes-in-rust-v0-155-0|7 Safety and Privacy changes in rust-v0.155.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-17-43953-preserve-per-image-generation-ids-in-image-generation-analytics-copyberry|♯43953 Preserve per-image generation IDs in image generation analytics @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-09-17-43846-include-completed-commentary-in-the-copy-picker-copyberry|♯43846 Include completed commentary in the /copy picker @copyberry]] · Interface Experience
- [[Changes/Codex CLI/2026-09-17-13-model-support-changes-in-rust-v0-155-0|13 Model Support changes in rust-v0.155.0]] · Model Support
- [[Changes/Codex CLI/2026-09-17-2-editor-experience-changes-in-rust-v0-155-0|2 Editor Experience changes in rust-v0.155.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-17-15-developer-workflow-changes-in-rust-v0-155-0|15 Developer Workflow changes in rust-v0.155.0]] · Developer Workflow
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
## Nearby in Memory and Personalization

- Earlier: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-vscode-added-memory-and-instructions-entries-to-the-customize-menu-memory-shows|VSCode Added Memory and Instructions entries to the Customize menu]]
- Later: 2026-09-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-21-tear-down-the-processes-an-internal-git-command-started-when-it-times-out-so-a-s|Tear down the processes an internal git command started when it times out, so a slow…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-17-2d450a&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-17-7-memory-and-personalization-changes-in-rust-v0-155-0.md%0ACard%20ID%3A%20codex-cli-2026-09-17-2d450a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.155.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->