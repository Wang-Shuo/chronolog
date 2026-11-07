---
card_id: ollama-2025-05-29-ed9639
date: '2025-05-29'
description: 'Ollama · 2025-05-29 · Model Support: 7 changes in v0.9.0 — [DeepSeek-R1-2508](https://ollama.com/library/deepseek-r1):
  DeepSeek-R1 has received a minor version…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 871
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 39feebc73ec6e0c4b720fc88400caa46736b1e7ff4e451b3cbe5f8460f7150a6
product: ollama
product_name: Ollama
record:
  card_id: ollama-2025-05-29-ed9639
  comparison: ''
  date: '2025-05-29'
  description: 'Ollama — v0.9.0: 7 Model Support changes'
  evidence:
  - quote: '[DeepSeek-R1-2508](https://ollama.com/library/deepseek-r1): DeepSeek-R1
      has received a minor version upgrade to DeepSeek-R1-0528 for the 8 billion parameter
      distilled model and the full 671 billion parameter model. In this update, DeepSeek
      R1 has significantly improved its reasoning and inference capabilities.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.9.0
  - quote: Ollama now has the ability to enable or disable thinking. This gives users
      the flexibility to choose the model’s thinking behavior for different applications
      and use cases.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.9.0
  - quote: When thinking is enabled, the output will separate the model’s thinking
      from the model’s output. When thinking is disabled, the model will not think
      and directly output the content.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.9.0
  - quote: 'Models that support thinking:'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.9.0
  - quote: more will be added under thinking models.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.9.0
  - quote: 'When running a model that supports thinking, Ollama will now display the
      model''s thoughts:'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.9.0
  - quote: 'In Ollama''s API, a model''s thinking is now returned as a separate `thinking`
      field for easy parsing:'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 7-model-support-changes-in-v0-9-0
  source_release: ollama-2025-05-29-v0-9-0-github-221722484-f8cc3c3d
  source_type: github_releases
  theme: model-support
  title: 7 Model Support changes in v0.9.0
  type: change
related_changes:
- '[[Changes/Cline/2025-05-28-2-model-support-changes-in-v3-17-6|2 Model Support changes
  in v3.17.6]]'
- '[[Changes/DeepSeek API/2025-05-28-deepseek-reasoner|deepseek-reasoner]]'
- "[[Changes/Open WebUI/2025-05-28-custom-advanced-model-parameters-you-can-now-add-your-own-tailor-made-advanced-p|\U0001F9E9
  Custom Advanced Model Parameters]]"
source_release: '[[Releases/Ollama/ollama-2025-05-29-v0-9-0-github-221722484-f8cc3c3d|ollama-2025-05-29-v0-9-0-github-221722484-f8cc3c3d]]'
source_type: github_releases
theme: model-support
title: 7 Model Support changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Model Support changes in v0.9.0

**Ollama** · 2025-05-29 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.9.0) · from [[Releases/Ollama/ollama-2025-05-29-v0-9-0-github-221722484-f8cc3c3d|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> [DeepSeek-R1-2508](https://ollama.com/library/deepseek-r1): DeepSeek-R1 has received a minor version upgrade to DeepSeek-R1-0528 for the 8 billion parameter distilled model and the full 671 billion parameter model. In this update, DeepSeek R1 has significantly improved its reasoning and inference capabilities.

> Ollama now has the ability to enable or disable thinking. This gives users the flexibility to choose the model’s thinking behavior for different applications and use cases.

> When thinking is enabled, the output will separate the model’s thinking from the model’s output. When thinking is disabled, the model will not think and directly output the content.

> Models that support thinking:

> more will be added under thinking models.

> When running a model that supports thinking, Ollama will now display the model's thoughts:

> In Ollama's API, a model's thinking is now returned as a separate `thinking` field for easy parsing:

Source: https://github.com/ollama/ollama/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2025-05-29-6-other-changes-in-v0-9-0|6 other changes in v0.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-05-28 · Open WebUI · [[Changes/Open WebUI/2025-05-28-custom-advanced-model-parameters-you-can-now-add-your-own-tailor-made-advanced-p|🧩 Custom Advanced Model Parameters]]
- Later: 2025-05-29 · Open WebUI · [[Changes/Open WebUI/2025-05-29-2-model-support-changes-in-v0-6-13|2 Model Support changes in v0.6.13]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2025-05-29-ed9639&body=Card%3A%20Changes%2FOllama%2F2025-05-29-7-model-support-changes-in-v0-9-0.md%0ACard%20ID%3A%20ollama-2025-05-29-ed9639%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->