---
card_id: cursor-2023-08-22-9181ad
date: '2023-08-22'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  lag_days: 110
  role: variant
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from:
- '[[Changes/Cursor/2023-08-22-follow-up-chat-messages-to-with-codebase-will-keep-the-codebase-context|cursor-2023-08-22-8a6a3a]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 27a525ac86b3cc58fc33bb6e3d25d7c419c66645a65421cf1c7868effaa139b9
product: cursor
product_name: Cursor
related_changes:
- '[[Changes/Cursor/2023-07-19-advanced-context-controls-only-show-up-if-you-have-indexed-your-codebase|cursor-2023-07-19-031260]]'
- '[[Changes/Cursor/2023-07-19-more-control-of-context-building-abilities-for-codebase-wide-chat|cursor-2023-07-19-14c678]]'
- '[[Changes/Cursor/2023-08-22-follow-up-chat-messages-to-with-codebase-will-keep-the-codebase-context|cursor-2023-08-22-8a6a3a]]'
source_release: '[[Releases/Cursor/cursor-2023-08-22-0-8-2-https-cursor-com-changelog-0-8-2-866d920f|cursor-2023-08-22-0-8-2-https-cursor-com-changelog-0-8-2-866d920f]]'
theme: context-window
type: change
---

# If you @ reference a long file that will be cutoff by the context limit, you'll

<!-- chronolog:begin region="description" -->
If you @ reference a long file that will be cutoff by the context limit, you'll be given the option to automatically chunk the file and scan it with many GPTs.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> If you @ reference a long file that will be cutoff by the context limit, you'll be given the option to automatically chunk the file and scan it with many GPTs.
>
> Source: https://cursor.com/changelog/0-8-2
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Cursor/2023-08-22-follow-up-chat-messages-to-with-codebase-will-keep-the-codebase-context|cursor-2023-08-22-8a6a3a]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Scope: tracked-products-only
- Role: variant
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 110
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes