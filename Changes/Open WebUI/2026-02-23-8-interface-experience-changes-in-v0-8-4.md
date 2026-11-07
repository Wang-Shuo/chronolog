---
card_id: open-webui-2026-02-23-576433
date: '2026-02-23'
description: "Open WebUI · 2026-02-23 · Interface Experience: 8 changes in v0.8.4
  — \U0001F3F7️ **Sort by dropdown.** Administrators can now sort groups using a dropdown
  menu with…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2507
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8220e4fc977640f6cc3947be89ab35539eb3ac7729f28fb308baafb9d835fe6b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-23-576433
  comparison: ''
  date: '2026-02-23'
  description: 'Open WebUI — v0.8.4: 8 Interface Experience changes'
  evidence:
  - quote: "\U0001F3F7️ **Sort by dropdown.** Administrators can now sort groups using
      a dropdown menu with options for Name or Members, replacing the previous clickable
      column headers."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F517 **Admin settings tab navigation.** The admin settings sidebar
      now supports native browser tab opening, allowing users to middle-click or right-click
      to open settings pages in new tabs. The navigation was converted from button-based
      to anchor-based elements. [#21721](https://github.com/open-webui/open-webui/pull/21721)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F480 **Cyclic chat history deadlock fix.** Chat histories with circular
      parent-child message references no longer cause the backend to freeze when syncing
      usage stats. The system now detects and safely aborts when encountering cyclic
      message references. [#21681](https://github.com/open-webui/open-webui/pull/21681)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F5B1️ **User menu drag and click fixes.** Fixed draggable ghost
      images when dragging menu items and eliminated phantom link clicks that occurred
      when dragging outside dropdown menus. [#21699](https://github.com/open-webui/open-webui/pull/21699)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F9ED **Admin and workspace nav drag fix.** Fixed ghost drag images
      when dragging top navigation tabs in the Admin and Workspace panels by adding
      proper drag constraints and text selection prevention. [#21701](https://github.com/open-webui/open-webui/pull/21701)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F3AE **Playground nav drag fix.** Fixed ghost drag images when dragging
      top navigation tabs in the Playground panel by adding proper drag constraints
      and text selection prevention. [#21704](https://github.com/open-webui/open-webui/pull/21704)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: ✋ **Dropdown menu drag fix.** Dropdown menu items can no longer be accidentally
      dragged as ghost images when highlighting text, making menu interactions smoother.
      [#21713](https://github.com/open-webui/open-webui/pull/21713)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F5C2️ **Folder menu drag fix.** Folder dropdown menu items can no
      longer be accidentally highlighted or dragged as ghost images, making folder
      options behave like standard menus. [#21753](https://github.com/open-webui/open-webui/pull/21753)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 8-interface-experience-changes-in-v0-8-4
  source_release: open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c
  source_type: github_releases
  theme: interface-experience
  title: 8 Interface Experience changes in v0.8.4
  type: change
related_changes:
- '[[Changes/OpenCode/2026-02-19-core-don-t-fetch-models-dev-on-completion|Core Don''t
  fetch models.dev on completion]]'
- '[[Changes/GitHub Copilot CLI/2026-02-20-add-configurable-status-line-support-to-display-dynamic-session-information-via|Add
  configurable status line support to display dynamic session information…]]'
- '[[Changes/Lovable/2026-02-23-drag-and-drop-reordering-of-pinned-tools-in-the-project-navigation-bar-has-been|Drag
  and drop reordering of pinned tools in the project navigation bar has been…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c]]'
source_type: github_releases
theme: interface-experience
title: 8 Interface Experience changes in v0.8.4
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Interface Experience changes in v0.8.4

**Open WebUI** · 2026-02-23 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.4) · from [[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|v0.8.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🏷️ **Sort by dropdown.** Administrators can now sort groups using a dropdown menu with options for Name or Members, replacing the previous clickable column headers.

> 🔗 **Admin settings tab navigation.** The admin settings sidebar now supports native browser tab opening, allowing users to middle-click or right-click to open settings pages in new tabs. The navigation was converted from button-based to anchor-based elements. [#21721](https://github.com/open-webui/open-webui/pull/21721)

> 💀 **Cyclic chat history deadlock fix.** Chat histories with circular parent-child message references no longer cause the backend to freeze when syncing usage stats. The system now detects and safely aborts when encountering cyclic message references. [#21681](https://github.com/open-webui/open-webui/pull/21681)

> 🖱️ **User menu drag and click fixes.** Fixed draggable ghost images when dragging menu items and eliminated phantom link clicks that occurred when dragging outside dropdown menus. [#21699](https://github.com/open-webui/open-webui/pull/21699)

> 🧭 **Admin and workspace nav drag fix.** Fixed ghost drag images when dragging top navigation tabs in the Admin and Workspace panels by adding proper drag constraints and text selection prevention. [#21701](https://github.com/open-webui/open-webui/pull/21701)

> 🎮 **Playground nav drag fix.** Fixed ghost drag images when dragging top navigation tabs in the Playground panel by adding proper drag constraints and text selection prevention. [#21704](https://github.com/open-webui/open-webui/pull/21704)

> ✋ **Dropdown menu drag fix.** Dropdown menu items can no longer be accidentally dragged as ghost images when highlighting text, making menu interactions smoother. [#21713](https://github.com/open-webui/open-webui/pull/21713)

> 🗂️ **Folder menu drag fix.** Folder dropdown menu items can no longer be accidentally highlighted or dragged as ghost images, making folder options behave like standard menus. [#21753](https://github.com/open-webui/open-webui/pull/21753)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-23-12-developer-workflow-changes-in-v0-8-4|12 Developer Workflow changes in v0.8.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-23-10-reliability-and-performance-changes-in-v0-8-4|10 Reliability and Performance changes in v0.8.4]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-23-text-file-type-detection-fix-typescript-and-other-text-files-that-were-mis-detec|📄 Text file type detection fix. TypeScript and other text files…]] · Multimodal Input
- [[Changes/Open WebUI/2026-02-23-2-memory-and-personalization-changes-in-v0-8-4|2 Memory and Personalization changes in v0.8.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-02-23-ui-accessibility-improvements-screen-reader-users-can-now-navigate-the-interface|♿ UI accessibility improvements. Screen reader users can now navigate…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-02-23-2-editor-experience-changes-in-v0-8-4|2 Editor Experience changes in v0.8.4]] · Editor Experience
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
## Nearby in Interface Experience

- Earlier: 2026-02-23 · Lovable · [[Changes/Lovable/2026-02-23-drag-and-drop-reordering-of-pinned-tools-in-the-project-navigation-bar-has-been|Drag and drop reordering of pinned tools in the project navigation bar has been…]]
- Later: 2026-02-23 · Superwhisper · [[Changes/Superwhisper/2026-02-23-new-input-device-auto-selection|New input device auto-selection]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-23-576433&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-23-8-interface-experience-changes-in-v0-8-4.md%0ACard%20ID%3A%20open-webui-2026-02-23-576433%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->