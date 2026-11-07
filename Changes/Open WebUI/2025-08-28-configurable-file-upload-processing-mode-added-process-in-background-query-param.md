---
card_id: open-webui-2025-08-28-c883d1
date: '2025-08-28'
description: "Open WebUI · 2025-08-28 · Apps and Integrations: \U0001F4C1 **Configurable
  File Upload Processing Mode**: Added \"process_in_background\" query parameter to
  the file…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2449
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: c6b6028c25777fa749a7e0a738c75c98b7744359e9da67b26111bb743eeedb20
product: open-webui
product_name: Open WebUI
record:
  ai_generated: true
  card_id: open-webui-2025-08-28-c883d1
  comparison: ''
  confidence: low
  date: '2025-08-28'
  description: "Open WebUI — v0.6.26: \U0001F4C1 **Configurable File Upload Processing
    Mode**: Added \"process_in_background\" query parameter to the file upload API
    endpoint, allowing clients to choose between asynchronous (default) and synchronous
    file processing. Setting \"process_in_background=false\" forces the upload request
    to wait until extraction and embedding complete, returning immediately usable
    files and simplifying integration for backend API consumers that prefer blocking
    calls over polling workflows."
  evidence:
  - quote: "\U0001F4C1 **Configurable File Upload Processing Mode**: Added \"process_in_background\"
      query parameter to the file upload API endpoint, allowing clients to choose
      between asynchronous (default) and synchronous file processing. Setting \"process_in_background=false\"
      forces the upload request to wait until extraction and embedding complete, returning
      immediately usable files and simplifying integration for backend API consumers
      that prefer blocking calls over polling workflows."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: open-webui
  product_name: Open WebUI
  slug: configurable-file-upload-processing-mode-added-process-in-background-query-param
  source_release: open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3
  source_type: github_releases
  theme: apps-integrations
  theme_matches:
  - matched_terms:
    - file upload
    score: 60
    theme: file-data
  - matched_terms:
    - integration
    score: 50
    theme: apps-integrations
  theme_resolution: manual-semantic-rule-v1
  title: "\U0001F4C1 **Configurable File Upload Processing Mode**"
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-08-26-5-apps-and-integrations-changes-in-rust-v0-24-0|5
  Apps and Integrations changes in rust-v0.24.0]]'
- '[[Changes/Dify/2025-08-27-11-apps-and-integrations-changes-in-1-8-0|11 Apps and
  Integrations changes in 1.8.0]]'
- '[[Changes/Gemini CLI/2025-08-27-2-apps-and-integrations-changes-in-v0-2-0|2 Apps
  and Integrations changes in v0.2.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3|open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3]]'
source_type: github_releases
theme: apps-integrations
title: "\U0001F4C1 Configurable File Upload Processing Mode"
type: change
---

<!-- chronolog:begin region="header" -->
# 📁 **Configurable File Upload Processing Mode**

**Open WebUI** · 2025-08-28 · [[Themes/apps-integrations|Apps and Integrations]] · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.26) · from [[Releases/Open WebUI/open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3|v0.6.26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> 📁 **Configurable File Upload Processing Mode**: Added "process_in_background" query parameter to the file upload API endpoint, allowing clients to choose between asynchronous (default) and synchronous file processing. Setting "process_in_background=false" forces the upload request to wait until extraction and embedding complete, returning immediately usable files and simplifying integration for backend API consumers that prefer blocking calls over polling workflows.
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
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
- [[Changes/Open WebUI/2025-08-28-3-files-and-data-changes-in-v0-6-26|3 Files and Data changes in v0.6.26]] · Files and Data
- [[Changes/Open WebUI/2025-08-28-7-other-changes-in-v0-6-26|7 other changes in v0.6.26]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-08-27 · Gemini CLI · [[Changes/Gemini CLI/2025-08-27-2-apps-and-integrations-changes-in-v0-2-0|2 Apps and Integrations changes in v0.2.0]]
- Later: 2025-08-29 · Codex CLI · [[Changes/Codex CLI/2025-08-29-3-apps-and-integrations-changes-in-rust-v0-26-0|3 Apps and Integrations changes in rust-v0.26.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-28-c883d1&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-28-configurable-file-upload-processing-mode-added-process-in-background-query-param.md%0ACard%20ID%3A%20open-webui-2025-08-28-c883d1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->