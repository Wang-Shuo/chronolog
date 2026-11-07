---
card_id: openclaw-2026-10-10-fccfb1
date: '2026-10-10'
description: 'OpenClaw · 2026-10-10 · Automation and Scheduling: 10 changes in v2026.10.1
  — Fresh packaged Mac app setup can run OpenClaw through This Mac without installing…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change
    gain, with volume automation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2579
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3dcc994fe98de765374cd3bc699ec412852920c8c46485b2fbb3b4e5a7e1ead4
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-10-fccfb1
  comparison: ''
  date: '2026-10-10'
  description: 'OpenClaw — v2026.10.1: 10 Automation and Scheduling changes'
  evidence:
  - quote: Fresh packaged Mac app setup can run OpenClaw through This Mac without
      installing Node or a separate CLI. It stops with the app by default. Enable
      Keep OpenClaw running when the app is closed to keep channels and automations
      running in the background; a paused Gateway stays paused.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Admins can use the CI popup to schedule PR repair and comment response,
      merge when ready, or archiving independently. These agent jobs use model allowance,
      need a running Gateway and scheduler, and continue after browser close or restart
      under existing approvals and repository conditions. Turning one off stops future
      runs but cannot undo an accepted external action; changing the enabling user's
      role does not cancel it. Archiving can also clean the session's managed worktree.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Usage keeps each recurring run's recorded creator when the next run starts,
      though already-lost attribution cannot be recovered. The CLI index also makes
      the existing cron show and cron scratch commands easier to find, with usage
      in the cron reference .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: When you ask an agent to run an automation, short jobs can return their
      outcome directly. Longer jobs keep running with a run ID for follow-up. Jobs
      that need the calling conversation acknowledge promptly so its turn can finish,
      and their reports can arrive afterward.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Agents can explicitly report failed scheduled work with AUTOMATION_FAILED
      alone on the first line, including in a child's answer. History records the
      explanation as an error, and announcements omit the marker. One-time jobs treat
      these reports as permanent failures. Silent recurring jobs without an alert
      route stay enabled through them, with increasing delays up to hourly; runtime
      faults or interrupted saving can still disable those jobs. See failure notifications
      and scheduled payload guidance .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Tool activity names the tool that ran and shows whether it is still running,
      finished or has an unknown outcome. Activity also corrects time-range totals,
      screenshot strips and filters; assignment menus offer one searchable list of
      loaded people and agents, and Mention Inbox failures retry on schedule. Eligible
      Activity changes appear immediately from session events, but compact lists can
      still retain some previous-model details after a model change.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Mac desktop automation uses Peekaboo 4.7.0. If an exact-window menu action
      cannot be dispatched safely, actionOnly refuses it; use the supported actionFirst
      fallback.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Sharing controls, agent discovery and command lists recheck access after
      delays or reconnects. Session read access works for shared GitHub publication
      options and receipts, while automation hides private working notes after access
      or ownership changes.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Approval links show supplied payment, recipient, posting and automation
      details before you decide. Unrelated edits preserve pending approvals; relevant
      authority changes invalidate them. Commands suppressing audit output follow
      ordinary read/write approval policy, including eligible automatic review.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Common command errors explain how to correct or recover the request. Missing
      results remain unknown, so inspect current state before retrying an action with
      side effects. gateway call checks connection settings; use config validate for
      a full configuration check. See Gateway calls , command arguments and optional
      tool-loop detection .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 10-automation-and-scheduling-changes-in-v2026-10-1
  source_release: openclaw-2026-10-10-v2026-10-1-d64e4e93
  source_type: openclaw_changelog
  theme: automation-scheduling
  title: 10 Automation and Scheduling changes in v2026.10.1
  type: change
related_changes:
- '[[Changes/OpenHands/2026-10-08-2-automation-and-scheduling-changes-in-v1-26-0|2
  Automation and Scheduling changes in v1.26.0]]'
- '[[Changes/Replit/2026-10-09-create-and-manage-tiktok-ads|Create and manage TikTok
  Ads]]'
- '[[Changes/Open WebUI/2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0|10
  Automation and Scheduling changes in v0.12.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|openclaw-2026-10-10-v2026-10-1-d64e4e93]]'
source_type: openclaw_changelog
theme: automation-scheduling
title: 10 Automation and Scheduling changes in v2026.10.1
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Automation and Scheduling changes in v2026.10.1

**OpenClaw** · 2026-10-10 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.1) · from [[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fresh packaged Mac app setup can run OpenClaw through This Mac without installing Node or a separate CLI. It stops with the app by default. Enable Keep OpenClaw running when the app is closed to keep channels and automations running in the background; a paused Gateway stays paused.

> Admins can use the CI popup to schedule PR repair and comment response, merge when ready, or archiving independently. These agent jobs use model allowance, need a running Gateway and scheduler, and continue after browser close or restart under existing approvals and repository conditions. Turning one off stops future runs but cannot undo an accepted external action; changing the enabling user's role does not cancel it. Archiving can also clean the session's managed worktree.

> Usage keeps each recurring run's recorded creator when the next run starts, though already-lost attribution cannot be recovered. The CLI index also makes the existing cron show and cron scratch commands easier to find, with usage in the cron reference .

> When you ask an agent to run an automation, short jobs can return their outcome directly. Longer jobs keep running with a run ID for follow-up. Jobs that need the calling conversation acknowledge promptly so its turn can finish, and their reports can arrive afterward.

> Agents can explicitly report failed scheduled work with AUTOMATION_FAILED alone on the first line, including in a child's answer. History records the explanation as an error, and announcements omit the marker. One-time jobs treat these reports as permanent failures. Silent recurring jobs without an alert route stay enabled through them, with increasing delays up to hourly; runtime faults or interrupted saving can still disable those jobs. See failure notifications and scheduled payload guidance .

> Tool activity names the tool that ran and shows whether it is still running, finished or has an unknown outcome. Activity also corrects time-range totals, screenshot strips and filters; assignment menus offer one searchable list of loaded people and agents, and Mention Inbox failures retry on schedule. Eligible Activity changes appear immediately from session events, but compact lists can still retain some previous-model details after a model change.

> Mac desktop automation uses Peekaboo 4.7.0. If an exact-window menu action cannot be dispatched safely, actionOnly refuses it; use the supported actionFirst fallback.

> Sharing controls, agent discovery and command lists recheck access after delays or reconnects. Session read access works for shared GitHub publication options and receipts, while automation hides private working notes after access or ownership changes.

> Approval links show supplied payment, recipient, posting and automation details before you decide. Unrelated edits preserve pending approvals; relevant authority changes invalidate them. Commands suppressing audit output follow ordinary read/write approval policy, including eligible automatic review.

> Common command errors explain how to correct or recover the request. Missing results remain unknown, so inspect current state before retrying an action with side effects. gateway call checks connection settings; use config validate for a full configuration check. See Gateway calls , command arguments and optional tool-loop detection .

Source: https://docs.openclaw.ai/releases/2026.10.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-10-2-reliability-and-performance-changes-in-v2026-10-1|2 Reliability and Performance changes in v2026.10.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-10-10-13-memory-and-personalization-changes-in-v2026-10-1|13 Memory and Personalization changes in v2026.10.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-10-96-apps-and-integrations-changes-in-v2026-10-1|96 Apps and Integrations changes in v2026.10.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-10-15-mobile-and-desktop-changes-in-v2026-10-1|15 Mobile and Desktop changes in v2026.10.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-10-12-context-window-changes-in-v2026-10-1|12 Context Window changes in v2026.10.1]] · Context Window
- [[Changes/OpenClaw/2026-10-10-4-pricing-model-changes-in-v2026-10-1|4 Pricing Model changes in v2026.10.1]] · Pricing Model
- [[Changes/OpenClaw/2026-10-10-18-account-and-access-changes-in-v2026-10-1|18 Account and Access changes in v2026.10.1]] · Account and Access
- [[Changes/OpenClaw/2026-10-10-18-model-support-changes-in-v2026-10-1|18 Model Support changes in v2026.10.1]] · Model Support
- [[Changes/OpenClaw/2026-10-10-20-safety-and-privacy-changes-in-v2026-10-1|20 Safety and Privacy changes in v2026.10.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-10-3-search-and-browsing-changes-in-v2026-10-1|3 Search and Browsing changes in v2026.10.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-10-10-plugin-authors-can-await-session-history-extension-changes-and-replay-metadata-t|Plugin authors can await session history, extension changes and replay metadata]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-10-2-accessibility-and-localization-changes-in-v2026-10-1|2 Accessibility and Localization changes in v2026.10.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-10-10-image-generation-with-oauth-can-retry-using-a-supported-openai-chat-model-in-age|Image generation with OAuth can retry using a supported OpenAI chat model…]] · Image Generation
- [[Changes/OpenClaw/2026-10-10-10-editor-experience-changes-in-v2026-10-1|10 Editor Experience changes in v2026.10.1]] · Editor Experience
- [[Changes/OpenClaw/2026-10-10-2-files-and-data-changes-in-v2026-10-1|2 Files and Data changes in v2026.10.1]] · Files and Data
- [[Changes/OpenClaw/2026-10-10-8-voice-and-audio-changes-in-v2026-10-1|8 Voice and Audio changes in v2026.10.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-10-27-agent-mode-changes-in-v2026-10-1|27 Agent Mode changes in v2026.10.1]] · Agent Mode
- [[Changes/OpenClaw/2026-10-10-12-collaboration-changes-in-v2026-10-1|12 Collaboration changes in v2026.10.1]] · Collaboration
- [[Changes/OpenClaw/2026-10-10-video-previews-new-video-previews-can-download-media-before-play|Video previews: New video previews can download media before Play]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-10-11-developer-workflow-changes-in-v2026-10-1|11 Developer Workflow changes in v2026.10.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-10-5-enterprise-and-administration-changes-in-v2026-10-1|5 Enterprise and Administration changes in v2026.10.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-10-20-interface-experience-changes-in-v2026-10-1|20 Interface Experience changes in v2026.10.1]] · Interface Experience
- [[Changes/OpenClaw/2026-10-10-112-other-changes-in-v2026-10-1|112 other changes in v2026.10.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-10-10 · Open WebUI · [[Changes/Open WebUI/2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0|10 Automation and Scheduling changes in v0.12.0]]
- Later: 2026-10-12 · OpenClaw · [[Changes/OpenClaw/2026-10-12-manually-started-jobs-an-accepted-automation-can-keep-using-its-allowed-tools-af|Manually started jobs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change gain, with volume automation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-10-fccfb1&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-10-10-automation-and-scheduling-changes-in-v2026-10-1.md%0ACard%20ID%3A%20openclaw-2026-10-10-fccfb1%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->