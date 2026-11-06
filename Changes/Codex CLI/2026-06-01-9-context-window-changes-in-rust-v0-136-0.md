---
card_id: codex-cli-2026-06-01-a2c432
date: '2026-06-01'
description: 'Codex CLI · 2026-06-01 · Context Window: 9 changes in 0.136.0 — Remote
  execution setup now supports `CODEX_API_KEY` registration for approved OpenAI hosts…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1124
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5790625575248907d53d822776b707223649032e3102276b60ced9c593bc358e
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-01-a2c432
  comparison: ''
  date: '2026-06-01'
  description: 'Codex CLI — 0.136.0: 9 Context Window changes'
  evidence:
  - quote: 'Remote execution setup now supports `CODEX_API_KEY` registration for approved
      OpenAI hosts, while remote-control websockets use short-lived server tokens
      instead of ChatGPT access tokens. (#24666, #24141)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: 'ChatGPT auth refreshes tokens before the five-minute expiry window and
      shows a relogin-required path for reused refresh tokens instead of collapsing
      into a generic cloud error. (#23546, #24830)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24892 Export Guardian prompt cache key helper @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24893 Add Guardian review prompt cache key @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24894 Assert Guardian prompt cache key reuse @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24803 Use stable Guardian prompt cache keys @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#23546 [codex-cli] Refresh near-expiry ChatGPT access tokens before requests
      @cooper-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24141 feat(app-server): migrate remote control to server tokens @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24918 Use internal model context fragments for goal steering @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-context-window-changes-in-rust-v0-136-0
  source_release: codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6
  source_type: github_releases
  theme: context-window
  title: 9 Context Window changes in rust-v0.136.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-28-4-context-window-changes-in-rust-v0-135-0|4 Context
  Window changes in rust-v0.135.0]]'
- '[[Changes/GitHub Copilot CLI/2026-05-28-2-context-window-changes-in-v1-0-55|2 Context
  Window changes in v1.0.55]]'
- '[[Changes/GitHub Copilot CLI/2026-05-29-2-context-window-changes-in-v1-0-56|2 Context
  Window changes in v1.0.56]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6|codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6]]'
source_type: github_releases
theme: context-window
title: 9 Context Window changes in rust-v0.136.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Context Window changes in rust-v0.136.0

**Codex CLI** · 2026-06-01 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.136.0) · from [[Releases/Codex CLI/codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6|0.136.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Remote execution setup now supports `CODEX_API_KEY` registration for approved OpenAI hosts, while remote-control websockets use short-lived server tokens instead of ChatGPT access tokens. (#24666, #24141)

> ChatGPT auth refreshes tokens before the five-minute expiry window and shows a relogin-required path for reused refresh tokens instead of collapsing into a generic cloud error. (#23546, #24830)

> #24892 Export Guardian prompt cache key helper @jif-oai

> #24893 Add Guardian review prompt cache key @jif-oai

> #24894 Assert Guardian prompt cache key reuse @jif-oai

> #24803 Use stable Guardian prompt cache keys @jif-oai

> #23546 [codex-cli] Refresh near-expiry ChatGPT access tokens before requests @cooper-oai

> #24141 feat(app-server): migrate remote control to server tokens @apanasenko-oai

> #24918 Use internal model context fragments for goal steering @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.136.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-01-25110-move-config-document-helpers-into-their-own-module-jif-oai|♯25110 Move config document helpers into their own module @jif-oai]] · Files and Data
- [[Changes/Codex CLI/2026-06-01-11-developer-workflow-changes-in-rust-v0-136-0|11 Developer Workflow changes in rust-v0.136.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-01-20-apps-and-integrations-changes-in-rust-v0-136-0|20 Apps and Integrations changes in rust-v0.136.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-01-11-safety-and-privacy-changes-in-rust-v0-136-0|11 Safety and Privacy changes in rust-v0.136.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-01-2-memory-and-personalization-changes-in-rust-v0-136-0|2 Memory and Personalization changes in rust-v0.136.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-06-01-5-model-support-changes-in-rust-v0-136-0|5 Model Support changes in rust-v0.136.0]] · Model Support
- [[Changes/Codex CLI/2026-06-01-3-agent-mode-changes-in-rust-v0-136-0|3 Agent Mode changes in rust-v0.136.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-01-2-editor-experience-changes-in-rust-v0-136-0|2 Editor Experience changes in rust-v0.136.0]] · Editor Experience
- [[Changes/Codex CLI/2026-06-01-3-search-and-browsing-changes-in-rust-v0-136-0|3 Search and Browsing changes in rust-v0.136.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-01-2-interface-experience-changes-in-rust-v0-136-0|2 Interface Experience changes in rust-v0.136.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-01-3-image-generation-changes-in-rust-v0-136-0|3 Image Generation changes in rust-v0.136.0]] · Image Generation
- [[Changes/Codex CLI/2026-06-01-57-other-changes-in-rust-v0-136-0|57 other changes in rust-v0.136.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-05-29 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-29-2-context-window-changes-in-v1-0-56|2 Context Window changes in v1.0.56]]
- Later: 2026-06-01 · Open WebUI · [[Changes/Open WebUI/2026-06-01-4-context-window-changes-in-v0-9-6|4 Context Window changes in v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-01-a2c432&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-01-9-context-window-changes-in-rust-v0-136-0.md%0ACard%20ID%3A%20codex-cli-2026-06-01-a2c432%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.136.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->