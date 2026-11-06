---
card_id: open-webui-2026-02-23-99a082
date: '2026-02-23'
description: "Open WebUI · 2026-02-23 · Other changes: 15 changes in v0.8.4 — \U0001F9E9
  **Skill JSON import support.** Skills can now be imported from both JSON and Markdown
  files…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d9eae583b7280b19319fd0aa763fd15ac397b2ac0894ad7cda7ea3f64b478098
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-23-99a082
  comparison: ''
  date: '2026-02-23'
  description: 'Open WebUI — v0.8.4: 15 other changes'
  evidence:
  - quote: "\U0001F9E9 **Skill JSON import support.** Skills can now be imported from
      both JSON and Markdown files. [#21511](https://github.com/open-webui/open-webui/issues/21511)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F4DD **Group description display.** The admin groups list now shows
      each group's description, making it easier for administrators to identify groups
      at a glance."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F4F6 **Admin groups list sorting.** The Group and Users columns
      in the admin groups list are now clickable for sorting, allowing administrators
      to sort groups alphabetically by name or numerically by member count. [#21692](https://github.com/open-webui/open-webui/pull/21692)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F53D **Rich UI auto-scroll.** The view now automatically scrolls
      to action-generated Rich UI content once it renders, ensuring users can see
      the results without manually scrolling. [#21698](https://github.com/open-webui/open-webui/pull/21698),
      [#21482](https://github.com/open-webui/open-webui/discussions/21482)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F5C2️ **JSON logging support.** Administrators can now enable JSON-formatted
      logging by setting the LOG_FORMAT environment variable to \"json\", making logs
      suitable for log aggregators like Loki, Fluentd, CloudWatch, and Datadog. [#21747](https://github.com/open-webui/open-webui/pull/21747)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F310 Translations for Finnish, French, Portuguese (Brazil), Simplified
      Chinese, and Traditional Chinese were enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F4AC **New chat message handling fix.** Fixed a bug where clicking
      \"New Chat\" after sending a message would silently drop subsequent messages.
      The system now properly clears pending message queues when starting a new conversation.
      [#21731](https://github.com/open-webui/open-webui/pull/21731)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: ⏱️ **Embeddings and proxy timeout fix.** The embeddings and OpenAI proxy
      endpoints now properly honor the AIOHTTP_CLIENT_TIMEOUT environment variable,
      instead of using default timeouts that could cause requests to hang. [#21558](https://github.com/open-webui/open-webui/pull/21558)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F527 **SCIM parameter handling.** The SCIM Users and Groups endpoints
      now accept out-of-range startIndex and count values by clamping them to valid
      ranges instead of returning errors, in compliance with RFC 7644. [#21577](https://github.com/open-webui/open-webui/pull/21577)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F6E0️ **Imported items display.** Imported functions and tools now
      appear immediately in the list after import, without requiring a page reload.
      [#21593](https://github.com/open-webui/open-webui/issues/21593)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: ✋ **Drag-and-drop overlay fix.** The "Add Files" overlay no longer remains
      stuck on screen when dragging files back out of the chat window in Mozilla Firefox.
      [#21664](https://github.com/open-webui/open-webui/pull/21664)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F4DD **Console log spam fix.** Requesting deleted or missing files
      no longer floods the backend console with Python traceback logs, thanks to proper
      exception handling for expected 404 errors. [#21687](https://github.com/open-webui/open-webui/pull/21687)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F3A8 **Dark mode select background fix.** Fixed an issue where select
      inputs and dropdown menus had inconsistent lighter background colors in dark
      mode by removing conflicting dark theme overrides, ensuring a cohesive transparent
      look. [#21728](https://github.com/open-webui/open-webui/pull/21728)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F4BE **Prompt import fix.** Importing prompts that were previously
      exported no longer fails with a \"[object Object]\" error toast, making prompt
      backup and restore work correctly. [#21594](https://github.com/open-webui/open-webui/issues/21594)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F4E2 **Banners relocated.** Banners configuration has been moved
      from Admin Panel - Settings - Interface to Admin Panel - Settings - General."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 15-other-changes-in-v0-8-4
  source_release: open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c
  source_type: github_releases
  theme: uncategorized
  title: 15 other changes in v0.8.4
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c]]'
source_type: github_releases
theme: uncategorized
title: 15 other changes in v0.8.4
type: change
---

<!-- chronolog:begin region="header" -->
# 15 other changes in v0.8.4

**Open WebUI** · 2026-02-23 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.4) · from [[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|v0.8.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧩 **Skill JSON import support.** Skills can now be imported from both JSON and Markdown files. [#21511](https://github.com/open-webui/open-webui/issues/21511)

> 📝 **Group description display.** The admin groups list now shows each group's description, making it easier for administrators to identify groups at a glance.

> 📶 **Admin groups list sorting.** The Group and Users columns in the admin groups list are now clickable for sorting, allowing administrators to sort groups alphabetically by name or numerically by member count. [#21692](https://github.com/open-webui/open-webui/pull/21692)

> 🔽 **Rich UI auto-scroll.** The view now automatically scrolls to action-generated Rich UI content once it renders, ensuring users can see the results without manually scrolling. [#21698](https://github.com/open-webui/open-webui/pull/21698), [#21482](https://github.com/open-webui/open-webui/discussions/21482)

> 🗂️ **JSON logging support.** Administrators can now enable JSON-formatted logging by setting the LOG_FORMAT environment variable to "json", making logs suitable for log aggregators like Loki, Fluentd, CloudWatch, and Datadog. [#21747](https://github.com/open-webui/open-webui/pull/21747)

> 🌐 Translations for Finnish, French, Portuguese (Brazil), Simplified Chinese, and Traditional Chinese were enhanced and expanded.

> 💬 **New chat message handling fix.** Fixed a bug where clicking "New Chat" after sending a message would silently drop subsequent messages. The system now properly clears pending message queues when starting a new conversation. [#21731](https://github.com/open-webui/open-webui/pull/21731)

> ⏱️ **Embeddings and proxy timeout fix.** The embeddings and OpenAI proxy endpoints now properly honor the AIOHTTP_CLIENT_TIMEOUT environment variable, instead of using default timeouts that could cause requests to hang. [#21558](https://github.com/open-webui/open-webui/pull/21558)

> 🔧 **SCIM parameter handling.** The SCIM Users and Groups endpoints now accept out-of-range startIndex and count values by clamping them to valid ranges instead of returning errors, in compliance with RFC 7644. [#21577](https://github.com/open-webui/open-webui/pull/21577)

> 🛠️ **Imported items display.** Imported functions and tools now appear immediately in the list after import, without requiring a page reload. [#21593](https://github.com/open-webui/open-webui/issues/21593)

> ✋ **Drag-and-drop overlay fix.** The "Add Files" overlay no longer remains stuck on screen when dragging files back out of the chat window in Mozilla Firefox. [#21664](https://github.com/open-webui/open-webui/pull/21664)

> 📝 **Console log spam fix.** Requesting deleted or missing files no longer floods the backend console with Python traceback logs, thanks to proper exception handling for expected 404 errors. [#21687](https://github.com/open-webui/open-webui/pull/21687)

> 🎨 **Dark mode select background fix.** Fixed an issue where select inputs and dropdown menus had inconsistent lighter background colors in dark mode by removing conflicting dark theme overrides, ensuring a cohesive transparent look. [#21728](https://github.com/open-webui/open-webui/pull/21728)

> 💾 **Prompt import fix.** Importing prompts that were previously exported no longer fails with a "[object Object]" error toast, making prompt backup and restore work correctly. [#21594](https://github.com/open-webui/open-webui/issues/21594)

> 📢 **Banners relocated.** Banners configuration has been moved from Admin Panel - Settings - Interface to Admin Panel - Settings - General.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-23-12-developer-workflow-changes-in-v0-8-4|12 Developer Workflow changes in v0.8.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-23-10-reliability-and-performance-changes-in-v0-8-4|10 Reliability and Performance changes in v0.8.4]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-23-text-file-type-detection-fix-typescript-and-other-text-files-that-were-mis-detec|📄 Text file type detection fix. TypeScript and other text files…]] · Multimodal Input
- [[Changes/Open WebUI/2026-02-23-2-memory-and-personalization-changes-in-v0-8-4|2 Memory and Personalization changes in v0.8.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-02-23-ui-accessibility-improvements-screen-reader-users-can-now-navigate-the-interface|♿ UI accessibility improvements. Screen reader users can now navigate…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-02-23-8-interface-experience-changes-in-v0-8-4|8 Interface Experience changes in v0.8.4]] · Interface Experience
- [[Changes/Open WebUI/2026-02-23-2-editor-experience-changes-in-v0-8-4|2 Editor Experience changes in v0.8.4]] · Editor Experience
- [[Changes/Open WebUI/2026-02-23-4-search-and-browsing-changes-in-v0-8-4|4 Search and Browsing changes in v0.8.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-02-23-mcp-ssl-verification-fix-mcp-tool-connections-now-properly-respect-the-aiohttp-c|🔓 MCP SSL verification fix. MCP tool connections now properly respect…]] · Apps and Integrations
- [[Changes/Open WebUI/2026-02-23-file-access-control-respect-the-files-list-and-search-endpoints-now-properly-res|🗄️ File access control respect. The files list and search endpoints now properly…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-02-23-3-account-and-access-changes-in-v0-8-4|3 Account and Access changes in v0.8.4]] · Account and Access
- [[Changes/Open WebUI/2026-02-23-3-safety-and-privacy-changes-in-v0-8-4|3 Safety and Privacy changes in v0.8.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-02-23-16-model-support-changes-in-v0-8-4|16 Model Support changes in v0.8.4]] · Model Support
- [[Changes/Open WebUI/2026-02-23-api-tools-fix-the-api-v1-chat-completions-endpoint-now-properly-respects-caller|🛠️ API tools fix. The /api/v1/chat/completions endpoint now properly respects…]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-23-99a082&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-23-15-other-changes-in-v0-8-4.md%0ACard%20ID%3A%20open-webui-2026-02-23-99a082%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->