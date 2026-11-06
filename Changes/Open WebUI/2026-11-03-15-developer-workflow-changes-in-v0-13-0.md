---
card_id: open-webui-2026-11-03-9d5604
date: '2026-11-03'
description: 'Open WebUI · 2026-11-03 · Developer Workflow: 15 changes in v0.13.0
  — ⚡ **Live terminal updates.** On terminals that support it, the Git panel, the
  list of…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1326
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8da6c98e0e673b5c5d59c0ca372591b88c7f46c9ca6e7a5e1b76d95e0d357518
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-11-03-9d5604
  comparison: ''
  date: '2026-11-03'
  description: 'Open WebUI — v0.13.0: 15 Developer Workflow changes'
  evidence:
  - quote: ⚡ **Live terminal updates.** On terminals that support it, the Git panel,
      the list of open ports and the running processes and their output now update
      as soon as something changes instead of every few seconds. [Commit](https://github.com/open-webui/open-webui/commit/c4c10aa2559e10883797e3dd6702e16dc36eff19),
      [Commit](https://github.com/open-webui/open-webui/commit/70c5e38fc7ce3864426b484c07ee201cba2b9d07)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F4AC **Comment threads.** Administrators can now turn on Comments
      in Admin Settings > General or with \"ENABLE_COMMENTS\", which lets users leave
      comments with replies, reactions and mentions on the chats, notes, models, knowledge
      bases, prompts, skills and tools they can open, including on a selected passage
      of a chat message, which then stays highlighted in the reply, or of a note page,
      shown in a Comments tab in the chat's side panel, which \"/comments\" opens,
      and with comment counts in the workspace lists. [Commit](https://github.com/open-webui/open-webui/commit/9d1b4ef362f103f2dda05760a44c96df82c064fd),
      [Commit](https://github.com/open-webui/open-webui/commit/91e8deee74c627fee29c4c81833766040334170f),
      [Commit](https://github.com/open-webui/open-webui/commit/63312766f8de94bc8a054d7923f2f83410b841a2),
      [Commit](https://github.com/open-webui/open-webui/commit/04d78a483de671dbe789082b79638f9e44078819)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F4D0 **Side panels on tablets.** On screens from 768 pixels wide,
      such as tablets and narrow windows, channel threads and the pages list and chat
      in notes now open beside the content instead of over it, picking a terminal
      opens its files beside the chat as well, and the search dialog shows its preview
      there by default and remembers whether you turned it on or off at any window
      size. [Commit](https://github.com/open-webui/open-webui/commit/cbeb8e3630cafd7ef6fd28b552bf7114729f21b9),
      [Commit](https://github.com/open-webui/open-webui/commit/c5981aaea6b25bb9b9601e62b9ff75da33aaaf4e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F4CA **More PowerPoint charts.** The PowerPoint preview now draws
      pie, doughnut and horizontal bar charts as well as values below zero, and shows
      \"Chart preview unavailable\" for charts it cannot draw. [Commit](https://github.com/open-webui/open-webui/commit/09fbbd6d69293084d9e09cbb7d3b93e5d305ec5c),
      [#32884](https://github.com/open-webui/open-webui/issues/32884)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F9CA **3D model previews.** GLB, glTF, STL, OBJ and PLY files in
      a terminal's file browser and in files shown in chat replies now open in a 3D
      viewer that you can rotate and zoom. [Commit](https://github.com/open-webui/open-webui/commit/fe0d22cc24ddc2421b4e36a66a174188cc61d265)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F4CF **Knowledge base file limits.** Administrators can now cap
      how many files a knowledge base holds, how large each of its files may be and
      how many files go into it in one upload, for all knowledge bases in Admin Settings
      > Documents or with \"KNOWLEDGE_MAX_FILE_COUNT\", \"KNOWLEDGE_MAX_FILE_SIZE\"
      and \"KNOWLEDGE_MAX_UPLOAD_COUNT\", and a knowledge base's owner can set its
      own file count and size limits under Advanced when creating it or from Settings
      in its menu, while the global limits always apply. [Commit](https://github.com/open-webui/open-webui/commit/7618df3f53a8db2ad5352a789c88673a736b07a4),
      [Commit](https://github.com/open-webui/open-webui/commit/5c4fb61d862b011cf9efda6b2289de637ba8d6bb),
      [#33318](https://github.com/open-webui/open-webui/issues/33318), [#24845](https://github.com/open-webui/open-webui/discussions/24845)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F4C4 **File sizes in previews.** Opened terminal files now show
      their size in the file toolbar, so you can check a document or generated output
      without leaving its preview. [Commit](https://github.com/open-webui/open-webui/commit/2e55c365645e538c54b0d31b7bc8a977f6bb8b85)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F5C2️ **Sort files by date added.** The terminal file browser can
      now sort files by when they were added, next to name, size and date modified,
      on terminals that report creation times. [Commit](https://github.com/open-webui/open-webui/commit/8c308e4e88c48924209f0018d73beb82a4ba2d94)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: ↕️ **Move blocks in notes.** Every paragraph, heading and other block in
      a note now has a handle beside it that you can drag to move the block, or click
      to move it up or down. [Commit](https://github.com/open-webui/open-webui/commit/3bb962f2bbd82ebe8ccad6f64304956aee2f4f97)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F4CB **Copy code in notes.** Code blocks in notes now have a Copy
      button and use clearer syntax colors in light mode. [Commit](https://github.com/open-webui/open-webui/commit/ab71357980dab80de23b3597a13a41557a11df99),
      [Commit](https://github.com/open-webui/open-webui/commit/ee8b69e718aa7f0b962309e0137aa81f557093eb),
      [#33455](https://github.com/open-webui/open-webui/issues/33455)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001FA9F **Thread message actions visible.** Hovering the top message
      in a channel thread now shows its whole actions toolbar instead of cutting off
      its top half at the edge of the panel. [Commit](https://github.com/open-webui/open-webui/commit/08f197ad8d87b4f71be311888541c601942e96b9),
      [#33472](https://github.com/open-webui/open-webui/issues/33472)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F4F6 **Temporary chats after reconnecting.** A reply that is still
      being written in a temporary chat now keeps arriving after the connection drops
      and comes back, and a reply that could not finish shows \"Connection lost. Please
      retry.\" instead of loading forever. [Commit](https://github.com/open-webui/open-webui/commit/321701c1af09d58f9ed6b67a22416ab8ddcfa165)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F600 **Channel reaction names.** Hovering a reaction on a channel
      message now shows who reacted when those names are available, instead of showing
      only the count. [Commit](https://github.com/open-webui/open-webui/commit/ea1c60fbdf3cfc08ddf4128ab33007380228e86c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F39B️ **Controls in the model menu.** The chat files, valves, system
      prompt and advanced parameters moved from the Controls panel at the top of the
      chat to Controls in the model controls menu next to the message input, and the
      button at the top now opens the tabbed side panel. [Commit](https://github.com/open-webui/open-webui/commit/2d7cf5ec99c3fa5c7ee48b91823fb8021b846cf3),
      [Commit](https://github.com/open-webui/open-webui/commit/950da84bdb57423d9d2ddd6d29659d56174d8c22)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F4ED **File processing alerts removed.** Personal notifications
      in Settings > Notifications no longer offer \"Retrieval Content process failed\",
      so notification webhooks no longer receive an alert when a file fails to process.
      [Commit](https://github.com/open-webui/open-webui/commit/3814b7b2f152c671fd3789e5a0099313d5316467)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 15-developer-workflow-changes-in-v0-13-0
  source_release: open-webui-2026-11-03-v0-13-0-github-432661497-44290c10
  source_type: github_releases
  theme: developer-workflow
  title: 15 Developer Workflow changes in v0.13.0
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-10-29-35-developer-workflow-changes-in-v0-12-5|35 Developer
  Workflow changes in v0.12.5]]'
- '[[Changes/Claude Code/2026-10-30-4-developer-workflow-changes-in-v2-1-314|4 Developer
  Workflow changes in v2.1.314]]'
- '[[Changes/Claude Code/2026-10-31-2-developer-workflow-changes-in-v2-1-316|2 Developer
  Workflow changes in v2.1.316]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-11-03-v0-13-0-github-432661497-44290c10|open-webui-2026-11-03-v0-13-0-github-432661497-44290c10]]'
source_type: github_releases
theme: developer-workflow
title: 15 Developer Workflow changes in v0.13.0
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Developer Workflow changes in v0.13.0

**Open WebUI** · 2026-11-03 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.13.0) · from [[Releases/Open WebUI/open-webui-2026-11-03-v0-13-0-github-432661497-44290c10|v0.13.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ⚡ **Live terminal updates.** On terminals that support it, the Git panel, the list of open ports and the running processes and their output now update as soon as something changes instead of every few seconds. [Commit](https://github.com/open-webui/open-webui/commit/c4c10aa2559e10883797e3dd6702e16dc36eff19), [Commit](https://github.com/open-webui/open-webui/commit/70c5e38fc7ce3864426b484c07ee201cba2b9d07)

> 💬 **Comment threads.** Administrators can now turn on Comments in Admin Settings > General or with "ENABLE_COMMENTS", which lets users leave comments with replies, reactions and mentions on the chats, notes, models, knowledge bases, prompts, skills and tools they can open, including on a selected passage of a chat message, which then stays highlighted in the reply, or of a note page, shown in a Comments tab in the chat's side panel, which "/comments" opens, and with comment counts in the workspace lists. [Commit](https://github.com/open-webui/open-webui/commit/9d1b4ef362f103f2dda05760a44c96df82c064fd), [Commit](https://github.com/open-webui/open-webui/commit/91e8deee74c627fee29c4c81833766040334170f), [Commit](https://github.com/open-webui/open-webui/commit/63312766f8de94bc8a054d7923f2f83410b841a2), [Commit](https://github.com/open-webui/open-webui/commit/04d78a483de671dbe789082b79638f9e44078819)

> 📐 **Side panels on tablets.** On screens from 768 pixels wide, such as tablets and narrow windows, channel threads and the pages list and chat in notes now open beside the content instead of over it, picking a terminal opens its files beside the chat as well, and the search dialog shows its preview there by default and remembers whether you turned it on or off at any window size. [Commit](https://github.com/open-webui/open-webui/commit/cbeb8e3630cafd7ef6fd28b552bf7114729f21b9), [Commit](https://github.com/open-webui/open-webui/commit/c5981aaea6b25bb9b9601e62b9ff75da33aaaf4e)

> 📊 **More PowerPoint charts.** The PowerPoint preview now draws pie, doughnut and horizontal bar charts as well as values below zero, and shows "Chart preview unavailable" for charts it cannot draw. [Commit](https://github.com/open-webui/open-webui/commit/09fbbd6d69293084d9e09cbb7d3b93e5d305ec5c), [#32884](https://github.com/open-webui/open-webui/issues/32884)

> 🧊 **3D model previews.** GLB, glTF, STL, OBJ and PLY files in a terminal's file browser and in files shown in chat replies now open in a 3D viewer that you can rotate and zoom. [Commit](https://github.com/open-webui/open-webui/commit/fe0d22cc24ddc2421b4e36a66a174188cc61d265)

> 📏 **Knowledge base file limits.** Administrators can now cap how many files a knowledge base holds, how large each of its files may be and how many files go into it in one upload, for all knowledge bases in Admin Settings > Documents or with "KNOWLEDGE_MAX_FILE_COUNT", "KNOWLEDGE_MAX_FILE_SIZE" and "KNOWLEDGE_MAX_UPLOAD_COUNT", and a knowledge base's owner can set its own file count and size limits under Advanced when creating it or from Settings in its menu, while the global limits always apply. [Commit](https://github.com/open-webui/open-webui/commit/7618df3f53a8db2ad5352a789c88673a736b07a4), [Commit](https://github.com/open-webui/open-webui/commit/5c4fb61d862b011cf9efda6b2289de637ba8d6bb), [#33318](https://github.com/open-webui/open-webui/issues/33318), [#24845](https://github.com/open-webui/open-webui/discussions/24845)

> 📄 **File sizes in previews.** Opened terminal files now show their size in the file toolbar, so you can check a document or generated output without leaving its preview. [Commit](https://github.com/open-webui/open-webui/commit/2e55c365645e538c54b0d31b7bc8a977f6bb8b85)

> 🗂️ **Sort files by date added.** The terminal file browser can now sort files by when they were added, next to name, size and date modified, on terminals that report creation times. [Commit](https://github.com/open-webui/open-webui/commit/8c308e4e88c48924209f0018d73beb82a4ba2d94)

> ↕️ **Move blocks in notes.** Every paragraph, heading and other block in a note now has a handle beside it that you can drag to move the block, or click to move it up or down. [Commit](https://github.com/open-webui/open-webui/commit/3bb962f2bbd82ebe8ccad6f64304956aee2f4f97)

> 📋 **Copy code in notes.** Code blocks in notes now have a Copy button and use clearer syntax colors in light mode. [Commit](https://github.com/open-webui/open-webui/commit/ab71357980dab80de23b3597a13a41557a11df99), [Commit](https://github.com/open-webui/open-webui/commit/ee8b69e718aa7f0b962309e0137aa81f557093eb), [#33455](https://github.com/open-webui/open-webui/issues/33455)

> 🪟 **Thread message actions visible.** Hovering the top message in a channel thread now shows its whole actions toolbar instead of cutting off its top half at the edge of the panel. [Commit](https://github.com/open-webui/open-webui/commit/08f197ad8d87b4f71be311888541c601942e96b9), [#33472](https://github.com/open-webui/open-webui/issues/33472)

> 📶 **Temporary chats after reconnecting.** A reply that is still being written in a temporary chat now keeps arriving after the connection drops and comes back, and a reply that could not finish shows "Connection lost. Please retry." instead of loading forever. [Commit](https://github.com/open-webui/open-webui/commit/321701c1af09d58f9ed6b67a22416ab8ddcfa165)

> 😀 **Channel reaction names.** Hovering a reaction on a channel message now shows who reacted when those names are available, instead of showing only the count. [Commit](https://github.com/open-webui/open-webui/commit/ea1c60fbdf3cfc08ddf4128ab33007380228e86c)

> 🎛️ **Controls in the model menu.** The chat files, valves, system prompt and advanced parameters moved from the Controls panel at the top of the chat to Controls in the model controls menu next to the message input, and the button at the top now opens the tabbed side panel. [Commit](https://github.com/open-webui/open-webui/commit/2d7cf5ec99c3fa5c7ee48b91823fb8021b846cf3), [Commit](https://github.com/open-webui/open-webui/commit/950da84bdb57423d9d2ddd6d29659d56174d8c22)

> 📭 **File processing alerts removed.** Personal notifications in Settings > Notifications no longer offer "Retrieval Content process failed", so notification webhooks no longer receive an alert when a file fails to process. [Commit](https://github.com/open-webui/open-webui/commit/3814b7b2f152c671fd3789e5a0099313d5316467)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-11-03-context-compaction-and-prompt-caching-when-the-same-model-handles-the-conversati|🧠 Context compaction and prompt caching. When the same model handles…]] · Pricing Model
- [[Changes/Open WebUI/2026-11-03-mcp-apps-in-chat-tools-from-mcp-servers-that-come-with-an-interactive-app-now-sh|🧩 MCP Apps in chat. Tools from MCP servers that come with an interactive app now…]] · Apps and Integrations
- [[Changes/Open WebUI/2026-11-03-4-model-support-changes-in-v0-13-0|4 Model Support changes in v0.13.0]] · Model Support
- [[Changes/Open WebUI/2026-11-03-new-chats-stay-in-sync-a-chat-started-from-the-home-page-keeps-syncing-with-the|🔃 New chats stay in sync. A chat started from the home page keeps syncing…]] · Collaboration
- [[Changes/Open WebUI/2026-11-03-4-voice-and-audio-changes-in-v0-13-0|4 Voice and Audio changes in v0.13.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-11-03-4-editor-experience-changes-in-v0-13-0|4 Editor Experience changes in v0.13.0]] · Editor Experience
- [[Changes/Open WebUI/2026-11-03-nested-code-previews-preview-now-opens-code-blocks-inside-lists-quotes-and-detai|🧩 Nested code previews. Preview now opens code blocks inside lists, quotes…]] · Artifact Creation
- [[Changes/Open WebUI/2026-11-03-live-context-usage-estimates-the-context-indicator-now-accounts-for-output-arriv|📏 Live context usage estimates. The context indicator now accounts for output…]] · Context Window
- [[Changes/Open WebUI/2026-11-03-2-automation-and-scheduling-changes-in-v0-13-0|2 Automation and Scheduling changes in v0.13.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-11-03-2-search-and-browsing-changes-in-v0-13-0|2 Search and Browsing changes in v0.13.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-11-03-image-drops-from-photo-apps-images-dropped-into-chats-and-channels-are-now-recog|🖼️ Image drops from photo apps. Images dropped into chats and channels are now…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-11-03-saved-oauth-provider-settings-oauth-providers-now-load-their-saved-connection-se|🔑 Saved OAuth provider settings. OAuth providers now load their saved connection…]] · Account and Access
- [[Changes/Open WebUI/2026-11-03-4-interface-experience-changes-in-v0-13-0|4 Interface Experience changes in v0.13.0]] · Interface Experience
- [[Changes/Open WebUI/2026-11-03-accessibility-improvements-screen-reader-users-now-hear-a-name-for-every-window|♿ Accessibility improvements. Screen reader users now hear a name for every…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-11-03-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-11-03-2-safety-and-privacy-changes-in-v0-13-0|2 Safety and Privacy changes in v0.13.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-11-03-no-sub-agent-limits-by-default-the-sub-agent-limits-in-admin-settings-and-throug|🔓 No sub-agent limits by default. The sub-agent limits in Admin Settings…]] · Agent Mode
- [[Changes/Open WebUI/2026-11-03-5-other-changes-in-v0-13-0|5 other changes in v0.13.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-10-31 · Claude Code · [[Changes/Claude Code/2026-10-31-2-developer-workflow-changes-in-v2-1-316|2 Developer Workflow changes in v2.1.316]]
- Later: 2026-11-04 · Dify · [[Changes/Dify/2026-11-04-2-developer-workflow-changes-in-1-19-0|2 Developer Workflow changes in 1.19.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-11-03-9d5604&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-11-03-15-developer-workflow-changes-in-v0-13-0.md%0ACard%20ID%3A%20open-webui-2026-11-03-9d5604%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.13.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->