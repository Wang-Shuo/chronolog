---
card_id: open-webui-2025-11-24-986542
date: '2025-11-24'
description: "Open WebUI · 2025-11-24 · Files and Data: 2 changes in v0.6.37 — \U0001F50D
  Hybrid search now indexes file metadata including filenames, titles, headings, sources,
  and…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode
    offset]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2259
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 353f7924ce92f9be5ca9948892412e06bf6d58c7ce113f523acd3e7e81e59e7b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-11-24-986542
  comparison: ''
  date: '2025-11-24'
  description: 'Open WebUI — v0.6.37: 2 Files and Data changes'
  evidence:
  - quote: "\U0001F50D Hybrid search now indexes file metadata including filenames,
      titles, headings, sources, and snippets alongside document content, enabling
      keyword queries to surface documents where search terms appear only in metadata,
      configurable via \"ENABLE_RAG_HYBRID_SEARCH_ENRICHED_TEXTS\" environment variable.
      [#19095](https://github.com/open-webui/open-webui/pull/19095)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F4DD Note PDF downloads now sanitize HTML content using DOMPurify
      before rendering, preventing potential DOM-based XSS attacks from malicious
      content in notes. [Commit](https://github.com/open-webui/open-webui/commit/03cc6ce8eb5c055115406e2304fbf7e3338b8dce)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-files-and-data-changes-in-v0-6-37
  source_release: open-webui-2025-11-24-v0-6-37-github-264669867-8b715894
  source_type: github_releases
  theme: file-data
  title: 2 Files and Data changes in v0.6.37
  type: change
related_changes:
- '[[Changes/Open WebUI/2025-11-06-3-files-and-data-changes-in-v0-6-35|3 Files and
  Data changes in v0.6.35]]'
- '[[Changes/Recraft/2025-11-18-you-can-now-enhance-any-layer-directly-on-the-canvas-with-drop-shadow-stroke-and|Layer
  effects: Shadows, strokes, and blurs]]'
- '[[Changes/Ollama/2025-11-19-deepseek-ocr-https-ollama-com-library-deepseek-ocr-deepseek-ocr-uses-optical-2d|DeepSeek-OCR((source
  link) DeepSeek-OCR uses optical…]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-11-24-v0-6-37-github-264669867-8b715894|open-webui-2025-11-24-v0-6-37-github-264669867-8b715894]]'
source_type: github_releases
theme: file-data
title: 2 Files and Data changes in v0.6.37
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Files and Data changes in v0.6.37

**Open WebUI** · 2025-11-24 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.37) · from [[Releases/Open WebUI/open-webui-2025-11-24-v0-6-37-github-264669867-8b715894|v0.6.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔍 Hybrid search now indexes file metadata including filenames, titles, headings, sources, and snippets alongside document content, enabling keyword queries to surface documents where search terms appear only in metadata, configurable via "ENABLE_RAG_HYBRID_SEARCH_ENRICHED_TEXTS" environment variable. [#19095](https://github.com/open-webui/open-webui/pull/19095)

> 📝 Note PDF downloads now sanitize HTML content using DOMPurify before rendering, preventing potential DOM-based XSS attacks from malicious content in notes. [Commit](https://github.com/open-webui/open-webui/commit/03cc6ce8eb5c055115406e2304fbf7e3338b8dce)

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
## Nearby in Files and Data

- Earlier: 2025-11-19 · Ollama · [[Changes/Ollama/2025-11-19-deepseek-ocr-https-ollama-com-library-deepseek-ocr-deepseek-ocr-uses-optical-2d|DeepSeek-OCR((source link) DeepSeek-OCR uses optical…]]
- Later: 2025-11-26 · Dify · [[Changes/Dify/2025-11-26-3-files-and-data-changes-in-1-10-1|3 Files and Data changes in 1.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode offset]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-11-24-986542&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-11-24-2-files-and-data-changes-in-v0-6-37.md%0ACard%20ID%3A%20open-webui-2025-11-24-986542%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.37%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->