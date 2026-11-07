---
card_id: ollama-2024-05-10-69a307
date: '2024-05-10'
description: 'Ollama · 2024-05-10 · Model Support: 5 changes in v0.1.35 — [Llama 3
  ChatQA](https://ollama.com/library/llama3-chatqa): A model from NVIDIA based on
  Llama 3…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 487
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5bee5e07d63a66e8c808225a4f1bba5d5ac2005a9e68888ad7ac3b9c9118afbe
product: ollama
product_name: Ollama
record:
  card_id: ollama-2024-05-10-69a307
  comparison: ''
  date: '2024-05-10'
  description: 'Ollama — v0.1.35: 5 Model Support changes'
  evidence:
  - quote: '[Llama 3 ChatQA](https://ollama.com/library/llama3-chatqa): A model from
      NVIDIA based on Llama 3 that excels at conversational question answering (QA)
      and retrieval-augmented generation (RAG).'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.35
  - quote: 'Quantization: `ollama create` can now quantize models when importing them
      using the `--quantize` or `-q` flag:'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.35
  - quote: '> `--quantize` works when importing `float16` or `float32` models:'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.35
  - quote: '> * From a binary GGUF files (e.g. `FROM ./model.gguf`)'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.35
  - quote: '> * From a library model (e.g. `FROM llama3:8b-instruct-fp16`)'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.35
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 5-model-support-changes-in-v0-1-35
  source_release: ollama-2024-05-10-v0-1-35-github-155045759-efae2ff7
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in v0.1.35
  type: change
related_changes:
- '[[Changes/Open WebUI/2024-05-08-2-model-support-changes-in-v0-1-124|2 Model Support
  changes in v0.1.124]]'
- '[[Changes/Dify/2024-05-09-11-model-support-changes-in-0-6-7|11 Model Support changes
  in 0.6.7]]'
- '[[Changes/Aider/2024-05-10-added-explicit-model-settings-for-openrouter-anthropic-claude-3-opus-gpt-3-5-tur|Added
  explicit model settings for openrouter/anthropic/claude-3-opus, gpt-3.5-turbo]]'
source_release: '[[Releases/Ollama/ollama-2024-05-10-v0-1-35-github-155045759-efae2ff7|ollama-2024-05-10-v0-1-35-github-155045759-efae2ff7]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in v0.1.35
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in v0.1.35

**Ollama** · 2024-05-10 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.1.35) · from [[Releases/Ollama/ollama-2024-05-10-v0-1-35-github-155045759-efae2ff7|v0.1.35]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> [Llama 3 ChatQA](https://ollama.com/library/llama3-chatqa): A model from NVIDIA based on Llama 3 that excels at conversational question answering (QA) and retrieval-augmented generation (RAG).

> Quantization: `ollama create` can now quantize models when importing them using the `--quantize` or `-q` flag:

> > `--quantize` works when importing `float16` or `float32` models:

> > * From a binary GGUF files (e.g. `FROM ./model.gguf`)

> > * From a library model (e.g. `FROM llama3:8b-instruct-fp16`)

Source: https://github.com/ollama/ollama/releases/tag/v0.1.35
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2024-05-10-ollama-will-now-more-accurately-estimate-how-much-memory-is-available-on-multi-g|Ollama will now more accurately estimate how much memory is available on multi-GPU…]] · Reliability and Performance
- [[Changes/Ollama/2024-05-10-3-other-changes-in-v0-1-35|3 other changes in v0.1.35]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2024-05-10 · Aider · [[Changes/Aider/2024-05-10-added-explicit-model-settings-for-openrouter-anthropic-claude-3-opus-gpt-3-5-tur|Added explicit model settings for openrouter/anthropic/claude-3-opus, gpt-3.5-turbo]]
- Later: 2024-05-13 · Aider · [[Changes/Aider/2024-05-13-3-model-support-changes-in-v0-35-0|3 Model Support changes in v0.35.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2024-05-10-69a307&body=Card%3A%20Changes%2FOllama%2F2024-05-10-5-model-support-changes-in-v0-1-35.md%0ACard%20ID%3A%20ollama-2024-05-10-69a307%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.1.35%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->