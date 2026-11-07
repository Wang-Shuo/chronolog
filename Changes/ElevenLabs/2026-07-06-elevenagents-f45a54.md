---
card_id: elevenlabs-2026-07-06-f45a54
date: '2026-07-06'
description: 'ElevenLabs · 2026-07-06 · Agent Mode: **Simulate conversation deprecation**:
  [Simulate…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1096
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: policy
machine_hash: 731cb1ce133dd6ab0b43f96fe009d473e46c7c9f8cb99e23ea019b8f64845bcd
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-07-06-f45a54
  comparison: ''
  confidence: low
  date: '2026-07-06'
  description: 'ElevenLabs — ElevenLabs updates — 2026-07-06: **Simulate conversation
    deprecation**: [Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation)
    and [Stream simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation-stream)
    are deprecated in favor of [Create test](https://elevenlabs.io/docs/api-reference/tests/create)
    and [Run tests on the agent](https://elevenlabs.io/docs/api-reference/tests/run-tests).'
  evidence:
  - quote: '**Simulate conversation deprecation**: [Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation)
      and [Stream simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation-stream)
      are deprecated in favor of [Create test](https://elevenlabs.io/docs/api-reference/tests/create)
      and [Run tests on the agent](https://elevenlabs.io/docs/api-reference/tests/run-tests).'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: '**Tool interruption mode**: `disable_interruptions` is deprecated across
      agent tool and MCP server schemas. Use `interruption_mode` (`ToolInterruptionMode`:
      `allow`, `disable_during_tool`, `disable_during_tool_and_turn`) instead, with
      per-tool overrides via `interruption_mode` on tool override models.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: '**Numeric evaluation scoring**: Evaluation criteria schemas add optional
      `scoring_mode` (`binary` | `numeric_uniform`), optional `max_score` (integer)
      and optional `score_instructions` (string). Evaluation results add optional
      numeric `score`. Conversation analysis payloads add optional `call_success_score`
      and `success_score`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: '**Conversation reasoning**: Transcript and history models add optional
      `reasoning` (`ConversationReasoningModel`) and transcript responses add optional
      `reasoned` (boolean). Agent prompt and LLM schemas add optional `enable_reasoning_summary`
      (boolean).'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: '**Conversation platform billing**: Conversation-related models add optional
      `platform_charge`, `platform_price` and `platform_usage` with per-category breakdown
      via `PlatformCategory` and `PlatformCategoryUsage`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: '**Conversation cost metadata**: Conversation history metadata adds required
      read-only `cost_fiat` (number, USD).'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: '**Unredacted webhook events**: `WebhookEventType` adds `unredacted_transcript`
      and `unredacted_audio` for webhook subscriptions that need unredacted payloads.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  - quote: '**Workflow phone transfer UUI limit**: `UUITransferConfig.data` maximum
      length increases from 256 to 8192 characters for RFC 7433 User-to-User Information
      on SIP REFER transfers.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/6
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: policy
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-07-06-2026-07-06-2f81327c
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-06-3-agent-mode-changes-in-v2-1-202|3 Agent Mode
  changes in v2.1.202]]'
- '[[Changes/ElevenLabs/2026-07-06-cli|CLI]]'
- '[[Changes/ElevenLabs/2026-07-06-elevenagents-c38b88|ElevenAgents]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-07-06-2026-07-06-2f81327c|elevenlabs-2026-07-06-2026-07-06-2f81327c]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-07-06 · [[Themes/agent-mode|Agent Mode]] · Policy · [Official source](https://elevenlabs.io/docs/changelog/2026/7/6) · from [[Releases/ElevenLabs/elevenlabs-2026-07-06-2026-07-06-2f81327c|ElevenLabs updates — 2026-07-06]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Simulate conversation deprecation**: [Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation) and [Stream simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation-stream) are deprecated in favor of [Create test](https://elevenlabs.io/docs/api-reference/tests/create) and [Run tests on the agent](https://elevenlabs.io/docs/api-reference/tests/run-tests).
>
> **Tool interruption mode**: `disable_interruptions` is deprecated across agent tool and MCP server schemas. Use `interruption_mode` (`ToolInterruptionMode`: `allow`, `disable_during_tool`, `disable_during_tool_and_turn`) instead, with per-tool overrides via `interruption_mode` on tool override models.
>
> **Numeric evaluation scoring**: Evaluation criteria schemas add optional `scoring_mode` (`binary` | `numeric_uniform`), optional `max_score` (integer) and optional `score_instructions` (string). Evaluation results add optional numeric `score`. Conversation analysis payloads add optional `call_success_score` and `success_score`.
>
> **Conversation reasoning**: Transcript and history models add optional `reasoning` (`ConversationReasoningModel`) and transcript responses add optional `reasoned` (boolean). Agent prompt and LLM schemas add optional `enable_reasoning_summary` (boolean).
>
> **Conversation platform billing**: Conversation-related models add optional `platform_charge`, `platform_price` and `platform_usage` with per-category breakdown via `PlatformCategory` and `PlatformCategoryUsage`.
>
> **Conversation cost metadata**: Conversation history metadata adds required read-only `cost_fiat` (number, USD).
>
> **Unredacted webhook events**: `WebhookEventType` adds `unredacted_transcript` and `unredacted_audio` for webhook subscriptions that need unredacted payloads.
>
> **Workflow phone transfer UUI limit**: `UUITransferConfig.data` maximum length increases from 256 to 8192 characters for RFC 7433 User-to-User Information on SIP REFER transfers.
>
> Source: https://elevenlabs.io/docs/changelog/2026/7/6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-07-06-elevencreative-studio|ElevenCreative Studio]] · Model Support
- [[Changes/ElevenLabs/2026-07-06-music|Music]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-06-speech-engine|Speech Engine]] · Account and Access
- [[Changes/ElevenLabs/2026-07-06-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-07-06-elevenagents|ElevenAgents]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-07-06-workspaces|Workspaces]] · Pricing Model
- [[Changes/ElevenLabs/2026-07-06-workspaces-9376f0|Workspaces]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-06-cli|CLI]] · Agent Mode
- [[Changes/ElevenLabs/2026-07-06-elevenagents-c38b88|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-07-06-elevencreative-studio-d7b18f|ElevenCreative Studio]] · Model Support
- [[Changes/ElevenLabs/2026-07-06-python-sdk|Python SDK]] · Pricing Model
- [[Changes/ElevenLabs/2026-07-06-javascript-sdk|JavaScript SDK]] · Pricing Model
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-07-06 · Claude Code · [[Changes/Claude Code/2026-07-06-3-agent-mode-changes-in-v2-1-202|3 Agent Mode changes in v2.1.202]]
- Later: 2026-07-06 · Kimi Code · [[Changes/Kimi Code/2026-07-06-web-replace-the-swarm-footer-with-a-single-inline-tool-card-that-shows-live-suba|web: Replace the swarm footer with a single inline tool card that shows live…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-07-06-f45a54&body=Card%3A%20Changes%2FElevenLabs%2F2026-07-06-elevenagents-f45a54.md%0ACard%20ID%3A%20elevenlabs-2026-07-06-f45a54%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F7%2F6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->