---
card_id: elevenlabs-2025-06-08-145d07
date: '2025-06-08'
description: 'ElevenLabs · 2025-06-08 · Agent Mode: **Supported Voices**:'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 703
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 7c6f89ef0cb8ee43fcad7ab4ffe94e51ac3028ed5870bdbc006be3db832f7059
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2025-06-08-145d07
  comparison: ''
  date: '2025-06-08'
  description: 'ElevenLabs — ElevenLabs updates — 2025-06-08: **Supported Voices**:'
  evidence:
  - quote: '**Supported Voices**:'
    source_release: https://elevenlabs.io/docs/changelog/2025/6/8
  - quote: '[Agent configuration](https://elevenlabs.io/docs/api-reference/agents/update#request.body.tts.supported_voices)
      - Added `optimize_streaming_latency`, `stability`, `speed`, and `similarity_boost`
      parameters for per-voice TTS customization'
    source_release: https://elevenlabs.io/docs/changelog/2025/6/8
  - quote: '**Transfer to Number**:'
    source_release: https://elevenlabs.io/docs/changelog/2025/6/8
  - quote: '[Agent configuration](https://elevenlabs.io/docs/api-reference/agents/update#request.body.system_tools.transfer_to_number)
      - Added `enable_client_message` parameter to control whether a message is played
      to the client during transfer'
    source_release: https://elevenlabs.io/docs/changelog/2025/6/8
  - quote: '**Knowledge Base**:'
    source_release: https://elevenlabs.io/docs/changelog/2025/6/8
  - quote: Knowledge base documents now use `supported_usages` instead of `prompt_injectable`
      for better usage mode control
    source_release: https://elevenlabs.io/docs/changelog/2025/6/8
  - quote: RAG index creation now returns enhanced response model with usage information
    source_release: https://elevenlabs.io/docs/changelog/2025/6/8
  - quote: '**Custom LLM**:'
    source_release: https://elevenlabs.io/docs/changelog/2025/6/8
  - quote: '[Agent configuration](https://elevenlabs.io/docs/api-reference/agents/update#request.body.llm.custom_llm)
      - Added `request_headers` parameter for custom header configuration'
    source_release: https://elevenlabs.io/docs/changelog/2025/6/8
  - quote: '**Widget Configuration**:'
    source_release: https://elevenlabs.io/docs/changelog/2025/6/8
  - quote: '[Agent platform settings](https://elevenlabs.io/docs/api-reference/agents/update#request.body.platform_settings.widget_config)
      - Added comprehensive `styles` configuration for widget appearance customization'
    source_release: https://elevenlabs.io/docs/changelog/2025/6/8
  - quote: Added support for [versioned LLM models](https://elevenlabs.io/docs/api-reference/agents/create#request.body.conversation_config.agent.prompt.llm)
      with explicit version identifiers
    source_release: https://elevenlabs.io/docs/changelog/2025/6/8
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2025-06-08-2025-06-08-c2ca0bb8
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/Cursor/2025-06-04-background-agent-for-everyone-8b35dc|Background Agent
  for everyone]]'
- '[[Changes/Cursor/2025-06-04-this-release-brings-bugbot-for-code-review-a-first-look-at-memories-one-click-mc|Cursor
  brings Bugbot for code review, a first look at memories, one-click MCP setup…]]'
- '[[Changes/Replit/2025-06-06-new-agent-entrypoints-in-workspace|New Agent entrypoints
  in workspace]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2025-06-08-2025-06-08-c2ca0bb8|elevenlabs-2025-06-08-2025-06-08-c2ca0bb8]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2025-06-08 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2025/6/8) · from [[Releases/ElevenLabs/elevenlabs-2025-06-08-2025-06-08-c2ca0bb8|ElevenLabs updates — 2025-06-08]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Supported Voices**:
>
> [Agent configuration](https://elevenlabs.io/docs/api-reference/agents/update#request.body.tts.supported_voices) - Added `optimize_streaming_latency`, `stability`, `speed`, and `similarity_boost` parameters for per-voice TTS customization
>
> **Transfer to Number**:
>
> [Agent configuration](https://elevenlabs.io/docs/api-reference/agents/update#request.body.system_tools.transfer_to_number) - Added `enable_client_message` parameter to control whether a message is played to the client during transfer
>
> **Knowledge Base**:
>
> Knowledge base documents now use `supported_usages` instead of `prompt_injectable` for better usage mode control
>
> RAG index creation now returns enhanced response model with usage information
>
> **Custom LLM**:
>
> [Agent configuration](https://elevenlabs.io/docs/api-reference/agents/update#request.body.llm.custom_llm) - Added `request_headers` parameter for custom header configuration
>
> **Widget Configuration**:
>
> [Agent platform settings](https://elevenlabs.io/docs/api-reference/agents/update#request.body.platform_settings.widget_config) - Added comprehensive `styles` configuration for widget appearance customization
>
> Added support for [versioned LLM models](https://elevenlabs.io/docs/api-reference/agents/create#request.body.conversation_config.agent.prompt.llm) with explicit version identifiers
>
> Source: https://elevenlabs.io/docs/changelog/2025/6/8
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2025-06-08-text-to-speech|Text to Speech]] · Model Support
- [[Changes/ElevenLabs/2025-06-08-agents-platform-5c0653|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2025-06-08-sdks|SDKs]] · Apps and Integrations
- [[Changes/ElevenLabs/2025-06-08-agents-platform-ce4a03|Agents Platform]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2025-06-06 · Replit · [[Changes/Replit/2025-06-06-new-agent-entrypoints-in-workspace|New Agent entrypoints in workspace]]
- Later: 2025-06-10 · OpenHands · [[Changes/OpenHands/2025-06-10-ensured-prs-opened-by-agent-is-properly-tracked-in-conversation-metadata-by-malh|Ensured PRs opened by agent is properly tracked in conversation metadata]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2025-06-08-145d07&body=Card%3A%20Changes%2FElevenLabs%2F2025-06-08-agents-platform.md%0ACard%20ID%3A%20elevenlabs-2025-06-08-145d07%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2025%2F6%2F8%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->