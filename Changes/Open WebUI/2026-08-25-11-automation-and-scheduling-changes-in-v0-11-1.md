---
card_id: open-webui-2026-08-25-49b908
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Automation and Scheduling: 11 changes in v0.11.1
  — \U0001F6A6 **Human in the loop tool approval.** Where an administrator has turned
  it on…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add
    data clean schedule]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 966
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1f2f2d2c1deb160d1afa723c1603f0c4d0ee032c7259db31fca2f8acf5d37dd8
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-49b908
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 11 Automation and Scheduling changes'
  evidence:
  - quote: "\U0001F6A6 **Human in the loop tool approval.** Where an administrator
      has turned it on, you can switch a conversation from letting tools run freely
      to being asked first, so a model that wants to use a tool stops and waits for
      you to allow or deny it, one call at a time in a saved conversation, by button
      or by keyboard shortcut, with your choice remembered for this conversation and
      for future ones, switching back to running freely releasing anything already
      waiting, and automations, channel replies, and temporary chats unaffected. [Commit](https://github.com/open-webui/open-webui/commit/7d99b2716a0472b2100b3a71825d8eb3fcbbe877),
      [Commit](https://github.com/open-webui/open-webui/commit/ec36972c2b5a8d48713f1a240b0ed305e535b4cc),
      [Commit](https://github.com/open-webui/open-webui/commit/653562d660398c32a9a193450bbbee300d7195c3),
      [Commit](https://github.com/open-webui/open-webui/commit/fa94a5ab2431edba064150651a14dd4992ef29e8),
      [Commit](https://github.com/open-webui/open-webui/commit/55c202e841e76cd69679206cd0ecb4a65b039ea4),
      [Commit](https://github.com/open-webui/open-webui/commit/30f82788bc75e6965da3766e3bf43840dd971eed),
      [Commit](https://github.com/open-webui/open-webui/commit/bbfdbd59f29e246db1d8b5c2401bc7b11aa32c99),
      [Commit](https://github.com/open-webui/open-webui/commit/7fc5fa1ff3f6cd6f0efcbf847064ca8d21620ba6),
      [Commit](https://github.com/open-webui/open-webui/commit/3eb65f47151af4fb4ccfaf33d6e77154546e7259),
      [Commit](https://github.com/open-webui/open-webui/commit/62fc436999ad32e82d1405ac14d1f03e0f0341ec)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4E2 **Automations that post to a channel.** An automation can now
      be pointed at a channel instead of a chat, so its scheduled run appears as a
      message there for everyone to see, chosen from a new destination picker that
      also covers folders. [Commit](https://github.com/open-webui/open-webui/commit/2649e3305c49cb37101c112ae10ffd8beacb5885)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4DF **Terminal availability and scope.** Administrators can now
      decide for each managed terminal whether it appears in chats and in automations
      at all, and whether everyone shares a single workspace or each chat or automation
      gets its own, with per chat terminals waiting until the conversation has been
      saved. [Commit](https://github.com/open-webui/open-webui/commit/009999f3636b1a3451f8fe55232e6ab132a64e66)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⌚ **Recurrence rules that could tie up the server.** How often an automation
      repeats is now taken from the rule the scheduler actually parsed rather than
      from the text of the rule, so a crafted rule can no longer disagree with what
      gets scheduled and walk the server through an unbounded run of occurrences,
      and a rule carrying a time zone on its start date now schedules instead of erroring.
      [Commit](https://github.com/open-webui/open-webui/commit/067114c28038b77045a3a1983e2e2719b1a32ad8)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⏰ **Listing automations through chat.** Asking a model to list your automations
      without naming a folder now returns every automation you have, instead of only
      the ones that sit outside a folder. [Commit](https://github.com/open-webui/open-webui/commit/f8ac75d188b7e07906aa1d5e648e3fc25a78ef2b)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F522 **Token counts for background chats.** Conversations started
      by automations, timers, sub-agents, and channels now report their token usage
      like any other chat, rather than arriving without it even when the model is
      set up to provide it. [#27661](https://github.com/open-webui/open-webui/pull/27661),
      [#27653](https://github.com/open-webui/open-webui/issues/27653)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⏲️ **Changing an automation through chat.** Asking a model to change one
      thing about an automation no longer moves it out of its folder or drops its
      model when the model fills those fields in blank instead of omitting them. [Commit](https://github.com/open-webui/open-webui/commit/90bb94abf9a8c6fbb87c72952295ae39d2ad98e5)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F502 **Automations that run a set number of times.** An automation
      asked to run a limited number of times is now rejected unless it says when to
      start counting from, rather than being accepted and then running indefinitely.
      [#27781](https://github.com/open-webui/open-webui/pull/27781), [#27780](https://github.com/open-webui/open-webui/issues/27780)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FAC0 **Scheduled work stopping without warning.** The routine that
      runs automations and calendar alerts can no longer be discarded while the application
      is running, which had silently stopped them firing with nothing reported, and
      it now stops cleanly on shutdown. [#28053](https://github.com/open-webui/open-webui/pull/28053),
      [#28052](https://github.com/open-webui/open-webui/issues/28052)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F521 **Searching for non-English tags and text.** Searching workspace
      models by tag, or prompts and automations by their contents, now finds entries
      containing characters outside the English alphabet, where roughly half were
      missed depending on which settings were in force when each one was saved. [#28399](https://github.com/open-webui/open-webui/pull/28399)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F51B **Enable or disable all automations only reaching the ones
      on screen.** Turning every automation on or off now covers every automation
      matching your current search and filter, where it only ever touched the ones
      loaded on the page you were looking at and left the rest running as they were.
      [Commit](https://github.com/open-webui/open-webui/commit/f4a0d3c9734d1662a3f78891f21934f2b82aed1e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 11-automation-and-scheduling-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: automation-scheduling
  title: 11 Automation and Scheduling changes in v0.11.1
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-08-25-free-go-plus-and-pro-users-can-share-scheduled-tasks-recipients-can-review-and-c|Share
  scheduled tasks]]'
- '[[Changes/ChatGPT/2026-08-25-free-users-can-create-up-to-three-active-scheduled-tasks-tasks-can-run-once-or-r|Scheduled
  tasks for Free users]]'
- '[[Changes/Dify/2026-08-25-feat-workflow-support-human-input-in-loop-and-iteration-by-laipz8200-in-https-gi|feat(workflow):
  support human input in loop and iteration]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: automation-scheduling
title: 11 Automation and Scheduling changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Automation and Scheduling changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🚦 **Human in the loop tool approval.** Where an administrator has turned it on, you can switch a conversation from letting tools run freely to being asked first, so a model that wants to use a tool stops and waits for you to allow or deny it, one call at a time in a saved conversation, by button or by keyboard shortcut, with your choice remembered for this conversation and for future ones, switching back to running freely releasing anything already waiting, and automations, channel replies, and temporary chats unaffected. [Commit](https://github.com/open-webui/open-webui/commit/7d99b2716a0472b2100b3a71825d8eb3fcbbe877), [Commit](https://github.com/open-webui/open-webui/commit/ec36972c2b5a8d48713f1a240b0ed305e535b4cc), [Commit](https://github.com/open-webui/open-webui/commit/653562d660398c32a9a193450bbbee300d7195c3), [Commit](https://github.com/open-webui/open-webui/commit/fa94a5ab2431edba064150651a14dd4992ef29e8), [Commit](https://github.com/open-webui/open-webui/commit/55c202e841e76cd69679206cd0ecb4a65b039ea4), [Commit](https://github.com/open-webui/open-webui/commit/30f82788bc75e6965da3766e3bf43840dd971eed), [Commit](https://github.com/open-webui/open-webui/commit/bbfdbd59f29e246db1d8b5c2401bc7b11aa32c99), [Commit](https://github.com/open-webui/open-webui/commit/7fc5fa1ff3f6cd6f0efcbf847064ca8d21620ba6), [Commit](https://github.com/open-webui/open-webui/commit/3eb65f47151af4fb4ccfaf33d6e77154546e7259), [Commit](https://github.com/open-webui/open-webui/commit/62fc436999ad32e82d1405ac14d1f03e0f0341ec)

> 📢 **Automations that post to a channel.** An automation can now be pointed at a channel instead of a chat, so its scheduled run appears as a message there for everyone to see, chosen from a new destination picker that also covers folders. [Commit](https://github.com/open-webui/open-webui/commit/2649e3305c49cb37101c112ae10ffd8beacb5885)

> 📟 **Terminal availability and scope.** Administrators can now decide for each managed terminal whether it appears in chats and in automations at all, and whether everyone shares a single workspace or each chat or automation gets its own, with per chat terminals waiting until the conversation has been saved. [Commit](https://github.com/open-webui/open-webui/commit/009999f3636b1a3451f8fe55232e6ab132a64e66)

> ⌚ **Recurrence rules that could tie up the server.** How often an automation repeats is now taken from the rule the scheduler actually parsed rather than from the text of the rule, so a crafted rule can no longer disagree with what gets scheduled and walk the server through an unbounded run of occurrences, and a rule carrying a time zone on its start date now schedules instead of erroring. [Commit](https://github.com/open-webui/open-webui/commit/067114c28038b77045a3a1983e2e2719b1a32ad8)

> ⏰ **Listing automations through chat.** Asking a model to list your automations without naming a folder now returns every automation you have, instead of only the ones that sit outside a folder. [Commit](https://github.com/open-webui/open-webui/commit/f8ac75d188b7e07906aa1d5e648e3fc25a78ef2b)

> 🔢 **Token counts for background chats.** Conversations started by automations, timers, sub-agents, and channels now report their token usage like any other chat, rather than arriving without it even when the model is set up to provide it. [#27661](https://github.com/open-webui/open-webui/pull/27661), [#27653](https://github.com/open-webui/open-webui/issues/27653)

> ⏲️ **Changing an automation through chat.** Asking a model to change one thing about an automation no longer moves it out of its folder or drops its model when the model fills those fields in blank instead of omitting them. [Commit](https://github.com/open-webui/open-webui/commit/90bb94abf9a8c6fbb87c72952295ae39d2ad98e5)

> 🔂 **Automations that run a set number of times.** An automation asked to run a limited number of times is now rejected unless it says when to start counting from, rather than being accepted and then running indefinitely. [#27781](https://github.com/open-webui/open-webui/pull/27781), [#27780](https://github.com/open-webui/open-webui/issues/27780)

> 🫀 **Scheduled work stopping without warning.** The routine that runs automations and calendar alerts can no longer be discarded while the application is running, which had silently stopped them firing with nothing reported, and it now stops cleanly on shutdown. [#28053](https://github.com/open-webui/open-webui/pull/28053), [#28052](https://github.com/open-webui/open-webui/issues/28052)

> 🔡 **Searching for non-English tags and text.** Searching workspace models by tag, or prompts and automations by their contents, now finds entries containing characters outside the English alphabet, where roughly half were missed depending on which settings were in force when each one was saved. [#28399](https://github.com/open-webui/open-webui/pull/28399)

> 🔛 **Enable or disable all automations only reaching the ones on screen.** Turning every automation on or off now covers every automation matching your current search and filter, where it only ever touched the ones loaded on the page you were looking at and left the rest running as they were. [Commit](https://github.com/open-webui/open-webui/commit/f4a0d3c9734d1662a3f78891f21934f2b82aed1e)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-08-25-9-files-and-data-changes-in-v0-11-1|9 Files and Data changes in v0.11.1]] · Files and Data
- [[Changes/Open WebUI/2026-08-25-image-generation-and-web-search-staying-switched-off-turning-either-off-now-take|🎨 Image generation and web search staying switched off. Turning either off now…]] · Image Generation
- [[Changes/Open WebUI/2026-08-25-7-safety-and-privacy-changes-in-v0-11-1|7 Safety and Privacy changes in v0.11.1]] · Safety and Privacy
- [[Changes/Open WebUI/2026-08-25-improved-ui-accessibility-a-closed-sidebar-is-no-longer-reachable-by-keyboard-or|♿ Improved UI accessibility. A closed sidebar is no longer reachable by keyboard…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-08-25-2-pricing-model-changes-in-v0-11-1|2 Pricing Model changes in v0.11.1]] · Pricing Model
- [[Changes/Open WebUI/2026-08-25-10-reliability-and-performance-changes-in-v0-11-1|10 Reliability and Performance changes in v0.11.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-08-25-6-collaboration-changes-in-v0-11-1|6 Collaboration changes in v0.11.1]] · Collaboration
- [[Changes/Open WebUI/2026-08-25-4-context-window-changes-in-v0-11-1|4 Context Window changes in v0.11.1]] · Context Window
- [[Changes/Open WebUI/2026-08-25-13-account-and-access-changes-in-v0-11-1|13 Account and Access changes in v0.11.1]] · Account and Access
- [[Changes/Open WebUI/2026-08-25-starting-up-on-windows-the-windows-start-script-now-creates-the-secret-key-it-ne|🪟 Starting up on Windows. The Windows start script now creates the secret key…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-08-25-2-multimodal-input-changes-in-v0-11-1|2 Multimodal Input changes in v0.11.1]] · Multimodal Input
- [[Changes/Open WebUI/2026-08-25-12-editor-experience-changes-in-v0-11-1|12 Editor Experience changes in v0.11.1]] · Editor Experience
- [[Changes/Open WebUI/2026-08-25-4-apps-and-integrations-changes-in-v0-11-1|4 Apps and Integrations changes in v0.11.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-08-25-73-developer-workflow-changes-in-v0-11-1|73 Developer Workflow changes in v0.11.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-08-25-8-memory-and-personalization-changes-in-v0-11-1|8 Memory and Personalization changes in v0.11.1]] · Memory and Personalization
- [[Changes/Open WebUI/2026-08-25-files-for-delegated-tasks-a-task-handed-to-a-sub-agent-can-now-carry-the-attachm|🤝 Files for delegated tasks. A task handed to a sub-agent can now carry…]] · Agent Mode
- [[Changes/Open WebUI/2026-08-25-4-enterprise-and-administration-changes-in-v0-11-1|4 Enterprise and Administration changes in v0.11.1]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-08-25-24-interface-experience-changes-in-v0-11-1|24 Interface Experience changes in v0.11.1]] · Interface Experience
- [[Changes/Open WebUI/2026-08-25-5-search-and-browsing-changes-in-v0-11-1|5 Search and Browsing changes in v0.11.1]] · Search and Browsing
- [[Changes/Open WebUI/2026-08-25-4-voice-and-audio-changes-in-v0-11-1|4 Voice and Audio changes in v0.11.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-08-25-56-model-support-changes-in-v0-11-1|56 Model Support changes in v0.11.1]] · Model Support
- [[Changes/Open WebUI/2026-08-25-39-other-changes-in-v0-11-1|39 other changes in v0.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-08-25 · Dify · [[Changes/Dify/2026-08-25-feat-workflow-support-human-input-in-loop-and-iteration-by-laipz8200-in-https-gi|feat(workflow): support human input in loop and iteration]]
- Later: 2026-08-26 · Codex CLI · [[Changes/Codex CLI/2026-08-26-40436-add-a-managed-gate-for-in-app-local-automation-copyberry|♯40436 Add a managed gate for in-app local automation @copyberry]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-01-02 · Dify · [[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add data clean schedule]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-49b908&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-11-automation-and-scheduling-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-49b908%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->