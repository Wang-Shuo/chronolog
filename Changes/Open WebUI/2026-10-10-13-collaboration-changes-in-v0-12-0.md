---
card_id: open-webui-2026-10-10-755a1d
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Collaboration: 13 changes in v0.12.0 — \U0001F46B
  **Replying in shared chats.** When sharing a chat with people or groups, or sharing
  a…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1235
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 67227a236af3647f7ac6a77355c32f61c4391998b8c09438c35765568b3c9731
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-755a1d
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 13 Collaboration changes'
  evidence:
  - quote: "\U0001F46B **Replying in shared chats.** When sharing a chat with people
      or groups, or sharing a folder, the new Sharing mode setting can be switched
      from Clone only to Allow replies, so everyone it is shared with can keep writing
      in the same conversation instead of cloning it. Each message shows the name
      and profile picture of who sent it, with other people's messages on the left
      in bubble view, replies stream live to everyone with the chat open, a line above
      the input shows who is typing, people can only edit, rate, regenerate or stop
      their own messages, and the owner's own chat settings, title and tags stay untouched
      by others. [Commit](https://github.com/open-webui/open-webui/commit/de73bb830aeb150bc5bb4707566d3969f70408b0),
      [Commit](https://github.com/open-webui/open-webui/commit/6cfd6987e5b220040c2e476105779dcc10d3d14b),
      [Commit](https://github.com/open-webui/open-webui/commit/1e9dd6e330548c20a1d4054206c3e1b77fb08a5a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4E1 **Lighter multi-instance streaming.** Deployments that share
      websocket traffic through Redis use less CPU while streaming, because each server
      now skips live updates for rooms it has no one in; set \"WEBSOCKET_REDIS_ROOM_CHANNELS\"
      to false to restore the previous delivery. [#28818](https://github.com/open-webui/open-webui/pull/28818),
      [#28173](https://github.com/open-webui/open-webui/issues/28173)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F512 **Share links of deleted folders.** Deleting a folder together
      with its chats now also removes those chats' share links, where the shared conversations
      stayed reachable through them. [#31306](https://github.com/open-webui/open-webui/pull/31306),
      [#31305](https://github.com/open-webui/open-webui/issues/31305)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F648 **Admin chat access setting enforced everywhere.** With \"ENABLE_ADMIN_CHAT_ACCESS\"
      turned off, administrators can no longer read, change, share, clone, delete,
      message into or attach other users' chats through direct API requests, where
      only opening them was refused. [#31416](https://github.com/open-webui/open-webui/pull/31416),
      [#31413](https://github.com/open-webui/open-webui/issues/31413)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F441️ **Cloning shared chats checks access first.** Cloning a shared
      chat now checks access to the share before its content is read, the same order
      the shared chat view uses. [#30388](https://github.com/open-webui/open-webui/pull/30388)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4C1 **Files attached to folders.** Files attached to a folder when
      it is created, or newly added by someone editing a shared folder, are now checked
      against that person's own access, so a folder can no longer be used to reach
      files they cannot open. [#30442](https://github.com/open-webui/open-webui/pull/30442)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F517 **Share link access after relinking.** Deleting a shared chat's
      link and creating a new one without closing the Share dialog now shows the new
      link's own access, where the dialog kept showing the old link's setting such
      as Public. [#31037](https://github.com/open-webui/open-webui/pull/31037), [#31029](https://github.com/open-webui/open-webui/issues/31029)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5E8️ **Share dialog wording.** The Share dialog now says a new
      link stays private until you choose who can view it, where it claimed anyone
      with the URL could view the chat. [#31420](https://github.com/open-webui/open-webui/pull/31420),
      [#31417](https://github.com/open-webui/open-webui/issues/31417)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F411 **Cloned chats in shared folders.** Cloning a chat in a folder
      shared with you with write access now keeps the clone in that folder, where
      it landed at the top of your chat list. [#31370](https://github.com/open-webui/open-webui/pull/31370),
      [#31369](https://github.com/open-webui/open-webui/issues/31369)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4E6 **New files in shared chats.** Files attached to a message
      together with a file already in the chat now open in shared copies of the chat,
      where none of the new files were recorded and people opening the shared chat
      could not open them. [#31650](https://github.com/open-webui/open-webui/pull/31650),
      [#31648](https://github.com/open-webui/open-webui/issues/31648)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4C3 **Line breaks after reloading.** Lines separated by a single
      line break now stay on separate lines after reloading the page, when opening
      a chat by its URL and on shared chat links, where they ran together into one
      line. [#31869](https://github.com/open-webui/open-webui/pull/31869)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F645 **Share hidden in the function menu without Community Sharing.**
      With Community Sharing off, the function menu in the admin Functions list no
      longer offers Share, matching the model, prompt and tool menus. [#31820](https://github.com/open-webui/open-webui/pull/31820),
      [#31819](https://github.com/open-webui/open-webui/issues/31819)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F516 **Page titles on external knowledge citations.** Citation markers
      in answers from external knowledge bases now show each page's title instead
      of the site's domain, falling back to the domain only when a page has no title,
      and pages that share a title no longer shift the labels of later citations.
      [#31982](https://github.com/open-webui/open-webui/pull/31982), [#31929](https://github.com/open-webui/open-webui/issues/31929)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 13-collaboration-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: collaboration
  title: 13 Collaboration changes in v0.12.0
  type: change
related_changes:
- '[[Changes/Claude/2026-10-07-monthly-api-credits-for-max-and-team-plans|Monthly
  API credits for Max and Team plans]]'
- '[[Changes/Codex CLI/2026-10-07-2-collaboration-changes-in-rust-v0-161-0|2 Collaboration
  changes in rust-v0.161.0]]'
- '[[Changes/Codex CLI/2026-10-08-2-collaboration-changes-in-rust-v0-162-0|2 Collaboration
  changes in rust-v0.162.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: collaboration
title: 13 Collaboration changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Collaboration changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 👫 **Replying in shared chats.** When sharing a chat with people or groups, or sharing a folder, the new Sharing mode setting can be switched from Clone only to Allow replies, so everyone it is shared with can keep writing in the same conversation instead of cloning it. Each message shows the name and profile picture of who sent it, with other people's messages on the left in bubble view, replies stream live to everyone with the chat open, a line above the input shows who is typing, people can only edit, rate, regenerate or stop their own messages, and the owner's own chat settings, title and tags stay untouched by others. [Commit](https://github.com/open-webui/open-webui/commit/de73bb830aeb150bc5bb4707566d3969f70408b0), [Commit](https://github.com/open-webui/open-webui/commit/6cfd6987e5b220040c2e476105779dcc10d3d14b), [Commit](https://github.com/open-webui/open-webui/commit/1e9dd6e330548c20a1d4054206c3e1b77fb08a5a)

> 📡 **Lighter multi-instance streaming.** Deployments that share websocket traffic through Redis use less CPU while streaming, because each server now skips live updates for rooms it has no one in; set "WEBSOCKET_REDIS_ROOM_CHANNELS" to false to restore the previous delivery. [#28818](https://github.com/open-webui/open-webui/pull/28818), [#28173](https://github.com/open-webui/open-webui/issues/28173)

> 🔒 **Share links of deleted folders.** Deleting a folder together with its chats now also removes those chats' share links, where the shared conversations stayed reachable through them. [#31306](https://github.com/open-webui/open-webui/pull/31306), [#31305](https://github.com/open-webui/open-webui/issues/31305)

> 🙈 **Admin chat access setting enforced everywhere.** With "ENABLE_ADMIN_CHAT_ACCESS" turned off, administrators can no longer read, change, share, clone, delete, message into or attach other users' chats through direct API requests, where only opening them was refused. [#31416](https://github.com/open-webui/open-webui/pull/31416), [#31413](https://github.com/open-webui/open-webui/issues/31413)

> 👁️ **Cloning shared chats checks access first.** Cloning a shared chat now checks access to the share before its content is read, the same order the shared chat view uses. [#30388](https://github.com/open-webui/open-webui/pull/30388)

> 📁 **Files attached to folders.** Files attached to a folder when it is created, or newly added by someone editing a shared folder, are now checked against that person's own access, so a folder can no longer be used to reach files they cannot open. [#30442](https://github.com/open-webui/open-webui/pull/30442)

> 🔗 **Share link access after relinking.** Deleting a shared chat's link and creating a new one without closing the Share dialog now shows the new link's own access, where the dialog kept showing the old link's setting such as Public. [#31037](https://github.com/open-webui/open-webui/pull/31037), [#31029](https://github.com/open-webui/open-webui/issues/31029)

> 🗨️ **Share dialog wording.** The Share dialog now says a new link stays private until you choose who can view it, where it claimed anyone with the URL could view the chat. [#31420](https://github.com/open-webui/open-webui/pull/31420), [#31417](https://github.com/open-webui/open-webui/issues/31417)

> 🐑 **Cloned chats in shared folders.** Cloning a chat in a folder shared with you with write access now keeps the clone in that folder, where it landed at the top of your chat list. [#31370](https://github.com/open-webui/open-webui/pull/31370), [#31369](https://github.com/open-webui/open-webui/issues/31369)

> 📦 **New files in shared chats.** Files attached to a message together with a file already in the chat now open in shared copies of the chat, where none of the new files were recorded and people opening the shared chat could not open them. [#31650](https://github.com/open-webui/open-webui/pull/31650), [#31648](https://github.com/open-webui/open-webui/issues/31648)

> 📃 **Line breaks after reloading.** Lines separated by a single line break now stay on separate lines after reloading the page, when opening a chat by its URL and on shared chat links, where they ran together into one line. [#31869](https://github.com/open-webui/open-webui/pull/31869)

> 🙅 **Share hidden in the function menu without Community Sharing.** With Community Sharing off, the function menu in the admin Functions list no longer offers Share, matching the model, prompt and tool menus. [#31820](https://github.com/open-webui/open-webui/pull/31820), [#31819](https://github.com/open-webui/open-webui/issues/31819)

> 🔖 **Page titles on external knowledge citations.** Citation markers in answers from external knowledge bases now show each page's title instead of the site's domain, falling back to the domain only when a page has no title, and pages that share a title no longer shift the labels of later citations. [#31982](https://github.com/open-webui/open-webui/pull/31982), [#31929](https://github.com/open-webui/open-webui/issues/31929)

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
## Nearby in Collaboration

- Earlier: 2026-10-08 · Codex CLI · [[Changes/Codex CLI/2026-10-08-2-collaboration-changes-in-rust-v0-162-0|2 Collaboration changes in rust-v0.162.0]]
- Later: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-changed-local-session-transcripts-to-also-record-each-api-request-s-system-promp|Changed local session transcripts to also record each API request's system prompt…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-24 · ChatGPT · [[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-755a1d&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-13-collaboration-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-755a1d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->