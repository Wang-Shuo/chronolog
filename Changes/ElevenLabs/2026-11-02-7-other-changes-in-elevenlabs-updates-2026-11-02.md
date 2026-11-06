---
card_id: elevenlabs-2026-11-02-89c6fa
date: '2026-11-02'
description: 'ElevenLabs · 2026-11-02 · Other changes: 7 changes in ElevenLabs updates
  — 2026-11-02 — **Telephony**: Twilio conference transfers can combine post-dial
  digits…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4b3b82a7c0ee5d1a4d2c4901174b1c7fa7e21d38d64361795db518723e47cfc9
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-11-02-89c6fa
  comparison: ''
  date: '2026-11-02'
  description: 'ElevenLabs — ElevenLabs updates — 2026-11-02: 7 other changes'
  evidence:
  - quote: '**Telephony**: Twilio conference transfers can combine post-dial digits
      with call screening (`require_acceptance`). Tools that wait for speech to finish,
      such as `transfer_to_number` and `end_call`, are skipped if the caller hangs
      up during their pre-tool speech. Calling `skip_turn` after a turn timeout starts
      the skip-turn wait, so the silence timeout no longer ends the call during it.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Pronunciation dictionary limit**: Applying pronunciation dictionaries
      can expand the input text to at most 50 times its length plus 10,000 characters.
      Requests over the limit return `400` `pronunciation_dictionary_expansion_too_large`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Invalid frames**: Frames that are not a JSON object receive an `input_error`
      message and the session continues.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Longer conversations**: Speech Engine conversations can last up to 2
      hours, up from 40 minutes. See [Speech Engine](https://elevenlabs.io/docs/overview/capabilities/speech-engine).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Request headers**: Speech Engine request header values can reference
      workspace secrets and are validated in the dashboard. Existing headers must
      be cleared before the WebSocket URL can change.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Higher upload limit**: [Upload music](https://elevenlabs.io/docs/api-reference/music/upload)
      accepts up to 100 songs per user per 24 hours, up from 20.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Fixes**: New users whose only invite is to a child workspace that inherits
      or borrows SSO can sign up with that SSO instead of receiving `400` `provider_not_allowed`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: elevenlabs
  product_name: ElevenLabs
  slug: 7-other-changes-in-elevenlabs-updates-2026-11-02
  source_release: elevenlabs-2026-11-02-2026-11-02-7efe9660
  source_type: elevenlabs_changelog
  theme: uncategorized
  title: 7 other changes in ElevenLabs updates — 2026-11-02
  type: change
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-11-02-2026-11-02-7efe9660|elevenlabs-2026-11-02-2026-11-02-7efe9660]]'
source_type: elevenlabs_changelog
theme: uncategorized
title: 7 other changes in ElevenLabs updates — 2026-11-02
type: change
---

<!-- chronolog:begin region="header" -->
# 7 other changes in ElevenLabs updates — 2026-11-02

**ElevenLabs** · 2026-11-02 · Other changes · Digest · [Official source](https://elevenlabs.io/docs/changelog/2026/11/2) · from [[Releases/ElevenLabs/elevenlabs-2026-11-02-2026-11-02-7efe9660|ElevenLabs updates — 2026-11-02]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Telephony**: Twilio conference transfers can combine post-dial digits with call screening (`require_acceptance`). Tools that wait for speech to finish, such as `transfer_to_number` and `end_call`, are skipped if the caller hangs up during their pre-tool speech. Calling `skip_turn` after a turn timeout starts the skip-turn wait, so the silence timeout no longer ends the call during it.

> **Pronunciation dictionary limit**: Applying pronunciation dictionaries can expand the input text to at most 50 times its length plus 10,000 characters. Requests over the limit return `400` `pronunciation_dictionary_expansion_too_large`.

> **Invalid frames**: Frames that are not a JSON object receive an `input_error` message and the session continues.

> **Longer conversations**: Speech Engine conversations can last up to 2 hours, up from 40 minutes. See [Speech Engine](https://elevenlabs.io/docs/overview/capabilities/speech-engine).

> **Request headers**: Speech Engine request header values can reference workspace secrets and are validated in the dashboard. Existing headers must be cleared before the WebSocket URL can change.

> **Higher upload limit**: [Upload music](https://elevenlabs.io/docs/api-reference/music/upload) accepts up to 100 songs per user per 24 hours, up from 20.

> **Fixes**: New users whose only invite is to a child workspace that inherits or borrows SSO can sign up with that SSO instead of receiving `400` `provider_not_allowed`.

Source: https://elevenlabs.io/docs/changelog/2026/11/2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-11-02-elevenlabs-cli|ElevenLabs CLI]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-4-safety-and-privacy-changes-in-elevenlabs-updates-2026-11-02|4 Safety and Privacy changes in ElevenLabs updates — 2026-11-02]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-11-02-3-pricing-model-changes-in-elevenlabs-updates-2026-11-02|3 Pricing Model changes in ElevenLabs updates — 2026-11-02]] · Pricing Model
- [[Changes/ElevenLabs/2026-11-02-analysis-items-api|Analysis items API]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-sfx-v3|SFX v3]] · Model Support
- [[Changes/ElevenLabs/2026-11-02-7-model-support-changes-in-elevenlabs-updates-2026-11-02|7 Model Support changes in ElevenLabs updates — 2026-11-02]] · Model Support
- [[Changes/ElevenLabs/2026-11-02-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-2-interface-experience-changes-in-elevenlabs-updates-2026-11-02|2 Interface Experience changes in ElevenLabs updates — 2026-11-02]] · Interface Experience
- [[Changes/ElevenLabs/2026-11-02-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-8-agent-mode-changes-in-elevenlabs-updates-2026-11-02|8 Agent Mode changes in ElevenLabs updates — 2026-11-02]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-workspaces|Workspaces]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-2-files-and-data-changes-in-elevenlabs-updates-2026-11-02|2 Files and Data changes in ElevenLabs updates — 2026-11-02]] · Files and Data
- [[Changes/ElevenLabs/2026-11-02-android-sdk|Android SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-11-02-eleven-realtime-for-every-workspace|Eleven Realtime for every workspace]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-noisy-environment-detection-in-the-api|Noisy environment detection in the API]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-unity-sdk|Unity SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-video-clip-background-removal-video-clips-have-a-remove-background-action-and-ri|Video clip background removal]] · Multimodal Input
- [[Changes/ElevenLabs/2026-11-02-svg-assets-svg-uploads-to-assets-stay-svg-and-render-as-vectors-including-in-the|SVG assets: SVG uploads to Assets stay SVG and render as vectors, including…]] · Editor Experience
- [[Changes/ElevenLabs/2026-11-02-channel-integrations-asynchronous-channels-such-as-slack-telegram-intercom-gmail|Channel integrations: Asynchronous channels such as Slack, Telegram, Intercom…]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-11-02-fixes-oauth-discovery-names-the-host-the-client-connected-to-so-mcp-clients-such|Fixes: OAuth discovery names the host the client connected to, so MCP clients…]] · Account and Access
- [[Changes/ElevenLabs/2026-11-02-16-voice-and-audio-changes-in-elevenlabs-updates-2026-11-02|16 Voice and Audio changes in ElevenLabs updates — 2026-11-02]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-fixes-history-items-for-v4-generations-keep-clone-strength-and-speed-in-their-sa|Fixes: History items for v4 generations keep clone_strength and speed…]] · Reliability and Performance
- [[Changes/ElevenLabs/2026-11-02-professional-voice-clones-on-eleven-v4|Professional Voice Clones on Eleven v4]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-realtime-entity-redaction|Realtime entity redaction]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-11-02-89c6fa&body=Card%3A%20Changes%2FElevenLabs%2F2026-11-02-7-other-changes-in-elevenlabs-updates-2026-11-02.md%0ACard%20ID%3A%20elevenlabs-2026-11-02-89c6fa%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F11%2F2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->