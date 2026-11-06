---
card_id: open-webui-2026-10-10-668723
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Mobile and Desktop: 3 changes in v0.12.0 —
  \U0001FA9F **Terminal instructions on Windows hosts.** The AGENTS.md file in the
  home folder of a…"
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1306
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6ea074c94a8cdc988cfb68a8dc12b81d1b06e0e751172032c9a0303442788301
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-668723
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 3 Mobile and Desktop changes'
  evidence:
  - quote: "\U0001FA9F **Terminal instructions on Windows hosts.** The AGENTS.md file
      in the home folder of a terminal running on Windows now reaches the model, where
      it was skipped because the Windows home path was not recognized. [#31342](https://github.com/open-webui/open-webui/pull/31342),
      [#31340](https://github.com/open-webui/open-webui/issues/31340)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F233 **Input methods with a follow-up suggestion.** Typing with
      a Chinese, Japanese or Korean input method into the empty chat input while a
      suggested follow-up is shown as grey text now works, where iOS lost focus after
      the first character and Chromium left the first letter behind. [#31393](https://github.com/open-webui/open-webui/pull/31393),
      [#31372](https://github.com/open-webui/open-webui/issues/31372)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4F8 **iPhone photos with vision models.** HEIC and HEIF photos
      from iPhones are now converted and uploaded as JPEG in chats, channels and notes
      whatever type the browser reports, where Firefox and some other browsers uploaded
      them as HEIC and vision models failed with an error. [#31649](https://github.com/open-webui/open-webui/pull/31649),
      [#28411](https://github.com/open-webui/open-webui/issues/28411)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-mobile-and-desktop-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: mobile-desktop
  title: 3 Mobile and Desktop changes in v0.12.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-08-changed-the-claude-apps-gateway-to-start-with-a-warning-and-serve-a-desktop-poli|Changed
  the Claude apps gateway to start with a warning and serve a desktop policy…]]'
- '[[Changes/Codex CLI/2026-10-08-50384-allow-opting-into-16-kib-arm64-code-pages-for-macos-signing-chess-oai|♯50384
  Allow opting into 16 KiB ARM64 code pages for macOS signing @chess-oai]]'
- '[[Changes/Replit/2026-10-09-replit-desktop-windows-preview-with-microsoft-and-nvidia|Replit
  Desktop Windows preview with Microsoft and NVIDIA]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: mobile-desktop
title: 3 Mobile and Desktop changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Mobile and Desktop changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🪟 **Terminal instructions on Windows hosts.** The AGENTS.md file in the home folder of a terminal running on Windows now reaches the model, where it was skipped because the Windows home path was not recognized. [#31342](https://github.com/open-webui/open-webui/pull/31342), [#31340](https://github.com/open-webui/open-webui/issues/31340)

> 🈳 **Input methods with a follow-up suggestion.** Typing with a Chinese, Japanese or Korean input method into the empty chat input while a suggested follow-up is shown as grey text now works, where iOS lost focus after the first character and Chromium left the first letter behind. [#31393](https://github.com/open-webui/open-webui/pull/31393), [#31372](https://github.com/open-webui/open-webui/issues/31372)

> 📸 **iPhone photos with vision models.** HEIC and HEIF photos from iPhones are now converted and uploaded as JPEG in chats, channels and notes whatever type the browser reports, where Firefox and some other browsers uploaded them as HEIC and vision models failed with an error. [#31649](https://github.com/open-webui/open-webui/pull/31649), [#28411](https://github.com/open-webui/open-webui/issues/28411)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-10-5-reliability-and-performance-changes-in-v0-12-0|5 Reliability and Performance changes in v0.12.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0|5 Enterprise and Administration changes in v0.12.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-10-27-developer-workflow-changes-in-v0-12-0|27 Developer Workflow changes in v0.12.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-10-5-image-generation-changes-in-v0-12-0|5 Image Generation changes in v0.12.0]] · Image Generation
- [[Changes/Open WebUI/2026-10-10-49-model-support-changes-in-v0-12-0|49 Model Support changes in v0.12.0]] · Model Support
- [[Changes/Open WebUI/2026-10-10-19-account-and-access-changes-in-v0-12-0|19 Account and Access changes in v0.12.0]] · Account and Access
- [[Changes/Open WebUI/2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0|10 Automation and Scheduling changes in v0.12.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-10-6-files-and-data-changes-in-v0-12-0|6 Files and Data changes in v0.12.0]] · Files and Data
- [[Changes/Open WebUI/2026-10-10-13-collaboration-changes-in-v0-12-0|13 Collaboration changes in v0.12.0]] · Collaboration
- [[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2 Memory and Personalization changes in v0.12.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-10-5-context-window-changes-in-v0-12-0|5 Context Window changes in v0.12.0]] · Context Window
- [[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface Experience changes in v0.12.0]] · Interface Experience
- [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]] · Agent Mode
- [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-10-09 · Replit · [[Changes/Replit/2026-10-09-replit-desktop-windows-preview-with-microsoft-and-nvidia|Replit Desktop Windows preview with Microsoft and NVIDIA]]
- Later: 2026-10-12 · Windsurf · [[Changes/Windsurf/2026-10-12-devin-desktop|Devin Desktop]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-668723&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-668723%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->