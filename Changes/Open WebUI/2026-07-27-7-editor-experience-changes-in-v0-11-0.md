---
card_id: open-webui-2026-07-27-f10d46
date: '2026-07-27'
description: "Open WebUI · 2026-07-27 · Editor Experience: 7 changes in v0.11.0 —
  \U0001F514 **Notification targets.** Notifications now have their own settings tab
  where you can…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1231
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1f0a0bf802db2a860ff7e4281963fbc1d272f568e8a32f1062129d95b93b6982
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-27-f10d46
  comparison: ''
  date: '2026-07-27'
  description: 'Open WebUI — v0.11.0: 7 Editor Experience changes'
  evidence:
  - quote: "\U0001F514 **Notification targets.** Notifications now have their own
      settings tab where you can send them to several webhook destinations, each picking
      which events it wants, from chats finishing or failing to channel messages and
      calendar alerts, with a test button and a choice between always notifying or
      only when you are away, and any webhook you already had is carried over for
      you. [Commit](https://github.com/open-webui/open-webui/commit/c55e373b994d3a14c99a97f44261422012f63266),
      [Commit](https://github.com/open-webui/open-webui/commit/cf235738f5a44db415012b3b0ebc1f6e752f5439),
      [Commit](https://github.com/open-webui/open-webui/commit/200d447f6289faca42f2a666bbabae2c7f3ebadf),
      [#24750](https://github.com/open-webui/open-webui/issues/24750)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F3A7 **No wasted work when nobody is listening.** Updates for a
      chat whose tab has been closed, or for requests made through the API, are no
      longer packaged up only to be discarded, which matters most on long streamed
      replies. [#27366](https://github.com/open-webui/open-webui/pull/27366), [Commit](https://github.com/open-webui/open-webui/commit/858e9236df1c3d84782e373c22b56cfc312b6db8)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F6C5 **Writing into someone else's chat.** Completion and action
      requests now confirm you own the chat they name before anything is written to
      it, so a filter or action can no longer be pointed at another person's conversation.
      [#27486](https://github.com/open-webui/open-webui/pull/27486)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9EA **Filter edits that survive a reload.** A change a filter makes
      to a finished response is now saved with the conversation, instead of showing
      on screen and reverting the next time the chat is opened. [#27414](https://github.com/open-webui/open-webui/pull/27414),
      [#27017](https://github.com/open-webui/open-webui/issues/27017)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4FB **Live updates in a second tab.** Opening Open WebUI again
      while already connected now joins the new tab to your event stream, so notifications
      and chat updates reach every open tab instead of only the first one. [Commit](https://github.com/open-webui/open-webui/commit/d14fddf25405cd58184fdef3d2af012503e4edd8)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9F0 **Model editor loading.** The model editor no longer fails
      to open when its tool list can't be loaded, falling back gracefully instead.
      [Commit](https://github.com/open-webui/open-webui/commit/10724d057af13a826c52e92b1c01a031656768d5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4F6 **Reconnect warnings on mobile.** Switching back to Open WebUI
      after using another app no longer flashes a connection lost warning while the
      tab wakes up and reconnects on its own. [Commit](https://github.com/open-webui/open-webui/commit/63ada247066dfc51e0e9559366f0cfd9a98db40b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 7-editor-experience-changes-in-v0-11-0
  source_release: open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f
  source_type: github_releases
  theme: editor-experience
  title: 7 Editor Experience changes in v0.11.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-21-added-emoji-shortcode-autocomplete-in-the-prompt-input-type-heart-to-insert-or-h|Added
  emoji shortcode autocomplete in the prompt input]]'
- '[[Changes/Codex CLI/2026-07-21-4-editor-experience-changes-in-rust-v0-145-0|4 Editor
  Experience changes in rust-v0.145.0]]'
- '[[Changes/GitHub Copilot CLI/2026-07-23-show-tab-in-settings-footer-to-switch-scope-tabs|Show
  Tab in /settings footer to switch scope tabs]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f]]'
source_type: github_releases
theme: editor-experience
title: 7 Editor Experience changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Editor Experience changes in v0.11.0

**Open WebUI** · 2026-07-27 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.0) · from [[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔔 **Notification targets.** Notifications now have their own settings tab where you can send them to several webhook destinations, each picking which events it wants, from chats finishing or failing to channel messages and calendar alerts, with a test button and a choice between always notifying or only when you are away, and any webhook you already had is carried over for you. [Commit](https://github.com/open-webui/open-webui/commit/c55e373b994d3a14c99a97f44261422012f63266), [Commit](https://github.com/open-webui/open-webui/commit/cf235738f5a44db415012b3b0ebc1f6e752f5439), [Commit](https://github.com/open-webui/open-webui/commit/200d447f6289faca42f2a666bbabae2c7f3ebadf), [#24750](https://github.com/open-webui/open-webui/issues/24750)

> 🎧 **No wasted work when nobody is listening.** Updates for a chat whose tab has been closed, or for requests made through the API, are no longer packaged up only to be discarded, which matters most on long streamed replies. [#27366](https://github.com/open-webui/open-webui/pull/27366), [Commit](https://github.com/open-webui/open-webui/commit/858e9236df1c3d84782e373c22b56cfc312b6db8)

> 🛅 **Writing into someone else's chat.** Completion and action requests now confirm you own the chat they name before anything is written to it, so a filter or action can no longer be pointed at another person's conversation. [#27486](https://github.com/open-webui/open-webui/pull/27486)

> 🧪 **Filter edits that survive a reload.** A change a filter makes to a finished response is now saved with the conversation, instead of showing on screen and reverting the next time the chat is opened. [#27414](https://github.com/open-webui/open-webui/pull/27414), [#27017](https://github.com/open-webui/open-webui/issues/27017)

> 📻 **Live updates in a second tab.** Opening Open WebUI again while already connected now joins the new tab to your event stream, so notifications and chat updates reach every open tab instead of only the first one. [Commit](https://github.com/open-webui/open-webui/commit/d14fddf25405cd58184fdef3d2af012503e4edd8)

> 🧰 **Model editor loading.** The model editor no longer fails to open when its tool list can't be loaded, falling back gracefully instead. [Commit](https://github.com/open-webui/open-webui/commit/10724d057af13a826c52e92b1c01a031656768d5)

> 📶 **Reconnect warnings on mobile.** Switching back to Open WebUI after using another app no longer flashes a connection lost warning while the tab wakes up and reconnects on its own. [Commit](https://github.com/open-webui/open-webui/commit/63ada247066dfc51e0e9559366f0cfd9a98db40b)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-27-9-automation-and-scheduling-changes-in-v0-11-0|9 Automation and Scheduling changes in v0.11.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety and Privacy changes in v0.11.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-27-4-voice-and-audio-changes-in-v0-11-0|4 Voice and Audio changes in v0.11.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-07-27-62-developer-workflow-changes-in-v0-11-0|62 Developer Workflow changes in v0.11.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-27-19-interface-experience-changes-in-v0-11-0|19 Interface Experience changes in v0.11.0]] · Interface Experience
- [[Changes/Open WebUI/2026-07-27-7-memory-and-personalization-changes-in-v0-11-0|7 Memory and Personalization changes in v0.11.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-07-27-sub-agents-administrators-can-now-enable-sub-agents-which-let-a-model-hand-parts|🤖 Sub-agents. Administrators can now enable sub-agents, which let a model hand…]] · Agent Mode
- [[Changes/Open WebUI/2026-07-27-media-types-an-extraction-engine-may-handle-administrators-can-now-list-which-im|🖼️ Media types an extraction engine may handle. Administrators can now list…]] · Multimodal Input
- [[Changes/Open WebUI/2026-07-27-15-account-and-access-changes-in-v0-11-0|15 Account and Access changes in v0.11.0]] · Account and Access
- [[Changes/Open WebUI/2026-07-27-shared-image-checkpoint-changes-only-administrators-can-now-change-the-instance|🖌️ Shared image checkpoint changes. Only administrators can now change…]] · Image Generation
- [[Changes/Open WebUI/2026-07-27-7-search-and-browsing-changes-in-v0-11-0|7 Search and Browsing changes in v0.11.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-07-27-2-collaboration-changes-in-v0-11-0|2 Collaboration changes in v0.11.0]] · Collaboration
- [[Changes/Open WebUI/2026-07-27-6-apps-and-integrations-changes-in-v0-11-0|6 Apps and Integrations changes in v0.11.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-07-27-3-enterprise-and-administration-changes-in-v0-11-0|3 Enterprise and Administration changes in v0.11.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-07-27-9-context-window-changes-in-v0-11-0|9 Context Window changes in v0.11.0]] · Context Window
- [[Changes/Open WebUI/2026-07-27-12-reliability-and-performance-changes-in-v0-11-0|12 Reliability and Performance changes in v0.11.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-07-27-2-pricing-model-changes-in-v0-11-0|2 Pricing Model changes in v0.11.0]] · Pricing Model
- [[Changes/Open WebUI/2026-07-27-9-files-and-data-changes-in-v0-11-0|9 Files and Data changes in v0.11.0]] · Files and Data
- [[Changes/Open WebUI/2026-07-27-39-model-support-changes-in-v0-11-0|39 Model Support changes in v0.11.0]] · Model Support
- [[Changes/Open WebUI/2026-07-27-2-mobile-and-desktop-changes-in-v0-11-0|2 Mobile and Desktop changes in v0.11.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-07-27-42-other-changes-in-v0-11-0|42 other changes in v0.11.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-07-23 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-23-show-tab-in-settings-footer-to-switch-scope-tabs|Show Tab in /settings footer to switch scope tabs]]
- Later: 2026-07-28 · Dify · [[Changes/Dify/2026-07-28-feat-web-locate-workflow-nodes-by-node-id-in-the-workflow-editor-by-ruanimal-in|feat(web): locate workflow nodes by node_id in the workflow editor]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-27-f10d46&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-27-7-editor-experience-changes-in-v0-11-0.md%0ACard%20ID%3A%20open-webui-2026-07-27-f10d46%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->