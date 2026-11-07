---
card_id: elevenlabs-2026-10-26-2cc87b
date: '2026-10-26'
description: 'ElevenLabs · 2026-10-26 · Agent Mode: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
  [Get…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1208
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: b054efde8240cf656f7b8282a1b1a1524995d48d0f65562450a1ce5a7a8c4c5a
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-10-26-2cc87b
  comparison: ''
  confidence: low
  date: '2026-10-26'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-26: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
    [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
  evidence:
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update
      agent](https://elevenlabs.io/docs/api-reference/agents/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: Prompt configuration adds `service_tier` (`standard` or `fast`, default
      `standard`). Workflow node prompt overrides add nullable `service_tier`.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: Widget configuration adds `mobile_fullscreen` (boolean, default `true`).
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '[List LLMs](https://elevenlabs.io/docs/api-reference/llm/list) - Each
      model adds required `available_service_tiers` (array of `standard` or `fast`).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '[Calculate LLM usage](https://elevenlabs.io/docs/api-reference/llm/calculate)
      and [Calculate expected LLM usage for an agent](https://elevenlabs.io/docs/api-reference/agents/calculate)
      - Added optional `service_tier`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '[Get widget](https://elevenlabs.io/docs/api-reference/widget/get) - Widget
      configuration adds `mobile_fullscreen` (boolean, default `true`).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '[Create crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/create-crawl-job)
      - Added optional `exclude_patterns` (array of strings, up to 50 items of up
      to 2,048 characters each).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '[Get crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/get-crawl-job)
      and [List crawl jobs](https://elevenlabs.io/docs/api-reference/knowledge-base/list-crawl-jobs)
      - Crawl jobs add `exclude_patterns` (array of strings).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: Knowledge base document responses - `auto_sync_info` removes the deprecated
      `auto_discover` field.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '[Run tests](https://elevenlabs.io/docs/api-reference/tests/run-tests)
      - Added optional `name` (string, 1 to 256 characters). [Get test invocation](https://elevenlabs.io/docs/api-reference/tests/test-invocations/get)
      and [List test invocations](https://elevenlabs.io/docs/api-reference/tests/test-invocations/list)
      return nullable `name`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '[Update branch](https://elevenlabs.io/docs/api-reference/agents/branches/update)
      - Added optional `description` (string, up to 4,096 characters). Pass an empty
      string to clear it.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '[Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: Conversation charging adds nullable `voice_surcharge_charge` (integer).
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: Agent definition source enum adds `architect`.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: Agent deployments (`GET /v1/convai/agents/{agent_id}/deployments`) - Deployment
      source enum adds `duplicate`.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: Conversation initiation client data, including the `conversation_initiation_client_data`
      WebSocket event and [Submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create)
      - Added optional `start_procedure_ids` (array of strings).
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: Tool type enum removes `api_integration_mcp`.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-10-26-2026-10-26-ca7c552d
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/AnythingLLM/2026-10-26-apply-workspace-model-changes-to-agent-sessions-mid-thread-by-shatfield4-in-http|Apply
  workspace model changes to agent sessions mid-thread]]'
- '[[Changes/Claude Code/2026-10-26-2-agent-mode-changes-in-v2-1-311|2 Agent Mode
  changes in v2.1.311]]'
- '[[Changes/ElevenLabs/2026-10-26-knowledge-base-crawl-exclusions|Knowledge base
  crawl exclusions]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-26-2026-10-26-ca7c552d|elevenlabs-2026-10-26-2026-10-26-ca7c552d]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-10-26 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/10/26) · from [[Releases/ElevenLabs/elevenlabs-2026-10-26-2026-10-26-ca7c552d|ElevenLabs updates — 2026-10-26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
>
> Prompt configuration adds `service_tier` (`standard` or `fast`, default `standard`). Workflow node prompt overrides add nullable `service_tier`.
>
> Widget configuration adds `mobile_fullscreen` (boolean, default `true`).
>
> [List LLMs](https://elevenlabs.io/docs/api-reference/llm/list) - Each model adds required `available_service_tiers` (array of `standard` or `fast`).
>
> [Calculate LLM usage](https://elevenlabs.io/docs/api-reference/llm/calculate) and [Calculate expected LLM usage for an agent](https://elevenlabs.io/docs/api-reference/agents/calculate) - Added optional `service_tier`.
>
> [Get widget](https://elevenlabs.io/docs/api-reference/widget/get) - Widget configuration adds `mobile_fullscreen` (boolean, default `true`).
>
> [Create crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/create-crawl-job) - Added optional `exclude_patterns` (array of strings, up to 50 items of up to 2,048 characters each).
>
> [Get crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/get-crawl-job) and [List crawl jobs](https://elevenlabs.io/docs/api-reference/knowledge-base/list-crawl-jobs) - Crawl jobs add `exclude_patterns` (array of strings).
>
> Knowledge base document responses - `auto_sync_info` removes the deprecated `auto_discover` field.
>
> [Run tests](https://elevenlabs.io/docs/api-reference/tests/run-tests) - Added optional `name` (string, 1 to 256 characters). [Get test invocation](https://elevenlabs.io/docs/api-reference/tests/test-invocations/get) and [List test invocations](https://elevenlabs.io/docs/api-reference/tests/test-invocations/list) return nullable `name`.
>
> [Update branch](https://elevenlabs.io/docs/api-reference/agents/branches/update) - Added optional `description` (string, up to 4,096 characters). Pass an empty string to clear it.
>
> [Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get)
>
> Conversation charging adds nullable `voice_surcharge_charge` (integer).
>
> Agent definition source enum adds `architect`.
>
> Agent deployments (`GET /v1/convai/agents/{agent_id}/deployments`) - Deployment source enum adds `duplicate`.
>
> Conversation initiation client data, including the `conversation_initiation_client_data` WebSocket event and [Submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create) - Added optional `start_procedure_ids` (array of strings).
>
> Tool type enum removes `api_integration_mcp`.
>
> Source: https://elevenlabs.io/docs/changelog/2026/10/26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-26-2-apps-and-integrations-changes-in-elevenlabs-updates-2026-10-26|2 Apps and Integrations changes in ElevenLabs updates — 2026-10-26]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-26-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-knowledge-base-crawl-exclusions|Knowledge base crawl exclusions]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-26-clone-strength-for-v4-voices|Clone strength for v4 voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-android-sdk|Android SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-10-26-2-pricing-model-changes-in-elevenlabs-updates-2026-10-26|2 Pricing Model changes in ElevenLabs updates — 2026-10-26]] · Pricing Model
- [[Changes/ElevenLabs/2026-10-26-transcript-downloads-the-dubbing-project-menu-can-download-target-language-trans|Transcript downloads: The dubbing project menu can download target language…]] · Interface Experience
- [[Changes/ElevenLabs/2026-10-26-video-to-music-studio-s-video-to-music-workflow-uses-music-v2-5-by-default|Video to music: Studio's video to music workflow uses Music v2.5 by default]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-26-2-editor-experience-changes-in-elevenlabs-updates-2026-10-26|2 Editor Experience changes in ElevenLabs updates — 2026-10-26]] · Editor Experience
- [[Changes/ElevenLabs/2026-10-26-dubbing|Dubbing]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-voice-changer|Voice Changer]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-2-mobile-and-desktop-changes-in-elevenlabs-updates-2026-10-26|2 Mobile and Desktop changes in ElevenLabs updates — 2026-10-26]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-10-26-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-14-voice-and-audio-changes-in-elevenlabs-updates-2026-10-26|14 Voice and Audio changes in ElevenLabs updates — 2026-10-26]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-voice-cloning-permissions-members-without-the-create-instant-voice-clone-or-crea|Voice cloning permissions]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-10-26-9-agent-mode-changes-in-elevenlabs-updates-2026-10-26|9 Agent Mode changes in ElevenLabs updates — 2026-10-26]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-26-fast-llm-service-tier|Fast LLM service tier]] · Model Support
- [[Changes/ElevenLabs/2026-10-26-3-model-support-changes-in-elevenlabs-updates-2026-10-26|3 Model Support changes in ElevenLabs updates — 2026-10-26]] · Model Support
- [[Changes/ElevenLabs/2026-10-26-elevenlabs-cli|ElevenLabs CLI]] · Account and Access
- [[Changes/ElevenLabs/2026-10-26-oauth-scope-oauth-clients-can-request-the-realtime-translation-scope|OAuth scope: OAuth clients can request the realtime_translation scope]] · Account and Access
- [[Changes/ElevenLabs/2026-10-26-9-other-changes-in-elevenlabs-updates-2026-10-26|9 other changes in ElevenLabs updates — 2026-10-26]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-26 · Claude Code · [[Changes/Claude Code/2026-10-26-2-agent-mode-changes-in-v2-1-311|2 Agent Mode changes in v2.1.311]]
- Later: 2026-10-26 · Google Antigravity · [[Changes/Google Antigravity/2026-10-26-added-drag-and-drop-support-for-files-or-screenshots-directly-onto-the-agent-pan|Added drag-and-drop support for files or screenshots directly onto the Agent panel]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-26-2cc87b&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-26-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-10-26-2cc87b%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->