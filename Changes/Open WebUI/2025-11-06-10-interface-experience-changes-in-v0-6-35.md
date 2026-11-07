---
card_id: open-webui-2025-11-06-4e636b
date: '2025-11-06'
description: 'Open WebUI · 2025-11-06 · Interface Experience: 10 changes in v0.6.35
  — ⌨️ Keyboard shortcut hints are now displayed on sidebar buttons with a refactored…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2398
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 14d95877a8693b34a5d6123867005ac459e137fa79b398594038eefc9753eab1
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-11-06-4e636b
  comparison: ''
  date: '2025-11-06'
  description: 'Open WebUI — v0.6.35: 10 Interface Experience changes'
  evidence:
  - quote: ⌨️ Keyboard shortcut hints are now displayed on sidebar buttons with a
      refactored shortcuts modal that accurately reflects all available hotkeys across
      different keyboard layouts. [#18473](https://github.com/open-webui/open-webui/pull/18473)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F4CC Sidebar models section is now collapsible, allowing users to
      expand and collapse the pinned models list for better sidebar organization.
      [Commit](https://github.com/open-webui/open-webui/commit/82c08a3b5d189f81c96b6548cc872198771015b0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F4C8 Mermaid diagram rendering errors no longer cause UI unavailability
      or display error messages below the input box. [#18493](https://github.com/open-webui/open-webui/pull/18493),
      [#18340](https://github.com/open-webui/open-webui/issues/18340)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F50E Folder tag search in the sidebar now correctly handles folder
      names with multiple spaces by replacing all spaces with underscores. [Commit](https://github.com/open-webui/open-webui/commit/a8fe979af68e47e4e4bb3eb76e48d93d60cd2a45)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F4C2 Move menu no longer displays when folders are empty. [#18484](https://github.com/open-webui/open-webui/pull/18484)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F4CD User menu, download submenu, and move submenu are now repositioned
      to prevent overlap with the Chat Controls sidebar when it is open. [Commit](https://github.com/open-webui/open-webui/commit/414ab51cb6df1ab0d6c85ac6c1f2c5c9a5f8e2aa)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F3AF Artifacts button no longer appears in the chat menu when there
      are no artifacts to display. [Commit](https://github.com/open-webui/open-webui/commit/ed6449d35f84f68dc75ee5c6b3f4748a3fda0096)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F3A8 Layout shift near system instructions is prevented by properly
      rendering the chat component when system prompts are empty. [#18594](https://github.com/open-webui/open-webui/pull/18594)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F4D0 Modal layout shift caused by scrollbar appearance is prevented
      by adding a stable scrollbar gutter. [#18591](https://github.com/open-webui/open-webui/pull/18591)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: ✨ Spacing between icon and label in the user menu dropdown items is now
      consistent. [#18595](https://github.com/open-webui/open-webui/pull/18595)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 10-interface-experience-changes-in-v0-6-35
  source_release: open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234
  source_type: github_releases
  theme: interface-experience
  title: 10 Interface Experience changes in v0.6.35
  type: change
related_changes:
- '[[Changes/v0/2025-10-30-we-redesigned-the-chat-sidebar-with-better-organization-faster-navigation-and-a|Redesigned
  Chat Sidebar]]'
- '[[Changes/Cline/2025-10-31-2-interface-experience-changes-in-v3-35-0|2 Interface
  Experience changes in v3.35.0]]'
- '[[Changes/Gemini CLI/2025-11-04-change-debug-drawer-keybinding-to-f12-by-scidomino-in-https-github-com-google-ge|Change
  debug drawer keybinding to F12]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234|open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234]]'
source_type: github_releases
theme: interface-experience
title: 10 Interface Experience changes in v0.6.35
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Interface Experience changes in v0.6.35

**Open WebUI** · 2025-11-06 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.35) · from [[Releases/Open WebUI/open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234|v0.6.35]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ⌨️ Keyboard shortcut hints are now displayed on sidebar buttons with a refactored shortcuts modal that accurately reflects all available hotkeys across different keyboard layouts. [#18473](https://github.com/open-webui/open-webui/pull/18473)

> 📌 Sidebar models section is now collapsible, allowing users to expand and collapse the pinned models list for better sidebar organization. [Commit](https://github.com/open-webui/open-webui/commit/82c08a3b5d189f81c96b6548cc872198771015b0)

> 📈 Mermaid diagram rendering errors no longer cause UI unavailability or display error messages below the input box. [#18493](https://github.com/open-webui/open-webui/pull/18493), [#18340](https://github.com/open-webui/open-webui/issues/18340)

> 🔎 Folder tag search in the sidebar now correctly handles folder names with multiple spaces by replacing all spaces with underscores. [Commit](https://github.com/open-webui/open-webui/commit/a8fe979af68e47e4e4bb3eb76e48d93d60cd2a45)

> 📂 Move menu no longer displays when folders are empty. [#18484](https://github.com/open-webui/open-webui/pull/18484)

> 📍 User menu, download submenu, and move submenu are now repositioned to prevent overlap with the Chat Controls sidebar when it is open. [Commit](https://github.com/open-webui/open-webui/commit/414ab51cb6df1ab0d6c85ac6c1f2c5c9a5f8e2aa)

> 🎯 Artifacts button no longer appears in the chat menu when there are no artifacts to display. [Commit](https://github.com/open-webui/open-webui/commit/ed6449d35f84f68dc75ee5c6b3f4748a3fda0096)

> 🎨 Layout shift near system instructions is prevented by properly rendering the chat component when system prompts are empty. [#18594](https://github.com/open-webui/open-webui/pull/18594)

> 📐 Modal layout shift caused by scrollbar appearance is prevented by adding a stable scrollbar gutter. [#18591](https://github.com/open-webui/open-webui/pull/18591)

> ✨ Spacing between icon and label in the user menu dropdown items is now consistent. [#18595](https://github.com/open-webui/open-webui/pull/18595)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-11-06-chat-controls-button-is-now-properly-hidden-on-mobile-for-users-without-admin-or|📱 Chat controls button is now properly hidden on mobile for users without admin…]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-11-06-3-voice-and-audio-changes-in-v0-6-35|3 Voice and Audio changes in v0.6.35]] · Voice and Audio
- [[Changes/Open WebUI/2025-11-06-10-model-support-changes-in-v0-6-35|10 Model Support changes in v0.6.35]] · Model Support
- [[Changes/Open WebUI/2025-11-06-2-multimodal-input-changes-in-v0-6-35|2 Multimodal Input changes in v0.6.35]] · Multimodal Input
- [[Changes/Open WebUI/2025-11-06-4-safety-and-privacy-changes-in-v0-6-35|4 Safety and Privacy changes in v0.6.35]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-06-3-developer-workflow-changes-in-v0-6-35|3 Developer Workflow changes in v0.6.35]] · Developer Workflow
- [[Changes/Open WebUI/2025-11-06-3-editor-experience-changes-in-v0-6-35|3 Editor Experience changes in v0.6.35]] · Editor Experience
- [[Changes/Open WebUI/2025-11-06-4-search-and-browsing-changes-in-v0-6-35|4 Search and Browsing changes in v0.6.35]] · Search and Browsing
- [[Changes/Open WebUI/2025-11-06-3-reliability-and-performance-changes-in-v0-6-35|3 Reliability and Performance changes in v0.6.35]] · Reliability and Performance
- [[Changes/Open WebUI/2025-11-06-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-11-06-3-context-window-changes-in-v0-6-35|3 Context Window changes in v0.6.35]] · Context Window
- [[Changes/Open WebUI/2025-11-06-edit-button-is-now-available-in-the-three-dot-menu-of-models-in-the-workspace-se|✏️ Edit button is now available in the three-dot menu of models in the workspace…]] · Model Support
- [[Changes/Open WebUI/2025-11-06-screen-reader-support-was-enhanced-by-wrapping-messages-in-semantic-elements-wit|♿ Screen reader support was enhanced by wrapping messages in semantic elements…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-11-06-external-document-loaders-can-now-optionally-forward-user-information-headers-wh|📄 External document loaders can now optionally forward user information headers…]] · Pricing Model
- [[Changes/Open WebUI/2025-11-06-3-files-and-data-changes-in-v0-6-35|3 Files and Data changes in v0.6.35]] · Files and Data
- [[Changes/Open WebUI/2025-11-06-2-apps-and-integrations-changes-in-v0-6-35|2 Apps and Integrations changes in v0.6.35]] · Apps and Integrations
- [[Changes/Open WebUI/2025-11-06-5-account-and-access-changes-in-v0-6-35|5 Account and Access changes in v0.6.35]] · Account and Access
- [[Changes/Open WebUI/2025-11-06-22-other-changes-in-v0-6-35|22 other changes in v0.6.35]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2025-11-04 · Gemini CLI · [[Changes/Gemini CLI/2025-11-04-change-debug-drawer-keybinding-to-f12-by-scidomino-in-https-github-com-google-ge|Change debug drawer keybinding to F12]]
- Later: 2025-11-06 · Raycast · [[Changes/Raycast/2025-11-06-general-improved-main-window-background-rendering-it-no-longer-displays-stale-ui|General : Improved main window background rendering]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-11-06-4e636b&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-11-06-10-interface-experience-changes-in-v0-6-35.md%0ACard%20ID%3A%20open-webui-2025-11-06-4e636b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.35%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->