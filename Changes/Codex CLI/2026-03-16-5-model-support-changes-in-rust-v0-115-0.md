---
card_id: codex-cli-2026-03-16-d3360c
date: '2026-03-16'
description: 'Codex CLI · 2026-03-16 · Model Support: 5 changes in 0.115.0 — Supported
  models can now request full-resolution image inspection through both `view_image`
  and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1162
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1b7f81e33f57bee9905722ee79bfb982c595b9e7bf7e80b136205f3074caec1d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-16-d3360c
  comparison: ''
  date: '2026-03-16'
  description: 'Codex CLI — 0.115.0: 5 Model Support changes'
  evidence:
  - quote: 'Supported models can now request full-resolution image inspection through
      both `view_image` and `codex.emitImage(..., detail: "original")`, which helps
      with precision visual tasks. (#14175)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: 'App integrations now use the Responses API tool-search flow, can suggest
      missing tools, and fall back cleanly when the active model does not support
      search-based lookup. (#14274, #14287, #14732)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14175 Let models opt into original image detail @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14502 feat(search_tool): gate search_tool on model supports_search_tool
      field @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#12024 Enforce errors on overriding built-in model providers @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-model-support-changes-in-rust-v0-115-0
  source_release: codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in rust-v0.115.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-03-14-3-model-support-changes-in-v0-18-0|3 Model Support
  changes in v0.18.0]]'
- '[[Changes/ChatGPT/2026-03-16-we-re-rolling-out-an-update-to-gpt-5-3-instant-that-improves-follow-up-tone-and|GPT-5.3
  Instant update]]'
- '[[Changes/Cline/2026-03-16-added-w-b-inference-by-coreweave-as-a-new-api-provider-with-17-models|Added
  W&B Inference by CoreWeave as a new API provider with 17 models]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db|codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in rust-v0.115.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in rust-v0.115.0

**Codex CLI** · 2026-03-16 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.115.0) · from [[Releases/Codex CLI/codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db|0.115.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Supported models can now request full-resolution image inspection through both `view_image` and `codex.emitImage(..., detail: "original")`, which helps with precision visual tasks. (#14175)

> App integrations now use the Responses API tool-search flow, can suggest missing tools, and fall back cleanly when the active model does not support search-based lookup. (#14274, #14287, #14732)

> #14175 Let models opt into original image detail @fjord-oai

> #14502 feat(search_tool): gate search_tool on model supports_search_tool field @apanasenko-oai

> #12024 Enforce errors on overriding built-in model providers @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.115.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-16-17-apps-and-integrations-changes-in-rust-v0-115-0|17 Apps and Integrations changes in rust-v0.115.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-16-2-context-window-changes-in-rust-v0-115-0|2 Context Window changes in rust-v0.115.0]] · Context Window
- [[Changes/Codex CLI/2026-03-16-16-agent-mode-changes-in-rust-v0-115-0|16 Agent Mode changes in rust-v0.115.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-16-2-mobile-and-desktop-changes-in-rust-v0-115-0|2 Mobile and Desktop changes in rust-v0.115.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-16-4-voice-and-audio-changes-in-rust-v0-115-0|4 Voice and Audio changes in rust-v0.115.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-16-14493-memories-focus-write-prompts-on-user-preferences-andi-oai|♯14493 memories: focus write prompts on user preferences @andi-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-16-9-safety-and-privacy-changes-in-rust-v0-115-0|9 Safety and Privacy changes in rust-v0.115.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-16-2-account-and-access-changes-in-rust-v0-115-0|2 Account and Access changes in rust-v0.115.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-16-2-developer-workflow-changes-in-rust-v0-115-0|2 Developer Workflow changes in rust-v0.115.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-16-14410-make-collab-model-metadata-accurate-on-completion-aibrahim-oai|♯14410 Make collab model metadata accurate on completion @aibrahim-oai]] · Interface Experience
- [[Changes/Codex CLI/2026-03-16-70-other-changes-in-rust-v0-115-0|70 other changes in rust-v0.115.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-03-16 · Cline · [[Changes/Cline/2026-03-16-added-w-b-inference-by-coreweave-as-a-new-api-provider-with-17-models|Added W&B Inference by CoreWeave as a new API provider with 17 models]]
- Later: 2026-03-16 · ElevenLabs · [[Changes/ElevenLabs/2026-03-16-music|Music]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-16-d3360c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-16-5-model-support-changes-in-rust-v0-115-0.md%0ACard%20ID%3A%20codex-cli-2026-03-16-d3360c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.115.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->