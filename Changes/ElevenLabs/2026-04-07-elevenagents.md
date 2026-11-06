---
card_id: elevenlabs-2026-04-07-60422b
date: '2026-04-07'
description: 'ElevenLabs · 2026-04-07 · Agent Mode: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
  [Get…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1006
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: f374d95da15c6229580b2034e95aaedf10cb4152b0fa7dfe431fb602d90205cd
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-04-07-60422b
  comparison: ''
  confidence: low
  date: '2026-04-07'
  description: 'ElevenLabs — ElevenLabs updates — 2026-04-07: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
    [Get agent](https://elevenlabs.io/docs/api-reference/agents/get), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
  evidence:
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Get agent](https://elevenlabs.io/docs/api-reference/agents/get), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: Added `data_collection_scopes` field (object, optional) to `AgentPlatformSettings`
      for per-item analysis scope control
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: '[Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: Added `visited_agents` field (array of `VisitedAgentRef`, optional) tracking
      agents visited during multi-agent conversations
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: Added `scoped` field (array of `ScopedAnalysisResult`) to conversation
      analysis response
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: '[Run conversation analysis](https://elevenlabs.io/docs/api-reference/conversations/analysis/run-analysis)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: Response now includes `scoped` analysis results with per-agent evaluation
      breakdowns
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: Agent workflow node overrides (`PromptAgentAPIModelOverrideConfig`)
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: Added `tool_ids` field (array of strings, optional) for restricting available
      tools per workflow node
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: Added `knowledge_base` field (object, optional) for overriding knowledge
      base per workflow node
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: '`ResponseFilterMode` enum'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: Added `hide_all` value
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: '`MockNoMatchBehavior` default'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: Changed default from `call_real_tool` to `raise_error`
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: '`ClientEvent` enum'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: Added `dtmf_request` value
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: Turn metrics
    source_release: https://elevenlabs.io/docs/changelog/2026/4/7
  - quote: Added `convai_tts_cascade` field (string, nullable) to `ConversationTurnMetrics`
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
- '[[Changes/Replit/2026-04-03-agent|Agent]]'
- '[[Changes/GitHub Copilot CLI/2026-04-06-2-agent-mode-changes-in-v1-0-19|2 Agent
  Mode changes in v1.0.19]]'
- '[[Changes/ElevenLabs/2026-04-07-new-endpoints|New Endpoints]]'
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
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
>
> Added `data_collection_scopes` field (object, optional) to `AgentPlatformSettings` for per-item analysis scope control
>
> [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)
>
> Added `visited_agents` field (array of `VisitedAgentRef`, optional) tracking agents visited during multi-agent conversations
>
> Added `scoped` field (array of `ScopedAnalysisResult`) to conversation analysis response
>
> [Run conversation analysis](https://elevenlabs.io/docs/api-reference/conversations/analysis/run-analysis)
>
> Response now includes `scoped` analysis results with per-agent evaluation breakdowns
>
> Agent workflow node overrides (`PromptAgentAPIModelOverrideConfig`)
>
> Added `tool_ids` field (array of strings, optional) for restricting available tools per workflow node
>
> Added `knowledge_base` field (object, optional) for overriding knowledge base per workflow node
>
> `ResponseFilterMode` enum
>
> Added `hide_all` value
>
> `MockNoMatchBehavior` default
>
> Changed default from `call_real_tool` to `raise_error`
>
> `ClientEvent` enum
>
> Added `dtmf_request` value
>
> Turn metrics
>
> Added `convai_tts_cascade` field (string, nullable) to `ConversationTurnMetrics`
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
- [[Changes/ElevenLabs/2026-04-07-javascript-sdk|JavaScript SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-04-07-packages|Packages]] · Multimodal Input
- [[Changes/ElevenLabs/2026-04-07-swift-sdk|Swift SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-07-elevenagents-e46dc6|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-04-07-speech-to-text-f6e004|Speech to Text]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-06 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-06-2-agent-mode-changes-in-v1-0-19|2 Agent Mode changes in v1.0.19]]
- Later: 2026-04-07 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-07-spinner-no-longer-appears-stuck-when-a-long-running-async-shell-command-is-activ|Spinner no longer appears stuck when a long-running async shell command is active]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-04-07-60422b&body=Card%3A%20Changes%2FElevenLabs%2F2026-04-07-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-04-07-60422b%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F4%2F7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->