---
card_id: open-webui-2026-06-29-78bf79
date: '2026-06-29'
description: "Open WebUI · 2026-06-29 · Mobile and Desktop: 4 changes in v0.10.0 —
  \U0001F5BC️ **iPhone images work with OpenAI image editing.** Uploaded images are
  now normalized…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command
    + R to insert a speaker label (ctrl + R on Windows)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2787
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f58b1ae2e790c8b77be1e27751cd870930cd3c94a162483778beea9d39e677c3
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-78bf79
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 4 Mobile and Desktop changes'
  evidence:
  - quote: "\U0001F5BC️ **iPhone images work with OpenAI image editing.** Uploaded
      images are now normalized before being sent to OpenAI image editing, fixing
      edits that failed for certain iPhone photo formats, with a new admin toggle
      to control the behavior. [Commit](https://github.com/open-webui/open-webui/commit/39837e0a3afd17b7ff617d97dddf4c5d6446e42d),
      [Commit](https://github.com/open-webui/open-webui/commit/2d3035a1122123df471ac9d0a591a9465a8212e2),
      [#26252](https://github.com/open-webui/open-webui/pull/26252), [#26249](https://github.com/open-webui/open-webui/issues/26249)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⌨️ **Enter key shows correctly on iOS.** The Enter key symbol in the keyboard
      shortcuts list no longer renders as an emoji on iOS. [#26173](https://github.com/open-webui/open-webui/pull/26173)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F501 **Recovers from a stuck streaming response.** If the signal
      that a response finished is missed — for example after a mobile app is backgrounded
      mid-stream — Open WebUI now recovers the chat instead of leaving it stuck in
      a streaming state. [Commit](https://github.com/open-webui/open-webui/commit/aa851d93c63e7da6e94292d0b7586674339d47e5),
      [Commit](https://github.com/open-webui/open-webui/commit/edf2c6c8f76e7f6a5917e991f371a604adc34c5f),
      [Commit](https://github.com/open-webui/open-webui/commit/2856def6c05b2fb8c55b4e7170f05db0c4f956f1),
      [#26320](https://github.com/open-webui/open-webui/pull/26320), [#26315](https://github.com/open-webui/open-webui/issues/26315)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4F1 **Better banner layout on mobile.** Notification banners now
      lay out correctly on small screens. [Commit](https://github.com/open-webui/open-webui/commit/4ed45ce84394c435405f93d03f07dabd797cdec3),
      [#24912](https://github.com/open-webui/open-webui/pull/24912)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-mobile-and-desktop-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: mobile-desktop
  title: 4 Mobile and Desktop changes in v0.10.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-06-29-android-sdk|Android SDK]]'
- '[[Changes/Kimi Code/2026-06-29-in-the-bundled-web-ui-new-and-clear-are-now-aliases-that-open-the-session-onboar|In
  the bundled web UI, /new and /clear are now aliases that open the session…]]'
- '[[Changes/Lovable/2026-06-29-fewer-taps-to-attach-images-on-mobile|Fewer taps to
  attach images on mobile]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: mobile-desktop
title: 4 Mobile and Desktop changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Mobile and Desktop changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🖼️ **iPhone images work with OpenAI image editing.** Uploaded images are now normalized before being sent to OpenAI image editing, fixing edits that failed for certain iPhone photo formats, with a new admin toggle to control the behavior. [Commit](https://github.com/open-webui/open-webui/commit/39837e0a3afd17b7ff617d97dddf4c5d6446e42d), [Commit](https://github.com/open-webui/open-webui/commit/2d3035a1122123df471ac9d0a591a9465a8212e2), [#26252](https://github.com/open-webui/open-webui/pull/26252), [#26249](https://github.com/open-webui/open-webui/issues/26249)

> ⌨️ **Enter key shows correctly on iOS.** The Enter key symbol in the keyboard shortcuts list no longer renders as an emoji on iOS. [#26173](https://github.com/open-webui/open-webui/pull/26173)

> 🔁 **Recovers from a stuck streaming response.** If the signal that a response finished is missed — for example after a mobile app is backgrounded mid-stream — Open WebUI now recovers the chat instead of leaving it stuck in a streaming state. [Commit](https://github.com/open-webui/open-webui/commit/aa851d93c63e7da6e94292d0b7586674339d47e5), [Commit](https://github.com/open-webui/open-webui/commit/edf2c6c8f76e7f6a5917e991f371a604adc34c5f), [Commit](https://github.com/open-webui/open-webui/commit/2856def6c05b2fb8c55b4e7170f05db0c4f956f1), [#26320](https://github.com/open-webui/open-webui/pull/26320), [#26315](https://github.com/open-webui/open-webui/issues/26315)

> 📱 **Better banner layout on mobile.** Notification banners now lay out correctly on small screens. [Commit](https://github.com/open-webui/open-webui/commit/4ed45ce84394c435405f93d03f07dabd797cdec3), [#24912](https://github.com/open-webui/open-webui/pull/24912)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-29-5-files-and-data-changes-in-v0-10-0|5 Files and Data changes in v0.10.0]] · Files and Data
- [[Changes/Open WebUI/2026-06-29-5-memory-and-personalization-changes-in-v0-10-0|5 Memory and Personalization changes in v0.10.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-29-3-voice-and-audio-changes-in-v0-10-0|3 Voice and Audio changes in v0.10.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-29-14-interface-experience-changes-in-v0-10-0|14 Interface Experience changes in v0.10.0]] · Interface Experience
- [[Changes/Open WebUI/2026-06-29-4-collaboration-changes-in-v0-10-0|4 Collaboration changes in v0.10.0]] · Collaboration
- [[Changes/Open WebUI/2026-06-29-client-user-agent-forwarded-to-model-backends-the-browser-s-user-agent-is-now-pa|🪪 Client User-Agent forwarded to model backends. The browser's User-Agent is now…]] · Agent Mode
- [[Changes/Open WebUI/2026-06-29-scim-sync-can-t-demote-an-admin-a-scim-provisioning-sync-that-marks-a-user-inact|🛟 SCIM sync can't demote an admin. A SCIM provisioning sync that marks a user…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-29-8-search-and-browsing-changes-in-v0-10-0|8 Search and Browsing changes in v0.10.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-29-25-model-support-changes-in-v0-10-0|25 Model Support changes in v0.10.0]] · Model Support
- [[Changes/Open WebUI/2026-06-29-6-reliability-and-performance-changes-in-v0-10-0|6 Reliability and Performance changes in v0.10.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-29-better-screen-reader-labels-on-toggles-integration-and-switch-toggles-now-expose|♿ Better screen-reader labels on toggles. Integration and switch toggles now…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-29-16-safety-and-privacy-changes-in-v0-10-0|16 Safety and Privacy changes in v0.10.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-29-2-pricing-model-changes-in-v0-10-0|2 Pricing Model changes in v0.10.0]] · Pricing Model
- [[Changes/Open WebUI/2026-06-29-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-29-9-account-and-access-changes-in-v0-10-0|9 Account and Access changes in v0.10.0]] · Account and Access
- [[Changes/Open WebUI/2026-06-29-usable-chat-input-on-mobile-with-many-tools-when-skills-tools-terminal-web-searc|📱 Usable chat input on mobile with many tools. When skills, tools, terminal, web…]] · Image Generation
- [[Changes/Open WebUI/2026-06-29-6-automation-and-scheduling-changes-in-v0-10-0|6 Automation and Scheduling changes in v0.10.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-29-3-context-window-changes-in-v0-10-0|3 Context Window changes in v0.10.0]] · Context Window
- [[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer Workflow changes in v0.10.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-29-10-editor-experience-changes-in-v0-10-0|10 Editor Experience changes in v0.10.0]] · Editor Experience
- [[Changes/Open WebUI/2026-06-29-29-other-changes-in-v0-10-0|29 other changes in v0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-06-29 · Lovable · [[Changes/Lovable/2026-06-29-fewer-taps-to-attach-images-on-mobile|Fewer taps to attach images on mobile]]
- Later: 2026-06-30 · Gemini · [[Changes/Gemini/2026-06-30-hand-off-the-heavy-lifting-to-gemini-spark-now-available-in-the-macos-app|Hand off the heavy lifting to Gemini Spark, now available in the macOS app]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command + R to insert a speaker label (ctrl + R on Windows)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-78bf79&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-4-mobile-and-desktop-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-78bf79%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->