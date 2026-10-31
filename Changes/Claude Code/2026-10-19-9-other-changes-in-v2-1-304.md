---
card_id: claude-code-2026-10-19-bb7c0d
date: '2026-10-19'
description: 'Claude Code · 2026-10-19 · Other changes: 9 changes in v2.1.304 — Added
  `e.isReadOnly` to a mod''s `tool.check` event, set when the tool call is read-only'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c95b8df7474ce26bacd90b0a1d74b0401dbe4c131634c2a1569ae3f3c33d2104
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-19-bb7c0d
  comparison: ''
  date: '2026-10-19'
  description: 'Claude Code — v2.1.304: 9 other changes'
  evidence:
  - quote: Added `e.isReadOnly` to a mod's `tool.check` event, set when the tool call
      is read-only
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  - quote: Improved `/usage` to say when a rate limit on usage data ends instead of
      "try again in a moment"
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  - quote: Improved the lines shown when a mod written in the session loads, reloads
      or fails to load
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  - quote: 'Improved artifacts with several views: when you ask for links to them,
      Claude now writes out each view''s link and explains that the address bar stays
      the same as you switch views'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  - quote: Improved how a remote session recovers its status when the server refuses
      a status update that carried other session data
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  - quote: 'Improved the `claude -p` invalid-settings warning: a file that did not
      load lists only what stopped it, and long lists are capped per file'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  - quote: 'Changed the `/artifacts` delete confirmation to show numbered choices:
      1 or Enter keeps the artifact, 2 deletes it, and y, n and Esc still work'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  - quote: Changed the question that turns on the mods Claude writes in a session
      to plain text with no link or session id; it stays up when a new turn starts,
      and Claude tells you what loaded when you turn them on
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  - quote: Changed tool search to be on by default behind a custom `ANTHROPIC_BASE_URL`;
      a 400 or 422 from the gateway is retried without it
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 9-other-changes-in-v2-1-304
  source_release: claude-code-2026-10-19-v2-1-304-github-417677344-46c4d994
  source_type: github_releases
  theme: uncategorized
  title: 9 other changes in v2.1.304
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-10-19-v2-1-304-github-417677344-46c4d994|claude-code-2026-10-19-v2-1-304-github-417677344-46c4d994]]'
source_type: github_releases
theme: uncategorized
title: 9 other changes in v2.1.304
type: change
---

<!-- chronolog:begin region="header" -->
# 9 other changes in v2.1.304

**Claude Code** · 2026-10-19 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.304) · from [[Releases/Claude Code/claude-code-2026-10-19-v2-1-304-github-417677344-46c4d994|v2.1.304]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `e.isReadOnly` to a mod's `tool.check` event, set when the tool call is read-only

> Improved `/usage` to say when a rate limit on usage data ends instead of "try again in a moment"

> Improved the lines shown when a mod written in the session loads, reloads or fails to load

> Improved artifacts with several views: when you ask for links to them, Claude now writes out each view's link and explains that the address bar stays the same as you switch views

> Improved how a remote session recovers its status when the server refuses a status update that carried other session data

> Improved the `claude -p` invalid-settings warning: a file that did not load lists only what stopped it, and long lists are capped per file

> Changed the `/artifacts` delete confirmation to show numbered choices: 1 or Enter keeps the artifact, 2 deletes it, and y, n and Esc still work

> Changed the question that turns on the mods Claude writes in a session to plain text with no link or session id; it stays up when a new turn starts, and Claude tells you what loaded when you turn them on

> Changed tool search to be on by default behind a custom `ANTHROPIC_BASE_URL`; a 400 or 422 from the gateway is retried without it

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-19-added-a-warning-on-pro-and-max-plans-when-resuming-an-inactive-conversation-woul|Added a warning on Pro and Max plans when resuming an inactive conversation would…]] · Collaboration
- [[Changes/Claude Code/2026-10-19-windows-improved-git-command-start-up-with-a-standard-git-for-windows-install-by|Windows: Improved git command start-up with a standard Git for Windows install…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-19-3-context-window-changes-in-v2-1-304|3 Context Window changes in v2.1.304]] · Context Window
- [[Changes/Claude Code/2026-10-19-8-apps-and-integrations-changes-in-v2-1-304|8 Apps and Integrations changes in v2.1.304]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-19-2-agent-mode-changes-in-v2-1-304|2 Agent Mode changes in v2.1.304]] · Agent Mode
- [[Changes/Claude Code/2026-10-19-3-developer-workflow-changes-in-v2-1-304|3 Developer Workflow changes in v2.1.304]] · Developer Workflow
- [[Changes/Claude Code/2026-10-19-added-decider-person-to-a-mod-s-tool-check-answer-only-the-permission-dialog-or|Added decider: "person" to a mod's tool.check answer: only the permission dialog…]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-19-added-claude-api-managed-agents-secure-which-compares-a-managed-agents-agent-s-s|Added /claude-api managed-agents-secure, which compares a Managed Agents agent's…]] · Agent Mode
- [[Changes/Claude Code/2026-10-19-2-model-support-changes-in-v2-1-304|2 Model Support changes in v2.1.304]] · Model Support
- [[Changes/Claude Code/2026-10-19-2-reliability-and-performance-changes-in-v2-1-304|2 Reliability and Performance changes in v2.1.304]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-19-bb7c0d&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-19-9-other-changes-in-v2-1-304.md%0ACard%20ID%3A%20claude-code-2026-10-19-bb7c0d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.304%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->