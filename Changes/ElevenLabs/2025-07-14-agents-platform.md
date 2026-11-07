---
card_id: elevenlabs-2025-07-14-699e17
date: '2025-07-14'
description: 'ElevenLabs · 2025-07-14 · Agent Mode: **Azure OpenAI custom LLM support**:
  Added support for Azure-hosted OpenAI models in custom LLM configurations. When…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 739
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: d87e7ae8680d86284c514a38603f93492e063555cf1d26cf0a24b1668a01ad3b
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2025-07-14-699e17
  comparison: ''
  confidence: low
  date: '2025-07-14'
  description: 'ElevenLabs — ElevenLabs updates — 2025-07-14: **Azure OpenAI custom
    LLM support**: Added support for Azure-hosted OpenAI models in custom LLM configurations.
    When using an Azure endpoint, a new required field for [API version](https://elevenlabs.io/docs/api-reference/agents/create#request.body.conversation_config.agent.prompt.custom_llm.api_version)
    is now available in the UI.'
  evidence:
  - quote: '**Azure OpenAI custom LLM support**: Added support for Azure-hosted OpenAI
      models in custom LLM configurations. When using an Azure endpoint, a new required
      field for [API version](https://elevenlabs.io/docs/api-reference/agents/create#request.body.conversation_config.agent.prompt.custom_llm.api_version)
      is now available in the UI.'
    source_release: https://elevenlabs.io/docs/changelog/2025/7/14
  - quote: '**Genesys output variables**: Added support for output variables when
      using [Genesys integrations](https://elevenlabs.io/docs/eleven-agents/phone-numbers/c-caa-s-integrations/genesys),
      enabling better call analytics and data collection.'
    source_release: https://elevenlabs.io/docs/changelog/2025/7/14
  - quote: '**Gemini 2.5 Preview Models Deprecation**: [Models](https://elevenlabs.io/docs/api-reference/agents/create#request.body.conversation_config.agent.prompt.llm)
      `gemini-2.5-flash-preview-05-20` and `gemini-2.5-flash-preview-04-17` have been
      deprecated in Agents Platform as they are being deprecated on 15th July by Google.
      All agents using these models will automatically be transferred to `gemini-2.5-flash`
      the next time they are used. No action is required.'
    source_release: https://elevenlabs.io/docs/changelog/2025/7/14
  - quote: '**WebRTC rollout**: Began progressive rollout of WebRTC capabilities for
      improved connection stability and performance. WebRTC mode can be selected in
      the React SDK and is used in 11.ai.'
    source_release: https://elevenlabs.io/docs/changelog/2025/7/14
  - quote: '**Keypad touch tone**: Fixed an issue affecting playing keypad touch tones
      on Twilio. See [keypad touch tone documentation](https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/play-keypad-touch-tone).'
    source_release: https://elevenlabs.io/docs/changelog/2025/7/14
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2025-07-14-2025-07-14-80d77c89
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/ElevenLabs/2025-07-07-sdks|SDKs]]'
- '[[Changes/Dify/2025-07-10-feat-retain-llm-setting-for-agent-node-by-fdb02983rhy-in-https-github-com-langge|feat:
  Retain llm setting for agent node]]'
- '[[Changes/Replit/2025-07-11-agent-multi-tool-calling-upgrade|Agent multi-tool calling
  upgrade]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2025-07-14-2025-07-14-80d77c89|elevenlabs-2025-07-14-2025-07-14-80d77c89]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2025-07-14 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2025/7/14) · from [[Releases/ElevenLabs/elevenlabs-2025-07-14-2025-07-14-80d77c89|ElevenLabs updates — 2025-07-14]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Azure OpenAI custom LLM support**: Added support for Azure-hosted OpenAI models in custom LLM configurations. When using an Azure endpoint, a new required field for [API version](https://elevenlabs.io/docs/api-reference/agents/create#request.body.conversation_config.agent.prompt.custom_llm.api_version) is now available in the UI.
>
> **Genesys output variables**: Added support for output variables when using [Genesys integrations](https://elevenlabs.io/docs/eleven-agents/phone-numbers/c-caa-s-integrations/genesys), enabling better call analytics and data collection.
>
> **Gemini 2.5 Preview Models Deprecation**: [Models](https://elevenlabs.io/docs/api-reference/agents/create#request.body.conversation_config.agent.prompt.llm) `gemini-2.5-flash-preview-05-20` and `gemini-2.5-flash-preview-04-17` have been deprecated in Agents Platform as they are being deprecated on 15th July by Google. All agents using these models will automatically be transferred to `gemini-2.5-flash` the next time they are used. No action is required.
>
> **WebRTC rollout**: Began progressive rollout of WebRTC capabilities for improved connection stability and performance. WebRTC mode can be selected in the React SDK and is used in 11.ai.
>
> **Keypad touch tone**: Fixed an issue affecting playing keypad touch tones on Twilio. See [keypad touch tone documentation](https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/play-keypad-touch-tone).
>
> Source: https://elevenlabs.io/docs/changelog/2025/7/14
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2025-07-14-text-to-voice|Text to Voice]] · Voice and Audio
- [[Changes/ElevenLabs/2025-07-14-sdks|SDKs]] · Apps and Integrations
- [[Changes/ElevenLabs/2025-07-14-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2025-07-14-agents-platform-d9d1f0|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2025-07-14-elevencreative-studio|ElevenCreative Studio]] · Memory and Personalization
- [[Changes/ElevenLabs/2025-07-14-text-to-voice-f4167d|Text to Voice]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2025-07-11 · Replit · [[Changes/Replit/2025-07-11-agent-multi-tool-calling-upgrade|Agent multi-tool calling upgrade]]
- Later: 2025-07-19 · Codex CLI · [[Changes/Codex CLI/2025-07-19-https-github-com-openai-codex-pull-1589-changes-ctrl-d-so-it-only-exits-the-tui|(source link) changes ctrl-d so it only exits the TUI…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2025-07-14-699e17&body=Card%3A%20Changes%2FElevenLabs%2F2025-07-14-agents-platform.md%0ACard%20ID%3A%20elevenlabs-2025-07-14-699e17%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2025%2F7%2F14%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->