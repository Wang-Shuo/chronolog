---
card_id: codex-cli-2026-07-08-51b914
date: '2026-07-08'
description: 'Codex CLI · 2026-07-08 · Model Support: 14 changes in 0.143.0 — Added
  Amazon Bedrock GPT-5.6 Sol, Terra, and Luna models, with first-class support for
  `max`…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1276
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a29c579ebc31ddb2a6675e7092d4e21660803d08ba82318a3a319e057cd5b6a7
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-08-51b914
  comparison: ''
  date: '2026-07-08'
  description: 'Codex CLI — 0.143.0: 14 Model Support changes'
  evidence:
  - quote: 'Added Amazon Bedrock GPT-5.6 Sol, Terra, and Luna models, with first-class
      support for `max` reasoning effort. (#30285, #30467)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29417 [codex] replace remote images with model-visible error text @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29490 chore: warn when Code Mode lacks model metadata @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29155 [codex] Expose service tier and reasoning effort in OTEL @daniel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29899 [codex] Update reasoning effort @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29856 Persist selected capability roots and resolve availability per
      model step @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29942 feat: add provider-aware model fallback to thread start @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29683 [codex] Add managed new-thread model settings @hefuc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30285 feat: add GPT-5.6 variants to Bedrock catalog @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29740 [codex] Use model metadata for skills usage instructions @ani-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30467 [codex] Treat max as a first-class reasoning effort @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30897 Fix inherited availability metadata for Bedrock models @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31262 [codex] Read retry model from buffering events @fc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31306 [codex] Support sequential cutoff reasoning summaries @ashwinnathan-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 14-model-support-changes-in-rust-v0-143-0
  source_release: codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c
  source_type: github_releases
  theme: model-support
  title: 14 Model Support changes in rust-v0.143.0
  type: change
related_changes:
- '[[Changes/OpenHands/2026-07-06-4-model-support-changes-in-1-9-0|4 Model Support
  changes in 1.9.0]]'
- '[[Changes/GitHub Copilot CLI/2026-07-07-6-model-support-changes-in-v1-0-69|6 Model
  Support changes in v1.0.69]]'
- '[[Changes/Lovable/2026-07-07-nano-banana-2-lite-image-model-for-ai-features-in-your-app|Nano
  Banana 2 Lite image model for AI features in your app]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c|codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c]]'
source_type: github_releases
theme: model-support
title: 14 Model Support changes in rust-v0.143.0
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Model Support changes in rust-v0.143.0

**Codex CLI** · 2026-07-08 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.143.0) · from [[Releases/Codex CLI/codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c|0.143.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added Amazon Bedrock GPT-5.6 Sol, Terra, and Luna models, with first-class support for `max` reasoning effort. (#30285, #30467)

> #29417 [codex] replace remote images with model-visible error text @rka-oai

> #29490 chore: warn when Code Mode lacks model metadata @celia-oai

> #29155 [codex] Expose service tier and reasoning effort in OTEL @daniel-oai

> #29899 [codex] Update reasoning effort @shijie-oai

> #29856 Persist selected capability roots and resolve availability per model step @jif-oai

> #29942 feat: add provider-aware model fallback to thread start @celia-oai

> #29683 [codex] Add managed new-thread model settings @hefuc-oai

> #30285 feat: add GPT-5.6 variants to Bedrock catalog @celia-oai

> #29740 [codex] Use model metadata for skills usage instructions @ani-oai

> #30467 [codex] Treat max as a first-class reasoning effort @shijie-oai

> #30897 Fix inherited availability metadata for Bedrock models @shijie-oai

> #31262 [codex] Read retry model from buffering events @fc-oai

> #31306 [codex] Support sequential cutoff reasoning summaries @ashwinnathan-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.143.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-08-5-collaboration-changes-in-rust-v0-143-0|5 Collaboration changes in rust-v0.143.0]] · Collaboration
- [[Changes/Codex CLI/2026-07-08-5-account-and-access-changes-in-rust-v0-143-0|5 Account and Access changes in rust-v0.143.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-08-66-apps-and-integrations-changes-in-rust-v0-143-0|66 Apps and Integrations changes in rust-v0.143.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-08-10-agent-mode-changes-in-rust-v0-143-0|10 Agent Mode changes in rust-v0.143.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-08-27714-app-server-document-thread-and-turn-ids-are-uuid7-owenlin0|♯27714 app-server: document thread and turn IDs are UUID7 @owenlin0]] · Files and Data
- [[Changes/Codex CLI/2026-07-08-13-safety-and-privacy-changes-in-rust-v0-143-0|13 Safety and Privacy changes in rust-v0.143.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-07-08-28593-codex-suppress-low-usage-remaining-warnings-when-credits-are-available-bro|♯28593 codex suppress low usage remaining warnings when credits are available…]] · Pricing Model
- [[Changes/Codex CLI/2026-07-08-12-context-window-changes-in-rust-v0-143-0|12 Context Window changes in rust-v0.143.0]] · Context Window
- [[Changes/Codex CLI/2026-07-08-30508-revert-make-auto-review-on-request-prompt-more-proactive-dylan-hurd-oai|♯30508 Revert "Make auto-review on-request prompt more proactive" @dylan-hurd-oai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-07-08-2-mobile-and-desktop-changes-in-rust-v0-143-0|2 Mobile and Desktop changes in rust-v0.143.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-08-3-editor-experience-changes-in-rust-v0-143-0|3 Editor Experience changes in rust-v0.143.0]] · Editor Experience
- [[Changes/Codex CLI/2026-07-08-7-developer-workflow-changes-in-rust-v0-143-0|7 Developer Workflow changes in rust-v0.143.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-08-3-image-generation-changes-in-rust-v0-143-0|3 Image Generation changes in rust-v0.143.0]] · Image Generation
- [[Changes/Codex CLI/2026-07-08-2-memory-and-personalization-changes-in-rust-v0-143-0|2 Memory and Personalization changes in rust-v0.143.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-08-remote-plugins-are-now-enabled-by-default-with-richer-catalog-rows-npm-marketpla|Remote plugins are now enabled by default, with richer catalog rows, npm marketplace…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-08-145-other-changes-in-rust-v0-143-0|145 other changes in rust-v0.143.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-07-07 · Lovable · [[Changes/Lovable/2026-07-07-nano-banana-2-lite-image-model-for-ai-features-in-your-app|Nano Banana 2 Lite image model for AI features in your app]]
- Later: 2026-07-09 · Cline · [[Changes/Cline/2026-07-09-allow-selecting-cline-free-models-on-the-clinepass-provider-organized-into-subsc|Allow selecting Cline free models on the ClinePass provider, organized…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-08-51b914&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-08-14-model-support-changes-in-rust-v0-143-0.md%0ACard%20ID%3A%20codex-cli-2026-07-08-51b914%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.143.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->