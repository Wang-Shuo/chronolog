---
card_id: openclaw-2026-09-23-ed115d
date: '2026-09-23'
description: 'OpenClaw · 2026-09-23 · Automation and Scheduling: 9 changes in v2026.9.6
  — Chat and sidebar updates avoid some layout stalls, and opening a conversation…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change
    gain, with volume automation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2562
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 24ae748dd0bba8554a6ab8b8dfce9b38445164ed78264baf0c35c961e47307cd
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-23-ed115d
  comparison: ''
  date: '2026-09-23'
  description: 'OpenClaw — v2026.9.6: 9 Automation and Scheduling changes'
  evidence:
  - quote: Chat and sidebar updates avoid some layout stalls, and opening a conversation
      downloads less information for Inbox alerts. The automation editor still loads
      the complete job settings when you open it.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Cleanup now distinguishes completed, deferred and partial results and explains
      why a worktree was retained. Partial CLI JSON results include details and exit
      with an error, so automation should not treat a reported deletion count as proof
      that all requested cleanup finished.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: After a restart, addressed messages can pick up fresh recent discussion
      from Slack and Discord without turning quiet room messages into new agent turns.
      The default windows are 50 messages for Slack and 20 for Discord, with 0 disabling
      automatic history. Slack's room historyLimit also caps thread.initialHistoryLimit
      , including when set to zero. Reads respect current access, edits, deletions,
      retention, and bounded retrieval, so unavailable history is omitted rather than
      replaced with stale text. Discord replies also retain quoted bot responses and
      automation alerts as untrusted context, making follow-ups understandable without
      copying the original message.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: You can use Run now on a paused automation in the Agents panel without
      enabling its schedule. A future Once job keeps its saved occurrence even with
      Delete after run enabled, including when a manual run waits past that date or
      OpenClaw restarts. Re-enabling makes the preserved occurrence available again,
      while genuine schedule edits still take effect and already-deleted jobs are
      not restored. Manage automations explains the controls and run history.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Remote administrators can create recurring automations in a fresh chat
      turn under their existing permissions, including jobs attached to the current
      conversation. WebChat can also create announcements back to that conversation
      using announce or omitted delivery settings. Fresh creation rights do not carry
      over to management continuations or grant access to the host, providers, or
      additional MCP tools, and an explicit delivery.channel=webchat remains invalid.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Creating or editing an automation preserves meaningful whitespace in shell
      commands, and invalid cron stagger values are rejected before they can partially
      change a job. Keyboard focus stays visible above the editor’s sticky save controls,
      delayed action feedback names the job you acted on, and timeout errors correctly
      explain that zero disables that particular timeout. Other execution limits still
      apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Substantively editing an automation now retires its previous Always allow
      approval, even if you later restore the old contents. Pausing and resuming an
      otherwise unchanged automation keeps its approval. Older grants without this
      binding need one fresh approval after upgrading, so unattended jobs may wait
      for you to approve their next matching operation. Standing automation approvals
      remain tied to the work you approved. Older binaries cannot enforce the new
      binding, and edits made by an older version without any observable record cannot
      be reconstructed after upgrading again.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: When messaging tools offer only sending and broadcasting, their definitions
      take up less model context while keeping supported options. Automation descriptions
      also remove repeated argument lists, and large tool outputs reuse valid text
      counts during context checks and trimming. Context limits and trimming rules
      stay the same.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Drafts, incognito sessions, hidden internal sessions, scheduled cron runs,
      and Home itself are excluded. Reopening or resetting an existing session does
      not send another notice, and pending notices do not survive a restart.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 9-automation-and-scheduling-changes-in-v2026-9-6
  source_release: openclaw-2026-09-23-v2026-9-6-3f12c824
  source_type: openclaw_changelog
  theme: automation-scheduling
  title: 9 Automation and Scheduling changes in v2026.9.6
  type: change
related_changes:
- '[[Changes/OpenHands/2026-09-22-chore-consume-sdk-1-49-4-and-automation-1-14-0-by-hieptl-in-https-github-com-ope|chore:
  consume SDK 1.49.4 and Automation 1.14.0]]'
- '[[Changes/OpenHands/2026-09-22-2-automation-and-scheduling-changes-in-v1-21-0|2
  Automation and Scheduling changes in v1.21.0]]'
- '[[Changes/Claude Code/2026-09-23-claude-tag-changed-the-routine-list-claude-gives-when-asked-in-a-slack-thread-to|Claude
  Tag Changed the routine list Claude gives when asked in a Slack thread…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|openclaw-2026-09-23-v2026-9-6-3f12c824]]'
source_type: openclaw_changelog
theme: automation-scheduling
title: 9 Automation and Scheduling changes in v2026.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Automation and Scheduling changes in v2026.9.6

**OpenClaw** · 2026-09-23 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.6) · from [[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|v2026.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Chat and sidebar updates avoid some layout stalls, and opening a conversation downloads less information for Inbox alerts. The automation editor still loads the complete job settings when you open it.

> Cleanup now distinguishes completed, deferred and partial results and explains why a worktree was retained. Partial CLI JSON results include details and exit with an error, so automation should not treat a reported deletion count as proof that all requested cleanup finished.

> After a restart, addressed messages can pick up fresh recent discussion from Slack and Discord without turning quiet room messages into new agent turns. The default windows are 50 messages for Slack and 20 for Discord, with 0 disabling automatic history. Slack's room historyLimit also caps thread.initialHistoryLimit , including when set to zero. Reads respect current access, edits, deletions, retention, and bounded retrieval, so unavailable history is omitted rather than replaced with stale text. Discord replies also retain quoted bot responses and automation alerts as untrusted context, making follow-ups understandable without copying the original message.

> You can use Run now on a paused automation in the Agents panel without enabling its schedule. A future Once job keeps its saved occurrence even with Delete after run enabled, including when a manual run waits past that date or OpenClaw restarts. Re-enabling makes the preserved occurrence available again, while genuine schedule edits still take effect and already-deleted jobs are not restored. Manage automations explains the controls and run history.

> Remote administrators can create recurring automations in a fresh chat turn under their existing permissions, including jobs attached to the current conversation. WebChat can also create announcements back to that conversation using announce or omitted delivery settings. Fresh creation rights do not carry over to management continuations or grant access to the host, providers, or additional MCP tools, and an explicit delivery.channel=webchat remains invalid.

> Creating or editing an automation preserves meaningful whitespace in shell commands, and invalid cron stagger values are rejected before they can partially change a job. Keyboard focus stays visible above the editor’s sticky save controls, delayed action feedback names the job you acted on, and timeout errors correctly explain that zero disables that particular timeout. Other execution limits still apply.

> Substantively editing an automation now retires its previous Always allow approval, even if you later restore the old contents. Pausing and resuming an otherwise unchanged automation keeps its approval. Older grants without this binding need one fresh approval after upgrading, so unattended jobs may wait for you to approve their next matching operation. Standing automation approvals remain tied to the work you approved. Older binaries cannot enforce the new binding, and edits made by an older version without any observable record cannot be reconstructed after upgrading again.

> When messaging tools offer only sending and broadcasting, their definitions take up less model context while keeping supported options. Automation descriptions also remove repeated argument lists, and large tool outputs reuse valid text counts during context checks and trimming. Context limits and trimming rules stay the same.

> Drafts, incognito sessions, hidden internal sessions, scheduled cron runs, and Home itself are excluded. Reopening or resetting an existing session does not send another notice, and pending notices do not survive a restart.

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
- [[Changes/OpenClaw/2026-09-23-22-model-support-changes-in-v2026-9-6|22 Model Support changes in v2026.9.6]] · Model Support
- [[Changes/OpenClaw/2026-09-23-119-other-changes-in-v2026-9-6|119 other changes in v2026.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-09-23 · Claude Code · [[Changes/Claude Code/2026-09-23-claude-tag-changed-the-routine-list-claude-gives-when-asked-in-a-slack-thread-to|Claude Tag Changed the routine list Claude gives when asked in a Slack thread…]]
- Later: 2026-09-23 · OpenHands · [[Changes/OpenHands/2026-09-23-chore-consume-sdk-1-49-5-and-automation-1-15-0-by-juanmichelini-in-https-github|chore: consume SDK 1.49.5 and Automation 1.15.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change gain, with volume automation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-23-ed115d&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-23-9-automation-and-scheduling-changes-in-v2026-9-6.md%0ACard%20ID%3A%20openclaw-2026-09-23-ed115d%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->