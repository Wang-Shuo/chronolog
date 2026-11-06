---
card_id: open-webui-2026-07-27-e51226
date: '2026-07-27'
description: 'Open WebUI · 2026-07-27 · Files and Data: 9 changes in v0.11.0 — ⚗️
  **Default file upload mode.** You can now choose in settings how attached files
  are handled…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2
    Files and Data changes in 0.2.2]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1159
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 77e7603315492c8fdceb952a51426c4c2fe02ee32f598d03e4269f4d813f5fac
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-27-e51226
  comparison: ''
  date: '2026-07-27'
  description: 'Open WebUI — v0.11.0: 9 Files and Data changes'
  evidence:
  - quote: ⚗️ **Default file upload mode.** You can now choose in settings how attached
      files are handled by default, rather than picking that on each upload. [#20900](https://github.com/open-webui/open-webui/pull/20900),
      [#18431](https://github.com/open-webui/open-webui/issues/18431)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F520 **Tokenizer loaded once.** The tokenizer used to split documents
      is now kept after first use rather than being loaded again for every file. [Commit](https://github.com/open-webui/open-webui/commit/7e31f64bc81b2264136a85efc7bb86c00f346784),
      [#27394](https://github.com/open-webui/open-webui/pull/27394)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4E1 **Lighter live connection handling.** Typing indicators, shared
      document edits and reconnections no longer re-read your account or copy the
      full participant list each time, and idle sessions are no longer rewritten every
      few seconds. [Commit](https://github.com/open-webui/open-webui/commit/021c4c7a2e8b5b213f49800ecd331b1b18c2ef99),
      [#27393](https://github.com/open-webui/open-webui/pull/27393)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4C9 **Charts in the code interpreter.** Code that draws a chart
      now runs in the default code interpreter setup, instead of failing with a syntax
      error unless file persistence was turned on. [#26800](https://github.com/open-webui/open-webui/pull/26800),
      [#26660](https://github.com/open-webui/open-webui/issues/26660)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F5A8️ **PDF text recognition.** The text recognition package is
      now included again, so the application starts and PDFs with image text extraction
      enabled upload correctly instead of failing. [#26851](https://github.com/open-webui/open-webui/pull/26851),
      [#26646](https://github.com/open-webui/open-webui/issues/26646), [#26994](https://github.com/open-webui/open-webui/issues/26994)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9FF **Mistral OCR on a stock install.** Extracting documents with
      Mistral OCR now works out of the box, instead of failing on a missing name resolution
      library that the code assumed was present. [#27440](https://github.com/open-webui/open-webui/pull/27440)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F587️ **Uploads with PaddleOCR-VL selected.** With PaddleOCR-VL
      chosen as the document loader, only PDFs and images now go to it and everything
      else falls back to the usual handling, so text, markdown, spreadsheet and Word
      files index instead of being rejected. [#27529](https://github.com/open-webui/open-webui/pull/27529),
      [#24988](https://github.com/open-webui/open-webui/issues/24988), [#26759](https://github.com/open-webui/open-webui/issues/26759)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4DA **Knowledge base upload reliability.** Adding a file directly
      to a knowledge base now finishes processing and linking the file before reporting
      success, so uploaded files are reliably searchable. [Commit](https://github.com/open-webui/open-webui/commit/f5b196c060805fd22e1aa1c9f738b60221ef0fd8)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4DB **Failures after a tool call.** A reply that fails while continuing
      after a tool call or a code interpreter run now says so, instead of stopping
      mid-answer with nothing to explain why. [Commit](https://github.com/open-webui/open-webui/commit/8ab44ed3b153dd8d8d57a444c98d100f281f7f7e),
      [#27426](https://github.com/open-webui/open-webui/pull/27426), [#27411](https://github.com/open-webui/open-webui/issues/27411)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 9-files-and-data-changes-in-v0-11-0
  source_release: open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f
  source_type: github_releases
  theme: file-data
  title: 9 Files and Data changes in v0.11.0
  type: change
related_changes:
- '[[Changes/Dify/2026-07-17-2-files-and-data-changes-in-1-16-0|2 Files and Data changes
  in 1.16.0]]'
- '[[Changes/Codex CLI/2026-07-21-33167-document-the-windows-exec-yield-time-range-copyberry|♯33167
  Document the Windows exec yield time range @copyberry]]'
- '[[Changes/ChatGPT/2026-07-23-we-re-starting-to-roll-out-a-new-health-experience-in-chatgpt-logged-in-free-go-b62f3b|We’re
  starting to roll out a new health experience in ChatGPT]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f]]'
source_type: github_releases
theme: file-data
title: 9 Files and Data changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Files and Data changes in v0.11.0

**Open WebUI** · 2026-07-27 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.0) · from [[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ⚗️ **Default file upload mode.** You can now choose in settings how attached files are handled by default, rather than picking that on each upload. [#20900](https://github.com/open-webui/open-webui/pull/20900), [#18431](https://github.com/open-webui/open-webui/issues/18431)

> 🔠 **Tokenizer loaded once.** The tokenizer used to split documents is now kept after first use rather than being loaded again for every file. [Commit](https://github.com/open-webui/open-webui/commit/7e31f64bc81b2264136a85efc7bb86c00f346784), [#27394](https://github.com/open-webui/open-webui/pull/27394)

> 📡 **Lighter live connection handling.** Typing indicators, shared document edits and reconnections no longer re-read your account or copy the full participant list each time, and idle sessions are no longer rewritten every few seconds. [Commit](https://github.com/open-webui/open-webui/commit/021c4c7a2e8b5b213f49800ecd331b1b18c2ef99), [#27393](https://github.com/open-webui/open-webui/pull/27393)

> 📉 **Charts in the code interpreter.** Code that draws a chart now runs in the default code interpreter setup, instead of failing with a syntax error unless file persistence was turned on. [#26800](https://github.com/open-webui/open-webui/pull/26800), [#26660](https://github.com/open-webui/open-webui/issues/26660)

> 🖨️ **PDF text recognition.** The text recognition package is now included again, so the application starts and PDFs with image text extraction enabled upload correctly instead of failing. [#26851](https://github.com/open-webui/open-webui/pull/26851), [#26646](https://github.com/open-webui/open-webui/issues/26646), [#26994](https://github.com/open-webui/open-webui/issues/26994)

> 🧿 **Mistral OCR on a stock install.** Extracting documents with Mistral OCR now works out of the box, instead of failing on a missing name resolution library that the code assumed was present. [#27440](https://github.com/open-webui/open-webui/pull/27440)

> 🖇️ **Uploads with PaddleOCR-VL selected.** With PaddleOCR-VL chosen as the document loader, only PDFs and images now go to it and everything else falls back to the usual handling, so text, markdown, spreadsheet and Word files index instead of being rejected. [#27529](https://github.com/open-webui/open-webui/pull/27529), [#24988](https://github.com/open-webui/open-webui/issues/24988), [#26759](https://github.com/open-webui/open-webui/issues/26759)

> 📚 **Knowledge base upload reliability.** Adding a file directly to a knowledge base now finishes processing and linking the file before reporting success, so uploaded files are reliably searchable. [Commit](https://github.com/open-webui/open-webui/commit/f5b196c060805fd22e1aa1c9f738b60221ef0fd8)

> 📛 **Failures after a tool call.** A reply that fails while continuing after a tool call or a code interpreter run now says so, instead of stopping mid-answer with nothing to explain why. [Commit](https://github.com/open-webui/open-webui/commit/8ab44ed3b153dd8d8d57a444c98d100f281f7f7e), [#27426](https://github.com/open-webui/open-webui/pull/27426), [#27411](https://github.com/open-webui/open-webui/issues/27411)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-27-9-automation-and-scheduling-changes-in-v0-11-0|9 Automation and Scheduling changes in v0.11.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety and Privacy changes in v0.11.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-27-4-voice-and-audio-changes-in-v0-11-0|4 Voice and Audio changes in v0.11.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-07-27-62-developer-workflow-changes-in-v0-11-0|62 Developer Workflow changes in v0.11.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-27-19-interface-experience-changes-in-v0-11-0|19 Interface Experience changes in v0.11.0]] · Interface Experience
- [[Changes/Open WebUI/2026-07-27-7-memory-and-personalization-changes-in-v0-11-0|7 Memory and Personalization changes in v0.11.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-07-27-sub-agents-administrators-can-now-enable-sub-agents-which-let-a-model-hand-parts|🤖 Sub-agents. Administrators can now enable sub-agents, which let a model hand…]] · Agent Mode
- [[Changes/Open WebUI/2026-07-27-media-types-an-extraction-engine-may-handle-administrators-can-now-list-which-im|🖼️ Media types an extraction engine may handle. Administrators can now list…]] · Multimodal Input
- [[Changes/Open WebUI/2026-07-27-15-account-and-access-changes-in-v0-11-0|15 Account and Access changes in v0.11.0]] · Account and Access
- [[Changes/Open WebUI/2026-07-27-shared-image-checkpoint-changes-only-administrators-can-now-change-the-instance|🖌️ Shared image checkpoint changes. Only administrators can now change…]] · Image Generation
- [[Changes/Open WebUI/2026-07-27-7-search-and-browsing-changes-in-v0-11-0|7 Search and Browsing changes in v0.11.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-07-27-2-collaboration-changes-in-v0-11-0|2 Collaboration changes in v0.11.0]] · Collaboration
- [[Changes/Open WebUI/2026-07-27-6-apps-and-integrations-changes-in-v0-11-0|6 Apps and Integrations changes in v0.11.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-07-27-3-enterprise-and-administration-changes-in-v0-11-0|3 Enterprise and Administration changes in v0.11.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-07-27-9-context-window-changes-in-v0-11-0|9 Context Window changes in v0.11.0]] · Context Window
- [[Changes/Open WebUI/2026-07-27-12-reliability-and-performance-changes-in-v0-11-0|12 Reliability and Performance changes in v0.11.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-07-27-2-pricing-model-changes-in-v0-11-0|2 Pricing Model changes in v0.11.0]] · Pricing Model
- [[Changes/Open WebUI/2026-07-27-39-model-support-changes-in-v0-11-0|39 Model Support changes in v0.11.0]] · Model Support
- [[Changes/Open WebUI/2026-07-27-7-editor-experience-changes-in-v0-11-0|7 Editor Experience changes in v0.11.0]] · Editor Experience
- [[Changes/Open WebUI/2026-07-27-2-mobile-and-desktop-changes-in-v0-11-0|2 Mobile and Desktop changes in v0.11.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-07-27-42-other-changes-in-v0-11-0|42 other changes in v0.11.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-07-23 · ChatGPT · [[Changes/ChatGPT/2026-07-23-we-re-starting-to-roll-out-a-new-health-experience-in-chatgpt-logged-in-free-go-b62f3b|We’re starting to roll out a new health experience in ChatGPT]]
- Later: 2026-07-28 · Dify · [[Changes/Dify/2026-07-28-3-files-and-data-changes-in-1-16-1|3 Files and Data changes in 1.16.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-25 · Dify · [[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2 Files and Data changes in 0.2.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-27-e51226&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-27-9-files-and-data-changes-in-v0-11-0.md%0ACard%20ID%3A%20open-webui-2026-07-27-e51226%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->