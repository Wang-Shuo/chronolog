---
card_id: open-webui-2026-03-25-e8cb95
date: '2026-03-25'
description: "Open WebUI · 2026-03-25 · Safety and Privacy: 4 changes in v0.8.11 —
  \U0001F512 **Model access control bypass.** Fixed a security vulnerability where
  external clients…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1074
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 82659e9147212216e44497f564785585c3f97c5fe67f9444c1f77c14b57d5332
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-25-e8cb95
  comparison: ''
  date: '2026-03-25'
  description: 'Open WebUI — v0.8.11: 4 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F512 **Model access control bypass.** Fixed a security vulnerability
      where external clients could bypass model access controls by setting a URL parameter,
      preventing unauthorized access to restricted models. [Commit](https://github.com/open-webui/open-webui/commit/c0385f60ba049da48d2d5452068586d375303c37)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F6E1️ **Terminal proxy path sanitization.** The terminal server
      proxy now properly sanitizes paths to prevent directory traversal and SSRF attacks,
      protecting against security vulnerabilities. [Commit](https://github.com/open-webui/open-webui/commit/f9d38a073fae32032ed44073cf2817cba20210bb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F510 **Collaborative document authorization.** Fixed a security
      vulnerability in collaborative documents where authorization could be bypassed
      using alternative document ID formats, preventing unauthorized access to notes.
      [Commit](https://github.com/open-webui/open-webui/commit/3107a5363d13c899a995c930cbb1121a80f754f9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F3AB **Password change complexity validation.** Password complexity
      rules are now properly enforced when users change their password, closing a
      security gap where new passwords could bypass configured complexity requirements.
      [Commit](https://github.com/open-webui/open-webui/commit/bd8aa3b6a0b6a2320f41b20a51b9842f39aadb7f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-safety-and-privacy-changes-in-v0-8-11
  source_release: open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in v0.8.11
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-20-2-safety-and-privacy-changes-in-v2-1-81|2 Safety
  and Privacy changes in v2.1.81]]'
- '[[Changes/Gemini CLI/2026-03-24-5-safety-and-privacy-changes-in-v0-35-0|5 Safety
  and Privacy changes in v0.35.0]]'
- '[[Changes/Claude Code/2026-03-25-2-safety-and-privacy-changes-in-v2-1-83|2 Safety
  and Privacy changes in v2.1.83]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in v0.8.11
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in v0.8.11

**Open WebUI** · 2026-03-25 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.11) · from [[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|v0.8.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔒 **Model access control bypass.** Fixed a security vulnerability where external clients could bypass model access controls by setting a URL parameter, preventing unauthorized access to restricted models. [Commit](https://github.com/open-webui/open-webui/commit/c0385f60ba049da48d2d5452068586d375303c37)

> 🛡️ **Terminal proxy path sanitization.** The terminal server proxy now properly sanitizes paths to prevent directory traversal and SSRF attacks, protecting against security vulnerabilities. [Commit](https://github.com/open-webui/open-webui/commit/f9d38a073fae32032ed44073cf2817cba20210bb)

> 🔐 **Collaborative document authorization.** Fixed a security vulnerability in collaborative documents where authorization could be bypassed using alternative document ID formats, preventing unauthorized access to notes. [Commit](https://github.com/open-webui/open-webui/commit/3107a5363d13c899a995c930cbb1121a80f754f9)

> 🎫 **Password change complexity validation.** Password complexity rules are now properly enforced when users change their password, closing a security gap where new passwords could bypass configured complexity requirements. [Commit](https://github.com/open-webui/open-webui/commit/bd8aa3b6a0b6a2320f41b20a51b9842f39aadb7f)

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
- [[Changes/Open WebUI/2026-03-25-3-apps-and-integrations-changes-in-v0-8-11|3 Apps and Integrations changes in v0.8.11]] · Apps and Integrations
- [[Changes/Open WebUI/2026-03-25-17-interface-experience-changes-in-v0-8-11|17 Interface Experience changes in v0.8.11]] · Interface Experience
- [[Changes/Open WebUI/2026-03-25-5-reliability-and-performance-changes-in-v0-8-11|5 Reliability and Performance changes in v0.8.11]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-25-tool-binary-response-handling-tool-servers-can-now-return-binary-data-such-as-im|🏮 Tool binary response handling. Tool servers can now return binary data such…]] · Multimodal Input
- [[Changes/Open WebUI/2026-03-25-23-model-support-changes-in-v0-8-11|23 Model Support changes in v0.8.11]] · Model Support
- [[Changes/Open WebUI/2026-03-25-34-developer-workflow-changes-in-v0-8-11|34 Developer Workflow changes in v0.8.11]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-25-metrics-export-interval-configuration-administrators-can-now-control-opentelemet|📊 Metrics export interval configuration. Administrators can now control…]] · Pricing Model
- [[Changes/Open WebUI/2026-03-25-19-other-changes-in-v0-8-11|19 other changes in v0.8.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-25 · Claude Code · [[Changes/Claude Code/2026-03-25-2-safety-and-privacy-changes-in-v2-1-83|2 Safety and Privacy changes in v2.1.83]]
- Later: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-fixed-the-allow-claude-to-edit-its-own-settings-for-this-session-permission-opti|Fixed the "allow Claude to edit its own settings for this session" permission option…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-25-e8cb95&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-25-4-safety-and-privacy-changes-in-v0-8-11.md%0ACard%20ID%3A%20open-webui-2026-03-25-e8cb95%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->