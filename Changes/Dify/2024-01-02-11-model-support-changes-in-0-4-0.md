---
card_id: dify-2024-01-02-61e530
date: '2024-01-02'
description: 'Dify · 2024-01-02 · Model Support: 11 changes in v0.4.0 — We''ve made
  some serious under-the-hood changes to how the Model Runtime works, making it more…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 358
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d31c9741f83dfcecced9a6f49495a55926861216b87dc5236623ea3cd5e1c901
product: dify
product_name: Dify
record:
  card_id: dify-2024-01-02-61e530
  comparison: ''
  date: '2024-01-02'
  description: 'Dify — v0.4.0: 11 Model Support changes'
  evidence:
  - quote: We've made some serious under-the-hood changes to how the Model Runtime
      works, making it more straightforward for our specific needs, and paving the
      way for smoother model expansions and more robust production use.
    source_release: https://github.com/langgenius/dify/releases/tag/0.4.0
  - quote: '**Model Runtime Rework:** We''ve moved away from LangChain, simplifying
      the model layer. Now, expanding models is as easy as setting up the model provider
      in the backend with a bit of YAML.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.4.0
  - quote: 'For more details, see: https://github.com/langgenius/dify/blob/main/api/core/model_runtime/README.md'
    source_release: https://github.com/langgenius/dify/releases/tag/0.4.0
  - quote: '**Model Providers Upgraded:** Support for both preset and custom models,
      ideal for adding OpenAI `fine-tuned models` or fitting into various MaaS platforms.
      Plus, you can now check out supported models without any initial configuration.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.4.0
  - quote: '**Context Size Definition:** Introduced distinct `context size` settings,
      separate from `Max Tokens`, to handle the different limits and sizes in models
      like OpenAI''s `GPT-4 Turbo`.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.4.0
  - quote: '**Flexible Model Parameters:** Customize your model''s behavior with easily
      adjustable parameters through YAML.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.4.0
  - quote: '**Model List Display:** The App now displays all supported preset models,
      including details on any that aren''t available and how to configure them.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.4.0
  - quote: '**New Model Additions:** Including Google''s `Gemini Pro` and `Gemini
      Pro Vision` models (Vision requires an image input), Azure OpenAI''s `GPT-4V`,
      and support for `OpenAI-API-compatible` providers.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.4.0
  - quote: '**Updates & Fixes:** We''ve updated other model providers to be in sync
      with the latest version APIs and features, and squashed a series of minor bugs
      for a smoother experience.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.4.0
  - quote: Model Runtime by @takatost in https://github.com/langgenius/dify/pull/1858
    source_release: https://github.com/langgenius/dify/releases/tag/0.4.0
  - quote: frontend for model runtime by @zxhlyh in https://github.com/langgenius/dify/pull/1861
    source_release: https://github.com/langgenius/dify/releases/tag/0.4.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 11-model-support-changes-in-0-4-0
  source_release: dify-2024-01-02-0-4-0-github-135559615-949bf14a
  source_type: github_releases
  theme: model-support
  title: 11 Model Support changes in 0.4.0
  type: change
related_changes:
- '[[Changes/Dify/2023-12-19-2-model-support-changes-in-0-3-34|2 Model Support changes
  in 0.3.34]]'
- '[[Changes/Ollama/2023-12-19-6-model-support-changes-in-v0-1-17|6 Model Support
  changes in v0.1.17]]'
- '[[Changes/Aider/2023-12-20-3-model-support-changes-in-v0-19-0|3 Model Support changes
  in v0.19.0]]'
source_release: '[[Releases/Dify/dify-2024-01-02-0-4-0-github-135559615-949bf14a|dify-2024-01-02-0-4-0-github-135559615-949bf14a]]'
source_type: github_releases
theme: model-support
title: 11 Model Support changes in 0.4.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Model Support changes in 0.4.0

**Dify** · 2024-01-02 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.4.0) · from [[Releases/Dify/dify-2024-01-02-0-4-0-github-135559615-949bf14a|v0.4.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> We've made some serious under-the-hood changes to how the Model Runtime works, making it more straightforward for our specific needs, and paving the way for smoother model expansions and more robust production use.

> **Model Runtime Rework:** We've moved away from LangChain, simplifying the model layer. Now, expanding models is as easy as setting up the model provider in the backend with a bit of YAML.

> For more details, see: https://github.com/langgenius/dify/blob/main/api/core/model_runtime/README.md

> **Model Providers Upgraded:** Support for both preset and custom models, ideal for adding OpenAI `fine-tuned models` or fitting into various MaaS platforms. Plus, you can now check out supported models without any initial configuration.

> **Context Size Definition:** Introduced distinct `context size` settings, separate from `Max Tokens`, to handle the different limits and sizes in models like OpenAI's `GPT-4 Turbo`.

> **Flexible Model Parameters:** Customize your model's behavior with easily adjustable parameters through YAML.

> **Model List Display:** The App now displays all supported preset models, including details on any that aren't available and how to configure them.

> **New Model Additions:** Including Google's `Gemini Pro` and `Gemini Pro Vision` models (Vision requires an image input), Azure OpenAI's `GPT-4V`, and support for `OpenAI-API-compatible` providers.

> **Updates & Fixes:** We've updated other model providers to be in sync with the latest version APIs and features, and squashed a series of minor bugs for a smoother experience.

> Model Runtime by @takatost in https://github.com/langgenius/dify/pull/1858

> frontend for model runtime by @zxhlyh in https://github.com/langgenius/dify/pull/1861

Source: https://github.com/langgenius/dify/releases/tag/0.4.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-01-02-feat-add-billing-switch-by-garfielddai-in-https-github-com-langgenius-dify-pull|feat: add billing switch]] · Pricing Model
- [[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add data clean schedule]] · Automation and Scheduling
- [[Changes/Dify/2024-01-02-gpt-2-tokenizer-files-now-cached-within-dify-s-codebase-making-builds-quicker-an|GPT-2 Tokenizer Files: Now cached within Dify's codebase, making builds quicker…]] · Editor Experience
- [[Changes/Dify/2024-01-02-the-dify-team|The Dify Team 🛠️]] · Collaboration
- [[Changes/Dify/2024-01-02-expanded-inference-support-xorbit-inference-now-includes-chat-mode-models-and-th|Expanded Inference Support: Xorbit Inference now includes chat mode models…]] · Agent Mode
- [[Changes/Dify/2024-01-02-20-other-changes-in-0-4-0|20 other changes in 0.4.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2023-12-20 · Aider · [[Changes/Aider/2023-12-20-3-model-support-changes-in-v0-19-0|3 Model Support changes in v0.19.0]]
- Later: 2024-01-03 · Ollama · [[Changes/Ollama/2024-01-03-5-model-support-changes-in-v0-1-18|5 Model Support changes in v0.1.18]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-01-02-61e530&body=Card%3A%20Changes%2FDify%2F2024-01-02-11-model-support-changes-in-0-4-0.md%0ACard%20ID%3A%20dify-2024-01-02-61e530%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.4.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->