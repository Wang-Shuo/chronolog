---
card_id: openclaw-2026-09-05-96b4e1
date: '2026-09-05'
description: 'OpenClaw · 2026-09-05 · Apps and Integrations: 35 changes in v2026.9.2
  — Open the dashboard to use its controls. Gallery cards leave MCP Apps and non-HTML…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2822
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 68331f64d3cdbb559671c9b5658ec565a6adf57da906fc82f7cad386945608d9
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-05-96b4e1
  comparison: ''
  date: '2026-09-05'
  description: 'OpenClaw — v2026.9.2: 35 Apps and Integrations changes'
  evidence:
  - quote: Open the dashboard to use its controls. Gallery cards leave MCP Apps and
      non-HTML widgets out of their previews, and their Live badge describes a running
      session rather than confirming that every displayed value is current. Named
      dashboard and short session links also avoid the broad session-list searches
      that added waiting on large installations.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Canvas and MCP App previews keep the information that makes them interactive
      and appear once when live conversation content becomes saved history. Already
      loaded widgets retain their input during supported panel changes and renewed
      preview links. Strict previews remain script-free, dashboard permissions stay
      separate from inline previews, and a full reload creates a fresh view.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Package updates preserve the files another updater is actively preparing
      and the shared plugin dependencies another installation still needs. Once the
      replacement Gateway has passed the existing readiness and version checks, the
      updater keeps that healthy process running instead of interrupting it with a
      second restart. Supported upgrades from the published v2026.8.2 package also
      retain the code needed by the older updater to finish replacement and bring
      its previously active managed service back.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: You can change more of how your Claw works without restarting the whole
      Gateway. With the default hybrid configuration reload , routine changes to tools,
      approvals, messaging, speech, browser defaults, retention, and update policy
      reach the next relevant operation while unaffected conversations stay connected.
      Logging changes reach already-running channels and plugins, dashboard serving
      can be switched on or off, and a loaded OpenTelemetry exporter can be replaced
      on its own when its settings change.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Several specific waits are addressed along the way. Committed restarts
      retire obsolete follow-up retries, suspended Gateways cancel background work
      that has not started, and bursts of file logs drain in batches. Already-running
      startup preparation and plugin cleanup are still joined, which can add time
      to a stop. A stop requested from within Gateway chat reports that it has been
      scheduled and lets the requesting operation settle, with final termination remaining
      the responsibility of the serving process or its service manager.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The external-app integration guide covers the handoff's expiry and refusal
      rules. Arming it alone does not stop the process, and pending final conversation
      writes can refuse the handoff. Terminal commands and scrollback end with the
      old process and are not recovered.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Full read-only lint finds expired credentials in the original agent and
      shared stores and reports their usable paths. Legacy Discord, Matrix, Codex,
      and Teams checks skip unrelated startup work when it is not needed. Invalid
      plugin settings now produce a configuration error instead of making the command
      appear missing, with core shell completion still available while you repair
      the settings and regenerate plugin completion. Use doctor --lint or bare doctor
      --json for read-only diagnosis, since ordinary Doctor can migrate state.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Startup also refreshes migrated plugin policy before checking readiness
      and avoids repeated database scans during migration decisions. Large valid agent
      configurations with repeated plugin-owned model choices no longer hit the repaired
      startup bottleneck. These changes let the affected installations reach their
      normal readiness checks, while genuine configuration changes or failed database
      checks still prevent startup.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Discord meetings can now leave behind notes you can return to, and Slack
      conversations give you more useful ways to stop work, follow a reply, or make
      a decision. The changes also carry through the everyday parts of messaging,
      from keeping the instructions attached to one message to preserving code, recordings,
      and generated files as they move through a conversation.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Existing apps need the two session-event subscriptions described in the
      Slack setup guide , and native session status requires a reply thread. A completed
      first reply can still lose its title association after cleanup or restart, and
      overlapping replies can still interfere with the shared working indicator. Progress
      cards also keep earlier errors as recovered history after a successful turn,
      so a finished task does not keep looking failed.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: When a Slack reply would be easier to use as a table or a few choices,
      the agent now has guidance to offer that format without requiring you to ask
      for Block Kit. A status request can become an organized report, or a decision
      can arrive with buttons that let you choose and continue the conversation. This
      uses the existing Slack renderer and supported controls, with plain text for
      simple replies and a text fallback for richer ones; the format the agent chooses
      still depends on the model and request.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Known webhook addresses now ask the sender to retry while a channel or
      plugin is being replaced. This depends on the sender honoring the retry response;
      the message has not been accepted or stored at that point. Multi-account IRC
      setups can also add or edit a non-default named account without disconnecting
      its siblings, while shared settings, default-account changes, and removals can
      still restart the channel.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Native verbose menus in Telegram, Slack, and Discord show the current level
      and let you choose on, off, or full without changing anything merely by opening
      the menu. Malformed explicit text commands such as /exec gateway now return
      an argument error instead of becoming an unintended message to the agent. For
      scripts changing channel accounts, a blank --account is rejected before a change
      begins; omit the option when you intend the command’s normal default selection.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Code examples need to survive as code, including the spaces and literal
      characters that make them useful. Shared reply cleanup and Markdown rendering
      now preserve more of that content through tables, repeated-prose removal, and
      final message rendering, while one-word Slack or Google Chat link labels remain
      readable on plain-text delivery paths.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Administrators and integrations also gain a Gateway API for inspecting
      provider accounts and saving or clearing their priority order. Configuration-controlled
      order remains authoritative, and a successful save can precede the background
      refresh that applies it.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Managed Codex now uses version 0.153.4 and resolves the installation owned
      by its plugin across supported installation layouts, including Windows launchers
      in paths with spaces. A missing managed package produces repair guidance instead
      of silently selecting an unrelated older binary. Externally managed runtimes
      retain the general 0.149.0 minimum, while individual features such as canonical
      message forks require a newer version.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Temporary provider errors receive more appropriate retry handling and advice.
      ChatGPT SSE preserves the service's requested retry delay, and eligible Bedrock
      connection failures before output can continue from completed tool work within
      the existing recovery limit. A failed unrelated harness plugin no longer blocks
      healthy models, later requests can recover from a transient catalog mismatch,
      and beginning provider sign-in leaves serving plugins active. These paths keep
      their existing safeguards against replaying completed effects.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: An unavailable optional Codex app no longer prevents an unrelated conversation
      or heartbeat check-in from starting when a successful app snapshot identifies
      the problem. OpenClaw logs the unavailable apps and continues with the remaining
      tools, including supported resumed sessions and forks. The unavailable app stays
      unavailable, and snapshot failures, tool permissions, and scheduled access checks
      retain their existing restrictions.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Connecting to your existing Chrome session no longer waits for npm's optional
      install audit when the default Chrome MCP helper needs to be downloaded. Chrome
      still needs remote debugging enabled and someone at the computer to approve
      its connection prompt. Custom launcher arguments retain their existing behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Trusted experimental plugins can put custom pages and controls into the
      web workspace, while MCP tools keep their connections when an unrelated server
      changes. For work that reaches another machine or another person, cloud coding
      sessions can push directly to GitHub and shared Beam snapshots can become new
      conversations with a Team agent.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Feature plugins can give your Claw its own pages, panels, widgets, and
      session actions, or replace parts of the conversation interface and the whole
      workspace. An agent can build a plugin archive and propose that exact archive
      for your review before installation, giving you a way to shape the interface
      around your work without changing OpenClaw itself.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Normal layouts currently hide the floating Customize UI entry, limiting
      access to replacement selection and Reload plugin UI . A full plugin workspace
      still offers Built-in recovery. Disabling the lab keeps installed plugins and
      their saved state, and enabled bundled interfaces such as Workboard remain available.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Commenting on a blocked card, refreshing its claim, or releasing that claim
      also reports a successful saved update correctly through the plugin-tools MCP
      bridge. Custom integrations consuming heartbeat, release, comment, or unblock
      results should read the returned card under card . The Workboard registration
      helper again supports integrations that let it create and manage the store.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Plugin updates give a clearer account of what is installed and what can
      change. If an official plugin is pinned to an older version, update and dry-run
      output can show the newer registry release and the explicit command to replace
      the pin. Existing pins stay in place until you choose otherwise. Repairing missing
      plugin files and updating a package now use its current contents, including
      removing settings for children that the replacement package has retired while
      preserving unrelated disabled plugins.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: 'Doctor also separates configuration problems from plugin problems. It
      keeps the original invalid-setting diagnostic instead of blaming whichever plugin
      happened to encounter it, and an absent plugin with an exact enabled: false
      marker no longer attracts contradictory installation advice just because it
      remains allowed. Real warnings still appear when console logging is set to warn.'
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: For valid retired plugins.installs records, openclaw doctor --fix preserves
      installation details before removing the old setting so service startup can
      proceed. It can also repair catalog-proven legacy official ClawHub provenance
      and explain the installation and storage paths behind a trust refusal. Malformed
      records still need correction, and trust rules remain in force. If an unreadable
      native service definition blocks an update, follow the service recovery guide
      , preserving and resupplying any values stored only in that service's environment.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: For replacement messaging plugins, settings validation, form metadata,
      and sensitive-field hints follow the plugin actually selected to run. This does
      not combine every inactive plugin's redaction hints, and sensitive fields belonging
      to an unselected schema can still remain visible.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Plugin authors should check one registration change before upgrading. A
      directly registered channel must declare a nonempty capabilities.chatTypes list
      using supported values. The channel builder still defaults omitted capabilities
      to direct messages; group, channel, and thread support must be declared explicitly.
      Narrow SDK compatibility repairs also retain positional text-chunking ranges
      and legacy provider-wrapper retry inputs. The latter remain deprecated and are
      ignored by built-in text transports, so new wrappers should omit maxRetries
      .
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Plugin branding now comes from artwork included in the installed package,
      so displaying its icon does not contact an arbitrary outside image host. Channel
      gallery rows, details, and setup screens use matching names and locally bundled
      icons, making the integration you are configuring easier to recognize.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Authors must include assets/icon.png to retain custom branding. URL-only
      packages show a generic fallback until updated, and missing or invalid artwork
      does not disable the plugin. Empty icon requests also close their file handles
      correctly instead of accumulating open files on repeated views.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Session-aware command integrations can now receive the current session
      UUID through the resolve_exec_env hook, letting a plugin pass it to scripts
      for attribution or callbacks. Exporting an environment variable still requires
      a plugin that chooses to do so.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Configured prompt and model-input hooks also remain active when HTTP scripts
      or local agent work selects a non-default model, while disabled and excluded
      plugins stay inactive. Installing an npm hook pack no longer requires changing
      inherited npm dry-run or download-directory settings; the installer keeps its
      archive in its own temporary workspace.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Restoring a plugin registry now cancels obsolete cleanup that was still
      queued, preserving its saved session state and reporting only cleanup changes
      that actually committed. Choosing cleanup targets also avoids decoding large
      saved prompts, reducing that particular source of pauses while keeping retained
      content intact.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Looking up or listing saved plugin artifacts reads committed data without
      creating an absent shared store. Missing storage produces an empty result, while
      damaged or unsupported storage still reports an error. Cleanup that writes to
      storage remains a separate operation.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The Lobster setup guide now includes the missing prerequisite. Install
      the optional official plugin with openclaw plugins install @openclaw/lobster
      , restart with openclaw gateway restart , then allow its tool. The tool remains
      unavailable in sandboxed tool contexts. These are corrected setup instructions
      for the existing integration.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 35-apps-and-integrations-changes-in-v2026-9-2
  source_release: openclaw-2026-09-05-v2026-9-2-377f6d77
  source_type: openclaw_changelog
  theme: apps-integrations
  title: 35 Apps and Integrations changes in v2026.9.2
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-03-26-apps-and-integrations-changes-in-v2026-9-1|26
  Apps and Integrations changes in v2026.9.1]]'
- '[[Changes/Claude Code/2026-09-04-vscode-added-an-add-server-form-and-a-remove-action-to-the-mcp-servers-dialog-so|VSCode
  Added an Add server form and a Remove action to the MCP servers dialog…]]'
- '[[Changes/GitHub Copilot CLI/2026-09-04-7-apps-and-integrations-changes-in-v1-0-83|7
  Apps and Integrations changes in v1.0.83]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|openclaw-2026-09-05-v2026-9-2-377f6d77]]'
source_type: openclaw_changelog
theme: apps-integrations
title: 35 Apps and Integrations changes in v2026.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 35 Apps and Integrations changes in v2026.9.2

**OpenClaw** · 2026-09-05 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.2) · from [[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Open the dashboard to use its controls. Gallery cards leave MCP Apps and non-HTML widgets out of their previews, and their Live badge describes a running session rather than confirming that every displayed value is current. Named dashboard and short session links also avoid the broad session-list searches that added waiting on large installations.

> Canvas and MCP App previews keep the information that makes them interactive and appear once when live conversation content becomes saved history. Already loaded widgets retain their input during supported panel changes and renewed preview links. Strict previews remain script-free, dashboard permissions stay separate from inline previews, and a full reload creates a fresh view.

> Package updates preserve the files another updater is actively preparing and the shared plugin dependencies another installation still needs. Once the replacement Gateway has passed the existing readiness and version checks, the updater keeps that healthy process running instead of interrupting it with a second restart. Supported upgrades from the published v2026.8.2 package also retain the code needed by the older updater to finish replacement and bring its previously active managed service back.

> You can change more of how your Claw works without restarting the whole Gateway. With the default hybrid configuration reload , routine changes to tools, approvals, messaging, speech, browser defaults, retention, and update policy reach the next relevant operation while unaffected conversations stay connected. Logging changes reach already-running channels and plugins, dashboard serving can be switched on or off, and a loaded OpenTelemetry exporter can be replaced on its own when its settings change.

> Several specific waits are addressed along the way. Committed restarts retire obsolete follow-up retries, suspended Gateways cancel background work that has not started, and bursts of file logs drain in batches. Already-running startup preparation and plugin cleanup are still joined, which can add time to a stop. A stop requested from within Gateway chat reports that it has been scheduled and lets the requesting operation settle, with final termination remaining the responsibility of the serving process or its service manager.

> The external-app integration guide covers the handoff's expiry and refusal rules. Arming it alone does not stop the process, and pending final conversation writes can refuse the handoff. Terminal commands and scrollback end with the old process and are not recovered.

> Full read-only lint finds expired credentials in the original agent and shared stores and reports their usable paths. Legacy Discord, Matrix, Codex, and Teams checks skip unrelated startup work when it is not needed. Invalid plugin settings now produce a configuration error instead of making the command appear missing, with core shell completion still available while you repair the settings and regenerate plugin completion. Use doctor --lint or bare doctor --json for read-only diagnosis, since ordinary Doctor can migrate state.

> Startup also refreshes migrated plugin policy before checking readiness and avoids repeated database scans during migration decisions. Large valid agent configurations with repeated plugin-owned model choices no longer hit the repaired startup bottleneck. These changes let the affected installations reach their normal readiness checks, while genuine configuration changes or failed database checks still prevent startup.

> Discord meetings can now leave behind notes you can return to, and Slack conversations give you more useful ways to stop work, follow a reply, or make a decision. The changes also carry through the everyday parts of messaging, from keeping the instructions attached to one message to preserving code, recordings, and generated files as they move through a conversation.

> Existing apps need the two session-event subscriptions described in the Slack setup guide , and native session status requires a reply thread. A completed first reply can still lose its title association after cleanup or restart, and overlapping replies can still interfere with the shared working indicator. Progress cards also keep earlier errors as recovered history after a successful turn, so a finished task does not keep looking failed.

> When a Slack reply would be easier to use as a table or a few choices, the agent now has guidance to offer that format without requiring you to ask for Block Kit. A status request can become an organized report, or a decision can arrive with buttons that let you choose and continue the conversation. This uses the existing Slack renderer and supported controls, with plain text for simple replies and a text fallback for richer ones; the format the agent chooses still depends on the model and request.

> Known webhook addresses now ask the sender to retry while a channel or plugin is being replaced. This depends on the sender honoring the retry response; the message has not been accepted or stored at that point. Multi-account IRC setups can also add or edit a non-default named account without disconnecting its siblings, while shared settings, default-account changes, and removals can still restart the channel.

> Native verbose menus in Telegram, Slack, and Discord show the current level and let you choose on, off, or full without changing anything merely by opening the menu. Malformed explicit text commands such as /exec gateway now return an argument error instead of becoming an unintended message to the agent. For scripts changing channel accounts, a blank --account is rejected before a change begins; omit the option when you intend the command’s normal default selection.

> Code examples need to survive as code, including the spaces and literal characters that make them useful. Shared reply cleanup and Markdown rendering now preserve more of that content through tables, repeated-prose removal, and final message rendering, while one-word Slack or Google Chat link labels remain readable on plain-text delivery paths.

> Administrators and integrations also gain a Gateway API for inspecting provider accounts and saving or clearing their priority order. Configuration-controlled order remains authoritative, and a successful save can precede the background refresh that applies it.

> Managed Codex now uses version 0.153.4 and resolves the installation owned by its plugin across supported installation layouts, including Windows launchers in paths with spaces. A missing managed package produces repair guidance instead of silently selecting an unrelated older binary. Externally managed runtimes retain the general 0.149.0 minimum, while individual features such as canonical message forks require a newer version.

> Temporary provider errors receive more appropriate retry handling and advice. ChatGPT SSE preserves the service's requested retry delay, and eligible Bedrock connection failures before output can continue from completed tool work within the existing recovery limit. A failed unrelated harness plugin no longer blocks healthy models, later requests can recover from a transient catalog mismatch, and beginning provider sign-in leaves serving plugins active. These paths keep their existing safeguards against replaying completed effects.

> An unavailable optional Codex app no longer prevents an unrelated conversation or heartbeat check-in from starting when a successful app snapshot identifies the problem. OpenClaw logs the unavailable apps and continues with the remaining tools, including supported resumed sessions and forks. The unavailable app stays unavailable, and snapshot failures, tool permissions, and scheduled access checks retain their existing restrictions.

> Connecting to your existing Chrome session no longer waits for npm's optional install audit when the default Chrome MCP helper needs to be downloaded. Chrome still needs remote debugging enabled and someone at the computer to approve its connection prompt. Custom launcher arguments retain their existing behavior.

> Trusted experimental plugins can put custom pages and controls into the web workspace, while MCP tools keep their connections when an unrelated server changes. For work that reaches another machine or another person, cloud coding sessions can push directly to GitHub and shared Beam snapshots can become new conversations with a Team agent.

> Feature plugins can give your Claw its own pages, panels, widgets, and session actions, or replace parts of the conversation interface and the whole workspace. An agent can build a plugin archive and propose that exact archive for your review before installation, giving you a way to shape the interface around your work without changing OpenClaw itself.

> Normal layouts currently hide the floating Customize UI entry, limiting access to replacement selection and Reload plugin UI . A full plugin workspace still offers Built-in recovery. Disabling the lab keeps installed plugins and their saved state, and enabled bundled interfaces such as Workboard remain available.

> Commenting on a blocked card, refreshing its claim, or releasing that claim also reports a successful saved update correctly through the plugin-tools MCP bridge. Custom integrations consuming heartbeat, release, comment, or unblock results should read the returned card under card . The Workboard registration helper again supports integrations that let it create and manage the store.

> Plugin updates give a clearer account of what is installed and what can change. If an official plugin is pinned to an older version, update and dry-run output can show the newer registry release and the explicit command to replace the pin. Existing pins stay in place until you choose otherwise. Repairing missing plugin files and updating a package now use its current contents, including removing settings for children that the replacement package has retired while preserving unrelated disabled plugins.

> Doctor also separates configuration problems from plugin problems. It keeps the original invalid-setting diagnostic instead of blaming whichever plugin happened to encounter it, and an absent plugin with an exact enabled: false marker no longer attracts contradictory installation advice just because it remains allowed. Real warnings still appear when console logging is set to warn.

> For valid retired plugins.installs records, openclaw doctor --fix preserves installation details before removing the old setting so service startup can proceed. It can also repair catalog-proven legacy official ClawHub provenance and explain the installation and storage paths behind a trust refusal. Malformed records still need correction, and trust rules remain in force. If an unreadable native service definition blocks an update, follow the service recovery guide , preserving and resupplying any values stored only in that service's environment.

> For replacement messaging plugins, settings validation, form metadata, and sensitive-field hints follow the plugin actually selected to run. This does not combine every inactive plugin's redaction hints, and sensitive fields belonging to an unselected schema can still remain visible.

> Plugin authors should check one registration change before upgrading. A directly registered channel must declare a nonempty capabilities.chatTypes list using supported values. The channel builder still defaults omitted capabilities to direct messages; group, channel, and thread support must be declared explicitly. Narrow SDK compatibility repairs also retain positional text-chunking ranges and legacy provider-wrapper retry inputs. The latter remain deprecated and are ignored by built-in text transports, so new wrappers should omit maxRetries .

> Plugin branding now comes from artwork included in the installed package, so displaying its icon does not contact an arbitrary outside image host. Channel gallery rows, details, and setup screens use matching names and locally bundled icons, making the integration you are configuring easier to recognize.

> Authors must include assets/icon.png to retain custom branding. URL-only packages show a generic fallback until updated, and missing or invalid artwork does not disable the plugin. Empty icon requests also close their file handles correctly instead of accumulating open files on repeated views.

> Session-aware command integrations can now receive the current session UUID through the resolve_exec_env hook, letting a plugin pass it to scripts for attribution or callbacks. Exporting an environment variable still requires a plugin that chooses to do so.

> Configured prompt and model-input hooks also remain active when HTTP scripts or local agent work selects a non-default model, while disabled and excluded plugins stay inactive. Installing an npm hook pack no longer requires changing inherited npm dry-run or download-directory settings; the installer keeps its archive in its own temporary workspace.

> Restoring a plugin registry now cancels obsolete cleanup that was still queued, preserving its saved session state and reporting only cleanup changes that actually committed. Choosing cleanup targets also avoids decoding large saved prompts, reducing that particular source of pauses while keeping retained content intact.

> Looking up or listing saved plugin artifacts reads committed data without creating an absent shared store. Missing storage produces an empty result, while damaged or unsupported storage still reports an error. Cleanup that writes to storage remains a separate operation.

> The Lobster setup guide now includes the missing prerequisite. Install the optional official plugin with openclaw plugins install @openclaw/lobster , restart with openclaw gateway restart , then allow its tool. The tool remains unavailable in sandboxed tool contexts. These are corrected setup instructions for the existing integration.

Source: https://docs.openclaw.ai/releases/2026.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-05-24-safety-and-privacy-changes-in-v2026-9-2|24 Safety and Privacy changes in v2026.9.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-05-3-pricing-model-changes-in-v2026-9-2|3 Pricing Model changes in v2026.9.2]] · Pricing Model
- [[Changes/OpenClaw/2026-09-05-8-editor-experience-changes-in-v2026-9-2|8 Editor Experience changes in v2026.9.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-05-progress-mode-can-stay-quiet-about-routine-tool-calls-while-keeping-the-updates|Progress mode can stay quiet about routine tool calls while keeping the updates…]] · Presentation Creation
- [[Changes/OpenClaw/2026-09-05-swarm-is-now-available-to-eligible-agents-without-a-separate-enablement-step-so|Swarm is now available to eligible agents without a separate enablement step…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-a-rejected-send-can-keep-its-original-attachments-and-retry-action-when-you-leav|A rejected send can keep its original attachments and Retry action when you leave…]] · Files and Data
- [[Changes/OpenClaw/2026-09-05-20-account-and-access-changes-in-v2026-9-2|20 Account and Access changes in v2026.9.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-05-17-model-support-changes-in-v2026-9-2|17 Model Support changes in v2026.9.2]] · Model Support
- [[Changes/OpenClaw/2026-09-05-16-developer-workflow-changes-in-v2026-9-2|16 Developer Workflow changes in v2026.9.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-21-memory-and-personalization-changes-in-v2026-9-2|21 Memory and Personalization changes in v2026.9.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-05-4-enterprise-and-administration-changes-in-v2026-9-2|4 Enterprise and Administration changes in v2026.9.2]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-05-if-background-image-video-or-music-generation-finishes-but-final-delivery-fails|If background image, video or music generation finishes but final delivery fails…]] · Music Generation
- [[Changes/OpenClaw/2026-09-05-34-agent-mode-changes-in-v2026-9-2|34 Agent Mode changes in v2026.9.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-8-automation-and-scheduling-changes-in-v2026-9-2|8 Automation and Scheduling changes in v2026.9.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-05-9-collaboration-changes-in-v2026-9-2|9 Collaboration changes in v2026.9.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-05-10-mobile-and-desktop-changes-in-v2026-9-2|10 Mobile and Desktop changes in v2026.9.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-05-15-context-window-changes-in-v2026-9-2|15 Context Window changes in v2026.9.2]] · Context Window
- [[Changes/OpenClaw/2026-09-05-4-search-and-browsing-changes-in-v2026-9-2|4 Search and Browsing changes in v2026.9.2]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-05-17-voice-and-audio-changes-in-v2026-9-2|17 Voice and Audio changes in v2026.9.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-05-21-interface-experience-changes-in-v2026-9-2|21 Interface Experience changes in v2026.9.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-05-3-reliability-and-performance-changes-in-v2026-9-2|3 Reliability and Performance changes in v2026.9.2]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-05-you-can-now-put-the-part-of-a-task-you-are-working-on-in-the-main-view-and-keep|Put the part of a task you are working on in the main view and keep the conversation…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-72-other-changes-in-v2026-9-2|72 other changes in v2026.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-04 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-04-7-apps-and-integrations-changes-in-v1-0-83|7 Apps and Integrations changes in v1.0.83]]
- Later: 2026-09-07 · ElevenLabs · [[Changes/ElevenLabs/2026-09-07-sdk-releases|SDK releases]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-05-96b4e1&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-05-35-apps-and-integrations-changes-in-v2026-9-2.md%0ACard%20ID%3A%20openclaw-2026-09-05-96b4e1%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->