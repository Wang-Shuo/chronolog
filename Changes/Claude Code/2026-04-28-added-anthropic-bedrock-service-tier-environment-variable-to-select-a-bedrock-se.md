---
card_id: claude-code-2026-04-28-4ff006
date: '2026-04-28'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1132
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-28-added-claude-plugin-prune-to-remove-orphaned-auto-installed-plugin-dependencies|claude-code-2026-04-28-1fc875]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 49a5b74d8ea36eea8fa8729c4630d0ba6b7f6eaaa2c680541e437a807ba8f10e
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-23-create-and-switch-between-named-custom-themes-from-theme-or-hand-edit-json-files|claude-code-2026-04-23-72b7ff]]'
- '[[Changes/Claude Code/2026-04-23-hooks-can-now-invoke-mcp-tools-directly-via-type-mcp-tool|claude-code-2026-04-23-f3019e]]'
- '[[Changes/Claude Code/2026-04-28-added-claude-plugin-prune-to-remove-orphaned-auto-installed-plugin-dependencies|claude-code-2026-04-28-1fc875]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-28-v2-1-122-github-314740479-0cc42196|claude-code-2026-04-28-v2-1-122-github-314740479-0cc42196]]'
theme: apps-integrations
type: change
---

# Added `ANTHROPIC_BEDROCK_SERVICE_TIER` environment variable to select a Bedrock

<!-- chronolog:begin region="description" -->
Added `ANTHROPIC_BEDROCK_SERVICE_TIER` environment variable to select a Bedrock service tier (`default`, `flex`, or `priority`), sent as the `X-Amzn-Bedrock-Service-Tier` header
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `ANTHROPIC_BEDROCK_SERVICE_TIER` environment variable to select a Bedrock service tier (`default`, `flex`, or `priority`), sent as the `X-Amzn-Bedrock-Service-Tier` header
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.122
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-28-added-claude-plugin-prune-to-remove-orphaned-auto-installed-plugin-dependencies|claude-code-2026-04-28-1fc875]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1132
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes