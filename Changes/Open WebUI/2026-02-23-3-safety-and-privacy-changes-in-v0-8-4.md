---
card_id: open-webui-2026-02-23-d27857
date: '2026-02-23'
description: "Open WebUI · 2026-02-23 · Safety and Privacy: 3 changes in v0.8.4 —
  \U0001F512 **Iframe sandbox security.** Embedded tools can no longer submit forms
  or access…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2036
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cb8ff91379e3b958b33b3ea4a2f22c74de315ce03f0429c2efe987098628eebe
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-23-d27857
  comparison: ''
  date: '2026-02-23'
  description: 'Open WebUI — v0.8.4: 3 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F512 **Iframe sandbox security.** Embedded tools can no longer submit
      forms or access same-origin content by default, improving security for users.
      [#21529](https://github.com/open-webui/open-webui/pull/21529)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F510 **Signup race condition fix.** Fixed a security vulnerability
      where multiple admin accounts could be created on fresh deployments when running
      multiple uvicorn workers. The signup handler now properly handles concurrent
      requests during first-user registration, preventing unauthorized admin privilege
      escalation. [#21631](https://github.com/open-webui/open-webui/pull/21631)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F512 **Model default feature permissions.** Model default features
      like code interpreter, web search, and image generation now respect global configuration
      and user permission settings, preventing disabled features from appearing in
      the chat input. [#21690](https://github.com/open-webui/open-webui/pull/21690)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-safety-and-privacy-changes-in-v0-8-4
  source_release: open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v0.8.4
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-02-23-workspaces|Workspaces]]'
- '[[Changes/Lovable/2026-02-23-guided-publishing-flow|Guided publishing flow]]'
- "[[Changes/Open WebUI/2026-02-23-backend-config-null-safety-language-detection-during-app-initialization-no-longe|\U0001F6E1️
  Backend config null safety. Language detection during app initialization no…]]"
source_release: '[[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v0.8.4
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v0.8.4

**Open WebUI** · 2026-02-23 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.4) · from [[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|v0.8.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔒 **Iframe sandbox security.** Embedded tools can no longer submit forms or access same-origin content by default, improving security for users. [#21529](https://github.com/open-webui/open-webui/pull/21529)

> 🔐 **Signup race condition fix.** Fixed a security vulnerability where multiple admin accounts could be created on fresh deployments when running multiple uvicorn workers. The signup handler now properly handles concurrent requests during first-user registration, preventing unauthorized admin privilege escalation. [#21631](https://github.com/open-webui/open-webui/pull/21631)

> 🔒 **Model default feature permissions.** Model default features like code interpreter, web search, and image generation now respect global configuration and user permission settings, preventing disabled features from appearing in the chat input. [#21690](https://github.com/open-webui/open-webui/pull/21690)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-23-12-developer-workflow-changes-in-v0-8-4|12 Developer Workflow changes in v0.8.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-23-10-reliability-and-performance-changes-in-v0-8-4|10 Reliability and Performance changes in v0.8.4]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-23-text-file-type-detection-fix-typescript-and-other-text-files-that-were-mis-detec|📄 Text file type detection fix. TypeScript and other text files…]] · Multimodal Input
- [[Changes/Open WebUI/2026-02-23-2-memory-and-personalization-changes-in-v0-8-4|2 Memory and Personalization changes in v0.8.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-02-23-ui-accessibility-improvements-screen-reader-users-can-now-navigate-the-interface|♿ UI accessibility improvements. Screen reader users can now navigate…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-02-23-8-interface-experience-changes-in-v0-8-4|8 Interface Experience changes in v0.8.4]] · Interface Experience
- [[Changes/Open WebUI/2026-02-23-2-editor-experience-changes-in-v0-8-4|2 Editor Experience changes in v0.8.4]] · Editor Experience
- [[Changes/Open WebUI/2026-02-23-4-search-and-browsing-changes-in-v0-8-4|4 Search and Browsing changes in v0.8.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-02-23-mcp-ssl-verification-fix-mcp-tool-connections-now-properly-respect-the-aiohttp-c|🔓 MCP SSL verification fix. MCP tool connections now properly respect…]] · Apps and Integrations
- [[Changes/Open WebUI/2026-02-23-file-access-control-respect-the-files-list-and-search-endpoints-now-properly-res|🗄️ File access control respect. The files list and search endpoints now properly…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-02-23-3-account-and-access-changes-in-v0-8-4|3 Account and Access changes in v0.8.4]] · Account and Access
- [[Changes/Open WebUI/2026-02-23-16-model-support-changes-in-v0-8-4|16 Model Support changes in v0.8.4]] · Model Support
- [[Changes/Open WebUI/2026-02-23-api-tools-fix-the-api-v1-chat-completions-endpoint-now-properly-respects-caller|🛠️ API tools fix. The /api/v1/chat/completions endpoint now properly respects…]] · Agent Mode
- [[Changes/Open WebUI/2026-02-23-15-other-changes-in-v0-8-4|15 other changes in v0.8.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-02-23 · Open WebUI · [[Changes/Open WebUI/2026-02-23-backend-config-null-safety-language-detection-during-app-initialization-no-longe|🛡️ Backend config null safety. Language detection during app initialization no…]]
- Later: 2026-02-24 · Claude Code · [[Changes/Claude Code/2026-02-24-3-safety-and-privacy-changes-in-v2-1-51|3 Safety and Privacy changes in v2.1.51]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-23-d27857&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-23-3-safety-and-privacy-changes-in-v0-8-4.md%0ACard%20ID%3A%20open-webui-2026-02-23-d27857%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->