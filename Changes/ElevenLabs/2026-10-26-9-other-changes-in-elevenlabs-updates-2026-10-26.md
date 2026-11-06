---
card_id: elevenlabs-2026-10-26-7fd0c0
date: '2026-10-26'
description: 'ElevenLabs · 2026-10-26 · Other changes: 9 changes in ElevenLabs updates
  — 2026-10-26 — **Knowledge base crawl exclusions**: [Create crawl…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4a5af8d949ba0b18dfb39e373b57aaa070c1208257e617068419f07f8ff2a831
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-10-26-7fd0c0
  comparison: ''
  date: '2026-10-26'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-26: 9 other changes'
  evidence:
  - quote: '**Knowledge base crawl exclusions**: [Create crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/create-crawl-job)
      accepts `exclude_patterns`, and the whole-website crawl dialog adds an **Exclude
      patterns** field. Matching URLs are skipped.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Test run names**: [Run tests](https://elevenlabs.io/docs/api-reference/tests/run-tests)
      accepts an optional `name`, which test invocations and their summaries return.
      `PATCH /v1/convai/test-invocations/{test_invocation_id}` renames a run, and
      setting `name` to `null` restores the generated title.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Phone number secrets**: Workspace secrets used as a Twilio auth token
      or an Exotel API token on a phone number show as in use and cannot be deleted
      while the number depends on them.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**PVC and IVC on v4 dialogue**: On the Text to Dialogue endpoints, `clone_strength`
      now decides whether a v4 PVC runs as a PVC or an IVC, and `use_pvc_as_ivc` is
      deprecated.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Expiring service account API keys**: Service account API keys accept
      `expires_at_unix` on [create](https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/create)
      and [update](https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/update),
      between 15 minutes and 90 days in the future. Later expiries are rejected with
      `400` `invalid_api_key_expiry`. On update, pass `"clear"` to remove an expiry.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**SCIM group seat types**: Workspaces that use SCIM without SCIM routing
      can assign a seat type to SCIM-synced groups from the **Groups** page.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Fixes**: [Delete invite](https://elevenlabs.io/docs/api-reference/workspace/invites/delete)
      returns `404` `invite_not_found` for an invite that does not exist, instead
      of a `500` error.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Media folders**: Workspace library files can be organized into folders
      in the Studio media browser.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Fixes**: Generations wait for a just-uploaded reference asset to finish
      processing instead of failing.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: elevenlabs
  product_name: ElevenLabs
  slug: 9-other-changes-in-elevenlabs-updates-2026-10-26
  source_release: elevenlabs-2026-10-26-2026-10-26-ca7c552d
  source_type: elevenlabs_changelog
  theme: uncategorized
  title: 9 other changes in ElevenLabs updates — 2026-10-26
  type: change
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-26-2026-10-26-ca7c552d|elevenlabs-2026-10-26-2026-10-26-ca7c552d]]'
source_type: elevenlabs_changelog
theme: uncategorized
title: 9 other changes in ElevenLabs updates — 2026-10-26
type: change
---

<!-- chronolog:begin region="header" -->
# 9 other changes in ElevenLabs updates — 2026-10-26

**ElevenLabs** · 2026-10-26 · Other changes · Digest · [Official source](https://elevenlabs.io/docs/changelog/2026/10/26) · from [[Releases/ElevenLabs/elevenlabs-2026-10-26-2026-10-26-ca7c552d|ElevenLabs updates — 2026-10-26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Knowledge base crawl exclusions**: [Create crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/create-crawl-job) accepts `exclude_patterns`, and the whole-website crawl dialog adds an **Exclude patterns** field. Matching URLs are skipped.

> **Test run names**: [Run tests](https://elevenlabs.io/docs/api-reference/tests/run-tests) accepts an optional `name`, which test invocations and their summaries return. `PATCH /v1/convai/test-invocations/{test_invocation_id}` renames a run, and setting `name` to `null` restores the generated title.

> **Phone number secrets**: Workspace secrets used as a Twilio auth token or an Exotel API token on a phone number show as in use and cannot be deleted while the number depends on them.

> **PVC and IVC on v4 dialogue**: On the Text to Dialogue endpoints, `clone_strength` now decides whether a v4 PVC runs as a PVC or an IVC, and `use_pvc_as_ivc` is deprecated.

> **Expiring service account API keys**: Service account API keys accept `expires_at_unix` on [create](https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/create) and [update](https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/update), between 15 minutes and 90 days in the future. Later expiries are rejected with `400` `invalid_api_key_expiry`. On update, pass `"clear"` to remove an expiry.

> **SCIM group seat types**: Workspaces that use SCIM without SCIM routing can assign a seat type to SCIM-synced groups from the **Groups** page.

> **Fixes**: [Delete invite](https://elevenlabs.io/docs/api-reference/workspace/invites/delete) returns `404` `invite_not_found` for an invite that does not exist, instead of a `500` error.

> **Media folders**: Workspace library files can be organized into folders in the Studio media browser.

> **Fixes**: Generations wait for a just-uploaded reference asset to finish processing instead of failing.

Source: https://elevenlabs.io/docs/changelog/2026/10/26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-26-2-apps-and-integrations-changes-in-elevenlabs-updates-2026-10-26|2 Apps and Integrations changes in ElevenLabs updates — 2026-10-26]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-26-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-knowledge-base-crawl-exclusions|Knowledge base crawl exclusions]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-26-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-26-clone-strength-for-v4-voices|Clone strength for v4 voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-android-sdk|Android SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-10-26-2-pricing-model-changes-in-elevenlabs-updates-2026-10-26|2 Pricing Model changes in ElevenLabs updates — 2026-10-26]] · Pricing Model
- [[Changes/ElevenLabs/2026-10-26-transcript-downloads-the-dubbing-project-menu-can-download-target-language-trans|Transcript downloads: The dubbing project menu can download target language…]] · Interface Experience
- [[Changes/ElevenLabs/2026-10-26-video-to-music-studio-s-video-to-music-workflow-uses-music-v2-5-by-default|Video to music: Studio's video to music workflow uses Music v2.5 by default]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-26-2-editor-experience-changes-in-elevenlabs-updates-2026-10-26|2 Editor Experience changes in ElevenLabs updates — 2026-10-26]] · Editor Experience
- [[Changes/ElevenLabs/2026-10-26-dubbing|Dubbing]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-voice-changer|Voice Changer]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-2-mobile-and-desktop-changes-in-elevenlabs-updates-2026-10-26|2 Mobile and Desktop changes in ElevenLabs updates — 2026-10-26]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-10-26-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-14-voice-and-audio-changes-in-elevenlabs-updates-2026-10-26|14 Voice and Audio changes in ElevenLabs updates — 2026-10-26]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-voice-cloning-permissions-members-without-the-create-instant-voice-clone-or-crea|Voice cloning permissions]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-10-26-9-agent-mode-changes-in-elevenlabs-updates-2026-10-26|9 Agent Mode changes in ElevenLabs updates — 2026-10-26]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-26-fast-llm-service-tier|Fast LLM service tier]] · Model Support
- [[Changes/ElevenLabs/2026-10-26-3-model-support-changes-in-elevenlabs-updates-2026-10-26|3 Model Support changes in ElevenLabs updates — 2026-10-26]] · Model Support
- [[Changes/ElevenLabs/2026-10-26-elevenlabs-cli|ElevenLabs CLI]] · Account and Access
- [[Changes/ElevenLabs/2026-10-26-oauth-scope-oauth-clients-can-request-the-realtime-translation-scope|OAuth scope: OAuth clients can request the realtime_translation scope]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-26-7fd0c0&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-26-9-other-changes-in-elevenlabs-updates-2026-10-26.md%0ACard%20ID%3A%20elevenlabs-2026-10-26-7fd0c0%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->