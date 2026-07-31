---
card_id: claude-code-2026-07-17-967a66
date: '2026-07-17'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1107
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-15-added-forward-subagent-text-flag-and-claude-code-forward-subagent-text-environme|claude-code-2026-07-15-12d419]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: e7b0fa0fd79f5c60336b971f6c802c9ac333dec779e189ac17137a2088657118
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-14-added-claude-code-process-wrapper-agent-view-and-the-background-service-now-hono|claude-code-2026-07-14-dfb540]]'
- '[[Changes/Claude Code/2026-07-15-improved-background-agent-result-reporting-claude-now-reports-the-status-of-stil|claude-code-2026-07-15-05aede]]'
- '[[Changes/Claude Code/2026-07-15-added-forward-subagent-text-flag-and-claude-code-forward-subagent-text-environme|claude-code-2026-07-15-12d419]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11|claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11]]'
theme: agent-mode
type: change
---

# Added a per-session cap on subagent spawns (default 200, override with `CLAUDE_C

<!-- chronolog:begin region="description" -->
Added a per-session cap on subagent spawns (default 200, override with `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`) to stop runaway delegation loops; `/clear` resets the budget
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added a per-session cap on subagent spawns (default 200, override with `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`) to stop runaway delegation loops; `/clear` resets the budget
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-15-added-forward-subagent-text-flag-and-claude-code-forward-subagent-text-environme|claude-code-2026-07-15-12d419]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1107
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes