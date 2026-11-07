---
card_id: open-webui-2025-12-02-242fa7
date: '2025-12-02'
description: "Open WebUI · 2025-12-02 · Developer Workflow: 13 changes in v0.6.41
  — \U0001F4E8 Direct Message channels now support a complete user-to-user messaging
  system with…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 990
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 52cae4ce872a6b0ced4cd88a7280f7ead9cb016cf29d3b58ae74d03568634438
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-02-242fa7
  comparison: ''
  date: '2025-12-02'
  description: 'Open WebUI — v0.6.41: 13 Developer Workflow changes'
  evidence:
  - quote: "\U0001F4E8 Direct Message channels now support a complete user-to-user
      messaging system with member-based access control, automatic deduplication for
      one-on-one conversations, optional channel naming, and distinct visual presentation
      using participant avatars instead of channel icons. [Commit](https://github.com/open-webui/open-webui/commit/acccb9afdd557274d6296c70258bb897bbb6652f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F4CC Message pinning functionality was added to channels, allowing
      users to pin important messages for easy reference with visual highlighting,
      a dedicated pinned messages modal accessible from the navbar, and complete backend
      support for tracking pinned status, pin timestamp, and the user who pinned each
      message. [Commit](https://github.com/open-webui/open-webui/commit/64b4d5d9c280b926746584aaf92b447d09deb386),
      [Commit](https://github.com/open-webui/open-webui/commit/aae2fce17355419d9c29f8100409108037895201)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F194 Users can now start Direct Message conversations directly from
      user profile previews by clicking the \"Message\" button, enabling quick access
      to private messaging without navigating away from the current channel. [Commit](https://github.com/open-webui/open-webui/commit/a0826ec9fedb56320532616d568fa59dda831d4e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F44D Channel message reactions now display the names of users who
      reacted when hovering over the emoji, showing up to three names with a count
      for additional reactors. [Commit](https://github.com/open-webui/open-webui/commit/05e79bdd0c7af70b631e958924e3656db1013b80)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F4E4 A group export API endpoint was added, enabling administrators
      to export complete group data including member lists for backup and migration
      purposes. [Commit](https://github.com/open-webui/open-webui/commit/09b6ea38c579659f8ca43ae5ea3746df3ac561ad)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F4E1 A new API endpoint was added to retrieve all users belonging
      to a specific group, enabling programmatic access to group membership information
      for administrative workflows. [Commit](https://github.com/open-webui/open-webui/commit/01868e856a10f474f74fbd1b4425dafdf949222f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F4C8 Active user count accuracy was significantly improved by replacing
      the socket-based USER_POOL tracking with a database-backed heartbeat mechanism,
      resolving long-standing issues where Redis deployments displayed inflated user
      counts due to stale sessions never being cleaned up on disconnect. [#16074](https://github.com/open-webui/open-webui/discussions/16074),
      [Commit](https://github.com/open-webui/open-webui/commit/70948f8803e417459d5203839f8077fdbfbbb213)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F4CE Web page attachment failures causing TypeError on metadata
      checks were resolved by correcting async threadpool parameter passing in vector
      database operations. [#19493](https://github.com/open-webui/open-webui/issues/19493),
      [Commit](https://github.com/open-webui/open-webui/commit/4370dee79e19d77062c03fba81780cb3b779fca3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001FA79 Database migration robustness was improved by automatically
      detecting and correcting missing primary key constraints on the user table,
      ensuring successful schema upgrades for databases with non-standard configurations.
      [#19487](https://github.com/open-webui/open-webui/discussions/19487), [Commit](https://github.com/open-webui/open-webui/commit/453ea9b9a167c0b03d86c46e6efd086bf10056ce)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F4A1 Knowledge base file tooltips now properly display the parent
      collection name when referencing files with the hash symbol, preventing confusion
      between identically-named files in different collections. [#19491](https://github.com/open-webui/open-webui/issues/19491),
      [Commit](https://github.com/open-webui/open-webui/commit/3fe5a47b0ff84ac97f8e4ff56a19fa2ec065bf66)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F4E6 Knowledge API batch file addition endpoint was corrected to
      properly handle async operations, resolving 500 Internal Server Error responses
      when adding multiple files simultaneously. [#19538](https://github.com/open-webui/open-webui/issues/19538),
      [Commit](https://github.com/open-webui/open-webui/commit/28659f60d94feb4f6a99bb1a5b54d7f45e5ea10f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F4C9 API response payload sizes were dramatically reduced by removing
      base64-encoded profile images from most endpoints, eliminating multi-megabyte
      responses caused by high-resolution avatars and enabling better browser caching.
      [#19519](https://github.com/open-webui/open-webui/issues/19519), [Commit](https://github.com/open-webui/open-webui/commit/384753c4c17f62a68d38af4bbcf55a21ee08e0f2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F46E Channel creation is now restricted to administrators only,
      with the channel add button hidden for regular users to maintain organizational
      control over communication channels. [Commit](https://github.com/open-webui/open-webui/commit/421aba7cd7cd708168b1f2565026c74525a67905)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 13-developer-workflow-changes-in-v0-6-41
  source_release: open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25
  source_type: github_releases
  theme: developer-workflow
  title: 13 Developer Workflow changes in v0.6.41
  type: change
related_changes:
- '[[Changes/Cline/2025-12-02-2-developer-workflow-changes-in-v3-39-0|2 Developer
  Workflow changes in v3.39.0]]'
- '[[Changes/Codex CLI/2025-12-02-4-developer-workflow-changes-in-rust-v0-64-0|4 Developer
  Workflow changes in rust-v0.64.0]]'
- '[[Changes/Gemini CLI/2025-12-02-4-developer-workflow-changes-in-v0-19-0|4 Developer
  Workflow changes in v0.19.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25]]'
source_type: github_releases
theme: developer-workflow
title: 13 Developer Workflow changes in v0.6.41
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Developer Workflow changes in v0.6.41

**Open WebUI** · 2025-12-02 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.41) · from [[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|v0.6.41]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📨 Direct Message channels now support a complete user-to-user messaging system with member-based access control, automatic deduplication for one-on-one conversations, optional channel naming, and distinct visual presentation using participant avatars instead of channel icons. [Commit](https://github.com/open-webui/open-webui/commit/acccb9afdd557274d6296c70258bb897bbb6652f)

> 📌 Message pinning functionality was added to channels, allowing users to pin important messages for easy reference with visual highlighting, a dedicated pinned messages modal accessible from the navbar, and complete backend support for tracking pinned status, pin timestamp, and the user who pinned each message. [Commit](https://github.com/open-webui/open-webui/commit/64b4d5d9c280b926746584aaf92b447d09deb386), [Commit](https://github.com/open-webui/open-webui/commit/aae2fce17355419d9c29f8100409108037895201)

> 🆔 Users can now start Direct Message conversations directly from user profile previews by clicking the "Message" button, enabling quick access to private messaging without navigating away from the current channel. [Commit](https://github.com/open-webui/open-webui/commit/a0826ec9fedb56320532616d568fa59dda831d4e)

> 👍 Channel message reactions now display the names of users who reacted when hovering over the emoji, showing up to three names with a count for additional reactors. [Commit](https://github.com/open-webui/open-webui/commit/05e79bdd0c7af70b631e958924e3656db1013b80)

> 📤 A group export API endpoint was added, enabling administrators to export complete group data including member lists for backup and migration purposes. [Commit](https://github.com/open-webui/open-webui/commit/09b6ea38c579659f8ca43ae5ea3746df3ac561ad)

> 📡 A new API endpoint was added to retrieve all users belonging to a specific group, enabling programmatic access to group membership information for administrative workflows. [Commit](https://github.com/open-webui/open-webui/commit/01868e856a10f474f74fbd1b4425dafdf949222f)

> 📈 Active user count accuracy was significantly improved by replacing the socket-based USER_POOL tracking with a database-backed heartbeat mechanism, resolving long-standing issues where Redis deployments displayed inflated user counts due to stale sessions never being cleaned up on disconnect. [#16074](https://github.com/open-webui/open-webui/discussions/16074), [Commit](https://github.com/open-webui/open-webui/commit/70948f8803e417459d5203839f8077fdbfbbb213)

> 📎 Web page attachment failures causing TypeError on metadata checks were resolved by correcting async threadpool parameter passing in vector database operations. [#19493](https://github.com/open-webui/open-webui/issues/19493), [Commit](https://github.com/open-webui/open-webui/commit/4370dee79e19d77062c03fba81780cb3b779fca3)

> 🩹 Database migration robustness was improved by automatically detecting and correcting missing primary key constraints on the user table, ensuring successful schema upgrades for databases with non-standard configurations. [#19487](https://github.com/open-webui/open-webui/discussions/19487), [Commit](https://github.com/open-webui/open-webui/commit/453ea9b9a167c0b03d86c46e6efd086bf10056ce)

> 💡 Knowledge base file tooltips now properly display the parent collection name when referencing files with the hash symbol, preventing confusion between identically-named files in different collections. [#19491](https://github.com/open-webui/open-webui/issues/19491), [Commit](https://github.com/open-webui/open-webui/commit/3fe5a47b0ff84ac97f8e4ff56a19fa2ec065bf66)

> 📦 Knowledge API batch file addition endpoint was corrected to properly handle async operations, resolving 500 Internal Server Error responses when adding multiple files simultaneously. [#19538](https://github.com/open-webui/open-webui/issues/19538), [Commit](https://github.com/open-webui/open-webui/commit/28659f60d94feb4f6a99bb1a5b54d7f45e5ea10f)

> 📉 API response payload sizes were dramatically reduced by removing base64-encoded profile images from most endpoints, eliminating multi-megabyte responses caused by high-resolution avatars and enabling better browser caching. [#19519](https://github.com/open-webui/open-webui/issues/19519), [Commit](https://github.com/open-webui/open-webui/commit/384753c4c17f62a68d38af4bbcf55a21ee08e0f2)

> 👮 Channel creation is now restricted to administrators only, with the channel add button hidden for regular users to maintain organizational control over communication channels. [Commit](https://github.com/open-webui/open-webui/commit/421aba7cd7cd708168b1f2565026c74525a67905)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-02-group-channels-were-introduced-as-a-new-channel-type-enabling-membership-based-c|👥 Group channels were introduced as a new channel type enabling membership-based…]] · Collaboration
- [[Changes/Open WebUI/2025-12-02-web-search-domain-filtering-was-corrected-to-properly-block-results-when-any-res|🛡️ Web search domain filtering was corrected to properly block results when any…]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-02-tool-call-response-token-duplication-was-fixed-by-removing-redundant-message-his|🔄 Tool call response token duplication was fixed by removing redundant message…]] · Context Window
- [[Changes/Open WebUI/2025-12-02-7-account-and-access-changes-in-v0-6-41|7 Account and Access changes in v0.6.41]] · Account and Access
- [[Changes/Open WebUI/2025-12-02-4-reliability-and-performance-changes-in-v0-6-41|4 Reliability and Performance changes in v0.6.41]] · Reliability and Performance
- [[Changes/Open WebUI/2025-12-02-2-safety-and-privacy-changes-in-v0-6-41|2 Safety and Privacy changes in v0.6.41]] · Safety and Privacy
- [[Changes/Open WebUI/2025-12-02-the-model-editor-interface-was-refined-with-access-control-settings-moved-to-a-d|🎨 The model editor interface was refined with access control settings moved…]] · Editor Experience
- [[Changes/Open WebUI/2025-12-02-9-model-support-changes-in-v0-6-41|9 Model Support changes in v0.6.41]] · Model Support
- [[Changes/Open WebUI/2025-12-02-image-generation-in-temporary-chats-was-fixed-by-correctly-handling-local-chat-s|🎨 Image generation in temporary chats was fixed by correctly handling local chat…]] · Image Generation
- [[Changes/Open WebUI/2025-12-02-2-enterprise-and-administration-changes-in-v0-6-41|2 Enterprise and Administration changes in v0.6.41]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-02-sentencetransformers-embedding-initialization-was-fixed-by-updating-the-transfor|🐍 SentenceTransformers embedding initialization was fixed by updating…]] · Files and Data
- [[Changes/Open WebUI/2025-12-02-11-interface-experience-changes-in-v0-6-41|11 Interface Experience changes in v0.6.41]] · Interface Experience
- [[Changes/Open WebUI/2025-12-02-2-apps-and-integrations-changes-in-v0-6-41|2 Apps and Integrations changes in v0.6.41]] · Apps and Integrations
- [[Changes/Open WebUI/2025-12-02-13-other-changes-in-v0-6-41|13 other changes in v0.6.41]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2025-12-02 · Gemini CLI · [[Changes/Gemini CLI/2025-12-02-4-developer-workflow-changes-in-v0-19-0|4 Developer Workflow changes in v0.19.0]]
- Later: 2025-12-04 · Cline · [[Changes/Cline/2025-12-04-docs-remove-advanced-patterns-and-testing-debugging-from-hooks-docs-by-jl-codes|docs: remove Advanced Patterns and Testing & Debugging from Hooks docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-02-242fa7&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-02-13-developer-workflow-changes-in-v0-6-41.md%0ACard%20ID%3A%20open-webui-2025-12-02-242fa7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.41%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->