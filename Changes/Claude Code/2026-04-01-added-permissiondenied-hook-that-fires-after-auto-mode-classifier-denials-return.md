---
card_id: claude-code-2026-04-01-e43a95
date: '2026-04-01'
description: 'Claude Code · 2026-04-01 · Agent Mode: Added `PermissionDenied` hook
  that fires after auto mode classifier denials — return `{retry: true}` to tell the
  model…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Welcome
    to the first nightly release!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1000
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: significant
machine_hash: a754c3871d921a0ff148b3a7b96340632cc9a21e168fd0be4def8532c4974e76
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-04-01-e43a95
  comparison: ''
  confidence: low
  date: '2026-04-01'
  description: 'Claude Code — v2.1.89: Added `PermissionDenied` hook that fires after
    auto mode classifier denials — return `{retry: true}` to tell the model it can
    retry'
  evidence:
  - quote: 'Added `PermissionDenied` hook that fires after auto mode classifier denials
      — return `{retry: true}` to tell the model it can retry'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
  extractor_version: fallback-v4
  impact: significant
  product: claude-code
  product_name: Claude Code
  slug: added-permissiondenied-hook-that-fires-after-auto-mode-classifier-denials-return
  source_release: claude-code-2026-04-01-v2-1-89-github-303967782-358023f0
  source_type: github_releases
  theme: agent-mode
  theme_matches:
  - matched_terms:
    - auto mode
    score: 60
    theme: agent-mode
  - matched_terms:
    - model
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: Added `PermissionDenied` hook that fires after auto mode classifier denials
  type: change
related_changes:
- '[[Changes/Cursor/2026-03-25-your-codebase-build-outputs-and-secrets-all-stay-on-internal-machines-running-in|Your
  codebase, build outputs, and secrets all stay on internal machines running…]]'
- '[[Changes/Cursor/2026-03-25-cursor-now-supports-self-hosted-cloud-agents-that-keep-your-code-and-tool-execut|Cursor
  now supports self-hosted cloud agents that keep your code and tool execution…]]'
- '[[Changes/Claude Code/2026-03-26-added-taskcreated-hook-that-fires-when-a-task-is-created-via-taskcreate|Added
  TaskCreated hook that fires when a task is created via TaskCreate]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|claude-code-2026-04-01-v2-1-89-github-303967782-358023f0]]'
source_type: github_releases
theme: agent-mode
title: Added PermissionDenied hook that fires after auto mode classifier denials
type: change
---

<!-- chronolog:begin region="header" -->
# Added `PermissionDenied` hook that fires after auto mode classifier denials

**Claude Code** · 2026-04-01 · [[Themes/agent-mode|Agent Mode]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.89) · from [[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|v2.1.89]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `PermissionDenied` hook that fires after auto mode classifier denials — return `{retry: true}` to tell the model it can retry
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-01-added-mcp-connection-nonblocking-true-for-p-mode-to-skip-the-mcp-connection-wait|Added MCP_CONNECTION_NONBLOCKING=true for -p mode to skip the MCP connection…]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-01-added-defer-permission-decision-to-pretooluse-hooks-headless-sessions-can-pause|Added "defer" permission decision to PreToolUse hooks]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-01-added-claude-code-no-flicker-1-environment-variable-to-opt-into-flicker-free-alt|Added CLAUDE_CODE_NO_FLICKER=1 environment variable to opt into flicker-free…]] · Interface Experience
- [[Changes/Claude Code/2026-04-01-added-named-subagents-to-mention-typeahead-suggestions|Added named subagents to @ mention typeahead suggestions]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-added-taskcreated-hook-that-fires-when-a-task-is-created-via-taskcreate|Added TaskCreated hook that fires when a task is created via TaskCreate]]
- Later: 2026-04-02 · Cursor · [[Changes/Cursor/2026-04-02-in-the-agents-window-you-can-use-design-mode-to-annotate-and-target-ui-elements|In the Agents Window, you can use Design Mode to annotate and target UI elements…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Welcome to the first nightly release!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-01-e43a95&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-01-added-permissiondenied-hook-that-fires-after-auto-mode-classifier-denials-return.md%0ACard%20ID%3A%20claude-code-2026-04-01-e43a95%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.89%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->