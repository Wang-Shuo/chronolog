---
card_id: claude-code-2026-03-07-3270e5
date: '2026-03-07'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2025-01-14-scheduled-tasks-is-in-early-beta-for-plus-pro-and-teams-eventually-this-will-be|chatgpt-2025-01-14-24a2be]]'
  lag_days: 417
  role: follower
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-07-added-cron-scheduling-tools-for-recurring-prompts-within-a-session|claude-code-2026-03-07-0243fb]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: a18c6bacb043be5bd2c4ef3cdfd8b201695a94e2d7ec85a60cbd77cda6f57abb
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-03-05-create-automations-at-cursor-com-automations-or-start-from-a-template-read-more|cursor-2026-03-05-e7f5c3]]'
- '[[Changes/Cursor/2026-03-05-automations-run-on-schedules-or-are-triggered-by-events-from-slack-linear-github|cursor-2026-03-05-fc1325]]'
- '[[Changes/Claude Code/2026-03-07-added-cron-scheduling-tools-for-recurring-prompts-within-a-session|claude-code-2026-03-07-0243fb]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-07-v2-1-71-github-294146317-ab5a32e0|claude-code-2026-03-07-v2-1-71-github-294146317-ab5a32e0]]'
theme: automation-scheduling
type: change
---

# Added `/loop` command to run a prompt or slash command on a recurring interval (

<!-- chronolog:begin region="description" -->
Added `/loop` command to run a prompt or slash command on a recurring interval (e.g. `/loop 5m check the deploy`)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `/loop` command to run a prompt or slash command on a recurring interval (e.g. `/loop 5m check the deploy`)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.71
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-07-added-cron-scheduling-tools-for-recurring-prompts-within-a-session|claude-code-2026-03-07-0243fb]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: automation-scheduling
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2025-01-14-scheduled-tasks-is-in-early-beta-for-plus-pro-and-teams-eventually-this-will-be|chatgpt-2025-01-14-24a2be]]
- Lag Days: 417
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes