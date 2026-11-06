---
card_id: open-webui-2026-02-12-962d8d
date: '2026-02-12'
description: "Open WebUI · 2026-02-12 · Search and Browsing: 5 changes in v0.8.0 —
  \U0001F680 **Async web search.** Web search operations now run asynchronously in
  the background…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1057
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f9b38770457039b8b6c73769dcb8377365bf76e2314128549a1a3ee7e6a5354d
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-12-962d8d
  comparison: ''
  date: '2026-02-12'
  description: 'Open WebUI — v0.8.0: 5 Search and Browsing changes'
  evidence:
  - quote: "\U0001F680 **Async web search.** Web search operations now run asynchronously
      in the background, allowing users to continue interacting with the application
      while searches complete. [#20630](https://github.com/open-webui/open-webui/pull/20630)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F9E0 **Smarter knowledge vs web search.** Models now choose more
      intelligently between knowledge base search and web search rather than always
      trying knowledge first. [#21115](https://github.com/open-webui/open-webui/pull/21115)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F50D **Yandex search provider.** Administrators can now configure
      Yandex as a web search provider, expanding search engine options for retrieval-augmented
      generation. [#20922](https://github.com/open-webui/open-webui/pull/20922)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F517 **Function chat ID propagation fix.** Functions now reliably
      receive the chat identifier during internal task invocations like web search
      query generation, RAG query generation, and image prompt generation, enabling
      stateful functions to maintain consistent per-chat state without fragmentation.
      [#20563](https://github.com/open-webui/open-webui/issues/20563), [#20585](https://github.com/open-webui/open-webui/pull/20585)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F50D **Chat search self-exclusion.** The \"search_chats\" builtin
      tool now excludes the current conversation from search results, preventing redundant
      matches. [#20718](https://github.com/open-webui/open-webui/issues/20718), [Commit](https://github.com/open-webui/open-webui/commit/1a4bdd2b30017d901b9cac1e2e10684ec1edd062)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-search-and-browsing-changes-in-v0-8-0
  source_release: open-webui-2026-02-12-v0-8-0-github-285910626-490914ba
  source_type: github_releases
  theme: search-browsing
  title: 5 Search and Browsing changes in v0.8.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-02-03-sub-agent-support-for-ollama-launch-for-planning-deep-research-and-similar-tasks|Sub-agent
  support for ollama launch for planning, deep research, and similar tasks]]'
- '[[Changes/Codex CLI/2026-02-04-2-search-and-browsing-changes-in-rust-v0-95-0|2
  Search and Browsing changes in rust-v0.95.0]]'
- '[[Changes/Codex CLI/2026-02-11-3-search-and-browsing-changes-in-rust-v0-99-0|3
  Search and Browsing changes in rust-v0.99.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|open-webui-2026-02-12-v0-8-0-github-285910626-490914ba]]'
source_type: github_releases
theme: search-browsing
title: 5 Search and Browsing changes in v0.8.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Search and Browsing changes in v0.8.0

**Open WebUI** · 2026-02-12 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.0) · from [[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|v0.8.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🚀 **Async web search.** Web search operations now run asynchronously in the background, allowing users to continue interacting with the application while searches complete. [#20630](https://github.com/open-webui/open-webui/pull/20630)

> 🧠 **Smarter knowledge vs web search.** Models now choose more intelligently between knowledge base search and web search rather than always trying knowledge first. [#21115](https://github.com/open-webui/open-webui/pull/21115)

> 🔍 **Yandex search provider.** Administrators can now configure Yandex as a web search provider, expanding search engine options for retrieval-augmented generation. [#20922](https://github.com/open-webui/open-webui/pull/20922)

> 🔗 **Function chat ID propagation fix.** Functions now reliably receive the chat identifier during internal task invocations like web search query generation, RAG query generation, and image prompt generation, enabling stateful functions to maintain consistent per-chat state without fragmentation. [#20563](https://github.com/open-webui/open-webui/issues/20563), [#20585](https://github.com/open-webui/open-webui/pull/20585)

> 🔍 **Chat search self-exclusion.** The "search_chats" builtin tool now excludes the current conversation from search results, preventing redundant matches. [#20718](https://github.com/open-webui/open-webui/issues/20718), [Commit](https://github.com/open-webui/open-webui/commit/1a4bdd2b30017d901b9cac1e2e10684ec1edd062)

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
- [[Changes/Open WebUI/2026-02-12-8-interface-experience-changes-in-v0-8-0|8 Interface Experience changes in v0.8.0]] · Interface Experience
- [[Changes/Open WebUI/2026-02-12-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-02-12-screen-reader-accessibility-screen-reader-users-now-hear-the-password-field-labe|♿ Screen reader accessibility. Screen reader users now hear the password field…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-02-12-10-files-and-data-changes-in-v0-8-0|10 Files and Data changes in v0.8.0]] · Files and Data
- [[Changes/Open WebUI/2026-02-12-6-apps-and-integrations-changes-in-v0-8-0|6 Apps and Integrations changes in v0.8.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-02-12-29-other-changes-in-v0-8-0|29 other changes in v0.8.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-02-11 · Codex CLI · [[Changes/Codex CLI/2026-02-11-3-search-and-browsing-changes-in-rust-v0-99-0|3 Search and Browsing changes in rust-v0.99.0]]
- Later: 2026-02-14 · Open WebUI · [[Changes/Open WebUI/2026-02-14-web-search-result-count-the-built-in-search-web-tool-now-respects-the-admin-conf|🔍 Web search result count. The built-in search_web tool now respects…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-12-962d8d&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-12-5-search-and-browsing-changes-in-v0-8-0.md%0ACard%20ID%3A%20open-webui-2026-02-12-962d8d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->