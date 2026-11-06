---
card_id: codex-cli-2026-04-23-6edf14
date: '2026-04-23'
description: 'Codex CLI · 2026-04-23 · Model Support: 6 changes in 0.123.0 — Added
  a built-in `amazon-bedrock` model provider with configurable AWS profile support
  (#18744).'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1200
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fe5219762d1f3bb4ec7c7e80544d1f1f4600f11b2d52b15c7bdfd255150aa198
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-23-6edf14
  comparison: ''
  date: '2026-04-23'
  description: 'Codex CLI — 0.123.0: 6 Model Support changes'
  evidence:
  - quote: Added a built-in `amazon-bedrock` model provider with configurable AWS
      profile support (#18744).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: 'Refreshed bundled model metadata, including the current `gpt-5.4` default
      (#18586, #18388, #18719).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18586 Update models.json @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18388 Update models.json @github-actions'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18719 Fix stale model test fixtures @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18744 feat: add a built-in Amazon Bedrock model provider @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-model-support-changes-in-rust-v0-123-0
  source_release: codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18
  source_type: github_releases
  theme: model-support
  title: 6 Model Support changes in rust-v0.123.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-22-2-model-support-changes-in-v2-1-117|2 Model Support
  changes in v2.1.117]]'
- '[[Changes/Cline/2026-04-22-onboarding-flow-now-uses-dynamically-fetched-recommended-models-instead-of-a-har|Onboarding
  flow now uses dynamically fetched recommended models instead…]]'
- '[[Changes/Ollama/2026-04-22-mlx-runner-adds-logprobs-support-for-compatible-models|MLX
  runner adds logprobs support for compatible models]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18|codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18]]'
source_type: github_releases
theme: model-support
title: 6 Model Support changes in rust-v0.123.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in rust-v0.123.0

**Codex CLI** · 2026-04-23 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.123.0) · from [[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18|0.123.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a built-in `amazon-bedrock` model provider with configurable AWS profile support (#18744).

> Refreshed bundled model metadata, including the current `gpt-5.4` default (#18586, #18388, #18719).

> #18586 Update models.json @aibrahim-oai

> #18388 Update models.json @github-actions

> #18719 Fix stale model test fixtures @aibrahim-oai

> #18744 feat: add a built-in Amazon Bedrock model provider @celia-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.123.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-23-18662-feat-add-metric-to-track-the-number-of-turns-with-memory-usage-jif-oai|♯18662 feat: add metric to track the number of turns with memory usage @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-04-23-18794-organize-context-fragments-pakrym-oai|♯18794 Organize context fragments @pakrym-oai]] · Context Window
- [[Changes/Codex CLI/2026-04-23-2-collaboration-changes-in-rust-v0-123-0|2 Collaboration changes in rust-v0.123.0]] · Collaboration
- [[Changes/Codex CLI/2026-04-23-8-agent-mode-changes-in-rust-v0-123-0|8 Agent Mode changes in rust-v0.123.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-23-6-safety-and-privacy-changes-in-rust-v0-123-0|6 Safety and Privacy changes in rust-v0.123.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-23-18633-use-app-server-thread-names-in-tui-picker-etraut-openai|♯18633 Use app server thread names in TUI picker @etraut-openai]] · Interface Experience
- [[Changes/Codex CLI/2026-04-23-added-mcp-verbose-for-full-mcp-server-diagnostics-resources-and-resource-templat|Added /mcp verbose for full MCP server diagnostics, resources, and resource…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-23-9-apps-and-integrations-changes-in-rust-v0-123-0|9 Apps and Integrations changes in rust-v0.123.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-23-18858-stabilize-debug-clear-memories-integration-test-jif-oai|♯18858 Stabilize debug clear memories integration test @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-23-11-developer-workflow-changes-in-rust-v0-123-0|11 Developer Workflow changes in rust-v0.123.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-23-18423-chore-document-intentional-await-holding-cases-bolinfest|♯18423 chore: document intentional await-holding cases @bolinfest]] · Files and Data
- [[Changes/Codex CLI/2026-04-23-45-other-changes-in-rust-v0-123-0|45 other changes in rust-v0.123.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-04-22 · Ollama · [[Changes/Ollama/2026-04-22-mlx-runner-adds-logprobs-support-for-compatible-models|MLX runner adds logprobs support for compatible models]]
- Later: 2026-04-23 · Codex CLI · [[Changes/Codex CLI/2026-04-23-4-model-support-changes-in-rust-v0-124-0|4 Model Support changes in rust-v0.124.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-23-6edf14&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-23-6-model-support-changes-in-rust-v0-123-0.md%0ACard%20ID%3A%20codex-cli-2026-04-23-6edf14%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.123.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->