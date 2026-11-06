---
card_id: github-copilot-cli-2026-08-27-38e301
date: '2026-08-27'
description: 'GitHub Copilot CLI · 2026-08-27 · Developer Workflow: 5 changes in 1.0.81
  — Startup now offers to restore sessions that were still open when their CLI went…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1258
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9c7bc63c3e32d5388454544fbd65629ad3621e3b739f5fa32890c3a1a81a76b6
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-08-27-38e301
  comparison: ''
  date: '2026-08-27'
  description: 'GitHub Copilot CLI — 1.0.81: 5 Developer Workflow changes'
  evidence:
  - quote: Startup now offers to restore sessions that were still open when their
      CLI went away, so a crash or a machine restart no longer means reopening each
      terminal by hand
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: On macOS and Linux, shell commands resolve the same tools a bash login
      shell does, including project environments activated from a profile
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: Typing `$` and pressing Enter opens the interactive shell again, instead
      of clearing the prompt and doing nothing
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: 'Keys sent to an unfocused terminal pane are no longer dropped: Enter and
      other keystrokes are handled even after a terminal focus-out report, so tmux
      and agent multiplexers can drive a background pane'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: Compact the autopilot goal panel to its identity row on a short terminal
      (a paused goal keeps its resume note), with ctrl+x → g to expand or collapse
      it by hand
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 5-developer-workflow-changes-in-v1-0-81
  source_release: github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a
  source_type: github_releases
  theme: developer-workflow
  title: 5 Developer Workflow changes in v1.0.81
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-26-changed-terminal-hyperlinks-in-rendered-markdown-link-targets-that-point-at-a-ne|Changed
  terminal hyperlinks in rendered markdown]]'
- '[[Changes/Codex CLI/2026-08-26-15-developer-workflow-changes-in-rust-v0-150-0|15
  Developer Workflow changes in rust-v0.150.0]]'
- '[[Changes/Claude Code/2026-08-27-changed-anthropic-telemetry-export-failures-to-log-at-debug-level-as-anthropic-t|Changed
  Anthropic telemetry export failures to log at debug level…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a|github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a]]'
source_type: github_releases
theme: developer-workflow
title: 5 Developer Workflow changes in v1.0.81
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Developer Workflow changes in v1.0.81

**GitHub Copilot CLI** · 2026-08-27 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.81) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a|1.0.81]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Startup now offers to restore sessions that were still open when their CLI went away, so a crash or a machine restart no longer means reopening each terminal by hand

> On macOS and Linux, shell commands resolve the same tools a bash login shell does, including project environments activated from a profile

> Typing `$` and pressing Enter opens the interactive shell again, instead of clearing the prompt and doing nothing

> Keys sent to an unfocused terminal pane are no longer dropped: Enter and other keystrokes are handled even after a terminal focus-out report, so tmux and agent multiplexers can drive a background pane

> Compact the autopilot goal panel to its identity row on a short terminal (a paused goal keeps its resume note), with ctrl+x → g to expand or collapse it by hand

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.81
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-08-27-resume-large-sessions-faster-by-showing-recent-history-first-while-older-message|Resume large sessions faster by showing recent history first while older messages load]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-08-27-2-enterprise-and-administration-changes-in-v1-0-81|2 Enterprise and Administration changes in v1.0.81]] · Enterprise and Administration
- [[Changes/GitHub Copilot CLI/2026-08-27-sandboxed-builds-on-windows-create-their-scratch-caches-on-first-run-so-cargo-go|Sandboxed builds on Windows create their scratch caches on first run, so cargo, go…]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-08-27-3-interface-experience-changes-in-v1-0-81|3 Interface Experience changes in v1.0.81]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-08-27-12-apps-and-integrations-changes-in-v1-0-81|12 Apps and Integrations changes in v1.0.81]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-08-27-8-agent-mode-changes-in-v1-0-81|8 Agent Mode changes in v1.0.81]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-08-27-hooks-can-now-receive-the-current-opentelemetry-trace-context-and-emit-correlate|Hooks can now receive the current OpenTelemetry trace context and emit correlated spans]] · Context Window
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
## Nearby in Developer Workflow

- Earlier: 2026-08-27 · Claude Code · [[Changes/Claude Code/2026-08-27-changed-anthropic-telemetry-export-failures-to-log-at-debug-level-as-anthropic-t|Changed Anthropic telemetry export failures to log at debug level…]]
- Later: 2026-08-28 · Claude Code · [[Changes/Claude Code/2026-08-28-3-developer-workflow-changes-in-v2-1-251|3 Developer Workflow changes in v2.1.251]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-08-27-38e301&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-08-27-5-developer-workflow-changes-in-v1-0-81.md%0ACard%20ID%3A%20github-copilot-cli-2026-08-27-38e301%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.81%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->