---
card_id: open-webui-2026-02-23-1343c8
date: '2026-02-23'
description: "Open WebUI · 2026-02-23 · Reliability and Performance: 10 changes in
  v0.8.4 — \U0001F680 **Message list performance.** Loading conversation history when
  sending…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2653
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cd0ad6331005169d81bec99d0a5ea95c42fb16e637f77f0abaf414b4b316c4f9
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-23-1343c8
  comparison: ''
  date: '2026-02-23'
  description: 'Open WebUI — v0.8.4: 10 Reliability and Performance changes'
  evidence:
  - quote: "\U0001F680 **Message list performance.** Loading conversation history
      when sending messages is now significantly faster, improving response latency
      before the model starts generating. This also speeds up chat search and RAG
      context building. [#21588](https://github.com/open-webui/open-webui/pull/21588)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F3AF **Concurrent embedding request control.** Administrators can
      now control the maximum number of concurrent embedding API requests using the
      RAG_EMBEDDING_CONCURRENT_REQUESTS environment variable, helping manage API rate
      limits while maintaining embedding performance. [#21662](https://github.com/open-webui/open-webui/pull/21662),
      [Commit](https://github.com/open-webui/open-webui/commit/5d4547f934b6fbe751bb2041f9597fe11ddf8e43)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: ⚡ **Message upsert optimization.** Loading chat data during message saving
      is now significantly faster by eliminating a redundant database call that occurred
      on every message upsert, which happens many times during streaming responses.
      [#21592](https://github.com/open-webui/open-webui/pull/21592)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: ⚡ **Message send optimization.** Loading chat data during message sending
      is now significantly faster by eliminating unnecessary full conversation history
      loads. The system now uses targeted queries that fetch only the needed data
      instead of loading entire chat objects with all message history. [#21596](https://github.com/open-webui/open-webui/pull/21596)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F680 **Tag filtering optimization.** Chat search with tag filtering
      now uses more efficient database queries, making filtered searches significantly
      faster. [Commit](https://github.com/open-webui/open-webui/commit/139f02a9d9fa2ffffcc96aa0de8af8ef51b6bcf2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: ⚡ **Shared chat loading optimization.** The shared chats endpoint now loads
      only the needed columns instead of the full conversation history, making shared
      chat listings significantly faster. [#21614](https://github.com/open-webui/open-webui/pull/21614)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F5C2️ **Archived and pinned chat loading.** Loading archived and
      pinned chat lists is now significantly faster by loading only the needed columns
      instead of full conversation data. [#21591](https://github.com/open-webui/open-webui/pull/21591)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F4A8 **Chat title query optimization.** Retrieving chat titles now
      queries only the title column instead of the entire conversation history, making
      title lookups significantly faster and reducing database load. [#21590](https://github.com/open-webui/open-webui/pull/21590)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: ⚡ **Tools list performance.** Loading the tools list is now significantly
      faster by deferring content and specs fields from database queries, and using
      cached tool modules instead of reloading them for each request. [Commit](https://github.com/open-webui/open-webui/commit/b48594a16680cc77921a4ed1a11ffa07df7edc60)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F504 **General improvements.** Various improvements were implemented
      across the application to enhance performance, stability, and security."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 10-reliability-and-performance-changes-in-v0-8-4
  source_release: open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c
  source_type: github_releases
  theme: reliability-performance
  title: 10 Reliability and Performance changes in v0.8.4
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-02-20-improve-code-search-speed-in-large-repos|Improve
  code search speed in large repos]]'
- '[[Changes/Ollama/2026-02-21-improved-tokenizer-performance|Improved tokenizer performance]]'
- '[[Changes/Lovable/2026-02-23-project-search-has-been-improved-with-faster-full-text-search-better-substring-m|Project
  search has been improved with faster full-text search, better substring…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c]]'
source_type: github_releases
theme: reliability-performance
title: 10 Reliability and Performance changes in v0.8.4
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Reliability and Performance changes in v0.8.4

**Open WebUI** · 2026-02-23 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.4) · from [[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|v0.8.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🚀 **Message list performance.** Loading conversation history when sending messages is now significantly faster, improving response latency before the model starts generating. This also speeds up chat search and RAG context building. [#21588](https://github.com/open-webui/open-webui/pull/21588)

> 🎯 **Concurrent embedding request control.** Administrators can now control the maximum number of concurrent embedding API requests using the RAG_EMBEDDING_CONCURRENT_REQUESTS environment variable, helping manage API rate limits while maintaining embedding performance. [#21662](https://github.com/open-webui/open-webui/pull/21662), [Commit](https://github.com/open-webui/open-webui/commit/5d4547f934b6fbe751bb2041f9597fe11ddf8e43)

> ⚡ **Message upsert optimization.** Loading chat data during message saving is now significantly faster by eliminating a redundant database call that occurred on every message upsert, which happens many times during streaming responses. [#21592](https://github.com/open-webui/open-webui/pull/21592)

> ⚡ **Message send optimization.** Loading chat data during message sending is now significantly faster by eliminating unnecessary full conversation history loads. The system now uses targeted queries that fetch only the needed data instead of loading entire chat objects with all message history. [#21596](https://github.com/open-webui/open-webui/pull/21596)

> 🚀 **Tag filtering optimization.** Chat search with tag filtering now uses more efficient database queries, making filtered searches significantly faster. [Commit](https://github.com/open-webui/open-webui/commit/139f02a9d9fa2ffffcc96aa0de8af8ef51b6bcf2)

> ⚡ **Shared chat loading optimization.** The shared chats endpoint now loads only the needed columns instead of the full conversation history, making shared chat listings significantly faster. [#21614](https://github.com/open-webui/open-webui/pull/21614)

> 🗂️ **Archived and pinned chat loading.** Loading archived and pinned chat lists is now significantly faster by loading only the needed columns instead of full conversation data. [#21591](https://github.com/open-webui/open-webui/pull/21591)

> 💨 **Chat title query optimization.** Retrieving chat titles now queries only the title column instead of the entire conversation history, making title lookups significantly faster and reducing database load. [#21590](https://github.com/open-webui/open-webui/pull/21590)

> ⚡ **Tools list performance.** Loading the tools list is now significantly faster by deferring content and specs fields from database queries, and using cached tool modules instead of reloading them for each request. [Commit](https://github.com/open-webui/open-webui/commit/b48594a16680cc77921a4ed1a11ffa07df7edc60)

> 🔄 **General improvements.** Various improvements were implemented across the application to enhance performance, stability, and security.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-23-12-developer-workflow-changes-in-v0-8-4|12 Developer Workflow changes in v0.8.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-23-text-file-type-detection-fix-typescript-and-other-text-files-that-were-mis-detec|📄 Text file type detection fix. TypeScript and other text files…]] · Multimodal Input
- [[Changes/Open WebUI/2026-02-23-2-memory-and-personalization-changes-in-v0-8-4|2 Memory and Personalization changes in v0.8.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-02-23-ui-accessibility-improvements-screen-reader-users-can-now-navigate-the-interface|♿ UI accessibility improvements. Screen reader users can now navigate…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-02-23-8-interface-experience-changes-in-v0-8-4|8 Interface Experience changes in v0.8.4]] · Interface Experience
- [[Changes/Open WebUI/2026-02-23-2-editor-experience-changes-in-v0-8-4|2 Editor Experience changes in v0.8.4]] · Editor Experience
- [[Changes/Open WebUI/2026-02-23-4-search-and-browsing-changes-in-v0-8-4|4 Search and Browsing changes in v0.8.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-02-23-mcp-ssl-verification-fix-mcp-tool-connections-now-properly-respect-the-aiohttp-c|🔓 MCP SSL verification fix. MCP tool connections now properly respect…]] · Apps and Integrations
- [[Changes/Open WebUI/2026-02-23-file-access-control-respect-the-files-list-and-search-endpoints-now-properly-res|🗄️ File access control respect. The files list and search endpoints now properly…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-02-23-3-account-and-access-changes-in-v0-8-4|3 Account and Access changes in v0.8.4]] · Account and Access
- [[Changes/Open WebUI/2026-02-23-3-safety-and-privacy-changes-in-v0-8-4|3 Safety and Privacy changes in v0.8.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-02-23-16-model-support-changes-in-v0-8-4|16 Model Support changes in v0.8.4]] · Model Support
- [[Changes/Open WebUI/2026-02-23-api-tools-fix-the-api-v1-chat-completions-endpoint-now-properly-respects-caller|🛠️ API tools fix. The /api/v1/chat/completions endpoint now properly respects…]] · Agent Mode
- [[Changes/Open WebUI/2026-02-23-15-other-changes-in-v0-8-4|15 other changes in v0.8.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-02-23 · Lovable · [[Changes/Lovable/2026-02-23-project-search-has-been-improved-with-faster-full-text-search-better-substring-m|Project search has been improved with faster full-text search, better substring…]]
- Later: 2026-02-24 · Cline · [[Changes/Cline/2026-02-24-preconnect-websocket-to-reduce-response-latency|Preconnect websocket to reduce response latency]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-23-1343c8&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-23-10-reliability-and-performance-changes-in-v0-8-4.md%0ACard%20ID%3A%20open-webui-2026-02-23-1343c8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->