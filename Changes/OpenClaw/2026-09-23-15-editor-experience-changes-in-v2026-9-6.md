---
card_id: openclaw-2026-09-23-650d24
date: '2026-09-23'
description: 'OpenClaw · 2026-09-23 · Editor Experience: 15 changes in v2026.9.6 —
  Use /export or /export-session without a path to download conversation Markdown
  from the…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1289
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 145b95ad9a806c2767e35dd57e8972c8e7a7983737325c1b38e748838caa4a94
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-23-650d24
  comparison: ''
  date: '2026-09-23'
  description: 'OpenClaw — v2026.9.6: 15 Editor Experience changes'
  evidence:
  - quote: Use /export or /export-session without a path to download conversation
      Markdown from the browser. The guidance now matches that workflow, and an invalid
      path or a late export completion preserves your current draft and attachments.
      HTML and workspace exports in other clients keep their separate behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Inbox snoozes stay separate for each account and Gateway in a shared browser,
      and Dismiss or Dismiss all shown makes the scope of clearing ordinary notifications
      explicit. Failed or uncertain sends now appear in Inbox → System , with conversation
      identity and Review opening their recovery controls, including offline. Ordinary
      queued messages stay in chat, and account or connection displays no longer show
      Outbox counts. Review does not resend or discard a message, recovery entries
      cannot be dismissed like ordinary notifications, and an uncertain message may
      already have arrived. These recovery entries belong to the local browser tab
      and Gateway, without per-person or cross-device isolation. Older snoozes without
      a known owner may let an alert reappear once.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Failed or timed-out chats can show their saved error and Copy error even
      when the live notification was missed, while temporary history-index rebuilding
      returns a retryable error. Failed pending messages can be discarded locally
      and stay removed after reload, and queued follow-ups can proceed once completion
      of their exact run is confirmed. Discarding does not undo accepted work or history.
      An outdated guarded Stop request also leaves a replacement conversation and
      its newer queued work alone.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Updates and Doctor can identify eligible managed Gateways pointing at a
      different installation. Eligible updates repair recognized stale service settings
      through a backed-up transaction, and standalone openclaw doctor --fix now uses
      that same repair on writable packaged installations. Supported custom values
      are preserved while unknown edits stay available for review. Credential writes
      and unrelated command changes still need confirmation, and unverified recovery
      remains pending. Supported Node installation changes may trigger a noninteractive
      installation of a private compatible Node runtime without changing system Node.
      Already-stopped services remain stopped, externally managed services keep their
      owner, and --no-restart does not rebind a service. Windows and some custom overrides
      retain the service-root fallback described in update execution .
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Source-checkout updates handle larger Git packs and shallow partial repositories,
      show installed and target revisions, and preserve local edits when checking
      retained builds for rollback. Older installed updaters may still need missing
      Git objects fetched or a manual first upgrade, and staged packs need disk space.
      Doctor also gives selective recovery advice for source self-links without rewriting
      unrelated dependency edits.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Editing a streamed Mattermost reply or completing an interactive button
      now preserves the post's existing pins and reactions. Partial edits also retain
      message text and files when those fields are omitted. Edits containing channel-wide
      mentions preserve the previously read properties, but can still overwrite property
      changes made elsewhere between the read and update.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Completed Claude replies can also arrive while native background research
      continues, even with previews and block streaming disabled. Channel progress
      previews show tracked checklists and completion counts without treating a completed
      checklist as the end of the run.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Delegated Codex work now completes from native completion events or recovered
      history, preventing parent commentary from being mistaken for a child's finished
      result. Parents can resume after yielding to deliver completed work, and eligible
      saved results can restore a missing final summary without repeating completed
      actions. Reply handling also distinguishes delivered, queued, and failed output
      while preserving unsent images and finalized text.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Small Codex catalog replies avoid waiting for a decoder worker to start,
      while large session lists reduce repeated scans and database work. Catalogs
      refresh incrementally, with full reconciliation at startup and reconnect; quiet
      edits or removals in older sessions may wait for a successful fifteen-minute
      safety cycle. Large catalog parsing moves off the Gateway's main thread, and
      recreated connections suppress unused notification traffic, reducing repeated
      processing without changing model generation.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Run history now shows OK · Error or OK · Unknown when execution succeeded
      but overall completion failed or remains uncertain. These runs still appear
      under the OK execution filter, so the delivery details matter when checking
      whether a report reached you. Confirmed final delivery can prevent a later tool
      error from turning a completed report into a false failure, while progress-only
      messages do not count as final delivery. Repeated failed runs in a persistent
      conversation also retain their original errors for diagnosis.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Queued children are recorded before startup, and native follow-ups before
      acceptance, while completion notices remain owed until the parent turn finishes.
      If follow-up acceptance is still pending, inspect the returned run before retrying.
      Results remain accessible through conversation compaction and cleanup, with
      existing access checks preserved; pending or failed saves remain visible rather
      than being treated as delivered results. Completion and cancellation notices
      keep their intended destination through delayed storage work, and an accepted
      or uncertain send no longer triggers fallback solely because a later save fails.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Publishing a session’s work accepts valid recreated branches even when
      their reflog has expired, while preserving published history through ancestry
      checks and publication conditional on the exact observed remote branch. Concurrent
      branch changes are rejected, and later workspace edits cannot enter an already
      accepted snapshot. Publication errors now distinguish another operation holding
      the lock from unavailable storage or cancellation, making the next step clearer.
      A storage failure can be retried with the original request or checkpoint; cancellation
      before the operation acquires its lock is not automatically retryable. Canceled
      Doctor inspections are reported as not performed, rather than as a health result.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Restored media-task status keeps the correct requester and current completion
      state. Media handling can fall back to a valid URL, and a staging failure preserves
      other attachments while retaining existing access and size limits.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Commands that stop reading their input early now return their actual exit
      status and error output, avoiding misleading broken-pipe failures. File edits
      also recover from limited newline and backslash encoding mistakes in replacement
      lists sent as strings, while preserving the intended literal text. Incomplete
      lists and malformed outer requests still fail validation without applying a
      partial edit.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Failed command launches preserve the original operating-system error, and
      valid JavaScript using dollar-prefixed names or dollar text now reaches Node
      without being mistaken for shell syntax. Node reports its own errors, and statements
      before a runtime error may already have run. An identical replacement repeated
      across batch and legacy edit arguments is applied once, while genuine duplicates
      within a batch and conflicting edits still fail without writing.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 15-editor-experience-changes-in-v2026-9-6
  source_release: openclaw-2026-09-23-v2026-9-6-3f12c824
  source_type: openclaw_changelog
  theme: editor-experience
  title: 15 Editor Experience changes in v2026.9.6
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-22-6-editor-experience-changes-in-rust-v0-156-0|6 Editor
  Experience changes in rust-v0.156.0]]'
- '[[Changes/GitHub Copilot CLI/2026-09-22-in-the-sessions-tab-rows-you-can-dismiss-now-take-x-then-x-again-to-confirm-a-lo|In
  the Sessions tab, rows you can dismiss now take x then x again to confirm]]'
- '[[Changes/Google Antigravity/2026-09-22-prompt-actions-in-interactive-widgets-and-html-artifacts-now-fill-in-and-focus-t|Prompt
  actions in interactive widgets and HTML artifacts now fill in and focus…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|openclaw-2026-09-23-v2026-9-6-3f12c824]]'
source_type: openclaw_changelog
theme: editor-experience
title: 15 Editor Experience changes in v2026.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Editor Experience changes in v2026.9.6

**OpenClaw** · 2026-09-23 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.6) · from [[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|v2026.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Use /export or /export-session without a path to download conversation Markdown from the browser. The guidance now matches that workflow, and an invalid path or a late export completion preserves your current draft and attachments. HTML and workspace exports in other clients keep their separate behavior.

> Inbox snoozes stay separate for each account and Gateway in a shared browser, and Dismiss or Dismiss all shown makes the scope of clearing ordinary notifications explicit. Failed or uncertain sends now appear in Inbox → System , with conversation identity and Review opening their recovery controls, including offline. Ordinary queued messages stay in chat, and account or connection displays no longer show Outbox counts. Review does not resend or discard a message, recovery entries cannot be dismissed like ordinary notifications, and an uncertain message may already have arrived. These recovery entries belong to the local browser tab and Gateway, without per-person or cross-device isolation. Older snoozes without a known owner may let an alert reappear once.

> Failed or timed-out chats can show their saved error and Copy error even when the live notification was missed, while temporary history-index rebuilding returns a retryable error. Failed pending messages can be discarded locally and stay removed after reload, and queued follow-ups can proceed once completion of their exact run is confirmed. Discarding does not undo accepted work or history. An outdated guarded Stop request also leaves a replacement conversation and its newer queued work alone.

> Updates and Doctor can identify eligible managed Gateways pointing at a different installation. Eligible updates repair recognized stale service settings through a backed-up transaction, and standalone openclaw doctor --fix now uses that same repair on writable packaged installations. Supported custom values are preserved while unknown edits stay available for review. Credential writes and unrelated command changes still need confirmation, and unverified recovery remains pending. Supported Node installation changes may trigger a noninteractive installation of a private compatible Node runtime without changing system Node. Already-stopped services remain stopped, externally managed services keep their owner, and --no-restart does not rebind a service. Windows and some custom overrides retain the service-root fallback described in update execution .

> Source-checkout updates handle larger Git packs and shallow partial repositories, show installed and target revisions, and preserve local edits when checking retained builds for rollback. Older installed updaters may still need missing Git objects fetched or a manual first upgrade, and staged packs need disk space. Doctor also gives selective recovery advice for source self-links without rewriting unrelated dependency edits.

> Editing a streamed Mattermost reply or completing an interactive button now preserves the post's existing pins and reactions. Partial edits also retain message text and files when those fields are omitted. Edits containing channel-wide mentions preserve the previously read properties, but can still overwrite property changes made elsewhere between the read and update.

> Completed Claude replies can also arrive while native background research continues, even with previews and block streaming disabled. Channel progress previews show tracked checklists and completion counts without treating a completed checklist as the end of the run.

> Delegated Codex work now completes from native completion events or recovered history, preventing parent commentary from being mistaken for a child's finished result. Parents can resume after yielding to deliver completed work, and eligible saved results can restore a missing final summary without repeating completed actions. Reply handling also distinguishes delivered, queued, and failed output while preserving unsent images and finalized text.

> Small Codex catalog replies avoid waiting for a decoder worker to start, while large session lists reduce repeated scans and database work. Catalogs refresh incrementally, with full reconciliation at startup and reconnect; quiet edits or removals in older sessions may wait for a successful fifteen-minute safety cycle. Large catalog parsing moves off the Gateway's main thread, and recreated connections suppress unused notification traffic, reducing repeated processing without changing model generation.

> Run history now shows OK · Error or OK · Unknown when execution succeeded but overall completion failed or remains uncertain. These runs still appear under the OK execution filter, so the delivery details matter when checking whether a report reached you. Confirmed final delivery can prevent a later tool error from turning a completed report into a false failure, while progress-only messages do not count as final delivery. Repeated failed runs in a persistent conversation also retain their original errors for diagnosis.

> Queued children are recorded before startup, and native follow-ups before acceptance, while completion notices remain owed until the parent turn finishes. If follow-up acceptance is still pending, inspect the returned run before retrying. Results remain accessible through conversation compaction and cleanup, with existing access checks preserved; pending or failed saves remain visible rather than being treated as delivered results. Completion and cancellation notices keep their intended destination through delayed storage work, and an accepted or uncertain send no longer triggers fallback solely because a later save fails.

> Publishing a session’s work accepts valid recreated branches even when their reflog has expired, while preserving published history through ancestry checks and publication conditional on the exact observed remote branch. Concurrent branch changes are rejected, and later workspace edits cannot enter an already accepted snapshot. Publication errors now distinguish another operation holding the lock from unavailable storage or cancellation, making the next step clearer. A storage failure can be retried with the original request or checkpoint; cancellation before the operation acquires its lock is not automatically retryable. Canceled Doctor inspections are reported as not performed, rather than as a health result.

> Restored media-task status keeps the correct requester and current completion state. Media handling can fall back to a valid URL, and a staging failure preserves other attachments while retaining existing access and size limits.

> Commands that stop reading their input early now return their actual exit status and error output, avoiding misleading broken-pipe failures. File edits also recover from limited newline and backslash encoding mistakes in replacement lists sent as strings, while preserving the intended literal text. Incomplete lists and malformed outer requests still fail validation without applying a partial edit.

> Failed command launches preserve the original operating-system error, and valid JavaScript using dollar-prefixed names or dollar text now reaches Node without being mistaken for shell syntax. Node reports its own errors, and statements before a runtime error may already have run. An identical replacement repeated across batch and legacy edit arguments is applied once, while genuine duplicates within a batch and conflicting edits still fail without writing.

Source: https://docs.openclaw.ai/releases/2026.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-23-50-safety-and-privacy-changes-in-v2026-9-6|50 Safety and Privacy changes in v2026.9.6]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-23-localization-maintenance-removes-entries-whose-interface-text-has-already-been-r|Localization maintenance removes entries whose interface text has already been…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-23-5-reliability-and-performance-changes-in-v2026-9-6|5 Reliability and Performance changes in v2026.9.6]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-23-2-image-generation-changes-in-v2026-9-6|2 Image Generation changes in v2026.9.6]] · Image Generation
- [[Changes/OpenClaw/2026-09-23-18-voice-and-audio-changes-in-v2026-9-6|18 Voice and Audio changes in v2026.9.6]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-23-25-context-window-changes-in-v2026-9-6|25 Context Window changes in v2026.9.6]] · Context Window
- [[Changes/OpenClaw/2026-09-23-16-mobile-and-desktop-changes-in-v2026-9-6|16 Mobile and Desktop changes in v2026.9.6]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-23-41-agent-mode-changes-in-v2026-9-6|41 Agent Mode changes in v2026.9.6]] · Agent Mode
- [[Changes/OpenClaw/2026-09-23-16-collaboration-changes-in-v2026-9-6|16 Collaboration changes in v2026.9.6]] · Collaboration
- [[Changes/OpenClaw/2026-09-23-2-enterprise-and-administration-changes-in-v2026-9-6|2 Enterprise and Administration changes in v2026.9.6]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-23-31-developer-workflow-changes-in-v2026-9-6|31 Developer Workflow changes in v2026.9.6]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-23-8-pricing-model-changes-in-v2026-9-6|8 Pricing Model changes in v2026.9.6]] · Pricing Model
- [[Changes/OpenClaw/2026-09-23-plugin-requested-answer-revisions-wait-for-session-history-to-become-available-a|Plugin-requested answer revisions wait for session history to become available…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-23-6-files-and-data-changes-in-v2026-9-6|6 Files and Data changes in v2026.9.6]] · Files and Data
- [[Changes/OpenClaw/2026-09-23-58-apps-and-integrations-changes-in-v2026-9-6|58 Apps and Integrations changes in v2026.9.6]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-23-17-account-and-access-changes-in-v2026-9-6|17 Account and Access changes in v2026.9.6]] · Account and Access
- [[Changes/OpenClaw/2026-09-23-background-image-video-and-music-generation-can-complete-independently-of-the-re|Background image, video, and music generation can complete independently…]] · Music Generation
- [[Changes/OpenClaw/2026-09-23-23-memory-and-personalization-changes-in-v2026-9-6|23 Memory and Personalization changes in v2026.9.6]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-23-3-search-and-browsing-changes-in-v2026-9-6|3 Search and Browsing changes in v2026.9.6]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-23-19-interface-experience-changes-in-v2026-9-6|19 Interface Experience changes in v2026.9.6]] · Interface Experience
- [[Changes/OpenClaw/2026-09-23-9-automation-and-scheduling-changes-in-v2026-9-6|9 Automation and Scheduling changes in v2026.9.6]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-23-22-model-support-changes-in-v2026-9-6|22 Model Support changes in v2026.9.6]] · Model Support
- [[Changes/OpenClaw/2026-09-23-119-other-changes-in-v2026-9-6|119 other changes in v2026.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-09-22 · Google Antigravity · [[Changes/Google Antigravity/2026-09-22-prompt-actions-in-interactive-widgets-and-html-artifacts-now-fill-in-and-focus-t|Prompt actions in interactive widgets and HTML artifacts now fill in and focus…]]
- Later: 2026-09-23 · Runway · [[Changes/Runway/2026-09-23-runway-is-now-available-directly-inside-davinci-resolve-bring-runway-s-tools-int|DaVinci Resolve Plugin]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-23-650d24&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-23-15-editor-experience-changes-in-v2026-9-6.md%0ACard%20ID%3A%20openclaw-2026-09-23-650d24%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->