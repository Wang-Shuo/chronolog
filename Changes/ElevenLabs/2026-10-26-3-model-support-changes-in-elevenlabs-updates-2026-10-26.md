---
card_id: elevenlabs-2026-10-26-d8ac58
date: '2026-10-26'
description: 'ElevenLabs · 2026-10-26 · Model Support: 3 changes in ElevenLabs updates
  — 2026-10-26 — **Fast LLM service tier**: Agents and workflow overrides accept…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1386
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f1cee62ff27eaa406d9fed5a06a24290f75f239b48a0875b8212b178214d424b
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-10-26-d8ac58
  comparison: ''
  date: '2026-10-26'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-26: 3 Model Support changes'
  evidence:
  - quote: '**Fast LLM service tier**: Agents and workflow overrides accept `service_tier`
      (`standard` or `fast`) on supported models. [List LLMs](https://elevenlabs.io/docs/api-reference/llm/list)
      returns `available_service_tiers` for each model, and the [LLM usage calculator](https://elevenlabs.io/docs/api-reference/llm/calculate)
      accepts `service_tier`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Analysis LLMs**: `claude-sonnet-5-5` can be selected as the analysis
      LLM for evaluation criteria and data collection, both for the agent and per
      item. Agents on Claude Sonnet 5.5 can also set reasoning effort to `none`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Retired models**: Image & Video and Flows requests for a retired model
      fail before generation with a `410` `model_retired` error that names the replacement
      model. Flows preflight reports the error on the affected node.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: elevenlabs
  product_name: ElevenLabs
  slug: 3-model-support-changes-in-elevenlabs-updates-2026-10-26
  source_release: elevenlabs-2026-10-26-2026-10-26-ca7c552d
  source_type: elevenlabs_changelog
  theme: model-support
  title: 3 Model Support changes in ElevenLabs updates — 2026-10-26
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-26-5-model-support-changes-in-v2-1-311|5 Model Support
  changes in v2.1.311]]'
- '[[Changes/Cline/2026-10-26-10-model-support-changes-in-v4-1-26|10 Model Support
  changes in v4.1.26]]'
- '[[Changes/ElevenLabs/2026-10-26-fast-llm-service-tier|Fast LLM service tier]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-26-2026-10-26-ca7c552d|elevenlabs-2026-10-26-2026-10-26-ca7c552d]]'
source_type: elevenlabs_changelog
theme: model-support
title: 3 Model Support changes in ElevenLabs updates — 2026-10-26
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in ElevenLabs updates — 2026-10-26

**ElevenLabs** · 2026-10-26 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://elevenlabs.io/docs/changelog/2026/10/26) · from [[Releases/ElevenLabs/elevenlabs-2026-10-26-2026-10-26-ca7c552d|ElevenLabs updates — 2026-10-26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Fast LLM service tier**: Agents and workflow overrides accept `service_tier` (`standard` or `fast`) on supported models. [List LLMs](https://elevenlabs.io/docs/api-reference/llm/list) returns `available_service_tiers` for each model, and the [LLM usage calculator](https://elevenlabs.io/docs/api-reference/llm/calculate) accepts `service_tier`.

> **Analysis LLMs**: `claude-sonnet-5-5` can be selected as the analysis LLM for evaluation criteria and data collection, both for the agent and per item. Agents on Claude Sonnet 5.5 can also set reasoning effort to `none`.

> **Retired models**: Image & Video and Flows requests for a retired model fail before generation with a `410` `model_retired` error that names the replacement model. Flows preflight reports the error on the affected node.

Source: https://elevenlabs.io/docs/changelog/2026/10/26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-26-2-apps-and-integrations-changes-in-elevenlabs-updates-2026-10-26|2 Apps and Integrations changes in ElevenLabs updates — 2026-10-26]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-26-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-knowledge-base-crawl-exclusions|Knowledge base crawl exclusions]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-26-elevenagents|ElevenAgents]] · Agent Mode
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
- [[Changes/ElevenLabs/2026-10-26-elevenlabs-cli|ElevenLabs CLI]] · Account and Access
- [[Changes/ElevenLabs/2026-10-26-oauth-scope-oauth-clients-can-request-the-realtime-translation-scope|OAuth scope: OAuth clients can request the realtime_translation scope]] · Account and Access
- [[Changes/ElevenLabs/2026-10-26-9-other-changes-in-elevenlabs-updates-2026-10-26|9 other changes in ElevenLabs updates — 2026-10-26]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-26 · Cline · [[Changes/Cline/2026-10-26-10-model-support-changes-in-v4-1-26|10 Model Support changes in v4.1.26]]
- Later: 2026-10-26 · Google Antigravity · [[Changes/Google Antigravity/2026-10-26-gemini-4-argon-refreshed-agent-interface-and-inline-diff-shortcuts|Gemini 4 Argon, Refreshed Agent Interface, and Inline Diff Shortcuts]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-26-d8ac58&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-26-3-model-support-changes-in-elevenlabs-updates-2026-10-26.md%0ACard%20ID%3A%20elevenlabs-2026-10-26-d8ac58%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->