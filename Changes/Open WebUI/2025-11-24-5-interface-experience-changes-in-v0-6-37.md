---
card_id: open-webui-2025-11-24-2cdf60
date: '2025-11-24'
description: "Open WebUI · 2025-11-24 · Interface Experience: 5 changes in v0.6.37
  — \U0001F5C4️ PostgreSQL pgvector now supports HNSW index types and large dimensional
  embeddings…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1050
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 06efc36668b2edcdbed7e30aef94db1913be8c176a4f6df4254273d8988d4f64
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-11-24-2cdf60
  comparison: ''
  date: '2025-11-24'
  description: 'Open WebUI — v0.6.37: 5 Interface Experience changes'
  evidence:
  - quote: "\U0001F5C4️ PostgreSQL pgvector now supports HNSW index types and large
      dimensional embeddings exceeding 2000 dimensions through automatic halfvec type
      selection, with configurable index methods via \"PGVECTOR_INDEX_METHOD\", \"PGVECTOR_HNSW_M\",
      \"PGVECTOR_HNSW_EF_CONSTRUCTION\", and \"PGVECTOR_IVFFLAT_LISTS\" environment
      variables. [#19158](https://github.com/open-webui/open-webui/pull/19158), [#16890](https://github.com/open-webui/open-webui/issues/16890)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F4C2 Knowledge base upload page now supports folder drag-and-drop
      with recursive directory handling, enabling batch uploads of entire directory
      structures instead of requiring individual file selection. [#19320](https://github.com/open-webui/open-webui/pull/19320)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F3A8 Sidebar collapse states for model lists and group information
      are now persistent across page refreshes, remembering user preferences through
      browser-based storage. [#19159](https://github.com/open-webui/open-webui/issues/19159)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F3A8 Background image display was enhanced with semi-transparent
      overlays for navbar and sidebar, creating a seamless and visually cohesive design
      across the entire interface. [#19157](https://github.com/open-webui/open-webui/issues/19157)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F527 Tool selection prompt now correctly handles user messages without
      duplication, removing redundant query prefixes and improving prompt clarity.
      [#19122](https://github.com/open-webui/open-webui/pull/19122), [#19121](https://github.com/open-webui/open-webui/issues/19121)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-interface-experience-changes-in-v0-6-37
  source_release: open-webui-2025-11-24-v0-6-37-github-264669867-8b715894
  source_type: github_releases
  theme: interface-experience
  title: 5 Interface Experience changes in v0.6.37
  type: change
related_changes:
- '[[Changes/Midjourney/2025-11-20-animate-manually-button-bumps-you-back-to-prompt-bar|Animate
  manually button bumps you back to prompt bar]]'
- '[[Changes/Cursor/2025-11-21-set-origin-allowlist-from-dashboard-to-restrict-browser-tools-browser-tools-and|Set
  origin allowlist from dashboard to restrict browser tools]]'
- '[[Changes/GitHub Copilot CLI/2025-11-24-improved-timeline-rendering-of-shell-tool-names|Improved
  timeline rendering of shell tool names]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-11-24-v0-6-37-github-264669867-8b715894|open-webui-2025-11-24-v0-6-37-github-264669867-8b715894]]'
source_type: github_releases
theme: interface-experience
title: 5 Interface Experience changes in v0.6.37
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Interface Experience changes in v0.6.37

**Open WebUI** · 2025-11-24 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.37) · from [[Releases/Open WebUI/open-webui-2025-11-24-v0-6-37-github-264669867-8b715894|v0.6.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗄️ PostgreSQL pgvector now supports HNSW index types and large dimensional embeddings exceeding 2000 dimensions through automatic halfvec type selection, with configurable index methods via "PGVECTOR_INDEX_METHOD", "PGVECTOR_HNSW_M", "PGVECTOR_HNSW_EF_CONSTRUCTION", and "PGVECTOR_IVFFLAT_LISTS" environment variables. [#19158](https://github.com/open-webui/open-webui/pull/19158), [#16890](https://github.com/open-webui/open-webui/issues/16890)

> 📂 Knowledge base upload page now supports folder drag-and-drop with recursive directory handling, enabling batch uploads of entire directory structures instead of requiring individual file selection. [#19320](https://github.com/open-webui/open-webui/pull/19320)

> 🎨 Sidebar collapse states for model lists and group information are now persistent across page refreshes, remembering user preferences through browser-based storage. [#19159](https://github.com/open-webui/open-webui/issues/19159)

> 🎨 Background image display was enhanced with semi-transparent overlays for navbar and sidebar, creating a seamless and visually cohesive design across the entire interface. [#19157](https://github.com/open-webui/open-webui/issues/19157)

> 🔧 Tool selection prompt now correctly handles user messages without duplication, removing redundant query prefixes and improving prompt clarity. [#19122](https://github.com/open-webui/open-webui/pull/19122), [#19121](https://github.com/open-webui/open-webui/issues/19121)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-11-24-3-search-and-browsing-changes-in-v0-6-37|3 Search and Browsing changes in v0.6.37]] · Search and Browsing
- [[Changes/Open WebUI/2025-11-24-model-cloning-is-now-available-in-admin-settings-allowing-administrators-to-quic|🤖 Model cloning is now available in admin settings, allowing administrators…]] · Model Support
- [[Changes/Open WebUI/2025-11-24-granular-sharing-permissions-are-now-available-with-two-tiered-control-separatin|🔐 Granular sharing permissions are now available with two-tiered control separating…]] · Safety and Privacy
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
- [[Changes/Open WebUI/2025-11-24-9-reliability-and-performance-changes-in-v0-6-37|9 Reliability and Performance changes in v0.6.37]] · Reliability and Performance
- [[Changes/Open WebUI/2025-11-24-4-apps-and-integrations-changes-in-v0-6-37|4 Apps and Integrations changes in v0.6.37]] · Apps and Integrations
- [[Changes/Open WebUI/2025-11-24-password-policy-enforcement-is-now-available-with-configurable-validation-rules|🔐 Password policy enforcement is now available with configurable validation rules…]] · Other changes
- [[Changes/Open WebUI/2025-11-24-24-other-changes-in-v0-6-37|24 other changes in v0.6.37]] · Other changes
- [[Changes/Open WebUI/2025-11-24-daily-active-user-metric-is-now-available-for-monitoring-tracking-unique-users-a|📊 Daily active user metric is now available for monitoring, tracking unique users…]] · Other changes
- [[Changes/Open WebUI/2025-11-24-base64-image-conversion-is-now-available-for-markdown-content-in-chat-responses|💨 Base64 image conversion is now available for markdown content in chat responses…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2025-11-24 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-11-24-improved-timeline-rendering-of-shell-tool-names|Improved timeline rendering of shell tool names]]
- Later: 2025-11-25 · Gamma · [[Changes/Gamma/2025-11-25-here-s-what-s-improved|Here's what's improved]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-11-24-2cdf60&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-11-24-5-interface-experience-changes-in-v0-6-37.md%0ACard%20ID%3A%20open-webui-2025-11-24-2cdf60%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.37%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->