---
card_id: elevenlabs-2026-06-29-2728df
date: '2026-06-29'
description: 'ElevenLabs · 2026-06-29 · Agent Mode: **Branch merge and rebase previews**:
  Added [Preview merged…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1089
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: e6e3e01548c8d8c2d8580c54f38d67b14b89534306da66cb963c1b28c82f9ad4
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-06-29-2728df
  comparison: ''
  confidence: low
  date: '2026-06-29'
  description: 'ElevenLabs — ElevenLabs updates — 2026-06-29: **Branch merge and rebase
    previews**: Added [Preview merged configuration](https://elevenlabs.io/docs/api-reference/agents/branches/preview)
    (`GET /v1/convai/agents/{agent_id}/branches/{source_branch_id}/merge-preview`)
    and preview rebased configuration (`GET /v1/convai/agents/{agent_id}/branches/{branch_id}/rebase-preview`)
    to inspect merged or rebased agent configuration before committing. Both return
    `MergePreviewResponseModel` with the resulting config, `overridden_fields`, and
    `source_identical_to_target`.'
  evidence:
  - quote: '**Branch merge and rebase previews**: Added [Preview merged configuration](https://elevenlabs.io/docs/api-reference/agents/branches/preview)
      (`GET /v1/convai/agents/{agent_id}/branches/{source_branch_id}/merge-preview`)
      and preview rebased configuration (`GET /v1/convai/agents/{agent_id}/branches/{branch_id}/rebase-preview`)
      to inspect merged or rebased agent configuration before committing. Both return
      `MergePreviewResponseModel` with the resulting config, `overridden_fields`,
      and `source_identical_to_target`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/29
  - quote: '**Branch usage metrics**: [List agent branches](https://elevenlabs.io/docs/api-reference/agents/branches/list)
      branch summary responses add optional `calls_7d` (integer) with seven-day call
      volume per branch.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/29
  - quote: '**Auth connection status**: Workspace auth connection response models
      replace OAuth-only `OAuthConnectionStatus` with shared `AuthConnectionStatus`
      (`active`, `refresh_failed`, `revoked`, `credential_invalid`). Bearer, Basic,
      mTLS, custom header, OAuth, OAuth2 JWT, Slack, URL secret and WhatsApp auth
      responses add optional `status`, `status_detail` and `status_updated_at` fields.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/29
  - quote: '**Tool response filtering**: HTTP and agent tool configuration schemas
      add optional `response_filter` to trim tool responses before they reach the
      LLM, with `response_filter_mode` and `response_filters` on related override
      models.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/29
  - quote: '**Workflow phone transfers**: Workflow phone-number transfer nodes add
      optional `uui` (`UUITransferConfig`) for RFC 7433 hex User-to-User Information
      on SIP REFER transfers.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/29
  - quote: '**Telephony agent assignment**: Twilio, Exotel and SIP trunk phone-number
      import request schemas add optional `agent_id` (string) to assign an agent during
      number setup.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/29
  - quote: '**Turn transcription on disabled interruptions**: Turn configuration schemas
      add optional `transcribe_on_disabled_interruptions` (boolean, default `false`)
      to control whether user speech is transcribed when interruptions are disabled.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/29
  - quote: '**Conversation sentiment**: Conversation summary schemas add optional
      `sentiment_analysis`. Conversation user models add optional `sentiment` with
      frustrated-conversation references.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/29
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-06-29-2026-06-29-7be10e9c
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Cursor/2026-06-29-remote-control-3ec330|Remote Control]]'
- '[[Changes/Cursor/2026-06-29-live-activities-and-push-notifications|Live Activities
  and push notifications]]'
- '[[Changes/Cursor/2026-06-29-cursor-for-ios-is-now-available-in-public-beta-on-all-paid-plans-launch-and-mana|Cursor
  for iOS is now available in public beta on all paid plans]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-06-29-2026-06-29-7be10e9c|elevenlabs-2026-06-29-2026-06-29-7be10e9c]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-06-29 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/6/29) · from [[Releases/ElevenLabs/elevenlabs-2026-06-29-2026-06-29-7be10e9c|ElevenLabs updates — 2026-06-29]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Branch merge and rebase previews**: Added [Preview merged configuration](https://elevenlabs.io/docs/api-reference/agents/branches/preview) (`GET /v1/convai/agents/{agent_id}/branches/{source_branch_id}/merge-preview`) and preview rebased configuration (`GET /v1/convai/agents/{agent_id}/branches/{branch_id}/rebase-preview`) to inspect merged or rebased agent configuration before committing. Both return `MergePreviewResponseModel` with the resulting config, `overridden_fields`, and `source_identical_to_target`.
>
> **Branch usage metrics**: [List agent branches](https://elevenlabs.io/docs/api-reference/agents/branches/list) branch summary responses add optional `calls_7d` (integer) with seven-day call volume per branch.
>
> **Auth connection status**: Workspace auth connection response models replace OAuth-only `OAuthConnectionStatus` with shared `AuthConnectionStatus` (`active`, `refresh_failed`, `revoked`, `credential_invalid`). Bearer, Basic, mTLS, custom header, OAuth, OAuth2 JWT, Slack, URL secret and WhatsApp auth responses add optional `status`, `status_detail` and `status_updated_at` fields.
>
> **Tool response filtering**: HTTP and agent tool configuration schemas add optional `response_filter` to trim tool responses before they reach the LLM, with `response_filter_mode` and `response_filters` on related override models.
>
> **Workflow phone transfers**: Workflow phone-number transfer nodes add optional `uui` (`UUITransferConfig`) for RFC 7433 hex User-to-User Information on SIP REFER transfers.
>
> **Telephony agent assignment**: Twilio, Exotel and SIP trunk phone-number import request schemas add optional `agent_id` (string) to assign an agent during number setup.
>
> **Turn transcription on disabled interruptions**: Turn configuration schemas add optional `transcribe_on_disabled_interruptions` (boolean, default `false`) to control whether user speech is transcribed when interruptions are disabled.
>
> **Conversation sentiment**: Conversation summary schemas add optional `sentiment_analysis`. Conversation user models add optional `sentiment` with frustrated-conversation references.
>
> Source: https://elevenlabs.io/docs/changelog/2026/6/29
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-06-29-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-29-workspaces|Workspaces]] · Model Support
- [[Changes/ElevenLabs/2026-06-29-ios-sdk|iOS SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-06-29-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-06-29-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-29-android-sdk|Android SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-06-29-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-29-elevenagents-a80e26|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-06-29-speech-to-text-b8f62a|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-29-text-to-speech|Text to Speech]] · Model Support
- [[Changes/ElevenLabs/2026-06-29-elevenagents-d1c29a|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-06-29-workspaces-e487d5|Workspaces]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-06-29 · Cursor · [[Changes/Cursor/2026-06-29-cursor-for-ios-is-now-available-in-public-beta-on-all-paid-plans-launch-and-mana|Cursor for iOS is now available in public beta on all paid plans]]
- Later: 2026-06-29 · Open WebUI · [[Changes/Open WebUI/2026-06-29-client-user-agent-forwarded-to-model-backends-the-browser-s-user-agent-is-now-pa|🪪 Client User-Agent forwarded to model backends. The browser's User-Agent is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-06-29-2728df&body=Card%3A%20Changes%2FElevenLabs%2F2026-06-29-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-06-29-2728df%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F6%2F29%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->