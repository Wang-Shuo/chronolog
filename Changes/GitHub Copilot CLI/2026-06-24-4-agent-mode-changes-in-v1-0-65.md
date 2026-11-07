---
card_id: github-copilot-cli-2026-06-24-ce3a41
date: '2026-06-24'
description: 'GitHub Copilot CLI · 2026-06-24 · Agent Mode: 4 changes in 1.0.65 —
  /cd now persists the working directory so resuming a session returns to it, and
  discovers…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1084
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0ec399bdacb390c9d07ff996af36ce7325bd99b48362a43c7b9c840c9953d3c2
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-24-ce3a41
  comparison: ''
  date: '2026-06-24'
  description: 'GitHub Copilot CLI — 1.0.65: 4 Agent Mode changes'
  evidence:
  - quote: /cd now persists the working directory so resuming a session returns to
      it, and discovers custom agents in the new directory
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.65
  - quote: Prevent brief console windows from flashing on Windows when the agent runs
      hook commands or resolves command paths
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.65
  - quote: Keep custom-agent subagent model selections when using BYOK providers
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.65
  - quote: Up/down history and Ctrl+R reverse search now include past shell commands
      while in normal mode, so you can recall and re-run a shell command without first
      typing ! to enter shell mode
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.65
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 4-agent-mode-changes-in-v1-0-65
  source_release: github-copilot-cli-2026-06-24-v1-0-65-github-344381970-307a94bd
  source_type: github_releases
  theme: agent-mode
  title: 4 Agent Mode changes in v1.0.65
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-06-22-new-entries-in-the-sensitive-paths-list-vscode-and-cache-are-now-recognized-as-s|New
  entries in the sensitive paths list]]'
- '[[Changes/Kimi Code/2026-06-22-allow-long-running-foreground-commands-and-subagents-to-be-moved-into-background|Allow
  long-running foreground commands and subagents to be moved into background…]]'
- '[[Changes/GitHub Copilot CLI/2026-06-23-6-agent-mode-changes-in-v1-0-64|6 Agent
  Mode changes in v1.0.64]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-24-v1-0-65-github-344381970-307a94bd|github-copilot-cli-2026-06-24-v1-0-65-github-344381970-307a94bd]]'
source_type: github_releases
theme: agent-mode
title: 4 Agent Mode changes in v1.0.65
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in v1.0.65

**GitHub Copilot CLI** · 2026-06-24 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.65) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-24-v1-0-65-github-344381970-307a94bd|1.0.65]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> /cd now persists the working directory so resuming a session returns to it, and discovers custom agents in the new directory

> Prevent brief console windows from flashing on Windows when the agent runs hook commands or resolves command paths

> Keep custom-agent subagent model selections when using BYOK providers

> Up/down history and Ctrl+R reverse search now include past shell commands while in normal mode, so you can recall and re-run a shell command without first typing ! to enter shell mode

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.65
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-24-add-a-copilot-skill-subcommand-and-a-skill-alias-for-skills-to-list-add-and-remo|Add a copilot skill subcommand (and a /skill alias for /skills) to list, add…]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-24-commands-with-slash-prefixed-string-arguments-e-g-body-azp-run-no-longer-trigger|Commands with slash-prefixed string arguments (e.g. --body "/azp run") no longer…]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-24-2-apps-and-integrations-changes-in-v1-0-65|2 Apps and Integrations changes in v1.0.65]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-24-2-interface-experience-changes-in-v1-0-65|2 Interface Experience changes in v1.0.65]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-24-handle-wakeup-misfires-with-a-graceful-message-when-no-self-paced-schedule-is-ac|Handle wakeup misfires with a graceful message when no self-paced schedule is active]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-24-silent-mcp-oauth-refresh-reuses-the-granted-scope-so-reconnects-stay-signed-in|Silent MCP OAuth refresh reuses the granted scope so reconnects stay signed in]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-24-remove-syntax-highlighting-from-shell-commands-in-the-timeline|Remove syntax highlighting from shell commands in the timeline]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-24-2-model-support-changes-in-v1-0-65|2 Model Support changes in v1.0.65]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-24-7-other-changes-in-v1-0-65|7 other changes in v1.0.65]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-06-23 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-23-6-agent-mode-changes-in-v1-0-64|6 Agent Mode changes in v1.0.64]]
- Later: 2026-06-25 · Claude Code · [[Changes/Claude Code/2026-06-25-3-agent-mode-changes-in-v2-1-193|3 Agent Mode changes in v2.1.193]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-24-ce3a41&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-24-4-agent-mode-changes-in-v1-0-65.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-24-ce3a41%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.65%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->