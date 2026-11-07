---
card_id: elevenlabs-2026-06-15-63961e
date: '2026-06-15'
description: 'ElevenLabs · 2026-06-15 · Agent Mode: Workflow override-agent nodes'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1075
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 0f831a5ee2fd6da2d655d08fc319eae944fe844fa50f305634c10b9d5e6430fe
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-06-15-63961e
  comparison: ''
  confidence: low
  date: '2026-06-15'
  description: 'ElevenLabs — ElevenLabs updates — 2026-06-15: Workflow override-agent
    nodes'
  evidence:
  - quote: Workflow override-agent nodes
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: Added optional `entry_behavior` enum (`generate_immediately`, `wait_for_user`,
      `auto`)
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: System tools
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: Added `end_procedure` tool config and error statuses
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: Transfer and interaction schemas
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: Added optional `preserve_client_tts_overrides` on transfers and transfer
      tool results
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: '`InteractionBudget` removes `async`; adds `5_minutes`, `10_minutes`, `1_hour`'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: Guardrails and TTS
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: Custom guardrails add optional `model` and `history_message_count`
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: Agent TTS settings add optional `enable_phoneme_tags`
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: SIP trunk models add optional `enabled_codecs` (`MediaCodec` enum)
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: Memory and code tools
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: Added `LoadableMemoryEntry` and `LoadMemoryEntryToolErrorStatus`
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: Agent testing
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: Raised attached test limits from 1000 to 5000 on run and resubmit requests
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: Tool JSON schema properties
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  - quote: Array properties add optional `is_omitted`
    source_release: https://elevenlabs.io/docs/changelog/2026/6/15
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-06-15-2026-06-15-9835dce0
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-06-13-4-agent-mode-changes-in-v1-0-62|4 Agent
  Mode changes in v1.0.62]]'
- '[[Changes/Claude Code/2026-06-15-2-agent-mode-changes-in-v2-1-178|2 Agent Mode
  changes in v2.1.178]]'
- '[[Changes/Codex CLI/2026-06-15-11-agent-mode-changes-in-rust-v0-140-0|11 Agent
  Mode changes in rust-v0.140.0]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-06-15-2026-06-15-9835dce0|elevenlabs-2026-06-15-2026-06-15-9835dce0]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-06-15 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/6/15) · from [[Releases/ElevenLabs/elevenlabs-2026-06-15-2026-06-15-9835dce0|ElevenLabs updates — 2026-06-15]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Workflow override-agent nodes
>
> Added optional `entry_behavior` enum (`generate_immediately`, `wait_for_user`, `auto`)
>
> System tools
>
> Added `end_procedure` tool config and error statuses
>
> Transfer and interaction schemas
>
> Added optional `preserve_client_tts_overrides` on transfers and transfer tool results
>
> `InteractionBudget` removes `async`; adds `5_minutes`, `10_minutes`, `1_hour`
>
> Guardrails and TTS
>
> Custom guardrails add optional `model` and `history_message_count`
>
> Agent TTS settings add optional `enable_phoneme_tags`
>
> SIP trunk models add optional `enabled_codecs` (`MediaCodec` enum)
>
> Memory and code tools
>
> Added `LoadableMemoryEntry` and `LoadMemoryEntryToolErrorStatus`
>
> Agent testing
>
> Raised attached test limits from 1000 to 5000 on run and resubmit requests
>
> Tool JSON schema properties
>
> Array properties add optional `is_omitted`
>
> Source: https://elevenlabs.io/docs/changelog/2026/6/15
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-06-15-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-15-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-06-15-voices-364b13|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-15-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-15-packages|Packages]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-06-15-workspaces|Workspaces]] · Editor Experience
- [[Changes/ElevenLabs/2026-06-15-elevencreative-studio|ElevenCreative Studio]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-15-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-15-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-15-speech-to-text-d2421e|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-15-ios-sdk|iOS SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-06-15-elevencreative-studio-f3d23d|ElevenCreative Studio]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-15-introducing-music-v2|Introducing Music v2]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-06-15 · Codex CLI · [[Changes/Codex CLI/2026-06-15-11-agent-mode-changes-in-rust-v0-140-0|11 Agent Mode changes in rust-v0.140.0]]
- Later: 2026-06-15 · Kimi Code · [[Changes/Kimi Code/2026-06-15-3-agent-mode-changes-in-kimi-code-0-15-0|3 Agent Mode changes in Kimi Code 0.15.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-06-15-63961e&body=Card%3A%20Changes%2FElevenLabs%2F2026-06-15-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-06-15-63961e%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F6%2F15%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->