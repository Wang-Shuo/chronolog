---
card_id: open-webui-2026-10-29-9144e9
date: '2026-10-29'
description: "Open WebUI · 2026-10-29 · Files and Data: 2 changes in v0.12.5 — \U0001F4C9
  **Negative relevance threshold.** The Relevance Threshold in Admin Settings > Documents
  now…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2
    Files and Data changes in 0.2.2]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1253
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 019b97dc48e095e04a0b8d1118f91fcf0074fa9338630da10b35725f82c05108
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-29-9144e9
  comparison: ''
  date: '2026-10-29'
  description: 'Open WebUI — v0.12.5: 2 Files and Data changes'
  evidence:
  - quote: "\U0001F4C9 **Negative relevance threshold.** The Relevance Threshold in
      Admin Settings > Documents now takes negative values for rerankers that return
      raw scores below zero, where the field refused them and a negative \"RAG_RELEVANCE_THRESHOLD\"
      kept the page from saving while hybrid search was on. [#33330](https://github.com/open-webui/open-webui/pull/33330),
      [#29888](https://github.com/open-webui/open-webui/issues/29888), [Commit](https://github.com/open-webui/open-webui/commit/34ef99dbfb0815fbca10d3faea2da7c50f29e19f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F522 **Empty embedding batch size.** Clearing the Embedding Batch
      Size in Admin Settings > Documents now saves the default of 1, where files uploaded
      afterwards failed to process. [#33288](https://github.com/open-webui/open-webui/pull/33288),
      [#33287](https://github.com/open-webui/open-webui/issues/33287), [Commit](https://github.com/open-webui/open-webui/commit/893dbc9bd8930cdb3be82f38c795366f3b8ca9b0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-files-and-data-changes-in-v0-12-5
  source_release: open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e
  source_type: github_releases
  theme: file-data
  title: 2 Files and Data changes in v0.12.5
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-10-27-built-in-browser-and-attachments-of-any-file-type|Built-in
  browser and attachments of any file type]]'
- '[[Changes/Google Antigravity/2026-10-27-pdf-files-now-open-in-a-built-in-pdf-viewer-both-in-the-file-viewer-and-when-an|PDF
  files now open in a built-in PDF viewer, both in the file viewer and…]]'
- '[[Changes/OpenHands/2026-10-27-feat-canvas-per-conversation-docker-runtime-and-settings-runtime-page-by-vascosc|feat(canvas):
  per-conversation Docker runtime and Settings → Runtime page]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e|open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e]]'
source_type: github_releases
theme: file-data
title: 2 Files and Data changes in v0.12.5
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Files and Data changes in v0.12.5

**Open WebUI** · 2026-10-29 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.5) · from [[Releases/Open WebUI/open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e|v0.12.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📉 **Negative relevance threshold.** The Relevance Threshold in Admin Settings > Documents now takes negative values for rerankers that return raw scores below zero, where the field refused them and a negative "RAG_RELEVANCE_THRESHOLD" kept the page from saving while hybrid search was on. [#33330](https://github.com/open-webui/open-webui/pull/33330), [#29888](https://github.com/open-webui/open-webui/issues/29888), [Commit](https://github.com/open-webui/open-webui/commit/34ef99dbfb0815fbca10d3faea2da7c50f29e19f)

> 🔢 **Empty embedding batch size.** Clearing the Embedding Batch Size in Admin Settings > Documents now saves the default of 1, where files uploaded afterwards failed to process. [#33288](https://github.com/open-webui/open-webui/pull/33288), [#33287](https://github.com/open-webui/open-webui/issues/33287), [Commit](https://github.com/open-webui/open-webui/commit/893dbc9bd8930cdb3be82f38c795366f3b8ca9b0)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-29-improved-ui-accessibility-screen-reader-and-keyboard-users-can-now-move-through|♿ Improved UI accessibility. Screen reader and keyboard users can now move…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-10-29-provider-details-for-models-administrators-editing-a-model-now-see-a-provider-de|📇 Provider details for models. Administrators editing a model now see a Provider…]] · Context Window
- [[Changes/Open WebUI/2026-10-29-2-memory-and-personalization-changes-in-v0-12-5|2 Memory and Personalization changes in v0.12.5]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-29-2-automation-and-scheduling-changes-in-v0-12-5|2 Automation and Scheduling changes in v0.12.5]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-29-photos-for-sub-agents-models-can-now-hand-a-photo-attached-in-the-chat-to-a-sub|🤖 Photos for sub-agents. Models can now hand a photo attached in the chat…]] · Agent Mode
- [[Changes/Open WebUI/2026-10-29-knowledge-base-api-responses-trimmed-adding-updating-or-removing-knowledge-base|📃 Knowledge base API responses trimmed. Adding, updating or removing knowledge…]] · Collaboration
- [[Changes/Open WebUI/2026-10-29-2-reliability-and-performance-changes-in-v0-12-5|2 Reliability and Performance changes in v0.12.5]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-29-35-developer-workflow-changes-in-v0-12-5|35 Developer Workflow changes in v0.12.5]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-29-7-model-support-changes-in-v0-12-5|7 Model Support changes in v0.12.5]] · Model Support
- [[Changes/Open WebUI/2026-10-29-admins-manage-user-api-keys-administrators-can-now-rotate-or-delete-a-user-s-api|🗝️ Admins manage user API keys. Administrators can now rotate or delete a user's…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-29-2-image-generation-changes-in-v0-12-5|2 Image Generation changes in v0.12.5]] · Image Generation
- [[Changes/Open WebUI/2026-10-29-2-apps-and-integrations-changes-in-v0-12-5|2 Apps and Integrations changes in v0.12.5]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-29-security-advisory-this-release-contains-security-fixes-we-strongly-recommend-upd|🛡️ Security Advisory: This release contains security fixes]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-29-2-interface-experience-changes-in-v0-12-5|2 Interface Experience changes in v0.12.5]] · Interface Experience
- [[Changes/Open WebUI/2026-10-29-read-aloud-with-kokoro-js-read-aloud-now-speaks-with-the-chosen-kokoro-voice-whe|🔊 Read Aloud with Kokoro.js. Read Aloud now speaks with the chosen Kokoro voice…]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-29-6-editor-experience-changes-in-v0-12-5|6 Editor Experience changes in v0.12.5]] · Editor Experience
- [[Changes/Open WebUI/2026-10-29-translation-updates-translations-for-portuguese-brazil-catalan-italian-azerbaija|🌐 Translation updates. Translations for Portuguese (Brazil), Catalan, Italian…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-10-27 · OpenHands · [[Changes/OpenHands/2026-10-27-feat-canvas-per-conversation-docker-runtime-and-settings-runtime-page-by-vascosc|feat(canvas): per-conversation Docker runtime and Settings → Runtime page]]
- Later: 2026-10-29 · OpenClaw · [[Changes/OpenClaw/2026-10-29-canvas-a2ui-and-discord-activity-now-avoid-unnecessary-processing-by-rejecting-o|Canvas/A2UI and Discord Activity now avoid unnecessary processing by rejecting…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-25 · Dify · [[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2 Files and Data changes in 0.2.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-29-9144e9&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-29-2-files-and-data-changes-in-v0-12-5.md%0ACard%20ID%3A%20open-webui-2026-10-29-9144e9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->