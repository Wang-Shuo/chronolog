---
card_id: claude-code-2026-06-02-ae28c1
date: '2026-06-02'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1172
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-02-acceptedits-mode-now-prompts-before-writing-build-tool-config-files-that-grant-c|claude-code-2026-06-02-58d83f]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: cbe0dc02c98fea7e3702818d71cd991ff157b76f86444d0ebf6494ff44dcbec9
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-28-status-line-commands-now-receive-columns-and-lines-environment-variables-so-scri|claude-code-2026-05-28-fe5ca3]]'
- '[[Changes/Claude Code/2026-05-29-enterworktree-can-now-switch-between-claude-managed-worktrees-mid-session|claude-code-2026-05-29-8c413b]]'
- '[[Changes/Claude Code/2026-06-02-acceptedits-mode-now-prompts-before-writing-build-tool-config-files-that-grant-c|claude-code-2026-06-02-58d83f]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-02-v2-1-161-github-333271302-7337e6fa|claude-code-2026-06-02-v2-1-161-github-333271302-7337e6fa]]'
theme: developer-workflow
type: change
---

# Parallel tool calls: a failed Bash command no longer cancels other calls in the

<!-- chronolog:begin region="description" -->
Parallel tool calls: a failed Bash command no longer cancels other calls in the same batch — each tool returns its own result independently
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Parallel tool calls: a failed Bash command no longer cancels other calls in the same batch — each tool returns its own result independently
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.161
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-02-acceptedits-mode-now-prompts-before-writing-build-tool-config-files-that-grant-c|claude-code-2026-06-02-58d83f]]
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