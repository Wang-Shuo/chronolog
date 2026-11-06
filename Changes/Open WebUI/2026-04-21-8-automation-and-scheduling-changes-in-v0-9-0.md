---
card_id: open-webui-2026-04-21-8569c4
date: '2026-04-21'
description: "Open WebUI · 2026-04-21 · Automation and Scheduling: 8 changes in v0.9.0
  — \U0001F916 **Scheduled chat automations.** You can now schedule the AI to run
  tasks…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add
    data clean schedule]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 840
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5d453c9052f4bb6da3c5c851a205579c29ff3936bb9aa60908639360736d4cc7
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-8569c4
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.0: 8 Automation and Scheduling changes'
  evidence:
  - quote: "\U0001F916 **Scheduled chat automations.** You can now schedule the AI
      to run tasks automatically on a recurring basis: daily digests, periodic reports,
      anything you'd otherwise need to remember to ask for. Create and manage automations
      from the Automations page or directly in chat, with full run history and manual
      trigger controls. [#23303](https://github.com/open-webui/open-webui/pull/23303),
      [Commit](https://github.com/open-webui/open-webui/commit/5a2ff8b2e5b6f55a20f7ed491f818490eb535ea7),
      [Commit](https://github.com/open-webui/open-webui/commit/d30a0531d4add045c21a2368d6321a9b1906865f),
      [Commit](https://github.com/open-webui/open-webui/commit/bae5ff938ac88a3a647cc31ca8db1101015ae18b),
      [Commit](https://github.com/open-webui/open-webui/commit/588b81eedaacbfd7394b707ae1600d9fb729b809..674695918e5e3e1811314ce2a082c5bbb42d76b2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9F0 **Automation tools in chat.** Built-in chat tools can now create,
      update, list, pause, and delete scheduled automations directly in conversation
      when automation access is enabled. [Commit](https://github.com/open-webui/open-webui/commit/588b81eedaacbfd7394b707ae1600d9fb729b809..674695918e5e3e1811314ce2a082c5bbb42d76b2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: ⏱️ **Automation scheduling limits.** Administrators can now set "AUTOMATION_MAX_COUNT"
      and "AUTOMATION_MIN_INTERVAL" to limit how many automations each non-admin user
      can create and prevent overly frequent schedules that could overload the system.
      [Commit](https://github.com/open-webui/open-webui/commit/406251c2f358ffabce4d631c98c6f2c879feae5c)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5D3️ **Calendar workspace and event management.** Open WebUI now
      has a full Calendar workspace. Create and manage events, set up recurring schedules,
      get reminders via in-app toasts or browser notifications, and see your scheduled
      automations alongside your calendar. [#23880](https://github.com/open-webui/open-webui/pull/23880)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: ⚙️ **Scheduler reminder configuration.** Administrators can now configure
      calendar reminder processing with "SCHEDULER_POLL_INTERVAL" and "CALENDAR_ALERT_LOOKAHEAD_MINUTES",
      while existing "AUTOMATION_POLL_INTERVAL" setups continue to work as a legacy
      fallback. [Commit](https://github.com/open-webui/open-webui/commit/e5b5a174265d6710e986f6534ee7e3b2923233be)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F916 **Automation worker async DB handling.** Automation claiming
      and run recording now use async database sessions consistently, improving worker
      stability for scheduled automations. [Commit](https://github.com/open-webui/open-webui/commit/cb6e77be3ec6ce00dd1f5b9ce3a655e6f65bc5da)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F552 **Automation timezone scheduling.** Scheduled automations now
      calculate each user’s next run time using that user’s saved timezone, preventing
      run drift caused by server-time fallback. [Commit](https://github.com/open-webui/open-webui/commit/a4d62253df55c6307112eb76a6bfa29a7f538e21)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F504 **Automation terminal source.** Automations now use the terminal
      configured on the selected model instead of a separate per-automation terminal
      picker, keeping terminal behavior consistent between chat and scheduled runs.
      [Commit](https://github.com/open-webui/open-webui/commit/47d413ce7b2a006a8126f4a9055b13e5fcb33a1d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 8-automation-and-scheduling-changes-in-v0-9-0
  source_release: open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a
  source_type: github_releases
  theme: automation-scheduling
  title: 8 Automation and Scheduling changes in v0.9.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-13-proactive-is-now-an-alias-for-loop|/proactive
  is now an alias for /loop]]'
- '[[Changes/Claude Code/2026-04-15-resume-continue-now-resurrects-unexpired-scheduled-tasks|--resume/--continue
  now resurrects unexpired scheduled tasks]]'
- '[[Changes/Claude Code/2026-04-17-improved-loop-pressing-esc-now-cancels-pending-wakeups-and-wakeups-display-as-cl|Improved
  /loop: pressing Esc now cancels pending wakeups, and wakeups display…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a]]'
source_type: github_releases
theme: automation-scheduling
title: 8 Automation and Scheduling changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Automation and Scheduling changes in v0.9.0

**Open WebUI** · 2026-04-21 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.0) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🤖 **Scheduled chat automations.** You can now schedule the AI to run tasks automatically on a recurring basis: daily digests, periodic reports, anything you'd otherwise need to remember to ask for. Create and manage automations from the Automations page or directly in chat, with full run history and manual trigger controls. [#23303](https://github.com/open-webui/open-webui/pull/23303), [Commit](https://github.com/open-webui/open-webui/commit/5a2ff8b2e5b6f55a20f7ed491f818490eb535ea7), [Commit](https://github.com/open-webui/open-webui/commit/d30a0531d4add045c21a2368d6321a9b1906865f), [Commit](https://github.com/open-webui/open-webui/commit/bae5ff938ac88a3a647cc31ca8db1101015ae18b), [Commit](https://github.com/open-webui/open-webui/commit/588b81eedaacbfd7394b707ae1600d9fb729b809..674695918e5e3e1811314ce2a082c5bbb42d76b2)

> 🧰 **Automation tools in chat.** Built-in chat tools can now create, update, list, pause, and delete scheduled automations directly in conversation when automation access is enabled. [Commit](https://github.com/open-webui/open-webui/commit/588b81eedaacbfd7394b707ae1600d9fb729b809..674695918e5e3e1811314ce2a082c5bbb42d76b2)

> ⏱️ **Automation scheduling limits.** Administrators can now set "AUTOMATION_MAX_COUNT" and "AUTOMATION_MIN_INTERVAL" to limit how many automations each non-admin user can create and prevent overly frequent schedules that could overload the system. [Commit](https://github.com/open-webui/open-webui/commit/406251c2f358ffabce4d631c98c6f2c879feae5c)

> 🗓️ **Calendar workspace and event management.** Open WebUI now has a full Calendar workspace. Create and manage events, set up recurring schedules, get reminders via in-app toasts or browser notifications, and see your scheduled automations alongside your calendar. [#23880](https://github.com/open-webui/open-webui/pull/23880)

> ⚙️ **Scheduler reminder configuration.** Administrators can now configure calendar reminder processing with "SCHEDULER_POLL_INTERVAL" and "CALENDAR_ALERT_LOOKAHEAD_MINUTES", while existing "AUTOMATION_POLL_INTERVAL" setups continue to work as a legacy fallback. [Commit](https://github.com/open-webui/open-webui/commit/e5b5a174265d6710e986f6534ee7e3b2923233be)

> 🤖 **Automation worker async DB handling.** Automation claiming and run recording now use async database sessions consistently, improving worker stability for scheduled automations. [Commit](https://github.com/open-webui/open-webui/commit/cb6e77be3ec6ce00dd1f5b9ce3a655e6f65bc5da)

> 🕒 **Automation timezone scheduling.** Scheduled automations now calculate each user’s next run time using that user’s saved timezone, preventing run drift caused by server-time fallback. [Commit](https://github.com/open-webui/open-webui/commit/a4d62253df55c6307112eb76a6bfa29a7f538e21)

> 🔄 **Automation terminal source.** Automations now use the terminal configured on the selected model instead of a separate per-automation terminal picker, keeping terminal behavior consistent between chat and scheduled runs. [Commit](https://github.com/open-webui/open-webui/commit/47d413ce7b2a006a8126f4a9055b13e5fcb33a1d)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-21-3-files-and-data-changes-in-v0-9-0|3 Files and Data changes in v0.9.0]] · Files and Data
- [[Changes/Open WebUI/2026-04-21-4-image-generation-changes-in-v0-9-0|4 Image Generation changes in v0.9.0]] · Image Generation
- [[Changes/Open WebUI/2026-04-21-28-model-support-changes-in-v0-9-0|28 Model Support changes in v0.9.0]] · Model Support
- [[Changes/Open WebUI/2026-04-21-5-editor-experience-changes-in-v0-9-0|5 Editor Experience changes in v0.9.0]] · Editor Experience
- [[Changes/Open WebUI/2026-04-21-persistent-chat-payload-efficiency-persisted-chats-now-use-server-side-history-l|🚀 Persistent chat payload efficiency. Persisted chats now use server-side…]] · Multimodal Input
- [[Changes/Open WebUI/2026-04-21-8-context-window-changes-in-v0-9-0|8 Context Window changes in v0.9.0]] · Context Window
- [[Changes/Open WebUI/2026-04-21-24-reliability-and-performance-changes-in-v0-9-0|24 Reliability and Performance changes in v0.9.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-21-4-apps-and-integrations-changes-in-v0-9-0|4 Apps and Integrations changes in v0.9.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-21-46-developer-workflow-changes-in-v0-9-0|46 Developer Workflow changes in v0.9.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-04-21-7-memory-and-personalization-changes-in-v0-9-0|7 Memory and Personalization changes in v0.9.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-21-2-mobile-and-desktop-changes-in-v0-9-0|2 Mobile and Desktop changes in v0.9.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-04-21-17-interface-experience-changes-in-v0-9-0|17 Interface Experience changes in v0.9.0]] · Interface Experience
- [[Changes/Open WebUI/2026-04-21-11-safety-and-privacy-changes-in-v0-9-0|11 Safety and Privacy changes in v0.9.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-04-21-4-search-and-browsing-changes-in-v0-9-0|4 Search and Browsing changes in v0.9.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-04-21-shared-chat-access-controls-you-can-now-control-who-has-access-to-a-shared-chat|🔗 Shared chat access controls. You can now control who has access to a shared…]] · Collaboration
- [[Changes/Open WebUI/2026-04-21-4-voice-and-audio-changes-in-v0-9-0|4 Voice and Audio changes in v0.9.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-04-21-17-account-and-access-changes-in-v0-9-0|17 Account and Access changes in v0.9.0]] · Account and Access
- [[Changes/Open WebUI/2026-04-21-21-other-changes-in-v0-9-0|21 other changes in v0.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-04-17 · Claude Code · [[Changes/Claude Code/2026-04-17-improved-loop-pressing-esc-now-cancels-pending-wakeups-and-wakeups-display-as-cl|Improved /loop: pressing Esc now cancels pending wakeups, and wakeups display…]]
- Later: 2026-04-23 · Gemini CLI · [[Changes/Gemini CLI/2026-04-23-feat-cli-extract-quotacontext-and-resolve-infinite-render-loop-by-adib234-in-htt|feat(cli): extract QuotaContext and resolve infinite render loop]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-01-02 · Dify · [[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add data clean schedule]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-8569c4&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-8-automation-and-scheduling-changes-in-v0-9-0.md%0ACard%20ID%3A%20open-webui-2026-04-21-8569c4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->