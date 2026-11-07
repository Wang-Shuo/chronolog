---
card_id: github-copilot-cli-2026-06-13-f625a8
date: '2026-06-13'
description: 'GitHub Copilot CLI · 2026-06-13 · Developer Workflow: 6 changes in 1.0.62
  — Shell tool errors now explain when a shell ID was stopped, completed, or reclaimed'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1183
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7692847defe1f8e02256b6b7b078860e7a385c4d7d124f56fd024d9cd185db9c
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-13-f625a8
  comparison: ''
  date: '2026-06-13'
  description: 'GitHub Copilot CLI — 1.0.62: 6 Developer Workflow changes'
  evidence:
  - quote: Shell tool errors now explain when a shell ID was stopped, completed, or
      reclaimed
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  - quote: Show 'YOLO' (allow all) indicator in the footer and add allow-all state
      to custom statusLine.command
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  - quote: Terminal colors update live when the active theme changes mid-session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  - quote: Nested subagents respect concurrency limits without blocking terminal input
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  - quote: Press W to create a worktree from the expanded issue or pull request details
      view
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  - quote: Shell commands run via lightweight process spawning instead of a pseudo-terminal;
      interactive input via write_bash is no longer supported
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 6-developer-workflow-changes-in-v1-0-62
  source_release: github-copilot-cli-2026-06-13-v1-0-62-github-339039020-f6ff7e5e
  source_type: github_releases
  theme: developer-workflow
  title: 6 Developer Workflow changes in v1.0.62
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-10-2-developer-workflow-changes-in-v2-1-172|2 Developer
  Workflow changes in v2.1.172]]'
- '[[Changes/OpenCode/2026-06-10-6-developer-workflow-changes-in-v1-17-0|6 Developer
  Workflow changes in v1.17.0]]'
- '[[Changes/OpenCode/2026-06-12-core-snapshot-creation-now-reuses-source-git-objects-to-avoid-long-re-hashing-de|Core
  Snapshot creation now reuses source Git objects to avoid long re-hashing delays…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-13-v1-0-62-github-339039020-f6ff7e5e|github-copilot-cli-2026-06-13-v1-0-62-github-339039020-f6ff7e5e]]'
source_type: github_releases
theme: developer-workflow
title: 6 Developer Workflow changes in v1.0.62
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Developer Workflow changes in v1.0.62

**GitHub Copilot CLI** · 2026-06-13 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.62) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-13-v1-0-62-github-339039020-f6ff7e5e|1.0.62]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Shell tool errors now explain when a shell ID was stopped, completed, or reclaimed

> Show 'YOLO' (allow all) indicator in the footer and add allow-all state to custom statusLine.command

> Terminal colors update live when the active theme changes mid-session

> Nested subagents respect concurrency limits without blocking terminal input

> Press W to create a worktree from the expanded issue or pull request details view

> Shell commands run via lightweight process spawning instead of a pseudo-terminal; interactive input via write_bash is no longer supported

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.62
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-13-8-apps-and-integrations-changes-in-v1-0-62|8 Apps and Integrations changes in v1.0.62]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-13-speed-up-branch-and-head-detection-in-warm-sessions|Speed up branch and HEAD detection in warm sessions]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-13-4-agent-mode-changes-in-v1-0-62|4 Agent Mode changes in v1.0.62]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-13-every-and-after-can-now-schedule-slash-commands-e-g-every-1d-chronicle-standup|/every and /after can now schedule slash commands (e.g. /every 1d /chronicle standup)]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-13-voice-runtime-download-dialog-no-longer-reopens-in-a-loop-after-an-install-failu|Voice runtime download dialog no longer reopens in a loop after an install failure]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-06-13-2-safety-and-privacy-changes-in-v1-0-62|2 Safety and Privacy changes in v1.0.62]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-13-2-editor-experience-changes-in-v1-0-62|2 Editor Experience changes in v1.0.62]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-13-honor-max-output-tokens-for-byok-responses-providers|Honor max_output_tokens for BYOK Responses providers]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-06-13-remote-mcp-oauth-servers-start-only-once-per-matching-config-instead-of-restarti|Remote MCP OAuth servers start only once per matching config instead of restarting…]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-13-git-commands-no-longer-flash-a-console-window-on-windows|Git commands no longer flash a console window on Windows]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-06-13-allow-sdk-clients-to-configure-session-memory-through-session-create-and-session|Allow SDK clients to configure session memory through session.create and session.resume]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-06-13-3-interface-experience-changes-in-v1-0-62|3 Interface Experience changes in v1.0.62]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-13-3-model-support-changes-in-v1-0-62|3 Model Support changes in v1.0.62]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-13-improve-color-contrast-in-github-themes-to-meet-wcag-aa-accessibility-standards|Improve color contrast in GitHub themes to meet WCAG AA accessibility standards]] · Accessibility and Localization
- [[Changes/GitHub Copilot CLI/2026-06-13-14-other-changes-in-v1-0-62|14 other changes in v1.0.62]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-06-12 · OpenCode · [[Changes/OpenCode/2026-06-12-core-snapshot-creation-now-reuses-source-git-objects-to-avoid-long-re-hashing-de|Core Snapshot creation now reuses source Git objects to avoid long re-hashing delays…]]
- Later: 2026-06-13 · OpenCode · [[Changes/OpenCode/2026-06-13-2-developer-workflow-changes-in-v1-17-6-1|2 Developer Workflow changes in v1.17.6 + 1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-13-f625a8&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-13-6-developer-workflow-changes-in-v1-0-62.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-13-f625a8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.62%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->