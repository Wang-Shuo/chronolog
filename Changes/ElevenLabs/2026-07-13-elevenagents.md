---
card_id: elevenlabs-2026-07-13-abd3ae
date: '2026-07-13'
description: 'ElevenLabs · 2026-07-13 · Agent Mode: **Per-agent sentiment analysis**:
  Platform settings add optional `sentiment_analysis` (`SentimentAnalysisSettings`)
  for…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1103
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: dd8ff500a1ea49fbcf8e288d98a3b23ef5c324e9008eb90e392940e9d0e14732
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-07-13-abd3ae
  comparison: ''
  confidence: low
  date: '2026-07-13'
  description: 'ElevenLabs — ElevenLabs updates — 2026-07-13: **Per-agent sentiment
    analysis**: Platform settings add optional `sentiment_analysis` (`SentimentAnalysisSettings`)
    for post-call sentiment scoring configuration per agent.'
  evidence:
  - quote: '**Per-agent sentiment analysis**: Platform settings add optional `sentiment_analysis`
      (`SentimentAnalysisSettings`) for post-call sentiment scoring configuration
      per agent.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/13
  - quote: '**Auto-translate transcripts**: Platform settings add optional `auto_translate_transcript_to_app_language`
      (boolean) to translate conversation transcripts to the viewer''s app language
      in history.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/13
  - quote: '**Nested agent transfers**: Workflows add push, pop and replace operations
      for nested agent transfers.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/13
  - quote: '**Backchannel detection**: Transcript user-turn models add optional `ignored_as_backchannel`
      (boolean) to mark utterances filtered as backchannels.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/13
  - quote: '**Auxiliary conversation audio**: [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)
      responses add required `has_auxiliary_audio` (boolean) alongside existing audio
      flags.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/13
  - quote: '**MCP environment scoping**: MCP server and tool routes add optional `environment`
      query parameter (defaults to production) on list tools, get tool, create tool
      config and update tool config endpoints.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/13
  - quote: '**Tool call sound override**: Tool and MCP override schemas allow `tool_call_sound:
      "off"` to silence per-tool call sounds while inheriting server defaults when
      unset.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/13
  - quote: '**Twilio SMS routing**: Twilio phone-number import requests add optional
      `enable_sms` (boolean, default on) to control inbound SMS routing during number
      setup.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/13
  - quote: '**User sentiment sorting**: [List users](https://elevenlabs.io/docs/api-reference/users/list)
      adds optional `sort_direction` and supports sorting by `average_sentiment_score`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/13
  - quote: '**Knowledge base external sync**: External sync schemas rename `ExternalSyncType`
      to `ExternalSyncProvider`, add sync job trigger and type enums with `KbExternalSyncJob`,
      and folder responses can include `active_sync_job` for in-flight or terminal
      sync status.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/13
  - quote: '**TTS latency setting deprecation**: `optimize_streaming_latency` on agent
      TTS settings is marked deprecated and documented as a no-op.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/13
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-07-13-2026-07-13-a5dee32c
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Ollama/2026-07-11-2-agent-mode-changes-in-v0-32-0|2 Agent Mode changes
  in v0.32.0]]'
- '[[Changes/Codex CLI/2026-07-13-2-agent-mode-changes-in-rust-v0-144-2|2 Agent Mode
  changes in rust-v0.144.2]]'
- '[[Changes/ElevenLabs/2026-07-13-python-sdk|Python SDK]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-07-13-2026-07-13-a5dee32c|elevenlabs-2026-07-13-2026-07-13-a5dee32c]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-07-13 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/7/13) · from [[Releases/ElevenLabs/elevenlabs-2026-07-13-2026-07-13-a5dee32c|ElevenLabs updates — 2026-07-13]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Per-agent sentiment analysis**: Platform settings add optional `sentiment_analysis` (`SentimentAnalysisSettings`) for post-call sentiment scoring configuration per agent.
>
> **Auto-translate transcripts**: Platform settings add optional `auto_translate_transcript_to_app_language` (boolean) to translate conversation transcripts to the viewer's app language in history.
>
> **Nested agent transfers**: Workflows add push, pop and replace operations for nested agent transfers.
>
> **Backchannel detection**: Transcript user-turn models add optional `ignored_as_backchannel` (boolean) to mark utterances filtered as backchannels.
>
> **Auxiliary conversation audio**: [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get) responses add required `has_auxiliary_audio` (boolean) alongside existing audio flags.
>
> **MCP environment scoping**: MCP server and tool routes add optional `environment` query parameter (defaults to production) on list tools, get tool, create tool config and update tool config endpoints.
>
> **Tool call sound override**: Tool and MCP override schemas allow `tool_call_sound: "off"` to silence per-tool call sounds while inheriting server defaults when unset.
>
> **Twilio SMS routing**: Twilio phone-number import requests add optional `enable_sms` (boolean, default on) to control inbound SMS routing during number setup.
>
> **User sentiment sorting**: [List users](https://elevenlabs.io/docs/api-reference/users/list) adds optional `sort_direction` and supports sorting by `average_sentiment_score`.
>
> **Knowledge base external sync**: External sync schemas rename `ExternalSyncType` to `ExternalSyncProvider`, add sync job trigger and type enums with `KbExternalSyncJob`, and folder responses can include `active_sync_job` for in-flight or terminal sync status.
>
> **TTS latency setting deprecation**: `optimize_streaming_latency` on agent TTS settings is marked deprecated and documented as a no-op.
>
> Source: https://elevenlabs.io/docs/changelog/2026/7/13
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-07-13-python-sdk|Python SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-07-13-workspaces|Workspaces]] · Collaboration
- [[Changes/ElevenLabs/2026-07-13-packages|Packages]] · Reliability and Performance
- [[Changes/ElevenLabs/2026-07-13-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-07-13-javascript-sdk|JavaScript SDK]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-07-13 · Codex CLI · [[Changes/Codex CLI/2026-07-13-2-agent-mode-changes-in-rust-v0-144-2|2 Agent Mode changes in rust-v0.144.2]]
- Later: 2026-07-13 · Google Antigravity · [[Changes/Google Antigravity/2026-07-13-2-agent-mode-changes-in-hub-v2-3-0-queued-messages-plain|2 Agent Mode changes in HUB v2.3.0 — Queued messages, plain…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-07-13-abd3ae&body=Card%3A%20Changes%2FElevenLabs%2F2026-07-13-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-07-13-abd3ae%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F7%2F13%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->