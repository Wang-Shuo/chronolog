---
card_id: open-webui-2026-10-29-112ce8
date: '2026-10-29'
description: "Open WebUI · 2026-10-29 · Automation and Scheduling: 2 changes in v0.12.5
  — \U0001F6A8 **Automation failure notifications.** Automation run failed is now
  an event users…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add
    data clean schedule]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1031
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 934ef740c201d8c4150ef4ad57a546e240e481ea41bda1a75444fb70613f5369
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-29-112ce8
  comparison: ''
  date: '2026-10-29'
  description: 'Open WebUI — v0.12.5: 2 Automation and Scheduling changes'
  evidence:
  - quote: "\U0001F6A8 **Automation failure notifications.** Automation run failed
      is now an event users can pick for their notification targets under Settings
      > Notifications, so the owner hears about every failed run with the automation's
      name and error. [#33331](https://github.com/open-webui/open-webui/pull/33331),
      [#33228](https://github.com/open-webui/open-webui/issues/33228), [Commit](https://github.com/open-webui/open-webui/commit/e49ff5df64a1523b80fce8ef03637953265c4355)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F4EE **Automation failure webhooks.** Admin event webhooks set to
      System events only no longer receive automation run failures, which now go to
      webhooks set to specific users or groups that include the automation's owner.
      [#33331](https://github.com/open-webui/open-webui/pull/33331), [Commit](https://github.com/open-webui/open-webui/commit/e49ff5df64a1523b80fce8ef03637953265c4355)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-automation-and-scheduling-changes-in-v0-12-5
  source_release: open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e
  source_type: github_releases
  theme: automation-scheduling
  title: 2 Automation and Scheduling changes in v0.12.5
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-10-27-refactor-core-cli-emit-tool-call-groups-from-the-scheduler-and-drop-the-ui-looka|refactor(core,cli):
  emit tool call groups from the scheduler and drop the UI lookahead]]'
- '[[Changes/OpenClaw/2026-10-27-4-automation-and-scheduling-changes-in-v2026-10-8|4
  Automation and Scheduling changes in v2026.10.8]]'
- '[[Changes/OpenHands/2026-10-27-6-automation-and-scheduling-changes-in-v1-34-0|6
  Automation and Scheduling changes in v1.34.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e|open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e]]'
source_type: github_releases
theme: automation-scheduling
title: 2 Automation and Scheduling changes in v0.12.5
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Automation and Scheduling changes in v0.12.5

**Open WebUI** · 2026-10-29 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.5) · from [[Releases/Open WebUI/open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e|v0.12.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🚨 **Automation failure notifications.** Automation run failed is now an event users can pick for their notification targets under Settings > Notifications, so the owner hears about every failed run with the automation's name and error. [#33331](https://github.com/open-webui/open-webui/pull/33331), [#33228](https://github.com/open-webui/open-webui/issues/33228), [Commit](https://github.com/open-webui/open-webui/commit/e49ff5df64a1523b80fce8ef03637953265c4355)

> 📮 **Automation failure webhooks.** Admin event webhooks set to System events only no longer receive automation run failures, which now go to webhooks set to specific users or groups that include the automation's owner. [#33331](https://github.com/open-webui/open-webui/pull/33331), [Commit](https://github.com/open-webui/open-webui/commit/e49ff5df64a1523b80fce8ef03637953265c4355)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-29-improved-ui-accessibility-screen-reader-and-keyboard-users-can-now-move-through|♿ Improved UI accessibility. Screen reader and keyboard users can now move…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-10-29-provider-details-for-models-administrators-editing-a-model-now-see-a-provider-de|📇 Provider details for models. Administrators editing a model now see a Provider…]] · Context Window
- [[Changes/Open WebUI/2026-10-29-2-memory-and-personalization-changes-in-v0-12-5|2 Memory and Personalization changes in v0.12.5]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-29-photos-for-sub-agents-models-can-now-hand-a-photo-attached-in-the-chat-to-a-sub|🤖 Photos for sub-agents. Models can now hand a photo attached in the chat…]] · Agent Mode
- [[Changes/Open WebUI/2026-10-29-knowledge-base-api-responses-trimmed-adding-updating-or-removing-knowledge-base|📃 Knowledge base API responses trimmed. Adding, updating or removing knowledge…]] · Collaboration
- [[Changes/Open WebUI/2026-10-29-2-reliability-and-performance-changes-in-v0-12-5|2 Reliability and Performance changes in v0.12.5]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-29-35-developer-workflow-changes-in-v0-12-5|35 Developer Workflow changes in v0.12.5]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-29-7-model-support-changes-in-v0-12-5|7 Model Support changes in v0.12.5]] · Model Support
- [[Changes/Open WebUI/2026-10-29-admins-manage-user-api-keys-administrators-can-now-rotate-or-delete-a-user-s-api|🗝️ Admins manage user API keys. Administrators can now rotate or delete a user's…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-29-2-image-generation-changes-in-v0-12-5|2 Image Generation changes in v0.12.5]] · Image Generation
- [[Changes/Open WebUI/2026-10-29-2-files-and-data-changes-in-v0-12-5|2 Files and Data changes in v0.12.5]] · Files and Data
- [[Changes/Open WebUI/2026-10-29-2-apps-and-integrations-changes-in-v0-12-5|2 Apps and Integrations changes in v0.12.5]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-29-security-advisory-this-release-contains-security-fixes-we-strongly-recommend-upd|🛡️ Security Advisory: This release contains security fixes]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-29-2-interface-experience-changes-in-v0-12-5|2 Interface Experience changes in v0.12.5]] · Interface Experience
- [[Changes/Open WebUI/2026-10-29-read-aloud-with-kokoro-js-read-aloud-now-speaks-with-the-chosen-kokoro-voice-whe|🔊 Read Aloud with Kokoro.js. Read Aloud now speaks with the chosen Kokoro voice…]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-29-6-editor-experience-changes-in-v0-12-5|6 Editor Experience changes in v0.12.5]] · Editor Experience
- [[Changes/Open WebUI/2026-10-29-translation-updates-translations-for-portuguese-brazil-catalan-italian-azerbaija|🌐 Translation updates. Translations for Portuguese (Brazil), Catalan, Italian…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-10-27 · OpenHands · [[Changes/OpenHands/2026-10-27-6-automation-and-scheduling-changes-in-v1-34-0|6 Automation and Scheduling changes in v1.34.0]]
- Later: 2026-10-29 · OpenCode · [[Changes/OpenCode/2026-10-29-sdk-add-client-experimental-schedule-create-list-get-pause-resume-delete-for-man|SDK Add…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-01-02 · Dify · [[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add data clean schedule]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-29-112ce8&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-29-2-automation-and-scheduling-changes-in-v0-12-5.md%0ACard%20ID%3A%20open-webui-2026-10-29-112ce8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->