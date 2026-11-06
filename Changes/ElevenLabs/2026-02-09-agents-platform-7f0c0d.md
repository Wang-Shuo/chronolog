---
card_id: elevenlabs-2026-02-09-7f0c0d
date: '2026-02-09'
description: 'ElevenLabs · 2026-02-09 · Agent Mode: **Custom guardrails**: Added support
  for user-defined output guardrails that allow you to create custom content filtering…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 949
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: d77e77ce5f01838eac4d03b53140958f9b119286457ab4b754eec9eec25d255d
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-02-09-7f0c0d
  comparison: ''
  confidence: low
  date: '2026-02-09'
  description: 'ElevenLabs — ElevenLabs updates — 2026-02-09: **Custom guardrails**:
    Added support for user-defined output guardrails that allow you to create custom
    content filtering rules beyond standard moderation. Configure guardrails with
    a name, prompt instruction (up to 10,000 characters), and choice of evaluation
    model (`gemini-2.5-flash-lite` or `gemini-2.0-flash`). When triggered, the guardrail
    ends the conversation. See the [Create agent API reference](https://elevenlabs.io/docs/api-reference/agents/create#request.body.conversation_config.safety.guardrails.custom)
    for configuration details.'
  evidence:
  - quote: '**Custom guardrails**: Added support for user-defined output guardrails
      that allow you to create custom content filtering rules beyond standard moderation.
      Configure guardrails with a name, prompt instruction (up to 10,000 characters),
      and choice of evaluation model (`gemini-2.5-flash-lite` or `gemini-2.0-flash`).
      When triggered, the guardrail ends the conversation. See the [Create agent API
      reference](https://elevenlabs.io/docs/api-reference/agents/create#request.body.conversation_config.safety.guardrails.custom)
      for configuration details.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  - quote: '**WhatsApp outbound messaging**: Added [Send outbound message](https://elevenlabs.io/docs/api-reference/whats-app/outbound-message)
      endpoint (`POST /v1/convai/whatsapp/outbound-message`) to initiate conversations
      via WhatsApp using message templates. Required fields include `whatsapp_phone_number_id`,
      `whatsapp_user_id`, `template_name`, `template_language_code`, `template_params`,
      and `agent_id`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  - quote: '**Eleven v3 conversational model**: Added `eleven_v3_conversational` to
      the available TTS models for agents, providing improved voice quality and expressiveness
      in agent conversations.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  - quote: '**Suggested audio tags**: Added `suggested_audio_tags` field to TTS configuration
      for agents using v3 models. Define up to 20 tags (e.g., "happy", "excited")
      to guide expressive speech generation, with optional descriptions for when each
      tag should be used.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  - quote: '**Tool error handling**: Added `tool_error_handling_mode` field to webhook
      tool configurations with options: `auto` (default, determines handling based
      on tool type), `summarized` (sends LLM-generated summary), `passthrough` (sends
      raw error), or `hide` (does not share error with agent).'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  - quote: '**Dynamic variable sanitization**: Added `sanitize` field (boolean, default
      `false`) to `DynamicVariableAssignment`. When enabled, the assignment value
      is removed from tool responses and transcripts while still being processed for
      variable assignment.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  - quote: '**Turn model selection**: Added `TurnModel` enum with `turn_v2` and `turn_v3`
      options for selecting the turn detection model version.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  - quote: '**Workflow node transfers**: Added `is_workflow_node_transfer` field (boolean,
      default `false`) to `AgentTransfer` schema for identifying transfers within
      workflow nodes.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  - quote: '**Transfer branch metadata**: Added `TransferBranchInfoTrafficSplit` and
      `TransferBranchInfoDefaultingToMain` schemas for tracking branch routing information
      in agent transfers.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  - quote: '**Workflow node transition testing**: Added `workflow_node_transition`
      assertion type for unit tests with `UnitTestWorkflowNodeTransitionEvaluationNodeId`
      schema to validate agent workflow transitions.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2026-02-09-2026-02-09-4b81b7a2
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-06-2-agent-mode-changes-in-v2-1-33|2 Agent Mode changes
  in v2.1.33]]'
- '[[Changes/Replit/2026-02-06-agent-inbox|Agent Inbox]]'
- '[[Changes/ElevenLabs/2026-02-09-agents-platform|Agents Platform]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-02-09-2026-02-09-4b81b7a2|elevenlabs-2026-02-09-2026-02-09-4b81b7a2]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2026-02-09 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/2/9) · from [[Releases/ElevenLabs/elevenlabs-2026-02-09-2026-02-09-4b81b7a2|ElevenLabs updates — 2026-02-09]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Custom guardrails**: Added support for user-defined output guardrails that allow you to create custom content filtering rules beyond standard moderation. Configure guardrails with a name, prompt instruction (up to 10,000 characters), and choice of evaluation model (`gemini-2.5-flash-lite` or `gemini-2.0-flash`). When triggered, the guardrail ends the conversation. See the [Create agent API reference](https://elevenlabs.io/docs/api-reference/agents/create#request.body.conversation_config.safety.guardrails.custom) for configuration details.
>
> **WhatsApp outbound messaging**: Added [Send outbound message](https://elevenlabs.io/docs/api-reference/whats-app/outbound-message) endpoint (`POST /v1/convai/whatsapp/outbound-message`) to initiate conversations via WhatsApp using message templates. Required fields include `whatsapp_phone_number_id`, `whatsapp_user_id`, `template_name`, `template_language_code`, `template_params`, and `agent_id`.
>
> **Eleven v3 conversational model**: Added `eleven_v3_conversational` to the available TTS models for agents, providing improved voice quality and expressiveness in agent conversations.
>
> **Suggested audio tags**: Added `suggested_audio_tags` field to TTS configuration for agents using v3 models. Define up to 20 tags (e.g., "happy", "excited") to guide expressive speech generation, with optional descriptions for when each tag should be used.
>
> **Tool error handling**: Added `tool_error_handling_mode` field to webhook tool configurations with options: `auto` (default, determines handling based on tool type), `summarized` (sends LLM-generated summary), `passthrough` (sends raw error), or `hide` (does not share error with agent).
>
> **Dynamic variable sanitization**: Added `sanitize` field (boolean, default `false`) to `DynamicVariableAssignment`. When enabled, the assignment value is removed from tool responses and transcripts while still being processed for variable assignment.
>
> **Turn model selection**: Added `TurnModel` enum with `turn_v2` and `turn_v3` options for selecting the turn detection model version.
>
> **Workflow node transfers**: Added `is_workflow_node_transfer` field (boolean, default `false`) to `AgentTransfer` schema for identifying transfers within workflow nodes.
>
> **Transfer branch metadata**: Added `TransferBranchInfoTrafficSplit` and `TransferBranchInfoDefaultingToMain` schemas for tracking branch routing information in agent transfers.
>
> **Workflow node transition testing**: Added `workflow_node_transition` assertion type for unit tests with `UnitTestWorkflowNodeTransitionEvaluationNodeId` schema to validate agent workflow transitions.
>
> Source: https://elevenlabs.io/docs/changelog/2026/2/9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-02-09-user-interface|User Interface]] · Interface Experience
- [[Changes/ElevenLabs/2026-02-09-agents-platform|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2026-02-09-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-02-09-new-endpoints|New Endpoints]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-02-09-javascript-sdk|JavaScript SDK]] · Model Support
- [[Changes/ElevenLabs/2026-02-09-python-sdk|Python SDK]] · Model Support
- [[Changes/ElevenLabs/2026-02-09-text-to-speech|Text to Speech]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-02-06 · Replit · [[Changes/Replit/2026-02-06-agent-inbox|Agent Inbox]]
- Later: 2026-02-10 · Gemini CLI · [[Changes/Gemini CLI/2026-02-10-4-agent-mode-changes-in-v0-28-0|4 Agent Mode changes in v0.28.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-02-09-7f0c0d&body=Card%3A%20Changes%2FElevenLabs%2F2026-02-09-agents-platform-7f0c0d.md%0ACard%20ID%3A%20elevenlabs-2026-02-09-7f0c0d%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F2%2F9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->