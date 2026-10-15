---
card_id: claude-code-2026-07-17-967a66
date: '2026-07-17'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1107
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: cf2be60bedc25f57839911e7559dd95ae335aa157148cd98a21e027f294b8605
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-17-967a66
  comparison: ''
  date: '2026-07-17'
  description: 'Claude Code — v2.1.212: Added a per-session cap on subagent spawns
    (default 200, override with `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`) to stop runaway
    delegation loops; `/clear` resets the budget'
  evidence:
  - quote: Added a per-session cap on subagent spawns (default 200, override with
      `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`) to stop runaway delegation loops; `/clear`
      resets the budget
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-a-per-session-cap-on-subagent-spawns-default-200-override-with-claude-code
  source_release: claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11
  source_type: github_releases
  theme: agent-mode
  title: Added a per-session cap on subagent spawns…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-14-added-claude-code-process-wrapper-agent-view-and-the-background-service-now-hono|claude-code-2026-07-14-dfb540]]'
- '[[Changes/Claude Code/2026-07-15-improved-background-agent-result-reporting-claude-now-reports-the-status-of-stil|claude-code-2026-07-15-05aede]]'
- '[[Changes/Claude Code/2026-07-15-added-forward-subagent-text-flag-and-claude-code-forward-subagent-text-environme|claude-code-2026-07-15-12d419]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11|claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11]]'
source_type: github_releases
theme: agent-mode
title: Added a per-session cap on subagent spawns…
type: change
---

# Added a per-session cap on subagent spawns…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.212: Added a per-session cap on subagent spawns (default 200, override with `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`) to stop runaway delegation loops; `/clear` resets the budget
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added a per-session cap on subagent spawns (default 200, override with `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`) to stop runaway delegation loops; `/clear` resets the budget
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1107
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes