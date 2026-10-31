---
card_id: claude-code-2026-07-01-d51817
date: '2026-07-01'
description: 'Claude Code · 2026-07-01 · Agent Mode: 5 changes in v2.1.198 — Subagents
  now run in the background by default, so Claude keeps working while they run and
  is…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1091
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9cc71454c4e6f4c80d7d59585b61dd18077e2c3ae7ad4c67f28f699b2826c700
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-01-d51817
  comparison: ''
  date: '2026-07-01'
  description: 'Claude Code — v2.1.198: 5 Agent Mode changes'
  evidence:
  - quote: Subagents now run in the background by default, so Claude keeps working
      while they run and is notified when they finish (previously a gradual rollout)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.198
  - quote: Added background agent notifications in `claude agents` — sessions that
      need input or finish now fire the `Notification` hook (`agent_needs_input` /
      `agent_completed`)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.198
  - quote: 'Improved focus mode: subagents launched in a turn now appear in its activity
      summary, and completed background notifications fold into a single count'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.198
  - quote: Subagents now treat messages from the agent that launched them as normal
      task direction; an agent's message is still never treated as the user's approval
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.198
  - quote: Removed the `/agents` wizard; ask Claude to create or manage subagents,
      or edit `.claude/agents/` directly
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.198
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-agent-mode-changes-in-v2-1-198
  source_release: claude-code-2026-07-01-v2-1-198-github-347599701-9cec0dab
  source_type: github_releases
  theme: agent-mode
  title: 5 Agent Mode changes in v2.1.198
  type: change
related_changes:
- '[[Changes/Cursor/2026-06-29-remote-control-3ec330|Remote Control]]'
- '[[Changes/Cursor/2026-06-29-live-activities-and-push-notifications|Live Activities
  and push notifications]]'
- '[[Changes/Cursor/2026-06-29-cursor-for-ios-is-now-available-in-public-beta-on-all-paid-plans-launch-and-mana|Cursor
  for iOS is now available in public beta on all paid plans]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-01-v2-1-198-github-347599701-9cec0dab|claude-code-2026-07-01-v2-1-198-github-347599701-9cec0dab]]'
source_type: github_releases
theme: agent-mode
title: 5 Agent Mode changes in v2.1.198
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Agent Mode changes in v2.1.198

**Claude Code** · 2026-07-01 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.198) · from [[Releases/Claude Code/claude-code-2026-07-01-v2-1-198-github-347599701-9cec0dab|v2.1.198]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Subagents now run in the background by default, so Claude keeps working while they run and is notified when they finish (previously a gradual rollout)

> Added background agent notifications in `claude agents` — sessions that need input or finish now fire the `Notification` hook (`agent_needs_input` / `agent_completed`)

> Improved focus mode: subagents launched in a turn now appear in its activity summary, and completed background notifications fold into a single count

> Subagents now treat messages from the agent that launched them as normal task direction; an agent's message is still never treated as the user's approval

> Removed the `/agents` wizard; ask Claude to create or manage subagents, or edit `.claude/agents/` directly

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.198
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-01-background-agents-launched-from-claude-agents-now-commit-push-and-open-a-draft-p|Background agents launched from claude agents now commit, push, and open a draft…]] · Developer Workflow
- [[Changes/Claude Code/2026-07-01-2-interface-experience-changes-in-v2-1-198|2 Interface Experience changes in v2.1.198]] · Interface Experience
- [[Changes/Claude Code/2026-07-01-login-now-opens-the-sign-in-dialog-from-the-claude-agents-view-instead-of-saying|/login now opens the sign-in dialog from the claude agents view instead…]] · Account and Access
- [[Changes/Claude Code/2026-07-01-claude-in-chrome-is-now-generally-available|Claude in Chrome is now generally available]] · Apps and Integrations
- [[Changes/Claude Code/2026-07-01-2-model-support-changes-in-v2-1-198|2 Model Support changes in v2.1.198]] · Model Support
- [[Changes/Claude Code/2026-07-01-added-dataviz-skill-for-chart-and-dashboard-design-guidance-with-a-runnable-colo|Added /dataviz skill for chart and dashboard design guidance with a runnable…]] · Apps and Integrations
- [[Changes/Claude Code/2026-07-01-subagents-and-context-compaction-now-inherit-the-session-s-extended-thinking-con|Subagents and context compaction now inherit the session's extended thinking…]] · Context Window
- [[Changes/Claude Code/2026-07-01-improved-syntax-highlighting-accuracy-in-code-blocks-diffs-and-file-previews-by|Improved syntax highlighting accuracy in code blocks, diffs, and file previews…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-06-29 · Cursor · [[Changes/Cursor/2026-06-29-cursor-for-ios-is-now-available-in-public-beta-on-all-paid-plans-launch-and-mana|Cursor for iOS is now available in public beta on all paid plans]]
- Later: 2026-07-06 · Claude Code · [[Changes/Claude Code/2026-07-06-3-agent-mode-changes-in-v2-1-202|3 Agent Mode changes in v2.1.202]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-01-d51817&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-01-5-agent-mode-changes-in-v2-1-198.md%0ACard%20ID%3A%20claude-code-2026-07-01-d51817%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.198%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->