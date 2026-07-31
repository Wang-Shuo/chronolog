---
card_id: chatgpt-2026-03-25-60882a
date: '2026-03-25'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  lag_days: 1056
  role: follower
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from:
- '[[Changes/ChatGPT/2026-03-05-gpt-5-4-brings-together-the-best-of-our-recent-advances-in-reasoning-coding-and|chatgpt-2026-03-05-77e8f3]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: a67fd9bc51a73b3fb024fe82fa79e33c6cd428a1660a3d8bb1b0ac798ad469bd
product: chatgpt
product_name: ChatGPT
related_changes:
- '[[Changes/Claude Code/2026-03-14-added-postcompact-hook-that-fires-after-compaction-completes|claude-code-2026-03-14-603f55]]'
- '[[Changes/Cursor/2026-03-19-standard-0-50-m-input-2-50-m-output-tokens|cursor-2026-03-19-2ef7b6]]'
- '[[Changes/Cursor/2026-03-19-fast-default-1-50-m-input-7-50-m-output-tokens|cursor-2026-03-19-425e73]]'
source_release: '[[Releases/ChatGPT/chatgpt-2026-03-25-large-pastes-are-now-handled-as-attachments-6bacf64e|chatgpt-2026-03-25-large-pastes-are-now-handled-as-attachments-6bacf64e]]'
theme: context-window
type: change
---

# Starting today for ChatGPT Plus, Pro, and Business users, long pastes are handle

<!-- chronolog:begin region="description" -->
Starting today for ChatGPT Plus, Pro, and Business users, long pastes are handled differently in ChatGPT. If you paste more than 5k characters into the composer, ChatGPT will automatically convert the content into an attachment instead of inserting it directly into the text field. This keeps the composer cleaner and helps prevent large pastes from consuming your entire context window. You can still move the content back into the message at any time by clicking on Show in text field to convert the attachment back to a direct paste.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Starting today for ChatGPT Plus, Pro, and Business users, long pastes are handled differently in ChatGPT. If you paste more than 5k characters into the composer, ChatGPT will automatically convert the content into an attachment instead of inserting it directly into the text field. This keeps the composer cleaner and helps prevent large pastes from consuming your entire context window. You can still move the content back into the message at any time by clicking on Show in text field to convert the attachment back to a direct paste.
>
> Source: https://help.openai.com/en/articles/6825453-chatgpt-release-notes#large-pastes-are-now-handled-as-attachments
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/ChatGPT/2026-03-05-gpt-5-4-brings-together-the-best-of-our-recent-advances-in-reasoning-coding-and|chatgpt-2026-03-05-77e8f3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 1056
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes