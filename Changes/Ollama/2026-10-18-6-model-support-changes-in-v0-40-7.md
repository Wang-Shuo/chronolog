---
card_id: ollama-2026-10-18-f80746
date: '2026-10-18'
description: 'Ollama · 2026-10-18 · Model Support: 6 changes in v0.40.7 — [pplx-decider](https://ollama.com/library/pplx-decider)
  is a 27B decision model from Perplexity…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1378
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6c02d78c6c0c635c777d4f61b3e432072ea9535a53698ca32c8b68d350738524
product: ollama
product_name: Ollama
record:
  card_id: ollama-2026-10-18-f80746
  comparison: ''
  date: '2026-10-18'
  description: 'Ollama — v0.40.7: 6 Model Support changes'
  evidence:
  - quote: '[pplx-decider](https://ollama.com/library/pplx-decider) is a 27B decision
      model from Perplexity, fine-tuned from'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.40.7
  - quote: Continuing an OpenAI-compatible Responses conversation no longer fails
      when switching between models with and without
    source_release: https://github.com/ollama/ollama/releases/tag/v0.40.7
  - quote: reasoning items, producing misordered/duplicate tool call events
    source_release: https://github.com/ollama/ollama/releases/tag/v0.40.7
  - quote: Requests routed to remote models are now cancelled on ollama.com when the
      client disconnects, instead of continuing
    source_release: https://github.com/ollama/ollama/releases/tag/v0.40.7
  - quote: '`ollama show` now reports which renderer and parser a model uses and where
      its chat template comes from; the API'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.40.7
  - quote: 'More draft models now work with speculative decoding: llama-server infers
      the draft type automatically instead of'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.40.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 6-model-support-changes-in-v0-40-7
  source_release: ollama-2026-10-18-v0-40-7-github-416126438-e146c3e4
  source_type: github_releases
  theme: model-support
  title: 6 Model Support changes in v0.40.7
  type: change
related_changes:
- '[[Changes/Replit/2026-10-16-claude-haiku-5-5-in-the-model-selector|Claude Haiku
  5.5 in the model selector]]'
- '[[Changes/v0/2026-10-16-gemini-4-requests-no-longer-fail-when-run-at-higher-effort-levels|Gemini
  4 requests no longer fail when run at higher effort levels]]'
- '[[Changes/DeepSeek API/2026-10-17-deepseek-v4-1-flash-1017-update|DeepSeek-V4.1-Flash-1017
  Update]]'
source_release: '[[Releases/Ollama/ollama-2026-10-18-v0-40-7-github-416126438-e146c3e4|ollama-2026-10-18-v0-40-7-github-416126438-e146c3e4]]'
source_type: github_releases
theme: model-support
title: 6 Model Support changes in v0.40.7
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in v0.40.7

**Ollama** · 2026-10-18 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.40.7) · from [[Releases/Ollama/ollama-2026-10-18-v0-40-7-github-416126438-e146c3e4|v0.40.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> [pplx-decider](https://ollama.com/library/pplx-decider) is a 27B decision model from Perplexity, fine-tuned from

> Continuing an OpenAI-compatible Responses conversation no longer fails when switching between models with and without

> reasoning items, producing misordered/duplicate tool call events

> Requests routed to remote models are now cancelled on ollama.com when the client disconnects, instead of continuing

> `ollama show` now reports which renderer and parser a model uses and where its chat template comes from; the API

> More draft models now work with speculative decoding: llama-server infers the draft type automatically instead of

Source: https://github.com/ollama/ollama/releases/tag/v0.40.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2026-10-18-2-context-window-changes-in-v0-40-7|2 Context Window changes in v0.40.7]] · Context Window
- [[Changes/Ollama/2026-10-18-4-other-changes-in-v0-40-7|4 other changes in v0.40.7]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-17 · DeepSeek API · [[Changes/DeepSeek API/2026-10-17-deepseek-v4-1-flash-1017-update|DeepSeek-V4.1-Flash-1017 Update]]
- Later: 2026-10-18 · OpenClaw · [[Changes/OpenClaw/2026-10-18-4-model-support-changes-in-v2026-10-5|4 Model Support changes in v2026.10.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2026-10-18-f80746&body=Card%3A%20Changes%2FOllama%2F2026-10-18-6-model-support-changes-in-v0-40-7.md%0ACard%20ID%3A%20ollama-2026-10-18-f80746%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.40.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->