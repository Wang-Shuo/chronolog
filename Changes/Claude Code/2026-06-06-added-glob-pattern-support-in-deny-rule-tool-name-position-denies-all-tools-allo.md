---
card_id: claude-code-2026-06-06-cd06e2
date: '2026-06-06'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1171
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-04-added-plugin-list-command-to-list-installed-plugins-with-enabled-disabled-filter|claude-code-2026-06-04-ddcc08]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 17f09f2653f700a95eadc9ec14b175300c76aae1a36572cad71ee79d757b149d
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-04-added-plugin-list-command-to-list-installed-plugins-with-enabled-disabled-filter|claude-code-2026-06-04-ddcc08]]'
- '[[Changes/Cursor/2026-06-04-custom-tools|cursor-2026-06-04-2a185a]]'
- '[[Changes/Cursor/2026-06-04-we-ve-shipped-a-batch-of-new-functionality-across-the-typescript-and-python-sdks|cursor-2026-06-04-73350b]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-06-v2-1-166-github-335118845-ef990727|claude-code-2026-06-06-v2-1-166-github-335118845-ef990727]]'
theme: apps-integrations
type: change
---

# Added glob pattern support in deny rule tool-name position (`"*"` denies all too

<!-- chronolog:begin region="description" -->
Added glob pattern support in deny rule tool-name position (`"*"` denies all tools); allow rules reject non-MCP globs, and unknown tool names in deny rules warn at startup
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added glob pattern support in deny rule tool-name position (`"*"` denies all tools); allow rules reject non-MCP globs, and unknown tool names in deny rules warn at startup
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.166
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-04-added-plugin-list-command-to-list-installed-plugins-with-enabled-disabled-filter|claude-code-2026-06-04-ddcc08]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1171
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes