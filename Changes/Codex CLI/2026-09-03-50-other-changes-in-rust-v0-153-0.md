---
card_id: codex-cli-2026-09-03-d6f955
date: '2026-09-03'
description: 'Codex CLI · 2026-09-03 · Other changes: 50 changes in 0.153.0 — Vim
  mode now supports undo with `u` and redo with `Ctrl+R`, preserving complete drafts…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6ced2380e9518117fc3e18598bf438ce5ae2c60ffe4820efc352ead35a8acb91
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-03-d6f955
  comparison: ''
  date: '2026-09-03'
  description: 'Codex CLI — 0.153.0: 50 other changes'
  evidence:
  - quote: Vim mode now supports undo with `u` and redo with `Ctrl+R`, preserving
      complete drafts including pasted content and attachments. ([#41941](https://github.com/openai/codex/pull/41941),
      [#42140](https://github.com/openai/codex/pull/42140))
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: Set `tui.auto_recap = false` to disable automatic recaps while keeping
      manual `/recap` available. ([#42101](https://github.com/openai/codex/pull/42101))
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: TUI history shows complete patches, input sent to background terminals,
      and individual completed commands. ([#41893](https://github.com/openai/codex/pull/41893),
      [#42107](https://github.com/openai/codex/pull/42107))
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: TUI sessions reconnect after an external app-server connection drops, preserving
      drafts and transcripts while keeping uncertain or queued submissions paused
      for review. ([#41911](https://github.com/openai/codex/pull/41911), [#41916](https://github.com/openai/codex/pull/41916),
      [#41918](https://github.com/openai/codex/pull/41918))
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: Full Access skips Guardian reviews for confirmation-only actions. User
      approval mode skips background Guardian scoring and prewarming, while sensitive-action
      checks and requests for user input retain their existing handling. ([#42147](https://github.com/openai/codex/pull/42147),
      [#42256](https://github.com/openai/codex/pull/42256))
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '`tui.disable_paste_burst` replaces the top-level setting, which remains
      supported as a fallback. ([#41976](https://github.com/openai/codex/pull/41976))'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[Full Changelog](https://github.com/openai/codex/compare/rust-v0.152.1...rust-v0.153.0)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41893](https://github.com/openai/codex/pull/41893) Show successful TUI
      commands individually'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41908](https://github.com/openai/codex/pull/41908) Avoid scanning archived
      rollouts when archiving threads'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41911](https://github.com/openai/codex/pull/41911) Preserve TUI drafts
      after app-server disconnects'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41912](https://github.com/openai/codex/pull/41912) Persist response
      token usage in rollout history'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41913](https://github.com/openai/codex/pull/41913) Preserve TUI status
      timing when the status row is hidden'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41915](https://github.com/openai/codex/pull/41915) Move the config schema
      generator into a dedicated crate'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41916](https://github.com/openai/codex/pull/41916) Reconnect TUI app-server
      sessions automatically'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41923](https://github.com/openai/codex/pull/41923) Allow per-call sideband
      endpoints for existing realtime calls'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41924](https://github.com/openai/codex/pull/41924) Record realtime conversation
      history in Core'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41925](https://github.com/openai/codex/pull/41925) Test repository-wide
      Rust formatter discovery'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41934](https://github.com/openai/codex/pull/41934) Omit undersized WAV
      output from Code Mode'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41936](https://github.com/openai/codex/pull/41936) Attach failed Guardian
      reviews to diagnostic reports'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41938](https://github.com/openai/codex/pull/41938) Clarify resume guidance
      in exit summaries'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41941](https://github.com/openai/codex/pull/41941) Add Vim undo to the
      TUI composer'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41950](https://github.com/openai/codex/pull/41950) Improve tracing for
      nested tool calls and exec processes'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41974](https://github.com/openai/codex/pull/41974) Track TUI starts
      by app server mode'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41976](https://github.com/openai/codex/pull/41976) Move `disable_paste_burst`
      under `[tui]`'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#41980](https://github.com/openai/codex/pull/41980) Preserve raw response
      usage metadata'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42003](https://github.com/openai/codex/pull/42003) Report turn trigger
      and source in turn analytics'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42033](https://github.com/openai/codex/pull/42033) Improve Guardian
      report diagnostics'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42043](https://github.com/openai/codex/pull/42043) Tag Codex home size
      metrics with compression state'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42065](https://github.com/openai/codex/pull/42065) Preserve Guardian
      history across thread reconstruction'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42066](https://github.com/openai/codex/pull/42066) Remove selected core
      test cases'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42069](https://github.com/openai/codex/pull/42069) Remove redundant
      test coverage'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42071](https://github.com/openai/codex/pull/42071) Detect Vite+-managed
      Codex installs'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42082](https://github.com/openai/codex/pull/42082) Attribute nested
      REPL reviews to their tool calls'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42086](https://github.com/openai/codex/pull/42086) Attribute Guardian
      reviews to OpenAI app tools'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42094](https://github.com/openai/codex/pull/42094) Record Windows MXC
      availability'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42096](https://github.com/openai/codex/pull/42096) Make diagnostic report
      uploads resilient to slow networks'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42101](https://github.com/openai/codex/pull/42101) Add a TUI setting
      to disable automatic recaps'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42102](https://github.com/openai/codex/pull/42102) Extract OTEL trace
      WebSocket into a reusable crate'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42109](https://github.com/openai/codex/pull/42109) Format Python scripts
      across the repository'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42121](https://github.com/openai/codex/pull/42121) Allow updating the
      approval reviewer for active turns'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42123](https://github.com/openai/codex/pull/42123) Preserve descriptive
      labels on local file links'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42135](https://github.com/openai/codex/pull/42135) Support thread forks
      from symlinked session roots'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42144](https://github.com/openai/codex/pull/42144) Add Guardian V2 analytics
      events'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42147](https://github.com/openai/codex/pull/42147) Skip Guardian reviews
      in Full Access'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42161](https://github.com/openai/codex/pull/42161) Split tool JSON Schema
      code into focused modules'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42164](https://github.com/openai/codex/pull/42164) Record result sources
      in app tool analytics'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42173](https://github.com/openai/codex/pull/42173) Support header injections
      in network requirements'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42174](https://github.com/openai/codex/pull/42174) Add a cacheable Bazel
      app-server schema bundle'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42178](https://github.com/openai/codex/pull/42178) Add structured asynchronous
      user input requests'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42256](https://github.com/openai/codex/pull/42256) Skip Guardian scoring
      in User approval mode'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 50-other-changes-in-rust-v0-153-0
  source_release: codex-cli-2026-09-03-rust-v0-153-0-github-381669913-72d3437f
  source_type: github_releases
  theme: uncategorized
  title: 50 other changes in rust-v0.153.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-03-rust-v0-153-0-github-381669913-72d3437f|codex-cli-2026-09-03-rust-v0-153-0-github-381669913-72d3437f]]'
source_type: github_releases
theme: uncategorized
title: 50 other changes in rust-v0.153.0
type: change
---

<!-- chronolog:begin region="header" -->
# 50 other changes in rust-v0.153.0

**Codex CLI** · 2026-09-03 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.153.0) · from [[Releases/Codex CLI/codex-cli-2026-09-03-rust-v0-153-0-github-381669913-72d3437f|0.153.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Vim mode now supports undo with `u` and redo with `Ctrl+R`, preserving complete drafts including pasted content and attachments. ([#41941](https://github.com/openai/codex/pull/41941), [#42140](https://github.com/openai/codex/pull/42140))

> Set `tui.auto_recap = false` to disable automatic recaps while keeping manual `/recap` available. ([#42101](https://github.com/openai/codex/pull/42101))

> TUI history shows complete patches, input sent to background terminals, and individual completed commands. ([#41893](https://github.com/openai/codex/pull/41893), [#42107](https://github.com/openai/codex/pull/42107))

> TUI sessions reconnect after an external app-server connection drops, preserving drafts and transcripts while keeping uncertain or queued submissions paused for review. ([#41911](https://github.com/openai/codex/pull/41911), [#41916](https://github.com/openai/codex/pull/41916), [#41918](https://github.com/openai/codex/pull/41918))

> Full Access skips Guardian reviews for confirmation-only actions. User approval mode skips background Guardian scoring and prewarming, while sensitive-action checks and requests for user input retain their existing handling. ([#42147](https://github.com/openai/codex/pull/42147), [#42256](https://github.com/openai/codex/pull/42256))

> `tui.disable_paste_burst` replaces the top-level setting, which remains supported as a fallback. ([#41976](https://github.com/openai/codex/pull/41976))

> [Full Changelog](https://github.com/openai/codex/compare/rust-v0.152.1...rust-v0.153.0)

> [#41893](https://github.com/openai/codex/pull/41893) Show successful TUI commands individually

> [#41908](https://github.com/openai/codex/pull/41908) Avoid scanning archived rollouts when archiving threads

> [#41911](https://github.com/openai/codex/pull/41911) Preserve TUI drafts after app-server disconnects

> [#41912](https://github.com/openai/codex/pull/41912) Persist response token usage in rollout history

> [#41913](https://github.com/openai/codex/pull/41913) Preserve TUI status timing when the status row is hidden

> [#41915](https://github.com/openai/codex/pull/41915) Move the config schema generator into a dedicated crate

> [#41916](https://github.com/openai/codex/pull/41916) Reconnect TUI app-server sessions automatically

> [#41923](https://github.com/openai/codex/pull/41923) Allow per-call sideband endpoints for existing realtime calls

> [#41924](https://github.com/openai/codex/pull/41924) Record realtime conversation history in Core

> [#41925](https://github.com/openai/codex/pull/41925) Test repository-wide Rust formatter discovery

> [#41934](https://github.com/openai/codex/pull/41934) Omit undersized WAV output from Code Mode

> [#41936](https://github.com/openai/codex/pull/41936) Attach failed Guardian reviews to diagnostic reports

> [#41938](https://github.com/openai/codex/pull/41938) Clarify resume guidance in exit summaries

> [#41941](https://github.com/openai/codex/pull/41941) Add Vim undo to the TUI composer

> [#41950](https://github.com/openai/codex/pull/41950) Improve tracing for nested tool calls and exec processes

> [#41974](https://github.com/openai/codex/pull/41974) Track TUI starts by app server mode

> [#41976](https://github.com/openai/codex/pull/41976) Move `disable_paste_burst` under `[tui]`

> [#41980](https://github.com/openai/codex/pull/41980) Preserve raw response usage metadata

> [#42003](https://github.com/openai/codex/pull/42003) Report turn trigger and source in turn analytics

> [#42033](https://github.com/openai/codex/pull/42033) Improve Guardian report diagnostics

> [#42043](https://github.com/openai/codex/pull/42043) Tag Codex home size metrics with compression state

> [#42065](https://github.com/openai/codex/pull/42065) Preserve Guardian history across thread reconstruction

> [#42066](https://github.com/openai/codex/pull/42066) Remove selected core test cases

> [#42069](https://github.com/openai/codex/pull/42069) Remove redundant test coverage

> [#42071](https://github.com/openai/codex/pull/42071) Detect Vite+-managed Codex installs

> [#42082](https://github.com/openai/codex/pull/42082) Attribute nested REPL reviews to their tool calls

> [#42086](https://github.com/openai/codex/pull/42086) Attribute Guardian reviews to OpenAI app tools

> [#42094](https://github.com/openai/codex/pull/42094) Record Windows MXC availability

> [#42096](https://github.com/openai/codex/pull/42096) Make diagnostic report uploads resilient to slow networks

> [#42101](https://github.com/openai/codex/pull/42101) Add a TUI setting to disable automatic recaps

> [#42102](https://github.com/openai/codex/pull/42102) Extract OTEL trace WebSocket into a reusable crate

> [#42109](https://github.com/openai/codex/pull/42109) Format Python scripts across the repository

> [#42121](https://github.com/openai/codex/pull/42121) Allow updating the approval reviewer for active turns

> [#42123](https://github.com/openai/codex/pull/42123) Preserve descriptive labels on local file links

> [#42135](https://github.com/openai/codex/pull/42135) Support thread forks from symlinked session roots

> [#42144](https://github.com/openai/codex/pull/42144) Add Guardian V2 analytics events

> [#42147](https://github.com/openai/codex/pull/42147) Skip Guardian reviews in Full Access

> [#42161](https://github.com/openai/codex/pull/42161) Split tool JSON Schema code into focused modules

> [#42164](https://github.com/openai/codex/pull/42164) Record result sources in app tool analytics

> [#42173](https://github.com/openai/codex/pull/42173) Support header injections in network requirements

> [#42174](https://github.com/openai/codex/pull/42174) Add a cacheable Bazel app-server schema bundle

> [#42178](https://github.com/openai/codex/pull/42178) Add structured asynchronous user input requests

> [#42256](https://github.com/openai/codex/pull/42256) Skip Guardian scoring in User approval mode

Source: https://github.com/openai/codex/releases/tag/rust-v0.153.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-03-42140-https-github-com-openai-codex-pull-42140-add-redo-support-to-vim-composer|♯42140((source link) Add redo support to Vim…]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-09-03-3-interface-experience-changes-in-rust-v0-153-0|3 Interface Experience changes in rust-v0.153.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-03-2-model-support-changes-in-rust-v0-153-0|2 Model Support changes in rust-v0.153.0]] · Model Support
- [[Changes/Codex CLI/2026-09-03-5-voice-and-audio-changes-in-rust-v0-153-0|5 Voice and Audio changes in rust-v0.153.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-03-42128-https-github-com-openai-codex-pull-42128-prepare-mcp-connections-for-coord|♯42128((source link) Prepare MCP connections…]] · Account and Access
- [[Changes/Codex CLI/2026-09-03-5-developer-workflow-changes-in-rust-v0-153-0|5 Developer Workflow changes in rust-v0.153.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-03-6-safety-and-privacy-changes-in-rust-v0-153-0|6 Safety and Privacy changes in rust-v0.153.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-03-41944-https-github-com-openai-codex-pull-41944-emit-turn-cost-telemetry-for-chat|♯41944((source link) Emit turn cost telemetry…]] · Pricing Model
- [[Changes/Codex CLI/2026-09-03-6-context-window-changes-in-rust-v0-153-0|6 Context Window changes in rust-v0.153.0]] · Context Window
- [[Changes/Codex CLI/2026-09-03-6-collaboration-changes-in-rust-v0-153-0|6 Collaboration changes in rust-v0.153.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-03-4-agent-mode-changes-in-rust-v0-153-0|4 Agent Mode changes in rust-v0.153.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-03-42068-https-github-com-openai-codex-pull-42068-detect-standalone-installs-from-t|♯42068((source link) Detect standalone installs…]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-03-18-apps-and-integrations-changes-in-rust-v0-153-0|18 Apps and Integrations changes in rust-v0.153.0]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-03-d6f955&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-03-50-other-changes-in-rust-v0-153-0.md%0ACard%20ID%3A%20codex-cli-2026-09-03-d6f955%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.153.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->