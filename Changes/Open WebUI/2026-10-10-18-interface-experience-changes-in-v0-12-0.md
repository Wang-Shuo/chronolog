---
card_id: open-webui-2026-10-10-a10caf
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Interface Experience: 18 changes in v0.12.0
  — \U0001FA9D **Import skills from a URL.** Administrators can now pick Import from
  URL in the…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2736
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e51f88fa71a5c4650c7c2cdd000abe3da29a6016520721ff86d832e07dcc9d47
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-a10caf
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 18 Interface Experience changes'
  evidence:
  - quote: "\U0001FA9D **Import skills from a URL.** Administrators can now pick Import
      from URL in the Skills workspace import menu to load skills from a GitHub repository,
      a GitHub folder or SKILL.md link, or a direct link to a ZIP, JSON or Markdown
      skill file, which open in the import preview to pick from; downloads are checked
      against internal addresses on every redirect and capped at 200 MiB. [Commit](https://github.com/open-webui/open-webui/commit/8d0ff76f2b8e21ae719a4b9338779b92b8778d98),
      [Commit](https://github.com/open-webui/open-webui/commit/d54aa9836eb7cf23e50b6f9ecd35316f09874f1b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ✋ **Tool approval in temporary chats.** With tool approval set to ask,
      tools called in a temporary chat now wait for an Allow or Deny dialog, where
      they ran without asking although the menu showed approval as on. [Commit](https://github.com/open-webui/open-webui/commit/82f142d376f8b2c83153607fd18ecff467e10c30),
      [#29249](https://github.com/open-webui/open-webui/issues/29249)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3AF **Skills from the / menu.** A skill picked from the / menu
      in the chat input is now applied to the reply the same way as one picked from
      the $ menu, where it was inserted as a mention and never loaded. [#31429](https://github.com/open-webui/open-webui/pull/31429),
      [#29978](https://github.com/open-webui/open-webui/issues/29978)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ♻️ **Skill toggles reach the chat.** Turning a skill on or off in the workspace
      now updates the skill menu in chat right away, where the old list stayed until
      a page reload. [#30966](https://github.com/open-webui/open-webui/pull/30966),
      [#30965](https://github.com/open-webui/open-webui/issues/30965)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4C1 **Folder clicks keep a chat's tools.** Clicking a folder name
      in the sidebar while a chat is open no longer swaps that chat's tools and skills
      for those of the folder's default model. [#30376](https://github.com/open-webui/open-webui/pull/30376),
      [#30226](https://github.com/open-webui/open-webui/issues/30226)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5C2️ **Blank folder names rejected.** Renaming or creating a folder
      with a name made only of spaces now shows \"Folder name cannot be empty.\" instead
      of saving a blank name that made the folder and its chats disappear from the
      sidebar after a refresh. [#31380](https://github.com/open-webui/open-webui/pull/31380),
      [#31379](https://github.com/open-webui/open-webui/issues/31379)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4E5 **Imported chats marked as read.** Imported and cloned chats
      no longer show as unread in the sidebar or count toward folder unread badges.
      [#30754](https://github.com/open-webui/open-webui/pull/30754), [#30750](https://github.com/open-webui/open-webui/issues/30750)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5B1️ **First click in dialogs opened from menus.** Menus such as
      the sidebar chat menu, the chat header menu, folder and note menus, the knowledge
      Add Content menu and the Actions menus now close when an item is picked, so
      the first click in the dialog it opens works, where buttons such as Copy Link
      and Confirm had to be clicked twice. [#31488](https://github.com/open-webui/open-webui/pull/31488),
      [Commit](https://github.com/open-webui/open-webui/commit/fdae17f8a6fc163f925b73286622eae32f029308),
      [#31486](https://github.com/open-webui/open-webui/issues/31486), [#31496](https://github.com/open-webui/open-webui/pull/31496),
      [#31493](https://github.com/open-webui/open-webui/issues/31493)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F532 **Full-screen chat input error.** Opening the full-screen chat
      input with text in it no longer throws an error in the browser console. [Commit](https://github.com/open-webui/open-webui/commit/b39abad5c28db8e69885b9fbc5f756ff74666a90),
      [#31465](https://github.com/open-webui/open-webui/issues/31465)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ✏️ **Folder rename saves once.** Renaming a folder in the sidebar and pressing
      Enter now saves the name once and shows one confirmation, where it saved it
      twice. [#31584](https://github.com/open-webui/open-webui/pull/31584), [#31582](https://github.com/open-webui/open-webui/issues/31582)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5D2️ **Read-only notes in the chat's note picker.** Searching the
      note picker in a chat now finds notes shared with you read only, where they
      disappeared as soon as you typed. [#30968](https://github.com/open-webui/open-webui/pull/30968),
      [#30967](https://github.com/open-webui/open-webui/issues/30967)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3AD **Pages with several main sections in the Playwright loader.**
      The Playwright web loader now reads the whole page when it has more than one
      main section, such as Ubiquiti tech specs pages, where it returned only the
      site menu and lost the actual content. [#31644](https://github.com/open-webui/open-webui/pull/31644),
      [#28643](https://github.com/open-webui/open-webui/issues/28643)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4E2 **Added channel members see the channel right away.** Someone
      added to a group channel or direct message now sees it appear in their sidebar
      and receives its new messages, edits, pins and reactions live, where nothing
      showed until they reloaded the page. [#31113](https://github.com/open-webui/open-webui/pull/31113),
      [#30432](https://github.com/open-webui/open-webui/issues/30432)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4CC **User menu pin buttons.** The Pin to Sidebar button in the
      user menu now switches its icon and tooltip as soon as it is clicked, and the
      pin buttons shown while holding Shift now hide when the window loses focus,
      where they stayed visible after Shift was released in another window. [#31843](https://github.com/open-webui/open-webui/pull/31843),
      [#31842](https://github.com/open-webui/open-webui/issues/31842), [#31841](https://github.com/open-webui/open-webui/pull/31841),
      [#31840](https://github.com/open-webui/open-webui/issues/31840)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4E4 **Unarchive from the chat menu.** The menu in the chat header
      now offers Unarchive for an archived chat and confirms it with a matching message,
      where it always showed Archive. [#31857](https://github.com/open-webui/open-webui/pull/31857),
      [#31473](https://github.com/open-webui/open-webui/issues/31473)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4C5 **Yesterday's chats on the first of the month.** Chats from
      the previous day are now listed under Yesterday in the sidebar on the first
      day of a month or year too, where they showed under Previous 7 days. [#31973](https://github.com/open-webui/open-webui/pull/31973),
      [#31964](https://github.com/open-webui/open-webui/issues/31964)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9F9 **Deleted chats leave their folder.** Deleting the open chat
      with the Delete Chat keyboard shortcut now also removes it from its folder in
      the sidebar, where it stayed listed there until the page was reloaded. [Commit](https://github.com/open-webui/open-webui/commit/5729d7ad810020a09563238ca9cba48943d6b5d9),
      [#31321](https://github.com/open-webui/open-webui/issues/31321)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F440 **Who added chats to a folder you share.** In a folder you
      own and share with others, chats they add now show their owner's profile picture
      in the sidebar, the same as in folders shared with you. [Commit](https://github.com/open-webui/open-webui/commit/ce18eca340e51111cae3612b1b8e07e916c06850)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 18-interface-experience-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: interface-experience
  title: 18 Interface Experience changes in v0.12.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-09-improved-fullscreen-mode-the-link-under-the-mouse-pointer-is-now-underlined-to-s|Improved
  fullscreen mode]]'
- '[[Changes/Devin/2026-10-09-secrets-sheets|Secrets sheets]]'
- '[[Changes/Raycast/2026-10-09-4-interface-experience-changes-in-raycast-macos-2-7|4
  Interface Experience changes in Raycast macos 2.7]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: interface-experience
title: 18 Interface Experience changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Interface Experience changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🪝 **Import skills from a URL.** Administrators can now pick Import from URL in the Skills workspace import menu to load skills from a GitHub repository, a GitHub folder or SKILL.md link, or a direct link to a ZIP, JSON or Markdown skill file, which open in the import preview to pick from; downloads are checked against internal addresses on every redirect and capped at 200 MiB. [Commit](https://github.com/open-webui/open-webui/commit/8d0ff76f2b8e21ae719a4b9338779b92b8778d98), [Commit](https://github.com/open-webui/open-webui/commit/d54aa9836eb7cf23e50b6f9ecd35316f09874f1b)

> ✋ **Tool approval in temporary chats.** With tool approval set to ask, tools called in a temporary chat now wait for an Allow or Deny dialog, where they ran without asking although the menu showed approval as on. [Commit](https://github.com/open-webui/open-webui/commit/82f142d376f8b2c83153607fd18ecff467e10c30), [#29249](https://github.com/open-webui/open-webui/issues/29249)

> 🎯 **Skills from the / menu.** A skill picked from the / menu in the chat input is now applied to the reply the same way as one picked from the $ menu, where it was inserted as a mention and never loaded. [#31429](https://github.com/open-webui/open-webui/pull/31429), [#29978](https://github.com/open-webui/open-webui/issues/29978)

> ♻️ **Skill toggles reach the chat.** Turning a skill on or off in the workspace now updates the skill menu in chat right away, where the old list stayed until a page reload. [#30966](https://github.com/open-webui/open-webui/pull/30966), [#30965](https://github.com/open-webui/open-webui/issues/30965)

> 📁 **Folder clicks keep a chat's tools.** Clicking a folder name in the sidebar while a chat is open no longer swaps that chat's tools and skills for those of the folder's default model. [#30376](https://github.com/open-webui/open-webui/pull/30376), [#30226](https://github.com/open-webui/open-webui/issues/30226)

> 🗂️ **Blank folder names rejected.** Renaming or creating a folder with a name made only of spaces now shows "Folder name cannot be empty." instead of saving a blank name that made the folder and its chats disappear from the sidebar after a refresh. [#31380](https://github.com/open-webui/open-webui/pull/31380), [#31379](https://github.com/open-webui/open-webui/issues/31379)

> 📥 **Imported chats marked as read.** Imported and cloned chats no longer show as unread in the sidebar or count toward folder unread badges. [#30754](https://github.com/open-webui/open-webui/pull/30754), [#30750](https://github.com/open-webui/open-webui/issues/30750)

> 🖱️ **First click in dialogs opened from menus.** Menus such as the sidebar chat menu, the chat header menu, folder and note menus, the knowledge Add Content menu and the Actions menus now close when an item is picked, so the first click in the dialog it opens works, where buttons such as Copy Link and Confirm had to be clicked twice. [#31488](https://github.com/open-webui/open-webui/pull/31488), [Commit](https://github.com/open-webui/open-webui/commit/fdae17f8a6fc163f925b73286622eae32f029308), [#31486](https://github.com/open-webui/open-webui/issues/31486), [#31496](https://github.com/open-webui/open-webui/pull/31496), [#31493](https://github.com/open-webui/open-webui/issues/31493)

> 🔲 **Full-screen chat input error.** Opening the full-screen chat input with text in it no longer throws an error in the browser console. [Commit](https://github.com/open-webui/open-webui/commit/b39abad5c28db8e69885b9fbc5f756ff74666a90), [#31465](https://github.com/open-webui/open-webui/issues/31465)

> ✏️ **Folder rename saves once.** Renaming a folder in the sidebar and pressing Enter now saves the name once and shows one confirmation, where it saved it twice. [#31584](https://github.com/open-webui/open-webui/pull/31584), [#31582](https://github.com/open-webui/open-webui/issues/31582)

> 🗒️ **Read-only notes in the chat's note picker.** Searching the note picker in a chat now finds notes shared with you read only, where they disappeared as soon as you typed. [#30968](https://github.com/open-webui/open-webui/pull/30968), [#30967](https://github.com/open-webui/open-webui/issues/30967)

> 🎭 **Pages with several main sections in the Playwright loader.** The Playwright web loader now reads the whole page when it has more than one main section, such as Ubiquiti tech specs pages, where it returned only the site menu and lost the actual content. [#31644](https://github.com/open-webui/open-webui/pull/31644), [#28643](https://github.com/open-webui/open-webui/issues/28643)

> 📢 **Added channel members see the channel right away.** Someone added to a group channel or direct message now sees it appear in their sidebar and receives its new messages, edits, pins and reactions live, where nothing showed until they reloaded the page. [#31113](https://github.com/open-webui/open-webui/pull/31113), [#30432](https://github.com/open-webui/open-webui/issues/30432)

> 📌 **User menu pin buttons.** The Pin to Sidebar button in the user menu now switches its icon and tooltip as soon as it is clicked, and the pin buttons shown while holding Shift now hide when the window loses focus, where they stayed visible after Shift was released in another window. [#31843](https://github.com/open-webui/open-webui/pull/31843), [#31842](https://github.com/open-webui/open-webui/issues/31842), [#31841](https://github.com/open-webui/open-webui/pull/31841), [#31840](https://github.com/open-webui/open-webui/issues/31840)

> 📤 **Unarchive from the chat menu.** The menu in the chat header now offers Unarchive for an archived chat and confirms it with a matching message, where it always showed Archive. [#31857](https://github.com/open-webui/open-webui/pull/31857), [#31473](https://github.com/open-webui/open-webui/issues/31473)

> 📅 **Yesterday's chats on the first of the month.** Chats from the previous day are now listed under Yesterday in the sidebar on the first day of a month or year too, where they showed under Previous 7 days. [#31973](https://github.com/open-webui/open-webui/pull/31973), [#31964](https://github.com/open-webui/open-webui/issues/31964)

> 🧹 **Deleted chats leave their folder.** Deleting the open chat with the Delete Chat keyboard shortcut now also removes it from its folder in the sidebar, where it stayed listed there until the page was reloaded. [Commit](https://github.com/open-webui/open-webui/commit/5729d7ad810020a09563238ca9cba48943d6b5d9), [#31321](https://github.com/open-webui/open-webui/issues/31321)

> 👀 **Who added chats to a folder you share.** In a folder you own and share with others, chats they add now show their owner's profile picture in the sidebar, the same as in folders shared with you. [Commit](https://github.com/open-webui/open-webui/commit/ce18eca340e51111cae3612b1b8e07e916c06850)

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
- [[Changes/Open WebUI/2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0|10 Automation and Scheduling changes in v0.12.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile and Desktop changes in v0.12.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-10-10-6-files-and-data-changes-in-v0-12-0|6 Files and Data changes in v0.12.0]] · Files and Data
- [[Changes/Open WebUI/2026-10-10-13-collaboration-changes-in-v0-12-0|13 Collaboration changes in v0.12.0]] · Collaboration
- [[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2 Memory and Personalization changes in v0.12.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-10-5-context-window-changes-in-v0-12-0|5 Context Window changes in v0.12.0]] · Context Window
- [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]] · Agent Mode
- [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-10-09 · Raycast · [[Changes/Raycast/2026-10-09-4-interface-experience-changes-in-raycast-macos-2-7|4 Interface Experience changes in Raycast macos 2.7]]
- Later: 2026-10-10 · OpenClaw · [[Changes/OpenClaw/2026-10-10-20-interface-experience-changes-in-v2026-10-1|20 Interface Experience changes in v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-a10caf&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-18-interface-experience-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-a10caf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->