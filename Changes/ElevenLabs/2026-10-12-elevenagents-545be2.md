---
card_id: elevenlabs-2026-10-12-545be2
date: '2026-10-12'
description: 'ElevenLabs · 2026-10-12 · Agent Mode: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
  [Get…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1194
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 9c0648bcfe3b020b12048527168eb23f59894b3acb9e7acb16b8afedc65ffa6c
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-10-12-545be2
  comparison: ''
  confidence: low
  date: '2026-10-12'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-12: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
    [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
  evidence:
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update
      agent](https://elevenlabs.io/docs/api-reference/agents/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: Workflow End nodes add `outcome` (`success` or `failure`, default `success`).
      The field is required in responses.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: Standalone workflow agent nodes and agent transfer configurations add nullable
      `branch_id` (string) to target a specific branch of the destination agent. When
      unset, the transfer follows the target agent's traffic deployment. Transfer
      tool results add a `configured` branch reason.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: Prompt override configurations add `tool_ids_strict` (boolean, default
      `false`).
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: TTS configuration `effects` add `pan` (number, -1 to 1, default `0`). The
      `seed` field is deprecated and has no effect.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: '[Get widget config](https://elevenlabs.io/docs/api-reference/widget/get)
      - Added `end_confirmation_enabled` (boolean, default `false`).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: '[List tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list)'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: Added optional `search` (string, maximum 200 characters) and `merged_into_ticket_id`
      (string) query parameters.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: Ticket responses add nullable `merged_into_ticket_id` and nullable `search_match`
      with `field` (`title`, `description`, `comment` or `turn_comment`), `snippet`,
      `highlight_start`, `highlight_end` and nullable `turn_index`.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: '[List workspace tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list-for-workspace)
      - Added optional `agent_id`, `sources`, `priorities`, `sort_by` (`created_at`
      or `priority`, default `created_at`), `owner_user_id`, `issue_type`, `label`,
      `merged_into_ticket_id` and `search` query parameters.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: '[List tests](https://elevenlabs.io/docs/api-reference/tests/list) - Added
      optional `created_by_user_id` (string). Use `@me` for the authenticated user.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: '[List test invocations](https://elevenlabs.io/docs/api-reference/tests/test-invocations/list)
      - Added optional `test_id` (string), `version_id` (string), `start_time` and
      `end_time` (integer, Unix seconds, inclusive) query parameters.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: '[Update agent branch](https://elevenlabs.io/docs/api-reference/agents/branches/update)
      - Added optional `auto_rebase` (boolean). Branch responses add `auto_rebase`
      (boolean, default `false`).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: '[Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: Twilio, SIP trunk and Exotel phone call metadata add nullable `call_result`
      with `answered`, `voicemail`, `busy`, `no_answer` and `failed` values.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: Batch call metadata adds nullable `cold_attempt` (integer) and nullable
      `conversation_type` (`initial`, `retry`, `callback` or `redirect`).
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: The conversation error type adds `workflow_end_failure`.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: Knowledge base auto-sync `auto_discover` is deprecated and no longer has
      any effect.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-10-12-2026-10-12-16e5a6a0
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes
  in v0.12.0]]'
- '[[Changes/OpenClaw/2026-10-10-27-agent-mode-changes-in-v2026-10-1|27 Agent Mode
  changes in v2026.10.1]]'
- '[[Changes/ElevenLabs/2026-10-12-elevenagents|ElevenAgents]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-12-2026-10-12-16e5a6a0|elevenlabs-2026-10-12-2026-10-12-16e5a6a0]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-10-12 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/10/12) · from [[Releases/ElevenLabs/elevenlabs-2026-10-12-2026-10-12-16e5a6a0|ElevenLabs updates — 2026-10-12]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
>
> Workflow End nodes add `outcome` (`success` or `failure`, default `success`). The field is required in responses.
>
> Standalone workflow agent nodes and agent transfer configurations add nullable `branch_id` (string) to target a specific branch of the destination agent. When unset, the transfer follows the target agent's traffic deployment. Transfer tool results add a `configured` branch reason.
>
> Prompt override configurations add `tool_ids_strict` (boolean, default `false`).
>
> TTS configuration `effects` add `pan` (number, -1 to 1, default `0`). The `seed` field is deprecated and has no effect.
>
> [Get widget config](https://elevenlabs.io/docs/api-reference/widget/get) - Added `end_confirmation_enabled` (boolean, default `false`).
>
> [List tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list)
>
> Added optional `search` (string, maximum 200 characters) and `merged_into_ticket_id` (string) query parameters.
>
> Ticket responses add nullable `merged_into_ticket_id` and nullable `search_match` with `field` (`title`, `description`, `comment` or `turn_comment`), `snippet`, `highlight_start`, `highlight_end` and nullable `turn_index`.
>
> [List workspace tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list-for-workspace) - Added optional `agent_id`, `sources`, `priorities`, `sort_by` (`created_at` or `priority`, default `created_at`), `owner_user_id`, `issue_type`, `label`, `merged_into_ticket_id` and `search` query parameters.
>
> [List tests](https://elevenlabs.io/docs/api-reference/tests/list) - Added optional `created_by_user_id` (string). Use `@me` for the authenticated user.
>
> [List test invocations](https://elevenlabs.io/docs/api-reference/tests/test-invocations/list) - Added optional `test_id` (string), `version_id` (string), `start_time` and `end_time` (integer, Unix seconds, inclusive) query parameters.
>
> [Update agent branch](https://elevenlabs.io/docs/api-reference/agents/branches/update) - Added optional `auto_rebase` (boolean). Branch responses add `auto_rebase` (boolean, default `false`).
>
> [Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get)
>
> Twilio, SIP trunk and Exotel phone call metadata add nullable `call_result` with `answered`, `voicemail`, `busy`, `no_answer` and `failed` values.
>
> Batch call metadata adds nullable `cold_attempt` (integer) and nullable `conversation_type` (`initial`, `retry`, `callback` or `redirect`).
>
> The conversation error type adds `workflow_end_failure`.
>
> Knowledge base auto-sync `auto_discover` is deprecated and no longer has any effect.
>
> Source: https://elevenlabs.io/docs/changelog/2026/10/12
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-12-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-12-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-text-to-speech|Text to Speech]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-12-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-music|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-12-text-to-dialogue|Text to Dialogue]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-elevenlabs-cli|ElevenLabs CLI]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-audio-effects|Audio effects]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-voices-e71bd5|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-speech-to-text-f7d11e|Speech to Text]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-10 · OpenClaw · [[Changes/OpenClaw/2026-10-10-27-agent-mode-changes-in-v2026-10-1|27 Agent Mode changes in v2026.10.1]]
- Later: 2026-10-12 · Google Antigravity · [[Changes/Google Antigravity/2026-10-12-you-can-now-attach-zip-archives-to-a-prompt-and-the-agent-unpacks-them-with-its|Attach .zip archives to a prompt, and the agent unpacks them with its tools]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-12-545be2&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-12-elevenagents-545be2.md%0ACard%20ID%3A%20elevenlabs-2026-10-12-545be2%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F12%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->