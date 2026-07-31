---
card_id: claude-code-2026-07-06-d6dd3f
date: '2026-07-06'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1096
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-06-added-a-dynamic-workflow-size-setting-in-config-for-controlling-how-large-claude|claude-code-2026-07-06-9942eb]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 3e144b489ed03f8e5e51c0fb1f6ece69baba9a7cc03d92dba8f0cbc3154d557c
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-01-subagents-now-run-in-the-background-by-default-so-claude-keeps-working-while-the|claude-code-2026-07-01-0bd143]]'
- '[[Changes/Claude Code/2026-07-01-added-background-agent-notifications-in-claude-agents-sessions-that-need-input-o|claude-code-2026-07-01-4d022c]]'
- '[[Changes/Claude Code/2026-07-06-added-a-dynamic-workflow-size-setting-in-config-for-controlling-how-large-claude|claude-code-2026-07-06-9942eb]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-06-v2-1-202-github-349856235-58e6d3e8|claude-code-2026-07-06-v2-1-202-github-349856235-58e6d3e8]]'
theme: agent-mode
type: change
---

# Added `workflow.run_id` and `workflow.name` OpenTelemetry attributes to telemetr

<!-- chronolog:begin region="description" -->
Added `workflow.run_id` and `workflow.name` OpenTelemetry attributes to telemetry emitted by workflow-spawned agents, so a workflow run's activity can be reconstructed from OTel data
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `workflow.run_id` and `workflow.name` OpenTelemetry attributes to telemetry emitted by workflow-spawned agents, so a workflow run's activity can be reconstructed from OTel data
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.202
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-06-added-a-dynamic-workflow-size-setting-in-config-for-controlling-how-large-claude|claude-code-2026-07-06-9942eb]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1096
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes