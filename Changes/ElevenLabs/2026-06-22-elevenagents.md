---
card_id: elevenlabs-2026-06-22-21166f
date: '2026-06-22'
description: 'ElevenLabs · 2026-06-22 · Agent Mode: **Branch rebase**: Added `POST
  /v1/convai/agents/{agent_id}/branches/{branch_id}/rebase` to rebase a branch onto
  the…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1082
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 7397d4045e9e22ccc1eae04e30a20a327a8e5dd491ac66cf084b85741c52f381
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-06-22-21166f
  comparison: ''
  confidence: low
  date: '2026-06-22'
  description: 'ElevenLabs — ElevenLabs updates — 2026-06-22: **Branch rebase**: Added
    `POST /v1/convai/agents/{agent_id}/branches/{branch_id}/rebase` to rebase a branch
    onto the latest main while preserving branch-specific changes. Agent version parent
    models add optional `rebased_from_version_id` (string) to track the source version
    after a rebase.'
  evidence:
  - quote: '**Branch rebase**: Added `POST /v1/convai/agents/{agent_id}/branches/{branch_id}/rebase`
      to rebase a branch onto the latest main while preserving branch-specific changes.
      Agent version parent models add optional `rebased_from_version_id` (string)
      to track the source version after a rebase.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/22
  - quote: '**Conversation product filtering**: [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
      and [Text search conversation messages](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search)
      add optional `conversation_product_type` query parameter (`agents` | `speech_engine`)
      to filter results by product. Conversation models introduce `ConversationProduct`
      for this distinction.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/22
  - quote: '**Conversation termination filtering**: [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
      adds optional `termination_reasons` query parameter (array of strings) to filter
      conversations by how they ended.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/22
  - quote: '**Per-agent topic discovery**: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create)
      and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update) platform
      settings add optional `topic_discovery` (`TopicDiscoverySettings`) for per-agent
      topic discovery configuration.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/22
  - quote: '**Background sound configuration**: Agent platform and conversation configuration
      models add optional `background_sound` (`BackgroundSoundConfig`) for ambient
      audio during conversations.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/22
  - quote: '**Turn interruption ignore terms**: Turn configuration schemas add optional
      `interruption_ignore_terms` (array of strings) to suppress turn detection on
      specific phrases.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/22
  - quote: '**Soft timeout filler randomization**: Soft timeout configuration adds
      optional `randomize_fillers` (boolean) to shuffle filler messages across soft
      timeouts. Soft timeout message and LLM prompt override fields now support dynamic
      variables.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/22
  - quote: '**Transcript user identifiers**: Transcript message models add optional
      `user_identifier` (string) on user-authored messages.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/22
  - quote: '**Simulation success conditions**: Agent simulation test schemas add optional
      `success_conditions` (array, up to 30 items). The legacy `success_condition`
      field is deprecated in favor of the array form.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/22
  - quote: '**Agent test repeat limit**: [Run tests on the agent](https://elevenlabs.io/docs/api-reference/tests/run-tests)
      raises the maximum `repeat_count` from 20 to 50.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/22
  - quote: '**Tool schema dynamic allowed values**: ElevenAgents tool JSON schema
      properties add optional `allowed_values_dynamic_variable` (string) for server-verified
      LLM value picks sourced from dynamic variables.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/22
  - quote: '**Widget signed URL docs**: [Get widget](https://elevenlabs.io/docs/api-reference/widget/get)
      updates `conversation_signature` documentation to reference `/v1/convai/conversation/get_signed_url`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/22
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-06-22-2026-06-22-645b32b5
  source_type: elevenlabs_changelog
  theme: agent-mode
  theme_matches:
  - matched_terms:
    - agent
    - agents
    score: 100
    theme: agent-mode
  - matched_terms:
    - models
    score: 50
    theme: model-support
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/OpenCode/2026-06-21-core-honor-configured-agent-step-limits-by-forcing-a-final-text-response-instead|Core
  Honor configured agent step limits by forcing a final text response instead…]]'
- '[[Changes/Claude Code/2026-06-22-2-agent-mode-changes-in-v2-1-186|2 Agent Mode
  changes in v2.1.186]]'
- '[[Changes/Codex CLI/2026-06-22-14-agent-mode-changes-in-rust-v0-142-0|14 Agent
  Mode changes in rust-v0.142.0]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-06-22-2026-06-22-645b32b5|elevenlabs-2026-06-22-2026-06-22-645b32b5]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-06-22 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/6/22) · from [[Releases/ElevenLabs/elevenlabs-2026-06-22-2026-06-22-645b32b5|ElevenLabs updates — 2026-06-22]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Branch rebase**: Added `POST /v1/convai/agents/{agent_id}/branches/{branch_id}/rebase` to rebase a branch onto the latest main while preserving branch-specific changes. Agent version parent models add optional `rebased_from_version_id` (string) to track the source version after a rebase.
>
> **Conversation product filtering**: [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list) and [Text search conversation messages](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search) add optional `conversation_product_type` query parameter (`agents` | `speech_engine`) to filter results by product. Conversation models introduce `ConversationProduct` for this distinction.
>
> **Conversation termination filtering**: [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list) adds optional `termination_reasons` query parameter (array of strings) to filter conversations by how they ended.
>
> **Per-agent topic discovery**: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create) and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update) platform settings add optional `topic_discovery` (`TopicDiscoverySettings`) for per-agent topic discovery configuration.
>
> **Background sound configuration**: Agent platform and conversation configuration models add optional `background_sound` (`BackgroundSoundConfig`) for ambient audio during conversations.
>
> **Turn interruption ignore terms**: Turn configuration schemas add optional `interruption_ignore_terms` (array of strings) to suppress turn detection on specific phrases.
>
> **Soft timeout filler randomization**: Soft timeout configuration adds optional `randomize_fillers` (boolean) to shuffle filler messages across soft timeouts. Soft timeout message and LLM prompt override fields now support dynamic variables.
>
> **Transcript user identifiers**: Transcript message models add optional `user_identifier` (string) on user-authored messages.
>
> **Simulation success conditions**: Agent simulation test schemas add optional `success_conditions` (array, up to 30 items). The legacy `success_condition` field is deprecated in favor of the array form.
>
> **Agent test repeat limit**: [Run tests on the agent](https://elevenlabs.io/docs/api-reference/tests/run-tests) raises the maximum `repeat_count` from 20 to 50.
>
> **Tool schema dynamic allowed values**: ElevenAgents tool JSON schema properties add optional `allowed_values_dynamic_variable` (string) for server-verified LLM value picks sourced from dynamic variables.
>
> **Widget signed URL docs**: [Get widget](https://elevenlabs.io/docs/api-reference/widget/get) updates `conversation_signature` documentation to reference `/v1/convai/conversation/get_signed_url`.
>
> Source: https://elevenlabs.io/docs/changelog/2026/6/22
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-06-22-python-sdk|Python SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-06-22-workspaces|Workspaces]] · Model Support
- [[Changes/ElevenLabs/2026-06-22-music|Music]] · Model Support
- [[Changes/ElevenLabs/2026-06-22-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-06-22-mcp-server|MCP Server]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-06-22-dubbing|Dubbing]] · Model Support
- [[Changes/ElevenLabs/2026-06-22-javascript-sdk|JavaScript SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-06-22-elevenagents-c51c4d|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-06-22-elevenagents-ee09f3|ElevenAgents]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-06-22 · Codex CLI · [[Changes/Codex CLI/2026-06-22-14-agent-mode-changes-in-rust-v0-142-0|14 Agent Mode changes in rust-v0.142.0]]
- Later: 2026-06-22 · Google Antigravity · [[Changes/Google Antigravity/2026-06-22-new-entries-in-the-sensitive-paths-list-vscode-and-cache-are-now-recognized-as-s|New entries in the sensitive paths list]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-06-22-21166f&body=Card%3A%20Changes%2FElevenLabs%2F2026-06-22-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-06-22-21166f%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F6%2F22%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->