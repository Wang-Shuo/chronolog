---
card_id: claude-code-2026-10-05-f09fee
date: '2026-10-05'
description: 'Claude Code · 2026-10-05 · Agent Mode: 4 changes in v2.1.290 — Improved
  the Read tool''s message for binary files: it now points Claude to a skill or a
  shell…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1187
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 231fdb0625ef4cd57021dc23ed4de10a8014a6f3d8e383c5ae0b95856d8d4d97
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-05-f09fee
  comparison: ''
  date: '2026-10-05'
  description: 'Claude Code — v2.1.290: 4 Agent Mode changes'
  evidence:
  - quote: 'Improved the Read tool''s message for binary files: it now points Claude
      to a skill or a shell command that can read the format'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Changed an in-process teammate's `agent_id` in Agent results to its agent
      ID (its `name@team` address stays in `teammate_id`); TeammateIdle hooks no longer
      fire from its subagents or forks
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: Changed `/model`, `/effort` and `/rename` sent from `claude agents` to
      a busy background session to apply right away, without a confirmation, instead
      of when the turn ends
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: 'Changed the built-in `gh api` in cloud sessions: a host other than github.com
      set in `GH_HOST` or `GH_REPO` is now refused (use `--hostname` or a full URL),
      and stderr notes requests to other hosts'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-agent-mode-changes-in-v2-1-290
  source_release: claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6
  source_type: github_releases
  theme: agent-mode
  title: 4 Agent Mode changes in v2.1.290
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-02-4-agent-mode-changes-in-v2-1-288|4 Agent Mode
  changes in v2.1.288]]'
- '[[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-url-to-set-up-the-managed-agents-pattern|Added
  /claude-api managed-agents-onboard url to set up the Managed Agents…]]'
- '[[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-quickstart-name-to-build-a-console-quick|Added
  /claude-api managed-agents-onboard quickstart-name to build a Console…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6]]'
source_type: github_releases
theme: agent-mode
title: 4 Agent Mode changes in v2.1.290
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in v2.1.290

**Claude Code** · 2026-10-05 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.290) · from [[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|v2.1.290]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved the Read tool's message for binary files: it now points Claude to a skill or a shell command that can read the format

> Changed an in-process teammate's `agent_id` in Agent results to its agent ID (its `name@team` address stays in `teammate_id`); TeammateIdle hooks no longer fire from its subagents or forks

> Changed `/model`, `/effort` and `/rename` sent from `claude agents` to a busy background session to apply right away, without a confirmation, instead of when the turn ends

> Changed the built-in `gh api` in cloud sessions: a host other than github.com set in `GH_HOST` or `GH_REPO` is now refused (use `--hostname` or a full URL), and stderr notes requests to other hosts

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-05-changed-background-sessions-waiting-on-a-scheduled-wakeup-loop-they-are-now-left|Changed background sessions waiting on a scheduled wakeup (/loop)]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-url-to-set-up-the-managed-agents-pattern|Added /claude-api managed-agents-onboard url to set up the Managed Agents…]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-19-safety-and-privacy-changes-in-v2-1-290|19 Safety and Privacy changes in v2.1.290]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-quickstart-name-to-build-a-console-quick|Added /claude-api managed-agents-onboard quickstart-name to build a Console…]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-3-account-and-access-changes-in-v2-1-290|3 Account and Access changes in v2.1.290]] · Account and Access
- [[Changes/Claude Code/2026-10-05-vscode-added-a-screen-reader-announcement-message-queued-when-you-send-a-message|VSCode Added a screen reader announcement, "Message queued.", when you send…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-05-changed-the-interactive-session-s-websearch-budget-to-refill-over-time-100-calls|Changed the interactive session's WebSearch budget to refill over time (100 calls/hour]] · Search and Browsing
- [[Changes/Claude Code/2026-10-05-14-apps-and-integrations-changes-in-v2-1-290|14 Apps and Integrations changes in v2.1.290]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-05-2-model-support-changes-in-v2-1-290|2 Model Support changes in v2.1.290]] · Model Support
- [[Changes/Claude Code/2026-10-05-5-developer-workflow-changes-in-v2-1-290|5 Developer Workflow changes in v2.1.290]] · Developer Workflow
- [[Changes/Claude Code/2026-10-05-changed-background-sessions-whose-scheduled-task-is-gone-they-now-move-to-comple|Changed background sessions whose scheduled task is gone]] · Automation and Scheduling
- [[Changes/Claude Code/2026-10-05-improved-responsiveness-while-resuming-large-sessions-timers-input-and-rendering|Improved responsiveness while resuming large sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-05-18-other-changes-in-v2-1-290|18 other changes in v2.1.290]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-02 · Claude Code · [[Changes/Claude Code/2026-10-02-4-agent-mode-changes-in-v2-1-288|4 Agent Mode changes in v2.1.288]]
- Later: 2026-10-06 · Claude Code · [[Changes/Claude Code/2026-10-06-3-agent-mode-changes-in-v2-1-292|3 Agent Mode changes in v2.1.292]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-05-f09fee&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-05-4-agent-mode-changes-in-v2-1-290.md%0ACard%20ID%3A%20claude-code-2026-10-05-f09fee%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.290%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->