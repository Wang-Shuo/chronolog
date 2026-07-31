---
card_id: claude-code-2026-06-02-a2671c
date: '2026-06-02'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-instant-fix-all-lint-errors-with-ai|cursor-2023-03-14-24e9bf]]'
  lag_days: 1176
  role: follower
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-22-diff-detail-view-can-now-be-scrolled-with-the-keyboard-arrows-j-k-pgup-pgdn-spac|claude-code-2026-05-22-d23d37]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 88729dfd68f03c970498c2c02db4821f26b86f1bc57a18a2c654d6d1cc8e0b02
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-05-07-the-commits-tab-gives-you-a-focused-view-of-commit-history-for-the-pr|cursor-2026-05-07-c20a06]]'
- '[[Changes/Cursor/2026-05-07-the-reviews-tab-now-shows-inline-review-threads-and-top-level-pr-comments|cursor-2026-05-07-fb2228]]'
- '[[Changes/Claude Code/2026-05-22-diff-detail-view-can-now-be-scrolled-with-the-keyboard-arrows-j-k-pgup-pgdn-spac|claude-code-2026-05-22-d23d37]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-02-v2-1-160-github-332740156-03dd8b5a|claude-code-2026-06-02-v2-1-160-github-332740156-03dd8b5a]]'
theme: editor-experience
type: change
---

# Edit no longer requires a separate Read after viewing a file with `grep`: single

<!-- chronolog:begin region="description" -->
Edit no longer requires a separate Read after viewing a file with `grep`: single-file `grep`/`egrep`/`fgrep` commands now satisfy the read-before-edit check
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Edit no longer requires a separate Read after viewing a file with `grep`: single-file `grep`/`egrep`/`fgrep` commands now satisfy the read-before-edit check
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.160
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-22-diff-detail-view-can-now-be-scrolled-with-the-keyboard-arrows-j-k-pgup-pgdn-spac|claude-code-2026-05-22-d23d37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: editor-experience
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-14-instant-fix-all-lint-errors-with-ai|cursor-2023-03-14-24e9bf]]
- Lag Days: 1176
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes