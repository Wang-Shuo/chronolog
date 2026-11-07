---
card_id: open-webui-2026-03-25-c97f9f
date: '2026-03-25'
description: "Open WebUI · 2026-03-25 · Interface Experience: 17 changes in v0.8.11
  — \U0001F4C1 **Chat folder emoji reset.** Users can now reset chat folder emojis
  back to the…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2537
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b0474fe8b1a22260fd8e17d65f718f00f7014bd301178d2eac86d5753bd75e4a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-25-c97f9f
  comparison: ''
  date: '2026-03-25'
  description: 'Open WebUI — v0.8.11: 17 Interface Experience changes'
  evidence:
  - quote: "\U0001F4C1 **Chat folder emoji reset.** Users can now reset chat folder
      emojis back to the default icon using a \"Reset to Default\" button in the emoji
      picker, making it easier to revert custom icons. [#22554](https://github.com/open-webui/open-webui/pull/22554)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4E1 **Terminal port previews.** Detected ports in the File Navigator
      can now be previewed inline with a browser-style view, navigation controls,
      and an address bar, instead of only opening in a new tab. [Commit](https://github.com/open-webui/open-webui/commit/689061822173e561a153290b2bb816f4cb6f4959),
      [Commit](https://github.com/open-webui/open-webui/commit/1dc647f43b1929f5c4d1af393a90a47f56cb745e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F9ED **File Navigator navigation history.** The File Navigator toolbar
      now includes Back and Forward buttons for navigating through folder and file
      history, similar to a web browser. [Commit](https://github.com/open-webui/open-webui/commit/3a4b862e818c69fff6f3a3c67b50c51aa00c03e9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4C2 **Files list pagination.** The files list API now supports
      pagination, returning paginated results with a total count for easier navigation
      through large file collections. [Commit](https://github.com/open-webui/open-webui/commit/f9756de693a93e918c037d757afddb7defc847e4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F6A9 **Drag chats as references.** Users can now drag chats from
      the sidebar and drop them into the message input to add them as Reference Chats.
      [Commit](https://github.com/open-webui/open-webui/commit/ebb7ce2092efc8d78da4974623647dbd18b6e372)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F9FD **Duplicate chat list refresh.** Sending messages no longer
      triggers duplicate sidebar chat list refreshes, eliminating an unnecessary database
      query that was already handled by the save and completion handlers. [#22982](https://github.com/open-webui/open-webui/pull/22982)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F9F9 **Chat history save optimization.** The chat list is no longer
      refreshed on every chat history save, branch navigation, or edit — only on meaningful
      state changes like new chat creation, title generation, and response completion.
      [#22983](https://github.com/open-webui/open-webui/pull/22983)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4DD **Input variables modal crash.** Fixed a crash that occurred
      when selecting custom prompts with prompt variables, causing the Input Variables
      modal to display an infinite loading spinner instead of the variable input fields.
      [#22748](https://github.com/open-webui/open-webui/issues/22748), [Commit](https://github.com/open-webui/open-webui/commit/0dcd6ac983bede06b8477179192154467f5b24a2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F5C2️ **Sidebar chat menu closure.** Sidebar chat dropdown menus
      now close properly after clicking \"Clone\", \"Share\", \"Download\", \"Rename\",
      \"Pin\", \"Move\", \"Archive\", or \"Delete\", instead of remaining visible.
      [#22884](https://github.com/open-webui/open-webui/pull/22884), [#22784](https://github.com/open-webui/open-webui/issues/22784)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F6A9 **User menu navigation fix.** Clicking Playground or Admin
      Panel from the user menu now uses client-side routing instead of causing full
      page reloads, restoring smooth SPA navigation. [Commit](https://github.com/open-webui/open-webui/commit/7ffcd3908ee90f88a4c4684d6cd6e75efd117461)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F9F9 **Channel thread sidebar cleanup.** The thread sidebar in channels
      and direct messages now automatically closes when the parent message is deleted,
      preventing orphaned threads. [#22890](https://github.com/open-webui/open-webui/pull/22890)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F465 **User groups display.** User groups in the admin panel profile
      preview now wrap properly instead of overflowing horizontally, with a scrollbar
      when the list is long. [#22547](https://github.com/open-webui/open-webui/pull/22547)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F532 **Markdown task list checkbox styling.** Fixed task list checkboxes
      in markdown rendering to display consistently without shrinking in narrow layouts.
      [#22886](https://github.com/open-webui/open-webui/pull/22886)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F3A8 **Artifacts sidebar tab background fix.** The Artifacts sidebar
      now correctly updates and displays when switching back to a browser tab that
      was in the background, ensuring artifacts are visible without requiring a manual
      refresh. [#22889](https://github.com/open-webui/open-webui/issues/22889)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4CA **Channel message data loading.** Fixed redundant 404 API calls
      that occurred when rendering channel messages, preventing unnecessary requests
      and console errors. [#22894](https://github.com/open-webui/open-webui/pull/22894)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F9E0 **Reasoning spinner content preservation.** Prior assistant
      content and tool call blocks no longer disappear during the reasoning spinner
      when responding after tool execution. [#23001](https://github.com/open-webui/open-webui/pull/23001)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F5B1️ **Dropdown submenu hover stability.** Secondary hover menus
      like Download and Move now remain open while navigating into them, fixing an
      issue where an 8px gap between the trigger and submenu would cause the menu
      to disappear before a selection could be made. [#22744](https://github.com/open-webui/open-webui/issues/22744),
      [Commit](https://github.com/open-webui/open-webui/commit/cffbc3558e911abd6c4780cd028794b2f7282cd7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 17-interface-experience-changes-in-v0-8-11
  source_release: open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69
  source_type: github_releases
  theme: interface-experience
  title: 17 Interface Experience changes in v0.8.11
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-25-2-interface-experience-changes-in-v2-1-83|2 Interface
  Experience changes in v2.1.83]]'
- '[[Changes/Gamma/2026-03-25-gamma-has-supported-code-blocks-for-a-while-but-the-code-inside-them-was-just-pl|Syntax
  highlighting for code blocks]]'
- '[[Changes/Google Antigravity/2026-03-25-improved-sidebar-design|Improved sidebar
  design]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69]]'
source_type: github_releases
theme: interface-experience
title: 17 Interface Experience changes in v0.8.11
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Interface Experience changes in v0.8.11

**Open WebUI** · 2026-03-25 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.11) · from [[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|v0.8.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📁 **Chat folder emoji reset.** Users can now reset chat folder emojis back to the default icon using a "Reset to Default" button in the emoji picker, making it easier to revert custom icons. [#22554](https://github.com/open-webui/open-webui/pull/22554)

> 📡 **Terminal port previews.** Detected ports in the File Navigator can now be previewed inline with a browser-style view, navigation controls, and an address bar, instead of only opening in a new tab. [Commit](https://github.com/open-webui/open-webui/commit/689061822173e561a153290b2bb816f4cb6f4959), [Commit](https://github.com/open-webui/open-webui/commit/1dc647f43b1929f5c4d1af393a90a47f56cb745e)

> 🧭 **File Navigator navigation history.** The File Navigator toolbar now includes Back and Forward buttons for navigating through folder and file history, similar to a web browser. [Commit](https://github.com/open-webui/open-webui/commit/3a4b862e818c69fff6f3a3c67b50c51aa00c03e9)

> 📂 **Files list pagination.** The files list API now supports pagination, returning paginated results with a total count for easier navigation through large file collections. [Commit](https://github.com/open-webui/open-webui/commit/f9756de693a93e918c037d757afddb7defc847e4)

> 🚩 **Drag chats as references.** Users can now drag chats from the sidebar and drop them into the message input to add them as Reference Chats. [Commit](https://github.com/open-webui/open-webui/commit/ebb7ce2092efc8d78da4974623647dbd18b6e372)

> 🧽 **Duplicate chat list refresh.** Sending messages no longer triggers duplicate sidebar chat list refreshes, eliminating an unnecessary database query that was already handled by the save and completion handlers. [#22982](https://github.com/open-webui/open-webui/pull/22982)

> 🧹 **Chat history save optimization.** The chat list is no longer refreshed on every chat history save, branch navigation, or edit — only on meaningful state changes like new chat creation, title generation, and response completion. [#22983](https://github.com/open-webui/open-webui/pull/22983)

> 📝 **Input variables modal crash.** Fixed a crash that occurred when selecting custom prompts with prompt variables, causing the Input Variables modal to display an infinite loading spinner instead of the variable input fields. [#22748](https://github.com/open-webui/open-webui/issues/22748), [Commit](https://github.com/open-webui/open-webui/commit/0dcd6ac983bede06b8477179192154467f5b24a2)

> 🗂️ **Sidebar chat menu closure.** Sidebar chat dropdown menus now close properly after clicking "Clone", "Share", "Download", "Rename", "Pin", "Move", "Archive", or "Delete", instead of remaining visible. [#22884](https://github.com/open-webui/open-webui/pull/22884), [#22784](https://github.com/open-webui/open-webui/issues/22784)

> 🚩 **User menu navigation fix.** Clicking Playground or Admin Panel from the user menu now uses client-side routing instead of causing full page reloads, restoring smooth SPA navigation. [Commit](https://github.com/open-webui/open-webui/commit/7ffcd3908ee90f88a4c4684d6cd6e75efd117461)

> 🧹 **Channel thread sidebar cleanup.** The thread sidebar in channels and direct messages now automatically closes when the parent message is deleted, preventing orphaned threads. [#22890](https://github.com/open-webui/open-webui/pull/22890)

> 👥 **User groups display.** User groups in the admin panel profile preview now wrap properly instead of overflowing horizontally, with a scrollbar when the list is long. [#22547](https://github.com/open-webui/open-webui/pull/22547)

> 🔲 **Markdown task list checkbox styling.** Fixed task list checkboxes in markdown rendering to display consistently without shrinking in narrow layouts. [#22886](https://github.com/open-webui/open-webui/pull/22886)

> 🎨 **Artifacts sidebar tab background fix.** The Artifacts sidebar now correctly updates and displays when switching back to a browser tab that was in the background, ensuring artifacts are visible without requiring a manual refresh. [#22889](https://github.com/open-webui/open-webui/issues/22889)

> 📊 **Channel message data loading.** Fixed redundant 404 API calls that occurred when rendering channel messages, preventing unnecessary requests and console errors. [#22894](https://github.com/open-webui/open-webui/pull/22894)

> 🧠 **Reasoning spinner content preservation.** Prior assistant content and tool call blocks no longer disappear during the reasoning spinner when responding after tool execution. [#23001](https://github.com/open-webui/open-webui/pull/23001)

> 🖱️ **Dropdown submenu hover stability.** Secondary hover menus like Download and Move now remain open while navigating into them, fixing an issue where an 8px gap between the trigger and submenu would cause the menu to disappear before a selection could be made. [#22744](https://github.com/open-webui/open-webui/issues/22744), [Commit](https://github.com/open-webui/open-webui/commit/cffbc3558e911abd6c4780cd028794b2f7282cd7)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-25-4-editor-experience-changes-in-v0-8-11|4 Editor Experience changes in v0.8.11]] · Editor Experience
- [[Changes/Open WebUI/2026-03-25-rag-query-generation-robustness-the-rag-query-generation-web-search-and-image-ge|🔍 RAG query generation robustness. The RAG query generation, web search…]] · Image Generation
- [[Changes/Open WebUI/2026-03-25-shared-chat-viewing-crash-shared-chats-can-now-be-viewed-by-unauthenticated-user|🐛 Shared chat viewing crash. Shared chats can now be viewed by unauthenticated…]] · Collaboration
- [[Changes/Open WebUI/2026-03-25-11-account-and-access-changes-in-v0-8-11|11 Account and Access changes in v0.8.11]] · Account and Access
- [[Changes/Open WebUI/2026-03-25-3-context-window-changes-in-v0-8-11|3 Context Window changes in v0.8.11]] · Context Window
- [[Changes/Open WebUI/2026-03-25-2-search-and-browsing-changes-in-v0-8-11|2 Search and Browsing changes in v0.8.11]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-25-2-files-and-data-changes-in-v0-8-11|2 Files and Data changes in v0.8.11]] · Files and Data
- [[Changes/Open WebUI/2026-03-25-4-memory-and-personalization-changes-in-v0-8-11|4 Memory and Personalization changes in v0.8.11]] · Memory and Personalization
- [[Changes/Open WebUI/2026-03-25-3-apps-and-integrations-changes-in-v0-8-11|3 Apps and Integrations changes in v0.8.11]] · Apps and Integrations
- [[Changes/Open WebUI/2026-03-25-5-reliability-and-performance-changes-in-v0-8-11|5 Reliability and Performance changes in v0.8.11]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-25-tool-binary-response-handling-tool-servers-can-now-return-binary-data-such-as-im|🏮 Tool binary response handling. Tool servers can now return binary data such…]] · Multimodal Input
- [[Changes/Open WebUI/2026-03-25-23-model-support-changes-in-v0-8-11|23 Model Support changes in v0.8.11]] · Model Support
- [[Changes/Open WebUI/2026-03-25-4-safety-and-privacy-changes-in-v0-8-11|4 Safety and Privacy changes in v0.8.11]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-25-34-developer-workflow-changes-in-v0-8-11|34 Developer Workflow changes in v0.8.11]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-25-metrics-export-interval-configuration-administrators-can-now-control-opentelemet|📊 Metrics export interval configuration. Administrators can now control…]] · Pricing Model
- [[Changes/Open WebUI/2026-03-25-19-other-changes-in-v0-8-11|19 other changes in v0.8.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-03-25 · Google Antigravity · [[Changes/Google Antigravity/2026-03-25-improved-sidebar-design|Improved sidebar design]]
- Later: 2026-03-26 · ChatGPT · [[Changes/ChatGPT/2026-03-26-to-give-you-more-space-to-view-your-most-critical-chats-and-projects-the-sidebar|A simplified sidebar on mobile]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-25-c97f9f&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-25-17-interface-experience-changes-in-v0-8-11.md%0ACard%20ID%3A%20open-webui-2026-03-25-c97f9f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->