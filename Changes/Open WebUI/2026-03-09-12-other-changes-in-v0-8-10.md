---
card_id: open-webui-2026-03-09-d25148
date: '2026-03-09'
description: "Open WebUI · 2026-03-09 · Other changes: 12 changes in v0.8.10 — \U0001F5C4️
  **MariaDB Vector community support.** Added MariaDB Vector as a new vector database…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0427775e4a56d3d6851dec67c66367b9c6297c81a251b2188075e2b8f4656bb7
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-09-d25148
  comparison: ''
  date: '2026-03-09'
  description: 'Open WebUI — v0.8.10: 12 other changes'
  evidence:
  - quote: "\U0001F5C4️ **MariaDB Vector community support.** Added MariaDB Vector
      as a new vector database backend, enabling deployments with VECTOR_DB=mariadb-vector;
      supports cosine and euclidean distance strategies with configurable HNSW indexing.
      [#21931](https://github.com/open-webui/open-webui/pull/21931)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  - quote: "\U0001F310 Translations for Portuguese (Brazil), Spanish, and Malay were
      enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  - quote: "\U0001F517 **Pipeline filter HTTP errors.** Fixed a bug where HTTP errors
      in pipeline inlet/outlet filters would silently corrupt the user's chat payload;
      errors are now properly raised before parsing the response. [#22445](https://github.com/open-webui/open-webui/pull/22445)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  - quote: "\U0001F6E0️ **Process shutdown handling.** Fixed bare except clauses in
      the main process that prevented clean shutdown; replaced with proper exception
      handling. [#22423](https://github.com/open-webui/open-webui/pull/22423)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  - quote: "\U0001F433 **Docker deployment startup.** Docker deployments now start
      correctly; the missing OpenTelemetry system metrics dependency was added. [#22447](https://github.com/open-webui/open-webui/pull/22447),
      [#22401](https://github.com/open-webui/open-webui/issues/22401)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  - quote: "\U0001F6E0️ **Tool access for non-admin users.** Fixed a NameError that
      prevented non-admin users from viewing tools; the missing has_access function
      is now properly imported. [#22393](https://github.com/open-webui/open-webui/issues/22393)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  - quote: "\U0001F4C4 **YAML file processing.** Fixed an error when uploading YAML
      files with Docling enabled; YAML and YML files are now properly recognized as
      text files and processed correctly. [#22399](https://github.com/open-webui/open-webui/pull/22399),
      [#22263](https://github.com/open-webui/open-webui/issues/22263)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  - quote: "\U0001F4C5 **Time range month names.** Fixed month names in time range
      labels appearing in the wrong language when OS regional settings differ from
      browser language; month names now consistently display in English. [#22454](https://github.com/open-webui/open-webui/pull/22454)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  - quote: "\U0001F50A **Azure TTS locale extraction.** Fixed Azure text-to-speech
      using incomplete locale codes in SSML; now correctly uses full locale like \"en-US\"
      instead of just \"en\". [#22443](https://github.com/open-webui/open-webui/pull/22443)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  - quote: "\U0001F4CA **Analytics group filtering.** Fixed token usage analytics
      not being filtered by user group; the query now properly respects group filters
      like other analytics metrics. [#22167](https://github.com/open-webui/open-webui/pull/22167)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  - quote: "\U0001F5BC️ **Pending message image display.** Fixed images in queued
      messages appearing blank; image thumbnails are now properly displayed in the
      pending message queue. [#22256](https://github.com/open-webui/open-webui/issues/22256)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  - quote: "\U0001F6E0️ **File metadata sanitization.** Fixed file uploads failing
      with JSON serialization errors when metadata contained non-serializable objects
      like callable functions; metadata is now sanitized before database insertion.
      [#20561](https://github.com/open-webui/open-webui/issues/20561)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 12-other-changes-in-v0-8-10
  source_release: open-webui-2026-03-09-v0-8-10-github-294485945-5852a771
  source_type: github_releases
  theme: uncategorized
  title: 12 other changes in v0.8.10
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-03-09-v0-8-10-github-294485945-5852a771|open-webui-2026-03-09-v0-8-10-github-294485945-5852a771]]'
source_type: github_releases
theme: uncategorized
title: 12 other changes in v0.8.10
type: change
---

<!-- chronolog:begin region="header" -->
# 12 other changes in v0.8.10

**Open WebUI** · 2026-03-09 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.10) · from [[Releases/Open WebUI/open-webui-2026-03-09-v0-8-10-github-294485945-5852a771|v0.8.10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗄️ **MariaDB Vector community support.** Added MariaDB Vector as a new vector database backend, enabling deployments with VECTOR_DB=mariadb-vector; supports cosine and euclidean distance strategies with configurable HNSW indexing. [#21931](https://github.com/open-webui/open-webui/pull/21931)

> 🌐 Translations for Portuguese (Brazil), Spanish, and Malay were enhanced and expanded.

> 🔗 **Pipeline filter HTTP errors.** Fixed a bug where HTTP errors in pipeline inlet/outlet filters would silently corrupt the user's chat payload; errors are now properly raised before parsing the response. [#22445](https://github.com/open-webui/open-webui/pull/22445)

> 🛠️ **Process shutdown handling.** Fixed bare except clauses in the main process that prevented clean shutdown; replaced with proper exception handling. [#22423](https://github.com/open-webui/open-webui/pull/22423)

> 🐳 **Docker deployment startup.** Docker deployments now start correctly; the missing OpenTelemetry system metrics dependency was added. [#22447](https://github.com/open-webui/open-webui/pull/22447), [#22401](https://github.com/open-webui/open-webui/issues/22401)

> 🛠️ **Tool access for non-admin users.** Fixed a NameError that prevented non-admin users from viewing tools; the missing has_access function is now properly imported. [#22393](https://github.com/open-webui/open-webui/issues/22393)

> 📄 **YAML file processing.** Fixed an error when uploading YAML files with Docling enabled; YAML and YML files are now properly recognized as text files and processed correctly. [#22399](https://github.com/open-webui/open-webui/pull/22399), [#22263](https://github.com/open-webui/open-webui/issues/22263)

> 📅 **Time range month names.** Fixed month names in time range labels appearing in the wrong language when OS regional settings differ from browser language; month names now consistently display in English. [#22454](https://github.com/open-webui/open-webui/pull/22454)

> 🔊 **Azure TTS locale extraction.** Fixed Azure text-to-speech using incomplete locale codes in SSML; now correctly uses full locale like "en-US" instead of just "en". [#22443](https://github.com/open-webui/open-webui/pull/22443)

> 📊 **Analytics group filtering.** Fixed token usage analytics not being filtered by user group; the query now properly respects group filters like other analytics metrics. [#22167](https://github.com/open-webui/open-webui/pull/22167)

> 🖼️ **Pending message image display.** Fixed images in queued messages appearing blank; image thumbnails are now properly displayed in the pending message queue. [#22256](https://github.com/open-webui/open-webui/issues/22256)

> 🛠️ **File metadata sanitization.** Fixed file uploads failing with JSON serialization errors when metadata contained non-serializable objects like callable functions; metadata is now sanitized before database insertion. [#20561](https://github.com/open-webui/open-webui/issues/20561)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-09-teams-webhook-crash-fixed-a-typeerror-crash-in-the-teams-webhook-handler-when-us|📨 Teams webhook crash. Fixed a TypeError crash in the Teams webhook handler…]] · Collaboration
- [[Changes/Open WebUI/2026-03-09-2-search-and-browsing-changes-in-v0-8-10|2 Search and Browsing changes in v0.8.10]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-09-2-developer-workflow-changes-in-v0-8-10|2 Developer Workflow changes in v0.8.10]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-09-2-account-and-access-changes-in-v0-8-10|2 Account and Access changes in v0.8.10]] · Account and Access
- [[Changes/Open WebUI/2026-03-09-azure-speech-transcription-errors-improved-azure-ai-speech-error-handling-to-dis|🎤 Azure speech transcription errors. Improved Azure AI Speech error handling…]] · Voice and Audio
- [[Changes/Open WebUI/2026-03-09-3-model-support-changes-in-v0-8-10|3 Model Support changes in v0.8.10]] · Model Support
- [[Changes/Open WebUI/2026-03-09-2-reliability-and-performance-changes-in-v0-8-10|2 Reliability and Performance changes in v0.8.10]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-09-d25148&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-09-12-other-changes-in-v0-8-10.md%0ACard%20ID%3A%20open-webui-2026-03-09-d25148%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.10%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->