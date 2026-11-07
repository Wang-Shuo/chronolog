---
card_id: ollama-2024-01-20-7ee973
date: '2024-01-20'
description: 'Ollama · 2024-01-20 · Model Support: 8 changes in v0.1.21 — [Qwen](https://ollama.ai/library/qwen):
  Qwen is a series of large language models by Alibaba Cloud…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 376
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 679f4fac237e09369bec068661d8fbcfa56e2d1953609cc12605dfc4c7b487a3
product: ollama
product_name: Ollama
record:
  card_id: ollama-2024-01-20-7ee973
  comparison: ''
  date: '2024-01-20'
  description: 'Ollama — v0.1.21: 8 Model Support changes'
  evidence:
  - quote: '[Qwen](https://ollama.ai/library/qwen): Qwen is a series of large language
      models by Alibaba Cloud spanning from 1.8B to 72B parameters.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.21
  - quote: '[DuckDB-NSQL](https://ollama.ai/library/duckdb-nsql): A text-to-sql LLM
      for DuckDB'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.21
  - quote: '[Stable Code](https://ollama.ai/library/stable-code): A new code completion
      model on par with Code Llama 7B and similar models.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.21
  - quote: '[Nous Hermes 2 Mixtral](https://ollama.ai/library/nous-hermes2-mixtral):
      The Nous Hermes 2 model from Nous Research, now trained over Mixtral.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.21
  - quote: Models can now be saved and loaded with `/save <model>` and `/load <model>`
      when using `ollama run`. This will save or load conversations and any model
      changes with `/set parameter`, `/set system` and more as a new model with the
      provided name.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.21
  - quote: After creating this model, running it will restore the message history.
      This is useful for techniques such as [Chain-Of-Thought](https://www.promptingguide.ai/techniques/cot)
      prompting
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.21
  - quote: If a GPU detection error is hit when attempting to run a model, Ollama
      will fallback to CPU
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.21
  - quote: New `MESSAGE` Modelfile command to set the conversation history when building
      a model
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.21
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 8-model-support-changes-in-v0-1-21
  source_release: ollama-2024-01-20-v0-1-21-github-137801319-d665d0af
  source_type: github_releases
  theme: model-support
  title: 8 Model Support changes in v0.1.21
  type: change
related_changes:
- '[[Changes/Dify/2024-01-17-5-model-support-changes-in-0-4-8|5 Model Support changes
  in 0.4.8]]'
- '[[Changes/Cursor/2024-01-18-cursor-fast-this-is-a-new-model-available-in-command-k-and-chat-expect-it-to-be|"cursor-fast":
  This is a new model available in command-k and chat]]'
- '[[Changes/Dify/2024-01-19-add-jina-embeddings-v2-base-de-model-configuration-by-joshua20231026-in-https-gi|Add
  jina-embeddings-v2-base-de model configuration]]'
source_release: '[[Releases/Ollama/ollama-2024-01-20-v0-1-21-github-137801319-d665d0af|ollama-2024-01-20-v0-1-21-github-137801319-d665d0af]]'
source_type: github_releases
theme: model-support
title: 8 Model Support changes in v0.1.21
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Model Support changes in v0.1.21

**Ollama** · 2024-01-20 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.1.21) · from [[Releases/Ollama/ollama-2024-01-20-v0-1-21-github-137801319-d665d0af|v0.1.21]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> [Qwen](https://ollama.ai/library/qwen): Qwen is a series of large language models by Alibaba Cloud spanning from 1.8B to 72B parameters.

> [DuckDB-NSQL](https://ollama.ai/library/duckdb-nsql): A text-to-sql LLM for DuckDB

> [Stable Code](https://ollama.ai/library/stable-code): A new code completion model on par with Code Llama 7B and similar models.

> [Nous Hermes 2 Mixtral](https://ollama.ai/library/nous-hermes2-mixtral): The Nous Hermes 2 model from Nous Research, now trained over Mixtral.

> Models can now be saved and loaded with `/save <model>` and `/load <model>` when using `ollama run`. This will save or load conversations and any model changes with `/set parameter`, `/set system` and more as a new model with the provided name.

> After creating this model, running it will restore the message history. This is useful for techniques such as [Chain-Of-Thought](https://www.promptingguide.ai/techniques/cot) prompting

> If a GPU detection error is hit when attempting to run a model, Ollama will fallback to CPU

> New `MESSAGE` Modelfile command to set the conversation history when building a model

Source: https://github.com/ollama/ollama/releases/tag/v0.1.21
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2024-01-20-2-developer-workflow-changes-in-v0-1-21|2 Developer Workflow changes in v0.1.21]] · Developer Workflow
- [[Changes/Ollama/2024-01-20-2-reliability-and-performance-changes-in-v0-1-21|2 Reliability and Performance changes in v0.1.21]] · Reliability and Performance
- [[Changes/Ollama/2024-01-20-2-other-changes-in-v0-1-21|2 other changes in v0.1.21]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2024-01-19 · Dify · [[Changes/Dify/2024-01-19-add-jina-embeddings-v2-base-de-model-configuration-by-joshua20231026-in-https-gi|Add jina-embeddings-v2-base-de model configuration]]
- Later: 2024-01-24 · Dify · [[Changes/Dify/2024-01-24-4-model-support-changes-in-0-5-0|4 Model Support changes in 0.5.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2024-01-20-7ee973&body=Card%3A%20Changes%2FOllama%2F2024-01-20-8-model-support-changes-in-v0-1-21.md%0ACard%20ID%3A%20ollama-2024-01-20-7ee973%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.1.21%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->