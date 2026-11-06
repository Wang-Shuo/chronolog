---
card_id: open-webui-2026-02-23-588a3c
date: '2026-02-23'
description: "Open WebUI · 2026-02-23 · Editor Experience: 2 changes in v0.8.4 — \U0001F4CB
  **Notes list payload optimization.** Notes list and search endpoints now return
  only a…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1077
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 32abc1bcd70d403c2a6a0c411714676e264594e7e149b5bac893fe5726905342
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-23-588a3c
  comparison: ''
  date: '2026-02-23'
  description: 'Open WebUI — v0.8.4: 2 Editor Experience changes'
  evidence:
  - quote: "\U0001F4CB **Notes list payload optimization.** Notes list and search
      endpoints now return only a 200-character preview instead of the full note content,
      reducing response payload from ~167 MB to ~10 KB for 60 notes and eliminating
      N+1 queries for access grants. The Notes tab now loads in seconds instead of
      tens of seconds. [#21549](https://github.com/open-webui/open-webui/pull/21549)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F4A5 **Admin functions page crash fix.** The admin Functions tab
      no longer crashes when clicked, fixing a null reference error that occurred
      while the functions list was loading. [#21661](https://github.com/open-webui/open-webui/pull/21661),
      [Commit](https://github.com/open-webui/open-webui/commit/8265422ba0660e7ba2192eb19efd70f8be652748)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-editor-experience-changes-in-v0-8-4
  source_release: open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c
  source_type: github_releases
  theme: editor-experience
  title: 2 Editor Experience changes in v0.8.4
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-19-simple-mode-claude-code-simple-now-includes-the-file-edit-tool-in-addition-to-th|Simple
  mode (CLAUDE_CODE_SIMPLE) now includes the file edit tool in addition…]]'
- '[[Changes/GitHub Copilot CLI/2026-02-19-3-editor-experience-changes-in-v0-0-412|3
  Editor Experience changes in v0.0.412]]'
- '[[Changes/Lovable/2026-02-23-the-plan-mode-https-docs-lovable-dev-features-plan-mode-md-editor-now-uses-a-ren|The
  Plan mode((source link) editor now uses…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c]]'
source_type: github_releases
theme: editor-experience
title: 2 Editor Experience changes in v0.8.4
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Editor Experience changes in v0.8.4

**Open WebUI** · 2026-02-23 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.4) · from [[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|v0.8.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📋 **Notes list payload optimization.** Notes list and search endpoints now return only a 200-character preview instead of the full note content, reducing response payload from ~167 MB to ~10 KB for 60 notes and eliminating N+1 queries for access grants. The Notes tab now loads in seconds instead of tens of seconds. [#21549](https://github.com/open-webui/open-webui/pull/21549)

> 💥 **Admin functions page crash fix.** The admin Functions tab no longer crashes when clicked, fixing a null reference error that occurred while the functions list was loading. [#21661](https://github.com/open-webui/open-webui/pull/21661), [Commit](https://github.com/open-webui/open-webui/commit/8265422ba0660e7ba2192eb19efd70f8be652748)

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
- [[Changes/Open WebUI/2026-02-23-4-search-and-browsing-changes-in-v0-8-4|4 Search and Browsing changes in v0.8.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-02-23-mcp-ssl-verification-fix-mcp-tool-connections-now-properly-respect-the-aiohttp-c|🔓 MCP SSL verification fix. MCP tool connections now properly respect…]] · Apps and Integrations
- [[Changes/Open WebUI/2026-02-23-file-access-control-respect-the-files-list-and-search-endpoints-now-properly-res|🗄️ File access control respect. The files list and search endpoints now properly…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-02-23-3-account-and-access-changes-in-v0-8-4|3 Account and Access changes in v0.8.4]] · Account and Access
- [[Changes/Open WebUI/2026-02-23-3-safety-and-privacy-changes-in-v0-8-4|3 Safety and Privacy changes in v0.8.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-02-23-16-model-support-changes-in-v0-8-4|16 Model Support changes in v0.8.4]] · Model Support
- [[Changes/Open WebUI/2026-02-23-api-tools-fix-the-api-v1-chat-completions-endpoint-now-properly-respects-caller|🛠️ API tools fix. The /api/v1/chat/completions endpoint now properly respects…]] · Agent Mode
- [[Changes/Open WebUI/2026-02-23-15-other-changes-in-v0-8-4|15 other changes in v0.8.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-02-23 · Lovable · [[Changes/Lovable/2026-02-23-the-plan-mode-https-docs-lovable-dev-features-plan-mode-md-editor-now-uses-a-ren|The Plan mode((source link) editor now uses…]]
- Later: 2026-02-23 · v0 · [[Changes/v0/2026-02-23-improved-payment-failure-handling-with-automatic-refresh-when-returning-to-the-t|Improved payment failure handling with automatic refresh when returning to the tab]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-23-588a3c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-23-2-editor-experience-changes-in-v0-8-4.md%0ACard%20ID%3A%20open-webui-2026-02-23-588a3c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->