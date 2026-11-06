---
card_id: elevenlabs-2026-01-05-5574b8
date: '2026-01-05'
description: 'ElevenLabs · 2026-01-05 · Agent Mode: **Conversation ID in Twilio/SIP
  webhooks**: The `conversation_id` is now included in webhook payloads when fetching…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 914
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 3d48e48ddead835a34c283ba785a48d7049b811abb29324ba78f19dae22fdaac
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-01-05-5574b8
  comparison: ''
  date: '2026-01-05'
  description: 'ElevenLabs — ElevenLabs updates — 2026-01-05: **Conversation ID in
    Twilio/SIP webhooks**: The `conversation_id` is now included in webhook payloads
    when fetching conversation initiation client data for Twilio, SIP, and WhatsApp
    integrations. This enables real-time monitoring without polling the API to retrieve
    conversation IDs.'
  evidence:
  - quote: '**Conversation ID in Twilio/SIP webhooks**: The `conversation_id` is now
      included in webhook payloads when fetching conversation initiation client data
      for Twilio, SIP, and WhatsApp integrations. This enables real-time monitoring
      without polling the API to retrieve conversation IDs.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/5
  - quote: '**Agent versioning fields**: Agent response models now include `version_id`,
      `branch_id`, and `main_branch_id` fields (nullable strings) for tracking agent
      versions and branches.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/5
  - quote: '**Conversation version tracking**: Added `version_id` field to conversation
      models to identify the agent version used for each conversation.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/5
  - quote: '**Batch call enhancements**: The `BatchCallRecipientStatus` enum now includes
      `dispatched` status, and batch call responses include `total_calls_finished`
      field with improved defaults for tracking.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/5
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2026-01-05-2026-01-05-6c816c7e
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/Lovable/2025-12-23-tasks|Tasks]]'
- '[[Changes/Dify/2025-12-25-2-agent-mode-changes-in-1-11-2|2 Agent Mode changes in
  1.11.2]]'
- '[[Changes/GitHub Copilot CLI/2026-01-02-built-in-subagents-for-exploring-and-managing-tasks|Built-in
  subagents for exploring and managing tasks]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-01-05-2026-01-05-6c816c7e|elevenlabs-2026-01-05-2026-01-05-6c816c7e]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2026-01-05 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/1/5) · from [[Releases/ElevenLabs/elevenlabs-2026-01-05-2026-01-05-6c816c7e|ElevenLabs updates — 2026-01-05]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Conversation ID in Twilio/SIP webhooks**: The `conversation_id` is now included in webhook payloads when fetching conversation initiation client data for Twilio, SIP, and WhatsApp integrations. This enables real-time monitoring without polling the API to retrieve conversation IDs.
>
> **Agent versioning fields**: Agent response models now include `version_id`, `branch_id`, and `main_branch_id` fields (nullable strings) for tracking agent versions and branches.
>
> **Conversation version tracking**: Added `version_id` field to conversation models to identify the agent version used for each conversation.
>
> **Batch call enhancements**: The `BatchCallRecipientStatus` enum now includes `dispatched` status, and batch call responses include `total_calls_finished` field with improved defaults for tracking.
>
> Source: https://elevenlabs.io/docs/changelog/2026/1/5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-01-05-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-05-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-05-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-01-05-agents-platform-bdcd71|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2026-01-05-voices|Voices]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-01-02 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-01-02-built-in-subagents-for-exploring-and-managing-tasks|Built-in subagents for exploring and managing tasks]]
- Later: 2026-01-07 · Codex CLI · [[Changes/Codex CLI/2026-01-07-4-agent-mode-changes-in-rust-v0-79-0|4 Agent Mode changes in rust-v0.79.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-01-05-5574b8&body=Card%3A%20Changes%2FElevenLabs%2F2026-01-05-agents-platform.md%0ACard%20ID%3A%20elevenlabs-2026-01-05-5574b8%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F1%2F5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->