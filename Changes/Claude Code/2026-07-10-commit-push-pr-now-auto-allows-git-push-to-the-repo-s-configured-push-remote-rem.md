---
card_id: claude-code-2026-07-10-6bcc0f
date: '2026-07-10'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1210
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-10-enterworktree-now-asks-for-confirmation-before-entering-a-git-worktree-outside-t|claude-code-2026-07-10-67e616]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: ad7453223ab26b37bde3dcf215c4130fac747b1fa77a5a39aab9351c0ac662d7
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-06-17-cursor-can-now-help-you-set-up-your-dev-environment-in-the-cloud-in-less-than-10|cursor-2026-06-17-acb560]]'
- '[[Changes/Claude Code/2026-07-02-claude-agents-session-rows-now-show-pull-request-links-as-bare-n-without-the-red|claude-code-2026-07-02-883324]]'
- '[[Changes/Claude Code/2026-07-10-enterworktree-now-asks-for-confirmation-before-entering-a-git-worktree-outside-t|claude-code-2026-07-10-67e616]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-10-v2-1-206-github-351694341-0226036e|claude-code-2026-07-10-v2-1-206-github-351694341-0226036e]]'
theme: developer-workflow
type: change
---

# `/commit-push-pr` now auto-allows `git push` to the repo's configured push remot

<!-- chronolog:begin region="description" -->
`/commit-push-pr` now auto-allows `git push` to the repo's configured push remote (`remote.pushDefault`, or the sole remote when only one is configured) in addition to `origin`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `/commit-push-pr` now auto-allows `git push` to the repo's configured push remote (`remote.pushDefault`, or the sole remote when only one is configured) in addition to `origin`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.206
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-10-enterworktree-now-asks-for-confirmation-before-entering-a-git-worktree-outside-t|claude-code-2026-07-10-67e616]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1210
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes