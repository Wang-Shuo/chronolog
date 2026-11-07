---
card_id: open-webui-2026-03-25-a6a0cc
date: '2026-03-25'
description: "Open WebUI · 2026-03-25 · Apps and Integrations: 3 changes in v0.8.11
  — \U0001F510 **MCP OAuth 2.1 static credentials.** MCP servers that require static
  client_id and…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1098
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 49acef432101dfce5fc376b6b6cd0dcb691ba0d37a6c5895fb37e400e3c670fb
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-25-a6a0cc
  comparison: ''
  date: '2026-03-25'
  description: 'Open WebUI — v0.8.11: 3 Apps and Integrations changes'
  evidence:
  - quote: "\U0001F510 **MCP OAuth 2.1 static credentials.** MCP servers that require
      static client_id and client_secret can now be connected using a new OAuth 2.1
      Static auth type, enabling integration with MCP servers that don't support dynamic
      client registration. [#22266](https://github.com/open-webui/open-webui/pull/22266),
      [Commit](https://github.com/open-webui/open-webui/commit/601bb783587a3e965cf88c148e4856b988655b13)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F9E9 **MCP integration visibility.** MCP (Streamable HTTP) integrations
      are now hidden from user-level settings, matching the intended behavior where
      only administrators can configure MCP connections through the admin panel. User-level
      connections now show the connection type as read-only. [#22615](https://github.com/open-webui/open-webui/issues/22615),
      [Commit](https://github.com/open-webui/open-webui/commit/1eef5b4f6a718c0fcf3605f1ed62669aca07b454)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F6E0️ **Plugin ID sanitization.** Creating Functions or Tools with
      emojis or special characters in their names now generates valid IDs that pass
      backend validation, instead of failing with an error. [#22695](https://github.com/open-webui/open-webui/pull/22695)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-apps-and-integrations-changes-in-v0-8-11
  source_release: open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v0.8.11
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-25-6-apps-and-integrations-changes-in-v2-1-83|6 Apps
  and Integrations changes in v2.1.83]]'
- '[[Changes/Google Antigravity/2026-03-25-linux-sandboxing-and-mcp-improvements|Linux
  Sandboxing and MCP Improvements]]'
- '[[Changes/Ollama/2026-03-25-openclaw-integration-improvements-for-gateway-checks|OpenClaw
  integration improvements for gateway checks]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v0.8.11
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v0.8.11

**Open WebUI** · 2026-03-25 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.11) · from [[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|v0.8.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔐 **MCP OAuth 2.1 static credentials.** MCP servers that require static client_id and client_secret can now be connected using a new OAuth 2.1 Static auth type, enabling integration with MCP servers that don't support dynamic client registration. [#22266](https://github.com/open-webui/open-webui/pull/22266), [Commit](https://github.com/open-webui/open-webui/commit/601bb783587a3e965cf88c148e4856b988655b13)

> 🧩 **MCP integration visibility.** MCP (Streamable HTTP) integrations are now hidden from user-level settings, matching the intended behavior where only administrators can configure MCP connections through the admin panel. User-level connections now show the connection type as read-only. [#22615](https://github.com/open-webui/open-webui/issues/22615), [Commit](https://github.com/open-webui/open-webui/commit/1eef5b4f6a718c0fcf3605f1ed62669aca07b454)

> 🛠️ **Plugin ID sanitization.** Creating Functions or Tools with emojis or special characters in their names now generates valid IDs that pass backend validation, instead of failing with an error. [#22695](https://github.com/open-webui/open-webui/pull/22695)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-25-4-editor-experience-changes-in-v0-8-11|4 Editor Experience changes in v0.8.11]] · Editor Experience
- [[Changes/Open WebUI/2026-03-25-rag-query-generation-robustness-the-rag-query-generation-web-search-and-image-ge|🔍 RAG query generation robustness. The RAG query generation, web search…]] · Image Generation
- [[Changes/Open WebUI/2026-03-25-shared-chat-viewing-crash-shared-chats-can-now-be-viewed-by-unauthenticated-user|🐛 Shared chat viewing crash. Shared chats can now be viewed by unauthenticated…]] · Collaboration
- [[Changes/Open WebUI/2026-03-25-11-account-and-access-changes-in-v0-8-11|11 Account and Access changes in v0.8.11]] · Account and Access
- [[Changes/Open WebUI/2026-03-25-3-context-window-changes-in-v0-8-11|3 Context Window changes in v0.8.11]] · Context Window
- [[Changes/Open WebUI/2026-03-25-2-search-and-browsing-changes-in-v0-8-11|2 Search and Browsing changes in v0.8.11]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-25-2-files-and-data-changes-in-v0-8-11|2 Files and Data changes in v0.8.11]] · Files and Data
- [[Changes/Open WebUI/2026-03-25-4-memory-and-personalization-changes-in-v0-8-11|4 Memory and Personalization changes in v0.8.11]] · Memory and Personalization
- [[Changes/Open WebUI/2026-03-25-17-interface-experience-changes-in-v0-8-11|17 Interface Experience changes in v0.8.11]] · Interface Experience
- [[Changes/Open WebUI/2026-03-25-5-reliability-and-performance-changes-in-v0-8-11|5 Reliability and Performance changes in v0.8.11]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-25-tool-binary-response-handling-tool-servers-can-now-return-binary-data-such-as-im|🏮 Tool binary response handling. Tool servers can now return binary data such…]] · Multimodal Input
- [[Changes/Open WebUI/2026-03-25-23-model-support-changes-in-v0-8-11|23 Model Support changes in v0.8.11]] · Model Support
- [[Changes/Open WebUI/2026-03-25-4-safety-and-privacy-changes-in-v0-8-11|4 Safety and Privacy changes in v0.8.11]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-25-34-developer-workflow-changes-in-v0-8-11|34 Developer Workflow changes in v0.8.11]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-25-metrics-export-interval-configuration-administrators-can-now-control-opentelemet|📊 Metrics export interval configuration. Administrators can now control…]] · Pricing Model
- [[Changes/Open WebUI/2026-03-25-19-other-changes-in-v0-8-11|19 other changes in v0.8.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-25 · Ollama · [[Changes/Ollama/2026-03-25-openclaw-integration-improvements-for-gateway-checks|OpenClaw integration improvements for gateway checks]]
- Later: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-5-apps-and-integrations-changes-in-v2-1-84|5 Apps and Integrations changes in v2.1.84]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-25-a6a0cc&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-25-3-apps-and-integrations-changes-in-v0-8-11.md%0ACard%20ID%3A%20open-webui-2026-03-25-a6a0cc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->