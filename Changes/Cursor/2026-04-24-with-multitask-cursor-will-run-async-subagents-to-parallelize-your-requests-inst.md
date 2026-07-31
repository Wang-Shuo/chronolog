---
card_id: cursor-2026-04-24-a02402
date: '2026-04-24'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1023
  role: variant
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Cursor/2026-04-24-multitask-in-agents-window|cursor-2026-04-24-998619]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 0051f907c99a6d6ecdad92dcece0e188e1d425b5ae9419908b45a2e79522ef70
product: cursor
product_name: Cursor
related_changes:
- '[[Changes/Cursor/2026-04-24-this-release-introduces-a-new-way-to-multitask-with-async-subagents-an-improved|cursor-2026-04-24-462263]]'
- '[[Changes/Cursor/2026-04-24-if-you-already-have-messages-in-the-queue-you-can-ask-cursor-to-multitask-on-the|cursor-2026-04-24-93ddaa]]'
- '[[Changes/Cursor/2026-04-24-multitask-in-agents-window|cursor-2026-04-24-998619]]'
source_release: '[[Releases/Cursor/cursor-2026-04-24-3-2-https-cursor-com-changelog-04-24-26-9ab6a4bf|cursor-2026-04-24-3-2-https-cursor-com-changelog-04-24-26-9ab6a4bf]]'
theme: agent-mode
type: change
---

# With /multitask, Cursor will run async subagents to parallelize your requests in

<!-- chronolog:begin region="description" -->
With /multitask, Cursor will run async subagents to parallelize your requests instead of adding them to the queue. It will also break down larger tasks into smaller chunks for a fleet of async subagents to tackle simultaneously.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> With /multitask, Cursor will run async subagents to parallelize your requests instead of adding them to the queue. It will also break down larger tasks into smaller chunks for a fleet of async subagents to tackle simultaneously.
>
> Source: https://cursor.com/changelog/04-24-26
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Cursor/2026-04-24-multitask-in-agents-window|cursor-2026-04-24-998619]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: variant
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1023
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes