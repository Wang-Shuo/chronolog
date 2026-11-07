---
card_id: codex-cli-2026-09-17-e3e8b0
date: '2026-09-17'
description: 'Codex CLI · 2026-09-17 · Apps and Integrations: 24 changes in 0.155.0
  — Added Touch ID verification for MCP requests in local TUI sessions on supported
  Macs…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2834
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f0f98552acd58d536c176c3468dc36c0b044dbb04a12c5134d6bd04c2b7395db
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-17-e3e8b0
  comparison: ''
  date: '2026-09-17'
  description: 'Codex CLI — 0.155.0: 24 Apps and Integrations changes'
  evidence:
  - quote: 'Added Touch ID verification for MCP requests in local TUI sessions on
      supported Macs. (#43624, #43712, #43715)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: Aligned Python SDK and runtime publishing with stable CLI releases, using
      matching versions and verifying runtime assets before SDK publication. (#44067)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43524 Restrict MCP user verification and add workspace-scoped identity
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43712 Enable MCP user verification in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43870 Close MCP stderr readers on client teardown @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43900 Propagate Apps tool refreshes to existing threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44032 Generate Python SDK types from repository app-server schemas @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44053 Test Python SDK against the built CLI and installed runtime @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44055 Gate Python SDK publishing on runtime availability and verify PyPI
      files @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44061 Build Python SDK artifacts before publishing the runtime @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44084 Expose Python SDK history selection and per-turn options @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44086 Add untrusted external messages to the Python SDK @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44121 Reuse MCP bindings while cached servers remain dormant @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44238 Fix MCP elicitation cancellation and reset state on reconnect @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44288 Prevent command hooks from hanging on blocked stdin @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44311 Honor shared Retry-After deadlines for remote control @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44318 Give hosted Codex Apps an independent MCP protocol opt-in @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44332 Persist disabled plugin IDs in thread settings @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44346 Support native verification in MCP tool continuations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44349 Distinguish forked sessions in session-start hooks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44400 Start Python SDK turn subscriptions at their attachment point @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44493 Bound MCP descriptions separately from Guardian action JSON @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44548 Add MIME-filtered resource listing for Codex Apps @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44571 Allow extensions to select MCP protocol mode per HTTP server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 24-apps-and-integrations-changes-in-rust-v0-155-0
  source_release: codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512
  source_type: github_releases
  theme: apps-integrations
  title: 24 Apps and Integrations changes in rust-v0.155.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-17-6-apps-and-integrations-changes-in-v2-1-275|6
  Apps and Integrations changes in v2.1.275]]'
- '[[Changes/Claude Code/2026-09-17-added-plugin-install-plugin-marketplace-source-which-offers-to-add-the-marketpla|Added
  /plugin install plugin --marketplace source, which offers to add…]]'
- '[[Changes/Cline/2026-09-17-terminal-commands-that-succeed-without-printing-anything-git-add-a-on-a-clean-tr|Terminal
  commands that succeed without printing anything…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512|codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512]]'
source_type: github_releases
theme: apps-integrations
title: 24 Apps and Integrations changes in rust-v0.155.0
type: change
---

<!-- chronolog:begin region="header" -->
# 24 Apps and Integrations changes in rust-v0.155.0

**Codex CLI** · 2026-09-17 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.155.0) · from [[Releases/Codex CLI/codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512|0.155.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added Touch ID verification for MCP requests in local TUI sessions on supported Macs. (#43624, #43712, #43715)

> Aligned Python SDK and runtime publishing with stable CLI releases, using matching versions and verifying runtime assets before SDK publication. (#44067)

> #43524 Restrict MCP user verification and add workspace-scoped identity @copyberry

> #43712 Enable MCP user verification in the TUI @copyberry

> #43870 Close MCP stderr readers on client teardown @copyberry

> #43900 Propagate Apps tool refreshes to existing threads @copyberry

> #44032 Generate Python SDK types from repository app-server schemas @copyberry

> #44053 Test Python SDK against the built CLI and installed runtime @copyberry

> #44055 Gate Python SDK publishing on runtime availability and verify PyPI files @copyberry

> #44061 Build Python SDK artifacts before publishing the runtime @copyberry

> #44084 Expose Python SDK history selection and per-turn options @copyberry

> #44086 Add untrusted external messages to the Python SDK @copyberry

> #44121 Reuse MCP bindings while cached servers remain dormant @copyberry

> #44238 Fix MCP elicitation cancellation and reset state on reconnect @copyberry

> #44288 Prevent command hooks from hanging on blocked stdin @copyberry

> #44311 Honor shared Retry-After deadlines for remote control @copyberry

> #44318 Give hosted Codex Apps an independent MCP protocol opt-in @copyberry

> #44332 Persist disabled plugin IDs in thread settings @copyberry

> #44346 Support native verification in MCP tool continuations @copyberry

> #44349 Distinguish forked sessions in session-start hooks @copyberry

> #44400 Start Python SDK turn subscriptions at their attachment point @copyberry

> #44493 Bound MCP descriptions separately from Guardian action JSON @copyberry

> #44548 Add MIME-filtered resource listing for Codex Apps @copyberry

> #44571 Allow extensions to select MCP protocol mode per HTTP server @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.155.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-17-7-safety-and-privacy-changes-in-rust-v0-155-0|7 Safety and Privacy changes in rust-v0.155.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-17-43953-preserve-per-image-generation-ids-in-image-generation-analytics-copyberry|♯43953 Preserve per-image generation IDs in image generation analytics @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-09-17-7-memory-and-personalization-changes-in-rust-v0-155-0|7 Memory and Personalization changes in rust-v0.155.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-17-43846-include-completed-commentary-in-the-copy-picker-copyberry|♯43846 Include completed commentary in the /copy picker @copyberry]] · Interface Experience
- [[Changes/Codex CLI/2026-09-17-13-model-support-changes-in-rust-v0-155-0|13 Model Support changes in rust-v0.155.0]] · Model Support
- [[Changes/Codex CLI/2026-09-17-2-editor-experience-changes-in-rust-v0-155-0|2 Editor Experience changes in rust-v0.155.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-17-15-developer-workflow-changes-in-rust-v0-155-0|15 Developer Workflow changes in rust-v0.155.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-17-20-voice-and-audio-changes-in-rust-v0-155-0|20 Voice and Audio changes in rust-v0.155.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-17-2-mobile-and-desktop-changes-in-rust-v0-155-0|2 Mobile and Desktop changes in rust-v0.155.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-17-20-context-window-changes-in-rust-v0-155-0|20 Context Window changes in rust-v0.155.0]] · Context Window
- [[Changes/Codex CLI/2026-09-17-44354-extract-shared-footer-hint-wrapping-in-the-tui-copyberry|♯44354 Extract shared footer hint wrapping in the TUI @copyberry]] · Collaboration
- [[Changes/Codex CLI/2026-09-17-9-agent-mode-changes-in-rust-v0-155-0|9 Agent Mode changes in rust-v0.155.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-17-6-account-and-access-changes-in-rust-v0-155-0|6 Account and Access changes in rust-v0.155.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-17-96-other-changes-in-rust-v0-155-0|96 other changes in rust-v0.155.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-17 · Cline · [[Changes/Cline/2026-09-17-terminal-commands-that-succeed-without-printing-anything-git-add-a-on-a-clean-tr|Terminal commands that succeed without printing anything…]]
- Later: 2026-09-17 · Descript · [[Changes/Descript/2026-09-17-zapier-out-in-public|Zapier, out in public]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-17-e3e8b0&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-17-24-apps-and-integrations-changes-in-rust-v0-155-0.md%0ACard%20ID%3A%20codex-cli-2026-09-17-e3e8b0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.155.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->