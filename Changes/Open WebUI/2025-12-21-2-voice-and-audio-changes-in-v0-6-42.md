---
card_id: open-webui-2025-12-21-f4cd9f
date: '2025-12-21'
description: "Open WebUI · 2025-12-21 · Voice and Audio: 2 changes in v0.6.42 — \U0001F3A4
  Audio file upload failures caused by MIME type matching issues with spacing variations
  and…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2722
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4edfce4bd9564c1f3521752971376940dbdeb48e1d976a636d64da4f3cfffbaf
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-21-f4cd9f
  comparison: ''
  date: '2025-12-21'
  description: 'Open WebUI — v0.6.42: 2 Voice and Audio changes'
  evidence:
  - quote: "\U0001F3A4 Audio file upload failures caused by MIME type matching issues
      with spacing variations and codec parameters were resolved by implementing proper
      MIME type parsing. [#17771](https://github.com/open-webui/open-webui/pull/17771),
      [#17761](https://github.com/open-webui/open-webui/issues/17761)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F528 Source-level log environment variables (AUDIO_LOG_LEVEL, CONFIG_LOG_LEVEL,
      MODELS_LOG_LEVEL, etc.) were removed as they provided limited configuration
      options and added significant complexity across 100+ files; the GLOBAL_LOG_LEVEL
      environment variable, which already took precedence over source-level settings,
      now serves as the exclusive logging configuration method. [#20045](https://github.com/open-webui/open-webui/pull/20045)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-voice-and-audio-changes-in-v0-6-42
  source_release: open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9
  source_type: github_releases
  theme: voice
  title: 2 Voice and Audio changes in v0.6.42
  type: change
related_changes:
- '[[Changes/Google Antigravity/2025-12-17-native-audio-support-for-the-agent|Native
  audio support for the agent]]'
- '[[Changes/HeyGen/2025-12-18-voice-doctor-is-a-chat-based-workflow-for-fixing-the-issues-you-only-notice-afte|Introducing
  Voice Doctor]]'
- '[[Changes/Runway/2025-12-18-text-to-speech-is-now-available-via-the-audio-tab-in-tool-mode-alongside-new-aud|New
  Audio Features]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9]]'
source_type: github_releases
theme: voice
title: 2 Voice and Audio changes in v0.6.42
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Voice and Audio changes in v0.6.42

**Open WebUI** · 2025-12-21 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.42) · from [[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|v0.6.42]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎤 Audio file upload failures caused by MIME type matching issues with spacing variations and codec parameters were resolved by implementing proper MIME type parsing. [#17771](https://github.com/open-webui/open-webui/pull/17771), [#17761](https://github.com/open-webui/open-webui/issues/17761)

> 🔨 Source-level log environment variables (AUDIO_LOG_LEVEL, CONFIG_LOG_LEVEL, MODELS_LOG_LEVEL, etc.) were removed as they provided limited configuration options and added significant complexity across 100+ files; the GLOBAL_LOG_LEVEL environment variable, which already took precedence over source-level settings, now serves as the exclusive logging configuration method. [#20045](https://github.com/open-webui/open-webui/pull/20045)

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
- [[Changes/Open WebUI/2025-12-21-8-interface-experience-changes-in-v0-6-42|8 Interface Experience changes in v0.6.42]] · Interface Experience
- [[Changes/Open WebUI/2025-12-21-4-account-and-access-changes-in-v0-6-42|4 Account and Access changes in v0.6.42]] · Account and Access
- [[Changes/Open WebUI/2025-12-21-external-reranker-operations-were-optimized-to-prevent-event-loop-blocking-by-of|⚡ External reranker operations were optimized to prevent event loop blocking…]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-12-21-3-search-and-browsing-changes-in-v0-6-42|3 Search and Browsing changes in v0.6.42]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-21-11-developer-workflow-changes-in-v0-6-42|11 Developer Workflow changes in v0.6.42]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-21-2-multimodal-input-changes-in-v0-6-42|2 Multimodal Input changes in v0.6.42]] · Multimodal Input
- [[Changes/Open WebUI/2025-12-21-4-image-generation-changes-in-v0-6-42|4 Image Generation changes in v0.6.42]] · Image Generation
- [[Changes/Open WebUI/2025-12-21-channel-image-upload-handling-was-optimized-to-process-and-store-compressed-imag|🖼️ Channel image upload handling was optimized to process and store compressed…]] · Memory and Personalization
- [[Changes/Open WebUI/2025-12-21-28-other-changes-in-v0-6-42|28 other changes in v0.6.42]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2025-12-18 · Runway · [[Changes/Runway/2025-12-18-text-to-speech-is-now-available-via-the-audio-tab-in-tool-mode-alongside-new-aud|New Audio Features]]
- Later: 2025-12-22 · Open WebUI · [[Changes/Open WebUI/2025-12-22-speech-to-text-default-content-type-handling-was-fixed-and-refactored-to-ensure|🎙️ Speech-to-Text default content type handling was fixed and refactored…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-21-f4cd9f&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-21-2-voice-and-audio-changes-in-v0-6-42.md%0ACard%20ID%3A%20open-webui-2025-12-21-f4cd9f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.42%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->