---
card_id: ollama-2023-10-27-8f4011
date: '2023-10-27'
description: 'Ollama · 2023-10-27 · Model Support: 5 changes in v0.1.6 — [Dolphin
  2.1 Mistral](https://ollama.ai/library/dolphin2.1-mistral): an instruct-tuned model
  based…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 291
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fd5753623afdf19eaf2e6f697c229377e6550b52a58bf4f58d864f14c7ca31f9
product: ollama
product_name: Ollama
record:
  card_id: ollama-2023-10-27-8f4011
  comparison: ''
  date: '2023-10-27'
  description: 'Ollama — v0.1.6: 5 Model Support changes'
  evidence:
  - quote: '[Dolphin 2.1 Mistral](https://ollama.ai/library/dolphin2.1-mistral): an
      instruct-tuned model based on Mistral and trained on a dataset filtered to remove
      alignment and bias.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.6
  - quote: 'The library models have been refreshed and revamped including `llama2`,
      `codellama`, and more:'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.6
  - quote: All `chat` or `instruct` models now support setting the `system` parameter,
      or `SYSTEM` command in the `Modelfile`
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.6
  - quote: Parameters (`num_ctx`, etc) have been updated for library models
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.6
  - quote: Model storage can now be configured with `OLLAMA_MODELS`. See the [FAQ](https://github.com/jmorganca/ollama/blob/main/docs/faq.md#how-can-i-change-where-ollama-stores-models)
      for more info on how to configure this.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 5-model-support-changes-in-v0-1-6
  source_release: ollama-2023-10-27-v0-1-6-github-127004875-cc195255
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in v0.1.6
  type: change
related_changes:
- '[[Changes/ChatGPT/2023-10-17-browsing-which-we-re-launched-a-few-weeks-ago-is-moving-out-of-beta-plus-and-ent|Browsing
  is now out of beta]]'
- '[[Changes/Aider/2023-10-18-show-models-supported-by-api-key-if-requested-model-isn-t-available|Show
  models supported by api/key if requested model isn''t available]]'
- '[[Changes/Ollama/2023-10-20-4-model-support-changes-in-v0-1-4|4 Model Support changes
  in v0.1.4]]'
source_release: '[[Releases/Ollama/ollama-2023-10-27-v0-1-6-github-127004875-cc195255|ollama-2023-10-27-v0-1-6-github-127004875-cc195255]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in v0.1.6
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in v0.1.6

**Ollama** · 2023-10-27 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.1.6) · from [[Releases/Ollama/ollama-2023-10-27-v0-1-6-github-127004875-cc195255|v0.1.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> [Dolphin 2.1 Mistral](https://ollama.ai/library/dolphin2.1-mistral): an instruct-tuned model based on Mistral and trained on a dataset filtered to remove alignment and bias.

> The library models have been refreshed and revamped including `llama2`, `codellama`, and more:

> All `chat` or `instruct` models now support setting the `system` parameter, or `SYSTEM` command in the `Modelfile`

> Parameters (`num_ctx`, etc) have been updated for library models

> Model storage can now be configured with `OLLAMA_MODELS`. See the [FAQ](https://github.com/jmorganca/ollama/blob/main/docs/faq.md#how-can-i-change-where-ollama-stores-models) for more info on how to configure this.

Source: https://github.com/ollama/ollama/releases/tag/v0.1.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2023-10-27-2-reliability-and-performance-changes-in-v0-1-6|2 Reliability and Performance changes in v0.1.6]] · Reliability and Performance
- [[Changes/Ollama/2023-10-27-2-other-changes-in-v0-1-6|2 other changes in v0.1.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2023-10-20 · Ollama · [[Changes/Ollama/2023-10-20-4-model-support-changes-in-v0-1-4|4 Model Support changes in v0.1.4]]
- Later: 2023-11-04 · Ollama · [[Changes/Ollama/2023-11-04-3-model-support-changes-in-v0-1-8|3 Model Support changes in v0.1.8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2023-10-27-8f4011&body=Card%3A%20Changes%2FOllama%2F2023-10-27-5-model-support-changes-in-v0-1-6.md%0ACard%20ID%3A%20ollama-2023-10-27-8f4011%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.1.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->