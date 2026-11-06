---
card_id: open-webui-2025-08-28-6e0a99
date: '2025-08-28'
description: "Open WebUI · 2025-08-28 · Reliability and Performance: 2 changes in
  v0.6.26 — \U0001F4E6 **Slim Docker Image Variant**: Added new slim Docker image
  option via…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 987
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c8632ce3bfdc4c5da88a529ae76fa7b4df76dc0fd162875882413949da57ac90
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-28-6e0a99
  comparison: ''
  date: '2025-08-28'
  description: 'Open WebUI — v0.6.26: 2 Reliability and Performance changes'
  evidence:
  - quote: "\U0001F4E6 **Slim Docker Image Variant**: Added new slim Docker image
      option via \"USE_SLIM\" build argument that excludes embedded AI models and
      Ollama installation, reducing image size by approximately 1GB. This variant
      enables faster image pulls and deployments for environments where AI models
      are managed externally, particularly beneficial for auto-scaling clusters and
      distributed deployments."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  - quote: "\U0001F504 **General Backend Refactoring**: Implemented various backend
      improvements to enhance performance, stability, and security, ensuring a more
      resilient and reliable platform for all users."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-reliability-and-performance-changes-in-v0-6-26
  source_release: open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3
  source_type: github_releases
  theme: reliability-performance
  title: 2 Reliability and Performance changes in v0.6.26
  type: change
related_changes:
- '[[Changes/Open WebUI/2025-08-21-6-reliability-and-performance-changes-in-v0-6-23|6
  Reliability and Performance changes in v0.6.23]]'
- '[[Changes/Codex CLI/2025-08-26-2-reliability-and-performance-changes-in-rust-v0-24-0|2
  Reliability and Performance changes in rust-v0.24.0]]'
- '[[Changes/Dify/2025-08-27-6-reliability-and-performance-changes-in-1-8-0|6 Reliability
  and Performance changes in 1.8.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3|open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3]]'
source_type: github_releases
theme: reliability-performance
title: 2 Reliability and Performance changes in v0.6.26
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Reliability and Performance changes in v0.6.26

**Open WebUI** · 2025-08-28 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.26) · from [[Releases/Open WebUI/open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3|v0.6.26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📦 **Slim Docker Image Variant**: Added new slim Docker image option via "USE_SLIM" build argument that excludes embedded AI models and Ollama installation, reducing image size by approximately 1GB. This variant enables faster image pulls and deployments for environments where AI models are managed externally, particularly beneficial for auto-scaling clusters and distributed deployments.

> 🔄 **General Backend Refactoring**: Implemented various backend improvements to enhance performance, stability, and security, ensuring a more resilient and reliable platform for all users.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-28-2-model-support-changes-in-v0-6-26|2 Model Support changes in v0.6.26]] · Model Support
- [[Changes/Open WebUI/2025-08-28-2-context-window-changes-in-v0-6-26|2 Context Window changes in v0.6.26]] · Context Window
- [[Changes/Open WebUI/2025-08-28-code-block-copy-button-content-fixed-fixed-an-issue-where-the-copy-button-in-cod|📋 Code Block Copy Button Content Fixed]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-28-2-safety-and-privacy-changes-in-v0-6-26|2 Safety and Privacy changes in v0.6.26]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-28-2-interface-experience-changes-in-v0-6-26|2 Interface Experience changes in v0.6.26]] · Interface Experience
- [[Changes/Open WebUI/2025-08-28-2-account-and-access-changes-in-v0-6-26|2 Account and Access changes in v0.6.26]] · Account and Access
- [[Changes/Open WebUI/2025-08-28-pdf-export-content-mismatch-fixed-resolved-an-issue-where-exporting-a-pdf-of-one|📄 PDF Export Content Mismatch Fixed]] · Memory and Personalization
- [[Changes/Open WebUI/2025-08-28-2-accessibility-and-localization-changes-in-v0-6-26|2 Accessibility and Localization changes in v0.6.26]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-28-2-search-and-browsing-changes-in-v0-6-26|2 Search and Browsing changes in v0.6.26]] · Search and Browsing
- [[Changes/Open WebUI/2025-08-28-configurable-file-upload-processing-mode-added-process-in-background-query-param|📁 Configurable File Upload Processing Mode]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-28-3-files-and-data-changes-in-v0-6-26|3 Files and Data changes in v0.6.26]] · Files and Data
- [[Changes/Open WebUI/2025-08-28-7-other-changes-in-v0-6-26|7 other changes in v0.6.26]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2025-08-27 · Dify · [[Changes/Dify/2025-08-27-6-reliability-and-performance-changes-in-1-8-0|6 Reliability and Performance changes in 1.8.0]]
- Later: 2025-08-29 · Codex CLI · [[Changes/Codex CLI/2025-08-29-performance-cleanup-remove-unnecessary-flush-calls|Performance/cleanup: remove unnecessary flush() calls]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-28-6e0a99&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-28-2-reliability-and-performance-changes-in-v0-6-26.md%0ACard%20ID%3A%20open-webui-2025-08-28-6e0a99%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->