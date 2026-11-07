---
card_id: elevenlabs-2026-04-07-e46dc6
date: '2026-04-07'
description: 'ElevenLabs · 2026-04-07 · Agent Mode: **Scoped conversation analysis**:
  Evaluation criteria and data collection items can now be scoped to `conversation`
  (full…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1006
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 9d9f9a47bfab779eea1350c0b77e857441cf480238dcf8f6606f2a3ab633c32f
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-04-07-e46dc6
  comparison: ''
  confidence: low
  date: '2026-04-07'
  description: 'ElevenLabs — ElevenLabs updates — 2026-04-07: **Scoped conversation
    analysis**: Evaluation criteria and data collection items can now be scoped to
    `conversation` (full transcript) or `agent` (only the portion where a specific
    agent was active). Added `scope` field to `PromptEvaluationCriteria`, `data_collection_scopes`
    to [agent platform settings](https://elevenlabs.io/docs/eleven-agents/customization/agent-analysis),
    and a new `scoped` array of `ScopedAnalysisResult` on the [conversation analysis](https://elevenlabs.io/docs/api-reference/conversations/analysis/run-analysis)
    response. This is particularly useful for multi-agent workflows where each agent
    should be evaluated independently.'
  evidence:
  - quote: '**Scoped conversation analysis**: Evaluation criteria and data collection
      items can now be scoped to `conversation` (full transcript) or `agent` (only
      the portion where a specific agent was active). Added `scope` field to `PromptEvaluationCriteria`,
      `data_collection_scopes` to [agent platform settings](https://elevenlabs.io/docs/eleven-agents/customization/agent-analysis),
      and a new `scoped` array of `ScopedAnalysisResult` on the [conversation analysis](https://elevenlabs.io/docs/api-reference/conversations/analysis/run-analysis)
      response. This is particularly useful for multi-agent workflows where each agent
      should be evaluated independently.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: '**Agent test folder management**: Tests can now be organized into folders.
      New endpoints for [creating](https://elevenlabs.io/docs/api-reference/tests/test-folders/create),
      [retrieving](https://elevenlabs.io/docs/api-reference/tests/test-folders/get),
      [updating](https://elevenlabs.io/docs/api-reference/tests/test-folders/update),
      and [deleting](https://elevenlabs.io/docs/api-reference/tests/test-folders/delete)
      test folders, plus [bulk moving](https://elevenlabs.io/docs/api-reference/tests/test-folders/move)
      tests between folders.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: '**Tool and knowledge base overrides in workflows**: Agent workflow node
      overrides now support `tool_ids` and `knowledge_base` fields in `PromptAgentAPIModelOverrideConfig`,
      allowing workflow nodes to control which tools and knowledge base documents
      each sub-agent can access.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: '**Response filter `hide_all` mode**: Added `hide_all` option to `ResponseFilterMode`,
      forcing the system to hide all fields of a tool response from the agent.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: '**Visited agents in conversation history**: The [get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)
      response now includes a `visited_agents` array of `VisitedAgentRef` objects
      (with `agent_id` and `branch_id`), tracking which agents participated in a multi-agent
      conversation.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: '**Multimodal message support in hooks**: The `useConversationControls`
      hook now exposes `sendMultimodalMessage`, and the `MultimodalMessageInput` type
      is exported from `@elevenlabs/client`, making it easier to send images and other
      multimodal content during conversations.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-04-07-2026-04-07-1ced55b5
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/HeyGen/2026-04-06-open-video-agent-type-your-prompt-and-generate-seedance-footage-will-automatical|Open
  Video Agent, type your prompt, and generate]]'
- '[[Changes/ElevenLabs/2026-04-07-new-endpoints|New Endpoints]]'
- '[[Changes/ElevenLabs/2026-04-07-elevenagents|ElevenAgents]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-04-07-2026-04-07-1ced55b5|elevenlabs-2026-04-07-2026-04-07-1ced55b5]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-04-07 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/4/7) · from [[Releases/ElevenLabs/elevenlabs-2026-04-07-2026-04-07-1ced55b5|ElevenLabs updates — 2026-04-07]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Scoped conversation analysis**: Evaluation criteria and data collection items can now be scoped to `conversation` (full transcript) or `agent` (only the portion where a specific agent was active). Added `scope` field to `PromptEvaluationCriteria`, `data_collection_scopes` to [agent platform settings](https://elevenlabs.io/docs/eleven-agents/customization/agent-analysis), and a new `scoped` array of `ScopedAnalysisResult` on the [conversation analysis](https://elevenlabs.io/docs/api-reference/conversations/analysis/run-analysis) response. This is particularly useful for multi-agent workflows where each agent should be evaluated independently.
>
> **Agent test folder management**: Tests can now be organized into folders. New endpoints for [creating](https://elevenlabs.io/docs/api-reference/tests/test-folders/create), [retrieving](https://elevenlabs.io/docs/api-reference/tests/test-folders/get), [updating](https://elevenlabs.io/docs/api-reference/tests/test-folders/update), and [deleting](https://elevenlabs.io/docs/api-reference/tests/test-folders/delete) test folders, plus [bulk moving](https://elevenlabs.io/docs/api-reference/tests/test-folders/move) tests between folders.
>
> **Tool and knowledge base overrides in workflows**: Agent workflow node overrides now support `tool_ids` and `knowledge_base` fields in `PromptAgentAPIModelOverrideConfig`, allowing workflow nodes to control which tools and knowledge base documents each sub-agent can access.
>
> **Response filter `hide_all` mode**: Added `hide_all` option to `ResponseFilterMode`, forcing the system to hide all fields of a tool response from the agent.
>
> **Visited agents in conversation history**: The [get conversation](https://elevenlabs.io/docs/api-reference/conversations/get) response now includes a `visited_agents` array of `VisitedAgentRef` objects (with `agent_id` and `branch_id`), tracking which agents participated in a multi-agent conversation.
>
> **Multimodal message support in hooks**: The `useConversationControls` hook now exposes `sendMultimodalMessage`, and the `MultimodalMessageInput` type is exported from `@elevenlabs/client`, making it easier to send images and other multimodal content during conversations.
>
> Source: https://elevenlabs.io/docs/changelog/2026/4/7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-04-07-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-07-new-endpoints|New Endpoints]] · Agent Mode
- [[Changes/ElevenLabs/2026-04-07-python-sdk|Python SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-04-07-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-07-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-04-07-voices-5fda10|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-07-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-04-07-javascript-sdk|JavaScript SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-04-07-packages|Packages]] · Multimodal Input
- [[Changes/ElevenLabs/2026-04-07-swift-sdk|Swift SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-07-speech-to-text-f6e004|Speech to Text]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-06 · HeyGen · [[Changes/HeyGen/2026-04-06-open-video-agent-type-your-prompt-and-generate-seedance-footage-will-automatical|Open Video Agent, type your prompt, and generate]]
- Later: 2026-04-07 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-07-spinner-no-longer-appears-stuck-when-a-long-running-async-shell-command-is-activ|Spinner no longer appears stuck when a long-running async shell command is active]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-04-07-e46dc6&body=Card%3A%20Changes%2FElevenLabs%2F2026-04-07-elevenagents-e46dc6.md%0ACard%20ID%3A%20elevenlabs-2026-04-07-e46dc6%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F4%2F7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->