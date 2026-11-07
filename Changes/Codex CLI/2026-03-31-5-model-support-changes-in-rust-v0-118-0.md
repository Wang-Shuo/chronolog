---
card_id: codex-cli-2026-03-31-e51d88
date: '2026-03-31'
description: 'Codex CLI · 2026-03-31 · Model Support: 5 changes in 0.118.0 — Custom
  model providers can now fetch and refresh short-lived bearer tokens dynamically,
  instead…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1177
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6f9fd50ddc6100ccdfda9d91e035ce0792ef3ae9ee7f09844d0fbf9c0924af93
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-31-e51d88
  comparison: ''
  date: '2026-03-31'
  description: 'Codex CLI — 0.118.0: 5 Model Support changes'
  evidence:
  - quote: 'Custom model providers can now fetch and refresh short-lived bearer tokens
      dynamically, instead of being limited to static credentials from config or environment
      variables. (#16286, #16287, #16288)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16031 codex-tools: extract responses API tool models @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16047 codex-tools: extract tool spec models @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16254 codex-tools: extract discoverable tool models @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16288 core: support dynamic auth tokens for model providers @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-model-support-changes-in-rust-v0-118-0
  source_release: codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in rust-v0.118.0
  type: change
related_changes:
- '[[Changes/Raycast/2026-03-27-2-model-support-changes-in-raycast-macos-0-51|2 Model
  Support changes in Raycast macos 0.51]]'
- '[[Changes/OpenCode/2026-03-29-2-model-support-changes-in-v1-3-6-2|2 Model Support
  changes in v1.3.6 + 2]]'
- '[[Changes/GitHub Copilot CLI/2026-03-30-2-model-support-changes-in-v1-0-13|2 Model
  Support changes in v1.0.13]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6|codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in rust-v0.118.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in rust-v0.118.0

**Codex CLI** · 2026-03-31 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.118.0) · from [[Releases/Codex CLI/codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6|0.118.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Custom model providers can now fetch and refresh short-lived bearer tokens dynamically, instead of being limited to static credentials from config or environment variables. (#16286, #16287, #16288)

> #16031 codex-tools: extract responses API tool models @bolinfest

> #16047 codex-tools: extract tool spec models @bolinfest

> #16254 codex-tools: extract discoverable tool models @bolinfest

> #16288 core: support dynamic auth tokens for model providers @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.118.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-31-16286-auth-generalize-external-auth-tokens-for-bearer-only-sources-bolinfest|♯16286 auth: generalize external auth tokens for bearer-only sources @bolinfest]] · Context Window
- [[Changes/Codex CLI/2026-03-31-16021-fix-copy-regression-in-tui-app-server-turn-completion-etraut-openai|♯16021 Fix /copy regression in tui_app_server turn completion @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-03-31-12-apps-and-integrations-changes-in-rust-v0-118-0|12 Apps and Integrations changes in rust-v0.118.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-31-16114-remove-tui-voice-transcription-feature-etraut-openai|♯16114 Remove TUI voice transcription feature @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-31-3-interface-experience-changes-in-rust-v0-118-0|3 Interface Experience changes in rust-v0.118.0]] · Interface Experience
- [[Changes/Codex CLI/2026-03-31-4-account-and-access-changes-in-rust-v0-118-0|4 Account and Access changes in rust-v0.118.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-31-3-developer-workflow-changes-in-rust-v0-118-0|3 Developer Workflow changes in rust-v0.118.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-31-15934-add-usage-based-business-plan-types-bwanner-oai|♯15934 Add usage-based business plan types @bwanner-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-03-31-7-safety-and-privacy-changes-in-rust-v0-118-0|7 Safety and Privacy changes in rust-v0.118.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-31-4-agent-mode-changes-in-rust-v0-118-0|4 Agent Mode changes in rust-v0.118.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-31-7-mobile-and-desktop-changes-in-rust-v0-118-0|7 Mobile and Desktop changes in rust-v0.118.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-31-4-collaboration-changes-in-rust-v0-118-0|4 Collaboration changes in rust-v0.118.0]] · Collaboration
- [[Changes/Codex CLI/2026-03-31-51-other-changes-in-rust-v0-118-0|51 other changes in rust-v0.118.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-03-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-30-2-model-support-changes-in-v1-0-13|2 Model Support changes in v1.0.13]]
- Later: 2026-03-31 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-31-3-model-support-changes-in-v1-0-14|3 Model Support changes in v1.0.14]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-31-e51d88&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-31-5-model-support-changes-in-rust-v0-118-0.md%0ACard%20ID%3A%20codex-cli-2026-03-31-e51d88%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.118.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->