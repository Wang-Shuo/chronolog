---
card_id: openclaw-2026-09-23-6f2950
date: '2026-09-23'
description: 'OpenClaw · 2026-09-23 · Developer Workflow: 31 changes in v2026.9.6
  — Use the command palette to start an independent task from text or a pasted screenshot…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2934
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7ca0624413f82aa63cf45746f1b1c4effe14cbb725f6ad3fe983d51a2d3c96a7
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-23-6f2950
  comparison: ''
  date: '2026-09-23'
  description: 'OpenClaw — v2026.9.6: 31 Developer Workflow changes'
  evidence:
  - quote: Use the command palette to start an independent task from text or a pasted
      screenshot while keeping your current conversation and draft in place. Press
      Cmd/Ctrl+K to open it and Cmd/Ctrl+Enter or New session to start the work, while
      ordinary Enter applies the current search instead of opening a stale result.
      Failed creation keeps images for another try, but closing the palette normally
      discards unsent images.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Suggested tasks keep their full summaries and Start controls reachable
      in shorter windows, and launching one in a new session or worktree leaves your
      current conversation and draft selected. If the selected repository cannot start
      the task, you can correct it without retyping the prompt, then explicitly retry
      with a usable repository that has a commit.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Leaving the worktree From choice untouched now starts from the fetched
      remote default branch, as does leaving Base branch empty when creating a worktree
      manually in Settings. An explicit or saved local branch keeps its meaning. Branch
      editing stays usable and an accepted start clears the custom name it consumed,
      so it does not accidentally name the next session. Rejected starts retain the
      name, and failed remote lookup retains the source-HEAD fallback. If name cleanup
      is unconfirmed, check Name before starting another session.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Failed Git discovery also keeps a saved separate-worktree choice instead
      of silently switching to the current checkout. Starting waits for recovery or
      your explicit Current checkout choice.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Goals now pause after terminal errors or timeouts, retaining their objective
      and usage with a frozen timer and a readable pause reason. Resume is deliberate,
      and an ordinary message does not restart a failed paused Goal. Starting or resuming
      a Goal still requires the built-in runtime.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Logs, Debug, Devices and channel-pairing views now pause selected background
      polling while hidden and refresh when you return. Explicit refresh remains available,
      and requests already underway are not canceled.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Historical conversation titles, ACP metadata, transcript markers, worktree
      paths and task identifiers are repaired through Doctor maintenance , keeping
      ordinary startup and reads from rewriting that history. openclaw update already
      runs the required repair pass. Supported container image upgrades now invoke
      Doctor maintenance automatically before serving. Direct binary replacements,
      state touched by older writers, or a specific remaining historical repair still
      need the supported Doctor preparation; when offline repair is required, stop
      writers and run openclaw doctor --fix against the same state and configuration
      before restarting.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Mac service commands recognize native XML and binary definitions, preserve
      original LaunchAgent bytes and permissions during supported rollback, and verify
      that the service has unloaded before reporting a completed stop. Run maintenance
      from the service owner's logged-in session and use openclaw gateway status --deep
      to inspect it; a disabled but still-loaded service must be unloaded before runtime
      replacement. Affected older update helpers may need their first upgrade from
      an independent Terminal. Service inspection from an inaccessible working directory
      remains a known limitation.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Git updates also check destination disk capacity before stopping the Gateway
      and avoid letting an unrelated unavailable remote block the selected update
      source. Stable and beta-fallback Git updates skip extended-stable tags, preserving
      the selected release line; older installed updaters retain their first-upgrade
      limits.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: A Gateway running in a terminal now hands supported updates to a fresh
      process, avoiding missing-module failures after its runtime files are replaced.
      Candidate validation happens while it serves, followed by a brief activation
      interruption; Stop waits for owned update work and leaves it stopped. OPENCLAW_NO_RESPAWN
      refuses before changes and gives manual instructions.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Use the coordinated openclaw update path when possible. A Gateway already
      running the new detection code can also notice manual package replacement and
      drain toward managed restart or foreground relaunch with openclaw gateway run
      ; an old running binary cannot gain that behavior from replacement files alone.
      If Stop remains unconfirmed, inspect the updater and retry Ctrl+C in the original
      terminal or SIGTERM to the original process, as described in update execution
      .
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Unsafe required state exits with code 78 and a repair reason. FUSE recovery
      needs same-directory hardlinks and directory synchronization; if the filesystem
      cannot provide them, expose the same retained data through its native backing
      path before retrying. Stop writers and run same-state offline openclaw doctor
      --fix when instructed or when a specific historical repair remains; a separate
      offline command is no longer required for every supported image swap.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Advanced operators can archive a supported detached managed worktree without
      losing partially staged edits, using openclaw worktrees remove <id> --exact-state
      <file> with a request matching its observed state, then openclaw worktrees restore
      <id> to recover it. This is an explicit archival route, separate from ordinary
      force removal. The original checkout is retained for 30 days, so its disk space
      is not immediately reclaimed.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Exact-state restoration requires a supporting runtime, a full non-sparse
      checkout, Git file refs and a supported index. Restoration normally returns
      the retained checkout, including later file writes; if only the snapshot survives,
      recovery covers eligible files and exact staging rather than a complete filesystem
      image or unrelated ignored caches.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Bzip2 skill archives can now be extracted without installing a system tar
      command. Finalizing an uploaded archive also lets OpenClaw continue handling
      other work while it hashes and stores the archive, and uploads that expire before
      finalization or a repeated commit are rejected. The rest of the upload's database
      work now runs in the background too, with expiry checked after queued work is
      admitted. Existing extraction permissions and protection for uploads already
      in use by an installation remain in place.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Updated Windows startup and recovery helpers avoid opening an extra blank
      console during background launches. Interactive commands keep their terminal,
      and the change takes effect when the replacement helpers run.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Explicit terminal status now takes precedence over contradictory output-limit
      hints, avoiding an unnecessary continuation request while keeping genuine length
      recovery available.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: If an older save trimmed a command, reapply the original command to repair
      it. When creating jobs from scripts, omit working-directory flags to use defaults
      instead of passing empty strings.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Task details show complete command inputs with sensitive values redacted,
      and distinguish live Running , Queued , waiting, and Finished execution from
      a saved task record. Quiet background commands can still show as running, while
      delayed activity no longer makes finished work look active. Finished describes
      execution, so success and pending result delivery remain separate facts, and
      unavailable activity does not by itself mean failure.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Failure notices offer concise previews with full diagnostics available
      through tasks show , and unreadable task metadata produces an explicit error
      instead of a falsely empty list. Previously truncated command inputs cannot
      be reconstructed, and command output remains bounded.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The GitHub reader brings public issues, pull-request discussions, commits,
      and expandable diffs beside your conversation, so you can inspect a reference
      without leaving chat. Tabs let you keep several items open, while previews and
      refreshable snapshots of automated checks help you follow the work. The reader
      is public-only and read-only, with private content and edits staying on GitHub;
      check results are bounded snapshots, not a merge-readiness verdict.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Applying cloud results and restoring rollback snapshots preserve exact
      supported filenames and file contents independently of Git attributes or checkout
      encodings. Canceling private preparation waits for staging cleanup to settle;
      the host filesystem’s filename restrictions still apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Command errors now distinguish an unsupported command form from a human
      denial and explain how to retry through the approval flow. Unsupported forms
      remain blocked. The approvals guide also clarifies the existing approvals get
      --node and approvals set --node commands, with --file or --stdin supplying a
      replacement policy.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: 'Sandboxed sessions can work on an authorized registered project with worktree:
      true in a private Docker or Podman checkout, with accepted changes returned
      to the managed worktree. Host Git credentials and ignored provisioning stay
      outside that checkout. Explicit read-only access remains read-only, and unsupported
      backends refuse this workflow. Later files created only on the host need git
      add before entering an existing private checkout. Let pending changes finish
      before downgrading, and use a supporting version to recover unfinished work,
      as described in managed project workspaces .'
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: In Discord, /new and /reset in unbound channels now respect channel disablement,
      allowlists, group policy, and server command authorization before changing a
      session. Previously bypassed commands may now be refused, while existing configured-binding
      recovery exceptions remain available.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Remote terminal typing and paste require less preparation, while tool-output
      redraws and scrollback reading avoid repeated work. On macOS and Linux, a terminal
      launched through Bun can also find a real Node installation when a shim hides
      it, keeping input and cursor keys working. A real Node installation is still
      required.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Agent requests skip unused diagnostics when debug logging is off, and media
      progress sections share a fresh task read within each turn. Large-request diagnostics
      and shell setup also avoid some repeated preparation before execution; these
      changes concern local setup work rather than media generation speed.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: These fixes address interrupted work, misleading command failures, and
      database waits that could get in the way of everyday use.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: A terminal on a paired node now reports a timeout and removes its local
      terminal session after the existing 30-second inactivity limit, even if the
      node never sends its first heartbeat. Each heartbeat renews that limit. OpenClaw
      requests cancellation once, but the local timeout does not confirm that the
      remote process has stopped.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: When a long terminal-upload filename needs shortening, the resulting name
      still follows the portable rules for reserved names and trailing characters.
      This applies to newly staged uploads and leaves existing filenames alone.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Gateway and command tests coordinate startup, background work and teardown
      more explicitly. Isolated ports, profiles and workspace fixtures help preserve
      coverage for complete workflows without letting unrelated activity interfere
      with assertions.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 31-developer-workflow-changes-in-v2026-9-6
  source_release: openclaw-2026-09-23-v2026-9-6-3f12c824
  source_type: openclaw_changelog
  theme: developer-workflow
  title: 31 Developer Workflow changes in v2026.9.6
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-23-7-developer-workflow-changes-in-v2-1-281|7 Developer
  Workflow changes in v2.1.281]]'
- '[[Changes/Cursor/2026-09-23-rollouts|Rollouts]]'
- '[[Changes/Cursor/2026-09-23-when-a-pull-request-opens-rollouts-reads-the-diff-and-the-systems-it-touches-the|Monitoring
  plans]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|openclaw-2026-09-23-v2026-9-6-3f12c824]]'
source_type: openclaw_changelog
theme: developer-workflow
title: 31 Developer Workflow changes in v2026.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 31 Developer Workflow changes in v2026.9.6

**OpenClaw** · 2026-09-23 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.6) · from [[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|v2026.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Use the command palette to start an independent task from text or a pasted screenshot while keeping your current conversation and draft in place. Press Cmd/Ctrl+K to open it and Cmd/Ctrl+Enter or New session to start the work, while ordinary Enter applies the current search instead of opening a stale result. Failed creation keeps images for another try, but closing the palette normally discards unsent images.

> Suggested tasks keep their full summaries and Start controls reachable in shorter windows, and launching one in a new session or worktree leaves your current conversation and draft selected. If the selected repository cannot start the task, you can correct it without retyping the prompt, then explicitly retry with a usable repository that has a commit.

> Leaving the worktree From choice untouched now starts from the fetched remote default branch, as does leaving Base branch empty when creating a worktree manually in Settings. An explicit or saved local branch keeps its meaning. Branch editing stays usable and an accepted start clears the custom name it consumed, so it does not accidentally name the next session. Rejected starts retain the name, and failed remote lookup retains the source-HEAD fallback. If name cleanup is unconfirmed, check Name before starting another session.

> Failed Git discovery also keeps a saved separate-worktree choice instead of silently switching to the current checkout. Starting waits for recovery or your explicit Current checkout choice.

> Goals now pause after terminal errors or timeouts, retaining their objective and usage with a frozen timer and a readable pause reason. Resume is deliberate, and an ordinary message does not restart a failed paused Goal. Starting or resuming a Goal still requires the built-in runtime.

> Logs, Debug, Devices and channel-pairing views now pause selected background polling while hidden and refresh when you return. Explicit refresh remains available, and requests already underway are not canceled.

> Historical conversation titles, ACP metadata, transcript markers, worktree paths and task identifiers are repaired through Doctor maintenance , keeping ordinary startup and reads from rewriting that history. openclaw update already runs the required repair pass. Supported container image upgrades now invoke Doctor maintenance automatically before serving. Direct binary replacements, state touched by older writers, or a specific remaining historical repair still need the supported Doctor preparation; when offline repair is required, stop writers and run openclaw doctor --fix against the same state and configuration before restarting.

> Mac service commands recognize native XML and binary definitions, preserve original LaunchAgent bytes and permissions during supported rollback, and verify that the service has unloaded before reporting a completed stop. Run maintenance from the service owner's logged-in session and use openclaw gateway status --deep to inspect it; a disabled but still-loaded service must be unloaded before runtime replacement. Affected older update helpers may need their first upgrade from an independent Terminal. Service inspection from an inaccessible working directory remains a known limitation.

> Git updates also check destination disk capacity before stopping the Gateway and avoid letting an unrelated unavailable remote block the selected update source. Stable and beta-fallback Git updates skip extended-stable tags, preserving the selected release line; older installed updaters retain their first-upgrade limits.

> A Gateway running in a terminal now hands supported updates to a fresh process, avoiding missing-module failures after its runtime files are replaced. Candidate validation happens while it serves, followed by a brief activation interruption; Stop waits for owned update work and leaves it stopped. OPENCLAW_NO_RESPAWN refuses before changes and gives manual instructions.

> Use the coordinated openclaw update path when possible. A Gateway already running the new detection code can also notice manual package replacement and drain toward managed restart or foreground relaunch with openclaw gateway run ; an old running binary cannot gain that behavior from replacement files alone. If Stop remains unconfirmed, inspect the updater and retry Ctrl+C in the original terminal or SIGTERM to the original process, as described in update execution .

> Unsafe required state exits with code 78 and a repair reason. FUSE recovery needs same-directory hardlinks and directory synchronization; if the filesystem cannot provide them, expose the same retained data through its native backing path before retrying. Stop writers and run same-state offline openclaw doctor --fix when instructed or when a specific historical repair remains; a separate offline command is no longer required for every supported image swap.

> Advanced operators can archive a supported detached managed worktree without losing partially staged edits, using openclaw worktrees remove \<id> --exact-state \<file> with a request matching its observed state, then openclaw worktrees restore \<id> to recover it. This is an explicit archival route, separate from ordinary force removal. The original checkout is retained for 30 days, so its disk space is not immediately reclaimed.

> Exact-state restoration requires a supporting runtime, a full non-sparse checkout, Git file refs and a supported index. Restoration normally returns the retained checkout, including later file writes; if only the snapshot survives, recovery covers eligible files and exact staging rather than a complete filesystem image or unrelated ignored caches.

> Bzip2 skill archives can now be extracted without installing a system tar command. Finalizing an uploaded archive also lets OpenClaw continue handling other work while it hashes and stores the archive, and uploads that expire before finalization or a repeated commit are rejected. The rest of the upload's database work now runs in the background too, with expiry checked after queued work is admitted. Existing extraction permissions and protection for uploads already in use by an installation remain in place.

> Updated Windows startup and recovery helpers avoid opening an extra blank console during background launches. Interactive commands keep their terminal, and the change takes effect when the replacement helpers run.

> Explicit terminal status now takes precedence over contradictory output-limit hints, avoiding an unnecessary continuation request while keeping genuine length recovery available.

> If an older save trimmed a command, reapply the original command to repair it. When creating jobs from scripts, omit working-directory flags to use defaults instead of passing empty strings.

> Task details show complete command inputs with sensitive values redacted, and distinguish live Running , Queued , waiting, and Finished execution from a saved task record. Quiet background commands can still show as running, while delayed activity no longer makes finished work look active. Finished describes execution, so success and pending result delivery remain separate facts, and unavailable activity does not by itself mean failure.

> Failure notices offer concise previews with full diagnostics available through tasks show , and unreadable task metadata produces an explicit error instead of a falsely empty list. Previously truncated command inputs cannot be reconstructed, and command output remains bounded.

> The GitHub reader brings public issues, pull-request discussions, commits, and expandable diffs beside your conversation, so you can inspect a reference without leaving chat. Tabs let you keep several items open, while previews and refreshable snapshots of automated checks help you follow the work. The reader is public-only and read-only, with private content and edits staying on GitHub; check results are bounded snapshots, not a merge-readiness verdict.

> Applying cloud results and restoring rollback snapshots preserve exact supported filenames and file contents independently of Git attributes or checkout encodings. Canceling private preparation waits for staging cleanup to settle; the host filesystem’s filename restrictions still apply.

> Command errors now distinguish an unsupported command form from a human denial and explain how to retry through the approval flow. Unsupported forms remain blocked. The approvals guide also clarifies the existing approvals get --node and approvals set --node commands, with --file or --stdin supplying a replacement policy.

> Sandboxed sessions can work on an authorized registered project with worktree: true in a private Docker or Podman checkout, with accepted changes returned to the managed worktree. Host Git credentials and ignored provisioning stay outside that checkout. Explicit read-only access remains read-only, and unsupported backends refuse this workflow. Later files created only on the host need git add before entering an existing private checkout. Let pending changes finish before downgrading, and use a supporting version to recover unfinished work, as described in managed project workspaces .

> In Discord, /new and /reset in unbound channels now respect channel disablement, allowlists, group policy, and server command authorization before changing a session. Previously bypassed commands may now be refused, while existing configured-binding recovery exceptions remain available.

> Remote terminal typing and paste require less preparation, while tool-output redraws and scrollback reading avoid repeated work. On macOS and Linux, a terminal launched through Bun can also find a real Node installation when a shim hides it, keeping input and cursor keys working. A real Node installation is still required.

> Agent requests skip unused diagnostics when debug logging is off, and media progress sections share a fresh task read within each turn. Large-request diagnostics and shell setup also avoid some repeated preparation before execution; these changes concern local setup work rather than media generation speed.

> These fixes address interrupted work, misleading command failures, and database waits that could get in the way of everyday use.

> A terminal on a paired node now reports a timeout and removes its local terminal session after the existing 30-second inactivity limit, even if the node never sends its first heartbeat. Each heartbeat renews that limit. OpenClaw requests cancellation once, but the local timeout does not confirm that the remote process has stopped.

> When a long terminal-upload filename needs shortening, the resulting name still follows the portable rules for reserved names and trailing characters. This applies to newly staged uploads and leaves existing filenames alone.

> Gateway and command tests coordinate startup, background work and teardown more explicitly. Isolated ports, profiles and workspace fixtures help preserve coverage for complete workflows without letting unrelated activity interfere with assertions.

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
## Nearby in Developer Workflow

- Earlier: 2026-09-23 · Cursor · [[Changes/Cursor/2026-09-23-when-a-pull-request-opens-rollouts-reads-the-diff-and-the-systems-it-touches-the|Monitoring plans]]
- Later: 2026-09-24 · Claude Code · [[Changes/Claude Code/2026-09-24-changed-windows-wsl-managed-settings-so-an-admin-policy-that-is-present-but-inva|Changed Windows/WSL managed settings so an admin policy that is present but invalid…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-23-6f2950&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-23-31-developer-workflow-changes-in-v2026-9-6.md%0ACard%20ID%3A%20openclaw-2026-09-23-6f2950%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->