---
card_id: elevenlabs-2026-11-02-58c1d6
date: '2026-11-02'
description: 'ElevenLabs · 2026-11-02 · Agent Mode: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create)
  and the agent get and update endpoints'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1215
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: db941d371a66bc2208c5f36c96b88b19eb98867c54b971790bae8b840611d9ef
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-11-02-58c1d6
  comparison: ''
  confidence: low
  date: '2026-11-02'
  description: 'ElevenLabs — ElevenLabs updates — 2026-11-02: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create)
    and the agent get and update endpoints'
  evidence:
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create)
      and the agent get and update endpoints'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: The prompt `llm` default changed from `gemini-2.5-flash` to `gemini-3.5-flash`.
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '`TurnConfig` adds `noisy_environment_detection` (boolean, default `false`)
      and `noisy_environment_message` (string). Language presets add nullable `noisy_environment_message_translation`,
      turn overrides and workflow overrides add nullable `noisy_environment_message`,
      and the override config adds `noisy_environment_message` (boolean, default `false`).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: Widget configuration adds `transcript_speech_sync_enabled` (boolean, default
      `true`).
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '`LLM` enum adds `gpt-6.1-terra`, including in `conversation_config_override`
      on the `/v1/convai/conversation` WebSocket.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '[List conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
      and [Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get)
      - Added nullable `user_message_count` and `agent_message_count` (integer).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '[Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: WhatsApp conversation info adds nullable `call_result` (`answered`, `voicemail`,
      `busy`, `no_answer` or `failed`) and `opening_message` (`template_name`, `wamid`,
      `sent_at_unix`, `delivered_at_unix`, `read_at_unix`, `replied_at_unix`, `failed_at_unix`,
      `error_code`, `pricing_category` and `billable`).
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: WhatsApp call permission requests add nullable `responded_at_unix` (integer),
      `permanent` (boolean) and `granted_by_user_call` (boolean).
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: Agent definition source enum adds `architect`.
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '[Update document](https://elevenlabs.io/docs/api-reference/knowledge-base/update)
      - Added optional `enable_auto_sync` (boolean), `auto_remove` (boolean), `minimum_frequency_days`
      (integer) and `tighten_only` (boolean, default `false`).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '[Update triage ticket](https://elevenlabs.io/docs/api-reference/triage-tickets/update)
      - Added optional `qa_comment` (string).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '[List test invocations](https://elevenlabs.io/docs/api-reference/tests/test-invocations/list)
      - Added optional `created_by_user_id` query parameter (string).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '[Create test](https://elevenlabs.io/docs/api-reference/tests/create) and
      the other test endpoints - Tool call evaluations add nullable `guardrail_trigger`
      (object with `type` `any`).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: Rebase a branch onto main (`POST /v1/convai/agents/{agent_id}/branches/{branch_id}/rebase`)
      - The request body accepts `application/json`.
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-11-02-2026-11-02-7efe9660
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-31-2-agent-mode-changes-in-v2-1-316|2 Agent Mode
  changes in v2.1.316]]'
- '[[Changes/ElevenLabs/2026-11-02-elevenlabs-cli|ElevenLabs CLI]]'
- '[[Changes/ElevenLabs/2026-11-02-analysis-items-api|Analysis items API]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-11-02-2026-11-02-7efe9660|elevenlabs-2026-11-02-2026-11-02-7efe9660]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-11-02 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/11/2) · from [[Releases/ElevenLabs/elevenlabs-2026-11-02-2026-11-02-7efe9660|ElevenLabs updates — 2026-11-02]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create) and the agent get and update endpoints
>
> The prompt `llm` default changed from `gemini-2.5-flash` to `gemini-3.5-flash`.
>
> `TurnConfig` adds `noisy_environment_detection` (boolean, default `false`) and `noisy_environment_message` (string). Language presets add nullable `noisy_environment_message_translation`, turn overrides and workflow overrides add nullable `noisy_environment_message`, and the override config adds `noisy_environment_message` (boolean, default `false`).
>
> Widget configuration adds `transcript_speech_sync_enabled` (boolean, default `true`).
>
> `LLM` enum adds `gpt-6.1-terra`, including in `conversation_config_override` on the `/v1/convai/conversation` WebSocket.
>
> [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list) and [Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get) - Added nullable `user_message_count` and `agent_message_count` (integer).
>
> [Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get)
>
> WhatsApp conversation info adds nullable `call_result` (`answered`, `voicemail`, `busy`, `no_answer` or `failed`) and `opening_message` (`template_name`, `wamid`, `sent_at_unix`, `delivered_at_unix`, `read_at_unix`, `replied_at_unix`, `failed_at_unix`, `error_code`, `pricing_category` and `billable`).
>
> WhatsApp call permission requests add nullable `responded_at_unix` (integer), `permanent` (boolean) and `granted_by_user_call` (boolean).
>
> Agent definition source enum adds `architect`.
>
> [Update document](https://elevenlabs.io/docs/api-reference/knowledge-base/update) - Added optional `enable_auto_sync` (boolean), `auto_remove` (boolean), `minimum_frequency_days` (integer) and `tighten_only` (boolean, default `false`).
>
> [Update triage ticket](https://elevenlabs.io/docs/api-reference/triage-tickets/update) - Added optional `qa_comment` (string).
>
> [List test invocations](https://elevenlabs.io/docs/api-reference/tests/test-invocations/list) - Added optional `created_by_user_id` query parameter (string).
>
> [Create test](https://elevenlabs.io/docs/api-reference/tests/create) and the other test endpoints - Tool call evaluations add nullable `guardrail_trigger` (object with `type` `any`).
>
> Rebase a branch onto main (`POST /v1/convai/agents/{agent_id}/branches/{branch_id}/rebase`) - The request body accepts `application/json`.
>
> Source: https://elevenlabs.io/docs/changelog/2026/11/2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-11-02-elevenlabs-cli|ElevenLabs CLI]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-4-safety-and-privacy-changes-in-elevenlabs-updates-2026-11-02|4 Safety and Privacy changes in ElevenLabs updates — 2026-11-02]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-11-02-3-pricing-model-changes-in-elevenlabs-updates-2026-11-02|3 Pricing Model changes in ElevenLabs updates — 2026-11-02]] · Pricing Model
- [[Changes/ElevenLabs/2026-11-02-analysis-items-api|Analysis items API]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-sfx-v3|SFX v3]] · Model Support
- [[Changes/ElevenLabs/2026-11-02-7-model-support-changes-in-elevenlabs-updates-2026-11-02|7 Model Support changes in ElevenLabs updates — 2026-11-02]] · Model Support
- [[Changes/ElevenLabs/2026-11-02-2-interface-experience-changes-in-elevenlabs-updates-2026-11-02|2 Interface Experience changes in ElevenLabs updates — 2026-11-02]] · Interface Experience
- [[Changes/ElevenLabs/2026-11-02-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-8-agent-mode-changes-in-elevenlabs-updates-2026-11-02|8 Agent Mode changes in ElevenLabs updates — 2026-11-02]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-workspaces|Workspaces]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-2-files-and-data-changes-in-elevenlabs-updates-2026-11-02|2 Files and Data changes in ElevenLabs updates — 2026-11-02]] · Files and Data
- [[Changes/ElevenLabs/2026-11-02-android-sdk|Android SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-11-02-eleven-realtime-for-every-workspace|Eleven Realtime for every workspace]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-noisy-environment-detection-in-the-api|Noisy environment detection in the API]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-unity-sdk|Unity SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-video-clip-background-removal-video-clips-have-a-remove-background-action-and-ri|Video clip background removal]] · Multimodal Input
- [[Changes/ElevenLabs/2026-11-02-svg-assets-svg-uploads-to-assets-stay-svg-and-render-as-vectors-including-in-the|SVG assets: SVG uploads to Assets stay SVG and render as vectors, including…]] · Editor Experience
- [[Changes/ElevenLabs/2026-11-02-channel-integrations-asynchronous-channels-such-as-slack-telegram-intercom-gmail|Channel integrations: Asynchronous channels such as Slack, Telegram, Intercom…]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-11-02-fixes-oauth-discovery-names-the-host-the-client-connected-to-so-mcp-clients-such|Fixes: OAuth discovery names the host the client connected to, so MCP clients…]] · Account and Access
- [[Changes/ElevenLabs/2026-11-02-16-voice-and-audio-changes-in-elevenlabs-updates-2026-11-02|16 Voice and Audio changes in ElevenLabs updates — 2026-11-02]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-fixes-history-items-for-v4-generations-keep-clone-strength-and-speed-in-their-sa|Fixes: History items for v4 generations keep clone_strength and speed…]] · Reliability and Performance
- [[Changes/ElevenLabs/2026-11-02-professional-voice-clones-on-eleven-v4|Professional Voice Clones on Eleven v4]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-realtime-entity-redaction|Realtime entity redaction]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-7-other-changes-in-elevenlabs-updates-2026-11-02|7 other changes in ElevenLabs updates — 2026-11-02]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-31 · Claude Code · [[Changes/Claude Code/2026-10-31-2-agent-mode-changes-in-v2-1-316|2 Agent Mode changes in v2.1.316]]
- Later: 2026-11-03 · Google Antigravity · [[Changes/Google Antigravity/2026-11-03-remote-agents-are-starting-to-roll-out-to-google-ai-ultra-and-pro-subscribers-co|Remote agents are starting to roll out to Google AI Ultra and Pro subscribers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-11-02-58c1d6&body=Card%3A%20Changes%2FElevenLabs%2F2026-11-02-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-11-02-58c1d6%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F11%2F2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->