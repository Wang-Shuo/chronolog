---
card_id: github-copilot-cli-2026-07-20-d2514c
date: '2026-07-20'
description: 'GitHub Copilot CLI · 2026-07-20 · Safety and Privacy: 4 changes in 1.0.72
  — Add opt-in git and gh authentication inside the OS sandbox'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1191
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d4cd666cccb10e3d77ca514508ce6b8bb1167cfad78d7c2d9a052a219438e2b1
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-07-20-d2514c
  comparison: ''
  date: '2026-07-20'
  description: 'GitHub Copilot CLI — 1.0.72: 4 Safety and Privacy changes'
  evidence:
  - quote: Add opt-in git and gh authentication inside the OS sandbox
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Sandbox macOS keychain access now defaults off for tighter isolation; re-enable
      it in /sandbox if a command needs it
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Toggling /sandbox restarts only local MCP servers and leaves remote servers
      connected
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Modified vim keys (Ctrl+K, uppercase J/K) no longer move the selection
      in tool-permission prompts and other text-input select menus; only unmodified
      j/k, the arrow keys, and Ctrl+P/Ctrl+N navigate.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 4-safety-and-privacy-changes-in-v1-0-72
  source_release: github-copilot-cli-2026-07-20-v1-0-72-github-356903706-84b07b91
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in v1.0.72
  type: change
related_changes:
- '[[Changes/Dify/2026-07-17-agent-app-enters-open-beta-and-is-now-enabled-by-default-for-all-users-it-introd|Agent
  App enters open beta and is now enabled by default for all users]]'
- '[[Changes/Claude Code/2026-07-18-9-safety-and-privacy-changes-in-v2-1-214|9 Safety
  and Privacy changes in v2.1.214]]'
- '[[Changes/Claude Code/2026-07-20-5-safety-and-privacy-changes-in-v2-1-216|5 Safety
  and Privacy changes in v2.1.216]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-20-v1-0-72-github-356903706-84b07b91|github-copilot-cli-2026-07-20-v1-0-72-github-356903706-84b07b91]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in v1.0.72
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in v1.0.72

**GitHub Copilot CLI** · 2026-07-20 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.72) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-20-v1-0-72-github-356903706-84b07b91|1.0.72]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add opt-in git and gh authentication inside the OS sandbox

> Sandbox macOS keychain access now defaults off for tighter isolation; re-enable it in /sandbox if a command needs it

> Toggling /sandbox restarts only local MCP servers and leaves remote servers connected

> Modified vim keys (Ctrl+K, uppercase J/K) no longer move the selection in tool-permission prompts and other text-input select menus; only unmodified j/k, the arrow keys, and Ctrl+P/Ctrl+N navigate.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.72
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-07-20-the-sessions-sidebar-is-now-navigable-with-the-keyboard-and-mouse-arrows-open-an|The Sessions sidebar is now navigable with the keyboard and mouse…]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-07-20-8-developer-workflow-changes-in-v1-0-72|8 Developer Workflow changes in v1.0.72]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-07-20-2-context-window-changes-in-v1-0-72|2 Context Window changes in v1.0.72]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-07-20-10-apps-and-integrations-changes-in-v1-0-72|10 Apps and Integrations changes in v1.0.72]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-07-20-preserve-pasted-prompt-content-when-changing-models-through-ctrl-x-model|Preserve pasted prompt content when changing models through Ctrl+X /model]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-07-20-3-agent-mode-changes-in-v1-0-72|3 Agent Mode changes in v1.0.72]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-07-20-2-editor-experience-changes-in-v1-0-72|2 Editor Experience changes in v1.0.72]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-07-20-13-other-changes-in-v1-0-72|13 other changes in v1.0.72]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-20 · Claude Code · [[Changes/Claude Code/2026-07-20-5-safety-and-privacy-changes-in-v2-1-216|5 Safety and Privacy changes in v2.1.216]]
- Later: 2026-07-21 · Claude Code · [[Changes/Claude Code/2026-07-21-fixed-remote-control-sessions-not-showing-a-pending-permission-prompt-or-dialog|Fixed Remote Control sessions not showing a pending permission prompt or dialog…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-07-20-d2514c&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-07-20-4-safety-and-privacy-changes-in-v1-0-72.md%0ACard%20ID%3A%20github-copilot-cli-2026-07-20-d2514c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.72%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->