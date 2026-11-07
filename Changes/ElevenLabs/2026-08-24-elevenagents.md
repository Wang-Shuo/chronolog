---
card_id: elevenlabs-2026-08-24-3d1765
date: '2026-08-24'
description: 'ElevenLabs · 2026-08-24 · Agent Mode: Agent update requests add optional
  nullable `procedures` (`object`). Each value requires `procedure_id` and `version_id`…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1145
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 65d324fa110431aa75d0f484a7d18885cd46bc7d3780d7d0e2023b8d32cb4170
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-08-24-3d1765
  comparison: ''
  confidence: low
  date: '2026-08-24'
  description: 'ElevenLabs — ElevenLabs updates — 2026-08-24: Agent update requests
    add optional nullable `procedures` (`object`). Each value requires `procedure_id`
    and `version_id` (strings). An empty object removes all procedures.'
  evidence:
  - quote: Agent update requests add optional nullable `procedures` (`object`). Each
      value requires `procedure_id` and `version_id` (strings). An empty object removes
      all procedures.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Conversation initiation configuration adds `enable_procedure_ids_from_client`
      (boolean, default `false`). Initiation data adds optional nullable `procedure_ids`
      (string array); an empty array disables all procedures for the starting agent.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: '`ClientEvent` adds `context_usage`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Soft-timeout overrides add optional nullable `additional_soft_timeout_messages`
      (string array).
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Constant values in analysis and schema override models now accept `null`.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  - quote: Widget configuration defaults for `mic_muting_enabled` and `transcript_enabled`
      changed from `false` to `true`. Set them explicitly to `false` to preserve the
      previous behavior.
    source_release: https://elevenlabs.io/docs/changelog/2026/8/24
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-08-24-2026-08-24-b7c01132
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Replit/2026-08-21-agent|Agent]]'
- '[[Changes/Replit/2026-08-21-steer-agent-while-working|Steer Agent while working]]'
- '[[Changes/Cline/2026-08-22-carry-session-and-client-identity-into-langfuse-traces-for-hub-backed-and-delega|Carry
  session and client identity into Langfuse traces for Hub-backed…]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-08-24-2026-08-24-b7c01132|elevenlabs-2026-08-24-2026-08-24-b7c01132]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-08-24 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/8/24) · from [[Releases/ElevenLabs/elevenlabs-2026-08-24-2026-08-24-b7c01132|ElevenLabs updates — 2026-08-24]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Agent update requests add optional nullable `procedures` (`object`). Each value requires `procedure_id` and `version_id` (strings). An empty object removes all procedures.
>
> Conversation initiation configuration adds `enable_procedure_ids_from_client` (boolean, default `false`). Initiation data adds optional nullable `procedure_ids` (string array); an empty array disables all procedures for the starting agent.
>
> `ClientEvent` adds `context_usage`.
>
> Soft-timeout overrides add optional nullable `additional_soft_timeout_messages` (string array).
>
> Constant values in analysis and schema override models now accept `null`.
>
> Widget configuration defaults for `mic_muting_enabled` and `transcript_enabled` changed from `false` to `true`. Set them explicitly to `false` to preserve the previous behavior.
>
> Source: https://elevenlabs.io/docs/changelog/2026/8/24
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-08-24-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-08-24-swift-sdk|Swift SDK]] · Pricing Model
- [[Changes/ElevenLabs/2026-08-24-javascript-sdk|JavaScript SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-08-24-packages|Packages]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-08-24-procedures|Procedures]] · Agent Mode
- [[Changes/ElevenLabs/2026-08-24-elevenagents-a7877c|ElevenAgents]] · Reliability and Performance
- [[Changes/ElevenLabs/2026-08-24-elevenlabs-cli|ElevenLabs CLI]] · Editor Experience
- [[Changes/ElevenLabs/2026-08-24-python-sdk|Python SDK]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-08-22 · Cline · [[Changes/Cline/2026-08-22-carry-session-and-client-identity-into-langfuse-traces-for-hub-backed-and-delega|Carry session and client identity into Langfuse traces for Hub-backed…]]
- Later: 2026-08-25 · Claude Code · [[Changes/Claude Code/2026-08-25-improved-subagent-results-a-subagent-that-stops-at-its-maxturns-limit-now-return|Improved subagent results]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-08-24-3d1765&body=Card%3A%20Changes%2FElevenLabs%2F2026-08-24-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-08-24-3d1765%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F8%2F24%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->