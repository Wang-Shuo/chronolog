---
card_id: claude-code-2026-09-02-bb25ae
date: '2026-09-02'
description: 'Claude Code · 2026-09-02 · Safety and Privacy: 4 changes in v2.1.259
  — Added `--permission-prompts none` for unattended headless hosts: anything that
  would…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1235
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ed0221405adc7c74037319c9ec7352eca37c5ff930518a533692f425ba2a5ba6
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-02-bb25ae
  comparison: ''
  date: '2026-09-02'
  description: 'Claude Code — v2.1.259: 4 Safety and Privacy changes'
  evidence:
  - quote: 'Added `--permission-prompts none` for unattended headless hosts: anything
      that would prompt is denied automatically while the active permission mode (including
      auto mode) keeps deciding'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.259
  - quote: Fixed concurrent sessions silently reverting each other's `~/.claude.json`
      changes — workspace trust no longer resets and MCP/project state is no longer
      lost when running many sessions at once
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.259
  - quote: Fixed the file edit permission dialog sometimes showing a changed line
      cut short with no indication
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.259
  - quote: Fixed remote and scheduled sessions doing nothing after a connector-tool
      permission prompt was approved while the session was paused
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.259
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-safety-and-privacy-changes-in-v2-1-259
  source_release: claude-code-2026-09-02-v2-1-259-github-381579834-0f335a0f
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in v2.1.259
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-28-6-safety-and-privacy-changes-in-v2-1-251|6 Safety
  and Privacy changes in v2.1.251]]'
- '[[Changes/Claude Code/2026-09-01-fixed-remote-and-scheduled-sessions-failing-with-user-messages-must-have-non-emp|Fixed
  remote and scheduled sessions failing…]]'
- '[[Changes/Claude Code/2026-09-01-10-safety-and-privacy-changes-in-v2-1-257|10 Safety
  and Privacy changes in v2.1.257]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-02-v2-1-259-github-381579834-0f335a0f|claude-code-2026-09-02-v2-1-259-github-381579834-0f335a0f]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in v2.1.259
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in v2.1.259

**Claude Code** · 2026-09-02 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.259) · from [[Releases/Claude Code/claude-code-2026-09-02-v2-1-259-github-381579834-0f335a0f|v2.1.259]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `--permission-prompts none` for unattended headless hosts: anything that would prompt is denied automatically while the active permission mode (including auto mode) keeps deciding

> Fixed concurrent sessions silently reverting each other's `~/.claude.json` changes — workspace trust no longer resets and MCP/project state is no longer lost when running many sessions at once

> Fixed the file edit permission dialog sometimes showing a changed line cut short with no indication

> Fixed remote and scheduled sessions doing nothing after a connector-tool permission prompt was approved while the session was paused

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.259
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-02-improved-terminal-resize-and-first-render-performance-for-long-responses-by-reus|Improved terminal resize and first-render performance for long responses by reusing…]] · Developer Workflow
- [[Changes/Claude Code/2026-09-02-vscode-added-an-active-quick-filter-and-a-status-filter-menu-needs-input-working|VSCode Added an Active quick filter and a status filter menu…]] · Interface Experience
- [[Changes/Claude Code/2026-09-02-5-apps-and-integrations-changes-in-v2-1-259|5 Apps and Integrations changes in v2.1.259]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-02-2-agent-mode-changes-in-v2-1-259|2 Agent Mode changes in v2.1.259]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-01 · Claude Code · [[Changes/Claude Code/2026-09-01-10-safety-and-privacy-changes-in-v2-1-257|10 Safety and Privacy changes in v2.1.257]]
- Later: 2026-09-03 · Claude Code · [[Changes/Claude Code/2026-09-03-7-safety-and-privacy-changes-in-v2-1-260|7 Safety and Privacy changes in v2.1.260]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-02-bb25ae&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-02-4-safety-and-privacy-changes-in-v2-1-259.md%0ACard%20ID%3A%20claude-code-2026-09-02-bb25ae%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.259%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->