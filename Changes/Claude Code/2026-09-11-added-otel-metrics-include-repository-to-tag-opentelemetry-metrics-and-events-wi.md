---
card_id: claude-code-2026-09-11-7141cf
date: '2026-09-11'
description: 'Claude Code · 2026-09-11 · Developer Workflow: Added `OTEL_METRICS_INCLUDE_REPOSITORY`
  to tag OpenTelemetry metrics and events with `vcs.*` repository…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1273
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 090d74cc5b4d7814c4efc6e8b1e7b997f2b8a0087dab3da823a691f7c37e737f
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
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-otel-metrics-include-repository-to-tag-opentelemetry-metrics-and-events-wi
  source_release: claude-code-2026-09-11-v2-1-269-github-387243742-288e9189
  source_type: github_releases
  theme: developer-workflow
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: Added `OTEL_METRICS_INCLUDE_REPOSITORY` to tag OpenTelemetry metrics and
    events…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-08-2-developer-workflow-changes-in-v2-1-265|2 Developer
  Workflow changes in v2.1.265]]'
- '[[Changes/Claude Code/2026-09-09-3-developer-workflow-changes-in-v2-1-267|3 Developer
  Workflow changes in v2.1.267]]'
- '[[Changes/Claude Code/2026-09-10-code-review-added-a-note-under-the-still-open-findings-list-in-follow-up-reviews|Code
  Review Added a note under the still-open findings list in follow-up reviews]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-11-v2-1-269-github-387243742-288e9189|claude-code-2026-09-11-v2-1-269-github-387243742-288e9189]]'
source_type: github_releases
theme: developer-workflow
title: Added OTEL_METRICS_INCLUDE_REPOSITORY to tag OpenTelemetry metrics and events…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `OTEL_METRICS_INCLUDE_REPOSITORY` to tag OpenTelemetry metrics and events…

**Claude Code** · 2026-09-11 · [[Themes/developer-workflow|Developer Workflow]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.269) · from [[Releases/Claude Code/claude-code-2026-09-11-v2-1-269-github-387243742-288e9189|v2.1.269]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `OTEL_METRICS_INCLUDE_REPOSITORY` to tag OpenTelemetry metrics and events with `vcs.*` repository attributes; commit events get `vcs.ref.head.*` with `OTEL_LOG_TOOL_DETAILS`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.269
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-11-vscode-improved-documents-and-messages-written-for-someone-other-than-the-user-c|VSCode Improved documents and messages written for someone other than the user]] · Files and Data
- [[Changes/Claude Code/2026-09-11-5-apps-and-integrations-changes-in-v2-1-269|5 Apps and Integrations changes in v2.1.269]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-11-added-output-style-name-to-list-and-switch-output-styles-including-over-remote-c|Added /output-style name to list and switch output styles, including over Remote…]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-11-changed-skills-synced-from-claude-ai-in-cloud-sessions-to-be-named-anthropic-ski|Changed skills synced from claude.ai in cloud sessions to be named…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-11-3-interface-experience-changes-in-v2-1-269|3 Interface Experience changes in v2.1.269]] · Interface Experience
- [[Changes/Claude Code/2026-09-11-improved-responsiveness-in-long-sessions-transcript-updates-no-longer-re-process|Improved responsiveness in long sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-11-3-editor-experience-changes-in-v2-1-269|3 Editor Experience changes in v2.1.269]] · Editor Experience
- [[Changes/Claude Code/2026-09-11-added-claude-code-gateway-model-discovery-timeout-ms-to-extend-the-llm-gateway-v|Added CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS to extend the LLM gateway…]] · Model Support
- [[Changes/Claude Code/2026-09-11-2-agent-mode-changes-in-v2-1-269|2 Agent Mode changes in v2.1.269]] · Agent Mode
- [[Changes/Claude Code/2026-09-11-5-safety-and-privacy-changes-in-v2-1-269|5 Safety and Privacy changes in v2.1.269]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-11-11-other-changes-in-v2-1-269|11 other changes in v2.1.269]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-10 · Claude Code · [[Changes/Claude Code/2026-09-10-code-review-added-a-note-under-the-still-open-findings-list-in-follow-up-reviews|Code Review Added a note under the still-open findings list in follow-up reviews]]
- Later: 2026-09-15 · Claude Code · [[Changes/Claude Code/2026-09-15-3-developer-workflow-changes-in-v2-1-273|3 Developer Workflow changes in v2.1.273]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-11-7141cf&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-11-added-otel-metrics-include-repository-to-tag-opentelemetry-metrics-and-events-wi.md%0ACard%20ID%3A%20claude-code-2026-09-11-7141cf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.269%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->