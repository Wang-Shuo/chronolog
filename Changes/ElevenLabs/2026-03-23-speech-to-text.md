---
card_id: elevenlabs-2026-03-23-04f76a
date: '2026-03-23'
description: 'ElevenLabs · 2026-03-23 · Voice and Audio: `GET /v1/speech-to-text/evaluation/eval-criteria`
  - List evaluation criteria'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 987
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: d3dc8476e7540ce9c60e3bc22c8912be0bf48350a33a0a09a553be9ca59748b4
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-03-23-04f76a
  comparison: ''
  date: '2026-03-23'
  description: 'ElevenLabs — ElevenLabs updates — 2026-03-23: `GET /v1/speech-to-text/evaluation/eval-criteria`
    - List evaluation criteria'
  evidence:
  - quote: '`GET /v1/speech-to-text/evaluation/eval-criteria` - List evaluation criteria'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`POST /v1/speech-to-text/evaluation/eval-criteria` - Create an evaluation
      criterion'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`GET /v1/speech-to-text/evaluation/eval-criteria/{criterion_id}` - Get
      a specific evaluation criterion'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`PATCH /v1/speech-to-text/evaluation/eval-criteria/{criterion_id}` - Update
      an evaluation criterion'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`DELETE /v1/speech-to-text/evaluation/eval-criteria/{criterion_id}` -
      Delete an evaluation criterion'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`POST /v1/speech-to-text/evaluation/evaluations` - Trigger an evaluation'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`GET /v1/speech-to-text/evaluation/evaluations` - List evaluations'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`GET /v1/speech-to-text/evaluation/evaluations/{evaluation_id}` - Get
      a specific evaluation'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`GET /v1/speech-to-text/evaluation/human-agents` - List human agents'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`GET /v1/speech-to-text/evaluation/human-agents/{agent_id}` - Get a human
      agent'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`DELETE /v1/speech-to-text/evaluation/human-agents/{agent_id}` - Delete
      a human agent'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`GET /v1/speech-to-text/evaluation/analytics` - Get evaluation analytics'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`GET /v1/speech-to-text/evaluation/eval-criteria/{criterion_id}/analytics`
      - Get analytics for a specific criterion'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '`GET /v1/speech-to-text/evaluation/human-agents/{agent_id}/analytics`
      - Get analytics for a specific human agent'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: speech-to-text
  source_release: elevenlabs-2026-03-23-2026-03-23-c7dac693
  source_type: elevenlabs_changelog
  theme: voice
  title: Speech to Text
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-03-16-packages|Packages]]'
- '[[Changes/Gemini CLI/2026-03-17-feat-voice-implement-speech-friendly-response-formatter-by-ayush31010-in-https-g|feat(voice):
  implement speech-friendly response formatter]]'
- '[[Changes/Codex CLI/2026-03-19-2-voice-and-audio-changes-in-rust-v0-116-0|2 Voice
  and Audio changes in rust-v0.116.0]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-03-23-2026-03-23-c7dac693|elevenlabs-2026-03-23-2026-03-23-c7dac693]]'
source_type: elevenlabs_changelog
theme: voice
title: Speech to Text
type: change
---

<!-- chronolog:begin region="header" -->
# Speech to Text

**ElevenLabs** · 2026-03-23 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/3/23) · from [[Releases/ElevenLabs/elevenlabs-2026-03-23-2026-03-23-c7dac693|ElevenLabs updates — 2026-03-23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `GET /v1/speech-to-text/evaluation/eval-criteria` - List evaluation criteria
>
> `POST /v1/speech-to-text/evaluation/eval-criteria` - Create an evaluation criterion
>
> `GET /v1/speech-to-text/evaluation/eval-criteria/{criterion_id}` - Get a specific evaluation criterion
>
> `PATCH /v1/speech-to-text/evaluation/eval-criteria/{criterion_id}` - Update an evaluation criterion
>
> `DELETE /v1/speech-to-text/evaluation/eval-criteria/{criterion_id}` - Delete an evaluation criterion
>
> `POST /v1/speech-to-text/evaluation/evaluations` - Trigger an evaluation
>
> `GET /v1/speech-to-text/evaluation/evaluations` - List evaluations
>
> `GET /v1/speech-to-text/evaluation/evaluations/{evaluation_id}` - Get a specific evaluation
>
> `GET /v1/speech-to-text/evaluation/human-agents` - List human agents
>
> `GET /v1/speech-to-text/evaluation/human-agents/{agent_id}` - Get a human agent
>
> `DELETE /v1/speech-to-text/evaluation/human-agents/{agent_id}` - Delete a human agent
>
> `GET /v1/speech-to-text/evaluation/analytics` - Get evaluation analytics
>
> `GET /v1/speech-to-text/evaluation/eval-criteria/{criterion_id}/analytics` - Get analytics for a specific criterion
>
> `GET /v1/speech-to-text/evaluation/human-agents/{agent_id}/analytics` - Get analytics for a specific human agent
>
> Source: https://elevenlabs.io/docs/changelog/2026/3/23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-03-23-packages|Packages]] · Multimodal Input
- [[Changes/ElevenLabs/2026-03-23-ios-sdk|iOS SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-03-23-workspaces|Workspaces]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-23-new-schemas|New Schemas]] · Model Support
- [[Changes/ElevenLabs/2026-03-23-packages-v1-0-0-release-candidate|Packages v1.0.0 Release Candidate]] · Reliability and Performance
- [[Changes/ElevenLabs/2026-03-23-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-03-23-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-23-javascript-sdk|JavaScript SDK]] · Multimodal Input
- [[Changes/ElevenLabs/2026-03-23-python-sdk|Python SDK]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-03-19 · Codex CLI · [[Changes/Codex CLI/2026-03-19-2-voice-and-audio-changes-in-rust-v0-116-0|2 Voice and Audio changes in rust-v0.116.0]]
- Later: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-slash-commands-unavailable-for-the-current-auth-setup-voice-mobile-chrome-upgrad|Slash commands unavailable for the current auth setup…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-03-23-04f76a&body=Card%3A%20Changes%2FElevenLabs%2F2026-03-23-speech-to-text.md%0ACard%20ID%3A%20elevenlabs-2026-03-23-04f76a%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F3%2F23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->