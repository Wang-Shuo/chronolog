---
card_id: openclaw-2026-09-30-bac7d4
date: '2026-09-30'
description: 'OpenClaw · 2026-09-30 · Automation and Scheduling: 11 changes in v2026.9.7
  — Tasks and TaskFlow panels, commands, and APIs are removed. Use subagent controls…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change
    gain, with volume automation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2569
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cebf8bbb8eb44794053b0342855d61f7ec6ae3fff327954be3497ce0c4cc8a0a
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-30-bac7d4
  comparison: ''
  date: '2026-09-30'
  description: 'OpenClaw — v2026.9.7: 11 Automation and Scheduling changes'
  evidence:
  - quote: Tasks and TaskFlow panels, commands, and APIs are removed. Use subagent
      controls , ACP sessions, background processes, Cron history, or Lobster pipelines
      for their respective work. Conversation transcripts, Workboard, and generated-media
      completion remain available. Plugin authors must migrate from the removed Task
      interfaces ; subagent wait and cancel calls now use runId and runIds . TaskFlow
      Webhooks have no equivalent HTTP replacement.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Discord and Slack now accept messages from other bots when allowBots is
      omitted, including after an upgrade. Set allowBots to false to keep the previous
      behavior. Existing access and mention rules still apply, but bot conversations
      can still loop.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: If prompted, run openclaw doctor --fix to repair older Dreaming schedules
      before creating or updating them. The repair makes a backup and preserves custom
      jobs and the surviving schedule’s history. Entries it cannot safely repair remain
      with warnings.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: The sidebar now shows newest-created threads first and hides message previews,
      automation chats and system chats. Use View options beside Threads to bring
      them back or sort by recent activity.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Android's Pages menu lets you open and pin work pages such as Agents, Automations
      and Terminal. Settings is now on the footer gear, available even offline, and
      can no longer be pinned. Ordinary chats appear separately in Threads; find automation
      conversations under Threads → Automations and manage schedules on the Automations
      work page. Existing conversations and their saved pins are kept.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Automations gain clearer setup, run history, and delivery status, alongside
      fixes for interrupted and delegated work.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: The Automations editor catches invalid webhook addresses before saving
      and correctly saves the default timing window for hourly jobs. The schedule
      guide explains exact timing and staggered starts.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: If your scripts create system-event jobs, remove --timeout-seconds from
      those commands. Cron add and create now reject that previously ignored option.
      Agent and command jobs keep timeout support; script jobs use --script-timeout-seconds
      .
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Enabled automations attached to a Workboard can now run when linked workers
      finish, fixing cases where they had to wait for the next scheduled run. Disabled
      jobs stay off, and the normal schedule remains a fallback. Older hosts without
      this trigger support report that it is unavailable.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Gmail watches renew once after an overdue wake and avoid overlapping renewal
      attempts. Stopping or replacing a watcher also stops its unfinished renewal.
      The renewal schedule and mail forwarding behavior are unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Code Mode shows a purpose title for new executions, and its error reports
      distinguish a failed tool from a later JavaScript error. A failed script may
      already have sent a message or taken another action, so check before retrying.
      Optional loop detection also recognizes more repeated work and remains off by
      default.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 11-automation-and-scheduling-changes-in-v2026-9-7
  source_release: openclaw-2026-09-30-v2026-9-7-3d25d2bd
  source_type: openclaw_changelog
  theme: automation-scheduling
  title: 11 Automation and Scheduling changes in v2026.9.7
  type: change
related_changes:
- '[[Changes/OpenHands/2026-09-25-3-automation-and-scheduling-changes-in-v1-24-0|3
  Automation and Scheduling changes in v1.24.0]]'
- '[[Changes/Manus/2026-09-28-a-new-architecture-new-products-and-new-capabilities-manus-studio-with-video-edi|Introducing
  Manus 2.0]]'
- '[[Changes/ChatGPT/2026-09-29-site-owners-can-also-create-recurring-cloud-schedules-from-automations-these-upd|Site
  owners can also create recurring cloud schedules from Automations]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|openclaw-2026-09-30-v2026-9-7-3d25d2bd]]'
source_type: openclaw_changelog
theme: automation-scheduling
title: 11 Automation and Scheduling changes in v2026.9.7
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Automation and Scheduling changes in v2026.9.7

**OpenClaw** · 2026-09-30 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.7) · from [[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|v2026.9.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Tasks and TaskFlow panels, commands, and APIs are removed. Use subagent controls , ACP sessions, background processes, Cron history, or Lobster pipelines for their respective work. Conversation transcripts, Workboard, and generated-media completion remain available. Plugin authors must migrate from the removed Task interfaces ; subagent wait and cancel calls now use runId and runIds . TaskFlow Webhooks have no equivalent HTTP replacement.

> Discord and Slack now accept messages from other bots when allowBots is omitted, including after an upgrade. Set allowBots to false to keep the previous behavior. Existing access and mention rules still apply, but bot conversations can still loop.

> If prompted, run openclaw doctor --fix to repair older Dreaming schedules before creating or updating them. The repair makes a backup and preserves custom jobs and the surviving schedule’s history. Entries it cannot safely repair remain with warnings.

> The sidebar now shows newest-created threads first and hides message previews, automation chats and system chats. Use View options beside Threads to bring them back or sort by recent activity.

> Android's Pages menu lets you open and pin work pages such as Agents, Automations and Terminal. Settings is now on the footer gear, available even offline, and can no longer be pinned. Ordinary chats appear separately in Threads; find automation conversations under Threads → Automations and manage schedules on the Automations work page. Existing conversations and their saved pins are kept.

> Automations gain clearer setup, run history, and delivery status, alongside fixes for interrupted and delegated work.

> The Automations editor catches invalid webhook addresses before saving and correctly saves the default timing window for hourly jobs. The schedule guide explains exact timing and staggered starts.

> If your scripts create system-event jobs, remove --timeout-seconds from those commands. Cron add and create now reject that previously ignored option. Agent and command jobs keep timeout support; script jobs use --script-timeout-seconds .

> Enabled automations attached to a Workboard can now run when linked workers finish, fixing cases where they had to wait for the next scheduled run. Disabled jobs stay off, and the normal schedule remains a fallback. Older hosts without this trigger support report that it is unavailable.

> Gmail watches renew once after an overdue wake and avoid overlapping renewal attempts. Stopping or replacing a watcher also stops its unfinished renewal. The renewal schedule and mail forwarding behavior are unchanged.

> Code Mode shows a purpose title for new executions, and its error reports distinguish a failed tool from a later JavaScript error. A failed script may already have sent a message or taken another action, so check before retrying. Optional loop detection also recognizes more repeated work and remains off by default.

Source: https://docs.openclaw.ai/releases/2026.9.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-30-4-context-window-changes-in-v2026-9-7|4 Context Window changes in v2026.9.7]] · Context Window
- [[Changes/OpenClaw/2026-09-30-13-developer-workflow-changes-in-v2026-9-7|13 Developer Workflow changes in v2026.9.7]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-30-3-files-and-data-changes-in-v2026-9-7|3 Files and Data changes in v2026.9.7]] · Files and Data
- [[Changes/OpenClaw/2026-09-30-13-account-and-access-changes-in-v2026-9-7|13 Account and Access changes in v2026.9.7]] · Account and Access
- [[Changes/OpenClaw/2026-09-30-2-enterprise-and-administration-changes-in-v2026-9-7|2 Enterprise and Administration changes in v2026.9.7]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-30-15-memory-and-personalization-changes-in-v2026-9-7|15 Memory and Personalization changes in v2026.9.7]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-30-33-agent-mode-changes-in-v2026-9-7|33 Agent Mode changes in v2026.9.7]] · Agent Mode
- [[Changes/OpenClaw/2026-09-30-17-interface-experience-changes-in-v2026-9-7|17 Interface Experience changes in v2026.9.7]] · Interface Experience
- [[Changes/OpenClaw/2026-09-30-36-apps-and-integrations-changes-in-v2026-9-7|36 Apps and Integrations changes in v2026.9.7]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-30-2-video-generation-changes-in-v2026-9-7|2 Video Generation changes in v2026.9.7]] · Video Generation
- [[Changes/OpenClaw/2026-09-30-12-voice-and-audio-changes-in-v2026-9-7|12 Voice and Audio changes in v2026.9.7]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-30-21-safety-and-privacy-changes-in-v2026-9-7|21 Safety and Privacy changes in v2026.9.7]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-30-administrators-can-opt-into-heap-snapshots-to-investigate-memory-growth-a-snapsh|Administrators can opt into heap snapshots to investigate memory growth]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-30-14-mobile-and-desktop-changes-in-v2026-9-7|14 Mobile and Desktop changes in v2026.9.7]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-30-9-editor-experience-changes-in-v2026-9-7|9 Editor Experience changes in v2026.9.7]] · Editor Experience
- [[Changes/OpenClaw/2026-09-30-22-model-support-changes-in-v2026-9-7|22 Model Support changes in v2026.9.7]] · Model Support
- [[Changes/OpenClaw/2026-09-30-4-search-and-browsing-changes-in-v2026-9-7|4 Search and Browsing changes in v2026.9.7]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-30-3-pricing-model-changes-in-v2026-9-7|3 Pricing Model changes in v2026.9.7]] · Pricing Model
- [[Changes/OpenClaw/2026-09-30-10-collaboration-changes-in-v2026-9-7|10 Collaboration changes in v2026.9.7]] · Collaboration
- [[Changes/OpenClaw/2026-09-30-4-multimodal-input-changes-in-v2026-9-7|4 Multimodal Input changes in v2026.9.7]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-30-72-other-changes-in-v2026-9-7|72 other changes in v2026.9.7]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-09-29 · ChatGPT · [[Changes/ChatGPT/2026-09-29-site-owners-can-also-create-recurring-cloud-schedules-from-automations-these-upd|Site owners can also create recurring cloud schedules from Automations]]
- Later: 2026-10-05 · Claude Code · [[Changes/Claude Code/2026-10-05-changed-background-sessions-whose-scheduled-task-is-gone-they-now-move-to-comple|Changed background sessions whose scheduled task is gone]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change gain, with volume automation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-30-bac7d4&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-30-11-automation-and-scheduling-changes-in-v2026-9-7.md%0ACard%20ID%3A%20openclaw-2026-09-30-bac7d4%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->