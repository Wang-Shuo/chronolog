---
card_id: cursor-2026-06-04-ee9248
date: '2026-06-04'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1064
  role: variant
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Cursor/2026-06-04-before-this-exposing-a-custom-capability-meant-standing-up-your-own-stdio-or-rem|cursor-2026-06-04-0a3ca5]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: a5556ce3295ec6db4081ca003bf6cded00d10ceccf33efaaa5a660a5dce92a6a
product: cursor
product_name: Cursor
related_changes:
- '[[Changes/Claude Code/2026-06-02-claude-agents-rows-now-show-done-total-before-the-detail-when-work-is-fanned-out|claude-code-2026-06-02-e9ef76]]'
- '[[Changes/ChatGPT/2026-06-04-lockdown-mode-is-now-available-to-all-logged-in-users-across-account-types-and-w|chatgpt-2026-06-04-88660d]]'
- '[[Changes/Cursor/2026-06-04-before-this-exposing-a-custom-capability-meant-standing-up-your-own-stdio-or-rem|cursor-2026-06-04-0a3ca5]]'
source_release: '[[Releases/Cursor/cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856|cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856]]'
theme: agent-mode
type: change
---

# By default, a local SDK agent runs tool calls without asking for approval, since

<!-- chronolog:begin region="description" -->
By default, a local SDK agent runs tool calls without asking for approval, since there's no human in the loop in a headless run. Set local.autoReview to route those calls through auto-review instead. A classifier decides which calls run automatically and which to hold back, rather than bypassing review entirely.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> By default, a local SDK agent runs tool calls without asking for approval, since there's no human in the loop in a headless run. Set local.autoReview to route those calls through auto-review instead. A classifier decides which calls run automatically and which to hold back, rather than bypassing review entirely.
>
> Source: https://cursor.com/changelog/sdk-updates-jun-2026
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Cursor/2026-06-04-before-this-exposing-a-custom-capability-meant-standing-up-your-own-stdio-or-rem|cursor-2026-06-04-0a3ca5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: variant
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1064
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes