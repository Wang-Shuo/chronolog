---
card_id: openclaw-2026-10-10-0ae713
date: '2026-10-10'
description: 'OpenClaw · 2026-10-10 · Memory and Personalization: 13 changes in v2026.10.1
  — Each recall feature requires a plugin that supports it. Recreate older spawned…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1178
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: eb80278e786d62d8b36eb1a1563edba854b927e5185ec5493e1a260b1d73a3e3
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-10-0ae713
  comparison: ''
  date: '2026-10-10'
  description: 'OpenClaw — v2026.10.1: 13 Memory and Personalization changes'
  evidence:
  - quote: Each recall feature requires a plugin that supports it. Recreate older
      spawned sessions from their parent to restore native memory access; if the parent
      predates reset tracking, do this after its next reset. Custom native-provider
      search clients must use API version 2. Memory Core search and deep index diagnostics
      refuse to use its separate index when another provider is selected.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Supporting memory plugins can save important context before a long conversation
      is summarized, using their own storage even when the workspace is read-only
      and permissions allow it. Saving is best effort, so compaction still proceeds
      if a save fails or is skipped. Memory Core continues using workspace files.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Codex connections without the managed inference relay now receive shared
      workspace persona and memory guidance, with edits reaching persistent conversations
      on the next turn. Selected personal USER.md profiles are omitted on these connections
      , so some previous preferences may disappear. Use the managed parent-only relay
      when you need those personal preferences.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Agents on paired devices regain permitted web, memory, session, installed-skill
      and GitHub identity tools while file and process work stays on the device. Larger
      tool batches queue, and browser or computer access depends on the device's capabilities.
      See node session hosting and cloud-worker guidance .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Search and Dreaming keep distinct memories in different languages, and
      Wiki searches retain accented and non-Latin words. Supported Brazilian Portuguese
      questions can prompt deeper lookup, and ordinary Conversation Summary notes
      become eligible for Dreaming. Blank searches offer keyword-retry guidance, filename
      searches avoid repeated scans, and recall instructions account for an optional
      Wiki. See the session search guide , Active Memory lookup explanation and recall
      setup guide .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Large conversation histories can become searchable again after database
      limits or a deadlock prevented indexing. Memory updates and cleanup put more
      database work in the background, and excluded system-only sessions stop falsely
      showing that the index needs updating. Forget keeps the original transcripts
      and excludes selected sessions from future indexing; if its result is uncertain,
      retry explicitly.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Memory search can resume with your primary embedding provider after an
      outage, without restarting or rebuilding the index. A later search attempts
      recovery when the provider, model and settings match the saved index and the
      fallback is incompatible; attempts have a 30-second cooldown, and a working
      compatible fallback stays in use. Bedrock indexing also shares credential lookups
      without preventing rotation, while Zhipu batches split and retry when its 64-item
      limit is reported in Chinese.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Memory and skill edits use a 30-second polling default when native file
      watching is unavailable or polling is selected. CHOKIDAR_INTERVAL overrides
      that default, down to 20 ms; shorter intervals mean more background scanning.
      Allow for the interval plus scan and debounce time before an edit appears. Status
      explains the watching mode and fallback reason; restart OpenClaw after repairing
      the native backend to try native watching again.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Very old Dreaming and Wiki installations need an upgrade recovery plan:
      Doctor no longer imports four pre-July Dreaming JSON journals or two older Wiki
      JSON formats. The files stay intact, and ordinary Markdown memories remain supported.
      Preserve a backup compatible with your current version before upgrading. A verified
      recovery route without a newer backup or established SQLite state remains missing;
      moving the old files aside does not migrate their data. See memory guidance
      and upgrading very old versions .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Check older Wiki settings and preserve retired Active Memory JSON preferences
      before upgrading. Doctor no longer repairs Wiki's bridge.readMemoryCore setting
      or warns about those preferences; an old Wiki configuration can fail validation
      without the former repair guidance.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Managed llama.cpp indexing uses smaller missing defaults while preserving
      explicit tuning. This lowers default concurrency and long-input capacity, so
      unusually long requests may need larger existing llama.cpp limits . Memory Wiki
      can also reuse a completed CLI compile, and memory indexing and dreaming continue
      through provider reloads.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Skills remain available after file notifications that report no content
      change, and development sessions avoid the resulting false restarts. Scanning
      skips temporary activity while still refreshing supporting files and rediscovering
      skills when needed. Skills and Memory now honor existing CHOKIDAR_INTERVAL overrides:
      the default is 30 seconds, the minimum is 20 ms, and shorter settings increase
      background scanning.'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Memory Wiki imports backtick-heavy text, and Plivo V3 verifies valid webhooks
      with prototype-named parameters. #162425 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 13-memory-and-personalization-changes-in-v2026-10-1
  source_release: openclaw-2026-10-10-v2026-10-1-d64e4e93
  source_type: openclaw_changelog
  theme: memory
  title: 13 Memory and Personalization changes in v2026.10.1
  type: change
related_changes:
- '[[Changes/Midjourney/2026-10-08-organization-improvements|ORGANIZATION IMPROVEMENTS]]'
- '[[Changes/OpenClaw/2026-10-08-2-memory-and-personalization-changes-in-v2026-9-9|2
  Memory and Personalization changes in v2026.9.9]]'
- '[[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2
  Memory and Personalization changes in v0.12.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|openclaw-2026-10-10-v2026-10-1-d64e4e93]]'
source_type: openclaw_changelog
theme: memory
title: 13 Memory and Personalization changes in v2026.10.1
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Memory and Personalization changes in v2026.10.1

**OpenClaw** · 2026-10-10 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.1) · from [[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Each recall feature requires a plugin that supports it. Recreate older spawned sessions from their parent to restore native memory access; if the parent predates reset tracking, do this after its next reset. Custom native-provider search clients must use API version 2. Memory Core search and deep index diagnostics refuse to use its separate index when another provider is selected.

> Supporting memory plugins can save important context before a long conversation is summarized, using their own storage even when the workspace is read-only and permissions allow it. Saving is best effort, so compaction still proceeds if a save fails or is skipped. Memory Core continues using workspace files.

> Codex connections without the managed inference relay now receive shared workspace persona and memory guidance, with edits reaching persistent conversations on the next turn. Selected personal USER.md profiles are omitted on these connections , so some previous preferences may disappear. Use the managed parent-only relay when you need those personal preferences.

> Agents on paired devices regain permitted web, memory, session, installed-skill and GitHub identity tools while file and process work stays on the device. Larger tool batches queue, and browser or computer access depends on the device's capabilities. See node session hosting and cloud-worker guidance .

> Search and Dreaming keep distinct memories in different languages, and Wiki searches retain accented and non-Latin words. Supported Brazilian Portuguese questions can prompt deeper lookup, and ordinary Conversation Summary notes become eligible for Dreaming. Blank searches offer keyword-retry guidance, filename searches avoid repeated scans, and recall instructions account for an optional Wiki. See the session search guide , Active Memory lookup explanation and recall setup guide .

> Large conversation histories can become searchable again after database limits or a deadlock prevented indexing. Memory updates and cleanup put more database work in the background, and excluded system-only sessions stop falsely showing that the index needs updating. Forget keeps the original transcripts and excludes selected sessions from future indexing; if its result is uncertain, retry explicitly.

> Memory search can resume with your primary embedding provider after an outage, without restarting or rebuilding the index. A later search attempts recovery when the provider, model and settings match the saved index and the fallback is incompatible; attempts have a 30-second cooldown, and a working compatible fallback stays in use. Bedrock indexing also shares credential lookups without preventing rotation, while Zhipu batches split and retry when its 64-item limit is reported in Chinese.

> Memory and skill edits use a 30-second polling default when native file watching is unavailable or polling is selected. CHOKIDAR_INTERVAL overrides that default, down to 20 ms; shorter intervals mean more background scanning. Allow for the interval plus scan and debounce time before an edit appears. Status explains the watching mode and fallback reason; restart OpenClaw after repairing the native backend to try native watching again.

> Very old Dreaming and Wiki installations need an upgrade recovery plan: Doctor no longer imports four pre-July Dreaming JSON journals or two older Wiki JSON formats. The files stay intact, and ordinary Markdown memories remain supported. Preserve a backup compatible with your current version before upgrading. A verified recovery route without a newer backup or established SQLite state remains missing; moving the old files aside does not migrate their data. See memory guidance and upgrading very old versions .

> Check older Wiki settings and preserve retired Active Memory JSON preferences before upgrading. Doctor no longer repairs Wiki's bridge.readMemoryCore setting or warns about those preferences; an old Wiki configuration can fail validation without the former repair guidance.

> Managed llama.cpp indexing uses smaller missing defaults while preserving explicit tuning. This lowers default concurrency and long-input capacity, so unusually long requests may need larger existing llama.cpp limits . Memory Wiki can also reuse a completed CLI compile, and memory indexing and dreaming continue through provider reloads.

> Skills remain available after file notifications that report no content change, and development sessions avoid the resulting false restarts. Scanning skips temporary activity while still refreshing supporting files and rediscovering skills when needed. Skills and Memory now honor existing CHOKIDAR_INTERVAL overrides: the default is 30 seconds, the minimum is 20 ms, and shorter settings increase background scanning.

> Memory Wiki imports backtick-heavy text, and Plivo V3 verifies valid webhooks with prototype-named parameters. #162425 . Thanks @steipete .

Source: https://docs.openclaw.ai/releases/2026.10.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-10-2-reliability-and-performance-changes-in-v2026-10-1|2 Reliability and Performance changes in v2026.10.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-10-10-96-apps-and-integrations-changes-in-v2026-10-1|96 Apps and Integrations changes in v2026.10.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-10-15-mobile-and-desktop-changes-in-v2026-10-1|15 Mobile and Desktop changes in v2026.10.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-10-12-context-window-changes-in-v2026-10-1|12 Context Window changes in v2026.10.1]] · Context Window
- [[Changes/OpenClaw/2026-10-10-4-pricing-model-changes-in-v2026-10-1|4 Pricing Model changes in v2026.10.1]] · Pricing Model
- [[Changes/OpenClaw/2026-10-10-18-account-and-access-changes-in-v2026-10-1|18 Account and Access changes in v2026.10.1]] · Account and Access
- [[Changes/OpenClaw/2026-10-10-18-model-support-changes-in-v2026-10-1|18 Model Support changes in v2026.10.1]] · Model Support
- [[Changes/OpenClaw/2026-10-10-20-safety-and-privacy-changes-in-v2026-10-1|20 Safety and Privacy changes in v2026.10.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-10-3-search-and-browsing-changes-in-v2026-10-1|3 Search and Browsing changes in v2026.10.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-10-10-plugin-authors-can-await-session-history-extension-changes-and-replay-metadata-t|Plugin authors can await session history, extension changes and replay metadata]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-10-2-accessibility-and-localization-changes-in-v2026-10-1|2 Accessibility and Localization changes in v2026.10.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-10-10-image-generation-with-oauth-can-retry-using-a-supported-openai-chat-model-in-age|Image generation with OAuth can retry using a supported OpenAI chat model…]] · Image Generation
- [[Changes/OpenClaw/2026-10-10-10-editor-experience-changes-in-v2026-10-1|10 Editor Experience changes in v2026.10.1]] · Editor Experience
- [[Changes/OpenClaw/2026-10-10-2-files-and-data-changes-in-v2026-10-1|2 Files and Data changes in v2026.10.1]] · Files and Data
- [[Changes/OpenClaw/2026-10-10-8-voice-and-audio-changes-in-v2026-10-1|8 Voice and Audio changes in v2026.10.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-10-27-agent-mode-changes-in-v2026-10-1|27 Agent Mode changes in v2026.10.1]] · Agent Mode
- [[Changes/OpenClaw/2026-10-10-12-collaboration-changes-in-v2026-10-1|12 Collaboration changes in v2026.10.1]] · Collaboration
- [[Changes/OpenClaw/2026-10-10-video-previews-new-video-previews-can-download-media-before-play|Video previews: New video previews can download media before Play]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-10-11-developer-workflow-changes-in-v2026-10-1|11 Developer Workflow changes in v2026.10.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-10-5-enterprise-and-administration-changes-in-v2026-10-1|5 Enterprise and Administration changes in v2026.10.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-10-20-interface-experience-changes-in-v2026-10-1|20 Interface Experience changes in v2026.10.1]] · Interface Experience
- [[Changes/OpenClaw/2026-10-10-10-automation-and-scheduling-changes-in-v2026-10-1|10 Automation and Scheduling changes in v2026.10.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-10-112-other-changes-in-v2026-10-1|112 other changes in v2026.10.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-10-10 · Open WebUI · [[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2 Memory and Personalization changes in v0.12.0]]
- Later: 2026-10-12 · OpenClaw · [[Changes/OpenClaw/2026-10-12-4-memory-and-personalization-changes-in-v2026-10-2|4 Memory and Personalization changes in v2026.10.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-10-0ae713&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-10-13-memory-and-personalization-changes-in-v2026-10-1.md%0ACard%20ID%3A%20openclaw-2026-10-10-0ae713%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->