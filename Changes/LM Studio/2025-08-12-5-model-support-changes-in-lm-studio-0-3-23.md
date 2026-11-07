---
card_id: lm-studio-2025-08-12-c34f63
date: '2025-08-12'
description: 'LM Studio · 2025-08-12 · Model Support: 5 changes in LM Studio 0.3.23
  — [llama.cpp][MoE] Add ability to offload expert weights to CPU/GPU RAM via "Force
  Model…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 946
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9370d3f3d78aace54b3f62fd8e1ebbbad5956b0ed4f718e41006d3dff9246eb3
product: lm-studio
product_name: LM Studio
record:
  card_id: lm-studio-2025-08-12-c34f63
  comparison: ''
  date: '2025-08-12'
  description: 'LM Studio — LM Studio 0.3.23: 5 Model Support changes'
  evidence:
  - quote: '[llama.cpp][MoE] Add ability to offload expert weights to CPU/GPU RAM
      via "Force Model Expert Weights onto CPU" in advanced load settings'
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.23
  - quote: Tool names are normalized before being provided to the model (replace whitespaces,
      special chars)
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.23
  - quote: '`message.content` will not include reasoning content or special tags'
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.23
  - quote: This matches the behavior of `o3-mini`.
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.23
  - quote: Reasoning content will be in `choices.message.reasoning` (stream=false)
      and `choices.delta.reasoning` (stream=true)
    source_release: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.23
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: lm-studio
  product_name: LM Studio
  slug: 5-model-support-changes-in-lm-studio-0-3-23
  source_release: lm-studio-2025-08-12-0-3-23-c3f0261e
  source_type: lmstudio_changelog
  theme: model-support
  title: 5 Model Support changes in LM Studio 0.3.23
  type: change
related_changes:
- '[[Changes/ChatGPT/2025-08-12-you-can-now-choose-between-auto-fast-and-thinking-for-gpt-5-most-users-will-want-f4c05b|GPT-5
  Updates]]'
- '[[Changes/Codex CLI/2025-08-12-https-github-com-openai-codex-pull-2183-include-output-truncation-message-in-too|(source
  link) Include output truncation message in tool…]]'
- '[[Changes/Gemini CLI/2025-08-12-7-model-support-changes-in-v0-1-19|7 Model Support
  changes in v0.1.19]]'
source_release: '[[Releases/LM Studio/lm-studio-2025-08-12-0-3-23-c3f0261e|lm-studio-2025-08-12-0-3-23-c3f0261e]]'
source_type: lmstudio_changelog
theme: model-support
title: 5 Model Support changes in LM Studio 0.3.23
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in LM Studio 0.3.23

**LM Studio** · 2025-08-12 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.23) · from [[Releases/LM Studio/lm-studio-2025-08-12-0-3-23-c3f0261e|LM Studio 0.3.23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> [llama.cpp][MoE] Add ability to offload expert weights to CPU/GPU RAM via "Force Model Expert Weights onto CPU" in advanced load settings

> Tool names are normalized before being provided to the model (replace whitespaces, special chars)

> `message.content` will not include reasoning content or special tags

> This matches the behavior of `o3-mini`.

> Reasoning content will be in `choices.message.reasoning` (stream=false) and `choices.delta.reasoning` (stream=true)

Source: https://lmstudio.ai/changelog/lmstudio/lmstudio-v0.3.23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/LM Studio/2025-08-12-for-gpt-oss|For gpt-oss]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-08-12 · Gemini CLI · [[Changes/Gemini CLI/2025-08-12-7-model-support-changes-in-v0-1-19|7 Model Support changes in v0.1.19]]
- Later: 2025-08-12 · Superwhisper · [[Changes/Superwhisper/2025-08-12-messages-mode-custom-model-fixes|Messages Mode & Custom Model Fixes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20lm-studio-2025-08-12-c34f63&body=Card%3A%20Changes%2FLM%20Studio%2F2025-08-12-5-model-support-changes-in-lm-studio-0-3-23.md%0ACard%20ID%3A%20lm-studio-2025-08-12-c34f63%0ASource%3A%20https%3A%2F%2Flmstudio.ai%2Fchangelog%2Flmstudio%2Flmstudio-v0.3.23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->