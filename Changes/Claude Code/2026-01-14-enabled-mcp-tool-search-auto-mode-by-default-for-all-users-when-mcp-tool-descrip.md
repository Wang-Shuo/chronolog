---
card_id: claude-code-2026-01-14-2caaef
date: '2026-01-14'
description: 'Claude Code · 2026-01-14 · Context Window: Enabled MCP tool search auto
  mode by default for all users. When MCP tool descriptions exceed 10% of the context…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 986
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 205df10431c612c64289fa84af3dd463755613a897c636d8c41de050ba6a49b8
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-01-14-2caaef
  comparison: ''
  date: '2026-01-14'
  description: 'Claude Code — v2.1.7: Enabled MCP tool search auto mode by default
    for all users. When MCP tool descriptions exceed 10% of the context window, they
    are automatically deferred and discovered via the MCPSearch tool instead of being
    loaded upfront. This reduces context usage for users with many MCP tools configured.
    Users can disable this by adding `MCPSearch` to `disallowedTools` in their settings.'
  evidence:
  - quote: Enabled MCP tool search auto mode by default for all users. When MCP tool
      descriptions exceed 10% of the context window, they are automatically deferred
      and discovered via the MCPSearch tool instead of being loaded upfront. This
      reduces context usage for users with many MCP tools configured. Users can disable
      this by adding `MCPSearch` to `disallowedTools` in their settings.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.7
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: enabled-mcp-tool-search-auto-mode-by-default-for-all-users-when-mcp-tool-descrip
  source_release: claude-code-2026-01-14-v2-1-7-github-276555327-bf21dc80
  source_type: github_releases
  theme: context-window
  theme_matches:
  - matched_terms:
    - context window
    - context
    score: 170
    theme: context-window
  - matched_terms:
    - auto mode
    score: 60
    theme: agent-mode
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  theme_resolution: manual-semantic-rule-v2
  title: Enabled MCP tool search auto mode by default for all users
  type: change
related_changes:
- '[[Changes/Cursor/2025-12-18-conversation-insights-2efafc|Conversation insights]]'
- '[[Changes/Claude Code/2025-12-19-improved-context-command-visualization-with-grouped-skills-and-agents-by-source|Improved
  /context command visualization with grouped skills and agents by source…]]'
- '[[Changes/Claude Code/2026-01-13-added-context-window-used-percentage-and-context-window-remaining-percentage-fie|Added
  context_window.used_percentage and context_window.remaining_percentage…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-01-14-v2-1-7-github-276555327-bf21dc80|claude-code-2026-01-14-v2-1-7-github-276555327-bf21dc80]]'
source_type: github_releases
theme: context-window
title: Enabled MCP tool search auto mode by default for all users
type: change
---

<!-- chronolog:begin region="header" -->
# Enabled MCP tool search auto mode by default for all users

**Claude Code** · 2026-01-14 · [[Themes/context-window|Context Window]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.7) · from [[Releases/Claude Code/claude-code-2026-01-14-v2-1-7-github-276555327-bf21dc80|v2.1.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Enabled MCP tool search auto mode by default for all users. When MCP tool descriptions exceed 10% of the context window, they are automatically deferred and discovered via the MCPSearch tool instead of being loaded upfront. This reduces context usage for users with many MCP tools configured. Users can disable this by adding `MCPSearch` to `disallowedTools` in their settings.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-01-14-added-inline-display-of-agent-s-final-response-in-task-notifications-making-it-e|Added inline display of agent's final response in task notifications, making…]] · Agent Mode
- [[Changes/Claude Code/2026-01-14-improved-typing-responsiveness-by-reducing-memory-allocation-overhead-in-termina|Improved typing responsiveness by reducing memory allocation overhead in terminal…]] · Reliability and Performance
- [[Changes/Claude Code/2026-01-14-changed-oauth-and-api-console-urls-from-console-anthropic-com-to-platform-claude|Changed OAuth and API Console URLs from console.anthropic.com to platform.claude.com]] · Account and Access
- [[Changes/Claude Code/2026-01-14-added-showturnduration-setting-to-hide-turn-duration-messages-e-g-cooked-for-1m|Added showTurnDuration setting to hide turn duration messages (e.g., "Cooked for 1m 6s")]] · Interface Experience
- [[Changes/Claude Code/2026-01-14-2-safety-and-privacy-changes-in-v2-1-7|2 Safety and Privacy changes in v2.1.7]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-01-13 · Claude Code · [[Changes/Claude Code/2026-01-13-added-context-window-used-percentage-and-context-window-remaining-percentage-fie|Added context_window.used_percentage and context_window.remaining_percentage…]]
- Later: 2026-01-16 · Claude Code · [[Changes/Claude Code/2026-01-16-added-auto-n-syntax-for-configuring-the-mcp-tool-search-auto-enable-threshold-wh|Added auto:N syntax for configuring the MCP tool search auto-enable threshold…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-01-14-2caaef&body=Card%3A%20Changes%2FClaude%20Code%2F2026-01-14-enabled-mcp-tool-search-auto-mode-by-default-for-all-users-when-mcp-tool-descrip.md%0ACard%20ID%3A%20claude-code-2026-01-14-2caaef%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->