---
card_id: elevenlabs-2025-09-29-7144f6
date: '2025-09-29'
description: 'ElevenLabs · 2025-09-29 · Agent Mode: **POST /v1/convai/agents/create**:
  Added `ignore_default_personality` boolean parameter to control whether agents should…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 816
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 8a45dca758e2d43d0e4ecde17d483f949da0ebf6f675d3e579e7537ba9d5644c
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2025-09-29-7144f6
  comparison: ''
  date: '2025-09-29'
  description: 'ElevenLabs — ElevenLabs updates — 2025-09-29: **POST /v1/convai/agents/create**:
    Added `ignore_default_personality` boolean parameter to control whether agents
    should ignore the default helpful personality behavior'
  evidence:
  - quote: '**POST /v1/convai/agents/create**: Added `ignore_default_personality`
      boolean parameter to control whether agents should ignore the default helpful
      personality behavior'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**PATCH /v1/convai/agents/{agent_id}**: Added `ignore_default_personality`
      field support for agent updates'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**GET /v1/convai/agents/{agent_id}**: Response now includes `ignore_default_personality`
      field in agent configuration'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**POST /v1/convai/mcp-servers**: Added interrupt control configuration
      parameters for disabling interruptions during tool calls'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**PATCH /v1/convai/mcp-servers/{mcp_server_id}**: Enhanced with interrupt
      control settings for MCP server configuration'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**GET /v1/convai/mcp-servers/{mcp_server_id}**: Response includes new
      interrupt control configuration fields'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**GET /v1/convai/conversations/{conversation_id}**: Response enhanced
      with alignment data fields for audio-text synchronization support'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**POST /v1/convai/agent-testing/create**: Enhanced to support workflow
      expressions functionality in agent testing'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**GET /v1/convai/agent-testing/{test_id}**: Response includes additional
      fields for workflow expression test results'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**PUT /v1/convai/agent-testing/{test_id}**: Request and response schemas
      updated for workflow expression support'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**POST /v1/convai/agents/{agent_id}/simulate-conversation**: Request schema
      updated to support workflow expressions in conversation simulation'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**POST /v1/convai/agents/{agent_id}/simulate-conversation/stream**: Streaming
      conversation simulation with workflow expression support'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**GET /v1/convai/settings**: Response includes new platform configuration
      options'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**PATCH /v1/convai/settings**: Request schema updated with new platform
      settings'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**POST /v1/convai/batch-calling/submit**: Request schema updates for batch
      calling functionality'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**PATCH /v1/convai/mcp-servers/{mcp_server_id}/approval-policy**: Response
      schema updated for approval policy management'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**POST /v1/convai/mcp-servers/{mcp_server_id}/tool-approvals**: Response
      schema enhanced for tool approval handling'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  - quote: '**DELETE /v1/convai/mcp-servers/{mcp_server_id}/tool-approvals/{tool_name}**:
      Response schema updated for tool approval removal'
    source_release: https://elevenlabs.io/docs/changelog/2025/9/29
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2025-09-29-2025-09-29-3f5c7c91
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/Cursor/2025-09-29-image-file-support-for-agent|Image file support for
  Agent]]'
- '[[Changes/Dify/2025-09-29-2-agent-mode-changes-in-1-9-1|2 Agent Mode changes in
  1.9.1]]'
- '[[Changes/ElevenLabs/2025-09-29-agents-platform|Agents Platform]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2025-09-29-2025-09-29-3f5c7c91|elevenlabs-2025-09-29-2025-09-29-3f5c7c91]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2025-09-29 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2025/9/29) · from [[Releases/ElevenLabs/elevenlabs-2025-09-29-2025-09-29-3f5c7c91|ElevenLabs updates — 2025-09-29]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **POST /v1/convai/agents/create**: Added `ignore_default_personality` boolean parameter to control whether agents should ignore the default helpful personality behavior
>
> **PATCH /v1/convai/agents/{agent_id}**: Added `ignore_default_personality` field support for agent updates
>
> **GET /v1/convai/agents/{agent_id}**: Response now includes `ignore_default_personality` field in agent configuration
>
> **POST /v1/convai/mcp-servers**: Added interrupt control configuration parameters for disabling interruptions during tool calls
>
> **PATCH /v1/convai/mcp-servers/{mcp_server_id}**: Enhanced with interrupt control settings for MCP server configuration
>
> **GET /v1/convai/mcp-servers/{mcp_server_id}**: Response includes new interrupt control configuration fields
>
> **GET /v1/convai/conversations/{conversation_id}**: Response enhanced with alignment data fields for audio-text synchronization support
>
> **POST /v1/convai/agent-testing/create**: Enhanced to support workflow expressions functionality in agent testing
>
> **GET /v1/convai/agent-testing/{test_id}**: Response includes additional fields for workflow expression test results
>
> **PUT /v1/convai/agent-testing/{test_id}**: Request and response schemas updated for workflow expression support
>
> **POST /v1/convai/agents/{agent_id}/simulate-conversation**: Request schema updated to support workflow expressions in conversation simulation
>
> **POST /v1/convai/agents/{agent_id}/simulate-conversation/stream**: Streaming conversation simulation with workflow expression support
>
> **GET /v1/convai/settings**: Response includes new platform configuration options
>
> **PATCH /v1/convai/settings**: Request schema updated with new platform settings
>
> **POST /v1/convai/batch-calling/submit**: Request schema updates for batch calling functionality
>
> **PATCH /v1/convai/mcp-servers/{mcp_server_id}/approval-policy**: Response schema updated for approval policy management
>
> **POST /v1/convai/mcp-servers/{mcp_server_id}/tool-approvals**: Response schema enhanced for tool approval handling
>
> **DELETE /v1/convai/mcp-servers/{mcp_server_id}/tool-approvals/{tool_name}**: Response schema updated for tool approval removal
>
> Source: https://elevenlabs.io/docs/changelog/2025/9/29
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2025-09-29-javascript-sdk|JavaScript SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2025-09-29-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2025-09-29-agents-platform|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2025-09-29-packages|Packages]] · Apps and Integrations
- [[Changes/ElevenLabs/2025-09-29-v1-tts-model-deprecation|v1 TTS model deprecation]] · Model Support
- [[Changes/ElevenLabs/2025-09-29-voice-management|Voice Management]] · Voice and Audio
- [[Changes/ElevenLabs/2025-09-29-text-to-speech|Text to Speech]] · Voice and Audio
- [[Changes/ElevenLabs/2025-09-29-speech-to-text-ac08d0|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2025-09-29-sdk-releases|SDK Releases]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2025-09-29 · Dify · [[Changes/Dify/2025-09-29-2-agent-mode-changes-in-1-9-1|2 Agent Mode changes in 1.9.1]]
- Later: 2025-10-01 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-10-01-improved-the-experience-of-writing-prompts-while-the-agent-is-running-up-down-ar|Improved the experience of writing prompts while the agent is running -- up/down…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2025-09-29-7144f6&body=Card%3A%20Changes%2FElevenLabs%2F2025-09-29-agents-platform-7144f6.md%0ACard%20ID%3A%20elevenlabs-2025-09-29-7144f6%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2025%2F9%2F29%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->