---
card_id: ollama-2026-09-29-5d54a2
date: '2026-09-29'
description: 'Ollama · 2026-09-29 · Model Support: 3 changes in v0.35.1 — Ollama now
  supports [Clef](https://ollama.com/library/clef) and [Clef…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1359
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2cb31a11a960927440b9d7dc66c21364b15eba3e06ab22bfe6bee18d7f13bcf3
product: ollama
product_name: Ollama
record:
  card_id: ollama-2026-09-29-5d54a2
  comparison: ''
  date: '2026-09-29'
  description: 'Ollama — v0.35.1: 3 Model Support changes'
  evidence:
  - quote: Ollama now supports [Clef](https://ollama.com/library/clef) and [Clef Flash](https://ollama.com/library/clef),
      Cloudflare's new open-source decision models, through `/v1/systemone`.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.35.1
  - quote: Modelfiles now support `CAPABILITY` declarations, so model creators can
      explicitly declare what a model can do. Declarations are preserved when creating
      from GGUF or safetensors, through model inheritance, and on Modelfile export
    source_release: https://github.com/ollama/ollama/releases/tag/v0.35.1
  - quote: '`ollama show` and the model list now report only `decision` as the capability
      for decision models, so clients no longer offer them for general chat, tools,
      or thinking'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.35.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 3-model-support-changes-in-v0-35-1
  source_release: ollama-2026-09-29-v0-35-1-github-399431834-a0bca098
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v0.35.1
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-29-3-model-support-changes-in-rust-v0-159-0|3 Model
  Support changes in rust-v0.159.0]]'
- '[[Changes/Codex CLI/2026-09-29-2-model-support-changes-in-rust-v0-159-1|2 Model
  Support changes in rust-v0.159.1]]'
- '[[Changes/Gemini CLI/2026-09-29-feat-gemini-3-8-flash-3-5-flash-lite-by-davidapierce-in-https-github-com-google|Feat/gemini
  3.8 flash 3.5 flash lite]]'
source_release: '[[Releases/Ollama/ollama-2026-09-29-v0-35-1-github-399431834-a0bca098|ollama-2026-09-29-v0-35-1-github-399431834-a0bca098]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v0.35.1
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v0.35.1

**Ollama** · 2026-09-29 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.35.1) · from [[Releases/Ollama/ollama-2026-09-29-v0-35-1-github-399431834-a0bca098|v0.35.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Ollama now supports [Clef](https://ollama.com/library/clef) and [Clef Flash](https://ollama.com/library/clef), Cloudflare's new open-source decision models, through `/v1/systemone`.

> Modelfiles now support `CAPABILITY` declarations, so model creators can explicitly declare what a model can do. Declarations are preserved when creating from GGUF or safetensors, through model inheritance, and on Modelfile export

> `ollama show` and the model list now report only `decision` as the capability for decision models, so clients no longer offer them for general chat, tools, or thinking

Source: https://github.com/ollama/ollama/releases/tag/v0.35.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2026-09-29-models-using-web-search-can-now-perform-up-to-ten-searches-per-response-up-from|Models using web search can now perform up to ten searches per response, up from three]] · Search and Browsing
- [[Changes/Ollama/2026-09-29-clef-27b-and-clef-flash-9b-are-multimodal-requests-can-now-include-images-alongs|Clef (27B) and Clef Flash (9B) are multimodal]] · Multimodal Input
- [[Changes/Ollama/2026-09-29-updated-llama-cpp-and-the-mlx-engine|Updated llama.cpp and the MLX engine]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-29 · Gemini CLI · [[Changes/Gemini CLI/2026-09-29-feat-gemini-3-8-flash-3-5-flash-lite-by-davidapierce-in-https-github-com-google|Feat/gemini 3.8 flash 3.5 flash lite]]
- Later: 2026-09-29 · v0 · [[Changes/v0/2026-09-29-what-counts-towards-chatgpt-usage|What counts towards ChatGPT usage?]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2026-09-29-5d54a2&body=Card%3A%20Changes%2FOllama%2F2026-09-29-3-model-support-changes-in-v0-35-1.md%0ACard%20ID%3A%20ollama-2026-09-29-5d54a2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.35.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->