---
card_id: github-copilot-cli-2026-03-26-551096
date: '2026-03-26'
description: 'GitHub Copilot CLI · 2026-03-26 · Other changes: 12 changes in 1.0.12
  — /session rename auto-generates a session name from conversation history when called…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3cc1a60e488b7eaccb65777b81faa791f9a873e2f474b3965985e62f8f533720
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-03-26-551096
  comparison: ''
  date: '2026-03-26'
  description: 'GitHub Copilot CLI — 1.0.12: 12 other changes'
  evidence:
  - quote: /session rename auto-generates a session name from conversation history
      when called without a name argument
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.12
  - quote: Remove --alt-screen flag and alt_screen setting; alt screen is now always
      enabled
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.12
  - quote: OSC 8 hyperlinks are now clickable in VS Code terminals
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.12
  - quote: PowerShell /flag arguments (e.g., /all, /enum-devices) are no longer mistakenly
      treated as file paths
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.12
  - quote: /yolo path permissions persist after using /clear to start a new session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.12
  - quote: Sessions with active work are no longer cleaned up by the stale session
      reaper
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.12
  - quote: Pressing Escape multiple times during autopilot cancellation no longer
      leaves the session stuck
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.12
  - quote: Read .claude/settings.json and .claude/settings.local.json as additional
      repo config sources
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.12
  - quote: OTEL hook executions are now recorded as span events instead of child spans,
      reducing trace clutter
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.12
  - quote: User prompt appears in the conversation immediately after pressing Enter
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.12
  - quote: /allow-all (/yolo) now supports on, off, and show subcommands to enable,
      disable, or check allow-all mode
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.12
  - quote: Ctrl+Y in plan mode opens the most recent research report when no plan
      exists yet
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.12
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 12-other-changes-in-v1-0-12
  source_release: github-copilot-cli-2026-03-26-v1-0-12-github-302121824-04d76a7e
  source_type: github_releases
  theme: uncategorized
  title: 12 other changes in v1.0.12
  type: change
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-26-v1-0-12-github-302121824-04d76a7e|github-copilot-cli-2026-03-26-v1-0-12-github-302121824-04d76a7e]]'
source_type: github_releases
theme: uncategorized
title: 12 other changes in v1.0.12
type: change
---

<!-- chronolog:begin region="header" -->
# 12 other changes in v1.0.12

**GitHub Copilot CLI** · 2026-03-26 · Other changes · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.12) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-26-v1-0-12-github-302121824-04d76a7e|1.0.12]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> /session rename auto-generates a session name from conversation history when called without a name argument

> Remove --alt-screen flag and alt_screen setting; alt screen is now always enabled

> OSC 8 hyperlinks are now clickable in VS Code terminals

> PowerShell /flag arguments (e.g., /all, /enum-devices) are no longer mistakenly treated as file paths

> /yolo path permissions persist after using /clear to start a new session

> Sessions with active work are no longer cleaned up by the stale session reaper

> Pressing Escape multiple times during autopilot cancellation no longer leaves the session stuck

> Read .claude/settings.json and .claude/settings.local.json as additional repo config sources

> OTEL hook executions are now recorded as span events instead of child spans, reducing trace clutter

> User prompt appears in the conversation immediately after pressing Enter

> /allow-all (/yolo) now supports on, off, and show subcommands to enable, disable, or check allow-all mode

> Ctrl+Y in plan mode opens the most recent research report when no plan exists yet

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.12
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-03-26-3-interface-experience-changes-in-v1-0-12|3 Interface Experience changes in v1.0.12]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-03-26-diff-view-correctly-renders-all-lines-when-intra-line-highlighting-is-present|/diff view correctly renders all lines when intra-line highlighting is present]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-03-26-cli-no-longer-crashes-with-out-of-memory-errors-when-running-shell-commands-that|CLI no longer crashes with out-of-memory errors when running shell commands…]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-03-26-resume-session-restores-the-previously-selected-custom-agent|Resume session restores the previously selected custom agent]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-03-26-4-apps-and-integrations-changes-in-v1-0-12|4 Apps and Integrations changes in v1.0.12]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-03-26-model-display-header-shows-the-active-reasoning-effort-level-e-g-high-next-to-th|Model display header shows the active reasoning effort level (e.g. "(high)") next…]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-03-26-2-mobile-and-desktop-changes-in-v1-0-12|2 Mobile and Desktop changes in v1.0.12]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-03-26-2-developer-workflow-changes-in-v1-0-12|2 Developer Workflow changes in v1.0.12]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-03-26-551096&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-03-26-12-other-changes-in-v1-0-12.md%0ACard%20ID%3A%20github-copilot-cli-2026-03-26-551096%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.12%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->