---
card_id: open-webui-2026-10-29-0ef02b
date: '2026-10-29'
description: 'Open WebUI · 2026-10-29 · Memory and Personalization: 2 changes in v0.12.5
  — ⚡ **Faster knowledge base commands.** Knowledge base commands such as ls, cat
  and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1197
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 902ba6ac4f3d3018758e007106123a2efbac94b6aa64d83a9a2842713736bbde
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-29-0ef02b
  comparison: ''
  date: '2026-10-29'
  description: 'Open WebUI — v0.12.5: 2 Memory and Personalization changes'
  evidence:
  - quote: ⚡ **Faster knowledge base commands.** Knowledge base commands such as ls,
      cat and grep and the knowledge base sync check now list files without loading
      every file's full text, so on large knowledge bases each call is up to ten times
      faster and uses far less memory. [#33332](https://github.com/open-webui/open-webui/pull/33332),
      [#33322](https://github.com/open-webui/open-webui/issues/33322), [Commit](https://github.com/open-webui/open-webui/commit/517f824eb42615b203eb5c1f8779c268aa829960)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F4E6 **Batched document embedding.** Large documents are now embedded
      and saved in batches of 1000 chunks by default, set with \"RAG_EMBEDDING_BUFFER_SIZE\",
      so processing a very large file holds far less in memory at once. [Commit](https://github.com/open-webui/open-webui/commit/58536b65038dc7ff17d02dd78c60cc71ce110f92)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-memory-and-personalization-changes-in-v0-12-5
  source_release: open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e
  source_type: github_releases
  theme: memory
  title: 2 Memory and Personalization changes in v0.12.5
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-27-4-memory-and-personalization-changes-in-v2026-10-8|4
  Memory and Personalization changes in v2026.10.8]]'
- '[[Changes/OpenCode/2026-10-27-8-memory-and-personalization-changes-in-v2-2-0|8
  Memory and Personalization changes in v2.2.0]]'
- '[[Changes/Codex CLI/2026-10-29-2-memory-and-personalization-changes-in-rust-v0-166-0|2
  Memory and Personalization changes in rust-v0.166.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e|open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e]]'
source_type: github_releases
theme: memory
title: 2 Memory and Personalization changes in v0.12.5
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Memory and Personalization changes in v0.12.5

**Open WebUI** · 2026-10-29 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.5) · from [[Releases/Open WebUI/open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e|v0.12.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ⚡ **Faster knowledge base commands.** Knowledge base commands such as ls, cat and grep and the knowledge base sync check now list files without loading every file's full text, so on large knowledge bases each call is up to ten times faster and uses far less memory. [#33332](https://github.com/open-webui/open-webui/pull/33332), [#33322](https://github.com/open-webui/open-webui/issues/33322), [Commit](https://github.com/open-webui/open-webui/commit/517f824eb42615b203eb5c1f8779c268aa829960)

> 📦 **Batched document embedding.** Large documents are now embedded and saved in batches of 1000 chunks by default, set with "RAG_EMBEDDING_BUFFER_SIZE", so processing a very large file holds far less in memory at once. [Commit](https://github.com/open-webui/open-webui/commit/58536b65038dc7ff17d02dd78c60cc71ce110f92)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-29-improved-ui-accessibility-screen-reader-and-keyboard-users-can-now-move-through|♿ Improved UI accessibility. Screen reader and keyboard users can now move…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-10-29-provider-details-for-models-administrators-editing-a-model-now-see-a-provider-de|📇 Provider details for models. Administrators editing a model now see a Provider…]] · Context Window
- [[Changes/Open WebUI/2026-10-29-2-automation-and-scheduling-changes-in-v0-12-5|2 Automation and Scheduling changes in v0.12.5]] · Automation and Scheduling
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
## Nearby in Memory and Personalization

- Earlier: 2026-10-29 · Codex CLI · [[Changes/Codex CLI/2026-10-29-2-memory-and-personalization-changes-in-rust-v0-166-0|2 Memory and Personalization changes in rust-v0.166.0]]
- Later: 2026-10-30 · ChatGPT · [[Changes/ChatGPT/2026-10-30-account-switching-is-rolling-out-to-the-chatgpt-ios-and-android-apps-you-can-sta|Account switching on iOS and Android]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-29-0ef02b&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-29-2-memory-and-personalization-changes-in-v0-12-5.md%0ACard%20ID%3A%20open-webui-2026-10-29-0ef02b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->