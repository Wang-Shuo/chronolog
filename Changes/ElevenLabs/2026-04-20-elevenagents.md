---
card_id: elevenlabs-2026-04-20-c7553f
date: '2026-04-20'
description: 'ElevenLabs · 2026-04-20 · Agent Mode: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
  [Get…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1019
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 63eaed3d39bdaecd7bb42c44e4805833fc1847544b63501796941a6cfdb76397
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-04-20-c7553f
  comparison: ''
  confidence: low
  date: '2026-04-20'
  description: 'ElevenLabs — ElevenLabs updates — 2026-04-20: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
    [Get agent](https://elevenlabs.io/docs/api-reference/agents/get), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
  evidence:
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Get agent](https://elevenlabs.io/docs/api-reference/agents/get), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: 'Added `analysis_llm` field (LLM enum, default: `gemini-2.5-flash`) to
      `AgentPlatformSettings` for configuring the default post-call analysis model'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: Data collection properties now use the `AnalysisProperty` schema with an
      optional per-item `llm` override field
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: '[Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: Added `starting_workflow_node_id` field (string, nullable) to conversation
      initiation client data
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: Added `enable_starting_workflow_node_id_from_client` field (boolean, default
      `false`) to `ConversationInitiationClientDataConfig`
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: '[Submit batch calling](https://elevenlabs.io/docs/api-reference/batch-calling/create)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: Added `external_link` field (string, nullable) to batch call records
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: '[List secrets](https://elevenlabs.io/docs/api-reference/workspace/secrets/list)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: Added optional `search` query parameter (string) for filtering secrets
      by name prefix
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: Added `gpt-5.4`, `gpt-5.4-2026-03-05`
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: '`LLMReasoningEffort` enum'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: Added `xhigh`
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: Workflow expressions (`ASTNode`)
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: Added `null_literal` discriminator value and `ASTNullNode` schema for null
      comparisons
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: Array tool parameters (`ArrayJsonSchemaProperty`)
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: Added `dynamic_variable` field (string, optional) for populating arrays
      from dynamic variables at runtime
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: Added `constant_value` field (array, nullable) for setting constant array
      values
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: '`items` field is no longer required (has a default schema)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: MCP tool config overrides
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: Response now uses `MCPToolConfigOverride-Output` schema (input/output split)
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-04-20-2026-04-20-9278926e
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Replit/2026-04-17-replit-agent-on-google-cloud-marketplace|Replit Agent
  on Google Cloud Marketplace]]'
- '[[Changes/Claude Code/2026-04-20-2-agent-mode-changes-in-v2-1-116|2 Agent Mode
  changes in v2.1.116]]'
- '[[Changes/Codex CLI/2026-04-20-10-agent-mode-changes-in-rust-v0-122-0|10 Agent
  Mode changes in rust-v0.122.0]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-04-20-2026-04-20-9278926e|elevenlabs-2026-04-20-2026-04-20-9278926e]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-04-20 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/4/20) · from [[Releases/ElevenLabs/elevenlabs-2026-04-20-2026-04-20-9278926e|ElevenLabs updates — 2026-04-20]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
>
> Added `analysis_llm` field (LLM enum, default: `gemini-2.5-flash`) to `AgentPlatformSettings` for configuring the default post-call analysis model
>
> Data collection properties now use the `AnalysisProperty` schema with an optional per-item `llm` override field
>
> [Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation)
>
> Added `starting_workflow_node_id` field (string, nullable) to conversation initiation client data
>
> Added `enable_starting_workflow_node_id_from_client` field (boolean, default `false`) to `ConversationInitiationClientDataConfig`
>
> [Submit batch calling](https://elevenlabs.io/docs/api-reference/batch-calling/create)
>
> Added `external_link` field (string, nullable) to batch call records
>
> [List secrets](https://elevenlabs.io/docs/api-reference/workspace/secrets/list)
>
> Added optional `search` query parameter (string) for filtering secrets by name prefix
>
> Added `gpt-5.4`, `gpt-5.4-2026-03-05`
>
> `LLMReasoningEffort` enum
>
> Added `xhigh`
>
> Workflow expressions (`ASTNode`)
>
> Added `null_literal` discriminator value and `ASTNullNode` schema for null comparisons
>
> Array tool parameters (`ArrayJsonSchemaProperty`)
>
> Added `dynamic_variable` field (string, optional) for populating arrays from dynamic variables at runtime
>
> Added `constant_value` field (array, nullable) for setting constant array values
>
> `items` field is no longer required (has a default schema)
>
> MCP tool config overrides
>
> Response now uses `MCPToolConfigOverride-Output` schema (input/output split)
>
> Source: https://elevenlabs.io/docs/changelog/2026/4/20
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-04-20-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-20-text-to-dialogue|Text to Dialogue]] · Files and Data
- [[Changes/ElevenLabs/2026-04-20-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-04-20-workspaces|Workspaces]] · Pricing Model
- [[Changes/ElevenLabs/2026-04-20-speech-to-text-c85018|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-20-elevenagents-d2ebb2|ElevenAgents]] · Memory and Personalization
- [[Changes/ElevenLabs/2026-04-20-other|Other]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-20 · Codex CLI · [[Changes/Codex CLI/2026-04-20-10-agent-mode-changes-in-rust-v0-122-0|10 Agent Mode changes in rust-v0.122.0]]
- Later: 2026-04-20 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-20-2-agent-mode-changes-in-v1-0-33|2 Agent Mode changes in v1.0.33]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-04-20-c7553f&body=Card%3A%20Changes%2FElevenLabs%2F2026-04-20-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-04-20-c7553f%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F4%2F20%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->