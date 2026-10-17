---
card_id: claude-code-2026-07-11-1c4cf2
date: '2026-07-11'
description: 'Claude Code · 2026-07-11 · Safety and Privacy: 2 changes in v2.1.207
  — Fixed remote managed settings from a non-interactive run (`claude -p`, the SDK)
  being…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1182
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 66642bb61843204cbcab43b2fa7e1e5ac47cbdc9fab817d56f7daa651636f72c
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-11-1c4cf2
  comparison: ''
  date: '2026-07-11'
  description: 'Claude Code — v2.1.207: 2 Safety and Privacy changes'
  evidence:
  - quote: Fixed remote managed settings from a non-interactive run (`claude -p`,
      the SDK) being permanently recorded as consented without ever showing the security
      consent dialog
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.207
  - quote: Fixed compound commands with `cd` prompting for permission when the only
      output redirect was to `/dev/null`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.207
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-safety-and-privacy-changes-in-v2-1-207
  source_release: claude-code-2026-07-11-v2-1-207-github-352355755-d77b8e91
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in v2.1.207
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-07-added-a-grey-badge-to-the-footer-when-in-manual-permission-mode-making-the-activ|Added
  a grey ⏸ badge to the footer when in manual permission mode, making the active…]]'
- '[[Changes/Claude Code/2026-07-08-background-task-notifications-now-explicitly-state-that-no-human-input-has-occur|Background
  task notifications now explicitly state that no human input has occurred…]]'
- '[[Changes/Claude Code/2026-07-10-fixed-permission-prompt-tool-pointing-at-an-mcp-server-crashing-with-mcp-tool-no|Fixed
  --permission-prompt-tool pointing at an MCP server crashing…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-11-v2-1-207-github-352355755-d77b8e91|claude-code-2026-07-11-v2-1-207-github-352355755-d77b8e91]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in v2.1.207
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in v2.1.207

**Claude Code** · 2026-07-11 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.207) · from [[Releases/Claude Code/claude-code-2026-07-11-v2-1-207-github-352355755-d77b8e91|v2.1.207]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed remote managed settings from a non-interactive run (`claude -p`, the SDK) being permanently recorded as consented without ever showing the security consent dialog

> Fixed compound commands with `cd` prompting for permission when the only output redirect was to `/dev/null`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.207
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-11-improved-agent-view-pasting-the-same-text-again-now-expands-the-collapsed-pasted|Improved agent view]] · Interface Experience
- [[Changes/Claude Code/2026-07-11-2-agent-mode-changes-in-v2-1-207|2 Agent Mode changes in v2.1.207]] · Agent Mode
- [[Changes/Claude Code/2026-07-11-auto-mode-is-now-available-without-claude-code-enable-auto-mode-opt-in-on-bedroc|Auto mode is now available without CLAUDE_CODE_ENABLE_AUTO_MODE opt-in on Bedrock…]] · Agent Mode
- [[Changes/Claude Code/2026-07-11-2-apps-and-integrations-changes-in-v2-1-207|2 Apps and Integrations changes in v2.1.207]] · Apps and Integrations
- [[Changes/Claude Code/2026-07-11-changed-bedrock-vertex-and-claude-platform-on-aws-to-default-to-claude-opus-4-8|Changed Bedrock, Vertex, and Claude Platform on AWS to default to Claude Opus 4.8]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-10 · Claude Code · [[Changes/Claude Code/2026-07-10-fixed-permission-prompt-tool-pointing-at-an-mcp-server-crashing-with-mcp-tool-no|Fixed --permission-prompt-tool pointing at an MCP server crashing…]]
- Later: 2026-07-14 · Claude Code · [[Changes/Claude Code/2026-07-14-3-safety-and-privacy-changes-in-v2-1-210|3 Safety and Privacy changes in v2.1.210]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-11-1c4cf2&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-11-2-safety-and-privacy-changes-in-v2-1-207.md%0ACard%20ID%3A%20claude-code-2026-07-11-1c4cf2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.207%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->