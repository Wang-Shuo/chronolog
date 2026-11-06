---
card_id: elevenlabs-2025-05-26-bec9ee
date: '2025-05-26'
description: 'ElevenLabs · 2025-05-26 · Agent Mode: **Secret dynamic variables**:
  Added support for specifying dynamic variables as secrets with the `secret__` prefix…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 690
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: e273555a76643b2129be985be76755829a534db6f77102cdfad34d0a9b25cb5b
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2025-05-26-bec9ee
  comparison: ''
  confidence: low
  date: '2025-05-26'
  description: 'ElevenLabs — ElevenLabs updates — 2025-05-26: **Secret dynamic variables**:
    Added support for specifying dynamic variables as secrets with the `secret__`
    prefix. Secret dynamic variables can only be used in webhook tool headers and
    are never sent to an LLM, enhancing security for sensitive data. [Learn more](https://elevenlabs.io/docs/eleven-agents/customization/personalization/dynamic-variables#secret-dynamic-variables).'
  evidence:
  - quote: '**Secret dynamic variables**: Added support for specifying dynamic variables
      as secrets with the `secret__` prefix. Secret dynamic variables can only be
      used in webhook tool headers and are never sent to an LLM, enhancing security
      for sensitive data. [Learn more](https://elevenlabs.io/docs/eleven-agents/customization/personalization/dynamic-variables#secret-dynamic-variables).'
    source_release: https://elevenlabs.io/docs/changelog/2025/5/26
  - quote: '**Skip turn system tool**: Introduced a new system tool called **skip_turn**.
      When enabled, the agent will skip its turn if the user explicitly indicates
      they need a moment to think or perform an action (e.g., "just a sec", "give
      me a minute"). This prevents turn timeout from being triggered during intentional
      user pauses. See the [skip turn tool docs](https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/skip-turn)
      for more information.'
    source_release: https://elevenlabs.io/docs/changelog/2025/5/26
  - quote: '**Text input support**: Added text input support in websocket connections
      via "user_message" event with text field. Also added "user_activity" event support
      to indicate typing or other UI activity, improving agent turn-taking when there''s
      interleaved text and audio input.'
    source_release: https://elevenlabs.io/docs/changelog/2025/5/26
  - quote: '**RAG chunk limit**: Added ability to configure the [maximum number of
      chunks](https://elevenlabs.io/docs/api-reference/agents/create#request.body.conversation_config.agent.prompt.rag.max_retrieved_rag_chunks_count)
      collected during RAG retrieval, giving users'
    source_release: https://elevenlabs.io/docs/changelog/2025/5/26
  - quote: more control over context window usage and costs.
    source_release: https://elevenlabs.io/docs/changelog/2025/5/26
  - quote: '**Enhanced widget configuration**: Expanded widget customization options
      to include [text input and text only mode](https://elevenlabs.io/docs/api-reference/widget/get#response.body.widget_config.text_only).'
    source_release: https://elevenlabs.io/docs/changelog/2025/5/26
  - quote: '**LLM usage calculator**: Introduced tools to calculate expected LLM token
      usage and costs for agents, helping with cost estimation and planning.'
    source_release: https://elevenlabs.io/docs/changelog/2025/5/26
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2025-05-26-2025-05-26-7c8cc0ee
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/ElevenLabs/2025-05-19-agents-platform-e84d3e|Agents Platform]]'
- '[[Changes/OpenHands/2025-05-20-2-agent-mode-changes-in-0-39-0|2 Agent Mode changes
  in 0.39.0]]'
- '[[Changes/ElevenLabs/2025-05-26-agents-platform|Agents Platform]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2025-05-26-2025-05-26-7c8cc0ee|elevenlabs-2025-05-26-2025-05-26-7c8cc0ee]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2025-05-26 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2025/5/26) · from [[Releases/ElevenLabs/elevenlabs-2025-05-26-2025-05-26-7c8cc0ee|ElevenLabs updates — 2025-05-26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Secret dynamic variables**: Added support for specifying dynamic variables as secrets with the `secret__` prefix. Secret dynamic variables can only be used in webhook tool headers and are never sent to an LLM, enhancing security for sensitive data. [Learn more](https://elevenlabs.io/docs/eleven-agents/customization/personalization/dynamic-variables#secret-dynamic-variables).
>
> **Skip turn system tool**: Introduced a new system tool called **skip_turn**. When enabled, the agent will skip its turn if the user explicitly indicates they need a moment to think or perform an action (e.g., "just a sec", "give me a minute"). This prevents turn timeout from being triggered during intentional user pauses. See the [skip turn tool docs](https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/skip-turn) for more information.
>
> **Text input support**: Added text input support in websocket connections via "user_message" event with text field. Also added "user_activity" event support to indicate typing or other UI activity, improving agent turn-taking when there's interleaved text and audio input.
>
> **RAG chunk limit**: Added ability to configure the [maximum number of chunks](https://elevenlabs.io/docs/api-reference/agents/create#request.body.conversation_config.agent.prompt.rag.max_retrieved_rag_chunks_count) collected during RAG retrieval, giving users
>
> more control over context window usage and costs.
>
> **Enhanced widget configuration**: Expanded widget customization options to include [text input and text only mode](https://elevenlabs.io/docs/api-reference/widget/get#response.body.widget_config.text_only).
>
> **LLM usage calculator**: Introduced tools to calculate expected LLM token usage and costs for agents, helping with cost estimation and planning.
>
> Source: https://elevenlabs.io/docs/changelog/2025/5/26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2025-05-26-voices|Voices]] · Collaboration
- [[Changes/ElevenLabs/2025-05-26-voices-341886|Voices]] · Collaboration
- [[Changes/ElevenLabs/2025-05-26-agents-platform|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2025-05-26-audio-native|Audio Native]] · Voice and Audio
- [[Changes/ElevenLabs/2025-05-26-text-to-speech|Text to Speech]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2025-05-20 · OpenHands · [[Changes/OpenHands/2025-05-20-2-agent-mode-changes-in-0-39-0|2 Agent Mode changes in 0.39.0]]
- Later: 2025-05-30 · Replit · [[Changes/Replit/2025-05-30-preview-empty-state-improvements|Preview empty state improvements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2025-05-26-bec9ee&body=Card%3A%20Changes%2FElevenLabs%2F2025-05-26-agents-platform-bec9ee.md%0ACard%20ID%3A%20elevenlabs-2025-05-26-bec9ee%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2025%2F5%2F26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->