---
card_id: openclaw-2026-09-19-95471a
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Mobile and Desktop: 23 changes in v2026.9.5
  — Web and macOS chat show each subagent task’s name beside a claw that moves while
  it runs…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1285
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 40a67ddb1e80916d619bf3f2d52dce3f7b8bd166dc82c06b5eabd952f6548e1b
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-95471a
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 23 Mobile and Desktop changes'
  evidence:
  - quote: Web and macOS chat show each subagent task’s name beside a claw that moves
      while it runs, with badges for failures and timeouts. Hover for its status,
      or use keyboard focus in the web UI; screen readers receive the explanation
      too. Reduced Motion keeps the claw still. In web chat, progress folds while
      you read older messages and stays compact as output arrives. Choose Latest to
      follow again. Manual open and closed choices are remembered for that conversation
      across visits and new runs on the same Gateway connection, and reset when you
      reload or switch connections. Completion can reopen progress only when you are
      already at the live end and have not manually closed it.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Progress cards avoid freezing on large runs of unmatched HTML opening tags,
      including in macOS WebKit. New background command tasks save short, redacted
      command previews as their labels, making tests and builds easier to distinguish
      without repeating Running . Existing task labels remain unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: When a split-chat window narrows, the active chat and its file panel now
      fill the available area. Widening it restores the saved desktop proportions
      and independent drafts, while hidden panes stay inactive.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Native shutdown can abandon unfinished calls when its deadline arrives,
      including after five seconds of draining on macOS launchd. An older running
      process still uses its old shutdown code. Where an external service manager
      owns OpenClaw, follow the Doctor recovery instructions to stop and restart it
      through that manager. Keep any preserved repair files until you have verified
      the result.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The Mac app now opens the Web experience by default, with an experimental
      Native option. Mobile and desktop updates also make conversations, connections
      and work waiting for your attention easier to manage.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: With multiple Gateways saved, the Android sidebar now lets you switch between
      them or add another without opening Settings. Add Gateway accepts a QR code,
      image, setup code or manual address and waits for Connect; Cancel keeps your
      current conversation. Unsent text and finished attachments stay with their Gateway,
      agent and conversation. Finish recording, importing or starting a send before
      switching. An offline Gateway stays selectable, but selecting it does not make
      it connected.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The Tauri companion can save direct and SSH Gateways, open independent
      dashboard windows and restore the last successful selection after a restart.
      Quick Chat, desktop actions and the Omarchy panel stay on Primary. Changing
      Primary requires separate confirmation and a saved token-authenticated connection.
      Linux needs an unlocked Secret Service credential store, and saved profiles
      from the separate Swift Mac app are not imported.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Manage Gateways now has focused Add and Edit forms. Back discards unsaved
      form changes; blank credentials retain a saved secret only for the same address.
      Setup, recovery, the manager and Quick Chat follow system appearance while preserving
      in-progress text, with the connected dashboard keeping its own appearance setting.
      On macOS, the Tauri startup crash is fixed and credential-store failures show
      one dismissible notice. Resolve the reported problem, then choose Manage Gateways
      → Try again.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Regular stable releases now start Linux desktop publication automatically.
      While a new bundle finishes, the updater can keep offering the previous signed
      AppImage. Linux downloads finish separately from the core release, so a new
      core version does not mean its desktop download is ready at the same time.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: On iPhone and iPad , completed intermediate work now folds into a tappable
      “Worked” row above the answer. Tap to inspect it and tap again to collapse it.
      Final answers and media stay visible, while active or unanswered work stays
      expanded.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Restoring queued messages now does less repeated database work on Android
      and Apple clients while preserving message and attachment order. Android also
      avoids reading unrelated queued messages before sending one, including messages
      waiting for another Gateway. Existing delivery order and retry behavior stay
      the same.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Completed answers in Android, iOS, native Mac chat and Mac Quick Chat can
      show up to eight cited-source cards. Open a card to read the recorded search
      snippet or page excerpt, then use Open source to visit the page. Cards need
      matching successful research from the same answer, and missing excerpts are
      shown as unavailable. Previews reuse recorded content without fetching the page
      again; Android does not retain this source evidence in its offline transcript
      cache.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: iOS Talk can return to Listening when developer diagnostic output is blocked.
      Delayed cleanup also stays with its original Gateway and account, so reconnecting
      cannot send an old session's close request through your new connection. If the
      original connection has retired, cleanup is rejected there.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The Gateway can keep handling other work while it looks up the device details
      needed for an iOS notification or wake request. Existing direct-device and relay
      registrations keep their current behavior, with no settings change needed.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Linux and macOS deployment images can also reuse a verified cloud-node
      archive after a restart , avoiding repeated compression. This requires updating
      the image recipe. Windows and existing images keep building normally, and worker
      installation and provisioning still happen.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: An agent on the computer running OpenClaw can now control its configured
      desktop without a separately paired node. Enable cua-computer , allow the computer
      tool, and use a vision-capable agent. The configured Gateway desktop is preferred
      by default. If it is unavailable, the request fails without sending input elsewhere.
      Provider setup and native display permissions still apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: For a lock naming another host, including after a machine rename, close
      the browser using that profile and verify its Chromium lock before retrying
      . Automatic cleanup of a browser left by an earlier OpenClaw runtime remains
      limited to Linux and macOS; this adds no Windows cross-runtime recovery. Late
      cleanup from an old Chrome connection also leaves its replacement alone, and
      cancelling a request before it starts preserves other callers' shared browser
      work.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Browser downloads and traces preserve the directory name you requested,
      including trailing spaces, and check the whole path before writing. If your
      output directory passes through a user-created symbolic link, choose its real,
      canonical path . The Invalid path error can now apply even when the final directory
      already exists. The macOS /tmp and /var system aliases remain supported.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: OpenClaw now automatically uses installed native helpers for supported
      guarded file operations on macOS, Linux, and Windows. Moves that must preserve
      an existing destination require that helper. If native mode is off or the helper
      is missing or unsupported, a move to an absent destination is refused with its
      source retained.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: File-based SecretRef credentials now require a private regular file with
      a single hard link. Existing hardlinked credentials can block startup or secret
      activation until you replace them with a new private file at the configured
      path; changing permissions alone is insufficient. Follow the Linux and macOS
      replacement procedure , then run openclaw secrets reload for a running Gateway
      or repair the file before restarting. The separate 1Password broker-token hardlink
      allowance remains in place.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: On POSIX hosts, a managed Signal connection can now use an optional private
      UNIX socket to restrict daemon access by OS user. HTTP remains the default.
      Follow the Signal setup guide for a distinct absolute socket path and a parent
      folder owned by the OpenClaw user with 0700 permissions. Socket failures do
      not fall back to HTTP. This option is unavailable on Windows and does not isolate
      processes running as the same user or administrators; Linux operators must also
      ensure the folder hierarchy has no ACLs granting others access.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The FreeBSD desktop now rejects Gateway token and password files owned
      by another user. If this affects your connection, correct the file ownership
      to match the account running the app or replace the credentials in Settings
      before reconnecting. Rejected files leave your saved settings intact.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Managed worktrees can now share unchanged source-file storage on eligible
      Linux Btrfs, macOS APFS, and Windows ReFS or Dev Drive destinations, while keeping
      each checkout's edits and setup independent. Sharing is selected automatically
      on supported destinations. Repeated APFS checkouts avoid the initial file-by-file
      cloning slowdown, and worktree removal saves recoverable tracked and untracked
      edits with less delay. Creation also checks space for the selected commit, while
      cleanup protects checkouts still being created, restored, or reused.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 23-mobile-and-desktop-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: mobile-desktop
  title: 23 Mobile and Desktop changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-18-claude-code-on-the-web-changed-the-admin-claude-code-setting-labeled-web-to-clou|Claude
  Code on the web Changed the admin Claude Code setting labeled…]]'
- '[[Changes/Google Antigravity/2026-09-19-file-and-network-sandboxing-on-windows-are-now-supported|File
  and network sandboxing on Windows are now supported]]'
- '[[Changes/Ollama/2026-09-19-ollama-s-macos-app-will-now-no-longer-reopen-windows-you-ve-closed-when-activati|Ollama''s
  macOS app will now no longer reopen windows you''ve closed when activating it]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: mobile-desktop
title: 23 Mobile and Desktop changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 23 Mobile and Desktop changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Web and macOS chat show each subagent task’s name beside a claw that moves while it runs, with badges for failures and timeouts. Hover for its status, or use keyboard focus in the web UI; screen readers receive the explanation too. Reduced Motion keeps the claw still. In web chat, progress folds while you read older messages and stays compact as output arrives. Choose Latest to follow again. Manual open and closed choices are remembered for that conversation across visits and new runs on the same Gateway connection, and reset when you reload or switch connections. Completion can reopen progress only when you are already at the live end and have not manually closed it.

> Progress cards avoid freezing on large runs of unmatched HTML opening tags, including in macOS WebKit. New background command tasks save short, redacted command previews as their labels, making tests and builds easier to distinguish without repeating Running . Existing task labels remain unchanged.

> When a split-chat window narrows, the active chat and its file panel now fill the available area. Widening it restores the saved desktop proportions and independent drafts, while hidden panes stay inactive.

> Native shutdown can abandon unfinished calls when its deadline arrives, including after five seconds of draining on macOS launchd. An older running process still uses its old shutdown code. Where an external service manager owns OpenClaw, follow the Doctor recovery instructions to stop and restart it through that manager. Keep any preserved repair files until you have verified the result.

> The Mac app now opens the Web experience by default, with an experimental Native option. Mobile and desktop updates also make conversations, connections and work waiting for your attention easier to manage.

> With multiple Gateways saved, the Android sidebar now lets you switch between them or add another without opening Settings. Add Gateway accepts a QR code, image, setup code or manual address and waits for Connect; Cancel keeps your current conversation. Unsent text and finished attachments stay with their Gateway, agent and conversation. Finish recording, importing or starting a send before switching. An offline Gateway stays selectable, but selecting it does not make it connected.

> The Tauri companion can save direct and SSH Gateways, open independent dashboard windows and restore the last successful selection after a restart. Quick Chat, desktop actions and the Omarchy panel stay on Primary. Changing Primary requires separate confirmation and a saved token-authenticated connection. Linux needs an unlocked Secret Service credential store, and saved profiles from the separate Swift Mac app are not imported.

> Manage Gateways now has focused Add and Edit forms. Back discards unsaved form changes; blank credentials retain a saved secret only for the same address. Setup, recovery, the manager and Quick Chat follow system appearance while preserving in-progress text, with the connected dashboard keeping its own appearance setting. On macOS, the Tauri startup crash is fixed and credential-store failures show one dismissible notice. Resolve the reported problem, then choose Manage Gateways → Try again.

> Regular stable releases now start Linux desktop publication automatically. While a new bundle finishes, the updater can keep offering the previous signed AppImage. Linux downloads finish separately from the core release, so a new core version does not mean its desktop download is ready at the same time.

> On iPhone and iPad , completed intermediate work now folds into a tappable “Worked” row above the answer. Tap to inspect it and tap again to collapse it. Final answers and media stay visible, while active or unanswered work stays expanded.

> Restoring queued messages now does less repeated database work on Android and Apple clients while preserving message and attachment order. Android also avoids reading unrelated queued messages before sending one, including messages waiting for another Gateway. Existing delivery order and retry behavior stay the same.

> Completed answers in Android, iOS, native Mac chat and Mac Quick Chat can show up to eight cited-source cards. Open a card to read the recorded search snippet or page excerpt, then use Open source to visit the page. Cards need matching successful research from the same answer, and missing excerpts are shown as unavailable. Previews reuse recorded content without fetching the page again; Android does not retain this source evidence in its offline transcript cache.

> iOS Talk can return to Listening when developer diagnostic output is blocked. Delayed cleanup also stays with its original Gateway and account, so reconnecting cannot send an old session's close request through your new connection. If the original connection has retired, cleanup is rejected there.

> The Gateway can keep handling other work while it looks up the device details needed for an iOS notification or wake request. Existing direct-device and relay registrations keep their current behavior, with no settings change needed.

> Linux and macOS deployment images can also reuse a verified cloud-node archive after a restart , avoiding repeated compression. This requires updating the image recipe. Windows and existing images keep building normally, and worker installation and provisioning still happen.

> An agent on the computer running OpenClaw can now control its configured desktop without a separately paired node. Enable cua-computer , allow the computer tool, and use a vision-capable agent. The configured Gateway desktop is preferred by default. If it is unavailable, the request fails without sending input elsewhere. Provider setup and native display permissions still apply.

> For a lock naming another host, including after a machine rename, close the browser using that profile and verify its Chromium lock before retrying . Automatic cleanup of a browser left by an earlier OpenClaw runtime remains limited to Linux and macOS; this adds no Windows cross-runtime recovery. Late cleanup from an old Chrome connection also leaves its replacement alone, and cancelling a request before it starts preserves other callers' shared browser work.

> Browser downloads and traces preserve the directory name you requested, including trailing spaces, and check the whole path before writing. If your output directory passes through a user-created symbolic link, choose its real, canonical path . The Invalid path error can now apply even when the final directory already exists. The macOS /tmp and /var system aliases remain supported.

> OpenClaw now automatically uses installed native helpers for supported guarded file operations on macOS, Linux, and Windows. Moves that must preserve an existing destination require that helper. If native mode is off or the helper is missing or unsupported, a move to an absent destination is refused with its source retained.

> File-based SecretRef credentials now require a private regular file with a single hard link. Existing hardlinked credentials can block startup or secret activation until you replace them with a new private file at the configured path; changing permissions alone is insufficient. Follow the Linux and macOS replacement procedure , then run openclaw secrets reload for a running Gateway or repair the file before restarting. The separate 1Password broker-token hardlink allowance remains in place.

> On POSIX hosts, a managed Signal connection can now use an optional private UNIX socket to restrict daemon access by OS user. HTTP remains the default. Follow the Signal setup guide for a distinct absolute socket path and a parent folder owned by the OpenClaw user with 0700 permissions. Socket failures do not fall back to HTTP. This option is unavailable on Windows and does not isolate processes running as the same user or administrators; Linux operators must also ensure the folder hierarchy has no ACLs granting others access.

> The FreeBSD desktop now rejects Gateway token and password files owned by another user. If this affects your connection, correct the file ownership to match the account running the app or replace the credentials in Settings before reconnecting. Rejected files leave your saved settings intact.

> Managed worktrees can now share unchanged source-file storage on eligible Linux Btrfs, macOS APFS, and Windows ReFS or Dev Drive destinations, while keeping each checkout's edits and setup independent. Sharing is selected automatically on supported destinations. Repeated APFS checkouts avoid the initial file-by-file cloning slowdown, and worktree removal saves recoverable tracked and untracked edits with less delay. Creation also checks space for the selected commit, while cleanup protects checkouts still being created, restored, or reused.

Source: https://docs.openclaw.ai/releases/2026.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-19-20-context-window-changes-in-v2026-9-5|20 Context Window changes in v2026.9.5]] · Context Window
- [[Changes/OpenClaw/2026-09-19-14-collaboration-changes-in-v2026-9-5|14 Collaboration changes in v2026.9.5]] · Collaboration
- [[Changes/OpenClaw/2026-09-19-the-browser-sidebar-gains-a-download-file-button-for-the-image-video-or-document|The Browser sidebar gains a Download file button for the image, video, or document…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-19-29-developer-workflow-changes-in-v2026-9-5|29 Developer Workflow changes in v2026.9.5]] · Developer Workflow
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
- [[Changes/OpenClaw/2026-09-19-6-search-and-browsing-changes-in-v2026-9-5|6 Search and Browsing changes in v2026.9.5]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-19-video-generation-preserves-repeated-reference-positions-so-the-same-image-can-se|Video generation preserves repeated reference positions, so the same image can serve…]] · Music Generation
- [[Changes/OpenClaw/2026-09-19-browser-pages-appear-directly-in-the-chat-panel-header-leaving-more-room-for-the|Browser pages appear directly in the Chat panel header, leaving more room for the page]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-19-7-files-and-data-changes-in-v2026-9-5|7 Files and Data changes in v2026.9.5]] · Files and Data
- [[Changes/OpenClaw/2026-09-19-15-voice-and-audio-changes-in-v2026-9-5|15 Voice and Audio changes in v2026.9.5]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-19-shared-helpers-consolidate-repeated-implementation-including-preparation-and-res|Shared helpers consolidate repeated implementation, including preparation…]] · Video Generation
- [[Changes/OpenClaw/2026-09-19-171-other-changes-in-v2026-9-5|171 other changes in v2026.9.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-09-19 · Ollama · [[Changes/Ollama/2026-09-19-ollama-s-macos-app-will-now-no-longer-reopen-windows-you-ve-closed-when-activati|Ollama's macOS app will now no longer reopen windows you've closed when activating it]]
- Later: 2026-09-21 · ChatGPT · [[Changes/ChatGPT/2026-09-21-you-can-now-track-your-credit-score-in-chatgpt-securely-connect-your-experian-cr|Credit scores in Finances]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-95471a&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-23-mobile-and-desktop-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-95471a%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->