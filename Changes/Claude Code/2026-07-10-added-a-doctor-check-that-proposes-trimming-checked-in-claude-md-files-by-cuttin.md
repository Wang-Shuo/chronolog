---
card_id: claude-code-2026-07-10-25ebde
date: '2026-07-10'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-instant-fix-all-lint-errors-with-ai|cursor-2023-03-14-24e9bf]]'
  lag_days: 1214
  role: follower
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-25-added-live-file-path-autocomplete-to-bash-mode|claude-code-2026-06-25-321283]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 34a606e74382075d008900458f0fcb10940b5217c9ddfaa54134071de946fd12
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-02-edit-no-longer-requires-a-separate-read-after-viewing-a-file-with-grep-single-fi|claude-code-2026-06-02-a2671c]]'
- '[[Changes/Cursor/2026-06-10-review-also-syncs-with-bugbot-on-github-and-gitlab-if-you-run-review-and-then-op|cursor-2026-06-10-ce252c]]'
- '[[Changes/Claude Code/2026-06-25-added-live-file-path-autocomplete-to-bash-mode|claude-code-2026-06-25-321283]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-10-v2-1-206-github-351694341-0226036e|claude-code-2026-07-10-v2-1-206-github-351694341-0226036e]]'
theme: editor-experience
type: change
---

# Added a `/doctor` check that proposes trimming checked-in `CLAUDE.md` files by c

<!-- chronolog:begin region="description" -->
Added a `/doctor` check that proposes trimming checked-in `CLAUDE.md` files by cutting content Claude could derive from the codebase
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added a `/doctor` check that proposes trimming checked-in `CLAUDE.md` files by cutting content Claude could derive from the codebase
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.206
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-25-added-live-file-path-autocomplete-to-bash-mode|claude-code-2026-06-25-321283]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: editor-experience
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-14-instant-fix-all-lint-errors-with-ai|cursor-2023-03-14-24e9bf]]
- Lag Days: 1214
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes