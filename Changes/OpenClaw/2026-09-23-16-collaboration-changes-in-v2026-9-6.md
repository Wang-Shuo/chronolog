---
card_id: openclaw-2026-09-23-53ca9e
date: '2026-09-23'
description: 'OpenClaw · 2026-09-23 · Collaboration: 16 changes in v2026.9.6 — You
  can also select up to ten people to mention when starting the task. Typing a name
  alone…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create
    a team here: (source link)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2812
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 82cfa3d710cb08e7fe5d5bd062d8da4017141d9f1327ede824402773fb2ae165
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-23-53ca9e
  comparison: ''
  date: '2026-09-23'
  description: 'OpenClaw — v2026.9.6: 16 Collaboration changes'
  evidence:
  - quote: You can also select up to ten people to mention when starting the task.
      Typing a name alone does not select a recipient, and a mention does not share
      the conversation or grant access.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Explicitly linked GitHub accounts can keep one person's avatar, preferences
      and mention Inbox, and people search supports full names and verified handles.
      Selected mentions show avatars and open full person cards using information
      you are allowed to see, while assignment and sharing pickers remain searchable
      and current. Typing or pasting a name alone does not notify someone or grant
      membership. Before downgrading, keep a backup because older writers can discard
      secondary account links, and upgrading again will not restore them without explicitly
      relinking.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: An explicit mention can bring an accessible conversation into Involving
      me without requiring you to reply first. Personal Hide and Show controls follow
      your profile across browsers and restarts, and a fresh mention can bring a hidden
      conversation back. These controls appear when more than one identity is available
      and remain separate from Inbox dismissal, shared membership and archive state.
      Older conversations are not scanned for missed mentions. See finding sessions
      by owner .
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: An unchanged dashboard restores its selected, closed and focused panel
      arrangement after reload, and moving a loaded widget to an unopened tab preserves
      unsaved input and counters. The layout menu shows when the current view matches
      its shared default, while a lone full-width widget gets more unobstructed space
      with controls in the task menu. Explicit presentation changes still take precedence,
      and preserving a widget during a move does not make arbitrary widget state durable
      across reloads or deletion.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Current finalization can keep database work in the compatible newly installed
      runtime after shared-state migration. That fix must already be in the installed
      updater and cannot patch an older driver that is already running; the narrower
      older-version handoff paths above remain separate. Code-only rollback after
      migration remains unsafe.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: More maintenance, snapshot and shared-state database work runs in background
      workers, reducing work that competes with messages and status requests. Catalog
      refreshes avoid redundant copies, unused queued snapshots can be canceled, and
      update rehearsals can capture consistent individual databases while other processes
      write. Retention rules and uncertain or active owners remain protected; these
      individual copies do not create an atomic rollback across every database.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Teams can use the current inbound message when adding, removing, or listing
      reactions in the same conversation, without requiring its message ID to be supplied
      again. Reactions in another conversation and message deletion still require
      an explicit ID.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Browser cards can show public page titles, favicons, and social images
      when a live screenshot is unavailable, making closed or historical pages easier
      to recognize. Repeated opens of the same page share a card within an activity
      group, while actual tabs and distinct routes stay separate. New Browser side
      panels use more available space without overriding your saved width. Retained
      computer screenshots also appear during runs and after reopening chat, with
      image-viewer, copy, and download controls. Discarded pixels cannot be recovered,
      and some saved-image layouts can still show duplicate tiles.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: This changes shared state to schema 18, which older versions refuse to
      read. Stop older writers and keep a verified pre-upgrade backup that captures
      data still in SQLite’s write-ahead log. Check recorded or uncertain GitHub effects
      before freshly authorizing unfinished legacy shared requests. To downgrade,
      use the matching older build and backup in a separate state directory; restoring
      local data does not undo changes already made on GitHub.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Team Reports adds a Work sessions directory and overview preview with links
      directly to current conversations. Member reports also link to conversations
      their members currently own. These are current work views, not a reconstruction
      of ownership during an older reporting period, and existing viewer permissions
      and exclusions for archived, incognito, automated, system, and hidden sessions
      still apply. Stored reports, transcripts, and full downloads are unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The shared Rust Gateway client updates Rustls to 0.23.45, including the
      fix for GHSA-2mjx-qc3c-rqvc.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Shared agent instructions more explicitly connect your corrections and
      an agent's promise to check something with continuing the authorized work. They
      also tell an agent receiving delegated results to address fixable failed checks
      before stopping, while preserving approval requirements, pauses, and cancellations.
      These are guidance changes, so individual model behavior can still vary.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: This works with supported local embedded, generic CLI, and native Codex
      conversations, excluding ACP, realtime, and remote-worker execution. Files are
      operator-created, and profile merges require moving them manually. A missing
      selected file leaves shared defaults rather than choosing someone else's file.
      These preferences do not isolate files or conversation history or grant tool
      permissions.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Temporary-directory checks no longer reject valid filesystem identifiers
      just because they use signed numbers. The shared filesystem dependency carries
      the fix into OpenClaw and components that use it directly.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Messaging tests isolate credentials, temporary paths and background work,
      and wait for delivery or cleanup to reach the state being checked. Shared fixtures
      retain each channel's existing regression scenarios.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Database and filesystem code share bounded reads, query preparation and
      record conversion, with selected database work moved to existing workers. Stored
      formats and data-ownership rules remain unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 16-collaboration-changes-in-v2026-9-6
  source_release: openclaw-2026-09-23-v2026-9-6-3f12c824
  source_type: openclaw_changelog
  theme: collaboration
  title: 16 Collaboration changes in v2026.9.6
  type: change
related_changes:
- '[[Changes/OpenHands/2026-09-22-test-strengthen-shared-utility-behavior-by-aivong-openhands-in-https-github-com|test:
  strengthen shared utility behavior]]'
- '[[Changes/Synthesia/2026-09-22-share-the-base-person-for-an-avatar-with-teammates-or-your-whole-workspace-so-th|Share
  customizable avatars with your team]]'
- '[[Changes/Cursor/2026-09-23-team-rules|Team rules]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|openclaw-2026-09-23-v2026-9-6-3f12c824]]'
source_type: openclaw_changelog
theme: collaboration
title: 16 Collaboration changes in v2026.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 16 Collaboration changes in v2026.9.6

**OpenClaw** · 2026-09-23 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.6) · from [[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|v2026.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> You can also select up to ten people to mention when starting the task. Typing a name alone does not select a recipient, and a mention does not share the conversation or grant access.

> Explicitly linked GitHub accounts can keep one person's avatar, preferences and mention Inbox, and people search supports full names and verified handles. Selected mentions show avatars and open full person cards using information you are allowed to see, while assignment and sharing pickers remain searchable and current. Typing or pasting a name alone does not notify someone or grant membership. Before downgrading, keep a backup because older writers can discard secondary account links, and upgrading again will not restore them without explicitly relinking.

> An explicit mention can bring an accessible conversation into Involving me without requiring you to reply first. Personal Hide and Show controls follow your profile across browsers and restarts, and a fresh mention can bring a hidden conversation back. These controls appear when more than one identity is available and remain separate from Inbox dismissal, shared membership and archive state. Older conversations are not scanned for missed mentions. See finding sessions by owner .

> An unchanged dashboard restores its selected, closed and focused panel arrangement after reload, and moving a loaded widget to an unopened tab preserves unsaved input and counters. The layout menu shows when the current view matches its shared default, while a lone full-width widget gets more unobstructed space with controls in the task menu. Explicit presentation changes still take precedence, and preserving a widget during a move does not make arbitrary widget state durable across reloads or deletion.

> Current finalization can keep database work in the compatible newly installed runtime after shared-state migration. That fix must already be in the installed updater and cannot patch an older driver that is already running; the narrower older-version handoff paths above remain separate. Code-only rollback after migration remains unsafe.

> More maintenance, snapshot and shared-state database work runs in background workers, reducing work that competes with messages and status requests. Catalog refreshes avoid redundant copies, unused queued snapshots can be canceled, and update rehearsals can capture consistent individual databases while other processes write. Retention rules and uncertain or active owners remain protected; these individual copies do not create an atomic rollback across every database.

> Teams can use the current inbound message when adding, removing, or listing reactions in the same conversation, without requiring its message ID to be supplied again. Reactions in another conversation and message deletion still require an explicit ID.

> Browser cards can show public page titles, favicons, and social images when a live screenshot is unavailable, making closed or historical pages easier to recognize. Repeated opens of the same page share a card within an activity group, while actual tabs and distinct routes stay separate. New Browser side panels use more available space without overriding your saved width. Retained computer screenshots also appear during runs and after reopening chat, with image-viewer, copy, and download controls. Discarded pixels cannot be recovered, and some saved-image layouts can still show duplicate tiles.

> This changes shared state to schema 18, which older versions refuse to read. Stop older writers and keep a verified pre-upgrade backup that captures data still in SQLite’s write-ahead log. Check recorded or uncertain GitHub effects before freshly authorizing unfinished legacy shared requests. To downgrade, use the matching older build and backup in a separate state directory; restoring local data does not undo changes already made on GitHub.

> Team Reports adds a Work sessions directory and overview preview with links directly to current conversations. Member reports also link to conversations their members currently own. These are current work views, not a reconstruction of ownership during an older reporting period, and existing viewer permissions and exclusions for archived, incognito, automated, system, and hidden sessions still apply. Stored reports, transcripts, and full downloads are unchanged.

> The shared Rust Gateway client updates Rustls to 0.23.45, including the fix for GHSA-2mjx-qc3c-rqvc.

> Shared agent instructions more explicitly connect your corrections and an agent's promise to check something with continuing the authorized work. They also tell an agent receiving delegated results to address fixable failed checks before stopping, while preserving approval requirements, pauses, and cancellations. These are guidance changes, so individual model behavior can still vary.

> This works with supported local embedded, generic CLI, and native Codex conversations, excluding ACP, realtime, and remote-worker execution. Files are operator-created, and profile merges require moving them manually. A missing selected file leaves shared defaults rather than choosing someone else's file. These preferences do not isolate files or conversation history or grant tool permissions.

> Temporary-directory checks no longer reject valid filesystem identifiers just because they use signed numbers. The shared filesystem dependency carries the fix into OpenClaw and components that use it directly.

> Messaging tests isolate credentials, temporary paths and background work, and wait for delivery or cleanup to reach the state being checked. Shared fixtures retain each channel's existing regression scenarios.

> Database and filesystem code share bounded reads, query preparation and record conversion, with selected database work moved to existing workers. Stored formats and data-ownership rules remain unchanged.

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
- [[Changes/OpenClaw/2026-09-23-15-editor-experience-changes-in-v2026-9-6|15 Editor Experience changes in v2026.9.6]] · Editor Experience
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
## Nearby in Collaboration

- Earlier: 2026-09-23 · Cursor · [[Changes/Cursor/2026-09-23-team-rules|Team rules]]
- Later: 2026-09-23 · Qoder · [[Changes/Qoder/2026-09-23-a-new-space-for-human-and-agent-collaboration|A New Space for Human and Agent Collaboration]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-01-11 · Descript · [[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create a team here: (source link)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-23-53ca9e&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-23-16-collaboration-changes-in-v2026-9-6.md%0ACard%20ID%3A%20openclaw-2026-09-23-53ca9e%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->