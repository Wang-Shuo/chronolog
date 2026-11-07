---
card_id: elevenlabs-2026-07-06-9306e4
date: '2026-07-06'
description: 'ElevenLabs · 2026-07-06 · Apps and Integrations: Tools and MCP'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2761
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: fcb59b5146b3a758ad2f25e3c00800fa46af09b82348ea6e48b0983896741eb4
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-07-06-9306e4
  comparison: ''
  date: '2026-07-06'
  description: 'ElevenLabs — ElevenLabs updates — 2026-07-06: Tools and MCP'
  evidence:
  - quote: Tools and MCP
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: Deprecated `disable_interruptions` in favor of `interruption_mode` (`allow`,
      `disable_during_tool`, `disable_during_tool_and_turn`)
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: Added per-tool `interruption_mode` overrides on MCP and tool override models
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: Evaluation and analysis
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: Added optional `scoring_mode`, `max_score` and `score_instructions` on
      evaluation criteria
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: Added optional numeric `score` on evaluation results
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: Added optional `call_success_score` and `success_score` on conversation
      analysis payloads
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: Transcripts and reasoning
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: Added optional `reasoning` (`ConversationReasoningModel`) on transcript
      and history models
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: Added optional `reasoned` (boolean) on transcript responses
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: Added optional `enable_reasoning_summary` (boolean) on agent prompt and
      LLM schemas
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: Billing and metadata
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: Added optional `platform_charge`, `platform_price` and `platform_usage`
      on conversation models
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: Added required read-only `cost_fiat` (USD) on conversation history metadata
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: Added `unredacted_transcript` and `unredacted_audio` to `WebhookEventType`
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: Increased `UUITransferConfig.data` max length from 256 to 8192 characters
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-07-06-2026-07-06-2f81327c
  source_type: elevenlabs_changelog
  theme: apps-integrations
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Replit/2026-07-03-integrations|Integrations]]'
- '[[Changes/Claude Code/2026-07-06-improved-mcp-error-messages-clearer-error-when-a-server-config-has-url-but-no-ty|Improved
  MCP error messages]]'
- '[[Changes/ElevenLabs/2026-07-06-sdk-releases|SDK Releases]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-07-06-2026-07-06-2f81327c|elevenlabs-2026-07-06-2026-07-06-2f81327c]]'
source_type: elevenlabs_changelog
theme: apps-integrations
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-07-06 · [[Themes/apps-integrations|Apps and Integrations]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/7/6) · from [[Releases/ElevenLabs/elevenlabs-2026-07-06-2026-07-06-2f81327c|ElevenLabs updates — 2026-07-06]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Tools and MCP
>
> Deprecated `disable_interruptions` in favor of `interruption_mode` (`allow`, `disable_during_tool`, `disable_during_tool_and_turn`)
>
> Added per-tool `interruption_mode` overrides on MCP and tool override models
>
> Evaluation and analysis
>
> Added optional `scoring_mode`, `max_score` and `score_instructions` on evaluation criteria
>
> Added optional numeric `score` on evaluation results
>
> Added optional `call_success_score` and `success_score` on conversation analysis payloads
>
> Transcripts and reasoning
>
> Added optional `reasoning` (`ConversationReasoningModel`) on transcript and history models
>
> Added optional `reasoned` (boolean) on transcript responses
>
> Added optional `enable_reasoning_summary` (boolean) on agent prompt and LLM schemas
>
> Billing and metadata
>
> Added optional `platform_charge`, `platform_price` and `platform_usage` on conversation models
>
> Added required read-only `cost_fiat` (USD) on conversation history metadata
>
> Added `unredacted_transcript` and `unredacted_audio` to `WebhookEventType`
>
> Increased `UUITransferConfig.data` max length from 256 to 8192 characters
>
> Source: https://elevenlabs.io/docs/changelog/2026/7/6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-07-06-elevencreative-studio|ElevenCreative Studio]] · Model Support
- [[Changes/ElevenLabs/2026-07-06-music|Music]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-06-speech-engine|Speech Engine]] · Account and Access
- [[Changes/ElevenLabs/2026-07-06-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-07-06-workspaces|Workspaces]] · Pricing Model
- [[Changes/ElevenLabs/2026-07-06-workspaces-9376f0|Workspaces]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-06-cli|CLI]] · Agent Mode
- [[Changes/ElevenLabs/2026-07-06-elevenagents-c38b88|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-07-06-elevencreative-studio-d7b18f|ElevenCreative Studio]] · Model Support
- [[Changes/ElevenLabs/2026-07-06-python-sdk|Python SDK]] · Pricing Model
- [[Changes/ElevenLabs/2026-07-06-elevenagents-f45a54|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-07-06-javascript-sdk|JavaScript SDK]] · Pricing Model
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-07-06 · Claude Code · [[Changes/Claude Code/2026-07-06-improved-mcp-error-messages-clearer-error-when-a-server-config-has-url-but-no-ty|Improved MCP error messages]]
- Later: 2026-07-06 · OpenCode · [[Changes/OpenCode/2026-07-06-core-fixed-paginated-mcp-tool-catalogs-losing-tool-metadata-and-output-schema-va|Core Fixed paginated MCP tool catalogs losing tool metadata and output schema validation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-07-06-9306e4&body=Card%3A%20Changes%2FElevenLabs%2F2026-07-06-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-07-06-9306e4%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F7%2F6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->