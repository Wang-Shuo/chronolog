---
card_id: open-webui-2025-11-24-d83da4
date: '2025-11-24'
description: "Open WebUI · 2025-11-24 · Reliability and Performance: 9 changes in
  v0.6.37 — \U0001F4C8 Model list API performance was optimized by pre-fetching user
  group memberships…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2562
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b85ba2cb5589e9d4bc4abaed77330e7e4f5d0f89e0f2976cf3c5adc6e4ead968
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-11-24-d83da4
  comparison: ''
  date: '2025-11-24'
  description: 'Open WebUI — v0.6.37: 9 Reliability and Performance changes'
  evidence:
  - quote: "\U0001F4C8 Model list API performance was optimized by pre-fetching user
      group memberships and removing profile image URLs from response payloads, significantly
      reducing both database queries and payload size for instances with large model
      lists, with profile images now served dynamically via dedicated endpoints. [#19097](https://github.com/open-webui/open-webui/pull/19097),
      [#18950](https://github.com/open-webui/open-webui/issues/18950)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: ⏩ Batch file processing performance was improved by reducing database queries
      by 67% while ensuring data consistency between vector and relational databases.
      [#18953](https://github.com/open-webui/open-webui/pull/18953)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F680 Chat import performance was dramatically improved by replacing
      individual per-chat API requests with a bulk import endpoint, reducing import
      time by up to 95% for large chat collections and providing user feedback via
      toast notifications displaying the number of successfully imported chats. [#17861](https://github.com/open-webui/open-webui/pull/17861)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: ⚡ Socket event broadcasting performance was optimized by implementing user-specific
      rooms, significantly reducing server overhead particularly for users with multiple
      concurrent sessions. [#18996](https://github.com/open-webui/open-webui/pull/18996)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F4DD Notes can now be created directly via the \"/notes/new\" URL
      endpoint with optional title and content query parameters, enabling faster note
      creation through bookmarks and shortcuts. [#19195](https://github.com/open-webui/open-webui/issues/19195)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F504 Various improvements were implemented across the frontend and
      backend to enhance performance, stability, and security."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F5C4️ S3 Vectors collection detection now correctly handles buckets
      with more than 2000 indexes by using direct index lookup instead of paginated
      list scanning, improving performance by approximately 8x and enabling RAG queries
      to work reliably at scale. [#19238](https://github.com/open-webui/open-webui/pull/19238),
      [#19233](https://github.com/open-webui/open-webui/issues/19233)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F4C8 Feedback retrieval performance was optimized by eliminating
      N+1 query patterns through database joins, adding server-side pagination and
      sorting, significantly reducing database load for instances with large feedback
      datasets. [#17976](https://github.com/open-webui/open-webui/pull/17976)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F5C4️ Group membership data storage was refactored from JSON arrays
      to a dedicated relational database table, significantly improving query performance
      and scalability for instances with large numbers of users and groups, while
      API responses now return member counts instead of full user ID arrays. [#19239](https://github.com/open-webui/open-webui/pull/19239)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 9-reliability-and-performance-changes-in-v0-6-37
  source_release: open-webui-2025-11-24-v0-6-37-github-264669867-8b715894
  source_type: github_releases
  theme: reliability-performance
  title: 9 Reliability and Performance changes in v0.6.37
  type: change
related_changes:
- '[[Changes/Replit/2025-11-21-fast-mode-now-available-to-everyone|Fast Mode now available
  to everyone]]'
- '[[Changes/Windsurf/2025-11-21-general-improvements|General Improvements]]'
- '[[Changes/Claude/2025-11-24-claude-for-excel-beta-release|Claude for Excel beta
  release]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-11-24-v0-6-37-github-264669867-8b715894|open-webui-2025-11-24-v0-6-37-github-264669867-8b715894]]'
source_type: github_releases
theme: reliability-performance
title: 9 Reliability and Performance changes in v0.6.37
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Reliability and Performance changes in v0.6.37

**Open WebUI** · 2025-11-24 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.37) · from [[Releases/Open WebUI/open-webui-2025-11-24-v0-6-37-github-264669867-8b715894|v0.6.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📈 Model list API performance was optimized by pre-fetching user group memberships and removing profile image URLs from response payloads, significantly reducing both database queries and payload size for instances with large model lists, with profile images now served dynamically via dedicated endpoints. [#19097](https://github.com/open-webui/open-webui/pull/19097), [#18950](https://github.com/open-webui/open-webui/issues/18950)

> ⏩ Batch file processing performance was improved by reducing database queries by 67% while ensuring data consistency between vector and relational databases. [#18953](https://github.com/open-webui/open-webui/pull/18953)

> 🚀 Chat import performance was dramatically improved by replacing individual per-chat API requests with a bulk import endpoint, reducing import time by up to 95% for large chat collections and providing user feedback via toast notifications displaying the number of successfully imported chats. [#17861](https://github.com/open-webui/open-webui/pull/17861)

> ⚡ Socket event broadcasting performance was optimized by implementing user-specific rooms, significantly reducing server overhead particularly for users with multiple concurrent sessions. [#18996](https://github.com/open-webui/open-webui/pull/18996)

> 📝 Notes can now be created directly via the "/notes/new" URL endpoint with optional title and content query parameters, enabling faster note creation through bookmarks and shortcuts. [#19195](https://github.com/open-webui/open-webui/issues/19195)

> 🔄 Various improvements were implemented across the frontend and backend to enhance performance, stability, and security.

> 🗄️ S3 Vectors collection detection now correctly handles buckets with more than 2000 indexes by using direct index lookup instead of paginated list scanning, improving performance by approximately 8x and enabling RAG queries to work reliably at scale. [#19238](https://github.com/open-webui/open-webui/pull/19238), [#19233](https://github.com/open-webui/open-webui/issues/19233)

> 📈 Feedback retrieval performance was optimized by eliminating N+1 query patterns through database joins, adding server-side pagination and sorting, significantly reducing database load for instances with large feedback datasets. [#17976](https://github.com/open-webui/open-webui/pull/17976)

> 🗄️ Group membership data storage was refactored from JSON arrays to a dedicated relational database table, significantly improving query performance and scalability for instances with large numbers of users and groups, while API responses now return member counts instead of full user ID arrays. [#19239](https://github.com/open-webui/open-webui/pull/19239)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-11-24-3-search-and-browsing-changes-in-v0-6-37|3 Search and Browsing changes in v0.6.37]] · Search and Browsing
- [[Changes/Open WebUI/2025-11-24-model-cloning-is-now-available-in-admin-settings-allowing-administrators-to-quic|🤖 Model cloning is now available in admin settings, allowing administrators…]] · Model Support
- [[Changes/Open WebUI/2025-11-24-granular-sharing-permissions-are-now-available-with-two-tiered-control-separatin|🔐 Granular sharing permissions are now available with two-tiered control separating…]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-24-5-interface-experience-changes-in-v0-6-37|5 Interface Experience changes in v0.6.37]] · Interface Experience
- [[Changes/Open WebUI/2025-11-24-granular-import-and-export-permissions-are-now-available-for-workspace-items-int|🔐 Granular import and export permissions are now available for workspace items…]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-24-prompt-autocompletion-is-now-available-independently-of-the-rich-text-input-sett|✍️ Prompt autocompletion is now available independently of the rich text input…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-11-24-rag-template-query-placeholder-escaping-logic-was-corrected-to-prevent-unintende|📝 RAG template query placeholder escaping logic was corrected to prevent unintended…]] · Context Window
- [[Changes/Open WebUI/2025-11-24-default-group-assignment-is-now-available-for-new-users-allowing-administrators|👥 Default group assignment is now available for new users, allowing administrators…]] · Model Support
- [[Changes/Open WebUI/2025-11-24-2-voice-and-audio-changes-in-v0-6-37|2 Voice and Audio changes in v0.6.37]] · Voice and Audio
- [[Changes/Open WebUI/2025-11-24-7-account-and-access-changes-in-v0-6-37|7 Account and Access changes in v0.6.37]] · Account and Access
- [[Changes/Open WebUI/2025-11-24-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-11-24-ui-scale-adjustment-is-now-available-in-interface-settings-allowing-users-to-inc|🎨 UI scale adjustment is now available in interface settings, allowing users…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-11-24-2-files-and-data-changes-in-v0-6-37|2 Files and Data changes in v0.6.37]] · Files and Data
- [[Changes/Open WebUI/2025-11-24-api-key-creation-is-now-controlled-by-granular-user-and-group-permissions-with-t|🔐 API key creation is now controlled by granular user and group permissions…]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-24-4-image-generation-changes-in-v0-6-37|4 Image Generation changes in v0.6.37]] · Image Generation
- [[Changes/Open WebUI/2025-11-24-websocket-and-redis-configuration-options-are-now-available-including-debug-logg|🔧 WebSocket and Redis configuration options are now available including debug…]] · Developer Workflow
- [[Changes/Open WebUI/2025-11-24-pwa-installations-on-ios-now-properly-refresh-after-server-container-restarts-re|📱 PWA installations on iOS now properly refresh after server container restarts…]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-11-24-11-model-support-changes-in-v0-6-37|11 Model Support changes in v0.6.37]] · Model Support
- [[Changes/Open WebUI/2025-11-24-4-apps-and-integrations-changes-in-v0-6-37|4 Apps and Integrations changes in v0.6.37]] · Apps and Integrations
- [[Changes/Open WebUI/2025-11-24-password-policy-enforcement-is-now-available-with-configurable-validation-rules|🔐 Password policy enforcement is now available with configurable validation rules…]] · Other changes
- [[Changes/Open WebUI/2025-11-24-24-other-changes-in-v0-6-37|24 other changes in v0.6.37]] · Other changes
- [[Changes/Open WebUI/2025-11-24-daily-active-user-metric-is-now-available-for-monitoring-tracking-unique-users-a|📊 Daily active user metric is now available for monitoring, tracking unique users…]] · Other changes
- [[Changes/Open WebUI/2025-11-24-base64-image-conversion-is-now-available-for-markdown-content-in-chat-responses|💨 Base64 image conversion is now available for markdown content in chat responses…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2025-11-24 · Claude · [[Changes/Claude/2025-11-24-claude-for-excel-beta-release|Claude for Excel beta release]]
- Later: 2025-11-25 · Open WebUI · [[Changes/Open WebUI/2025-11-25-various-improvements-were-implemented-across-the-frontend-and-backend-to-enhance|🔄 Various improvements were implemented across the frontend and backend to enhance…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-11-24-d83da4&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-11-24-9-reliability-and-performance-changes-in-v0-6-37.md%0ACard%20ID%3A%20open-webui-2025-11-24-d83da4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.37%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->