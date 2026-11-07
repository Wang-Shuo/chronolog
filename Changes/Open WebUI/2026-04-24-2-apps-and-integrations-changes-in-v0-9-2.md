---
card_id: open-webui-2026-04-24-8cc66d
date: '2026-04-24'
description: "Open WebUI · 2026-04-24 · Apps and Integrations: 2 changes in v0.9.2
  — \U0001F527 **MCP task cancellation stability.** Interrupted MCP tool calls no
  longer cause CPU…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1128
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 748ec52a2136ba69652b880c98808e04314fe56ead29469f8af93f87f8b0239b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-24-8cc66d
  comparison: ''
  date: '2026-04-24'
  description: 'Open WebUI — v0.9.2: 2 Apps and Integrations changes'
  evidence:
  - quote: "\U0001F527 **MCP task cancellation stability.** Interrupted MCP tool calls
      no longer cause CPU spikes or runaway cleanup behavior. MCP client disconnection
      now runs in the same asyncio task as connection, respecting cancel scope constraints,
      and chat-active events are properly shielded during cancellation."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F504 **MCP resource content handling.** MCP tool results with the
      `resource` content type are now correctly detected and their `resource.text`
      payload is extracted, instead of being silently ignored."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-apps-and-integrations-changes-in-v0-9-2
  source_release: open-webui-2026-04-24-v0-9-2-github-313142735-f0842502
  source_type: github_releases
  theme: apps-integrations
  title: 2 Apps and Integrations changes in v0.9.2
  type: change
related_changes:
- '[[Changes/Lovable/2026-04-24-productivity-app-connectors-google-workspace-microsoft-365|Productivity
  app connectors: Google Workspace, Microsoft 365]]'
- '[[Changes/Lovable/2026-04-24-saml-2-0-single-sign-on-for-your-apps|SAML 2.0 single
  sign-on for your apps]]'
- '[[Changes/Lovable/2026-04-24-chat-connectors-sentry-mcp|Chat connectors: Sentry
  MCP]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-24-v0-9-2-github-313142735-f0842502|open-webui-2026-04-24-v0-9-2-github-313142735-f0842502]]'
source_type: github_releases
theme: apps-integrations
title: 2 Apps and Integrations changes in v0.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Apps and Integrations changes in v0.9.2

**Open WebUI** · 2026-04-24 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.2) · from [[Releases/Open WebUI/open-webui-2026-04-24-v0-9-2-github-313142735-f0842502|v0.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔧 **MCP task cancellation stability.** Interrupted MCP tool calls no longer cause CPU spikes or runaway cleanup behavior. MCP client disconnection now runs in the same asyncio task as connection, respecting cancel scope constraints, and chat-active events are properly shielded during cancellation.

> 🔄 **MCP resource content handling.** MCP tool results with the `resource` content type are now correctly detected and their `resource.text` payload is extracted, instead of being silently ignored.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-24-2-memory-and-personalization-changes-in-v0-9-2|2 Memory and Personalization changes in v0.9.2]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-24-4-model-support-changes-in-v0-9-2|4 Model Support changes in v0.9.2]] · Model Support
- [[Changes/Open WebUI/2026-04-24-automation-model-detection-the-create-automation-tool-now-correctly-detects-the|🧩 Automation model detection. The create_automation tool now correctly detects…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-24-3-reliability-and-performance-changes-in-v0-9-2|3 Reliability and Performance changes in v0.9.2]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-24-3-context-window-changes-in-v0-9-2|3 Context Window changes in v0.9.2]] · Context Window
- [[Changes/Open WebUI/2026-04-24-2-editor-experience-changes-in-v0-9-2|2 Editor Experience changes in v0.9.2]] · Editor Experience
- [[Changes/Open WebUI/2026-04-24-3-account-and-access-changes-in-v0-9-2|3 Account and Access changes in v0.9.2]] · Account and Access
- [[Changes/Open WebUI/2026-04-24-paddleocr-vl-document-extraction-administrators-can-now-use-paddleocr-vl-as-a-co|🧠 PaddleOCR-vl document extraction. Administrators can now use PaddleOCR-vl…]] · Files and Data
- [[Changes/Open WebUI/2026-04-24-13-other-changes-in-v0-9-2|13 other changes in v0.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-24 · Lovable · [[Changes/Lovable/2026-04-24-chat-connectors-sentry-mcp|Chat connectors: Sentry MCP]]
- Later: 2026-04-24 · OpenCode · [[Changes/OpenCode/2026-04-24-added-an-experimental-http-api-endpoint-for-mcp-server-status|Added an experimental HTTP API endpoint for MCP server status]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-24-8cc66d&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-24-2-apps-and-integrations-changes-in-v0-9-2.md%0ACard%20ID%3A%20open-webui-2026-04-24-8cc66d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->