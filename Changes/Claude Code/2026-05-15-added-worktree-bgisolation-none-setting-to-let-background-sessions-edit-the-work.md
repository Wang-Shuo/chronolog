---
card_id: claude-code-2026-05-15-85301e
date: '2026-05-15'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1154
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-08-improved-visual-consistency-across-slash-command-dialogs-standardized-footer-hin|claude-code-2026-05-08-c64f98]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 7e4fbcd42f779b5cc2115bb617588a0f5a56006392e8d7cf6c7d546ab2249e6f
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-05-07-a-new-pr-review-experience-is-now-available-in-cursor-3-take-prs-from-creation-t|cursor-2026-05-07-485ba7]]'
- '[[Changes/Cursor/2026-05-07-this-release-introduces-a-new-pr-review-experience-faster-execution-on-plans-thr|cursor-2026-05-07-f07eb6]]'
- '[[Changes/Claude Code/2026-05-08-improved-visual-consistency-across-slash-command-dialogs-standardized-footer-hin|claude-code-2026-05-08-c64f98]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c|claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c]]'
theme: developer-workflow
type: change
---

# Added `worktree.bgIsolation: "none"` setting to let background sessions edit the

<!-- chronolog:begin region="description" -->
Added `worktree.bgIsolation: "none"` setting to let background sessions edit the working copy directly without `EnterWorktree`, for repos where worktrees are impractical
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `worktree.bgIsolation: "none"` setting to let background sessions edit the working copy directly without `EnterWorktree`, for repos where worktrees are impractical
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.143
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-08-improved-visual-consistency-across-slash-command-dialogs-standardized-footer-hin|claude-code-2026-05-08-c64f98]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1154
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes