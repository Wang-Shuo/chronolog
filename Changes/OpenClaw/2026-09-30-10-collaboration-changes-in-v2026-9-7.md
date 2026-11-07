---
card_id: openclaw-2026-09-30-f39749
date: '2026-09-30'
description: 'OpenClaw · 2026-09-30 · Collaboration: 10 changes in v2026.9.7 — Shared
  networks have more room for simultaneous connection attempts, with the default…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1225
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 00b8c8f769e1c1160ae37972fbe419ca73620203b49f43e04ff0b84852215078
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-30-f39749
  comparison: ''
  date: '2026-09-30'
  description: 'OpenClaw — v2026.9.7: 10 Collaboration changes'
  evidence:
  - quote: Shared networks have more room for simultaneous connection attempts, with
      the default allowance rising from 32 to 128 pending, unauthenticated connections
      per IP. That permits more sockets to consume server resources; administrators
      can lower the allowance . A retry countdown shows when the browser will try
      again after OpenClaw answers an HTTP check. The busy message does not diagnose
      the failed connection, so persistent problems still need connection troubleshooting
      .
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: In shared turns, specify whose screen or theme should change. Other personal
      settings need a new personal turn. The original owner’s permissions, approvals,
      and provider account still apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Shared chats show two full draft previews and summarize additional people
      typing in a compact row. Paused previews fade away, and resumed typing keeps
      its place. These are temporary previews of unsent text, not saved messages.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Telegram, Feishu, Teams, and Nextcloud Talk can receive webhooks on the
      Gateway's HTTP port. Follow Doctor's migration guidance , update your external
      callback or proxy, and verify incoming messages before setting legacyWebhook
      to false . Keep that setting to leave the old port closed. Telegram polling
      and Feishu WebSocket connections are unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Choose View transcript on a run to read its conversation and load earlier
      messages. Isolated runs show their own conversation; custom-session jobs show
      the conversation shared across runs. Run history remains available after Tasks
      retirement, and the sessions CLI can archive or delete a stored run by its exact
      key. Retention limits are unchanged, and previously deleted history is not restored.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Team Reports keeps existing daily, weekly, and monthly reports when GitHub
      or Discord collection fails. A first failed collection leaves the affected period
      unpublished. Check status warnings and regenerate the affected day once access
      returns. Report generation moves more work into the background. After changing
      Discord channels or collection filters, manually regenerate affected days so
      those changes are included.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Chat can start while Session Share waits for a slow paired source, with
      available sessions appearing when the list arrives. Resetting or deleting a
      session no longer shuts down ClickClack discussions elsewhere, and Workboard
      action menus size themselves to their contents.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Administrators can merge duplicate user profiles , including profiles without
      email addresses, with openclaw users merge <source-profile-id> --into <target-profile-id>
      . The target keeps its role and conflicting preferences; old permissions do
      not transfer and historical records keep their original identities. Move personal
      USER.md files manually and expect affected clients to reconnect. The shared
      Owner profile cannot be merged.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: OpenClaw does less repeated processing while displaying replies and sharing
      progress updates. Very large updates also avoid extra work once they exceed
      what can be replayed after a reconnect.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Worker chats keep their workspace through automatic daily or idle resets,
      so they can continue replying there. This does not change /new or /reset , or
      restore workspaces already disconnected from a chat. A stuck cloud worker also
      no longer blocks unrelated sessions, though work sharing a session or environment
      may still wait.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 10-collaboration-changes-in-v2026-9-7
  source_release: openclaw-2026-09-30-v2026-9-7-3d25d2bd
  source_type: openclaw_changelog
  theme: collaboration
  title: 10 Collaboration changes in v2026.9.7
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-29-your-chatgpt-profile-now-brings-together-your-bio-activity-and-sites-you-choose-09d5dd|Share
  your profile and showcase your Sites]]'
- '[[Changes/ChatGPT/2026-09-29-space-brings-your-pages-files-and-related-work-together-in-chatgpt-create-a-spac|Organize
  your work in ChatGPT Space]]'
- '[[Changes/Codex CLI/2026-09-29-2-collaboration-changes-in-rust-v0-159-0|2 Collaboration
  changes in rust-v0.159.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|openclaw-2026-09-30-v2026-9-7-3d25d2bd]]'
source_type: openclaw_changelog
theme: collaboration
title: 10 Collaboration changes in v2026.9.7
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Collaboration changes in v2026.9.7

**OpenClaw** · 2026-09-30 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.7) · from [[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|v2026.9.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Shared networks have more room for simultaneous connection attempts, with the default allowance rising from 32 to 128 pending, unauthenticated connections per IP. That permits more sockets to consume server resources; administrators can lower the allowance . A retry countdown shows when the browser will try again after OpenClaw answers an HTTP check. The busy message does not diagnose the failed connection, so persistent problems still need connection troubleshooting .

> In shared turns, specify whose screen or theme should change. Other personal settings need a new personal turn. The original owner’s permissions, approvals, and provider account still apply.

> Shared chats show two full draft previews and summarize additional people typing in a compact row. Paused previews fade away, and resumed typing keeps its place. These are temporary previews of unsent text, not saved messages.

> Telegram, Feishu, Teams, and Nextcloud Talk can receive webhooks on the Gateway's HTTP port. Follow Doctor's migration guidance , update your external callback or proxy, and verify incoming messages before setting legacyWebhook to false . Keep that setting to leave the old port closed. Telegram polling and Feishu WebSocket connections are unchanged.

> Choose View transcript on a run to read its conversation and load earlier messages. Isolated runs show their own conversation; custom-session jobs show the conversation shared across runs. Run history remains available after Tasks retirement, and the sessions CLI can archive or delete a stored run by its exact key. Retention limits are unchanged, and previously deleted history is not restored.

> Team Reports keeps existing daily, weekly, and monthly reports when GitHub or Discord collection fails. A first failed collection leaves the affected period unpublished. Check status warnings and regenerate the affected day once access returns. Report generation moves more work into the background. After changing Discord channels or collection filters, manually regenerate affected days so those changes are included.

> Chat can start while Session Share waits for a slow paired source, with available sessions appearing when the list arrives. Resetting or deleting a session no longer shuts down ClickClack discussions elsewhere, and Workboard action menus size themselves to their contents.

> Administrators can merge duplicate user profiles , including profiles without email addresses, with openclaw users merge \<source-profile-id> --into \<target-profile-id> . The target keeps its role and conflicting preferences; old permissions do not transfer and historical records keep their original identities. Move personal USER.md files manually and expect affected clients to reconnect. The shared Owner profile cannot be merged.

> OpenClaw does less repeated processing while displaying replies and sharing progress updates. Very large updates also avoid extra work once they exceed what can be replayed after a reconnect.

> Worker chats keep their workspace through automatic daily or idle resets, so they can continue replying there. This does not change /new or /reset , or restore workspaces already disconnected from a chat. A stuck cloud worker also no longer blocks unrelated sessions, though work sharing a session or environment may still wait.

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
- [[Changes/OpenClaw/2026-09-30-9-editor-experience-changes-in-v2026-9-7|9 Editor Experience changes in v2026.9.7]] · Editor Experience
- [[Changes/OpenClaw/2026-09-30-22-model-support-changes-in-v2026-9-7|22 Model Support changes in v2026.9.7]] · Model Support
- [[Changes/OpenClaw/2026-09-30-11-automation-and-scheduling-changes-in-v2026-9-7|11 Automation and Scheduling changes in v2026.9.7]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-30-4-search-and-browsing-changes-in-v2026-9-7|4 Search and Browsing changes in v2026.9.7]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-30-3-pricing-model-changes-in-v2026-9-7|3 Pricing Model changes in v2026.9.7]] · Pricing Model
- [[Changes/OpenClaw/2026-09-30-4-multimodal-input-changes-in-v2026-9-7|4 Multimodal Input changes in v2026.9.7]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-30-72-other-changes-in-v2026-9-7|72 other changes in v2026.9.7]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Collaboration

- Earlier: 2026-09-29 · Codex CLI · [[Changes/Codex CLI/2026-09-29-2-collaboration-changes-in-rust-v0-159-0|2 Collaboration changes in rust-v0.159.0]]
- Later: 2026-10-01 · Codex CLI · [[Changes/Codex CLI/2026-10-01-49130-move-content-filter-guidance-into-the-shared-responses-retry-handler-won-o|♯49130 Move content-filter guidance into the shared Responses retry handler @won-openai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-24 · ChatGPT · [[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-30-f39749&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-30-10-collaboration-changes-in-v2026-9-7.md%0ACard%20ID%3A%20openclaw-2026-09-30-f39749%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->