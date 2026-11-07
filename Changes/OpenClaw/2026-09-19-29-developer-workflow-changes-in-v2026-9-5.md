---
card_id: openclaw-2026-09-19-195138
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Developer Workflow: 29 changes in v2026.9.5
  — The installer can reuse your compatible Node and nvm setup without replacing system…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2930
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a04d13b3556bf38c889412be7be5e07b825ab66c4d4681c66fca062a08ee74d0
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-195138
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 29 Developer Workflow changes'
  evidence:
  - quote: The installer can reuse your compatible Node and nvm setup without replacing
      system software or changing your shell profile unnecessarily. If it needs to
      install Node through nvm, it asks first and explains any change to your default
      Node version. If you decline or run unattended, it stops and gives you commands
      to prepare the installation.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Setup and error messages explain how to connect to a Gateway you start
      yourself, using the same account you used for onboarding. Run openclaw gateway
      run in a terminal or manage an installed package service separately. The CLI
      does not install or control FreeBSD services, and it cannot report their status.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Migration commands now keep your selected source, output format and credential
      exclusions when shared options appear before list , plan or apply . Options
      explicitly set on a subcommand still take precedence. Use openclaw migrate plan
      to preview a migration. The apply command does not support dry runs and now
      rejects a preceding --dry-run before changing anything.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The command palette shows Searching sessions… or Searching commands… while
      it is still looking, with local commands available in the meantime. When you
      compose text with an input method, Enter, Escape, and arrow keys stay with that
      input instead of selecting a result or closing the palette.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: A worktree needs a Git checkout. Local means the computer running OpenClaw,
      which may be different from the computer running your browser.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Activity now shows available Git change counts and pull-request previews,
      so you can check coding work without opening every conversation. Review also
      restores missing patches for filenames containing spaces or escaped characters.
      Activity counts describe the checkout or pull request, including applicable
      uncommitted work. Recent pull-request links from the same repository remain
      available after checkout changes, and the check-status control is easier to
      recognize and open.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Pull-request badges now reflect fetched state, and status reads say Loading
      . Shared publication progress can return after reconnecting or reloading, with
      unavailable warnings when fresh GitHub information cannot be fetched.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: For an open or draft pull request, open the CI indicator to see named checks
      and expand GitHub Actions jobs for their steps, statuses, and durations. Details
      refresh while the monitor is open, with warnings and Retry for unavailable,
      partial, or rate-limited results. Full logs open on GitHub; other CI services
      remain listed without Actions step details.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Relative local file references resolve from the session’s selected project
      or worktree and appear as attachments, with existing file-access checks. Files
      on a remote execution host must first arrive through managed attachment delivery.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Within Chat, shell sessions now appear directly in the side-panel header
      beside their status and actions, leaving more room for output. Choose + → Terminal
      again to open another shell.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Full Debug status, health and model snapshots refresh when opened, when
      the connection or agent changes, or when you choose Refresh . Heartbeat and
      command activity stay live.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Updates recognize custom npm installations, handle affected pnpm package-directory
      changes, and check build identity before skipping an explicitly selected same-version
      package. Git updates can prepare their required files before stopping service,
      and Mac package replacement preserves launcher permissions.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Doctor's Git maintenance guide also explains optional cleanup of harmless
      leftover partial-clone markers. Check for missing objects and verify integrity
      first, move markers into the prescribed backup, and keep that backup through
      successful follow-up checks. Cleanup remains a manual choice.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Doctor refusals during affected older Git updates now provide manual recovery
      commands when the previous revision can be verified, or ask you to inspect Git
      history when it cannot. Wait for the updater to exit and use an independent
      terminal; restoring source alone is insufficient after data repairs. Update
      reports also distinguish an unavailable version reading from a real mismatch,
      and separate saved recovery advice from a Gateway responding now. That response
      does not establish that the update succeeded or make rollback safe.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Git and package updates can now finish Doctor work without mistakenly rejecting
      the updater that handed it over. An older updater already running can still
      report Parent executor is suspended for its candidate. After it exits, run openclaw
      update repair --yes --json from the updated installation with the same profile
      and state/config overrides. Check the repair result before restarting a stopped
      Gateway through its service owner.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: For settings that run a command to obtain a secret, a remaining limitation
      can allow that preflight command to start after delegated approval ends. Do
      not rely on canceling the approval to prevent every such command from starting.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Refreshing Git update status clears stale reminders and behind counts when
      the checkout is current or ahead. Update settings also display an inferred Extended
      stable channel correctly.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: You can change supported access rules and reply settings for new work without
      reconnecting the bot. Work already underway keeps the settings it started with.
      Token, connection, account, and native-command changes still require their usual
      refresh.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: New update and restart notices go only to destinations matched to configured
      command owners, and update notices respect account send settings. Unsupported
      destinations lose notices and restart continuations, while update results remain
      in the Control UI. Review owner eligibility and account send settings if chat
      notices stop arriving. Later policy changes do not recall notices already queued.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: An agent can now open a separately visible child session for a registered
      project or managed GitHub repository , optionally in its own worktree. This
      gives delegated work its own place to run and a session you can follow. Visible
      children can also inherit the current conversation while the parent keeps working,
      with their own assignment made explicit after the inherited history.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Choose New workspace to start a task on a cloud worker or eligible paired
      device without supplying a repository. Remote sessions choose it by default
      when you have not explicitly selected a folder, project, or worktree. The selection
      survives draft reload and placement recovery, while explicit source choices
      keep their existing validation.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: If you use custom Homebrew curl or git paths, move HOMEBREW_CURL_PATH and
      HOMEBREW_GIT_PATH from the launch-directory .env into your launching shell or
      ~/.openclaw/.env . Project environment files can no longer choose those executables
      during an approved dependency install.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: OpenClaw's built-in agent runtime now masks recognized and registered secrets
      in completed tool-result text before the next model request, including file
      reads, command output, and tool errors. With redaction enabled, custom rules
      retain built-in credential checks. The release also corrects mistaken masking
      of public status links and masks reflected bot credentials in new Mattermost
      error diagnostics.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Everyday terminal use gains image previews and clearer feedback, while
      managed worktrees can share source storage across more platforms. Background
      history loading helps OpenClaw stay responsive while opening large conversations.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Received and generated images now appear as static previews in Ghostty,
      iTerm2, and Kitty, including supported images in reopened conversations and
      tool cards. Terminal image previews show up to four images per message and keep
      the 24 most recent previews. Unsupported terminals retain readable text, and
      previews are off by default inside tmux and GNU Screen.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The terminal shows your remembered conversation name while startup checks
      finish, then confirms it or falls back to the actual session. Ctrl+C hints no
      longer hide an ongoing response's activity indicator. Local commands resolve
      relative working directories from the session workspace, keeping ~ literal and
      .. parent-relative.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Managed worktree cleanup preserves unpublished work and retains checkouts
      whose branch changed or whose HEAD became detached. Use openclaw worktrees remove
      <id> --if-lossless to remove only eligible clean, published worktrees. Run-end
      cleanup uses the same non-force path.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Linux Gateways running on Node use a small command-launch helper to avoid
      launching covered commands from the large Gateway process, including Git requests
      over its WebSocket connection. If the helper cannot start initially, that Gateway
      process keeps direct launching. Later helper loss fails affected commands without
      rerunning them. Queued launches can still outlast approval revocation, and a
      failed search launch can leave grep waiting. File-limit errors now retain their
      original diagnosis and allow later commands after resource pressure clears;
      the failed command is not retried automatically.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: PR cleanup stops when worktree ownership is ambiguous, orphaned, or incomplete,
      preserving paths and metadata for diagnosis. PR tooling also disables automatic
      maintenance during fetches to avoid unrelated metadata pruning.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 29-developer-workflow-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: developer-workflow
  title: 29 Developer Workflow changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-18-improved-ultrareview-when-there-s-nothing-to-review-messages-say-which-case-you|Improved
  /ultrareview when there''s nothing to review]]'
- '[[Changes/Google Antigravity/2026-09-18-a-command-that-is-killed-when-the-app-restarts-is-now-reported-as-canceled-inste|A
  command that is killed when the app restarts is now reported as canceled instead…]]'
- '[[Changes/Qoder/2026-09-18-worktree-improved-starting-point-list-loading-and-creation-preparation-for-large|Worktree:
  Improved starting-point list loading and creation preparation…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: developer-workflow
title: 29 Developer Workflow changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 29 Developer Workflow changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The installer can reuse your compatible Node and nvm setup without replacing system software or changing your shell profile unnecessarily. If it needs to install Node through nvm, it asks first and explains any change to your default Node version. If you decline or run unattended, it stops and gives you commands to prepare the installation.

> Setup and error messages explain how to connect to a Gateway you start yourself, using the same account you used for onboarding. Run openclaw gateway run in a terminal or manage an installed package service separately. The CLI does not install or control FreeBSD services, and it cannot report their status.

> Migration commands now keep your selected source, output format and credential exclusions when shared options appear before list , plan or apply . Options explicitly set on a subcommand still take precedence. Use openclaw migrate plan to preview a migration. The apply command does not support dry runs and now rejects a preceding --dry-run before changing anything.

> The command palette shows Searching sessions… or Searching commands… while it is still looking, with local commands available in the meantime. When you compose text with an input method, Enter, Escape, and arrow keys stay with that input instead of selecting a result or closing the palette.

> A worktree needs a Git checkout. Local means the computer running OpenClaw, which may be different from the computer running your browser.

> Activity now shows available Git change counts and pull-request previews, so you can check coding work without opening every conversation. Review also restores missing patches for filenames containing spaces or escaped characters. Activity counts describe the checkout or pull request, including applicable uncommitted work. Recent pull-request links from the same repository remain available after checkout changes, and the check-status control is easier to recognize and open.

> Pull-request badges now reflect fetched state, and status reads say Loading . Shared publication progress can return after reconnecting or reloading, with unavailable warnings when fresh GitHub information cannot be fetched.

> For an open or draft pull request, open the CI indicator to see named checks and expand GitHub Actions jobs for their steps, statuses, and durations. Details refresh while the monitor is open, with warnings and Retry for unavailable, partial, or rate-limited results. Full logs open on GitHub; other CI services remain listed without Actions step details.

> Relative local file references resolve from the session’s selected project or worktree and appear as attachments, with existing file-access checks. Files on a remote execution host must first arrive through managed attachment delivery.

> Within Chat, shell sessions now appear directly in the side-panel header beside their status and actions, leaving more room for output. Choose + → Terminal again to open another shell.

> Full Debug status, health and model snapshots refresh when opened, when the connection or agent changes, or when you choose Refresh . Heartbeat and command activity stay live.

> Updates recognize custom npm installations, handle affected pnpm package-directory changes, and check build identity before skipping an explicitly selected same-version package. Git updates can prepare their required files before stopping service, and Mac package replacement preserves launcher permissions.

> Doctor's Git maintenance guide also explains optional cleanup of harmless leftover partial-clone markers. Check for missing objects and verify integrity first, move markers into the prescribed backup, and keep that backup through successful follow-up checks. Cleanup remains a manual choice.

> Doctor refusals during affected older Git updates now provide manual recovery commands when the previous revision can be verified, or ask you to inspect Git history when it cannot. Wait for the updater to exit and use an independent terminal; restoring source alone is insufficient after data repairs. Update reports also distinguish an unavailable version reading from a real mismatch, and separate saved recovery advice from a Gateway responding now. That response does not establish that the update succeeded or make rollback safe.

> Git and package updates can now finish Doctor work without mistakenly rejecting the updater that handed it over. An older updater already running can still report Parent executor is suspended for its candidate. After it exits, run openclaw update repair --yes --json from the updated installation with the same profile and state/config overrides. Check the repair result before restarting a stopped Gateway through its service owner.

> For settings that run a command to obtain a secret, a remaining limitation can allow that preflight command to start after delegated approval ends. Do not rely on canceling the approval to prevent every such command from starting.

> Refreshing Git update status clears stale reminders and behind counts when the checkout is current or ahead. Update settings also display an inferred Extended stable channel correctly.

> You can change supported access rules and reply settings for new work without reconnecting the bot. Work already underway keeps the settings it started with. Token, connection, account, and native-command changes still require their usual refresh.

> New update and restart notices go only to destinations matched to configured command owners, and update notices respect account send settings. Unsupported destinations lose notices and restart continuations, while update results remain in the Control UI. Review owner eligibility and account send settings if chat notices stop arriving. Later policy changes do not recall notices already queued.

> An agent can now open a separately visible child session for a registered project or managed GitHub repository , optionally in its own worktree. This gives delegated work its own place to run and a session you can follow. Visible children can also inherit the current conversation while the parent keeps working, with their own assignment made explicit after the inherited history.

> Choose New workspace to start a task on a cloud worker or eligible paired device without supplying a repository. Remote sessions choose it by default when you have not explicitly selected a folder, project, or worktree. The selection survives draft reload and placement recovery, while explicit source choices keep their existing validation.

> If you use custom Homebrew curl or git paths, move HOMEBREW_CURL_PATH and HOMEBREW_GIT_PATH from the launch-directory .env into your launching shell or ~/.openclaw/.env . Project environment files can no longer choose those executables during an approved dependency install.

> OpenClaw's built-in agent runtime now masks recognized and registered secrets in completed tool-result text before the next model request, including file reads, command output, and tool errors. With redaction enabled, custom rules retain built-in credential checks. The release also corrects mistaken masking of public status links and masks reflected bot credentials in new Mattermost error diagnostics.

> Everyday terminal use gains image previews and clearer feedback, while managed worktrees can share source storage across more platforms. Background history loading helps OpenClaw stay responsive while opening large conversations.

> Received and generated images now appear as static previews in Ghostty, iTerm2, and Kitty, including supported images in reopened conversations and tool cards. Terminal image previews show up to four images per message and keep the 24 most recent previews. Unsupported terminals retain readable text, and previews are off by default inside tmux and GNU Screen.

> The terminal shows your remembered conversation name while startup checks finish, then confirms it or falls back to the actual session. Ctrl+C hints no longer hide an ongoing response's activity indicator. Local commands resolve relative working directories from the session workspace, keeping ~ literal and .. parent-relative.

> Managed worktree cleanup preserves unpublished work and retains checkouts whose branch changed or whose HEAD became detached. Use openclaw worktrees remove \<id> --if-lossless to remove only eligible clean, published worktrees. Run-end cleanup uses the same non-force path.

> Linux Gateways running on Node use a small command-launch helper to avoid launching covered commands from the large Gateway process, including Git requests over its WebSocket connection. If the helper cannot start initially, that Gateway process keeps direct launching. Later helper loss fails affected commands without rerunning them. Queued launches can still outlast approval revocation, and a failed search launch can leave grep waiting. File-limit errors now retain their original diagnosis and allow later commands after resource pressure clears; the failed command is not retried automatically.

> PR cleanup stops when worktree ownership is ambiguous, orphaned, or incomplete, preserving paths and metadata for diagnosis. PR tooling also disables automatic maintenance during fetches to avoid unrelated metadata pruning.

Source: https://docs.openclaw.ai/releases/2026.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-19-20-context-window-changes-in-v2026-9-5|20 Context Window changes in v2026.9.5]] · Context Window
- [[Changes/OpenClaw/2026-09-19-14-collaboration-changes-in-v2026-9-5|14 Collaboration changes in v2026.9.5]] · Collaboration
- [[Changes/OpenClaw/2026-09-19-the-browser-sidebar-gains-a-download-file-button-for-the-image-video-or-document|The Browser sidebar gains a Download file button for the image, video, or document…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-19-5-reliability-and-performance-changes-in-v2026-9-5|5 Reliability and Performance changes in v2026.9.5]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-19-retained-conversation-history-continues-to-follow-current-sharing-permissions-af|Retained conversation history continues to follow current sharing permissions after…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-19-2-enterprise-and-administration-changes-in-v2026-9-5|2 Enterprise and Administration changes in v2026.9.5]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-19-72-agent-mode-changes-in-v2026-9-5|72 Agent Mode changes in v2026.9.5]] · Agent Mode
- [[Changes/OpenClaw/2026-09-19-21-editor-experience-changes-in-v2026-9-5|21 Editor Experience changes in v2026.9.5]] · Editor Experience
- [[Changes/OpenClaw/2026-09-19-28-model-support-changes-in-v2026-9-5|28 Model Support changes in v2026.9.5]] · Model Support
- [[Changes/OpenClaw/2026-09-19-39-safety-and-privacy-changes-in-v2026-9-5|39 Safety and Privacy changes in v2026.9.5]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-19-14-automation-and-scheduling-changes-in-v2026-9-5|14 Automation and Scheduling changes in v2026.9.5]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-19-32-interface-experience-changes-in-v2026-9-5|32 Interface Experience changes in v2026.9.5]] · Interface Experience
- [[Changes/OpenClaw/2026-09-19-you-can-now-set-the-approval-reviewer-s-reasoning-and-optional-fast-mode-indepen|Set the approval reviewer's reasoning and optional Fast mode independently…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-19-you-can-now-install-the-cli-on-freebsd-with-install-cli-sh-using-system-node-and|Install the CLI on FreeBSD with install-cli.sh using system Node and npm]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-19-6-pricing-model-changes-in-v2026-9-5|6 Pricing Model changes in v2026.9.5]] · Pricing Model
- [[Changes/OpenClaw/2026-09-19-28-account-and-access-changes-in-v2026-9-5|28 Account and Access changes in v2026.9.5]] · Account and Access
- [[Changes/OpenClaw/2026-09-19-31-memory-and-personalization-changes-in-v2026-9-5|31 Memory and Personalization changes in v2026.9.5]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-19-you-can-now-ask-btw-side-questions-about-photos-attached-to-the-current-message|Ask /btw side questions about photos attached to the current message when using…]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-19-52-apps-and-integrations-changes-in-v2026-9-5|52 Apps and Integrations changes in v2026.9.5]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-19-23-mobile-and-desktop-changes-in-v2026-9-5|23 Mobile and Desktop changes in v2026.9.5]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-19-6-search-and-browsing-changes-in-v2026-9-5|6 Search and Browsing changes in v2026.9.5]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-19-video-generation-preserves-repeated-reference-positions-so-the-same-image-can-se|Video generation preserves repeated reference positions, so the same image can serve…]] · Music Generation
- [[Changes/OpenClaw/2026-09-19-browser-pages-appear-directly-in-the-chat-panel-header-leaving-more-room-for-the|Browser pages appear directly in the Chat panel header, leaving more room for the page]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-19-7-files-and-data-changes-in-v2026-9-5|7 Files and Data changes in v2026.9.5]] · Files and Data
- [[Changes/OpenClaw/2026-09-19-15-voice-and-audio-changes-in-v2026-9-5|15 Voice and Audio changes in v2026.9.5]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-19-shared-helpers-consolidate-repeated-implementation-including-preparation-and-res|Shared helpers consolidate repeated implementation, including preparation…]] · Video Generation
- [[Changes/OpenClaw/2026-09-19-171-other-changes-in-v2026-9-5|171 other changes in v2026.9.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-18 · Qoder · [[Changes/Qoder/2026-09-18-worktree-improved-starting-point-list-loading-and-creation-preparation-for-large|Worktree: Improved starting-point list loading and creation preparation…]]
- Later: 2026-09-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-21-5-developer-workflow-changes-in-v1-0-87|5 Developer Workflow changes in v1.0.87]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-195138&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-29-developer-workflow-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-195138%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->