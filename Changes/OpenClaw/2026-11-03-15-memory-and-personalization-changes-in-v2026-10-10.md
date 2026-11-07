---
card_id: openclaw-2026-11-03-814e52
date: '2026-11-03'
description: 'OpenClaw · 2026-11-03 · Memory and Personalization: 15 changes in v2026.10.10
  — There’s plenty beyond those highlights, with hundreds of improvements and fixes…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1202
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 60fe83d7fc70e5c6ad38dbb002917eb32dab26450f52cec62d36c75e80521e8e
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-11-03-814e52
  comparison: ''
  date: '2026-11-03'
  description: 'OpenClaw — v2026.10.10: 15 Memory and Personalization changes'
  evidence:
  - quote: There’s plenty beyond those highlights, with hundreds of improvements and
      fixes for everyday chats, memory search, automations, coding agents and connected
      devices.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Memory indexing now batches conversation updates after a quiet period instead
      of repeatedly working during active turns. Recent conversation text may therefore
      take longer to appear in memory search.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Agent preparation and long conversations use less memory and repeat less
      work, especially when many agents or models are configured.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Starting OpenClaw no longer opens every agent's memory index at once. Each
      index opens when needed, while plugin reloads resume indexing that was already
      active.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Memory search can find notes that a natural-language question previously
      missed, keep relevant older dated notes eligible and rank weak keyword matches
      below closer matches in meaning. These are improvements to existing search,
      not a guarantee that every exact match comes first. If you set a minimum search
      score yourself, lower it if useful results disappear after the ranking change.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Memory search now explains more embedding-provider failures and keeps a
      previously usable index available when rebuilding fails. After a database worker
      stops, a later request can reopen the existing index, although searches during
      recovery can still fail.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Memory reads through the CLI and supported plugins now reach the intended
      agent’s permitted notes more consistently, while private or untrusted content
      remains subject to its existing access checks.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: During memory setup, you can optionally test an embedding provider and
      model before saving them. Skipping or failing the check leaves existing settings
      intact, and interrupted import setup can return to its result and Continue action.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Memory embedding requests now respect the chosen provider’s private-network
      rules, including when a service redirects to a private address. If your embedding
      service depends on that route, you may need to allow it explicitly; invalid
      Google or LM Studio headers identify the affected setting.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Memory Wiki now finds matching filenames without scanning every page in
      those searches, matches equivalent Unicode spellings and recognizes more local
      Markdown links in lint and backlinks.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Memory Wiki keeps Notes inside its marked human section when regenerating
      concept pages, and memory maintenance leaves unreadable source files and Dream
      Diary entries untouched. If a file is damaged, preserve the original and repair
      a copy before retrying. Handwritten text outside the marked Notes section on
      older generated pages is not protected.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: ChatGPT imports now keep readable prose and pasted text from supported
      transcripts; Hermes memory imports reject malformed text instead of changing
      the source or destination. Replace unexpected special files with regular readable
      files, and convert a copy of malformed text before retrying.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Memory can save a checkpoint before conversation compaction even when a
      provider omits token-use data. File-based checkpoints also reject exact copies
      of already saved blocks and can retry with new text.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: New network results reached through Tool Search or Code Mode now keep their
      untrusted-source label in later replies, so memory can treat them like directly
      retrieved network content. Existing history and stored memory are not relabeled.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: The Mac memory readout now counts memory the system can reclaim, so available
      memory is no longer understated.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 15-memory-and-personalization-changes-in-v2026-10-10
  source_release: openclaw-2026-11-03-v2026-10-10-c26ff355
  source_type: openclaw_changelog
  theme: memory
  title: 15 Memory and Personalization changes in v2026.10.10
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-10-29-2-memory-and-personalization-changes-in-v0-12-5|2
  Memory and Personalization changes in v0.12.5]]'
- '[[Changes/ChatGPT/2026-10-30-account-switching-is-rolling-out-to-the-chatgpt-ios-and-android-apps-you-can-sta|Account
  switching on iOS and Android]]'
- '[[Changes/Lovable/2026-10-30-lovable-remembers-what-you-tell-it|Lovable remembers
  what you tell it]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-11-03-v2026-10-10-c26ff355|openclaw-2026-11-03-v2026-10-10-c26ff355]]'
source_type: openclaw_changelog
theme: memory
title: 15 Memory and Personalization changes in v2026.10.10
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Memory and Personalization changes in v2026.10.10

**OpenClaw** · 2026-11-03 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.10) · from [[Releases/OpenClaw/openclaw-2026-11-03-v2026-10-10-c26ff355|v2026.10.10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> There’s plenty beyond those highlights, with hundreds of improvements and fixes for everyday chats, memory search, automations, coding agents and connected devices.

> Memory indexing now batches conversation updates after a quiet period instead of repeatedly working during active turns. Recent conversation text may therefore take longer to appear in memory search.

> Agent preparation and long conversations use less memory and repeat less work, especially when many agents or models are configured.

> Starting OpenClaw no longer opens every agent's memory index at once. Each index opens when needed, while plugin reloads resume indexing that was already active.

> Memory search can find notes that a natural-language question previously missed, keep relevant older dated notes eligible and rank weak keyword matches below closer matches in meaning. These are improvements to existing search, not a guarantee that every exact match comes first. If you set a minimum search score yourself, lower it if useful results disappear after the ranking change.

> Memory search now explains more embedding-provider failures and keeps a previously usable index available when rebuilding fails. After a database worker stops, a later request can reopen the existing index, although searches during recovery can still fail.

> Memory reads through the CLI and supported plugins now reach the intended agent’s permitted notes more consistently, while private or untrusted content remains subject to its existing access checks.

> During memory setup, you can optionally test an embedding provider and model before saving them. Skipping or failing the check leaves existing settings intact, and interrupted import setup can return to its result and Continue action.

> Memory embedding requests now respect the chosen provider’s private-network rules, including when a service redirects to a private address. If your embedding service depends on that route, you may need to allow it explicitly; invalid Google or LM Studio headers identify the affected setting.

> Memory Wiki now finds matching filenames without scanning every page in those searches, matches equivalent Unicode spellings and recognizes more local Markdown links in lint and backlinks.

> Memory Wiki keeps Notes inside its marked human section when regenerating concept pages, and memory maintenance leaves unreadable source files and Dream Diary entries untouched. If a file is damaged, preserve the original and repair a copy before retrying. Handwritten text outside the marked Notes section on older generated pages is not protected.

> ChatGPT imports now keep readable prose and pasted text from supported transcripts; Hermes memory imports reject malformed text instead of changing the source or destination. Replace unexpected special files with regular readable files, and convert a copy of malformed text before retrying.

> Memory can save a checkpoint before conversation compaction even when a provider omits token-use data. File-based checkpoints also reject exact copies of already saved blocks and can retry with new text.

> New network results reached through Tool Search or Code Mode now keep their untrusted-source label in later replies, so memory can treat them like directly retrieved network content. Existing history and stored memory are not relabeled.

> The Mac memory readout now counts memory the system can reclaim, so available memory is no longer understated.

Source: https://docs.openclaw.ai/releases/2026.10.10
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-11-03-generated-images-music-and-video-can-wait-behind-a-busy-chat-without-reporting-f|Generated images, music and video can wait behind a busy chat without reporting…]] · Multimodal Input
- [[Changes/OpenClaw/2026-11-03-you-can-now-guide-the-same-running-conversation-from-the-control-ui-or-an-admini|Guide the same running conversation from the Control UI or an administrator-linked…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-11-03-2-files-and-data-changes-in-v2026-10-10|2 Files and Data changes in v2026.10.10]] · Files and Data
- [[Changes/OpenClaw/2026-11-03-6-account-and-access-changes-in-v2026-10-10|6 Account and Access changes in v2026.10.10]] · Account and Access
- [[Changes/OpenClaw/2026-11-03-image-generation-and-editing-now-reject-invalid-size-and-shape-options-before-co|Image generation and editing now reject invalid size and shape options before…]] · Image Generation
- [[Changes/OpenClaw/2026-11-03-9-agent-mode-changes-in-v2026-10-10|9 Agent Mode changes in v2026.10.10]] · Agent Mode
- [[Changes/OpenClaw/2026-11-03-13-interface-experience-changes-in-v2026-10-10|13 Interface Experience changes in v2026.10.10]] · Interface Experience
- [[Changes/OpenClaw/2026-11-03-you-can-now-work-directly-in-a-folder-on-another-computer-connected-to-openclaw|Work directly in a folder on another computer connected to OpenClaw]] · Agent Mode
- [[Changes/OpenClaw/2026-11-03-5-context-window-changes-in-v2026-10-10|5 Context Window changes in v2026.10.10]] · Context Window
- [[Changes/OpenClaw/2026-11-03-4-automation-and-scheduling-changes-in-v2026-10-10|4 Automation and Scheduling changes in v2026.10.10]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-11-03-3-editor-experience-changes-in-v2026-10-10|3 Editor Experience changes in v2026.10.10]] · Editor Experience
- [[Changes/OpenClaw/2026-11-03-web-search-now-honors-more-of-your-chosen-provider-settings-result-counts-and-ti|Web search now honors more of your chosen provider settings, result counts…]] · Search and Browsing
- [[Changes/OpenClaw/2026-11-03-6-collaboration-changes-in-v2026-10-10|6 Collaboration changes in v2026.10.10]] · Collaboration
- [[Changes/OpenClaw/2026-11-03-6-voice-and-audio-changes-in-v2026-10-10|6 Voice and Audio changes in v2026.10.10]] · Voice and Audio
- [[Changes/OpenClaw/2026-11-03-7-safety-and-privacy-changes-in-v2026-10-10|7 Safety and Privacy changes in v2026.10.10]] · Safety and Privacy
- [[Changes/OpenClaw/2026-11-03-4-mobile-and-desktop-changes-in-v2026-10-10|4 Mobile and Desktop changes in v2026.10.10]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-11-03-retrying-a-meeting-transcript-from-summary-or-transcript-now-restores-all-availa|Retrying a meeting transcript from Summary or Transcript now restores all available pages]] · Meeting Notes
- [[Changes/OpenClaw/2026-11-03-18-developer-workflow-changes-in-v2026-10-10|18 Developer Workflow changes in v2026.10.10]] · Developer Workflow
- [[Changes/OpenClaw/2026-11-03-21-apps-and-integrations-changes-in-v2026-10-10|21 Apps and Integrations changes in v2026.10.10]] · Apps and Integrations
- [[Changes/OpenClaw/2026-11-03-17-model-support-changes-in-v2026-10-10|17 Model Support changes in v2026.10.10]] · Model Support
- [[Changes/OpenClaw/2026-11-03-incognito-conversations-now-keep-openclaw-conversation-contents-in-memory-instea|Incognito conversations now keep OpenClaw conversation contents in memory instead…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-11-03-83-other-changes-in-v2026-10-10|83 other changes in v2026.10.10]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-10-30 · Lovable · [[Changes/Lovable/2026-10-30-lovable-remembers-what-you-tell-it|Lovable remembers what you tell it]]
- Later: 2026-11-04 · Lovable · [[Changes/Lovable/2026-11-04-dreaming-lovable-keeps-its-memory-up-to-date|Dreaming: Lovable keeps its memory up to date]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-11-03-814e52&body=Card%3A%20Changes%2FOpenClaw%2F2026-11-03-15-memory-and-personalization-changes-in-v2026-10-10.md%0ACard%20ID%3A%20openclaw-2026-11-03-814e52%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.10%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->