---
created: '2023-03-23'
date: '2026-07-24'
machine_hash: 89f95df15540163c76ecfd4db97facb2bef8df7f33af7838f1951b79f2b60d86
modified: '2026-07-24'
products_involved:
- ChatGPT
- Claude Code
- Cursor
status: official
tags:
- theme
- moc
theme: apps-integrations
---

# Theme: apps-integrations

## Cross-Product Timeline
<!-- chronolog:begin region="timeline" -->
```mermaid
timeline
    title apps-integrations
    2023-03-23 : ChatGPT : We are announcing experimental support for AI plugins in ChatGPT — tools designe
    2023-03-23 : ChatGPT : Today, we will begin extending plugin access to users and developers from our wa
    2023-05-04 : Cursor : One-Click Extension Import from VS Code (beta). As a highly requested feature, w
    2023-05-12 : ChatGPT : Plugins: Try a new version of ChatGPT that knows when and how to use third-party
    2023-05-12 : ChatGPT : In the “Plugins” dropdown, click “Plugin Store” to install and enable new plugin
    2023-05-17 : Cursor : You can Pin custom extensions to your activity bar in the top left
    2023-06-09 : Cursor : You can now have the AI read documentation on your behalf! This will improve it'
    2023-06-16 : Cursor : We've added support for using your Azure OpenAI credentials. Also, small improve
    2023-06-27 : Cursor : cursor:// deep linking works now, so you should be able to log in to extensions
    2023-06-27 : Cursor : Better support for extensions (specifically re-enables the welcomeView)
    2023-07-03 : Cursor : Also, Cursor's AI will now use popular documentation to improve the answers to y
    2023-07-07 : Cursor : Makes it clearer which docs are being looked at by the AI
    2023-07-07 : Cursor : Improved the "@Add new doc" experience
    2023-07-07 : Cursor : AI will respond with citations when you reference docs
    2023-07-28 : Cursor : More robust extension handling. You can now use pre-release extensions again.
    2023-09-08 : Cursor : The main addition in this update is better docs support. This means you can add
    2023-09-11 : Cursor : We serve extensions now using Cursor's Extension Marketplace
    2023-09-17 : Cursor : We point to a different marketplace for downloading extensions, and use a fork o
    2023-10-20 : Cursor : Cursor is now based on VS Code 1.83.1. This ensures that the newest versions of
    2023-11-06 : ChatGPT : Plus and Enterprise users can start creating GPTs this week. Later this month, w
    2023-11-06 : ChatGPT : You can now create custom versions of ChatGPT that combine instructions, extra k
    2023-11-15 : Cursor : Now based on VS Code 1.84.2. Notably, this fixes a few notebook bugs, and ensure
    2023-11-15 : Cursor : Cursor is now based on VS Code 1.84.2. Notably, this fixes a few notebook bugs,
    2023-12-16 : Cursor : Copilot++: We've continued to improve the Copilot++ ghost text experience. Surpr
    2024-01-10 : ChatGPT : Explore GPTs at chatgpt.com/gpts.
    2024-01-10 : ChatGPT : Discover what’s trending in the GPT Store
    2024-01-15 : Cursor : Supports newer version of python extension
    2024-01-25 : Cursor : UPDATE (0.24.3-0.24.4): Adds ability to configure OpenAI base URL, fixes getcurs
    2024-05-16 : ChatGPT : Upload the latest file versions directly from Google Drive, Microsoft OneDrive P
    2024-07-03 : Cursor : Docs management! Go to Cursor Settings > Features > Docs to re-index your docs.
    2024-11-22 : ChatGPT : Recent GPTs & Pinned GPT's are now displayed below conversations
    2025-02-19 : Cursor : MCP: Improved reliability and quality of life enhancements for building MCP serv
    2025-02-19 : Cursor : 0.46.2: Improved MCP reliability, added option to disable yolo mode for MCP
    2025-03-23 : Cursor : Projects with MCP servers will now prompt users to enable them
    2025-05-15 : ChatGPT : The GitHub connector is now available globally to Plus/Pro/Team users, including
    2025-06-04 : ChatGPT : Supported connectors: Google Drive, SharePoint, Dropbox, Box, Outlook, Gmail, Go
    2025-06-04 : ChatGPT : Admin-published connectors appear in the connector list for all users
    2025-06-04 : ChatGPT : Admins and users can now build and deploy custom connectors to proprietary syste
    2025-06-12 : Cursor : Mention @Cursor in any thread with a prompt like:
    2025-06-24 : ChatGPT : Pro users are now able to use chat search connectors (in addition to deep resear
    2025-07-03 : Cursor : To-dos are also visible in Slack if integration is setup!
    2025-07-03 : Cursor : The agent breaks down longer tasks with dependencies, visible to you in chat and
    2025-07-24 : ChatGPT : Pro users can now utilize chat search with HubSpot and custom connectors (MCP) i
    2025-08-11 : ChatGPT : Note: Connectors for Plus/Pro plans are not available in EEA, Switzerland, and t
    2025-08-11 : ChatGPT : Now connect even more tools in ChatGPT for useful, relevant responses in chat.
    2025-08-13 : ChatGPT : Gmail, Google Calendar, and Google Contacts Connectors in ChatGPT are now availa
    2025-09-29 : Cursor : Browser Controls
    2025-10-09 : ChatGPT : We're adding Notion and Linear as synced connectors (for Pro users), so you can
    2025-10-13 : ChatGPT : Installing the app requires the connector to be enabled for your account.
    2025-10-13 : ChatGPT : We’re rolling out two new ways to bring Slack and ChatGPT together: a connector
    2025-10-13 : ChatGPT : Both app and connector are available to Plus, Pro, Business and Enterprise/Edu c
    2025-10-13 : ChatGPT : With the ChatGPT app for Slack, you can chat one-on-one with ChatGPT in a dedica
    2025-10-29 : Cursor : Browser (GA)
    2025-12-18 : ChatGPT : You can now browse and add approved apps in the new app directory. Apps let you
    2025-12-19 : Claude Code : Added search filtering to the plugin discover screen (type to filter by name, de
    2025-12-22 : Cursor : Improved integrated browser to support opening multiple tabs.
    2025-12-22 : Cursor : Cursor now separates processes running for user-installed extensions and built-i
    2026-01-08 : Cursor : Rules generation and management
    2026-01-08 : Cursor : This release introduces new CLI controls for models, MCP management, rules and c
    2026-01-09 : Claude Code : Added `FORCE_AUTOUPDATE_PLUGINS` environment variable to allow plugin autoupdate
    2026-01-13 : Claude Code : Added automatic discovery of skills from nested `.claude/skills` directories whe
    2026-01-20 : Claude Code : Added support for pinning plugins to specific git commit SHAs, allowing marketpl
    2026-01-20 : Claude Code : Added search to installed plugins list - type to filter by name or description
    2026-01-22 : Claude Code : [VSCode] Added native plugin management support
    2026-01-23 : Claude Code : Changed skills without additional permissions or hooks to be allowed without req
    2026-01-23 : Claude Code : [SDK] Added replay of `queued_command` attachment messages as `SDKUserMessageRep
    2026-01-30 : Claude Code : VSCode: Enabled Claude in Chrome integration
    2026-02-05 : Claude Code : Skills defined in `.claude/skills/` within additional directories (`--add-dir`)
    2026-02-06 : Claude Code : Added plugin name to skill descriptions and `/skills` menu for better discoverab
    2026-02-17 : Claude Code : Added support for reading `enabledPlugins` and `extraKnownMarketplaces` from `--
    2026-02-17 : Claude Code : Added `SDKRateLimitInfo` and `SDKRateLimitEvent` types to the SDK, enabling cons
    2026-02-17 : Cursor : Plugins package skills, subagents, MCP servers, hooks, and rules, into a single
    2026-02-17 : Cursor : Plugins on the Cursor Marketplace
    2026-02-17 : Cursor : Browse plugins at cursor.com/marketplace or install directly in the editor with
    2026-02-17 : Cursor : Our initial partners include Amplitude, AWS, Figma, Linear, Stripe, and more. Th
    2026-02-19 : ChatGPT : Preview diagrams and mini apps directly in chat
    2026-02-20 : Claude Code : `CLAUDE_CODE_SIMPLE` mode now also disables MCP tools, attachments, hooks, and C
    2026-02-24 : Claude Code : Added support for custom npm registries and specific version pinning when instal
    2026-02-24 : Claude Code : Added `claude remote-control` subcommand for external builds, enabling local env
    2026-02-24 : Claude Code : Updated plugin marketplace default git timeout from 30s to 120s and added `CLAUD
    2026-02-25 : ChatGPT : Additionally, use connected apps directly in chats.
    2026-02-25 : ChatGPT : Sources from apps: Paste a link to a Slack channel or Google Drive file or folde
    2026-02-25 : Claude Code : Expand Remote Control to more users
    2026-02-28 : Claude Code : Added `ENABLE_CLAUDEAI_MCP_SERVERS=false` env var to opt out from making claude.
    2026-03-03 : Cursor : MCP Apps support interactive user interfaces like charts from Amplitude, diagram
    2026-03-05 : Claude Code : Added the `/claude-api` skill for building applications with the Claude API and
    2026-03-05 : Claude Code : Added optional name argument to `/remote-control` and `claude remote-control` (`
    2026-03-06 : Claude Code : Reduced Remote Control `/poll` rate to once per 10 minutes while connected (was
    2026-03-10 : Claude Code : Changed tool search to bypass the third-party proxy gate when the environment va
    2026-03-10 : Claude Code : Added `claude plugins` as an alias for `claude plugin`
    2026-03-11 : Cursor : Try out the new plugins at cursor.com/marketplace, or read more in our announcem
    2026-03-11 : Cursor : We've added more than 30 new plugins from partners such as Atlassian, Datadog, G
    2026-03-12 : Claude Code : Changed `--plugin-dir` so local dev copies now override installed marketplace pl
    2026-03-14 : Claude Code : Added new `Elicitation` and `ElicitationResult` hooks to intercept and override
    2026-03-14 : Claude Code : Added MCP elicitation support — MCP servers can now request structured input mid
    2026-03-17 : Claude Code : Added `StopFailure` hook event that fires when the turn ends due to an API error
    2026-03-17 : Claude Code : Added `effort`, `maxTurns`, and `disallowedTools` frontmatter support for plugin
    2026-03-17 : Claude Code : Added `${CLAUDE_PLUGIN_DATA}` variable for plugin persistent state that survives
    2026-03-19 : Claude Code : Added `source: 'settings'` plugin marketplace source — declare plugin entries in
    2026-03-19 : Claude Code : Added `--channels` (research preview) — allow MCP servers to push messages into
    2026-03-19 : Claude Code : Added CLI tool usage detection to plugin tips, in addition to file pattern match
    2026-03-20 : Claude Code : Improved MCP read/search tool calls to collapse into a single "Queried {server}"
    2026-03-25 : ChatGPT : Google’s file connectors in ChatGPT are now unified under Google Drive, providin
    2026-03-25 : Claude Code : Added `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` to strip Anthropic and cloud provider
    2026-03-25 : Claude Code : Added `disableDeepLinkRegistration` setting to prevent `claude-cli://` protocol
    2026-03-25 : Claude Code : Added `CwdChanged` and `FileChanged` hook events for reactive environment manage
    2026-03-26 : Claude Code : Added `CLAUDE_CODE_MCP_SERVER_NAME` and `CLAUDE_CODE_MCP_SERVER_URL` environment
    2026-03-26 : Claude Code : Deep link queries (`claude-cli://open?q=…`) now support up to 5,000 characters,
    2026-03-27 : ChatGPT : We’re rolling out updated Box, Notion, Linear, and Dropbox apps in ChatGPT. Thes
    2026-03-27 : ChatGPT : If you already use these apps in ChatGPT, reconnect the app to start using the u
    2026-03-27 : Claude Code : Reduced startup event-loop stalls when many claude.ai MCP connectors are configu
    2026-04-01 : Claude Code : Added `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode to skip the MCP connection
    2026-04-01 : Claude Code : Added `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE` env var to keep the exist
    2026-04-02 : Claude Code : Added support for multi-line prompts in `claude-cli://open?q=` deep links (encod
    2026-04-02 : Claude Code : Added MCP tool result persistence override via `_meta["anthropic/maxResultSizeCh
    2026-04-02 : Claude Code : Added `disableSkillShellExecution` setting to disable inline shell execution in
    2026-04-02 : Claude Code : Plugins can now ship executables under `bin/` and invoke them as bare commands f
    2026-04-04 : Claude Code : Remote Control session names now use your hostname as the default prefix (e.g. `
    2026-04-07 : Claude Code : Added `hookSpecificOutput.sessionTitle` to `UserPromptSubmit` hooks for setting
    2026-04-07 : Claude Code : Added support for Amazon Bedrock powered by Mantle, set `CLAUDE_CODE_USE_MANTLE=
    2026-04-07 : Claude Code : Added compact `Slacked #channel` header with a clickable channel link for Slack
    2026-04-07 : Claude Code : Added `keep-coding-instructions` frontmatter field support for plugin output sty
    2026-04-08 : Cursor : Bugbot MCP Support
    2026-04-08 : Cursor : Bugbot Learned Rules
    2026-04-08 : Cursor : It looks at reactions and replies to Bugbot comments and comments from human rev
    2026-04-08 : Cursor : This release introduces updates to Bugbot including the ability to self-improve
    2026-04-13 : Claude Code : Added background monitor support for plugins via a top-level `monitors` manifest
    2026-04-13 : Claude Code : Added PreCompact hook support: hooks can now block compaction by exiting with co
    2026-04-20 : Claude Code : Faster MCP startup when multiple stdio servers are configured; `resources/templa
    2026-04-22 : Claude Code : Faster startup when both local and claude.ai MCP servers are configured (concurr
    2026-04-23 : Claude Code : Create and switch between named custom themes from `/theme`, or hand-edit JSON f
    2026-04-23 : Claude Code : Hooks can now invoke MCP tools directly via `type: "mcp_tool"`
    2026-04-28 : Claude Code : Added `claude plugin prune` to remove orphaned auto-installed plugin dependencie
    2026-04-28 : Claude Code : Added `ANTHROPIC_BEDROCK_SERVICE_TIER` environment variable to select a Bedrock
    2026-04-28 : Claude Code : `/mcp` now shows claude.ai connectors hidden by a manually-added server with the
    2026-04-28 : Claude Code : Added `alwaysLoad` option to MCP server config — when `true`, all tools from tha
    2026-04-28 : Claude Code : PostToolUse hooks can now replace tool output for all tools via `hookSpecificOut
    2026-04-29 : Cursor : We're introducing the Cursor SDK so you can build agents with the same runtime,
    2026-04-29 : Cursor : Run npm install @cursor/sdk to get started. You can also use Cursor's native /sd
    2026-05-01 : Cursor : Plugins bundle capabilities like MCP servers, skills, subagents, rules, and hook
    2026-05-01 : Cursor : Required: users always have the plugin and cannot uninstall it
    2026-05-01 : Cursor : Default On: users get the plugin installed by default, but can opt out
    2026-05-04 : Claude Code : `--plugin-dir` now accepts `.zip` plugin archives in addition to directories
    2026-05-04 : Claude Code : `/mcp` now shows the tool count for connected servers and flags servers that con
    2026-05-06 : Claude Code : Plugin manifests: `themes` and `monitors` should now be declared under `"experim
    2026-05-06 : Claude Code : Added `CLAUDE_CODE_SESSION_ID` environment variable to the Bash tool subprocess
    2026-05-06 : Claude Code : Added `--plugin-url <url>` flag to fetch a plugin `.zip` archive from a URL for
    2026-05-07 : Claude Code : Hooks now receive the active effort level via the `effort.level` JSON input fiel
    2026-05-11 : Claude Code : Added `claude plugin details <name>` to show a plugin's component inventory and
    2026-05-11 : Claude Code : Added `/goal` command: set a completion condition and Claude keeps working acros
    2026-05-11 : Cursor : Get started by installing the integration in the Cursor dashboard. Learn more in
    2026-05-12 : Claude Code : Plugins now warn when a default component folder (e.g. `commands/`) is silently
    2026-05-13 : Claude Code : Added `terminalSequence` field to hook JSON output so hooks can emit desktop not
    2026-05-13 : Claude Code : Added `CLAUDE_CODE_PLUGIN_PREFER_HTTPS` to clone GitHub plugin sources over HTTP
    2026-05-14 : Claude Code : Plugins with a root-level `SKILL.md` and no `skills/` subdirectory are now surfa
    2026-05-14 : Claude Code : The `/plugin` details pane and `claude plugin details` now show LSP servers a pl
    2026-05-14 : Claude Code : `/web-setup` warns before replacing an existing GitHub App connection
    2026-05-15 : Claude Code : Added plugin dependency enforcement: `claude plugin disable` now refuses when an
    2026-05-19 : Claude Code : `/plugin` Discover and Browse screens now show a plugin's commands, agents, skil
    2026-05-19 : Cursor : Cursor is now available in Jira.
    2026-05-19 : Cursor : You can ask Cursor to fix bugs, add features, update tests, or investigate somet
    2026-05-19 : Cursor : Install the integration from Cursor integrations. You need Cursor admin access a
    2026-05-22 : Claude Code : `/usage` now shows a per-category breakdown of what's driving your limits usage
    2026-05-22 : Claude Code : Enterprise: added the `allowAllClaudeAiMcps` managed setting to load claude.ai c
    2026-05-27 : Claude Code : `SessionStart` hooks can now set the session title via `hookSpecificOutput.sessi
    2026-05-27 : Claude Code : `SessionStart` hooks can now return `reloadSkills: true` to re-scan skill direct
    2026-05-28 : Claude Code : Added `skipLfs` option to `github`/`git` plugin marketplace sources to skip Git
    2026-05-29 : Claude Code : Added `claude plugin init <name>` to scaffold a new plugin in `.claude/skills`
    2026-05-29 : Claude Code : Plugins in `.claude/skills` directories are now automatically loaded, no marketp
    2026-05-29 : Claude Code : Added autocomplete for `/plugin` arguments: subcommands, installed plugin names,
    2026-06-02 : Claude Code : `/mcp` now collapses claude.ai connectors you've never signed in to behind a "Sh
    2026-06-03 : Claude Code : Remote Control now shows as a persistent footer pill (with a link to the session
    2026-06-04 : Claude Code : Hooks: Stop and SubagentStop hooks can now return `hookSpecificOutput.additional
    2026-06-04 : Claude Code : Added `/plugin list` command to list installed plugins, with `--enabled`/`--disa
    2026-06-04 : Cursor : Custom tools
    2026-06-04 : Cursor : We've shipped a batch of new functionality across the TypeScript and Python SDKs
    2026-06-06 : Claude Code : Added glob pattern support in deny rule tool-name position (`"*"` denies all too
    2026-06-10 : Claude Code : Added a search bar when browsing a marketplace's plugins in `/plugin`
    2026-06-10 : Claude Code : Amazon Bedrock now reads the AWS region from `~/.aws` config files when `AWS_REG
    2026-06-15 : Claude Code : Skills in nested `.claude/skills` directories now load when working on files the
    2026-06-16 : Claude Code : Improved plugin loading performance in remote sessions
    2026-06-17 : ChatGPT : Monitoring tasks can search the web and check connected apps for changes and not
    2026-06-17 : Claude Code : Added `/config key=value` syntax to set any setting from the prompt (e.g. `/conf
    2026-06-18 : Cursor : An emoji trigger for Slack
    2026-06-19 : Claude Code : Added `attribution.sessionUrl` setting to omit the claude.ai session link from c
    2026-06-22 : Claude Code : Added a "Skills" section to the `/plugin` Installed tab
    2026-06-22 : Cursor : You can now add and manage plugins, skills, MCPs, subagents, rules, commands, an
    2026-06-22 : Cursor : Add any to your setup with one click from the new Customize page and extend Curs
    2026-06-22 : Cursor : Marketplace leaderboard
    2026-06-22 : Cursor : Plugins, skills, and MCPs let you customize Cursor for your workflows. The new C
    2026-06-23 : Claude Code : Improved `/install-github-app`: GitHub Actions workflow setup is now optional —
    2026-06-24 : Claude Code : Improved MCP error messages: HTTP 404 errors now show the URL and point to your
    2026-06-24 : Claude Code : Improved MCP server reliability: capability discovery (`tools/list`, `prompts/li
    2026-06-29 : Cursor : Remote Control
    2026-06-30 : Cursor : When an admin sets up Team MCP servers for cloud agents, they can make those sam
    2026-06-30 : Cursor : Admins can now configure Team MCP servers once and distribute them across cloud
    2026-07-01 : Claude Code : Claude in Chrome is now generally available
    2026-07-01 : Claude Code : Added `/dataviz` skill for chart and dashboard design guidance with a runnable c
    2026-07-02 : Claude Code : Stacked slash-skill invocations like `/skill-a /skill-b do XYZ` now load all lea
    2026-07-06 : Claude Code : Improved MCP error messages: clearer error when a server config has `url` but no
    2026-07-07 : Claude Code : Added the session's additional working directories to MCP `roots/list`, with `no
    2026-07-09 : ChatGPT : We’re also replacing the App Directory with the Plugin Directory. Existing app c
    2026-07-09 : ChatGPT : Enterprise and Edu users can find skills under Plugins in the sidebar, on the Sk
    2026-07-13 : ChatGPT : ChatGPT is also available on Kakao in South Korea and Viber in supported markets
    2026-07-15 : Claude Code : Hardened synced skill/plugin directory naming on Windows and kept CCR web fetch/
    2026-07-17 : Claude Code : MCP tool calls running longer than 2 minutes now move to the background automati
    2026-07-17 : Cursor : Cursor in Slack now shares a plan before it starts, runs in multi-repo environme
    2026-07-17 : Cursor : We also refined how Cursor's responses look in Slack. In-message buttons are gon
    2026-07-22 : Claude Code : Added HTTP status and error text to `claude mcp list` and `/mcp` when a server f
    2026-07-24 : Claude Code : Added `mcp_server_errors` to the headless stream-json init event, listing `--mcp
    2026-07-24 : Claude Code : Added `DirectoryAdded` hook that fires after `/add-dir` or the SDK `register_rep
```
<!-- chronolog:end -->

## Change Cards
<!-- chronolog:begin region="cards" -->
- 2023-03-23 ChatGPT: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|We are announcing experimental support for AI plugins in ChatGPT — tools designe]]
- 2023-03-23 ChatGPT: [[Changes/ChatGPT/2023-03-23-today-we-will-begin-extending-plugin-access-to-users-and-developers-from-our-wai|Today, we will begin extending plugin access to users and developers from our wa]]
- 2023-05-04 Cursor: [[Changes/Cursor/2023-05-04-one-click-extension-import-from-vs-code-beta-as-a-highly-requested-feature-we-re|One-Click Extension Import from VS Code (beta). As a highly requested feature, w]]
- 2023-05-12 ChatGPT: [[Changes/ChatGPT/2023-05-12-plugins-try-a-new-version-of-chatgpt-that-knows-when-and-how-to-use-third-party|Plugins: Try a new version of ChatGPT that knows when and how to use third-party]]
- 2023-05-12 ChatGPT: [[Changes/ChatGPT/2023-05-12-in-the-plugins-dropdown-click-plugin-store-to-install-and-enable-new-plugins|In the “Plugins” dropdown, click “Plugin Store” to install and enable new plugin]]
- 2023-05-17 Cursor: [[Changes/Cursor/2023-05-17-you-can-pin-custom-extensions-to-your-activity-bar-in-the-top-left|You can Pin custom extensions to your activity bar in the top left]]
- 2023-06-09 Cursor: [[Changes/Cursor/2023-06-09-you-can-now-have-the-ai-read-documentation-on-your-behalf-this-will-improve-it-s|You can now have the AI read documentation on your behalf! This will improve it']]
- 2023-06-16 Cursor: [[Changes/Cursor/2023-06-16-we-ve-added-support-for-using-your-azure-openai-credentials-also-small-improveme|We've added support for using your Azure OpenAI credentials. Also, small improve]]
- 2023-06-27 Cursor: [[Changes/Cursor/2023-06-27-cursor-deep-linking-works-now-so-you-should-be-able-to-log-in-to-extensions|cursor:// deep linking works now, so you should be able to log in to extensions]]
- 2023-06-27 Cursor: [[Changes/Cursor/2023-06-27-better-support-for-extensions-specifically-re-enables-the-welcomeview|Better support for extensions (specifically re-enables the welcomeView)]]
- 2023-07-03 Cursor: [[Changes/Cursor/2023-07-03-also-cursor-s-ai-will-now-use-popular-documentation-to-improve-the-answers-to-yo|Also, Cursor's AI will now use popular documentation to improve the answers to y]]
- 2023-07-07 Cursor: [[Changes/Cursor/2023-07-07-makes-it-clearer-which-docs-are-being-looked-at-by-the-ai|Makes it clearer which docs are being looked at by the AI]]
- 2023-07-07 Cursor: [[Changes/Cursor/2023-07-07-improved-the-add-new-doc-experience|Improved the "@Add new doc" experience]]
- 2023-07-07 Cursor: [[Changes/Cursor/2023-07-07-ai-will-respond-with-citations-when-you-reference-docs|AI will respond with citations when you reference docs]]
- 2023-07-28 Cursor: [[Changes/Cursor/2023-07-28-more-robust-extension-handling-you-can-now-use-pre-release-extensions-again|More robust extension handling. You can now use pre-release extensions again.]]
- 2023-09-08 Cursor: [[Changes/Cursor/2023-09-08-the-main-addition-in-this-update-is-better-docs-support-this-means-you-can-add-a|The main addition in this update is better docs support. This means you can add]]
- 2023-09-11 Cursor: [[Changes/Cursor/2023-09-11-we-serve-extensions-now-using-cursor-s-extension-marketplace|We serve extensions now using Cursor's Extension Marketplace]]
- 2023-09-17 Cursor: [[Changes/Cursor/2023-09-17-we-point-to-a-different-marketplace-for-downloading-extensions-and-use-a-fork-of|We point to a different marketplace for downloading extensions, and use a fork o]]
- 2023-10-20 Cursor: [[Changes/Cursor/2023-10-20-cursor-is-now-based-on-vs-code-1-83-1-this-ensures-that-the-newest-versions-of-a|Cursor is now based on VS Code 1.83.1. This ensures that the newest versions of]]
- 2023-11-06 ChatGPT: [[Changes/ChatGPT/2023-11-06-plus-and-enterprise-users-can-start-creating-gpts-this-week-later-this-month-we|Plus and Enterprise users can start creating GPTs this week. Later this month, w]]
- 2023-11-06 ChatGPT: [[Changes/ChatGPT/2023-11-06-you-can-now-create-custom-versions-of-chatgpt-that-combine-instructions-extra-kn|You can now create custom versions of ChatGPT that combine instructions, extra k]]
- 2023-11-15 Cursor: [[Changes/Cursor/2023-11-15-now-based-on-vs-code-1-84-2-notably-this-fixes-a-few-notebook-bugs-and-ensures-t|Now based on VS Code 1.84.2. Notably, this fixes a few notebook bugs, and ensure]]
- 2023-11-15 Cursor: [[Changes/Cursor/2023-11-15-cursor-is-now-based-on-vs-code-1-84-2-notably-this-fixes-a-few-notebook-bugs-and|Cursor is now based on VS Code 1.84.2. Notably, this fixes a few notebook bugs,]]
- 2023-12-16 Cursor: [[Changes/Cursor/2023-12-16-copilot-we-ve-continued-to-improve-the-copilot-ghost-text-experience-surprisingl|Copilot++: We've continued to improve the Copilot++ ghost text experience. Surpr]]
- 2024-01-10 ChatGPT: [[Changes/ChatGPT/2024-01-10-explore-gpts-at-chatgpt-com-gpts|Explore GPTs at chatgpt.com/gpts.]]
- 2024-01-10 ChatGPT: [[Changes/ChatGPT/2024-01-10-discover-what-s-trending-in-the-gpt-store|Discover what’s trending in the GPT Store]]
- 2024-01-15 Cursor: [[Changes/Cursor/2024-01-15-supports-newer-version-of-python-extension|Supports newer version of python extension]]
- 2024-01-25 Cursor: [[Changes/Cursor/2024-01-25-update-0-24-3-0-24-4-adds-ability-to-configure-openai-base-url-fixes-getcursor-c|UPDATE (0.24.3-0.24.4): Adds ability to configure OpenAI base URL, fixes getcurs]]
- 2024-05-16 ChatGPT: [[Changes/ChatGPT/2024-05-16-upload-the-latest-file-versions-directly-from-google-drive-microsoft-onedrive-pe|Upload the latest file versions directly from Google Drive, Microsoft OneDrive P]]
- 2024-07-03 Cursor: [[Changes/Cursor/2024-07-03-docs-management-go-to-cursor-settings-features-docs-to-re-index-your-docs|Docs management! Go to Cursor Settings > Features > Docs to re-index your docs.]]
- 2024-11-22 ChatGPT: [[Changes/ChatGPT/2024-11-22-recent-gpts-pinned-gpt-s-are-now-displayed-below-conversations|Recent GPTs & Pinned GPT's are now displayed below conversations]]
- 2025-02-19 Cursor: [[Changes/Cursor/2025-02-19-mcp-improved-reliability-and-quality-of-life-enhancements-for-building-mcp-serve|MCP: Improved reliability and quality of life enhancements for building MCP serv]]
- 2025-02-19 Cursor: [[Changes/Cursor/2025-02-19-0-46-2-improved-mcp-reliability-added-option-to-disable-yolo-mode-for-mcp|0.46.2: Improved MCP reliability, added option to disable yolo mode for MCP]]
- 2025-03-23 Cursor: [[Changes/Cursor/2025-03-23-projects-with-mcp-servers-will-now-prompt-users-to-enable-them|Projects with MCP servers will now prompt users to enable them]]
- 2025-05-15 ChatGPT: [[Changes/ChatGPT/2025-05-15-the-github-connector-is-now-available-globally-to-plus-pro-team-users-including|The GitHub connector is now available globally to Plus/Pro/Team users, including]]
- 2025-06-04 ChatGPT: [[Changes/ChatGPT/2025-06-04-supported-connectors-google-drive-sharepoint-dropbox-box-outlook-gmail-google-ca|Supported connectors: Google Drive, SharePoint, Dropbox, Box, Outlook, Gmail, Go]]
- 2025-06-04 ChatGPT: [[Changes/ChatGPT/2025-06-04-admin-published-connectors-appear-in-the-connector-list-for-all-users|Admin-published connectors appear in the connector list for all users]]
- 2025-06-04 ChatGPT: [[Changes/ChatGPT/2025-06-04-admins-and-users-can-now-build-and-deploy-custom-connectors-to-proprietary-syste|Admins and users can now build and deploy custom connectors to proprietary syste]]
- 2025-06-12 Cursor: [[Changes/Cursor/2025-06-12-mention-cursor-in-any-thread-with-a-prompt-like|Mention @Cursor in any thread with a prompt like:]]
- 2025-06-24 ChatGPT: [[Changes/ChatGPT/2025-06-24-pro-users-are-now-able-to-use-chat-search-connectors-in-addition-to-deep-researc|Pro users are now able to use chat search connectors (in addition to deep resear]]
- 2025-07-03 Cursor: [[Changes/Cursor/2025-07-03-to-dos-are-also-visible-in-slack-if-integration-is-setup|To-dos are also visible in Slack if integration is setup!]]
- 2025-07-03 Cursor: [[Changes/Cursor/2025-07-03-the-agent-breaks-down-longer-tasks-with-dependencies-visible-to-you-in-chat-and|The agent breaks down longer tasks with dependencies, visible to you in chat and]]
- 2025-07-24 ChatGPT: [[Changes/ChatGPT/2025-07-24-pro-users-can-now-utilize-chat-search-with-hubspot-and-custom-connectors-mcp-in|Pro users can now utilize chat search with HubSpot and custom connectors (MCP) i]]
- 2025-08-11 ChatGPT: [[Changes/ChatGPT/2025-08-11-note-connectors-for-plus-pro-plans-are-not-available-in-eea-switzerland-and-the|Note: Connectors for Plus/Pro plans are not available in EEA, Switzerland, and t]]
- 2025-08-11 ChatGPT: [[Changes/ChatGPT/2025-08-11-now-connect-even-more-tools-in-chatgpt-for-useful-relevant-responses-in-chat|Now connect even more tools in ChatGPT for useful, relevant responses in chat.]]
- 2025-08-13 ChatGPT: [[Changes/ChatGPT/2025-08-13-gmail-google-calendar-and-google-contacts-connectors-in-chatgpt-are-now-availabl|Gmail, Google Calendar, and Google Contacts Connectors in ChatGPT are now availa]]
- 2025-09-29 Cursor: [[Changes/Cursor/2025-09-29-browser-controls|Browser Controls]]
- 2025-10-09 ChatGPT: [[Changes/ChatGPT/2025-10-09-we-re-adding-notion-and-linear-as-synced-connectors-for-pro-users-so-you-can-sec|We're adding Notion and Linear as synced connectors (for Pro users), so you can]]
- 2025-10-13 ChatGPT: [[Changes/ChatGPT/2025-10-13-installing-the-app-requires-the-connector-to-be-enabled-for-your-account|Installing the app requires the connector to be enabled for your account.]]
- 2025-10-13 ChatGPT: [[Changes/ChatGPT/2025-10-13-we-re-rolling-out-two-new-ways-to-bring-slack-and-chatgpt-together-a-connector-t|We’re rolling out two new ways to bring Slack and ChatGPT together: a connector]]
- 2025-10-13 ChatGPT: [[Changes/ChatGPT/2025-10-13-both-app-and-connector-are-available-to-plus-pro-business-and-enterprise-edu-cus|Both app and connector are available to Plus, Pro, Business and Enterprise/Edu c]]
- 2025-10-13 ChatGPT: [[Changes/ChatGPT/2025-10-13-with-the-chatgpt-app-for-slack-you-can-chat-one-on-one-with-chatgpt-in-a-dedicat|With the ChatGPT app for Slack, you can chat one-on-one with ChatGPT in a dedica]]
- 2025-10-29 Cursor: [[Changes/Cursor/2025-10-29-browser-ga|Browser (GA)]]
- 2025-12-18 ChatGPT: [[Changes/ChatGPT/2025-12-18-you-can-now-browse-and-add-approved-apps-in-the-new-app-directory-apps-let-you-w|You can now browse and add approved apps in the new app directory. Apps let you]]
- 2025-12-19 Claude Code: [[Changes/Claude Code/2025-12-19-added-search-filtering-to-the-plugin-discover-screen-type-to-filter-by-name-desc|Added search filtering to the plugin discover screen (type to filter by name, de]]
- 2025-12-22 Cursor: [[Changes/Cursor/2025-12-22-improved-integrated-browser-to-support-opening-multiple-tabs|Improved integrated browser to support opening multiple tabs.]]
- 2025-12-22 Cursor: [[Changes/Cursor/2025-12-22-cursor-now-separates-processes-running-for-user-installed-extensions-and-built-i|Cursor now separates processes running for user-installed extensions and built-i]]
- 2026-01-08 Cursor: [[Changes/Cursor/2026-01-08-rules-generation-and-management|Rules generation and management]]
- 2026-01-08 Cursor: [[Changes/Cursor/2026-01-08-this-release-introduces-new-cli-controls-for-models-mcp-management-rules-and-com|This release introduces new CLI controls for models, MCP management, rules and c]]
- 2026-01-09 Claude Code: [[Changes/Claude Code/2026-01-09-added-force-autoupdate-plugins-environment-variable-to-allow-plugin-autoupdate-e|Added `FORCE_AUTOUPDATE_PLUGINS` environment variable to allow plugin autoupdate]]
- 2026-01-13 Claude Code: [[Changes/Claude Code/2026-01-13-added-automatic-discovery-of-skills-from-nested-claude-skills-directories-when-w|Added automatic discovery of skills from nested `.claude/skills` directories whe]]
- 2026-01-20 Claude Code: [[Changes/Claude Code/2026-01-20-added-support-for-pinning-plugins-to-specific-git-commit-shas-allowing-marketpla|Added support for pinning plugins to specific git commit SHAs, allowing marketpl]]
- 2026-01-20 Claude Code: [[Changes/Claude Code/2026-01-20-added-search-to-installed-plugins-list-type-to-filter-by-name-or-description|Added search to installed plugins list - type to filter by name or description]]
- 2026-01-22 Claude Code: [[Changes/Claude Code/2026-01-22-vscode-added-native-plugin-management-support|[VSCode] Added native plugin management support]]
- 2026-01-23 Claude Code: [[Changes/Claude Code/2026-01-23-changed-skills-without-additional-permissions-or-hooks-to-be-allowed-without-req|Changed skills without additional permissions or hooks to be allowed without req]]
- 2026-01-23 Claude Code: [[Changes/Claude Code/2026-01-23-sdk-added-replay-of-queued-command-attachment-messages-as-sdkusermessagereplay-e|[SDK] Added replay of `queued_command` attachment messages as `SDKUserMessageRep]]
- 2026-01-30 Claude Code: [[Changes/Claude Code/2026-01-30-vscode-enabled-claude-in-chrome-integration|VSCode: Enabled Claude in Chrome integration]]
- 2026-02-05 Claude Code: [[Changes/Claude Code/2026-02-05-skills-defined-in-claude-skills-within-additional-directories-add-dir-are-now-lo|Skills defined in `.claude/skills/` within additional directories (`--add-dir`)]]
- 2026-02-06 Claude Code: [[Changes/Claude Code/2026-02-06-added-plugin-name-to-skill-descriptions-and-skills-menu-for-better-discoverabili|Added plugin name to skill descriptions and `/skills` menu for better discoverab]]
- 2026-02-17 Claude Code: [[Changes/Claude Code/2026-02-17-added-support-for-reading-enabledplugins-and-extraknownmarketplaces-from-add-dir|Added support for reading `enabledPlugins` and `extraKnownMarketplaces` from `--]]
- 2026-02-17 Claude Code: [[Changes/Claude Code/2026-02-17-added-sdkratelimitinfo-and-sdkratelimitevent-types-to-the-sdk-enabling-consumers|Added `SDKRateLimitInfo` and `SDKRateLimitEvent` types to the SDK, enabling cons]]
- 2026-02-17 Cursor: [[Changes/Cursor/2026-02-17-plugins-package-skills-subagents-mcp-servers-hooks-and-rules-into-a-single-insta|Plugins package skills, subagents, MCP servers, hooks, and rules, into a single]]
- 2026-02-17 Cursor: [[Changes/Cursor/2026-02-17-plugins-on-the-cursor-marketplace|Plugins on the Cursor Marketplace]]
- 2026-02-17 Cursor: [[Changes/Cursor/2026-02-17-browse-plugins-at-cursor-com-marketplace-or-install-directly-in-the-editor-with|Browse plugins at cursor.com/marketplace or install directly in the editor with]]
- 2026-02-17 Cursor: [[Changes/Cursor/2026-02-17-our-initial-partners-include-amplitude-aws-figma-linear-stripe-and-more-these-pl|Our initial partners include Amplitude, AWS, Figma, Linear, Stripe, and more. Th]]
- 2026-02-19 ChatGPT: [[Changes/ChatGPT/2026-02-19-preview-diagrams-and-mini-apps-directly-in-chat|Preview diagrams and mini apps directly in chat]]
- 2026-02-20 Claude Code: [[Changes/Claude Code/2026-02-20-claude-code-simple-mode-now-also-disables-mcp-tools-attachments-hooks-and-claude|`CLAUDE_CODE_SIMPLE` mode now also disables MCP tools, attachments, hooks, and C]]
- 2026-02-24 Claude Code: [[Changes/Claude Code/2026-02-24-added-support-for-custom-npm-registries-and-specific-version-pinning-when-instal|Added support for custom npm registries and specific version pinning when instal]]
- 2026-02-24 Claude Code: [[Changes/Claude Code/2026-02-24-added-claude-remote-control-subcommand-for-external-builds-enabling-local-enviro|Added `claude remote-control` subcommand for external builds, enabling local env]]
- 2026-02-24 Claude Code: [[Changes/Claude Code/2026-02-24-updated-plugin-marketplace-default-git-timeout-from-30s-to-120s-and-added-claude|Updated plugin marketplace default git timeout from 30s to 120s and added `CLAUD]]
- 2026-02-25 ChatGPT: [[Changes/ChatGPT/2026-02-25-additionally-use-connected-apps-directly-in-chats|Additionally, use connected apps directly in chats.]]
- 2026-02-25 ChatGPT: [[Changes/ChatGPT/2026-02-25-sources-from-apps-paste-a-link-to-a-slack-channel-or-google-drive-file-or-folder|Sources from apps: Paste a link to a Slack channel or Google Drive file or folde]]
- 2026-02-25 Claude Code: [[Changes/Claude Code/2026-02-25-expand-remote-control-to-more-users|Expand Remote Control to more users]]
- 2026-02-28 Claude Code: [[Changes/Claude Code/2026-02-28-added-enable-claudeai-mcp-servers-false-env-var-to-opt-out-from-making-claude-ai|Added `ENABLE_CLAUDEAI_MCP_SERVERS=false` env var to opt out from making claude.]]
- 2026-03-03 Cursor: [[Changes/Cursor/2026-03-03-mcp-apps-support-interactive-user-interfaces-like-charts-from-amplitude-diagrams|MCP Apps support interactive user interfaces like charts from Amplitude, diagram]]
- 2026-03-05 Claude Code: [[Changes/Claude Code/2026-03-05-added-the-claude-api-skill-for-building-applications-with-the-claude-api-and-ant|Added the `/claude-api` skill for building applications with the Claude API and]]
- 2026-03-05 Claude Code: [[Changes/Claude Code/2026-03-05-added-optional-name-argument-to-remote-control-and-claude-remote-control-remote|Added optional name argument to `/remote-control` and `claude remote-control` (`]]
- 2026-03-06 Claude Code: [[Changes/Claude Code/2026-03-06-reduced-remote-control-poll-rate-to-once-per-10-minutes-while-connected-was-1-2s|Reduced Remote Control `/poll` rate to once per 10 minutes while connected (was]]
- 2026-03-10 Claude Code: [[Changes/Claude Code/2026-03-10-changed-tool-search-to-bypass-the-third-party-proxy-gate-when-the-environment-va|Changed tool search to bypass the third-party proxy gate when the environment va]]
- 2026-03-10 Claude Code: [[Changes/Claude Code/2026-03-10-added-claude-plugins-as-an-alias-for-claude-plugin|Added `claude plugins` as an alias for `claude plugin`]]
- 2026-03-11 Cursor: [[Changes/Cursor/2026-03-11-try-out-the-new-plugins-at-cursor-com-marketplace-or-read-more-in-our-announceme|Try out the new plugins at cursor.com/marketplace, or read more in our announcem]]
- 2026-03-11 Cursor: [[Changes/Cursor/2026-03-11-we-ve-added-more-than-30-new-plugins-from-partners-such-as-atlassian-datadog-git|We've added more than 30 new plugins from partners such as Atlassian, Datadog, G]]
- 2026-03-12 Claude Code: [[Changes/Claude Code/2026-03-12-changed-plugin-dir-so-local-dev-copies-now-override-installed-marketplace-plugin|Changed `--plugin-dir` so local dev copies now override installed marketplace pl]]
- 2026-03-14 Claude Code: [[Changes/Claude Code/2026-03-14-added-new-elicitation-and-elicitationresult-hooks-to-intercept-and-override-resp|Added new `Elicitation` and `ElicitationResult` hooks to intercept and override]]
- 2026-03-14 Claude Code: [[Changes/Claude Code/2026-03-14-added-mcp-elicitation-support-mcp-servers-can-now-request-structured-input-mid-t|Added MCP elicitation support — MCP servers can now request structured input mid]]
- 2026-03-17 Claude Code: [[Changes/Claude Code/2026-03-17-added-stopfailure-hook-event-that-fires-when-the-turn-ends-due-to-an-api-error-r|Added `StopFailure` hook event that fires when the turn ends due to an API error]]
- 2026-03-17 Claude Code: [[Changes/Claude Code/2026-03-17-added-effort-maxturns-and-disallowedtools-frontmatter-support-for-plugin-shipped|Added `effort`, `maxTurns`, and `disallowedTools` frontmatter support for plugin]]
- 2026-03-17 Claude Code: [[Changes/Claude Code/2026-03-17-added-claude-plugin-data-variable-for-plugin-persistent-state-that-survives-plug|Added `${CLAUDE_PLUGIN_DATA}` variable for plugin persistent state that survives]]
- 2026-03-19 Claude Code: [[Changes/Claude Code/2026-03-19-added-source-settings-plugin-marketplace-source-declare-plugin-entries-inline-in|Added `source: 'settings'` plugin marketplace source — declare plugin entries in]]
- 2026-03-19 Claude Code: [[Changes/Claude Code/2026-03-19-added-channels-research-preview-allow-mcp-servers-to-push-messages-into-your-ses|Added `--channels` (research preview) — allow MCP servers to push messages into]]
- 2026-03-19 Claude Code: [[Changes/Claude Code/2026-03-19-added-cli-tool-usage-detection-to-plugin-tips-in-addition-to-file-pattern-matchi|Added CLI tool usage detection to plugin tips, in addition to file pattern match]]
- 2026-03-20 Claude Code: [[Changes/Claude Code/2026-03-20-improved-mcp-read-search-tool-calls-to-collapse-into-a-single-queried-server-lin|Improved MCP read/search tool calls to collapse into a single "Queried {server}"]]
- 2026-03-25 ChatGPT: [[Changes/ChatGPT/2026-03-25-google-s-file-connectors-in-chatgpt-are-now-unified-under-google-drive-providing|Google’s file connectors in ChatGPT are now unified under Google Drive, providin]]
- 2026-03-25 Claude Code: [[Changes/Claude Code/2026-03-25-added-claude-code-subprocess-env-scrub-1-to-strip-anthropic-and-cloud-provider-c|Added `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` to strip Anthropic and cloud provider]]
- 2026-03-25 Claude Code: [[Changes/Claude Code/2026-03-25-added-disabledeeplinkregistration-setting-to-prevent-claude-cli-protocol-handler|Added `disableDeepLinkRegistration` setting to prevent `claude-cli://` protocol]]
- 2026-03-25 Claude Code: [[Changes/Claude Code/2026-03-25-added-cwdchanged-and-filechanged-hook-events-for-reactive-environment-management|Added `CwdChanged` and `FileChanged` hook events for reactive environment manage]]
- 2026-03-26 Claude Code: [[Changes/Claude Code/2026-03-26-added-claude-code-mcp-server-name-and-claude-code-mcp-server-url-environment-var|Added `CLAUDE_CODE_MCP_SERVER_NAME` and `CLAUDE_CODE_MCP_SERVER_URL` environment]]
- 2026-03-26 Claude Code: [[Changes/Claude Code/2026-03-26-deep-link-queries-claude-cli-open-q-now-support-up-to-5-000-characters-with-a-sc|Deep link queries (`claude-cli://open?q=…`) now support up to 5,000 characters,]]
- 2026-03-27 ChatGPT: [[Changes/ChatGPT/2026-03-27-we-re-rolling-out-updated-box-notion-linear-and-dropbox-apps-in-chatgpt-these-up|We’re rolling out updated Box, Notion, Linear, and Dropbox apps in ChatGPT. Thes]]
- 2026-03-27 ChatGPT: [[Changes/ChatGPT/2026-03-27-if-you-already-use-these-apps-in-chatgpt-reconnect-the-app-to-start-using-the-up|If you already use these apps in ChatGPT, reconnect the app to start using the u]]
- 2026-03-27 Claude Code: [[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|Reduced startup event-loop stalls when many claude.ai MCP connectors are configu]]
- 2026-04-01 Claude Code: [[Changes/Claude Code/2026-04-01-added-mcp-connection-nonblocking-true-for-p-mode-to-skip-the-mcp-connection-wait|Added `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode to skip the MCP connection]]
- 2026-04-01 Claude Code: [[Changes/Claude Code/2026-04-01-added-claude-code-plugin-keep-marketplace-on-failure-env-var-to-keep-the-existin|Added `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE` env var to keep the exist]]
- 2026-04-02 Claude Code: [[Changes/Claude Code/2026-04-02-added-support-for-multi-line-prompts-in-claude-cli-open-q-deep-links-encoded-new|Added support for multi-line prompts in `claude-cli://open?q=` deep links (encod]]
- 2026-04-02 Claude Code: [[Changes/Claude Code/2026-04-02-added-mcp-tool-result-persistence-override-via-meta-anthropic-maxresultsizechars|Added MCP tool result persistence override via `_meta["anthropic/maxResultSizeCh]]
- 2026-04-02 Claude Code: [[Changes/Claude Code/2026-04-02-added-disableskillshellexecution-setting-to-disable-inline-shell-execution-in-sk|Added `disableSkillShellExecution` setting to disable inline shell execution in]]
- 2026-04-02 Claude Code: [[Changes/Claude Code/2026-04-02-plugins-can-now-ship-executables-under-bin-and-invoke-them-as-bare-commands-from|Plugins can now ship executables under `bin/` and invoke them as bare commands f]]
- 2026-04-04 Claude Code: [[Changes/Claude Code/2026-04-04-remote-control-session-names-now-use-your-hostname-as-the-default-prefix-e-g-myh|Remote Control session names now use your hostname as the default prefix (e.g. `]]
- 2026-04-07 Claude Code: [[Changes/Claude Code/2026-04-07-added-hookspecificoutput-sessiontitle-to-userpromptsubmit-hooks-for-setting-the|Added `hookSpecificOutput.sessionTitle` to `UserPromptSubmit` hooks for setting]]
- 2026-04-07 Claude Code: [[Changes/Claude Code/2026-04-07-added-support-for-amazon-bedrock-powered-by-mantle-set-claude-code-use-mantle-1|Added support for Amazon Bedrock powered by Mantle, set `CLAUDE_CODE_USE_MANTLE=]]
- 2026-04-07 Claude Code: [[Changes/Claude Code/2026-04-07-added-compact-slacked-channel-header-with-a-clickable-channel-link-for-slack-mcp|Added compact `Slacked #channel` header with a clickable channel link for Slack]]
- 2026-04-07 Claude Code: [[Changes/Claude Code/2026-04-07-added-keep-coding-instructions-frontmatter-field-support-for-plugin-output-style|Added `keep-coding-instructions` frontmatter field support for plugin output sty]]
- 2026-04-08 Cursor: [[Changes/Cursor/2026-04-08-bugbot-mcp-support|Bugbot MCP Support]]
- 2026-04-08 Cursor: [[Changes/Cursor/2026-04-08-bugbot-learned-rules|Bugbot Learned Rules]]
- 2026-04-08 Cursor: [[Changes/Cursor/2026-04-08-it-looks-at-reactions-and-replies-to-bugbot-comments-and-comments-from-human-rev|It looks at reactions and replies to Bugbot comments and comments from human rev]]
- 2026-04-08 Cursor: [[Changes/Cursor/2026-04-08-this-release-introduces-updates-to-bugbot-including-the-ability-to-self-improve|This release introduces updates to Bugbot including the ability to self-improve]]
- 2026-04-13 Claude Code: [[Changes/Claude Code/2026-04-13-added-background-monitor-support-for-plugins-via-a-top-level-monitors-manifest-k|Added background monitor support for plugins via a top-level `monitors` manifest]]
- 2026-04-13 Claude Code: [[Changes/Claude Code/2026-04-13-added-precompact-hook-support-hooks-can-now-block-compaction-by-exiting-with-cod|Added PreCompact hook support: hooks can now block compaction by exiting with co]]
- 2026-04-20 Claude Code: [[Changes/Claude Code/2026-04-20-faster-mcp-startup-when-multiple-stdio-servers-are-configured-resources-template|Faster MCP startup when multiple stdio servers are configured; `resources/templa]]
- 2026-04-22 Claude Code: [[Changes/Claude Code/2026-04-22-faster-startup-when-both-local-and-claude-ai-mcp-servers-are-configured-concurre|Faster startup when both local and claude.ai MCP servers are configured (concurr]]
- 2026-04-23 Claude Code: [[Changes/Claude Code/2026-04-23-create-and-switch-between-named-custom-themes-from-theme-or-hand-edit-json-files|Create and switch between named custom themes from `/theme`, or hand-edit JSON f]]
- 2026-04-23 Claude Code: [[Changes/Claude Code/2026-04-23-hooks-can-now-invoke-mcp-tools-directly-via-type-mcp-tool|Hooks can now invoke MCP tools directly via `type: "mcp_tool"`]]
- 2026-04-28 Claude Code: [[Changes/Claude Code/2026-04-28-added-claude-plugin-prune-to-remove-orphaned-auto-installed-plugin-dependencies|Added `claude plugin prune` to remove orphaned auto-installed plugin dependencie]]
- 2026-04-28 Claude Code: [[Changes/Claude Code/2026-04-28-added-anthropic-bedrock-service-tier-environment-variable-to-select-a-bedrock-se|Added `ANTHROPIC_BEDROCK_SERVICE_TIER` environment variable to select a Bedrock]]
- 2026-04-28 Claude Code: [[Changes/Claude Code/2026-04-28-mcp-now-shows-claude-ai-connectors-hidden-by-a-manually-added-server-with-the-sa|`/mcp` now shows claude.ai connectors hidden by a manually-added server with the]]
- 2026-04-28 Claude Code: [[Changes/Claude Code/2026-04-28-added-alwaysload-option-to-mcp-server-config-when-true-all-tools-from-that-serve|Added `alwaysLoad` option to MCP server config — when `true`, all tools from tha]]
- 2026-04-28 Claude Code: [[Changes/Claude Code/2026-04-28-posttooluse-hooks-can-now-replace-tool-output-for-all-tools-via-hookspecificoutp|PostToolUse hooks can now replace tool output for all tools via `hookSpecificOut]]
- 2026-04-29 Cursor: [[Changes/Cursor/2026-04-29-we-re-introducing-the-cursor-sdk-so-you-can-build-agents-with-the-same-runtime-h|We're introducing the Cursor SDK so you can build agents with the same runtime,]]
- 2026-04-29 Cursor: [[Changes/Cursor/2026-04-29-run-npm-install-cursor-sdk-to-get-started-you-can-also-use-cursor-s-native-sdk-s|Run npm install @cursor/sdk to get started. You can also use Cursor's native /sd]]
- 2026-05-01 Cursor: [[Changes/Cursor/2026-05-01-plugins-bundle-capabilities-like-mcp-servers-skills-subagents-rules-and-hooks-th|Plugins bundle capabilities like MCP servers, skills, subagents, rules, and hook]]
- 2026-05-01 Cursor: [[Changes/Cursor/2026-05-01-required-users-always-have-the-plugin-and-cannot-uninstall-it|Required: users always have the plugin and cannot uninstall it]]
- 2026-05-01 Cursor: [[Changes/Cursor/2026-05-01-default-on-users-get-the-plugin-installed-by-default-but-can-opt-out|Default On: users get the plugin installed by default, but can opt out]]
- 2026-05-04 Claude Code: [[Changes/Claude Code/2026-05-04-plugin-dir-now-accepts-zip-plugin-archives-in-addition-to-directories|`--plugin-dir` now accepts `.zip` plugin archives in addition to directories]]
- 2026-05-04 Claude Code: [[Changes/Claude Code/2026-05-04-mcp-now-shows-the-tool-count-for-connected-servers-and-flags-servers-that-connec|`/mcp` now shows the tool count for connected servers and flags servers that con]]
- 2026-05-06 Claude Code: [[Changes/Claude Code/2026-05-06-plugin-manifests-themes-and-monitors-should-now-be-declared-under-experimental-t|Plugin manifests: `themes` and `monitors` should now be declared under `"experim]]
- 2026-05-06 Claude Code: [[Changes/Claude Code/2026-05-06-added-claude-code-session-id-environment-variable-to-the-bash-tool-subprocess-en|Added `CLAUDE_CODE_SESSION_ID` environment variable to the Bash tool subprocess]]
- 2026-05-06 Claude Code: [[Changes/Claude Code/2026-05-06-added-plugin-url-url-flag-to-fetch-a-plugin-zip-archive-from-a-url-for-the-curre|Added `--plugin-url <url>` flag to fetch a plugin `.zip` archive from a URL for]]
- 2026-05-07 Claude Code: [[Changes/Claude Code/2026-05-07-hooks-now-receive-the-active-effort-level-via-the-effort-level-json-input-field|Hooks now receive the active effort level via the `effort.level` JSON input fiel]]
- 2026-05-11 Claude Code: [[Changes/Claude Code/2026-05-11-added-claude-plugin-details-name-to-show-a-plugin-s-component-inventory-and-proj|Added `claude plugin details <name>` to show a plugin's component inventory and]]
- 2026-05-11 Claude Code: [[Changes/Claude Code/2026-05-11-added-goal-command-set-a-completion-condition-and-claude-keeps-working-across-tu|Added `/goal` command: set a completion condition and Claude keeps working acros]]
- 2026-05-11 Cursor: [[Changes/Cursor/2026-05-11-get-started-by-installing-the-integration-in-the-cursor-dashboard-learn-more-in|Get started by installing the integration in the Cursor dashboard. Learn more in]]
- 2026-05-12 Claude Code: [[Changes/Claude Code/2026-05-12-plugins-now-warn-when-a-default-component-folder-e-g-commands-is-silently-ignore|Plugins now warn when a default component folder (e.g. `commands/`) is silently]]
- 2026-05-13 Claude Code: [[Changes/Claude Code/2026-05-13-added-terminalsequence-field-to-hook-json-output-so-hooks-can-emit-desktop-notif|Added `terminalSequence` field to hook JSON output so hooks can emit desktop not]]
- 2026-05-13 Claude Code: [[Changes/Claude Code/2026-05-13-added-claude-code-plugin-prefer-https-to-clone-github-plugin-sources-over-https|Added `CLAUDE_CODE_PLUGIN_PREFER_HTTPS` to clone GitHub plugin sources over HTTP]]
- 2026-05-14 Claude Code: [[Changes/Claude Code/2026-05-14-plugins-with-a-root-level-skill-md-and-no-skills-subdirectory-are-now-surfaced-a|Plugins with a root-level `SKILL.md` and no `skills/` subdirectory are now surfa]]
- 2026-05-14 Claude Code: [[Changes/Claude Code/2026-05-14-the-plugin-details-pane-and-claude-plugin-details-now-show-lsp-servers-a-plugin|The `/plugin` details pane and `claude plugin details` now show LSP servers a pl]]
- 2026-05-14 Claude Code: [[Changes/Claude Code/2026-05-14-web-setup-warns-before-replacing-an-existing-github-app-connection|`/web-setup` warns before replacing an existing GitHub App connection]]
- 2026-05-15 Claude Code: [[Changes/Claude Code/2026-05-15-added-plugin-dependency-enforcement-claude-plugin-disable-now-refuses-when-anoth|Added plugin dependency enforcement: `claude plugin disable` now refuses when an]]
- 2026-05-19 Claude Code: [[Changes/Claude Code/2026-05-19-plugin-discover-and-browse-screens-now-show-a-plugin-s-commands-agents-skills-ho|`/plugin` Discover and Browse screens now show a plugin's commands, agents, skil]]
- 2026-05-19 Cursor: [[Changes/Cursor/2026-05-19-cursor-is-now-available-in-jira|Cursor is now available in Jira.]]
- 2026-05-19 Cursor: [[Changes/Cursor/2026-05-19-you-can-ask-cursor-to-fix-bugs-add-features-update-tests-or-investigate-somethin|You can ask Cursor to fix bugs, add features, update tests, or investigate somet]]
- 2026-05-19 Cursor: [[Changes/Cursor/2026-05-19-install-the-integration-from-cursor-integrations-you-need-cursor-admin-access-an|Install the integration from Cursor integrations. You need Cursor admin access a]]
- 2026-05-22 Claude Code: [[Changes/Claude Code/2026-05-22-usage-now-shows-a-per-category-breakdown-of-what-s-driving-your-limits-usage-ski|`/usage` now shows a per-category breakdown of what's driving your limits usage]]
- 2026-05-22 Claude Code: [[Changes/Claude Code/2026-05-22-enterprise-added-the-allowallclaudeaimcps-managed-setting-to-load-claude-ai-clou|Enterprise: added the `allowAllClaudeAiMcps` managed setting to load claude.ai c]]
- 2026-05-27 Claude Code: [[Changes/Claude Code/2026-05-27-sessionstart-hooks-can-now-set-the-session-title-via-hookspecificoutput-sessiont|`SessionStart` hooks can now set the session title via `hookSpecificOutput.sessi]]
- 2026-05-27 Claude Code: [[Changes/Claude Code/2026-05-27-sessionstart-hooks-can-now-return-reloadskills-true-to-re-scan-skill-directories|`SessionStart` hooks can now return `reloadSkills: true` to re-scan skill direct]]
- 2026-05-28 Claude Code: [[Changes/Claude Code/2026-05-28-added-skiplfs-option-to-github-git-plugin-marketplace-sources-to-skip-git-lfs-do|Added `skipLfs` option to `github`/`git` plugin marketplace sources to skip Git]]
- 2026-05-29 Claude Code: [[Changes/Claude Code/2026-05-29-added-claude-plugin-init-name-to-scaffold-a-new-plugin-in-claude-skills|Added `claude plugin init <name>` to scaffold a new plugin in `.claude/skills`]]
- 2026-05-29 Claude Code: [[Changes/Claude Code/2026-05-29-plugins-in-claude-skills-directories-are-now-automatically-loaded-no-marketplace|Plugins in `.claude/skills` directories are now automatically loaded, no marketp]]
- 2026-05-29 Claude Code: [[Changes/Claude Code/2026-05-29-added-autocomplete-for-plugin-arguments-subcommands-installed-plugin-names-and-p|Added autocomplete for `/plugin` arguments: subcommands, installed plugin names,]]
- 2026-06-02 Claude Code: [[Changes/Claude Code/2026-06-02-mcp-now-collapses-claude-ai-connectors-you-ve-never-signed-in-to-behind-a-show-u|`/mcp` now collapses claude.ai connectors you've never signed in to behind a "Sh]]
- 2026-06-03 Claude Code: [[Changes/Claude Code/2026-06-03-remote-control-now-shows-as-a-persistent-footer-pill-with-a-link-to-the-session|Remote Control now shows as a persistent footer pill (with a link to the session]]
- 2026-06-04 Claude Code: [[Changes/Claude Code/2026-06-04-hooks-stop-and-subagentstop-hooks-can-now-return-hookspecificoutput-additionalco|Hooks: Stop and SubagentStop hooks can now return `hookSpecificOutput.additional]]
- 2026-06-04 Claude Code: [[Changes/Claude Code/2026-06-04-added-plugin-list-command-to-list-installed-plugins-with-enabled-disabled-filter|Added `/plugin list` command to list installed plugins, with `--enabled`/`--disa]]
- 2026-06-04 Cursor: [[Changes/Cursor/2026-06-04-custom-tools|Custom tools]]
- 2026-06-04 Cursor: [[Changes/Cursor/2026-06-04-we-ve-shipped-a-batch-of-new-functionality-across-the-typescript-and-python-sdks|We've shipped a batch of new functionality across the TypeScript and Python SDKs]]
- 2026-06-06 Claude Code: [[Changes/Claude Code/2026-06-06-added-glob-pattern-support-in-deny-rule-tool-name-position-denies-all-tools-allo|Added glob pattern support in deny rule tool-name position (`"*"` denies all too]]
- 2026-06-10 Claude Code: [[Changes/Claude Code/2026-06-10-added-a-search-bar-when-browsing-a-marketplace-s-plugins-in-plugin|Added a search bar when browsing a marketplace's plugins in `/plugin`]]
- 2026-06-10 Claude Code: [[Changes/Claude Code/2026-06-10-amazon-bedrock-now-reads-the-aws-region-from-aws-config-files-when-aws-region-is|Amazon Bedrock now reads the AWS region from `~/.aws` config files when `AWS_REG]]
- 2026-06-15 Claude Code: [[Changes/Claude Code/2026-06-15-skills-in-nested-claude-skills-directories-now-load-when-working-on-files-there|Skills in nested `.claude/skills` directories now load when working on files the]]
- 2026-06-16 Claude Code: [[Changes/Claude Code/2026-06-16-improved-plugin-loading-performance-in-remote-sessions|Improved plugin loading performance in remote sessions]]
- 2026-06-17 ChatGPT: [[Changes/ChatGPT/2026-06-17-monitoring-tasks-can-search-the-web-and-check-connected-apps-for-changes-and-not|Monitoring tasks can search the web and check connected apps for changes and not]]
- 2026-06-17 Claude Code: [[Changes/Claude Code/2026-06-17-added-config-key-value-syntax-to-set-any-setting-from-the-prompt-e-g-config-thin|Added `/config key=value` syntax to set any setting from the prompt (e.g. `/conf]]
- 2026-06-18 Cursor: [[Changes/Cursor/2026-06-18-an-emoji-trigger-for-slack|An emoji trigger for Slack]]
- 2026-06-19 Claude Code: [[Changes/Claude Code/2026-06-19-added-attribution-sessionurl-setting-to-omit-the-claude-ai-session-link-from-com|Added `attribution.sessionUrl` setting to omit the claude.ai session link from c]]
- 2026-06-22 Claude Code: [[Changes/Claude Code/2026-06-22-added-a-skills-section-to-the-plugin-installed-tab|Added a "Skills" section to the `/plugin` Installed tab]]
- 2026-06-22 Cursor: [[Changes/Cursor/2026-06-22-you-can-now-add-and-manage-plugins-skills-mcps-subagents-rules-commands-and-hook|You can now add and manage plugins, skills, MCPs, subagents, rules, commands, an]]
- 2026-06-22 Cursor: [[Changes/Cursor/2026-06-22-add-any-to-your-setup-with-one-click-from-the-new-customize-page-and-extend-curs|Add any to your setup with one click from the new Customize page and extend Curs]]
- 2026-06-22 Cursor: [[Changes/Cursor/2026-06-22-marketplace-leaderboard|Marketplace leaderboard]]
- 2026-06-22 Cursor: [[Changes/Cursor/2026-06-22-plugins-skills-and-mcps-let-you-customize-cursor-for-your-workflows-the-new-cust|Plugins, skills, and MCPs let you customize Cursor for your workflows. The new C]]
- 2026-06-23 Claude Code: [[Changes/Claude Code/2026-06-23-improved-install-github-app-github-actions-workflow-setup-is-now-optional-you-ca|Improved `/install-github-app`: GitHub Actions workflow setup is now optional —]]
- 2026-06-24 Claude Code: [[Changes/Claude Code/2026-06-24-improved-mcp-error-messages-http-404-errors-now-show-the-url-and-point-to-your-m|Improved MCP error messages: HTTP 404 errors now show the URL and point to your]]
- 2026-06-24 Claude Code: [[Changes/Claude Code/2026-06-24-improved-mcp-server-reliability-capability-discovery-tools-list-prompts-list-res|Improved MCP server reliability: capability discovery (`tools/list`, `prompts/li]]
- 2026-06-29 Cursor: [[Changes/Cursor/2026-06-29-remote-control|Remote Control]]
- 2026-06-30 Cursor: [[Changes/Cursor/2026-06-30-when-an-admin-sets-up-team-mcp-servers-for-cloud-agents-they-can-make-those-same|When an admin sets up Team MCP servers for cloud agents, they can make those sam]]
- 2026-06-30 Cursor: [[Changes/Cursor/2026-06-30-admins-can-now-configure-team-mcp-servers-once-and-distribute-them-across-cloud|Admins can now configure Team MCP servers once and distribute them across cloud]]
- 2026-07-01 Claude Code: [[Changes/Claude Code/2026-07-01-claude-in-chrome-is-now-generally-available|Claude in Chrome is now generally available]]
- 2026-07-01 Claude Code: [[Changes/Claude Code/2026-07-01-added-dataviz-skill-for-chart-and-dashboard-design-guidance-with-a-runnable-colo|Added `/dataviz` skill for chart and dashboard design guidance with a runnable c]]
- 2026-07-02 Claude Code: [[Changes/Claude Code/2026-07-02-stacked-slash-skill-invocations-like-skill-a-skill-b-do-xyz-now-load-all-leading|Stacked slash-skill invocations like `/skill-a /skill-b do XYZ` now load all lea]]
- 2026-07-06 Claude Code: [[Changes/Claude Code/2026-07-06-improved-mcp-error-messages-clearer-error-when-a-server-config-has-url-but-no-ty|Improved MCP error messages: clearer error when a server config has `url` but no]]
- 2026-07-07 Claude Code: [[Changes/Claude Code/2026-07-07-added-the-session-s-additional-working-directories-to-mcp-roots-list-with-notifi|Added the session's additional working directories to MCP `roots/list`, with `no]]
- 2026-07-09 ChatGPT: [[Changes/ChatGPT/2026-07-09-we-re-also-replacing-the-app-directory-with-the-plugin-directory-existing-app-co|We’re also replacing the App Directory with the Plugin Directory. Existing app c]]
- 2026-07-09 ChatGPT: [[Changes/ChatGPT/2026-07-09-enterprise-and-edu-users-can-find-skills-under-plugins-in-the-sidebar-on-the-ski|Enterprise and Edu users can find skills under Plugins in the sidebar, on the Sk]]
- 2026-07-13 ChatGPT: [[Changes/ChatGPT/2026-07-13-chatgpt-is-also-available-on-kakao-in-south-korea-and-viber-in-supported-markets|ChatGPT is also available on Kakao in South Korea and Viber in supported markets]]
- 2026-07-15 Claude Code: [[Changes/Claude Code/2026-07-15-hardened-synced-skill-plugin-directory-naming-on-windows-and-kept-ccr-web-fetch|Hardened synced skill/plugin directory naming on Windows and kept CCR web fetch/]]
- 2026-07-17 Claude Code: [[Changes/Claude Code/2026-07-17-mcp-tool-calls-running-longer-than-2-minutes-now-move-to-the-background-automati|MCP tool calls running longer than 2 minutes now move to the background automati]]
- 2026-07-17 Cursor: [[Changes/Cursor/2026-07-17-cursor-in-slack-now-shares-a-plan-before-it-starts-runs-in-multi-repo-environmen|Cursor in Slack now shares a plan before it starts, runs in multi-repo environme]]
- 2026-07-17 Cursor: [[Changes/Cursor/2026-07-17-we-also-refined-how-cursor-s-responses-look-in-slack-in-message-buttons-are-gone|We also refined how Cursor's responses look in Slack. In-message buttons are gon]]
- 2026-07-22 Claude Code: [[Changes/Claude Code/2026-07-22-added-http-status-and-error-text-to-claude-mcp-list-and-mcp-when-a-server-fails|Added HTTP status and error text to `claude mcp list` and `/mcp` when a server f]]
- 2026-07-24 Claude Code: [[Changes/Claude Code/2026-07-24-added-mcp-server-errors-to-the-headless-stream-json-init-event-listing-mcp-confi|Added `mcp_server_errors` to the headless stream-json init event, listing `--mcp]]
- 2026-07-24 Claude Code: [[Changes/Claude Code/2026-07-24-added-directoryadded-hook-that-fires-after-add-dir-or-the-sdk-register-repo-root|Added `DirectoryAdded` hook that fires after `/add-dir` or the SDK `register_rep]]
<!-- chronolog:end -->