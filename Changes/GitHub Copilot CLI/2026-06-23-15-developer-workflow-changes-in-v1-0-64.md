---
card_id: github-copilot-cli-2026-06-23-d772f3
date: '2026-06-23'
description: 'GitHub Copilot CLI · 2026-06-23 · Developer Workflow: 15 changes in
  1.0.64 — Free-text search terms containing colons (e.g. `CLI:`) now return correct
  results…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1193
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3f8a8d28a77a9ffdc77f84670e501785da63a35c5af76a84bcb9e2c545450fd5
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-23-d772f3
  comparison: ''
  date: '2026-06-23'
  description: 'GitHub Copilot CLI — 1.0.64: 15 Developer Workflow changes'
  evidence:
  - quote: Free-text search terms containing colons (e.g. `CLI:`) now return correct
      results in Issues and Pull requests search instead of being misread as invalid
      qualifiers by GitHub
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Keep terminal output aligned after terminal resizes
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Wrap expanded compact timeline shell entries so long commands and descriptions
      stay visible
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Add /branch as an alias for /fork, matching Claude Code's command naming
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: 'Experimental: adds a `--worktree [name]` (`-w`) flag (enable with `/experimental`)
      that creates or reuses a git worktree under `<repo>.worktrees/` and starts the
      session inside it'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Add Ctrl+Backspace binding in /terminal-setup for Windows Terminal
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Respect tmux color detection in WSL sessions
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Shell session starts correctly when a nix-provided bash is first in PATH
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Content exclusion no longer blocks shell commands on command names or phantom
      paths
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Exit message always shows the session ID in the resume command instead
      of the friendly name
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Code search and worktree listing are faster
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Syntax-highlight shell commands in the timeline
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Show shell timeline rows with a yellow $ prompt and Shell label
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Remove terminal-reported color scheme support
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Add /diagnose command to analyze session logs
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 15-developer-workflow-changes-in-v1-0-64
  source_release: github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd
  source_type: github_releases
  theme: developer-workflow
  title: 15 Developer Workflow changes in v1.0.64
  type: change
related_changes:
- '[[Changes/OpenCode/2026-06-21-terminal-only-show-the-background-subagent-shortcut-when-the-server-supports-it|Terminal
  Only show the background subagent shortcut when the server supports it]]'
- '[[Changes/Claude Code/2026-06-22-changed-review-pr-to-use-the-same-review-engine-as-code-review-medium|Changed
  /review pr to use the same review engine as /code-review medium]]'
- '[[Changes/Codex CLI/2026-06-22-4-developer-workflow-changes-in-rust-v0-142-0|4
  Developer Workflow changes in rust-v0.142.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd|github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd]]'
source_type: github_releases
theme: developer-workflow
title: 15 Developer Workflow changes in v1.0.64
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Developer Workflow changes in v1.0.64

**GitHub Copilot CLI** · 2026-06-23 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.64) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd|1.0.64]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Free-text search terms containing colons (e.g. `CLI:`) now return correct results in Issues and Pull requests search instead of being misread as invalid qualifiers by GitHub

> Keep terminal output aligned after terminal resizes

> Wrap expanded compact timeline shell entries so long commands and descriptions stay visible

> Add /branch as an alias for /fork, matching Claude Code's command naming

> Experimental: adds a `--worktree [name]` (`-w`) flag (enable with `/experimental`) that creates or reuses a git worktree under `<repo>.worktrees/` and starts the session inside it

> Add Ctrl+Backspace binding in /terminal-setup for Windows Terminal

> Respect tmux color detection in WSL sessions

> Shell session starts correctly when a nix-provided bash is first in PATH

> Content exclusion no longer blocks shell commands on command names or phantom paths

> Exit message always shows the session ID in the resume command instead of the friendly name

> Code search and worktree listing are faster

> Syntax-highlight shell commands in the timeline

> Show shell timeline rows with a yellow $ prompt and Shell label

> Remove terminal-reported color scheme support

> Add /diagnose command to analyze session logs

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.64
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-23-clear-queued-tool-images-when-vision-is-disabled|Clear queued tool images when vision is disabled]] · Multimodal Input
- [[Changes/GitHub Copilot CLI/2026-06-23-9-editor-experience-changes-in-v1-0-64|9 Editor Experience changes in v1.0.64]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-23-2-account-and-access-changes-in-v1-0-64|2 Account and Access changes in v1.0.64]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-23-preserve-open-canvas-instances-across-reconnects-and-restarts|Preserve open canvas instances across reconnects and restarts]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-06-23-6-safety-and-privacy-changes-in-v1-0-64|6 Safety and Privacy changes in v1.0.64]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-23-preserve-markdown-blockquotes-in-share-exports|Preserve Markdown blockquotes in /share exports]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-06-23-show-per-model-token-totals-in-usage-and-speed-up-large-history-scans|Show per-model token totals in /usage and speed up large history scans]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-23-add-loop-alias-for-the-every-command|Add /loop alias for the /every command]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-23-add-mcp-registry-installation-for-browsing-and-installing-mcp-servers|Add /mcp registry installation for browsing and installing MCP servers]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-06-23-8-apps-and-integrations-changes-in-v1-0-64|8 Apps and Integrations changes in v1.0.64]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-23-7-model-support-changes-in-v1-0-64|7 Model Support changes in v1.0.64]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-23-6-agent-mode-changes-in-v1-0-64|6 Agent Mode changes in v1.0.64]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-23-11-interface-experience-changes-in-v1-0-64|11 Interface Experience changes in v1.0.64]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-23-4-projects-and-workspaces-changes-in-v1-0-64|4 Projects and Workspaces changes in v1.0.64]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-06-23-display-cache-write-pricing-for-models-that-omit-it|Display cache-write pricing for models that omit it]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-06-23-3-context-window-changes-in-v1-0-64|3 Context Window changes in v1.0.64]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-06-23-42-other-changes-in-v1-0-64|42 other changes in v1.0.64]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-06-22 · Codex CLI · [[Changes/Codex CLI/2026-06-22-4-developer-workflow-changes-in-rust-v0-142-0|4 Developer Workflow changes in rust-v0.142.0]]
- Later: 2026-06-23 · Windsurf · [[Changes/Windsurf/2026-06-23-cli-and-devin-local|CLI and Devin Local]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-23-d772f3&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-23-15-developer-workflow-changes-in-v1-0-64.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-23-d772f3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.64%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->