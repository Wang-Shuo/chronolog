---
card_id: openclaw-2026-09-23-a437f4
date: '2026-09-23'
description: 'OpenClaw · 2026-09-23 · Apps and Integrations: 58 changes in v2026.9.6
  — Ask an agent to discover, choose or create a personal theme and save it to your…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1280
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dc6360c544319f8f883560c5f36576a6fe1c4dea8377443b6a52938ff612a916
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-23-a437f4
  comparison: ''
  date: '2026-09-23'
  description: 'OpenClaw — v2026.9.6: 58 Apps and Integrations changes'
  evidence:
  - quote: Ask an agent to discover, choose or create a personal theme and save it
      to your authenticated profile for use across signed-in browsers. Appearance
      uses the same catalog, including enabled plugin themes, and connected browsers
      update as choices change. This requires an updated UI and Gateway together,
      while older tweakcn imports remain browser-local. If a selected theme becomes
      unavailable, Claw renders temporarily and the selection is retained for its
      return.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Plugin themes can also package bounded, self-contained SVG hats and composer
      visitors, while personal themes use the built-in decoration choices. The existing
      Lobster visits preference still controls visitors.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Personal and plugin themes can opt into neutral branding, their own waiting
      phrases and supported avatar hats or visitors. Omitted options retain the usual
      appearance, and these additions do not change built-in themes by default.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Use current view as default now saves both the opening view and split or
      fullscreen presentation, while personal layouts retain priority and existing
      viewers are not rearranged. Identical previously approved widgets can also avoid
      another model review for the same agent, name, content and declarations, subject
      to current permissions. This temporary reuse excludes new or changed widgets,
      MCP apps and Incognito sessions; see dashboards .
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Activity shows compact, uncropped HTTPS image previews that can expand
      without taking over the list, and plugin README and agent-file previews can
      load HTTPS images automatically. Those images are fetched directly by your browser,
      so their hosts receive its network address. HTTP images remain blocked, and
      Markdown attachments and Workshop previews retain click-to-open behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Packaged headless nodes on stable or beta releases now update automatically
      when their work and cleanup are idle, keeping their pairing, settings and launch
      options. They check hourly after connecting, leave at least 12 hours between
      activations, and fall back to the previous runtime if the replacement cannot
      start. Busy work and plugins without explicit idle reporting can defer activation
      indefinitely.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Large-fleet updates reuse configuration and plugin inspections and prioritize
      repairs needed to start the replacement. Optional checks that are deferred have
      not passed yet, so run openclaw doctor --fix after activation to finish them.
      Older installed updaters keep their existing time limits until they have been
      replaced.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Doctor's final results now retain the original reason for a refused migration,
      identify plugins that failed to load, and give useful disk-space guidance. Completed
      checks survive cleanup-only delays instead of becoming false update failures,
      while unfinished checks still report a timeout. Standalone noninteractive Doctor
      exits with an error for plugin-load failures; updater-invoked Doctor can retain
      those findings as warnings when the update can otherwise proceed. See how updates
      run for the remaining older-updater limits.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: After a manual core upgrade, openclaw doctor --fix can bring eligible official
      npm plugins back into line while respecting newer pins and nondefault tags.
      Repair guidance now distinguishes an attainable release from registry lag, reports
      unreadable required manifests, and avoids sending you around a circular migration
      fix. Third-party plugins stay with their own maintainers, unavailable packages
      remain warnings, and missing required manifests can still make post-upgrade
      checks fail.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Doctor can reconnect existing settings after an interrupted installation
      of a trusted, declared replacement plugin ID, while existing canonical settings
      and explicit disables take precedence. Candidate inspection also accepts valid
      import.meta syntax and names remaining per-plugin parse warnings without treating
      a malformed plugin as healthy.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Updates preserve local plugin overrides and the npm copies they shadow,
      with guidance about which copy is active. Check that your override supports
      the new release, or deliberately remove it to return to the managed copy. Preserving
      a local plugin does not grant it trust, and channels blocked by trust policy
      stop retrying until that policy is resolved. The plugin sync guidance explains
      the update behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Plugin and hook updates can finish longer work when no work deadline was
      supplied, while explicitly short deadlines are honored. The same distinction
      carries through supported Doctor, plugin-convergence and finalization paths,
      without removing separate metadata, readiness, cleanup or enclosing updater
      limits. Git plugin clone and checkout still have a cancellation gap when running
      without a deadline, so this is not a promise that every stalled update can be
      canceled immediately.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: OpenClaw reclaims eligible abandoned managed plugin copies after an ownership
      check and a one-hour grace period, while session cleanup avoids repeatedly scanning
      data it cannot reclaim. Active and protected history remains protected, and
      openclaw sessions cleanup --enforce still requests immediate cleanup. Committed
      session resets finish their remaining actions even if later cleanup fails, with
      the original error kept visible.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Managed updates can finish with recoverable plugin warnings and keep a
      verified new Gateway running while remaining maintenance waits. Results distinguish
      a healthy requested version from a restored previous version and show which
      repairs are still pending. Retaining the updater also takes less copying on
      filesystems with hard-link support, although some mixed link/copy layouts can
      still block that step.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Reply completion tracking also survives failing plugin observers, and delayed
      cleanup preserves newer Discord and Slack previews and Slack messages people
      have replied to. A cleanup failure does not resend an accepted answer. Message
      dry runs now report a simulation rather than delivery, without automatically
      sending a real message.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Removing or disabling a Discord account, or removing a Matrix, Telegram,
      or Slack account, no longer blocks conversation discovery for the remaining
      active accounts. Retained history stays intact, while access to retired-account
      conversations is still restricted. An account that is configured but not yet
      ready can remain temporarily unavailable.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Matrix also restores single-message assistant and tool progress drafts
      in affected sessions by using the account's saved settings. Final replies are
      unchanged, and multi-message chunking still requires the plugin runtime.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: When several iMessage questions arrive while an answer is being written,
      queued text and media replies can stay attached to the question that prompted
      each one. Explicit targets and the first , all , and off reply settings still
      apply. This requires both the updated iMessage plugin and a host that supports
      its inferred reply targets; updating the plugin alone is insufficient. The startup
      database read that establishes the latest seen message also moves off the Gateway's
      main thread.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Long tasks with repeated tool calls can recover from later context overflows
      after the model makes successful progress, instead of exhausting one recovery
      allowance for the entire task. Repeated attempts without progress remain bounded,
      and refusals, errors, aborted replies, or replies cut short by a length limit
      do not renew that allowance. Conversation compaction also keeps working after
      a plugin reload by using the current plugins.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Skill Workshop now lists current skill files and records successful tool-mediated
      use even when diagnostics are disabled. A rejected proposal remains a failed
      review when the reviewer sends no reply, and reviews delayed until idle time
      use the current plugins. Usage counts start with recorded activity rather than
      filling in older history, exclude native Codex skill activation, and do not
      follow files when they move.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Plugin Skill previews now show the main instructions before fetching supporting
      documents, so you can begin reading without waiting for every file. Supporting
      files load when you select them, failed reads offer Retry, and background loading
      preserves your selected document and reading position. Previewing does not install
      or execute the plugin, and reopening the preview lets you see installed files
      that were edited while it was open.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Mac settings distinguish an installed Chrome extension from one that needs
      enabling, and provide separate guidance when its helper needs repair. Older
      Mac apps keep a usable setup path with a newer Dashboard, including an unknown
      status when the older app cannot establish whether the extension is installed.
      Installation status remains separate from a live browser connection.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Mac packaging trims files the app's private worker does not need, reducing
      the universal app's size while retaining Apple silicon and Intel support. The
      packaging correction also keeps nested helpers needed by bundled subprocess
      support, including configured stdio MCP servers. Normal npm installations keep
      their CLI and Gateway functionality.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The separate @openclaw/typesafe plugin is available on npm for OpenClaw
      and plugin API 2026.9.6 or newer. Install and enable it, add a protected API-key
      reference, then select Jev or Jev 1.13.0. Hosted evaluations send the supplied
      information to TypeSafe and incur its normal API charges. Requests can allow
      up to thirty seconds, with shorter caller deadlines and saved timeout settings
      respected. If replacing an external prototype, preserve its settings, credentials,
      and policy before uninstalling; uninstall --keep-files does not keep the configuration.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The optional ONNX plugin makes structured choices locally on the CPU without
      sending the supplied information to a hosted inference service. Its @openclaw/onnx
      package is available on npm for OpenClaw and plugin API 2026.9.6 or newer. Install
      and enable it, prepare one of seven model presets, and select it as a Decision
      Model. Five presets have pinned downloads and two require local exports; none
      is enabled automatically.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The TypeSafe plugin also connects the Decision Model role to a local Kev
      server you run yourself. Install and enable @openclaw/typesafe from npm on OpenClaw
      and plugin API 2026.9.6 or newer, then configure the server's loopback address
      and select Kev. The server controls the loaded model weights, and its address
      applies to every request through the plugin. Local mode needs no hosted key
      and does not fall back to hosted Jev.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Expanded llmman guidance explains existing local and hybrid setup, model
      names, credentials, and troubleshooting. It documents the existing integration
      rather than adding a new provider or routing feature.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Scheduled Codex app calls retain the connected-account approval requirements
      captured when the schedule was created, alongside current policy. Plugin installation
      refreshes shared information without treating another conversation's readiness
      as proof that an app is usable in this one, and prompts dismiss when another
      connected client actually answers them. Missing configured plugins no longer
      restrict otherwise eligible connected apps, while a present plugin disabled
      by an administrator retains its restrictions. Older custom runtimes may need
      /new or /reset after installation.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Eligible local, agent-scoped Codex background titles and narratives can
      run with administrator hooks in a verified isolated environment. Model-callable
      tools, apps, and MCP remain unavailable there, and unsupported launchers may
      need a directly executable wrapper. Optional finalization can also choose silence
      without generating a missing-summary fallback, while required replies and failure
      reporting remain intact.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Automatic approval remains limited to one execution, with persistent trust
      requiring an explicit choice and empty approval forms requiring Allow or Decline.
      Recovery retains evidence of prior tool effects, but uncertain partial media
      delivery can still require checking what arrived. Updated Codex and Copilot
      plugins need a matching core SDK for the delegated-result repair.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: OpenClaw can keep apps beside your conversation, show more kinds of cloud
      desktops, and make the browser work easier to inspect as it happens.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Remote Portals now use their published HTTPS addresses. Managed Tailscale
      Portals stay private to your tailnet even when the Gateway uses Funnel, and
      their separate ports need to be allowed. An optional wildcard proxy needs your
      own DNS, TLS, access controls, and a Gateway restart. Forwarding the Gateway
      alone does not expose the apps. Upgrade OpenClaw and its bundled providers together,
      and stop attachments before downgrading.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Access to the computer running the Gateway remains a separate opt-in. An
      administrator can enable Host Desktop from Systems , with setup guidance for
      missing services and macOS permissions. Labs changes, including Systems enablement,
      apply without restarting the Gateway when automatic configuration reload is
      enabled. Turning access off closes viewers but leaves system screen-sharing
      services and cloud workers running. Code Mode and Tool Search changes apply
      to future runs, and disabling Custom plugin UI requires a browser-tab reload
      to clear code that already ran.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Ordinary Codex Computer Use turns using the default non-strict readiness
      setting no longer wait for optional live desktop probes before starting. Installation,
      available tools, and permissions still matter, and a later desktop call can
      still fail; strict readiness and explicit status or install commands keep their
      live checks. Computer-control helpers also find a suitable Node runtime when
      a Bun shim shadows it, though Bun users still need Node installed. Browser refusals
      give recovery guidance that matches the actual policy or plugin problem, and
      Linux X11 apps that previously missed brief key taps can detect them.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: New CLI-backend turns keep access to their permitted OpenClaw tools after
      a plugin replacement, without needing a Gateway restart. Long-running MCP calls
      also keep their local connection alive while awaiting a result, and Bun cleanup
      handles a supervisor that outlives its command. Each new turn still needs an
      active grant, and connection keepalives neither extend deadlines nor indicate
      progress.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Codex-owned MCP connections also honor configured startup and tool deadlines
      and explicit parallel-call hints, while native read-only parallelism keeps its
      own rules. Expired legacy SSE connections are replaced for later calls after
      a message request receives a 404; the call that discovers the expiration still
      fails and is not replayed.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Documents and previews use your configured GitHub identity to avoid unnecessary
      anonymous rate-limit failures. Screenshots load anonymously without cookies
      or credentials, supporting PNG, JPEG, GIF, and WebP files up to 2 MiB. If your
      installation uses a restrictive plugin allowlist, add and enable github while
      preserving its other entries to use the reader and previews.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: An agent that explicitly waits for delegated work can resume using supported
      owner-only plugin tools without requiring another message from you. Eligible
      sessions also retain their GitHub tools across supported harness continuations,
      with the same current permissions and publication approvals. Plugin authors
      must opt in to the owner-authorized continuation contract and check that authority
      immediately before an action; unrelated sessions and scheduled jobs gain no
      owner privileges.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Chat plugin cards update to Installed after installation, and agent guidance
      favors tools you already have before suggesting more from ClawHub. Plugin archives
      avoid development-only dependency failures, while incomplete npm installations
      name missing required dependencies and can be repaired by Doctor when eligible.
      Repairs deferred during an update may require another Doctor run afterward.
      Installation fixes also cover stale paths after moving OpenClaw, equivalent
      Windows directory names, and native dependency asset paths.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Administrators can install directly from a plugin’s overview and follow
      stage progress and elapsed time through completion. Installation accepts the
      plugin’s declared capabilities without granting hook or model permissions, and
      policy warnings still require acknowledgment. Ready new plugins enable automatically,
      while missing required configuration or an existing disabled choice keeps them
      disabled. Disabled installed plugins put Enable first. The final response determines
      success, and uncertain outcomes retain protection against duplicate installation.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Plugin loading follows the current selected copy, profile, and configuration,
      including valid structured secret references. A failed setup keeps its original
      error without repeatedly initializing the same plugin, and repeated failures
      no longer bury distinct diagnostics in duplicates or remove healthy sibling
      tools. Packaged installations also skip unnecessary source parsing during plugin
      startup.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Dependency warnings now recognize plugin IDs despite capitalization differences,
      valid stored-secret references avoid false setup errors, and malformed external
      schemas no longer prevent healthy plugins from loading. Invalid settings and
      malformed bundled schemas still fail.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Unchanged sibling plugins keep running when another workspace’s plugin
      changes, object keys reorder, or duplicate notifications report the same configuration.
      Changes to actual values, list order, sources, or policy still trigger the required
      refresh.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: A busy plugin reload can now refuse before stopping the serving runtime,
      keeping chat available while an active turn or its cleanup still needs that
      plugin. Active search and fetch calls retain their selected plugin files until
      the work actually finishes. Finish the work and retry a refused replacement;
      it is not queued automatically.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Reloads already waiting for active calls can restore the previous runtime
      when its recovery files remain intact and the replacement cannot finish, including
      recovery after delayed cleanup succeeds within the existing 60-second window.
      A retirement timeout does not mean plugin files have been deleted, and cleanup
      that never finishes can still need operator attention.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Replacement can also proceed when the old temporary source files have disappeared,
      with a warning that the previous code cannot be restored. If that replacement
      fails, the affected plugin remains visibly failed until a replacement succeeds.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Requests crossing reloaded plugin code also retain their context and selected
      plugins, so provider hooks and failure handling use the intended request settings.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Growing plugin caches no longer consume a shared row quota that can block
      replies, execution records, or background jobs. Individual namespace, expiry,
      value, and blob limits still apply, but total storage can grow. Keep a verified
      pre-update backup if you may downgrade, because older versions restore the aggregate
      quota. Do not delete durable ownership records to make the data fit that older
      limit.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Managed model-catalog temporary files can now be reclaimed after a crash
      while live workers retain the files they need. Model discovery reuses an already
      loaded plugin’s files instead of creating duplicate copies, and ordinary CLI
      runs release their own scratch copies when they finish.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Plugin authors also gain awaited conversation-binding inspection and activity
      APIs while existing synchronous APIs remain through their deprecation window.
      CLI and loopback MCP completion hooks again receive isolated outcomes and approved
      arguments without duplicate notification; these observers are best effort and
      do not block the tool, and results that cannot be isolated are skipped with
      a warning.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Stopping or restarting ClickClack waits for accepted room creation and
      persistence to finish, helping those operations complete before the integration
      closes.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Help and read-only commands for hooks, nodes, sandboxes, and worktrees
      load less unused code. JSON agent and session listings also avoid repeated lookups
      or terminal-only display preparation while preserving their output.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Compact tool previews omit extreme array nesting instead of overflowing
      the formatter, without changing the original arguments used to run the tool.
      Plugin authors using the display metadata helper should expect values beyond
      64 array levels to be omitted and a possible undefined result. Suggestions after
      an unknown-tool request also avoid repeated lookup preparation.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Commands give more useful feedback for invalid agent selections and empty
      node invocation keys, and plugin and skill listings preserve version labels
      without adding duplicate prefixes. If a request times out or loses its connection
      after being sent, the message now advises checking its current state before
      retrying, because the operation may already have completed.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Messaging integrations share configuration types, formatting and account-preparation
      helpers. This maintenance retains existing routing, account ownership and attachment
      choices.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Plugin tests cover asset lookup across installation layouts, cleanup after
      failed preparation and package lifecycle behavior. Their fixtures isolate database
      state and temporary dependencies while retaining existing assertions.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Plugin loading and catalogs avoid repeated path resolution, unused metadata
      reads and temporary allocations. Existing tool behavior, migration history and
      execution ownership are preserved.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: QA Lab keeps Evidence Archive filters within their toolbar and rejects
      replay reports with missing runtime results. Channel test tools also improve
      credential-fixture cleanup and retain clearer bounded failure diagnostics. Existing
      scenarios are selectable, and QA Lab controls and links receive layout and refresh
      fixes. Slack and Discord readiness tools require provisioned credential pools;
      Slack message checks make explicitly requested test writes, while Discord's
      read-only checks do not establish write permissions. API receipts, Gateway replies
      and actual client rendering remain separate checks.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 58-apps-and-integrations-changes-in-v2026-9-6
  source_release: openclaw-2026-09-23-v2026-9-6-3f12c824
  source_type: openclaw_changelog
  theme: apps-integrations
  title: 58 Apps and Integrations changes in v2026.9.6
  type: change
related_changes:
- '[[Changes/Cursor/2026-09-23-integrations|Integrations]]'
- '[[Changes/Lovable/2026-09-23-app-chat-connectors-aws-api-azure-cloud-api-azure-graph-entra-api-google-cloud-a|App
  + chat connectors]]'
- '[[Changes/Lovable/2026-09-23-typo-tolerant-connector-search|Typo-tolerant connector
  search]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|openclaw-2026-09-23-v2026-9-6-3f12c824]]'
source_type: openclaw_changelog
theme: apps-integrations
title: 58 Apps and Integrations changes in v2026.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 58 Apps and Integrations changes in v2026.9.6

**OpenClaw** · 2026-09-23 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.6) · from [[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|v2026.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Ask an agent to discover, choose or create a personal theme and save it to your authenticated profile for use across signed-in browsers. Appearance uses the same catalog, including enabled plugin themes, and connected browsers update as choices change. This requires an updated UI and Gateway together, while older tweakcn imports remain browser-local. If a selected theme becomes unavailable, Claw renders temporarily and the selection is retained for its return.

> Plugin themes can also package bounded, self-contained SVG hats and composer visitors, while personal themes use the built-in decoration choices. The existing Lobster visits preference still controls visitors.

> Personal and plugin themes can opt into neutral branding, their own waiting phrases and supported avatar hats or visitors. Omitted options retain the usual appearance, and these additions do not change built-in themes by default.

> Use current view as default now saves both the opening view and split or fullscreen presentation, while personal layouts retain priority and existing viewers are not rearranged. Identical previously approved widgets can also avoid another model review for the same agent, name, content and declarations, subject to current permissions. This temporary reuse excludes new or changed widgets, MCP apps and Incognito sessions; see dashboards .

> Activity shows compact, uncropped HTTPS image previews that can expand without taking over the list, and plugin README and agent-file previews can load HTTPS images automatically. Those images are fetched directly by your browser, so their hosts receive its network address. HTTP images remain blocked, and Markdown attachments and Workshop previews retain click-to-open behavior.

> Packaged headless nodes on stable or beta releases now update automatically when their work and cleanup are idle, keeping their pairing, settings and launch options. They check hourly after connecting, leave at least 12 hours between activations, and fall back to the previous runtime if the replacement cannot start. Busy work and plugins without explicit idle reporting can defer activation indefinitely.

> Large-fleet updates reuse configuration and plugin inspections and prioritize repairs needed to start the replacement. Optional checks that are deferred have not passed yet, so run openclaw doctor --fix after activation to finish them. Older installed updaters keep their existing time limits until they have been replaced.

> Doctor's final results now retain the original reason for a refused migration, identify plugins that failed to load, and give useful disk-space guidance. Completed checks survive cleanup-only delays instead of becoming false update failures, while unfinished checks still report a timeout. Standalone noninteractive Doctor exits with an error for plugin-load failures; updater-invoked Doctor can retain those findings as warnings when the update can otherwise proceed. See how updates run for the remaining older-updater limits.

> After a manual core upgrade, openclaw doctor --fix can bring eligible official npm plugins back into line while respecting newer pins and nondefault tags. Repair guidance now distinguishes an attainable release from registry lag, reports unreadable required manifests, and avoids sending you around a circular migration fix. Third-party plugins stay with their own maintainers, unavailable packages remain warnings, and missing required manifests can still make post-upgrade checks fail.

> Doctor can reconnect existing settings after an interrupted installation of a trusted, declared replacement plugin ID, while existing canonical settings and explicit disables take precedence. Candidate inspection also accepts valid import.meta syntax and names remaining per-plugin parse warnings without treating a malformed plugin as healthy.

> Updates preserve local plugin overrides and the npm copies they shadow, with guidance about which copy is active. Check that your override supports the new release, or deliberately remove it to return to the managed copy. Preserving a local plugin does not grant it trust, and channels blocked by trust policy stop retrying until that policy is resolved. The plugin sync guidance explains the update behavior.

> Plugin and hook updates can finish longer work when no work deadline was supplied, while explicitly short deadlines are honored. The same distinction carries through supported Doctor, plugin-convergence and finalization paths, without removing separate metadata, readiness, cleanup or enclosing updater limits. Git plugin clone and checkout still have a cancellation gap when running without a deadline, so this is not a promise that every stalled update can be canceled immediately.

> OpenClaw reclaims eligible abandoned managed plugin copies after an ownership check and a one-hour grace period, while session cleanup avoids repeatedly scanning data it cannot reclaim. Active and protected history remains protected, and openclaw sessions cleanup --enforce still requests immediate cleanup. Committed session resets finish their remaining actions even if later cleanup fails, with the original error kept visible.

> Managed updates can finish with recoverable plugin warnings and keep a verified new Gateway running while remaining maintenance waits. Results distinguish a healthy requested version from a restored previous version and show which repairs are still pending. Retaining the updater also takes less copying on filesystems with hard-link support, although some mixed link/copy layouts can still block that step.

> Reply completion tracking also survives failing plugin observers, and delayed cleanup preserves newer Discord and Slack previews and Slack messages people have replied to. A cleanup failure does not resend an accepted answer. Message dry runs now report a simulation rather than delivery, without automatically sending a real message.

> Removing or disabling a Discord account, or removing a Matrix, Telegram, or Slack account, no longer blocks conversation discovery for the remaining active accounts. Retained history stays intact, while access to retired-account conversations is still restricted. An account that is configured but not yet ready can remain temporarily unavailable.

> Matrix also restores single-message assistant and tool progress drafts in affected sessions by using the account's saved settings. Final replies are unchanged, and multi-message chunking still requires the plugin runtime.

> When several iMessage questions arrive while an answer is being written, queued text and media replies can stay attached to the question that prompted each one. Explicit targets and the first , all , and off reply settings still apply. This requires both the updated iMessage plugin and a host that supports its inferred reply targets; updating the plugin alone is insufficient. The startup database read that establishes the latest seen message also moves off the Gateway's main thread.

> Long tasks with repeated tool calls can recover from later context overflows after the model makes successful progress, instead of exhausting one recovery allowance for the entire task. Repeated attempts without progress remain bounded, and refusals, errors, aborted replies, or replies cut short by a length limit do not renew that allowance. Conversation compaction also keeps working after a plugin reload by using the current plugins.

> Skill Workshop now lists current skill files and records successful tool-mediated use even when diagnostics are disabled. A rejected proposal remains a failed review when the reviewer sends no reply, and reviews delayed until idle time use the current plugins. Usage counts start with recorded activity rather than filling in older history, exclude native Codex skill activation, and do not follow files when they move.

> Plugin Skill previews now show the main instructions before fetching supporting documents, so you can begin reading without waiting for every file. Supporting files load when you select them, failed reads offer Retry, and background loading preserves your selected document and reading position. Previewing does not install or execute the plugin, and reopening the preview lets you see installed files that were edited while it was open.

> Mac settings distinguish an installed Chrome extension from one that needs enabling, and provide separate guidance when its helper needs repair. Older Mac apps keep a usable setup path with a newer Dashboard, including an unknown status when the older app cannot establish whether the extension is installed. Installation status remains separate from a live browser connection.

> Mac packaging trims files the app's private worker does not need, reducing the universal app's size while retaining Apple silicon and Intel support. The packaging correction also keeps nested helpers needed by bundled subprocess support, including configured stdio MCP servers. Normal npm installations keep their CLI and Gateway functionality.

> The separate @openclaw/typesafe plugin is available on npm for OpenClaw and plugin API 2026.9.6 or newer. Install and enable it, add a protected API-key reference, then select Jev or Jev 1.13.0. Hosted evaluations send the supplied information to TypeSafe and incur its normal API charges. Requests can allow up to thirty seconds, with shorter caller deadlines and saved timeout settings respected. If replacing an external prototype, preserve its settings, credentials, and policy before uninstalling; uninstall --keep-files does not keep the configuration.

> The optional ONNX plugin makes structured choices locally on the CPU without sending the supplied information to a hosted inference service. Its @openclaw/onnx package is available on npm for OpenClaw and plugin API 2026.9.6 or newer. Install and enable it, prepare one of seven model presets, and select it as a Decision Model. Five presets have pinned downloads and two require local exports; none is enabled automatically.

> The TypeSafe plugin also connects the Decision Model role to a local Kev server you run yourself. Install and enable @openclaw/typesafe from npm on OpenClaw and plugin API 2026.9.6 or newer, then configure the server's loopback address and select Kev. The server controls the loaded model weights, and its address applies to every request through the plugin. Local mode needs no hosted key and does not fall back to hosted Jev.

> Expanded llmman guidance explains existing local and hybrid setup, model names, credentials, and troubleshooting. It documents the existing integration rather than adding a new provider or routing feature.

> Scheduled Codex app calls retain the connected-account approval requirements captured when the schedule was created, alongside current policy. Plugin installation refreshes shared information without treating another conversation's readiness as proof that an app is usable in this one, and prompts dismiss when another connected client actually answers them. Missing configured plugins no longer restrict otherwise eligible connected apps, while a present plugin disabled by an administrator retains its restrictions. Older custom runtimes may need /new or /reset after installation.

> Eligible local, agent-scoped Codex background titles and narratives can run with administrator hooks in a verified isolated environment. Model-callable tools, apps, and MCP remain unavailable there, and unsupported launchers may need a directly executable wrapper. Optional finalization can also choose silence without generating a missing-summary fallback, while required replies and failure reporting remain intact.

> Automatic approval remains limited to one execution, with persistent trust requiring an explicit choice and empty approval forms requiring Allow or Decline. Recovery retains evidence of prior tool effects, but uncertain partial media delivery can still require checking what arrived. Updated Codex and Copilot plugins need a matching core SDK for the delegated-result repair.

> OpenClaw can keep apps beside your conversation, show more kinds of cloud desktops, and make the browser work easier to inspect as it happens.

> Remote Portals now use their published HTTPS addresses. Managed Tailscale Portals stay private to your tailnet even when the Gateway uses Funnel, and their separate ports need to be allowed. An optional wildcard proxy needs your own DNS, TLS, access controls, and a Gateway restart. Forwarding the Gateway alone does not expose the apps. Upgrade OpenClaw and its bundled providers together, and stop attachments before downgrading.

> Access to the computer running the Gateway remains a separate opt-in. An administrator can enable Host Desktop from Systems , with setup guidance for missing services and macOS permissions. Labs changes, including Systems enablement, apply without restarting the Gateway when automatic configuration reload is enabled. Turning access off closes viewers but leaves system screen-sharing services and cloud workers running. Code Mode and Tool Search changes apply to future runs, and disabling Custom plugin UI requires a browser-tab reload to clear code that already ran.

> Ordinary Codex Computer Use turns using the default non-strict readiness setting no longer wait for optional live desktop probes before starting. Installation, available tools, and permissions still matter, and a later desktop call can still fail; strict readiness and explicit status or install commands keep their live checks. Computer-control helpers also find a suitable Node runtime when a Bun shim shadows it, though Bun users still need Node installed. Browser refusals give recovery guidance that matches the actual policy or plugin problem, and Linux X11 apps that previously missed brief key taps can detect them.

> New CLI-backend turns keep access to their permitted OpenClaw tools after a plugin replacement, without needing a Gateway restart. Long-running MCP calls also keep their local connection alive while awaiting a result, and Bun cleanup handles a supervisor that outlives its command. Each new turn still needs an active grant, and connection keepalives neither extend deadlines nor indicate progress.

> Codex-owned MCP connections also honor configured startup and tool deadlines and explicit parallel-call hints, while native read-only parallelism keeps its own rules. Expired legacy SSE connections are replaced for later calls after a message request receives a 404; the call that discovers the expiration still fails and is not replayed.

> Documents and previews use your configured GitHub identity to avoid unnecessary anonymous rate-limit failures. Screenshots load anonymously without cookies or credentials, supporting PNG, JPEG, GIF, and WebP files up to 2 MiB. If your installation uses a restrictive plugin allowlist, add and enable github while preserving its other entries to use the reader and previews.

> An agent that explicitly waits for delegated work can resume using supported owner-only plugin tools without requiring another message from you. Eligible sessions also retain their GitHub tools across supported harness continuations, with the same current permissions and publication approvals. Plugin authors must opt in to the owner-authorized continuation contract and check that authority immediately before an action; unrelated sessions and scheduled jobs gain no owner privileges.

> Chat plugin cards update to Installed after installation, and agent guidance favors tools you already have before suggesting more from ClawHub. Plugin archives avoid development-only dependency failures, while incomplete npm installations name missing required dependencies and can be repaired by Doctor when eligible. Repairs deferred during an update may require another Doctor run afterward. Installation fixes also cover stale paths after moving OpenClaw, equivalent Windows directory names, and native dependency asset paths.

> Administrators can install directly from a plugin’s overview and follow stage progress and elapsed time through completion. Installation accepts the plugin’s declared capabilities without granting hook or model permissions, and policy warnings still require acknowledgment. Ready new plugins enable automatically, while missing required configuration or an existing disabled choice keeps them disabled. Disabled installed plugins put Enable first. The final response determines success, and uncertain outcomes retain protection against duplicate installation.

> Plugin loading follows the current selected copy, profile, and configuration, including valid structured secret references. A failed setup keeps its original error without repeatedly initializing the same plugin, and repeated failures no longer bury distinct diagnostics in duplicates or remove healthy sibling tools. Packaged installations also skip unnecessary source parsing during plugin startup.

> Dependency warnings now recognize plugin IDs despite capitalization differences, valid stored-secret references avoid false setup errors, and malformed external schemas no longer prevent healthy plugins from loading. Invalid settings and malformed bundled schemas still fail.

> Unchanged sibling plugins keep running when another workspace’s plugin changes, object keys reorder, or duplicate notifications report the same configuration. Changes to actual values, list order, sources, or policy still trigger the required refresh.

> A busy plugin reload can now refuse before stopping the serving runtime, keeping chat available while an active turn or its cleanup still needs that plugin. Active search and fetch calls retain their selected plugin files until the work actually finishes. Finish the work and retry a refused replacement; it is not queued automatically.

> Reloads already waiting for active calls can restore the previous runtime when its recovery files remain intact and the replacement cannot finish, including recovery after delayed cleanup succeeds within the existing 60-second window. A retirement timeout does not mean plugin files have been deleted, and cleanup that never finishes can still need operator attention.

> Replacement can also proceed when the old temporary source files have disappeared, with a warning that the previous code cannot be restored. If that replacement fails, the affected plugin remains visibly failed until a replacement succeeds.

> Requests crossing reloaded plugin code also retain their context and selected plugins, so provider hooks and failure handling use the intended request settings.

> Growing plugin caches no longer consume a shared row quota that can block replies, execution records, or background jobs. Individual namespace, expiry, value, and blob limits still apply, but total storage can grow. Keep a verified pre-update backup if you may downgrade, because older versions restore the aggregate quota. Do not delete durable ownership records to make the data fit that older limit.

> Managed model-catalog temporary files can now be reclaimed after a crash while live workers retain the files they need. Model discovery reuses an already loaded plugin’s files instead of creating duplicate copies, and ordinary CLI runs release their own scratch copies when they finish.

> Plugin authors also gain awaited conversation-binding inspection and activity APIs while existing synchronous APIs remain through their deprecation window. CLI and loopback MCP completion hooks again receive isolated outcomes and approved arguments without duplicate notification; these observers are best effort and do not block the tool, and results that cannot be isolated are skipped with a warning.

> Stopping or restarting ClickClack waits for accepted room creation and persistence to finish, helping those operations complete before the integration closes.

> Help and read-only commands for hooks, nodes, sandboxes, and worktrees load less unused code. JSON agent and session listings also avoid repeated lookups or terminal-only display preparation while preserving their output.

> Compact tool previews omit extreme array nesting instead of overflowing the formatter, without changing the original arguments used to run the tool. Plugin authors using the display metadata helper should expect values beyond 64 array levels to be omitted and a possible undefined result. Suggestions after an unknown-tool request also avoid repeated lookup preparation.

> Commands give more useful feedback for invalid agent selections and empty node invocation keys, and plugin and skill listings preserve version labels without adding duplicate prefixes. If a request times out or loses its connection after being sent, the message now advises checking its current state before retrying, because the operation may already have completed.

> Messaging integrations share configuration types, formatting and account-preparation helpers. This maintenance retains existing routing, account ownership and attachment choices.

> Plugin tests cover asset lookup across installation layouts, cleanup after failed preparation and package lifecycle behavior. Their fixtures isolate database state and temporary dependencies while retaining existing assertions.

> Plugin loading and catalogs avoid repeated path resolution, unused metadata reads and temporary allocations. Existing tool behavior, migration history and execution ownership are preserved.

> QA Lab keeps Evidence Archive filters within their toolbar and rejects replay reports with missing runtime results. Channel test tools also improve credential-fixture cleanup and retain clearer bounded failure diagnostics. Existing scenarios are selectable, and QA Lab controls and links receive layout and refresh fixes. Slack and Discord readiness tools require provisioned credential pools; Slack message checks make explicitly requested test writes, while Discord's read-only checks do not establish write permissions. API receipts, Gateway replies and actual client rendering remain separate checks.

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
## Nearby in Apps and Integrations

- Earlier: 2026-09-23 · Lovable · [[Changes/Lovable/2026-09-23-typo-tolerant-connector-search|Typo-tolerant connector search]]
- Later: 2026-09-23 · Runway · [[Changes/Runway/2026-09-23-runway-mcp-is-now-available-on-cursor-s-marketplace-making-it-easy-to-bring-runw|Runway MCP on Cursor]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-23-a437f4&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-23-58-apps-and-integrations-changes-in-v2026-9-6.md%0ACard%20ID%3A%20openclaw-2026-09-23-a437f4%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->