---
card_id: claude-code-2026-10-05-51194c
date: '2026-10-05'
description: 'Claude Code · 2026-10-05 · Reliability and Performance: 2 changes in
  v2.1.290 — Improved responsiveness while resuming large sessions: timers, input
  and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1390
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bd11b10cc7eea33011789b8df38132e723ec233ba0b54b4a87ed124121aac61c
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-05-51194c
  comparison: ''
  date: '2026-10-05'
  description: 'Claude Code — v2.1.290: 2 Reliability and Performance changes'
  evidence:
  - quote: 'Improved responsiveness while resuming large sessions: timers, input and
      rendering keep running while the transcript loads'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: 'Changed background sessions waiting on a scheduled wakeup (`/loop`): they
      are now left running through updates and low memory, where being restarted or
      shut down could silently lose the wakeup'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-reliability-and-performance-changes-in-v2-1-290
  source_release: claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6
  source_type: github_releases
  theme: reliability-performance
  title: 2 Reliability and Performance changes in v2.1.290
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-28-improved-startup-time-and-memory-use-by-building-only-the-parts-of-the-settings|Improved
  startup time and memory use by building only the parts of the settings…]]'
- '[[Changes/Claude Code/2026-09-29-fixed-the-powershell-tool-s-permission-check-skipping-deny-and-ask-rules-and-cac|Fixed
  the PowerShell tool''s permission check skipping deny and ask rules…]]'
- '[[Changes/Claude Code/2026-10-01-3-reliability-and-performance-changes-in-v2-1-287|3
  Reliability and Performance changes in v2.1.287]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6]]'
source_type: github_releases
theme: reliability-performance
title: 2 Reliability and Performance changes in v2.1.290
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Reliability and Performance changes in v2.1.290

**Claude Code** · 2026-10-05 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.290) · from [[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|v2.1.290]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved responsiveness while resuming large sessions: timers, input and rendering keep running while the transcript loads

> Changed background sessions waiting on a scheduled wakeup (`/loop`): they are now left running through updates and low memory, where being restarted or shut down could silently lose the wakeup

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-url-to-set-up-the-managed-agents-pattern|Added /claude-api managed-agents-onboard url to set up the Managed Agents…]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-19-safety-and-privacy-changes-in-v2-1-290|19 Safety and Privacy changes in v2.1.290]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-quickstart-name-to-build-a-console-quick|Added /claude-api managed-agents-onboard quickstart-name to build a Console…]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-3-account-and-access-changes-in-v2-1-290|3 Account and Access changes in v2.1.290]] · Account and Access
- [[Changes/Claude Code/2026-10-05-vscode-added-a-screen-reader-announcement-message-queued-when-you-send-a-message|VSCode Added a screen reader announcement, "Message queued.", when you send…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-05-changed-the-interactive-session-s-websearch-budget-to-refill-over-time-100-calls|Changed the interactive session's WebSearch budget to refill over time (100 calls/hour]] · Search and Browsing
- [[Changes/Claude Code/2026-10-05-14-apps-and-integrations-changes-in-v2-1-290|14 Apps and Integrations changes in v2.1.290]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-05-4-agent-mode-changes-in-v2-1-290|4 Agent Mode changes in v2.1.290]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-2-model-support-changes-in-v2-1-290|2 Model Support changes in v2.1.290]] · Model Support
- [[Changes/Claude Code/2026-10-05-5-developer-workflow-changes-in-v2-1-290|5 Developer Workflow changes in v2.1.290]] · Developer Workflow
- [[Changes/Claude Code/2026-10-05-changed-background-sessions-whose-scheduled-task-is-gone-they-now-move-to-comple|Changed background sessions whose scheduled task is gone]] · Automation and Scheduling
- [[Changes/Claude Code/2026-10-05-18-other-changes-in-v2-1-290|18 other changes in v2.1.290]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-3-reliability-and-performance-changes-in-v2-1-287|3 Reliability and Performance changes in v2.1.287]]
- Later: 2026-10-06 · Claude Code · [[Changes/Claude Code/2026-10-06-improved-rendering-speed-of-long-bulleted-or-numbered-replies-they-stream-resize|Improved rendering speed of long bulleted or numbered replies]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-05-51194c&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-05-2-reliability-and-performance-changes-in-v2-1-290.md%0ACard%20ID%3A%20claude-code-2026-10-05-51194c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.290%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->