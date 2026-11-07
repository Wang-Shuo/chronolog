---
card_id: ollama-2024-10-11-98a9b1
date: '2024-10-11'
description: 'Ollama · 2024-10-11 · Model Support: 4 changes in v0.3.13 — [Llama Guard
  3](https://ollama.com/library/llama-guard3): a series of models by Meta, fine-tuned…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 641
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8dccca9d742f0dff76439d3b1e792ae90a1acaa9912ae1696fcca2d1614d1455
product: ollama
product_name: Ollama
record:
  card_id: ollama-2024-10-11-98a9b1
  comparison: ''
  date: '2024-10-11'
  description: 'Ollama — v0.3.13: 4 Model Support changes'
  evidence:
  - quote: '[Llama Guard 3](https://ollama.com/library/llama-guard3): a series of
      models by Meta, fine-tuned for content safety classification of LLM inputs and
      responses.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.3.13
  - quote: Default model in quickstart is now `llama3.2`
    source_release: https://github.com/ollama/ollama/releases/tag/v0.3.13
  - quote: '`ollama rm` will now stop a model if it is running prior to deleting it'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.3.13
  - quote: Ollama is transitioning to a new Go-based subprocess model runner with
      improved reliability and caching. This new runner found under the `llama` directory
      replaces the previous code under `llm/ext_server`. During this transition period,
      the new Go runner is opt-in at build time, and requires using a different approach
      to build. For more information see [development.md](https://github.com/ollama/ollama/blob/main/docs/development.md).
    source_release: https://github.com/ollama/ollama/releases/tag/v0.3.13
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 4-model-support-changes-in-v0-3-13
  source_release: ollama-2024-10-11-v0-3-13-github-179444955-6d78c25a
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in v0.3.13
  type: change
related_changes:
- '[[Changes/Raycast/2024-10-09-quick-ai-regenerating-after-changing-the-model-should-now-utilize-the-new-model|Quick
  AI: Regenerating after changing the model should now utilize the new model]]'
- '[[Changes/Superwhisper/2024-10-09-removed-realtime-option-for-offline-models-this-is-currently-a-wip-stay-tuned|Removed
  realtime option for offline models (this is currently a WIP, stay tuned)]]'
- '[[Changes/Superwhisper/2024-10-09-history-speakers-separation|History & Speakers
  separation]]'
source_release: '[[Releases/Ollama/ollama-2024-10-11-v0-3-13-github-179444955-6d78c25a|ollama-2024-10-11-v0-3-13-github-179444955-6d78c25a]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in v0.3.13
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v0.3.13

**Ollama** · 2024-10-11 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.3.13) · from [[Releases/Ollama/ollama-2024-10-11-v0-3-13-github-179444955-6d78c25a|v0.3.13]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> [Llama Guard 3](https://ollama.com/library/llama-guard3): a series of models by Meta, fine-tuned for content safety classification of LLM inputs and responses.

> Default model in quickstart is now `llama3.2`

> `ollama rm` will now stop a model if it is running prior to deleting it

> Ollama is transitioning to a new Go-based subprocess model runner with improved reliability and caching. This new runner found under the `llama` directory replaces the previous code under `llm/ext_server`. During this transition period, the new Go runner is opt-in at build time, and requires using a different approach to build. For more information see [development.md](https://github.com/ollama/ollama/blob/main/docs/development.md).

Source: https://github.com/ollama/ollama/releases/tag/v0.3.13
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2024-10-11-2-other-changes-in-v0-3-13|2 other changes in v0.3.13]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2024-10-09 · Superwhisper · [[Changes/Superwhisper/2024-10-09-history-speakers-separation|History & Speakers separation]]
- Later: 2024-10-13 · ElevenLabs · [[Changes/ElevenLabs/2024-10-13-model|Model]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2024-10-11-98a9b1&body=Card%3A%20Changes%2FOllama%2F2024-10-11-4-model-support-changes-in-v0-3-13.md%0ACard%20ID%3A%20ollama-2024-10-11-98a9b1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.3.13%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->