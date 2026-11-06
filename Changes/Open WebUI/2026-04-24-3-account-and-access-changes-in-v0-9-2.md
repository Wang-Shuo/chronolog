---
card_id: open-webui-2026-04-24-d2aa1f
date: '2026-04-24'
description: "Open WebUI · 2026-04-24 · Account and Access: 3 changes in v0.9.2 —
  \U0001F511 **Custom API key header.** Administrators can now configure a custom
  header name for API…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1121
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 937dc9de25967dad5a99ed5f375a460c80becf6dee7d3390d9752108b2cb73b2
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-24-d2aa1f
  comparison: ''
  date: '2026-04-24'
  description: 'Open WebUI — v0.9.2: 3 Account and Access changes'
  evidence:
  - quote: "\U0001F511 **Custom API key header.** Administrators can now configure
      a custom header name for API key authentication via the `CUSTOM_API_KEY_HEADER`
      environment variable, enabling compatibility with reverse proxies that use the
      `Authorization` header for their own authentication."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F50C **OAuth session disconnection.** Users can now disconnect OAuth
      sessions for specific providers (e.g., MCP connections) through a new API endpoint,
      enabling cleaner re-authentication workflows."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F310 **OAuth discovery fallback.** OAuth protected resource discovery
      now falls back to well-known RFC 9728 URIs when the `WWW-Authenticate` header
      doesn't contain a `resource_metadata` link, improving compatibility with more
      MCP server implementations."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-account-and-access-changes-in-v0-9-2
  source_release: open-webui-2026-04-24-v0-9-2-github-313142735-f0842502
  source_type: github_releases
  theme: account-access
  title: 3 Account and Access changes in v0.9.2
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-04-22-we-re-launching-chatgpt-for-clinicians-a-free-version-of-chatgpt-for-verified-cl|ChatGPT
  for Clinicians]]'
- '[[Changes/Gemini CLI/2026-04-23-docs-correct-documentation-for-enforced-authentication-type-by-cocosheng-g-in-ht|docs:
  correct documentation for enforced authentication type]]'
- '[[Changes/GitHub Copilot CLI/2026-04-23-2-account-and-access-changes-in-v1-0-35|2
  Account and Access changes in v1.0.35]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-24-v0-9-2-github-313142735-f0842502|open-webui-2026-04-24-v0-9-2-github-313142735-f0842502]]'
source_type: github_releases
theme: account-access
title: 3 Account and Access changes in v0.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Account and Access changes in v0.9.2

**Open WebUI** · 2026-04-24 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.2) · from [[Releases/Open WebUI/open-webui-2026-04-24-v0-9-2-github-313142735-f0842502|v0.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔑 **Custom API key header.** Administrators can now configure a custom header name for API key authentication via the `CUSTOM_API_KEY_HEADER` environment variable, enabling compatibility with reverse proxies that use the `Authorization` header for their own authentication.

> 🔌 **OAuth session disconnection.** Users can now disconnect OAuth sessions for specific providers (e.g., MCP connections) through a new API endpoint, enabling cleaner re-authentication workflows.

> 🌐 **OAuth discovery fallback.** OAuth protected resource discovery now falls back to well-known RFC 9728 URIs when the `WWW-Authenticate` header doesn't contain a `resource_metadata` link, improving compatibility with more MCP server implementations.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-24-2-memory-and-personalization-changes-in-v0-9-2|2 Memory and Personalization changes in v0.9.2]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-24-4-model-support-changes-in-v0-9-2|4 Model Support changes in v0.9.2]] · Model Support
- [[Changes/Open WebUI/2026-04-24-automation-model-detection-the-create-automation-tool-now-correctly-detects-the|🧩 Automation model detection. The create_automation tool now correctly detects…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-24-3-reliability-and-performance-changes-in-v0-9-2|3 Reliability and Performance changes in v0.9.2]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-24-3-context-window-changes-in-v0-9-2|3 Context Window changes in v0.9.2]] · Context Window
- [[Changes/Open WebUI/2026-04-24-2-apps-and-integrations-changes-in-v0-9-2|2 Apps and Integrations changes in v0.9.2]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-24-2-editor-experience-changes-in-v0-9-2|2 Editor Experience changes in v0.9.2]] · Editor Experience
- [[Changes/Open WebUI/2026-04-24-paddleocr-vl-document-extraction-administrators-can-now-use-paddleocr-vl-as-a-co|🧠 PaddleOCR-vl document extraction. Administrators can now use PaddleOCR-vl…]] · Files and Data
- [[Changes/Open WebUI/2026-04-24-13-other-changes-in-v0-9-2|13 other changes in v0.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-04-23 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-23-2-account-and-access-changes-in-v1-0-35|2 Account and Access changes in v1.0.35]]
- Later: 2026-04-28 · Claude Code · [[Changes/Claude Code/2026-04-28-clarified-the-mcp-message-shown-when-an-mcp-server-is-still-unauthorized-after-t|Clarified the /mcp message shown when an MCP server is still unauthorized after…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-24-d2aa1f&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-24-3-account-and-access-changes-in-v0-9-2.md%0ACard%20ID%3A%20open-webui-2026-04-24-d2aa1f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->