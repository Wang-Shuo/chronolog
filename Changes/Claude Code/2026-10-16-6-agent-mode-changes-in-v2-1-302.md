---
card_id: claude-code-2026-10-16-54d195
date: '2026-10-16'
description: 'Claude Code · 2026-10-16 · Agent Mode: 6 changes in v2.1.302 — Added
  `CLAUDE_CODE_AUTO_MODE_MODEL` to choose the model the client-side auto mode classifier…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1198
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d2a6e2525b879292c17ed10539523972d1857b1f76ca1d616ffd0405f681889d
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-16-54d195
  comparison: ''
  date: '2026-10-16'
  description: 'Claude Code — v2.1.302: 6 Agent Mode changes'
  evidence:
  - quote: Added `CLAUDE_CODE_AUTO_MODE_MODEL` to choose the model the client-side
      auto mode classifier uses; it does not change the model for server-side auto
      mode
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.302
  - quote: 'Improved auto mode with the server-side classifier: a conversation too
      long for the safety check is now compacted, instead of every checked tool call
      being denied'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.302
  - quote: 'Changed fork subagents (`subagent_type: "fork"`) to be on by default in
      `claude -p`, the Agent SDK, the desktop app and VS Code, as they already are
      in the terminal; `CLAUDE_CODE_FORK_SUBAGENT=0` turns them off, and `claude mcp
      serve` never offers them'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.302
  - quote: Changed the desktop app and VS Code to always run the main conversation's
      subagents in the background, as the terminal does, rather than let Claude choose;
      a subagent's own Agent calls in `claude -p`, the Agent SDK, the desktop app
      and VS Code now run in the foreground by default
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.302
  - quote: Changed the `← for agents` footer hint to hide 10 seconds after a session
      opens; the count of agents waiting on you still shows
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.302
  - quote: Changed prompt and agent hooks so that at most 12 of one event run at a
      time; the rest wait their turn
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.302
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-agent-mode-changes-in-v2-1-302
  source_release: claude-code-2026-10-16-v2-1-302-github-415177347-763faf43
  source_type: github_releases
  theme: agent-mode
  title: 6 Agent Mode changes in v2.1.302
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-14-5-agent-mode-changes-in-v2-1-299|5 Agent Mode
  changes in v2.1.299]]'
- '[[Changes/Claude Code/2026-10-14-3-agent-mode-changes-in-v2-1-300|3 Agent Mode
  changes in v2.1.300]]'
- '[[Changes/ChatGPT/2026-10-16-multiple-agents-that-can-work-on-different-parts-of-a-task-in-parallel-you-can-f|Multiple
  agents that can work on different parts of a task in parallel]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-16-v2-1-302-github-415177347-763faf43|claude-code-2026-10-16-v2-1-302-github-415177347-763faf43]]'
source_type: github_releases
theme: agent-mode
title: 6 Agent Mode changes in v2.1.302
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Agent Mode changes in v2.1.302

**Claude Code** · 2026-10-16 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.302) · from [[Releases/Claude Code/claude-code-2026-10-16-v2-1-302-github-415177347-763faf43|v2.1.302]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `CLAUDE_CODE_AUTO_MODE_MODEL` to choose the model the client-side auto mode classifier uses; it does not change the model for server-side auto mode

> Improved auto mode with the server-side classifier: a conversation too long for the safety check is now compacted, instead of every checked tool call being denied

> Changed fork subagents (`subagent_type: "fork"`) to be on by default in `claude -p`, the Agent SDK, the desktop app and VS Code, as they already are in the terminal; `CLAUDE_CODE_FORK_SUBAGENT=0` turns them off, and `claude mcp serve` never offers them

> Changed the desktop app and VS Code to always run the main conversation's subagents in the background, as the terminal does, rather than let Claude choose; a subagent's own Agent calls in `claude -p`, the Agent SDK, the desktop app and VS Code now run in the foreground by default

> Changed the `← for agents` footer hint to hide 10 seconds after a session opens; the count of agents waiting on you still shows

> Changed prompt and agent hooks so that at most 12 of one event run at a time; the rest wait their turn

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.302
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-16-2-safety-and-privacy-changes-in-v2-1-302|2 Safety and Privacy changes in v2.1.302]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-16-improved-the-message-when-a-background-session-reopened-from-another-folder-has|Improved the message when a background session reopened from another folder has no…]] · Model Support
- [[Changes/Claude Code/2026-10-16-2-context-window-changes-in-v2-1-302|2 Context Window changes in v2.1.302]] · Context Window
- [[Changes/Claude Code/2026-10-16-3-apps-and-integrations-changes-in-v2-1-302|3 Apps and Integrations changes in v2.1.302]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-16-added-a-notice-to-design-sync-and-design-login-that-standalone-claude-design-cla|Added a notice to /design-sync and /design-login that standalone Claude Design…]] · Account and Access
- [[Changes/Claude Code/2026-10-16-6-other-changes-in-v2-1-302|6 other changes in v2.1.302]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-16 · ChatGPT · [[Changes/ChatGPT/2026-10-16-multiple-agents-that-can-work-on-different-parts-of-a-task-in-parallel-you-can-f|Multiple agents that can work on different parts of a task in parallel]]
- Later: 2026-10-16 · Cursor · [[Changes/Cursor/2026-10-16-environments-api|Environments API]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-16-54d195&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-16-6-agent-mode-changes-in-v2-1-302.md%0ACard%20ID%3A%20claude-code-2026-10-16-54d195%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.302%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->