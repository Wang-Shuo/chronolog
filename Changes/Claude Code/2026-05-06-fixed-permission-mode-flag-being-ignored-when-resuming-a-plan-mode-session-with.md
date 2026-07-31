---
card_id: claude-code-2026-05-06-ab7de0
date: '2026-05-06'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1116
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-01-dangerously-skip-permissions-now-bypasses-prompts-for-writes-to-claude-git-vscod|claude-code-2026-05-01-92258f]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 65ed79cd8eed7abd7defb4f73c6459d94fa2bc7e86fbadd45d838a799603055f
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-04-30-vulnerability-scanner|cursor-2026-04-30-7bb8a5]]'
- '[[Changes/Claude Code/2026-05-01-dangerously-skip-permissions-now-bypasses-prompts-for-writes-to-claude-git-vscod|claude-code-2026-05-01-92258f]]'
- '[[Changes/Cursor/2026-05-01-default-off-users-can-discover-and-opt-in|cursor-2026-05-01-759bfb]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-06-v2-1-132-github-318578987-ed60d664|claude-code-2026-05-06-v2-1-132-github-318578987-ed60d664]]'
theme: safety-privacy
type: change
---

# Fixed `--permission-mode` flag being ignored when resuming a plan-mode session w

<!-- chronolog:begin region="description" -->
Fixed `--permission-mode` flag being ignored when resuming a plan-mode session with `-p --continue`/`--resume`, and plan mode not being re-applied after `ExitPlanMode` within the same session
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed `--permission-mode` flag being ignored when resuming a plan-mode session with `-p --continue`/`--resume`, and plan mode not being re-applied after `ExitPlanMode` within the same session
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.132
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-01-dangerously-skip-permissions-now-bypasses-prompts-for-writes-to-claude-git-vscod|claude-code-2026-05-01-92258f]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1116
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes