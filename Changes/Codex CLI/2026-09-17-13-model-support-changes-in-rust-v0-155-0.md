---
card_id: codex-cli-2026-09-17-81e64b
date: '2026-09-17'
description: 'Codex CLI · 2026-09-17 · Model Support: 13 changes in 0.155.0 — Switching
  accounts now invalidates remote-control sessions, cached WebSocket state, and model…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1347
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3de9d5d74734848cd2af3fa7c426332910f653ae48028b9992fa5da373dfb17f
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-17-81e64b
  comparison: ''
  date: '2026-09-17'
  description: 'Codex CLI — 0.155.0: 13 Model Support changes'
  evidence:
  - quote: 'Switching accounts now invalidates remote-control sessions, cached WebSocket
      state, and model catalogs belonging to the previous identity. (#43906, #44341,
      #44489)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43604 Exclude base instructions from the bundled model catalog @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43795 Pin request reasoning effort while configuration overrides are
      active @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43897 Persist provider and auth identity with model catalog caches @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43906 Scope model catalog caches to the current provider and auth identity
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43921 Show streaming reasoning summaries in the TUI status row @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44243 Use the originating model when recording conversation history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44249 Normalize image detail for the receiving model @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44250 Remove retired model entries while preserving migration prompts
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44276 Avoid duplicate reasoning effort updates during turn recovery @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44277 Surface environment startup failure reasons to the model @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44285 Preserve prewarmed reasoning effort across replay and early rollback
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44392 Add opt-in model discovery for OpenAI API keys @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 13-model-support-changes-in-rust-v0-155-0
  source_release: codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512
  source_type: github_releases
  theme: model-support
  title: 13 Model Support changes in rust-v0.155.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-17-2-model-support-changes-in-v2-1-274|2 Model Support
  changes in v2.1.274]]'
- '[[Changes/Claude Code/2026-09-17-added-a-send-now-key-ctrl-enter-or-ctrl-x-ctrl-s-that-interrupts-the-current-tur|Added
  a send-now key (ctrl+enter, or ctrl+x ctrl+s) that interrupts the current turn…]]'
- '[[Changes/Cline/2026-09-17-13-model-support-changes-in-v4-1-19|13 Model Support
  changes in v4.1.19]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512|codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512]]'
source_type: github_releases
theme: model-support
title: 13 Model Support changes in rust-v0.155.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Model Support changes in rust-v0.155.0

**Codex CLI** · 2026-09-17 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.155.0) · from [[Releases/Codex CLI/codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512|0.155.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Switching accounts now invalidates remote-control sessions, cached WebSocket state, and model catalogs belonging to the previous identity. (#43906, #44341, #44489)

> #43604 Exclude base instructions from the bundled model catalog @copyberry

> #43795 Pin request reasoning effort while configuration overrides are active @copyberry

> #43897 Persist provider and auth identity with model catalog caches @copyberry

> #43906 Scope model catalog caches to the current provider and auth identity @copyberry

> #43921 Show streaming reasoning summaries in the TUI status row @copyberry

> #44243 Use the originating model when recording conversation history @copyberry

> #44249 Normalize image detail for the receiving model @copyberry

> #44250 Remove retired model entries while preserving migration prompts @copyberry

> #44276 Avoid duplicate reasoning effort updates during turn recovery @copyberry

> #44277 Surface environment startup failure reasons to the model @copyberry

> #44285 Preserve prewarmed reasoning effort across replay and early rollback @copyberry

> #44392 Add opt-in model discovery for OpenAI API keys @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.155.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-17-7-safety-and-privacy-changes-in-rust-v0-155-0|7 Safety and Privacy changes in rust-v0.155.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-17-43953-preserve-per-image-generation-ids-in-image-generation-analytics-copyberry|♯43953 Preserve per-image generation IDs in image generation analytics @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-09-17-7-memory-and-personalization-changes-in-rust-v0-155-0|7 Memory and Personalization changes in rust-v0.155.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-17-43846-include-completed-commentary-in-the-copy-picker-copyberry|♯43846 Include completed commentary in the /copy picker @copyberry]] · Interface Experience
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
## Nearby in Model Support

- Earlier: 2026-09-17 · Cline · [[Changes/Cline/2026-09-17-13-model-support-changes-in-v4-1-19|13 Model Support changes in v4.1.19]]
- Later: 2026-09-17 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-17-expanded-reasoning-text-in-the-compact-timeline-is-no-longer-dimmed-so-it-is-as|Expanded reasoning text in the compact timeline is no longer dimmed, so it…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-17-81e64b&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-17-13-model-support-changes-in-rust-v0-155-0.md%0ACard%20ID%3A%20codex-cli-2026-09-17-81e64b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.155.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->