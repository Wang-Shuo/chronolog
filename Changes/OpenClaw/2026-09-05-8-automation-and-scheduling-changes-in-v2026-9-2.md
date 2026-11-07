---
card_id: openclaw-2026-09-05-96ba11
date: '2026-09-05'
description: 'OpenClaw · 2026-09-05 · Automation and Scheduling: 8 changes in v2026.9.2
  — The Mentions Inbox is temporary. Entries last up to seven days, can be removed…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change
    gain, with volume automation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2544
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e426289b4f3802cd16da167dad38bc268a833592c1bce5bdb486c8f2c8fa35ed
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-05-96ba11
  comparison: ''
  date: '2026-09-05'
  description: 'OpenClaw — v2026.9.2: 8 Automation and Scheduling changes'
  evidence:
  - quote: The Mentions Inbox is temporary. Entries last up to seven days, can be
      removed sooner by capacity limits, and clear when OpenClaw restarts or upgrades.
      Opening a mention leaves it in the list until you dismiss it. Optional Someone
      mentions me browser alerts default off and are best effort. The Inbox also keeps
      automation and model sign-in warnings current through busy periods, and an automation
      alert's arrow opens Automations.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: You can manage existing automations from authenticated admin chat, keep
      their saved schedules and permissions through edits and copies, and let a self-cleaning
      job finish its result after removing its own schedule. Background checks retain
      their conversation context, while delegated tasks gain more specific recovery
      and stop behavior so you can follow the work through an interruption.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: An administrator can now use Control UI chat to manage existing automations
      across the Gateway, including a reminder created in Telegram. You can ask your
      Claw to find it, inspect it, change it, run it or remove it, with the same administrative
      reach as the Automations page.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Editing an automation now keeps the timing and alert choices you saved,
      including fractional-second cooldowns and stagger windows. A 90-second interval
      stays visible as 90 seconds, while alert settings that follow global defaults
      remain inherited until you deliberately override them. Copies also retain tool
      restrictions, model fallbacks and context choices, with fresh authorization
      for the new job.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Job management also preserves newer run results and timing when scheduling
      is disabled, while cleanup can remove expired idle sessions without getting
      stuck behind a busy one. In experimental Claws, successful installation retries
      clear old scheduler errors, and unchanged jobs no longer look modified merely
      because a status response includes extra metadata.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: An eligible automation attached to a persistent session can refresh its
      pinned dashboard widgets without keeping the browser open. It needs an explicit
      scheduled tool policy allowing show_widget , and its calls must pin the result;
      displaying an inline widget or opening it on a device still requires the appropriate
      client. When you do open Automations, bursts of activity share refresh requests
      while current status and run history continue to appear.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: On macOS, authorized Peekaboo computer-control requests can scroll at a
      screen position or at the pointer without requiring modifier keys or hitting
      an incorrect stale-snapshot refusal. Background scrolling still needs a window
      and an element from its current observation, so a background request does not
      silently become a foreground scroll. The Mac integration also adopts Peekaboo
      4.3.0's native automation and Bridge repairs while retaining the existing computer-control
      settings and permissions.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Larger Swarm jobs in Code Mode now queue calls when the bridge is full,
      allowing accepted work to advance as space opens without manually splitting
      the job into batches. Stopping the run prevents its remaining queued calls from
      launching, and pauses within the same process preserve the original arguments.
      Result collection also preserves the text or structured format requested when
      each helper started, while agents sharing global sessions can use the same group
      name without sharing one another's concurrency allowance or retention schedule.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 8-automation-and-scheduling-changes-in-v2026-9-2
  source_release: openclaw-2026-09-05-v2026-9-2-377f6d77
  source_type: openclaw_changelog
  theme: automation-scheduling
  title: 8 Automation and Scheduling changes in v2026.9.2
  type: change
related_changes:
- '[[Changes/Devin/2026-09-02-scheduled-scans-in-automations|Scheduled Scans in Automations]]'
- '[[Changes/OpenClaw/2026-09-03-13-automation-and-scheduling-changes-in-v2026-9-1|13
  Automation and Scheduling changes in v2026.9.1]]'
- '[[Changes/Devin/2026-09-04-code-scan-no-op-runs-when-there-are-no-new-commits|Code
  Scan No-Op Runs When There Are No New Commits]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|openclaw-2026-09-05-v2026-9-2-377f6d77]]'
source_type: openclaw_changelog
theme: automation-scheduling
title: 8 Automation and Scheduling changes in v2026.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Automation and Scheduling changes in v2026.9.2

**OpenClaw** · 2026-09-05 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.2) · from [[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The Mentions Inbox is temporary. Entries last up to seven days, can be removed sooner by capacity limits, and clear when OpenClaw restarts or upgrades. Opening a mention leaves it in the list until you dismiss it. Optional Someone mentions me browser alerts default off and are best effort. The Inbox also keeps automation and model sign-in warnings current through busy periods, and an automation alert's arrow opens Automations.

> You can manage existing automations from authenticated admin chat, keep their saved schedules and permissions through edits and copies, and let a self-cleaning job finish its result after removing its own schedule. Background checks retain their conversation context, while delegated tasks gain more specific recovery and stop behavior so you can follow the work through an interruption.

> An administrator can now use Control UI chat to manage existing automations across the Gateway, including a reminder created in Telegram. You can ask your Claw to find it, inspect it, change it, run it or remove it, with the same administrative reach as the Automations page.

> Editing an automation now keeps the timing and alert choices you saved, including fractional-second cooldowns and stagger windows. A 90-second interval stays visible as 90 seconds, while alert settings that follow global defaults remain inherited until you deliberately override them. Copies also retain tool restrictions, model fallbacks and context choices, with fresh authorization for the new job.

> Job management also preserves newer run results and timing when scheduling is disabled, while cleanup can remove expired idle sessions without getting stuck behind a busy one. In experimental Claws, successful installation retries clear old scheduler errors, and unchanged jobs no longer look modified merely because a status response includes extra metadata.

> An eligible automation attached to a persistent session can refresh its pinned dashboard widgets without keeping the browser open. It needs an explicit scheduled tool policy allowing show_widget , and its calls must pin the result; displaying an inline widget or opening it on a device still requires the appropriate client. When you do open Automations, bursts of activity share refresh requests while current status and run history continue to appear.

> On macOS, authorized Peekaboo computer-control requests can scroll at a screen position or at the pointer without requiring modifier keys or hitting an incorrect stale-snapshot refusal. Background scrolling still needs a window and an element from its current observation, so a background request does not silently become a foreground scroll. The Mac integration also adopts Peekaboo 4.3.0's native automation and Bridge repairs while retaining the existing computer-control settings and permissions.

> Larger Swarm jobs in Code Mode now queue calls when the bridge is full, allowing accepted work to advance as space opens without manually splitting the job into batches. Stopping the run prevents its remaining queued calls from launching, and pauses within the same process preserve the original arguments. Result collection also preserves the text or structured format requested when each helper started, while agents sharing global sessions can use the same group name without sharing one another's concurrency allowance or retention schedule.

Source: https://docs.openclaw.ai/releases/2026.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-05-24-safety-and-privacy-changes-in-v2026-9-2|24 Safety and Privacy changes in v2026.9.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-05-3-pricing-model-changes-in-v2026-9-2|3 Pricing Model changes in v2026.9.2]] · Pricing Model
- [[Changes/OpenClaw/2026-09-05-8-editor-experience-changes-in-v2026-9-2|8 Editor Experience changes in v2026.9.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-05-progress-mode-can-stay-quiet-about-routine-tool-calls-while-keeping-the-updates|Progress mode can stay quiet about routine tool calls while keeping the updates…]] · Presentation Creation
- [[Changes/OpenClaw/2026-09-05-swarm-is-now-available-to-eligible-agents-without-a-separate-enablement-step-so|Swarm is now available to eligible agents without a separate enablement step…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-a-rejected-send-can-keep-its-original-attachments-and-retry-action-when-you-leav|A rejected send can keep its original attachments and Retry action when you leave…]] · Files and Data
- [[Changes/OpenClaw/2026-09-05-20-account-and-access-changes-in-v2026-9-2|20 Account and Access changes in v2026.9.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-05-17-model-support-changes-in-v2026-9-2|17 Model Support changes in v2026.9.2]] · Model Support
- [[Changes/OpenClaw/2026-09-05-16-developer-workflow-changes-in-v2026-9-2|16 Developer Workflow changes in v2026.9.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-21-memory-and-personalization-changes-in-v2026-9-2|21 Memory and Personalization changes in v2026.9.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-05-4-enterprise-and-administration-changes-in-v2026-9-2|4 Enterprise and Administration changes in v2026.9.2]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-05-if-background-image-video-or-music-generation-finishes-but-final-delivery-fails|If background image, video or music generation finishes but final delivery fails…]] · Music Generation
- [[Changes/OpenClaw/2026-09-05-34-agent-mode-changes-in-v2026-9-2|34 Agent Mode changes in v2026.9.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-35-apps-and-integrations-changes-in-v2026-9-2|35 Apps and Integrations changes in v2026.9.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-05-9-collaboration-changes-in-v2026-9-2|9 Collaboration changes in v2026.9.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-05-10-mobile-and-desktop-changes-in-v2026-9-2|10 Mobile and Desktop changes in v2026.9.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-05-15-context-window-changes-in-v2026-9-2|15 Context Window changes in v2026.9.2]] · Context Window
- [[Changes/OpenClaw/2026-09-05-4-search-and-browsing-changes-in-v2026-9-2|4 Search and Browsing changes in v2026.9.2]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-05-17-voice-and-audio-changes-in-v2026-9-2|17 Voice and Audio changes in v2026.9.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-05-21-interface-experience-changes-in-v2026-9-2|21 Interface Experience changes in v2026.9.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-05-3-reliability-and-performance-changes-in-v2026-9-2|3 Reliability and Performance changes in v2026.9.2]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-05-you-can-now-put-the-part-of-a-task-you-are-working-on-in-the-main-view-and-keep|Put the part of a task you are working on in the main view and keep the conversation…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-72-other-changes-in-v2026-9-2|72 other changes in v2026.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-09-04 · Devin · [[Changes/Devin/2026-09-04-code-scan-no-op-runs-when-there-are-no-new-commits|Code Scan No-Op Runs When There Are No New Commits]]
- Later: 2026-09-08 · OpenClaw · [[Changes/OpenClaw/2026-09-08-7-automation-and-scheduling-changes-in-v2026-9-3|7 Automation and Scheduling changes in v2026.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change gain, with volume automation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-05-96ba11&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-05-8-automation-and-scheduling-changes-in-v2026-9-2.md%0ACard%20ID%3A%20openclaw-2026-09-05-96ba11%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->