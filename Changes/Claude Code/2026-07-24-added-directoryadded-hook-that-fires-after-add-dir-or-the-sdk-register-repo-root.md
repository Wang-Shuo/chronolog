---
card_id: claude-code-2026-07-24-c4cc36
date: '2026-07-24'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1219
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-24-added-mcp-server-errors-to-the-headless-stream-json-init-event-listing-mcp-confi|claude-code-2026-07-24-b7c5f4]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 7884d7d6a7a79814812e42e4bad5084a505c63b9faeebcb33ac1db715730c406
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-07-17-we-also-refined-how-cursor-s-responses-look-in-slack-in-message-buttons-are-gone|cursor-2026-07-17-40bd59]]'
- '[[Changes/Claude Code/2026-07-22-added-http-status-and-error-text-to-claude-mcp-list-and-mcp-when-a-server-fails|claude-code-2026-07-22-770179]]'
- '[[Changes/Claude Code/2026-07-24-added-mcp-server-errors-to-the-headless-stream-json-init-event-listing-mcp-confi|claude-code-2026-07-24-b7c5f4]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-24-v2-1-219-github-359412713-6c14d233|claude-code-2026-07-24-v2-1-219-github-359412713-6c14d233]]'
theme: apps-integrations
type: change
---

# Added `DirectoryAdded` hook that fires after `/add-dir` or the SDK `register_rep

<!-- chronolog:begin region="description" -->
Added `DirectoryAdded` hook that fires after `/add-dir` or the SDK `register_repo_root` control request registers a new working directory mid-session
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `DirectoryAdded` hook that fires after `/add-dir` or the SDK `register_repo_root` control request registers a new working directory mid-session
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.219
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-24-added-mcp-server-errors-to-the-headless-stream-json-init-event-listing-mcp-confi|claude-code-2026-07-24-b7c5f4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1219
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes