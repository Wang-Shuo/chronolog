---
card_id: ollama-2024-07-02-22b89c
date: '2024-07-02'
description: 'Ollama · 2024-07-02 · Reliability and Performance: 5 changes in v0.2.0
  — Ollama can now serve multiple requests at the same time, using only a little bit
  of…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2052
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ad9dfc683fb647f5cfc40c2ddc7a56a20a34af4bf16a55f70faa7e641b2f03cd
product: ollama
product_name: Ollama
record:
  card_id: ollama-2024-07-02-22b89c
  comparison: ''
  date: '2024-07-02'
  description: 'Ollama — v0.2.0: 5 Reliability and Performance changes'
  evidence:
  - quote: 'Ollama can now serve multiple requests at the same time, using only a
      little bit of additional memory for each request. This enables use cases such
      as:'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.2.0
  - quote: 'Retrieval Augmented Generation (RAG): both the embedding and text completion
      models can be loaded into memory simultaneously.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.2.0
  - quote: Models are automatically loaded and unloaded based on requests and how
      much GPU memory is available.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.2.0
  - quote: '[GLM-4](https://ollama.com/library/glm4): A strong multi-lingual general
      language model with competitive performance to Llama 3.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.2.0
  - quote: Ollama will now return an error if the system does not have enough memory
      to run a model on Linux
    source_release: https://github.com/ollama/ollama/releases/tag/v0.2.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 5-reliability-and-performance-changes-in-v0-2-0
  source_release: ollama-2024-07-02-v0-2-0-github-163643882-25f7f395
  source_type: github_releases
  theme: reliability-performance
  title: 5 Reliability and Performance changes in v0.2.0
  type: change
related_changes:
- '[[Changes/Dify/2024-06-14-2-reliability-and-performance-changes-in-0-6-11|2 Reliability
  and Performance changes in 0.6.11]]'
- '[[Changes/Notion/2024-06-18-plus-a-few-more-of-your-top-requests|Plus a few more
  of your top requests.]]'
- '[[Changes/Ollama/2024-06-22-3-reliability-and-performance-changes-in-v0-1-46|3
  Reliability and Performance changes in v0.1.46]]'
source_release: '[[Releases/Ollama/ollama-2024-07-02-v0-2-0-github-163643882-25f7f395|ollama-2024-07-02-v0-2-0-github-163643882-25f7f395]]'
source_type: github_releases
theme: reliability-performance
title: 5 Reliability and Performance changes in v0.2.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Reliability and Performance changes in v0.2.0

**Ollama** · 2024-07-02 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.2.0) · from [[Releases/Ollama/ollama-2024-07-02-v0-2-0-github-163643882-25f7f395|v0.2.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Ollama can now serve multiple requests at the same time, using only a little bit of additional memory for each request. This enables use cases such as:

> Retrieval Augmented Generation (RAG): both the embedding and text completion models can be loaded into memory simultaneously.

> Models are automatically loaded and unloaded based on requests and how much GPU memory is available.

> [GLM-4](https://ollama.com/library/glm4): A strong multi-lingual general language model with competitive performance to Llama 3.

> Ollama will now return an error if the system does not have enough memory to run a model on Linux

Source: https://github.com/ollama/ollama/releases/tag/v0.2.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2024-07-02-6-model-support-changes-in-v0-2-0|6 Model Support changes in v0.2.0]] · Model Support
- [[Changes/Ollama/2024-07-02-2-agent-mode-changes-in-v0-2-0|2 Agent Mode changes in v0.2.0]] · Agent Mode
- [[Changes/Ollama/2024-07-02-2-interface-experience-changes-in-v0-2-0|2 Interface Experience changes in v0.2.0]] · Interface Experience
- [[Changes/Ollama/2024-07-02-processing-different-parts-of-a-document-simultaneously|Processing different parts of a document simultaneously]] · Files and Data
- [[Changes/Ollama/2024-07-02-7-other-changes-in-v0-2-0|7 other changes in v0.2.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2024-06-22 · Ollama · [[Changes/Ollama/2024-06-22-3-reliability-and-performance-changes-in-v0-1-46|3 Reliability and Performance changes in v0.1.46]]
- Later: 2024-07-04 · Aider · [[Changes/Aider/2024-07-04-3-reliability-and-performance-changes-in-v0-42-0|3 Reliability and Performance changes in v0.42.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2024-07-02-22b89c&body=Card%3A%20Changes%2FOllama%2F2024-07-02-5-reliability-and-performance-changes-in-v0-2-0.md%0ACard%20ID%3A%20ollama-2024-07-02-22b89c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.2.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->