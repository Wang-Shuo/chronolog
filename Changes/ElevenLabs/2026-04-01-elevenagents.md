---
card_id: elevenlabs-2026-04-01-189c5c
date: '2026-04-01'
description: 'ElevenLabs · 2026-04-01 · Agent Mode: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
  [Update…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1000
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 21249d25ff471f09e38c56acbf1fb333ae8c09f9559cd6b3552bc89403f2e3b1
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-04-01-189c5c
  comparison: ''
  confidence: low
  date: '2026-04-01'
  description: 'ElevenLabs — ElevenLabs updates — 2026-04-01: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
    [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
  evidence:
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: Added `file_input` field (`FileInputConfig`, optional) to `ConversationConfig`,
      enabling file upload support (images, PDFs) in chat conversations when the LLM
      supports multimodal input
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: Added `max_conversation_duration_message` field (string, optional) to agent
      configuration — the agent sends this message when the session time limit is
      reached
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: '[Create test](https://elevenlabs.io/docs/api-reference/tests/create),
      [Update test](https://elevenlabs.io/docs/api-reference/tests/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: Added `tool_mock_config` field (object, optional) — a map of tool names
      to `ToolResponseMockConfig` entries for controlling tool mocking behavior during
      simulation
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: '[Text search conversations](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: Added `sort_by` query parameter (string, optional) — accepts `search_score`
      (default) or `created_at`
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: '[Submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: Added `branch_id` field (string, optional) to target a specific agent branch
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: Added `environment` field (string, optional) to specify the target environment
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: '[Twilio outbound call](https://elevenlabs.io/docs/api-reference/twilio/outbound-call),
      [SIP trunk outbound call](https://elevenlabs.io/docs/api-reference/sip-trunk/outbound-call)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: Conversation initiation client data now accepts `branch_id` and `environment`
      optional fields
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-04-01-2026-04-01-d4336c3f
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/OpenCode/2026-03-31-core-subagent-tool-calls-stay-clickable-while-they-are-pending|Core
  Subagent tool calls stay clickable while they are pending]]'
- '[[Changes/Claude Code/2026-04-01-3-agent-mode-changes-in-v2-1-89|3 Agent Mode changes
  in v2.1.89]]'
- '[[Changes/Cline/2026-04-01-exclude-new-task-tool-from-system-prompt-in-yolo-headless-mode|Exclude
  new_task tool from system prompt in yolo/headless mode]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-04-01-2026-04-01-d4336c3f|elevenlabs-2026-04-01-2026-04-01-d4336c3f]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-04-01 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/4/1) · from [[Releases/ElevenLabs/elevenlabs-2026-04-01-2026-04-01-d4336c3f|ElevenLabs updates — 2026-04-01]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
>
> Added `file_input` field (`FileInputConfig`, optional) to `ConversationConfig`, enabling file upload support (images, PDFs) in chat conversations when the LLM supports multimodal input
>
> Added `max_conversation_duration_message` field (string, optional) to agent configuration — the agent sends this message when the session time limit is reached
>
> [Create test](https://elevenlabs.io/docs/api-reference/tests/create), [Update test](https://elevenlabs.io/docs/api-reference/tests/update)
>
> Added `tool_mock_config` field (object, optional) — a map of tool names to `ToolResponseMockConfig` entries for controlling tool mocking behavior during simulation
>
> [Text search conversations](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search)
>
> Added `sort_by` query parameter (string, optional) — accepts `search_score` (default) or `created_at`
>
> [Submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create)
>
> Added `branch_id` field (string, optional) to target a specific agent branch
>
> Added `environment` field (string, optional) to specify the target environment
>
> [Twilio outbound call](https://elevenlabs.io/docs/api-reference/twilio/outbound-call), [SIP trunk outbound call](https://elevenlabs.io/docs/api-reference/sip-trunk/outbound-call)
>
> Conversation initiation client data now accepts `branch_id` and `environment` optional fields
>
> Source: https://elevenlabs.io/docs/changelog/2026/4/1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-04-01-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-01-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-01-elevenagents-2b20f8|ElevenAgents]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-04-01-javascript-sdk|JavaScript SDK]] · Multimodal Input
- [[Changes/ElevenLabs/2026-04-01-packages|Packages]] · Agent Mode
- [[Changes/ElevenLabs/2026-04-01-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-01-voices-7b77ff|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-01-speech-to-text-8868d1|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-01-new-endpoints|New Endpoints]] · Agent Mode
- [[Changes/ElevenLabs/2026-04-01-music|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-04-01-sdk-releases|SDK Releases]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-01 · Cline · [[Changes/Cline/2026-04-01-exclude-new-task-tool-from-system-prompt-in-yolo-headless-mode|Exclude new_task tool from system prompt in yolo/headless mode]]
- Later: 2026-04-01 · Gemini CLI · [[Changes/Gemini CLI/2026-04-01-10-agent-mode-changes-in-v0-36-0|10 Agent Mode changes in v0.36.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-04-01-189c5c&body=Card%3A%20Changes%2FElevenLabs%2F2026-04-01-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-04-01-189c5c%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F4%2F1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->