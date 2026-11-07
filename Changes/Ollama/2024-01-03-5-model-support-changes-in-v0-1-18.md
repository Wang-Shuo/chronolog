---
card_id: ollama-2024-01-03-d5b0f4
date: '2024-01-03'
description: 'Ollama · 2024-01-03 · Model Support: 5 changes in v0.1.18 — [TinyLlama](https://ollama.ai/library/tinyllama):
  a compact 1.1B Llama model on 3 trillion tokens'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 359
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 24cfb8d270a2f34923656d31873fa9859dec44b2be8a36452e6d0d1b4c175c2d
product: ollama
product_name: Ollama
record:
  card_id: ollama-2024-01-03-d5b0f4
  comparison: ''
  date: '2024-01-03'
  description: 'Ollama — v0.1.18: 5 Model Support changes'
  evidence:
  - quote: '[TinyLlama](https://ollama.ai/library/tinyllama): a compact 1.1B Llama
      model on 3 trillion tokens'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.18
  - quote: '[OpenHermes 2](https://ollama.ai/library/openhermes): A 7B model, fine-tuned
      on Mistral with strong multi-turn chat skills and system prompt capabilities.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.18
  - quote: '[WizardCoder 33B](https://ollama.ai/library/wizardcoder): a new 33B state
      of the art code generation model: `ollama run wizardcoder:33b`'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.18
  - quote: '[Dolphin Phi](https://ollama.ai/library/dolphin-phi): a 2.7B uncensored
      model, based on the Phi language model by Microsoft Research'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.18
  - quote: Ollama will now automatically pull new models when running older `ggml`
      format models. If using custom `ggml` format models in a `Modelfile`, please
      [import GGUF](https://github.com/jmorganca/ollama/blob/main/docs/import.md)
      models instead.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.18
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 5-model-support-changes-in-v0-1-18
  source_release: ollama-2024-01-03-v0-1-18-github-134950093-b924051a
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in v0.1.18
  type: change
related_changes:
- '[[Changes/Ollama/2023-12-19-6-model-support-changes-in-v0-1-17|6 Model Support
  changes in v0.1.17]]'
- '[[Changes/Aider/2023-12-20-3-model-support-changes-in-v0-19-0|3 Model Support changes
  in v0.19.0]]'
- '[[Changes/Dify/2024-01-02-11-model-support-changes-in-0-4-0|11 Model Support changes
  in 0.4.0]]'
source_release: '[[Releases/Ollama/ollama-2024-01-03-v0-1-18-github-134950093-b924051a|ollama-2024-01-03-v0-1-18-github-134950093-b924051a]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in v0.1.18
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in v0.1.18

**Ollama** · 2024-01-03 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.1.18) · from [[Releases/Ollama/ollama-2024-01-03-v0-1-18-github-134950093-b924051a|v0.1.18]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> [TinyLlama](https://ollama.ai/library/tinyllama): a compact 1.1B Llama model on 3 trillion tokens

> [OpenHermes 2](https://ollama.ai/library/openhermes): A 7B model, fine-tuned on Mistral with strong multi-turn chat skills and system prompt capabilities.

> [WizardCoder 33B](https://ollama.ai/library/wizardcoder): a new 33B state of the art code generation model: `ollama run wizardcoder:33b`

> [Dolphin Phi](https://ollama.ai/library/dolphin-phi): a 2.7B uncensored model, based on the Phi language model by Microsoft Research

> Ollama will now automatically pull new models when running older `ggml` format models. If using custom `ggml` format models in a `Modelfile`, please [import GGUF](https://github.com/jmorganca/ollama/blob/main/docs/import.md) models instead.

Source: https://github.com/ollama/ollama/releases/tag/v0.1.18
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2024-01-03-improved-performance-when-sending-follow-up-messages-in-ollama-run-or-via-the-ap|Improved performance when sending follow up messages in ollama run or via the API]] · Reliability and Performance
- [[Changes/Ollama/2024-01-03-added-shortcuts-help-command-to-ollama-run-to-list-keyboard-shortcuts|Added /? shortcuts help command to ollama run to list keyboard shortcuts]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2024-01-02 · Dify · [[Changes/Dify/2024-01-02-11-model-support-changes-in-0-4-0|11 Model Support changes in 0.4.0]]
- Later: 2024-01-04 · Aider · [[Changes/Aider/2024-01-04-add-images-to-the-chat-to-automatically-use-gpt-4-vision-by-joshuavial|Add images to the chat to automatically use GPT-4 Vision, by @joshuavial]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2024-01-03-d5b0f4&body=Card%3A%20Changes%2FOllama%2F2024-01-03-5-model-support-changes-in-v0-1-18.md%0ACard%20ID%3A%20ollama-2024-01-03-d5b0f4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.1.18%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->