---
card_id: elevenlabs-2026-02-02-34be4c
date: '2026-02-02'
description: 'ElevenLabs · 2026-02-02 · Safety and Privacy: **Permission clarifications**:
  Workspace group and invite endpoints now document specific permission requirements…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1023
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: eedc24afba3e4d6848d5c83199f90ec33447316e3619d83feb52e056611af199
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-02-02-34be4c
  comparison: ''
  date: '2026-02-02'
  description: 'ElevenLabs — ElevenLabs updates — 2026-02-02: **Permission clarifications**:
    Workspace group and invite endpoints now document specific permission requirements
    (`group_members_manage` for group member operations, `WORKSPACE_MEMBERS_INVITE`
    for workspace invitations) instead of requiring workspace administrator status.'
  evidence:
  - quote: '**Permission clarifications**: Workspace group and invite endpoints now
      document specific permission requirements (`group_members_manage` for group
      member operations, `WORKSPACE_MEMBERS_INVITE` for workspace invitations) instead
      of requiring workspace administrator status.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: '**New permission types**: Added `group_members_manage` and `terms_of_service_accept`
      to the `PermissionType` enum.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: workspaces
  source_release: elevenlabs-2026-02-02-2026-02-02-2180766f
  source_type: elevenlabs_changelog
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Workspaces
  type: change
related_changes:
- '[[Changes/Claude Code/2026-01-30-permissions-now-respect-content-level-ask-over-tool-level-allow-previously-allow|Permissions
  now respect content-level ask over tool-level allow]]'
- '[[Changes/GitHub Copilot CLI/2026-01-30-acp-server-support-permission-flags-yolo-allow-all-etc-and-permissions-config|ACP
  server support permission flags: --yolo, --allow-all, etc. and permissions config]]'
- '[[Changes/Codex CLI/2026-01-31-4-safety-and-privacy-changes-in-rust-v0-93-0|4 Safety
  and Privacy changes in rust-v0.93.0]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-02-02-2026-02-02-2180766f|elevenlabs-2026-02-02-2026-02-02-2180766f]]'
source_type: elevenlabs_changelog
theme: safety-privacy
title: Workspaces
type: change
---

<!-- chronolog:begin region="header" -->
# Workspaces

**ElevenLabs** · 2026-02-02 · [[Themes/safety-privacy|Safety and Privacy]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/2/2) · from [[Releases/ElevenLabs/elevenlabs-2026-02-02-2026-02-02-2180766f|ElevenLabs updates — 2026-02-02]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Permission clarifications**: Workspace group and invite endpoints now document specific permission requirements (`group_members_manage` for group member operations, `WORKSPACE_MEMBERS_INVITE` for workspace invitations) instead of requiring workspace administrator status.
>
> **New permission types**: Added `group_members_manage` and `terms_of_service_accept` to the `PermissionType` enum.
>
> Source: https://elevenlabs.io/docs/changelog/2026/2/2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-02-02-new-schemas|New Schemas]] · Voice and Audio
- [[Changes/ElevenLabs/2026-02-02-python-sdk|Python SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-02-02-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-02-02-eleven-v3|Eleven v3]] · Reliability and Performance
- [[Changes/ElevenLabs/2026-02-02-text-to-dialogue|Text-to-Dialogue]] · Model Support
- [[Changes/ElevenLabs/2026-02-02-widget-packages|Widget Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-02-02-javascript-sdk|JavaScript SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-02-02-react-and-client-sdks|React and Client SDKs]] · Voice and Audio
- [[Changes/ElevenLabs/2026-02-02-user|User]] · Model Support
- [[Changes/ElevenLabs/2026-02-02-agents-platform|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2026-02-02-agents-platform-fb792c|Agents Platform]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-01-31 · Codex CLI · [[Changes/Codex CLI/2026-01-31-4-safety-and-privacy-changes-in-rust-v0-93-0|4 Safety and Privacy changes in rust-v0.93.0]]
- Later: 2026-02-02 · OpenHands · [[Changes/OpenHands/2026-02-02-2-safety-and-privacy-changes-in-1-3-0|2 Safety and Privacy changes in 1.3.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-02-02-34be4c&body=Card%3A%20Changes%2FElevenLabs%2F2026-02-02-workspaces.md%0ACard%20ID%3A%20elevenlabs-2026-02-02-34be4c%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F2%2F2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->