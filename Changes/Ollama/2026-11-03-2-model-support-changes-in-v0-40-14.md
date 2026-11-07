---
card_id: ollama-2026-11-03-eacb3d
date: '2026-11-03'
description: 'Ollama · 2026-11-03 · Model Support: 2 changes in v0.40.14 — `ollama
  launch claude` now applies the model''s output token limit for Claude Code, so cloud
  models…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1394
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ffc4edee27927e84638afa9fb48697578cca3a56a4133949c75a727a18a523c9
product: ollama
product_name: Ollama
record:
  card_id: ollama-2026-11-03-eacb3d
  comparison: ''
  date: '2026-11-03'
  description: 'Ollama — v0.40.14: 2 Model Support changes'
  evidence:
  - quote: '`ollama launch claude` now applies the model''s output token limit for
      Claude Code, so cloud models no longer run into the 128k default cap'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.40.14
  - quote: OpenAI-compatible endpoints no longer override a model's packaged sampler
      defaults — clients that send no `temperature`/`top_p` get the model's own values
      instead of 1.0, matching `/api/chat`
    source_release: https://github.com/ollama/ollama/releases/tag/v0.40.14
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 2-model-support-changes-in-v0-40-14
  source_release: ollama-2026-11-03-v0-40-14-github-432169781-b3886e93
  source_type: github_releases
  theme: model-support
  title: 2 Model Support changes in v0.40.14
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-11-02-7-model-support-changes-in-elevenlabs-updates-2026-11-02|7
  Model Support changes in ElevenLabs updates — 2026-11-02]]'
- '[[Changes/Google Antigravity/2026-11-03-voice-mode-enabled-by-gemini-live-lets-you-talk-to-antigravity-and-hand-requests|Voice
  mode, enabled by Gemini Live, lets you talk to Antigravity and hand requests…]]'
- '[[Changes/Ollama/2026-11-03-2-model-support-changes-in-v0-40-15|2 Model Support
  changes in v0.40.15]]'
source_release: '[[Releases/Ollama/ollama-2026-11-03-v0-40-14-github-432169781-b3886e93|ollama-2026-11-03-v0-40-14-github-432169781-b3886e93]]'
source_type: github_releases
theme: model-support
title: 2 Model Support changes in v0.40.14
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Model Support changes in v0.40.14

**Ollama** · 2026-11-03 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.40.14) · from [[Releases/Ollama/ollama-2026-11-03-v0-40-14-github-432169781-b3886e93|v0.40.14]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `ollama launch claude` now applies the model's output token limit for Claude Code, so cloud models no longer run into the 128k default cap

> OpenAI-compatible endpoints no longer override a model's packaged sampler defaults — clients that send no `temperature`/`top_p` get the model's own values instead of 1.0, matching `/api/chat`

Source: https://github.com/ollama/ollama/releases/tag/v0.40.14
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2026-11-03-cloud-web-search-responses-on-api-chat-are-now-decoded-correctly-including-compr|Cloud web search responses on /api/chat are now decoded correctly, including…]] · Search and Browsing
- [[Changes/Ollama/2026-11-03-faster-top-k-sampling-on-mlx-for-large-vocabularies|Faster top-k sampling on MLX for large vocabularies]] · Reliability and Performance
- [[Changes/Ollama/2026-11-03-3-other-changes-in-v0-40-14|3 other changes in v0.40.14]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-11-03 · Ollama · [[Changes/Ollama/2026-11-03-2-model-support-changes-in-v0-40-15|2 Model Support changes in v0.40.15]]
- Later: 2026-11-03 · Open WebUI · [[Changes/Open WebUI/2026-11-03-4-model-support-changes-in-v0-13-0|4 Model Support changes in v0.13.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2026-11-03-eacb3d&body=Card%3A%20Changes%2FOllama%2F2026-11-03-2-model-support-changes-in-v0-40-14.md%0ACard%20ID%3A%20ollama-2026-11-03-eacb3d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.40.14%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->