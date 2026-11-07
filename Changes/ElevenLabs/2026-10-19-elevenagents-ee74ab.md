---
card_id: elevenlabs-2026-10-19-ee74ab
date: '2026-10-19'
description: 'ElevenLabs · 2026-10-19 · Agent Mode: [Get agent](https://elevenlabs.io/docs/api-reference/agents/get),
  [Update…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1201
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: c812ffb026f9aad69725fd7cf5068fb1085fabdab2adaaedcb04cc46c90ded9e
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-10-19-ee74ab
  comparison: ''
  confidence: low
  date: '2026-10-19'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-19: [Get agent](https://elevenlabs.io/docs/api-reference/agents/get),
    [Update agent](https://elevenlabs.io/docs/api-reference/agents/update), [Preview
    rebase](https://elevenlabs.io/docs/api-reference/agents/branches/preview-rebase)
    and [Preview merge](https://elevenlabs.io/docs/api-reference/agents/branches/preview-merge)'
  evidence:
  - quote: '[Get agent](https://elevenlabs.io/docs/api-reference/agents/get), [Update
      agent](https://elevenlabs.io/docs/api-reference/agents/update), [Preview rebase](https://elevenlabs.io/docs/api-reference/agents/branches/preview-rebase)
      and [Preview merge](https://elevenlabs.io/docs/api-reference/agents/branches/preview-merge)'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: Added optional `include_procedure_generated_workflow_elements` (boolean,
      default `true`). When `false`, the returned workflow contains only authored
      nodes and edges, without those generated from structured procedures.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update
      agent](https://elevenlabs.io/docs/api-reference/agents/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: The `llm` enum adds `gemini-4-argon`, `claude-opus-4-6` and `nemotron-35-super-vl-nvfp4`.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: TTS configuration `effects` removes the deprecated `seed` field.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '[Delete agent](https://elevenlabs.io/docs/api-reference/agents/delete)
      - Added optional `force` (boolean, default `false`).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '[List agents](https://elevenlabs.io/docs/api-reference/agents/list) -
      `sort_by` adds `updated_at`. Agent summaries add required `updated_at_unix_secs`
      (integer).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '[Rebase branch](https://elevenlabs.io/docs/api-reference/agents/branches/rebase)
      and [Preview rebase](https://elevenlabs.io/docs/api-reference/agents/branches/preview-rebase)
      - Added optional `source_branch_id` (string). Defaults to the agent''s main
      branch.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '[Outbound call](https://elevenlabs.io/docs/api-reference/twilio/outbound-call),
      [Submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create)
      and [Get batch call](https://elevenlabs.io/docs/api-reference/batch-calling/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: Twilio machine detection configuration adds `actions`, an array of rules
      with required `action` (`hang_up`) and required `answered_by` (array of `human`,
      `fax`, `unknown`, `machine_start`, `machine_end_beep`, `machine_end_silence`
      or `machine_end_other`). Each action can appear in at most one rule.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '[Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: Transcript tool calls add nullable `tool_id` (string). It is not set for
      tools without an ID, such as system tools.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: Turn metrics add nullable `voice_id` (string).
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: Tool results add nullable `to_agent` and `to_node` (string).
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: WhatsApp conversation info adds nullable `recipient` with nullable `phone`
      and `bsuid` (string), and nullable `call_permission_request` with required `state`
      (`blocked`, `sent`, `accepted` or `declined`) and nullable `requested_at_unix`
      (integer).
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: The platform charge category enum adds `v3_addon`, `v4_addon` and `rag_addon`.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '[Get ticket](https://elevenlabs.io/docs/api-reference/triage-tickets/get),
      [List tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list)
      and [List workspace tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list-for-workspace)'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: Ticket responses add required `status_changes`, an array of objects with
      `status`, nullable `changed_by_user_id` (string) and `changed_at_unix_secs`
      (integer).
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-10-19-2026-10-19-dd219c14
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-19-added-claude-api-managed-agents-secure-which-compares-a-managed-agents-agent-s-s|Added
  /claude-api managed-agents-secure, which compares a Managed Agents agent''s…]]'
- '[[Changes/ElevenLabs/2026-10-19-javascript-sdk|JavaScript SDK]]'
- '[[Changes/ElevenLabs/2026-10-19-elevenagents-b18b24|ElevenAgents]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-19-2026-10-19-dd219c14|elevenlabs-2026-10-19-2026-10-19-dd219c14]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-10-19 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/10/19) · from [[Releases/ElevenLabs/elevenlabs-2026-10-19-2026-10-19-dd219c14|ElevenLabs updates — 2026-10-19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Get agent](https://elevenlabs.io/docs/api-reference/agents/get), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update), [Preview rebase](https://elevenlabs.io/docs/api-reference/agents/branches/preview-rebase) and [Preview merge](https://elevenlabs.io/docs/api-reference/agents/branches/preview-merge)
>
> Added optional `include_procedure_generated_workflow_elements` (boolean, default `true`). When `false`, the returned workflow contains only authored nodes and edges, without those generated from structured procedures.
>
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
>
> The `llm` enum adds `gemini-4-argon`, `claude-opus-4-6` and `nemotron-35-super-vl-nvfp4`.
>
> TTS configuration `effects` removes the deprecated `seed` field.
>
> [Delete agent](https://elevenlabs.io/docs/api-reference/agents/delete) - Added optional `force` (boolean, default `false`).
>
> [List agents](https://elevenlabs.io/docs/api-reference/agents/list) - `sort_by` adds `updated_at`. Agent summaries add required `updated_at_unix_secs` (integer).
>
> [Rebase branch](https://elevenlabs.io/docs/api-reference/agents/branches/rebase) and [Preview rebase](https://elevenlabs.io/docs/api-reference/agents/branches/preview-rebase) - Added optional `source_branch_id` (string). Defaults to the agent's main branch.
>
> [Outbound call](https://elevenlabs.io/docs/api-reference/twilio/outbound-call), [Submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create) and [Get batch call](https://elevenlabs.io/docs/api-reference/batch-calling/get)
>
> Twilio machine detection configuration adds `actions`, an array of rules with required `action` (`hang_up`) and required `answered_by` (array of `human`, `fax`, `unknown`, `machine_start`, `machine_end_beep`, `machine_end_silence` or `machine_end_other`). Each action can appear in at most one rule.
>
> [Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get)
>
> Transcript tool calls add nullable `tool_id` (string). It is not set for tools without an ID, such as system tools.
>
> Turn metrics add nullable `voice_id` (string).
>
> Tool results add nullable `to_agent` and `to_node` (string).
>
> WhatsApp conversation info adds nullable `recipient` with nullable `phone` and `bsuid` (string), and nullable `call_permission_request` with required `state` (`blocked`, `sent`, `accepted` or `declined`) and nullable `requested_at_unix` (integer).
>
> The platform charge category enum adds `v3_addon`, `v4_addon` and `rag_addon`.
>
> [Get ticket](https://elevenlabs.io/docs/api-reference/triage-tickets/get), [List tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list) and [List workspace tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list-for-workspace)
>
> Ticket responses add required `status_changes`, an array of objects with `status`, nullable `changed_by_user_id` (string) and `changed_at_unix_secs` (integer).
>
> Source: https://elevenlabs.io/docs/changelog/2026/10/19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-19-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-19-music-and-sound-effects|Music and Sound Effects]] · Enterprise and Administration
- [[Changes/ElevenLabs/2026-10-19-eleven-realtime|Eleven Realtime]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-elevenagents|ElevenAgents]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-video-to-music|Video to Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-19-realtime-translation|Realtime Translation]] · Enterprise and Administration
- [[Changes/ElevenLabs/2026-10-19-javascript-sdk|JavaScript SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-elevenagents-b18b24|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-music|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-19-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-python-sdk|Python SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-19-voices-f9aa8c|Voices]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-19 · Claude Code · [[Changes/Claude Code/2026-10-19-added-claude-api-managed-agents-secure-which-compares-a-managed-agents-agent-s-s|Added /claude-api managed-agents-secure, which compares a Managed Agents agent's…]]
- Later: 2026-10-19 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-19-2-agent-mode-changes-in-v1-0-100|2 Agent Mode changes in v1.0.100]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-19-ee74ab&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-19-elevenagents-ee74ab.md%0ACard%20ID%3A%20elevenlabs-2026-10-19-ee74ab%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->