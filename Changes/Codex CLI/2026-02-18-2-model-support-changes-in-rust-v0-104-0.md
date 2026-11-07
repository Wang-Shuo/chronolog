---
card_id: codex-cli-2026-02-18-3824a9
date: '2026-02-18'
description: 'Codex CLI · 2026-02-18 · Model Support: 2 changes in 0.104.0 — Reduced
  false-positive safety-check downgrade behavior by relying on the response header
  model…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1136
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9f670068352377eb4fdb5357824c355a062f9a261b6f6e3fe1bbd41a06ba8358
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-18-3824a9
  comparison: ''
  date: '2026-02-18'
  description: 'Codex CLI — 0.104.0: 2 Model Support changes'
  evidence:
  - quote: Reduced false-positive safety-check downgrade behavior by relying on the
      response header model (and websocket top-level events) rather than the response
      body model slug. (#12061)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.104.0
  - quote: '#12061 Chore: remove response model check and rely on header model for
      downgrade @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.104.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 2-model-support-changes-in-rust-v0-104-0
  source_release: codex-cli-2026-02-18-rust-v0-104-0-github-287549221-f2e69b34
  source_type: github_releases
  theme: model-support
  title: 2 Model Support changes in rust-v0.104.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-02-17-2-model-support-changes-in-v0-0-411|2 Model
  Support changes in v0.0.411]]'
- '[[Changes/Midjourney/2026-02-17-please-note|Please Note]]'
- '[[Changes/Open WebUI/2026-02-17-4-model-support-changes-in-v0-8-3|4 Model Support
  changes in v0.8.3]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-18-rust-v0-104-0-github-287549221-f2e69b34|codex-cli-2026-02-18-rust-v0-104-0-github-287549221-f2e69b34]]'
source_type: github_releases
theme: model-support
title: 2 Model Support changes in rust-v0.104.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Model Support changes in rust-v0.104.0

**Codex CLI** · 2026-02-18 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.104.0) · from [[Releases/Codex CLI/codex-cli-2026-02-18-rust-v0-104-0-github-287549221-f2e69b34|0.104.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Reduced false-positive safety-check downgrade behavior by relying on the response header model (and websocket top-level events) rather than the response body model slug. (#12061)

> #12061 Chore: remove response model check and rely on header model for downgrade @shijie-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.104.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-18-protocol-core-now-carry-distinct-approval-ids-for-command-approvals-to-support-m|Protocol/core now carry distinct approval IDs for command approvals to support…]] · Agent Mode
- [[Changes/Codex CLI/2026-02-18-2-context-window-changes-in-rust-v0-104-0|2 Context Window changes in rust-v0.104.0]] · Context Window
- [[Changes/Codex CLI/2026-02-18-2-developer-workflow-changes-in-rust-v0-104-0|2 Developer Workflow changes in rust-v0.104.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-18-8-other-changes-in-rust-v0-104-0|8 other changes in rust-v0.104.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-02-17 · Open WebUI · [[Changes/Open WebUI/2026-02-17-4-model-support-changes-in-v0-8-3|4 Model Support changes in v0.8.3]]
- Later: 2026-02-18 · Cursor · [[Changes/Cursor/2026-02-18-2-model-support-changes-in-cli-improvements-and-mermaid-ascii|2 Model Support changes in CLI Improvements and Mermaid ASCII…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-18-3824a9&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-18-2-model-support-changes-in-rust-v0-104-0.md%0ACard%20ID%3A%20codex-cli-2026-02-18-3824a9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.104.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->