---
card_id: codex-cli-2026-03-02-aeee8c
date: '2026-03-02'
description: 'Codex CLI · 2026-03-02 · Memory and Personalization: 6 changes in 0.107.0
  — Memories are now configurable, and there is a new `codex debug clear-memories`…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 956
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2751257c3c8ab1aa30825c8b5fe2a3bb4550d6d500b1002784e8e2d9bdf167fd
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-02-aeee8c
  comparison: ''
  date: '2026-03-02'
  description: 'Codex CLI — 0.107.0: 6 Memory and Personalization changes'
  evidence:
  - quote: 'Memories are now configurable, and there is a new `codex debug clear-memories`
      command to fully reset saved memory state when needed. (#12997, #12999, #13002,
      #13085)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12940 feat: add git info to memories @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12997 feat: add use memories config @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12999 feat: gen memories config @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#13002 feat: use the memory mode for phase 1 extraction @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#13085 feat: add debug clear-memories command to hard-wipe memories state
      @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-memory-and-personalization-changes-in-rust-v0-107-0
  source_release: codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f
  source_type: github_releases
  theme: memory
  title: 6 Memory and Personalization changes in rust-v0.107.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-26-claude-automatically-saves-useful-context-to-auto-memory-manage-with-memory|Claude
  automatically saves useful context to auto-memory]]'
- '[[Changes/Codex CLI/2026-02-26-3-memory-and-personalization-changes-in-rust-v0-106-0|3
  Memory and Personalization changes in rust-v0.106.0]]'
- '[[Changes/Claude Code/2026-02-28-project-configs-auto-memory-now-shared-across-git-worktrees-of-the-same-reposito|Project
  configs & auto memory now shared across git worktrees of the same repository]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f|codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f]]'
source_type: github_releases
theme: memory
title: 6 Memory and Personalization changes in rust-v0.107.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Memory and Personalization changes in rust-v0.107.0

**Codex CLI** · 2026-03-02 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.107.0) · from [[Releases/Codex CLI/codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f|0.107.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Memories are now configurable, and there is a new `codex debug clear-memories` command to fully reset saved memory state when needed. (#12997, #12999, #13002, #13085)

> #12940 feat: add git info to memories @jif-oai

> #12997 feat: add use memories config @jif-oai

> #12999 feat: gen memories config @jif-oai

> #13002 feat: use the memory mode for phase 1 extraction @jif-oai

> #13085 feat: add debug clear-memories command to hard-wipe memories state @sayan-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.107.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-02-2-multimodal-input-changes-in-rust-v0-107-0|2 Multimodal Input changes in rust-v0.107.0]] · Multimodal Input
- [[Changes/Codex CLI/2026-03-02-you-can-now-fork-a-thread-into-sub-agents-making-it-easier-to-branch-work-withou|Fork a thread into sub-agents, making it easier to branch work without leaving…]] · Agent Mode
- [[Changes/Codex CLI/2026-03-02-3-apps-and-integrations-changes-in-rust-v0-107-0|3 Apps and Integrations changes in rust-v0.107.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-02-3-account-and-access-changes-in-rust-v0-107-0|3 Account and Access changes in rust-v0.107.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-02-3-developer-workflow-changes-in-rust-v0-107-0|3 Developer Workflow changes in rust-v0.107.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-02-12947-feat-add-local-date-timezone-to-turn-environment-context-celia-oai|♯12947 feat: add local date/timezone to turn environment context @celia-oai]] · Context Window
- [[Changes/Codex CLI/2026-03-02-2-agent-mode-changes-in-rust-v0-107-0|2 Agent Mode changes in rust-v0.107.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-02-4-model-support-changes-in-rust-v0-107-0|4 Model Support changes in rust-v0.107.0]] · Model Support
- [[Changes/Codex CLI/2026-03-02-3-editor-experience-changes-in-rust-v0-107-0|3 Editor Experience changes in rust-v0.107.0]] · Editor Experience
- [[Changes/Codex CLI/2026-03-02-5-voice-and-audio-changes-in-rust-v0-107-0|5 Voice and Audio changes in rust-v0.107.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-02-8-safety-and-privacy-changes-in-rust-v0-107-0|8 Safety and Privacy changes in rust-v0.107.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-02-24-other-changes-in-rust-v0-107-0|24 other changes in rust-v0.107.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-02-28 · Claude Code · [[Changes/Claude Code/2026-02-28-project-configs-auto-memory-now-shared-across-git-worktrees-of-the-same-reposito|Project configs & auto memory now shared across git worktrees of the same repository]]
- Later: 2026-03-05 · Codex CLI · [[Changes/Codex CLI/2026-03-05-5-memory-and-personalization-changes-in-rust-v0-110-0|5 Memory and Personalization changes in rust-v0.110.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-02-aeee8c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-02-6-memory-and-personalization-changes-in-rust-v0-107-0.md%0ACard%20ID%3A%20codex-cli-2026-03-02-aeee8c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.107.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->