---
card_id: openclaw-2026-09-30-345249
date: '2026-09-30'
description: 'OpenClaw · 2026-09-30 · Memory and Personalization: 15 changes in v2026.9.7
  — If an update blocks the editor, Review file drafts lets you copy or download…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1168
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 39dae33f7ca2f89b0b297ea0272505f13c063c8cc14214a0ef216663a1615cb2
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-30-345249
  comparison: ''
  date: '2026-09-30'
  description: 'OpenClaw — v2026.9.7: 15 Memory and Personalization changes'
  evidence:
  - quote: If an update blocks the editor, Review file drafts lets you copy or download
      unsaved work. Keep anything you need before explicitly discarding drafts and
      refreshing. Copying alone does not unlock refresh, and a manual browser reload
      or tab closure still loses these drafts. Incognito drafts have the same memory-only
      limit.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Diagnostics show more detail about worker memory use and failed operations.
      Deep status and Doctor warn when the running Gateway has lost its Node executable
      and needs a restart. For monitoring, use /readyz to detect recorded terminal
      database failures; /healthz only shows that the process is alive.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: OpenClaw fixes missed memory updates and search failures, with repairs
      for older Dreaming schedules and protection for standalone QMD files.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Memory search can fall back to existing keyword matches when an optional
      embedding service fails. A working keyword index is required, and explicitly
      selected remote providers still report errors. Searches also keep English terms
      in mixed Chinese-English questions, and Active Memory recognizes more Russian
      questions about past conversations.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: With memory watching enabled, notes edited during an update are picked
      up in a follow-up pass. Large folders configured as extra memory paths also
      avoid unnecessary rescans when unrelated files change.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Dreaming stops adding its own nested reflections to new memories from daily
      notes. Newly saved snippets also favor complete words and mark shortened text
      with an ellipsis. Existing entries remain unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Memory Wiki avoids unnecessary work when searching or opening pages with
      many links. Open Knowledge Format imports also preserve links inside code examples
      instead of rewriting them.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Desktop Codex Computer Use sessions launched and connected directly by
      OpenClaw now keep their configured persona and memory-plugin guidance. Restart
      the Gateway to load the fix. Native child agents do not automatically inherit
      this guidance.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Cleanup of old scheduled sessions does more work in the background and
      uses less temporary memory, reducing interruptions to other activity. Retention
      rules and transcript archiving are unchanged, and cleanup can still take longer
      overall in custom stores. The scheduling guide explains late starts, startup
      catch-up, and shutdown.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: LanceDB statistics now limit database reads to 60 seconds and return zero
      when the memory table is missing. Plugin startup can take additional time.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Compatible paired hosts can keep up to two idle workers loaded for two
      minutes to reduce startup work for follow-up messages. Those workers continue
      to use memory while idle. Stop or reclaim the placement to release them sooner;
      Chat Stop without an active turn does not release them.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Incognito skips automatic memory and learning, and keeps conversation content
      out of saved browser copies and supported diagnostic logs and plugin observers.
      Tabs left open from the older UI must reload after updating to apply this browser
      protection, so save anything you need first. Older logs remain. Tools can still
      write files, and model providers can still retain messages.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Busy chats release large pieces of data they no longer need. Related memory-management
      changes reduced long pauses in tests with many simultaneous replies, though
      pauses can still occur.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Closing Control UI terminal tabs also releases memory that could remain
      held after the tab closed, while other open terminals keep working.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Busy installations may use more memory for queued database input, with
      its allowance rising from 64 to 256 MiB. If a global or unknown session address
      is rejected as ambiguous, choose a specific conversation. Existing history is
      kept without merging or renaming it.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 15-memory-and-personalization-changes-in-v2026-9-7
  source_release: openclaw-2026-09-30-v2026-9-7-3d25d2bd
  source_type: openclaw_changelog
  theme: memory
  title: 15 Memory and Personalization changes in v2026.9.7
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-29-pages-follow-space-s-availability-and-sharing-settings-sharing-a-page-does-not-g|Pages
  follow Space’s availability and sharing settings]]'
- '[[Changes/ChatGPT/2026-09-29-you-can-use-your-chatgpt-account-to-sign-in-to-participating-products-without-cr|Sign
  in to other products with ChatGPT]]'
- '[[Changes/Claude Code/2026-09-29-changed-memory-so-that-auto-memory-can-no-longer-be-turned-on-from-a-background|Changed
  /memory so that Auto-memory can no longer be turned on from a background…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|openclaw-2026-09-30-v2026-9-7-3d25d2bd]]'
source_type: openclaw_changelog
theme: memory
title: 15 Memory and Personalization changes in v2026.9.7
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Memory and Personalization changes in v2026.9.7

**OpenClaw** · 2026-09-30 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.7) · from [[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|v2026.9.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> If an update blocks the editor, Review file drafts lets you copy or download unsaved work. Keep anything you need before explicitly discarding drafts and refreshing. Copying alone does not unlock refresh, and a manual browser reload or tab closure still loses these drafts. Incognito drafts have the same memory-only limit.

> Diagnostics show more detail about worker memory use and failed operations. Deep status and Doctor warn when the running Gateway has lost its Node executable and needs a restart. For monitoring, use /readyz to detect recorded terminal database failures; /healthz only shows that the process is alive.

> OpenClaw fixes missed memory updates and search failures, with repairs for older Dreaming schedules and protection for standalone QMD files.

> Memory search can fall back to existing keyword matches when an optional embedding service fails. A working keyword index is required, and explicitly selected remote providers still report errors. Searches also keep English terms in mixed Chinese-English questions, and Active Memory recognizes more Russian questions about past conversations.

> With memory watching enabled, notes edited during an update are picked up in a follow-up pass. Large folders configured as extra memory paths also avoid unnecessary rescans when unrelated files change.

> Dreaming stops adding its own nested reflections to new memories from daily notes. Newly saved snippets also favor complete words and mark shortened text with an ellipsis. Existing entries remain unchanged.

> Memory Wiki avoids unnecessary work when searching or opening pages with many links. Open Knowledge Format imports also preserve links inside code examples instead of rewriting them.

> Desktop Codex Computer Use sessions launched and connected directly by OpenClaw now keep their configured persona and memory-plugin guidance. Restart the Gateway to load the fix. Native child agents do not automatically inherit this guidance.

> Cleanup of old scheduled sessions does more work in the background and uses less temporary memory, reducing interruptions to other activity. Retention rules and transcript archiving are unchanged, and cleanup can still take longer overall in custom stores. The scheduling guide explains late starts, startup catch-up, and shutdown.

> LanceDB statistics now limit database reads to 60 seconds and return zero when the memory table is missing. Plugin startup can take additional time.

> Compatible paired hosts can keep up to two idle workers loaded for two minutes to reduce startup work for follow-up messages. Those workers continue to use memory while idle. Stop or reclaim the placement to release them sooner; Chat Stop without an active turn does not release them.

> Incognito skips automatic memory and learning, and keeps conversation content out of saved browser copies and supported diagnostic logs and plugin observers. Tabs left open from the older UI must reload after updating to apply this browser protection, so save anything you need first. Older logs remain. Tools can still write files, and model providers can still retain messages.

> Busy chats release large pieces of data they no longer need. Related memory-management changes reduced long pauses in tests with many simultaneous replies, though pauses can still occur.

> Closing Control UI terminal tabs also releases memory that could remain held after the tab closed, while other open terminals keep working.

> Busy installations may use more memory for queued database input, with its allowance rising from 64 to 256 MiB. If a global or unknown session address is rejected as ambiguous, choose a specific conversation. Existing history is kept without merging or renaming it.

Source: https://docs.openclaw.ai/releases/2026.9.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-30-4-context-window-changes-in-v2026-9-7|4 Context Window changes in v2026.9.7]] · Context Window
- [[Changes/OpenClaw/2026-09-30-13-developer-workflow-changes-in-v2026-9-7|13 Developer Workflow changes in v2026.9.7]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-30-3-files-and-data-changes-in-v2026-9-7|3 Files and Data changes in v2026.9.7]] · Files and Data
- [[Changes/OpenClaw/2026-09-30-13-account-and-access-changes-in-v2026-9-7|13 Account and Access changes in v2026.9.7]] · Account and Access
- [[Changes/OpenClaw/2026-09-30-2-enterprise-and-administration-changes-in-v2026-9-7|2 Enterprise and Administration changes in v2026.9.7]] · Enterprise and Administration
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
- [[Changes/OpenClaw/2026-09-30-10-collaboration-changes-in-v2026-9-7|10 Collaboration changes in v2026.9.7]] · Collaboration
- [[Changes/OpenClaw/2026-09-30-4-multimodal-input-changes-in-v2026-9-7|4 Multimodal Input changes in v2026.9.7]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-30-72-other-changes-in-v2026-9-7|72 other changes in v2026.9.7]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-09-29 · Claude Code · [[Changes/Claude Code/2026-09-29-changed-memory-so-that-auto-memory-can-no-longer-be-turned-on-from-a-background|Changed /memory so that Auto-memory can no longer be turned on from a background…]]
- Later: 2026-10-01 · ChatGPT · [[Changes/ChatGPT/2026-10-01-virtually-try-on-clothing-and-accessories-a-try-on-button-will-appear-on-product|Virtually try on clothing and accessories]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-30-345249&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-30-15-memory-and-personalization-changes-in-v2026-9-7.md%0ACard%20ID%3A%20openclaw-2026-09-30-345249%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->