---
card_id: claude-code-2026-07-01-4d022c
date: '2026-07-01'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1091
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-01-subagents-now-run-in-the-background-by-default-so-claude-keeps-working-while-the|claude-code-2026-07-01-0bd143]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: 15e876975dda53958239d8c13a131ec081ed57bfa478765060c972d32bb725cf
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-26-improved-claude-agents-completed-list-to-fill-available-vertical-space-on-short|claude-code-2026-06-26-3f8647]]'
- '[[Changes/Cursor/2026-06-29-cloud-agents-run-in-isolated-virtual-machines-with-full-development-environments|cursor-2026-06-29-40b244]]'
- '[[Changes/Claude Code/2026-07-01-subagents-now-run-in-the-background-by-default-so-claude-keeps-working-while-the|claude-code-2026-07-01-0bd143]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-01-v2-1-198-github-347599701-9cec0dab|claude-code-2026-07-01-v2-1-198-github-347599701-9cec0dab]]'
theme: agent-mode
type: change
---

# Added background agent notifications in `claude agents` — sessions that need inp

<!-- chronolog:begin region="description" -->
Added background agent notifications in `claude agents` — sessions that need input or finish now fire the `Notification` hook (`agent_needs_input` / `agent_completed`)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added background agent notifications in `claude agents` — sessions that need input or finish now fire the `Notification` hook (`agent_needs_input` / `agent_completed`)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.198
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-01-subagents-now-run-in-the-background-by-default-so-claude-keeps-working-while-the|claude-code-2026-07-01-0bd143]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1091
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes