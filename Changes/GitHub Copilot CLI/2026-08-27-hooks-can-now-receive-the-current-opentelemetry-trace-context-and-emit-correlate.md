---
card_id: github-copilot-cli-2026-08-27-5ebed9
date: '2026-08-27'
description: 'GitHub Copilot CLI · 2026-08-27 · Context Window: Hooks can now receive
  the current OpenTelemetry trace context and emit correlated spans: inputs gain…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2535
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 064fcfec1a333e61ec1c3218b3d993886334921488d9ec18a2a8a7d02306b4b8
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-08-27-5ebed9
  comparison: ''
  date: '2026-08-27'
  description: 'GitHub Copilot CLI — 1.0.81: Hooks can now receive the current OpenTelemetry
    trace context and emit correlated spans: inputs gain `traceparent` (plus `tracestate`
    when the span has vendor state); command hooks also get env vars.'
  evidence:
  - quote: 'Hooks can now receive the current OpenTelemetry trace context and emit
      correlated spans: inputs gain `traceparent` (plus `tracestate` when the span
      has vendor state); command hooks also get env vars.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: hooks-can-now-receive-the-current-opentelemetry-trace-context-and-emit-correlate
  source_release: github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a
  source_type: github_releases
  theme: context-window
  title: Hooks can now receive the current OpenTelemetry trace context and emit correlated
    spans
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-08-26-14-context-window-changes-in-rust-v0-150-0|14 Context
  Window changes in rust-v0.150.0]]'
- '[[Changes/Claude Code/2026-08-27-improved-the-workflow-tool-s-prompt-footprint-its-description-is-now-about-1k-to|Improved
  the Workflow tool''s prompt footprint]]'
- '[[Changes/Codex CLI/2026-08-27-2-context-window-changes-in-rust-v0-150-1|2 Context
  Window changes in rust-v0.150.1]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a|github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a]]'
source_type: github_releases
theme: context-window
title: Hooks can now receive the current OpenTelemetry trace context and emit correlated
  spans
type: change
---

<!-- chronolog:begin region="header" -->
# Hooks can now receive the current OpenTelemetry trace context and emit correlated spans

**GitHub Copilot CLI** · 2026-08-27 · [[Themes/context-window|Context Window]] · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.81) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a|1.0.81]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Hooks can now receive the current OpenTelemetry trace context and emit correlated spans: inputs gain `traceparent` (plus `tracestate` when the span has vendor state); command hooks also get env vars.
>
> Source: https://github.com/github/copilot-cli/releases/tag/v1.0.81
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-08-27-resume-large-sessions-faster-by-showing-recent-history-first-while-older-message|Resume large sessions faster by showing recent history first while older messages load]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-08-27-2-enterprise-and-administration-changes-in-v1-0-81|2 Enterprise and Administration changes in v1.0.81]] · Enterprise and Administration
- [[Changes/GitHub Copilot CLI/2026-08-27-sandboxed-builds-on-windows-create-their-scratch-caches-on-first-run-so-cargo-go|Sandboxed builds on Windows create their scratch caches on first run, so cargo, go…]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-08-27-5-developer-workflow-changes-in-v1-0-81|5 Developer Workflow changes in v1.0.81]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-08-27-3-interface-experience-changes-in-v1-0-81|3 Interface Experience changes in v1.0.81]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-08-27-12-apps-and-integrations-changes-in-v1-0-81|12 Apps and Integrations changes in v1.0.81]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-08-27-8-agent-mode-changes-in-v1-0-81|8 Agent Mode changes in v1.0.81]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-08-27-ship-mcp-2026-07-28-support-to-cli-sdk-ide-and-in-memory-clients|Ship MCP 2026-07-28 support to CLI, SDK, IDE, and in-memory clients]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-08-27-add-copilot-app-to-open-the-github-copilot-app-in-the-current-directory|Add copilot app to open the GitHub Copilot app in the current directory]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-08-27-2-account-and-access-changes-in-v1-0-81|2 Account and Access changes in v1.0.81]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-08-27-use-x-to-remove-scheduled-every-and-after-prompts-in-schedule-manager|Use x to remove scheduled /every and /after prompts in Schedule Manager]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-08-27-canvas-windows-open-and-refresh-in-the-background-instead-of-stealing-focus-from|Canvas windows open and refresh in the background instead of stealing focus…]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-08-27-4-model-support-changes-in-v1-0-81|4 Model Support changes in v1.0.81]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-08-27-5-safety-and-privacy-changes-in-v1-0-81|5 Safety and Privacy changes in v1.0.81]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-08-27-use-ctrl-space-to-toggle-voice-dictation|Use Ctrl+Space to toggle voice dictation]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-08-27-6-other-changes-in-v1-0-81|6 other changes in v1.0.81]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-08-27 · Codex CLI · [[Changes/Codex CLI/2026-08-27-2-context-window-changes-in-rust-v0-150-1|2 Context Window changes in rust-v0.150.1]]
- Later: 2026-08-28 · Claude Code · [[Changes/Claude Code/2026-08-28-improved-retry-when-the-model-s-tool-call-is-malformed-the-broken-output-is-now|Improved retry when the model's tool call is malformed]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-08-27-5ebed9&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-08-27-hooks-can-now-receive-the-current-opentelemetry-trace-context-and-emit-correlate.md%0ACard%20ID%3A%20github-copilot-cli-2026-08-27-5ebed9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.81%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->