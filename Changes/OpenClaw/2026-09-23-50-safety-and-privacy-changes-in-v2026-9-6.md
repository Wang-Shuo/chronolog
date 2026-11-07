---
card_id: openclaw-2026-09-23-0c5420
date: '2026-09-23'
description: 'OpenClaw · 2026-09-23 · Safety and Privacy: 50 changes in v2026.9.6
  — If Node explicitly denies permission to start worker threads, OpenClaw can check
  SQLite…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2248
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4a96140c5f6459788542162d7e61e2a12a064a31d95e5a36018b580b14923c27
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-23-0c5420
  comparison: ''
  date: '2026-09-23'
  description: 'OpenClaw — v2026.9.6: 50 Safety and Privacy changes'
  evidence:
  - quote: If Node explicitly denies permission to start worker threads, OpenClaw
      can check SQLite in the current process instead of incorrectly reporting that
      SQLite is unavailable. This helps setup and diagnostics in restricted environments
      while leaving permissions and the Gateway's other worker requirements in place.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: When Podman cannot create a sandbox because its host-side init helper is
      missing, the error now explains what to repair. Install catatonit or correct
      its configured path on the computer running the Podman engine, including inside
      Podman Machine when you use it. The Podman setup guide covers this requirement,
      which you must supply before retrying with the existing sandbox protections
      enabled.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Eligible connections served from the same Gateway's HTTPS origin can fetch
      inline transcript artifacts as raw file bytes, with fresh download permission
      on each click. The connection-bound links expire after five minutes and are
      not share links. Proxy operators must forward /api/artifacts/download/ under
      the configured UI mount, as described in the client guide ; other connections
      and failed HTTP transfers retain the authenticated chat-connection path. Reconnecting
      or closing the preview prevents an outdated transfer from saving.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Self-contained HTML attachments can fill the available height beside chat,
      making larger reports and interactive pages easier to inspect. Same-origin UTF-8
      HTML previews now support up to 2 MiB, while text, Markdown and workspace reading
      or editing retain their 256 KiB limits. Cross-origin HTML remains download-only
      and the preview's sandbox permissions are unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Agent questions keep entered answers and selected options while you move
      between them, retain the original wording after completion, and stay with the
      conversation they came from. Optional questions remain reachable above the composer
      or in a minimized strip, and unedited questions can move to history after later
      successful work while remaining reopenable. Archival supplies no answer or permission,
      secret answers remain masked, and blocking questions retain their separate Skip
      action. Ordinary and Other answers now support multiple lines, with Enter adding
      a line and Cmd/Ctrl+Enter submitting. Unfinished optional answers can recover
      after reload, reconnect or switching conversations in the same browser and authenticated
      Gateway identity, within a seven-day expiry and shared 20-record limit. Incognito
      and deletion retire saved data, and storage or conflicting-tab problems show
      a warning.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Available Right Now includes tools bound to the current conversation and
      refreshes after a session reset, so the inventory better reflects the tools
      that conversation can use. Opening Tools also avoids refreshing the entire model
      catalog unnecessarily. Inspecting this list does not add tools or grant permission
      to run them.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: An approved browser can also finish reconnecting when pairing approval
      overlaps its handshake, while current identity and permission checks still apply.
      Disconnects without a supplied reason explain whether reconnection is automatic
      or needs a retry.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Backups also recognize duplicate registrations of the same database and
      preserve committed journal data across supported hardlink aliases. If a core
      database has hardlinks, include every alias in the backup's admitted resources
      and stop writers when directed; conflicting owners, ambiguous journals or capture-time
      changes still prevent an archive. Maintaining a private snapshot does not grant
      permission to maintain its live source.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Doctor preserves explicitly chosen workspace locations, leaves comments
      and formatting alone when no repair is needed, and keeps session-store ownership
      through unrelated settings changes. It can offer confirmed recovery of a removed
      owner setting from an eligible root-only, same-store backup, while conflicting
      tool lists are repaired only when permissions can be preserved. Ambiguous permission
      changes remain your decision, and a refused configuration write stops dependent
      service repair.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: For deferred maintenance, stop the Gateway through its service owner, run
      openclaw update repair , then start it through the same owner. Required database
      repairs, invalid settings, lost permission or a repair process that may still
      be writing prevent completion; a warning does not mean every check passed.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: New reports explain when another OpenClaw process is using the same state,
      distinguish invalid configuration from a validator that could not run, and preserve
      sanitized npm causes with relevant disk-space, permission or missing-version
      guidance. These capture improvements apply to runs using the updated updater;
      they cannot add details to an older run.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Canceled Mattermost sends stop before their next recipient lookup, upload,
      or posting request, and shared message actions stop later recipient lookups
      after cancellation. Teams polls also stop before submission when permission
      to send ends. Already accepted messages and polls keep their delivery results
      and vote tracking, so cancellation does not retract something already sent or
      guarantee that an in-flight request can be stopped.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Unchanged Skills no longer trigger needless session rebuilds and chat metadata
      refreshes, and identical copies stop producing duplicate precedence warnings.
      Instruction edits and changes to which skill takes priority still refresh the
      session, while supporting scripts and assets continue updating in sandbox copies.
      Discovery also handles returning to an idle workspace and, on Windows, deleting
      and recreating a skill folder or its parent. Skill folders added during a rescan
      stay watched for later edits, and filtering Skills keeps each group that remains
      visible in its existing open or closed state.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Safety guides and supporting files also stop triggering quarantine or critical
      audit findings solely for prompt-related wording. Three keyword rules were removed
      for both harmless guidance and actual instruction-override text, without a replacement
      detector. Credential checks, approval policy and other blocking rules still
      apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The native apps make everyday conversations easier to write, read, and
      return to, with more room for replies and clearer controls when a connection
      or permission needs attention.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Android chat brings Gallery, File, and Location into the attachment menu,
      with a microphone tap for dictation and a long press for voice options. Location
      goes into a draft you can review before choosing Send, using only the foreground
      permission and precision you allowed. Failed tools and recovery instructions
      are easier to read, and tapping an eligible reply's timestamp opens its recorded
      model, token use, and estimated cost. Those details describe one model call,
      so they are not a whole-conversation total or a final bill.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Mac permission controls can request missing Screen Recording or Accessibility
      access through Grant, with System Settings nearby when more help is needed.
      After updating both the native app and Gateway, interacting with OpenClaw also
      gives agents basic recent-computer activity without Accessibility permission.
      The renamed System-wide presence detection option stays off by default and needs
      Accessibility for activity in other apps. Turning it off now disables only system-wide
      detection, including for previously disabled preferences; app-local activity
      remains eligible and does not prove who is physically at the computer or which
      device sent a message.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Existing native-app languages receive refreshed labels for Android controls,
      Wear reply reading, Apple chat and progress, and Mac consent screens. The translations
      help explain the current controls and permissions without introducing new languages
      or changing what those permissions allow.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Models settings now brings global defaults and the selected agent's provider
      connections into one workflow, preserving unfinished setup input during rescans.
      Saving credentials leaves model activation as a separate choice. A model-only
      change preserves a compatible saved runtime but clears an incompatible saved
      runtime and its native consent so configured routing can apply. Explicitly choosing
      an incompatible runtime, or a model whose configured native runtime is unavailable,
      still rejects the change without altering the session. Model and effort controls
      remain usable in narrow chats, with more accurate refresh feedback, supported
      thinking choices, and Fast preferences for delegated work. Agent-requested model
      changes through session_status now use Gateway checks for runtime, sandbox,
      worker placement, and the intended session, rejecting stale or incompatible
      updates without changing agent or global defaults.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: You can select installed OpenCode, Qwen Code, Pi ACP, and Kilo Code agents
      from Models settings and use their streamed replies in ordinary chat. Install
      and sign in to the app on the computer running OpenClaw, then use the discovery
      feedback and Check again control to resolve unavailable models. Detection alone
      does not confirm sign-in. Native-agent setup explains how an administrator's
      Continue for this chat grants Full Access, turns off optional sandboxing for
      that chat, and consents to the native app's permissions. Required sandbox and
      workspace boundaries still apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: An explicitly selected CLI that is unavailable now reports the failure
      instead of silently switching to API access. Restore that CLI or explicitly
      choose an API route. Claude's picker labels help distinguish those routes, but
      an API-key account still incurs API charges through Claude CLI. Native consent
      must be renewed after a reset, runtime change, or stronger settings and does
      not carry into forks; deleting the OpenClaw session leaves the native app's
      history intact.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: An installed, signed-in GitHub Copilot CLI can now supply models for ordinary
      web and channel conversations. Copilot setup uses the account running OpenClaw
      on that computer, with access and billing owned by Copilot; explicit bring-your-own-key
      settings and environment tokens can affect which account is used. Discovery
      is enabled by default, and disabling it stops new discovery and turns while
      admitted work continues. These native turns use the app's host permissions,
      without OpenClaw sandbox or workspace-only confinement.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: TypeSafe Jev lets supporting plugins choose among options, score supplied
      information, or estimate whether a condition is met. It uses the optional Decision
      Model role, which stays separate from chat and is off by default. Selecting
      a decision model does not start background work or give an agent new tools or
      permission to act.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Codex account status now identifies the selected connection and reports
      a deleted profile's own errors instead of showing another subscription as active.
      Credential import asks for consent before inspection, and upgrade guidance distinguishes
      missing local profiles from provider authentication failures. Follow the agent-
      and profile-specific recovery guidance and verify the result with an unfiltered
      auth list; credentials are not imported automatically. Migration guidance also
      explains when secret inspection can still prompt for Keychain access. Onboarding
      now explains the import scope before review and apply, including that sessions
      and chat history are excluded, credentials require separate consent, and configuration
      and hooks need manual review.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Older adopted chats without a saved source keep their history but need
      fresh adoption into a new chat. Pinned chats need their original source restored,
      or the replacement adopted separately. Older nodes require an update and refreshed
      capability approval to continue, and native terminal or paired-node CLI resume
      requires a local stdio source. Archiving a parent protects active descendants,
      while required requests and tool arguments must still fit the history limits.
      Sandbox-required sessions cannot use host-only forks, and rewinding or switching
      branches can reduce prompt-cache reuse without erasing provider-side history.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Interactive Codex sandbox commands now receive real terminals, Ctrl-C reaches
      interactive and noninteractive commands, and exit results identify the requested
      process. If command execution is allowed but process management is denied, permitted
      commands can finish in the foreground while background continuation and explicitly
      excluded shell tools remain unavailable. POSIX installations running Bun need
      a real Node runtime for terminal helpers. Cleanup retains owned resources until
      work settles, including canceled readiness probes.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: With OpenClaw's sandbox exec-server and a retained sandbox lease, canceling
      a turn now stops its own processes and admitted child work while preserving
      independent background work in the same native thread. Revoking the original
      source can still stop its retained work; releasing the final lease cleans up
      children, and other native execution modes retain thread-wide cleanup.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Scheduled jobs keep their own execution and result-saving lifetime after
      the conversation turn that created them ends. Their command launcher remains
      available after background handoff, and parent conversations stay available
      while delegated work or its delivery is pending. Canceling a job or withdrawing
      message permission stops later message actions while preserving records of deliveries
      already accepted.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Completed child results can reach a parent after it yields, and delayed
      cross-session replies can resume a requester after its original connection ends.
      The retained permission context lasts within the running process; restart recovery
      and explicit retries require newly admitted authority. Later turns recognize
      earlier pending children without restarting them, and matching late results
      are accepted without resending input. Running children continue through existing
      completion delivery, while paused children still need a continuation through
      sessions_send .
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Ask the agent to open an app in Crabbox and show it beside your chat, then
      keep working with the same machine on later turns. Attached apps need a configured
      Crabbox profile and a persistent conversation outside a sandbox. Attached machines
      skip unnecessary agent startup preparation because the agent stays on its original
      host and workspace. Native Linux apps also need a desktop-enabled profile and
      the Cloud Worker Desktop lab, while web apps open in a Portal. Files must be
      copied or prepared on that machine explicitly. Closing the panel leaves apps
      running, so save the outputs you need and stop the Crabbox when finished.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Chrome extension setup now shares one inspect, install, and verify flow
      across desktop apps, the CLI , and the TUI . Use openclaw browser extension
      setup --action inspect or /browser-setup inspect to see what still needs attention,
      with install and verify actions available from the same commands. Setup preserves
      your selected browser profile and distinguishes installation, Chrome approval,
      and an authenticated connection. It runs on the computer hosting the command,
      including the remote host when you use SSH. A remote Gateway still needs a browser
      node on the computer running Chrome, and Chrome's extension installation and
      permission approval remain required.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Setup also requires participant consent, Developer Tools access, and manually
      reduced macOS SIP debugging protections. Every allowed handle has owner authority,
      only one managed call can run at a time, and agent-initiated calls require one-shot
      approval. Follow the setup guide before enabling it.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The default Node executor runs with the Gateway’s operating-system privileges
      and is not a security sandbox. Choose quickjs through tools.codeMode.executor
      for an isolated guest, or disable Code Mode when trusted Node execution is inappropriate.
      Explicit legacy quickjs-wasi choices migrate to QuickJS; choosing an executor
      alone does not force activation. An unavailable selected executor fails without
      falling back, and neither executor resumes cells after a Gateway restart.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Session writers can publish ordinary changes from sessions they created
      through the configured shared GitHub account . Membership in someone else’s
      session does not grant that right. Adding, editing, deleting, or renaming GitHub
      Actions workflow files, and publishing through a personal account, require full
      operator write permission. Queued requests stay tied to the original requester
      and accepted permission ceiling across restarts; a new invitation or later promotion
      cannot revive an ended grant. Results GitHub already accepted can still be recorded
      after a disconnect, but that does not authorize another write. Uncertain readback
      remains pending.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Agents can discover configured cloud profiles and request an advertised
      operating system and machine size when starting a separate visible worktree
      session. The cloud-session tool path requires a live hosted Gateway, a supported
      provider, and the existing placement permissions. Failed or uncertain starts
      retain the session for inspection without silently running locally, so inspect
      that state before retrying. Work already assigned remotely also avoids provisioning
      an unrelated local Docker sandbox.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Cloud workspaces can return larger rebases within increased transfer limits,
      and transfers work on POSIX hosts whose defaults create group-writable directories.
      The permission repair applies only to OpenClaw-owned directories, preserving
      transferred file modes and the host’s defaults. Large returns remain bounded
      at 500,000 before-and-after records and 768 MiB of changed content or patch
      data, with the existing 64 MiB per-file and 256 MiB compressed rollback limits.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Grouped, searchable settings bring related fields and permissions together,
      and Ask OpenClaw opens an editable, unsent help draft for the selected plugin.
      Administrators can explicitly reveal a stored literal API key for a declared
      field at the current configuration revision; secret references and environment
      values are not resolved or revealed. Damaged installations get recorded-source
      reinstall guidance rather than a misleading consent request, while complete
      plugins still require capability consent.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Permission checks now cover more of the moments when a chat starts, a file
      is read, or background work continues after its original request. These changes
      also make credential repair and access changes clearer for people operating
      OpenClaw.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: A native-agent chat now asks for the required confirmation before saving
      or running its first message. An eligible administrator can choose Continue
      for this chat , which grants Full Access and disables optional sandboxing for
      that chat, then retries the original message once while keeping an inherited
      model selection. Declining leaves the message unsent, although an empty chat
      may remain. Consent applies only to that chat and runtime, and cannot waive
      mandatory sandbox, workspace, or remote-execution restrictions. The native-agent
      permission guide explains this choice.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Native hook responses arriving after their deadline also return a timeout
      instead of a late success. Default Codex permission checks deny on that timeout;
      this does not cancel work already running on the server.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Standalone tool calls now follow an authenticated operator's agent and
      sandbox restrictions even when no saved session exists. Automation that relied
      on that exception may now be refused; callers required to use a sandbox must
      first create and target a recorded sandboxed session. Agent shell scripts also
      need to send reports through available attributed session tools or normal subagent
      completion, so their messages retain their agent origin. The shell marker used
      for this check is not authentication or isolation from other processes owned
      by the same user.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Role restrictions now preserve the access they still permit, such as narrowing
      a write credential to read-only. Built-in tools retain their permitted default
      access, while explicitly supplied permission lists stay exact, including an
      empty list. Queued and delegated work keeps the initiating operator's permission
      ceiling and respects later revocation; incompatible queued inputs wait in order
      instead of borrowing stronger permissions.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: File patches also recheck permission before changing files, and operator
      logs explain which workspace restriction rejected a patch without relaxing required
      roots. Automatic cleanup now follows each sandbox owner's retention settings,
      so one agent's shorter retention window does not prematurely remove another's
      working environment.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Sessions that require a sandbox now reject host-only native forks before
      creating the new conversation. If permissions change during creation, initialization
      stops and cleanup removes only the unfinished work still owned by that operation.
      Plugin authors should adopt sessionForkV2 and its checks immediately before
      native changes. The older sessionFork remains source-compatible through October
      12, 2026, but does not gain those final checks.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Background commands using the optional secret proxy on the Gateway host
      now keep HTTPS access after the originating turn ends. Each command retains
      its original secrets and allowed destinations until it stops. After changing
      credentials or bindings, stop older commands to revoke their access immediately
      and start a new run and command to use the changes. Exit, cancellation, timeout,
      and Gateway shutdown also revoke access. This proxy does not cover sandbox,
      remote-node, or provider-native shell execution.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Chat images, documents, and trusted audio now retain the requesting sender's
      file restrictions throughout preparation. Pending reads and copies stop when
      access is revoked, the workspace or execution location changes, or the turn
      is canceled, and rejected preparation removes its newly staged files. Already-produced
      text remains available, while previously retained attachments keep their existing
      retention rules. These boundaries are covered in the Control UI security model
      .
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Pending session previews and local tool inventories now recheck access
      and the exact conversation before returning content, while queued plugin context
      stays with its selected conversation across resets and conflicting names. Recovery
      continuations also check permission on their destination conversation. An ordinary
      disconnect does not cancel admitted work, but revoking its original permission
      can.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Administrators can grant operator.sessions.read and operator.sessions.write
      for conversation work without granting general settings, secrets, or administration
      access. A verified person with session-write access can create their own conversations
      using valid saved defaults or Gateway model and account selection, and Stop
      stays tied to the original run and caller. Shared read access does not grant
      permission to change someone else's conversation. Explicit personal-account
      selection and changing defaults still require broader write access, and these
      permissions are not a boundary around just one session.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Credential preparation and permission checks share existing helpers and
      avoid repeated reads or unused data preparation. The work retains current account
      selection, access rules and redaction behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Model and provider processing avoid repeated catalog searches, metadata
      preparation and response parsing. Selection precedence, permission checks, provider
      output and fallback rules remain intact.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 50-safety-and-privacy-changes-in-v2026-9-6
  source_release: openclaw-2026-09-23-v2026-9-6-3f12c824
  source_type: openclaw_changelog
  theme: safety-privacy
  title: 50 Safety and Privacy changes in v2026.9.6
  type: change
related_changes:
- '[[Changes/Devin/2026-09-23-devin-resumes-right-after-permission-responses|Devin
  Resumes Right After Permission Responses]]'
- '[[Changes/Kimi Code/2026-09-23-harden-workspace-security-block-file-tools-from-accessing-files-outside-the-work|Harden
  workspace security]]'
- '[[Changes/Lovable/2026-09-23-redesigned-project-security-view|Redesigned project
  Security view]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|openclaw-2026-09-23-v2026-9-6-3f12c824]]'
source_type: openclaw_changelog
theme: safety-privacy
title: 50 Safety and Privacy changes in v2026.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 50 Safety and Privacy changes in v2026.9.6

**OpenClaw** · 2026-09-23 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.6) · from [[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|v2026.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> If Node explicitly denies permission to start worker threads, OpenClaw can check SQLite in the current process instead of incorrectly reporting that SQLite is unavailable. This helps setup and diagnostics in restricted environments while leaving permissions and the Gateway's other worker requirements in place.

> When Podman cannot create a sandbox because its host-side init helper is missing, the error now explains what to repair. Install catatonit or correct its configured path on the computer running the Podman engine, including inside Podman Machine when you use it. The Podman setup guide covers this requirement, which you must supply before retrying with the existing sandbox protections enabled.

> Eligible connections served from the same Gateway's HTTPS origin can fetch inline transcript artifacts as raw file bytes, with fresh download permission on each click. The connection-bound links expire after five minutes and are not share links. Proxy operators must forward /api/artifacts/download/ under the configured UI mount, as described in the client guide ; other connections and failed HTTP transfers retain the authenticated chat-connection path. Reconnecting or closing the preview prevents an outdated transfer from saving.

> Self-contained HTML attachments can fill the available height beside chat, making larger reports and interactive pages easier to inspect. Same-origin UTF-8 HTML previews now support up to 2 MiB, while text, Markdown and workspace reading or editing retain their 256 KiB limits. Cross-origin HTML remains download-only and the preview's sandbox permissions are unchanged.

> Agent questions keep entered answers and selected options while you move between them, retain the original wording after completion, and stay with the conversation they came from. Optional questions remain reachable above the composer or in a minimized strip, and unedited questions can move to history after later successful work while remaining reopenable. Archival supplies no answer or permission, secret answers remain masked, and blocking questions retain their separate Skip action. Ordinary and Other answers now support multiple lines, with Enter adding a line and Cmd/Ctrl+Enter submitting. Unfinished optional answers can recover after reload, reconnect or switching conversations in the same browser and authenticated Gateway identity, within a seven-day expiry and shared 20-record limit. Incognito and deletion retire saved data, and storage or conflicting-tab problems show a warning.

> Available Right Now includes tools bound to the current conversation and refreshes after a session reset, so the inventory better reflects the tools that conversation can use. Opening Tools also avoids refreshing the entire model catalog unnecessarily. Inspecting this list does not add tools or grant permission to run them.

> An approved browser can also finish reconnecting when pairing approval overlaps its handshake, while current identity and permission checks still apply. Disconnects without a supplied reason explain whether reconnection is automatic or needs a retry.

> Backups also recognize duplicate registrations of the same database and preserve committed journal data across supported hardlink aliases. If a core database has hardlinks, include every alias in the backup's admitted resources and stop writers when directed; conflicting owners, ambiguous journals or capture-time changes still prevent an archive. Maintaining a private snapshot does not grant permission to maintain its live source.

> Doctor preserves explicitly chosen workspace locations, leaves comments and formatting alone when no repair is needed, and keeps session-store ownership through unrelated settings changes. It can offer confirmed recovery of a removed owner setting from an eligible root-only, same-store backup, while conflicting tool lists are repaired only when permissions can be preserved. Ambiguous permission changes remain your decision, and a refused configuration write stops dependent service repair.

> For deferred maintenance, stop the Gateway through its service owner, run openclaw update repair , then start it through the same owner. Required database repairs, invalid settings, lost permission or a repair process that may still be writing prevent completion; a warning does not mean every check passed.

> New reports explain when another OpenClaw process is using the same state, distinguish invalid configuration from a validator that could not run, and preserve sanitized npm causes with relevant disk-space, permission or missing-version guidance. These capture improvements apply to runs using the updated updater; they cannot add details to an older run.

> Canceled Mattermost sends stop before their next recipient lookup, upload, or posting request, and shared message actions stop later recipient lookups after cancellation. Teams polls also stop before submission when permission to send ends. Already accepted messages and polls keep their delivery results and vote tracking, so cancellation does not retract something already sent or guarantee that an in-flight request can be stopped.

> Unchanged Skills no longer trigger needless session rebuilds and chat metadata refreshes, and identical copies stop producing duplicate precedence warnings. Instruction edits and changes to which skill takes priority still refresh the session, while supporting scripts and assets continue updating in sandbox copies. Discovery also handles returning to an idle workspace and, on Windows, deleting and recreating a skill folder or its parent. Skill folders added during a rescan stay watched for later edits, and filtering Skills keeps each group that remains visible in its existing open or closed state.

> Safety guides and supporting files also stop triggering quarantine or critical audit findings solely for prompt-related wording. Three keyword rules were removed for both harmless guidance and actual instruction-override text, without a replacement detector. Credential checks, approval policy and other blocking rules still apply.

> The native apps make everyday conversations easier to write, read, and return to, with more room for replies and clearer controls when a connection or permission needs attention.

> Android chat brings Gallery, File, and Location into the attachment menu, with a microphone tap for dictation and a long press for voice options. Location goes into a draft you can review before choosing Send, using only the foreground permission and precision you allowed. Failed tools and recovery instructions are easier to read, and tapping an eligible reply's timestamp opens its recorded model, token use, and estimated cost. Those details describe one model call, so they are not a whole-conversation total or a final bill.

> Mac permission controls can request missing Screen Recording or Accessibility access through Grant, with System Settings nearby when more help is needed. After updating both the native app and Gateway, interacting with OpenClaw also gives agents basic recent-computer activity without Accessibility permission. The renamed System-wide presence detection option stays off by default and needs Accessibility for activity in other apps. Turning it off now disables only system-wide detection, including for previously disabled preferences; app-local activity remains eligible and does not prove who is physically at the computer or which device sent a message.

> Existing native-app languages receive refreshed labels for Android controls, Wear reply reading, Apple chat and progress, and Mac consent screens. The translations help explain the current controls and permissions without introducing new languages or changing what those permissions allow.

> Models settings now brings global defaults and the selected agent's provider connections into one workflow, preserving unfinished setup input during rescans. Saving credentials leaves model activation as a separate choice. A model-only change preserves a compatible saved runtime but clears an incompatible saved runtime and its native consent so configured routing can apply. Explicitly choosing an incompatible runtime, or a model whose configured native runtime is unavailable, still rejects the change without altering the session. Model and effort controls remain usable in narrow chats, with more accurate refresh feedback, supported thinking choices, and Fast preferences for delegated work. Agent-requested model changes through session_status now use Gateway checks for runtime, sandbox, worker placement, and the intended session, rejecting stale or incompatible updates without changing agent or global defaults.

> You can select installed OpenCode, Qwen Code, Pi ACP, and Kilo Code agents from Models settings and use their streamed replies in ordinary chat. Install and sign in to the app on the computer running OpenClaw, then use the discovery feedback and Check again control to resolve unavailable models. Detection alone does not confirm sign-in. Native-agent setup explains how an administrator's Continue for this chat grants Full Access, turns off optional sandboxing for that chat, and consents to the native app's permissions. Required sandbox and workspace boundaries still apply.

> An explicitly selected CLI that is unavailable now reports the failure instead of silently switching to API access. Restore that CLI or explicitly choose an API route. Claude's picker labels help distinguish those routes, but an API-key account still incurs API charges through Claude CLI. Native consent must be renewed after a reset, runtime change, or stronger settings and does not carry into forks; deleting the OpenClaw session leaves the native app's history intact.

> An installed, signed-in GitHub Copilot CLI can now supply models for ordinary web and channel conversations. Copilot setup uses the account running OpenClaw on that computer, with access and billing owned by Copilot; explicit bring-your-own-key settings and environment tokens can affect which account is used. Discovery is enabled by default, and disabling it stops new discovery and turns while admitted work continues. These native turns use the app's host permissions, without OpenClaw sandbox or workspace-only confinement.

> TypeSafe Jev lets supporting plugins choose among options, score supplied information, or estimate whether a condition is met. It uses the optional Decision Model role, which stays separate from chat and is off by default. Selecting a decision model does not start background work or give an agent new tools or permission to act.

> Codex account status now identifies the selected connection and reports a deleted profile's own errors instead of showing another subscription as active. Credential import asks for consent before inspection, and upgrade guidance distinguishes missing local profiles from provider authentication failures. Follow the agent- and profile-specific recovery guidance and verify the result with an unfiltered auth list; credentials are not imported automatically. Migration guidance also explains when secret inspection can still prompt for Keychain access. Onboarding now explains the import scope before review and apply, including that sessions and chat history are excluded, credentials require separate consent, and configuration and hooks need manual review.

> Older adopted chats without a saved source keep their history but need fresh adoption into a new chat. Pinned chats need their original source restored, or the replacement adopted separately. Older nodes require an update and refreshed capability approval to continue, and native terminal or paired-node CLI resume requires a local stdio source. Archiving a parent protects active descendants, while required requests and tool arguments must still fit the history limits. Sandbox-required sessions cannot use host-only forks, and rewinding or switching branches can reduce prompt-cache reuse without erasing provider-side history.

> Interactive Codex sandbox commands now receive real terminals, Ctrl-C reaches interactive and noninteractive commands, and exit results identify the requested process. If command execution is allowed but process management is denied, permitted commands can finish in the foreground while background continuation and explicitly excluded shell tools remain unavailable. POSIX installations running Bun need a real Node runtime for terminal helpers. Cleanup retains owned resources until work settles, including canceled readiness probes.

> With OpenClaw's sandbox exec-server and a retained sandbox lease, canceling a turn now stops its own processes and admitted child work while preserving independent background work in the same native thread. Revoking the original source can still stop its retained work; releasing the final lease cleans up children, and other native execution modes retain thread-wide cleanup.

> Scheduled jobs keep their own execution and result-saving lifetime after the conversation turn that created them ends. Their command launcher remains available after background handoff, and parent conversations stay available while delegated work or its delivery is pending. Canceling a job or withdrawing message permission stops later message actions while preserving records of deliveries already accepted.

> Completed child results can reach a parent after it yields, and delayed cross-session replies can resume a requester after its original connection ends. The retained permission context lasts within the running process; restart recovery and explicit retries require newly admitted authority. Later turns recognize earlier pending children without restarting them, and matching late results are accepted without resending input. Running children continue through existing completion delivery, while paused children still need a continuation through sessions_send .

> Ask the agent to open an app in Crabbox and show it beside your chat, then keep working with the same machine on later turns. Attached apps need a configured Crabbox profile and a persistent conversation outside a sandbox. Attached machines skip unnecessary agent startup preparation because the agent stays on its original host and workspace. Native Linux apps also need a desktop-enabled profile and the Cloud Worker Desktop lab, while web apps open in a Portal. Files must be copied or prepared on that machine explicitly. Closing the panel leaves apps running, so save the outputs you need and stop the Crabbox when finished.

> Chrome extension setup now shares one inspect, install, and verify flow across desktop apps, the CLI , and the TUI . Use openclaw browser extension setup --action inspect or /browser-setup inspect to see what still needs attention, with install and verify actions available from the same commands. Setup preserves your selected browser profile and distinguishes installation, Chrome approval, and an authenticated connection. It runs on the computer hosting the command, including the remote host when you use SSH. A remote Gateway still needs a browser node on the computer running Chrome, and Chrome's extension installation and permission approval remain required.

> Setup also requires participant consent, Developer Tools access, and manually reduced macOS SIP debugging protections. Every allowed handle has owner authority, only one managed call can run at a time, and agent-initiated calls require one-shot approval. Follow the setup guide before enabling it.

> The default Node executor runs with the Gateway’s operating-system privileges and is not a security sandbox. Choose quickjs through tools.codeMode.executor for an isolated guest, or disable Code Mode when trusted Node execution is inappropriate. Explicit legacy quickjs-wasi choices migrate to QuickJS; choosing an executor alone does not force activation. An unavailable selected executor fails without falling back, and neither executor resumes cells after a Gateway restart.

> Session writers can publish ordinary changes from sessions they created through the configured shared GitHub account . Membership in someone else’s session does not grant that right. Adding, editing, deleting, or renaming GitHub Actions workflow files, and publishing through a personal account, require full operator write permission. Queued requests stay tied to the original requester and accepted permission ceiling across restarts; a new invitation or later promotion cannot revive an ended grant. Results GitHub already accepted can still be recorded after a disconnect, but that does not authorize another write. Uncertain readback remains pending.

> Agents can discover configured cloud profiles and request an advertised operating system and machine size when starting a separate visible worktree session. The cloud-session tool path requires a live hosted Gateway, a supported provider, and the existing placement permissions. Failed or uncertain starts retain the session for inspection without silently running locally, so inspect that state before retrying. Work already assigned remotely also avoids provisioning an unrelated local Docker sandbox.

> Cloud workspaces can return larger rebases within increased transfer limits, and transfers work on POSIX hosts whose defaults create group-writable directories. The permission repair applies only to OpenClaw-owned directories, preserving transferred file modes and the host’s defaults. Large returns remain bounded at 500,000 before-and-after records and 768 MiB of changed content or patch data, with the existing 64 MiB per-file and 256 MiB compressed rollback limits.

> Grouped, searchable settings bring related fields and permissions together, and Ask OpenClaw opens an editable, unsent help draft for the selected plugin. Administrators can explicitly reveal a stored literal API key for a declared field at the current configuration revision; secret references and environment values are not resolved or revealed. Damaged installations get recorded-source reinstall guidance rather than a misleading consent request, while complete plugins still require capability consent.

> Permission checks now cover more of the moments when a chat starts, a file is read, or background work continues after its original request. These changes also make credential repair and access changes clearer for people operating OpenClaw.

> A native-agent chat now asks for the required confirmation before saving or running its first message. An eligible administrator can choose Continue for this chat , which grants Full Access and disables optional sandboxing for that chat, then retries the original message once while keeping an inherited model selection. Declining leaves the message unsent, although an empty chat may remain. Consent applies only to that chat and runtime, and cannot waive mandatory sandbox, workspace, or remote-execution restrictions. The native-agent permission guide explains this choice.

> Native hook responses arriving after their deadline also return a timeout instead of a late success. Default Codex permission checks deny on that timeout; this does not cancel work already running on the server.

> Standalone tool calls now follow an authenticated operator's agent and sandbox restrictions even when no saved session exists. Automation that relied on that exception may now be refused; callers required to use a sandbox must first create and target a recorded sandboxed session. Agent shell scripts also need to send reports through available attributed session tools or normal subagent completion, so their messages retain their agent origin. The shell marker used for this check is not authentication or isolation from other processes owned by the same user.

> Role restrictions now preserve the access they still permit, such as narrowing a write credential to read-only. Built-in tools retain their permitted default access, while explicitly supplied permission lists stay exact, including an empty list. Queued and delegated work keeps the initiating operator's permission ceiling and respects later revocation; incompatible queued inputs wait in order instead of borrowing stronger permissions.

> File patches also recheck permission before changing files, and operator logs explain which workspace restriction rejected a patch without relaxing required roots. Automatic cleanup now follows each sandbox owner's retention settings, so one agent's shorter retention window does not prematurely remove another's working environment.

> Sessions that require a sandbox now reject host-only native forks before creating the new conversation. If permissions change during creation, initialization stops and cleanup removes only the unfinished work still owned by that operation. Plugin authors should adopt sessionForkV2 and its checks immediately before native changes. The older sessionFork remains source-compatible through October 12, 2026, but does not gain those final checks.

> Background commands using the optional secret proxy on the Gateway host now keep HTTPS access after the originating turn ends. Each command retains its original secrets and allowed destinations until it stops. After changing credentials or bindings, stop older commands to revoke their access immediately and start a new run and command to use the changes. Exit, cancellation, timeout, and Gateway shutdown also revoke access. This proxy does not cover sandbox, remote-node, or provider-native shell execution.

> Chat images, documents, and trusted audio now retain the requesting sender's file restrictions throughout preparation. Pending reads and copies stop when access is revoked, the workspace or execution location changes, or the turn is canceled, and rejected preparation removes its newly staged files. Already-produced text remains available, while previously retained attachments keep their existing retention rules. These boundaries are covered in the Control UI security model .

> Pending session previews and local tool inventories now recheck access and the exact conversation before returning content, while queued plugin context stays with its selected conversation across resets and conflicting names. Recovery continuations also check permission on their destination conversation. An ordinary disconnect does not cancel admitted work, but revoking its original permission can.

> Administrators can grant operator.sessions.read and operator.sessions.write for conversation work without granting general settings, secrets, or administration access. A verified person with session-write access can create their own conversations using valid saved defaults or Gateway model and account selection, and Stop stays tied to the original run and caller. Shared read access does not grant permission to change someone else's conversation. Explicit personal-account selection and changing defaults still require broader write access, and these permissions are not a boundary around just one session.

> Credential preparation and permission checks share existing helpers and avoid repeated reads or unused data preparation. The work retains current account selection, access rules and redaction behavior.

> Model and provider processing avoid repeated catalog searches, metadata preparation and response parsing. Selection precedence, permission checks, provider output and fallback rules remain intact.

Source: https://docs.openclaw.ai/releases/2026.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

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
- [[Changes/OpenClaw/2026-09-23-9-automation-and-scheduling-changes-in-v2026-9-6|9 Automation and Scheduling changes in v2026.9.6]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-23-22-model-support-changes-in-v2026-9-6|22 Model Support changes in v2026.9.6]] · Model Support
- [[Changes/OpenClaw/2026-09-23-119-other-changes-in-v2026-9-6|119 other changes in v2026.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-23 · Lovable · [[Changes/Lovable/2026-09-23-redesigned-project-security-view|Redesigned project Security view]]
- Later: 2026-09-24 · Claude Code · [[Changes/Claude Code/2026-09-24-4-safety-and-privacy-changes-in-v2-1-282|4 Safety and Privacy changes in v2.1.282]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-23-0c5420&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-23-50-safety-and-privacy-changes-in-v2026-9-6.md%0ACard%20ID%3A%20openclaw-2026-09-23-0c5420%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->