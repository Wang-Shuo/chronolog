---
card_id: claude-code-2026-04-01-789bcb
date: '2026-04-01'
description: 'Claude Code · 2026-04-01 · Safety and Privacy: Added `"defer"` permission
  decision to `PreToolUse` hooks — headless sessions can pause at a tool call and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1081
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: ef2fc6be75cd7b336e2bf2a67a54913313b4c189f9e963a2a44b606d6d022bec
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-01-789bcb
  comparison: ''
  date: '2026-04-01'
  description: 'Claude Code — v2.1.89: Added `"defer"` permission decision to `PreToolUse`
    hooks — headless sessions can pause at a tool call and resume with `-p --resume`
    to have the hook re-evaluate'
  evidence:
  - quote: Added `"defer"` permission decision to `PreToolUse` hooks — headless sessions
      can pause at a tool call and resume with `-p --resume` to have the hook re-evaluate
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-defer-permission-decision-to-pretooluse-hooks-headless-sessions-can-pause
  source_release: claude-code-2026-04-01-v2-1-89-github-303967782-358023f0
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Added `"defer"` permission decision to `PreToolUse` hooks
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-01-added-husky-to-protected-directories-acceptedits-mode|Added
  .husky to protected directories (acceptEdits mode)]]'
- '[[Changes/Claude Code/2026-04-01-fixed-ui-crash-when-malformed-tool-input-reached-the-permission-dialog|Fixed
  UI crash when malformed tool input reached the permission dialog]]'
- '[[Changes/Claude Code/2026-04-01-hardened-powershell-tool-permission-checks-fixed-trailing-background-job-bypass|Hardened
  PowerShell tool permission checks]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|claude-code-2026-04-01-v2-1-89-github-303967782-358023f0]]'
source_type: github_releases
superseded: true
theme: safety-privacy
title: Added "defer" permission decision to PreToolUse hooks
type: change
---

<!-- chronolog:begin region="header" -->
# Added `"defer"` permission decision to `PreToolUse` hooks

**Claude Code** · 2026-04-01 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.89) · from [[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|v2.1.89]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `"defer"` permission decision to `PreToolUse` hooks — headless sessions can pause at a tool call and resume with `-p --resume` to have the hook re-evaluate
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-01-added-mcp-connection-nonblocking-true-for-p-mode-to-skip-the-mcp-connection-wait|Added MCP_CONNECTION_NONBLOCKING=true for -p mode to skip the MCP connection…]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-01-added-claude-code-no-flicker-1-environment-variable-to-opt-into-flicker-free-alt|Added CLAUDE_CODE_NO_FLICKER=1 environment variable to opt into flicker-free…]] · Interface Experience
- [[Changes/Claude Code/2026-04-01-added-permissiondenied-hook-that-fires-after-auto-mode-classifier-denials-return|Added PermissionDenied hook that fires after auto mode classifier denials]] · Agent Mode
- [[Changes/Claude Code/2026-04-01-added-named-subagents-to-mention-typeahead-suggestions|Added named subagents to @ mention typeahead suggestions]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-01 · Claude Code · [[Changes/Claude Code/2026-04-01-hardened-powershell-tool-permission-checks-fixed-trailing-background-job-bypass|Hardened PowerShell tool permission checks]]
- Later: 2026-04-02 · Claude Code · [[Changes/Claude Code/2026-04-02-fixed-plan-mode-in-remote-sessions-losing-track-of-the-plan-file-after-a-contain|Fixed plan mode in remote sessions losing track of the plan file after a container…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-01-789bcb&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-01-added-defer-permission-decision-to-pretooluse-hooks-headless-sessions-can-pause.md%0ACard%20ID%3A%20claude-code-2026-04-01-789bcb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.89%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->