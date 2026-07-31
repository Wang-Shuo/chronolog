---
card_id: chatgpt-2026-06-22-e5a8ab
date: '2026-06-22'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  lag_days: 1145
  role: follower
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from:
- '[[Changes/ChatGPT/2026-03-25-starting-today-for-chatgpt-plus-pro-and-business-users-long-pastes-are-handled-d|chatgpt-2026-03-25-60882a]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: ff335e94629d464a3164d5d6c36edbbbc84606352c3b1461fdbeebd3901f3946
product: chatgpt
product_name: ChatGPT
related_changes:
- '[[Changes/Cursor/2026-06-04-this-release-introduces-design-mode-for-faster-canvas-editing-new-ways-to-unders|cursor-2026-06-04-434310]]'
- '[[Changes/Claude Code/2026-06-08-added-cd-command-to-move-a-session-to-a-new-working-directory-without-breaking-t|claude-code-2026-06-08-c60825]]'
- '[[Changes/Claude Code/2026-06-12-vscode-added-usage-attribution-to-the-account-usage-dialog-usage-showing-cache-m|claude-code-2026-06-12-7832d6]]'
source_release: '[[Releases/ChatGPT/chatgpt-2026-06-22-large-pastes-are-now-handled-as-attachments-for-more-plans-64db97b0|chatgpt-2026-06-22-large-pastes-are-now-handled-as-attachments-for-more-plans-64db97b0]]'
theme: context-window
type: change
---

# Starting today for ChatGPT Free and Go users, long pastes are handled differentl

<!-- chronolog:begin region="description" -->
Starting today for ChatGPT Free and Go users, long pastes are handled differently in ChatGPT. If you paste more than 10k characters into the composer, ChatGPT will automatically convert the content into an attachment instead of inserting it directly into the text field. This keeps the composer cleaner and helps prevent large pastes from consuming your entire context window. You can still move the content back into the message at any time by clicking on Show in text field to convert the attachment back to a direct paste. This is already available to ChatGPT Plus, Pro, and Business users. Previously if you sent more than 5k characters it was sent as an attachment. The threshold has now also been raised to 10k characters.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Starting today for ChatGPT Free and Go users, long pastes are handled differently in ChatGPT. If you paste more than 10k characters into the composer, ChatGPT will automatically convert the content into an attachment instead of inserting it directly into the text field. This keeps the composer cleaner and helps prevent large pastes from consuming your entire context window. You can still move the content back into the message at any time by clicking on Show in text field to convert the attachment back to a direct paste. This is already available to ChatGPT Plus, Pro, and Business users. Previously if you sent more than 5k characters it was sent as an attachment. The threshold has now also been raised to 10k characters.
>
> Source: https://help.openai.com/en/articles/6825453-chatgpt-release-notes#large-pastes-are-now-handled-as-attachments-for-more-plans
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/ChatGPT/2026-03-25-starting-today-for-chatgpt-plus-pro-and-business-users-long-pastes-are-handled-d|chatgpt-2026-03-25-60882a]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 1145
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes