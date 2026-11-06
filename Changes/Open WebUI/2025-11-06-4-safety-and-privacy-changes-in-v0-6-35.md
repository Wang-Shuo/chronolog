---
card_id: open-webui-2025-11-06-409c70
date: '2025-11-06'
description: "Open WebUI · 2025-11-06 · Safety and Privacy: 4 changes in v0.6.35 —
  \U0001F512 CORS origin validation was added to WebSocket connections as a defense-in-depth
  security…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 935
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e6f844db60a6a96e31cf30612ff2fa7d06f070a4060b11fd151cf511ac00b011
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-11-06-409c70
  comparison: ''
  date: '2025-11-06'
  description: 'Open WebUI — v0.6.35: 4 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F512 CORS origin validation was added to WebSocket connections as
      a defense-in-depth security measure against cross-site WebSocket hijacking attacks.
      [#18411](https://github.com/open-webui/open-webui/pull/18411), [#18410](https://github.com/open-webui/open-webui/issues/18410)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F40D Experimental initial preparations for Python 3.13 compatibility
      by updating dependencies with security enhancements and cryptographic improvements.
      [#18430](https://github.com/open-webui/open-webui/pull/18430), [#18424](https://github.com/open-webui/open-webui/pull/18424)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F512 Server-Sent Event (SSE) code injection vulnerability in Direct
      Connections is resolved by blocking event emission from untrusted external model
      servers; event emitters from direct connected model servers are no longer supported,
      preventing arbitrary JavaScript execution in user browsers. [Commit](https://github.com/open-webui/open-webui/commit/8af6a4cf21b756a66cd58378a01c60f74c39b7ca)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F6E1️ DOM XSS vulnerability in \"Insert Prompt as Rich Text\" is
      resolved by sanitizing HTML content with DOMPurify before rendering. [Commit](https://github.com/open-webui/open-webui/commit/eb9c4c0e358c274aea35f21c2856c0a20051e5f1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-safety-and-privacy-changes-in-v0-6-35
  source_release: open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in v0.6.35
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-11-04-3-safety-and-privacy-changes-in-rust-v0-54-0|3 Safety
  and Privacy changes in rust-v0.54.0]]'
- '[[Changes/Gemini CLI/2025-11-04-fix-infra-simplify-cancel-in-progress-and-add-permission-to-set-status-step-by-s|fix(infra)
  - Simplify cancel in progress and add permission to set status step]]'
- '[[Changes/ElevenLabs/2025-11-05-security|Security]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234|open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in v0.6.35
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in v0.6.35

**Open WebUI** · 2025-11-06 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.35) · from [[Releases/Open WebUI/open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234|v0.6.35]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔒 CORS origin validation was added to WebSocket connections as a defense-in-depth security measure against cross-site WebSocket hijacking attacks. [#18411](https://github.com/open-webui/open-webui/pull/18411), [#18410](https://github.com/open-webui/open-webui/issues/18410)

> 🐍 Experimental initial preparations for Python 3.13 compatibility by updating dependencies with security enhancements and cryptographic improvements. [#18430](https://github.com/open-webui/open-webui/pull/18430), [#18424](https://github.com/open-webui/open-webui/pull/18424)

> 🔒 Server-Sent Event (SSE) code injection vulnerability in Direct Connections is resolved by blocking event emission from untrusted external model servers; event emitters from direct connected model servers are no longer supported, preventing arbitrary JavaScript execution in user browsers. [Commit](https://github.com/open-webui/open-webui/commit/8af6a4cf21b756a66cd58378a01c60f74c39b7ca)

> 🛡️ DOM XSS vulnerability in "Insert Prompt as Rich Text" is resolved by sanitizing HTML content with DOMPurify before rendering. [Commit](https://github.com/open-webui/open-webui/commit/eb9c4c0e358c274aea35f21c2856c0a20051e5f1)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-11-06-chat-controls-button-is-now-properly-hidden-on-mobile-for-users-without-admin-or|📱 Chat controls button is now properly hidden on mobile for users without admin…]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-11-06-3-voice-and-audio-changes-in-v0-6-35|3 Voice and Audio changes in v0.6.35]] · Voice and Audio
- [[Changes/Open WebUI/2025-11-06-10-model-support-changes-in-v0-6-35|10 Model Support changes in v0.6.35]] · Model Support
- [[Changes/Open WebUI/2025-11-06-2-multimodal-input-changes-in-v0-6-35|2 Multimodal Input changes in v0.6.35]] · Multimodal Input
- [[Changes/Open WebUI/2025-11-06-3-developer-workflow-changes-in-v0-6-35|3 Developer Workflow changes in v0.6.35]] · Developer Workflow
- [[Changes/Open WebUI/2025-11-06-10-interface-experience-changes-in-v0-6-35|10 Interface Experience changes in v0.6.35]] · Interface Experience
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
## Nearby in Safety and Privacy

- Earlier: 2025-11-05 · ElevenLabs · [[Changes/ElevenLabs/2025-11-05-security|Security]]
- Later: 2025-11-07 · Codex CLI · [[Changes/Codex CLI/2025-11-07-2-safety-and-privacy-changes-in-rust-v0-56-0|2 Safety and Privacy changes in rust-v0.56.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-11-06-409c70&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-11-06-4-safety-and-privacy-changes-in-v0-6-35.md%0ACard%20ID%3A%20open-webui-2025-11-06-409c70%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.35%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->