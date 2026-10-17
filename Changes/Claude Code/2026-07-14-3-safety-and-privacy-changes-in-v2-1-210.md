---
card_id: claude-code-2026-07-14-113a82
date: '2026-07-14'
description: 'Claude Code · 2026-07-14 · Safety and Privacy: 3 changes in v2.1.210
  — Added a startup warning for `Write(path)`, `NotebookEdit(path)`, and `Glob(path)`…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1185
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 64fbe60bac3ce1870254d83ced34577be32796026d266e9b3d249ac50154db2d
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-14-113a82
  comparison: ''
  date: '2026-07-14'
  description: 'Claude Code — v2.1.210: 3 Safety and Privacy changes'
  evidence:
  - quote: Added a startup warning for `Write(path)`, `NotebookEdit(path)`, and `Glob(path)`
      permission rules — use `Edit(path)` or `Read(path)` instead
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.210
  - quote: 'Improved auto mode: the permission classifier now defaults to Sonnet 5
      for external sessions, validated on the session''s first request and pinned
      for the session'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.210
  - quote: Screen reader mode now announces permission mode changes aloud when cycling
      modes with Shift+Tab
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.210
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-safety-and-privacy-changes-in-v2-1-210
  source_release: claude-code-2026-07-14-v2-1-210-github-354034085-7eba9ec7
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v2.1.210
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-08-background-task-notifications-now-explicitly-state-that-no-human-input-has-occur|Background
  task notifications now explicitly state that no human input has occurred…]]'
- '[[Changes/Claude Code/2026-07-10-fixed-permission-prompt-tool-pointing-at-an-mcp-server-crashing-with-mcp-tool-no|Fixed
  --permission-prompt-tool pointing at an MCP server crashing…]]'
- '[[Changes/Claude Code/2026-07-11-2-safety-and-privacy-changes-in-v2-1-207|2 Safety
  and Privacy changes in v2.1.207]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-14-v2-1-210-github-354034085-7eba9ec7|claude-code-2026-07-14-v2-1-210-github-354034085-7eba9ec7]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v2.1.210
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v2.1.210

**Claude Code** · 2026-07-14 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.210) · from [[Releases/Claude Code/claude-code-2026-07-14-v2-1-210-github-354034085-7eba9ec7|v2.1.210]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a startup warning for `Write(path)`, `NotebookEdit(path)`, and `Glob(path)` permission rules — use `Edit(path)` or `Read(path)` instead

> Improved auto mode: the permission classifier now defaults to Sonnet 5 for external sessions, validated on the session's first request and pinned for the session

> Screen reader mode now announces permission mode changes aloud when cycling modes with Shift+Tab

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.210
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-14-2-interface-experience-changes-in-v2-1-210|2 Interface Experience changes in v2.1.210]] · Interface Experience
- [[Changes/Claude Code/2026-07-14-improved-the-bash-powershell-tool-message-when-a-command-hits-its-timeout-and-is|Improved the Bash/PowerShell tool message when a command hits its timeout…]] · Model Support
- [[Changes/Claude Code/2026-07-14-memory-writes-that-leave-a-memory-md-index-over-its-read-limit-now-produce-an-ex|Memory writes that leave a MEMORY.md index over its read limit now produce…]] · Memory and Personalization
- [[Changes/Claude Code/2026-07-14-3-agent-mode-changes-in-v2-1-210|3 Agent Mode changes in v2.1.210]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-11 · Claude Code · [[Changes/Claude Code/2026-07-11-2-safety-and-privacy-changes-in-v2-1-207|2 Safety and Privacy changes in v2.1.207]]
- Later: 2026-07-14 · Claude Code · [[Changes/Claude Code/2026-07-14-fixed-multi-second-per-turn-slowdowns-in-sessions-with-many-permission-deny-ask|Fixed multi-second per-turn slowdowns in sessions with many permission deny/ask rules]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-14-113a82&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-14-3-safety-and-privacy-changes-in-v2-1-210.md%0ACard%20ID%3A%20claude-code-2026-07-14-113a82%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.210%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->