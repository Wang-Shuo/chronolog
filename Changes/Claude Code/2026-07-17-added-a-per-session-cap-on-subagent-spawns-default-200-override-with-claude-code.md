---
card_id: claude-code-2026-07-17-967a66
date: '2026-07-17'
description: 'Claude Code · 2026-07-17 · Agent Mode: Added a per-session cap on subagent
  spawns (default 200, override with `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`) to stop…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Welcome
    to the first nightly release!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1107
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: bbd37d2654f2215dabd50a26edf107eb936b5d6bd5811828cc55c71a78a8df3f
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-17-967a66
  comparison: ''
  date: '2026-07-17'
  description: 'Claude Code — v2.1.212: Added a per-session cap on subagent spawns
    (default 200, override with `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`) to stop runaway
    delegation loops; `/clear` resets the budget'
  evidence:
  - quote: Added a per-session cap on subagent spawns (default 200, override with
      `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`) to stop runaway delegation loops; `/clear`
      resets the budget
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-a-per-session-cap-on-subagent-spawns-default-200-override-with-claude-code
  source_release: claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11
  source_type: github_releases
  theme: agent-mode
  title: Added a per-session cap on subagent spawns…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-14-added-claude-code-process-wrapper-agent-view-and-the-background-service-now-hono|Added
  CLAUDE_CODE_PROCESS_WRAPPER: agent view and the background service now honor…]]'
- '[[Changes/Claude Code/2026-07-15-improved-background-agent-result-reporting-claude-now-reports-the-status-of-stil|Improved
  background agent result reporting]]'
- '[[Changes/Claude Code/2026-07-15-added-forward-subagent-text-flag-and-claude-code-forward-subagent-text-environme|Added
  --forward-subagent-text flag and CLAUDE_CODE_FORWARD_SUBAGENT_TEXT…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11|claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11]]'
source_type: github_releases
theme: agent-mode
title: Added a per-session cap on subagent spawns…
type: change
---

<!-- chronolog:begin region="header" -->
# Added a per-session cap on subagent spawns…

**Claude Code** · 2026-07-17 · [[Themes/agent-mode|Agent Mode]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.212) · from [[Releases/Claude Code/claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11|v2.1.212]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added a per-session cap on subagent spawns (default 200, override with `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`) to stop runaway delegation loops; `/clear` resets the budget
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-17-mcp-tool-calls-running-longer-than-2-minutes-now-move-to-the-background-automati|MCP tool calls running longer than 2 minutes now move to the background…]] · Apps and Integrations
- [[Changes/Claude Code/2026-07-17-added-claude-auto-mode-reset-to-restore-the-default-auto-mode-configuration-with|Added claude auto-mode reset to restore the default auto-mode configuration…]] · Agent Mode
- [[Changes/Claude Code/2026-07-17-fork-now-copies-your-conversation-into-a-new-background-session-its-own-row-in-c|/fork now copies your conversation into a new background session…]] · Agent Mode
- [[Changes/Claude Code/2026-07-17-added-a-session-wide-limit-on-websearch-tool-calls-default-200-tunable-via-claud|Added a session-wide limit on WebSearch tool calls…]] · Search and Browsing
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-07-15 · Claude Code · [[Changes/Claude Code/2026-07-15-added-forward-subagent-text-flag-and-claude-code-forward-subagent-text-environme|Added --forward-subagent-text flag and CLAUDE_CODE_FORWARD_SUBAGENT_TEXT…]]
- Later: 2026-07-17 · Cursor · [[Changes/Cursor/2026-07-17-cursor-now-responds-with-a-plan-before-it-begins-so-you-can-jump-in-and-redirect|Cursor now responds with a plan before it begins, so you can jump in and redirect early]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Welcome to the first nightly release!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-17-967a66&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-17-added-a-per-session-cap-on-subagent-spawns-default-200-override-with-claude-code.md%0ACard%20ID%3A%20claude-code-2026-07-17-967a66%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.212%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->