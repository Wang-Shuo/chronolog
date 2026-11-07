---
card_id: open-webui-2025-08-21-127566
date: '2025-08-21'
description: 'Open WebUI · 2025-08-21 · Search and Browsing: 3 changes in v0.6.23
  — ⚡ **Asynchronous Chat Payload Processing**: Refactored the chat completion pipeline
  to…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added
    ability to batch delete/ignore search results]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1911
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8e3989407fd4ec455f6ead1c1d8f06dce6ea73f91447eb94d967c7b26fde0247
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-21-127566
  comparison: ''
  date: '2025-08-21'
  description: 'Open WebUI — v0.6.23: 3 Search and Browsing changes'
  evidence:
  - quote: '⚡ **Asynchronous Chat Payload Processing**: Refactored the chat completion
      pipeline to return a response immediately for streaming requests involving web
      search or tool calls. This enables users to stop ongoing generations promptly
      and preventing network timeouts during lengthy preprocessing phases, thus significantly
      improving user experience and responsiveness.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F50D **Clarified Web Search Engine Label for DDGS**: Addressed user
      confusion and inaccurate labeling by renaming \"duckduckgo\" to \"DDGS\" (Dux
      Distributed Global Search) in the web search engine selector. This clarifies
      that the system utilizes DDGS, a metasearch library that aggregates results
      from various search providers, accurately reflecting its underlying functionality
      rather than implying exclusive use of DuckDuckGo's search engine."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F310 **Renamed Web Search Concurrency Setting**: The environment
      variable \"WEB_SEARCH_CONCURRENT_REQUESTS\" has been renamed to \"WEB_LOADER_CONCURRENT_REQUESTS\".
      This change clarifies its scope, explicitly applying to the concurrency of the
      web loader component (which fetches content from search results) rather than
      the initial search engine query. Users relying on the old environment variable
      name for configuring web search concurrency must update their configurations
      to use \"WEB_LOADER_CONCURRENT_REQUESTS\"."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-search-and-browsing-changes-in-v0-6-23
  source_release: open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46
  source_type: github_releases
  theme: search-browsing
  title: 3 Search and Browsing changes in v0.6.23
  type: change
related_changes:
- '[[Changes/ChatGPT/2025-08-11-now-connect-even-more-tools-in-chatgpt-for-useful-relevant-responses-in-chat-the|Now
  connect even more tools in ChatGPT for useful, relevant responses in chat]]'
- '[[Changes/Ollama/2025-08-15-ollama-s-new-app-will-now-remember-default-selections-for-default-model-turbo-an|Ollama''s
  new app will now remember default selections for default model, Turbo…]]'
- '[[Changes/Gemini CLI/2025-08-18-feat-core-migrate-web-search-write-file-and-discovered-tool-by-joshualitt-in-htt|feat(core):
  Migrate web-search, write-file, and discovered-tool]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46]]'
source_type: github_releases
theme: search-browsing
title: 3 Search and Browsing changes in v0.6.23
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Search and Browsing changes in v0.6.23

**Open WebUI** · 2025-08-21 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.23) · from [[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|v0.6.23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ⚡ **Asynchronous Chat Payload Processing**: Refactored the chat completion pipeline to return a response immediately for streaming requests involving web search or tool calls. This enables users to stop ongoing generations promptly and preventing network timeouts during lengthy preprocessing phases, thus significantly improving user experience and responsiveness.

> 🔍 **Clarified Web Search Engine Label for DDGS**: Addressed user confusion and inaccurate labeling by renaming "duckduckgo" to "DDGS" (Dux Distributed Global Search) in the web search engine selector. This clarifies that the system utilizes DDGS, a metasearch library that aggregates results from various search providers, accurately reflecting its underlying functionality rather than implying exclusive use of DuckDuckGo's search engine.

> 🌐 **Renamed Web Search Concurrency Setting**: The environment variable "WEB_SEARCH_CONCURRENT_REQUESTS" has been renamed to "WEB_LOADER_CONCURRENT_REQUESTS". This change clarifies its scope, explicitly applying to the concurrency of the web loader component (which fetches content from search results) rather than the initial search engine query. Users relying on the old environment variable name for configuring web search concurrency must update their configurations to use "WEB_LOADER_CONCURRENT_REQUESTS".

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-21-8-interface-experience-changes-in-v0-6-23|8 Interface Experience changes in v0.6.23]] · Interface Experience
- [[Changes/Open WebUI/2025-08-21-restored-message-toolbar-icons-for-empty-messages-with-files-fixed-an-issue-wher|🐛 Restored Message Toolbar Icons for Empty Messages with Files]] · Editor Experience
- [[Changes/Open WebUI/2025-08-21-resolved-silently-dropped-streaming-response-chunks-fixed-an-issue-where-the-fin|💬 Resolved Silently Dropped Streaming Response Chunks]] · Files and Data
- [[Changes/Open WebUI/2025-08-21-3-mobile-and-desktop-changes-in-v0-6-23|3 Mobile and Desktop changes in v0.6.23]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-08-21-6-reliability-and-performance-changes-in-v0-6-23|6 Reliability and Performance changes in v0.6.23]] · Reliability and Performance
- [[Changes/Open WebUI/2025-08-21-6-safety-and-privacy-changes-in-v0-6-23|6 Safety and Privacy changes in v0.6.23]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-21-2-voice-and-audio-changes-in-v0-6-23|2 Voice and Audio changes in v0.6.23]] · Voice and Audio
- [[Changes/Open WebUI/2025-08-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-08-21-2-accessibility-and-localization-changes-in-v0-6-23|2 Accessibility and Localization changes in v0.6.23]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-21-7-model-support-changes-in-v0-6-23|7 Model Support changes in v0.6.23]] · Model Support
- [[Changes/Open WebUI/2025-08-21-resolved-image-generation-api-size-parameter-issue-fixed-a-bug-where-the-api-v1|🖼️ Resolved Image Generation API Size Parameter Issue]] · Image Generation
- [[Changes/Open WebUI/2025-08-21-resolved-code-block-input-issue-with-shift-enter-fixed-a-bug-where-typing-three|📝 Resolved Code Block Input Issue with Shift+Enter]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-21-5-apps-and-integrations-changes-in-v0-6-23|5 Apps and Integrations changes in v0.6.23]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-21-3-account-and-access-changes-in-v0-6-23|3 Account and Access changes in v0.6.23]] · Account and Access
- [[Changes/Open WebUI/2025-08-21-23-other-changes-in-v0-6-23|23 other changes in v0.6.23]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2025-08-18 · Gemini CLI · [[Changes/Gemini CLI/2025-08-18-feat-core-migrate-web-search-write-file-and-discovered-tool-by-joshualitt-in-htt|feat(core): Migrate web-search, write-file, and discovered-tool]]
- Later: 2025-08-26 · Codex CLI · [[Changes/Codex CLI/2025-08-26-2-search-and-browsing-changes-in-rust-v0-24-0|2 Search and Browsing changes in rust-v0.24.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-05-28 · Descript · [[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added ability to batch delete/ignore search results]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-21-127566&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-21-3-search-and-browsing-changes-in-v0-6-23.md%0ACard%20ID%3A%20open-webui-2025-08-21-127566%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->