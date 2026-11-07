---
card_id: open-webui-2026-03-08-6a48d5
date: '2026-03-08'
description: "Open WebUI · 2026-03-08 · Interface Experience: 5 changes in v0.8.9
  — \U0001F4BB **Code syntax highlighting and XLSX improvements in Open Terminal.**
  Code files now…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1154
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d5c91238a56538cf56243cc84085c72d268bdbaf3f15f7e54bb979c3921d1ccf
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-08-6a48d5
  comparison: ''
  date: '2026-03-08'
  description: 'Open WebUI — v0.8.9: 5 Interface Experience changes'
  evidence:
  - quote: "\U0001F4BB **Code syntax highlighting and XLSX improvements in Open Terminal.**
      Code files now display with syntax highlighting in the Open Terminal file navigator,
      and XLSX spreadsheets now show column headers and row numbers for easier navigation.
      [Commit](https://github.com/open-webui/open-webui/commit/f962bae98306ea9264967b78b803397f4821f9b0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F514 **Banner loading on navigation.** Admin-configured banners
      now load when navigating to the homepage, not just on page refresh, ensuring
      users see new banners immediately. [#22340](https://github.com/open-webui/open-webui/pull/22340),
      [#22180](https://github.com/open-webui/open-webui/issues/22180)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F500 **Artifact navigation.** Artifact navigation via arrow buttons
      now works correctly; the selected artifact is no longer reset when content updates.
      [#22239](https://github.com/open-webui/open-webui/pull/22239)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F3A8 **Button spinner alignment.** Button spinners across multiple
      modals now align correctly and stay on the same line as the button text, fixing
      layout issues when loading states are displayed. [#22227](https://github.com/open-webui/open-webui/pull/22227)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F3F7️ **Banner type dropdown fix.** Fixed a bug where selecting
      a banner type required two clicks to register, as the first selection was being
      swallowed due to DOM structure changes. The dropdown now works correctly on
      the first click. [#22378](https://github.com/open-webui/open-webui/pull/22378)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-interface-experience-changes-in-v0-8-9
  source_release: open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb
  source_type: github_releases
  theme: interface-experience
  title: 5 Interface Experience changes in v0.8.9
  type: change
related_changes:
- '[[Changes/Replit/2026-03-06-ai-chat-message-truncation|AI Chat message truncation]]'
- '[[Changes/OpenCode/2026-03-07-2-interface-experience-changes-in-v1-2-21|2 Interface
  Experience changes in v1.2.21]]'
- '[[Changes/Codex CLI/2026-03-08-added-a-new-model-selection-surface-update-so-the-latest-model-catalog-changes-a|Added
  a new model-selection surface update so the latest model catalog changes…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb|open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb]]'
source_type: github_releases
theme: interface-experience
title: 5 Interface Experience changes in v0.8.9
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Interface Experience changes in v0.8.9

**Open WebUI** · 2026-03-08 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.9) · from [[Releases/Open WebUI/open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb|v0.8.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 💻 **Code syntax highlighting and XLSX improvements in Open Terminal.** Code files now display with syntax highlighting in the Open Terminal file navigator, and XLSX spreadsheets now show column headers and row numbers for easier navigation. [Commit](https://github.com/open-webui/open-webui/commit/f962bae98306ea9264967b78b803397f4821f9b0)

> 🔔 **Banner loading on navigation.** Admin-configured banners now load when navigating to the homepage, not just on page refresh, ensuring users see new banners immediately. [#22340](https://github.com/open-webui/open-webui/pull/22340), [#22180](https://github.com/open-webui/open-webui/issues/22180)

> 🔀 **Artifact navigation.** Artifact navigation via arrow buttons now works correctly; the selected artifact is no longer reset when content updates. [#22239](https://github.com/open-webui/open-webui/pull/22239)

> 🎨 **Button spinner alignment.** Button spinners across multiple modals now align correctly and stay on the same line as the button text, fixing layout issues when loading states are displayed. [#22227](https://github.com/open-webui/open-webui/pull/22227)

> 🏷️ **Banner type dropdown fix.** Fixed a bug where selecting a banner type required two clicks to register, as the first selection was being swallowed due to DOM structure changes. The dropdown now works correctly on the first click. [#22378](https://github.com/open-webui/open-webui/pull/22378)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-08-image-generation-in-temporary-chats-generated-images-now-display-correctly-in-te|🖌️ Image generation in temporary chats. Generated images now display correctly…]] · Image Generation
- [[Changes/Open WebUI/2026-03-08-2-context-window-changes-in-v0-8-9|2 Context Window changes in v0.8.9]] · Context Window
- [[Changes/Open WebUI/2026-03-08-microsoft-oauth-refresh-token-fix-fixed-a-bug-where-microsoft-oauth-refresh-toke|🔐 Microsoft OAuth refresh token fix. Fixed a bug where Microsoft OAuth refresh…]] · Account and Access
- [[Changes/Open WebUI/2026-03-08-17-developer-workflow-changes-in-v0-8-9|17 Developer Workflow changes in v0.8.9]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-08-2-voice-and-audio-changes-in-v0-8-9|2 Voice and Audio changes in v0.8.9]] · Voice and Audio
- [[Changes/Open WebUI/2026-03-08-android-photo-capture-fixed-an-issue-where-the-first-photo-taken-in-chat-appeare|📷 Android photo capture. Fixed an issue where the first photo taken in chat…]] · Files and Data
- [[Changes/Open WebUI/2026-03-08-2-search-and-browsing-changes-in-v0-8-9|2 Search and Browsing changes in v0.8.9]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-08-open-terminal-html-editing-users-can-now-edit-html-source-files-in-open-terminal|✏️ Open Terminal HTML editing. Users can now edit HTML source files in Open…]] · Editor Experience
- [[Changes/Open WebUI/2026-03-08-system-metrics-via-opentelemetry-administrators-can-now-monitor-python-runtime-a|📡 System metrics via OpenTelemetry. Administrators can now monitor Python…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-03-08-artifacts-reactive-loop-fix-fixed-an-infinite-reactive-loop-in-chat-when-artifac|♾️ Artifacts reactive loop fix. Fixed an infinite reactive loop in chat…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-03-08-13-reliability-and-performance-changes-in-v0-8-9|13 Reliability and Performance changes in v0.8.9]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-08-9-model-support-changes-in-v0-8-9|9 Model Support changes in v0.8.9]] · Model Support
- [[Changes/Open WebUI/2026-03-08-open-terminal-permission-fix-open-terminal-is-now-visible-without-requiring-allo|🖥️ Open Terminal permission fix. Open Terminal is now visible without requiring…]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-08-14-other-changes-in-v0-8-9|14 other changes in v0.8.9]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-03-08 · Codex CLI · [[Changes/Codex CLI/2026-03-08-added-a-new-model-selection-surface-update-so-the-latest-model-catalog-changes-a|Added a new model-selection surface update so the latest model catalog changes…]]
- Later: 2026-03-08 · OpenCode · [[Changes/OpenCode/2026-03-08-2-interface-experience-changes-in-v1-2-22|2 Interface Experience changes in v1.2.22]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-08-6a48d5&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-08-5-interface-experience-changes-in-v0-8-9.md%0ACard%20ID%3A%20open-webui-2026-03-08-6a48d5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->