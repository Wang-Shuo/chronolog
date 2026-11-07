---
card_id: elevenlabs-2026-07-20-58210d
date: '2026-07-20'
description: 'ElevenLabs · 2026-07-20 · Voice and Audio: **Webhook event subscriptions**:
  [Update workspace…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2933
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 7ab6f683d80c89cda8269e475dfd1f60d1592567af3ea32c6908ff1626f676c9
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-07-20-58210d
  comparison: ''
  confidence: low
  date: '2026-07-20'
  description: 'ElevenLabs — ElevenLabs updates — 2026-07-20: **Webhook event subscriptions**:
    [Update workspace webhook](https://elevenlabs.io/docs/api-reference/webhooks/update)
    requests add optional `events` (`WorkspaceWebhookEventType[]`) with `voice_library_removal_notice`,
    `speech_to_text` and `agent_qa`. Webhook responses can return the subscribed event
    list.'
  evidence:
  - quote: '**Webhook event subscriptions**: [Update workspace webhook](https://elevenlabs.io/docs/api-reference/webhooks/update)
      requests add optional `events` (`WorkspaceWebhookEventType[]`) with `voice_library_removal_notice`,
      `speech_to_text` and `agent_qa`. Webhook responses can return the subscribed
      event list.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  - quote: '**Usage analytics dimensions**: [Get workspace usage](https://elevenlabs.io/docs/api-reference/analytics/workspace/usage)
      adds `surface` and `actor` to the `group_by` values.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  - quote: '**Clear service account limits**: [Update service account API key](https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/update)
      accepts `character_limit: "clear"` to remove a monthly character limit, alongside
      `"no_update"` and integer values.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  - quote: '**Alerting webhook references**: Alerting webhook notifier schemas now
      identify a workspace webhook with required `webhook_id` (string) instead of
      embedding `url`, `method` and `headers`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: workspaces
  source_release: elevenlabs-2026-07-20-2026-07-20-b16c37ed
  source_type: elevenlabs_changelog
  theme: voice
  theme_matches:
  - matched_terms:
    - voice
    - speech to text
    score: 180
    theme: voice
  - matched_terms:
    - agent
    score: 50
    theme: agent-mode
  title: Workspaces
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-07-20-speech-to-text-2aefae|Speech to Text]]'
- '[[Changes/ElevenLabs/2026-07-20-music|Music]]'
- '[[Changes/ElevenLabs/2026-07-20-python-sdk|Python SDK]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-07-20-2026-07-20-b16c37ed|elevenlabs-2026-07-20-2026-07-20-b16c37ed]]'
source_type: elevenlabs_changelog
theme: voice
title: Workspaces
type: change
---

<!-- chronolog:begin region="header" -->
# Workspaces

**ElevenLabs** · 2026-07-20 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/7/20) · from [[Releases/ElevenLabs/elevenlabs-2026-07-20-2026-07-20-b16c37ed|ElevenLabs updates — 2026-07-20]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Webhook event subscriptions**: [Update workspace webhook](https://elevenlabs.io/docs/api-reference/webhooks/update) requests add optional `events` (`WorkspaceWebhookEventType[]`) with `voice_library_removal_notice`, `speech_to_text` and `agent_qa`. Webhook responses can return the subscribed event list.
>
> **Usage analytics dimensions**: [Get workspace usage](https://elevenlabs.io/docs/api-reference/analytics/workspace/usage) adds `surface` and `actor` to the `group_by` values.
>
> **Clear service account limits**: [Update service account API key](https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/update) accepts `character_limit: "clear"` to remove a monthly character limit, alongside `"no_update"` and integer values.
>
> **Alerting webhook references**: Alerting webhook notifier schemas now identify a workspace webhook with required `webhook_id` (string) instead of embedding `url`, `method` and `headers`.
>
> Source: https://elevenlabs.io/docs/changelog/2026/7/20
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-07-20-android-sdk|Android SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-07-20-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-speech-to-text-2aefae|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-music|Music]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-cli|CLI]] · Agent Mode
- [[Changes/ElevenLabs/2026-07-20-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-07-20-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-sdk-releases|SDK Releases]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-07-17 · Dify · [[Changes/Dify/2026-07-17-3-voice-and-audio-changes-in-1-16-0|3 Voice and Audio changes in 1.16.0]]
- Later: 2026-07-21 · Codex CLI · [[Changes/Codex CLI/2026-07-21-7-voice-and-audio-changes-in-rust-v0-145-0|7 Voice and Audio changes in rust-v0.145.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-07-20-58210d&body=Card%3A%20Changes%2FElevenLabs%2F2026-07-20-workspaces.md%0ACard%20ID%3A%20elevenlabs-2026-07-20-58210d%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F7%2F20%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->