---
card_id: open-webui-2026-03-25-fd7a05
date: '2026-03-25'
description: "Open WebUI · 2026-03-25 · Other changes: 19 changes in v0.8.11 — \U0001F512
  **Trusted role header configuration.** Administrators can now configure the…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cf374f04d004065a2afc24d3b0c45d4cf8f0ed1b989dc5fbd9aa71df5d00d6bb
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-25-fd7a05
  comparison: ''
  date: '2026-03-25'
  description: 'Open WebUI — v0.8.11: 19 other changes'
  evidence:
  - quote: "\U0001F512 **Trusted role header configuration.** Administrators can now
      configure the WEBUI_AUTH_TRUSTED_ROLE_HEADER environment variable to set user
      roles (admin, user, or pending) via a trusted header from their identity provider
      or reverse proxy. [#22523](https://github.com/open-webui/open-webui/pull/22523)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F50C **Embed prompt confirmation.** Interactive tool embeds can
      now submit prompts to the chat without requiring same-origin access, showing
      a confirmation dialog for cross-origin requests to prevent abuse. [#22908](https://github.com/open-webui/open-webui/pull/22908)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: ✨ **Smoother loading animation.** The loading shimmer animation now looks
      smoother and more natural, with softer highlight colors. [#22516](https://github.com/open-webui/open-webui/pull/22516)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F3E5 **Readiness probe endpoint.** A new /ready endpoint is now
      available for Kubernetes deployments, returning 200 only after startup completes
      and database/Redis are reachable, enabling more reliable container orchestration.
      [#22507](https://github.com/open-webui/open-webui/pull/22507)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F310 Translations for Finnish, Portuguese (Portugal), Catalan, Turkish,
      Japanese, Simplified Chinese, Traditional Chinese, Estonian, Spanish, Azerbaijani,
      and German were enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F50D **SCIM group filtering.** The SCIM endpoint now properly handles
      displayName and externalId filters when provisioning groups from identity providers
      like Microsoft Entra ID, preventing all groups from being returned instead of
      the filtered subset. [#21543](https://github.com/open-webui/open-webui/pull/21543)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F5C4️ **Migration reliability.** Database migrations no longer fail
      when chat data has unexpected format, making upgrades more reliable. [#22588](https://github.com/open-webui/open-webui/pull/22588),
      [#22568](https://github.com/open-webui/open-webui/issues/22568)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F9ED **Chat deletion and archive redirection.** Users are now redirected
      to the chat list when deleting or archiving the currently active chat, instead
      of being left on a stale chat page. [#22755](https://github.com/open-webui/open-webui/pull/22755)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4CE **Channel message attachments.** Users can now press Enter
      to send messages with only file or image attachments in channels, direct messages,
      and threads, aligning with the behavior of the Send button. [#22752](https://github.com/open-webui/open-webui/pull/22752)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4A1 **Chat input suggestion modal.** The suggestion modal for tags,
      mentions, and commands now correctly reappears when backspacing into a trigger
      character after it was dismissed. [#22899](https://github.com/open-webui/open-webui/pull/22899)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F9F9 **Webhook profile image errors.** Fixed 404 errors appearing
      in the browser console when scrolling through channel messages sent by webhooks,
      by skipping the user profile preview for webhook senders. [#22893](https://github.com/open-webui/open-webui/pull/22893)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F503 **Chat input URL indexing fix.** Fixed an issue where URLs
      could be indexed twice when using multiple triggers followed by backspace and
      re-entering a URL. [#22749](https://github.com/open-webui/open-webui/issues/22749)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F50E **Search modal chat preview avatars.** Fixed assistant profile
      images not displaying in the chat preview pane of the Search Modal. [#22782](https://github.com/open-webui/open-webui/pull/22782)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4CB **Prompts search pagination fix.** Fixed a bug where searching
      prompts from a paginated page would incorrectly use the current page number,
      resulting in \"No prompts found\" even when matching results existed. [#22912](https://github.com/open-webui/open-webui/pull/22912)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F524 **Emoji removal for text normalization.** Fixed the emoji removal
      function used in search and title generation to correctly handle all emoji types,
      including those with variation selectors (❤️, ☀️, ✅), keycap sequences (1️⃣),
      and ZWJ family sequences (\U0001F468\U0001F469\U0001F467\U0001F466). [#22915](https://github.com/open-webui/open-webui/pull/22915)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: ⏹️ **Task cancellation status tracking.** Cancelled tasks now correctly
      mark only the affected messages as done instead of clearing all task statuses
      for the chat, ensuring proper status tracking when multiple messages have pending
      tasks. [#22743](https://github.com/open-webui/open-webui/pull/22743)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F3A8 **Filter icon display fix.** Fixed filter icons showing the
      wrong icon after removing one of multiple active filters below the chat input.
      [#22862](https://github.com/open-webui/open-webui/pull/22862)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4CB **Chat title preservation.** Regenerating responses or using
      branches no longer overwrites user-specified chat titles when auto-naming is
      disabled, by checking the full chat message count instead of just the current
      branch. [#22754](https://github.com/open-webui/open-webui/pull/22754)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F513 **Forward auth proxy compatibility.** Fixed error pages that
      could appear when using authenticating reverse-proxies by properly handling
      401 responses from background API requests, allowing the browser to re-authenticate
      with the identity provider. [#22942](https://github.com/open-webui/open-webui/pull/22942)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 19-other-changes-in-v0-8-11
  source_release: open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69
  source_type: github_releases
  theme: uncategorized
  title: 19 other changes in v0.8.11
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69]]'
source_type: github_releases
theme: uncategorized
title: 19 other changes in v0.8.11
type: change
---

<!-- chronolog:begin region="header" -->
# 19 other changes in v0.8.11

**Open WebUI** · 2026-03-25 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.11) · from [[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|v0.8.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔒 **Trusted role header configuration.** Administrators can now configure the WEBUI_AUTH_TRUSTED_ROLE_HEADER environment variable to set user roles (admin, user, or pending) via a trusted header from their identity provider or reverse proxy. [#22523](https://github.com/open-webui/open-webui/pull/22523)

> 🔌 **Embed prompt confirmation.** Interactive tool embeds can now submit prompts to the chat without requiring same-origin access, showing a confirmation dialog for cross-origin requests to prevent abuse. [#22908](https://github.com/open-webui/open-webui/pull/22908)

> ✨ **Smoother loading animation.** The loading shimmer animation now looks smoother and more natural, with softer highlight colors. [#22516](https://github.com/open-webui/open-webui/pull/22516)

> 🏥 **Readiness probe endpoint.** A new /ready endpoint is now available for Kubernetes deployments, returning 200 only after startup completes and database/Redis are reachable, enabling more reliable container orchestration. [#22507](https://github.com/open-webui/open-webui/pull/22507)

> 🌐 Translations for Finnish, Portuguese (Portugal), Catalan, Turkish, Japanese, Simplified Chinese, Traditional Chinese, Estonian, Spanish, Azerbaijani, and German were enhanced and expanded.

> 🔍 **SCIM group filtering.** The SCIM endpoint now properly handles displayName and externalId filters when provisioning groups from identity providers like Microsoft Entra ID, preventing all groups from being returned instead of the filtered subset. [#21543](https://github.com/open-webui/open-webui/pull/21543)

> 🗄️ **Migration reliability.** Database migrations no longer fail when chat data has unexpected format, making upgrades more reliable. [#22588](https://github.com/open-webui/open-webui/pull/22588), [#22568](https://github.com/open-webui/open-webui/issues/22568)

> 🧭 **Chat deletion and archive redirection.** Users are now redirected to the chat list when deleting or archiving the currently active chat, instead of being left on a stale chat page. [#22755](https://github.com/open-webui/open-webui/pull/22755)

> 📎 **Channel message attachments.** Users can now press Enter to send messages with only file or image attachments in channels, direct messages, and threads, aligning with the behavior of the Send button. [#22752](https://github.com/open-webui/open-webui/pull/22752)

> 💡 **Chat input suggestion modal.** The suggestion modal for tags, mentions, and commands now correctly reappears when backspacing into a trigger character after it was dismissed. [#22899](https://github.com/open-webui/open-webui/pull/22899)

> 🧹 **Webhook profile image errors.** Fixed 404 errors appearing in the browser console when scrolling through channel messages sent by webhooks, by skipping the user profile preview for webhook senders. [#22893](https://github.com/open-webui/open-webui/pull/22893)

> 🔃 **Chat input URL indexing fix.** Fixed an issue where URLs could be indexed twice when using multiple triggers followed by backspace and re-entering a URL. [#22749](https://github.com/open-webui/open-webui/issues/22749)

> 🔎 **Search modal chat preview avatars.** Fixed assistant profile images not displaying in the chat preview pane of the Search Modal. [#22782](https://github.com/open-webui/open-webui/pull/22782)

> 📋 **Prompts search pagination fix.** Fixed a bug where searching prompts from a paginated page would incorrectly use the current page number, resulting in "No prompts found" even when matching results existed. [#22912](https://github.com/open-webui/open-webui/pull/22912)

> 🔤 **Emoji removal for text normalization.** Fixed the emoji removal function used in search and title generation to correctly handle all emoji types, including those with variation selectors (❤️, ☀️, ✅), keycap sequences (1️⃣), and ZWJ family sequences (👨👩👧👦). [#22915](https://github.com/open-webui/open-webui/pull/22915)

> ⏹️ **Task cancellation status tracking.** Cancelled tasks now correctly mark only the affected messages as done instead of clearing all task statuses for the chat, ensuring proper status tracking when multiple messages have pending tasks. [#22743](https://github.com/open-webui/open-webui/pull/22743)

> 🎨 **Filter icon display fix.** Fixed filter icons showing the wrong icon after removing one of multiple active filters below the chat input. [#22862](https://github.com/open-webui/open-webui/pull/22862)

> 📋 **Chat title preservation.** Regenerating responses or using branches no longer overwrites user-specified chat titles when auto-naming is disabled, by checking the full chat message count instead of just the current branch. [#22754](https://github.com/open-webui/open-webui/pull/22754)

> 🔓 **Forward auth proxy compatibility.** Fixed error pages that could appear when using authenticating reverse-proxies by properly handling 401 responses from background API requests, allowing the browser to re-authenticate with the identity provider. [#22942](https://github.com/open-webui/open-webui/pull/22942)

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
- [[Changes/Open WebUI/2026-03-25-17-interface-experience-changes-in-v0-8-11|17 Interface Experience changes in v0.8.11]] · Interface Experience
- [[Changes/Open WebUI/2026-03-25-5-reliability-and-performance-changes-in-v0-8-11|5 Reliability and Performance changes in v0.8.11]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-25-tool-binary-response-handling-tool-servers-can-now-return-binary-data-such-as-im|🏮 Tool binary response handling. Tool servers can now return binary data such…]] · Multimodal Input
- [[Changes/Open WebUI/2026-03-25-23-model-support-changes-in-v0-8-11|23 Model Support changes in v0.8.11]] · Model Support
- [[Changes/Open WebUI/2026-03-25-4-safety-and-privacy-changes-in-v0-8-11|4 Safety and Privacy changes in v0.8.11]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-25-34-developer-workflow-changes-in-v0-8-11|34 Developer Workflow changes in v0.8.11]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-25-metrics-export-interval-configuration-administrators-can-now-control-opentelemet|📊 Metrics export interval configuration. Administrators can now control…]] · Pricing Model
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-25-fd7a05&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-25-19-other-changes-in-v0-8-11.md%0ACard%20ID%3A%20open-webui-2026-03-25-fd7a05%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->