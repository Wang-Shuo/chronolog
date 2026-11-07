---
card_id: elevenlabs-2026-08-31-543885
date: '2026-08-31'
description: 'ElevenLabs · 2026-08-31 · Agent Mode: [List agents](https://elevenlabs.io/docs/api-reference/agents/list)
  - `GET /v1/convai/agents`'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1152
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 228c3dc09b73889f77b5e3f7ad2fc613b5a546eccfa215d9207dcc87289cd3ac
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-08-31-543885
  comparison: ''
  date: '2026-08-31'
  description: 'ElevenLabs — ElevenLabs updates — 2026-08-31: [List agents](https://elevenlabs.io/docs/api-reference/agents/list)
    - `GET /v1/convai/agents`'
  evidence:
  - quote: '[List agents](https://elevenlabs.io/docs/api-reference/agents/list) -
      `GET /v1/convai/agents`'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/31
  - quote: Added optional nullable `tags` (string array). Repeat the query parameter
      to match any supplied tag.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/31
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update
      agent](https://elevenlabs.io/docs/api-reference/agents/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/31
  - quote: Added optional nullable `conversation_config.conversation.dtmf_input_settings`
      (`DTMFInputConfig`). It supports `dtmf_input_timeout` (number, 0.5–10 seconds,
      default `2`), `hash_terminator` (boolean, default `true`) and `redact_input`
      (boolean, default `false`).
    source_release: https://elevenlabs.io/docs/changelog/2026/8/31
  - quote: Added optional `sip_refer_play_dialtone` (boolean, default `true`) to phone-number
      transfer configuration. Set it to `false` to keep the original call leg silent
      while a SIP REFER transfer completes.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/31
  - quote: Start- and end-procedure system tools now accept either a `ProcedureVersionRef`
      or a `ProcedureDraftRef`. Draft references require `procedure_id` (string) and
      set `version_id` to `null`.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/31
  - quote: '[Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)
      - `GET /v1/convai/conversations/{conversation_id}`'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/31
  - quote: Added `file_inputs` (array of `ConversationHistoryTranscriptFileInputResponseModel`)
      to transcript entries. Each item requires `file_id`, `original_filename`, `mime_type`
      and `file_url` (strings).
    source_release: https://elevenlabs.io/docs/changelog/2026/8/31
  - quote: Added optional nullable `campaign` (`BatchCallingCampaignInformation`)
      to batch-call metadata. The object requires `campaign_id` and `campaign_lead_id`
      (strings).
    source_release: https://elevenlabs.io/docs/changelog/2026/8/31
  - quote: Added `dtmf` to `ChatSourceMedium`.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/31
  - quote: Conversation triage ticket issue types add `incorrect_information`, `documentation_gap`,
      `platform_bug` and `wrong_action`.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/31
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-08-31-2026-08-31-cce0450b
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Replit/2026-08-28-agent|Agent]]'
- '[[Changes/Codex CLI/2026-08-29-2-agent-mode-changes-in-rust-v0-151-0|2 Agent Mode
  changes in rust-v0.151.0]]'
- '[[Changes/ElevenLabs/2026-08-31-elevenlabs-cli|ElevenLabs CLI]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-08-31-2026-08-31-cce0450b|elevenlabs-2026-08-31-2026-08-31-cce0450b]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-08-31 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/8/31) · from [[Releases/ElevenLabs/elevenlabs-2026-08-31-2026-08-31-cce0450b|ElevenLabs updates — 2026-08-31]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [List agents](https://elevenlabs.io/docs/api-reference/agents/list) - `GET /v1/convai/agents`
>
> Added optional nullable `tags` (string array). Repeat the query parameter to match any supplied tag.
>
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
>
> Added optional nullable `conversation_config.conversation.dtmf_input_settings` (`DTMFInputConfig`). It supports `dtmf_input_timeout` (number, 0.5–10 seconds, default `2`), `hash_terminator` (boolean, default `true`) and `redact_input` (boolean, default `false`).
>
> Added optional `sip_refer_play_dialtone` (boolean, default `true`) to phone-number transfer configuration. Set it to `false` to keep the original call leg silent while a SIP REFER transfer completes.
>
> Start- and end-procedure system tools now accept either a `ProcedureVersionRef` or a `ProcedureDraftRef`. Draft references require `procedure_id` (string) and set `version_id` to `null`.
>
> [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get) - `GET /v1/convai/conversations/{conversation_id}`
>
> Added `file_inputs` (array of `ConversationHistoryTranscriptFileInputResponseModel`) to transcript entries. Each item requires `file_id`, `original_filename`, `mime_type` and `file_url` (strings).
>
> Added optional nullable `campaign` (`BatchCallingCampaignInformation`) to batch-call metadata. The object requires `campaign_id` and `campaign_lead_id` (strings).
>
> Added `dtmf` to `ChatSourceMedium`.
>
> Conversation triage ticket issue types add `incorrect_information`, `documentation_gap`, `platform_bug` and `wrong_action`.
>
> Source: https://elevenlabs.io/docs/changelog/2026/8/31
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-08-31-dubbing|Dubbing]] · Files and Data
- [[Changes/ElevenLabs/2026-08-31-elevenlabs-cli|ElevenLabs CLI]] · Agent Mode
- [[Changes/ElevenLabs/2026-08-31-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-08-31-python-sdk|Python SDK]] · Multimodal Input
- [[Changes/ElevenLabs/2026-08-31-javascript-sdk|JavaScript SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-08-31-android-sdk|Android SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-08-31-elevenagents-ca07b9|ElevenAgents]] · Multimodal Input
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-08-29 · Codex CLI · [[Changes/Codex CLI/2026-08-29-2-agent-mode-changes-in-rust-v0-151-0|2 Agent Mode changes in rust-v0.151.0]]
- Later: 2026-09-01 · Claude Code · [[Changes/Claude Code/2026-09-01-5-agent-mode-changes-in-v2-1-257|5 Agent Mode changes in v2.1.257]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-08-31-543885&body=Card%3A%20Changes%2FElevenLabs%2F2026-08-31-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-08-31-543885%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F8%2F31%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->