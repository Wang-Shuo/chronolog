---
card_id: open-webui-2026-02-23-a4200f
date: '2026-02-23'
description: "Open WebUI · 2026-02-23 · Enterprise and Administration: \U0001F5C4️
  **File access control respect.** The files list and search endpoints now properly
  respect the…"
diffusion:
  first_in_tracked: '[[Changes/Gemini/2023-05-05-access-for-google-workspace-accounts|Access
    for Google Workspace accounts]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1025
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: f6d7bff9e027fe3e612c6f4356bc6dc1246c2f30d0b315c2ccf669a172fbb5a8
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-23-a4200f
  comparison: ''
  date: '2026-02-23'
  description: "Open WebUI — v0.8.4: \U0001F5C4️ **File access control respect.**
    The files list and search endpoints now properly respect the BYPASS_ADMIN_ACCESS_CONTROL
    setting, ensuring admins only see their own files when the setting is disabled,
    consistent with other endpoints. [#21595](https://github.com/open-webui/open-webui/pull/21595),
    [#21589](https://github.com/open-webui/open-webui/issues/21589)"
  evidence:
  - quote: "\U0001F5C4️ **File access control respect.** The files list and search
      endpoints now properly respect the BYPASS_ADMIN_ACCESS_CONTROL setting, ensuring
      admins only see their own files when the setting is disabled, consistent with
      other endpoints. [#21595](https://github.com/open-webui/open-webui/pull/21595),
      [#21589](https://github.com/open-webui/open-webui/issues/21589)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: open-webui
  product_name: Open WebUI
  slug: file-access-control-respect-the-files-list-and-search-endpoints-now-properly-res
  source_release: open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c
  source_type: github_releases
  theme: enterprise-admin
  title: "\U0001F5C4️ **File access control respect.** The files list and search endpoints
    now properly…"
  type: change
related_changes:
- '[[Changes/Replit/2026-02-20-teams-and-enterprise|Teams and Enterprise]]'
- '[[Changes/Lovable/2026-02-23-admin-controls-for-app-connectors|Admin controls for
  app connectors]]'
- '[[Changes/Lovable/2026-02-23-scim-provisioning|SCIM provisioning]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c]]'
source_type: github_releases
theme: enterprise-admin
title: "\U0001F5C4️ File access control respect. The files list and search endpoints
  now properly…"
type: change
---

<!-- chronolog:begin region="header" -->
# 🗄️ **File access control respect.** The files list and search endpoints now properly…

**Open WebUI** · 2026-02-23 · [[Themes/enterprise-admin|Enterprise and Administration]] · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.4) · from [[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|v0.8.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> 🗄️ **File access control respect.** The files list and search endpoints now properly respect the BYPASS_ADMIN_ACCESS_CONTROL setting, ensuring admins only see their own files when the setting is disabled, consistent with other endpoints. [#21595](https://github.com/open-webui/open-webui/pull/21595), [#21589](https://github.com/open-webui/open-webui/issues/21589)
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
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
- [[Changes/Open WebUI/2026-02-23-3-account-and-access-changes-in-v0-8-4|3 Account and Access changes in v0.8.4]] · Account and Access
- [[Changes/Open WebUI/2026-02-23-3-safety-and-privacy-changes-in-v0-8-4|3 Safety and Privacy changes in v0.8.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-02-23-16-model-support-changes-in-v0-8-4|16 Model Support changes in v0.8.4]] · Model Support
- [[Changes/Open WebUI/2026-02-23-api-tools-fix-the-api-v1-chat-completions-endpoint-now-properly-respects-caller|🛠️ API tools fix. The /api/v1/chat/completions endpoint now properly respects…]] · Agent Mode
- [[Changes/Open WebUI/2026-02-23-15-other-changes-in-v0-8-4|15 other changes in v0.8.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2026-02-23 · Lovable · [[Changes/Lovable/2026-02-23-scim-provisioning|SCIM provisioning]]
- Later: 2026-02-25 · Gemini CLI · [[Changes/Gemini CLI/2026-02-25-feat-admin-add-admin-controls-documentation-by-skeshive-in-https-github-com-goog|feat(admin): Add admin controls documentation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-05 · Gemini · [[Changes/Gemini/2023-05-05-access-for-google-workspace-accounts|Access for Google Workspace accounts]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-23-a4200f&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-23-file-access-control-respect-the-files-list-and-search-endpoints-now-properly-res.md%0ACard%20ID%3A%20open-webui-2026-02-23-a4200f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->