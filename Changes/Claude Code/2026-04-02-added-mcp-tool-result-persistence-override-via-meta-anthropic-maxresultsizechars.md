---
card_id: claude-code-2026-04-02-ba957b
date: '2026-04-02'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1106
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-02-added-support-for-multi-line-prompts-in-claude-cli-open-q-deep-links-encoded-new|claude-code-2026-04-02-a9c889]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 00258bec0086ebc63bd963e2e21b488acffb2a3cdd43a3c4af9f83fd985c4873
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-01-added-mcp-connection-nonblocking-true-for-p-mode-to-skip-the-mcp-connection-wait|claude-code-2026-04-01-210067]]'
- '[[Changes/Claude Code/2026-04-01-added-claude-code-plugin-keep-marketplace-on-failure-env-var-to-keep-the-existin|claude-code-2026-04-01-5bb86f]]'
- '[[Changes/Claude Code/2026-04-02-added-support-for-multi-line-prompts-in-claude-cli-open-q-deep-links-encoded-new|claude-code-2026-04-02-a9c889]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-02-v2-1-91-github-304899951-a56266fc|claude-code-2026-04-02-v2-1-91-github-304899951-a56266fc]]'
theme: apps-integrations
type: change
---

# Added MCP tool result persistence override via `_meta["anthropic/maxResultSizeCh

<!-- chronolog:begin region="description" -->
Added MCP tool result persistence override via `_meta["anthropic/maxResultSizeChars"]` annotation (up to 500K), allowing larger results like DB schemas to pass through without truncation
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added MCP tool result persistence override via `_meta["anthropic/maxResultSizeChars"]` annotation (up to 500K), allowing larger results like DB schemas to pass through without truncation
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.91
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-02-added-support-for-multi-line-prompts-in-claude-cli-open-q-deep-links-encoded-new|claude-code-2026-04-02-a9c889]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1106
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes