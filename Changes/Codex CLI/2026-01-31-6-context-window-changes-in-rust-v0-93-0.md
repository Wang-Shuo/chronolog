---
card_id: codex-cli-2026-01-31-019f4c
date: '2026-01-31'
description: 'Codex CLI · 2026-01-31 · Context Window: 6 changes in 0.93.0 — App-server
  can now run in external auth mode, accepting ChatGPT auth tokens from a host app
  and…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2327
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 96913a278877549d1c5e9507f80069ba909fcaa936656cc118334b46544bbafb
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-31-019f4c
  comparison: ''
  date: '2026-01-31'
  description: 'Codex CLI — 0.93.0: 6 Context Window changes'
  evidence:
  - quote: App-server can now run in external auth mode, accepting ChatGPT auth tokens
      from a host app and requesting refreshes when needed. (#10012)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9944 TUI footer: right-align context and degrade shortcut summary + mode
      cleanly @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9950 fix(app-server, core): defer initial context write to rollout file
      until first turn @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10034 compaction @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10129 Ensure auto-compaction starts after turn started @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10123 Add app-server compaction item notifications tests @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-context-window-changes-in-rust-v0-93-0
  source_release: codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8
  source_type: github_releases
  theme: context-window
  title: 6 Context Window changes in rust-v0.93.0
  type: change
related_changes:
- '[[Changes/Cline/2026-01-30-new-model-added-kimi-k2-5-model-to-moonshot-provider-262k-context-image-support|New
  model: Added Kimi-K2.5 model to Moonshot provider…]]'
- '[[Changes/Cline/2026-01-30-new-model-added-kimi-k2-5-model-to-moonshot-provider-262k-context-image-support-53f1f0|New
  model: Added Kimi-K2.5 model to Moonshot provider…]]'
- '[[Changes/Cline/2026-01-30-new-model-added-kimi-k2-5-model-to-moonshot-provider-262k-context-image-support-9b8adb|New
  model: Added Kimi-K2.5 model to Moonshot provider…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8|codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8]]'
source_type: github_releases
theme: context-window
title: 6 Context Window changes in rust-v0.93.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Context Window changes in rust-v0.93.0

**Codex CLI** · 2026-01-31 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.93.0) · from [[Releases/Codex CLI/codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8|0.93.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server can now run in external auth mode, accepting ChatGPT auth tokens from a host app and requesting refreshes when needed. (#10012)

> #9944 TUI footer: right-align context and degrade shortcut summary + mode cleanly @charley-oai

> #9950 fix(app-server, core): defer initial context write to rollout file until first turn @owenlin0

> #10034 compaction @aibrahim-oai

> #10129 Ensure auto-compaction starts after turn started @aibrahim-oai

> #10123 Add app-server compaction item notifications tests @aibrahim-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.93.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-31-6-memory-and-personalization-changes-in-rust-v0-93-0|6 Memory and Personalization changes in rust-v0.93.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-01-31-10191-chore-app-server-document-authmode-owenlin0|♯10191 chore(app-server): document AuthMode @owenlin0]] · Files and Data
- [[Changes/Codex CLI/2026-01-31-10011-really-fix-pwd-for-windows-codex-zip-iceweasel-oai|♯10011 really fix pwd for windows codex zip @iceweasel-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-31-9654-show-oauth-error-descriptions-in-callback-responses-blevy-oai|♯9654 Show OAuth error descriptions in callback responses @blevy-oai]] · Account and Access
- [[Changes/Codex CLI/2026-01-31-3-interface-experience-changes-in-rust-v0-93-0|3 Interface Experience changes in rust-v0.93.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-31-3-reliability-and-performance-changes-in-rust-v0-93-0|3 Reliability and Performance changes in rust-v0.93.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-01-31-10118-codex-cli-show-model-capacity-guidance-on-429-ccy-oai|♯10118 CodexCLI Show model-capacity guidance on 429 @ccy-oai]] · Model Support
- [[Changes/Codex CLI/2026-01-31-6-developer-workflow-changes-in-rust-v0-93-0|6 Developer Workflow changes in rust-v0.93.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-31-10030-clarify-external-editor-env-var-message-joshka-oai|♯10030 Clarify external editor env var message @joshka-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-01-31-smart-approvals-are-now-enabled-by-default-with-explicit-approval-prompts-for-mc|Smart approvals are now enabled by default, with explicit approval prompts for MCP…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-31-4-safety-and-privacy-changes-in-rust-v0-93-0|4 Safety and Privacy changes in rust-v0.93.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-31-14-apps-and-integrations-changes-in-rust-v0-93-0|14 Apps and Integrations changes in rust-v0.93.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-31-3-search-and-browsing-changes-in-rust-v0-93-0|3 Search and Browsing changes in rust-v0.93.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-01-31-added-apps-to-browse-connectors-in-tui-and-insertion-for-app-prompts-9728|Added /apps to browse connectors in TUI and $ insertion for app prompts]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-31-97-other-changes-in-rust-v0-93-0|97 other changes in rust-v0.93.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-01-30 · Cline · [[Changes/Cline/2026-01-30-new-model-added-kimi-k2-5-model-to-moonshot-provider-262k-context-image-support-9b8adb|New model: Added Kimi-K2.5 model to Moonshot provider…]]
- Later: 2026-01-31 · OpenCode · [[Changes/OpenCode/2026-01-31-core-add-copilot-specific-provider-to-properly-handle-reasoning-tokens|Core Add Copilot-specific provider to properly handle reasoning tokens]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-31-019f4c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-31-6-context-window-changes-in-rust-v0-93-0.md%0ACard%20ID%3A%20codex-cli-2026-01-31-019f4c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.93.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->