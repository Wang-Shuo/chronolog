---
card_id: claude-code-2026-03-17-d73d30
date: '2026-03-17'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1090
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-17-added-effort-maxturns-and-disallowedtools-frontmatter-support-for-plugin-shipped|claude-code-2026-03-17-567e32]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 2704cc3ebb8bafa6dac7de6925cae4ec49a3c56e4eba7c117ee0b082daa85d61
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-14-added-mcp-elicitation-support-mcp-servers-can-now-request-structured-input-mid-t|claude-code-2026-03-14-928360]]'
- '[[Changes/Claude Code/2026-03-17-added-stopfailure-hook-event-that-fires-when-the-turn-ends-due-to-an-api-error-r|claude-code-2026-03-17-331b63]]'
- '[[Changes/Claude Code/2026-03-17-added-effort-maxturns-and-disallowedtools-frontmatter-support-for-plugin-shipped|claude-code-2026-03-17-567e32]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-17-v2-1-78-github-298204446-1f2c1721|claude-code-2026-03-17-v2-1-78-github-298204446-1f2c1721]]'
theme: apps-integrations
type: change
---

# Added `${CLAUDE_PLUGIN_DATA}` variable for plugin persistent state that survives

<!-- chronolog:begin region="description" -->
Added `${CLAUDE_PLUGIN_DATA}` variable for plugin persistent state that survives plugin updates; `/plugin uninstall` prompts before deleting it
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `${CLAUDE_PLUGIN_DATA}` variable for plugin persistent state that survives plugin updates; `/plugin uninstall` prompts before deleting it
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.78
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-17-added-effort-maxturns-and-disallowedtools-frontmatter-support-for-plugin-shipped|claude-code-2026-03-17-567e32]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1090
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes