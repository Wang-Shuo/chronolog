---
card_id: claude-code-2026-07-03-53ba6a
date: '2026-07-03'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]'
  lag_days: 1271
  role: follower
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-26-added-claude-code-disable-mouse-clicks-to-disable-mouse-click-drag-hover-in-full|claude-code-2026-06-26-0f04df]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: a9222537261aacef5f64e209a9456ff3118b0aa486d2fd517c6521508af6185e
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-23-added-org-configured-model-restrictions-to-the-model-picker-model-model-and-anth|claude-code-2026-06-23-761df2]]'
- '[[Changes/Claude Code/2026-06-23-improved-btw-with-arrow-navigation-to-step-through-earlier-answers|claude-code-2026-06-23-cb71e8]]'
- '[[Changes/Claude Code/2026-06-26-added-claude-code-disable-mouse-clicks-to-disable-mouse-click-drag-hover-in-full|claude-code-2026-06-26-0f04df]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-03-v2-1-200-github-348415228-64d6d68d|claude-code-2026-07-03-v2-1-200-github-348415228-64d6d68d]]'
theme: interface-experience
type: change
---

# Changed `AskUserQuestion` dialogs to no longer auto-continue by default; opt int

<!-- chronolog:begin region="description" -->
Changed `AskUserQuestion` dialogs to no longer auto-continue by default; opt into an idle timeout via `/config`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Changed `AskUserQuestion` dialogs to no longer auto-continue by default; opt into an idle timeout via `/config`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.200
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-26-added-claude-code-disable-mouse-clicks-to-disable-mouse-click-drag-hover-in-full|claude-code-2026-06-26-0f04df]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: interface-experience
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]
- Lag Days: 1271
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes