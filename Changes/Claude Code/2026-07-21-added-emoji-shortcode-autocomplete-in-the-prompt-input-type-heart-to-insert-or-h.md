---
card_id: claude-code-2026-07-21-f13b52
date: '2026-07-21'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-instant-fix-all-lint-errors-with-ai|cursor-2023-03-14-24e9bf]]'
  lag_days: 1225
  role: follower
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-14-added-viminsertmoderemaps-setting-map-two-key-insert-mode-sequences-like-jj-to-e|claude-code-2026-07-14-7fcf5d]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 5a05a9b14485b9e4c4597879283b51b9ca1d0a0c52497ced82046b949e429298
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-25-added-live-file-path-autocomplete-to-bash-mode|claude-code-2026-06-25-321283]]'
- '[[Changes/Claude Code/2026-07-10-added-a-doctor-check-that-proposes-trimming-checked-in-claude-md-files-by-cuttin|claude-code-2026-07-10-25ebde]]'
- '[[Changes/Claude Code/2026-07-14-added-viminsertmoderemaps-setting-map-two-key-insert-mode-sequences-like-jj-to-e|claude-code-2026-07-14-7fcf5d]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-21-v2-1-217-github-357601516-b5c19f5d|claude-code-2026-07-21-v2-1-217-github-357601516-b5c19f5d]]'
theme: editor-experience
type: change
---

# Added emoji shortcode autocomplete in the prompt input: type `:heart:` to insert

<!-- chronolog:begin region="description" -->
Added emoji shortcode autocomplete in the prompt input: type `:heart:` to insert ❤️, or `:hea` for suggestions — disable with the `emojiCompletionEnabled` setting
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added emoji shortcode autocomplete in the prompt input: type `:heart:` to insert ❤️, or `:hea` for suggestions — disable with the `emojiCompletionEnabled` setting
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.217
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-14-added-viminsertmoderemaps-setting-map-two-key-insert-mode-sequences-like-jj-to-e|claude-code-2026-07-14-7fcf5d]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: editor-experience
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-14-instant-fix-all-lint-errors-with-ai|cursor-2023-03-14-24e9bf]]
- Lag Days: 1225
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes