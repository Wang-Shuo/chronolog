---
card_id: claude-code-2026-03-20-649a2d
date: '2026-03-20'
description: 'Claude Code · 2026-03-20 · Developer Workflow: 4 changes in v2.1.81
  — Added `--bare` flag for scripted `-p` calls — skips hooks, LSP, plugin sync, and
  skill…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1098
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e9cef6b0277bb5b67e71a3618885d4e1200161a30383329e756db44a9a39d829
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-20-649a2d
  comparison: ''
  date: '2026-03-20'
  description: 'Claude Code — v2.1.81: 4 Developer Workflow changes'
  evidence:
  - quote: Added `--bare` flag for scripted `-p` calls — skips hooks, LSP, plugin
      sync, and skill directory walks; requires `ANTHROPIC_API_KEY` or an `apiKeyHelper`
      via `--settings` (OAuth and keychain auth disabled); auto-memory fully disabled
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.81
  - quote: Resuming a session that was in a worktree now switches back to that worktree
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.81
  - quote: Improved `!` bash mode discoverability — Claude now suggests it when you
      need to run an interactive command
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.81
  - quote: Disabled line-by-line response streaming on Windows (including WSL in Windows
      Terminal) due to rendering issues
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.81
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-developer-workflow-changes-in-v2-1-81
  source_release: claude-code-2026-03-20-v2-1-81-github-299621655-10d2d4fe
  source_type: github_releases
  theme: developer-workflow
  title: 4 Developer Workflow changes in v2.1.81
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-14-4-developer-workflow-changes-in-v2-1-76|4 Developer
  Workflow changes in v2.1.76]]'
- '[[Changes/Claude Code/2026-03-17-background-bash-tasks-are-now-killed-if-output-exceeds-5gb-preventing-runaway-pr|Background
  bash tasks are now killed if output exceeds 5GB, preventing runaway…]]'
- '[[Changes/Claude Code/2026-03-17-terminal-notifications-iterm2-kitty-ghostty-popups-progress-bar-now-reach-the-ou|Terminal
  notifications (iTerm2/Kitty/Ghostty popups, progress bar) now reach…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-20-v2-1-81-github-299621655-10d2d4fe|claude-code-2026-03-20-v2-1-81-github-299621655-10d2d4fe]]'
source_type: github_releases
theme: developer-workflow
title: 4 Developer Workflow changes in v2.1.81
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Developer Workflow changes in v2.1.81

**Claude Code** · 2026-03-20 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.81) · from [[Releases/Claude Code/claude-code-2026-03-20-v2-1-81-github-299621655-10d2d4fe|v2.1.81]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `--bare` flag for scripted `-p` calls — skips hooks, LSP, plugin sync, and skill directory walks; requires `ANTHROPIC_API_KEY` or an `apiKeyHelper` via `--settings` (OAuth and keychain auth disabled); auto-memory fully disabled

> Resuming a session that was in a worktree now switches back to that worktree

> Improved `!` bash mode discoverability — Claude now suggests it when you need to run an interactive command

> Disabled line-by-line response streaming on Windows (including WSL in Windows Terminal) due to rendering issues

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.81
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-20-2-safety-and-privacy-changes-in-v2-1-81|2 Safety and Privacy changes in v2.1.81]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-20-changed-plan-mode-to-hide-the-clear-context-option-by-default-restore-with-showc|Changed plan mode to hide the "clear context" option by default…]] · Context Window
- [[Changes/Claude Code/2026-03-20-3-apps-and-integrations-changes-in-v2-1-81|3 Apps and Integrations changes in v2.1.81]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-20-updated-mcp-oauth-to-support-client-id-metadata-document-cimd-sep-991-for-server|Updated MCP OAuth to support Client ID Metadata Document (CIMD / SEP-991)…]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-17 · Claude Code · [[Changes/Claude Code/2026-03-17-terminal-notifications-iterm2-kitty-ghostty-popups-progress-bar-now-reach-the-ou|Terminal notifications (iTerm2/Kitty/Ghostty popups, progress bar) now reach…]]
- Later: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-5-developer-workflow-changes-in-v2-1-84|5 Developer Workflow changes in v2.1.84]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-20-649a2d&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-20-4-developer-workflow-changes-in-v2-1-81.md%0ACard%20ID%3A%20claude-code-2026-03-20-649a2d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.81%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->