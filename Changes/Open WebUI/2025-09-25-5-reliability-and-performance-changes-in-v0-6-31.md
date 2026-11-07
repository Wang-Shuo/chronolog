---
card_id: open-webui-2025-09-25-f7e1b8
date: '2025-09-25'
description: "Open WebUI · 2025-09-25 · Reliability and Performance: 5 changes in
  v0.6.31 — \U0001F4CA Notes query performance was optimized through database-level
  filtering and…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2502
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 739ca21e7afb975baf2b94106deffaba8328d34dbe3cb7dbb8bfd39ef757a0dd
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-09-25-f7e1b8
  comparison: ''
  date: '2025-09-25'
  description: 'Open WebUI — v0.6.31: 5 Reliability and Performance changes'
  evidence:
  - quote: "\U0001F4CA Notes query performance was optimized through database-level
      filtering and separated access control logic, reducing memory usage and eliminating
      N+1 query problems for better scalability. [#17607](https://github.com/open-webui/open-webui/pull/17607)
      [Commit](https://github.com/open-webui/open-webui/pull/17747/commits/da661756fa7eec754270e6dd8c67cbf74a28a17f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  - quote: ⚡ Page loading performance was optimized by deferring API requests until
      components are actually opened, including ChangelogModal, ModelSelector, RecursiveFolder,
      ArchivedChatsModal, and SearchModal. [#17542](https://github.com/open-webui/open-webui/pull/17542),
      [#17555](https://github.com/open-webui/open-webui/pull/17555), [#17557](https://github.com/open-webui/open-webui/pull/17557),
      [#17541](https://github.com/open-webui/open-webui/pull/17541), [#17640](https://github.com/open-webui/open-webui/pull/17640)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  - quote: ⚡ Bundle size was reduced by 1.58MB through optimized highlight.js language
      support, improving page loading speed and reducing bandwidth usage. [#17645](https://github.com/open-webui/open-webui/pull/17645)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  - quote: "\U0001F504 Various improvements were implemented across the frontend and
      backend to enhance performance, stability, and security."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  - quote: "\U0001F4BE Memory leaks in file handling and HTTP connections are prevented
      through proper resource cleanup, ensuring stable memory usage during large file
      downloads and processing operations. [#17608](https://github.com/open-webui/open-webui/pull/17608)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-reliability-and-performance-changes-in-v0-6-31
  source_release: open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead
  source_type: github_releases
  theme: reliability-performance
  title: 5 Reliability and Performance changes in v0.6.31
  type: change
related_changes:
- '[[Changes/Dify/2025-09-22-5-reliability-and-performance-changes-in-1-9-0|5 Reliability
  and Performance changes in 1.9.0]]'
- '[[Changes/Gemini CLI/2025-09-24-feat-add-cached-string-width-function-for-performance-optimization-by-jacob314-i|feat:
  add cached string width function for performance optimization]]'
- '[[Changes/LM Studio/2025-09-24-improved-memory-usage-estimation-used-for-model-loading-guardrails|Improved
  memory usage estimation used for model loading guardrails]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead|open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead]]'
source_type: github_releases
theme: reliability-performance
title: 5 Reliability and Performance changes in v0.6.31
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Reliability and Performance changes in v0.6.31

**Open WebUI** · 2025-09-25 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.31) · from [[Releases/Open WebUI/open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead|v0.6.31]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📊 Notes query performance was optimized through database-level filtering and separated access control logic, reducing memory usage and eliminating N+1 query problems for better scalability. [#17607](https://github.com/open-webui/open-webui/pull/17607) [Commit](https://github.com/open-webui/open-webui/pull/17747/commits/da661756fa7eec754270e6dd8c67cbf74a28a17f)

> ⚡ Page loading performance was optimized by deferring API requests until components are actually opened, including ChangelogModal, ModelSelector, RecursiveFolder, ArchivedChatsModal, and SearchModal. [#17542](https://github.com/open-webui/open-webui/pull/17542), [#17555](https://github.com/open-webui/open-webui/pull/17555), [#17557](https://github.com/open-webui/open-webui/pull/17557), [#17541](https://github.com/open-webui/open-webui/pull/17541), [#17640](https://github.com/open-webui/open-webui/pull/17640)

> ⚡ Bundle size was reduced by 1.58MB through optimized highlight.js language support, improving page loading speed and reducing bandwidth usage. [#17645](https://github.com/open-webui/open-webui/pull/17645)

> 🔄 Various improvements were implemented across the frontend and backend to enhance performance, stability, and security.

> 💾 Memory leaks in file handling and HTTP connections are prevented through proper resource cleanup, ensuring stable memory usage during large file downloads and processing operations. [#17608](https://github.com/open-webui/open-webui/pull/17608)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-09-25-editor-collaboration-functionality-was-refactored-to-reduce-package-size-by-390k|⚡ Editor collaboration functionality was refactored to reduce package size by 390KB…]] · Collaboration
- [[Changes/Open WebUI/2025-09-25-4-apps-and-integrations-changes-in-v0-6-31|4 Apps and Integrations changes in v0.6.31]] · Apps and Integrations
- [[Changes/Open WebUI/2025-09-25-2-editor-experience-changes-in-v0-6-31|2 Editor Experience changes in v0.6.31]] · Editor Experience
- [[Changes/Open WebUI/2025-09-25-rag-query-generation-is-now-skipped-when-all-attached-files-are-set-to-full-cont|🔍 RAG query generation is now skipped when all attached files are set to full…]] · Context Window
- [[Changes/Open WebUI/2025-09-25-3-safety-and-privacy-changes-in-v0-6-31|3 Safety and Privacy changes in v0.6.31]] · Safety and Privacy
- [[Changes/Open WebUI/2025-09-25-4-model-support-changes-in-v0-6-31|4 Model Support changes in v0.6.31]] · Model Support
- [[Changes/Open WebUI/2025-09-25-enhanced-user-interface-accessibility-through-the-addition-of-unique-element-ids|♿ Enhanced user interface accessibility through the addition of unique element IDs…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-09-25-2-search-and-browsing-changes-in-v0-6-31|2 Search and Browsing changes in v0.6.31]] · Search and Browsing
- [[Changes/Open WebUI/2025-09-25-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-09-25-image-generation-model-selection-was-centralized-to-enable-dynamic-model-overrid|🎨 Image generation model selection was centralized to enable dynamic model override…]] · Image Generation
- [[Changes/Open WebUI/2025-09-25-4-interface-experience-changes-in-v0-6-31|4 Interface Experience changes in v0.6.31]] · Interface Experience
- [[Changes/Open WebUI/2025-09-25-file-upload-handling-was-improved-to-properly-recognize-uploaded-files-even-when|📎 File upload handling was improved to properly recognize uploaded files even…]] · Files and Data
- [[Changes/Open WebUI/2025-09-25-2-account-and-access-changes-in-v0-6-31|2 Account and Access changes in v0.6.31]] · Account and Access
- [[Changes/Open WebUI/2025-09-25-2-developer-workflow-changes-in-v0-6-31|2 Developer Workflow changes in v0.6.31]] · Developer Workflow
- [[Changes/Open WebUI/2025-09-25-17-other-changes-in-v0-6-31|17 other changes in v0.6.31]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2025-09-24 · LM Studio · [[Changes/LM Studio/2025-09-24-improved-memory-usage-estimation-used-for-model-loading-guardrails|Improved memory usage estimation used for model loading guardrails]]
- Later: 2025-09-26 · Codex CLI · [[Changes/Codex CLI/2025-09-26-stability-and-correctness-token-usage-fix-for-compaction-sse-mounting-reliabilit|Stability and correctness]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-09-25-f7e1b8&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-09-25-5-reliability-and-performance-changes-in-v0-6-31.md%0ACard%20ID%3A%20open-webui-2025-09-25-f7e1b8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.31%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->