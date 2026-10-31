---
card_id: claude-code-2026-07-06-090056
date: '2026-07-06'
description: 'Claude Code · 2026-07-06 · Agent Mode: 3 changes in v2.1.202 — Added
  a "Dynamic workflow size" setting in `/config` for controlling how large Claude
  generally…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1096
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f8b9340d8c22a78990549efe65f25bbcb6ed183cd939f22870fa9626d5a244a5
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-06-090056
  comparison: ''
  date: '2026-07-06'
  description: 'Claude Code — v2.1.202: 3 Agent Mode changes'
  evidence:
  - quote: Added a "Dynamic workflow size" setting in `/config` for controlling how
      large Claude generally makes dynamic workflows (small/medium/large agent counts)
      — an advisory guideline, not an enforced cap
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.202
  - quote: Added `workflow.run_id` and `workflow.name` OpenTelemetry attributes to
      telemetry emitted by workflow-spawned agents, so a workflow run's activity can
      be reconstructed from OTel data
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.202
  - quote: 'Improved `/workflows` agent list layout: wider titles, a dedicated time
      column, shorter model names, and no per-row tool-call counts'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.202
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-agent-mode-changes-in-v2-1-202
  source_release: claude-code-2026-07-06-v2-1-202-github-349856235-58e6d3e8
  source_type: github_releases
  theme: agent-mode
  title: 3 Agent Mode changes in v2.1.202
  type: change
related_changes:
- '[[Changes/Cursor/2026-06-29-live-activities-and-push-notifications|Live Activities
  and push notifications]]'
- '[[Changes/Cursor/2026-06-29-cursor-for-ios-is-now-available-in-public-beta-on-all-paid-plans-launch-and-mana|Cursor
  for iOS is now available in public beta on all paid plans]]'
- '[[Changes/Claude Code/2026-07-01-5-agent-mode-changes-in-v2-1-198|5 Agent Mode
  changes in v2.1.198]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-06-v2-1-202-github-349856235-58e6d3e8|claude-code-2026-07-06-v2-1-202-github-349856235-58e6d3e8]]'
source_type: github_releases
theme: agent-mode
title: 3 Agent Mode changes in v2.1.202
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Agent Mode changes in v2.1.202

**Claude Code** · 2026-07-06 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.202) · from [[Releases/Claude Code/claude-code-2026-07-06-v2-1-202-github-349856235-58e6d3e8|v2.1.202]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a "Dynamic workflow size" setting in `/config` for controlling how large Claude generally makes dynamic workflows (small/medium/large agent counts) — an advisory guideline, not an enforced cap

> Added `workflow.run_id` and `workflow.name` OpenTelemetry attributes to telemetry emitted by workflow-spawned agents, so a workflow run's activity can be reconstructed from OTel data

> Improved `/workflows` agent list layout: wider titles, a dedicated time column, shorter model names, and no per-row tool-call counts

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.202
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-06-changed-review-pr-back-to-a-fast-single-pass-review-use-code-review-level-pr-for|Changed /review pr back to a fast single-pass review]] · Developer Workflow
- [[Changes/Claude Code/2026-07-06-improved-mcp-error-messages-clearer-error-when-a-server-config-has-url-but-no-ty|Improved MCP error messages]] · Apps and Integrations
- [[Changes/Claude Code/2026-07-06-fixed-remote-control-sessions-showing-the-wrong-permission-mode-in-the-mobile-an|Fixed /remote-control sessions showing the wrong permission mode in the mobile…]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-07-01 · Claude Code · [[Changes/Claude Code/2026-07-01-5-agent-mode-changes-in-v2-1-198|5 Agent Mode changes in v2.1.198]]
- Later: 2026-07-07 · Claude Code · [[Changes/Claude Code/2026-07-07-2-agent-mode-changes-in-v2-1-203|2 Agent Mode changes in v2.1.203]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-06-090056&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-06-3-agent-mode-changes-in-v2-1-202.md%0ACard%20ID%3A%20claude-code-2026-07-06-090056%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.202%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->