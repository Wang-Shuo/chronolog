---
card_id: openclaw-2026-09-19-932e84
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Apps and Integrations: 52 changes in v2026.9.5
  — Plugin pages can now join your saved sidebar order alongside built-in pages, keeping…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1276
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1a5a6405d09c1ebca7b4492fb367dd01fd00680986929289411481e845c93eaa
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-932e84
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 52 Apps and Integrations changes'
  evidence:
  - quote: Plugin pages can now join your saved sidebar order alongside built-in pages,
      keeping their places after a reload or temporary absence. Home stays first in
      chip mode. Pages shown by default can be reordered, but only optional plugin
      pages can be dragged out to unpin them.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Standalone RPC and MCP integrations must start screen actions from a Control
      UI connection or a turn begun there; the previous broadcast behavior is no longer
      supported. If the original browser has disconnected or no browser was captured,
      the action returns UNAVAILABLE . Ask again from the open Control UI.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Unavailable configured plugin paths now produce actionable warnings while
      preserving their settings. Fix the reported path or permissions, then run openclaw
      doctor --fix ; the plugin remains unavailable until repaired, and structural
      errors can still block the update. Pending plugin migrations retain their original
      inputs, so conflicting edits are refused until repair finishes. Complete pending
      migrations before returning to an older build when you need to preserve later
      ACP session changes.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: A separate early check stops the update before staging when every eligible
      location has a measured shortage of space for its state snapshot. Free space
      or choose a suitable TMPDIR before retrying. That early inventory excludes plugin
      copies and registered external databases; unknown measurements remain warnings,
      and the complete later check still runs. Older installed updaters retain their
      first-update behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Backups can complete when unrelated application databases contain broken
      references between records, while OpenClaw's managed databases and declared
      plugin databases still receive checked snapshots. Agent and plugin discovery
      works during concurrent writes, including when workspace files are excluded.
      If discovery fails, resolve the error before creating a state backup. --only-config
      saves just the active JSON configuration file, excluding included files, state,
      and external credentials.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Slack keeps one progress card per command, shows interactive choices once,
      and preserves the complete written answer when controls cannot be used. A duplicate
      event waiting in one thread no longer holds up unrelated threads, and compatible
      corrections can reach a queued turn once it starts running.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: You can change supported access and reply settings for new work without
      reconnecting Slack. Replies already underway keep their original settings. Account,
      connection, and other settings that require a restart still reconnect Slack.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Incoming messages remain queued for retry through temporary Slack authorization
      outages, while invalid credentials stay rejected. Socket Mode also handles the
      affected rate-limit and incomplete notifications without crashing the Gateway.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: iMessage setup now offers to correct a command path that points to a folder
      or a file that cannot run. Custom Windows command extensions must be allowed
      by PATHEXT ; passing the availability check still does not guarantee the command
      will launch.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Authorized operators can use Allow Once or Deny on OpenClaw change-approval
      cards in Discord and Slack, and late button responses no longer overwrite the
      final result. Slack can also finish the original pending card after a restart.
      Configured approval forwarding also sends a text prompt when the destination's
      native approval handler is inactive. A local prompt or a recovering handler
      can show the same request again; a handler stopping after the request arrives
      does not trigger rerouting.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: iMessage, WhatsApp, Signal, and Matrix now wait for approval controls to
      finish registering or clearing before reporting that operation complete. Plugin
      authors must await the updated registration and deletion methods and use a supporting
      host. If optional storage fails, the fallback lasts only until the process stops;
      see the approval SDK guidance .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Verified official channel plugins installed through supported external
      installation paths regain replies from delegated work that finishes after the
      original turn ends, including the affected Discord setup. LINE and the shared
      SMS and Zalo webhook paths also keep replies and queued follow-ups alive after
      the initial incoming request finishes. Existing cancellation and access checks
      still apply; this does not extend the official-plugin repair to arbitrary third-party
      plugins.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: In Slack's compact progress mode, the last complete update stays visible
      until the next complete one arrives, instead of being replaced by a word fragment.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Messages now use the room or conversation selected through the active channel
      plugin, without a saved account default adding a conflicting destination and
      blocking the send.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Official Mattermost, Teams, and Feishu installations also restore their
      supported, permitted context reads. Mattermost history reads remain disabled
      until enabled, and Teams member lookup still excludes private and shared channels.
      Authenticated dashboard conversations can use supported official-plugin reads
      under their existing permissions. Channel-origin replies through CLI backends
      also regain permitted Discord actions and Discord/Slack reads; this does not
      grant the same authority to scheduled work.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Update core and the official plugin together. OpenClaw 2026.9.4 lacks the
      required plugin API, so updating the plugin alone is not sufficient. See the
      channel-plugin guidance for the supported read actions.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: These libraries are unpublished and their APIs are unstable. Product integration
      and deployment remain the developer's responsibility, and system.run is not
      included. The bridge authenticates messages without encrypting them, and cancellation
      of native work depends on handlers cooperating.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: On an eligible Mac running OpenClaw, Apple Foundation Models can help with
      setup and short utility tasks without an API key. This optional route requires
      Apple silicon, macOS 27 or later, enabled and downloaded Apple Intelligence,
      Apple developer tools with the macOS 27 SDK, and a model with at least 8,192
      context tokens. Those requirements apply to the Gateway host; connecting a Mac
      app to a Linux or Windows Gateway does not supply the model.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Connecting a provider keeps your chosen model. Replacement sign-ins saved
      through Model Setup stay inactive until you successfully test and explicitly
      activate them. If activation fails, setup can restore your working connection
      without overwriting newer connection edits. If setup requests a plugin update
      or Gateway restart, complete it and retry activation. Before downgrading OpenClaw,
      remove inactive replacement sign-ins or restore the state from before setup,
      because older versions may use them.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Long foreground commands can use their accepted execution time without
      prematurely aborting the whole agent turn. Codex commands on paired nodes also
      honor their resolved command budget; upgrade OpenClaw core and the Codex plugin
      together for that repair. Setting a command timeout to zero disables only its
      process timer, while transport deadlines, Stop and approval limits still apply.
      CLI-backed turns also preserve remaining timeout budgets across detected long
      process freezes.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Hooks that run during daily or idle session resets can now finish delayed
      work after the triggering request ends. This lets a hook wait for another operation
      and continue its work without losing its place when that request finishes.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Click a field in a managed Agent browser panel or Browser dashboard and
      paste plain text with Cmd+V , Ctrl+V , or right-click Paste . Password fields,
      multiline text, and fields inside embedded pages are supported. Paste waits
      for the remote click to succeed and does not submit the form or change the remote
      clipboard. File and image paste and Chrome MCP existing-session profiles remain
      unsupported. See Browser panel controls .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Install or reload supported plugins while your Gateway keeps running, and
      give teammates read-only access to selected conversations.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The CLI also accepts several plugins in one enable, disable, reload, update
      or uninstall command. Earlier successful changes remain if later work fails,
      so review the result before retrying. Local files and marketplace registrations
      must be available on the Gateway computer, and offline installs wait for startup.
      If installation saves but activation fails, follow the repair message and run
      openclaw plugins reload .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: After a replacement timeout, recovery can wait up to 60 seconds for unfinished
      work, restore the previous plugin and restart eligible channels. Cleanup failures
      can still require another reload or a Gateway restart. Restart into the updated
      code to receive this repair. Rebuilt bundled code and enabling experimental
      native plugin UI retain their separate restart requirements; native UI also
      needs a browser reload.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Changing Lossless settings no longer lets cleanup from the old plugin close
      the replacement's database. Eligible failed replacements can recover using the
      previous code and settings, while unchanged plugins keep running. Successful
      cleanup is required before replacement, so slow cleanup delays recovery and
      a cleanup failure can leave the affected plugin unavailable. A plugin replacing
      itself from an active call must wait for that call to finish.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Bun-hosted Gateways can reload supported installed-plugin source through
      the existing source checks, and receive targeted fixes for TypeScript, JSX and
      deferred imports. Node also handles directly imported source SDK code through
      the appropriate loader. Compatibility still depends on the runtime and plugin's
      imports. Some Bun cases require a patched runtime, while conditional package
      exports and indirect source-SDK imports retain known gaps.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Plugin details load through one ClawHub request. Operators of a self-hosted
      registry must add support for /api/v1/packages/{name}/detail before upgrading
      this client.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: With telemetry enabled, deliberate plugin searches send normalized query
      text and remote result counts to ClawHub analytics, which retains queries for
      30 days. Local inventory matches and user, device and session identifiers are
      excluded. Set CLAWHUB_DISABLE_TELEMETRY to opt out while keeping search results
      available.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Plugin Settings can organize options into searchable sections, with per-field
      reset controls and permissions on the same page. Plugins without section definitions
      keep their complete flat form. Text and number edits commit when you leave the
      field, while switches commit immediately. Escape also commits the focused edit
      before leaving Settings.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Administrators can inspect supported credential fields to see whether a
      plugin uses an entered key, an environment fallback or a secret reference, and
      edit declared references directly in Settings. Existing keys stay masked, and
      only a newly entered replacement can be revealed. Environment fallbacks remain
      inspect-only, and read-only configuration cannot be edited.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Use Ask OpenClaw on a plugin or individual setting to prepare a contextual
      question without losing your existing conversation or draft. The question stays
      unsent until you choose Send. Generated value previews withhold recognized sensitive
      values, and help waits while a sensitive setup answer is in progress. This protection
      applies to the generated preview, so check any private information you type
      yourself.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Plugin authors get clearer build and verification errors when a package
      is missing its manifest or a declared JavaScript entry. Builds preserve existing
      manifest and package-folder permissions. Plugins stored beneath a symlinked
      parent directory also regain correct manifest hashes; after updating, use openclaw
      plugins registry --refresh to repair affected registry metadata.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Registration-time api.config and its descendants are now read-only. Plugins
      that mutate them can throw or have writes ignored, so authors need to update
      those integrations. See the related maintenance change .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Earlier successful steps can remain after a later failure, so follow the
      reported recovery instructions before retrying. An interrupted installation
      can also refuse to resume if model or companion-agent availability changes.
      Offline installation still needs a restart. Removing a Claw leaves global plugins
      installed by default; explicitly selected plugin removal waits for active work
      to finish.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Opening a Workboard and claiming a task now involve less unrelated card
      data, so damaged records elsewhere no longer block those actions. Other application
      work can continue while Workboard waits on its database, and plugin reload lets
      already-accepted storage work finish. Damaged records still need attention when
      read directly, and archived cards still prevent a board from being deleted.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Other work can continue while Team Reports waits on its database to save
      a report. Large roster refreshes use fewer writes, and a failed refresh preserves
      the complete previous report and roster. Standalone plugin installations need
      a compatible host with the SQLite worker SDK.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Read-only Doctor checks preserve working MCP OAuth logins by leaving schema
      inspection to authenticated operations that can save refreshed credentials.
      Use --severity-min info to see deferred checks and openclaw mcp probe <name>
      for a configured server. Plugin-provided servers and agent-local profiles need
      an authenticated serving-agent turn. Already-invalid logins still need reauthorization.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Claude CLI tools remain usable after the turn that started their listener
      finishes. Silent configured MCP calls receive the existing 15-minute active-tool
      allowance, with cancellation and transport deadlines still in force. Servers
      denied as a whole no longer start, and unused discovery connections can close
      while retained tools remain available. If cleanup remains unconfirmed, inspect
      or stop the affected processes before rerunning Doctor.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Plugin authors can use awaited storage, task and flow operations so their
      database work can run while other application work continues. Loading saved
      tasks and workflows at startup, during reloads and before awaited SDK reads
      now uses the background worker too. Webhooks and Lobster wait for managed-flow
      saves before returning results or starting dependent work. Data-only keyed-store
      operations now use the shared database worker; callback-based updates, validation
      and serialization still run on the calling thread. The storage migration guide
      explains how to switch interfaces without copying data.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: When a custom context-engine hook fails, the conversation's message order
      and tool-result history are restored for retry. Pending work keeps the resources
      it needs, and delayed subagent cleanup stops incorrectly disabling a healthy
      engine just because its original caller has finished. The history repair restores
      the message list, not arbitrary changes a plugin made inside individual messages.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Intentionally disabling a recognized selected engine uses the built-in
      engine and keeps your choice for re-enabling. A cold start can still report
      a missing engine when its plugin has a different ID and no ownership registration
      is available. Genuine plugin failures retain their existing isolation behavior,
      and earlier quarantine is not automatically cleared.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Deferred plugin webhook callbacks can finish after the request that started
      them ends, while remaining tracked during Gateway shutdown. This repairs the
      closed-request failure that could interrupt background processing. Plugin authors
      using the deferred-work helper should account for callbacks having their own
      lifetime and continuing after the requester cancels.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: With Code Mode enabled, an agent can find native and MCP tools together
      by describing the task it needs to perform. Optional TypeScript checks help
      combine calls and report several errors at once, while existing permissions
      and approvals still apply. Exact tool names now distinguish capitalization,
      and an active wait keeps its tool-call deadline instead of expiring as an idle
      snapshot.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Integrations can request only the files an assistant delivered for a chosen
      run, leaving out user uploads and raw tool observations. Set messageRole to
      assistant together with runId ; the run ID alone does not select outputs. Scoped
      managed downloads return the exact selected file or report it missing when its
      ID is stale.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Older Gateways reject the new filter. Integrations must show that limitation
      instead of silently retrying without it.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Limited tool profiles now also restrict Codex native shell and file access
      , and isolated workers retain the command restrictions set by the Gateway. Keep
      restricted Codex sessions on a compatible managed runtime. Worker commands that
      need unsupported remote approvals must run locally under the configured approval
      policy; incompatible retained workers need recovery or reprovisioning. Workspace
      plugins need explicit trust before replacing configured channels.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The discovery opt-out that OpenClaw saves for native conversations no longer
      produces a misleading disabled-plugin warning or, by itself, enables Codex and
      expands the plugin allow-list. Doctor offers manual guidance for matching historical
      entries, since it cannot tell whether you intended to enable the plugin. Those
      entries are preserved. Other activation rules still apply, including Doctor's
      default-model repair when no model is configured.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Rotating webhook credentials, changing hook policy, or disabling hooks
      now stops outdated pending requests before they dispatch more work. A request
      rejected because settings changed receives 409 and can be retried with the current
      route and credentials. Already accepted work remains accepted, and successful
      replay keeps its original result without launching duplicate work.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Client developers can now add selected-account checks so their apps detect
      when the chosen account no longer matches the signed-in profile. Already accepted
      work keeps its original conversation and receipt through ordinary disconnects
      or later account selection changes. These checks are opt-in; other requests
      keep their existing behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Newly accepted native Codex child results can also support restart recovery
      of a still-owed parent channel reply without rerunning the child. This requires
      a recorded accepted completion and a supported outbound channel route. Control
      UI, route-less, remote-worker, and never-admitted completions are outside this
      recovery path. Update the Gateway and Codex plugin together, and finish pending
      recovery before downgrading.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Some operations still require Node. The worker, provider, and Discord compatibility
      fixes were tested with custom Bun builds; stock Bun 1.4.2 lacks a required SQLite
      fix and still has Slack interoperability limits. They do not establish complete
      support for that stock runtime.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 52-apps-and-integrations-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: apps-integrations
  title: 52 Apps and Integrations changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/Lovable/2026-09-17-connect-your-app-to-the-lovable-api|Connect your app
  to the Lovable API]]'
- '[[Changes/Claude Code/2026-09-18-6-apps-and-integrations-changes-in-v2-1-277|6
  Apps and Integrations changes in v2.1.277]]'
- '[[Changes/OpenClaw/2026-09-19-you-can-now-ask-btw-side-questions-about-photos-attached-to-the-current-message|Ask
  /btw side questions about photos attached to the current message when using…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: apps-integrations
title: 52 Apps and Integrations changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 52 Apps and Integrations changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Plugin pages can now join your saved sidebar order alongside built-in pages, keeping their places after a reload or temporary absence. Home stays first in chip mode. Pages shown by default can be reordered, but only optional plugin pages can be dragged out to unpin them.

> Standalone RPC and MCP integrations must start screen actions from a Control UI connection or a turn begun there; the previous broadcast behavior is no longer supported. If the original browser has disconnected or no browser was captured, the action returns UNAVAILABLE . Ask again from the open Control UI.

> Unavailable configured plugin paths now produce actionable warnings while preserving their settings. Fix the reported path or permissions, then run openclaw doctor --fix ; the plugin remains unavailable until repaired, and structural errors can still block the update. Pending plugin migrations retain their original inputs, so conflicting edits are refused until repair finishes. Complete pending migrations before returning to an older build when you need to preserve later ACP session changes.

> A separate early check stops the update before staging when every eligible location has a measured shortage of space for its state snapshot. Free space or choose a suitable TMPDIR before retrying. That early inventory excludes plugin copies and registered external databases; unknown measurements remain warnings, and the complete later check still runs. Older installed updaters retain their first-update behavior.

> Backups can complete when unrelated application databases contain broken references between records, while OpenClaw's managed databases and declared plugin databases still receive checked snapshots. Agent and plugin discovery works during concurrent writes, including when workspace files are excluded. If discovery fails, resolve the error before creating a state backup. --only-config saves just the active JSON configuration file, excluding included files, state, and external credentials.

> Slack keeps one progress card per command, shows interactive choices once, and preserves the complete written answer when controls cannot be used. A duplicate event waiting in one thread no longer holds up unrelated threads, and compatible corrections can reach a queued turn once it starts running.

> You can change supported access and reply settings for new work without reconnecting Slack. Replies already underway keep their original settings. Account, connection, and other settings that require a restart still reconnect Slack.

> Incoming messages remain queued for retry through temporary Slack authorization outages, while invalid credentials stay rejected. Socket Mode also handles the affected rate-limit and incomplete notifications without crashing the Gateway.

> iMessage setup now offers to correct a command path that points to a folder or a file that cannot run. Custom Windows command extensions must be allowed by PATHEXT ; passing the availability check still does not guarantee the command will launch.

> Authorized operators can use Allow Once or Deny on OpenClaw change-approval cards in Discord and Slack, and late button responses no longer overwrite the final result. Slack can also finish the original pending card after a restart. Configured approval forwarding also sends a text prompt when the destination's native approval handler is inactive. A local prompt or a recovering handler can show the same request again; a handler stopping after the request arrives does not trigger rerouting.

> iMessage, WhatsApp, Signal, and Matrix now wait for approval controls to finish registering or clearing before reporting that operation complete. Plugin authors must await the updated registration and deletion methods and use a supporting host. If optional storage fails, the fallback lasts only until the process stops; see the approval SDK guidance .

> Verified official channel plugins installed through supported external installation paths regain replies from delegated work that finishes after the original turn ends, including the affected Discord setup. LINE and the shared SMS and Zalo webhook paths also keep replies and queued follow-ups alive after the initial incoming request finishes. Existing cancellation and access checks still apply; this does not extend the official-plugin repair to arbitrary third-party plugins.

> In Slack's compact progress mode, the last complete update stays visible until the next complete one arrives, instead of being replaced by a word fragment.

> Messages now use the room or conversation selected through the active channel plugin, without a saved account default adding a conflicting destination and blocking the send.

> Official Mattermost, Teams, and Feishu installations also restore their supported, permitted context reads. Mattermost history reads remain disabled until enabled, and Teams member lookup still excludes private and shared channels. Authenticated dashboard conversations can use supported official-plugin reads under their existing permissions. Channel-origin replies through CLI backends also regain permitted Discord actions and Discord/Slack reads; this does not grant the same authority to scheduled work.

> Update core and the official plugin together. OpenClaw 2026.9.4 lacks the required plugin API, so updating the plugin alone is not sufficient. See the channel-plugin guidance for the supported read actions.

> These libraries are unpublished and their APIs are unstable. Product integration and deployment remain the developer's responsibility, and system.run is not included. The bridge authenticates messages without encrypting them, and cancellation of native work depends on handlers cooperating.

> On an eligible Mac running OpenClaw, Apple Foundation Models can help with setup and short utility tasks without an API key. This optional route requires Apple silicon, macOS 27 or later, enabled and downloaded Apple Intelligence, Apple developer tools with the macOS 27 SDK, and a model with at least 8,192 context tokens. Those requirements apply to the Gateway host; connecting a Mac app to a Linux or Windows Gateway does not supply the model.

> Connecting a provider keeps your chosen model. Replacement sign-ins saved through Model Setup stay inactive until you successfully test and explicitly activate them. If activation fails, setup can restore your working connection without overwriting newer connection edits. If setup requests a plugin update or Gateway restart, complete it and retry activation. Before downgrading OpenClaw, remove inactive replacement sign-ins or restore the state from before setup, because older versions may use them.

> Long foreground commands can use their accepted execution time without prematurely aborting the whole agent turn. Codex commands on paired nodes also honor their resolved command budget; upgrade OpenClaw core and the Codex plugin together for that repair. Setting a command timeout to zero disables only its process timer, while transport deadlines, Stop and approval limits still apply. CLI-backed turns also preserve remaining timeout budgets across detected long process freezes.

> Hooks that run during daily or idle session resets can now finish delayed work after the triggering request ends. This lets a hook wait for another operation and continue its work without losing its place when that request finishes.

> Click a field in a managed Agent browser panel or Browser dashboard and paste plain text with Cmd+V , Ctrl+V , or right-click Paste . Password fields, multiline text, and fields inside embedded pages are supported. Paste waits for the remote click to succeed and does not submit the form or change the remote clipboard. File and image paste and Chrome MCP existing-session profiles remain unsupported. See Browser panel controls .

> Install or reload supported plugins while your Gateway keeps running, and give teammates read-only access to selected conversations.

> The CLI also accepts several plugins in one enable, disable, reload, update or uninstall command. Earlier successful changes remain if later work fails, so review the result before retrying. Local files and marketplace registrations must be available on the Gateway computer, and offline installs wait for startup. If installation saves but activation fails, follow the repair message and run openclaw plugins reload .

> After a replacement timeout, recovery can wait up to 60 seconds for unfinished work, restore the previous plugin and restart eligible channels. Cleanup failures can still require another reload or a Gateway restart. Restart into the updated code to receive this repair. Rebuilt bundled code and enabling experimental native plugin UI retain their separate restart requirements; native UI also needs a browser reload.

> Changing Lossless settings no longer lets cleanup from the old plugin close the replacement's database. Eligible failed replacements can recover using the previous code and settings, while unchanged plugins keep running. Successful cleanup is required before replacement, so slow cleanup delays recovery and a cleanup failure can leave the affected plugin unavailable. A plugin replacing itself from an active call must wait for that call to finish.

> Bun-hosted Gateways can reload supported installed-plugin source through the existing source checks, and receive targeted fixes for TypeScript, JSX and deferred imports. Node also handles directly imported source SDK code through the appropriate loader. Compatibility still depends on the runtime and plugin's imports. Some Bun cases require a patched runtime, while conditional package exports and indirect source-SDK imports retain known gaps.

> Plugin details load through one ClawHub request. Operators of a self-hosted registry must add support for /api/v1/packages/{name}/detail before upgrading this client.

> With telemetry enabled, deliberate plugin searches send normalized query text and remote result counts to ClawHub analytics, which retains queries for 30 days. Local inventory matches and user, device and session identifiers are excluded. Set CLAWHUB_DISABLE_TELEMETRY to opt out while keeping search results available.

> Plugin Settings can organize options into searchable sections, with per-field reset controls and permissions on the same page. Plugins without section definitions keep their complete flat form. Text and number edits commit when you leave the field, while switches commit immediately. Escape also commits the focused edit before leaving Settings.

> Administrators can inspect supported credential fields to see whether a plugin uses an entered key, an environment fallback or a secret reference, and edit declared references directly in Settings. Existing keys stay masked, and only a newly entered replacement can be revealed. Environment fallbacks remain inspect-only, and read-only configuration cannot be edited.

> Use Ask OpenClaw on a plugin or individual setting to prepare a contextual question without losing your existing conversation or draft. The question stays unsent until you choose Send. Generated value previews withhold recognized sensitive values, and help waits while a sensitive setup answer is in progress. This protection applies to the generated preview, so check any private information you type yourself.

> Plugin authors get clearer build and verification errors when a package is missing its manifest or a declared JavaScript entry. Builds preserve existing manifest and package-folder permissions. Plugins stored beneath a symlinked parent directory also regain correct manifest hashes; after updating, use openclaw plugins registry --refresh to repair affected registry metadata.

> Registration-time api.config and its descendants are now read-only. Plugins that mutate them can throw or have writes ignored, so authors need to update those integrations. See the related maintenance change .

> Earlier successful steps can remain after a later failure, so follow the reported recovery instructions before retrying. An interrupted installation can also refuse to resume if model or companion-agent availability changes. Offline installation still needs a restart. Removing a Claw leaves global plugins installed by default; explicitly selected plugin removal waits for active work to finish.

> Opening a Workboard and claiming a task now involve less unrelated card data, so damaged records elsewhere no longer block those actions. Other application work can continue while Workboard waits on its database, and plugin reload lets already-accepted storage work finish. Damaged records still need attention when read directly, and archived cards still prevent a board from being deleted.

> Other work can continue while Team Reports waits on its database to save a report. Large roster refreshes use fewer writes, and a failed refresh preserves the complete previous report and roster. Standalone plugin installations need a compatible host with the SQLite worker SDK.

> Read-only Doctor checks preserve working MCP OAuth logins by leaving schema inspection to authenticated operations that can save refreshed credentials. Use --severity-min info to see deferred checks and openclaw mcp probe \<name> for a configured server. Plugin-provided servers and agent-local profiles need an authenticated serving-agent turn. Already-invalid logins still need reauthorization.

> Claude CLI tools remain usable after the turn that started their listener finishes. Silent configured MCP calls receive the existing 15-minute active-tool allowance, with cancellation and transport deadlines still in force. Servers denied as a whole no longer start, and unused discovery connections can close while retained tools remain available. If cleanup remains unconfirmed, inspect or stop the affected processes before rerunning Doctor.

> Plugin authors can use awaited storage, task and flow operations so their database work can run while other application work continues. Loading saved tasks and workflows at startup, during reloads and before awaited SDK reads now uses the background worker too. Webhooks and Lobster wait for managed-flow saves before returning results or starting dependent work. Data-only keyed-store operations now use the shared database worker; callback-based updates, validation and serialization still run on the calling thread. The storage migration guide explains how to switch interfaces without copying data.

> When a custom context-engine hook fails, the conversation's message order and tool-result history are restored for retry. Pending work keeps the resources it needs, and delayed subagent cleanup stops incorrectly disabling a healthy engine just because its original caller has finished. The history repair restores the message list, not arbitrary changes a plugin made inside individual messages.

> Intentionally disabling a recognized selected engine uses the built-in engine and keeps your choice for re-enabling. A cold start can still report a missing engine when its plugin has a different ID and no ownership registration is available. Genuine plugin failures retain their existing isolation behavior, and earlier quarantine is not automatically cleared.

> Deferred plugin webhook callbacks can finish after the request that started them ends, while remaining tracked during Gateway shutdown. This repairs the closed-request failure that could interrupt background processing. Plugin authors using the deferred-work helper should account for callbacks having their own lifetime and continuing after the requester cancels.

> With Code Mode enabled, an agent can find native and MCP tools together by describing the task it needs to perform. Optional TypeScript checks help combine calls and report several errors at once, while existing permissions and approvals still apply. Exact tool names now distinguish capitalization, and an active wait keeps its tool-call deadline instead of expiring as an idle snapshot.

> Integrations can request only the files an assistant delivered for a chosen run, leaving out user uploads and raw tool observations. Set messageRole to assistant together with runId ; the run ID alone does not select outputs. Scoped managed downloads return the exact selected file or report it missing when its ID is stale.

> Older Gateways reject the new filter. Integrations must show that limitation instead of silently retrying without it.

> Limited tool profiles now also restrict Codex native shell and file access , and isolated workers retain the command restrictions set by the Gateway. Keep restricted Codex sessions on a compatible managed runtime. Worker commands that need unsupported remote approvals must run locally under the configured approval policy; incompatible retained workers need recovery or reprovisioning. Workspace plugins need explicit trust before replacing configured channels.

> The discovery opt-out that OpenClaw saves for native conversations no longer produces a misleading disabled-plugin warning or, by itself, enables Codex and expands the plugin allow-list. Doctor offers manual guidance for matching historical entries, since it cannot tell whether you intended to enable the plugin. Those entries are preserved. Other activation rules still apply, including Doctor's default-model repair when no model is configured.

> Rotating webhook credentials, changing hook policy, or disabling hooks now stops outdated pending requests before they dispatch more work. A request rejected because settings changed receives 409 and can be retried with the current route and credentials. Already accepted work remains accepted, and successful replay keeps its original result without launching duplicate work.

> Client developers can now add selected-account checks so their apps detect when the chosen account no longer matches the signed-in profile. Already accepted work keeps its original conversation and receipt through ordinary disconnects or later account selection changes. These checks are opt-in; other requests keep their existing behavior.

> Newly accepted native Codex child results can also support restart recovery of a still-owed parent channel reply without rerunning the child. This requires a recorded accepted completion and a supported outbound channel route. Control UI, route-less, remote-worker, and never-admitted completions are outside this recovery path. Update the Gateway and Codex plugin together, and finish pending recovery before downgrading.

> Some operations still require Node. The worker, provider, and Discord compatibility fixes were tested with custom Bun builds; stock Bun 1.4.2 lacks a required SQLite fix and still has Slack interoperability limits. They do not establish complete support for that stock runtime.

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
## Nearby in Apps and Integrations

- Earlier: 2026-09-18 · Claude Code · [[Changes/Claude Code/2026-09-18-6-apps-and-integrations-changes-in-v2-1-277|6 Apps and Integrations changes in v2.1.277]]
- Later: 2026-09-21 · ElevenLabs · [[Changes/ElevenLabs/2026-09-21-sdk-releases|SDK releases]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-932e84&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-52-apps-and-integrations-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-932e84%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->