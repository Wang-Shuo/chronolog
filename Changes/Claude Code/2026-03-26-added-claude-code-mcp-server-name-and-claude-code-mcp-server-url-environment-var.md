---
card_id: claude-code-2026-03-26-30d322
date: '2026-03-26'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1099
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-25-added-cwdchanged-and-filechanged-hook-events-for-reactive-environment-management|claude-code-2026-03-25-f3027d]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 90e02ac6dbe2cf452672d0e2d5d921b65d583e695531e729b4a4b837ca5be434
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-25-added-claude-code-subprocess-env-scrub-1-to-strip-anthropic-and-cloud-provider-c|claude-code-2026-03-25-502a32]]'
- '[[Changes/Claude Code/2026-03-25-added-disabledeeplinkregistration-setting-to-prevent-claude-cli-protocol-handler|claude-code-2026-03-25-7f5292]]'
- '[[Changes/Claude Code/2026-03-25-added-cwdchanged-and-filechanged-hook-events-for-reactive-environment-management|claude-code-2026-03-25-f3027d]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-26-v2-1-85-github-302129484-6eb9dcd7|claude-code-2026-03-26-v2-1-85-github-302129484-6eb9dcd7]]'
theme: apps-integrations
type: change
---

# Added `CLAUDE_CODE_MCP_SERVER_NAME` and `CLAUDE_CODE_MCP_SERVER_URL` environment

<!-- chronolog:begin region="description" -->
Added `CLAUDE_CODE_MCP_SERVER_NAME` and `CLAUDE_CODE_MCP_SERVER_URL` environment variables to MCP `headersHelper` scripts, allowing one helper to serve multiple servers
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_CODE_MCP_SERVER_NAME` and `CLAUDE_CODE_MCP_SERVER_URL` environment variables to MCP `headersHelper` scripts, allowing one helper to serve multiple servers
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.85
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-25-added-cwdchanged-and-filechanged-hook-events-for-reactive-environment-management|claude-code-2026-03-25-f3027d]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1099
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes