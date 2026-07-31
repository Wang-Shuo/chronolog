---
card_id: claude-code-2026-05-27-667596
date: '2026-05-27'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1166
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-21-renamed-simplify-to-code-review-it-now-reports-correctness-bugs-at-a-chosen-effo|claude-code-2026-05-21-b0bdbe]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 4e7951712073d051765ef58b39f5cecff281c073d7166b50434948c31766b820
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-15-added-worktree-bgisolation-none-setting-to-let-background-sessions-edit-the-work|claude-code-2026-05-15-85301e]]'
- '[[Changes/Claude Code/2026-05-21-renamed-simplify-to-code-review-with-an-optional-effort-level-e-g-code-review-hi|claude-code-2026-05-21-796b5a]]'
- '[[Changes/Claude Code/2026-05-21-renamed-simplify-to-code-review-it-now-reports-correctness-bugs-at-a-chosen-effo|claude-code-2026-05-21-b0bdbe]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-27-v2-1-152-github-329718732-e62ea850|claude-code-2026-05-27-v2-1-152-github-329718732-e62ea850]]'
theme: developer-workflow
type: change
---

# `/code-review --fix` now applies review findings to your working tree after the

<!-- chronolog:begin region="description" -->
`/code-review --fix` now applies review findings to your working tree after the review, surfacing reuse, simplification, and efficiency suggestions; `/simplify` now invokes `/code-review --fix`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `/code-review --fix` now applies review findings to your working tree after the review, surfacing reuse, simplification, and efficiency suggestions; `/simplify` now invokes `/code-review --fix`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.152
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-21-renamed-simplify-to-code-review-it-now-reports-correctness-bugs-at-a-chosen-effo|claude-code-2026-05-21-b0bdbe]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1166
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes