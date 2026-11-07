---
card_id: open-webui-2025-12-21-c87345
date: '2025-12-21'
description: "Open WebUI · 2025-12-21 · Developer Workflow: 11 changes in v0.6.42
  — \U0001F5C2️ Knowledge workspace listing now uses server-side pagination loading
  30 collections at…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2658
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0e92b93480522ed033cbfafba1b8deba941d36cd60d36d7afc5ef8b3737ea7c0
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-21-c87345
  comparison: ''
  date: '2025-12-21'
  description: 'Open WebUI — v0.6.42: 11 Developer Workflow changes'
  evidence:
  - quote: "\U0001F5C2️ Knowledge workspace listing now uses server-side pagination
      loading 30 collections at a time with new search endpoints supporting query
      filtering and view options for created versus shared collections. [Commit](https://github.com/open-webui/open-webui/commit/ceae3d48e603f53313d5483abe94099e20e914e8)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4D6 Knowledge workspace now displays all collections with read
      access including shared read-only collections, enabling users to discover and
      explore knowledge bases they don't own while maintaining proper access controls
      through visual \"Read Only\" badges and automatically disabled editing controls
      for name, description, file uploads, content editing, and deletion operations.
      [Commit](https://github.com/open-webui/open-webui/commit/693636d971d0e8398fa0c9ec3897686750007af5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4CB Chat file associations are now properly tracked in the database
      through a new \"chat_file\" table, enabling accurate file management across
      chats and ensuring proper cleanup of files when chats are deleted, while improving
      database consistency in multi-node deployments. [Commit](https://github.com/open-webui/open-webui/commit/f1bf4f20c53e6493f0eb6fa2f12cb84c2d22da52)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F465 User profile previews now display group membership information
      for easier identification of user roles and permissions. [Commit](https://github.com/open-webui/open-webui/commit/2b1a29d44bde9fbc20ff9f0a5ded1ce8ded9d90d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4E1 A new /feedbacks/all/ids API endpoint was added to return only
      feedback IDs without metadata, significantly improving performance for external
      integrations working with large feedback collections. [Commit](https://github.com/open-webui/open-webui/commit/53c1ca64b7205d85f6de06bd69e3e265d15546b8)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F9E9 Chat loading failures when channels permissions were disabled
      are now prevented through graceful error handling. [Commit](https://github.com/open-webui/open-webui/commit/5c2df97f04cce5cb7087d288f816f91a739688c1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F464 User list popup display in the admin panel was fixed to correctly
      track user identity when sorting or filtering changes the list order, preventing
      popups from showing incorrect user information. [Commit](https://github.com/open-webui/open-webui/commit/ae47101dc6aef2c7d8ae0d843985341fff820057),
      [#20046](https://github.com/open-webui/open-webui/issues/20046)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4C4 DOCX file parsing now works correctly in temporary chats through
      client-side text extraction, preventing raw data from being displayed. [Commit](https://github.com/open-webui/open-webui/commit/6993b0b40b10af8cdbe6626702cc94080fff9e22)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F534 Redis cluster compatibility issues with disabled KEYS command
      were resolved by replacing blocking KEYS operations with production-safe SCAN
      iterations. [#19871](https://github.com/open-webui/open-webui/pull/19871), [#15834](https://github.com/open-webui/open-webui/issues/15834)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4AB Channel name length is now limited to 128 characters with validation
      to prevent display issues caused by excessively long names. [Commit](https://github.com/open-webui/open-webui/commit/f509f5542dde384d34402f6df763f49a06bea109)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F50E Bocha search with filter list functionality now works correctly
      by returning results as a list instead of a dictionary wrapper, ensuring compatibility
      with result filtering operations. [Commit](https://github.com/open-webui/open-webui/commit/b5bd8704fe1672da839bb3be6210d7cb494797ce),
      [#19733](https://github.com/open-webui/open-webui/issues/19733)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 11-developer-workflow-changes-in-v0-6-42
  source_release: open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9
  source_type: github_releases
  theme: developer-workflow
  title: 11 Developer Workflow changes in v0.6.42
  type: change
related_changes:
- '[[Changes/Claude Code/2025-12-19-2-developer-workflow-changes-in-v2-0-74|2 Developer
  Workflow changes in v2.0.74]]'
- '[[Changes/Codex CLI/2025-12-19-6-developer-workflow-changes-in-rust-v0-76-0|6 Developer
  Workflow changes in rust-v0.76.0]]'
- '[[Changes/OpenCode/2025-12-19-2-developer-workflow-changes-in-v1-0-170|2 Developer
  Workflow changes in v1.0.170]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9]]'
source_type: github_releases
theme: developer-workflow
title: 11 Developer Workflow changes in v0.6.42
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Developer Workflow changes in v0.6.42

**Open WebUI** · 2025-12-21 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.42) · from [[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|v0.6.42]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗂️ Knowledge workspace listing now uses server-side pagination loading 30 collections at a time with new search endpoints supporting query filtering and view options for created versus shared collections. [Commit](https://github.com/open-webui/open-webui/commit/ceae3d48e603f53313d5483abe94099e20e914e8)

> 📖 Knowledge workspace now displays all collections with read access including shared read-only collections, enabling users to discover and explore knowledge bases they don't own while maintaining proper access controls through visual "Read Only" badges and automatically disabled editing controls for name, description, file uploads, content editing, and deletion operations. [Commit](https://github.com/open-webui/open-webui/commit/693636d971d0e8398fa0c9ec3897686750007af5)

> 📋 Chat file associations are now properly tracked in the database through a new "chat_file" table, enabling accurate file management across chats and ensuring proper cleanup of files when chats are deleted, while improving database consistency in multi-node deployments. [Commit](https://github.com/open-webui/open-webui/commit/f1bf4f20c53e6493f0eb6fa2f12cb84c2d22da52)

> 👥 User profile previews now display group membership information for easier identification of user roles and permissions. [Commit](https://github.com/open-webui/open-webui/commit/2b1a29d44bde9fbc20ff9f0a5ded1ce8ded9d90d)

> 📡 A new /feedbacks/all/ids API endpoint was added to return only feedback IDs without metadata, significantly improving performance for external integrations working with large feedback collections. [Commit](https://github.com/open-webui/open-webui/commit/53c1ca64b7205d85f6de06bd69e3e265d15546b8)

> 🧩 Chat loading failures when channels permissions were disabled are now prevented through graceful error handling. [Commit](https://github.com/open-webui/open-webui/commit/5c2df97f04cce5cb7087d288f816f91a739688c1)

> 👤 User list popup display in the admin panel was fixed to correctly track user identity when sorting or filtering changes the list order, preventing popups from showing incorrect user information. [Commit](https://github.com/open-webui/open-webui/commit/ae47101dc6aef2c7d8ae0d843985341fff820057), [#20046](https://github.com/open-webui/open-webui/issues/20046)

> 📄 DOCX file parsing now works correctly in temporary chats through client-side text extraction, preventing raw data from being displayed. [Commit](https://github.com/open-webui/open-webui/commit/6993b0b40b10af8cdbe6626702cc94080fff9e22)

> 🔴 Redis cluster compatibility issues with disabled KEYS command were resolved by replacing blocking KEYS operations with production-safe SCAN iterations. [#19871](https://github.com/open-webui/open-webui/pull/19871), [#15834](https://github.com/open-webui/open-webui/issues/15834)

> 💫 Channel name length is now limited to 128 characters with validation to prevent display issues caused by excessively long names. [Commit](https://github.com/open-webui/open-webui/commit/f509f5542dde384d34402f6df763f49a06bea109)

> 🔎 Bocha search with filter list functionality now works correctly by returning results as a list instead of a dictionary wrapper, ensuring compatibility with result filtering operations. [Commit](https://github.com/open-webui/open-webui/commit/b5bd8704fe1672da839bb3be6210d7cb494797ce), [#19733](https://github.com/open-webui/open-webui/issues/19733)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-21-user-uploaded-images-are-now-automatically-converted-from-base64-to-actual-file|🖼️ User-uploaded images are now automatically converted from base64 to actual file…]] · Collaboration
- [[Changes/Open WebUI/2025-12-21-3-editor-experience-changes-in-v0-6-42|3 Editor Experience changes in v0.6.42]] · Editor Experience
- [[Changes/Open WebUI/2025-12-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-21-2-apps-and-integrations-changes-in-v0-6-42|2 Apps and Integrations changes in v0.6.42]] · Apps and Integrations
- [[Changes/Open WebUI/2025-12-21-6-files-and-data-changes-in-v0-6-42|6 Files and Data changes in v0.6.42]] · Files and Data
- [[Changes/Open WebUI/2025-12-21-7-reliability-and-performance-changes-in-v0-6-42|7 Reliability and Performance changes in v0.6.42]] · Reliability and Performance
- [[Changes/Open WebUI/2025-12-21-11-model-support-changes-in-v0-6-42|11 Model Support changes in v0.6.42]] · Model Support
- [[Changes/Open WebUI/2025-12-21-6-safety-and-privacy-changes-in-v0-6-42|6 Safety and Privacy changes in v0.6.42]] · Safety and Privacy
- [[Changes/Open WebUI/2025-12-21-8-interface-experience-changes-in-v0-6-42|8 Interface Experience changes in v0.6.42]] · Interface Experience
- [[Changes/Open WebUI/2025-12-21-4-account-and-access-changes-in-v0-6-42|4 Account and Access changes in v0.6.42]] · Account and Access
- [[Changes/Open WebUI/2025-12-21-external-reranker-operations-were-optimized-to-prevent-event-loop-blocking-by-of|⚡ External reranker operations were optimized to prevent event loop blocking…]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-12-21-3-search-and-browsing-changes-in-v0-6-42|3 Search and Browsing changes in v0.6.42]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-21-2-multimodal-input-changes-in-v0-6-42|2 Multimodal Input changes in v0.6.42]] · Multimodal Input
- [[Changes/Open WebUI/2025-12-21-4-image-generation-changes-in-v0-6-42|4 Image Generation changes in v0.6.42]] · Image Generation
- [[Changes/Open WebUI/2025-12-21-2-voice-and-audio-changes-in-v0-6-42|2 Voice and Audio changes in v0.6.42]] · Voice and Audio
- [[Changes/Open WebUI/2025-12-21-channel-image-upload-handling-was-optimized-to-process-and-store-compressed-imag|🖼️ Channel image upload handling was optimized to process and store compressed…]] · Memory and Personalization
- [[Changes/Open WebUI/2025-12-21-28-other-changes-in-v0-6-42|28 other changes in v0.6.42]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2025-12-19 · OpenCode · [[Changes/OpenCode/2025-12-19-2-developer-workflow-changes-in-v1-0-170|2 Developer Workflow changes in v1.0.170]]
- Later: 2025-12-22 · Cline · [[Changes/Cline/2025-12-22-enhanced-background-terminal-execution-with-command-tracking-log-file-output-zom|Enhanced background terminal execution with command tracking, log file output…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-21-c87345&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-21-11-developer-workflow-changes-in-v0-6-42.md%0ACard%20ID%3A%20open-webui-2025-12-21-c87345%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.42%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->