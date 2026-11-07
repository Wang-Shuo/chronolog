---
card_id: open-webui-2026-06-29-0c6101
date: '2026-06-29'
description: "Open WebUI · 2026-06-29 · Interface Experience: 14 changes in v0.10.0
  — \U0001F5A5️ **Setting for terminal sidebar auto-open.** A new interface setting
  controls whether…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2633
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 49fd2b4825a16c9b233dbb0ef92a4fe80e8fbd77c1a9f83548de8662ea1f2ff9
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-0c6101
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 14 Interface Experience changes'
  evidence:
  - quote: "\U0001F5A5️ **Setting for terminal sidebar auto-open.** A new interface
      setting controls whether the files sidebar opens automatically when you select
      a terminal. [Commit](https://github.com/open-webui/open-webui/commit/958237473f8cbde97eb0df8c21f2a4de088c4459),
      [#25628](https://github.com/open-webui/open-webui/pull/25628)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4CC **Reorder pinned notes by dragging.** Pinned notes in the sidebar
      can now be dragged to reorder them. [#25677](https://github.com/open-webui/open-webui/pull/25677)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F590️ **Drag items from the sidebar into chat.** Folders, notes,
      and models — including pinned notes — can now be dragged from the sidebar into
      the chat input. [#25771](https://github.com/open-webui/open-webui/pull/25771),
      [Commit](https://github.com/open-webui/open-webui/commit/dc1bc41d2e), [#26384](https://github.com/open-webui/open-webui/pull/26384)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F39B️ **Unified model picker for workspace base model.** Choosing
      a base model in the model editor now uses the searchable model selector instead
      of a plain field, making it easier to find and pick the right model. [Commit](https://github.com/open-webui/open-webui/commit/c89fd237b822877bffbb33a37402622983c7189d),
      [#24576](https://github.com/open-webui/open-webui/issues/24576)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4C8 **Richer analytics with a date picker.** The analytics dashboard
      now lets you choose a date range and shows additional columns. [#25922](https://github.com/open-webui/open-webui/pull/25922),
      [#25919](https://github.com/open-webui/open-webui/issues/25919)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **Smoother tool-call rendering.** Displaying tool calls now parses their
      content iteratively, avoiding slowdowns on deeply nested data. [#26146](https://github.com/open-webui/open-webui/pull/26146)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F9F5 **Code blocks render in channel threads.** Code blocks now
      display correctly in a channel's thread view, where duplicated message identifiers
      previously broke their rendering. [Commit](https://github.com/open-webui/open-webui/commit/7d1f9415807a47e0da4f862327e9802a3b839753),
      [#25917](https://github.com/open-webui/open-webui/pull/25917)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4CC **Pinned notes stay in sync.** Pinning, unpinning, or deleting
      a note now updates the sidebar's pinned list consistently, instead of showing
      a stale pin state. [#25918](https://github.com/open-webui/open-webui/pull/25918),
      [#25640](https://github.com/open-webui/open-webui/pull/25640)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F9F7 **Damaged chat history recovers more reliably.** When a chat's
      current position is missing or points at a malformed message, Open WebUI now
      repairs it from the latest valid message — on both the client and the server
      — instead of risking a broken history view. [Commit](https://github.com/open-webui/open-webui/commit/2308b59f135e4c2da11eabdf2306e55a5dd4e9fb),
      [Commit](https://github.com/open-webui/open-webui/commit/a146e17bdcaf94fee3a98aa36b4f401e1f06c1d4),
      [#26298](https://github.com/open-webui/open-webui/pull/26298), [#26258](https://github.com/open-webui/open-webui/pull/26258),
      [#26257](https://github.com/open-webui/open-webui/issues/26257)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F3F7️ **Long chat tag lists scroll.** The tags section in the chat
      menu now scrolls instead of overflowing when a chat has many tags. [#26031](https://github.com/open-webui/open-webui/pull/26031)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F39B️ **Chat controls persist across navigation.** Edits to chat
      controls are now kept when navigating between chats, and reverting a control
      to the chat's saved value persists correctly, instead of being lost. [#26336](https://github.com/open-webui/open-webui/pull/26336),
      [#25793](https://github.com/open-webui/open-webui/pull/25793)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4DC **No stray scrollbar on the About page.** Extra spacing that
      caused an unnecessary scrollbar on the About settings page has been removed.
      [#25802](https://github.com/open-webui/open-webui/pull/25802)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ➗ **Large math expressions no longer crash rendering.** Parsing math delimiters
      no longer overflows on very large or deeply nested input, so messages with heavy
      math render instead of failing. [#25845](https://github.com/open-webui/open-webui/pull/25845)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4DC **Visible chat scrollbar.** The chat area now shows a scrollbar,
      making it easier to scroll through long responses. [Commit](https://github.com/open-webui/open-webui/commit/d56e1cb0b9),
      [#25833](https://github.com/open-webui/open-webui/issues/25833)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 14-interface-experience-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: interface-experience
  title: 14 Interface Experience changes in v0.10.0
  type: change
related_changes:
- '[[Changes/v0/2026-06-26-2-interface-experience-changes-in-platform-api-v2-mcp-chat-tools|2
  Interface Experience changes in Platform API v2, MCP chat tools…]]'
- '[[Changes/Cline/2026-06-29-fully-remove-the-clinepass-feature-flag-so-clinepass-is-available-everywhere-in|Fully
  remove the ClinePass feature flag so ClinePass is available everywhere in the UI]]'
- '[[Changes/Kimi Code/2026-06-29-2-interface-experience-changes-in-kimi-code-0-20-2|2
  Interface Experience changes in Kimi Code 0.20.2]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: interface-experience
title: 14 Interface Experience changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Interface Experience changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🖥️ **Setting for terminal sidebar auto-open.** A new interface setting controls whether the files sidebar opens automatically when you select a terminal. [Commit](https://github.com/open-webui/open-webui/commit/958237473f8cbde97eb0df8c21f2a4de088c4459), [#25628](https://github.com/open-webui/open-webui/pull/25628)

> 📌 **Reorder pinned notes by dragging.** Pinned notes in the sidebar can now be dragged to reorder them. [#25677](https://github.com/open-webui/open-webui/pull/25677)

> 🖐️ **Drag items from the sidebar into chat.** Folders, notes, and models — including pinned notes — can now be dragged from the sidebar into the chat input. [#25771](https://github.com/open-webui/open-webui/pull/25771), [Commit](https://github.com/open-webui/open-webui/commit/dc1bc41d2e), [#26384](https://github.com/open-webui/open-webui/pull/26384)

> 🎛️ **Unified model picker for workspace base model.** Choosing a base model in the model editor now uses the searchable model selector instead of a plain field, making it easier to find and pick the right model. [Commit](https://github.com/open-webui/open-webui/commit/c89fd237b822877bffbb33a37402622983c7189d), [#24576](https://github.com/open-webui/open-webui/issues/24576)

> 📈 **Richer analytics with a date picker.** The analytics dashboard now lets you choose a date range and shows additional columns. [#25922](https://github.com/open-webui/open-webui/pull/25922), [#25919](https://github.com/open-webui/open-webui/issues/25919)

> ⚡ **Smoother tool-call rendering.** Displaying tool calls now parses their content iteratively, avoiding slowdowns on deeply nested data. [#26146](https://github.com/open-webui/open-webui/pull/26146)

> 🧵 **Code blocks render in channel threads.** Code blocks now display correctly in a channel's thread view, where duplicated message identifiers previously broke their rendering. [Commit](https://github.com/open-webui/open-webui/commit/7d1f9415807a47e0da4f862327e9802a3b839753), [#25917](https://github.com/open-webui/open-webui/pull/25917)

> 📌 **Pinned notes stay in sync.** Pinning, unpinning, or deleting a note now updates the sidebar's pinned list consistently, instead of showing a stale pin state. [#25918](https://github.com/open-webui/open-webui/pull/25918), [#25640](https://github.com/open-webui/open-webui/pull/25640)

> 🧷 **Damaged chat history recovers more reliably.** When a chat's current position is missing or points at a malformed message, Open WebUI now repairs it from the latest valid message — on both the client and the server — instead of risking a broken history view. [Commit](https://github.com/open-webui/open-webui/commit/2308b59f135e4c2da11eabdf2306e55a5dd4e9fb), [Commit](https://github.com/open-webui/open-webui/commit/a146e17bdcaf94fee3a98aa36b4f401e1f06c1d4), [#26298](https://github.com/open-webui/open-webui/pull/26298), [#26258](https://github.com/open-webui/open-webui/pull/26258), [#26257](https://github.com/open-webui/open-webui/issues/26257)

> 🏷️ **Long chat tag lists scroll.** The tags section in the chat menu now scrolls instead of overflowing when a chat has many tags. [#26031](https://github.com/open-webui/open-webui/pull/26031)

> 🎛️ **Chat controls persist across navigation.** Edits to chat controls are now kept when navigating between chats, and reverting a control to the chat's saved value persists correctly, instead of being lost. [#26336](https://github.com/open-webui/open-webui/pull/26336), [#25793](https://github.com/open-webui/open-webui/pull/25793)

> 📜 **No stray scrollbar on the About page.** Extra spacing that caused an unnecessary scrollbar on the About settings page has been removed. [#25802](https://github.com/open-webui/open-webui/pull/25802)

> ➗ **Large math expressions no longer crash rendering.** Parsing math delimiters no longer overflows on very large or deeply nested input, so messages with heavy math render instead of failing. [#25845](https://github.com/open-webui/open-webui/pull/25845)

> 📜 **Visible chat scrollbar.** The chat area now shows a scrollbar, making it easier to scroll through long responses. [Commit](https://github.com/open-webui/open-webui/commit/d56e1cb0b9), [#25833](https://github.com/open-webui/open-webui/issues/25833)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-29-5-files-and-data-changes-in-v0-10-0|5 Files and Data changes in v0.10.0]] · Files and Data
- [[Changes/Open WebUI/2026-06-29-5-memory-and-personalization-changes-in-v0-10-0|5 Memory and Personalization changes in v0.10.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-29-3-voice-and-audio-changes-in-v0-10-0|3 Voice and Audio changes in v0.10.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-29-4-collaboration-changes-in-v0-10-0|4 Collaboration changes in v0.10.0]] · Collaboration
- [[Changes/Open WebUI/2026-06-29-client-user-agent-forwarded-to-model-backends-the-browser-s-user-agent-is-now-pa|🪪 Client User-Agent forwarded to model backends. The browser's User-Agent is now…]] · Agent Mode
- [[Changes/Open WebUI/2026-06-29-scim-sync-can-t-demote-an-admin-a-scim-provisioning-sync-that-marks-a-user-inact|🛟 SCIM sync can't demote an admin. A SCIM provisioning sync that marks a user…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-29-8-search-and-browsing-changes-in-v0-10-0|8 Search and Browsing changes in v0.10.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-29-25-model-support-changes-in-v0-10-0|25 Model Support changes in v0.10.0]] · Model Support
- [[Changes/Open WebUI/2026-06-29-6-reliability-and-performance-changes-in-v0-10-0|6 Reliability and Performance changes in v0.10.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-29-4-mobile-and-desktop-changes-in-v0-10-0|4 Mobile and Desktop changes in v0.10.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-29-better-screen-reader-labels-on-toggles-integration-and-switch-toggles-now-expose|♿ Better screen-reader labels on toggles. Integration and switch toggles now…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-29-16-safety-and-privacy-changes-in-v0-10-0|16 Safety and Privacy changes in v0.10.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-29-2-pricing-model-changes-in-v0-10-0|2 Pricing Model changes in v0.10.0]] · Pricing Model
- [[Changes/Open WebUI/2026-06-29-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-29-9-account-and-access-changes-in-v0-10-0|9 Account and Access changes in v0.10.0]] · Account and Access
- [[Changes/Open WebUI/2026-06-29-usable-chat-input-on-mobile-with-many-tools-when-skills-tools-terminal-web-searc|📱 Usable chat input on mobile with many tools. When skills, tools, terminal, web…]] · Image Generation
- [[Changes/Open WebUI/2026-06-29-6-automation-and-scheduling-changes-in-v0-10-0|6 Automation and Scheduling changes in v0.10.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-29-3-context-window-changes-in-v0-10-0|3 Context Window changes in v0.10.0]] · Context Window
- [[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer Workflow changes in v0.10.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-29-10-editor-experience-changes-in-v0-10-0|10 Editor Experience changes in v0.10.0]] · Editor Experience
- [[Changes/Open WebUI/2026-06-29-29-other-changes-in-v0-10-0|29 other changes in v0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-06-29 · Kimi Code · [[Changes/Kimi Code/2026-06-29-2-interface-experience-changes-in-kimi-code-0-20-2|2 Interface Experience changes in Kimi Code 0.20.2]]
- Later: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-3-interface-experience-changes-in-v1-0-66|3 Interface Experience changes in v1.0.66]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-0c6101&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-14-interface-experience-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-0c6101%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->