---
card_id: claude-code-2026-10-05-51194c
date: '2026-10-05'
description: 'Claude Code · 2026-10-05 · Reliability and Performance: 2 changes in
  v2.1.290 — Improved responsiveness while resuming large sessions: timers, input
  and…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2877
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fcf91d3f8a2512e8f56539798dc3471959d8db97e514bcc8a21fcaedd83a709e
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
- '[[Changes/Claude Code/2026-10-01-3-reliability-and-performance-changes-in-v2-1-287|3
  Reliability and Performance changes in v2.1.287]]'
- '[[Changes/Runway/2026-10-02-agent-can-now-generate-with-seedance-2-5-draft-mode-creating-fast-480p-drafts-wi|Seedance
  2.5 Draft Mode in Agent]]'
- '[[Changes/Superwhisper/2026-10-02-faster-microphone-start-when-beginning-recording-across-all-input-devices|Faster
  microphone start when beginning recording across all input devices]]'
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

- Earlier: 2026-10-02 · Superwhisper · [[Changes/Superwhisper/2026-10-02-faster-microphone-start-when-beginning-recording-across-all-input-devices|Faster microphone start when beginning recording across all input devices]]
- Later: 2026-10-05 · Raycast · [[Changes/Raycast/2026-10-05-7-reliability-and-performance-changes-in-raycast-windows-2-6|7 Reliability and Performance changes in Raycast windows 2.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-05-51194c&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-05-2-reliability-and-performance-changes-in-v2-1-290.md%0ACard%20ID%3A%20claude-code-2026-10-05-51194c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.290%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->