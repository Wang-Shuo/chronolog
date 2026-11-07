---
card_id: codex-cli-2026-07-09-ab3059
date: '2026-07-09'
description: 'Codex CLI · 2026-07-09 · Model Support: 8 changes in 0.144.0 — Resumed
  ChatGPT threads recover when compaction references a retired model by retrying with
  the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1277
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 14d3900b2ab1eca92e6c1a6f4a12dfacc666e367f608968f03289048fb6884c3
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-09-ab3059
  comparison: ''
  date: '2026-07-09'
  description: 'Codex CLI — 0.144.0: 8 Model Support changes'
  evidence:
  - quote: Resumed ChatGPT threads recover when compaction references a retired model
      by retrying with the currently selected model. (#30319)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: Made Amazon Bedrock model names clearly identify their GPT-5.6 family and
      variant. (#31636)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31312 Use model catalog approval messages @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#30319 fix: retry rejected previous-model compaction with selected model
      @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31636 feat: change amazon Bedrock GPT-5.6 display names @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#21818 Update models.json @github-actions'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31361 model-provider: route model discovery through HTTP client factory
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31684 Update models.json @github-actions'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 8-model-support-changes-in-rust-v0-144-0
  source_release: codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96
  source_type: github_releases
  theme: model-support
  title: 8 Model Support changes in rust-v0.144.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-07-08-14-model-support-changes-in-rust-v0-143-0|14 Model
  Support changes in rust-v0.143.0]]'
- '[[Changes/Kimi Code/2026-07-08-2-model-support-changes-in-kimi-code-0-23-2|2 Model
  Support changes in Kimi Code 0.23.2]]'
- '[[Changes/Cline/2026-07-09-allow-selecting-cline-free-models-on-the-clinepass-provider-organized-into-subsc|Allow
  selecting Cline free models on the ClinePass provider, organized…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96|codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96]]'
source_type: github_releases
theme: model-support
title: 8 Model Support changes in rust-v0.144.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Model Support changes in rust-v0.144.0

**Codex CLI** · 2026-07-09 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.144.0) · from [[Releases/Codex CLI/codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96|0.144.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Resumed ChatGPT threads recover when compaction references a retired model by retrying with the currently selected model. (#30319)

> Made Amazon Bedrock model names clearly identify their GPT-5.6 family and variant. (#31636)

> #31312 Use model catalog approval messages @dylan-hurd-oai

> #30319 fix: retry rejected previous-model compaction with selected model @celia-oai

> #31636 feat: change amazon Bedrock GPT-5.6 display names @celia-oai

> #21818 Update models.json @github-actions

> #31361 model-provider: route model discovery through HTTP client factory @bolinfest

> #31684 Update models.json @github-actions

Source: https://github.com/openai/codex/releases/tag/rust-v0.144.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-09-31191-handle-completion-separators-and-popup-dismissal-charliemarsh-oai|♯31191 Handle completion separators and popup dismissal @charliemarsh-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-07-09-31596-use-the-image-generation-extension-by-default-won-openai|♯31596 Use the image generation extension by default @won-openai]] · Image Generation
- [[Changes/Codex CLI/2026-07-09-responses-websockets-continue-using-the-low-latency-transport-while-respecting-s|Responses WebSockets continue using the low-latency transport while respecting…]] · Reliability and Performance
- [[Changes/Codex CLI/2026-07-09-31356-ci-run-v8-source-builds-on-windows-2025-anp-oai|♯31356 ci: run V8 source builds on Windows 2025 @anp-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-09-11-apps-and-integrations-changes-in-rust-v0-144-0|11 Apps and Integrations changes in rust-v0.144.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-09-31587-stabilize-shared-rollout-budget-test-jif-oai|♯31587 Stabilize shared rollout budget test @jif-oai]] · Collaboration
- [[Changes/Codex CLI/2026-07-09-31525-core-migrate-standalone-web-search-to-extension-owned-turn-items-owenlin0|♯31525 core: migrate standalone web search to extension-owned turn items @owenlin0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-09-5-account-and-access-changes-in-rust-v0-144-0|5 Account and Access changes in rust-v0.144.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-09-usage-limit-reset-credits-now-show-their-type-and-expiration-and-let-you-choose|Usage-limit reset credits now show their type and expiration, and let you choose…]] · Pricing Model
- [[Changes/Codex CLI/2026-07-09-3-context-window-changes-in-rust-v0-144-0|3 Context Window changes in rust-v0.144.0]] · Context Window
- [[Changes/Codex CLI/2026-07-09-3-interface-experience-changes-in-rust-v0-144-0|3 Interface Experience changes in rust-v0.144.0]] · Interface Experience
- [[Changes/Codex CLI/2026-07-09-6-developer-workflow-changes-in-rust-v0-144-0|6 Developer Workflow changes in rust-v0.144.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-09-4-safety-and-privacy-changes-in-rust-v0-144-0|4 Safety and Privacy changes in rust-v0.144.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-07-09-4-agent-mode-changes-in-rust-v0-144-0|4 Agent Mode changes in rust-v0.144.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-09-43-other-changes-in-rust-v0-144-0|43 other changes in rust-v0.144.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-07-09 · Cline · [[Changes/Cline/2026-07-09-allow-selecting-cline-free-models-on-the-clinepass-provider-organized-into-subsc|Allow selecting Cline free models on the ClinePass provider, organized…]]
- Later: 2026-07-09 · OpenCode · [[Changes/OpenCode/2026-07-09-3-model-support-changes-in-v1-17-18-1|3 Model Support changes in v1.17.18 + 1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-09-ab3059&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-09-8-model-support-changes-in-rust-v0-144-0.md%0ACard%20ID%3A%20codex-cli-2026-07-09-ab3059%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.144.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->