---
card_id: codex-cli-2026-04-24-4d5935
date: '2026-04-24'
description: 'Codex CLI · 2026-04-24 · Safety and Privacy: 9 changes in 0.125.0 —
  Permission profiles now round-trip across TUI sessions, user turns, MCP sandbox
  state…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1104
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ad87d3930bc49d699a6d6716e4e60bb94bef50818b2b394e0d0230c354526e0a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-24-4d5935
  comparison: ''
  date: '2026-04-24'
  description: 'Codex CLI — 0.125.0: 9 Safety and Privacy changes'
  evidence:
  - quote: 'Permission profiles now round-trip across TUI sessions, user turns, MCP
      sandbox state, shell escalation, and app-server APIs. (#18284, #18285, #18286,
      #18287, #19231)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: 'Windows sandbox startup handles multiple CLI versions and installed app
      directories better, and background `Start-Process` calls avoid visible PowerShell
      windows. (#19044, #19180, #19214)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: 'App-server docs and generated schemas were refreshed for the new transport,
      thread, marketplace, sticky environment, and permission-profile APIs. (#18255,
      #18897, #19014, #19074, #19231)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19149 Update safety check wording @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18284 tui: sync session permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18285 tui: carry permission profiles on user turns @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18286 mcp: include permission profiles in sandbox state @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18287 shell-escalation: carry resolved permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19180 use a version-specific suffix for command runner binary in .sandbox-bin
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-safety-and-privacy-changes-in-rust-v0-125-0
  source_release: codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c
  source_type: github_releases
  theme: safety-privacy
  title: 9 Safety and Privacy changes in rust-v0.125.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-04-23-6-safety-and-privacy-changes-in-rust-v0-123-0|6
  Safety and Privacy changes in rust-v0.123.0]]'
- '[[Changes/Gemini CLI/2026-04-23-6-safety-and-privacy-changes-in-v0-39-0|6 Safety
  and Privacy changes in v0.39.0]]'
- '[[Changes/GitHub Copilot CLI/2026-04-23-permission-prompts-appear-correctly-in-remote-sessions-for-the-cli-tui|Permission
  prompts appear correctly in remote sessions for the CLI TUI]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c|codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c]]'
source_type: github_releases
theme: safety-privacy
title: 9 Safety and Privacy changes in rust-v0.125.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Safety and Privacy changes in rust-v0.125.0

**Codex CLI** · 2026-04-24 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.125.0) · from [[Releases/Codex CLI/codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c|0.125.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Permission profiles now round-trip across TUI sessions, user turns, MCP sandbox state, shell escalation, and app-server APIs. (#18284, #18285, #18286, #18287, #19231)

> Windows sandbox startup handles multiple CLI versions and installed app directories better, and background `Start-Process` calls avoid visible PowerShell windows. (#19044, #19180, #19214)

> App-server docs and generated schemas were refreshed for the new transport, thread, marketplace, sticky environment, and permission-profile APIs. (#18255, #18897, #19014, #19074, #19231)

> #19149 Update safety check wording @etraut-openai

> #18284 tui: sync session permission profiles @bolinfest

> #18285 tui: carry permission profiles on user turns @bolinfest

> #18286 mcp: include permission profiles in sandbox state @bolinfest

> #18287 shell-escalation: carry resolved permission profiles @bolinfest

> #19180 use a version-specific suffix for command runner binary in .sandbox-bin @iceweasel-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.125.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-24-5-agent-mode-changes-in-rust-v0-125-0|5 Agent Mode changes in rust-v0.125.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-24-2-context-window-changes-in-rust-v0-125-0|2 Context Window changes in rust-v0.125.0]] · Context Window
- [[Changes/Codex CLI/2026-04-24-19167-ci-add-macos-keychain-entitlements-euroelessar|♯19167 ci: add macOS keychain entitlements @euroelessar]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-24-windows-bazel-ci-now-uses-a-stable-path-and-shared-query-startup-path-for-better|Windows Bazel CI now uses a stable PATH and shared query startup path for better…]] · Collaboration
- [[Changes/Codex CLI/2026-04-24-2-developer-workflow-changes-in-rust-v0-125-0|2 Developer Workflow changes in rust-v0.125.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-24-5-model-support-changes-in-rust-v0-125-0|5 Model Support changes in rust-v0.125.0]] · Model Support
- [[Changes/Codex CLI/2026-04-24-11-apps-and-integrations-changes-in-rust-v0-125-0|11 Apps and Integrations changes in rust-v0.125.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-24-32-other-changes-in-rust-v0-125-0|32 other changes in rust-v0.125.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-23 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-23-permission-prompts-appear-correctly-in-remote-sessions-for-the-cli-tui|Permission prompts appear correctly in remote sessions for the CLI TUI]]
- Later: 2026-04-27 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-27-location-based-permission-persistence-is-now-enabled-by-default-so-approvals-car|Location-based permission persistence is now enabled by default, so approvals carry…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-24-4d5935&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-24-9-safety-and-privacy-changes-in-rust-v0-125-0.md%0ACard%20ID%3A%20codex-cli-2026-04-24-4d5935%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.125.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->