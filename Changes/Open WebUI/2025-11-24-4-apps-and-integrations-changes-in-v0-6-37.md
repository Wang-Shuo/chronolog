---
card_id: open-webui-2025-11-24-e00962
date: '2025-11-24'
description: "Open WebUI · 2025-11-24 · Apps and Integrations: 4 changes in v0.6.37
  — \U0001F5C4️ Weaviate is now supported as a vector database option, providing an
  additional…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 977
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2bebf6876918eb609dc8049342b644c2c32cb31d8888f1e7ee6d0cc4ca725e65
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-11-24-e00962
  comparison: ''
  date: '2025-11-24'
  description: 'Open WebUI — v0.6.37: 4 Apps and Integrations changes'
  evidence:
  - quote: "\U0001F5C4️ Weaviate is now supported as a vector database option, providing
      an additional choice for RAG document storage alongside existing ChromaDB, Milvus,
      Qdrant, and OpenSearch integrations. [#14747](https://github.com/open-webui/open-webui/pull/14747)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: ⚡ External embedding generation now processes API requests in parallel
      instead of sequential batches, reducing document processing time by 10-50x when
      using OpenAI, Azure OpenAI, or Ollama embedding providers, with large PDFs now
      processing in seconds instead of minutes. [#19296](https://github.com/open-webui/open-webui/pull/19296)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F527 Custom headers can now be configured for remote MCP and OpenAPI
      tool server connections, enabling integration with services that require additional
      authentication headers. [#18918](https://github.com/open-webui/open-webui/issues/18918)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: ⚙️ OAuth dynamic client registration now correctly converts empty strings
      to None for optional fields, preventing validation failures in MCP package integration.
      [#19144](https://github.com/open-webui/open-webui/pull/19144), [#19129](https://github.com/open-webui/open-webui/issues/19129)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-apps-and-integrations-changes-in-v0-6-37
  source_release: open-webui-2025-11-24-v0-6-37-github-264669867-8b715894
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v0.6.37
  type: change
related_changes:
- '[[Changes/Replit/2025-11-21-new-connector-todoist|New connector: Todoist]]'
- '[[Changes/Windsurf/2025-11-21-mcp-servers|MCP Servers]]'
- '[[Changes/GitHub Copilot CLI/2025-11-24-mcp-servers-work-in-prompt-mode|MCP servers
  work in --prompt mode]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-11-24-v0-6-37-github-264669867-8b715894|open-webui-2025-11-24-v0-6-37-github-264669867-8b715894]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v0.6.37
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v0.6.37

**Open WebUI** · 2025-11-24 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.37) · from [[Releases/Open WebUI/open-webui-2025-11-24-v0-6-37-github-264669867-8b715894|v0.6.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗄️ Weaviate is now supported as a vector database option, providing an additional choice for RAG document storage alongside existing ChromaDB, Milvus, Qdrant, and OpenSearch integrations. [#14747](https://github.com/open-webui/open-webui/pull/14747)

> ⚡ External embedding generation now processes API requests in parallel instead of sequential batches, reducing document processing time by 10-50x when using OpenAI, Azure OpenAI, or Ollama embedding providers, with large PDFs now processing in seconds instead of minutes. [#19296](https://github.com/open-webui/open-webui/pull/19296)

> 🔧 Custom headers can now be configured for remote MCP and OpenAPI tool server connections, enabling integration with services that require additional authentication headers. [#18918](https://github.com/open-webui/open-webui/issues/18918)

> ⚙️ OAuth dynamic client registration now correctly converts empty strings to None for optional fields, preventing validation failures in MCP package integration. [#19144](https://github.com/open-webui/open-webui/pull/19144), [#19129](https://github.com/open-webui/open-webui/issues/19129)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-11-24-3-search-and-browsing-changes-in-v0-6-37|3 Search and Browsing changes in v0.6.37]] · Search and Browsing
- [[Changes/Open WebUI/2025-11-24-model-cloning-is-now-available-in-admin-settings-allowing-administrators-to-quic|🤖 Model cloning is now available in admin settings, allowing administrators…]] · Model Support
- [[Changes/Open WebUI/2025-11-24-granular-sharing-permissions-are-now-available-with-two-tiered-control-separatin|🔐 Granular sharing permissions are now available with two-tiered control separating…]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-24-5-interface-experience-changes-in-v0-6-37|5 Interface Experience changes in v0.6.37]] · Interface Experience
- [[Changes/Open WebUI/2025-11-24-granular-import-and-export-permissions-are-now-available-for-workspace-items-int|🔐 Granular import and export permissions are now available for workspace items…]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-24-prompt-autocompletion-is-now-available-independently-of-the-rich-text-input-sett|✍️ Prompt autocompletion is now available independently of the rich text input…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-11-24-rag-template-query-placeholder-escaping-logic-was-corrected-to-prevent-unintende|📝 RAG template query placeholder escaping logic was corrected to prevent unintended…]] · Context Window
- [[Changes/Open WebUI/2025-11-24-default-group-assignment-is-now-available-for-new-users-allowing-administrators|👥 Default group assignment is now available for new users, allowing administrators…]] · Model Support
- [[Changes/Open WebUI/2025-11-24-2-voice-and-audio-changes-in-v0-6-37|2 Voice and Audio changes in v0.6.37]] · Voice and Audio
- [[Changes/Open WebUI/2025-11-24-7-account-and-access-changes-in-v0-6-37|7 Account and Access changes in v0.6.37]] · Account and Access
- [[Changes/Open WebUI/2025-11-24-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-11-24-ui-scale-adjustment-is-now-available-in-interface-settings-allowing-users-to-inc|🎨 UI scale adjustment is now available in interface settings, allowing users…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-11-24-2-files-and-data-changes-in-v0-6-37|2 Files and Data changes in v0.6.37]] · Files and Data
- [[Changes/Open WebUI/2025-11-24-api-key-creation-is-now-controlled-by-granular-user-and-group-permissions-with-t|🔐 API key creation is now controlled by granular user and group permissions…]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-24-4-image-generation-changes-in-v0-6-37|4 Image Generation changes in v0.6.37]] · Image Generation
- [[Changes/Open WebUI/2025-11-24-websocket-and-redis-configuration-options-are-now-available-including-debug-logg|🔧 WebSocket and Redis configuration options are now available including debug…]] · Developer Workflow
- [[Changes/Open WebUI/2025-11-24-pwa-installations-on-ios-now-properly-refresh-after-server-container-restarts-re|📱 PWA installations on iOS now properly refresh after server container restarts…]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-11-24-11-model-support-changes-in-v0-6-37|11 Model Support changes in v0.6.37]] · Model Support
- [[Changes/Open WebUI/2025-11-24-9-reliability-and-performance-changes-in-v0-6-37|9 Reliability and Performance changes in v0.6.37]] · Reliability and Performance
- [[Changes/Open WebUI/2025-11-24-password-policy-enforcement-is-now-available-with-configurable-validation-rules|🔐 Password policy enforcement is now available with configurable validation rules…]] · Other changes
- [[Changes/Open WebUI/2025-11-24-24-other-changes-in-v0-6-37|24 other changes in v0.6.37]] · Other changes
- [[Changes/Open WebUI/2025-11-24-daily-active-user-metric-is-now-available-for-monitoring-tracking-unique-users-a|📊 Daily active user metric is now available for monitoring, tracking unique users…]] · Other changes
- [[Changes/Open WebUI/2025-11-24-base64-image-conversion-is-now-available-for-markdown-content-in-chat-responses|💨 Base64 image conversion is now available for markdown content in chat responses…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-11-24 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-11-24-mcp-servers-work-in-prompt-mode|MCP servers work in --prompt mode]]
- Later: 2025-11-25 · Open WebUI · [[Changes/Open WebUI/2025-11-25-tool-servers-and-mcp-connections-now-support-function-name-filtering-allowing-ad|🔌 Tool servers and MCP connections now support function name filtering, allowing…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-11-24-e00962&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-11-24-4-apps-and-integrations-changes-in-v0-6-37.md%0ACard%20ID%3A%20open-webui-2025-11-24-e00962%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.37%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->