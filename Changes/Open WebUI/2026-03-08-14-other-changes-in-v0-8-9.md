---
card_id: open-webui-2026-03-08-8cdf57
date: '2026-03-08'
description: 'Open WebUI · 2026-03-08 · Other changes: 14 changes in v0.8.9 — ⏱️ **Event
  call timeout configuration.** Administrators can now configure the WebSocket event…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 338c6eea7de4b44fdc08b9066210b176f00da58ff942805bd02ede32e7036779
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-08-8cdf57
  comparison: ''
  date: '2026-03-08'
  description: 'Open WebUI — v0.8.9: 14 other changes'
  evidence:
  - quote: ⏱️ **Event call timeout configuration.** Administrators can now configure
      the WebSocket event call timeout via the WEBSOCKET_EVENT_CALLER_TIMEOUT environment
      variable, giving users more time to respond to event_call forms instead of timing
      out after 60 seconds. [#22222](https://github.com/open-webui/open-webui/pull/22222),
      [#22220](https://github.com/open-webui/open-webui/issues/22220)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F310 Translations for French, Finnish, Turkish, German, Simplified
      Chinese, and Traditional Chinese were enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F517 **Tool server URL trailing slash.** Fixed tool server connection
      failures when URLs have trailing slashes by stripping them before path concatenation.
      Previously, URLs like \"http://host:8080/v1/\" + \"/openapi.json\" produced
      double-slash URLs that some servers rejected. [#22116](https://github.com/open-webui/open-webui/pull/22116),
      [#21917](https://github.com/open-webui/open-webui/issues/21917)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F6E1️ **Citation parser error handling.** Fixed crashes when tools
      return error strings instead of expected data structures by adding type guards
      to the citation parser. The system now returns an empty source list instead
      of crashing with AttributeError. [#22118](https://github.com/open-webui/open-webui/pull/22118)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F50A **TTS thinking content.** Fixed TTS playback reading think
      tags instead of skipping them by handling edge cases where code blocks inside
      thinking content prevented proper tag removal. [#22237](https://github.com/open-webui/open-webui/pull/22237),
      [#22197](https://github.com/open-webui/open-webui/issues/22197)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4E5 **Chat archive handler.** The archive button in the chat navbar
      now actually archives the chat and refreshes the chat list, instead of doing
      nothing. [#22229](https://github.com/open-webui/open-webui/pull/22229)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F40D **BeautifulSoup4 dependency.** Added the missing BeautifulSoup4
      package to backend requirements, fixing failures when using features that depend
      on HTML parsing. [#22231](https://github.com/open-webui/open-webui/pull/22231)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F465 **Group users default sort.** Group members in the admin panel
      now sort by last active time by default instead of creation date, making it
      easier to find active users. [#22211](https://github.com/open-webui/open-webui/pull/22211)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F513 **Tool access permissions.** Users can now change tool and
      skill access permissions from private to public without errors. [#22325](https://github.com/open-webui/open-webui/pull/22325),
      [#22324](https://github.com/open-webui/open-webui/issues/22324)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4CF **OpenTelemetry metric descriptions.** Fixed conflicting metric
      instrument descriptions that caused warnings in the OpenTelemetry collector,
      resulting in cleaner telemetry logs for administrators. [#22293](https://github.com/open-webui/open-webui/pull/22293)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F522 **Non-streaming token tracking.** Token usage from non-streaming
      chat responses is now correctly saved to the database, fixing missing token
      counts in the Admin Panel analytics. Previously, non-streaming responses saved
      NULL usage data, causing messages to be excluded from token aggregation queries.
      [#22166](https://github.com/open-webui/open-webui/pull/22166)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F5BC️ **Chat overview profile image sizing.** Fixed a bug where
      profile images in the chat overview could shrink incorrectly in tight spaces.
      The images now maintain their proper size with the flex-shrink-0 property. [#22261](https://github.com/open-webui/open-webui/pull/22261)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4E8 **Queued messages display.** Fixed an issue where queued messages
      could be cut off or hidden. The queued messages area now scrolls properly when
      content exceeds the visible area, showing up to 25% of the viewport height.
      [#22176](https://github.com/open-webui/open-webui/pull/22176)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4CB **Analytics chat list duplicate fix.** Fixed a bug where the
      Analytics page chat list threw an \"each_key_duplicate\" Svelte error when chat
      IDs were duplicated during pagination. The fix adds deterministic ordering to
      prevent duplicate entries. [#22383](https://github.com/open-webui/open-webui/pull/22383)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 14-other-changes-in-v0-8-9
  source_release: open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb
  source_type: github_releases
  theme: uncategorized
  title: 14 other changes in v0.8.9
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb|open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb]]'
source_type: github_releases
theme: uncategorized
title: 14 other changes in v0.8.9
type: change
---

<!-- chronolog:begin region="header" -->
# 14 other changes in v0.8.9

**Open WebUI** · 2026-03-08 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.9) · from [[Releases/Open WebUI/open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb|v0.8.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ⏱️ **Event call timeout configuration.** Administrators can now configure the WebSocket event call timeout via the WEBSOCKET_EVENT_CALLER_TIMEOUT environment variable, giving users more time to respond to event_call forms instead of timing out after 60 seconds. [#22222](https://github.com/open-webui/open-webui/pull/22222), [#22220](https://github.com/open-webui/open-webui/issues/22220)

> 🌐 Translations for French, Finnish, Turkish, German, Simplified Chinese, and Traditional Chinese were enhanced and expanded.

> 🔗 **Tool server URL trailing slash.** Fixed tool server connection failures when URLs have trailing slashes by stripping them before path concatenation. Previously, URLs like "http://host:8080/v1/" + "/openapi.json" produced double-slash URLs that some servers rejected. [#22116](https://github.com/open-webui/open-webui/pull/22116), [#21917](https://github.com/open-webui/open-webui/issues/21917)

> 🛡️ **Citation parser error handling.** Fixed crashes when tools return error strings instead of expected data structures by adding type guards to the citation parser. The system now returns an empty source list instead of crashing with AttributeError. [#22118](https://github.com/open-webui/open-webui/pull/22118)

> 🔊 **TTS thinking content.** Fixed TTS playback reading think tags instead of skipping them by handling edge cases where code blocks inside thinking content prevented proper tag removal. [#22237](https://github.com/open-webui/open-webui/pull/22237), [#22197](https://github.com/open-webui/open-webui/issues/22197)

> 📥 **Chat archive handler.** The archive button in the chat navbar now actually archives the chat and refreshes the chat list, instead of doing nothing. [#22229](https://github.com/open-webui/open-webui/pull/22229)

> 🐍 **BeautifulSoup4 dependency.** Added the missing BeautifulSoup4 package to backend requirements, fixing failures when using features that depend on HTML parsing. [#22231](https://github.com/open-webui/open-webui/pull/22231)

> 👥 **Group users default sort.** Group members in the admin panel now sort by last active time by default instead of creation date, making it easier to find active users. [#22211](https://github.com/open-webui/open-webui/pull/22211)

> 🔓 **Tool access permissions.** Users can now change tool and skill access permissions from private to public without errors. [#22325](https://github.com/open-webui/open-webui/pull/22325), [#22324](https://github.com/open-webui/open-webui/issues/22324)

> 📏 **OpenTelemetry metric descriptions.** Fixed conflicting metric instrument descriptions that caused warnings in the OpenTelemetry collector, resulting in cleaner telemetry logs for administrators. [#22293](https://github.com/open-webui/open-webui/pull/22293)

> 🔢 **Non-streaming token tracking.** Token usage from non-streaming chat responses is now correctly saved to the database, fixing missing token counts in the Admin Panel analytics. Previously, non-streaming responses saved NULL usage data, causing messages to be excluded from token aggregation queries. [#22166](https://github.com/open-webui/open-webui/pull/22166)

> 🖼️ **Chat overview profile image sizing.** Fixed a bug where profile images in the chat overview could shrink incorrectly in tight spaces. The images now maintain their proper size with the flex-shrink-0 property. [#22261](https://github.com/open-webui/open-webui/pull/22261)

> 📨 **Queued messages display.** Fixed an issue where queued messages could be cut off or hidden. The queued messages area now scrolls properly when content exceeds the visible area, showing up to 25% of the viewport height. [#22176](https://github.com/open-webui/open-webui/pull/22176)

> 📋 **Analytics chat list duplicate fix.** Fixed a bug where the Analytics page chat list threw an "each_key_duplicate" Svelte error when chat IDs were duplicated during pagination. The fix adds deterministic ordering to prevent duplicate entries. [#22383](https://github.com/open-webui/open-webui/pull/22383)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-08-image-generation-in-temporary-chats-generated-images-now-display-correctly-in-te|🖌️ Image generation in temporary chats. Generated images now display correctly…]] · Image Generation
- [[Changes/Open WebUI/2026-03-08-2-context-window-changes-in-v0-8-9|2 Context Window changes in v0.8.9]] · Context Window
- [[Changes/Open WebUI/2026-03-08-microsoft-oauth-refresh-token-fix-fixed-a-bug-where-microsoft-oauth-refresh-toke|🔐 Microsoft OAuth refresh token fix. Fixed a bug where Microsoft OAuth refresh…]] · Account and Access
- [[Changes/Open WebUI/2026-03-08-17-developer-workflow-changes-in-v0-8-9|17 Developer Workflow changes in v0.8.9]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-08-5-interface-experience-changes-in-v0-8-9|5 Interface Experience changes in v0.8.9]] · Interface Experience
- [[Changes/Open WebUI/2026-03-08-2-voice-and-audio-changes-in-v0-8-9|2 Voice and Audio changes in v0.8.9]] · Voice and Audio
- [[Changes/Open WebUI/2026-03-08-android-photo-capture-fixed-an-issue-where-the-first-photo-taken-in-chat-appeare|📷 Android photo capture. Fixed an issue where the first photo taken in chat…]] · Files and Data
- [[Changes/Open WebUI/2026-03-08-2-search-and-browsing-changes-in-v0-8-9|2 Search and Browsing changes in v0.8.9]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-08-open-terminal-html-editing-users-can-now-edit-html-source-files-in-open-terminal|✏️ Open Terminal HTML editing. Users can now edit HTML source files in Open…]] · Editor Experience
- [[Changes/Open WebUI/2026-03-08-system-metrics-via-opentelemetry-administrators-can-now-monitor-python-runtime-a|📡 System metrics via OpenTelemetry. Administrators can now monitor Python…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-03-08-artifacts-reactive-loop-fix-fixed-an-infinite-reactive-loop-in-chat-when-artifac|♾️ Artifacts reactive loop fix. Fixed an infinite reactive loop in chat…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-03-08-13-reliability-and-performance-changes-in-v0-8-9|13 Reliability and Performance changes in v0.8.9]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-08-9-model-support-changes-in-v0-8-9|9 Model Support changes in v0.8.9]] · Model Support
- [[Changes/Open WebUI/2026-03-08-open-terminal-permission-fix-open-terminal-is-now-visible-without-requiring-allo|🖥️ Open Terminal permission fix. Open Terminal is now visible without requiring…]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-08-8cdf57&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-08-14-other-changes-in-v0-8-9.md%0ACard%20ID%3A%20open-webui-2026-03-08-8cdf57%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->