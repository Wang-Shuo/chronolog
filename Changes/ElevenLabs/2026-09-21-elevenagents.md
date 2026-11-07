---
card_id: elevenlabs-2026-09-21-5fc350
date: '2026-09-21'
description: 'ElevenLabs · 2026-09-21 · Agent Mode: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
  [Get…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1173
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 19c55387f3722c5a73dfdb79a6ca83afa17663762f48076aefd8608b531f7fbd
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-09-21-5fc350
  comparison: ''
  confidence: low
  date: '2026-09-21'
  description: 'ElevenLabs — ElevenLabs updates — 2026-09-21: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
    [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
  evidence:
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update
      agent](https://elevenlabs.io/docs/api-reference/agents/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/21
  - quote: Prompt configuration adds `enable_parallel_tool_calls` (boolean, default
      `true`). Workflow overrides accept a nullable boolean.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/21
  - quote: The `LLM` enum adds `gpt-6-astra`, including conversation initiation overrides.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/21
  - quote: Alerting integration notifiers now use `integration_type` to select `pagerduty`
      or `slack`. Slack notifiers require `connection_id` and `channel_id` (strings);
      `channel_id` accepts 1–64 characters.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/21
  - quote: '[List conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
      and [Resolve conversation reference](https://elevenlabs.io/docs/api-reference/conversations/resolve)'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/21
  - quote: '`data_collection_params` no longer accepts the `missing` operator. Use
      an empty value to match conversations where the field was not collected.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/21
  - quote: An empty value in `dynamic_variable_params` matches conversations where
      the variable was not set.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/21
  - quote: '[Create Speech Engine](https://elevenlabs.io/docs/api-reference/speech-engine/create),
      [Get Speech Engine](https://elevenlabs.io/docs/api-reference/speech-engine/get)
      and [Update Speech Engine](https://elevenlabs.io/docs/api-reference/speech-engine/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/21
  - quote: Added `cascade_timeout_seconds` (number, 2–15). Create requests default
      to `4`, update requests accept a nullable value and responses require the field.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/21
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-09-21-2026-09-21-6d2d4d80
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-19-you-can-now-set-the-approval-reviewer-s-reasoning-and-optional-fast-mode-indepen|Set
  the approval reviewer''s reasoning and optional Fast mode independently…]]'
- '[[Changes/Devin/2026-09-21-swe-2-research-preview-in-the-agent-selector|SWE-2 Research
  Preview in the Agent Selector]]'
- '[[Changes/Devin/2026-09-21-shell-command-durations-in-the-worklog|Shell Command
  Durations in the Worklog]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-09-21-2026-09-21-6d2d4d80|elevenlabs-2026-09-21-2026-09-21-6d2d4d80]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-09-21 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/9/21) · from [[Releases/ElevenLabs/elevenlabs-2026-09-21-2026-09-21-6d2d4d80|ElevenLabs updates — 2026-09-21]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
>
> Prompt configuration adds `enable_parallel_tool_calls` (boolean, default `true`). Workflow overrides accept a nullable boolean.
>
> The `LLM` enum adds `gpt-6-astra`, including conversation initiation overrides.
>
> Alerting integration notifiers now use `integration_type` to select `pagerduty` or `slack`. Slack notifiers require `connection_id` and `channel_id` (strings); `channel_id` accepts 1–64 characters.
>
> [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list) and [Resolve conversation reference](https://elevenlabs.io/docs/api-reference/conversations/resolve)
>
> `data_collection_params` no longer accepts the `missing` operator. Use an empty value to match conversations where the field was not collected.
>
> An empty value in `dynamic_variable_params` matches conversations where the variable was not set.
>
> [Create Speech Engine](https://elevenlabs.io/docs/api-reference/speech-engine/create), [Get Speech Engine](https://elevenlabs.io/docs/api-reference/speech-engine/get) and [Update Speech Engine](https://elevenlabs.io/docs/api-reference/speech-engine/update)
>
> Added `cascade_timeout_seconds` (number, 2–15). Create requests default to `4`, update requests accept a nullable value and responses require the field.
>
> Source: https://elevenlabs.io/docs/changelog/2026/9/21
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-09-21-image-and-video|Image and video]] · Image Generation
- [[Changes/ElevenLabs/2026-09-21-text-to-speech|Text to Speech]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-21-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-09-21-text-to-speech-576ca6|Text to Speech]] · Model Support
- [[Changes/ElevenLabs/2026-09-21-javascript-sdk|JavaScript SDK]] · Model Support
- [[Changes/ElevenLabs/2026-09-21-python-sdk|Python SDK]] · Model Support
- [[Changes/ElevenLabs/2026-09-21-user|User]] · Pricing Model
- [[Changes/ElevenLabs/2026-09-21-image-and-video-915070|Image and video]] · Image Generation
- [[Changes/ElevenLabs/2026-09-21-elevenagents-d15bdd|ElevenAgents]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-21 · Devin · [[Changes/Devin/2026-09-21-shell-command-durations-in-the-worklog|Shell Command Durations in the Worklog]]
- Later: 2026-09-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-21-show-live-elapsed-time-for-execution-subagents-in-timeline-entries|Show live elapsed time for execution subagents in timeline entries]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-09-21-5fc350&body=Card%3A%20Changes%2FElevenLabs%2F2026-09-21-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-09-21-5fc350%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F9%2F21%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->