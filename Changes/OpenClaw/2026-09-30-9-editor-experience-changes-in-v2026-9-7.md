---
card_id: openclaw-2026-09-30-aa791d
date: '2026-09-30'
description: 'OpenClaw · 2026-09-30 · Editor Experience: 9 changes in v2026.9.7 —
  If a shared configuration file sets the opposite choice, edit that file directly.
  For…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2880
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a276b5f7f89a885ea868f7c34d0b48b6eb20915963b6ad7b0e0e974d273d1079
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-30-aa791d
  comparison: ''
  date: '2026-09-30'
  description: 'OpenClaw — v2026.9.7: 9 Editor Experience changes'
  evidence:
  - quote: If a shared configuration file sets the opposite choice, edit that file
      directly. For remote setup, omit an unused --workspace path if it is invalid
      on the computer running setup.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Split panes restore their own conversations after reload, and chats follow
      history changes made in another tab while keeping unsent drafts. Quoted reply
      drafts also retain their selected quote. Removed queued messages stay hidden
      after reconnect, though their stored content is not erased.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: When Settings rejects a change, it explains why and keeps your edits available
      to correct or retry. Discard draft and reload restores saved settings and removes
      all unsaved configuration edits . If a save’s result is uncertain, return to
      the original Gateway to retry or discard it. Follow any Apply or restart instructions
      before expecting a saved change to take effect.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Live Activity now records only while its view and browser tab are visible,
      for up to 100 accessible active sessions. It misses activity while you are elsewhere
      and starts empty after you leave the page and return. Raw Debug history likewise
      starts when diagnostics open and disappears when the last diagnostic view closes.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Graceful restarts also preserve completed workspace edits and the same
      machine for node-backed cloud and paired-device sessions. Interrupted tool calls
      are not replayed. This does not recover edits already lost in an older version
      or provide the same protection after abrupt machine loss or for SSH-backed sessions.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Skill Workshop refreshes suggestions when you return and removes Apply
      buttons from outdated proposals. If a revision request fails, your saved instructions
      return to the editor so you can try again. Comparison labels now make clear
      which saved version you are viewing changes against.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: A lost machine leaves only the last saved workspace, and forced destruction
      discards unsaved edits. Failed cleanup can leave a machine running and charging
      you. If automatic cleanup gives up, inspect and stop the Crabbox lease, then
      retry Stop in the conversation.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Incognito conversations now expire 24 hours after creation or when the
      Gateway restarts, whichever comes first. Activity does not extend the deadline.
      Expiry stops active work and discards the conversation without an archive, so
      save anything you need beforehand. Reloading or closing the tab also discards
      unsent drafts and attachments.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Closing a browser tab no longer causes false server errors. If access expires
      while a request is waiting, OpenClaw returns an access error or closes a response
      already in progress. Operators investigating connection failures on a shared
      network can use the connection rate-limit guide .
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 9-editor-experience-changes-in-v2026-9-7
  source_release: openclaw-2026-09-30-v2026-9-7-3d25d2bd
  source_type: openclaw_changelog
  theme: editor-experience
  title: 9 Editor Experience changes in v2026.9.7
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-30-improved-the-external-editor-ctrl-g-editors-that-take-a-line-number-now-open-on|Improved
  the external editor (Ctrl+G)]]'
- '[[Changes/Devin/2026-09-30-messages-are-no-longer-lost-when-the-connection-drops|Messages
  Are No Longer Lost When the Connection Drops]]'
- '[[Changes/Devin/2026-09-30-devin-mono-for-code-and-terminals|Devin Mono for Code
  and Terminals]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|openclaw-2026-09-30-v2026-9-7-3d25d2bd]]'
source_type: openclaw_changelog
theme: editor-experience
title: 9 Editor Experience changes in v2026.9.7
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Editor Experience changes in v2026.9.7

**OpenClaw** · 2026-09-30 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.7) · from [[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|v2026.9.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> If a shared configuration file sets the opposite choice, edit that file directly. For remote setup, omit an unused --workspace path if it is invalid on the computer running setup.

> Split panes restore their own conversations after reload, and chats follow history changes made in another tab while keeping unsent drafts. Quoted reply drafts also retain their selected quote. Removed queued messages stay hidden after reconnect, though their stored content is not erased.

> When Settings rejects a change, it explains why and keeps your edits available to correct or retry. Discard draft and reload restores saved settings and removes all unsaved configuration edits . If a save’s result is uncertain, return to the original Gateway to retry or discard it. Follow any Apply or restart instructions before expecting a saved change to take effect.

> Live Activity now records only while its view and browser tab are visible, for up to 100 accessible active sessions. It misses activity while you are elsewhere and starts empty after you leave the page and return. Raw Debug history likewise starts when diagnostics open and disappears when the last diagnostic view closes.

> Graceful restarts also preserve completed workspace edits and the same machine for node-backed cloud and paired-device sessions. Interrupted tool calls are not replayed. This does not recover edits already lost in an older version or provide the same protection after abrupt machine loss or for SSH-backed sessions.

> Skill Workshop refreshes suggestions when you return and removes Apply buttons from outdated proposals. If a revision request fails, your saved instructions return to the editor so you can try again. Comparison labels now make clear which saved version you are viewing changes against.

> A lost machine leaves only the last saved workspace, and forced destruction discards unsaved edits. Failed cleanup can leave a machine running and charging you. If automatic cleanup gives up, inspect and stop the Crabbox lease, then retry Stop in the conversation.

> Incognito conversations now expire 24 hours after creation or when the Gateway restarts, whichever comes first. Activity does not extend the deadline. Expiry stops active work and discards the conversation without an archive, so save anything you need beforehand. Reloading or closing the tab also discards unsent drafts and attachments.

> Closing a browser tab no longer causes false server errors. If access expires while a request is waiting, OpenClaw returns an access error or closes a response already in progress. Operators investigating connection failures on a shared network can use the connection rate-limit guide .

Source: https://docs.openclaw.ai/releases/2026.9.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-30-4-context-window-changes-in-v2026-9-7|4 Context Window changes in v2026.9.7]] · Context Window
- [[Changes/OpenClaw/2026-09-30-13-developer-workflow-changes-in-v2026-9-7|13 Developer Workflow changes in v2026.9.7]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-30-3-files-and-data-changes-in-v2026-9-7|3 Files and Data changes in v2026.9.7]] · Files and Data
- [[Changes/OpenClaw/2026-09-30-13-account-and-access-changes-in-v2026-9-7|13 Account and Access changes in v2026.9.7]] · Account and Access
- [[Changes/OpenClaw/2026-09-30-2-enterprise-and-administration-changes-in-v2026-9-7|2 Enterprise and Administration changes in v2026.9.7]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-30-15-memory-and-personalization-changes-in-v2026-9-7|15 Memory and Personalization changes in v2026.9.7]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-30-33-agent-mode-changes-in-v2026-9-7|33 Agent Mode changes in v2026.9.7]] · Agent Mode
- [[Changes/OpenClaw/2026-09-30-17-interface-experience-changes-in-v2026-9-7|17 Interface Experience changes in v2026.9.7]] · Interface Experience
- [[Changes/OpenClaw/2026-09-30-36-apps-and-integrations-changes-in-v2026-9-7|36 Apps and Integrations changes in v2026.9.7]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-30-2-video-generation-changes-in-v2026-9-7|2 Video Generation changes in v2026.9.7]] · Video Generation
- [[Changes/OpenClaw/2026-09-30-12-voice-and-audio-changes-in-v2026-9-7|12 Voice and Audio changes in v2026.9.7]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-30-21-safety-and-privacy-changes-in-v2026-9-7|21 Safety and Privacy changes in v2026.9.7]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-30-administrators-can-opt-into-heap-snapshots-to-investigate-memory-growth-a-snapsh|Administrators can opt into heap snapshots to investigate memory growth]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-30-14-mobile-and-desktop-changes-in-v2026-9-7|14 Mobile and Desktop changes in v2026.9.7]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-30-22-model-support-changes-in-v2026-9-7|22 Model Support changes in v2026.9.7]] · Model Support
- [[Changes/OpenClaw/2026-09-30-11-automation-and-scheduling-changes-in-v2026-9-7|11 Automation and Scheduling changes in v2026.9.7]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-30-4-search-and-browsing-changes-in-v2026-9-7|4 Search and Browsing changes in v2026.9.7]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-30-3-pricing-model-changes-in-v2026-9-7|3 Pricing Model changes in v2026.9.7]] · Pricing Model
- [[Changes/OpenClaw/2026-09-30-10-collaboration-changes-in-v2026-9-7|10 Collaboration changes in v2026.9.7]] · Collaboration
- [[Changes/OpenClaw/2026-09-30-4-multimodal-input-changes-in-v2026-9-7|4 Multimodal Input changes in v2026.9.7]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-30-72-other-changes-in-v2026-9-7|72 other changes in v2026.9.7]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-09-30 · Devin · [[Changes/Devin/2026-09-30-devin-mono-for-code-and-terminals|Devin Mono for Code and Terminals]]
- Later: 2026-10-01 · AnythingLLM · [[Changes/AnythingLLM/2026-10-01-autosave-workspace-settings-on-edit-by-shatfield4-in-https-github-com-mintplex-l|Autosave workspace settings on edit]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-30-aa791d&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-30-9-editor-experience-changes-in-v2026-9-7.md%0ACard%20ID%3A%20openclaw-2026-09-30-aa791d%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->