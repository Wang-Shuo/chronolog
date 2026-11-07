---
card_id: open-webui-2025-12-21-4f878d
date: '2025-12-21'
description: "Open WebUI · 2025-12-21 · Files and Data: 6 changes in v0.6.42 — \U0001F4CA
  File viewer modal was significantly enhanced with native-like viewers for Excel/CSV…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2
    Files and Data changes in 0.2.2]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 941
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8e5e34308a8e6d91135156ff9ead7b148d249366a3a25671702244bf2c716ad9
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-21-4f878d
  comparison: ''
  date: '2025-12-21'
  description: 'Open WebUI — v0.6.42: 6 Files and Data changes'
  evidence:
  - quote: "\U0001F4CA File viewer modal was significantly enhanced with native-like
      viewers for Excel/CSV spreadsheets rendering as interactive scrollable tables
      with multi-sheet navigation support, Markdown documents displaying with full
      typography including headers, lists, links, and tables, and source code files
      showing syntax highlighting, all accessible through a tabbed interface defaulting
      to raw text view. [#20035](https://github.com/open-webui/open-webui/pull/20035),
      [#2867](https://github.com/open-webui/open-webui/issues/2867)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4CE Channel file association tracking was implemented, automatically
      linking uploaded files to their respective channels with a dedicated association
      table enabling better organization and future file management features within
      channels. [Commit](https://github.com/open-webui/open-webui/commit/2bccf8350d0915f69b8020934bb179c52e81b7b5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: ⏳ The "MINERU_API_TIMEOUT" environment variable now allows configuring
      request timeouts for MinerU document processing operations. [#20016](https://github.com/open-webui/open-webui/pull/20016),
      [#18495](https://github.com/open-webui/open-webui/issues/18495)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4DD Notes \"Improve\" action now works correctly after the streaming
      API change in v0.6.41 by ensuring uploaded files are fully retrieved with complete
      metadata before processing, restoring note improvement and summarization functionality.
      [Commit](https://github.com/open-webui/open-webui/commit/a3458f492c53a3b00405f59fbe1ea953fe364f18),
      [#20078](https://github.com/open-webui/open-webui/discussions/20078)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F5D1️ Legacy knowledge base support for deprecated document collections
      and tag-based collections was removed; users with pre-knowledge base documents
      must migrate to the current knowledge base system as legacy items will no longer
      appear in selectors or command menus. [Commit](https://github.com/open-webui/open-webui/commit/a934dc997ed67a036dd7975e380f8036c447d3ed)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F40D LangChain was upgraded to version 1.2.0, representing a major
      dependency update and significant progress toward Python 3.13 compatibility
      while improving RAG pipeline functionality for document loading and retrieval
      operations. [#19991](https://github.com/open-webui/open-webui/pull/19991)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-files-and-data-changes-in-v0-6-42
  source_release: open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9
  source_type: github_releases
  theme: file-data
  title: 6 Files and Data changes in v0.6.42
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-12-15-8024-docs-document-enabling-experimental-skills|♯8024
  docs: document enabling experimental skills]]'
- '[[Changes/ElevenLabs/2025-12-15-knowledge-base|Knowledge Base]]'
- '[[Changes/ElevenLabs/2025-12-15-new-endpoints|New Endpoints]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9]]'
source_type: github_releases
theme: file-data
title: 6 Files and Data changes in v0.6.42
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Files and Data changes in v0.6.42

**Open WebUI** · 2025-12-21 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.42) · from [[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|v0.6.42]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📊 File viewer modal was significantly enhanced with native-like viewers for Excel/CSV spreadsheets rendering as interactive scrollable tables with multi-sheet navigation support, Markdown documents displaying with full typography including headers, lists, links, and tables, and source code files showing syntax highlighting, all accessible through a tabbed interface defaulting to raw text view. [#20035](https://github.com/open-webui/open-webui/pull/20035), [#2867](https://github.com/open-webui/open-webui/issues/2867)

> 📎 Channel file association tracking was implemented, automatically linking uploaded files to their respective channels with a dedicated association table enabling better organization and future file management features within channels. [Commit](https://github.com/open-webui/open-webui/commit/2bccf8350d0915f69b8020934bb179c52e81b7b5)

> ⏳ The "MINERU_API_TIMEOUT" environment variable now allows configuring request timeouts for MinerU document processing operations. [#20016](https://github.com/open-webui/open-webui/pull/20016), [#18495](https://github.com/open-webui/open-webui/issues/18495)

> 📝 Notes "Improve" action now works correctly after the streaming API change in v0.6.41 by ensuring uploaded files are fully retrieved with complete metadata before processing, restoring note improvement and summarization functionality. [Commit](https://github.com/open-webui/open-webui/commit/a3458f492c53a3b00405f59fbe1ea953fe364f18), [#20078](https://github.com/open-webui/open-webui/discussions/20078)

> 🗑️ Legacy knowledge base support for deprecated document collections and tag-based collections was removed; users with pre-knowledge base documents must migrate to the current knowledge base system as legacy items will no longer appear in selectors or command menus. [Commit](https://github.com/open-webui/open-webui/commit/a934dc997ed67a036dd7975e380f8036c447d3ed)

> 🐍 LangChain was upgraded to version 1.2.0, representing a major dependency update and significant progress toward Python 3.13 compatibility while improving RAG pipeline functionality for document loading and retrieval operations. [#19991](https://github.com/open-webui/open-webui/pull/19991)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-21-user-uploaded-images-are-now-automatically-converted-from-base64-to-actual-file|🖼️ User-uploaded images are now automatically converted from base64 to actual file…]] · Collaboration
- [[Changes/Open WebUI/2025-12-21-3-editor-experience-changes-in-v0-6-42|3 Editor Experience changes in v0.6.42]] · Editor Experience
- [[Changes/Open WebUI/2025-12-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-21-2-apps-and-integrations-changes-in-v0-6-42|2 Apps and Integrations changes in v0.6.42]] · Apps and Integrations
- [[Changes/Open WebUI/2025-12-21-7-reliability-and-performance-changes-in-v0-6-42|7 Reliability and Performance changes in v0.6.42]] · Reliability and Performance
- [[Changes/Open WebUI/2025-12-21-11-model-support-changes-in-v0-6-42|11 Model Support changes in v0.6.42]] · Model Support
- [[Changes/Open WebUI/2025-12-21-6-safety-and-privacy-changes-in-v0-6-42|6 Safety and Privacy changes in v0.6.42]] · Safety and Privacy
- [[Changes/Open WebUI/2025-12-21-8-interface-experience-changes-in-v0-6-42|8 Interface Experience changes in v0.6.42]] · Interface Experience
- [[Changes/Open WebUI/2025-12-21-4-account-and-access-changes-in-v0-6-42|4 Account and Access changes in v0.6.42]] · Account and Access
- [[Changes/Open WebUI/2025-12-21-external-reranker-operations-were-optimized-to-prevent-event-loop-blocking-by-of|⚡ External reranker operations were optimized to prevent event loop blocking…]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-12-21-3-search-and-browsing-changes-in-v0-6-42|3 Search and Browsing changes in v0.6.42]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-21-11-developer-workflow-changes-in-v0-6-42|11 Developer Workflow changes in v0.6.42]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-21-2-multimodal-input-changes-in-v0-6-42|2 Multimodal Input changes in v0.6.42]] · Multimodal Input
- [[Changes/Open WebUI/2025-12-21-4-image-generation-changes-in-v0-6-42|4 Image Generation changes in v0.6.42]] · Image Generation
- [[Changes/Open WebUI/2025-12-21-2-voice-and-audio-changes-in-v0-6-42|2 Voice and Audio changes in v0.6.42]] · Voice and Audio
- [[Changes/Open WebUI/2025-12-21-channel-image-upload-handling-was-optimized-to-process-and-store-compressed-imag|🖼️ Channel image upload handling was optimized to process and store compressed…]] · Memory and Personalization
- [[Changes/Open WebUI/2025-12-21-28-other-changes-in-v0-6-42|28 other changes in v0.6.42]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2025-12-15 · ElevenLabs · [[Changes/ElevenLabs/2025-12-15-new-endpoints|New Endpoints]]
- Later: 2025-12-25 · Dify · [[Changes/Dify/2025-12-25-add-file-upload-enabled-check-and-new-i18n-message-by-halogen22-in-https-github|Add file upload enabled check and new i18n message]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-25 · Dify · [[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2 Files and Data changes in 0.2.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-21-4f878d&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-21-6-files-and-data-changes-in-v0-6-42.md%0ACard%20ID%3A%20open-webui-2025-12-21-4f878d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.42%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->