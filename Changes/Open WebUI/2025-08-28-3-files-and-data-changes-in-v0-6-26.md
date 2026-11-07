---
card_id: open-webui-2025-08-28-d99e7c
date: '2025-08-28'
description: "Open WebUI · 2025-08-28 · Files and Data: 3 changes in v0.6.26 — \U0001F4C4
  **Optimized PDF Export for Smaller File Size**: PDF exports are now significantly
  optimized…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2
    Files and Data changes in 0.2.2]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 826
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e2c8df501b87dc77c46d0bb2e11ceca2fe874053c831981102eeada2c435f3ed
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-28-d99e7c
  comparison: ''
  date: '2025-08-28'
  description: 'Open WebUI — v0.6.26: 3 Files and Data changes'
  evidence:
  - quote: "\U0001F4C4 **Optimized PDF Export for Smaller File Size**: PDF exports
      are now significantly optimized, producing much smaller files for faster downloads
      and easier sharing or archiving of your chats and documents."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  - quote: "\U0001F4C4 **Datalab Marker API Document Loader Fixed**: Fixed broken
      Datalab Marker API document loader functionality by correcting URL path handling
      for both hosted Datalab services and self-hosted Marker servers. Removed hardcoded
      \"/marker\" paths from the loader code and restored proper default URL structure,
      ensuring PDF and document processing works correctly with both deployment types."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  - quote: "\U0001F50D **Hybrid Search Parameter Handling Fixed**: Fixed an issue
      where the \"hybrid\" parameter in collection query requests was not being properly
      evaluated, causing the system to ignore user-specified hybrid search preferences
      and only check global configuration. Additionally resolved a division by zero
      error that occurred in hybrid search when BM25Retriever was called with empty
      document lists, ensuring robust search functionality across all collection states."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-files-and-data-changes-in-v0-6-26
  source_release: open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3
  source_type: github_releases
  theme: file-data
  title: 3 Files and Data changes in v0.6.26
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-08-14-document-certificate-issue-workaround-by-scidomino-in-https-github-com-google-ge|Document
  certificate issue workaround]]'
- "[[Changes/Open WebUI/2025-08-21-resolved-silently-dropped-streaming-response-chunks-fixed-an-issue-where-the-fin|\U0001F4AC
  Resolved Silently Dropped Streaming Response Chunks]]"
- '[[Changes/Dify/2025-08-27-4-files-and-data-changes-in-1-8-0|4 Files and Data changes
  in 1.8.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3|open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3]]'
source_type: github_releases
theme: file-data
title: 3 Files and Data changes in v0.6.26
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Files and Data changes in v0.6.26

**Open WebUI** · 2025-08-28 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.26) · from [[Releases/Open WebUI/open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3|v0.6.26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📄 **Optimized PDF Export for Smaller File Size**: PDF exports are now significantly optimized, producing much smaller files for faster downloads and easier sharing or archiving of your chats and documents.

> 📄 **Datalab Marker API Document Loader Fixed**: Fixed broken Datalab Marker API document loader functionality by correcting URL path handling for both hosted Datalab services and self-hosted Marker servers. Removed hardcoded "/marker" paths from the loader code and restored proper default URL structure, ensuring PDF and document processing works correctly with both deployment types.

> 🔍 **Hybrid Search Parameter Handling Fixed**: Fixed an issue where the "hybrid" parameter in collection query requests was not being properly evaluated, causing the system to ignore user-specified hybrid search preferences and only check global configuration. Additionally resolved a division by zero error that occurred in hybrid search when BM25Retriever was called with empty document lists, ensuring robust search functionality across all collection states.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-28-2-model-support-changes-in-v0-6-26|2 Model Support changes in v0.6.26]] · Model Support
- [[Changes/Open WebUI/2025-08-28-2-context-window-changes-in-v0-6-26|2 Context Window changes in v0.6.26]] · Context Window
- [[Changes/Open WebUI/2025-08-28-code-block-copy-button-content-fixed-fixed-an-issue-where-the-copy-button-in-cod|📋 Code Block Copy Button Content Fixed]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-28-2-safety-and-privacy-changes-in-v0-6-26|2 Safety and Privacy changes in v0.6.26]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-28-2-reliability-and-performance-changes-in-v0-6-26|2 Reliability and Performance changes in v0.6.26]] · Reliability and Performance
- [[Changes/Open WebUI/2025-08-28-2-interface-experience-changes-in-v0-6-26|2 Interface Experience changes in v0.6.26]] · Interface Experience
- [[Changes/Open WebUI/2025-08-28-2-account-and-access-changes-in-v0-6-26|2 Account and Access changes in v0.6.26]] · Account and Access
- [[Changes/Open WebUI/2025-08-28-pdf-export-content-mismatch-fixed-resolved-an-issue-where-exporting-a-pdf-of-one|📄 PDF Export Content Mismatch Fixed]] · Memory and Personalization
- [[Changes/Open WebUI/2025-08-28-2-accessibility-and-localization-changes-in-v0-6-26|2 Accessibility and Localization changes in v0.6.26]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-28-2-search-and-browsing-changes-in-v0-6-26|2 Search and Browsing changes in v0.6.26]] · Search and Browsing
- [[Changes/Open WebUI/2025-08-28-configurable-file-upload-processing-mode-added-process-in-background-query-param|📁 Configurable File Upload Processing Mode]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-28-7-other-changes-in-v0-6-26|7 other changes in v0.6.26]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2025-08-27 · Dify · [[Changes/Dify/2025-08-27-4-files-and-data-changes-in-1-8-0|4 Files and Data changes in 1.8.0]]
- Later: 2025-09-05 · Codex CLI · [[Changes/Codex CLI/2025-09-05-3118-codex-document-use-experimental-reasoning-summary-toml-key-config|♯3118 codex document use_experimental_reasoning_summary toml key config]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-25 · Dify · [[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2 Files and Data changes in 0.2.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-28-d99e7c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-28-3-files-and-data-changes-in-v0-6-26.md%0ACard%20ID%3A%20open-webui-2025-08-28-d99e7c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->