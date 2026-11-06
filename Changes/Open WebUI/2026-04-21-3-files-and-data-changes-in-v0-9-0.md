---
card_id: open-webui-2026-04-21-2b39ac
date: '2026-04-21'
description: "Open WebUI · 2026-04-21 · Files and Data: 3 changes in v0.9.0 — \U0001F4E4
  **CSV feedback export.** Feedback history can now be exported as either JSON or
  CSV, making…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2
    Files and Data changes in 0.2.2]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1062
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 33a663ddc19d3ab2738d8f0c8ef239141500b8c4581f6e506e44d4d7945ee9c2
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-2b39ac
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.0: 3 Files and Data changes'
  evidence:
  - quote: "\U0001F4E4 **CSV feedback export.** Feedback history can now be exported
      as either JSON or CSV, making it easier to analyze feedback in spreadsheet tools.
      [Commit](https://github.com/open-webui/open-webui/commit/342582676a5212bf196a69d11825cb407992f257)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9FC **Null-byte document sanitization.** PDF and other document
      ingests now sanitize null bytes and invalid surrogate characters before pgvector
      writes, preventing PostgreSQL upload failures and allowing affected files to
      index successfully. [#22992](https://github.com/open-webui/open-webui/issues/22992),
      [Commit](https://github.com/open-webui/open-webui/commit/8dba798cce9fb1efc5f6acc5f37b152662db78d7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: ➕ **Attachment menu auto-close.** The chat attachment menu now closes immediately
      after selecting upload actions like file upload, camera capture, web attach,
      Google Drive, or OneDrive, preventing the menu from lingering on screen. [Commit](https://github.com/open-webui/open-webui/commit/4764dd5d3765c22384ed38cbc97a8170daa7a75f),
      [#23320](https://github.com/open-webui/open-webui/issues/23320)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-files-and-data-changes-in-v0-9-0
  source_release: open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a
  source_type: github_releases
  theme: file-data
  title: 3 Files and Data changes in v0.9.0
  type: change
related_changes:
- '[[Changes/Cursor/2026-04-13-plan-tabs-now-get-the-same-document-behaviors-as-files-support-for-reliable-load|Plan
  tabs now get the same document behaviors as files]]'
- '[[Changes/Cursor/2026-04-15-cursor-can-now-respond-by-creating-interactive-canvases-c4a1d3|Cursor
  can now respond by creating interactive canvases]]'
- '[[Changes/ElevenLabs/2026-04-20-text-to-dialogue|Text to Dialogue]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a]]'
source_type: github_releases
theme: file-data
title: 3 Files and Data changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Files and Data changes in v0.9.0

**Open WebUI** · 2026-04-21 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.0) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📤 **CSV feedback export.** Feedback history can now be exported as either JSON or CSV, making it easier to analyze feedback in spreadsheet tools. [Commit](https://github.com/open-webui/open-webui/commit/342582676a5212bf196a69d11825cb407992f257)

> 🧼 **Null-byte document sanitization.** PDF and other document ingests now sanitize null bytes and invalid surrogate characters before pgvector writes, preventing PostgreSQL upload failures and allowing affected files to index successfully. [#22992](https://github.com/open-webui/open-webui/issues/22992), [Commit](https://github.com/open-webui/open-webui/commit/8dba798cce9fb1efc5f6acc5f37b152662db78d7)

> ➕ **Attachment menu auto-close.** The chat attachment menu now closes immediately after selecting upload actions like file upload, camera capture, web attach, Google Drive, or OneDrive, preventing the menu from lingering on screen. [Commit](https://github.com/open-webui/open-webui/commit/4764dd5d3765c22384ed38cbc97a8170daa7a75f), [#23320](https://github.com/open-webui/open-webui/issues/23320)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-21-4-image-generation-changes-in-v0-9-0|4 Image Generation changes in v0.9.0]] · Image Generation
- [[Changes/Open WebUI/2026-04-21-28-model-support-changes-in-v0-9-0|28 Model Support changes in v0.9.0]] · Model Support
- [[Changes/Open WebUI/2026-04-21-5-editor-experience-changes-in-v0-9-0|5 Editor Experience changes in v0.9.0]] · Editor Experience
- [[Changes/Open WebUI/2026-04-21-persistent-chat-payload-efficiency-persisted-chats-now-use-server-side-history-l|🚀 Persistent chat payload efficiency. Persisted chats now use server-side…]] · Multimodal Input
- [[Changes/Open WebUI/2026-04-21-8-context-window-changes-in-v0-9-0|8 Context Window changes in v0.9.0]] · Context Window
- [[Changes/Open WebUI/2026-04-21-24-reliability-and-performance-changes-in-v0-9-0|24 Reliability and Performance changes in v0.9.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-21-4-apps-and-integrations-changes-in-v0-9-0|4 Apps and Integrations changes in v0.9.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-21-46-developer-workflow-changes-in-v0-9-0|46 Developer Workflow changes in v0.9.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-04-21-8-automation-and-scheduling-changes-in-v0-9-0|8 Automation and Scheduling changes in v0.9.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-21-7-memory-and-personalization-changes-in-v0-9-0|7 Memory and Personalization changes in v0.9.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-21-2-mobile-and-desktop-changes-in-v0-9-0|2 Mobile and Desktop changes in v0.9.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-04-21-17-interface-experience-changes-in-v0-9-0|17 Interface Experience changes in v0.9.0]] · Interface Experience
- [[Changes/Open WebUI/2026-04-21-11-safety-and-privacy-changes-in-v0-9-0|11 Safety and Privacy changes in v0.9.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-04-21-4-search-and-browsing-changes-in-v0-9-0|4 Search and Browsing changes in v0.9.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-04-21-shared-chat-access-controls-you-can-now-control-who-has-access-to-a-shared-chat|🔗 Shared chat access controls. You can now control who has access to a shared…]] · Collaboration
- [[Changes/Open WebUI/2026-04-21-4-voice-and-audio-changes-in-v0-9-0|4 Voice and Audio changes in v0.9.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-04-21-17-account-and-access-changes-in-v0-9-0|17 Account and Access changes in v0.9.0]] · Account and Access
- [[Changes/Open WebUI/2026-04-21-21-other-changes-in-v0-9-0|21 other changes in v0.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-04-20 · ElevenLabs · [[Changes/ElevenLabs/2026-04-20-text-to-dialogue|Text to Dialogue]]
- Later: 2026-04-23 · Codex CLI · [[Changes/Codex CLI/2026-04-23-18423-chore-document-intentional-await-holding-cases-bolinfest|♯18423 chore: document intentional await-holding cases @bolinfest]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-25 · Dify · [[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2 Files and Data changes in 0.2.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-2b39ac&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-3-files-and-data-changes-in-v0-9-0.md%0ACard%20ID%3A%20open-webui-2026-04-21-2b39ac%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->