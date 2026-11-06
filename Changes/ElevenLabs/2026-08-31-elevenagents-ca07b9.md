---
card_id: elevenlabs-2026-08-31-ca07b9
date: '2026-08-31'
description: 'ElevenLabs · 2026-08-31 · Multimodal Input: **Phone keypad input**:
  Agent conversation configuration now supports optional `dtmf_input_settings` for
  [DTMF…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-09-19-add-video-to-cn-readme-by-crazywoola-in-https-github-com-langgenius-dify-pull-11|add
    video to cn readme]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1077
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: multimodal
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: ee5f91dfe1f2d8eeb965913beffbf4ac482eb5e3029d81633d933c9836368339
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-08-31-ca07b9
  comparison: ''
  confidence: low
  date: '2026-08-31'
  description: 'ElevenLabs — ElevenLabs updates — 2026-08-31: **Phone keypad input**:
    Agent conversation configuration now supports optional `dtmf_input_settings` for
    [DTMF input](https://elevenlabs.io/docs/eleven-agents/customization/multimodal-input#dtmf-input).
    Configure the digit timeout, use `#` as a terminator and redact keypad entries
    from transcripts, logs and analysis.'
  evidence:
  - quote: '**Phone keypad input**: Agent conversation configuration now supports
      optional `dtmf_input_settings` for [DTMF input](https://elevenlabs.io/docs/eleven-agents/customization/multimodal-input#dtmf-input).
      Configure the digit timeout, use `#` as a terminator and redact keypad entries
      from transcripts, logs and analysis.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/31
  - quote: '**Conversation attachment history**: [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)
      transcript entries now include `file_inputs`, an array containing every attached
      file''s ID, name, MIME type and URL.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/31
  - quote: '**Agent tag filtering**: [List agents](https://elevenlabs.io/docs/api-reference/agents/list)
      now accepts an optional `tags` query parameter. Repeat the parameter to match
      agents with any of the supplied tags.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/31
  - quote: '**Batch campaign context**: [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)
      now identifies batch calls with nullable `campaign` metadata containing the
      required `campaign_id` and `campaign_lead_id`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/31
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-08-31-2026-08-31-cce0450b
  source_type: elevenlabs_changelog
  theme: multimodal
  theme_matches:
  - matched_terms:
    - multimodal
    - multimodal input
    score: 230
    theme: multimodal
  - matched_terms:
    - agent
    - agents
    score: 100
    theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Dify/2026-08-25-3-multimodal-input-changes-in-1-17-0|3 Multimodal Input
  changes in 1.17.0]]'
- '[[Changes/Open WebUI/2026-08-25-2-multimodal-input-changes-in-v0-11-1|2 Multimodal
  Input changes in v0.11.1]]'
- '[[Changes/ElevenLabs/2026-08-31-python-sdk|Python SDK]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-08-31-2026-08-31-cce0450b|elevenlabs-2026-08-31-2026-08-31-cce0450b]]'
source_type: elevenlabs_changelog
theme: multimodal
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-08-31 · [[Themes/multimodal|Multimodal Input]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/8/31) · from [[Releases/ElevenLabs/elevenlabs-2026-08-31-2026-08-31-cce0450b|ElevenLabs updates — 2026-08-31]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Phone keypad input**: Agent conversation configuration now supports optional `dtmf_input_settings` for [DTMF input](https://elevenlabs.io/docs/eleven-agents/customization/multimodal-input#dtmf-input). Configure the digit timeout, use `#` as a terminator and redact keypad entries from transcripts, logs and analysis.
>
> **Conversation attachment history**: [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get) transcript entries now include `file_inputs`, an array containing every attached file's ID, name, MIME type and URL.
>
> **Agent tag filtering**: [List agents](https://elevenlabs.io/docs/api-reference/agents/list) now accepts an optional `tags` query parameter. Repeat the parameter to match agents with any of the supplied tags.
>
> **Batch campaign context**: [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get) now identifies batch calls with nullable `campaign` metadata containing the required `campaign_id` and `campaign_lead_id`.
>
> Source: https://elevenlabs.io/docs/changelog/2026/8/31
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-08-31-dubbing|Dubbing]] · Files and Data
- [[Changes/ElevenLabs/2026-08-31-elevenlabs-cli|ElevenLabs CLI]] · Agent Mode
- [[Changes/ElevenLabs/2026-08-31-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-08-31-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-08-31-python-sdk|Python SDK]] · Multimodal Input
- [[Changes/ElevenLabs/2026-08-31-javascript-sdk|JavaScript SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-08-31-android-sdk|Android SDK]] · Mobile and Desktop
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Multimodal Input

- Earlier: 2026-08-25 · Open WebUI · [[Changes/Open WebUI/2026-08-25-2-multimodal-input-changes-in-v0-11-1|2 Multimodal Input changes in v0.11.1]]
- Later: 2026-09-10 · DeepSeek API · [[Changes/DeepSeek API/2026-09-10-deepseek-v4-1-flash-release|DeepSeek-V4.1-Flash Release]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-09-19 · Dify · [[Changes/Dify/2023-09-19-add-video-to-cn-readme-by-crazywoola-in-https-github-com-langgenius-dify-pull-11|add video to cn readme]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-08-31-ca07b9&body=Card%3A%20Changes%2FElevenLabs%2F2026-08-31-elevenagents-ca07b9.md%0ACard%20ID%3A%20elevenlabs-2026-08-31-ca07b9%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F8%2F31%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->