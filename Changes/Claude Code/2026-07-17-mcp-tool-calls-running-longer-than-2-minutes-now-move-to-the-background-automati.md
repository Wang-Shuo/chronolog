---
card_id: claude-code-2026-07-17-0b1708
date: '2026-07-17'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1212
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-15-hardened-synced-skill-plugin-directory-naming-on-windows-and-kept-ccr-web-fetch|claude-code-2026-07-15-a7c9ca]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 09883e2d7c540a6d3e7baaa89a006c016b9e946db68018b81c7f13edf9c9c1f2
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-07-09-enterprise-and-edu-users-can-find-skills-under-plugins-in-the-sidebar-on-the-ski|chatgpt-2026-07-09-baa5ca]]'
- '[[Changes/ChatGPT/2026-07-13-chatgpt-is-also-available-on-kakao-in-south-korea-and-viber-in-supported-markets|chatgpt-2026-07-13-68bda1]]'
- '[[Changes/Claude Code/2026-07-15-hardened-synced-skill-plugin-directory-naming-on-windows-and-kept-ccr-web-fetch|claude-code-2026-07-15-a7c9ca]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11|claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11]]'
theme: apps-integrations
type: change
---

# MCP tool calls running longer than 2 minutes now move to the background automati

<!-- chronolog:begin region="description" -->
MCP tool calls running longer than 2 minutes now move to the background automatically so the session stays usable; configure the threshold or disable with `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> MCP tool calls running longer than 2 minutes now move to the background automatically so the session stays usable; configure the threshold or disable with `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-15-hardened-synced-skill-plugin-directory-naming-on-windows-and-kept-ccr-web-fetch|claude-code-2026-07-15-a7c9ca]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1212
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes