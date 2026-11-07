---
card_id: codex-cli-2026-06-25-918f31
date: '2026-06-25'
description: 'Codex CLI · 2026-06-25 · Model Support: 4 changes in 0.142.2 — Remote
  HTTP(S) image inputs now return clear model-visible validation errors; inline data
  URLs…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1263
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 07ae31118beb30a8054e74f00d4ccb8b0b4e1e3ea2ed2c03943ab4473d47050b
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-25-918f31
  comparison: ''
  date: '2026-06-25'
  description: 'Codex CLI — 0.142.2: 4 Model Support changes'
  evidence:
  - quote: 'Remote HTTP(S) image inputs now return clear model-visible validation
      errors; inline data URLs and local images remain supported. (#29417, #29419)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: Code Mode now warns when the selected model lacks the required metadata.
      (#29490)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#29417 [codex] replace remote images with model-visible error text @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  - quote: '#29490 chore: warn when Code Mode lacks model metadata @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-model-support-changes-in-rust-v0-142-2
  source_release: codex-cli-2026-06-25-rust-v0-142-2-github-344540546-8fdabe3c
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in rust-v0.142.2
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-06-24-2-model-support-changes-in-v1-0-65|2 Model
  Support changes in v1.0.65]]'
- '[[Changes/OpenCode/2026-06-24-core-hid-gpt-5-5-pro-when-using-codex-oauth|Core
  Hid gpt-5.5-pro when using Codex OAuth]]'
- '[[Changes/Claude Code/2026-06-25-added-claude-code-assistant-response-opentelemetry-log-event-containing-the-mode|Added
  claude_code.assistant_response OpenTelemetry log event containing…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-25-rust-v0-142-2-github-344540546-8fdabe3c|codex-cli-2026-06-25-rust-v0-142-2-github-344540546-8fdabe3c]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in rust-v0.142.2
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in rust-v0.142.2

**Codex CLI** · 2026-06-25 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.142.2) · from [[Releases/Codex CLI/codex-cli-2026-06-25-rust-v0-142-2-github-344540546-8fdabe3c|0.142.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Remote HTTP(S) image inputs now return clear model-visible validation errors; inline data URLs and local images remain supported. (#29417, #29419)

> Code Mode now warns when the selected model lacks the required metadata. (#29490)

> #29417 [codex] replace remote images with model-visible error text @rka-oai

> #29490 chore: warn when Code Mode lacks model metadata @celia-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.142.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-25-macos-authentication-clients-can-honor-system-proxy-pac-and-wpad-settings-when-r|macOS authentication clients can honor system proxy, PAC, and WPAD settings…]] · Account and Access
- [[Changes/Codex CLI/2026-06-25-26709-pac-4-add-macos-system-proxy-resolver-canvrno-oai|♯26709 PAC 4 - Add macOS system proxy resolver @canvrno-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-25-2-context-window-changes-in-rust-v0-142-2|2 Context Window changes in rust-v0.142.2]] · Context Window
- [[Changes/Codex CLI/2026-06-25-9-apps-and-integrations-changes-in-rust-v0-142-2|9 Apps and Integrations changes in rust-v0.142.2]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-25-apps-can-display-richer-safety-buffering-ui-using-server-provided-visibility-and|Apps can display richer safety-buffering UI using server-provided visibility…]] · Reliability and Performance
- [[Changes/Codex CLI/2026-06-25-2-safety-and-privacy-changes-in-rust-v0-142-2|2 Safety and Privacy changes in rust-v0.142.2]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-25-13-other-changes-in-rust-v0-142-2|13 other changes in rust-v0.142.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-06-25 · Claude Code · [[Changes/Claude Code/2026-06-25-added-claude-code-assistant-response-opentelemetry-log-event-containing-the-mode|Added claude_code.assistant_response OpenTelemetry log event containing…]]
- Later: 2026-06-25 · Dify · [[Changes/Dify/2026-06-25-17-model-support-changes-in-1-15-0|17 Model Support changes in 1.15.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-25-918f31&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-25-4-model-support-changes-in-rust-v0-142-2.md%0ACard%20ID%3A%20codex-cli-2026-06-25-918f31%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.142.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->