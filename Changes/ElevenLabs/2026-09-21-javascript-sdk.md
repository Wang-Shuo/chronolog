---
card_id: elevenlabs-2026-09-21-5e616a
date: '2026-09-21'
description: 'ElevenLabs · 2026-09-21 · Model Support: [v2.69.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.69.0)
  - Added `transcriptEdit` to the realtime…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1351
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: dd6ebee798161f1f2a2e98ce61865646915d3c715376a534e1703c01e63514c8
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-09-21-5e616a
  comparison: ''
  confidence: low
  date: '2026-09-21'
  description: 'ElevenLabs — ElevenLabs updates — 2026-09-21: [v2.69.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.69.0)
    - Added `transcriptEdit` to the realtime Speech to Text wrapper, with edited text
    delivered through `edited_transcript` events. Fixed Speech Engine JWT verification
    for API keys with data residency suffixes. Added `phoneNumbers.listV2` and Flows
    template methods to list and get templates and list, create and get runs. Regenerated
    clients and types for GPT Image 2.5, Slack agent alerting, parallel tool calls,
    `gpt-6-astra`, service account API key concurrency limits, Music zero retention,
    conversation filters and MCP tool approval statuses.'
  evidence:
  - quote: '[v2.69.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.69.0)
      - Added `transcriptEdit` to the realtime Speech to Text wrapper, with edited
      text delivered through `edited_transcript` events. Fixed Speech Engine JWT verification
      for API keys with data residency suffixes. Added `phoneNumbers.listV2` and Flows
      template methods to list and get templates and list, create and get runs. Regenerated
      clients and types for GPT Image 2.5, Slack agent alerting, parallel tool calls,
      `gpt-6-astra`, service account API key concurrency limits, Music zero retention,
      conversation filters and MCP tool approval statuses.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/21
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: javascript-sdk
  source_release: elevenlabs-2026-09-21-2026-09-21-6d2d4d80
  source_type: elevenlabs_changelog
  theme: model-support
  theme_matches:
  - matched_terms:
    - speech to text
    score: 70
    theme: voice
  - matched_terms:
    - gpt image
    score: 60
    theme: image-generation
  - matched_terms:
    - agent
    score: 50
    theme: agent-mode
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  theme_resolution: manual-semantic-rule-v2
  title: JavaScript SDK
  type: change
related_changes:
- '[[Changes/Ollama/2026-09-19-2-model-support-changes-in-v0-34-3|2 Model Support
  changes in v0.34.3]]'
- '[[Changes/OpenClaw/2026-09-19-28-model-support-changes-in-v2026-9-5|28 Model Support
  changes in v2026.9.5]]'
- '[[Changes/ElevenLabs/2026-09-21-text-to-speech-576ca6|Text to Speech]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-09-21-2026-09-21-6d2d4d80|elevenlabs-2026-09-21-2026-09-21-6d2d4d80]]'
source_type: elevenlabs_changelog
theme: model-support
title: JavaScript SDK
type: change
---

<!-- chronolog:begin region="header" -->
# JavaScript SDK

**ElevenLabs** · 2026-09-21 · [[Themes/model-support|Model Support]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/9/21) · from [[Releases/ElevenLabs/elevenlabs-2026-09-21-2026-09-21-6d2d4d80|ElevenLabs updates — 2026-09-21]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [v2.69.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.69.0) - Added `transcriptEdit` to the realtime Speech to Text wrapper, with edited text delivered through `edited_transcript` events. Fixed Speech Engine JWT verification for API keys with data residency suffixes. Added `phoneNumbers.listV2` and Flows template methods to list and get templates and list, create and get runs. Regenerated clients and types for GPT Image 2.5, Slack agent alerting, parallel tool calls, `gpt-6-astra`, service account API key concurrency limits, Music zero retention, conversation filters and MCP tool approval statuses.
>
> Source: https://elevenlabs.io/docs/changelog/2026/9/21
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-09-21-image-and-video|Image and video]] · Image Generation
- [[Changes/ElevenLabs/2026-09-21-text-to-speech|Text to Speech]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-21-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-09-21-text-to-speech-576ca6|Text to Speech]] · Model Support
- [[Changes/ElevenLabs/2026-09-21-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-09-21-python-sdk|Python SDK]] · Model Support
- [[Changes/ElevenLabs/2026-09-21-user|User]] · Pricing Model
- [[Changes/ElevenLabs/2026-09-21-image-and-video-915070|Image and video]] · Image Generation
- [[Changes/ElevenLabs/2026-09-21-elevenagents-d15bdd|ElevenAgents]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-19 · OpenClaw · [[Changes/OpenClaw/2026-09-19-28-model-support-changes-in-v2026-9-5|28 Model Support changes in v2026.9.5]]
- Later: 2026-09-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-21-enable-the-rubber-duck-agent-for-every-model-family-and-for-low-cost-tier-sessio|Enable the rubber-duck agent for every model family and for low-cost-tier session models]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-09-21-5e616a&body=Card%3A%20Changes%2FElevenLabs%2F2026-09-21-javascript-sdk.md%0ACard%20ID%3A%20elevenlabs-2026-09-21-5e616a%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F9%2F21%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->