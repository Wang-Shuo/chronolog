---
card_id: open-webui-2025-08-28-b4386a
date: '2025-08-28'
description: 'Open WebUI · 2025-08-28 · Search and Browsing: 2 changes in v0.6.26
  — ⚡ **Query Generation Caching**: Added "ENABLE_QUERIES_CACHE" environment variable
  to…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 889
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 68740ab6e53514a0c9a895b7b54033e3b35126a0079d49836b0d0e0d42045247
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-28-b4386a
  comparison: ''
  date: '2025-08-28'
  description: 'Open WebUI — v0.6.26: 2 Search and Browsing changes'
  evidence:
  - quote: '⚡ **Query Generation Caching**: Added "ENABLE_QUERIES_CACHE" environment
      variable to enable request-scoped caching of generated search queries. When
      both web search and file retrieval are active, queries generated for web search
      are automatically reused for file retrieval, eliminating duplicate LLM API calls
      and reducing token usage and costs while maintaining search quality.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  - quote: "\U0001F310 **Playwright Timeout Configuration Corrected**: Fixed an issue
      where Playwright timeout values were incorrectly converted from milliseconds
      to seconds with an additional 1000x multiplier, causing excessively long web
      loading timeouts. The timeout parameter now correctly uses the configured millisecond
      values as intended, ensuring responsive web search and document loading operations."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-search-and-browsing-changes-in-v0-6-26
  source_release: open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3
  source_type: github_releases
  theme: search-browsing
  title: 2 Search and Browsing changes in v0.6.26
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-08-18-feat-core-migrate-web-search-write-file-and-discovered-tool-by-joshualitt-in-htt|feat(core):
  Migrate web-search, write-file, and discovered-tool]]'
- '[[Changes/Open WebUI/2025-08-21-3-search-and-browsing-changes-in-v0-6-23|3 Search
  and Browsing changes in v0.6.23]]'
- '[[Changes/Codex CLI/2025-08-26-2-search-and-browsing-changes-in-rust-v0-24-0|2
  Search and Browsing changes in rust-v0.24.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3|open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3]]'
source_type: github_releases
theme: search-browsing
title: 2 Search and Browsing changes in v0.6.26
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Search and Browsing changes in v0.6.26

**Open WebUI** · 2025-08-28 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.26) · from [[Releases/Open WebUI/open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3|v0.6.26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ⚡ **Query Generation Caching**: Added "ENABLE_QUERIES_CACHE" environment variable to enable request-scoped caching of generated search queries. When both web search and file retrieval are active, queries generated for web search are automatically reused for file retrieval, eliminating duplicate LLM API calls and reducing token usage and costs while maintaining search quality.

> 🌐 **Playwright Timeout Configuration Corrected**: Fixed an issue where Playwright timeout values were incorrectly converted from milliseconds to seconds with an additional 1000x multiplier, causing excessively long web loading timeouts. The timeout parameter now correctly uses the configured millisecond values as intended, ensuring responsive web search and document loading operations.

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
- [[Changes/Open WebUI/2025-08-28-configurable-file-upload-processing-mode-added-process-in-background-query-param|📁 Configurable File Upload Processing Mode]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-28-3-files-and-data-changes-in-v0-6-26|3 Files and Data changes in v0.6.26]] · Files and Data
- [[Changes/Open WebUI/2025-08-28-7-other-changes-in-v0-6-26|7 other changes in v0.6.26]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2025-08-26 · Codex CLI · [[Changes/Codex CLI/2025-08-26-2-search-and-browsing-changes-in-rust-v0-24-0|2 Search and Browsing changes in rust-v0.24.0]]
- Later: 2025-09-03 · Codex CLI · [[Changes/Codex CLI/2025-09-03-3061-show-loading-state-when-search-results-are-pending|♯3061 Show loading state when @ search results are pending]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-28-b4386a&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-28-2-search-and-browsing-changes-in-v0-6-26.md%0ACard%20ID%3A%20open-webui-2025-08-28-b4386a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->