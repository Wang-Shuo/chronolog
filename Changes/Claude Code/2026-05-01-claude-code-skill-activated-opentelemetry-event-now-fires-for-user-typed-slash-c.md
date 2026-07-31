---
card_id: claude-code-2026-05-01-2a9a10
date: '2026-05-01'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2025-01-14-scheduled-tasks-is-in-early-beta-for-plus-pro-and-teams-eventually-this-will-be|chatgpt-2025-01-14-24a2be]]'
  lag_days: 472
  role: follower
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-13-proactive-is-now-an-alias-for-loop|claude-code-2026-04-13-dcb90e]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 8c8a2f1ba0bc13137778e33066535ef1e2bc5aea81615ca8b606301788926ea3
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-03-11-most-plugins-contain-mcps-that-cloud-agents-can-use-when-kicked-off-manually-or|cursor-2026-03-11-453ce9]]'
- '[[Changes/Claude Code/2026-03-26-added-timestamp-markers-in-transcripts-when-scheduled-tasks-loop-croncreate-fire|claude-code-2026-03-26-2821da]]'
- '[[Changes/Claude Code/2026-04-13-proactive-is-now-an-alias-for-loop|claude-code-2026-04-13-dcb90e]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb|claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb]]'
theme: automation-scheduling
type: change
---

# `claude_code.skill_activated` OpenTelemetry event now fires for user-typed slash

<!-- chronolog:begin region="description" -->
`claude_code.skill_activated` OpenTelemetry event now fires for user-typed slash commands and carries a new `invocation_trigger` attribute (`"user-slash"`, `"claude-proactive"`, or `"nested-skill"`)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `claude_code.skill_activated` OpenTelemetry event now fires for user-typed slash commands and carries a new `invocation_trigger` attribute (`"user-slash"`, `"claude-proactive"`, or `"nested-skill"`)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-13-proactive-is-now-an-alias-for-loop|claude-code-2026-04-13-dcb90e]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: automation-scheduling
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2025-01-14-scheduled-tasks-is-in-early-beta-for-plus-pro-and-teams-eventually-this-will-be|chatgpt-2025-01-14-24a2be]]
- Lag Days: 472
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes