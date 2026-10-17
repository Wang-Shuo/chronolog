---
card_id: claude-code-2026-07-17-c5314d
date: '2026-07-17'
description: 'Claude Code · 2026-07-17 · Safety and Privacy: 3 changes in v2.1.212
  — Fixed plan mode auto-running file-modifying Bash commands (e.g. `touch`, `rm`)
  without a…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1188
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b4a0dd63cbb258e1434a2cec58d3c65ac032a14e474c08a026d793a9ea501eec
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-17-c5314d
  comparison: ''
  date: '2026-07-17'
  description: 'Claude Code — v2.1.212: 3 Safety and Privacy changes'
  evidence:
  - quote: Fixed plan mode auto-running file-modifying Bash commands (e.g. `touch`,
      `rm`) without a permission prompt or SDK `canUseTool` callback
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  - quote: Deprecated the Task tool's `mode` parameter (now ignored); subagents inherit
      the parent session's permission mode by default
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  - quote: 'Changed agent view / `claude agents --json`: sessions waiting on a sandbox,
      MCP-input, or managed-settings prompt now show as "Needs input" instead of "Working"'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-safety-and-privacy-changes-in-v2-1-212
  source_release: claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v2.1.212
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-14-3-safety-and-privacy-changes-in-v2-1-210|3 Safety
  and Privacy changes in v2.1.210]]'
- '[[Changes/Claude Code/2026-07-14-fixed-multi-second-per-turn-slowdowns-in-sessions-with-many-permission-deny-ask|Fixed
  multi-second per-turn slowdowns in sessions with many permission deny/ask rules]]'
- '[[Changes/Claude Code/2026-07-15-2-safety-and-privacy-changes-in-v2-1-211|2 Safety
  and Privacy changes in v2.1.211]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11|claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v2.1.212
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v2.1.212

**Claude Code** · 2026-07-17 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.212) · from [[Releases/Claude Code/claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11|v2.1.212]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed plan mode auto-running file-modifying Bash commands (e.g. `touch`, `rm`) without a permission prompt or SDK `canUseTool` callback

> Deprecated the Task tool's `mode` parameter (now ignored); subagents inherit the parent session's permission mode by default

> Changed agent view / `claude agents --json`: sessions waiting on a sandbox, MCP-input, or managed-settings prompt now show as "Needs input" instead of "Working"

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-17-7-agent-mode-changes-in-v2-1-212|7 Agent Mode changes in v2.1.212]] · Agent Mode
- [[Changes/Claude Code/2026-07-17-typing-resume-in-the-agent-view-now-opens-a-picker-of-past-sessions-including-se|Typing /resume in the agent view now opens a picker of past sessions]] · Interface Experience
- [[Changes/Claude Code/2026-07-17-updated-the-auth-status-panel-title-from-cloud-authentication-to-authentication|Updated the auth status panel title from "Cloud authentication" to "Authentication"]] · Account and Access
- [[Changes/Claude Code/2026-07-17-3-search-and-browsing-changes-in-v2-1-212|3 Search and Browsing changes in v2.1.212]] · Search and Browsing
- [[Changes/Claude Code/2026-07-17-2-apps-and-integrations-changes-in-v2-1-212|2 Apps and Integrations changes in v2.1.212]] · Apps and Integrations
- [[Changes/Claude Code/2026-07-17-3-model-support-changes-in-v2-1-212|3 Model Support changes in v2.1.212]] · Model Support
- [[Changes/Claude Code/2026-07-17-corrected-an-earlier-release-note-2-1-200-tmux-through-the-3-6-series-lacks-sync|Corrected an earlier release note (2.1.200)]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-15 · Claude Code · [[Changes/Claude Code/2026-07-15-2-safety-and-privacy-changes-in-v2-1-211|2 Safety and Privacy changes in v2.1.211]]
- Later: 2026-07-18 · Claude Code · [[Changes/Claude Code/2026-07-18-9-safety-and-privacy-changes-in-v2-1-214|9 Safety and Privacy changes in v2.1.214]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-17-c5314d&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-17-3-safety-and-privacy-changes-in-v2-1-212.md%0ACard%20ID%3A%20claude-code-2026-07-17-c5314d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.212%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->