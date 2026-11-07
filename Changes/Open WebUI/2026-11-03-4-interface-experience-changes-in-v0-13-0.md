---
card_id: open-webui-2026-11-03-c1265c
date: '2026-11-03'
description: 'Open WebUI · 2026-11-03 · Interface Experience: 4 changes in v0.13.0
  — ✨ **Generate title from top bar.** The rename field at the top of an open chat
  now has…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2760
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8aab70e114a6255b79dcb6954904c688e1d4776de864dc9c7b4c684c8ecfe2dc
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-11-03-c1265c
  comparison: ''
  date: '2026-11-03'
  description: 'Open WebUI — v0.13.0: 4 Interface Experience changes'
  evidence:
  - quote: ✨ **Generate title from top bar.** The rename field at the top of an open
      chat now has the same sparkle button as the sidebar, which generates a title
      from the conversation and saves it right away. [#33382](https://github.com/open-webui/open-webui/pull/33382)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: ⏸️ **Approvals shown in sidebar.** Chats in the sidebar now show a "Waiting
      for approval" marker while a tool call in them waits for you to allow or deny
      it. [Commit](https://github.com/open-webui/open-webui/commit/ddb43c83bac60553b002f148265db0900bc2b9f4),
      [Commit](https://github.com/open-webui/open-webui/commit/2840f0e07b398b76db04978334e3232fe8b89c31)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F50C **Responses-backed API streaming.** Clients using Open WebUI’s
      Chat Completions API now receive the expected streaming format even when the
      upstream model uses the Responses API, including text, reasoning, tool calls,
      token usage and completion reasons. [Commit](https://github.com/open-webui/open-webui/commit/e789513ea62eb0c56f36d7c48996f084931f1c49)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F5FA️ **Overview in the chat menu.** The chat Overview, the map
      of all messages and their branches, now opens as a full-screen window from Overview
      in the chat's menu instead of as a tab in Chat Controls. [Commit](https://github.com/open-webui/open-webui/commit/fe0d22cc24ddc2421b4e36a66a174188cc61d265)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-interface-experience-changes-in-v0-13-0
  source_release: open-webui-2026-11-03-v0-13-0-github-432661497-44290c10
  source_type: github_releases
  theme: interface-experience
  title: 4 Interface Experience changes in v0.13.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-11-02-2-interface-experience-changes-in-elevenlabs-updates-2026-11-02|2
  Interface Experience changes in ElevenLabs updates — 2026-11-02]]'
- '[[Changes/Google Antigravity/2026-11-03-5-interface-experience-changes-in-hub-v2-29-0-voice-mode-remote|5
  Interface Experience changes in HUB v2.29.0 — Voice mode, remote…]]'
- '[[Changes/Ollama/2026-11-03-picker-shows-ollama-s-actual-model-names|picker shows
  Ollama''s actual model names]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-11-03-v0-13-0-github-432661497-44290c10|open-webui-2026-11-03-v0-13-0-github-432661497-44290c10]]'
source_type: github_releases
theme: interface-experience
title: 4 Interface Experience changes in v0.13.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Interface Experience changes in v0.13.0

**Open WebUI** · 2026-11-03 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.13.0) · from [[Releases/Open WebUI/open-webui-2026-11-03-v0-13-0-github-432661497-44290c10|v0.13.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ✨ **Generate title from top bar.** The rename field at the top of an open chat now has the same sparkle button as the sidebar, which generates a title from the conversation and saves it right away. [#33382](https://github.com/open-webui/open-webui/pull/33382)

> ⏸️ **Approvals shown in sidebar.** Chats in the sidebar now show a "Waiting for approval" marker while a tool call in them waits for you to allow or deny it. [Commit](https://github.com/open-webui/open-webui/commit/ddb43c83bac60553b002f148265db0900bc2b9f4), [Commit](https://github.com/open-webui/open-webui/commit/2840f0e07b398b76db04978334e3232fe8b89c31)

> 🔌 **Responses-backed API streaming.** Clients using Open WebUI’s Chat Completions API now receive the expected streaming format even when the upstream model uses the Responses API, including text, reasoning, tool calls, token usage and completion reasons. [Commit](https://github.com/open-webui/open-webui/commit/e789513ea62eb0c56f36d7c48996f084931f1c49)

> 🗺️ **Overview in the chat menu.** The chat Overview, the map of all messages and their branches, now opens as a full-screen window from Overview in the chat's menu instead of as a tab in Chat Controls. [Commit](https://github.com/open-webui/open-webui/commit/fe0d22cc24ddc2421b4e36a66a174188cc61d265)

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
- [[Changes/Open WebUI/2026-11-03-15-developer-workflow-changes-in-v0-13-0|15 Developer Workflow changes in v0.13.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-11-03-accessibility-improvements-screen-reader-users-now-hear-a-name-for-every-window|♿ Accessibility improvements. Screen reader users now hear a name for every…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-11-03-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-11-03-2-safety-and-privacy-changes-in-v0-13-0|2 Safety and Privacy changes in v0.13.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-11-03-no-sub-agent-limits-by-default-the-sub-agent-limits-in-admin-settings-and-throug|🔓 No sub-agent limits by default. The sub-agent limits in Admin Settings…]] · Agent Mode
- [[Changes/Open WebUI/2026-11-03-5-other-changes-in-v0-13-0|5 other changes in v0.13.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-11-03 · Ollama · [[Changes/Ollama/2026-11-03-picker-shows-ollama-s-actual-model-names|picker shows Ollama's actual model names]]
- Later: 2026-11-03 · OpenClaw · [[Changes/OpenClaw/2026-11-03-13-interface-experience-changes-in-v2026-10-10|13 Interface Experience changes in v2026.10.10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-11-03-c1265c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-11-03-4-interface-experience-changes-in-v0-13-0.md%0ACard%20ID%3A%20open-webui-2026-11-03-c1265c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.13.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->