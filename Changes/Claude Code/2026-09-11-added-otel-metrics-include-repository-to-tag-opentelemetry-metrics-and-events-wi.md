---
card_id: claude-code-2026-09-11-7141cf
date: '2026-09-11'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1273
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: 74303be86799dd937d2ee76e864a6d370ae462546da4bc2b078c4147f3ec920c
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-11-7141cf
  comparison: ''
  date: '2026-09-11'
  description: 'Claude Code — v2.1.269: Added `OTEL_METRICS_INCLUDE_REPOSITORY` to
    tag OpenTelemetry metrics and events with `vcs.*` repository attributes; commit
    events get `vcs.ref.head.*` with `OTEL_LOG_TOOL_DETAILS`'
  evidence:
  - quote: Added `OTEL_METRICS_INCLUDE_REPOSITORY` to tag OpenTelemetry metrics and
      events with `vcs.*` repository attributes; commit events get `vcs.ref.head.*`
      with `OTEL_LOG_TOOL_DETAILS`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.269
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-otel-metrics-include-repository-to-tag-opentelemetry-metrics-and-events-wi
  source_release: claude-code-2026-09-11-v2-1-269-github-387243742-288e9189
  source_type: github_releases
  theme: developer-workflow
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: Added `OTEL_METRICS_INCLUDE_REPOSITORY` to tag OpenTelemetry metrics and
    events
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-28-added-attach-logs-stop-respawn-and-rm-to-claude-help-the-resume-message-for-a-ru|claude-code-2026-08-28-4b188b]]'
- '[[Changes/Claude Code/2026-09-04-added-bashoutputmaxchars-and-taskoutputmaxchars-settings-to-raise-how-much-comma|claude-code-2026-09-04-7733cf]]'
- '[[Changes/Claude Code/2026-09-09-improved-the-bash-tool-s-description-guidance-so-claude-describes-what-a-command|claude-code-2026-09-09-b44608]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-11-v2-1-269-github-387243742-288e9189|claude-code-2026-09-11-v2-1-269-github-387243742-288e9189]]'
source_type: github_releases
theme: developer-workflow
title: Added OTEL_METRICS_INCLUDE_REPOSITORY to tag OpenTelemetry metrics and events
type: change
---

# Added `OTEL_METRICS_INCLUDE_REPOSITORY` to tag OpenTelemetry metrics and events

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.269: Added `OTEL_METRICS_INCLUDE_REPOSITORY` to tag OpenTelemetry metrics and events with `vcs.*` repository attributes; commit events get `vcs.ref.head.*` with `OTEL_LOG_TOOL_DETAILS`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `OTEL_METRICS_INCLUDE_REPOSITORY` to tag OpenTelemetry metrics and events with `vcs.*` repository attributes; commit events get `vcs.ref.head.*` with `OTEL_LOG_TOOL_DETAILS`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.269
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1273
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes