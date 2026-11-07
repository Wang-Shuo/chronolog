---
card_id: open-webui-2025-12-21-a258c8
date: '2025-12-21'
description: "Open WebUI · 2025-12-21 · Interface Experience: 8 changes in v0.6.42
  — \U0001FA9F Sidebar width is now resizable on desktop devices with persistent storage
  in…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2443
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 06443e6eea639f594bed1eae7e314ed1bc8348b22352de5200a635bd69bead0a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-21-a258c8
  comparison: ''
  date: '2025-12-21'
  description: 'Open WebUI — v0.6.42: 8 Interface Experience changes'
  evidence:
  - quote: "\U0001FA9F Sidebar width is now resizable on desktop devices with persistent
      storage in localStorage, enforcing minimum and maximum width constraints (220px
      to 480px) while all layout components now reference the dynamic sidebar width
      via CSS variables for consistent responsive behavior. [Commit](https://github.com/open-webui/open-webui/commit/b364cf43d3e8fd3557f65f17bc285bfaca5ed368)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4C4 Notes can now be created directly from the chat input field,
      allowing users to save drafted messages or content as notes without navigation
      or retyping. [Commit](https://github.com/open-webui/open-webui/commit/00c2b6ca405d617e3d7520953a00a36c19c790ec)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001FA9F Sidebar folders, channels, and pinned models sections now automatically
      expand when creating new items or pinning models, providing immediate visual
      feedback for user actions. [Commit](https://github.com/open-webui/open-webui/commit/f826d3ed75213a0a1b31b50d030bfb1d5e91d199),
      [#19929](https://github.com/open-webui/open-webui/pull/19929)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4CF Chat input now displays an expand button in the top-right corner
      when messages exceed two lines, providing optional access to a full-screen editor
      for composing longer messages with enhanced workspace and visibility while temporarily
      disabling the main input to prevent editing conflicts. [Commit](https://github.com/open-webui/open-webui/commit/205c7111200c22da42e9b5fe1e676aec9cca6daa)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F465 User selection in the \"Edit User Group\" modal now preserves
      pagination position, allowing administrators to select multiple users across
      pages without resetting to page 1. [#19959](https://github.com/open-webui/open-webui/pull/19959)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4D1 Source citation rendering errors when citation syntax appeared
      in user messages or contexts without source data were resolved. [Commit](https://github.com/open-webui/open-webui/commit/3c8f1cf8e58d52e86375634b0381374298b1b4f3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: ⌨️ Regenerate response keyboard shortcut now only activates when chat input
      is selected, preventing unintended regeneration when modals are open or other
      UI elements are focused. [#19875](https://github.com/open-webui/open-webui/pull/19875)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F5E3️ MoA completion handling stability was improved with null safety
      checks for response objects, boolean casting for settings, and proper timeout
      type definitions. [#19921](https://github.com/open-webui/open-webui/pull/19921)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 8-interface-experience-changes-in-v0-6-42
  source_release: open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9
  source_type: github_releases
  theme: interface-experience
  title: 8 Interface Experience changes in v0.6.42
  type: change
related_changes:
- '[[Changes/OpenCode/2025-12-19-terminal-implement-smooth-scrolling-for-autocomplete-dropdown-navigation|Terminal
  Implement smooth scrolling for autocomplete dropdown navigation]]'
- '[[Changes/Replit/2025-12-19-status-dot-design-update|Status Dot Design Update]]'
- '[[Changes/Raycast/2025-12-20-you-ve-probably-seen-these-in-raycast-when-your-search-term-doesn-t-have-any-mat|You''ve
  probably seen these in Raycast, when your search term doesn''t have any…]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9]]'
source_type: github_releases
theme: interface-experience
title: 8 Interface Experience changes in v0.6.42
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Interface Experience changes in v0.6.42

**Open WebUI** · 2025-12-21 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.42) · from [[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|v0.6.42]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🪟 Sidebar width is now resizable on desktop devices with persistent storage in localStorage, enforcing minimum and maximum width constraints (220px to 480px) while all layout components now reference the dynamic sidebar width via CSS variables for consistent responsive behavior. [Commit](https://github.com/open-webui/open-webui/commit/b364cf43d3e8fd3557f65f17bc285bfaca5ed368)

> 📄 Notes can now be created directly from the chat input field, allowing users to save drafted messages or content as notes without navigation or retyping. [Commit](https://github.com/open-webui/open-webui/commit/00c2b6ca405d617e3d7520953a00a36c19c790ec)

> 🪟 Sidebar folders, channels, and pinned models sections now automatically expand when creating new items or pinning models, providing immediate visual feedback for user actions. [Commit](https://github.com/open-webui/open-webui/commit/f826d3ed75213a0a1b31b50d030bfb1d5e91d199), [#19929](https://github.com/open-webui/open-webui/pull/19929)

> 📏 Chat input now displays an expand button in the top-right corner when messages exceed two lines, providing optional access to a full-screen editor for composing longer messages with enhanced workspace and visibility while temporarily disabling the main input to prevent editing conflicts. [Commit](https://github.com/open-webui/open-webui/commit/205c7111200c22da42e9b5fe1e676aec9cca6daa)

> 👥 User selection in the "Edit User Group" modal now preserves pagination position, allowing administrators to select multiple users across pages without resetting to page 1. [#19959](https://github.com/open-webui/open-webui/pull/19959)

> 📑 Source citation rendering errors when citation syntax appeared in user messages or contexts without source data were resolved. [Commit](https://github.com/open-webui/open-webui/commit/3c8f1cf8e58d52e86375634b0381374298b1b4f3)

> ⌨️ Regenerate response keyboard shortcut now only activates when chat input is selected, preventing unintended regeneration when modals are open or other UI elements are focused. [#19875](https://github.com/open-webui/open-webui/pull/19875)

> 🗣️ MoA completion handling stability was improved with null safety checks for response objects, boolean casting for settings, and proper timeout type definitions. [#19921](https://github.com/open-webui/open-webui/pull/19921)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-21-user-uploaded-images-are-now-automatically-converted-from-base64-to-actual-file|🖼️ User-uploaded images are now automatically converted from base64 to actual file…]] · Collaboration
- [[Changes/Open WebUI/2025-12-21-3-editor-experience-changes-in-v0-6-42|3 Editor Experience changes in v0.6.42]] · Editor Experience
- [[Changes/Open WebUI/2025-12-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-21-2-apps-and-integrations-changes-in-v0-6-42|2 Apps and Integrations changes in v0.6.42]] · Apps and Integrations
- [[Changes/Open WebUI/2025-12-21-6-files-and-data-changes-in-v0-6-42|6 Files and Data changes in v0.6.42]] · Files and Data
- [[Changes/Open WebUI/2025-12-21-7-reliability-and-performance-changes-in-v0-6-42|7 Reliability and Performance changes in v0.6.42]] · Reliability and Performance
- [[Changes/Open WebUI/2025-12-21-11-model-support-changes-in-v0-6-42|11 Model Support changes in v0.6.42]] · Model Support
- [[Changes/Open WebUI/2025-12-21-6-safety-and-privacy-changes-in-v0-6-42|6 Safety and Privacy changes in v0.6.42]] · Safety and Privacy
- [[Changes/Open WebUI/2025-12-21-4-account-and-access-changes-in-v0-6-42|4 Account and Access changes in v0.6.42]] · Account and Access
- [[Changes/Open WebUI/2025-12-21-external-reranker-operations-were-optimized-to-prevent-event-loop-blocking-by-of|⚡ External reranker operations were optimized to prevent event loop blocking…]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-12-21-3-search-and-browsing-changes-in-v0-6-42|3 Search and Browsing changes in v0.6.42]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-21-11-developer-workflow-changes-in-v0-6-42|11 Developer Workflow changes in v0.6.42]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-21-2-multimodal-input-changes-in-v0-6-42|2 Multimodal Input changes in v0.6.42]] · Multimodal Input
- [[Changes/Open WebUI/2025-12-21-4-image-generation-changes-in-v0-6-42|4 Image Generation changes in v0.6.42]] · Image Generation
- [[Changes/Open WebUI/2025-12-21-2-voice-and-audio-changes-in-v0-6-42|2 Voice and Audio changes in v0.6.42]] · Voice and Audio
- [[Changes/Open WebUI/2025-12-21-channel-image-upload-handling-was-optimized-to-process-and-store-compressed-imag|🖼️ Channel image upload handling was optimized to process and store compressed…]] · Memory and Personalization
- [[Changes/Open WebUI/2025-12-21-28-other-changes-in-v0-6-42|28 other changes in v0.6.42]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2025-12-20 · Raycast · [[Changes/Raycast/2025-12-20-you-ve-probably-seen-these-in-raycast-when-your-search-term-doesn-t-have-any-mat|You've probably seen these in Raycast, when your search term doesn't have any…]]
- Later: 2025-12-22 · Cline · [[Changes/Cline/2025-12-22-model-picker-favorites-ordering-star-toggle-and-keyboard-navigation-for-openrout|Model picker favorites ordering, star toggle, and keyboard navigation for OpenRouter…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-21-a258c8&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-21-8-interface-experience-changes-in-v0-6-42.md%0ACard%20ID%3A%20open-webui-2025-12-21-a258c8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.42%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->