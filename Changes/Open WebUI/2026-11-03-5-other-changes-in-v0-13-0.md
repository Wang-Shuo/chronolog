---
card_id: open-webui-2026-11-03-dcd229
date: '2026-11-03'
description: "Open WebUI · 2026-11-03 · Other changes: 5 changes in v0.13.0 — \U0001F3F7️
  **Role prompt variable.** System prompts, saved prompts and chat requests through
  the API…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5089709451c9c49dfe59b0930470cc8c93b0e7d197afb22275951fdf2993dfba
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-11-03-dcd229
  comparison: ''
  date: '2026-11-03'
  description: 'Open WebUI — v0.13.0: 5 other changes'
  evidence:
  - quote: "\U0001F3F7️ **Role prompt variable.** System prompts, saved prompts and
      chat requests through the API can now use \"{{USER_ROLE}}\", which is replaced
      with the signed-in user's role, such as admin or user. [#33441](https://github.com/open-webui/open-webui/pull/33441),
      [#4765](https://github.com/open-webui/open-webui/discussions/4765)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F310 **Translation updates.** Translations for Portuguese (Brazil),
      Latvian, Azerbaijani, Basque, Bengali, Bosnian, Bulgarian, Cebuano, Croatian,
      Czech, Danish, Dutch, Estonian, Faroese, Filipino, Galician, German, Greek,
      Hebrew, Hungarian, Indonesian, Irish, Japanese, Korean, Lithuanian, Malay, Norwegian
      Bokmål, Persian, Polish, Punjabi, Romanian, Russian, Serbian, Slovak, Slovenian,
      Spanish (Spain), Tamil, Turkish, Turkmen, Ukrainian and Vietnamese were enhanced
      and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F9F5 **Thread reply focus.** Choosing Reply in Thread on a channel
      message now puts the cursor in the thread's reply box, also when the thread
      panel is already open. [#33467](https://github.com/open-webui/open-webui/pull/33467),
      [#33466](https://github.com/open-webui/open-webui/issues/33466)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: '⚠️ **Database Migrations**: This release includes database schema changes;
      we strongly recommend backing up your database and all associated data before
      upgrading in production environments. If you are running a multi-worker, multi-server,
      or load-balanced deployment, all instances must be updated simultaneously, rolling
      updates are not supported and will cause application failures due to schema
      incompatibility.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F501 **Higher tool-call limit.** A single response with native function
      calling can now run up to 1024 rounds of tool calls before it stops with \"Tool-call
      limit reached\", up from 256, and setting \"CHAT_RESPONSE_MAX_TOOL_CALL_ITERATIONS\"
      to 256 keeps the old limit. [#33384](https://github.com/open-webui/open-webui/pull/33384)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-other-changes-in-v0-13-0
  source_release: open-webui-2026-11-03-v0-13-0-github-432661497-44290c10
  source_type: github_releases
  theme: uncategorized
  title: 5 other changes in v0.13.0
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-11-03-v0-13-0-github-432661497-44290c10|open-webui-2026-11-03-v0-13-0-github-432661497-44290c10]]'
source_type: github_releases
theme: uncategorized
title: 5 other changes in v0.13.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 other changes in v0.13.0

**Open WebUI** · 2026-11-03 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.13.0) · from [[Releases/Open WebUI/open-webui-2026-11-03-v0-13-0-github-432661497-44290c10|v0.13.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🏷️ **Role prompt variable.** System prompts, saved prompts and chat requests through the API can now use "{{USER_ROLE}}", which is replaced with the signed-in user's role, such as admin or user. [#33441](https://github.com/open-webui/open-webui/pull/33441), [#4765](https://github.com/open-webui/open-webui/discussions/4765)

> 🌐 **Translation updates.** Translations for Portuguese (Brazil), Latvian, Azerbaijani, Basque, Bengali, Bosnian, Bulgarian, Cebuano, Croatian, Czech, Danish, Dutch, Estonian, Faroese, Filipino, Galician, German, Greek, Hebrew, Hungarian, Indonesian, Irish, Japanese, Korean, Lithuanian, Malay, Norwegian Bokmål, Persian, Polish, Punjabi, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish (Spain), Tamil, Turkish, Turkmen, Ukrainian and Vietnamese were enhanced and expanded.

> 🧵 **Thread reply focus.** Choosing Reply in Thread on a channel message now puts the cursor in the thread's reply box, also when the thread panel is already open. [#33467](https://github.com/open-webui/open-webui/pull/33467), [#33466](https://github.com/open-webui/open-webui/issues/33466)

> ⚠️ **Database Migrations**: This release includes database schema changes; we strongly recommend backing up your database and all associated data before upgrading in production environments. If you are running a multi-worker, multi-server, or load-balanced deployment, all instances must be updated simultaneously, rolling updates are not supported and will cause application failures due to schema incompatibility.

> 🔁 **Higher tool-call limit.** A single response with native function calling can now run up to 1024 rounds of tool calls before it stops with "Tool-call limit reached", up from 256, and setting "CHAT_RESPONSE_MAX_TOOL_CALL_ITERATIONS" to 256 keeps the old limit. [#33384](https://github.com/open-webui/open-webui/pull/33384)

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
- [[Changes/Open WebUI/2026-11-03-4-interface-experience-changes-in-v0-13-0|4 Interface Experience changes in v0.13.0]] · Interface Experience
- [[Changes/Open WebUI/2026-11-03-accessibility-improvements-screen-reader-users-now-hear-a-name-for-every-window|♿ Accessibility improvements. Screen reader users now hear a name for every…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-11-03-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-11-03-2-safety-and-privacy-changes-in-v0-13-0|2 Safety and Privacy changes in v0.13.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-11-03-no-sub-agent-limits-by-default-the-sub-agent-limits-in-admin-settings-and-throug|🔓 No sub-agent limits by default. The sub-agent limits in Admin Settings…]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-11-03-dcd229&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-11-03-5-other-changes-in-v0-13-0.md%0ACard%20ID%3A%20open-webui-2026-11-03-dcd229%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.13.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->