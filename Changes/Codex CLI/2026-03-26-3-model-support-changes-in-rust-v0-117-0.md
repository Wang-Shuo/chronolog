---
card_id: codex-cli-2026-03-26-f7a317
date: '2026-03-26'
description: 'Codex CLI · 2026-03-26 · Model Support: 3 changes in 0.117.0 — `tui_app_server`
  no longer duplicates live reasoning summaries or `/review` output, and it…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1172
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 65397ad209c6a88edb99e48a9beaa2cc2f5e8c4881c25b9df0ddac7c934a474a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-26-f7a317
  comparison: ''
  date: '2026-03-26'
  description: 'Codex CLI — 0.117.0: 3 Model Support changes'
  evidence:
  - quote: '`tui_app_server` no longer duplicates live reasoning summaries or `/review`
      output, and it preserves transcript text instead of dropping it under backpressure.
      (#15758, #15839, #15759)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#14888 Feat: reuse persisted model and reasoning effort on thread resume
      @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15758 fix(tui): avoid duplicate live reasoning summaries @fcoury'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-model-support-changes-in-rust-v0-117-0
  source_release: codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in rust-v0.117.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-03-23-ensure-models-appear-in-picker-correctly-display-model-names-where-possible|Ensure
  models appear in picker correctly, display model names where possible]]'
- '[[Changes/Gemini CLI/2026-03-24-7-model-support-changes-in-v0-35-0|7 Model Support
  changes in v0.35.0]]'
- '[[Changes/Claude Code/2026-03-26-added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef|Added
  ANTHROPIC_DEFAULT{OPUS,SONNET,HAIKU}MODEL_SUPPORTS env vars to override…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6|codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in rust-v0.117.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in rust-v0.117.0

**Codex CLI** · 2026-03-26 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.117.0) · from [[Releases/Codex CLI/codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6|0.117.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `tui_app_server` no longer duplicates live reasoning summaries or `/review` output, and it preserves transcript text instead of dropping it under backpressure. (#15758, #15839, #15759)

> #14888 Feat: reuse persisted model and reasoning effort on thread resume @shijie-oai

> #15758 fix(tui): avoid duplicate live reasoning summaries @fcoury

Source: https://github.com/openai/codex/releases/tag/rust-v0.117.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-26-19-developer-workflow-changes-in-rust-v0-117-0|19 Developer Workflow changes in rust-v0.117.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-26-15789-treat-chatgpt-hc-plan-as-enterprise-arnavdugar-openai|♯15789 Treat ChatGPT hc plan as Enterprise @arnavdugar-openai]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-03-26-the-app-server-backed-tui-is-now-enabled-by-default-and-the-plugin-app-rollout-f|The app-server-backed TUI is now enabled by default, and the plugin/app rollout…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-26-plugins-are-now-a-first-class-workflow-codex-can-sync-product-scoped-plugins-at|Plugins are now a first-class workflow]] · Search and Browsing
- [[Changes/Codex CLI/2026-03-26-2-image-generation-changes-in-rust-v0-117-0|2 Image Generation changes in rust-v0.117.0]] · Image Generation
- [[Changes/Codex CLI/2026-03-26-15579-increase-voice-space-hold-timeout-to-1s-aibrahim-oai|♯15579 Increase voice space hold timeout to 1s @aibrahim-oai]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-26-2-automation-and-scheduling-changes-in-rust-v0-117-0|2 Automation and Scheduling changes in rust-v0.117.0]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-03-26-5-context-window-changes-in-rust-v0-117-0|5 Context Window changes in rust-v0.117.0]] · Context Window
- [[Changes/Codex CLI/2026-03-26-14945-feat-tui-restore-composer-history-in-app-server-tui-fcoury|♯14945 feat(tui): restore composer history in app-server tui @fcoury]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-03-26-15480-use-shift-left-to-edit-queued-messages-in-tmux-charley-oai|♯15480 Use Shift+Left to edit queued messages in tmux @charley-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-03-26-3-interface-experience-changes-in-rust-v0-117-0|3 Interface Experience changes in rust-v0.117.0]] · Interface Experience
- [[Changes/Codex CLI/2026-03-26-4-account-and-access-changes-in-rust-v0-117-0|4 Account and Access changes in rust-v0.117.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-26-19-agent-mode-changes-in-rust-v0-117-0|19 Agent Mode changes in rust-v0.117.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-26-57-apps-and-integrations-changes-in-rust-v0-117-0|57 Apps and Integrations changes in rust-v0.117.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-26-3-mobile-and-desktop-changes-in-rust-v0-117-0|3 Mobile and Desktop changes in rust-v0.117.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-26-5-safety-and-privacy-changes-in-rust-v0-117-0|5 Safety and Privacy changes in rust-v0.117.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-26-15175-chore-morpheus-does-not-generate-memories-jif-oai|♯15175 chore: morpheus does not generate memories @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-26-117-other-changes-in-rust-v0-117-0|117 other changes in rust-v0.117.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef|Added ANTHROPIC_DEFAULT{OPUS,SONNET,HAIKU}MODEL_SUPPORTS env vars to override…]]
- Later: 2026-03-26 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-26-model-display-header-shows-the-active-reasoning-effort-level-e-g-high-next-to-th|Model display header shows the active reasoning effort level (e.g. "(high)") next…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-26-f7a317&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-26-3-model-support-changes-in-rust-v0-117-0.md%0ACard%20ID%3A%20codex-cli-2026-03-26-f7a317%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.117.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->