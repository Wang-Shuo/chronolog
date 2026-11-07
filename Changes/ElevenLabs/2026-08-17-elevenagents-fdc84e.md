---
card_id: elevenlabs-2026-08-17-fdc84e
date: '2026-08-17'
description: 'ElevenLabs · 2026-08-17 · Agent Mode: Added optional `queueing` (`AgentQueueingConfig`)
  to agent platform settings. It contains `enabled` (boolean, default…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1138
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 8712871c7db8a45d81675cf91a1f7a428d2981dab24419c9e55f8d743772e166
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-08-17-fdc84e
  comparison: ''
  confidence: low
  date: '2026-08-17'
  description: 'ElevenLabs — ElevenLabs updates — 2026-08-17: Added optional `queueing`
    (`AgentQueueingConfig`) to agent platform settings. It contains `enabled` (boolean,
    default `false`) and `wait_timeout_seconds` (integer greater than 0 and at most
    1,800, default `180`)'
  evidence:
  - quote: Added optional `queueing` (`AgentQueueingConfig`) to agent platform settings.
      It contains `enabled` (boolean, default `false`) and `wait_timeout_seconds`
      (integer greater than 0 and at most 1,800, default `180`)
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  - quote: Added optional `schema_overrides` to `WorkflowToolLocator`; per-node constant,
      dynamic variable, LLM or omit overrides take precedence over tool-level overrides
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  - quote: Added `merge_with_default_ignore_terms` (boolean, default `false`) to turn
      configuration and related override schemas
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  - quote: Added `disable_until_first_user_message` (boolean, default `false`) to
      soft-timeout configuration and related override schemas
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  - quote: Added required read-only `status` (`success`, `error`, `blocked` or `skipped`)
      to realtime agent tool response events
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  - quote: Added `avaya` to conversation initiation sources and `avaya_api_key` to
      authorization methods
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  - quote: Added `gemini-3.6-flash` and `gemini-3.7-flash` to supported agent LLM
      values
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  - quote: Changed `BackgroundSoundConfig.volume` default from `0.6` to `0.15` and
      `crossfade_loop` default from `false` to `true`
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  - quote: Removed `CustomToolApiSchemaConfig`; generated SDK users importing this
      type must remove the import
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  - quote: Removed `scim_external_id` from `WorkspaceGroupResponseModel`
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-08-17-2026-08-17-6196d42b
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-17-removed-the-redundant-allowed-by-auto-mode-classifier-line-that-auto-mode-showed|Removed
  the redundant "Allowed by auto mode classifier" line that auto mode showed…]]'
- '[[Changes/Cursor/2026-08-17-agents-in-every-repo|Agents in every repo]]'
- '[[Changes/ElevenLabs/2026-08-17-elevenagents|ElevenAgents]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-08-17-2026-08-17-6196d42b|elevenlabs-2026-08-17-2026-08-17-6196d42b]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-08-17 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/8/17) · from [[Releases/ElevenLabs/elevenlabs-2026-08-17-2026-08-17-6196d42b|ElevenLabs updates — 2026-08-17]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added optional `queueing` (`AgentQueueingConfig`) to agent platform settings. It contains `enabled` (boolean, default `false`) and `wait_timeout_seconds` (integer greater than 0 and at most 1,800, default `180`)
>
> Added optional `schema_overrides` to `WorkflowToolLocator`; per-node constant, dynamic variable, LLM or omit overrides take precedence over tool-level overrides
>
> Added `merge_with_default_ignore_terms` (boolean, default `false`) to turn configuration and related override schemas
>
> Added `disable_until_first_user_message` (boolean, default `false`) to soft-timeout configuration and related override schemas
>
> Added required read-only `status` (`success`, `error`, `blocked` or `skipped`) to realtime agent tool response events
>
> Added `avaya` to conversation initiation sources and `avaya_api_key` to authorization methods
>
> Added `gemini-3.6-flash` and `gemini-3.7-flash` to supported agent LLM values
>
> Changed `BackgroundSoundConfig.volume` default from `0.6` to `0.15` and `crossfade_loop` default from `false` to `true`
>
> Removed `CustomToolApiSchemaConfig`; generated SDK users importing this type must remove the import
>
> Removed `scim_external_id` from `WorkspaceGroupResponseModel`
>
> Source: https://elevenlabs.io/docs/changelog/2026/8/17
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-08-17-python-sdk|Python SDK]] · Multimodal Input
- [[Changes/ElevenLabs/2026-08-17-elevencreative|ElevenCreative]] · Editor Experience
- [[Changes/ElevenLabs/2026-08-17-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-08-17-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-08-17-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-08-17-javascript-sdk|JavaScript SDK]] · Multimodal Input
- [[Changes/ElevenLabs/2026-08-17-elevencreative-fd6a14|ElevenCreative]] · Multimodal Input
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-08-17 · Cursor · [[Changes/Cursor/2026-08-17-agents-in-every-repo|Agents in every repo]]
- Later: 2026-08-17 · OpenHands · [[Changes/OpenHands/2026-08-17-docs-agents-add-a-repository-map-clarifying-what-belongs-where-by-smolpaws-in-ht|docs(agents): add a repository map clarifying what belongs where]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-08-17-fdc84e&body=Card%3A%20Changes%2FElevenLabs%2F2026-08-17-elevenagents-fdc84e.md%0ACard%20ID%3A%20elevenlabs-2026-08-17-fdc84e%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F8%2F17%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->