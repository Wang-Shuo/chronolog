---
card_id: open-webui-2026-06-01-0c8b8c
date: '2026-06-01'
description: "Open WebUI · 2026-06-01 · Other changes: 20 changes in v0.9.6 — \U0001F4E6
  **Official knowledge base sync tool.** A new companion tool from Open WebUI, oikb,
  keeps a…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6da5ab2c00fa24e2cb5d857045226728fc70a2ea4e61728d9fcd4eabaa506d26
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-01-0c8b8c
  comparison: ''
  date: '2026-06-01'
  description: 'Open WebUI — v0.9.6: 20 other changes'
  evidence:
  - quote: "\U0001F4E6 **Official knowledge base sync tool.** A new companion tool
      from Open WebUI, oikb, keeps a knowledge base in sync with a local directory,
      GitHub repo, S3 bucket, Confluence space, or any of more than 40 other sources,
      uploading only new and changed files using the incremental sync support added
      in this release. [oikb](https://github.com/open-webui/oikb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F310 **Translation updates.** Translations for Spanish (Spain),
      Swedish, German, Korean, Catalan, Russian, Irish, Simplified Chinese, Traditional
      Chinese, Finnish, Polish, Turkish, and Malay were enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F512 **Knowledge base access check in search tool.** The built-in
      knowledge search tool now verifies that the caller can access a knowledge base
      before searching it by id, preventing users from reading the contents of knowledge
      bases they have not been granted access to. [#25113](https://github.com/open-webui/open-webui/pull/25113)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F523 **Collection name validation.** Vector collection names are
      now rejected unless they contain only safe characters, preventing malformed
      names from reaching the vector store or breaking out of a database query expression.
      [#24982](https://github.com/open-webui/open-webui/pull/24982)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4DC **Prompt history authorization.** Comparing, deleting, and
      restoring prompt versions now verify the history entry belongs to the prompt
      you're authorized for, preventing access to or modification of another prompt's
      version history. [#25056](https://github.com/open-webui/open-webui/pull/25056)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F9F1 **API key endpoint restriction bypass.** The endpoint allow-list
      that limits which paths an API key may reach is now matched against the routed
      request path directly, preventing a crafted request from slipping past the restriction.
      [#25123](https://github.com/open-webui/open-webui/pull/25123)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001FAA4 **Cache file path traversal.** The cache file server now requires
      an exact directory boundary match, closing a gap where a sibling directory whose
      name began with the cache directory's name could be used to serve files from
      outside it. [#25086](https://github.com/open-webui/open-webui/pull/25086)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4CC **Chat file attachment access checks.** Attaching files to
      a chat now links only files the caller can read, preventing a user from associating
      another user's file with their chat to access its contents. [#25054](https://github.com/open-webui/open-webui/pull/25054)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4C5 **Calendar event move authorization.** Updating a calendar
      event to move it into a different calendar now requires write access on the
      destination calendar, preventing users from injecting events into calendars
      they cannot write to. [#24764](https://github.com/open-webui/open-webui/pull/24764)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F578️ **Web loader SSRF gating with Playwright.** When the Playwright-based
      web loader is in use, page navigations and redirects are now validated the same
      way as the default loader, closing a gap where the Playwright path could reach
      internal or otherwise blocked URLs. [#24756](https://github.com/open-webui/open-webui/pull/24756)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F5C2️ **Chat folder ownership checks.** Creating a chat or updating
      a chat's folder now verifies the referenced folder belongs to the current user,
      preventing chats from being associated with folders owned by other people. [#24588](https://github.com/open-webui/open-webui/pull/24588)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F39B️ **Filter changes to message output.** Filter functions that
      modify a message's structured output after generation now have those changes
      saved and displayed, instead of being discarded when only the output, not the
      text content, was changed. [#24884](https://github.com/open-webui/open-webui/pull/24884)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: ⏩ **Titles and tags reflect filtered output.** Outlet filters now run before
      automatic title, tag, and follow-up generation, so those are based on the final
      filtered message instead of the unfiltered version. [#24717](https://github.com/open-webui/open-webui/pull/24717)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4BE **Action-replaced message content persists.** Message content
      replaced by an action function through its event emitter is now kept when the
      chat is saved, instead of reverting to the original after a page reload. [#24585](https://github.com/open-webui/open-webui/issues/24585),
      [#25485](https://github.com/open-webui/open-webui/pull/25485)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F9F9 **Usage timer cleanup on send failure.** The background usage-stats
      timer started during message generation is now always cleared, even when sending
      a message fails, preventing leaked timers from accumulating over a session.
      [#25478](https://github.com/open-webui/open-webui/pull/25478)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F514 **Accurate knowledge upload feedback.** Dragging files into
      a knowledge base no longer shows an upload notification before the upload has
      actually been processed. [#25484](https://github.com/open-webui/open-webui/pull/25484)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: ♿ **High-contrast timestamp readability.** The user message timestamp now
      uses the correct colors in high-contrast mode instead of inverted ones, keeping
      it readable. [#25461](https://github.com/open-webui/open-webui/pull/25461)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F6DF **Resilience to corrupted local storage.** Corrupted data in
      the browser's local storage no longer crashes the interface; affected settings
      and dismissed-banner state now fall back to safe defaults. [#25481](https://github.com/open-webui/open-webui/pull/25481)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: '⚠️ **Database Migrations**: This release includes database schema changes;
      we strongly recommend backing up your database and all associated data before
      upgrading in production environments. If you are running a multi-worker, multi-server,
      or load-balanced deployment, all instances must be updated simultaneously, rolling
      updates are not supported and will cause application failures due to schema
      incompatibility.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F511 **\"WEBUI_SECRET_KEY\" is now a hard requirement even for unsupported
      deployments.** Deployments that start the backend in an explicitly unsupported
      way (such as invoking uvicorn directly) without setting \"WEBUI_SECRET_KEY\"
      will now refuse to start instead of falling back to an empty key; the supported
      start methods (start.sh, start_windows.bat, and \"open-webui serve\") still
      set or auto-generate it automatically, so standard deployments are unaffected.
      Direct Uvicorn startup is not supported. [#25218](https://github.com/open-webui/open-webui/pull/25218)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 20-other-changes-in-v0-9-6
  source_release: open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e
  source_type: github_releases
  theme: uncategorized
  title: 20 other changes in v0.9.6
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e]]'
source_type: github_releases
theme: uncategorized
title: 20 other changes in v0.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 20 other changes in v0.9.6

**Open WebUI** · 2026-06-01 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.6) · from [[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📦 **Official knowledge base sync tool.** A new companion tool from Open WebUI, oikb, keeps a knowledge base in sync with a local directory, GitHub repo, S3 bucket, Confluence space, or any of more than 40 other sources, uploading only new and changed files using the incremental sync support added in this release. [oikb](https://github.com/open-webui/oikb)

> 🌐 **Translation updates.** Translations for Spanish (Spain), Swedish, German, Korean, Catalan, Russian, Irish, Simplified Chinese, Traditional Chinese, Finnish, Polish, Turkish, and Malay were enhanced and expanded.

> 🔒 **Knowledge base access check in search tool.** The built-in knowledge search tool now verifies that the caller can access a knowledge base before searching it by id, preventing users from reading the contents of knowledge bases they have not been granted access to. [#25113](https://github.com/open-webui/open-webui/pull/25113)

> 🔣 **Collection name validation.** Vector collection names are now rejected unless they contain only safe characters, preventing malformed names from reaching the vector store or breaking out of a database query expression. [#24982](https://github.com/open-webui/open-webui/pull/24982)

> 📜 **Prompt history authorization.** Comparing, deleting, and restoring prompt versions now verify the history entry belongs to the prompt you're authorized for, preventing access to or modification of another prompt's version history. [#25056](https://github.com/open-webui/open-webui/pull/25056)

> 🧱 **API key endpoint restriction bypass.** The endpoint allow-list that limits which paths an API key may reach is now matched against the routed request path directly, preventing a crafted request from slipping past the restriction. [#25123](https://github.com/open-webui/open-webui/pull/25123)

> 🪤 **Cache file path traversal.** The cache file server now requires an exact directory boundary match, closing a gap where a sibling directory whose name began with the cache directory's name could be used to serve files from outside it. [#25086](https://github.com/open-webui/open-webui/pull/25086)

> 📌 **Chat file attachment access checks.** Attaching files to a chat now links only files the caller can read, preventing a user from associating another user's file with their chat to access its contents. [#25054](https://github.com/open-webui/open-webui/pull/25054)

> 📅 **Calendar event move authorization.** Updating a calendar event to move it into a different calendar now requires write access on the destination calendar, preventing users from injecting events into calendars they cannot write to. [#24764](https://github.com/open-webui/open-webui/pull/24764)

> 🕸️ **Web loader SSRF gating with Playwright.** When the Playwright-based web loader is in use, page navigations and redirects are now validated the same way as the default loader, closing a gap where the Playwright path could reach internal or otherwise blocked URLs. [#24756](https://github.com/open-webui/open-webui/pull/24756)

> 🗂️ **Chat folder ownership checks.** Creating a chat or updating a chat's folder now verifies the referenced folder belongs to the current user, preventing chats from being associated with folders owned by other people. [#24588](https://github.com/open-webui/open-webui/pull/24588)

> 🎛️ **Filter changes to message output.** Filter functions that modify a message's structured output after generation now have those changes saved and displayed, instead of being discarded when only the output, not the text content, was changed. [#24884](https://github.com/open-webui/open-webui/pull/24884)

> ⏩ **Titles and tags reflect filtered output.** Outlet filters now run before automatic title, tag, and follow-up generation, so those are based on the final filtered message instead of the unfiltered version. [#24717](https://github.com/open-webui/open-webui/pull/24717)

> 💾 **Action-replaced message content persists.** Message content replaced by an action function through its event emitter is now kept when the chat is saved, instead of reverting to the original after a page reload. [#24585](https://github.com/open-webui/open-webui/issues/24585), [#25485](https://github.com/open-webui/open-webui/pull/25485)

> 🧹 **Usage timer cleanup on send failure.** The background usage-stats timer started during message generation is now always cleared, even when sending a message fails, preventing leaked timers from accumulating over a session. [#25478](https://github.com/open-webui/open-webui/pull/25478)

> 🔔 **Accurate knowledge upload feedback.** Dragging files into a knowledge base no longer shows an upload notification before the upload has actually been processed. [#25484](https://github.com/open-webui/open-webui/pull/25484)

> ♿ **High-contrast timestamp readability.** The user message timestamp now uses the correct colors in high-contrast mode instead of inverted ones, keeping it readable. [#25461](https://github.com/open-webui/open-webui/pull/25461)

> 🛟 **Resilience to corrupted local storage.** Corrupted data in the browser's local storage no longer crashes the interface; affected settings and dismissed-banner state now fall back to safe defaults. [#25481](https://github.com/open-webui/open-webui/pull/25481)

> ⚠️ **Database Migrations**: This release includes database schema changes; we strongly recommend backing up your database and all associated data before upgrading in production environments. If you are running a multi-worker, multi-server, or load-balanced deployment, all instances must be updated simultaneously, rolling updates are not supported and will cause application failures due to schema incompatibility.

> 🔑 **"WEBUI_SECRET_KEY" is now a hard requirement even for unsupported deployments.** Deployments that start the backend in an explicitly unsupported way (such as invoking uvicorn directly) without setting "WEBUI_SECRET_KEY" will now refuse to start instead of falling back to an empty key; the supported start methods (start.sh, start_windows.bat, and "open-webui serve") still set or auto-generate it automatically, so standard deployments are unaffected. Direct Uvicorn startup is not supported. [#25218](https://github.com/open-webui/open-webui/pull/25218)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-01-bulk-enable-or-disable-automations-automations-can-now-be-enabled-or-disabled-in|🔘 Bulk enable or disable automations. Automations can now be enabled or disabled…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-01-4-context-window-changes-in-v0-9-6|4 Context Window changes in v0.9.6]] · Context Window
- [[Changes/Open WebUI/2026-06-01-2-memory-and-personalization-changes-in-v0-9-6|2 Memory and Personalization changes in v0.9.6]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-01-keyboard-and-screen-reader-access-to-menus-the-integrations-more-options-and-use|♿ Keyboard and screen reader access to menus. The integrations, more-options…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-01-27-developer-workflow-changes-in-v0-9-6|27 Developer Workflow changes in v0.9.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-01-4-interface-experience-changes-in-v0-9-6|4 Interface Experience changes in v0.9.6]] · Interface Experience
- [[Changes/Open WebUI/2026-06-01-4-editor-experience-changes-in-v0-9-6|4 Editor Experience changes in v0.9.6]] · Editor Experience
- [[Changes/Open WebUI/2026-06-01-5-files-and-data-changes-in-v0-9-6|5 Files and Data changes in v0.9.6]] · Files and Data
- [[Changes/Open WebUI/2026-06-01-7-safety-and-privacy-changes-in-v0-9-6|7 Safety and Privacy changes in v0.9.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-01-startup-on-non-unicode-consoles-open-webui-no-longer-crashes-at-startup-when-the|🥾 Startup on non-Unicode consoles. Open WebUI no longer crashes at startup…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-01-youtube-short-link-transcripts-pasting-a-youtu-be-short-link-into-a-chat-now-loa|📺 YouTube short link transcripts. Pasting a "youtu.be" short link into a chat…]] · Multimodal Input
- [[Changes/Open WebUI/2026-06-01-9-search-and-browsing-changes-in-v0-9-6|9 Search and Browsing changes in v0.9.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-01-shared-chat-file-write-protection-access-to-a-file-through-a-shared-chat-now-onl|🔐 Shared-chat file write protection. Access to a file through a shared chat now…]] · Collaboration
- [[Changes/Open WebUI/2026-06-01-2-enterprise-and-administration-changes-in-v0-9-6|2 Enterprise and Administration changes in v0.9.6]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-01-image-generation-with-non-standard-response-headers-image-generation-now-works-w|🖌️ Image generation with non-standard response headers. Image generation now…]] · Image Generation
- [[Changes/Open WebUI/2026-06-01-6-account-and-access-changes-in-v0-9-6|6 Account and Access changes in v0.9.6]] · Account and Access
- [[Changes/Open WebUI/2026-06-01-12-model-support-changes-in-v0-9-6|12 Model Support changes in v0.9.6]] · Model Support
- [[Changes/Open WebUI/2026-06-01-4-apps-and-integrations-changes-in-v0-9-6|4 Apps and Integrations changes in v0.9.6]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-01-5-reliability-and-performance-changes-in-v0-9-6|5 Reliability and Performance changes in v0.9.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-01-4-voice-and-audio-changes-in-v0-9-6|4 Voice and Audio changes in v0.9.6]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-01-0c8b8c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-01-20-other-changes-in-v0-9-6.md%0ACard%20ID%3A%20open-webui-2026-06-01-0c8b8c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->