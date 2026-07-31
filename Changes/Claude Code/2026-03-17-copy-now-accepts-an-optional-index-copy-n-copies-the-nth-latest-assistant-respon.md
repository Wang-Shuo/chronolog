---
card_id: claude-code-2026-03-17-4c7440
date: '2026-03-17'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]'
  lag_days: 1163
  role: follower
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-11-added-modeloverrides-setting-to-map-model-picker-entries-to-custom-provider-mode|claude-code-2026-03-11-0db484]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 94fa0e44c021beb6302baee7af33ffecd630fc8e41f770544a555b306228047c
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-11-improved-up-arrow-after-interrupting-claude-now-restores-the-interrupted-prompt|claude-code-2026-03-11-06b3d2]]'
- '[[Changes/Claude Code/2026-03-11-added-modeloverrides-setting-to-map-model-picker-entries-to-custom-provider-mode|claude-code-2026-03-11-0db484]]'
- '[[Changes/ChatGPT/2026-03-17-the-auto-functionality-can-be-accessed-by-clicking-configure-in-the-model-picker|chatgpt-2026-03-17-d07eb7]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c|claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c]]'
theme: interface-experience
type: change
---

# `/copy` now accepts an optional index: `/copy N` copies the Nth-latest assistant

<!-- chronolog:begin region="description" -->
`/copy` now accepts an optional index: `/copy N` copies the Nth-latest assistant response
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `/copy` now accepts an optional index: `/copy N` copies the Nth-latest assistant response
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-11-added-modeloverrides-setting-to-map-model-picker-entries-to-custom-provider-mode|claude-code-2026-03-11-0db484]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: interface-experience
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]
- Lag Days: 1163
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes