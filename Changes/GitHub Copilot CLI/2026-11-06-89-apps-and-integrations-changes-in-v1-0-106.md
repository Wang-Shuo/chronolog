---
card_id: github-copilot-cli-2026-11-06-9e9c38
date: '2026-11-06'
description: 'GitHub Copilot CLI · 2026-11-06 · Apps and Integrations: 89 changes
  in 1.0.106 — Add COPILOT_SESSION_CWD for launching and expanding LSP and local MCP
  server…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2884
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f4e972ce56f5d580458c515a7a627635b467281617fde2ef400b34e7f8cd45df
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-11-06-9e9c38
  comparison: ''
  date: '2026-11-06'
  description: 'GitHub Copilot CLI — 1.0.106: 89 Apps and Integrations changes'
  evidence:
  - quote: Add COPILOT_SESSION_CWD for launching and expanding LSP and local MCP server
      configs
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Sandboxed local MCP servers respect relative filesystem permissions from
      the session directory, even when configured with a different working directory.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Sandboxed local MCP servers now start correctly when configured with a
      relative cwd.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Suppress unnecessary MCP reload summaries when plugin servers remain unchanged
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Form and settings text fields show the control characters of a stored value,
      such as an MCP server command, instead of letting them recolor or hide its text.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Removing a local marketplace now refuses while one of its plugins is enabled,
      --force also clears that plugin, and /plugin marketplace remove accepts --force
      before the name.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: 'The /user switch, environment and /mcp auth pickers, the Run on: status
      and the Outgoing connections list no longer let escape sequences in names, paths
      or URLs restyle the terminal.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: 'Plugin rules with `alwaysApply: false` now stay out of the prompt until
      you enable them in `/instructions`; before, every session applied them until
      `/instructions` or `/plugins` was opened.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A repository hook file under .github/hooks that cannot be read, or a hook
      entry in it that is invalid, is now reported with the file and the reason, at
      startup and after `/cd` into the repository, instead of being skipped silently.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The SDK's session.workspaces.updateMetadata now renames a session that
      already has a name, and both it and session.name.set reject names that session
      creation rejects.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Sandboxed local MCP servers now honor a configured npm_config_cache and
      can write to that cache when dev-tool access is enabled.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Show the MCP reload confirmation after /cd even when a plugin refresh happens
      at the same time
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Avoid false "MCP Servers reloaded" notifications during startup when no
      servers change
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Reduce the wait for the first prompt when multiple MCP servers are unresponsive
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A tool call to an HTTP MCP server that fails with a server error or a dropped
      connection no longer shows an internal Rust type name in front of the reason.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot plugin uninstall` now removes a plugin that `copilot plugin list`
      still shows after its installed files went missing, instead of reporting that
      it is not installed'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot plugin install` now reports a plugin manifest field it ignored,
      instead of installing a plugin with no skills in silence.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP, LSP and plugin.json config files saved with a UTF-8 byte-order mark,
      as Windows PowerShell 5 and older Notepad versions write them, are now loaded
      instead of being rejected or ignored.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot plugin list` and `copilot plugin update` no longer pass control
      characters from a plugin''s name, marketplace or version through to the terminal.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A failed tool call's error text, such as an MCP server's, no longer passes
      escape sequences to the terminal, so it cannot hide text or start a link in
      the failure row.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The move of an older `$XDG_CONFIG_HOME/.copilot` directory into `~/.copilot`
      now also brings over your MCP servers, language servers, saved folder permissions,
      personal instructions, custom agents and skills, and no longer replaces a symlink
      in `~/.copilot` whose target is missing.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Custom subagents with private MCP connections no longer start inherited
      servers excluded by their resolved tool list.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: SDK `extensions.discover()` now lists extensions from enabled plugins installed
      from a local directory marketplace, which sessions already load, and `extensions.enable`
      accepts them under plugin-only extension policy.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Nested subagents inherit and can use MCP tools allowed by the session policy.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: When an MCP server fails to connect, the warning now shows the server's
      error text as plain text, so escape sequences in it can no longer hide or recolor
      the warning or split it across extra lines.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: copilot mcp enable now fails with a clear message for a server the repository
      disables, instead of reporting success and changing nothing
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The `.vscode/mcp.json` migration notice now appears in repository subdirectories
      and after `/cd` into another workspace, and no longer appears for repositories
      already migrated to `.mcp.json`.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Allow /mcp enable and /mcp disable for servers granted GitHub auth at startup
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Signing in to a remote MCP server whose protected resource is a bare origin
      such as https://mcp.example.com no longer sends the resource with an added trailing
      slash, which authorization servers that compare it exactly rejected.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The details view in /skills, /plugin and /mcp no longer passes terminal
      control characters from a skill, plugin or server's metadata through to the
      terminal; its trust and data blocks now show them escaped.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Expanding a tool call with Ctrl+O now shows the values of object and array
      arguments instead of a `{…}` or `[N items]` placeholder, so MCP calls that take
      a nested parameters object can be inspected
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Command hooks receive COPILOT_HOOK_DEPTH so hook-launched sessions can
      stop recursive agentStop chains
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP reload now reports one settled connection summary per reconciliation
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Repository disableAllHooks continues suppressing user hooks after trusted-workspace
      rebuilds
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A long name that wraps beside other text in a row, such as in /extensions
      manage or the /agent picker, no longer loses a character where it wraps.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The /instructions picker no longer lets terminal escape sequences or line
      breaks in an instruction file name or plugin name restyle the list or draw extra
      rows.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Local MCP servers start once per session when the first credential resolves
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: An MCP tool title, or tool arguments the model writes, can no longer use
      8-bit control characters to erase or redraw the tool approval dialog or the
      timeline row
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Plugin rules whose `globs` is a comma-separated string, such as `"*.ts,*.tsx"`,
      now apply to the files those patterns match instead of never applying.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`/remote on` tries again after an earlier attempt failed, instead of reporting
      "Remote control status: connecting." and doing nothing until the CLI is restarted.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: An invalid server entry in a trusted workspace `.mcp.json`, or a file that
      is malformed or unreadable, is now reported as an MCP warning in interactive
      sessions and in `copilot -p` (stderr, or a `session.warning` event with `--output-format
      json`) instead of the server silently missing; before, only `copilot mcp list`
      said why.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Connector authorization stays actionable while plugin inventory is loading
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Plugin installs and uninstalls keep unrelated extension processes running
      in active sessions.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep MCP registry forms and review summaries readable by sanitizing labels
      and truncating on grapheme boundaries
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Installing plugins from different GitHub or URL sources keeps separate
      cache directories.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP servers no longer reload when plugin activation fingerprints change
      without changing active plugins or trust.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Enforce listed choices in MCP enum and multi-select prompts so tool calls
      submit valid values.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot plugin list` shows a plugin that managed policy enables as enabled
      instead of `[disabled]`.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: ACP sessions include skills from live local marketplace plugins in /skills
      list and available commands.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Plugin uninstall on Windows now explains when another app is using a plugin
      file and how to resolve it.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Local plugins with matching directory names now install into separate cache
      directories.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Install PyPI MCP registry servers with pinned package versions
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP stdio requests fail immediately when a response exceeds the 16 MiB
      line limit.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: An HTTP MCP server that accepts connections but never answers now holds
      startup for its connection timeout once, instead of three times over
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Saving MCP server changes preserves symlinked mcp-config.json files and
      updates the symlink target.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Blocked MCP server warnings now include the specific registry failure reason.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: CLI config commands now wait for SDK shutdown before exit and preserve
      the command exit status.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: /extensions mode now reports when the chosen mode cannot be saved or applied,
      instead of closing as if the change was accepted while the previous mode keeps
      running.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP detail view no longer shows a false 'not connected' error for uninstalled
      catalog entries, and shows connecting or disabled for installed servers in those
      states
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: copilot mcp list, get and add with --json now escape C1 control characters
      from a server's command, arguments and environment variable names instead of
      writing them to the terminal raw
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A local MCP server that cannot start now names its missing working directory
      or command, instead of showing the same "No such file or directory" error, printed
      twice, for either case.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot plugin list` reports an invalid config file as one error line
      instead of crashing with a source dump'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot plugin update --all` reports an invalid config file as one error
      line instead of crashing with a source dump'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Commands like --help, version, mcp list, and skill list no longer fail
      when piped to head or grep -q
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Preserve decimal precision when adjusting numeric form fields in MCP elicitation
      prompts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP form string length validation now counts Unicode characters correctly.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Trusted non-git folders now load skills from repo-enabled plugins.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Prompt mode warns when untrusted folders skip repository hooks or workspace
      MCP servers.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Pending-work resume now runs post-tool hooks for completed external tools
      and emits a safe result when post-tool processing fails.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: copilot mcp add rejects invalid --header names and control-character values
      before saving server settings
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep marketplace plugin caches when refresh fails, so transient update
      errors do not remove working checkouts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP policy warnings no longer list servers you have explicitly disabled
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Source-qualified custom agent tool filters now correctly enable the selected
      built-in, MCP, and custom tools.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Installed plugins remain available after moving your Copilot home directory
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Trim edge separators from MCP namespace names so hosted tool search reliably
      resolves connector tools in Responses sessions
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Removing an MCP server now also clears its saved enabled or disabled state,
      so a server added later under the same name starts enabled.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Prevent enterprise-disabled plugins from activating during managed-settings
      startup
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Prompt mode now honors MCP sampling requests when tools are pre-approved
      with --allow-all-tools or mcp-sampling rules.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Reloading extensions now stops running extension processes when extensions.mode
      is disabled.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP sampling requests in headless prompt mode now cancel immediately when
      no host can respond
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Trusted non-repository folders apply enabledPlugins in prompt and plugin
      reload flows
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Built-in browser hooks honor activation settings after reconciliation.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Managed plugins restore activation in existing sessions after policy changes
      during reload.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP tools keep friendly server labels in output while identity-sensitive
      behavior uses the configured server key.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Improve MCP HTTP discovery reliability by waiting longer before legacy
      fallback
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Update the built-in browser-use plugin to 0.1.0 with improved setup and
      browser integration behavior
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP content addressed only to the user is no longer sent to the model,
      and the interactive CLI shows such images inline, even in collapsed tool calls,
      or as saved files
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Plugin and marketplace changes keep the built-in GitHub MCP connection
      when your credentials are unchanged, and /clear and /new connect it once instead
      of twice
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Align /mcp slash-command verbs with the CLI and add ls aliases to list
      commands.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 89-apps-and-integrations-changes-in-v1-0-106
  source_release: github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4
  source_type: github_releases
  theme: apps-integrations
  title: 89 Apps and Integrations changes in v1.0.106
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-11-06-12-apps-and-integrations-changes-in-rust-v0-167-0|12
  Apps and Integrations changes in rust-v0.167.0]]'
- '[[Changes/Descript/2026-11-06-search-for-what-s-in-the-shot-b035ff|Search for what''s
  in the shot]]'
- '[[Changes/Descript/2026-11-06-claude-code-and-codex-can-connect-to-the-descript-mcp-now-if-it-failed-before-re|Claude
  Code and Codex can connect to the Descript MCP now]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4]]'
source_type: github_releases
theme: apps-integrations
title: 89 Apps and Integrations changes in v1.0.106
type: change
---

<!-- chronolog:begin region="header" -->
# 89 Apps and Integrations changes in v1.0.106

**GitHub Copilot CLI** · 2026-11-06 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.106) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add COPILOT_SESSION_CWD for launching and expanding LSP and local MCP server configs

> Sandboxed local MCP servers respect relative filesystem permissions from the session directory, even when configured with a different working directory.

> Sandboxed local MCP servers now start correctly when configured with a relative cwd.

> Suppress unnecessary MCP reload summaries when plugin servers remain unchanged

> Form and settings text fields show the control characters of a stored value, such as an MCP server command, instead of letting them recolor or hide its text.

> Removing a local marketplace now refuses while one of its plugins is enabled, --force also clears that plugin, and /plugin marketplace remove accepts --force before the name.

> The /user switch, environment and /mcp auth pickers, the Run on: status and the Outgoing connections list no longer let escape sequences in names, paths or URLs restyle the terminal.

> Plugin rules with `alwaysApply: false` now stay out of the prompt until you enable them in `/instructions`; before, every session applied them until `/instructions` or `/plugins` was opened.

> A repository hook file under .github/hooks that cannot be read, or a hook entry in it that is invalid, is now reported with the file and the reason, at startup and after `/cd` into the repository, instead of being skipped silently.

> The SDK's session.workspaces.updateMetadata now renames a session that already has a name, and both it and session.name.set reject names that session creation rejects.

> Sandboxed local MCP servers now honor a configured npm_config_cache and can write to that cache when dev-tool access is enabled.

> Show the MCP reload confirmation after /cd even when a plugin refresh happens at the same time

> Avoid false "MCP Servers reloaded" notifications during startup when no servers change

> Reduce the wait for the first prompt when multiple MCP servers are unresponsive

> A tool call to an HTTP MCP server that fails with a server error or a dropped connection no longer shows an internal Rust type name in front of the reason.

> `copilot plugin uninstall` now removes a plugin that `copilot plugin list` still shows after its installed files went missing, instead of reporting that it is not installed

> `copilot plugin install` now reports a plugin manifest field it ignored, instead of installing a plugin with no skills in silence.

> MCP, LSP and plugin.json config files saved with a UTF-8 byte-order mark, as Windows PowerShell 5 and older Notepad versions write them, are now loaded instead of being rejected or ignored.

> `copilot plugin list` and `copilot plugin update` no longer pass control characters from a plugin's name, marketplace or version through to the terminal.

> A failed tool call's error text, such as an MCP server's, no longer passes escape sequences to the terminal, so it cannot hide text or start a link in the failure row.

> The move of an older `$XDG_CONFIG_HOME/.copilot` directory into `~/.copilot` now also brings over your MCP servers, language servers, saved folder permissions, personal instructions, custom agents and skills, and no longer replaces a symlink in `~/.copilot` whose target is missing.

> Custom subagents with private MCP connections no longer start inherited servers excluded by their resolved tool list.

> SDK `extensions.discover()` now lists extensions from enabled plugins installed from a local directory marketplace, which sessions already load, and `extensions.enable` accepts them under plugin-only extension policy.

> Nested subagents inherit and can use MCP tools allowed by the session policy.

> When an MCP server fails to connect, the warning now shows the server's error text as plain text, so escape sequences in it can no longer hide or recolor the warning or split it across extra lines.

> copilot mcp enable now fails with a clear message for a server the repository disables, instead of reporting success and changing nothing

> The `.vscode/mcp.json` migration notice now appears in repository subdirectories and after `/cd` into another workspace, and no longer appears for repositories already migrated to `.mcp.json`.

> Allow /mcp enable and /mcp disable for servers granted GitHub auth at startup

> Signing in to a remote MCP server whose protected resource is a bare origin such as https://mcp.example.com no longer sends the resource with an added trailing slash, which authorization servers that compare it exactly rejected.

> The details view in /skills, /plugin and /mcp no longer passes terminal control characters from a skill, plugin or server's metadata through to the terminal; its trust and data blocks now show them escaped.

> Expanding a tool call with Ctrl+O now shows the values of object and array arguments instead of a `{…}` or `[N items]` placeholder, so MCP calls that take a nested parameters object can be inspected

> Command hooks receive COPILOT_HOOK_DEPTH so hook-launched sessions can stop recursive agentStop chains

> MCP reload now reports one settled connection summary per reconciliation

> Repository disableAllHooks continues suppressing user hooks after trusted-workspace rebuilds

> A long name that wraps beside other text in a row, such as in /extensions manage or the /agent picker, no longer loses a character where it wraps.

> The /instructions picker no longer lets terminal escape sequences or line breaks in an instruction file name or plugin name restyle the list or draw extra rows.

> Local MCP servers start once per session when the first credential resolves

> An MCP tool title, or tool arguments the model writes, can no longer use 8-bit control characters to erase or redraw the tool approval dialog or the timeline row

> Plugin rules whose `globs` is a comma-separated string, such as `"*.ts,*.tsx"`, now apply to the files those patterns match instead of never applying.

> `/remote on` tries again after an earlier attempt failed, instead of reporting "Remote control status: connecting." and doing nothing until the CLI is restarted.

> An invalid server entry in a trusted workspace `.mcp.json`, or a file that is malformed or unreadable, is now reported as an MCP warning in interactive sessions and in `copilot -p` (stderr, or a `session.warning` event with `--output-format json`) instead of the server silently missing; before, only `copilot mcp list` said why.

> Connector authorization stays actionable while plugin inventory is loading

> Plugin installs and uninstalls keep unrelated extension processes running in active sessions.

> Keep MCP registry forms and review summaries readable by sanitizing labels and truncating on grapheme boundaries

> Installing plugins from different GitHub or URL sources keeps separate cache directories.

> MCP servers no longer reload when plugin activation fingerprints change without changing active plugins or trust.

> Enforce listed choices in MCP enum and multi-select prompts so tool calls submit valid values.

> `copilot plugin list` shows a plugin that managed policy enables as enabled instead of `[disabled]`.

> ACP sessions include skills from live local marketplace plugins in /skills list and available commands.

> Plugin uninstall on Windows now explains when another app is using a plugin file and how to resolve it.

> Local plugins with matching directory names now install into separate cache directories.

> Install PyPI MCP registry servers with pinned package versions

> MCP stdio requests fail immediately when a response exceeds the 16 MiB line limit.

> An HTTP MCP server that accepts connections but never answers now holds startup for its connection timeout once, instead of three times over

> Saving MCP server changes preserves symlinked mcp-config.json files and updates the symlink target.

> Blocked MCP server warnings now include the specific registry failure reason.

> CLI config commands now wait for SDK shutdown before exit and preserve the command exit status.

> /extensions mode now reports when the chosen mode cannot be saved or applied, instead of closing as if the change was accepted while the previous mode keeps running.

> MCP detail view no longer shows a false 'not connected' error for uninstalled catalog entries, and shows connecting or disabled for installed servers in those states

> copilot mcp list, get and add with --json now escape C1 control characters from a server's command, arguments and environment variable names instead of writing them to the terminal raw

> A local MCP server that cannot start now names its missing working directory or command, instead of showing the same "No such file or directory" error, printed twice, for either case.

> `copilot plugin list` reports an invalid config file as one error line instead of crashing with a source dump

> `copilot plugin update --all` reports an invalid config file as one error line instead of crashing with a source dump

> Commands like --help, version, mcp list, and skill list no longer fail when piped to head or grep -q

> Preserve decimal precision when adjusting numeric form fields in MCP elicitation prompts

> MCP form string length validation now counts Unicode characters correctly.

> Trusted non-git folders now load skills from repo-enabled plugins.

> Prompt mode warns when untrusted folders skip repository hooks or workspace MCP servers.

> Pending-work resume now runs post-tool hooks for completed external tools and emits a safe result when post-tool processing fails.

> copilot mcp add rejects invalid --header names and control-character values before saving server settings

> Keep marketplace plugin caches when refresh fails, so transient update errors do not remove working checkouts

> MCP policy warnings no longer list servers you have explicitly disabled

> Source-qualified custom agent tool filters now correctly enable the selected built-in, MCP, and custom tools.

> Installed plugins remain available after moving your Copilot home directory

> Trim edge separators from MCP namespace names so hosted tool search reliably resolves connector tools in Responses sessions

> Removing an MCP server now also clears its saved enabled or disabled state, so a server added later under the same name starts enabled.

> Prevent enterprise-disabled plugins from activating during managed-settings startup

> Prompt mode now honors MCP sampling requests when tools are pre-approved with --allow-all-tools or mcp-sampling rules.

> Reloading extensions now stops running extension processes when extensions.mode is disabled.

> MCP sampling requests in headless prompt mode now cancel immediately when no host can respond

> Trusted non-repository folders apply enabledPlugins in prompt and plugin reload flows

> Built-in browser hooks honor activation settings after reconciliation.

> Managed plugins restore activation in existing sessions after policy changes during reload.

> MCP tools keep friendly server labels in output while identity-sensitive behavior uses the configured server key.

> Improve MCP HTTP discovery reliability by waiting longer before legacy fallback

> Update the built-in browser-use plugin to 0.1.0 with improved setup and browser integration behavior

> MCP content addressed only to the user is no longer sent to the model, and the interactive CLI shows such images inline, even in collapsed tool calls, or as saved files

> Plugin and marketplace changes keep the built-in GitHub MCP connection when your credentials are unchanged, and /clear and /new connect it once instead of twice

> Align /mcp slash-command verbs with the CLI and add ls aliases to list commands.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.106
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-11-06-4-voice-and-audio-changes-in-v1-0-106|4 Voice and Audio changes in v1.0.106]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-11-06-2-files-and-data-changes-in-v1-0-106|2 Files and Data changes in v1.0.106]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-11-06-3-reliability-and-performance-changes-in-v1-0-106|3 Reliability and Performance changes in v1.0.106]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-11-06-34-agent-mode-changes-in-v1-0-106|34 Agent Mode changes in v1.0.106]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-11-06-10-memory-and-personalization-changes-in-v1-0-106|10 Memory and Personalization changes in v1.0.106]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-11-06-64-developer-workflow-changes-in-v1-0-106|64 Developer Workflow changes in v1.0.106]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-11-06-34-safety-and-privacy-changes-in-v1-0-106|34 Safety and Privacy changes in v1.0.106]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-11-06-9-collaboration-changes-in-v1-0-106|9 Collaboration changes in v1.0.106]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-11-06-8-mobile-and-desktop-changes-in-v1-0-106|8 Mobile and Desktop changes in v1.0.106]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-11-06-4-projects-and-workspaces-changes-in-v1-0-106|4 Projects and Workspaces changes in v1.0.106]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-11-06-8-accessibility-and-localization-changes-in-v1-0-106|8 Accessibility and Localization changes in v1.0.106]] · Accessibility and Localization
- [[Changes/GitHub Copilot CLI/2026-11-06-17-context-window-changes-in-v1-0-106|17 Context Window changes in v1.0.106]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-11-06-57-editor-experience-changes-in-v1-0-106|57 Editor Experience changes in v1.0.106]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-33-model-support-changes-in-v1-0-106|33 Model Support changes in v1.0.106]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-11-06-2-image-generation-changes-in-v1-0-106|2 Image Generation changes in v1.0.106]] · Image Generation
- [[Changes/GitHub Copilot CLI/2026-11-06-42-interface-experience-changes-in-v1-0-106|42 Interface Experience changes in v1.0.106]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-5-pricing-model-changes-in-v1-0-106|5 Pricing Model changes in v1.0.106]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-11-06-in-the-every-schedule-manager-x-now-removes-the-highlighted-schedule-even-after|In the /every schedule manager, x now removes the highlighted schedule even after…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-11-06-23-account-and-access-changes-in-v1-0-106|23 Account and Access changes in v1.0.106]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-11-06-172-other-changes-in-v1-0-106|172 other changes in v1.0.106]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-11-06 · Descript · [[Changes/Descript/2026-11-06-claude-code-and-codex-can-connect-to-the-descript-mcp-now-if-it-failed-before-re|Claude Code and Codex can connect to the Descript MCP now]]
- Later: 2026-11-06 · OpenCode · [[Changes/OpenCode/2026-11-06-shared-mcp-connections|Shared MCP Connections]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-11-06-9e9c38&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-11-06-89-apps-and-integrations-changes-in-v1-0-106.md%0ACard%20ID%3A%20github-copilot-cli-2026-11-06-9e9c38%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.106%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->