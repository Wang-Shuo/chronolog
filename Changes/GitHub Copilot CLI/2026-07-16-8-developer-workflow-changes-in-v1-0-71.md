---
card_id: github-copilot-cli-2026-07-16-6a6a59
date: '2026-07-16'
description: 'GitHub Copilot CLI · 2026-07-16 · Developer Workflow: 8 changes in 1.0.71
  — Avoid leaving long-running background git processes after exit'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2865
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 85e66cceb465e8a47342cbba71ca8e719a8fd519a0b8d0b265e50fa0bd0b4152
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-07-16-6a6a59
  comparison: ''
  date: '2026-07-16'
  description: 'GitHub Copilot CLI — 1.0.71: 8 Developer Workflow changes'
  evidence:
  - quote: Avoid leaving long-running background git processes after exit
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Add a configurable maximum for Ctrl+R command history
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: /terminal-setup no longer skips setup on terminals without real kitty keyboard
      support
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: 'Split /worktree and /move: /worktree now creates a new worktree and leaves
      your uncommitted changes behind, while the new /move carries them into the new
      worktree'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Shell completions suggest positional-argument choices
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Show retained shell output in /tasks Shell Details for finished tasks
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Shell completions stop suggesting subcommands as flag values
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Hide the inert navigate and view-log hints in the empty /lsp logs (LSP
      Services) panel
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 8-developer-workflow-changes-in-v1-0-71
  source_release: github-copilot-cli-2026-07-16-v1-0-71-github-354824472-a089f622
  source_type: github_releases
  theme: developer-workflow
  title: 8 Developer Workflow changes in v1.0.71
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-14-agent-view-ctrl-x-now-deletes-renamed-branch-worktrees-never-destroys-unpushed-c|Agent
  view: Ctrl+X now deletes renamed-branch worktrees, never destroys unpushed…]]'
- '[[Changes/OpenCode/2026-07-14-desktop-fixed-terminal-tabs-stealing-focus-when-they-mount|Desktop
  Fixed terminal tabs stealing focus when they mount]]'
- '[[Changes/Codex CLI/2026-07-16-2-developer-workflow-changes-in-rust-v0-144-5|2
  Developer Workflow changes in rust-v0.144.5]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-16-v1-0-71-github-354824472-a089f622|github-copilot-cli-2026-07-16-v1-0-71-github-354824472-a089f622]]'
source_type: github_releases
theme: developer-workflow
title: 8 Developer Workflow changes in v1.0.71
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Developer Workflow changes in v1.0.71

**GitHub Copilot CLI** · 2026-07-16 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.71) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-16-v1-0-71-github-354824472-a089f622|1.0.71]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Avoid leaving long-running background git processes after exit

> Add a configurable maximum for Ctrl+R command history

> /terminal-setup no longer skips setup on terminals without real kitty keyboard support

> Split /worktree and /move: /worktree now creates a new worktree and leaves your uncommitted changes behind, while the new /move carries them into the new worktree

> Shell completions suggest positional-argument choices

> Show retained shell output in /tasks Shell Details for finished tasks

> Shell completions stop suggesting subcommands as flag values

> Hide the inert navigate and view-log hints in the empty /lsp logs (LSP Services) panel

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.71
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-07-16-3-model-support-changes-in-v1-0-71|3 Model Support changes in v1.0.71]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-07-16-server-mode-reconnects-oauth-mcp-servers-from-cached-tokens|Server mode reconnects OAuth MCP servers from cached tokens]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-07-16-5-editor-experience-changes-in-v1-0-71|5 Editor Experience changes in v1.0.71]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-07-16-add-canvas-support-in-the-cli-for-extension-driven-interactions|Add canvas support in the CLI for extension-driven interactions]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-07-16-refresh-memory-context-after-30-minutes-in-long-lived-sessions|Refresh memory context after 30 minutes in long-lived sessions]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-07-16-2-safety-and-privacy-changes-in-v1-0-71|2 Safety and Privacy changes in v1.0.71]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-07-16-3-pricing-model-changes-in-v1-0-71|3 Pricing Model changes in v1.0.71]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-07-16-2-collaboration-changes-in-v1-0-71|2 Collaboration changes in v1.0.71]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-07-16-2-context-window-changes-in-v1-0-71|2 Context Window changes in v1.0.71]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-07-16-add-plugins-marketplace-browse-and-update-commands|Add plugins marketplace browse and update commands]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-07-16-add-voice-devices-to-choose-and-persist-the-microphone-for-voice-mode|Add /voice devices to choose and persist the microphone for voice mode]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-07-16-16-apps-and-integrations-changes-in-v1-0-71|16 Apps and Integrations changes in v1.0.71]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-07-16-5-interface-experience-changes-in-v1-0-71|5 Interface Experience changes in v1.0.71]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-07-16-8-agent-mode-changes-in-v1-0-71|8 Agent Mode changes in v1.0.71]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-07-16-30-other-changes-in-v1-0-71|30 other changes in v1.0.71]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-07-16 · Codex CLI · [[Changes/Codex CLI/2026-07-16-2-developer-workflow-changes-in-rust-v0-144-5|2 Developer Workflow changes in rust-v0.144.5]]
- Later: 2026-07-16 · OpenCode · [[Changes/OpenCode/2026-07-16-desktop-fixed-startup-readiness-so-wsl-server-loading-is-included-before-the-des|Desktop Fixed startup readiness so WSL server loading is included before the desktop…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-07-16-6a6a59&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-07-16-8-developer-workflow-changes-in-v1-0-71.md%0ACard%20ID%3A%20github-copilot-cli-2026-07-16-6a6a59%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.71%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->