---
card_id: cursor-2026-05-07-ec5b1b
date: '2026-05-07'
description: 'Cursor · 2026-05-07 · Reliability and Performance: Cursor can now execute
  on plans faster by multitasking across tasks instead of tackling them one at a time.'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1239
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: d00e069505353269badce3c130b7ed9beb9c43772a4bfa6610be127ab7df5eef
product: cursor
product_name: Cursor
record:
  card_id: cursor-2026-05-07-ec5b1b
  comparison: ''
  date: '2026-05-07'
  description: 'Cursor — PR Review, Build Plan in Parallel, and Split PRs: Cursor
    can now execute on plans faster by multitasking across tasks instead of tackling
    them one at a time.'
  evidence:
  - quote: Cursor can now execute on plans faster by multitasking across tasks instead
      of tackling them one at a time.
    source_release: https://cursor.com/changelog/05-07-26
  - quote: Click "Build in Parallel" to have it identify independent parts of your
      plan and run them simultaneously using async subagents. Cursor will keep dependent
      steps in order when needed.
    source_release: https://cursor.com/changelog/05-07-26
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: cursor
  product_name: Cursor
  slug: build-in-parallel-from-plans
  source_release: cursor-2026-05-07-3-3-https-cursor-com-changelog-05-07-26-9d8a16d3
  source_type: cursor_changelog
  theme: reliability-performance
  title: Build in parallel from plans
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-06-updated-the-tui-fullscreen-startup-banner-to-describe-additional-renderer-benefi|Updated
  the /tui fullscreen startup banner to describe additional renderer…]]'
- '[[Changes/Claude Code/2026-05-07-improved-memory-usage-by-releasing-warm-spare-background-workers-under-memory-pr|Improved
  memory usage by releasing warm-spare background workers under memory pressure]]'
- '[[Changes/Cursor/2026-05-07-pin-skills-as-quick-actions|Pin skills as quick actions]]'
source_release: '[[Releases/Cursor/cursor-2026-05-07-3-3-https-cursor-com-changelog-05-07-26-9d8a16d3|cursor-2026-05-07-3-3-https-cursor-com-changelog-05-07-26-9d8a16d3]]'
source_type: cursor_changelog
theme: reliability-performance
title: Build in parallel from plans
type: change
---

<!-- chronolog:begin region="header" -->
# Build in parallel from plans

**Cursor** · 2026-05-07 · [[Themes/reliability-performance|Reliability and Performance]] · Launch · [Official source](https://cursor.com/changelog/05-07-26) · from [[Releases/Cursor/cursor-2026-05-07-3-3-https-cursor-com-changelog-05-07-26-9d8a16d3|PR Review, Build Plan in Parallel, and Split PRs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Cursor can now execute on plans faster by multitasking across tasks instead of tackling them one at a time.
>
> Click "Build in Parallel" to have it identify independent parts of your plan and run them simultaneously using async subagents. Cursor will keep dependent steps in order when needed.
>
> Source: https://cursor.com/changelog/05-07-26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cursor/2026-05-07-pin-skills-as-quick-actions|Pin skills as quick actions]] · Reliability and Performance
- [[Changes/Cursor/2026-05-07-improved-prompt-input-undo-grouping-so-undo-redo-feels-more-natural-during-edits|Improved prompt input undo grouping, so undo/redo feels more natural during edits]] · Editor Experience
- [[Changes/Cursor/2026-05-07-made-mcp-connection-behavior-more-predictable-and-added-explicit-stale-token-cle|Made MCP connection behavior more predictable, and added explicit stale token…]] · Apps and Integrations
- [[Changes/Cursor/2026-05-07-added-the-ability-to-control-explore-subagent-behavior-from-settings-choose-a-sp|Added the ability to control Explore subagent behavior from settings]] · Agent Mode
- [[Changes/Cursor/2026-05-07-pr-review|PR review]] · Developer Workflow
- [[Changes/Cursor/2026-05-07-multitask-is-now-available-in-the-editor-for-running-async-subagents-to-parallel|/multitask is now available in the editor for running async subagents to parallelize…]] · Editor Experience
- [[Changes/Cursor/2026-05-07-this-release-introduces-a-new-pr-review-experience-faster-execution-on-plans-thr|Cursor introduces a new PR review experience, faster execution on plans through…]] · Developer Workflow
- [[Changes/Cursor/2026-05-07-added-support-for-general-model-names-for-subagent-configuration-i-e-set-model-o|Added support for general model names for subagent configuration (i.e., set model]] · Model Support
- [[Changes/Cursor/2026-05-07-improved-long-chat-handling-and-reduced-jumpiness-and-other-surprising-behaviors|Improved long-chat handling and reduced jumpiness and other surprising behaviors]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-05-07 · Claude Code · [[Changes/Claude Code/2026-05-07-improved-memory-usage-by-releasing-warm-spare-background-workers-under-memory-pr|Improved memory usage by releasing warm-spare background workers under memory pressure]]
- Later: 2026-05-11 · Claude Code · [[Changes/Claude Code/2026-05-11-added-scroll-speed-command-to-tune-mouse-wheel-scroll-speed-with-a-live-preview|Added /scroll-speed command to tune mouse wheel scroll speed with a live preview]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cursor-2026-05-07-ec5b1b&body=Card%3A%20Changes%2FCursor%2F2026-05-07-build-in-parallel-from-plans.md%0ACard%20ID%3A%20cursor-2026-05-07-ec5b1b%0ASource%3A%20https%3A%2F%2Fcursor.com%2Fchangelog%2F05-07-26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->