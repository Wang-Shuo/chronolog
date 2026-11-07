---
card_id: open-webui-2026-01-09-4e81f2
date: '2026-01-09'
description: "Open WebUI · 2026-01-09 · Files and Data: 5 changes in v0.7.0 — \U0001F517
  Users can now click citation content links to jump directly to the relevant portion
  of source…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode
    offset]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2305
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5c0f693ded10d0264a04a062c8b3f9ed72e09d1b12a3021ff9307d4ea5d0b4fc
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-01-09-4e81f2
  comparison: ''
  date: '2026-01-09'
  description: 'Open WebUI — v0.7.0: 5 Files and Data changes'
  evidence:
  - quote: "\U0001F517 Users can now click citation content links to jump directly
      to the relevant portion of source documents with automatic text highlighting,
      making it easier to verify AI responses against their original sources. [#20116](https://github.com/open-webui/open-webui/pull/20116),
      [Commit](https://github.com/open-webui/open-webui/commit/40c45ffe1f9b45538d32c8ecba8cac62c6eca503)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F9E9 Administrators can now set a minimum chunk size target using
      the \"CHUNK_MIN_SIZE_TARGET\" setting to merge small markdown header chunks
      with neighbors, which improves retrieval quality by eliminating tiny meaningless
      fragments, significantly speeds up document processing and embedding, reduces
      storage costs, and lowers embedding API costs or local compute requirements.
      [#19595](https://github.com/open-webui/open-webui/issues/19595), [#20314](https://github.com/open-webui/open-webui/pull/20314),
      [Commit](https://github.com/open-webui/open-webui/commit/c32435958073cf002d87e78544baa88bc4e15d7f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4BE Administrators can now use openGauss as the vector database
      backend for knowledge base document storage and retrieval. [#20179](https://github.com/open-webui/open-webui/pull/20179)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4C4 Administrators can now properly configure the MinerU document
      parsing service as the MinerU Cloud API key field is now available in the Admin
      Panel Documents settings. [#20319](https://github.com/open-webui/open-webui/issues/20319),
      [#20328](https://github.com/open-webui/open-webui/pull/20328)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4DD Administrators who previously used the standalone \"Markdown
      (Header)\" text splitter must now switch to \"character\" or \"token\" mode
      with the new \"ENABLE_MARKDOWN_HEADER_TEXT_SPLITTER\" toggle enabled, as document
      chunking now applies markdown header splitting as a preprocessing step before
      character or token splitting. [Commit](https://github.com/open-webui/open-webui/commit/d3a682759f375c6cb0bc8c170f62863a070f712e),
      [Commit](https://github.com/open-webui/open-webui/commit/18a33a079bf07487edffc421a721c86194cc90c9),
      [Commit](https://github.com/open-webui/open-webui/commit/08bf4670ec862018f9dc57296cb19fd5eab14ef6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-files-and-data-changes-in-v0-7-0
  source_release: open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c
  source_type: github_releases
  theme: file-data
  title: 5 Files and Data changes in v0.7.0
  type: change
related_changes:
- '[[Changes/Dify/2025-12-25-add-file-upload-enabled-check-and-new-i18n-message-by-halogen22-in-https-github|Add
  file upload enabled check and new i18n message]]'
- '[[Changes/Cline/2026-01-09-revert-8341-due-to-regressions-in-diff-view-document-truncation-see-8423-8429|Revert
  ♯8341 due to regressions in diff view/document truncation (see ♯8423, ♯8429)]]'
- '[[Changes/Codex CLI/2026-01-09-app-server-readme-now-documents-skills-support-and-usage-8853|App-server
  README now documents skills support and usage]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c]]'
source_type: github_releases
theme: file-data
title: 5 Files and Data changes in v0.7.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Files and Data changes in v0.7.0

**Open WebUI** · 2026-01-09 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.7.0) · from [[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|v0.7.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔗 Users can now click citation content links to jump directly to the relevant portion of source documents with automatic text highlighting, making it easier to verify AI responses against their original sources. [#20116](https://github.com/open-webui/open-webui/pull/20116), [Commit](https://github.com/open-webui/open-webui/commit/40c45ffe1f9b45538d32c8ecba8cac62c6eca503)

> 🧩 Administrators can now set a minimum chunk size target using the "CHUNK_MIN_SIZE_TARGET" setting to merge small markdown header chunks with neighbors, which improves retrieval quality by eliminating tiny meaningless fragments, significantly speeds up document processing and embedding, reduces storage costs, and lowers embedding API costs or local compute requirements. [#19595](https://github.com/open-webui/open-webui/issues/19595), [#20314](https://github.com/open-webui/open-webui/pull/20314), [Commit](https://github.com/open-webui/open-webui/commit/c32435958073cf002d87e78544baa88bc4e15d7f)

> 💾 Administrators can now use openGauss as the vector database backend for knowledge base document storage and retrieval. [#20179](https://github.com/open-webui/open-webui/pull/20179)

> 📄 Administrators can now properly configure the MinerU document parsing service as the MinerU Cloud API key field is now available in the Admin Panel Documents settings. [#20319](https://github.com/open-webui/open-webui/issues/20319), [#20328](https://github.com/open-webui/open-webui/pull/20328)

> 📝 Administrators who previously used the standalone "Markdown (Header)" text splitter must now switch to "character" or "token" mode with the new "ENABLE_MARKDOWN_HEADER_TEXT_SPLITTER" toggle enabled, as document chunking now applies markdown header splitting as a preprocessing step before character or token splitting. [Commit](https://github.com/open-webui/open-webui/commit/d3a682759f375c6cb0bc8c170f62863a070f712e), [Commit](https://github.com/open-webui/open-webui/commit/18a33a079bf07487edffc421a721c86194cc90c9), [Commit](https://github.com/open-webui/open-webui/commit/08bf4670ec862018f9dc57296cb19fd5eab14ef6)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-01-09-3-editor-experience-changes-in-v0-7-0|3 Editor Experience changes in v0.7.0]] · Editor Experience
- [[Changes/Open WebUI/2026-01-09-users-on-windows-now-see-correctly-preserved-line-breaks-when-using-the-clipboar|📋 Users on Windows now see correctly preserved line breaks when using…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-01-09-2-memory-and-personalization-changes-in-v0-7-0|2 Memory and Personalization changes in v0.7.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-01-09-4-search-and-browsing-changes-in-v0-7-0|4 Search and Browsing changes in v0.7.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-01-09-3-apps-and-integrations-changes-in-v0-7-0|3 Apps and Integrations changes in v0.7.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-01-09-3-context-window-changes-in-v0-7-0|3 Context Window changes in v0.7.0]] · Context Window
- [[Changes/Open WebUI/2026-01-09-9-reliability-and-performance-changes-in-v0-7-0|9 Reliability and Performance changes in v0.7.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-01-09-6-safety-and-privacy-changes-in-v0-7-0|6 Safety and Privacy changes in v0.7.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-01-09-3-account-and-access-changes-in-v0-7-0|3 Account and Access changes in v0.7.0]] · Account and Access
- [[Changes/Open WebUI/2026-01-09-4-image-generation-changes-in-v0-7-0|4 Image Generation changes in v0.7.0]] · Image Generation
- [[Changes/Open WebUI/2026-01-09-5-interface-experience-changes-in-v0-7-0|5 Interface Experience changes in v0.7.0]] · Interface Experience
- [[Changes/Open WebUI/2026-01-09-11-model-support-changes-in-v0-7-0|11 Model Support changes in v0.7.0]] · Model Support
- [[Changes/Open WebUI/2026-01-09-24-developer-workflow-changes-in-v0-7-0|24 Developer Workflow changes in v0.7.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-01-09-3-voice-and-audio-changes-in-v0-7-0|3 Voice and Audio changes in v0.7.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-01-09-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-01-09-26-other-changes-in-v0-7-0|26 other changes in v0.7.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-01-09 · Codex CLI · [[Changes/Codex CLI/2026-01-09-app-server-readme-now-documents-skills-support-and-usage-8853|App-server README now documents skills support and usage]]
- Later: 2026-01-09 · OpenCode · [[Changes/OpenCode/2026-01-09-core-document-cargofmt-in-docs|Core Document cargofmt in docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode offset]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-01-09-4e81f2&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-01-09-5-files-and-data-changes-in-v0-7-0.md%0ACard%20ID%3A%20open-webui-2026-01-09-4e81f2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.7.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->