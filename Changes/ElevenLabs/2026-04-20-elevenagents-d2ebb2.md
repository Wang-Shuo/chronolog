---
card_id: elevenlabs-2026-04-20-d2ebb2
date: '2026-04-20'
description: 'ElevenLabs · 2026-04-20 · Memory and Personalization: **Workflow starting
  node override**: Conversations can now be started at a specific workflow node by…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1005
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: b017925eea6e0626870ab1f136628b65dc76a550f38c584f5d470f26da114d64
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-04-20-d2ebb2
  comparison: ''
  confidence: low
  date: '2026-04-20'
  description: 'ElevenLabs — ElevenLabs updates — 2026-04-20: **Workflow starting
    node override**: Conversations can now be started at a specific workflow node
    by passing `starting_workflow_node_id` in the [conversation initiation client
    data](https://elevenlabs.io/docs/api-reference/agents/create). This is gated by
    an opt-in `enable_starting_workflow_node_id_from_client` field in the agent''s
    platform override settings. When enabled, clients can specify which node to begin
    a conversation at, which is useful for agent memory and longer-term WebSocket
    use cases. If the specified node does not exist, the conversation falls back to
    the default entry point.'
  evidence:
  - quote: '**Workflow starting node override**: Conversations can now be started
      at a specific workflow node by passing `starting_workflow_node_id` in the [conversation
      initiation client data](https://elevenlabs.io/docs/api-reference/agents/create).
      This is gated by an opt-in `enable_starting_workflow_node_id_from_client` field
      in the agent''s platform override settings. When enabled, clients can specify
      which node to begin a conversation at, which is useful for agent memory and
      longer-term WebSocket use cases. If the specified node does not exist, the conversation
      falls back to the default entry point.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: '**Post-call analysis LLM configuration**: Agent platform settings now
      include an `analysis_llm` field (default: `gemini-2.5-flash`) that sets the
      default LLM for post-call analysis, including evaluation criteria and data collection.
      Individual data collection properties can override this default with a per-item
      `llm` field via the new `AnalysisProperty` schema, giving fine-grained control
      over which model processes each analysis item.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: '**New LLM options**: Added `gpt-5.4` to the list of available LLM providers
      for agent configuration. Added `xhigh` to the `LLMReasoningEffort` enum for
      extended reasoning on supported models.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: '**Null literal in workflow expressions**: Workflow conditional expressions
      now support null comparisons via the new `ASTNullNode` type, enabling branches
      like "if variable is null" in workflow logic.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: '**Get secret by ID**: A new [get secret](https://elevenlabs.io/docs/api-reference/workspace/secrets/get)
      endpoint (`GET /v1/convai/secrets/{secret_id}`) retrieves a single workspace
      secret by its ID. The [list secrets](https://elevenlabs.io/docs/api-reference/workspace/secrets/list)
      endpoint also now accepts a `search` query parameter to filter secrets by name
      prefix.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  - quote: '**Searchable phone numbers in batch calling**: The batch calling form
      in the dashboard now includes a searchable phone number selector, making it
      easier to find the right outbound number when configuring batch calls.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/20
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-04-20-2026-04-20-9278926e
  source_type: elevenlabs_changelog
  theme: memory
  theme_matches:
  - matched_terms:
    - memory
    score: 110
    theme: memory
  - matched_terms:
    - agent
    - agents
    score: 100
    theme: agent-mode
  theme_resolution: manual-semantic-rule-v1
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-04-16-custom-instructions-and-skills-refresh-from-disk-after-clear-or-new|Custom
  instructions and skills refresh from disk after /clear or /new]]'
- '[[Changes/OpenCode/2026-04-16-core-the-bash-tool-uses-less-memory-on-large-command-output|Core
  The bash tool uses less memory on large command output]]'
- '[[Changes/Codex CLI/2026-04-20-4-memory-and-personalization-changes-in-rust-v0-122-0|4
  Memory and Personalization changes in rust-v0.122.0]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-04-20-2026-04-20-9278926e|elevenlabs-2026-04-20-2026-04-20-9278926e]]'
source_type: elevenlabs_changelog
theme: memory
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-04-20 · [[Themes/memory|Memory and Personalization]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/4/20) · from [[Releases/ElevenLabs/elevenlabs-2026-04-20-2026-04-20-9278926e|ElevenLabs updates — 2026-04-20]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Workflow starting node override**: Conversations can now be started at a specific workflow node by passing `starting_workflow_node_id` in the [conversation initiation client data](https://elevenlabs.io/docs/api-reference/agents/create). This is gated by an opt-in `enable_starting_workflow_node_id_from_client` field in the agent's platform override settings. When enabled, clients can specify which node to begin a conversation at, which is useful for agent memory and longer-term WebSocket use cases. If the specified node does not exist, the conversation falls back to the default entry point.
>
> **Post-call analysis LLM configuration**: Agent platform settings now include an `analysis_llm` field (default: `gemini-2.5-flash`) that sets the default LLM for post-call analysis, including evaluation criteria and data collection. Individual data collection properties can override this default with a per-item `llm` field via the new `AnalysisProperty` schema, giving fine-grained control over which model processes each analysis item.
>
> **New LLM options**: Added `gpt-5.4` to the list of available LLM providers for agent configuration. Added `xhigh` to the `LLMReasoningEffort` enum for extended reasoning on supported models.
>
> **Null literal in workflow expressions**: Workflow conditional expressions now support null comparisons via the new `ASTNullNode` type, enabling branches like "if variable is null" in workflow logic.
>
> **Get secret by ID**: A new [get secret](https://elevenlabs.io/docs/api-reference/workspace/secrets/get) endpoint (`GET /v1/convai/secrets/{secret_id}`) retrieves a single workspace secret by its ID. The [list secrets](https://elevenlabs.io/docs/api-reference/workspace/secrets/list) endpoint also now accepts a `search` query parameter to filter secrets by name prefix.
>
> **Searchable phone numbers in batch calling**: The batch calling form in the dashboard now includes a searchable phone number selector, making it easier to find the right outbound number when configuring batch calls.
>
> Source: https://elevenlabs.io/docs/changelog/2026/4/20
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-04-20-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-20-text-to-dialogue|Text to Dialogue]] · Files and Data
- [[Changes/ElevenLabs/2026-04-20-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-04-20-workspaces|Workspaces]] · Pricing Model
- [[Changes/ElevenLabs/2026-04-20-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-04-20-speech-to-text-c85018|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-20-other|Other]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-04-20 · Codex CLI · [[Changes/Codex CLI/2026-04-20-4-memory-and-personalization-changes-in-rust-v0-122-0|4 Memory and Personalization changes in rust-v0.122.0]]
- Later: 2026-04-21 · Open WebUI · [[Changes/Open WebUI/2026-04-21-7-memory-and-personalization-changes-in-v0-9-0|7 Memory and Personalization changes in v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-04-20-d2ebb2&body=Card%3A%20Changes%2FElevenLabs%2F2026-04-20-elevenagents-d2ebb2.md%0ACard%20ID%3A%20elevenlabs-2026-04-20-d2ebb2%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F4%2F20%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->