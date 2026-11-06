---
card_id: ollama-2025-08-05-be983f
date: '2025-08-05'
description: 'Ollama · 2025-08-05 · Reliability and Performance: 2 changes in v0.11.0
  — **Configurable reasoning effort:** Easily adjust the reasoning effort (low, medium…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 964
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 28b7929a0b485f6584d3203bfd7dbc699396792a1d1326f8c731bc37f951b9e1
product: ollama
product_name: Ollama
record:
  card_id: ollama-2025-08-05-be983f
  comparison: ''
  date: '2025-08-05'
  description: 'Ollama — v0.11.0: 2 Reliability and Performance changes'
  evidence:
  - quote: '**Configurable reasoning effort:** Easily adjust the reasoning effort
      (low, medium, high) based on your specific use case and latency needs.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.11.0
  - quote: OpenAI utilizes quantization to reduce the memory footprint of the gpt-oss
      models. The models are post-trained with quantization of the mixture-of-experts
      (MoE) weights to MXFP4 format, where the weights are quantized to 4.25 bits
      per parameter. The MoE weights are responsible for 90+% of the total parameter
      count, and quantizing these to MXFP4 enables the smaller model to run on systems
      with as little as 16GB memory, and the larger model to fit on a single 80GB
      GPU.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 2-reliability-and-performance-changes-in-v0-11-0
  source_release: ollama-2025-08-05-v0-11-0-github-237715736-1e21e755
  source_type: github_releases
  theme: reliability-performance
  title: 2 Reliability and Performance changes in v0.11.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-07-30-run-model-availability-check-in-the-background-to-speed-up-startup-by-sandytao52|Run
  model availability check in the background to speed up startup]]'
- '[[Changes/Gemini CLI/2025-08-02-2-reliability-and-performance-changes-in-v0-1-16|2
  Reliability and Performance changes in v0.1.16]]'
- '[[Changes/Gemini CLI/2025-08-05-2-reliability-and-performance-changes-in-v0-1-17|2
  Reliability and Performance changes in v0.1.17]]'
source_release: '[[Releases/Ollama/ollama-2025-08-05-v0-11-0-github-237715736-1e21e755|ollama-2025-08-05-v0-11-0-github-237715736-1e21e755]]'
source_type: github_releases
theme: reliability-performance
title: 2 Reliability and Performance changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Reliability and Performance changes in v0.11.0

**Ollama** · 2025-08-05 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.11.0) · from [[Releases/Ollama/ollama-2025-08-05-v0-11-0-github-237715736-1e21e755|v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Configurable reasoning effort:** Easily adjust the reasoning effort (low, medium, high) based on your specific use case and latency needs.

> OpenAI utilizes quantization to reduce the memory footprint of the gpt-oss models. The models are post-trained with quantization of the mixture-of-experts (MoE) weights to MXFP4 format, where the weights are quantized to 4.25 bits per parameter. The MoE weights are responsible for 90+% of the total parameter count, and quantizing these to MXFP4 enables the smaller model to run on systems with as little as 16GB memory, and the larger model to fit on a single 80GB GPU.

Source: https://github.com/ollama/ollama/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2025-08-05-the-model-can-be-downloaded-directly-in-ollama-s-new-app-or-via-the-terminal|The model can be downloaded directly in Ollama’s new app or via the terminal]] · Developer Workflow
- [[Changes/Ollama/2025-08-05-3-model-support-changes-in-v0-11-0|3 Model Support changes in v0.11.0]] · Model Support
- [[Changes/Ollama/2025-08-05-agentic-capabilities-use-the-models-native-capabilities-for-function-calling-web|Agentic capabilities: Use the models’ native capabilities for function calling…]] · Search and Browsing
- [[Changes/Ollama/2025-08-05-7-other-changes-in-v0-11-0|7 other changes in v0.11.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2025-08-05 · Gemini CLI · [[Changes/Gemini CLI/2025-08-05-2-reliability-and-performance-changes-in-v0-1-17|2 Reliability and Performance changes in v0.1.17]]
- Later: 2025-08-06 · Cursor · [[Changes/Cursor/2025-08-06-1-4-5-improved-performance|1.4.5: Improved performance]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2025-08-05-be983f&body=Card%3A%20Changes%2FOllama%2F2025-08-05-2-reliability-and-performance-changes-in-v0-11-0.md%0ACard%20ID%3A%20ollama-2025-08-05-be983f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->