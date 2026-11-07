---
card_id: codex-cli-2026-10-01-3fc61b
date: '2026-10-01'
description: 'Codex CLI · 2026-10-01 · Model Support: 5 changes in 0.160.0 — Explicit
  provider model catalogs no longer include unsupported bundled models or reuse stale…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1361
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0af9ab73b10c436fc4f850b3297cbffa0dbc47b2094834f078b4d9e3d82226df
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-01-3fc61b
  comparison: ''
  date: '2026-10-01'
  description: 'Codex CLI — 0.160.0: 5 Model Support changes'
  evidence:
  - quote: Explicit provider model catalogs no longer include unsupported bundled
      models or reuse stale entries after refresh failures. (#49135)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49135 Treat explicit provider model catalogs as authoritative @andrewgu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49144 Preserve server reasoning summary and verbosity settings in the
      TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49145 Hide reasoning summary settings in `/status` for server connections
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  - quote: '#49171 Fix model provider lookup for TUI history @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.160.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-model-support-changes-in-rust-v0-160-0
  source_release: codex-cli-2026-10-01-rust-v0-160-0-github-401312540-620e0269
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in rust-v0.160.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-30-22-model-support-changes-in-v2026-9-7|22 Model Support
  changes in v2026.9.7]]'
- '[[Changes/OpenCode/2026-09-30-send-namespaced-session-and-parent-session-identity-headers-with-model-requests|Send
  namespaced session and parent-session identity headers with model requests]]'
- '[[Changes/Claude Code/2026-10-01-4-model-support-changes-in-v2-1-287|4 Model Support
  changes in v2.1.287]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-01-rust-v0-160-0-github-401312540-620e0269|codex-cli-2026-10-01-rust-v0-160-0-github-401312540-620e0269]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in rust-v0.160.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in rust-v0.160.0

**Codex CLI** · 2026-10-01 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.160.0) · from [[Releases/Codex CLI/codex-cli-2026-10-01-rust-v0-160-0-github-401312540-620e0269|0.160.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Explicit provider model catalogs no longer include unsupported bundled models or reuse stale entries after refresh failures. (#49135)

> #49135 Treat explicit provider model catalogs as authoritative @andrewgu-oai

> #49144 Preserve server reasoning summary and verbosity settings in the TUI @etraut-openai

> #49145 Hide reasoning summary settings in `/status` for server connections @etraut-openai

> #49171 Fix model provider lookup for TUI history @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.160.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-01-2-interface-experience-changes-in-rust-v0-160-0|2 Interface Experience changes in rust-v0.160.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-01-browse-older-tasks-in-the-agent-command-center-with-a-keyboard-accessible-show-m|Browse older tasks in the agent command center with a keyboard-accessible…]] · Search and Browsing
- [[Changes/Codex CLI/2026-10-01-49130-move-content-filter-guidance-into-the-shared-responses-retry-handler-won-o|♯49130 Move content-filter guidance into the shared Responses retry handler @won-openai]] · Collaboration
- [[Changes/Codex CLI/2026-10-01-49079-update-and-centralize-tui-subscription-labels-etraut-openai|♯49079 Update and centralize TUI subscription labels @etraut-openai]] · Pricing Model
- [[Changes/Codex CLI/2026-10-01-4-apps-and-integrations-changes-in-rust-v0-160-0|4 Apps and Integrations changes in rust-v0.160.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-01-49000-isolate-the-memory-startup-metadata-test-from-git-enrichment-jif-oai|♯49000 Isolate the memory startup metadata test from Git enrichment @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-01-6-agent-mode-changes-in-rust-v0-160-0|6 Agent Mode changes in rust-v0.160.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-01-2-account-and-access-changes-in-rust-v0-160-0|2 Account and Access changes in rust-v0.160.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-01-7-safety-and-privacy-changes-in-rust-v0-160-0|7 Safety and Privacy changes in rust-v0.160.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-01-49082-skip-remote-git-discovery-for-guardian-diff-paths-jif-oai|♯49082 Skip remote Git discovery for Guardian diff paths @jif-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-10-01-49093-simplify-startup-promotions-to-platform-specific-desktop-app-tips-etraut-o|♯49093 Simplify startup promotions to platform-specific desktop app tips @etraut-openai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-01-3-context-window-changes-in-rust-v0-160-0|3 Context Window changes in rust-v0.160.0]] · Context Window
- [[Changes/Codex CLI/2026-10-01-49073-surface-realtime-voice-catalog-failures-in-the-tui-etraut-openai|♯49073 Surface realtime voice catalog failures in the TUI @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-01-2-developer-workflow-changes-in-rust-v0-160-0|2 Developer Workflow changes in rust-v0.160.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-01-29-other-changes-in-rust-v0-160-0|29 other changes in rust-v0.160.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-4-model-support-changes-in-v2-1-287|4 Model Support changes in v2.1.287]]
- Later: 2026-10-01 · Suno · [[Changes/Suno/2026-10-01-meet-the-first-model-to-create-a-speech-and-its-soundtrack-together-in-one-take|Introducing Speech (beta)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-01-3fc61b&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-01-5-model-support-changes-in-rust-v0-160-0.md%0ACard%20ID%3A%20codex-cli-2026-10-01-3fc61b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.160.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->