---
card_id: chatgpt-2026-02-20-0ba0b2
date: '2026-02-20'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  lag_days: 1023
  role: follower
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from:
- '[[Changes/ChatGPT/2026-02-13-attach-up-to-20-files-in-a-single-message-you-can-now-upload-up-to-20-files-at-o|chatgpt-2026-02-13-87b8a0]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: e80dc5f08a515dda2a4a08edaadd1c5655ce6424893cf7c13b3ce7a53302ef8f
product: chatgpt
product_name: ChatGPT
related_changes:
- '[[Changes/Claude Code/2026-02-05-added-summarize-from-here-to-the-message-selector-allowing-partial-conversation|claude-code-2026-02-05-976b5f]]'
- '[[Changes/ChatGPT/2026-02-13-attach-up-to-20-files-in-a-single-message-you-can-now-upload-up-to-20-files-at-o|chatgpt-2026-02-13-87b8a0]]'
- '[[Changes/Claude Code/2026-02-13-improved-rename-to-auto-generate-session-name-from-conversation-context-when-cal|claude-code-2026-02-13-3770b4]]'
source_release: '[[Releases/ChatGPT/chatgpt-2026-02-20-expanded-context-window-for-thinking-31f2c4c2|chatgpt-2026-02-20-expanded-context-window-for-thinking-31f2c4c2]]'
theme: context-window
type: change
---

# ChatGPT now has a total context window length of 256k tokens (128k input and 128

<!-- chronolog:begin region="description" -->
ChatGPT now has a total context window length of 256k tokens (128k input and 128k max output) when you manually select Thinking. Previously it was 196k total tokens.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> ChatGPT now has a total context window length of 256k tokens (128k input and 128k max output) when you manually select Thinking. Previously it was 196k total tokens.
>
> Source: https://help.openai.com/en/articles/6825453-chatgpt-release-notes#expanded-context-window-for-thinking
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/ChatGPT/2026-02-13-attach-up-to-20-files-in-a-single-message-you-can-now-upload-up-to-20-files-at-o|chatgpt-2026-02-13-87b8a0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 1023
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes