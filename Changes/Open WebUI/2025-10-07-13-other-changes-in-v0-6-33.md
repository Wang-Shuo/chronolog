---
card_id: open-webui-2025-10-07-f90363
date: '2025-10-07'
description: "Open WebUI · 2025-10-07 · Other changes: 13 changes in v0.6.33 — \U0001F4CA
  Chat overview flow diagram now supports toggling between vertical and horizontal
  layout…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dfdb6cf01a2bbfcba5ae8834cdeef32badb9de92c783c47226f12b84edc37bb4
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-10-07-f90363
  comparison: ''
  date: '2025-10-07'
  description: 'Open WebUI — v0.6.33: 13 other changes'
  evidence:
  - quote: "\U0001F4CA Chat overview flow diagram now supports toggling between vertical
      and horizontal layout orientations for improved visualization flexibility. [#17941](https://github.com/open-webui/open-webui/pull/17941)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F50A OpenAI Text-to-Speech engine now supports additional parameters,
      allowing users to customize TTS behavior with provider-specific options via
      JSON configuration. [#17985](https://github.com/open-webui/open-webui/issues/17985),
      [#17188](https://github.com/open-webui/open-webui/pull/17188)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F522 Ollama embedding endpoint now supports the optional dimensions
      parameter for controlling embedding output size, compatible with Ollama v0.11.11
      and later. [#17942](https://github.com/open-webui/open-webui/pull/17942)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: ⚙️ Server startup script now supports passing arbitrary arguments to uvicorn,
      enabling custom server configuration options. [#17919](https://github.com/open-webui/open-webui/pull/17919),
      [#17918](https://github.com/open-webui/open-webui/issues/17918)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F310 Translations for German, Danish, Spanish, Korean, Portuguese
      (Brazil), Simplified Chinese, and Traditional Chinese were enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F5C4️ Redis Sentinel and Redis Cluster configurations with the experimental
      ENABLE_STAR_SESSIONS_MIDDLEWARE feature are now properly isolated by making
      the feature opt-in only, preventing ReadOnlyError failures when connecting to
      read replicas in multi-node Redis deployments. [#18073](https://github.com/open-webui/open-webui/issues/18073)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F50D Hybrid search with reranking now handles empty result sets
      gracefully instead of crashing with ValueError when all results are filtered
      out due to relevance thresholds. [#18096](https://github.com/open-webui/open-webui/issues/18096)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F50D Reranking models without defined padding tokens now work correctly
      by automatically falling back to eos_token_id as pad_token_id, fixing \"Cannot
      handle batch sizes > 1\" errors for models like Qwen3-Reranker. [#18108](https://github.com/open-webui/open-webui/pull/18108),
      [#16027](https://github.com/open-webui/open-webui/discussions/16027)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F6D1 Task cancellation API now returns accurate response status,
      correctly reporting successful cancellations instead of incorrectly indicating
      failures. [#17920](https://github.com/open-webui/open-webui/issues/17920)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F4AC Follow-up query suggestions are now generated and displayed
      in temporary chats, matching the behavior of saved chats. [#14987](https://github.com/open-webui/open-webui/issues/14987)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F6E0️ OpenAPI tool server calls with optional parameters now execute
      successfully even when no arguments are provided, removing the incorrect requirement
      for a request body. [#18036](https://github.com/open-webui/open-webui/issues/18036)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F6E0️ Third-party tool responses containing non-UTF8 or invalid
      byte sequences are now handled gracefully without causing request failures.
      [#17882](https://github.com/open-webui/open-webui/pull/17882)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F5C4️ Milvus vector database dependency is updated from pymilvus
      2.5.0 to 2.6.2, ensuring compatibility with newer Milvus versions but requiring
      users on older Milvus instances to either upgrade their database or manually
      downgrade the pymilvus package. [#18066](https://github.com/open-webui/open-webui/pull/18066)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 13-other-changes-in-v0-6-33
  source_release: open-webui-2025-10-07-v0-6-33-github-252853067-e907999d
  source_type: github_releases
  theme: uncategorized
  title: 13 other changes in v0.6.33
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2025-10-07-v0-6-33-github-252853067-e907999d|open-webui-2025-10-07-v0-6-33-github-252853067-e907999d]]'
source_type: github_releases
theme: uncategorized
title: 13 other changes in v0.6.33
type: change
---

<!-- chronolog:begin region="header" -->
# 13 other changes in v0.6.33

**Open WebUI** · 2025-10-07 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.33) · from [[Releases/Open WebUI/open-webui-2025-10-07-v0-6-33-github-252853067-e907999d|v0.6.33]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📊 Chat overview flow diagram now supports toggling between vertical and horizontal layout orientations for improved visualization flexibility. [#17941](https://github.com/open-webui/open-webui/pull/17941)

> 🔊 OpenAI Text-to-Speech engine now supports additional parameters, allowing users to customize TTS behavior with provider-specific options via JSON configuration. [#17985](https://github.com/open-webui/open-webui/issues/17985), [#17188](https://github.com/open-webui/open-webui/pull/17188)

> 🔢 Ollama embedding endpoint now supports the optional dimensions parameter for controlling embedding output size, compatible with Ollama v0.11.11 and later. [#17942](https://github.com/open-webui/open-webui/pull/17942)

> ⚙️ Server startup script now supports passing arbitrary arguments to uvicorn, enabling custom server configuration options. [#17919](https://github.com/open-webui/open-webui/pull/17919), [#17918](https://github.com/open-webui/open-webui/issues/17918)

> 🌐 Translations for German, Danish, Spanish, Korean, Portuguese (Brazil), Simplified Chinese, and Traditional Chinese were enhanced and expanded.

> 🗄️ Redis Sentinel and Redis Cluster configurations with the experimental ENABLE_STAR_SESSIONS_MIDDLEWARE feature are now properly isolated by making the feature opt-in only, preventing ReadOnlyError failures when connecting to read replicas in multi-node Redis deployments. [#18073](https://github.com/open-webui/open-webui/issues/18073)

> 🔍 Hybrid search with reranking now handles empty result sets gracefully instead of crashing with ValueError when all results are filtered out due to relevance thresholds. [#18096](https://github.com/open-webui/open-webui/issues/18096)

> 🔍 Reranking models without defined padding tokens now work correctly by automatically falling back to eos_token_id as pad_token_id, fixing "Cannot handle batch sizes > 1" errors for models like Qwen3-Reranker. [#18108](https://github.com/open-webui/open-webui/pull/18108), [#16027](https://github.com/open-webui/open-webui/discussions/16027)

> 🛑 Task cancellation API now returns accurate response status, correctly reporting successful cancellations instead of incorrectly indicating failures. [#17920](https://github.com/open-webui/open-webui/issues/17920)

> 💬 Follow-up query suggestions are now generated and displayed in temporary chats, matching the behavior of saved chats. [#14987](https://github.com/open-webui/open-webui/issues/14987)

> 🛠️ OpenAPI tool server calls with optional parameters now execute successfully even when no arguments are provided, removing the incorrect requirement for a request body. [#18036](https://github.com/open-webui/open-webui/issues/18036)

> 🛠️ Third-party tool responses containing non-UTF8 or invalid byte sequences are now handled gracefully without causing request failures. [#17882](https://github.com/open-webui/open-webui/pull/17882)

> 🗄️ Milvus vector database dependency is updated from pymilvus 2.5.0 to 2.6.2, ensuring compatibility with newer Milvus versions but requiring users on older Milvus instances to either upgrade their database or manually downgrade the pymilvus package. [#18066](https://github.com/open-webui/open-webui/pull/18066)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-10-07-8-model-support-changes-in-v0-6-33|8 Model Support changes in v0.6.33]] · Model Support
- [[Changes/Open WebUI/2025-10-07-10-account-and-access-changes-in-v0-6-33|10 Account and Access changes in v0.6.33]] · Account and Access
- [[Changes/Open WebUI/2025-10-07-2-files-and-data-changes-in-v0-6-33|2 Files and Data changes in v0.6.33]] · Files and Data
- [[Changes/Open WebUI/2025-10-07-tab-characters-are-now-preserved-when-pasting-code-or-formatted-text-into-the-ch|⌨️ Tab characters are now preserved when pasting code or formatted text…]] · Editor Experience
- [[Changes/Open WebUI/2025-10-07-2-search-and-browsing-changes-in-v0-6-33|2 Search and Browsing changes in v0.6.33]] · Search and Browsing
- [[Changes/Open WebUI/2025-10-07-6-reliability-and-performance-changes-in-v0-6-33|6 Reliability and Performance changes in v0.6.33]] · Reliability and Performance
- [[Changes/Open WebUI/2025-10-07-redis-session-storage-is-now-available-as-an-experimental-option-for-oauth-authe|🗄️ Redis session storage is now available as an experimental option for OAuth…]] · Account and Access
- [[Changes/Open WebUI/2025-10-07-8-interface-experience-changes-in-v0-6-33|8 Interface Experience changes in v0.6.33]] · Interface Experience
- [[Changes/Open WebUI/2025-10-07-azure-text-to-speech-now-properly-escapes-special-characters-like-ampersands-in|🔊 Azure Text-to-Speech now properly escapes special characters like ampersands…]] · Voice and Audio
- [[Changes/Open WebUI/2025-10-07-3-developer-workflow-changes-in-v0-6-33|3 Developer Workflow changes in v0.6.33]] · Developer Workflow
- [[Changes/Open WebUI/2025-10-07-3-apps-and-integrations-changes-in-v0-6-33|3 Apps and Integrations changes in v0.6.33]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-10-07-f90363&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-10-07-13-other-changes-in-v0-6-33.md%0ACard%20ID%3A%20open-webui-2025-10-07-f90363%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.33%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->