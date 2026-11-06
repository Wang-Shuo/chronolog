---
card_id: open-webui-2026-10-16-149f19
date: '2026-10-16'
description: "Open WebUI · 2026-10-16 · Files and Data: 4 changes in v0.12.3 — \U0001F4AD
  **Comments in document previews.** Word, Excel, PowerPoint and PDF files opened
  in the…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2
    Files and Data changes in 0.2.2]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1240
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e35e8e738bc24d80620560a3ba428590347d4d09614bb6dd1230b06c3aa8af05
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-16-149f19
  comparison: ''
  date: '2026-10-16'
  description: 'Open WebUI — v0.12.3: 4 Files and Data changes'
  evidence:
  - quote: "\U0001F4AD **Comments in document previews.** Word, Excel, PowerPoint
      and PDF files opened in the terminal file browser now show their comments and
      replies, marked where they belong in the document and opened by hovering or
      tapping a marker, and older .xls spreadsheets can now be previewed too. [Commit](https://github.com/open-webui/open-webui/commit/ba0b2169e1799e1915c6dbb071c56d54896467fb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F4C4 **PDF export of long notes and chats.** Long notes and chats
      now download as PDF, where Firefox failed with \"Canvas exceeds max size\" and
      Chrome saved a black PDF. [#32459](https://github.com/open-webui/open-webui/pull/32459),
      [Commit](https://github.com/open-webui/open-webui/commit/f78e46ef44ecc1a7ea8a4951edc17e22bf1d5cad),
      [#18334](https://github.com/open-webui/open-webui/issues/18334), [#26373](https://github.com/open-webui/open-webui/issues/26373),
      [#19583](https://github.com/open-webui/open-webui/discussions/19583)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F4D1 **Scanned PDF previews.** Previewing a scanned PDF without
      a text layer in the knowledge base viewer no longer scrolls the page up and
      pushes the header and toolbar out of reach. [#32487](https://github.com/open-webui/open-webui/pull/32487),
      [Commit](https://github.com/open-webui/open-webui/commit/1bc5648a7b67c82405f86ed4bd0506f9ae3eb739),
      [#32481](https://github.com/open-webui/open-webui/issues/32481)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F4E5 **PDF links read as documents.** PDFs from sites that block
      unknown clients, such as Wikimedia, and arXiv links like arxiv.org/pdf/1706.03762
      now go to document extraction, where the model got the raw PDF bytes. [#32523](https://github.com/open-webui/open-webui/pull/32523)
      [Commit](https://github.com/open-webui/open-webui/commit/a5942da0a264b4e97a5d6a18adea7d4fcbfc275a)
      [#32524](https://github.com/open-webui/open-webui/pull/32524) [Commit](https://github.com/open-webui/open-webui/commit/823670d9fa925255d3ebf28e55779b8be45a1c3a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-files-and-data-changes-in-v0-12-3
  source_release: open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d
  source_type: github_releases
  theme: file-data
  title: 4 Files and Data changes in v0.12.3
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-14-2-files-and-data-changes-in-v2-1-299|2 Files and
  Data changes in v2.1.299]]'
- '[[Changes/Lovable/2026-10-15-documents-in-the-project-chat-show-their-name-and-type|Documents
  in the project chat show their name and type]]'
- '[[Changes/Lovable/2026-10-15-select-and-sort-files-faster-in-the-files-tab|Select
  and sort files faster in the Files tab]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d|open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d]]'
source_type: github_releases
theme: file-data
title: 4 Files and Data changes in v0.12.3
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Files and Data changes in v0.12.3

**Open WebUI** · 2026-10-16 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.3) · from [[Releases/Open WebUI/open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d|v0.12.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 💭 **Comments in document previews.** Word, Excel, PowerPoint and PDF files opened in the terminal file browser now show their comments and replies, marked where they belong in the document and opened by hovering or tapping a marker, and older .xls spreadsheets can now be previewed too. [Commit](https://github.com/open-webui/open-webui/commit/ba0b2169e1799e1915c6dbb071c56d54896467fb)

> 📄 **PDF export of long notes and chats.** Long notes and chats now download as PDF, where Firefox failed with "Canvas exceeds max size" and Chrome saved a black PDF. [#32459](https://github.com/open-webui/open-webui/pull/32459), [Commit](https://github.com/open-webui/open-webui/commit/f78e46ef44ecc1a7ea8a4951edc17e22bf1d5cad), [#18334](https://github.com/open-webui/open-webui/issues/18334), [#26373](https://github.com/open-webui/open-webui/issues/26373), [#19583](https://github.com/open-webui/open-webui/discussions/19583)

> 📑 **Scanned PDF previews.** Previewing a scanned PDF without a text layer in the knowledge base viewer no longer scrolls the page up and pushes the header and toolbar out of reach. [#32487](https://github.com/open-webui/open-webui/pull/32487), [Commit](https://github.com/open-webui/open-webui/commit/1bc5648a7b67c82405f86ed4bd0506f9ae3eb739), [#32481](https://github.com/open-webui/open-webui/issues/32481)

> 📥 **PDF links read as documents.** PDFs from sites that block unknown clients, such as Wikimedia, and arXiv links like arxiv.org/pdf/1706.03762 now go to document extraction, where the model got the raw PDF bytes. [#32523](https://github.com/open-webui/open-webui/pull/32523) [Commit](https://github.com/open-webui/open-webui/commit/a5942da0a264b4e97a5d6a18adea7d4fcbfc275a) [#32524](https://github.com/open-webui/open-webui/pull/32524) [Commit](https://github.com/open-webui/open-webui/commit/823670d9fa925255d3ebf28e55779b8be45a1c3a)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-16-built-in-tools-turned-back-on-stay-on-a-built-in-tool-such-as-memory-that-is-off|🧰 Built-in tools turned back on stay on. A built-in tool such as Memory…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-16-20-developer-workflow-changes-in-v0-12-3|20 Developer Workflow changes in v0.12.3]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-16-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-16-3-model-support-changes-in-v0-12-3|3 Model Support changes in v0.12.3]] · Model Support
- [[Changes/Open WebUI/2026-10-16-2-account-and-access-changes-in-v0-12-3|2 Account and Access changes in v0.12.3]] · Account and Access
- [[Changes/Open WebUI/2026-10-16-2-enterprise-and-administration-changes-in-v0-12-3|2 Enterprise and Administration changes in v0.12.3]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-16-2-context-window-changes-in-v0-12-3|2 Context Window changes in v0.12.3]] · Context Window
- [[Changes/Open WebUI/2026-10-16-clear-input-selections-shortcut-clearing-the-model-override-selected-tools-and-f|🧹 Clear Input Selections shortcut. Clearing the model override, selected tools…]] · Image Generation
- [[Changes/Open WebUI/2026-10-16-built-in-tools-with-a-custom-tools-parameter-a-model-with-a-custom-parameter-nam|🧩 Built-in tools with a custom tools parameter. A model with a custom parameter…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-16-4-interface-experience-changes-in-v0-12-3|4 Interface Experience changes in v0.12.3]] · Interface Experience
- [[Changes/Open WebUI/2026-10-16-2-editor-experience-changes-in-v0-12-3|2 Editor Experience changes in v0.12.3]] · Editor Experience
- [[Changes/Open WebUI/2026-10-16-2-safety-and-privacy-changes-in-v0-12-3|2 Safety and Privacy changes in v0.12.3]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-16-2-collaboration-changes-in-v0-12-3|2 Collaboration changes in v0.12.3]] · Collaboration
- [[Changes/Open WebUI/2026-10-16-translation-updates-translations-for-portuguese-brazil-chinese-traditional-arabi|🌐 Translation updates. Translations for Portuguese (Brazil), Chinese…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-10-15 · Lovable · [[Changes/Lovable/2026-10-15-select-and-sort-files-faster-in-the-files-tab|Select and sort files faster in the Files tab]]
- Later: 2026-10-16 · v0 · [[Changes/v0/2026-10-16-polished-the-design-mode-canvas-toolbar-and-panel-with-crisper-selection-real-fo|Polished the Design Mode canvas, toolbar, and panel, with crisper selection, real…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-25 · Dify · [[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2 Files and Data changes in 0.2.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-16-149f19&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-16-4-files-and-data-changes-in-v0-12-3.md%0ACard%20ID%3A%20open-webui-2026-10-16-149f19%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->