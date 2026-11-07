---
card_id: elevenlabs-2026-11-02-44d2d9
date: '2026-11-02'
description: 'ElevenLabs · 2026-11-02 · Model Support: 7 changes in ElevenLabs updates
  — 2026-11-02 — **GPT-6.1 Terra**: `gpt-6.1-terra` can be selected as the agent LLM
  and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1393
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a056b426fdc08f026f72eaa734827aba7567852bec0999784d087534eb9cd859
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-11-02-44d2d9
  comparison: ''
  date: '2026-11-02'
  description: 'ElevenLabs — ElevenLabs updates — 2026-11-02: 7 Model Support changes'
  evidence:
  - quote: '**GPT-6.1 Terra**: `gpt-6.1-terra` can be selected as the agent LLM and
      as the analysis LLM, on the standard and fast service tiers, with reasoning
      effort from `none` to `max` (default `medium`).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Default LLM**: New agents created without an explicit LLM use `gemini-3.5-flash`
      instead of `gemini-2.5-flash`, and the default backup LLM cascade leads with
      Gemini 3.5 Flash models. Existing agents are unchanged. Gemini 3.5 Flash-Lite
      is also available in the India and Singapore isolated environments.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Model deprecations**: `gpt-4.1-nano` and `gpt-4o-2024-05-13`, which
      OpenAI shut down on October 23, are deprecated immediately, and agents using
      them run on `gpt-5.6-luna` and `gpt-5.6-sol` respectively. `gpt-5`, `gpt-5-mini`,
      `gpt-5-nano` and their `2025-08-07` snapshots are deprecated ahead of OpenAI''s
      December 11 shutdown, with traffic moving to `gpt-5.6-sol`, `gpt-5.6-terra`
      and `gpt-5.6-luna` in steps from 10% on November 11 to 100% on December 6. [List
      LLMs](https://elevenlabs.io/docs/api-reference/llm/list) returns `deprecation_info`
      for these models. Claude Sonnet 4.5 is deprecated on November 30, with Claude
      Sonnet 4.6 as the replacement, and is removed from model selectors. The fallback
      ramp for `gemini-2.5-flash` and `gemini-2.5-flash-lite` now starts on November
      8 instead of November 1; the November 30 cutoff is unchanged.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Workflows**: Update state nodes and the `update_state` tool can override
      LLM settings (model, temperature, token limit and reasoning) for the rest of
      the conversation from a new **LLM** tab. Double-click a workflow edge to add
      reroute points that shape it. Workflow tool nodes accept only configurable system
      tools plus `start_procedure` and `end_procedure`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**SFX v3 for everyone**: SFX v3 (`eleven_text_to_sound_v3`) is available
      to every workspace and is the default model in Sound Effects, Studio and Flows.
      The sound effects that [Video to music](https://elevenlabs.io/docs/api-reference/music/video-to-music)
      adds with `add_sfx` are generated with SFX v3. See [SFX v3](https://elevenlabs.io/docs/overview/models#sfx-v3).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Flows**: Node groups and the structure sidebar are available in every
      workspace. LLM nodes on video-capable models such as `gemini-3.5-flash-llm`
      accept video prompt references.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Cached LLM tokens**: Cache writes are billed at least at the input rate
      and cache reads at the vendor''s cached rate. LLM calls for post-call analysis,
      guardrails and agent tests bill cached prompt tokens at those rates instead
      of the full input rate. Gemini 2.5 Flash-Lite cache reads are billed at 0.01
      instead of 0.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: elevenlabs
  product_name: ElevenLabs
  slug: 7-model-support-changes-in-elevenlabs-updates-2026-11-02
  source_release: elevenlabs-2026-11-02-2026-11-02-7efe9660
  source_type: elevenlabs_changelog
  theme: model-support
  title: 7 Model Support changes in ElevenLabs updates — 2026-11-02
  type: change
related_changes:
- '[[Changes/Replit/2026-10-30-gpt-6-1-terra-in-the-model-selector|GPT-6.1 Terra in
  the model selector]]'
- '[[Changes/Claude Code/2026-10-31-deprecated-fast-mode-for-opus-4-8-as-of-october-30-2026-it-will-be-removed-on-no|Deprecated
  fast mode for Opus 4.8 as of October 30, 2026]]'
- '[[Changes/ElevenLabs/2026-11-02-sfx-v3|SFX v3]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-11-02-2026-11-02-7efe9660|elevenlabs-2026-11-02-2026-11-02-7efe9660]]'
source_type: elevenlabs_changelog
theme: model-support
title: 7 Model Support changes in ElevenLabs updates — 2026-11-02
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Model Support changes in ElevenLabs updates — 2026-11-02

**ElevenLabs** · 2026-11-02 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://elevenlabs.io/docs/changelog/2026/11/2) · from [[Releases/ElevenLabs/elevenlabs-2026-11-02-2026-11-02-7efe9660|ElevenLabs updates — 2026-11-02]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **GPT-6.1 Terra**: `gpt-6.1-terra` can be selected as the agent LLM and as the analysis LLM, on the standard and fast service tiers, with reasoning effort from `none` to `max` (default `medium`).

> **Default LLM**: New agents created without an explicit LLM use `gemini-3.5-flash` instead of `gemini-2.5-flash`, and the default backup LLM cascade leads with Gemini 3.5 Flash models. Existing agents are unchanged. Gemini 3.5 Flash-Lite is also available in the India and Singapore isolated environments.

> **Model deprecations**: `gpt-4.1-nano` and `gpt-4o-2024-05-13`, which OpenAI shut down on October 23, are deprecated immediately, and agents using them run on `gpt-5.6-luna` and `gpt-5.6-sol` respectively. `gpt-5`, `gpt-5-mini`, `gpt-5-nano` and their `2025-08-07` snapshots are deprecated ahead of OpenAI's December 11 shutdown, with traffic moving to `gpt-5.6-sol`, `gpt-5.6-terra` and `gpt-5.6-luna` in steps from 10% on November 11 to 100% on December 6. [List LLMs](https://elevenlabs.io/docs/api-reference/llm/list) returns `deprecation_info` for these models. Claude Sonnet 4.5 is deprecated on November 30, with Claude Sonnet 4.6 as the replacement, and is removed from model selectors. The fallback ramp for `gemini-2.5-flash` and `gemini-2.5-flash-lite` now starts on November 8 instead of November 1; the November 30 cutoff is unchanged.

> **Workflows**: Update state nodes and the `update_state` tool can override LLM settings (model, temperature, token limit and reasoning) for the rest of the conversation from a new **LLM** tab. Double-click a workflow edge to add reroute points that shape it. Workflow tool nodes accept only configurable system tools plus `start_procedure` and `end_procedure`.

> **SFX v3 for everyone**: SFX v3 (`eleven_text_to_sound_v3`) is available to every workspace and is the default model in Sound Effects, Studio and Flows. The sound effects that [Video to music](https://elevenlabs.io/docs/api-reference/music/video-to-music) adds with `add_sfx` are generated with SFX v3. See [SFX v3](https://elevenlabs.io/docs/overview/models#sfx-v3).

> **Flows**: Node groups and the structure sidebar are available in every workspace. LLM nodes on video-capable models such as `gemini-3.5-flash-llm` accept video prompt references.

> **Cached LLM tokens**: Cache writes are billed at least at the input rate and cache reads at the vendor's cached rate. LLM calls for post-call analysis, guardrails and agent tests bill cached prompt tokens at those rates instead of the full input rate. Gemini 2.5 Flash-Lite cache reads are billed at 0.01 instead of 0.

Source: https://elevenlabs.io/docs/changelog/2026/11/2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-11-02-elevenlabs-cli|ElevenLabs CLI]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-4-safety-and-privacy-changes-in-elevenlabs-updates-2026-11-02|4 Safety and Privacy changes in ElevenLabs updates — 2026-11-02]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-11-02-3-pricing-model-changes-in-elevenlabs-updates-2026-11-02|3 Pricing Model changes in ElevenLabs updates — 2026-11-02]] · Pricing Model
- [[Changes/ElevenLabs/2026-11-02-analysis-items-api|Analysis items API]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-sfx-v3|SFX v3]] · Model Support
- [[Changes/ElevenLabs/2026-11-02-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-2-interface-experience-changes-in-elevenlabs-updates-2026-11-02|2 Interface Experience changes in ElevenLabs updates — 2026-11-02]] · Interface Experience
- [[Changes/ElevenLabs/2026-11-02-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-8-agent-mode-changes-in-elevenlabs-updates-2026-11-02|8 Agent Mode changes in ElevenLabs updates — 2026-11-02]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-workspaces|Workspaces]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-2-files-and-data-changes-in-elevenlabs-updates-2026-11-02|2 Files and Data changes in ElevenLabs updates — 2026-11-02]] · Files and Data
- [[Changes/ElevenLabs/2026-11-02-android-sdk|Android SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-11-02-eleven-realtime-for-every-workspace|Eleven Realtime for every workspace]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-noisy-environment-detection-in-the-api|Noisy environment detection in the API]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-unity-sdk|Unity SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-video-clip-background-removal-video-clips-have-a-remove-background-action-and-ri|Video clip background removal]] · Multimodal Input
- [[Changes/ElevenLabs/2026-11-02-svg-assets-svg-uploads-to-assets-stay-svg-and-render-as-vectors-including-in-the|SVG assets: SVG uploads to Assets stay SVG and render as vectors, including…]] · Editor Experience
- [[Changes/ElevenLabs/2026-11-02-channel-integrations-asynchronous-channels-such-as-slack-telegram-intercom-gmail|Channel integrations: Asynchronous channels such as Slack, Telegram, Intercom…]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-11-02-fixes-oauth-discovery-names-the-host-the-client-connected-to-so-mcp-clients-such|Fixes: OAuth discovery names the host the client connected to, so MCP clients…]] · Account and Access
- [[Changes/ElevenLabs/2026-11-02-16-voice-and-audio-changes-in-elevenlabs-updates-2026-11-02|16 Voice and Audio changes in ElevenLabs updates — 2026-11-02]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-fixes-history-items-for-v4-generations-keep-clone-strength-and-speed-in-their-sa|Fixes: History items for v4 generations keep clone_strength and speed…]] · Reliability and Performance
- [[Changes/ElevenLabs/2026-11-02-professional-voice-clones-on-eleven-v4|Professional Voice Clones on Eleven v4]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-realtime-entity-redaction|Realtime entity redaction]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-7-other-changes-in-elevenlabs-updates-2026-11-02|7 other changes in ElevenLabs updates — 2026-11-02]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-31 · Claude Code · [[Changes/Claude Code/2026-10-31-deprecated-fast-mode-for-opus-4-8-as-of-october-30-2026-it-will-be-removed-on-no|Deprecated fast mode for Opus 4.8 as of October 30, 2026]]
- Later: 2026-11-03 · Google Antigravity · [[Changes/Google Antigravity/2026-11-03-voice-mode-enabled-by-gemini-live-lets-you-talk-to-antigravity-and-hand-requests|Voice mode, enabled by Gemini Live, lets you talk to Antigravity and hand requests…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-11-02-44d2d9&body=Card%3A%20Changes%2FElevenLabs%2F2026-11-02-7-model-support-changes-in-elevenlabs-updates-2026-11-02.md%0ACard%20ID%3A%20elevenlabs-2026-11-02-44d2d9%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F11%2F2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->