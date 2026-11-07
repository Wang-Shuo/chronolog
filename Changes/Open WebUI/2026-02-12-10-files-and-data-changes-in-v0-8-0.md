---
card_id: open-webui-2026-02-12-ce528c
date: '2026-02-12'
description: "Open WebUI · 2026-02-12 · Files and Data: 10 changes in v0.8.0 — \U0001F40D
  **Native function calling code execution.** Code execution now works with Native
  function…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode
    offset]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2339
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4100f1edc8ed53e07b0a14c89e3e14b0332383d319a35b70267f98496dae2416
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-12-ce528c
  comparison: ''
  date: '2026-02-12'
  description: 'Open WebUI — v0.8.0: 10 Files and Data changes'
  evidence:
  - quote: "\U0001F40D **Native function calling code execution.** Code execution
      now works with Native function calling mode, allowing models to autonomously
      run Python code for calculations, data analysis, and visualizations without
      requiring Default mode. [#20592](https://github.com/open-webui/open-webui/pull/20592),
      [Docs:#998](https://github.com/open-webui/docs/pull/998)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4C1 **User file management.** Users can now view, search, and delete
      all their uploaded files from Settings, providing centralized file management
      in one place. [Commit](https://github.com/open-webui/open-webui/commit/93ed4ae2cda2f4311143e51f586aaa73b83a37a7),
      [#21047](https://github.com/open-webui/open-webui/pull/21047)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4D1 **PDF loading modes.** Administrators can now choose between
      \"page\" and \"single\" PDF loading modes, allowing documents to be processed
      as individual pages or as complete documents for better chunking across page
      boundaries. [Commit](https://github.com/open-webui/open-webui/commit/ecbdef732bc71a07c21bbb679edb420f26eac181)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4DA **Knowledge base file upload fix.** Uploading files to knowledge
      bases now works correctly, fixing database mapping errors that prevented file
      uploads. [#20925](https://github.com/open-webui/open-webui/issues/20925), [#20931](https://github.com/open-webui/open-webui/pull/20931)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F527 **Multi-worker knowledge base timeout fix.** In multi-worker
      deployments, uploading very large documents to knowledge bases no longer causes
      workers to be killed by health check timeouts, and administrators can now configure
      a custom embedding timeout via \"RAG_EMBEDDING_TIMEOUT\". [#21158](https://github.com/open-webui/open-webui/pull/21158),
      [Discussion](https://github.com/open-webui/open-webui/discussions/21151), [Commit](https://github.com/open-webui/open-webui/commit/c653e4ec54d070aee5e9568d016daebb61f06632)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4C4 **Markdown Header Text Splitter persistence.** The \"Markdown
      Header Text Splitter\" document setting now persists correctly when disabled,
      preventing it from reverting to enabled after page refresh. [#20929](https://github.com/open-webui/open-webui/issues/20929),
      [#20930](https://github.com/open-webui/open-webui/pull/20930)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4DA **Knowledge base pagination fix.** Paginating through knowledge
      base files no longer shows duplicates or skips files when multiple documents
      share the same update timestamp. [#20846](https://github.com/open-webui/open-webui/issues/20846),
      [Commit](https://github.com/open-webui/open-webui/commit/a9a0ce6beaa286cc18eff24b518a6f3d7a560e2f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F433 **Airgapped NLTK tokenizer fix.** Document extraction now works
      reliably in airgapped environments after container restarts by bundling NLTK
      tokenizer data in the Docker image. [#21165](https://github.com/open-webui/open-webui/pull/21165),
      [#21150](https://github.com/open-webui/open-webui/issues/21150)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4BE **File upload settings persistence.** File upload settings
      (Max Upload Size, Max File Count, Image Compression dimensions) now persist
      correctly and are no longer erased when updating other RAG configuration settings.
      [#21057](https://github.com/open-webui/open-webui/issues/21057), [Commit](https://github.com/open-webui/open-webui/commit/258454276e1ef8ded24968515f7bf5e1833ca011)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F6E0️ **OpenSearch 3.0 compatibility fix.** Document uploads to
      knowledge bases now work correctly when using OpenSearch backend with opensearch-py
      >= 3.0.0, fixing a TypeError that previously caused failures. [#21248](https://github.com/open-webui/open-webui/pull/21248),
      [#20649](https://github.com/open-webui/open-webui/issues/20649)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 10-files-and-data-changes-in-v0-8-0
  source_release: open-webui-2026-02-12-v0-8-0-github-285910626-490914ba
  source_type: github_releases
  theme: file-data
  title: 10 Files and Data changes in v0.8.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-04-improved-pdf-and-request-size-error-messages-to-show-actual-limits-100-pages-20m|Improved
  PDF and request size error messages to show actual limits (100 pages, 20MB)]]'
- '[[Changes/Codex CLI/2026-02-05-10667-chore-app-server-document-experimental-api-opt-in-owenlin0|♯10667
  chore(app-server): document experimental API opt-in @owenlin0]]'
- '[[Changes/Dify/2026-02-11-2-files-and-data-changes-in-1-13-0|2 Files and Data changes
  in 1.13.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|open-webui-2026-02-12-v0-8-0-github-285910626-490914ba]]'
source_type: github_releases
theme: file-data
title: 10 Files and Data changes in v0.8.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Files and Data changes in v0.8.0

**Open WebUI** · 2026-02-12 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.0) · from [[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|v0.8.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🐍 **Native function calling code execution.** Code execution now works with Native function calling mode, allowing models to autonomously run Python code for calculations, data analysis, and visualizations without requiring Default mode. [#20592](https://github.com/open-webui/open-webui/pull/20592), [Docs:#998](https://github.com/open-webui/docs/pull/998)

> 📁 **User file management.** Users can now view, search, and delete all their uploaded files from Settings, providing centralized file management in one place. [Commit](https://github.com/open-webui/open-webui/commit/93ed4ae2cda2f4311143e51f586aaa73b83a37a7), [#21047](https://github.com/open-webui/open-webui/pull/21047)

> 📑 **PDF loading modes.** Administrators can now choose between "page" and "single" PDF loading modes, allowing documents to be processed as individual pages or as complete documents for better chunking across page boundaries. [Commit](https://github.com/open-webui/open-webui/commit/ecbdef732bc71a07c21bbb679edb420f26eac181)

> 📚 **Knowledge base file upload fix.** Uploading files to knowledge bases now works correctly, fixing database mapping errors that prevented file uploads. [#20925](https://github.com/open-webui/open-webui/issues/20925), [#20931](https://github.com/open-webui/open-webui/pull/20931)

> 🔧 **Multi-worker knowledge base timeout fix.** In multi-worker deployments, uploading very large documents to knowledge bases no longer causes workers to be killed by health check timeouts, and administrators can now configure a custom embedding timeout via "RAG_EMBEDDING_TIMEOUT". [#21158](https://github.com/open-webui/open-webui/pull/21158), [Discussion](https://github.com/open-webui/open-webui/discussions/21151), [Commit](https://github.com/open-webui/open-webui/commit/c653e4ec54d070aee5e9568d016daebb61f06632)

> 📄 **Markdown Header Text Splitter persistence.** The "Markdown Header Text Splitter" document setting now persists correctly when disabled, preventing it from reverting to enabled after page refresh. [#20929](https://github.com/open-webui/open-webui/issues/20929), [#20930](https://github.com/open-webui/open-webui/pull/20930)

> 📚 **Knowledge base pagination fix.** Paginating through knowledge base files no longer shows duplicates or skips files when multiple documents share the same update timestamp. [#20846](https://github.com/open-webui/open-webui/issues/20846), [Commit](https://github.com/open-webui/open-webui/commit/a9a0ce6beaa286cc18eff24b518a6f3d7a560e2f)

> 🐳 **Airgapped NLTK tokenizer fix.** Document extraction now works reliably in airgapped environments after container restarts by bundling NLTK tokenizer data in the Docker image. [#21165](https://github.com/open-webui/open-webui/pull/21165), [#21150](https://github.com/open-webui/open-webui/issues/21150)

> 💾 **File upload settings persistence.** File upload settings (Max Upload Size, Max File Count, Image Compression dimensions) now persist correctly and are no longer erased when updating other RAG configuration settings. [#21057](https://github.com/open-webui/open-webui/issues/21057), [Commit](https://github.com/open-webui/open-webui/commit/258454276e1ef8ded24968515f7bf5e1833ca011)

> 🛠️ **OpenSearch 3.0 compatibility fix.** Document uploads to knowledge bases now work correctly when using OpenSearch backend with opensearch-py >= 3.0.0, fixing a TypeError that previously caused failures. [#21248](https://github.com/open-webui/open-webui/pull/21248), [#20649](https://github.com/open-webui/open-webui/issues/20649)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-12-16-reliability-and-performance-changes-in-v0-8-0|16 Reliability and Performance changes in v0.8.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-12-audio-service-timeout-handling-audio-transcription-and-text-to-speech-requests-n|🔌 Audio service timeout handling. Audio transcription and text-to-speech…]] · Voice and Audio
- [[Changes/Open WebUI/2026-02-12-2-editor-experience-changes-in-v0-8-0|2 Editor Experience changes in v0.8.0]] · Editor Experience
- [[Changes/Open WebUI/2026-02-12-5-safety-and-privacy-changes-in-v0-8-0|5 Safety and Privacy changes in v0.8.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-02-12-19-model-support-changes-in-v0-8-0|19 Model Support changes in v0.8.0]] · Model Support
- [[Changes/Open WebUI/2026-02-12-27-developer-workflow-changes-in-v0-8-0|27 Developer Workflow changes in v0.8.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-12-5-context-window-changes-in-v0-8-0|5 Context Window changes in v0.8.0]] · Context Window
- [[Changes/Open WebUI/2026-02-12-2-image-generation-changes-in-v0-8-0|2 Image Generation changes in v0.8.0]] · Image Generation
- [[Changes/Open WebUI/2026-02-12-2-memory-and-personalization-changes-in-v0-8-0|2 Memory and Personalization changes in v0.8.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-02-12-gboard-multi-line-paste-fix-multi-line-text-pasted-from-gboard-on-android-now-in|📱 Gboard multi-line paste fix. Multi-line text pasted from Gboard on Android now…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-02-12-2-collaboration-changes-in-v0-8-0|2 Collaboration changes in v0.8.0]] · Collaboration
- [[Changes/Open WebUI/2026-02-12-6-account-and-access-changes-in-v0-8-0|6 Account and Access changes in v0.8.0]] · Account and Access
- [[Changes/Open WebUI/2026-02-12-async-pipeline-operations-pipeline-operations-now-run-asynchronously-instead-of|🔧 Async pipeline operations. Pipeline operations now run asynchronously instead…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-02-12-5-search-and-browsing-changes-in-v0-8-0|5 Search and Browsing changes in v0.8.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-02-12-8-interface-experience-changes-in-v0-8-0|8 Interface Experience changes in v0.8.0]] · Interface Experience
- [[Changes/Open WebUI/2026-02-12-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-02-12-screen-reader-accessibility-screen-reader-users-now-hear-the-password-field-labe|♿ Screen reader accessibility. Screen reader users now hear the password field…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-02-12-6-apps-and-integrations-changes-in-v0-8-0|6 Apps and Integrations changes in v0.8.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-02-12-29-other-changes-in-v0-8-0|29 other changes in v0.8.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-02-11 · Dify · [[Changes/Dify/2026-02-11-2-files-and-data-changes-in-1-13-0|2 Files and Data changes in 1.13.0]]
- Later: 2026-02-13 · ChatGPT · [[Changes/ChatGPT/2026-02-13-expanded-file-type-support-we-now-support-additional-text-and-code-file-formats|Expanded file type support]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode offset]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-12-ce528c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-12-10-files-and-data-changes-in-v0-8-0.md%0ACard%20ID%3A%20open-webui-2026-02-12-ce528c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->