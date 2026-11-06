---
card_id: codex-cli-2026-06-01-8b39a3
date: '2026-06-01'
description: 'Codex CLI · 2026-06-01 · Model Support: 5 changes in 0.136.0 — Refreshed
  Amazon Bedrock catalog metadata, including GPT-5.5, removal of unsupported OSS…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1239
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 422b773cbad3e5716e9e19afbc1d0960032b6e7593ec59130af1261f31787402
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-01-8b39a3
  comparison: ''
  date: '2026-06-01'
  description: 'Codex CLI — 0.136.0: 5 Model Support changes'
  evidence:
  - quote: 'Refreshed Amazon Bedrock catalog metadata, including GPT-5.5, removal
      of unsupported OSS entries, and default-tier-only GPT model behavior. (#24701,
      #24960, #25318)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24701 chore: add GPT-5.5 to the Amazon Bedrock catalog @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24960 [codex] Remove Bedrock OSS models from catalog @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25031 [codex] Add model tool mode selector @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25318 fix: Limit Bedrock GPT models to default service tier @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-model-support-changes-in-rust-v0-136-0
  source_release: codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in rust-v0.136.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-28-3-model-support-changes-in-v1-0-55|3 Model
  Support changes in v1.0.55]]'
- '[[Changes/GitHub Copilot CLI/2026-05-29-2-model-support-changes-in-v1-0-56|2 Model
  Support changes in v1.0.56]]'
- '[[Changes/Claude Code/2026-05-30-auto-mode-is-now-available-on-bedrock-vertex-and-foundry-for-opus-4-7-and-opus-4|Auto
  mode is now available on Bedrock, Vertex, and Foundry for Opus 4.7 and Opus 4.8]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6|codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in rust-v0.136.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in rust-v0.136.0

**Codex CLI** · 2026-06-01 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.136.0) · from [[Releases/Codex CLI/codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6|0.136.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Refreshed Amazon Bedrock catalog metadata, including GPT-5.5, removal of unsupported OSS entries, and default-tier-only GPT model behavior. (#24701, #24960, #25318)

> #24701 chore: add GPT-5.5 to the Amazon Bedrock catalog @celia-oai

> #24960 [codex] Remove Bedrock OSS models from catalog @celia-oai

> #25031 [codex] Add model tool mode selector @aibrahim-oai

> #25318 fix: Limit Bedrock GPT models to default service tier @owenlin0

Source: https://github.com/openai/codex/releases/tag/rust-v0.136.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-01-25110-move-config-document-helpers-into-their-own-module-jif-oai|♯25110 Move config document helpers into their own module @jif-oai]] · Files and Data
- [[Changes/Codex CLI/2026-06-01-11-developer-workflow-changes-in-rust-v0-136-0|11 Developer Workflow changes in rust-v0.136.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-01-20-apps-and-integrations-changes-in-rust-v0-136-0|20 Apps and Integrations changes in rust-v0.136.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-01-11-safety-and-privacy-changes-in-rust-v0-136-0|11 Safety and Privacy changes in rust-v0.136.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-01-2-memory-and-personalization-changes-in-rust-v0-136-0|2 Memory and Personalization changes in rust-v0.136.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-06-01-3-agent-mode-changes-in-rust-v0-136-0|3 Agent Mode changes in rust-v0.136.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-01-2-editor-experience-changes-in-rust-v0-136-0|2 Editor Experience changes in rust-v0.136.0]] · Editor Experience
- [[Changes/Codex CLI/2026-06-01-9-context-window-changes-in-rust-v0-136-0|9 Context Window changes in rust-v0.136.0]] · Context Window
- [[Changes/Codex CLI/2026-06-01-3-search-and-browsing-changes-in-rust-v0-136-0|3 Search and Browsing changes in rust-v0.136.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-01-2-interface-experience-changes-in-rust-v0-136-0|2 Interface Experience changes in rust-v0.136.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-01-3-image-generation-changes-in-rust-v0-136-0|3 Image Generation changes in rust-v0.136.0]] · Image Generation
- [[Changes/Codex CLI/2026-06-01-57-other-changes-in-rust-v0-136-0|57 other changes in rust-v0.136.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-05-30 · Claude Code · [[Changes/Claude Code/2026-05-30-auto-mode-is-now-available-on-bedrock-vertex-and-foundry-for-opus-4-7-and-opus-4|Auto mode is now available on Bedrock, Vertex, and Foundry for Opus 4.7 and Opus 4.8]]
- Later: 2026-06-01 · ElevenLabs · [[Changes/ElevenLabs/2026-06-01-workspaces|Workspaces]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-01-8b39a3&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-01-5-model-support-changes-in-rust-v0-136-0.md%0ACard%20ID%3A%20codex-cli-2026-06-01-8b39a3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.136.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->