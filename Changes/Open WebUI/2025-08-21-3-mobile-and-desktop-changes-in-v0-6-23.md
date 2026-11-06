---
card_id: open-webui-2025-08-21-2bde85
date: '2025-08-21'
description: 'Open WebUI · 2025-08-21 · Mobile and Desktop: 3 changes in v0.6.23 —
  ✨ **Dynamic Loading of ''kokoro-js''**: Implemented dynamic loading for the ''kokoro-js''…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 891
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6b042c1851742aff7767dc06f13954ed4b97c16540f824f2ecd5eb2b41d5ee21
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-21-2bde85
  comparison: ''
  date: '2025-08-21'
  description: 'Open WebUI — v0.6.23: 3 Mobile and Desktop changes'
  evidence:
  - quote: '✨ **Dynamic Loading of ''kokoro-js''**: Implemented dynamic loading for
      the ''kokoro-js'' library, preventing failures and improving compatibility on
      older iOS browsers that may not support direct imports or certain modern JavaScript
      APIs like ''DecompressionStream''.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F4DD **Resolved Chinese Input 'Enter' Key Issue (macOS & iOS Safari)**:
      Fixed a bug where pressing the 'Enter' key during text composition with Input
      Method Editors (IMEs) on macOS and iOS Safari browsers would prematurely send
      the message. The system now robustly handles the composition state by addressing
      a 'compositionend' event bug specific to Safari, ensuring a smooth and expected
      typing experience for users of various languages, including Chinese and Korean."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F4F1 **Disabled Overscroll for iOS Frontend**: Fixed an issue where
      overscrolling was enabled on iOS devices, causing unexpected scrolling behavior
      over fixed or sticky elements within the PWA. Overscroll has now been disabled,
      providing a more native application-like experience for iOS users."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-mobile-and-desktop-changes-in-v0-6-23
  source_release: open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46
  source_type: github_releases
  theme: mobile-desktop
  title: 3 Mobile and Desktop changes in v0.6.23
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-08-14-2-mobile-and-desktop-changes-in-v0-1-21|2 Mobile
  and Desktop changes in v0.1.21]]'
- '[[Changes/Ollama/2025-08-15-reduced-size-of-installation-on-windows-and-linux|Reduced
  size of installation on Windows and Linux]]'
- '[[Changes/Codex CLI/2025-08-20-2-mobile-and-desktop-changes-in-rust-v0-23-0|2 Mobile
  and Desktop changes in rust-v0.23.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46]]'
source_type: github_releases
theme: mobile-desktop
title: 3 Mobile and Desktop changes in v0.6.23
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Mobile and Desktop changes in v0.6.23

**Open WebUI** · 2025-08-21 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.23) · from [[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|v0.6.23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ✨ **Dynamic Loading of 'kokoro-js'**: Implemented dynamic loading for the 'kokoro-js' library, preventing failures and improving compatibility on older iOS browsers that may not support direct imports or certain modern JavaScript APIs like 'DecompressionStream'.

> 📝 **Resolved Chinese Input 'Enter' Key Issue (macOS & iOS Safari)**: Fixed a bug where pressing the 'Enter' key during text composition with Input Method Editors (IMEs) on macOS and iOS Safari browsers would prematurely send the message. The system now robustly handles the composition state by addressing a 'compositionend' event bug specific to Safari, ensuring a smooth and expected typing experience for users of various languages, including Chinese and Korean.

> 📱 **Disabled Overscroll for iOS Frontend**: Fixed an issue where overscrolling was enabled on iOS devices, causing unexpected scrolling behavior over fixed or sticky elements within the PWA. Overscroll has now been disabled, providing a more native application-like experience for iOS users.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-21-8-interface-experience-changes-in-v0-6-23|8 Interface Experience changes in v0.6.23]] · Interface Experience
- [[Changes/Open WebUI/2025-08-21-restored-message-toolbar-icons-for-empty-messages-with-files-fixed-an-issue-wher|🐛 Restored Message Toolbar Icons for Empty Messages with Files]] · Editor Experience
- [[Changes/Open WebUI/2025-08-21-3-search-and-browsing-changes-in-v0-6-23|3 Search and Browsing changes in v0.6.23]] · Search and Browsing
- [[Changes/Open WebUI/2025-08-21-resolved-silently-dropped-streaming-response-chunks-fixed-an-issue-where-the-fin|💬 Resolved Silently Dropped Streaming Response Chunks]] · Files and Data
- [[Changes/Open WebUI/2025-08-21-6-reliability-and-performance-changes-in-v0-6-23|6 Reliability and Performance changes in v0.6.23]] · Reliability and Performance
- [[Changes/Open WebUI/2025-08-21-6-safety-and-privacy-changes-in-v0-6-23|6 Safety and Privacy changes in v0.6.23]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-21-2-voice-and-audio-changes-in-v0-6-23|2 Voice and Audio changes in v0.6.23]] · Voice and Audio
- [[Changes/Open WebUI/2025-08-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-08-21-2-accessibility-and-localization-changes-in-v0-6-23|2 Accessibility and Localization changes in v0.6.23]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-21-7-model-support-changes-in-v0-6-23|7 Model Support changes in v0.6.23]] · Model Support
- [[Changes/Open WebUI/2025-08-21-resolved-image-generation-api-size-parameter-issue-fixed-a-bug-where-the-api-v1|🖼️ Resolved Image Generation API Size Parameter Issue]] · Image Generation
- [[Changes/Open WebUI/2025-08-21-resolved-code-block-input-issue-with-shift-enter-fixed-a-bug-where-typing-three|📝 Resolved Code Block Input Issue with Shift+Enter]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-21-5-apps-and-integrations-changes-in-v0-6-23|5 Apps and Integrations changes in v0.6.23]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-21-3-account-and-access-changes-in-v0-6-23|3 Account and Access changes in v0.6.23]] · Account and Access
- [[Changes/Open WebUI/2025-08-21-23-other-changes-in-v0-6-23|23 other changes in v0.6.23]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2025-08-20 · Codex CLI · [[Changes/Codex CLI/2025-08-20-2-mobile-and-desktop-changes-in-rust-v0-23-0|2 Mobile and Desktop changes in rust-v0.23.0]]
- Later: 2025-08-22 · ChatGPT · [[Changes/ChatGPT/2025-08-22-this-feature-will-initially-only-be-available-on-the-chatgpt-website-and-windows|This feature will initially only be available on the ChatGPT website and Windows app]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-21-2bde85&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-21-3-mobile-and-desktop-changes-in-v0-6-23.md%0ACard%20ID%3A%20open-webui-2025-08-21-2bde85%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->