---
card_id: claude-code-2026-07-06-d6dd3f
date: '2026-07-06'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1096
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: f100b187fc5910b1a7afee0b7bb91460859bdab2ce0df4d055121281d315ada6
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-06-d6dd3f
  comparison: ''
  date: '2026-07-06'
  description: 'Claude Code — v2.1.202: Added `workflow.run_id` and `workflow.name`
    OpenTelemetry attributes to telemetry emitted by workflow-spawned agents, so a
    workflow run''s activity can be reconstructed from OTel data'
  evidence:
  - quote: Added `workflow.run_id` and `workflow.name` OpenTelemetry attributes to
      telemetry emitted by workflow-spawned agents, so a workflow run's activity can
      be reconstructed from OTel data
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.202
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-workflow-run-id-and-workflow-name-opentelemetry-attributes-to-telemetry-em
  source_release: claude-code-2026-07-06-v2-1-202-github-349856235-58e6d3e8
  source_type: github_releases
  theme: agent-mode
  title: Added `workflow.run_id` and `workflow.name` OpenTelemetry attributes to telemetry…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-01-subagents-now-run-in-the-background-by-default-so-claude-keeps-working-while-the|claude-code-2026-07-01-0bd143]]'
- '[[Changes/Claude Code/2026-07-01-added-background-agent-notifications-in-claude-agents-sessions-that-need-input-o|claude-code-2026-07-01-4d022c]]'
- '[[Changes/Claude Code/2026-07-06-added-a-dynamic-workflow-size-setting-in-config-for-controlling-how-large-claude|claude-code-2026-07-06-9942eb]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-06-v2-1-202-github-349856235-58e6d3e8|claude-code-2026-07-06-v2-1-202-github-349856235-58e6d3e8]]'
source_type: github_releases
theme: agent-mode
title: Added workflow.run_id and workflow.name OpenTelemetry attributes to telemetry…
type: change
---

# Added `workflow.run_id` and `workflow.name` OpenTelemetry attributes to telemetry…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.202: Added `workflow.run_id` and `workflow.name` OpenTelemetry attributes to telemetry emitted by workflow-spawned agents, so a workflow run's activity can be reconstructed from OTel data
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `workflow.run_id` and `workflow.name` OpenTelemetry attributes to telemetry emitted by workflow-spawned agents, so a workflow run's activity can be reconstructed from OTel data
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.202
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
- Lag Days: 1096
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes