---
card_id: codex-cli-2026-04-24-bec64b
date: '2026-04-24'
description: 'Codex CLI · 2026-04-24 · Model Support: 5 changes in 0.125.0 — Model
  providers now own model discovery, with AWS/Bedrock account state exposed to app
  clients…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1201
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7ea6b6594e89d7f52fec386ce9d0833a11041e704b1dbba6164594a3bffbb37b
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-24-bec64b
  comparison: ''
  date: '2026-04-24'
  description: 'Codex CLI — 0.125.0: 5 Model Support changes'
  evidence:
  - quote: 'Model providers now own model discovery, with AWS/Bedrock account state
      exposed to app clients. (#18950, #19048)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '`codex exec --json` now reports reasoning-token usage for programmatic
      consumers. (#19308)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: Refreshed `models.json` and related core, app-server, SDK, and TUI fixtures
      for the latest model catalog and reasoning defaults. (#19323)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18950 feat: let model providers own model discovery @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19323 Update models.json and related fixtures @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-model-support-changes-in-rust-v0-125-0
  source_release: codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in rust-v0.125.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-04-23-recommended-models-in-ollama-launch-now-appear-in-a-fixed-canonical-order|Recommended
  models in ollama launch now appear in a fixed, canonical order]]'
- '[[Changes/OpenCode/2026-04-23-2-model-support-changes-in-v1-14-22-1|2 Model Support
  changes in v1.14.22 + 1]]'
- '[[Changes/Cline/2026-04-24-add-gpt-5-5-model-support-for-openai-codex-subscription-users|Add
  GPT-5.5 model support for OpenAI Codex subscription users]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c|codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in rust-v0.125.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in rust-v0.125.0

**Codex CLI** · 2026-04-24 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.125.0) · from [[Releases/Codex CLI/codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c|0.125.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Model providers now own model discovery, with AWS/Bedrock account state exposed to app clients. (#18950, #19048)

> `codex exec --json` now reports reasoning-token usage for programmatic consumers. (#19308)

> Refreshed `models.json` and related core, app-server, SDK, and TUI fixtures for the latest model catalog and reasoning defaults. (#19323)

> #18950 feat: let model providers own model discovery @celia-oai

> #19323 Update models.json and related fixtures @sayan-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.125.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-24-5-agent-mode-changes-in-rust-v0-125-0|5 Agent Mode changes in rust-v0.125.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-24-9-safety-and-privacy-changes-in-rust-v0-125-0|9 Safety and Privacy changes in rust-v0.125.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-24-2-context-window-changes-in-rust-v0-125-0|2 Context Window changes in rust-v0.125.0]] · Context Window
- [[Changes/Codex CLI/2026-04-24-19167-ci-add-macos-keychain-entitlements-euroelessar|♯19167 ci: add macOS keychain entitlements @euroelessar]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-24-windows-bazel-ci-now-uses-a-stable-path-and-shared-query-startup-path-for-better|Windows Bazel CI now uses a stable PATH and shared query startup path for better…]] · Collaboration
- [[Changes/Codex CLI/2026-04-24-2-developer-workflow-changes-in-rust-v0-125-0|2 Developer Workflow changes in rust-v0.125.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-24-11-apps-and-integrations-changes-in-rust-v0-125-0|11 Apps and Integrations changes in rust-v0.125.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-24-32-other-changes-in-rust-v0-125-0|32 other changes in rust-v0.125.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-04-24 · Cline · [[Changes/Cline/2026-04-24-add-gpt-5-5-model-support-for-openai-codex-subscription-users|Add GPT-5.5 model support for OpenAI Codex subscription users]]
- Later: 2026-04-24 · DeepSeek API · [[Changes/DeepSeek API/2026-04-24-deepseek-v4|DeepSeek-V4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-24-bec64b&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-24-5-model-support-changes-in-rust-v0-125-0.md%0ACard%20ID%3A%20codex-cli-2026-04-24-bec64b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.125.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->