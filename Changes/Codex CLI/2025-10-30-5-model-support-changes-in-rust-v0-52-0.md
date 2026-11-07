---
card_id: codex-cli-2025-10-30-34dd27
date: '2025-10-30'
description: 'Codex CLI · 2025-10-30 · Model Support: 5 changes in 0.52.0 — Conversation
  management: centralized truncation for all tool outputs; filter out prior-turn…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1025
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7502e47866273cb4ae02841fbb498a25796531aa9c9a87997b2dd18a0d740896
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-10-30-34dd27
  comparison: ''
  date: '2025-10-30'
  description: 'Codex CLI — 0.52.0: 5 Model Support changes'
  evidence:
  - quote: 'Conversation management: centralized truncation for all tool outputs;
      filter out prior-turn reasoning; annotate conversations with model_provider.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'feat: annotate conversations with model_provider for filtering in https://github.com/openai/codex/pull/5658'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'feat: update NewConversationParams to take an optional model_provider
      in https://github.com/openai/codex/pull/5793'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'feat: support verbosity in model_family in https://github.com/openai/codex/pull/5821'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Filter out reasoning items from previous turns in https://github.com/openai/codex/pull/5857
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-model-support-changes-in-rust-v0-52-0
  source_release: codex-cli-2025-10-30-rust-v0-52-0-github-258584762-83f2b559
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in rust-v0.52.0
  type: change
related_changes:
- '[[Changes/Cursor/2025-10-29-plan-mode-in-background|Plan Mode in Background]]'
- '[[Changes/Gemini CLI/2025-10-29-5-model-support-changes-in-v0-11-0|5 Model Support
  changes in v0.11.0]]'
- '[[Changes/Ollama/2025-10-29-4-model-support-changes-in-v0-12-7|4 Model Support
  changes in v0.12.7]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-10-30-rust-v0-52-0-github-258584762-83f2b559|codex-cli-2025-10-30-rust-v0-52-0-github-258584762-83f2b559]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in rust-v0.52.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in rust-v0.52.0

**Codex CLI** · 2025-10-30 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.52.0) · from [[Releases/Codex CLI/codex-cli-2025-10-30-rust-v0-52-0-github-258584762-83f2b559|0.52.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Conversation management: centralized truncation for all tool outputs; filter out prior-turn reasoning; annotate conversations with model_provider.

> feat: annotate conversations with model_provider for filtering in https://github.com/openai/codex/pull/5658

> feat: update NewConversationParams to take an optional model_provider in https://github.com/openai/codex/pull/5793

> feat: support verbosity in model_family in https://github.com/openai/codex/pull/5821

> Filter out reasoning items from previous turns in https://github.com/openai/codex/pull/5857

Source: https://github.com/openai/codex/releases/tag/rust-v0.52.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-10-30-chore-speed-up-pipeline-in-https-github-com-openai-codex-pull-5812|chore: speed-up pipeline in (source link)]] · Reliability and Performance
- [[Changes/Codex CLI/2025-10-30-ability-to-buy-credits-for-more-usage-more-information-https-help-openai-com-en|Ability to buy credits for more usage]] · Pricing Model
- [[Changes/Codex CLI/2025-10-30-11-apps-and-integrations-changes-in-rust-v0-52-0|11 Apps and Integrations changes in rust-v0.52.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-10-30-chore-decompose-submission-loop-in-https-github-com-openai-codex-pull-5854|chore: decompose submission loop in (source link)]] · Automation and Scheduling
- [[Changes/Codex CLI/2025-10-30-3-agent-mode-changes-in-rust-v0-52-0|3 Agent Mode changes in rust-v0.52.0]] · Agent Mode
- [[Changes/Codex CLI/2025-10-30-2-context-window-changes-in-rust-v0-52-0|2 Context Window changes in rust-v0.52.0]] · Context Window
- [[Changes/Codex CLI/2025-10-30-2-account-and-access-changes-in-rust-v0-52-0|2 Account and Access changes in rust-v0.52.0]] · Account and Access
- [[Changes/Codex CLI/2025-10-30-chore-config-editor-in-https-github-com-openai-codex-pull-5878|chore: config editor in (source link)]] · Editor Experience
- [[Changes/Codex CLI/2025-10-30-5-developer-workflow-changes-in-rust-v0-52-0|5 Developer Workflow changes in rust-v0.52.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-10-30-3-safety-and-privacy-changes-in-rust-v0-52-0|3 Safety and Privacy changes in rust-v0.52.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-10-30-59-other-changes-in-rust-v0-52-0|59 other changes in rust-v0.52.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-10-29 · Ollama · [[Changes/Ollama/2025-10-29-4-model-support-changes-in-v0-12-7|4 Model Support changes in v0.12.7]]
- Later: 2025-10-30 · Ollama · [[Changes/Ollama/2025-10-30-ollama-will-now-stop-running-a-model-before-removing-it-via-ollama-rm|Ollama will now stop running a model before removing it via ollama rm]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-10-30-34dd27&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-10-30-5-model-support-changes-in-rust-v0-52-0.md%0ACard%20ID%3A%20codex-cli-2025-10-30-34dd27%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.52.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->