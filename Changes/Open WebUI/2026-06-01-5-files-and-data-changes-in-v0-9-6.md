---
card_id: open-webui-2026-06-01-446c65
date: '2026-06-01'
description: "Open WebUI · 2026-06-01 · Files and Data: 5 changes in v0.9.6 — \U0001F4C3
  **Legacy Word document support.** Older \".doc\" Word files can now have their text
  extracted…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2
    Files and Data changes in 0.2.2]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1103
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 905408d7a96e9ab915fcf13912a32916ac9fceb8120d148365e830b8c92a7d62
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-01-446c65
  comparison: ''
  date: '2026-06-01'
  description: 'Open WebUI — v0.9.6: 5 Files and Data changes'
  evidence:
  - quote: "\U0001F4C3 **Legacy Word document support.** Older \".doc\" Word files
      can now have their text extracted by the default document extraction engine,
      in addition to the modern \".docx\" format. [Commit](https://github.com/open-webui/open-webui/commit/9e3e24e304f8ff210494380b46f614a2984cafb3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F418 **Knowledge search on large documents.** Searching knowledge
      bases on PostgreSQL no longer fails when scanning across documents with very
      large extracted text content. [#24670](https://github.com/open-webui/open-webui/issues/24670),
      [Commit](https://github.com/open-webui/open-webui/commit/d74ee34d9128295faa116c919bd1dcca77744975)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: ⌨️ **Responsive knowledge file search.** Searching for knowledge files
      in the chat picker and model knowledge selector now matches on file names by
      default instead of scanning the full extracted text of every document on each
      keystroke, keeping the search responsive on large deployments, with content
      search available as an explicit opt-in. [#25082](https://github.com/open-webui/open-webui/issues/25082),
      [#25119](https://github.com/open-webui/open-webui/pull/25119), [Commit](https://github.com/open-webui/open-webui/commit/591e0aafa1d5e21dcd9fa1279dada2076968b9cb)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4E5 **Document processing with empty embeddings.** Saving documents
      to the vector database no longer crashes when an embedding step returns no vectors,
      allowing the process to continue instead of failing the whole upload. [#25166](https://github.com/open-webui/open-webui/issues/25166)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F34E **Safari PDF handling.** PDF processing now works in Safari,
      which doesn't support the stream iteration the previous code relied on. [#25151](https://github.com/open-webui/open-webui/issues/25151),
      [#25473](https://github.com/open-webui/open-webui/pull/25473)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-files-and-data-changes-in-v0-9-6
  source_release: open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e
  source_type: github_releases
  theme: file-data
  title: 5 Files and Data changes in v0.9.6
  type: change
related_changes:
- '[[Changes/Replit/2026-05-29-generate-media-right-on-canvas|Generate media right
  on Canvas]]'
- '[[Changes/Codex CLI/2026-06-01-25110-move-config-document-helpers-into-their-own-module-jif-oai|♯25110
  Move config document helpers into their own module @jif-oai]]'
- '[[Changes/GitHub Copilot CLI/2026-06-01-canvas-providers-can-return-file-urls-in-open-results-for-local-file-previews|Canvas
  providers can return file:// URLs in open results for local file previews]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e]]'
source_type: github_releases
theme: file-data
title: 5 Files and Data changes in v0.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Files and Data changes in v0.9.6

**Open WebUI** · 2026-06-01 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.6) · from [[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📃 **Legacy Word document support.** Older ".doc" Word files can now have their text extracted by the default document extraction engine, in addition to the modern ".docx" format. [Commit](https://github.com/open-webui/open-webui/commit/9e3e24e304f8ff210494380b46f614a2984cafb3)

> 🐘 **Knowledge search on large documents.** Searching knowledge bases on PostgreSQL no longer fails when scanning across documents with very large extracted text content. [#24670](https://github.com/open-webui/open-webui/issues/24670), [Commit](https://github.com/open-webui/open-webui/commit/d74ee34d9128295faa116c919bd1dcca77744975)

> ⌨️ **Responsive knowledge file search.** Searching for knowledge files in the chat picker and model knowledge selector now matches on file names by default instead of scanning the full extracted text of every document on each keystroke, keeping the search responsive on large deployments, with content search available as an explicit opt-in. [#25082](https://github.com/open-webui/open-webui/issues/25082), [#25119](https://github.com/open-webui/open-webui/pull/25119), [Commit](https://github.com/open-webui/open-webui/commit/591e0aafa1d5e21dcd9fa1279dada2076968b9cb)

> 📥 **Document processing with empty embeddings.** Saving documents to the vector database no longer crashes when an embedding step returns no vectors, allowing the process to continue instead of failing the whole upload. [#25166](https://github.com/open-webui/open-webui/issues/25166)

> 🍎 **Safari PDF handling.** PDF processing now works in Safari, which doesn't support the stream iteration the previous code relied on. [#25151](https://github.com/open-webui/open-webui/issues/25151), [#25473](https://github.com/open-webui/open-webui/pull/25473)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-01-bulk-enable-or-disable-automations-automations-can-now-be-enabled-or-disabled-in|🔘 Bulk enable or disable automations. Automations can now be enabled or disabled…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-01-4-context-window-changes-in-v0-9-6|4 Context Window changes in v0.9.6]] · Context Window
- [[Changes/Open WebUI/2026-06-01-2-memory-and-personalization-changes-in-v0-9-6|2 Memory and Personalization changes in v0.9.6]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-01-keyboard-and-screen-reader-access-to-menus-the-integrations-more-options-and-use|♿ Keyboard and screen reader access to menus. The integrations, more-options…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-01-27-developer-workflow-changes-in-v0-9-6|27 Developer Workflow changes in v0.9.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-01-4-interface-experience-changes-in-v0-9-6|4 Interface Experience changes in v0.9.6]] · Interface Experience
- [[Changes/Open WebUI/2026-06-01-4-editor-experience-changes-in-v0-9-6|4 Editor Experience changes in v0.9.6]] · Editor Experience
- [[Changes/Open WebUI/2026-06-01-7-safety-and-privacy-changes-in-v0-9-6|7 Safety and Privacy changes in v0.9.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-01-startup-on-non-unicode-consoles-open-webui-no-longer-crashes-at-startup-when-the|🥾 Startup on non-Unicode consoles. Open WebUI no longer crashes at startup…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-01-youtube-short-link-transcripts-pasting-a-youtu-be-short-link-into-a-chat-now-loa|📺 YouTube short link transcripts. Pasting a "youtu.be" short link into a chat…]] · Multimodal Input
- [[Changes/Open WebUI/2026-06-01-9-search-and-browsing-changes-in-v0-9-6|9 Search and Browsing changes in v0.9.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-01-shared-chat-file-write-protection-access-to-a-file-through-a-shared-chat-now-onl|🔐 Shared-chat file write protection. Access to a file through a shared chat now…]] · Collaboration
- [[Changes/Open WebUI/2026-06-01-2-enterprise-and-administration-changes-in-v0-9-6|2 Enterprise and Administration changes in v0.9.6]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-01-image-generation-with-non-standard-response-headers-image-generation-now-works-w|🖌️ Image generation with non-standard response headers. Image generation now…]] · Image Generation
- [[Changes/Open WebUI/2026-06-01-6-account-and-access-changes-in-v0-9-6|6 Account and Access changes in v0.9.6]] · Account and Access
- [[Changes/Open WebUI/2026-06-01-12-model-support-changes-in-v0-9-6|12 Model Support changes in v0.9.6]] · Model Support
- [[Changes/Open WebUI/2026-06-01-4-apps-and-integrations-changes-in-v0-9-6|4 Apps and Integrations changes in v0.9.6]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-01-5-reliability-and-performance-changes-in-v0-9-6|5 Reliability and Performance changes in v0.9.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-01-4-voice-and-audio-changes-in-v0-9-6|4 Voice and Audio changes in v0.9.6]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-01-20-other-changes-in-v0-9-6|20 other changes in v0.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-06-01 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-01-canvas-providers-can-return-file-urls-in-open-results-for-local-file-previews|Canvas providers can return file:// URLs in open results for local file previews]]
- Later: 2026-06-04 · Codex CLI · [[Changes/Codex CLI/2026-06-04-25682-codex-document-out-of-line-test-module-convention-anp-oai|♯25682 codex document out-of-line test module convention @anp-oai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-25 · Dify · [[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2 Files and Data changes in 0.2.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-01-446c65&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-01-5-files-and-data-changes-in-v0-9-6.md%0ACard%20ID%3A%20open-webui-2026-06-01-446c65%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->