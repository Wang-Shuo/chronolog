---
card_id: ollama-2023-10-20-aae1f7
date: '2023-10-20'
description: 'Ollama · 2023-10-20 · Model Support: 4 changes in v0.1.4 — [OpenHermes
  2 Mistral](https://ollama.ai/library/openhermes2-mistral): a new fine-tuned model
  based…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 284
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1f8097b04684ddaa4c80faea76f3c4631b2154106d4f00f3f09fd40e7c074e3e
product: ollama
product_name: Ollama
record:
  card_id: ollama-2023-10-20-aae1f7
  comparison: ''
  date: '2023-10-20'
  description: 'Ollama — v0.1.4: 4 Model Support changes'
  evidence:
  - quote: '[OpenHermes 2 Mistral](https://ollama.ai/library/openhermes2-mistral):
      a new fine-tuned model based on Mistral, trained on open datasets totalling
      over 900,000 instructions. This model has strong multi-turn chat skills, surpassing
      previous Hermes 13B models and even matching 70B models on some benchmarks.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.4
  - quote: 'Faster model switching: models will now stay loaded between requests when
      using different parameters (e.g. `temperature`) or system prompts'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.4
  - quote: '`starcoder`, `sqlcoder` and `falcon` models now have unicode support.
      Note: they will need to be re-pulled (e.g. `ollama pull starcoder`)'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.4
  - quote: New documentation guide on [importing existing models](https://github.com/jmorganca/ollama/blob/main/docs/import.md)
      to Ollama (GGUF, PyTorch, etc)
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 4-model-support-changes-in-v0-1-4
  source_release: ollama-2023-10-20-v0-1-4-github-125837077-2c3cf7e5
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in v0.1.4
  type: change
related_changes:
- '[[Changes/ChatGPT/2023-10-16-we-ve-integrated-dall-e-3-with-chatgpt-allowing-it-to-respond-to-your-requests-w-ad3caf|DALL·E
  3 is now rolling out in beta]]'
- '[[Changes/ChatGPT/2023-10-17-browsing-which-we-re-launched-a-few-weeks-ago-is-moving-out-of-beta-plus-and-ent|Browsing
  is now out of beta]]'
- '[[Changes/Aider/2023-10-18-show-models-supported-by-api-key-if-requested-model-isn-t-available|Show
  models supported by api/key if requested model isn''t available]]'
source_release: '[[Releases/Ollama/ollama-2023-10-20-v0-1-4-github-125837077-2c3cf7e5|ollama-2023-10-20-v0-1-4-github-125837077-2c3cf7e5]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in v0.1.4
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v0.1.4

**Ollama** · 2023-10-20 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.1.4) · from [[Releases/Ollama/ollama-2023-10-20-v0-1-4-github-125837077-2c3cf7e5|v0.1.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> [OpenHermes 2 Mistral](https://ollama.ai/library/openhermes2-mistral): a new fine-tuned model based on Mistral, trained on open datasets totalling over 900,000 instructions. This model has strong multi-turn chat skills, surpassing previous Hermes 13B models and even matching 70B models on some benchmarks.

> Faster model switching: models will now stay loaded between requests when using different parameters (e.g. `temperature`) or system prompts

> `starcoder`, `sqlcoder` and `falcon` models now have unicode support. Note: they will need to be re-pulled (e.g. `ollama pull starcoder`)

> New documentation guide on [importing existing models](https://github.com/jmorganca/ollama/blob/main/docs/import.md) to Ollama (GGUF, PyTorch, etc)

Source: https://github.com/ollama/ollama/releases/tag/v0.1.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2023-10-20-ollama-run-will-now-show-more-descriptive-errors-when-encountering-runtime-issue|ollama run will now show more descriptive errors when encountering runtime issues…]] · Reliability and Performance
- [[Changes/Ollama/2023-10-20-2-other-changes-in-v0-1-4|2 other changes in v0.1.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2023-10-18 · Aider · [[Changes/Aider/2023-10-18-show-models-supported-by-api-key-if-requested-model-isn-t-available|Show models supported by api/key if requested model isn't available]]
- Later: 2023-10-27 · Ollama · [[Changes/Ollama/2023-10-27-5-model-support-changes-in-v0-1-6|5 Model Support changes in v0.1.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2023-10-20-aae1f7&body=Card%3A%20Changes%2FOllama%2F2023-10-20-4-model-support-changes-in-v0-1-4.md%0ACard%20ID%3A%20ollama-2023-10-20-aae1f7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.1.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->