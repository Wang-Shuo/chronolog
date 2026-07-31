---
card_id: claude-code-2026-07-19-3944a0
date: '2026-07-19'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1219
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-10-added-directory-path-suggestions-to-cd-matching-add-dir-behavior|claude-code-2026-07-10-e508b3]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 24b756e19f01a6da954d117e6d0662f9ef063e58d97874495f534eb92fdf0c65
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-10-enterworktree-now-asks-for-confirmation-before-entering-a-git-worktree-outside-t|claude-code-2026-07-10-67e616]]'
- '[[Changes/Claude Code/2026-07-10-commit-push-pr-now-auto-allows-git-push-to-the-repo-s-configured-push-remote-rem|claude-code-2026-07-10-6bcc0f]]'
- '[[Changes/Claude Code/2026-07-10-added-directory-path-suggestions-to-cd-matching-add-dir-behavior|claude-code-2026-07-10-e508b3]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-19-v2-1-215-github-356226333-6836aad6|claude-code-2026-07-19-v2-1-215-github-356226333-6836aad6]]'
theme: developer-workflow
type: change
---

# Claude no longer runs the `/verify` and `/code-review` skills on its own; invoke

<!-- chronolog:begin region="description" -->
Claude no longer runs the `/verify` and `/code-review` skills on its own; invoke them with `/verify` or `/code-review` when you want them
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Claude no longer runs the `/verify` and `/code-review` skills on its own; invoke them with `/verify` or `/code-review` when you want them
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.215
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-10-added-directory-path-suggestions-to-cd-matching-add-dir-behavior|claude-code-2026-07-10-e508b3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1219
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes