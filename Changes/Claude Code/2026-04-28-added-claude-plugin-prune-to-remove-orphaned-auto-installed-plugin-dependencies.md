---
card_id: claude-code-2026-04-28-1fc875
date: '2026-04-28'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1132
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-23-hooks-can-now-invoke-mcp-tools-directly-via-type-mcp-tool|claude-code-2026-04-23-f3019e]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 3abe680a2698649e692b64bd2eeeb20eec72f6e0402efe7e1bd3b5612ad067d1
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-22-faster-startup-when-both-local-and-claude-ai-mcp-servers-are-configured-concurre|claude-code-2026-04-22-b8b25a]]'
- '[[Changes/Claude Code/2026-04-23-create-and-switch-between-named-custom-themes-from-theme-or-hand-edit-json-files|claude-code-2026-04-23-72b7ff]]'
- '[[Changes/Claude Code/2026-04-23-hooks-can-now-invoke-mcp-tools-directly-via-type-mcp-tool|claude-code-2026-04-23-f3019e]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-28-v2-1-121-github-314262096-ff31d5ce|claude-code-2026-04-28-v2-1-121-github-314262096-ff31d5ce]]'
theme: apps-integrations
type: change
---

# Added `claude plugin prune` to remove orphaned auto-installed plugin dependencie

<!-- chronolog:begin region="description" -->
Added `claude plugin prune` to remove orphaned auto-installed plugin dependencies; `plugin uninstall --prune` cascades
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `claude plugin prune` to remove orphaned auto-installed plugin dependencies; `plugin uninstall --prune` cascades
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.121
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-23-hooks-can-now-invoke-mcp-tools-directly-via-type-mcp-tool|claude-code-2026-04-23-f3019e]]
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