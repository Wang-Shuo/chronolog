---
card_id: open-webui-2026-10-10-6618be
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Automation and Scheduling: 10 changes in v0.12.0
  — \U0001F916 **Automation and sub-agent access ends with the account's sessions.**
  Signing an…"
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
machine_hash: 34c77142cba9d7b680104eccd2a6eed51666cd594d58a135d6ce21fb3fcf436e
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-6618be
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 10 Automation and Scheduling changes'
  evidence:
  - quote: "\U0001F916 **Automation and sub-agent access ends with the account's sessions.**
      Signing an account out of every device, for example by changing its password,
      now also cuts off its running automations and sub-agents, whose access stayed
      valid for up to an hour. [Commit](https://github.com/open-webui/open-webui/commit/24e30d1cbdaab624dfe20f479f805e6791cf0226)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ⏰ **Automations on Windows with PostgreSQL.** Automations can be created,
      edited and run again on Windows servers using PostgreSQL, where 0.11.4 rejected
      every schedule with an error and the scheduler failed on each tick. [#30424](https://github.com/open-webui/open-webui/pull/30424),
      [#30400](https://github.com/open-webui/open-webui/issues/30400)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F916 **Automations keep their model's tools.** The first automation
      run after a restart now uses its model's tools, MCP servers, default features
      and filters, where it previously ran without them and a channel automation showed
      the model ID instead of its name. [#30379](https://github.com/open-webui/open-webui/pull/30379),
      [#27694](https://github.com/open-webui/open-webui/issues/27694)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F570️ **Last run after Run now.** Running an automation with Run
      now now updates its last run time on the automation page and in the Automations
      list right away, where they kept showing \"Last run Never\" or the last scheduled
      run. [#31583](https://github.com/open-webui/open-webui/pull/31583), [#31580](https://github.com/open-webui/open-webui/issues/31580)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F418 **Non-ASCII search on PostgreSQL.** Searching automations by
      a word from their prompt and filtering models or prompts by a tag now find non-ASCII
      words such as Chinese on PostgreSQL, where they found nothing. [#31423](https://github.com/open-webui/open-webui/pull/31423),
      [#31422](https://github.com/open-webui/open-webui/issues/31422)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F524 **Non-English text in searches and size limits.** With \"ENABLE_ORJSON\"
      off, non-English letters are now saved as written instead of as escape codes,
      so case-insensitive searches such as model tag filters and automation search
      find them, and user and chat variables in Cyrillic or Chinese are no longer
      refused as too large at about a sixth of the 100,000 character limit; text saved
      earlier keeps the escape codes until it is next edited. [#31615](https://github.com/open-webui/open-webui/pull/31615)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5D3️ **Scheduled Tasks calendar run counts.** An automation limited
      to a number of runs now shows only the runs still to come in the Scheduled Tasks
      calendar, and very frequent schedules no longer show up short or empty. [#31604](https://github.com/open-webui/open-webui/pull/31604),
      [#31600](https://github.com/open-webui/open-webui/issues/31600)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4F1 **No keyboard popping up from menus on phones.** Closing the
      Integrations menu or opening a dropdown in the automation dialog on a phone
      no longer brings up the on-screen keyboard. [#31657](https://github.com/open-webui/open-webui/pull/31657),
      [#31656](https://github.com/open-webui/open-webui/issues/31656)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F30D **Dates and times in your language.** Dates, times, relative
      times such as \"2 hours ago\" and automation schedules across analytics, evaluations,
      functions, users, chats, notes, files, search, channels and the calendar now
      follow the interface language, where many of them were always shown in English.
      \"DEFAULT_LOCALE\" is now the starting language for anyone who has not picked
      one, ahead of the browser language. [#32131](https://github.com/open-webui/open-webui/issues/32131),
      [Commit](https://github.com/open-webui/open-webui/commit/7d205a86dc80f72718857a4785854e4455cb28d5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4CF **Long menu labels in other languages.** Menus such as the
      Actions menu in Workspace Models, the + menu in the chat input and the menus
      in Automations, Archived Chats, Personalization and Feedbacks now widen to fit
      longer translated labels and keep them left aligned, where long labels wrapped
      over the next row or showed centered. [#32151](https://github.com/open-webui/open-webui/pull/32151),
      [#32150](https://github.com/open-webui/open-webui/issues/32150)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 10-automation-and-scheduling-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: automation-scheduling
  title: 10 Automation and Scheduling changes in v0.12.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-08-2-automation-and-scheduling-changes-in-v2026-9-9|2
  Automation and Scheduling changes in v2026.9.9]]'
- '[[Changes/OpenHands/2026-10-08-2-automation-and-scheduling-changes-in-v1-26-0|2
  Automation and Scheduling changes in v1.26.0]]'
- '[[Changes/Replit/2026-10-09-create-and-manage-tiktok-ads|Create and manage TikTok
  Ads]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: automation-scheduling
title: 10 Automation and Scheduling changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Automation and Scheduling changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🤖 **Automation and sub-agent access ends with the account's sessions.** Signing an account out of every device, for example by changing its password, now also cuts off its running automations and sub-agents, whose access stayed valid for up to an hour. [Commit](https://github.com/open-webui/open-webui/commit/24e30d1cbdaab624dfe20f479f805e6791cf0226)

> ⏰ **Automations on Windows with PostgreSQL.** Automations can be created, edited and run again on Windows servers using PostgreSQL, where 0.11.4 rejected every schedule with an error and the scheduler failed on each tick. [#30424](https://github.com/open-webui/open-webui/pull/30424), [#30400](https://github.com/open-webui/open-webui/issues/30400)

> 🤖 **Automations keep their model's tools.** The first automation run after a restart now uses its model's tools, MCP servers, default features and filters, where it previously ran without them and a channel automation showed the model ID instead of its name. [#30379](https://github.com/open-webui/open-webui/pull/30379), [#27694](https://github.com/open-webui/open-webui/issues/27694)

> 🕰️ **Last run after Run now.** Running an automation with Run now now updates its last run time on the automation page and in the Automations list right away, where they kept showing "Last run Never" or the last scheduled run. [#31583](https://github.com/open-webui/open-webui/pull/31583), [#31580](https://github.com/open-webui/open-webui/issues/31580)

> 🐘 **Non-ASCII search on PostgreSQL.** Searching automations by a word from their prompt and filtering models or prompts by a tag now find non-ASCII words such as Chinese on PostgreSQL, where they found nothing. [#31423](https://github.com/open-webui/open-webui/pull/31423), [#31422](https://github.com/open-webui/open-webui/issues/31422)

> 🔤 **Non-English text in searches and size limits.** With "ENABLE_ORJSON" off, non-English letters are now saved as written instead of as escape codes, so case-insensitive searches such as model tag filters and automation search find them, and user and chat variables in Cyrillic or Chinese are no longer refused as too large at about a sixth of the 100,000 character limit; text saved earlier keeps the escape codes until it is next edited. [#31615](https://github.com/open-webui/open-webui/pull/31615)

> 🗓️ **Scheduled Tasks calendar run counts.** An automation limited to a number of runs now shows only the runs still to come in the Scheduled Tasks calendar, and very frequent schedules no longer show up short or empty. [#31604](https://github.com/open-webui/open-webui/pull/31604), [#31600](https://github.com/open-webui/open-webui/issues/31600)

> 📱 **No keyboard popping up from menus on phones.** Closing the Integrations menu or opening a dropdown in the automation dialog on a phone no longer brings up the on-screen keyboard. [#31657](https://github.com/open-webui/open-webui/pull/31657), [#31656](https://github.com/open-webui/open-webui/issues/31656)

> 🌍 **Dates and times in your language.** Dates, times, relative times such as "2 hours ago" and automation schedules across analytics, evaluations, functions, users, chats, notes, files, search, channels and the calendar now follow the interface language, where many of them were always shown in English. "DEFAULT_LOCALE" is now the starting language for anyone who has not picked one, ahead of the browser language. [#32131](https://github.com/open-webui/open-webui/issues/32131), [Commit](https://github.com/open-webui/open-webui/commit/7d205a86dc80f72718857a4785854e4455cb28d5)

> 📏 **Long menu labels in other languages.** Menus such as the Actions menu in Workspace Models, the + menu in the chat input and the menus in Automations, Archived Chats, Personalization and Feedbacks now widen to fit longer translated labels and keep them left aligned, where long labels wrapped over the next row or showed centered. [#32151](https://github.com/open-webui/open-webui/pull/32151), [#32150](https://github.com/open-webui/open-webui/issues/32150)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-10-5-reliability-and-performance-changes-in-v0-12-0|5 Reliability and Performance changes in v0.12.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0|5 Enterprise and Administration changes in v0.12.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-10-27-developer-workflow-changes-in-v0-12-0|27 Developer Workflow changes in v0.12.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-10-5-image-generation-changes-in-v0-12-0|5 Image Generation changes in v0.12.0]] · Image Generation
- [[Changes/Open WebUI/2026-10-10-49-model-support-changes-in-v0-12-0|49 Model Support changes in v0.12.0]] · Model Support
- [[Changes/Open WebUI/2026-10-10-19-account-and-access-changes-in-v0-12-0|19 Account and Access changes in v0.12.0]] · Account and Access
- [[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile and Desktop changes in v0.12.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-10-10-6-files-and-data-changes-in-v0-12-0|6 Files and Data changes in v0.12.0]] · Files and Data
- [[Changes/Open WebUI/2026-10-10-13-collaboration-changes-in-v0-12-0|13 Collaboration changes in v0.12.0]] · Collaboration
- [[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2 Memory and Personalization changes in v0.12.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-10-5-context-window-changes-in-v0-12-0|5 Context Window changes in v0.12.0]] · Context Window
- [[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface Experience changes in v0.12.0]] · Interface Experience
- [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]] · Agent Mode
- [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-10-09 · Replit · [[Changes/Replit/2026-10-09-create-and-manage-tiktok-ads|Create and manage TikTok Ads]]
- Later: 2026-10-10 · OpenClaw · [[Changes/OpenClaw/2026-10-10-10-automation-and-scheduling-changes-in-v2026-10-1|10 Automation and Scheduling changes in v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change gain, with volume automation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-6618be&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-6618be%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->