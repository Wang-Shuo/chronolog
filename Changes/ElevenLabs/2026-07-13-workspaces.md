---
card_id: elevenlabs-2026-07-13-75a036
date: '2026-07-13'
description: 'ElevenLabs · 2026-07-13 · Collaboration: **Create service accounts**:
  Added [Create service…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1146
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 250a030608930118d9ec112a7271fb751210d7c87ec35f877f7946c69f075d43
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-07-13-75a036
  comparison: ''
  date: '2026-07-13'
  description: 'ElevenLabs — ElevenLabs updates — 2026-07-13: **Create service accounts**:
    Added [Create service account](https://elevenlabs.io/docs/api-reference/service-accounts/create)
    (`POST /v1/service-accounts`) with optional `default_sharing_groups` (`DefaultSharingGroupConfig`)
    for programmatic service-account provisioning.'
  evidence:
  - quote: '**Create service accounts**: Added [Create service account](https://elevenlabs.io/docs/api-reference/service-accounts/create)
      (`POST /v1/service-accounts`) with optional `default_sharing_groups` (`DefaultSharingGroupConfig`)
      for programmatic service-account provisioning.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/13
  - quote: '**List workspace members**: Added [Get workspace members](https://elevenlabs.io/docs/api-reference/workspace/members/list)
      (`GET /v1/workspace/members`) returning `WorkspaceMemberResponseModel` entries
      with user id, email, seat status, owner and locked flags. Service accounts are
      excluded.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/13
  - quote: '**Invite credit caps**: Workspace invite payloads (single and bulk) add
      optional `usage_limit` for a monthly credit cap on invitees.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/13
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: workspaces
  source_release: elevenlabs-2026-07-13-2026-07-13-a5dee32c
  source_type: elevenlabs_changelog
  theme: collaboration
  title: Workspaces
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-07-08-5-collaboration-changes-in-rust-v0-143-0|5 Collaboration
  changes in rust-v0.143.0]]'
- '[[Changes/ChatGPT/2026-07-09-existing-group-chats-will-remain-available-and-can-continue-to-be-used-for-now-w|Existing
  group chats will remain available and can continue to be used for now]]'
- '[[Changes/Codex CLI/2026-07-09-31587-stabilize-shared-rollout-budget-test-jif-oai|♯31587
  Stabilize shared rollout budget test @jif-oai]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-07-13-2026-07-13-a5dee32c|elevenlabs-2026-07-13-2026-07-13-a5dee32c]]'
source_type: elevenlabs_changelog
theme: collaboration
title: Workspaces
type: change
---

<!-- chronolog:begin region="header" -->
# Workspaces

**ElevenLabs** · 2026-07-13 · [[Themes/collaboration|Collaboration]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/7/13) · from [[Releases/ElevenLabs/elevenlabs-2026-07-13-2026-07-13-a5dee32c|ElevenLabs updates — 2026-07-13]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Create service accounts**: Added [Create service account](https://elevenlabs.io/docs/api-reference/service-accounts/create) (`POST /v1/service-accounts`) with optional `default_sharing_groups` (`DefaultSharingGroupConfig`) for programmatic service-account provisioning.
>
> **List workspace members**: Added [Get workspace members](https://elevenlabs.io/docs/api-reference/workspace/members/list) (`GET /v1/workspace/members`) returning `WorkspaceMemberResponseModel` entries with user id, email, seat status, owner and locked flags. Service accounts are excluded.
>
> **Invite credit caps**: Workspace invite payloads (single and bulk) add optional `usage_limit` for a monthly credit cap on invitees.
>
> Source: https://elevenlabs.io/docs/changelog/2026/7/13
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-07-13-python-sdk|Python SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-07-13-packages|Packages]] · Reliability and Performance
- [[Changes/ElevenLabs/2026-07-13-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-07-13-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-07-13-javascript-sdk|JavaScript SDK]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Collaboration

- Earlier: 2026-07-09 · Codex CLI · [[Changes/Codex CLI/2026-07-09-31587-stabilize-shared-rollout-budget-test-jif-oai|♯31587 Stabilize shared rollout budget test @jif-oai]]
- Later: 2026-07-16 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-16-2-collaboration-changes-in-v1-0-71|2 Collaboration changes in v1.0.71]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-24 · ChatGPT · [[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-07-13-75a036&body=Card%3A%20Changes%2FElevenLabs%2F2026-07-13-workspaces.md%0ACard%20ID%3A%20elevenlabs-2026-07-13-75a036%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F7%2F13%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->