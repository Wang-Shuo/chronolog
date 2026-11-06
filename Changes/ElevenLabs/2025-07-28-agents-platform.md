---
card_id: elevenlabs-2025-07-28-2f7a74
date: '2025-07-28'
description: 'ElevenLabs · 2025-07-28 · Agent Mode: **Post-call webhook migration**:
  The post call webhook format is being migrated so that webhook handlers can be auto…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 753
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: bf1584424e06aa48c0cdc73e1fca91073cabebb65d598e6395696f84128b9205
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2025-07-28-2f7a74
  comparison: ''
  date: '2025-07-28'
  description: 'ElevenLabs — ElevenLabs updates — 2025-07-28: **Post-call webhook
    migration**: The post call webhook format is being migrated so that webhook handlers
    can be auto generated in the SDKs. This is not a breaking change, and no further
    action is required if your current handler accepts additional fields. Please see
    more information [here](https://elevenlabs.io/docs/eleven-agents/workflows/post-call-webhooks#migration-notice-enhanced-webhook-format).'
  evidence:
  - quote: '**Post-call webhook migration**: The post call webhook format is being
      migrated so that webhook handlers can be auto generated in the SDKs. This is
      not a breaking change, and no further action is required if your current handler
      accepts additional fields. Please see more information [here](https://elevenlabs.io/docs/eleven-agents/workflows/post-call-webhooks#migration-notice-enhanced-webhook-format).'
    source_release: https://elevenlabs.io/docs/changelog/2025/7/28
  - quote: '**Agent transfer improvements**: Fixed system variable `system_agent_id`
      to properly update after agent-to-agent transfers, ensuring accurate conversation
      context tracking. Added new `system_current_agent_id` variable for tracking
      current active agent. Learn more about [dynamic variables](https://elevenlabs.io/docs/eleven-agents/customization/personalization/dynamic-variables#system-dynamic-variables).'
    source_release: https://elevenlabs.io/docs/changelog/2025/7/28
  - quote: '**Enhanced public agent page**: Added text input functionality and dynamic
      variable support to the public talk-to-agent page. You can now pass dynamic
      variables via URL parameters (e.g., `?var_username=value`) and use text input
      during voice conversations. See [dynamic variables guide](https://elevenlabs.io/docs/eleven-agents/customization/personalization/dynamic-variables#public-talk-to-page-integration).'
    source_release: https://elevenlabs.io/docs/changelog/2025/7/28
  - quote: '**Voicemail detection**: Added voicemail detection as a built-in tool
      for ElevenLabs agents to improve call handling. Learn about [voicemail detection](https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/voicemail-detection).'
    source_release: https://elevenlabs.io/docs/changelog/2025/7/28
  - quote: '**Conversation filtering**: Added `user_id` query parameter to [conversation
      list endpoint](https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/list#request.query.user_id.user_id)
      for filtering conversations by initiating user.'
    source_release: https://elevenlabs.io/docs/changelog/2025/7/28
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2025-07-28-2025-07-28-ee33c25b
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/OpenHands/2025-07-24-2-agent-mode-changes-in-0-50-0|2 Agent Mode changes
  in 0.50.0]]'
- '[[Changes/Gemini CLI/2025-07-25-5-agent-mode-changes-in-v0-1-14|5 Agent Mode changes
  in v0.1.14]]'
- '[[Changes/Replit/2025-07-25-queue|Queue]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2025-07-28-2025-07-28-ee33c25b|elevenlabs-2025-07-28-2025-07-28-ee33c25b]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2025-07-28 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2025/7/28) · from [[Releases/ElevenLabs/elevenlabs-2025-07-28-2025-07-28-ee33c25b|ElevenLabs updates — 2025-07-28]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Post-call webhook migration**: The post call webhook format is being migrated so that webhook handlers can be auto generated in the SDKs. This is not a breaking change, and no further action is required if your current handler accepts additional fields. Please see more information [here](https://elevenlabs.io/docs/eleven-agents/workflows/post-call-webhooks#migration-notice-enhanced-webhook-format).
>
> **Agent transfer improvements**: Fixed system variable `system_agent_id` to properly update after agent-to-agent transfers, ensuring accurate conversation context tracking. Added new `system_current_agent_id` variable for tracking current active agent. Learn more about [dynamic variables](https://elevenlabs.io/docs/eleven-agents/customization/personalization/dynamic-variables#system-dynamic-variables).
>
> **Enhanced public agent page**: Added text input functionality and dynamic variable support to the public talk-to-agent page. You can now pass dynamic variables via URL parameters (e.g., `?var_username=value`) and use text input during voice conversations. See [dynamic variables guide](https://elevenlabs.io/docs/eleven-agents/customization/personalization/dynamic-variables#public-talk-to-page-integration).
>
> **Voicemail detection**: Added voicemail detection as a built-in tool for ElevenLabs agents to improve call handling. Learn about [voicemail detection](https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/voicemail-detection).
>
> **Conversation filtering**: Added `user_id` query parameter to [conversation list endpoint](https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/list#request.query.user_id.user_id) for filtering conversations by initiating user.
>
> Source: https://elevenlabs.io/docs/changelog/2025/7/28
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2025-07-28-agents-platform-504721|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2025-07-28-sdks|SDKs]] · Apps and Integrations
- [[Changes/ElevenLabs/2025-07-28-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2025-07-28-text-to-voice|Text to Voice]] · Voice and Audio
- [[Changes/ElevenLabs/2025-07-28-speech-to-text-b64b2f|Speech to Text]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2025-07-25 · Replit · [[Changes/Replit/2025-07-25-queue|Queue]]
- Later: 2025-07-29 · Cursor · [[Changes/Cursor/2025-07-29-agents-can-now-use-your-native-terminal-a-new-terminal-will-be-created-when-need|Share terminal with Agent]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2025-07-28-2f7a74&body=Card%3A%20Changes%2FElevenLabs%2F2025-07-28-agents-platform.md%0ACard%20ID%3A%20elevenlabs-2025-07-28-2f7a74%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2025%2F7%2F28%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->