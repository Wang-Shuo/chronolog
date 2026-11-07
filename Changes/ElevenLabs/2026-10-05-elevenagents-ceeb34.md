---
card_id: elevenlabs-2026-10-05-ceeb34
date: '2026-10-05'
description: 'ElevenLabs · 2026-10-05 · Agent Mode: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
  [Get…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1187
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: a1c27e38ae4b21f9761b9b35b7c65aa986e5c5661b54acbaa2fa02307183f0ba
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-10-05-ceeb34
  comparison: ''
  confidence: low
  date: '2026-10-05'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-05: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
    [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
  evidence:
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update
      agent](https://elevenlabs.io/docs/api-reference/agents/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: Added `gpt-6.1-sol` and `claude-sonnet-5-5` to the `LLM` enum.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: Added `eleven_v4` and `eleven_v4_turbo` to the conversational TTS model
      options. The default changed from `eleven_flash_v2` to `eleven_v4_turbo`.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: Agent transfers and standalone workflow agent nodes add optional `preserve_voice_settings`
      (boolean, default `false`) to retain the base voice, TTS model and voice settings
      after a transfer.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: Skip-turn tool configurations add optional `wait_timeout_secs` (number,
      default `-1`). A value of `-1` keeps the agent silent until the caller speaks.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: Post-call webhook configurations add optional `exclude_transcript` (boolean,
      default `false`) to omit turn-by-turn transcripts from JSON transcription webhooks.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: Conversation history redaction configurations add optional `excluded_data_collection_ids`
      (string array, maximum 50) to preserve selected extracted values while redacting
      their rationales.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: Client tool `response_timeout_secs` now accepts `-1` to wait indefinitely
      when `expects_response` is enabled.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '[List tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list)'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: Added optional `priorities` (array) with `low`, `medium`, `high` and `urgent`
      values.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: Added `sort_by` with `created_at` and `priority` values; the default is
      `created_at`.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: Ticket responses now require `title`, nullable `priority`, and a `priority_changes`
      array. Ticket creation and update requests can set `priority`, and ticket status
      adds `cancelled`.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '[List tools](https://elevenlabs.io/docs/api-reference/tools/list) - Added
      optional nullable `used_by_agent_id` (string) to return tools referenced by
      an agent''s main branch.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '[Export batch call results](https://elevenlabs.io/docs/api-reference/batch-calling/export)
      - Added optional nullable `limit` (integer, minimum `1`) to export only the
      first recipients as a column preview.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '[List test invocations](https://elevenlabs.io/docs/api-reference/tests/test-invocations/list)
      and [Get test invocation](https://elevenlabs.io/docs/api-reference/tests/test-invocations/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: Test invocation summaries add required `cancelled_count` (integer) and
      optional `cancelled` (boolean, default `false`).
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: Test run status adds `cancelled`.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '[Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get)
      - Transcript entries add optional nullable `platform_event` with `user_turn_timeout`
      and `skip_turn_wait_elapsed` values.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '[Get agent version metadata](https://elevenlabs.io/docs/api-reference/agents/versions/get)
      - Added optional nullable `merged_authors`, an array describing the people who
      published changes merged into the main branch.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '[Get crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/get-crawl-job)
      - Removed the deprecated `max_depth` response field.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-10-05-2026-10-05-4039c076
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-05-4-agent-mode-changes-in-v2-1-290|4 Agent Mode
  changes in v2.1.290]]'
- '[[Changes/ElevenLabs/2026-10-05-elevenagents|ElevenAgents]]'
- '[[Changes/ElevenLabs/2026-10-05-elevenagents-5bf5b0|ElevenAgents]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-05-2026-10-05-4039c076|elevenlabs-2026-10-05-2026-10-05-4039c076]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-10-05 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/10/5) · from [[Releases/ElevenLabs/elevenlabs-2026-10-05-2026-10-05-4039c076|ElevenLabs updates — 2026-10-05]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
>
> Added `gpt-6.1-sol` and `claude-sonnet-5-5` to the `LLM` enum.
>
> Added `eleven_v4` and `eleven_v4_turbo` to the conversational TTS model options. The default changed from `eleven_flash_v2` to `eleven_v4_turbo`.
>
> Agent transfers and standalone workflow agent nodes add optional `preserve_voice_settings` (boolean, default `false`) to retain the base voice, TTS model and voice settings after a transfer.
>
> Skip-turn tool configurations add optional `wait_timeout_secs` (number, default `-1`). A value of `-1` keeps the agent silent until the caller speaks.
>
> Post-call webhook configurations add optional `exclude_transcript` (boolean, default `false`) to omit turn-by-turn transcripts from JSON transcription webhooks.
>
> Conversation history redaction configurations add optional `excluded_data_collection_ids` (string array, maximum 50) to preserve selected extracted values while redacting their rationales.
>
> Client tool `response_timeout_secs` now accepts `-1` to wait indefinitely when `expects_response` is enabled.
>
> [List tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list)
>
> Added optional `priorities` (array) with `low`, `medium`, `high` and `urgent` values.
>
> Added `sort_by` with `created_at` and `priority` values; the default is `created_at`.
>
> Ticket responses now require `title`, nullable `priority`, and a `priority_changes` array. Ticket creation and update requests can set `priority`, and ticket status adds `cancelled`.
>
> [List tools](https://elevenlabs.io/docs/api-reference/tools/list) - Added optional nullable `used_by_agent_id` (string) to return tools referenced by an agent's main branch.
>
> [Export batch call results](https://elevenlabs.io/docs/api-reference/batch-calling/export) - Added optional nullable `limit` (integer, minimum `1`) to export only the first recipients as a column preview.
>
> [List test invocations](https://elevenlabs.io/docs/api-reference/tests/test-invocations/list) and [Get test invocation](https://elevenlabs.io/docs/api-reference/tests/test-invocations/get)
>
> Test invocation summaries add required `cancelled_count` (integer) and optional `cancelled` (boolean, default `false`).
>
> Test run status adds `cancelled`.
>
> [Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get) - Transcript entries add optional nullable `platform_event` with `user_turn_timeout` and `skip_turn_wait_elapsed` values.
>
> [Get agent version metadata](https://elevenlabs.io/docs/api-reference/agents/versions/get) - Added optional nullable `merged_authors`, an array describing the people who published changes merged into the main branch.
>
> [Get crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/get-crawl-job) - Removed the deprecated `max_depth` response field.
>
> Source: https://elevenlabs.io/docs/changelog/2026/10/5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-05-swift-sdk|Swift SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-05-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-05-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-05-elevenagents-5bf5b0|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-05-python-sdk|Python SDK]] · Model Support
- [[Changes/ElevenLabs/2026-10-05-javascript-sdk|JavaScript SDK]] · Model Support
- [[Changes/ElevenLabs/2026-10-05-sdk-releases|SDK releases]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-05 · Claude Code · [[Changes/Claude Code/2026-10-05-4-agent-mode-changes-in-v2-1-290|4 Agent Mode changes in v2.1.290]]
- Later: 2026-10-05 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-05-5-agent-mode-changes-in-v1-0-92|5 Agent Mode changes in v1.0.92]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-05-ceeb34&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-05-elevenagents-ceeb34.md%0ACard%20ID%3A%20elevenlabs-2026-10-05-ceeb34%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->