---
card_id: open-webui-2026-11-03-32a61b
date: '2026-11-03'
description: "Open WebUI · 2026-11-03 · Model Support: 4 changes in v0.13.0 — \U0001F4BB
  **Open WebUI Desktop 0.1.x.** The separately installed app for macOS, Windows and
  Linux now…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1394
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 42d83fbcd0abe3880223b55a6974f9863110f0dd06fb5c1769e5ac62ae6451c6
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-11-03-32a61b
  comparison: ''
  date: '2026-11-03'
  description: 'Open WebUI — v0.13.0: 4 Model Support changes'
  evidence:
  - quote: "\U0001F4BB **Open WebUI Desktop 0.1.x.** The separately installed app
      for macOS, Windows and Linux now focuses on setting up and running Open WebUI
      on your own computer, with optional llama.cpp local models. The 0.1.0–0.1.4
      updates bring a slimmer interface, searchable settings, startup logs, optional
      automatic Desktop updates, start-to-tray controls and image copying and saving.
      They also improve screen sharing, knowledge folder uploads, Linux graphics and
      shortcuts, and NVIDIA/AMD local-model setup and updates. Use it for a managed
      local installation and local AI workflows. [Desktop changelog](https://github.com/open-webui/desktop/blob/v0.1.4/CHANGELOG.md),
      [Download v0.1.4](https://github.com/open-webui/desktop/releases/tag/v0.1.4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F6E0️ **Tool creation from chat.** Models with native function calling
      can now create a private Python tool in your workspace when you ask them to,
      for administrators and users allowed to create workspace tools, and it can be
      turned off per model under Tool Creation in the model editor's builtin tools.
      [Commit](https://github.com/open-webui/open-webui/commit/91241306e2541e984591435d8c25e9ab1442db6b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F4C2 **Temporary Chat on folder pages.** Turning Temporary Chat
      on or off on a folder's page, with the button at the top or with \"/temporary\",
      now keeps you on the folder page, so the next chat is still saved in the folder
      and gets its system prompt, default model and knowledge. [#33456](https://github.com/open-webui/open-webui/pull/33456),
      [#33448](https://github.com/open-webui/open-webui/issues/33448)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F3E0 **New chat initialization.** Opening or reloading the home
      page or a folder now selects the model and applies chat URL parameters again,
      instead of leaving the model empty and ignoring the link’s settings. [Commit](https://github.com/open-webui/open-webui/commit/082df44d92178b6895153774bf6656c538cbce40)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-model-support-changes-in-v0-13-0
  source_release: open-webui-2026-11-03-v0-13-0-github-432661497-44290c10
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in v0.13.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-11-02-7-model-support-changes-in-elevenlabs-updates-2026-11-02|7
  Model Support changes in ElevenLabs updates — 2026-11-02]]'
- '[[Changes/Ollama/2026-11-03-2-model-support-changes-in-v0-40-15|2 Model Support
  changes in v0.40.15]]'
- '[[Changes/Ollama/2026-11-03-2-model-support-changes-in-v0-40-14|2 Model Support
  changes in v0.40.14]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-11-03-v0-13-0-github-432661497-44290c10|open-webui-2026-11-03-v0-13-0-github-432661497-44290c10]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in v0.13.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v0.13.0

**Open WebUI** · 2026-11-03 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.13.0) · from [[Releases/Open WebUI/open-webui-2026-11-03-v0-13-0-github-432661497-44290c10|v0.13.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 💻 **Open WebUI Desktop 0.1.x.** The separately installed app for macOS, Windows and Linux now focuses on setting up and running Open WebUI on your own computer, with optional llama.cpp local models. The 0.1.0–0.1.4 updates bring a slimmer interface, searchable settings, startup logs, optional automatic Desktop updates, start-to-tray controls and image copying and saving. They also improve screen sharing, knowledge folder uploads, Linux graphics and shortcuts, and NVIDIA/AMD local-model setup and updates. Use it for a managed local installation and local AI workflows. [Desktop changelog](https://github.com/open-webui/desktop/blob/v0.1.4/CHANGELOG.md), [Download v0.1.4](https://github.com/open-webui/desktop/releases/tag/v0.1.4)

> 🛠️ **Tool creation from chat.** Models with native function calling can now create a private Python tool in your workspace when you ask them to, for administrators and users allowed to create workspace tools, and it can be turned off per model under Tool Creation in the model editor's builtin tools. [Commit](https://github.com/open-webui/open-webui/commit/91241306e2541e984591435d8c25e9ab1442db6b)

> 📂 **Temporary Chat on folder pages.** Turning Temporary Chat on or off on a folder's page, with the button at the top or with "/temporary", now keeps you on the folder page, so the next chat is still saved in the folder and gets its system prompt, default model and knowledge. [#33456](https://github.com/open-webui/open-webui/pull/33456), [#33448](https://github.com/open-webui/open-webui/issues/33448)

> 🏠 **New chat initialization.** Opening or reloading the home page or a folder now selects the model and applies chat URL parameters again, instead of leaving the model empty and ignoring the link’s settings. [Commit](https://github.com/open-webui/open-webui/commit/082df44d92178b6895153774bf6656c538cbce40)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-11-03-context-compaction-and-prompt-caching-when-the-same-model-handles-the-conversati|🧠 Context compaction and prompt caching. When the same model handles…]] · Pricing Model
- [[Changes/Open WebUI/2026-11-03-mcp-apps-in-chat-tools-from-mcp-servers-that-come-with-an-interactive-app-now-sh|🧩 MCP Apps in chat. Tools from MCP servers that come with an interactive app now…]] · Apps and Integrations
- [[Changes/Open WebUI/2026-11-03-new-chats-stay-in-sync-a-chat-started-from-the-home-page-keeps-syncing-with-the|🔃 New chats stay in sync. A chat started from the home page keeps syncing…]] · Collaboration
- [[Changes/Open WebUI/2026-11-03-4-voice-and-audio-changes-in-v0-13-0|4 Voice and Audio changes in v0.13.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-11-03-4-editor-experience-changes-in-v0-13-0|4 Editor Experience changes in v0.13.0]] · Editor Experience
- [[Changes/Open WebUI/2026-11-03-nested-code-previews-preview-now-opens-code-blocks-inside-lists-quotes-and-detai|🧩 Nested code previews. Preview now opens code blocks inside lists, quotes…]] · Artifact Creation
- [[Changes/Open WebUI/2026-11-03-live-context-usage-estimates-the-context-indicator-now-accounts-for-output-arriv|📏 Live context usage estimates. The context indicator now accounts for output…]] · Context Window
- [[Changes/Open WebUI/2026-11-03-2-automation-and-scheduling-changes-in-v0-13-0|2 Automation and Scheduling changes in v0.13.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-11-03-2-search-and-browsing-changes-in-v0-13-0|2 Search and Browsing changes in v0.13.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-11-03-image-drops-from-photo-apps-images-dropped-into-chats-and-channels-are-now-recog|🖼️ Image drops from photo apps. Images dropped into chats and channels are now…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-11-03-saved-oauth-provider-settings-oauth-providers-now-load-their-saved-connection-se|🔑 Saved OAuth provider settings. OAuth providers now load their saved connection…]] · Account and Access
- [[Changes/Open WebUI/2026-11-03-15-developer-workflow-changes-in-v0-13-0|15 Developer Workflow changes in v0.13.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-11-03-4-interface-experience-changes-in-v0-13-0|4 Interface Experience changes in v0.13.0]] · Interface Experience
- [[Changes/Open WebUI/2026-11-03-accessibility-improvements-screen-reader-users-now-hear-a-name-for-every-window|♿ Accessibility improvements. Screen reader users now hear a name for every…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-11-03-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-11-03-2-safety-and-privacy-changes-in-v0-13-0|2 Safety and Privacy changes in v0.13.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-11-03-no-sub-agent-limits-by-default-the-sub-agent-limits-in-admin-settings-and-throug|🔓 No sub-agent limits by default. The sub-agent limits in Admin Settings…]] · Agent Mode
- [[Changes/Open WebUI/2026-11-03-5-other-changes-in-v0-13-0|5 other changes in v0.13.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-11-03 · Ollama · [[Changes/Ollama/2026-11-03-2-model-support-changes-in-v0-40-14|2 Model Support changes in v0.40.14]]
- Later: 2026-11-04 · Dify · [[Changes/Dify/2026-11-04-4-model-support-changes-in-1-19-0|4 Model Support changes in 1.19.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-11-03-32a61b&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-11-03-4-model-support-changes-in-v0-13-0.md%0ACard%20ID%3A%20open-webui-2026-11-03-32a61b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.13.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->