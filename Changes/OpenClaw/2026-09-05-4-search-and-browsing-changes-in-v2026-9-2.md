---
card_id: openclaw-2026-09-05-a8738e
date: '2026-09-05'
description: 'OpenClaw · 2026-09-05 · Search and Browsing: 4 changes in v2026.9.2
  — The Dashboard gallery gives saved boards a place you can browse by sight, search
  by task…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1262
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f802331d24994234af159008e7b043d6dcb726b99bd43345e918a1b88f069d4c
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-05-a8738e
  comparison: ''
  date: '2026-09-05'
  description: 'OpenClaw — v2026.9.2: 4 Search and Browsing changes'
  evidence:
  - quote: The Dashboard gallery gives saved boards a place you can browse by sight,
      search by task or author, and sort by title or recent activity, including dashboards
      beyond the first page of conversations. Supported boards show passive previews
      of their saved HTML as you scroll, making it easier to recognize the one you
      want before opening it with its conversation.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Saving a Wiki claim now rejects confidence values outside the supported
      0–1 range before changing the page, preventing those new values from distorting
      later search results. Existing pages remain readable, including older invalid
      values that this change does not repair.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: ClawHub installation also stops with repair or restore guidance when its
      shared tracking file is damaged, preserving the file and existing skills instead
      of replacing their update and integrity records. Normal installation and updates
      can resume after valid tracking is restored. Large archive uploads and library
      browsing also avoid unnecessary copies of archive content or skill payloads,
      while keeping their existing results, selected revisions, and permissions.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Model pickers keep the names, reasoning information, and configured choices
      they already know through more refresh and configuration-reload cases. Native
      Codex models retain their account-scoped availability, repeated browsing can
      reuse discovered inventory when a provider is unavailable, and Hugging Face's
      bundled models remain selectable before a key is added. A listed model still
      needs valid credentials, compatible runtime support, and account access before
      it can answer.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-search-and-browsing-changes-in-v2026-9-2
  source_release: openclaw-2026-09-05-v2026-9-2-377f6d77
  source_type: openclaw_changelog
  theme: search-browsing
  title: 4 Search and Browsing changes in v2026.9.2
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-01-changed-btw-history-browsing-from-to-shift-shift-or-stepping-through-your-recent|Changed
  /btw history browsing from ←/→ to Shift+←/Shift+→ (or /)…]]'
- '[[Changes/OpenClaw/2026-09-01-importing-or-returning-to-a-large-retained-history-also-requires-less-local-work|Importing
  or returning to a large retained history also requires less local work…]]'
- '[[Changes/OpenClaw/2026-09-03-2-search-and-browsing-changes-in-v2026-9-1|2 Search
  and Browsing changes in v2026.9.1]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|openclaw-2026-09-05-v2026-9-2-377f6d77]]'
source_type: openclaw_changelog
theme: search-browsing
title: 4 Search and Browsing changes in v2026.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Search and Browsing changes in v2026.9.2

**OpenClaw** · 2026-09-05 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.2) · from [[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The Dashboard gallery gives saved boards a place you can browse by sight, search by task or author, and sort by title or recent activity, including dashboards beyond the first page of conversations. Supported boards show passive previews of their saved HTML as you scroll, making it easier to recognize the one you want before opening it with its conversation.

> Saving a Wiki claim now rejects confidence values outside the supported 0–1 range before changing the page, preventing those new values from distorting later search results. Existing pages remain readable, including older invalid values that this change does not repair.

> ClawHub installation also stops with repair or restore guidance when its shared tracking file is damaged, preserving the file and existing skills instead of replacing their update and integrity records. Normal installation and updates can resume after valid tracking is restored. Large archive uploads and library browsing also avoid unnecessary copies of archive content or skill payloads, while keeping their existing results, selected revisions, and permissions.

> Model pickers keep the names, reasoning information, and configured choices they already know through more refresh and configuration-reload cases. Native Codex models retain their account-scoped availability, repeated browsing can reuse discovered inventory when a provider is unavailable, and Hugging Face's bundled models remain selectable before a key is added. A listed model still needs valid credentials, compatible runtime support, and account access before it can answer.

Source: https://docs.openclaw.ai/releases/2026.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-05-24-safety-and-privacy-changes-in-v2026-9-2|24 Safety and Privacy changes in v2026.9.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-05-3-pricing-model-changes-in-v2026-9-2|3 Pricing Model changes in v2026.9.2]] · Pricing Model
- [[Changes/OpenClaw/2026-09-05-8-editor-experience-changes-in-v2026-9-2|8 Editor Experience changes in v2026.9.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-05-progress-mode-can-stay-quiet-about-routine-tool-calls-while-keeping-the-updates|Progress mode can stay quiet about routine tool calls while keeping the updates…]] · Presentation Creation
- [[Changes/OpenClaw/2026-09-05-swarm-is-now-available-to-eligible-agents-without-a-separate-enablement-step-so|Swarm is now available to eligible agents without a separate enablement step…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-a-rejected-send-can-keep-its-original-attachments-and-retry-action-when-you-leav|A rejected send can keep its original attachments and Retry action when you leave…]] · Files and Data
- [[Changes/OpenClaw/2026-09-05-20-account-and-access-changes-in-v2026-9-2|20 Account and Access changes in v2026.9.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-05-17-model-support-changes-in-v2026-9-2|17 Model Support changes in v2026.9.2]] · Model Support
- [[Changes/OpenClaw/2026-09-05-16-developer-workflow-changes-in-v2026-9-2|16 Developer Workflow changes in v2026.9.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-21-memory-and-personalization-changes-in-v2026-9-2|21 Memory and Personalization changes in v2026.9.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-05-4-enterprise-and-administration-changes-in-v2026-9-2|4 Enterprise and Administration changes in v2026.9.2]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-05-if-background-image-video-or-music-generation-finishes-but-final-delivery-fails|If background image, video or music generation finishes but final delivery fails…]] · Music Generation
- [[Changes/OpenClaw/2026-09-05-34-agent-mode-changes-in-v2026-9-2|34 Agent Mode changes in v2026.9.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-35-apps-and-integrations-changes-in-v2026-9-2|35 Apps and Integrations changes in v2026.9.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-05-8-automation-and-scheduling-changes-in-v2026-9-2|8 Automation and Scheduling changes in v2026.9.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-05-9-collaboration-changes-in-v2026-9-2|9 Collaboration changes in v2026.9.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-05-10-mobile-and-desktop-changes-in-v2026-9-2|10 Mobile and Desktop changes in v2026.9.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-05-15-context-window-changes-in-v2026-9-2|15 Context Window changes in v2026.9.2]] · Context Window
- [[Changes/OpenClaw/2026-09-05-17-voice-and-audio-changes-in-v2026-9-2|17 Voice and Audio changes in v2026.9.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-05-21-interface-experience-changes-in-v2026-9-2|21 Interface Experience changes in v2026.9.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-05-3-reliability-and-performance-changes-in-v2026-9-2|3 Reliability and Performance changes in v2026.9.2]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-05-you-can-now-put-the-part-of-a-task-you-are-working-on-in-the-main-view-and-keep|Put the part of a task you are working on in the main view and keep the conversation…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-72-other-changes-in-v2026-9-2|72 other changes in v2026.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-09-03 · OpenClaw · [[Changes/OpenClaw/2026-09-03-2-search-and-browsing-changes-in-v2026-9-1|2 Search and Browsing changes in v2026.9.1]]
- Later: 2026-09-08 · OpenClaw · [[Changes/OpenClaw/2026-09-08-3-search-and-browsing-changes-in-v2026-9-3|3 Search and Browsing changes in v2026.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-05-a8738e&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-05-4-search-and-browsing-changes-in-v2026-9-2.md%0ACard%20ID%3A%20openclaw-2026-09-05-a8738e%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->