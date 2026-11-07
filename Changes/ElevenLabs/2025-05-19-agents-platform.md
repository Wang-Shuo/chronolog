---
card_id: elevenlabs-2025-05-19-482f59
date: '2025-05-19'
description: 'ElevenLabs · 2025-05-19 · Agent Mode: **Agents & Conversations**:'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 683
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 752712bf347e26a6a2fc3a4e9092c1d45afca27887c7176932cd55bf358bc660
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2025-05-19-482f59
  comparison: ''
  date: '2025-05-19'
  description: 'ElevenLabs — ElevenLabs updates — 2025-05-19: **Agents & Conversations**:'
  evidence:
  - quote: '**Agents & Conversations**:'
    source_release: https://elevenlabs.io/docs/changelog/2025/5/19
  - quote: Endpoint `GET /v1/convai/conversation/get_signed_url` (snake_case path)
      has been deprecated. Use the new `GET /v1/convai/conversation/get-signed-url`
      (kebab-case path) instead.
    source_release: https://elevenlabs.io/docs/changelog/2025/5/19
  - quote: '**Phone Numbers**:'
    source_release: https://elevenlabs.io/docs/changelog/2025/5/19
  - quote: '[Get Phone Number Details](https://elevenlabs.io/docs/eleven-agents/api-reference/phone-numbers/get)
      - Response schema for `GET /v1/convai/phone-numbers/{phone_number_id}` updated
      to distinct `Twilio` and `SIPTrunk` provider details.'
    source_release: https://elevenlabs.io/docs/changelog/2025/5/19
  - quote: '[Update Phone Number](https://elevenlabs.io/docs/eleven-agents/api-reference/phone-numbers/update)
      - Response schema for `PATCH /v1/convai/phone-numbers/{phone_number_id}` updated
      similarly for `Twilio` and `SIPTrunk`.'
    source_release: https://elevenlabs.io/docs/changelog/2025/5/19
  - quote: '[List Phone Numbers](https://elevenlabs.io/docs/eleven-agents/api-reference/phone-numbers/list)
      - Response schema for `GET /v1/convai/phone-numbers/` list items updated for
      `Twilio` and `SIPTrunk` providers.'
    source_release: https://elevenlabs.io/docs/changelog/2025/5/19
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2025-05-19-2025-05-19-5c8acc59
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/Devin/2025-05-15-it-s-true-coding-agents-can-be-overconfident-that-s-why-devin-2-1-now-provides-c|It''s
  true: coding agents can be overconfident]]'
- '[[Changes/Dify/2025-05-15-imagine-if-every-idea-could-become-an-ai-agent-with-dify-if-you-can-ask-it-you-c|Imagine
  if every idea could become an AI agent]]'
- '[[Changes/Replit/2025-05-16-ask-agent-to-add-a-database|Ask Agent to add a database]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2025-05-19-2025-05-19-5c8acc59|elevenlabs-2025-05-19-2025-05-19-5c8acc59]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2025-05-19 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2025/5/19) · from [[Releases/ElevenLabs/elevenlabs-2025-05-19-2025-05-19-5c8acc59|ElevenLabs updates — 2025-05-19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Agents & Conversations**:
>
> Endpoint `GET /v1/convai/conversation/get_signed_url` (snake_case path) has been deprecated. Use the new `GET /v1/convai/conversation/get-signed-url` (kebab-case path) instead.
>
> **Phone Numbers**:
>
> [Get Phone Number Details](https://elevenlabs.io/docs/eleven-agents/api-reference/phone-numbers/get) - Response schema for `GET /v1/convai/phone-numbers/{phone_number_id}` updated to distinct `Twilio` and `SIPTrunk` provider details.
>
> [Update Phone Number](https://elevenlabs.io/docs/eleven-agents/api-reference/phone-numbers/update) - Response schema for `PATCH /v1/convai/phone-numbers/{phone_number_id}` updated similarly for `Twilio` and `SIPTrunk`.
>
> [List Phone Numbers](https://elevenlabs.io/docs/eleven-agents/api-reference/phone-numbers/list) - Response schema for `GET /v1/convai/phone-numbers/` list items updated for `Twilio` and `SIPTrunk` providers.
>
> Source: https://elevenlabs.io/docs/changelog/2025/5/19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2025-05-19-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2025-05-19-voices|Voices]] · Collaboration
- [[Changes/ElevenLabs/2025-05-19-billing|Billing]] · Pricing Model
- [[Changes/ElevenLabs/2025-05-19-text-to-speech|Text To Speech]] · Model Support
- [[Changes/ElevenLabs/2025-05-19-agents-platform-e84d3e|Agents Platform]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2025-05-16 · Replit · [[Changes/Replit/2025-05-16-ask-agent-to-add-a-database|Ask Agent to add a database]]
- Later: 2025-05-20 · OpenHands · [[Changes/OpenHands/2025-05-20-2-agent-mode-changes-in-0-39-0|2 Agent Mode changes in 0.39.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2025-05-19-482f59&body=Card%3A%20Changes%2FElevenLabs%2F2025-05-19-agents-platform.md%0ACard%20ID%3A%20elevenlabs-2025-05-19-482f59%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2025%2F5%2F19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->