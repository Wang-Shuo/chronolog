---
card_id: cursor-2026-06-04-0a3ca5
date: '2026-06-04'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1064
  role: variant
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Cursor/2026-05-29-configure-your-run-mode-in-settings-cursor-settings-agents-approvals-execution-y|cursor-2026-05-29-d4afd0]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: 80d0277c83739fe4ca7be8533ffe8712b1e6c90062e4be3ef1e2cfbb619bea5a
product: cursor
product_name: Cursor
related_changes:
- '[[Changes/Claude Code/2026-06-02-improved-performance-of-opening-recently-inactive-background-agent-sessions-in-c|claude-code-2026-06-02-ab10e4]]'
- '[[Changes/Claude Code/2026-06-02-claude-agents-rows-now-show-done-total-before-the-detail-when-work-is-fanned-out|claude-code-2026-06-02-e9ef76]]'
- '[[Changes/ChatGPT/2026-06-04-lockdown-mode-is-now-available-to-all-logged-in-users-across-account-types-and-w|chatgpt-2026-06-04-88660d]]'
source_release: '[[Releases/Cursor/cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856|cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856]]'
theme: agent-mode
type: change
---

# Before this, exposing a custom capability meant standing up your own stdio or re

<!-- chronolog:begin region="description" -->
Before this, exposing a custom capability meant standing up your own stdio or remote HTTP MCP server and wiring it into the agent. Now a function definition is enough. Custom tools are also visible to every subagent of a parent agent, so a tool you define once is available throughout the whole run.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Before this, exposing a custom capability meant standing up your own stdio or remote HTTP MCP server and wiring it into the agent. Now a function definition is enough. Custom tools are also visible to every subagent of a parent agent, so a tool you define once is available throughout the whole run.
>
> Source: https://cursor.com/changelog/sdk-updates-jun-2026
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Cursor/2026-05-29-configure-your-run-mode-in-settings-cursor-settings-agents-approvals-execution-y|cursor-2026-05-29-d4afd0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: variant
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1064
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes