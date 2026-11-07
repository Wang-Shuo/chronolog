---
card_id: ollama-2026-09-14-463b8a
date: '2026-09-14'
description: 'Ollama · 2026-09-14 · Model Support: 2 changes in v0.34.1 — MLX safetensors
  `ollama create` no longer experimental. GGUF model creation now requires using…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1344
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3410439a486a251c644f22eca5d1eb6df6c9b9fdb0ceca518d605e83a897577d
product: ollama
product_name: Ollama
record:
  card_id: ollama-2026-09-14-463b8a
  comparison: ''
  date: '2026-09-14'
  description: 'Ollama — v0.34.1: 2 Model Support changes'
  evidence:
  - quote: MLX safetensors `ollama create` no longer experimental. GGUF model creation
      now requires using llama.cpp tooling for safetensor conversion and quantization.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.34.1
  - quote: 'Deprecated `typical_p`: it can no longer be set when creating new models,
      existing GGUF models retain support.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.34.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 2-model-support-changes-in-v0-34-1
  source_release: ollama-2026-09-14-v0-34-1-github-388717036-07219146
  source_type: github_releases
  theme: model-support
  title: 2 Model Support changes in v0.34.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-14-2-model-support-changes-in-v2-1-271|2 Model Support
  changes in v2.1.271]]'
- '[[Changes/ElevenLabs/2026-09-14-javascript-sdk|JavaScript SDK]]'
- '[[Changes/ElevenLabs/2026-09-14-python-sdk|Python SDK]]'
source_release: '[[Releases/Ollama/ollama-2026-09-14-v0-34-1-github-388717036-07219146|ollama-2026-09-14-v0-34-1-github-388717036-07219146]]'
source_type: github_releases
theme: model-support
title: 2 Model Support changes in v0.34.1
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Model Support changes in v0.34.1

**Ollama** · 2026-09-14 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.34.1) · from [[Releases/Ollama/ollama-2026-09-14-v0-34-1-github-388717036-07219146|v0.34.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> MLX safetensors `ollama create` no longer experimental. GGUF model creation now requires using llama.cpp tooling for safetensor conversion and quantization.

> Deprecated `typical_p`: it can no longer be set when creating new models, existing GGUF models retain support.

Source: https://github.com/ollama/ollama/releases/tag/v0.34.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2026-09-14-2-reliability-and-performance-changes-in-v0-34-1|2 Reliability and Performance changes in v0.34.1]] · Reliability and Performance
- [[Changes/Ollama/2026-09-14-runaway-repeat-token-detection-now-requires-100-repeat-tokens-for-reduced-false|Runaway repeat token detection now requires 100 repeat tokens for reduced false…]] · Context Window
- [[Changes/Ollama/2026-09-14-mlx-and-llama-cpp-updates|MLX and llama.cpp updates]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-14 · ElevenLabs · [[Changes/ElevenLabs/2026-09-14-python-sdk|Python SDK]]
- Later: 2026-09-14 · OpenCode · [[Changes/OpenCode/2026-09-14-request-summarized-adaptive-thinking-for-github-copilot-models|Request summarized adaptive thinking for GitHub Copilot models]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2026-09-14-463b8a&body=Card%3A%20Changes%2FOllama%2F2026-09-14-2-model-support-changes-in-v0-34-1.md%0ACard%20ID%3A%20ollama-2026-09-14-463b8a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.34.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->