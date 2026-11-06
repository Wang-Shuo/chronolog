---
card_id: codex-cli-2026-09-28-36b6fc
date: '2026-09-28'
description: 'Codex CLI · 2026-09-28 · Memory and Personalization: 3 changes in 0.158.0
  — #47817 Stabilize thread resume and memory dual-write tests @jif-oai'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1166
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2799e9c20eea6a1d9ed0e2e8c3b62fe6eba5ed06e47e7c257ee399a3f14ebd63
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-28-36b6fc
  comparison: ''
  date: '2026-09-28'
  description: 'Codex CLI — 0.158.0: 3 Memory and Personalization changes'
  evidence:
  - quote: '#47817 Stabilize thread resume and memory dual-write tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47946 Add an in-memory agent message board for ephemeral sessions @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47952 Prune expired in-memory message board registry entries @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-memory-and-personalization-changes-in-rust-v0-158-0
  source_release: codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7
  source_type: github_releases
  theme: memory
  title: 3 Memory and Personalization changes in rust-v0.158.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-09-22-resuming-large-local-sessions-keeps-transcript-memory-bounded-for-smoother-cli-p|Resuming
  large local sessions keeps transcript memory bounded for smoother CLI performance]]'
- '[[Changes/Claude Code/2026-09-25-improved-lists-in-help-hooks-copy-chrome-memory-ide-release-notes-rewind-diff-re|Improved
  lists in /help, /hooks, /copy, /chrome, /memory, /ide…]]'
- '[[Changes/Claude Code/2026-09-28-improved-auto-memory-loading-invisible-characters-and-tags-that-imitate-claude-c|Improved
  auto-memory loading]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7]]'
source_type: github_releases
theme: memory
title: 3 Memory and Personalization changes in rust-v0.158.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Memory and Personalization changes in rust-v0.158.0

**Codex CLI** · 2026-09-28 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.158.0) · from [[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|0.158.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #47817 Stabilize thread resume and memory dual-write tests @jif-oai

> #47946 Add an in-memory agent message board for ephemeral sessions @jif-oai

> #47952 Prune expired in-memory message board registry entries @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.158.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-28-9-safety-and-privacy-changes-in-rust-v0-158-0|9 Safety and Privacy changes in rust-v0.158.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-28-47975-prevent-stale-voice-answers-from-reappearing-during-speech-recovery-etraut|♯47975 Prevent stale voice answers from reappearing during speech recovery @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-28-13-apps-and-integrations-changes-in-rust-v0-158-0|13 Apps and Integrations changes in rust-v0.158.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-28-8-account-and-access-changes-in-rust-v0-158-0|8 Account and Access changes in rust-v0.158.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-28-3-mobile-and-desktop-changes-in-rust-v0-158-0|3 Mobile and Desktop changes in rust-v0.158.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-28-2-collaboration-changes-in-rust-v0-158-0|2 Collaboration changes in rust-v0.158.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-28-7-model-support-changes-in-rust-v0-158-0|7 Model Support changes in rust-v0.158.0]] · Model Support
- [[Changes/Codex CLI/2026-09-28-3-image-generation-changes-in-rust-v0-158-0|3 Image Generation changes in rust-v0.158.0]] · Image Generation
- [[Changes/Codex CLI/2026-09-28-4-editor-experience-changes-in-rust-v0-158-0|4 Editor Experience changes in rust-v0.158.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-28-6-interface-experience-changes-in-rust-v0-158-0|6 Interface Experience changes in rust-v0.158.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-28-47984-add-multi-agent-spawn-latency-and-failure-metrics-owenlin0|♯47984 Add multi-agent spawn latency and failure metrics @owenlin0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-28-14-developer-workflow-changes-in-rust-v0-158-0|14 Developer Workflow changes in rust-v0.158.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-28-11-agent-mode-changes-in-rust-v0-158-0|11 Agent Mode changes in rust-v0.158.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-28-17-context-window-changes-in-rust-v0-158-0|17 Context Window changes in rust-v0.158.0]] · Context Window
- [[Changes/Codex CLI/2026-09-28-96-other-changes-in-rust-v0-158-0|96 other changes in rust-v0.158.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-09-28 · Claude Code · [[Changes/Claude Code/2026-09-28-improved-auto-memory-loading-invisible-characters-and-tags-that-imitate-claude-c|Improved auto-memory loading]]
- Later: 2026-09-28 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-28-add-support-for-claude-code-rule-files-in-claude-rules-as-custom-instructions|Add support for Claude Code rule files in .claude/rules as custom instructions]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-28-36b6fc&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-28-3-memory-and-personalization-changes-in-rust-v0-158-0.md%0ACard%20ID%3A%20codex-cli-2026-09-28-36b6fc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.158.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->