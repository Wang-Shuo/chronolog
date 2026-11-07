---
card_id: elevenlabs-2026-03-02-bb56b9
date: '2026-03-02'
description: 'ElevenLabs · 2026-03-02 · Agent Mode: [List agent tests](https://elevenlabs.io/docs/api-reference/tests/list)'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 970
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: f99ed0a0d1ac453e70a9cdc20d62a23c76bb80c120fd4bfbd0b894a4b52a6617
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-03-02-bb56b9
  comparison: ''
  confidence: low
  date: '2026-03-02'
  description: 'ElevenLabs — ElevenLabs updates — 2026-03-02: [List agent tests](https://elevenlabs.io/docs/api-reference/tests/list)'
  evidence:
  - quote: '[List agent tests](https://elevenlabs.io/docs/api-reference/tests/list)'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: Added `parent_folder_id` query parameter (string, optional) to filter tests
      by folder
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: Added `include_folders` query parameter (boolean, optional) to include
      folder objects in results
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: Added `sort_mode` query parameter (string, optional) to control result
      ordering
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: 'Response now includes folder metadata: entity type, parent path, and children
      count on `UnitTestSummaryResponseModel`'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: '[Create agent test](https://elevenlabs.io/docs/api-reference/tests/create),
      [Update agent test](https://elevenlabs.io/docs/api-reference/tests/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: Added `parent_folder_id` field (string, optional) for assigning a test
      to a folder
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Update agent](https://elevenlabs.io/docs/api-reference/agents/update), [Get
      agent](https://elevenlabs.io/docs/api-reference/agents/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: Added `summary_language` field (string, optional) to agent configuration
      for post-conversation summary language
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: Added `widget.dismissible` (boolean) - allow users to collapse or dismiss
      the widget
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: Added `widget.show_agent_status` (boolean) - display tool usage status
      indicator in widget
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: Added `widget.show_conversation_id` (boolean) - show conversation ID after
      call ends; defaults to `true`
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: Added `widget.strip_audio_tags` (boolean) - hide audio tags from transcripts;
      defaults to `true`
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: Added `widget.syntax_highlight_theme` (string, nullable) - code block highlighting
      theme (`null`, `light`, or `dark`)
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: Added new workflow node type `say` with `WorkflowSayNodeModel` schema,
      including `conversation_config`, `additional_prompt`, and tool/knowledge base
      overrides; message payload supports `literal` and `prompt` discriminated variants
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: '[Twilio outbound call](https://elevenlabs.io/docs/api-reference/twilio/outbound-call)'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: Added `call_recording_enabled` field (boolean, optional) to enable recording
      of outbound Twilio calls
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: '[Update WhatsApp account](https://elevenlabs.io/docs/api-reference/whats-app/accounts/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: Added `enable_messaging` field (boolean, optional) to enable or disable
      messaging for the account
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: '[Update webhook](https://elevenlabs.io/docs/api-reference/webhooks/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  - quote: Added `schema_overrides` field (object, optional) for customizing webhook
      payload schema
    source_release: https://elevenlabs.io/docs/changelog/2026/3/2
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-03-02-2026-03-02-97fa6f5d
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-03-02-you-can-now-fork-a-thread-into-sub-agents-making-it-easier-to-branch-work-withou|Fork
  a thread into sub-agents, making it easier to branch work without leaving…]]'
- '[[Changes/Codex CLI/2026-03-02-2-agent-mode-changes-in-rust-v0-107-0|2 Agent Mode
  changes in rust-v0.107.0]]'
- '[[Changes/ElevenLabs/2026-03-02-new-schemas|New Schemas]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-03-02-2026-03-02-97fa6f5d|elevenlabs-2026-03-02-2026-03-02-97fa6f5d]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-03-02 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/3/2) · from [[Releases/ElevenLabs/elevenlabs-2026-03-02-2026-03-02-97fa6f5d|ElevenLabs updates — 2026-03-02]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [List agent tests](https://elevenlabs.io/docs/api-reference/tests/list)
>
> Added `parent_folder_id` query parameter (string, optional) to filter tests by folder
>
> Added `include_folders` query parameter (boolean, optional) to include folder objects in results
>
> Added `sort_mode` query parameter (string, optional) to control result ordering
>
> Response now includes folder metadata: entity type, parent path, and children count on `UnitTestSummaryResponseModel`
>
> [Create agent test](https://elevenlabs.io/docs/api-reference/tests/create), [Update agent test](https://elevenlabs.io/docs/api-reference/tests/update)
>
> Added `parent_folder_id` field (string, optional) for assigning a test to a folder
>
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get)
>
> Added `summary_language` field (string, optional) to agent configuration for post-conversation summary language
>
> Added `widget.dismissible` (boolean) - allow users to collapse or dismiss the widget
>
> Added `widget.show_agent_status` (boolean) - display tool usage status indicator in widget
>
> Added `widget.show_conversation_id` (boolean) - show conversation ID after call ends; defaults to `true`
>
> Added `widget.strip_audio_tags` (boolean) - hide audio tags from transcripts; defaults to `true`
>
> Added `widget.syntax_highlight_theme` (string, nullable) - code block highlighting theme (`null`, `light`, or `dark`)
>
> Added new workflow node type `say` with `WorkflowSayNodeModel` schema, including `conversation_config`, `additional_prompt`, and tool/knowledge base overrides; message payload supports `literal` and `prompt` discriminated variants
>
> [Twilio outbound call](https://elevenlabs.io/docs/api-reference/twilio/outbound-call)
>
> Added `call_recording_enabled` field (boolean, optional) to enable recording of outbound Twilio calls
>
> [Update WhatsApp account](https://elevenlabs.io/docs/api-reference/whats-app/accounts/update)
>
> Added `enable_messaging` field (boolean, optional) to enable or disable messaging for the account
>
> [Update webhook](https://elevenlabs.io/docs/api-reference/webhooks/update)
>
> Added `schema_overrides` field (object, optional) for customizing webhook payload schema
>
> Source: https://elevenlabs.io/docs/changelog/2026/3/2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-03-02-elevenagents|ElevenAgents]] · Interface Experience
- [[Changes/ElevenLabs/2026-03-02-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-03-02-javascript-sdk|JavaScript SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-02-python-sdk|Python SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-02-audio-native|Audio Native]] · Voice and Audio
- [[Changes/ElevenLabs/2026-03-02-new-schemas|New Schemas]] · Agent Mode
- [[Changes/ElevenLabs/2026-03-02-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-02-voices-cb334d|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-03-02-music|Music]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-03-02 · Codex CLI · [[Changes/Codex CLI/2026-03-02-2-agent-mode-changes-in-rust-v0-107-0|2 Agent Mode changes in rust-v0.107.0]]
- Later: 2026-03-03 · Cline · [[Changes/Cline/2026-03-03-add-user-agent-header-to-requests-sent-to-the-cline-backend|Add User-Agent header to requests sent to the Cline backend]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-03-02-bb56b9&body=Card%3A%20Changes%2FElevenLabs%2F2026-03-02-elevenagents-bb56b9.md%0ACard%20ID%3A%20elevenlabs-2026-03-02-bb56b9%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F3%2F2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->