---
card_id: ollama-2024-12-04-fb863e
date: '2024-12-04'
description: 'Ollama · 2024-12-04 · Model Support: 3 changes in v0.5.0 — Ollama now
  supports structured outputs, making it possible to constrain a model''s output to
  a…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 695
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a4b7508874ab044328690f8fe96d224374a58d2e94a355ba807fbf8f00fb6260
product: ollama
product_name: Ollama
record:
  card_id: ollama-2024-12-04-fb863e
  comparison: ''
  date: '2024-12-04'
  description: 'Ollama — v0.5.0: 3 Model Support changes'
  evidence:
  - quote: Ollama now supports structured outputs, making it possible to constrain
      a model's output to a specific format defined by a JSON schema. The Ollama Python
      and JavaScript libraries have been updated to support structured outputs, together
      with Ollama's OpenAI-compatible API endpoints.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.5.0
  - quote: Using the [Ollama Python library](https://github.com/ollama/ollama-python),
      pass in the schema as a JSON object to the `format` parameter as either `dict`
      or use Pydantic (recommended) to serialize the schema using `model_json_schema()`.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.5.0
  - quote: 'Note: in the future flash attention will be enabled by default where available,
      with kv cache quantization available on a per-model basis'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.5.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 3-model-support-changes-in-v0-5-0
  source_release: ollama-2024-12-04-v0-5-0-github-189045442-b67e54b1
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v0.5.0
  type: change
related_changes:
- '[[Changes/Ollama/2024-11-28-2-model-support-changes-in-v0-4-6|2 Model Support changes
  in v0.4.6]]'
- '[[Changes/Aider/2024-12-01-pdf-support-for-sonnet-and-gemini-models|PDF support
  for Sonnet and Gemini models]]'
- '[[Changes/Dify/2024-12-03-2-model-support-changes-in-0-13-0|2 Model Support changes
  in 0.13.0]]'
source_release: '[[Releases/Ollama/ollama-2024-12-04-v0-5-0-github-189045442-b67e54b1|ollama-2024-12-04-v0-5-0-github-189045442-b67e54b1]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v0.5.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v0.5.0

**Ollama** · 2024-12-04 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.5.0) · from [[Releases/Ollama/ollama-2024-12-04-v0-5-0-github-189045442-b67e54b1|v0.5.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Ollama now supports structured outputs, making it possible to constrain a model's output to a specific format defined by a JSON schema. The Ollama Python and JavaScript libraries have been updated to support structured outputs, together with Ollama's OpenAI-compatible API endpoints.

> Using the [Ollama Python library](https://github.com/ollama/ollama-python), pass in the schema as a JSON object to the `format` parameter as either `dict` or use Pydantic (recommended) to serialize the schema using `model_json_schema()`.

> Note: in the future flash attention will be enabled by default where available, with kv cache quantization available on a per-model basis

Source: https://github.com/ollama/ollama/releases/tag/v0.5.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2024-12-04-experimental-new-flag-to-set-kv-cache-quantization-to-4-bit-q4-0-8-bit-q8-0-or-1|Experimental: new flag to set KV cache quantization to 4-bit (q4_0), 8-bit…]] · Context Window
- [[Changes/Ollama/2024-12-04-2-reliability-and-performance-changes-in-v0-5-0|2 Reliability and Performance changes in v0.5.0]] · Reliability and Performance
- [[Changes/Ollama/2024-12-04-4-other-changes-in-v0-5-0|4 other changes in v0.5.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2024-12-03 · Dify · [[Changes/Dify/2024-12-03-2-model-support-changes-in-0-13-0|2 Model Support changes in 0.13.0]]
- Later: 2024-12-05 · Dify · [[Changes/Dify/2024-12-05-4-model-support-changes-in-0-13-1|4 Model Support changes in 0.13.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2024-12-04-fb863e&body=Card%3A%20Changes%2FOllama%2F2024-12-04-3-model-support-changes-in-v0-5-0.md%0ACard%20ID%3A%20ollama-2024-12-04-fb863e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.5.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->