---
card_id: open-webui-2026-08-25-6b109a
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Collaboration: 6 changes in v0.11.1 — \U0001F5C2️
  **Folder permissions when starting a chat.** Starting a conversation filed into
  a folder now…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create
    a team here: (source link)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2783
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e0dc97432101ecde91297216ada2b16e055a898f4ae03d284f8adcefde883919
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-6b109a
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 6 Collaboration changes'
  evidence:
  - quote: "\U0001F5C2️ **Folder permissions when starting a chat.** Starting a conversation
      filed into a folder now checks that you are allowed to write to that folder,
      a check the message sending path had been skipping, and every place a chat can
      be filed now treats ownership, shared access, and unknown folders the same way.
      [#28366](https://github.com/open-webui/open-webui/pull/28366)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FAAA **Authorship in shared chats.** A chat shared with you now
      shows the name and picture of whoever wrote it, in the message list and in the
      overview panel, rather than crediting the messages to you. [#28274](https://github.com/open-webui/open-webui/pull/28274),
      [#28273](https://github.com/open-webui/open-webui/issues/28273)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9D1\U0001F91D\U0001F9D1 **Owner avatars on shared chats.** The
      picture beside a chat someone shared with you now loads, and falls back to the
      default image if it cannot, rather than leaving a blank gap when the interface
      and the server are on different addresses. [#28272](https://github.com/open-webui/open-webui/pull/28272),
      [#28271](https://github.com/open-webui/open-webui/issues/28271)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4CB **Finding notes shared read only.** A note shared publicly
      for reading now appears in the read only view of your notes, where it was readable
      by anyone with the link but listed nowhere at all. [#27637](https://github.com/open-webui/open-webui/pull/27637),
      [#27487](https://github.com/open-webui/open-webui/issues/27487)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5C3 **Shared folders reordering themselves.** The list of folders
      shared with you now keeps a consistent order, where on PostgreSQL renaming a
      folder could shuffle the ones beside it. [#28804](https://github.com/open-webui/open-webui/pull/28804)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FAF1 **Abandoned changes to a group's sharing setting.** Closing
      the edit dialog for a user group without saving now discards a change to who
      can share to that group, where the change stayed on screen and was written to
      the database the next time anything else about the group was saved. [#28076](https://github.com/open-webui/open-webui/pull/28076),
      [#28075](https://github.com/open-webui/open-webui/issues/28075)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-collaboration-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: collaboration
  title: 6 Collaboration changes in v0.11.1
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-08-20-share-a-read-only-snapshot-of-a-codex-chat-personal-share-links-can-be-opened-by|Share
  a read-only snapshot of a Codex chat]]'
- '[[Changes/Codex CLI/2026-08-20-2-collaboration-changes-in-rust-v0-149-0|2 Collaboration
  changes in rust-v0.149.0]]'
- '[[Changes/Dify/2026-08-25-5-collaboration-changes-in-1-17-0|5 Collaboration changes
  in 1.17.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: collaboration
title: 6 Collaboration changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Collaboration changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗂️ **Folder permissions when starting a chat.** Starting a conversation filed into a folder now checks that you are allowed to write to that folder, a check the message sending path had been skipping, and every place a chat can be filed now treats ownership, shared access, and unknown folders the same way. [#28366](https://github.com/open-webui/open-webui/pull/28366)

> 🪪 **Authorship in shared chats.** A chat shared with you now shows the name and picture of whoever wrote it, in the message list and in the overview panel, rather than crediting the messages to you. [#28274](https://github.com/open-webui/open-webui/pull/28274), [#28273](https://github.com/open-webui/open-webui/issues/28273)

> 🧑🤝🧑 **Owner avatars on shared chats.** The picture beside a chat someone shared with you now loads, and falls back to the default image if it cannot, rather than leaving a blank gap when the interface and the server are on different addresses. [#28272](https://github.com/open-webui/open-webui/pull/28272), [#28271](https://github.com/open-webui/open-webui/issues/28271)

> 📋 **Finding notes shared read only.** A note shared publicly for reading now appears in the read only view of your notes, where it was readable by anyone with the link but listed nowhere at all. [#27637](https://github.com/open-webui/open-webui/pull/27637), [#27487](https://github.com/open-webui/open-webui/issues/27487)

> 🗃 **Shared folders reordering themselves.** The list of folders shared with you now keeps a consistent order, where on PostgreSQL renaming a folder could shuffle the ones beside it. [#28804](https://github.com/open-webui/open-webui/pull/28804)

> 🫱 **Abandoned changes to a group's sharing setting.** Closing the edit dialog for a user group without saving now discards a change to who can share to that group, where the change stayed on screen and was written to the database the next time anything else about the group was saved. [#28076](https://github.com/open-webui/open-webui/pull/28076), [#28075](https://github.com/open-webui/open-webui/issues/28075)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-08-25-9-files-and-data-changes-in-v0-11-1|9 Files and Data changes in v0.11.1]] · Files and Data
- [[Changes/Open WebUI/2026-08-25-image-generation-and-web-search-staying-switched-off-turning-either-off-now-take|🎨 Image generation and web search staying switched off. Turning either off now…]] · Image Generation
- [[Changes/Open WebUI/2026-08-25-7-safety-and-privacy-changes-in-v0-11-1|7 Safety and Privacy changes in v0.11.1]] · Safety and Privacy
- [[Changes/Open WebUI/2026-08-25-improved-ui-accessibility-a-closed-sidebar-is-no-longer-reachable-by-keyboard-or|♿ Improved UI accessibility. A closed sidebar is no longer reachable by keyboard…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-08-25-2-pricing-model-changes-in-v0-11-1|2 Pricing Model changes in v0.11.1]] · Pricing Model
- [[Changes/Open WebUI/2026-08-25-11-automation-and-scheduling-changes-in-v0-11-1|11 Automation and Scheduling changes in v0.11.1]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-08-25-10-reliability-and-performance-changes-in-v0-11-1|10 Reliability and Performance changes in v0.11.1]] · Reliability and Performance
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
## Nearby in Collaboration

- Earlier: 2026-08-25 · Dify · [[Changes/Dify/2026-08-25-5-collaboration-changes-in-1-17-0|5 Collaboration changes in 1.17.0]]
- Later: 2026-08-27 · Qoder · [[Changes/Qoder/2026-08-27-an-ecosystem-that-connects-with-70-plugins-20-000-skills-and-40-connectors-qoder|An ecosystem that connects]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-01-11 · Descript · [[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create a team here: (source link)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-6b109a&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-6-collaboration-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-6b109a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->