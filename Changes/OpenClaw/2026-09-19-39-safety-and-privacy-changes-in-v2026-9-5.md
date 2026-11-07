---
card_id: openclaw-2026-09-19-43edb1
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Safety and Privacy: 39 changes in v2026.9.5
  — Fresh OpenAI and ChatGPT/Codex setups start with Astra if you haven''t chosen
  a primary…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2244
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fc7fb2c8fe6463d7b1fe948b75c4e1b6b98adefcc476034f4fb9bc2e9bef295d
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-43edb1
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 39 Safety and Privacy changes'
  evidence:
  - quote: Fresh OpenAI and ChatGPT/Codex setups start with Astra if you haven't chosen
      a primary model. Existing choices stay in place. If your account does not offer
      Astra, choose an available model during OpenAI setup . Verified official plugins
      also skip a redundant approval step before sign-in. Third-party plugins and
      those OpenClaw cannot verify still need the applicable consent .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Local onboarding now selects Full tools when no profile is set, including
      when you rerun onboarding. This includes messaging and available optional tools
      from enabled plugins. Explicit profiles stay in place, and an ordinary upgrade
      leaves an unset profile unchanged. Security settings now save an explicit Full
      choice. Full selects tools; Full Access controls execution permissions, which
      remain separate from tool selection and other access restrictions.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Mac app CLI setup can now recover from temporary-directory permission errors
      without an administrator password, provided /tmp is writable. The Linux companion's
      installer also avoids the bundled OpenSSL conflict that could stop system download
      tools during AppImage setup.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: When OpenClaw runs in Docker, its sandbox shell and browser tools can now
      see the same workspace and skill files even when the host uses different paths.
      Workspace and state folders, including nested managed sources, must use verified
      host bind mounts . Named volumes, tmpfs and files stored only in the image remain
      unsupported, and OpenClaw refuses sources whose container or Docker daemon it
      cannot verify. Read-only mounts stay read-only, and custom sandbox binds still
      use host paths.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Restart the Gateway after changing its mounts or Docker connection. If
      existing sandbox containers have different mounts, OpenClaw keeps them and gives
      you a command to recreate the affected containers. Browser-control connections
      over the default Compose bridge remain a separate limitation.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The model picker opens with choices already loaded, and adds newly discovered
      models while the menu stays open. Models settings also keep healthy choices
      usable when another provider fails, with a warning and Retry available. Account
      labels help distinguish subscription access, API keys, and an explicitly selected
      account. People with permission to edit a session can also change its thinking
      level and fast mode for subsequent turns.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: If the model list or selected account changes during loading, the picker
      can retry the resulting stale-list rejection once without losing your draft.
      The retry keeps the original time limit and still respects cancellation. A second
      failure stays visible; permission and connection failures do not trigger this
      retry.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Channels show artwork from the plugin that provides them. Local session
      links have a claw marker and aligned titles, and desktop WebKit browsers show
      the missing chat permission icons again.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Owners can ask their agent to update the OpenClaw installation hosting
      the conversation through the default tool profiles. /update remains available
      when the model or update tool is unavailable. Existing owner permissions and
      restart restrictions still apply. Optional first-owner setup asks you to confirm
      the exact account and defaults to Skip; ordinary permission to chat does not
      grant administration.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Review the selected CLI's permission policy. Kimi runs its single repair
      prompt with native automatic permissions and no approval prompts, which triage
      announces before launch. Qwen opens an interactive session with its normal approvals;
      saved headless commands retain its native restrictions.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: A missing plugin update no longer has to hold up the core update. OpenClaw
      can keep a compatible installed plugin and explain what still needs repair or
      consent. Eligible official plugins pinned to older releases can return to normal
      catalog updates, including some manually pinned versions. A version or tag explicitly
      requested in your current update command still takes precedence. Explicitly
      linked local plugins keep their selected source, even when a bundled plugin
      has the same name; follow the warning to update them at their source. A completed
      core update can therefore still need plugin follow-up. The update guide explains
      these outcomes.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Once the corrected updater is installed, update checks account for large
      databases and plugin folders when choosing temporary storage and allowing time
      to finish. Simple version checks avoid copying entire conversation histories.
      Checks of the proposed update leave copied background tasks idle and live Workshop
      files intact, preserve authentication policy, and avoid using the MCP Apps sandbox
      port needed by your running installation.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Background update checks now read and save their data in the background,
      and shutdown waits for accepted checks to finish their save attempt. Usage statistics
      remain opt-in, and current consent, Do Not Track, and update-check settings
      are checked before a request is sent. Storage failures can still prevent those
      results from reaching disk.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Online openclaw status --json now uses the running Gateway's facts instead
      of repeating local fleet scans. Its collection flags distinguish uncollected
      checks from clean results, and some fields can be null . Run openclaw security
      audit , openclaw plugins inspect --all , or openclaw memory status --deep when
      you need those inspections. Plugin authors must also treat registration-time
      api.config as read-only; plugins that modify it may fail.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: OpenClaw does less repeated database work when reading and saving conversations,
      including fewer unnecessary file-permission changes on macOS and Linux. On older
      installations, offline Doctor recovery can make conversations searchable again
      when they were missing from the old registry and their transcript files still
      exist. Explicitly deleted conversations stay deleted.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Verified official Discord, Slack, and Matrix installs can retrieve supported
      context from other conversations when your account and destination rules allow
      it. Discord also restores permission and server metadata lookups. Matrix reads
      follow the existing room and direct-message access rules , with no new permission
      to change messages.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Doctor also points out automation paths left behind when Workshop moves
      a skill, so you can update the affected jobs yourself. When sandbox restrictions
      block Workshop, troubleshooting guidance explains that restriction before suggesting
      changes to the tool allowlist.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: OpenClaw can keep handling other requests while it checks what skills need
      to run, prepares their commands or reads sandbox files. This helps when several
      agents start work at once. Some preparation paths can take longer or use more
      CPU while allowing those other requests to proceed.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Security scans use fresh findings after a skill file is replaced. If you
      edit a file during a scan and the scan fails, finish editing and retry. Oversized
      source files are skipped. If a newly loaded pinned skill is rejected because
      its instructions exceed 1 MiB or use a disallowed link, restore the skill artifact
      or explicitly detach the pin.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Microphone permission controls offer Retry or Open Settings. After granting
      access, return to the watch app and tap again to start recording. If the microphone
      cannot start, Voice now shows an audio error.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Rust developers can build on repository-local Gateway and node-host libraries
      for connections, reconnection, platform-managed signing and commands that accept
      input or report progress. A separate-process bridge adds authenticated messages
      and local permission checks.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Manual model choices now follow your allowed-model list , including choices
      made through commands and saved automations. A model being the configured primary
      or fallback no longer grants permission to select it manually. If an existing
      explicit choice is rejected, use Default where supported or add the intended
      model to the list. Current-model reasoning controls remain available, and automatically
      selected child models keep their separate selection rules.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: With a supporting Codex model, you can answer a question in the web UI
      while work continues, or return to it after the turn finishes. Suggested answers
      require your submission. When policy requires permission for a requester's connected
      MCP tool, Codex now asks you to allow that call once or deny it.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Eligible defensive-security requests can receive one automatic Daybreak
      retry after a structured OpenAI policy refusal, in both native Codex and embedded
      OpenAI chats. The retry keeps your selected session model in place. Successful
      interactive embedded retries name Daybreak or your configured retry model before
      the answer, including in the originating group or channel.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Scheduled message edits, deletions and pins must match the saved creator
      provider and account and use an adapter that declares the necessary authorization
      support. Update OpenClaw and the plugin and load its updated registration if
      an unsupported adapter refuses these actions. Claude-created automations preserve
      their saved execution target under automatic placement, but a conflicting explicit
      host or required sandbox policy rejects execution, including for existing jobs
      with that saved target.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Use a visible native subagent with exactly one of projectId or projectGitUrl
      , leaving cwd unset. GitHub HTTPS and git@github.com repository URLs are supported;
      local paths, file URLs, other Git hosts, hidden runs and ACP runs are excluded.
      Existing sandbox boundaries, tool limits and setup-script permissions still
      apply, and arbitrary external directories still require administrator access.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The optional Crabbox sandbox backend can run commands and file tools on
      a cloud machine while your agent and model credentials stay on the host. Enable
      and configure the plugin to use it. Initial support is direct Daytona with a
      compatible Crabbox build; version 0.56.0 lacks the required capability, so prepared-worker
      support alone is not enough. Cloud resource usage applies, and this backend
      does not support sandboxed browsers or Docker bind mounts.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: If Docker or Podman sandbox setup fails, OpenClaw now tries to remove the
      container created by that attempt. Existing containers with a conflicting name
      are left alone. Cleanup can still fail, in which case the error reports both
      the setup and cleanup failures so you know what needs attention.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The viewer's Match option resizes compatible virtual desktops to fit the
      panel when you have control and permission to resize. Fit remains the default,
      and older fixed-size workers need a backend update and reprovisioning. Supported
      browsers in a secure context can also open a view-only Picture-in-Picture window,
      letting you watch the desktop beside other work. Keep the originating viewer
      open.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: With hot reload enabled, you can change browser enablement, JavaScript
      permission, and network policy without restarting the whole Gateway. The browser
      service still restarts, canceling pending work and closing OpenClaw-managed
      Chrome tabs. Attached and remote browsers stay open, but OpenClaw disconnects
      from them. Extension relay settings still require a Gateway restart.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: You can install or reload supported plugins without restarting the Gateway,
      making it easier to add an integration or try a plugin without taking the whole
      installation offline. Owners can do this through the command line or an authorized
      chat command, and the Plugins UI helps you find official and ClawHub packages.
      Existing permission checks and consent still apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: These changes tighten specific permission checks and improve how OpenClaw
      handles credentials in tool results and diagnostics. Client developers can also
      add checks that tie actions to the selected account.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Covered Gateway and node command paths now recheck saved approval-file
      permissions before launch and keep reviewed programs tied to their approved
      paths. This does not stop a process that has already started, and queued Linux
      helper launches can still start after approval is revoked. Requester-specific
      MCP tools in OpenClaw's Codex integration also ask for an allow-once or deny
      decision when policy requires it. Full-permission sessions and the trusted OAuth
      sign-in step retain their exceptions; SDK integrations need to supply the approval
      callback.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Sandboxed Codex file changes through OpenClaw's shipped local and remote
      bridges now reject directory links that redirect them into protected locations.
      Authorized directory aliases still work. Sandbox file tools also follow the
      files and permissions visible inside the container, including overlapping mounts.
      Use exec for container-only storage that file tools cannot verify, and recreate
      affected containers after changing bind sources or access modes. See the Docker
      sandbox guide for the supported mount changes. The patch-tool guide explains
      why full command access can still leave file changes restricted.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Sandbox media reads and reply attachments now retain the active session's
      allowed folders, rejecting reads from another session's sandbox and reply staging
      from an unmounted host workspace on the affected paths. Plugin SDK integrations
      must supply trusted session context to access sandbox files. Authorized workspace
      reads remain available, including the existing caller-workspace access in ordinary
      inbound processing.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: GitHub Copilot sign-in attempts stop further guarded requests and sign-in
      steps when the attempt is revoked or superseded. MiniMax chat sign-in also checks
      current permission before subsequent token requests in both global and CN flows.
      These changes stop later acquisition steps; they do not revoke existing credentials
      or undo token requests already sent.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: IMAP email handling updates Nodemailer for reported security advisories.
      The Tauri desktop app updates Rustls to reject invalid TLS 1.3 handshake sequences
      in its Gateway WebSocket and updater HTTPS connections, while retaining certificate
      and fingerprint checks.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Cancelling during preparation can now stop pending workspace writes, edits,
      and directory changes, with permission checked again before the covered changes
      are made. Cancelled or timed-out CLI runs also lose Gateway tool access during
      process cleanup. Worker attachments copy within their allowed size without overwriting
      files from earlier turns. Cancelling before an attachment is published leaves
      no new destination file; attachments already published, including any replacements
      you later saved, stay in place. Managed worktrees also preserve supported files
      while rejecting source files replaced with symlinks.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: 'Completed host commands now clean up their retained child processes before
      reporting completion, reducing process buildup during long-running sessions.
      This changes shell backgrounding. Children started with & stop when the root
      command finishes. For work that should continue across turns, use background:
      true with the long-running command as the root, then collect its result through
      process . Background command guidance explains the lifetime; sandbox lifetimes
      remain controlled by the sandbox backend.'
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 39-safety-and-privacy-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: safety-privacy
  title: 39 Safety and Privacy changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-09-18-stop-asking-for-approval-of-bash-commands-that-cannot-be-statically-analyzed-in|Stop
  asking for approval of bash commands that cannot be statically analyzed in Ask…]]'
- '[[Changes/Replit/2026-09-18-investigate-with-expanded-audit-logs|Investigate with
  expanded audit logs]]'
- '[[Changes/Google Antigravity/2026-09-19-windows-sandbox-support|Windows sandbox
  support]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: safety-privacy
title: 39 Safety and Privacy changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 39 Safety and Privacy changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fresh OpenAI and ChatGPT/Codex setups start with Astra if you haven't chosen a primary model. Existing choices stay in place. If your account does not offer Astra, choose an available model during OpenAI setup . Verified official plugins also skip a redundant approval step before sign-in. Third-party plugins and those OpenClaw cannot verify still need the applicable consent .

> Local onboarding now selects Full tools when no profile is set, including when you rerun onboarding. This includes messaging and available optional tools from enabled plugins. Explicit profiles stay in place, and an ordinary upgrade leaves an unset profile unchanged. Security settings now save an explicit Full choice. Full selects tools; Full Access controls execution permissions, which remain separate from tool selection and other access restrictions.

> Mac app CLI setup can now recover from temporary-directory permission errors without an administrator password, provided /tmp is writable. The Linux companion's installer also avoids the bundled OpenSSL conflict that could stop system download tools during AppImage setup.

> When OpenClaw runs in Docker, its sandbox shell and browser tools can now see the same workspace and skill files even when the host uses different paths. Workspace and state folders, including nested managed sources, must use verified host bind mounts . Named volumes, tmpfs and files stored only in the image remain unsupported, and OpenClaw refuses sources whose container or Docker daemon it cannot verify. Read-only mounts stay read-only, and custom sandbox binds still use host paths.

> Restart the Gateway after changing its mounts or Docker connection. If existing sandbox containers have different mounts, OpenClaw keeps them and gives you a command to recreate the affected containers. Browser-control connections over the default Compose bridge remain a separate limitation.

> The model picker opens with choices already loaded, and adds newly discovered models while the menu stays open. Models settings also keep healthy choices usable when another provider fails, with a warning and Retry available. Account labels help distinguish subscription access, API keys, and an explicitly selected account. People with permission to edit a session can also change its thinking level and fast mode for subsequent turns.

> If the model list or selected account changes during loading, the picker can retry the resulting stale-list rejection once without losing your draft. The retry keeps the original time limit and still respects cancellation. A second failure stays visible; permission and connection failures do not trigger this retry.

> Channels show artwork from the plugin that provides them. Local session links have a claw marker and aligned titles, and desktop WebKit browsers show the missing chat permission icons again.

> Owners can ask their agent to update the OpenClaw installation hosting the conversation through the default tool profiles. /update remains available when the model or update tool is unavailable. Existing owner permissions and restart restrictions still apply. Optional first-owner setup asks you to confirm the exact account and defaults to Skip; ordinary permission to chat does not grant administration.

> Review the selected CLI's permission policy. Kimi runs its single repair prompt with native automatic permissions and no approval prompts, which triage announces before launch. Qwen opens an interactive session with its normal approvals; saved headless commands retain its native restrictions.

> A missing plugin update no longer has to hold up the core update. OpenClaw can keep a compatible installed plugin and explain what still needs repair or consent. Eligible official plugins pinned to older releases can return to normal catalog updates, including some manually pinned versions. A version or tag explicitly requested in your current update command still takes precedence. Explicitly linked local plugins keep their selected source, even when a bundled plugin has the same name; follow the warning to update them at their source. A completed core update can therefore still need plugin follow-up. The update guide explains these outcomes.

> Once the corrected updater is installed, update checks account for large databases and plugin folders when choosing temporary storage and allowing time to finish. Simple version checks avoid copying entire conversation histories. Checks of the proposed update leave copied background tasks idle and live Workshop files intact, preserve authentication policy, and avoid using the MCP Apps sandbox port needed by your running installation.

> Background update checks now read and save their data in the background, and shutdown waits for accepted checks to finish their save attempt. Usage statistics remain opt-in, and current consent, Do Not Track, and update-check settings are checked before a request is sent. Storage failures can still prevent those results from reaching disk.

> Online openclaw status --json now uses the running Gateway's facts instead of repeating local fleet scans. Its collection flags distinguish uncollected checks from clean results, and some fields can be null . Run openclaw security audit , openclaw plugins inspect --all , or openclaw memory status --deep when you need those inspections. Plugin authors must also treat registration-time api.config as read-only; plugins that modify it may fail.

> OpenClaw does less repeated database work when reading and saving conversations, including fewer unnecessary file-permission changes on macOS and Linux. On older installations, offline Doctor recovery can make conversations searchable again when they were missing from the old registry and their transcript files still exist. Explicitly deleted conversations stay deleted.

> Verified official Discord, Slack, and Matrix installs can retrieve supported context from other conversations when your account and destination rules allow it. Discord also restores permission and server metadata lookups. Matrix reads follow the existing room and direct-message access rules , with no new permission to change messages.

> Doctor also points out automation paths left behind when Workshop moves a skill, so you can update the affected jobs yourself. When sandbox restrictions block Workshop, troubleshooting guidance explains that restriction before suggesting changes to the tool allowlist.

> OpenClaw can keep handling other requests while it checks what skills need to run, prepares their commands or reads sandbox files. This helps when several agents start work at once. Some preparation paths can take longer or use more CPU while allowing those other requests to proceed.

> Security scans use fresh findings after a skill file is replaced. If you edit a file during a scan and the scan fails, finish editing and retry. Oversized source files are skipped. If a newly loaded pinned skill is rejected because its instructions exceed 1 MiB or use a disallowed link, restore the skill artifact or explicitly detach the pin.

> Microphone permission controls offer Retry or Open Settings. After granting access, return to the watch app and tap again to start recording. If the microphone cannot start, Voice now shows an audio error.

> Rust developers can build on repository-local Gateway and node-host libraries for connections, reconnection, platform-managed signing and commands that accept input or report progress. A separate-process bridge adds authenticated messages and local permission checks.

> Manual model choices now follow your allowed-model list , including choices made through commands and saved automations. A model being the configured primary or fallback no longer grants permission to select it manually. If an existing explicit choice is rejected, use Default where supported or add the intended model to the list. Current-model reasoning controls remain available, and automatically selected child models keep their separate selection rules.

> With a supporting Codex model, you can answer a question in the web UI while work continues, or return to it after the turn finishes. Suggested answers require your submission. When policy requires permission for a requester's connected MCP tool, Codex now asks you to allow that call once or deny it.

> Eligible defensive-security requests can receive one automatic Daybreak retry after a structured OpenAI policy refusal, in both native Codex and embedded OpenAI chats. The retry keeps your selected session model in place. Successful interactive embedded retries name Daybreak or your configured retry model before the answer, including in the originating group or channel.

> Scheduled message edits, deletions and pins must match the saved creator provider and account and use an adapter that declares the necessary authorization support. Update OpenClaw and the plugin and load its updated registration if an unsupported adapter refuses these actions. Claude-created automations preserve their saved execution target under automatic placement, but a conflicting explicit host or required sandbox policy rejects execution, including for existing jobs with that saved target.

> Use a visible native subagent with exactly one of projectId or projectGitUrl , leaving cwd unset. GitHub HTTPS and git@github.com repository URLs are supported; local paths, file URLs, other Git hosts, hidden runs and ACP runs are excluded. Existing sandbox boundaries, tool limits and setup-script permissions still apply, and arbitrary external directories still require administrator access.

> The optional Crabbox sandbox backend can run commands and file tools on a cloud machine while your agent and model credentials stay on the host. Enable and configure the plugin to use it. Initial support is direct Daytona with a compatible Crabbox build; version 0.56.0 lacks the required capability, so prepared-worker support alone is not enough. Cloud resource usage applies, and this backend does not support sandboxed browsers or Docker bind mounts.

> If Docker or Podman sandbox setup fails, OpenClaw now tries to remove the container created by that attempt. Existing containers with a conflicting name are left alone. Cleanup can still fail, in which case the error reports both the setup and cleanup failures so you know what needs attention.

> The viewer's Match option resizes compatible virtual desktops to fit the panel when you have control and permission to resize. Fit remains the default, and older fixed-size workers need a backend update and reprovisioning. Supported browsers in a secure context can also open a view-only Picture-in-Picture window, letting you watch the desktop beside other work. Keep the originating viewer open.

> With hot reload enabled, you can change browser enablement, JavaScript permission, and network policy without restarting the whole Gateway. The browser service still restarts, canceling pending work and closing OpenClaw-managed Chrome tabs. Attached and remote browsers stay open, but OpenClaw disconnects from them. Extension relay settings still require a Gateway restart.

> You can install or reload supported plugins without restarting the Gateway, making it easier to add an integration or try a plugin without taking the whole installation offline. Owners can do this through the command line or an authorized chat command, and the Plugins UI helps you find official and ClawHub packages. Existing permission checks and consent still apply.

> These changes tighten specific permission checks and improve how OpenClaw handles credentials in tool results and diagnostics. Client developers can also add checks that tie actions to the selected account.

> Covered Gateway and node command paths now recheck saved approval-file permissions before launch and keep reviewed programs tied to their approved paths. This does not stop a process that has already started, and queued Linux helper launches can still start after approval is revoked. Requester-specific MCP tools in OpenClaw's Codex integration also ask for an allow-once or deny decision when policy requires it. Full-permission sessions and the trusted OAuth sign-in step retain their exceptions; SDK integrations need to supply the approval callback.

> Sandboxed Codex file changes through OpenClaw's shipped local and remote bridges now reject directory links that redirect them into protected locations. Authorized directory aliases still work. Sandbox file tools also follow the files and permissions visible inside the container, including overlapping mounts. Use exec for container-only storage that file tools cannot verify, and recreate affected containers after changing bind sources or access modes. See the Docker sandbox guide for the supported mount changes. The patch-tool guide explains why full command access can still leave file changes restricted.

> Sandbox media reads and reply attachments now retain the active session's allowed folders, rejecting reads from another session's sandbox and reply staging from an unmounted host workspace on the affected paths. Plugin SDK integrations must supply trusted session context to access sandbox files. Authorized workspace reads remain available, including the existing caller-workspace access in ordinary inbound processing.

> GitHub Copilot sign-in attempts stop further guarded requests and sign-in steps when the attempt is revoked or superseded. MiniMax chat sign-in also checks current permission before subsequent token requests in both global and CN flows. These changes stop later acquisition steps; they do not revoke existing credentials or undo token requests already sent.

> IMAP email handling updates Nodemailer for reported security advisories. The Tauri desktop app updates Rustls to reject invalid TLS 1.3 handshake sequences in its Gateway WebSocket and updater HTTPS connections, while retaining certificate and fingerprint checks.

> Cancelling during preparation can now stop pending workspace writes, edits, and directory changes, with permission checked again before the covered changes are made. Cancelled or timed-out CLI runs also lose Gateway tool access during process cleanup. Worker attachments copy within their allowed size without overwriting files from earlier turns. Cancelling before an attachment is published leaves no new destination file; attachments already published, including any replacements you later saved, stay in place. Managed worktrees also preserve supported files while rejecting source files replaced with symlinks.

> Completed host commands now clean up their retained child processes before reporting completion, reducing process buildup during long-running sessions. This changes shell backgrounding. Children started with & stop when the root command finishes. For work that should continue across turns, use background: true with the long-running command as the root, then collect its result through process . Background command guidance explains the lifetime; sandbox lifetimes remain controlled by the sandbox backend.

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
## Nearby in Safety and Privacy

- Earlier: 2026-09-19 · Google Antigravity · [[Changes/Google Antigravity/2026-09-19-windows-sandbox-support|Windows sandbox support]]
- Later: 2026-09-21 · ChatGPT · [[Changes/ChatGPT/2026-09-21-privacy-center-is-rolling-out-to-signed-in-chatgpt-free-go-plus-and-pro-users-it-0d2f36|Privacy Center in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-43edb1&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-39-safety-and-privacy-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-43edb1%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->