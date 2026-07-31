---
card_id: claude-code-2026-03-10-7bf58e
date: '2026-03-10'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]'
  lag_days: 1156
  role: follower
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-05-added-numeric-keypad-support-for-selecting-options-in-claude-s-interview-questio|claude-code-2026-03-05-b1f867]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: a9b268f6f6f87ddde89dfda185190c3dedcf2e6a57c0061873836a34e6dae509
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-02-26-added-copy-command-to-show-an-interactive-picker-when-code-blocks-are-present-al|claude-code-2026-02-26-a51fd0]]'
- '[[Changes/ChatGPT/2026-02-27-automatic-scroll-to-latest-message-existing-conversations-now-automatically-scro|chatgpt-2026-02-27-0e79ba]]'
- '[[Changes/Claude Code/2026-03-05-added-numeric-keypad-support-for-selecting-options-in-claude-s-interview-questio|claude-code-2026-03-05-b1f867]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-10-v2-1-72-github-294951528-18ee0f48|claude-code-2026-03-10-v2-1-72-github-294951528-18ee0f48]]'
theme: interface-experience
type: change
---

# Added `w` key in `/copy` to write the focused selection directly to a file, bypa

<!-- chronolog:begin region="description" -->
Added `w` key in `/copy` to write the focused selection directly to a file, bypassing the clipboard (useful over SSH)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `w` key in `/copy` to write the focused selection directly to a file, bypassing the clipboard (useful over SSH)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.72
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-05-added-numeric-keypad-support-for-selecting-options-in-claude-s-interview-questio|claude-code-2026-03-05-b1f867]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: interface-experience
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]
- Lag Days: 1156
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes