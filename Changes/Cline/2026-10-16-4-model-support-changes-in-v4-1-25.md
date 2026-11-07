---
card_id: cline-2026-10-16-513c68
date: '2026-10-16'
description: 'Cline · 2026-10-16 · Model Support: 4 changes in v4.1.25 — With no model
  chosen, the Cline provider now uses Gemini 4 Argon, the new first model in Cline''s…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1376
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 61c811ddfdd5be5cc867ec68b687830ca9242853a3d51026dbc79917396e2bd8
product: cline
product_name: Cline
record:
  card_id: cline-2026-10-16-513c68
  comparison: ''
  date: '2026-10-16'
  description: 'Cline — v4.1.25: 4 Model Support changes'
  evidence:
  - quote: With no model chosen, the Cline provider now uses Gemini 4 Argon, the new
      first model in Cline's recommended list. OpenRouter stays on Claude Sonnet 5.5.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.25
  - quote: Refreshed the model catalog. Adds the Boundless and Standard Compute providers,
      and SambaNova now comes from the catalog with MiniMax M3 as its default. The
      Cline recommended list adds Gemini 4 Argon and drops Grok 4.7, and the Cline
      free list replaces Step 5 Preview with Nemotron 3.5 Super VL. OpenCode Go no
      longer lists MiniMax M2.7. Default models change for Cortecs, CrossModel, Eden
      AI, Google Gemini, GitHub Copilot, Google Vertex AI, LLM Gateway, Ofox, OpenCode
      Go, and Prime Inference (Gemini 4 Argon), Fireworks AI, Nebius Token Factory,
      and Requesty (Muse Spark Open), CoreWeave, DigitalOcean, NanoGPT, and Nvidia
      (Nemotron 3.5 Super VL), Aixy and Neon (Claude Haiku 5.5), Agnes AI, Ambient,
      IteraCompute, Poe, Scaleway, and SenseNova. If you use one of those providers
      without pinning a model, expect a different default.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.25
  - quote: 'Long requests to local models (LM Studio, Ollama) no longer fail after
      5 minutes of silence with `terminated: BodyTimeoutError` while the server is
      still processing a large prompt.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.25
  - quote: Images and files attached to an answer to one of Cline's questions now
      reach the model instead of being dropped.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.25
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 4-model-support-changes-in-v4-1-25
  source_release: cline-2026-10-16-v4-1-25-github-414630227-91f6e52e
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in v4.1.25
  type: change
related_changes:
- '[[Changes/Suno/2026-10-15-shareable-custom-models-to-share-with-your-collaborators-and-riff-on-new-ideas-n|Shareable
  custom models To share with your collaborators and riff on new ideas]]'
- '[[Changes/ChatGPT/2026-10-16-gpt-6-pro-in-the-chat-tab-now-offers|GPT-6 Pro in
  the chat tab now offers]]'
- '[[Changes/Claude Code/2026-10-16-improved-the-message-when-a-background-session-reopened-from-another-folder-has|Improved
  the message when a background session reopened from another folder has no…]]'
source_release: '[[Releases/Cline/cline-2026-10-16-v4-1-25-github-414630227-91f6e52e|cline-2026-10-16-v4-1-25-github-414630227-91f6e52e]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in v4.1.25
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v4.1.25

**Cline** · 2026-10-16 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.25) · from [[Releases/Cline/cline-2026-10-16-v4-1-25-github-414630227-91f6e52e|v4.1.25]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> With no model chosen, the Cline provider now uses Gemini 4 Argon, the new first model in Cline's recommended list. OpenRouter stays on Claude Sonnet 5.5.

> Refreshed the model catalog. Adds the Boundless and Standard Compute providers, and SambaNova now comes from the catalog with MiniMax M3 as its default. The Cline recommended list adds Gemini 4 Argon and drops Grok 4.7, and the Cline free list replaces Step 5 Preview with Nemotron 3.5 Super VL. OpenCode Go no longer lists MiniMax M2.7. Default models change for Cortecs, CrossModel, Eden AI, Google Gemini, GitHub Copilot, Google Vertex AI, LLM Gateway, Ofox, OpenCode Go, and Prime Inference (Gemini 4 Argon), Fireworks AI, Nebius Token Factory, and Requesty (Muse Spark Open), CoreWeave, DigitalOcean, NanoGPT, and Nvidia (Nemotron 3.5 Super VL), Aixy and Neon (Claude Haiku 5.5), Agnes AI, Ambient, IteraCompute, Poe, Scaleway, and SenseNova. If you use one of those providers without pinning a model, expect a different default.

> Long requests to local models (LM Studio, Ollama) no longer fail after 5 minutes of silence with `terminated: BodyTimeoutError` while the server is still processing a large prompt.

> Images and files attached to an answer to one of Cline's questions now reach the model instead of being dropped.

Source: https://github.com/cline/cline/releases/tag/v4.1.25
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-10-16-cline-cloud-sessions-rolling-out-gradually-run-a-task-in-a-hosted-sandbox-on-a-g|Cline Cloud sessions, rolling out gradually]] · Safety and Privacy
- [[Changes/Cline/2026-10-16-auto-compact-and-its-strategy-setting-sit-together-again-in-feature-settings|Auto Compact and its strategy setting sit together again in Feature settings]] · Context Window
- [[Changes/Cline/2026-10-16-3-other-changes-in-v4-1-25|3 other changes in v4.1.25]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-16 · Claude Code · [[Changes/Claude Code/2026-10-16-improved-the-message-when-a-background-session-reopened-from-another-folder-has|Improved the message when a background session reopened from another folder has no…]]
- Later: 2026-10-16 · Open WebUI · [[Changes/Open WebUI/2026-10-16-3-model-support-changes-in-v0-12-3|3 Model Support changes in v0.12.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-10-16-513c68&body=Card%3A%20Changes%2FCline%2F2026-10-16-4-model-support-changes-in-v4-1-25.md%0ACard%20ID%3A%20cline-2026-10-16-513c68%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.25%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->