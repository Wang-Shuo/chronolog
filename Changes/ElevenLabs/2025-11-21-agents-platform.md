---
card_id: elevenlabs-2025-11-21-3928d2
date: '2025-11-21'
description: 'ElevenLabs · 2025-11-21 · Agent Mode: [Submit batch calling](https://elevenlabs.io/docs/api-reference/batch-calling/create)'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 869
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 8390a8521477175568690164093336e8f83145113207edeb1bf84542378a18b5
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2025-11-21-3928d2
  comparison: ''
  date: '2025-11-21'
  description: 'ElevenLabs — ElevenLabs updates — 2025-11-21: [Submit batch calling](https://elevenlabs.io/docs/api-reference/batch-calling/create)'
  evidence:
  - quote: '[Submit batch calling](https://elevenlabs.io/docs/api-reference/batch-calling/create)'
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: Request body schema updated (backward compatible)
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: Response schema updated (backward compatible)
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: '[Get batch calling status](https://elevenlabs.io/docs/api-reference/batch-calling/get)'
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: '[Cancel batch calling](https://elevenlabs.io/docs/api-reference/batch-calling/cancel)'
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: '[Retry batch calling](https://elevenlabs.io/docs/api-reference/batch-calling/retry)'
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: '[Get agent settings](https://elevenlabs.io/docs/api-reference/workspace/get)'
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: '[Update agent settings](https://elevenlabs.io/docs/api-reference/workspace/update)'
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: Request and response schemas updated (backward compatible)
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create)'
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: Request schema updated with improved guardrails structure (breaking change
      - simplified `guardrails` to direct reference, removing `oneOf`)
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: '[Get agent](https://elevenlabs.io/docs/api-reference/agents/get)'
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: Response schema updated (breaking change - removed feature-flagged `version_id`
      and `branch_id` fields)
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: '[Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: '[Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation)'
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: Request schema updated (backward compatible)
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: '[Simulate conversation stream](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation-stream)'
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: '[Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)'
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: 'Client events updated:'
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: Added `agent_tool_request` event type
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: 'Tool configurations updated:'
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: Added `use_out_of_band_dtmf` to `PlayDTMFToolConfig`
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  - quote: Removed `ApiIntegrationWebhookToolConfigExternal-*` schemas and their discriminator
      mappings
    source_release: https://elevenlabs.io/docs/changelog/2025/11/21
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2025-11-21-2025-11-21-d3d6b6ca
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-11-19-2-agent-mode-changes-in-rust-v0-59-0|2 Agent Mode
  changes in rust-v0.59.0]]'
- '[[Changes/Cursor/2025-11-21-instant-grep-beta|Instant Grep (Beta)]]'
- '[[Changes/Cursor/2025-11-21-2-agent-mode-changes-in-2-1|2 Agent Mode changes in
  2.1]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2025-11-21-2025-11-21-d3d6b6ca|elevenlabs-2025-11-21-2025-11-21-d3d6b6ca]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2025-11-21 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2025/11/21) · from [[Releases/ElevenLabs/elevenlabs-2025-11-21-2025-11-21-d3d6b6ca|ElevenLabs updates — 2025-11-21]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Submit batch calling](https://elevenlabs.io/docs/api-reference/batch-calling/create)
>
> Request body schema updated (backward compatible)
>
> Response schema updated (backward compatible)
>
> [Get batch calling status](https://elevenlabs.io/docs/api-reference/batch-calling/get)
>
> [Cancel batch calling](https://elevenlabs.io/docs/api-reference/batch-calling/cancel)
>
> [Retry batch calling](https://elevenlabs.io/docs/api-reference/batch-calling/retry)
>
> [Get agent settings](https://elevenlabs.io/docs/api-reference/workspace/get)
>
> [Update agent settings](https://elevenlabs.io/docs/api-reference/workspace/update)
>
> Request and response schemas updated (backward compatible)
>
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create)
>
> Request schema updated with improved guardrails structure (breaking change - simplified `guardrails` to direct reference, removing `oneOf`)
>
> [Get agent](https://elevenlabs.io/docs/api-reference/agents/get)
>
> Response schema updated (breaking change - removed feature-flagged `version_id` and `branch_id` fields)
>
> [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
>
> [Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation)
>
> Request schema updated (backward compatible)
>
> [Simulate conversation stream](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation-stream)
>
> [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)
>
> Client events updated:
>
> Added `agent_tool_request` event type
>
> Tool configurations updated:
>
> Added `use_out_of_band_dtmf` to `PlayDTMFToolConfig`
>
> Removed `ApiIntegrationWebhookToolConfigExternal-*` schemas and their discriminator mappings
>
> Source: https://elevenlabs.io/docs/changelog/2025/11/21
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2025-11-21-generate-single-use-token-https-elevenlabs-io-docs-api-reference-tokens-create|Generate single-use token((source link)]] · Context Window
- [[Changes/ElevenLabs/2025-11-21-python-sdk|Python SDK]] · Model Support
- [[Changes/ElevenLabs/2025-11-21-text-to-speech|Text to Speech]] · Voice and Audio
- [[Changes/ElevenLabs/2025-11-21-voice-management|Voice Management]] · Voice and Audio
- [[Changes/ElevenLabs/2025-11-21-elevencreative-studio|ElevenCreative Studio]] · Voice and Audio
- [[Changes/ElevenLabs/2025-11-21-javascript-sdk|JavaScript SDK]] · Model Support
- [[Changes/ElevenLabs/2025-11-21-packages|Packages]] · Apps and Integrations
- [[Changes/ElevenLabs/2025-11-21-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2025-11-21-4-voice-and-audio-changes-in-elevenlabs-updates-2025-11-21|4 Voice and Audio changes in ElevenLabs updates — 2025-11-21]] · Voice and Audio
- [[Changes/ElevenLabs/2025-11-21-agents-platform-bffd62|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2025-11-21-get-user-subscription-https-elevenlabs-io-docs-api-reference-user-subscription-g|Get user subscription((source link)]] · Pricing Model
- [[Changes/ElevenLabs/2025-11-21-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2025-11-21-5-other-changes-in-elevenlabs-updates-2025-11-21|5 other changes in ElevenLabs updates — 2025-11-21]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2025-11-21 · Cursor · [[Changes/Cursor/2025-11-21-2-agent-mode-changes-in-2-1|2 Agent Mode changes in 2.1]]
- Later: 2025-11-27 · ElevenLabs · [[Changes/ElevenLabs/2025-11-27-agents-platform|Agents Platform]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2025-11-21-3928d2&body=Card%3A%20Changes%2FElevenLabs%2F2025-11-21-agents-platform.md%0ACard%20ID%3A%20elevenlabs-2025-11-21-3928d2%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2025%2F11%2F21%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->