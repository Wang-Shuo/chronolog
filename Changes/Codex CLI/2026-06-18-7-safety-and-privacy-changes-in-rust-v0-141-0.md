---
card_id: codex-cli-2026-06-18-065cb9
date: '2026-06-18'
description: 'Codex CLI · 2026-06-18 · Safety and Privacy: 7 changes in 0.141.0 —
  Cross-platform remote execution now preserves executor-native working directories
  and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1159
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: de84a3418503f49963d0b5cb3310bd9601ee830f519f3fcc39d3921e500381f4
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-18-065cb9
  comparison: ''
  date: '2026-06-18'
  description: 'Codex CLI — 0.141.0: 7 Safety and Privacy changes'
  evidence:
  - quote: 'Cross-platform remote execution now preserves executor-native working
      directories and shells, including filesystem permission paths across app-server
      and exec-server boundaries. (#27819, #27995, #28032, #28122, #28165, #28367)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: 'Windows sandbox execution repairs stale credentials automatically and
      gives PowerShell commands more time before backgrounding. (#27086, #27944)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28357 Extract shared Windows sandbox session runner @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27944 recover stale Windows sandbox credentials @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28358 Add hidden Windows sandbox wrapper entrypoint @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28165 Use PathUri in filesystem permission paths for exec-server @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28367 Use ApiPathString in app-server filesystem permission paths @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-safety-and-privacy-changes-in-rust-v0-141-0
  source_release: codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75
  source_type: github_releases
  theme: safety-privacy
  title: 7 Safety and Privacy changes in rust-v0.141.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-06-15-27490-remove-tui-legacy-windows-sandbox-dependency-etraut-openai|♯27490
  Remove TUI legacy Windows sandbox dependency @etraut-openai]]'
- '[[Changes/Claude Code/2026-06-17-added-sandbox-allowappleevents-opt-in-setting-that-lets-sandboxed-commands-send|Added
  sandbox.allowAppleEvents opt-in setting that lets sandboxed commands send…]]'
- '[[Changes/ChatGPT/2026-06-18-app-permission-controls-you-can-now-choose-when-chatgpt-asks-before-using-connec|App
  permission controls: You can now choose when ChatGPT asks before using connected
  apps]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75|codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75]]'
source_type: github_releases
theme: safety-privacy
title: 7 Safety and Privacy changes in rust-v0.141.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Safety and Privacy changes in rust-v0.141.0

**Codex CLI** · 2026-06-18 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.141.0) · from [[Releases/Codex CLI/codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75|0.141.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Cross-platform remote execution now preserves executor-native working directories and shells, including filesystem permission paths across app-server and exec-server boundaries. (#27819, #27995, #28032, #28122, #28165, #28367)

> Windows sandbox execution repairs stale credentials automatically and gives PowerShell commands more time before backgrounding. (#27086, #27944)

> #28357 Extract shared Windows sandbox session runner @iceweasel-oai

> #27944 recover stale Windows sandbox credentials @iceweasel-oai

> #28358 Add hidden Windows sandbox wrapper entrypoint @iceweasel-oai

> #28165 Use PathUri in filesystem permission paths for exec-server @anp-oai

> #28367 Use ApiPathString in app-server filesystem permission paths @anp-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.141.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-18-5-agent-mode-changes-in-rust-v0-141-0|5 Agent Mode changes in rust-v0.141.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-18-7-developer-workflow-changes-in-rust-v0-141-0|7 Developer Workflow changes in rust-v0.141.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-18-tls-connections-now-support-p-521-certificate-signatures-commonly-used-by-enterp|TLS connections now support P-521 certificate signatures commonly used by enterprise…]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-06-18-28257-support-staging-oauth-client-id-overrides-apanasenko-oai|♯28257 Support staging OAuth client ID overrides @apanasenko-oai]] · Account and Access
- [[Changes/Codex CLI/2026-06-18-2-context-window-changes-in-rust-v0-141-0|2 Context Window changes in rust-v0.141.0]] · Context Window
- [[Changes/Codex CLI/2026-06-18-17-apps-and-integrations-changes-in-rust-v0-141-0|17 Apps and Integrations changes in rust-v0.141.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-18-3-memory-and-personalization-changes-in-rust-v0-141-0|3 Memory and Personalization changes in rust-v0.141.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-06-18-28143-feat-app-server-expose-rate-limit-reset-credits-jayp-oai|♯28143 feat(app-server): expose rate-limit reset credits @jayp-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-06-18-42-other-changes-in-rust-v0-141-0|42 other changes in rust-v0.141.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-06-18 · ChatGPT · [[Changes/ChatGPT/2026-06-18-app-permission-controls-you-can-now-choose-when-chatgpt-asks-before-using-connec|App permission controls: You can now choose when ChatGPT asks before using connected apps]]
- Later: 2026-06-19 · v0 · [[Changes/v0/2026-06-19-responding-to-an-agent-prompt-for-an-environment-variable-permission-question-or|Responding to an agent prompt for an environment variable, permission, question…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-18-065cb9&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-18-7-safety-and-privacy-changes-in-rust-v0-141-0.md%0ACard%20ID%3A%20codex-cli-2026-06-18-065cb9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.141.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->