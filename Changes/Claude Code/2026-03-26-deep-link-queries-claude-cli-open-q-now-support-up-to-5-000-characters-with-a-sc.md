---
card_id: claude-code-2026-03-26-7f4ed1
date: '2026-03-26'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1099
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-26-added-claude-code-mcp-server-name-and-claude-code-mcp-server-url-environment-var|claude-code-2026-03-26-30d322]]'
extractor_version: fallback-v2
impact: significant
machine_hash: a26190df03740f5c1286131efac7303f3b188a591b9b2d2e7733aa30f568885a
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-25-added-disabledeeplinkregistration-setting-to-prevent-claude-cli-protocol-handler|claude-code-2026-03-25-7f5292]]'
- '[[Changes/Claude Code/2026-03-25-added-cwdchanged-and-filechanged-hook-events-for-reactive-environment-management|claude-code-2026-03-25-f3027d]]'
- '[[Changes/Claude Code/2026-03-26-added-claude-code-mcp-server-name-and-claude-code-mcp-server-url-environment-var|claude-code-2026-03-26-30d322]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-26-v2-1-85-github-302129484-6eb9dcd7|claude-code-2026-03-26-v2-1-85-github-302129484-6eb9dcd7]]'
theme: apps-integrations
type: change
---

# Deep link queries (`claude-cli://open?q=…`) now support up to 5,000 characters,

<!-- chronolog:begin region="description" -->
Deep link queries (`claude-cli://open?q=…`) now support up to 5,000 characters, with a "scroll to review" warning for long pre-filled prompts
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Deep link queries (`claude-cli://open?q=…`) now support up to 5,000 characters, with a "scroll to review" warning for long pre-filled prompts
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.85
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-26-added-claude-code-mcp-server-name-and-claude-code-mcp-server-url-environment-var|claude-code-2026-03-26-30d322]]
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