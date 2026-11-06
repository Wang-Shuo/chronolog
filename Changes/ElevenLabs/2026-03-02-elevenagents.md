---
card_id: elevenlabs-2026-03-02-247dfc
date: '2026-03-02'
description: 'ElevenLabs · 2026-03-02 · Interface Experience: **New widget configuration
  options**: Several new settings are now available for the ElevenAgents conversation…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1148
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 046a9c20fa102be8e0c8ca625cbefba6edb1a157074511d99926b515a81a9a94
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-03-02-247dfc
  comparison: ''
  confidence: low
  date: '2026-03-02'
  description: 'ElevenLabs — ElevenLabs updates — 2026-03-02: **New widget configuration
    options**: Several new settings are now available for the ElevenAgents conversation
    widget in the agent dashboard:'
  evidence:
  - quote: '**New widget configuration options**: Several new settings are now available
      for the ElevenAgents conversation widget in the agent dashboard:'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: '**Collapsible widget** (`widget.dismissible`): Allow users to minimize
      or dismiss the widget during a conversation.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: '**Action indicator** (`widget.show_agent_status`): Display a visual indicator
      when the agent is actively using tools, with distinct states for working, done,
      and error. Enabling this setting automatically adds `agent_tool_request` and
      `agent_tool_response` to the agent''s client events.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: '**Conversation ID display** (`widget.show_conversation_id`): Show the
      conversation ID to users after a call ends. Defaults to `true` for both new
      and existing agents.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: '**Audio tag visibility** (`widget.strip_audio_tags`): Hide audio tags
      from conversation transcripts. Defaults to `true` for both new and existing
      agents.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: '**Syntax highlighting theme** (`widget.syntax_highlight_theme`): Configure
      code block highlighting in transcripts. Accepts `null` (Auto), `light`, or `dark`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: '**Folder-aware agent testing**: The [List agent tests](https://elevenlabs.io/docs/api-reference/tests/list)
      endpoint now supports organizing tests into folders. Added `parent_folder_id`,
      `include_folders`, and `sort_mode` query parameters for filtered listing. Test
      creation and update endpoints accept `parent_folder_id` to assign tests to folders,
      and test summaries now include entity type, parent folder path, and children
      count.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: '**Workflow `say` node**: Added a new `say` node type to agent workflows
      (`WorkflowSayNodeModel`). This node supports `conversation_config`, `additional_prompt`,
      and tool and knowledge base overrides. The node''s message payload uses a discriminated
      union with two variants: `literal` (static text via `text`) and `prompt` (LLM-generated
      via `prompt`).'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: '**SMB tool configuration**: Formalized the `SMBToolConfig` schema with
      a required, discriminated `params` object. Supported operation types are `create`,
      `list`, `search`, `update`, and `delete`, each applicable to SMB entity categories
      including clients, staff, services, products, and assets.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: '**Summary language for agents**: Added `summary_language` field to agent
      configuration to specify the language for post-conversation summaries.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: '**Twilio call recording**: Added optional `call_recording_enabled` field
      to the [Twilio outbound call](https://elevenlabs.io/docs/api-reference/twilio/outbound-call)
      request body to enable recording of outbound calls.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: '**WhatsApp messaging flag**: Added `enable_messaging` flag to WhatsApp
      account models and update requests to control whether messaging is enabled for
      a given phone number.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-03-02-2026-03-02-97fa6f5d
  source_type: elevenlabs_changelog
  theme: interface-experience
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Replit/2026-02-27-system-theme-support|System theme support]]'
- '[[Changes/Claude Code/2026-02-28-added-always-copy-full-response-option-to-the-copy-picker-when-selected-future-c|Added
  "Always copy full response" option to the /copy picker]]'
- '[[Changes/Open WebUI/2026-03-01-4-interface-experience-changes-in-v0-8-6|4 Interface
  Experience changes in v0.8.6]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-03-02-2026-03-02-97fa6f5d|elevenlabs-2026-03-02-2026-03-02-97fa6f5d]]'
source_type: elevenlabs_changelog
theme: interface-experience
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-03-02 · [[Themes/interface-experience|Interface Experience]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/3/2) · from [[Releases/ElevenLabs/elevenlabs-2026-03-02-2026-03-02-97fa6f5d|ElevenLabs updates — 2026-03-02]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **New widget configuration options**: Several new settings are now available for the ElevenAgents conversation widget in the agent dashboard:
>
> **Collapsible widget** (`widget.dismissible`): Allow users to minimize or dismiss the widget during a conversation.
>
> **Action indicator** (`widget.show_agent_status`): Display a visual indicator when the agent is actively using tools, with distinct states for working, done, and error. Enabling this setting automatically adds `agent_tool_request` and `agent_tool_response` to the agent's client events.
>
> **Conversation ID display** (`widget.show_conversation_id`): Show the conversation ID to users after a call ends. Defaults to `true` for both new and existing agents.
>
> **Audio tag visibility** (`widget.strip_audio_tags`): Hide audio tags from conversation transcripts. Defaults to `true` for both new and existing agents.
>
> **Syntax highlighting theme** (`widget.syntax_highlight_theme`): Configure code block highlighting in transcripts. Accepts `null` (Auto), `light`, or `dark`.
>
> **Folder-aware agent testing**: The [List agent tests](https://elevenlabs.io/docs/api-reference/tests/list) endpoint now supports organizing tests into folders. Added `parent_folder_id`, `include_folders`, and `sort_mode` query parameters for filtered listing. Test creation and update endpoints accept `parent_folder_id` to assign tests to folders, and test summaries now include entity type, parent folder path, and children count.
>
> **Workflow `say` node**: Added a new `say` node type to agent workflows (`WorkflowSayNodeModel`). This node supports `conversation_config`, `additional_prompt`, and tool and knowledge base overrides. The node's message payload uses a discriminated union with two variants: `literal` (static text via `text`) and `prompt` (LLM-generated via `prompt`).
>
> **SMB tool configuration**: Formalized the `SMBToolConfig` schema with a required, discriminated `params` object. Supported operation types are `create`, `list`, `search`, `update`, and `delete`, each applicable to SMB entity categories including clients, staff, services, products, and assets.
>
> **Summary language for agents**: Added `summary_language` field to agent configuration to specify the language for post-conversation summaries.
>
> **Twilio call recording**: Added optional `call_recording_enabled` field to the [Twilio outbound call](https://elevenlabs.io/docs/api-reference/twilio/outbound-call) request body to enable recording of outbound calls.
>
> **WhatsApp messaging flag**: Added `enable_messaging` flag to WhatsApp account models and update requests to control whether messaging is enabled for a given phone number.
>
> Source: https://elevenlabs.io/docs/changelog/2026/3/2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-03-02-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-03-02-javascript-sdk|JavaScript SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-02-python-sdk|Python SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-02-audio-native|Audio Native]] · Voice and Audio
- [[Changes/ElevenLabs/2026-03-02-new-schemas|New Schemas]] · Agent Mode
- [[Changes/ElevenLabs/2026-03-02-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-02-elevenagents-bb56b9|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-03-02-voices-cb334d|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-03-02-music|Music]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-03-01 · Open WebUI · [[Changes/Open WebUI/2026-03-01-4-interface-experience-changes-in-v0-8-6|4 Interface Experience changes in v0.8.6]]
- Later: 2026-03-02 · Open WebUI · [[Changes/Open WebUI/2026-03-02-chat-history-pagination-fixed-an-issue-where-older-messages-in-long-chats-were-n|📜 Chat history pagination. Fixed an issue where older messages in long chats…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-03-02-247dfc&body=Card%3A%20Changes%2FElevenLabs%2F2026-03-02-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-03-02-247dfc%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F3%2F2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->