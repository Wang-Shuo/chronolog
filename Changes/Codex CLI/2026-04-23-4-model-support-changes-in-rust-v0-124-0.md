---
card_id: codex-cli-2026-04-23-eef248
date: '2026-04-23'
description: 'Codex CLI · 2026-04-23 · Model Support: 4 changes in 0.124.0 — The TUI
  now has quick reasoning controls: `Alt+,` lowers reasoning, `Alt+.` raises it, and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1200
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0fca1a5dff0b6bb84e316f2e4ae9835c893264dbf27f9be533a97a36a7f42d56
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-23-eef248
  comparison: ''
  date: '2026-04-23'
  description: 'Codex CLI — 0.124.0: 4 Model Support changes'
  evidence:
  - quote: 'The TUI now has quick reasoning controls: `Alt+,` lowers reasoning, `Alt+.`
      raises it, and accepted model upgrades now reset reasoning to the new model’s
      default instead of carrying over stale settings. (#18866, #19085)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18866 feat(tui): shortcuts to change reasoning level temporarily @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#17820 feat: add AWS SigV4 auth for OpenAI-compatible model providers
      @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19085 Persist target default reasoning on model upgrade @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-model-support-changes-in-rust-v0-124-0
  source_release: codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in rust-v0.124.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-04-22-mlx-runner-adds-logprobs-support-for-compatible-models|MLX
  runner adds logprobs support for compatible models]]'
- '[[Changes/Superwhisper/2026-04-22-4-model-support-changes-in-superwhisper-windows-1-3-9|4
  Model Support changes in Superwhisper Windows 1.3.9]]'
- '[[Changes/Codex CLI/2026-04-23-6-model-support-changes-in-rust-v0-123-0|6 Model
  Support changes in rust-v0.123.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b|codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in rust-v0.124.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in rust-v0.124.0

**Codex CLI** · 2026-04-23 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.124.0) · from [[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b|0.124.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The TUI now has quick reasoning controls: `Alt+,` lowers reasoning, `Alt+.` raises it, and accepted model upgrades now reset reasoning to the new model’s default instead of carrying over stale settings. (#18866, #19085)

> #18866 feat(tui): shortcuts to change reasoning level temporarily @fcoury-oai

> #17820 feat: add AWS SigV4 auth for OpenAI-compatible model providers @celia-oai

> #19085 Persist target default reasoning on model upgrade @shijie-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.124.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-23-17-safety-and-privacy-changes-in-rust-v0-124-0|17 Safety and Privacy changes in rust-v0.124.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-23-12-apps-and-integrations-changes-in-rust-v0-124-0|12 Apps and Integrations changes in rust-v0.124.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-23-2-developer-workflow-changes-in-rust-v0-124-0|2 Developer Workflow changes in rust-v0.124.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-23-18973-chore-prep-memories-for-ab-jif-oai|♯18973 chore: prep memories for AB @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-23-11-agent-mode-changes-in-rust-v0-124-0|11 Agent Mode changes in rust-v0.124.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-23-2-context-window-changes-in-rust-v0-124-0|2 Context Window changes in rust-v0.124.0]] · Context Window
- [[Changes/Codex CLI/2026-04-23-45-other-changes-in-rust-v0-124-0|45 other changes in rust-v0.124.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-04-23 · Codex CLI · [[Changes/Codex CLI/2026-04-23-6-model-support-changes-in-rust-v0-123-0|6 Model Support changes in rust-v0.123.0]]
- Later: 2026-04-23 · Gemini CLI · [[Changes/Gemini CLI/2026-04-23-2-model-support-changes-in-v0-39-0|2 Model Support changes in v0.39.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-23-eef248&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-23-4-model-support-changes-in-rust-v0-124-0.md%0ACard%20ID%3A%20codex-cli-2026-04-23-eef248%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.124.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->