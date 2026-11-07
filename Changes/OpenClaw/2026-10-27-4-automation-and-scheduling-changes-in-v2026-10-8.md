---
card_id: openclaw-2026-10-27-436806
date: '2026-10-27'
description: 'OpenClaw · 2026-10-27 · Automation and Scheduling: 4 changes in v2026.10.8
  — Cron scripts can use the current plugin hooks on their next run after a plugin
  is…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change
    gain, with volume automation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2596
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e583d55530e4a84d0929794081f6c8a8df5a5086d38875c6cfd626be8e961214
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-27-436806
  comparison: ''
  date: '2026-10-27'
  description: 'OpenClaw — v2026.10.8: 4 Automation and Scheduling changes'
  evidence:
  - quote: Cron scripts can use the current plugin hooks on their next run after a
      plugin is replaced, without restarting the Gateway.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Background command completions now wait for the heartbeat that started
      them, preventing the completion from interrupting the heartbeat and repeatedly
      waking the same cron work.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Conversation history can load after switching providers when a retained
      Claude CLI binding and a forwarded cron message previously caused it to fail.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Session deletion, transcript archiving and retained cron history work through
      symlinked state directories with SQLite and PostgreSQL.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-automation-and-scheduling-changes-in-v2026-10-8
  source_release: openclaw-2026-10-27-v2026-10-8-9d674f40
  source_type: openclaw_changelog
  theme: automation-scheduling
  title: 4 Automation and Scheduling changes in v2026.10.8
  type: change
related_changes:
- '[[Changes/OpenHands/2026-10-23-2-automation-and-scheduling-changes-in-v1-33-0|2
  Automation and Scheduling changes in v1.33.0]]'
- '[[Changes/ChatGPT/2026-10-27-icloud-users-can-now-connect-mail-and-calendar-to-chatgpt-to-find-emails-catch-u|iCloud
  users can now connect Mail and Calendar to ChatGPT to find emails, catch up…]]'
- '[[Changes/Gemini CLI/2026-10-27-refactor-core-cli-emit-tool-call-groups-from-the-scheduler-and-drop-the-ui-looka|refactor(core,cli):
  emit tool call groups from the scheduler and drop the UI lookahead]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-27-v2026-10-8-9d674f40|openclaw-2026-10-27-v2026-10-8-9d674f40]]'
source_type: openclaw_changelog
theme: automation-scheduling
title: 4 Automation and Scheduling changes in v2026.10.8
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Automation and Scheduling changes in v2026.10.8

**OpenClaw** · 2026-10-27 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.8) · from [[Releases/OpenClaw/openclaw-2026-10-27-v2026-10-8-9d674f40|v2026.10.8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Cron scripts can use the current plugin hooks on their next run after a plugin is replaced, without restarting the Gateway.

> Background command completions now wait for the heartbeat that started them, preventing the completion from interrupting the heartbeat and repeatedly waking the same cron work.

> Conversation history can load after switching providers when a retained Claude CLI binding and a forwarded cron message previously caused it to fail.

> Session deletion, transcript archiving and retained cron history work through symlinked state directories with SQLite and PostgreSQL.

Source: https://docs.openclaw.ai/releases/2026.10.8
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-27-6-voice-and-audio-changes-in-v2026-10-8|6 Voice and Audio changes in v2026.10.8]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-27-6-model-support-changes-in-v2026-10-8|6 Model Support changes in v2026.10.8]] · Model Support
- [[Changes/OpenClaw/2026-10-27-2-developer-workflow-changes-in-v2026-10-8|2 Developer Workflow changes in v2026.10.8]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-27-on-linux-doctor-can-repair-a-managed-gateway-that-is-using-an-unsupported-node-v|On Linux, Doctor can repair a managed Gateway that is using an unsupported Node…]] · Interface Experience
- [[Changes/OpenClaw/2026-10-27-oversized-macos-camera-clips-and-screen-recordings-now-return-an-error-instead-o|Oversized macOS camera clips and screen recordings now return an error instead…]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-27-future-macos-updates-wait-for-the-serving-gateway-to-exit-and-release-its-databa|Future macOS updates wait for the serving Gateway to exit and release its databases…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-27-4-memory-and-personalization-changes-in-v2026-10-8|4 Memory and Personalization changes in v2026.10.8]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-27-5-account-and-access-changes-in-v2026-10-8|5 Account and Access changes in v2026.10.8]] · Account and Access
- [[Changes/OpenClaw/2026-10-27-2-safety-and-privacy-changes-in-v2026-10-8|2 Safety and Privacy changes in v2026.10.8]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-27-the-control-ui-now-reconnects-when-a-visible-tab-has-lost-contact-but-still-show|The Control UI now reconnects when a visible tab has lost contact but still shows…]] · Editor Experience
- [[Changes/OpenClaw/2026-10-27-7-agent-mode-changes-in-v2026-10-8|7 Agent Mode changes in v2026.10.8]] · Agent Mode
- [[Changes/OpenClaw/2026-10-27-9-apps-and-integrations-changes-in-v2026-10-8|9 Apps and Integrations changes in v2026.10.8]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-27-malformed-microsoft-teams-message-html-no-longer-causes-the-parsing-stalls-that|Malformed Microsoft Teams message HTML no longer causes the parsing stalls…]] · Collaboration
- [[Changes/OpenClaw/2026-10-27-32-other-changes-in-v2026-10-8|32 other changes in v2026.10.8]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-10-27 · Gemini CLI · [[Changes/Gemini CLI/2026-10-27-refactor-core-cli-emit-tool-call-groups-from-the-scheduler-and-drop-the-ui-looka|refactor(core,cli): emit tool call groups from the scheduler and drop the UI lookahead]]
- Later: 2026-10-27 · OpenHands · [[Changes/OpenHands/2026-10-27-6-automation-and-scheduling-changes-in-v1-34-0|6 Automation and Scheduling changes in v1.34.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change gain, with volume automation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-27-436806&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-27-4-automation-and-scheduling-changes-in-v2026-10-8.md%0ACard%20ID%3A%20openclaw-2026-10-27-436806%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.8%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->