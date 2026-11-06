---
card_id: open-webui-2026-04-21-556bbe
date: '2026-04-21'
description: 'Open WebUI · 2026-04-21 · Other changes: 21 changes in v0.9.0 — > [!CAUTION]'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cb2937a2800eeb3212beb5d0fc9077b0f84c841676c0c5f27948d7df31c86beb
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-556bbe
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.0: 21 other changes'
  evidence:
  - quote: '> [!CAUTION]'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: '> ⚠️ **Database Migrations**: This release includes database schema changes;
      we strongly recommend backing up your database and all associated data before
      upgrading in production environments. If you are running a multi-worker, multi-server,
      or load-balanced deployment, all instances must be updated simultaneously, rolling
      updates are not supported and will cause application failures due to schema
      incompatibility.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F3AF **Template token scan optimization.** Streaming responses now
      skip unnecessary token-replacement processing when no template markers are present,
      reducing per-update overhead and keeping chat output smoother during rapid generation.
      [#23161](https://github.com/open-webui/open-webui/pull/23161)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F464 **User endpoint query reduction.** Session-based user settings
      and status endpoints now avoid redundant user re-fetches, reducing unnecessary
      database load while preserving behavior. [#23794](https://github.com/open-webui/open-webui/pull/23794)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F310 **Translation updates.** Translations for Irish, Catalan, German,
      Simplified Chinese, Hindi, and Portuguese (Brazil) were enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5C2️ **Folder ownership assignment hardening.** Folder create and
      update inputs now reject unexpected extra fields, preventing clients from overriding
      protected values like ownership through mass-assignment payloads. [#23648](https://github.com/open-webui/open-webui/pull/23648)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F504 **Immediate outlet filter updates.** Assistant messages modified
      by outlet filters now appear correctly as soon as streaming completes, without
      requiring a page refresh. [#23829](https://github.com/open-webui/open-webui/pull/23829)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F30A **Middleware cancellation reliability.** Long-running requests
      now complete more reliably by preventing middleware-level cancellations from
      interrupting in-flight database and embedding work, reducing unexpected failures
      and noisy error logs when connections close early. [#23709](https://github.com/open-webui/open-webui/pull/23709)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5B1️ **Custom action icon drag prevention.** Custom user-added
      action icons in chat responses are no longer accidentally draggable, so clicks
      and hover interactions behave consistently with built-in action icons. [#23412](https://github.com/open-webui/open-webui/pull/23412)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5BC️ **Profile image URL validation.** Profile saves now accept
      valid Open WebUI profile-image paths, trusted external HTTP(S) avatar URLs,
      and safe raster data-image formats while rejecting unsafe URL patterns that
      could be abused. [#23389](https://github.com/open-webui/open-webui/pull/23389)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F310 **IPv6 SSRF address blocking.** URL validation now uses standard
      IP address checks for both IPv4 and IPv6, preventing private, loopback, link-local,
      reserved, and mapped-address SSRF bypasses through IPv6 hostname resolution.
      [#23453](https://github.com/open-webui/open-webui/pull/23453)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F512 **API key endpoint restriction bypass.** API key endpoint restrictions
      are now enforced regardless of whether the key is sent through Authorization
      headers, cookies, or \"x-api-key\", preventing bypass through alternate key
      transport paths. [#23637](https://github.com/open-webui/open-webui/pull/23637)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6D1 **Socket role invalidation.** Socket sessions now disconnect
      automatically when a user is demoted or deleted, preventing stale admin privileges
      from persisting until reconnect. [#23642](https://github.com/open-webui/open-webui/pull/23642)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6D1 **Task endpoint access control.** Global task listing and direct
      task stop endpoints are now restricted to administrators, while regular users
      can stop only their own chat tasks through a scoped chat endpoint. [#23454](https://github.com/open-webui/open-webui/pull/23454)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6AB **Inactive member channel access.** Deactivated group members
      can no longer read or write channel content through direct API calls, so channel
      permissions now match active membership status. [#23623](https://github.com/open-webui/open-webui/pull/23623)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4CC **Pinned webhook message handling.** Viewing pinned webhook
      messages now works reliably even when webhook profile data is missing, preventing
      server errors and frontend crashes in channel pinned message dialogs. [#23414](https://github.com/open-webui/open-webui/pull/23414)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9FE **Prompt variable form saving.** Prompt variable forms now
      save reliably without runtime errors or an unresponsive save action, so input
      values and placeholders work correctly when applying prompt templates with variables.
      [#23225](https://github.com/open-webui/open-webui/issues/23225), [#23480](https://github.com/open-webui/open-webui/issues/23480)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4CA **Usage statistic preservation.** Follow-up generation no longer
      overwrites existing token usage fields, so stored usage statistics remain accurate
      for the main response. [#23152](https://github.com/open-webui/open-webui/issues/23152)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5BC️ **Gravatar profile photo saving.** Gravatar profile images
      can now be saved successfully from account settings, with clearer validation
      and error handling instead of failing with generic object errors. [#23156](https://github.com/open-webui/open-webui/issues/23156)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001FA9F **Details expansion preference.** Tool call detail groups now
      honor the 'Always Expand Details' chat setting, so they open expanded by default
      when that preference is enabled. [#23262](https://github.com/open-webui/open-webui/pull/23262),
      [#23255](https://github.com/open-webui/open-webui/issues/23255)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6A7 **OpenAI passthrough now opt-in.** Direct OpenAI catch-all
      proxy requests are now disabled by default and require enabling \"ENABLE_OPENAI_API_PASSTHROUGH\",
      so deployments relying on passthrough must explicitly turn it on after upgrading.
      [#23640](https://github.com/open-webui/open-webui/pull/23640)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 21-other-changes-in-v0-9-0
  source_release: open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a
  source_type: github_releases
  theme: uncategorized
  title: 21 other changes in v0.9.0
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a]]'
source_type: github_releases
theme: uncategorized
title: 21 other changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 21 other changes in v0.9.0

**Open WebUI** · 2026-04-21 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.0) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> > [!CAUTION]

> > ⚠️ **Database Migrations**: This release includes database schema changes; we strongly recommend backing up your database and all associated data before upgrading in production environments. If you are running a multi-worker, multi-server, or load-balanced deployment, all instances must be updated simultaneously, rolling updates are not supported and will cause application failures due to schema incompatibility.

> 🎯 **Template token scan optimization.** Streaming responses now skip unnecessary token-replacement processing when no template markers are present, reducing per-update overhead and keeping chat output smoother during rapid generation. [#23161](https://github.com/open-webui/open-webui/pull/23161)

> 👤 **User endpoint query reduction.** Session-based user settings and status endpoints now avoid redundant user re-fetches, reducing unnecessary database load while preserving behavior. [#23794](https://github.com/open-webui/open-webui/pull/23794)

> 🌐 **Translation updates.** Translations for Irish, Catalan, German, Simplified Chinese, Hindi, and Portuguese (Brazil) were enhanced and expanded.

> 🗂️ **Folder ownership assignment hardening.** Folder create and update inputs now reject unexpected extra fields, preventing clients from overriding protected values like ownership through mass-assignment payloads. [#23648](https://github.com/open-webui/open-webui/pull/23648)

> 🔄 **Immediate outlet filter updates.** Assistant messages modified by outlet filters now appear correctly as soon as streaming completes, without requiring a page refresh. [#23829](https://github.com/open-webui/open-webui/pull/23829)

> 🌊 **Middleware cancellation reliability.** Long-running requests now complete more reliably by preventing middleware-level cancellations from interrupting in-flight database and embedding work, reducing unexpected failures and noisy error logs when connections close early. [#23709](https://github.com/open-webui/open-webui/pull/23709)

> 🖱️ **Custom action icon drag prevention.** Custom user-added action icons in chat responses are no longer accidentally draggable, so clicks and hover interactions behave consistently with built-in action icons. [#23412](https://github.com/open-webui/open-webui/pull/23412)

> 🖼️ **Profile image URL validation.** Profile saves now accept valid Open WebUI profile-image paths, trusted external HTTP(S) avatar URLs, and safe raster data-image formats while rejecting unsafe URL patterns that could be abused. [#23389](https://github.com/open-webui/open-webui/pull/23389)

> 🌐 **IPv6 SSRF address blocking.** URL validation now uses standard IP address checks for both IPv4 and IPv6, preventing private, loopback, link-local, reserved, and mapped-address SSRF bypasses through IPv6 hostname resolution. [#23453](https://github.com/open-webui/open-webui/pull/23453)

> 🔒 **API key endpoint restriction bypass.** API key endpoint restrictions are now enforced regardless of whether the key is sent through Authorization headers, cookies, or "x-api-key", preventing bypass through alternate key transport paths. [#23637](https://github.com/open-webui/open-webui/pull/23637)

> 🛑 **Socket role invalidation.** Socket sessions now disconnect automatically when a user is demoted or deleted, preventing stale admin privileges from persisting until reconnect. [#23642](https://github.com/open-webui/open-webui/pull/23642)

> 🛑 **Task endpoint access control.** Global task listing and direct task stop endpoints are now restricted to administrators, while regular users can stop only their own chat tasks through a scoped chat endpoint. [#23454](https://github.com/open-webui/open-webui/pull/23454)

> 🚫 **Inactive member channel access.** Deactivated group members can no longer read or write channel content through direct API calls, so channel permissions now match active membership status. [#23623](https://github.com/open-webui/open-webui/pull/23623)

> 📌 **Pinned webhook message handling.** Viewing pinned webhook messages now works reliably even when webhook profile data is missing, preventing server errors and frontend crashes in channel pinned message dialogs. [#23414](https://github.com/open-webui/open-webui/pull/23414)

> 🧾 **Prompt variable form saving.** Prompt variable forms now save reliably without runtime errors or an unresponsive save action, so input values and placeholders work correctly when applying prompt templates with variables. [#23225](https://github.com/open-webui/open-webui/issues/23225), [#23480](https://github.com/open-webui/open-webui/issues/23480)

> 📊 **Usage statistic preservation.** Follow-up generation no longer overwrites existing token usage fields, so stored usage statistics remain accurate for the main response. [#23152](https://github.com/open-webui/open-webui/issues/23152)

> 🖼️ **Gravatar profile photo saving.** Gravatar profile images can now be saved successfully from account settings, with clearer validation and error handling instead of failing with generic object errors. [#23156](https://github.com/open-webui/open-webui/issues/23156)

> 🪟 **Details expansion preference.** Tool call detail groups now honor the 'Always Expand Details' chat setting, so they open expanded by default when that preference is enabled. [#23262](https://github.com/open-webui/open-webui/pull/23262), [#23255](https://github.com/open-webui/open-webui/issues/23255)

> 🚧 **OpenAI passthrough now opt-in.** Direct OpenAI catch-all proxy requests are now disabled by default and require enabling "ENABLE_OPENAI_API_PASSTHROUGH", so deployments relying on passthrough must explicitly turn it on after upgrading. [#23640](https://github.com/open-webui/open-webui/pull/23640)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-21-3-files-and-data-changes-in-v0-9-0|3 Files and Data changes in v0.9.0]] · Files and Data
- [[Changes/Open WebUI/2026-04-21-4-image-generation-changes-in-v0-9-0|4 Image Generation changes in v0.9.0]] · Image Generation
- [[Changes/Open WebUI/2026-04-21-28-model-support-changes-in-v0-9-0|28 Model Support changes in v0.9.0]] · Model Support
- [[Changes/Open WebUI/2026-04-21-5-editor-experience-changes-in-v0-9-0|5 Editor Experience changes in v0.9.0]] · Editor Experience
- [[Changes/Open WebUI/2026-04-21-persistent-chat-payload-efficiency-persisted-chats-now-use-server-side-history-l|🚀 Persistent chat payload efficiency. Persisted chats now use server-side…]] · Multimodal Input
- [[Changes/Open WebUI/2026-04-21-8-context-window-changes-in-v0-9-0|8 Context Window changes in v0.9.0]] · Context Window
- [[Changes/Open WebUI/2026-04-21-24-reliability-and-performance-changes-in-v0-9-0|24 Reliability and Performance changes in v0.9.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-21-4-apps-and-integrations-changes-in-v0-9-0|4 Apps and Integrations changes in v0.9.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-21-46-developer-workflow-changes-in-v0-9-0|46 Developer Workflow changes in v0.9.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-04-21-8-automation-and-scheduling-changes-in-v0-9-0|8 Automation and Scheduling changes in v0.9.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-21-7-memory-and-personalization-changes-in-v0-9-0|7 Memory and Personalization changes in v0.9.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-21-2-mobile-and-desktop-changes-in-v0-9-0|2 Mobile and Desktop changes in v0.9.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-04-21-17-interface-experience-changes-in-v0-9-0|17 Interface Experience changes in v0.9.0]] · Interface Experience
- [[Changes/Open WebUI/2026-04-21-11-safety-and-privacy-changes-in-v0-9-0|11 Safety and Privacy changes in v0.9.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-04-21-4-search-and-browsing-changes-in-v0-9-0|4 Search and Browsing changes in v0.9.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-04-21-shared-chat-access-controls-you-can-now-control-who-has-access-to-a-shared-chat|🔗 Shared chat access controls. You can now control who has access to a shared…]] · Collaboration
- [[Changes/Open WebUI/2026-04-21-4-voice-and-audio-changes-in-v0-9-0|4 Voice and Audio changes in v0.9.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-04-21-17-account-and-access-changes-in-v0-9-0|17 Account and Access changes in v0.9.0]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-556bbe&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-21-other-changes-in-v0-9-0.md%0ACard%20ID%3A%20open-webui-2026-04-21-556bbe%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->