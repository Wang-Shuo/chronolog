---
card_id: claude-code-2026-07-14-610e14
date: '2026-07-14'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  lag_days: 1282
  role: follower
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-03-claude-sonnet-5-sessions-no-longer-use-the-mid-conversation-system-role-for-harn|claude-code-2026-07-03-8405a6]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 34717624559897a5c66d3fa295e6d78cda51cfb5a637412ffedab3321c211d23
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-01-gateway-added-claude-platform-on-aws-anthropicaws-as-an-upstream-provider-model|claude-code-2026-07-01-d0f0de]]'
- '[[Changes/Claude Code/2026-07-03-claude-sonnet-5-sessions-no-longer-use-the-mid-conversation-system-role-for-harn|claude-code-2026-07-03-8405a6]]'
- '[[Changes/ChatGPT/2026-07-06-we-re-rolling-out-gpt-5-5-instant-mini-in-chatgpt-it-replaces-gpt-5-3-instant-mi|chatgpt-2026-07-06-367b99]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-14-v2-1-210-github-354034085-7eba9ec7|claude-code-2026-07-14-v2-1-210-github-354034085-7eba9ec7]]'
theme: model-support
type: change
---

# Improved the Bash/PowerShell tool message when a command hits its timeout and is

<!-- chronolog:begin region="description" -->
Improved the Bash/PowerShell tool message when a command hits its timeout and is auto-backgrounded, so the model can distinguish a hang from an explicit background request
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved the Bash/PowerShell tool message when a command hits its timeout and is auto-backgrounded, so the model can distinguish a hang from an explicit background request
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.210
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-03-claude-sonnet-5-sessions-no-longer-use-the-mid-conversation-system-role-for-harn|claude-code-2026-07-03-8405a6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: model-support
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]
- Lag Days: 1282
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes