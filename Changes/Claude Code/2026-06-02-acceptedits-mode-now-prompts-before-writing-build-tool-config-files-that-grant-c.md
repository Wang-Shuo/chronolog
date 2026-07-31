---
card_id: claude-code-2026-06-02-58d83f
date: '2026-06-02'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1172
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-29-enterworktree-can-now-switch-between-claude-managed-worktrees-mid-session|claude-code-2026-05-29-8c413b]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 148f4e0c56927c3277ba8bcd8a6cdad0b83452c0660b165d39e1e728a8224afd
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-27-added-reload-skills-command-to-re-scan-skill-directories-without-restarting-the|claude-code-2026-05-27-8c63c5]]'
- '[[Changes/Claude Code/2026-05-28-status-line-commands-now-receive-columns-and-lines-environment-variables-so-scri|claude-code-2026-05-28-fe5ca3]]'
- '[[Changes/Claude Code/2026-05-29-enterworktree-can-now-switch-between-claude-managed-worktrees-mid-session|claude-code-2026-05-29-8c413b]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-02-v2-1-160-github-332740156-03dd8b5a|claude-code-2026-06-02-v2-1-160-github-332740156-03dd8b5a]]'
theme: developer-workflow
type: change
---

# `acceptEdits` mode now prompts before writing build-tool config files that grant

<!-- chronolog:begin region="description" -->
`acceptEdits` mode now prompts before writing build-tool config files that grant code execution (`.npmrc`, `.yarnrc*`, `bunfig.toml`, `.bazelrc`, `.pre-commit-config.yaml`, `.devcontainer/`, etc.)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `acceptEdits` mode now prompts before writing build-tool config files that grant code execution (`.npmrc`, `.yarnrc*`, `bunfig.toml`, `.bazelrc`, `.pre-commit-config.yaml`, `.devcontainer/`, etc.)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.160
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-29-enterworktree-can-now-switch-between-claude-managed-worktrees-mid-session|claude-code-2026-05-29-8c413b]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1172
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes