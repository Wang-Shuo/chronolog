---
card_id: claude-code-2026-05-29-801fdf
date: '2026-05-29'
description: 'Claude Code · 2026-05-29 · Developer Workflow: 3 changes in v2.1.157
  — `EnterWorktree` can now switch between Claude-managed worktrees mid-session'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1168
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2ff1fd729b8768b7d2313592bbca9d1b187a9f93157bec919b0d7285c681b500
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-29-801fdf
  comparison: ''
  date: '2026-05-29'
  description: 'Claude Code — v2.1.157: 3 Developer Workflow changes'
  evidence:
  - quote: '`EnterWorktree` can now switch between Claude-managed worktrees mid-session'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.157
  - quote: Worktrees managed by Claude are now left unlocked when the agent finishes,
      so `git worktree remove`/`prune` can clean them up
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.157
  - quote: '`/terminal-setup` now disables GPU acceleration in VS Code/Cursor/Windsurf
      integrated terminals to prevent garbled-text rendering'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.157
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-developer-workflow-changes-in-v2-1-157
  source_release: claude-code-2026-05-29-v2-1-157-github-331670634-f5eda9d8
  source_type: github_releases
  theme: developer-workflow
  title: 3 Developer Workflow changes in v2.1.157
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-27-added-reload-skills-command-to-re-scan-skill-directories-without-restarting-the|Added
  /reload-skills command to re-scan skill directories without restarting the session]]'
- '[[Changes/Claude Code/2026-05-28-simplify-now-runs-a-cleanup-only-review-reuse-simplification-efficiency-altitude|/simplify
  now runs a cleanup-only review…]]'
- '[[Changes/Claude Code/2026-05-28-status-line-commands-now-receive-columns-and-lines-environment-variables-so-scri|Status
  line commands now receive COLUMNS and LINES environment variables…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-29-v2-1-157-github-331670634-f5eda9d8|claude-code-2026-05-29-v2-1-157-github-331670634-f5eda9d8]]'
source_type: github_releases
theme: developer-workflow
title: 3 Developer Workflow changes in v2.1.157
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Developer Workflow changes in v2.1.157

**Claude Code** · 2026-05-29 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.157) · from [[Releases/Claude Code/claude-code-2026-05-29-v2-1-157-github-331670634-f5eda9d8|v2.1.157]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `EnterWorktree` can now switch between Claude-managed worktrees mid-session

> Worktrees managed by Claude are now left unlocked when the agent finishes, so `git worktree remove`/`prune` can clean them up

> `/terminal-setup` now disables GPU acceleration in VS Code/Cursor/Windsurf integrated terminals to prevent garbled-text rendering

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.157
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-29-claude-agents-slash-command-autocomplete-in-the-dispatch-input-now-matches-subst|claude agents: slash-command autocomplete in the dispatch input now matches substrings]] · Interface Experience
- [[Changes/Claude Code/2026-05-29-claude-agents-the-agent-field-in-settings-json-is-now-honored-for-dispatched-ses|claude agents: the agent field in settings.json is now honored for dispatched…]] · Agent Mode
- [[Changes/Claude Code/2026-05-29-2-safety-and-privacy-changes-in-v2-1-157|2 Safety and Privacy changes in v2.1.157]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-29-removed-the-ide-for-startup-hint-toast|Removed the "/ide for …" startup hint toast]] · Editor Experience
- [[Changes/Claude Code/2026-05-29-improved-performance-of-long-and-resumed-conversations-by-eliminating-redundant|Improved performance of long and resumed conversations by eliminating redundant…]] · Reliability and Performance
- [[Changes/Claude Code/2026-05-29-4-apps-and-integrations-changes-in-v2-1-157|4 Apps and Integrations changes in v2.1.157]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-29-3-other-changes-in-v2-1-157|3 other changes in v2.1.157]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-05-28 · Claude Code · [[Changes/Claude Code/2026-05-28-status-line-commands-now-receive-columns-and-lines-environment-variables-so-scri|Status line commands now receive COLUMNS and LINES environment variables…]]
- Later: 2026-06-02 · Claude Code · [[Changes/Claude Code/2026-06-02-2-developer-workflow-changes-in-v2-1-160|2 Developer Workflow changes in v2.1.160]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-29-801fdf&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-29-3-developer-workflow-changes-in-v2-1-157.md%0ACard%20ID%3A%20claude-code-2026-05-29-801fdf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.157%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->