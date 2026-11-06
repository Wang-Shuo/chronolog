---
card_id: codex-cli-2026-10-27-06d725
date: '2026-10-27'
description: 'Codex CLI · 2026-10-27 · Model Support: 9 changes in 0.165.0 — Added
  a built-in Google Cloud Vertex AI provider, configured with `model_provider = "gcp"`…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1387
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3bcb8b2ff5f90bde138ed2cb2b03796d6baf4e35bf77c6d6597c6dde17d578f0
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-27-06d725
  comparison: ''
  date: '2026-10-27'
  description: 'Codex CLI — 0.165.0: 9 Model Support changes'
  evidence:
  - quote: Added a built-in Google Cloud Vertex AI provider, configured with `model_provider
      = "gcp"`. (#56265)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: Added GPT-6.1 Terra to the model catalogs. (#57337)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: Enabled reasoning effort changes during a conversation by default for supported
      models. (#56163)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: Stopped retrying when a provider reports that a model was not found, preserving
      its error message. (#56445)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56163 Enable reasoning effort overrides by default @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56233 Make Opus encoder test timestamps follow sample time @goodman-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56272 Upgrade Python SDK model generation to datamodel-code-generator
      0.64.0 @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56284 Scope model catalogs and caches by thread originator @kennyyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#57337 [0.165.0-alpha.1.2] Backport GPT-6.1 Terra to the model catalogs
      @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-model-support-changes-in-rust-v0-165-0
  source_release: codex-cli-2026-10-27-rust-v0-165-0-github-425927431-1fa685eb
  source_type: github_releases
  theme: model-support
  title: 9 Model Support changes in rust-v0.165.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-26-5-model-support-changes-in-v2-1-311|5 Model Support
  changes in v2.1.311]]'
- '[[Changes/Cline/2026-10-26-10-model-support-changes-in-v4-1-26|10 Model Support
  changes in v4.1.26]]'
- '[[Changes/Claude Code/2026-10-27-3-model-support-changes-in-v2-1-312|3 Model Support
  changes in v2.1.312]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-27-rust-v0-165-0-github-425927431-1fa685eb|codex-cli-2026-10-27-rust-v0-165-0-github-425927431-1fa685eb]]'
source_type: github_releases
theme: model-support
title: 9 Model Support changes in rust-v0.165.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Model Support changes in rust-v0.165.0

**Codex CLI** · 2026-10-27 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.165.0) · from [[Releases/Codex CLI/codex-cli-2026-10-27-rust-v0-165-0-github-425927431-1fa685eb|0.165.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a built-in Google Cloud Vertex AI provider, configured with `model_provider = "gcp"`. (#56265)

> Added GPT-6.1 Terra to the model catalogs. (#57337)

> Enabled reasoning effort changes during a conversation by default for supported models. (#56163)

> Stopped retrying when a provider reports that a model was not found, preserving its error message. (#56445)

> #56163 Enable reasoning effort overrides by default @felixxia-oai

> #56233 Make Opus encoder test timestamps follow sample time @goodman-oai

> #56272 Upgrade Python SDK model generation to datamodel-code-generator 0.64.0 @anp-oai

> #56284 Scope model catalogs and caches by thread originator @kennyyi-oai

> #57337 [0.165.0-alpha.1.2] Backport GPT-6.1 Terra to the model catalogs @shijie-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.165.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-27-added-a-repository-filter-to-the-session-picker-and-directory-grouping-to-the-ag|Added a repository filter to the session picker and directory grouping to the agent…]] · Interface Experience
- [[Changes/Codex CLI/2026-10-27-3-safety-and-privacy-changes-in-rust-v0-165-0|3 Safety and Privacy changes in rust-v0.165.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-27-4-agent-mode-changes-in-rust-v0-165-0|4 Agent Mode changes in rust-v0.165.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-27-2-context-window-changes-in-rust-v0-165-0|2 Context Window changes in rust-v0.165.0]] · Context Window
- [[Changes/Codex CLI/2026-10-27-10-apps-and-integrations-changes-in-rust-v0-165-0|10 Apps and Integrations changes in rust-v0.165.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-27-3-developer-workflow-changes-in-rust-v0-165-0|3 Developer Workflow changes in rust-v0.165.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-27-5-memory-and-personalization-changes-in-rust-v0-165-0|5 Memory and Personalization changes in rust-v0.165.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-27-3-account-and-access-changes-in-rust-v0-165-0|3 Account and Access changes in rust-v0.165.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-27-39-other-changes-in-rust-v0-165-0|39 other changes in rust-v0.165.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-27 · Claude Code · [[Changes/Claude Code/2026-10-27-3-model-support-changes-in-v2-1-312|3 Model Support changes in v2.1.312]]
- Later: 2026-10-27 · Gemini CLI · [[Changes/Gemini CLI/2026-10-27-add-banner-about-gemini-cli-not-being-optimized-for-gemini-4-by-srithreepo-in-ht|Add Banner about Gemini CLI not being optimized for Gemini 4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-27-06d725&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-27-9-model-support-changes-in-rust-v0-165-0.md%0ACard%20ID%3A%20codex-cli-2026-10-27-06d725%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.165.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->