---
card_id: open-webui-2026-01-09-a02aaa
date: '2026-01-09'
description: "Open WebUI · 2026-01-09 · Account and Access: 3 changes in v0.7.0 —
  \U0001F4DA Users can now ask the model to search their knowledge bases and retrieve
  documents…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1016
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2094a75eaeebcd9eae134dde08c1ad4291d66d35a0f371836a600c41148ca84d
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-01-09-a02aaa
  comparison: ''
  date: '2026-01-09'
  description: 'Open WebUI — v0.7.0: 3 Account and Access changes'
  evidence:
  - quote: "\U0001F4DA Users can now ask the model to search their knowledge bases
      and retrieve documents without manually attaching files—for example, \"find
      the section about authentication in our API docs\" or \"what do our internal
      guidelines say about X?\" [Commit](https://github.com/open-webui/open-webui/commit/c8622adcb01f3091b17ca50f8c8e2f20c7b9cd2a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001FA9D Channel managers can now create webhooks to allow external
      services to post messages to channels without authentication. [Commit](https://github.com/open-webui/open-webui/commit/cd296fcf0d79cecd1a6a3ee4e492c6b5246ca7ae)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: ⏱️ Administrators using custom "AIOHTTP_CLIENT_TIMEOUT" settings now see
      the configured timeout correctly applied to embedding generation, OAuth discovery,
      webhook calls, and tool/function loading instead of falling back to the default
      300-second timeout. [Commit](https://github.com/open-webui/open-webui/commit/e67891a374625d9888ec391da561f0b4ed79ed5d)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-account-and-access-changes-in-v0-7-0
  source_release: open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c
  source_type: github_releases
  theme: account-access
  title: 3 Account and Access changes in v0.7.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-01-07-2-account-and-access-changes-in-rust-v0-79-0|2 Account
  and Access changes in rust-v0.79.0]]'
- '[[Changes/Gemini CLI/2026-01-07-validate-oauth-resource-parameter-matches-mcp-server-url-by-galz10-in-https-gith|Validate
  OAuth resource parameter matches MCP server URL]]'
- '[[Changes/OpenCode/2026-01-08-core-use-correct-authorization-server-url-for-oauth-discovery-in-mcp|Core
  Use correct authorization server URL for OAuth discovery in MCP]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c]]'
source_type: github_releases
theme: account-access
title: 3 Account and Access changes in v0.7.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Account and Access changes in v0.7.0

**Open WebUI** · 2026-01-09 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.7.0) · from [[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|v0.7.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📚 Users can now ask the model to search their knowledge bases and retrieve documents without manually attaching files—for example, "find the section about authentication in our API docs" or "what do our internal guidelines say about X?" [Commit](https://github.com/open-webui/open-webui/commit/c8622adcb01f3091b17ca50f8c8e2f20c7b9cd2a)

> 🪝 Channel managers can now create webhooks to allow external services to post messages to channels without authentication. [Commit](https://github.com/open-webui/open-webui/commit/cd296fcf0d79cecd1a6a3ee4e492c6b5246ca7ae)

> ⏱️ Administrators using custom "AIOHTTP_CLIENT_TIMEOUT" settings now see the configured timeout correctly applied to embedding generation, OAuth discovery, webhook calls, and tool/function loading instead of falling back to the default 300-second timeout. [Commit](https://github.com/open-webui/open-webui/commit/e67891a374625d9888ec391da561f0b4ed79ed5d)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-01-09-3-editor-experience-changes-in-v0-7-0|3 Editor Experience changes in v0.7.0]] · Editor Experience
- [[Changes/Open WebUI/2026-01-09-users-on-windows-now-see-correctly-preserved-line-breaks-when-using-the-clipboar|📋 Users on Windows now see correctly preserved line breaks when using…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-01-09-2-memory-and-personalization-changes-in-v0-7-0|2 Memory and Personalization changes in v0.7.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-01-09-4-search-and-browsing-changes-in-v0-7-0|4 Search and Browsing changes in v0.7.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-01-09-3-apps-and-integrations-changes-in-v0-7-0|3 Apps and Integrations changes in v0.7.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-01-09-5-files-and-data-changes-in-v0-7-0|5 Files and Data changes in v0.7.0]] · Files and Data
- [[Changes/Open WebUI/2026-01-09-3-context-window-changes-in-v0-7-0|3 Context Window changes in v0.7.0]] · Context Window
- [[Changes/Open WebUI/2026-01-09-9-reliability-and-performance-changes-in-v0-7-0|9 Reliability and Performance changes in v0.7.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-01-09-6-safety-and-privacy-changes-in-v0-7-0|6 Safety and Privacy changes in v0.7.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-01-09-4-image-generation-changes-in-v0-7-0|4 Image Generation changes in v0.7.0]] · Image Generation
- [[Changes/Open WebUI/2026-01-09-5-interface-experience-changes-in-v0-7-0|5 Interface Experience changes in v0.7.0]] · Interface Experience
- [[Changes/Open WebUI/2026-01-09-11-model-support-changes-in-v0-7-0|11 Model Support changes in v0.7.0]] · Model Support
- [[Changes/Open WebUI/2026-01-09-24-developer-workflow-changes-in-v0-7-0|24 Developer Workflow changes in v0.7.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-01-09-3-voice-and-audio-changes-in-v0-7-0|3 Voice and Audio changes in v0.7.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-01-09-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-01-09-26-other-changes-in-v0-7-0|26 other changes in v0.7.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-01-08 · OpenCode · [[Changes/OpenCode/2026-01-08-core-use-correct-authorization-server-url-for-oauth-discovery-in-mcp|Core Use correct authorization server URL for OAuth discovery in MCP]]
- Later: 2026-01-09 · OpenCode · [[Changes/OpenCode/2026-01-09-terminal-enable-api-key-prompt-for-bedrock-in-auth-login|Terminal Enable API key prompt for Bedrock in auth login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-01-09-a02aaa&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-01-09-3-account-and-access-changes-in-v0-7-0.md%0ACard%20ID%3A%20open-webui-2026-01-09-a02aaa%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.7.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->