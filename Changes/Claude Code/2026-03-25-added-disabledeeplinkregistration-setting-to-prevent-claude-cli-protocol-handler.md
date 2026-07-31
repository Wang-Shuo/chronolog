---
card_id: claude-code-2026-03-25-7f5292
date: '2026-03-25'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1098
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-25-added-claude-code-subprocess-env-scrub-1-to-strip-anthropic-and-cloud-provider-c|claude-code-2026-03-25-502a32]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 29b5d1892ddadf547233f3dbf11e6536605c70400d6175ad8da6f3893a8f2aa1
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-20-improved-mcp-read-search-tool-calls-to-collapse-into-a-single-queried-server-lin|claude-code-2026-03-20-a75158]]'
- '[[Changes/ChatGPT/2026-03-25-google-s-file-connectors-in-chatgpt-are-now-unified-under-google-drive-providing|chatgpt-2026-03-25-6c2ae6]]'
- '[[Changes/Claude Code/2026-03-25-added-claude-code-subprocess-env-scrub-1-to-strip-anthropic-and-cloud-provider-c|claude-code-2026-03-25-502a32]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317|claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317]]'
theme: apps-integrations
type: change
---

# Added `disableDeepLinkRegistration` setting to prevent `claude-cli://` protocol

<!-- chronolog:begin region="description" -->
Added `disableDeepLinkRegistration` setting to prevent `claude-cli://` protocol handler registration
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `disableDeepLinkRegistration` setting to prevent `claude-cli://` protocol handler registration
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-25-added-claude-code-subprocess-env-scrub-1-to-strip-anthropic-and-cloud-provider-c|claude-code-2026-03-25-502a32]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1098
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes