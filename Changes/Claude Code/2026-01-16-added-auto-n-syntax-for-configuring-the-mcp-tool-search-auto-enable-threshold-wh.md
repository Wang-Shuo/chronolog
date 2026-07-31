---
card_id: claude-code-2026-01-16-35ca77
date: '2026-01-16'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  lag_days: 988
  role: follower
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-01-13-added-context-window-used-percentage-and-context-window-remaining-percentage-fie|claude-code-2026-01-13-00ffe3]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: b30ca2b6efcdc0dc0143a66887954865366ec410bb9639d6d886e2098b840238
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2025-09-12-cursor-automatically-summarizes-long-conversation-for-you-when-reaching-the-cont|cursor-2025-09-12-7d0a07]]'
- '[[Changes/Cursor/2025-12-18-cursor-can-now-analyze-the-code-and-context-in-each-agent-session-to-understand|cursor-2025-12-18-becfd8]]'
- '[[Changes/Claude Code/2026-01-13-added-context-window-used-percentage-and-context-window-remaining-percentage-fie|claude-code-2026-01-13-00ffe3]]'
source_release: '[[Releases/Claude Code/claude-code-2026-01-16-v2-1-9-github-277250534-9563859d|claude-code-2026-01-16-v2-1-9-github-277250534-9563859d]]'
theme: context-window
type: change
---

# Added `auto:N` syntax for configuring the MCP tool search auto-enable threshold,

<!-- chronolog:begin region="description" -->
Added `auto:N` syntax for configuring the MCP tool search auto-enable threshold, where N is the context window percentage (0-100)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `auto:N` syntax for configuring the MCP tool search auto-enable threshold, where N is the context window percentage (0-100)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.9
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-01-13-added-context-window-used-percentage-and-context-window-remaining-percentage-fie|claude-code-2026-01-13-00ffe3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 988
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes