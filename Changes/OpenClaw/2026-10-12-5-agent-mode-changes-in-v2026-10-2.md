---
card_id: openclaw-2026-10-12-d80567
date: '2026-10-12'
description: 'OpenClaw · 2026-10-12 · Agent Mode: 5 changes in v2026.10.2 — Typed
  stop commands. In a connected non-global chat, /stop clears queued follow-ups as
  well as…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1194
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 447a7c31195db914fea1e39f6e0461ee017b9a6d3acc5f8797adb321073c1463
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-12-d80567
  comparison: ''
  date: '2026-10-12'
  description: 'OpenClaw — v2026.10.2: 5 Agent Mode changes'
  evidence:
  - quote: 'Typed stop commands. In a connected non-global chat, /stop clears queued
      follow-ups as well as active work, so waiting messages do not immediately restart
      the agent. The Stop button and offline replay still stop only the particular
      run. See the chat cancellation guide . #167860 , thanks to @masatohoshino and
      @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  - quote: 'Replies during startup. Messages can wait for their own agent to finish
      starting, while agents already ready keep answering independently. #168826 ,
      thanks to @steipete , @xiaozishan and @obviyus .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  - quote: 'Messages between agents. Replayed messages retain the original sender
      label, including when one agent forwards another sender''s text, so the receiving
      agent keeps that context on later turns. #169130 , thanks to @RomneyDa .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  - quote: 'Helper answers. Helpers using ACP or the shared CLI fallback pass their
      complete new answers back to the main agent, including the end of long reports
      and the answer for the right task. Delayed older results also stop replacing
      newer accepted answers. See announcement guidance . #165800 , #166139 , thanks
      to @yetval , @steipete , @holgergruenhagen , @potterdigital , @Leli1024 , @zyz619963502zyz
      , @Yun-0000 and @michaeljgood71 .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  - quote: 'Replies after helper results. The main agent can keep working on a helper''s
      result without losing its final reply when the helper''s delivery deadline expires.
      Normal task time limits and Stop still apply; see handoff guidance . #164282
      , thanks to @Oldrich333 and @obviyus .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 5-agent-mode-changes-in-v2026-10-2
  source_release: openclaw-2026-10-12-v2026-10-2-9abf70fc
  source_type: openclaw_changelog
  theme: agent-mode
  title: 5 Agent Mode changes in v2026.10.2
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-10-12-elevenagents-545be2|ElevenAgents]]'
- '[[Changes/Google Antigravity/2026-10-12-you-can-now-attach-zip-archives-to-a-prompt-and-the-agent-unpacks-them-with-its|Attach
  .zip archives to a prompt, and the agent unpacks them with its tools]]'
- '[[Changes/Google Antigravity/2026-10-12-subagent-launches-now-show-as-a-one-line-row-with-a-live-status-icon-like-other|Subagent
  launches now show as a one-line row with a live status icon, like other…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-12-v2026-10-2-9abf70fc|openclaw-2026-10-12-v2026-10-2-9abf70fc]]'
source_type: openclaw_changelog
theme: agent-mode
title: 5 Agent Mode changes in v2026.10.2
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Agent Mode changes in v2026.10.2

**OpenClaw** · 2026-10-12 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.2) · from [[Releases/OpenClaw/openclaw-2026-10-12-v2026-10-2-9abf70fc|v2026.10.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Typed stop commands. In a connected non-global chat, /stop clears queued follow-ups as well as active work, so waiting messages do not immediately restart the agent. The Stop button and offline replay still stop only the particular run. See the chat cancellation guide . #167860 , thanks to @masatohoshino and @steipete .

> Replies during startup. Messages can wait for their own agent to finish starting, while agents already ready keep answering independently. #168826 , thanks to @steipete , @xiaozishan and @obviyus .

> Messages between agents. Replayed messages retain the original sender label, including when one agent forwards another sender's text, so the receiving agent keeps that context on later turns. #169130 , thanks to @RomneyDa .

> Helper answers. Helpers using ACP or the shared CLI fallback pass their complete new answers back to the main agent, including the end of long reports and the answer for the right task. Delayed older results also stop replacing newer accepted answers. See announcement guidance . #165800 , #166139 , thanks to @yetval , @steipete , @holgergruenhagen , @potterdigital , @Leli1024 , @zyz619963502zyz , @Yun-0000 and @michaeljgood71 .

> Replies after helper results. The main agent can keep working on a helper's result without losing its final reply when the helper's delivery deadline expires. Normal task time limits and Stop still apply; see handoff guidance . #164282 , thanks to @Oldrich333 and @obviyus .

Source: https://docs.openclaw.ai/releases/2026.10.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-12-5-apps-and-integrations-changes-in-v2026-10-2|5 Apps and Integrations changes in v2026.10.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-12-4-memory-and-personalization-changes-in-v2026-10-2|4 Memory and Personalization changes in v2026.10.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-12-older-session-history-doctor-can-continue-repairing-leftover-session-files-while|Older session history]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-12-2-pricing-model-changes-in-v2026-10-2|2 Pricing Model changes in v2026.10.2]] · Pricing Model
- [[Changes/OpenClaw/2026-10-12-9-model-support-changes-in-v2026-10-2|9 Model Support changes in v2026.10.2]] · Model Support
- [[Changes/OpenClaw/2026-10-12-4-context-window-changes-in-v2026-10-2|4 Context Window changes in v2026.10.2]] · Context Window
- [[Changes/OpenClaw/2026-10-12-dictation-holding-the-microphone-and-releasing-it-no-longer-stops-recording-prem|Dictation. Holding the microphone and releasing it no longer stops recording prematurely]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-12-managed-browser-tabs-at-the-shared-tab-limit-locally-managed-browser-cleanup-fav|Managed browser tabs]] · Editor Experience
- [[Changes/OpenClaw/2026-10-12-2-developer-workflow-changes-in-v2026-10-2|2 Developer Workflow changes in v2026.10.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-12-home-notifications-creating-many-chats-no-longer-fills-home-s-notification-queue|Home notifications]] · Collaboration
- [[Changes/OpenClaw/2026-10-12-manually-started-jobs-an-accepted-automation-can-keep-using-its-allowed-tools-af|Manually started jobs]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-12-2-mobile-and-desktop-changes-in-v2026-10-2|2 Mobile and Desktop changes in v2026.10.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-12-plugin-approval-waits-affected-plugin-tools-can-wait-for-your-approval-for-the-e|Plugin approval waits]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-12-summaries-before-completion-replies-when-a-long-conversation-needs-a-summary-ope|Summaries before completion replies]] · Interface Experience
- [[Changes/OpenClaw/2026-10-12-23-other-changes-in-v2026-10-2|23 other changes in v2026.10.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-12 · Google Antigravity · [[Changes/Google Antigravity/2026-10-12-subagent-launches-now-show-as-a-one-line-row-with-a-live-status-icon-like-other|Subagent launches now show as a one-line row with a live status icon, like other…]]
- Later: 2026-10-12 · OpenHands · [[Changes/OpenHands/2026-10-12-4-agent-mode-changes-in-v1-27-0|4 Agent Mode changes in v1.27.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-12-d80567&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-12-5-agent-mode-changes-in-v2026-10-2.md%0ACard%20ID%3A%20openclaw-2026-10-12-d80567%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->