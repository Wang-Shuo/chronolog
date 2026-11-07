---
card_id: openclaw-2026-09-30-20fd40
date: '2026-09-30'
description: 'OpenClaw · 2026-09-30 · Developer Workflow: 13 changes in v2026.9.7
  — OpenClaw can use your configured public HTTPS address for device join links and
  QR setup…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2941
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d3cd71dbc59dbf9fd17130f6a8b97a2d61d9d95772307ebe8edc7dec36e7985b
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-30-20fd40
  comparison: ''
  date: '2026-09-30'
  description: 'OpenClaw — v2026.9.7: 13 Developer Workflow changes'
  evidence:
  - quote: OpenClaw can use your configured public HTTPS address for device join links
      and QR setup . Used or expired dashboard links now explain how to get a fresh
      one with openclaw dashboard on the computer running OpenClaw. Links remain single-use
      and expire after ten minutes. When a browser requests admin access, its Inbox
      now shows the exact approval command to run on the computer hosting OpenClaw.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Source updates now rebuild missing or stale program files even when the
      source is already current. They also check for build locks and conflicting worktrees
      before stopping OpenClaw. If an older updater gets stuck, use the manual source-update
      procedure from an external terminal. Confirm all associated compiler processes
      have stopped before releasing a build lock. Rollback may leave OpenClaw stopped
      when local changes prevent restoring the previous source.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: When the installed updater includes this fix, an eligible failed Git update
      can restore the previous version even without usable branch history. It leaves
      the checkout detached at the previous commit and the branch at the failed candidate.
      Follow the branch repair instructions in the rollback report before continuing
      work on that branch.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: With a compatible job-capable OCM manager, you can request an update from
      the Control UI or internal /update and follow its progress through a reconnect.
      OCM handles verification and recovery. Explicit Git targets and unsupported
      package dev-channel requests are refused.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Automatic worktree cleanup starts one hour after OpenClaw starts. Frequent
      restarts can delay it, so use openclaw worktrees gc when you need immediate
      cleanup. Moved or unreadable worktrees are kept for inspection, and session-cleanup
      dry runs avoid changing records.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: For an interrupted clean removal, openclaw worktrees recover-removal can
      recover from the original snapshot. Stop other programs writing to that worktree
      first and leave space to rebuild missing files. Use retire-snapshot only when
      you no longer need that snapshot's managed restore option; retirement permanently
      removes it. Orphans without a snapshot require manual recovery in a separate
      checkout.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Mattermost can replace an outdated slash command even when the deletion
      response is interrupted. Reactions also reach the reacted-to message's thread
      when it can be found, falling back to the parent conversation if it cannot.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Jobs scheduled for a named conversation now run in its saved project directory
      or managed Git worktree. If the worktree is missing or no longer matches the
      conversation, the job stops. Restore its binding or recreate the job from a
      valid bound conversation before retrying. New unbound sessions still use the
      agent's configured workspace, while current and isolated jobs stay detached.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Approval handling now preserves the original permissions through waits
      and recovery. Approval diagnostics also explain why terminal tools are unavailable.
      If you used Disable All , repeat it and Save to include previously omitted GitHub
      and transcript tools.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Shell approvals now reject combined options that read commands from standard
      input instead of the reviewed script. If a command such as bash -se job.sh is
      refused, invoke the script directly when that is the code you intend to run.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: You can handle more everyday settings and shared work through chat, with
      updates to terminal controls and busy conversations.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Shell commands can use more of the current Code Mode call’s remaining time
      to finish, reducing unnecessary follow-up checks for short commands. Longer
      commands still return a process handle, and explicit background requests keep
      their behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: A completed command keeps its result when a busy OpenClaw processes the
      finish notification late, instead of incorrectly reporting a timeout. Windows
      commands can finish their cleanup before exiting, and Linux background-process
      cleanup handles more leftover processes that have already exited. Commands still
      running keep their existing deadlines and operating-system restrictions.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 13-developer-workflow-changes-in-v2026-9-7
  source_release: openclaw-2026-09-30-v2026-9-7-3d25d2bd
  source_type: openclaw_changelog
  theme: developer-workflow
  title: 13 Developer Workflow changes in v2026.9.7
  type: change
related_changes:
- '[[Changes/Devin/2026-09-30-read-only-live-shell-preview|Read-Only Live Shell Preview]]'
- '[[Changes/Devin/2026-09-30-devin-fixes-its-own-prs-review-findings-before-they-are-posted|Devin
  Fixes Its Own PRs'' Review Findings Before They Are Posted]]'
- '[[Changes/Google Antigravity/2026-09-30-pressing-cmd-a-or-ctrl-a-now-selects-only-the-content-pane-or-terminal-you-are-f|Pressing
  Cmd+A or Ctrl+A now selects only the content pane or terminal you…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|openclaw-2026-09-30-v2026-9-7-3d25d2bd]]'
source_type: openclaw_changelog
theme: developer-workflow
title: 13 Developer Workflow changes in v2026.9.7
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Developer Workflow changes in v2026.9.7

**OpenClaw** · 2026-09-30 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.7) · from [[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|v2026.9.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> OpenClaw can use your configured public HTTPS address for device join links and QR setup . Used or expired dashboard links now explain how to get a fresh one with openclaw dashboard on the computer running OpenClaw. Links remain single-use and expire after ten minutes. When a browser requests admin access, its Inbox now shows the exact approval command to run on the computer hosting OpenClaw.

> Source updates now rebuild missing or stale program files even when the source is already current. They also check for build locks and conflicting worktrees before stopping OpenClaw. If an older updater gets stuck, use the manual source-update procedure from an external terminal. Confirm all associated compiler processes have stopped before releasing a build lock. Rollback may leave OpenClaw stopped when local changes prevent restoring the previous source.

> When the installed updater includes this fix, an eligible failed Git update can restore the previous version even without usable branch history. It leaves the checkout detached at the previous commit and the branch at the failed candidate. Follow the branch repair instructions in the rollback report before continuing work on that branch.

> With a compatible job-capable OCM manager, you can request an update from the Control UI or internal /update and follow its progress through a reconnect. OCM handles verification and recovery. Explicit Git targets and unsupported package dev-channel requests are refused.

> Automatic worktree cleanup starts one hour after OpenClaw starts. Frequent restarts can delay it, so use openclaw worktrees gc when you need immediate cleanup. Moved or unreadable worktrees are kept for inspection, and session-cleanup dry runs avoid changing records.

> For an interrupted clean removal, openclaw worktrees recover-removal can recover from the original snapshot. Stop other programs writing to that worktree first and leave space to rebuild missing files. Use retire-snapshot only when you no longer need that snapshot's managed restore option; retirement permanently removes it. Orphans without a snapshot require manual recovery in a separate checkout.

> Mattermost can replace an outdated slash command even when the deletion response is interrupted. Reactions also reach the reacted-to message's thread when it can be found, falling back to the parent conversation if it cannot.

> Jobs scheduled for a named conversation now run in its saved project directory or managed Git worktree. If the worktree is missing or no longer matches the conversation, the job stops. Restore its binding or recreate the job from a valid bound conversation before retrying. New unbound sessions still use the agent's configured workspace, while current and isolated jobs stay detached.

> Approval handling now preserves the original permissions through waits and recovery. Approval diagnostics also explain why terminal tools are unavailable. If you used Disable All , repeat it and Save to include previously omitted GitHub and transcript tools.

> Shell approvals now reject combined options that read commands from standard input instead of the reviewed script. If a command such as bash -se job.sh is refused, invoke the script directly when that is the code you intend to run.

> You can handle more everyday settings and shared work through chat, with updates to terminal controls and busy conversations.

> Shell commands can use more of the current Code Mode call’s remaining time to finish, reducing unnecessary follow-up checks for short commands. Longer commands still return a process handle, and explicit background requests keep their behavior.

> A completed command keeps its result when a busy OpenClaw processes the finish notification late, instead of incorrectly reporting a timeout. Windows commands can finish their cleanup before exiting, and Linux background-process cleanup handles more leftover processes that have already exited. Commands still running keep their existing deadlines and operating-system restrictions.

Source: https://docs.openclaw.ai/releases/2026.9.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-30-4-context-window-changes-in-v2026-9-7|4 Context Window changes in v2026.9.7]] · Context Window
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
- [[Changes/OpenClaw/2026-09-30-10-collaboration-changes-in-v2026-9-7|10 Collaboration changes in v2026.9.7]] · Collaboration
- [[Changes/OpenClaw/2026-09-30-4-multimodal-input-changes-in-v2026-9-7|4 Multimodal Input changes in v2026.9.7]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-30-72-other-changes-in-v2026-9-7|72 other changes in v2026.9.7]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-30 · Google Antigravity · [[Changes/Google Antigravity/2026-09-30-pressing-cmd-a-or-ctrl-a-now-selects-only-the-content-pane-or-terminal-you-are-f|Pressing Cmd+A or Ctrl+A now selects only the content pane or terminal you…]]
- Later: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-3-developer-workflow-changes-in-v2-1-287|3 Developer Workflow changes in v2.1.287]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-30-20fd40&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-30-13-developer-workflow-changes-in-v2026-9-7.md%0ACard%20ID%3A%20openclaw-2026-09-30-20fd40%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->