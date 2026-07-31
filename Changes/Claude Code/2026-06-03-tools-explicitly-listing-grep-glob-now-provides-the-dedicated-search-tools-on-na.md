---
card_id: claude-code-2026-06-03-74afd0
date: '2026-06-03'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1173
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-02-parallel-tool-calls-a-failed-bash-command-no-longer-cancels-other-calls-in-the-s|claude-code-2026-06-02-ae28c1]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 21edf89e88868f03a2296b0c3dceb61fcb16dfa6b6b02e7b07da0f5406ae003e
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-29-enterworktree-can-now-switch-between-claude-managed-worktrees-mid-session|claude-code-2026-05-29-8c413b]]'
- '[[Changes/Claude Code/2026-06-02-acceptedits-mode-now-prompts-before-writing-build-tool-config-files-that-grant-c|claude-code-2026-06-02-58d83f]]'
- '[[Changes/Claude Code/2026-06-02-parallel-tool-calls-a-failed-bash-command-no-longer-cancels-other-calls-in-the-s|claude-code-2026-06-02-ae28c1]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-03-v2-1-162-github-333906405-cdc7c67c|claude-code-2026-06-03-v2-1-162-github-333906405-cdc7c67c]]'
theme: developer-workflow
type: change
---

# `--tools`: explicitly listing Grep/Glob now provides the dedicated search tools

<!-- chronolog:begin region="description" -->
`--tools`: explicitly listing Grep/Glob now provides the dedicated search tools on native builds with embedded search (previously these names were silently ignored)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `--tools`: explicitly listing Grep/Glob now provides the dedicated search tools on native builds with embedded search (previously these names were silently ignored)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.162
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-02-parallel-tool-calls-a-failed-bash-command-no-longer-cancels-other-calls-in-the-s|claude-code-2026-06-02-ae28c1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1173
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes