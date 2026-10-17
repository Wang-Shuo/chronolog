---
card_id: claude-code-2026-08-19-b3dc4b
date: '2026-08-19'
description: 'Claude Code · 2026-08-19 · Other changes: 3 changes in v2.1.236 — `/goal`:
  an idle session whose goal is parked behind long-running background work now checks…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a8b7c243a4915abec3dfdd7eb46eb4fb07692097a89b446dfbf55785f862ecf0
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-19-b3dc4b
  comparison: ''
  date: '2026-08-19'
  description: 'Claude Code — v2.1.236: 3 other changes'
  evidence:
  - quote: '`/goal`: an idle session whose goal is parked behind long-running background
      work now checks in automatically after 30 minutes (then 1h, 2h) instead of waiting
      for you to return'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.236
  - quote: '`SendMessage` now refuses further messages to a session up front once
      a rapid burst would exceed what that session''s inbox accepts, instead of reporting
      them sent while they were dropped'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.236
  - quote: Aligned the session title chip on the prompt border with the footer's right
      edge
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.236
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-other-changes-in-v2-1-236
  source_release: claude-code-2026-08-19-v2-1-236-github-373272539-bbbacf79
  source_type: github_releases
  theme: uncategorized
  title: 3 other changes in v2.1.236
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-08-19-v2-1-236-github-373272539-bbbacf79|claude-code-2026-08-19-v2-1-236-github-373272539-bbbacf79]]'
source_type: github_releases
theme: uncategorized
title: 3 other changes in v2.1.236
type: change
---

<!-- chronolog:begin region="header" -->
# 3 other changes in v2.1.236

**Claude Code** · 2026-08-19 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.236) · from [[Releases/Claude Code/claude-code-2026-08-19-v2-1-236-github-373272539-bbbacf79|v2.1.236]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `/goal`: an idle session whose goal is parked behind long-running background work now checks in automatically after 30 minutes (then 1h, 2h) instead of waiting for you to return

> `SendMessage` now refuses further messages to a session up front once a rapid burst would exceed what that session's inbox accepts, instead of reporting them sent while they were dropped

> Aligned the session title chip on the prompt border with the footer's right edge

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.236
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-19-improved-startup-performance-the-session-counter-is-now-written-in-the-backgroun|Improved startup performance: the session counter is now written in the background]] · Reliability and Performance
- [[Changes/Claude Code/2026-08-19-added-anthropic-default-model-environment-variable-sets-the-model-new-sessions-s|Added ANTHROPIC_DEFAULT_MODEL environment variable]] · Model Support
- [[Changes/Claude Code/2026-08-19-added-notify-when-idle-to-cross-session-sendmessage-ask-another-claude-code-sess|Added notify_when_idle to cross-session SendMessage]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-19-2-safety-and-privacy-changes-in-v2-1-236|2 Safety and Privacy changes in v2.1.236]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-19-2-developer-workflow-changes-in-v2-1-236|2 Developer Workflow changes in v2.1.236]] · Developer Workflow
- [[Changes/Claude Code/2026-08-19-changed-the-model-picker-to-highlight-only-the-newest-model-s-name-so-the-highli|Changed the /model picker to highlight only the newest model's name…]] · Interface Experience
- [[Changes/Claude Code/2026-08-19-4-agent-mode-changes-in-v2-1-236|4 Agent Mode changes in v2.1.236]] · Agent Mode
- [[Changes/Claude Code/2026-08-19-sigterm-in-print-sdk-mode-no-longer-records-an-interrupted-turn-or-synthetic-too|SIGTERM in print/SDK mode no longer records an interrupted turn or synthetic tool…]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-19-usage-now-shows-the-usage-credits-spend-row-for-team-and-enterprise-members-and|/usage now shows the usage-credits spend row for Team and Enterprise members…]] · Pricing Model
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-19-b3dc4b&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-19-3-other-changes-in-v2-1-236.md%0ACard%20ID%3A%20claude-code-2026-08-19-b3dc4b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.236%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->