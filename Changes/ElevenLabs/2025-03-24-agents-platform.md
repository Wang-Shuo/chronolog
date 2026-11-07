---
card_id: elevenlabs-2025-03-24-c10a04
date: '2025-03-24'
description: 'ElevenLabs · 2025-03-24 · Agent Mode: Updated Agents Platform endpoints:'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 627
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: c7a52c3a1176461f7ce8bc9a7b24cf2c6b8894852bc92b90dffd21b9b75976a2
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2025-03-24-c10a04
  comparison: ''
  date: '2025-03-24'
  description: 'ElevenLabs — ElevenLabs updates — 2025-03-24: Updated Agents Platform
    endpoints:'
  evidence:
  - quote: 'Updated Agents Platform endpoints:'
    source_release: https://elevenlabs.io/docs/changelog/2025/3/24
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create)
      - Added `mic_muting_enabled` property for UI control and `workspace_overrides`
      property for workspace-specific configurations'
    source_release: https://elevenlabs.io/docs/changelog/2025/3/24
  - quote: '[Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
      - Added `workspace_overrides` property for customizing agent behavior per workspace'
    source_release: https://elevenlabs.io/docs/changelog/2025/3/24
  - quote: '[Get agent](https://elevenlabs.io/docs/api-reference/agents/get) - Added
      `workspace_overrides` property to the response'
    source_release: https://elevenlabs.io/docs/changelog/2025/3/24
  - quote: '[Get widget](https://elevenlabs.io/docs/api-reference/widget/get) - Added
      `mic_muting_enabled` property for controlling microphone muting in the widget
      UI'
    source_release: https://elevenlabs.io/docs/changelog/2025/3/24
  - quote: '[Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)
      - Added rag information to view knowledge base content used during conversations'
    source_release: https://elevenlabs.io/docs/changelog/2025/3/24
  - quote: '[Create phone number](https://elevenlabs.io/docs/api-reference/phone-numbers)
      - Replaced generic structure with specific twilio phone number and sip trunk
      options'
    source_release: https://elevenlabs.io/docs/changelog/2025/3/24
  - quote: '[Compute RAG index](https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/compute-rag-index)
      - Removed `force_reindex` query parameter for more controlled indexing'
    source_release: https://elevenlabs.io/docs/changelog/2025/3/24
  - quote: '[List knowledge base documents](https://elevenlabs.io/docs/api-reference/knowledge-base/list)
      - Changed response structure to support different document types'
    source_release: https://elevenlabs.io/docs/changelog/2025/3/24
  - quote: '[Get knowledge base document](https://elevenlabs.io/docs/api-reference/knowledge-base/get-document)
      - Modified to return different response models based on document type'
    source_release: https://elevenlabs.io/docs/changelog/2025/3/24
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2025-03-24-2025-03-24-f58d02b9
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/Dify/2025-03-18-feat-add-click-away-and-mounting-logic-to-agent-setting-component-by-fdb02983rhy|feat:
  add click-away and mounting logic to agent setting component]]'
- '[[Changes/Replit/2025-03-21-agent-timeline-messages|Agent timeline messages]]'
- '[[Changes/Cursor/2025-03-23-built-in-modes-custom-modes-beta|Built-in modes & custom
  modes (beta)]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2025-03-24-2025-03-24-f58d02b9|elevenlabs-2025-03-24-2025-03-24-f58d02b9]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2025-03-24 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2025/3/24) · from [[Releases/ElevenLabs/elevenlabs-2025-03-24-2025-03-24-f58d02b9|ElevenLabs updates — 2025-03-24]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Updated Agents Platform endpoints:
>
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create) - Added `mic_muting_enabled` property for UI control and `workspace_overrides` property for workspace-specific configurations
>
> [Update agent](https://elevenlabs.io/docs/api-reference/agents/update) - Added `workspace_overrides` property for customizing agent behavior per workspace
>
> [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) - Added `workspace_overrides` property to the response
>
> [Get widget](https://elevenlabs.io/docs/api-reference/widget/get) - Added `mic_muting_enabled` property for controlling microphone muting in the widget UI
>
> [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get) - Added rag information to view knowledge base content used during conversations
>
> [Create phone number](https://elevenlabs.io/docs/api-reference/phone-numbers) - Replaced generic structure with specific twilio phone number and sip trunk options
>
> [Compute RAG index](https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/compute-rag-index) - Removed `force_reindex` query parameter for more controlled indexing
>
> [List knowledge base documents](https://elevenlabs.io/docs/api-reference/knowledge-base/list) - Changed response structure to support different document types
>
> [Get knowledge base document](https://elevenlabs.io/docs/api-reference/knowledge-base/get-document) - Modified to return different response models based on document type
>
> Source: https://elevenlabs.io/docs/changelog/2025/3/24
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2025-03-24-voice-management|Voice Management]] · Voice and Audio
- [[Changes/ElevenLabs/2025-03-24-core-app-signup-added-signup-endpoints-for-the-new-core-mobile-app|Core app signup: Added signup endpoints for the new Core mobile app]] · Mobile and Desktop
- [[Changes/ElevenLabs/2025-03-24-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2025-03-24-speech-to-text-c41742|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2025-03-24-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2025-03-24-elevencreative-studio|ElevenCreative Studio]] · Voice and Audio
- [[Changes/ElevenLabs/2025-03-24-agents-platform-e22490|Agents Platform]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2025-03-23 · Cursor · [[Changes/Cursor/2025-03-23-built-in-modes-custom-modes-beta|Built-in modes & custom modes (beta)]]
- Later: 2025-03-28 · Replit · [[Changes/Replit/2025-03-28-agent-v2-is-now-available|Agent v2 is now available]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2025-03-24-c10a04&body=Card%3A%20Changes%2FElevenLabs%2F2025-03-24-agents-platform.md%0ACard%20ID%3A%20elevenlabs-2025-03-24-c10a04%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2025%2F3%2F24%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->