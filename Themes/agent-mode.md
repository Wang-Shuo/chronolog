---
created: '2023-07-06'
date: '2026-07-28'
machine_hash: 1ccce1643e5abc540cbff1fb78924cf71ede0874f388ae64204d596e937adea4
modified: '2026-07-28'
products_involved:
- ChatGPT
- Claude Code
- Cursor
status: official
tags:
- theme
- moc
theme: agent-mode
---

# Theme: agent-mode

## Cross-Product Timeline
<!-- chronolog:begin region="timeline" -->
```mermaid
timeline
    title agent-mode
    2023-07-06 : Cursor : Welcome to the first nightly release! It comes with agents, which we aren't rele
    2023-07-10 : Cursor : This nightly build comes with experimental interface agent support!
    2023-07-10 : Cursor : The goal: you write an interface specification, and an agent writes both the tes
    2024-02-15 : Cursor : Interpreter Mode: We've made some big improvements to the backend powering inter
    2024-08-02 : Cursor : Concurrent composers support, composer control panel, and various bug fixes such
    2024-12-17 : Cursor : Agent auto-saves changes to disk
    2024-12-17 : Cursor : @docs, @git, @web, and @folder are now available in the agent
    2025-01-23 : Cursor : Agent sees recent changes: The agent can use a tool to see your recent changes.
    2025-01-23 : Cursor : .cursor/rules: Users can write several repository-level rules to disk in the .cu
    2025-04-15 : Cursor : We’ve also fixed a long-standing issue where Always attached rules now persist a
    2025-04-15 : Cursor : For Auto Attached rules with path patterns defined, Agent will now automatically
    2025-04-15 : Cursor : Automated and improved rules
    2025-05-15 : Cursor : Introducing unified request-based pricing, Max Mode for all top models, and Back
    2025-06-04 : Cursor : This release brings Bugbot for code review, a first look at memories, one-click
    2025-06-04 : Cursor : Background Agent for everyone
    2025-06-12 : Cursor : You can now launch Background Agents directly from Slack by mentioning @Cursor.
    2025-06-12 : Cursor : Agents run remotely in a secure environment and you'll get updates directly in S
    2025-07-03 : Cursor : Agents now plan ahead with structured to-do lists, making long-horizon tasks eas
    2025-07-03 : Cursor : Queued messages
    2025-07-03 : Cursor : Agent To-dos
    2025-07-29 : Cursor : Agents can now use your native terminal. A new terminal will be created when nee
    2025-08-06 : Cursor : More Agent steerability
    2025-08-06 : Cursor : Improved Agent tools
    2025-08-06 : Cursor : Sending messages while Cursor is working now does a better job of steering the a
    2025-08-21 : Cursor : Run Agents in Linear
    2025-08-21 : Cursor : You can now start Background Agents directly from Linear. Delegate tasks to Curs
    2025-08-21 : Cursor : OS notifications from Agent
    2025-09-29 : ChatGPT : We’re introducing Instant Checkout in ChatGPT and the Agentic Commerce Protocol
    2025-09-29 : Cursor : Cursor can now write detailed plans before starting complex tasks. This allows a
    2025-09-29 : Cursor : Agent can take screenshots, improve UI, and debug client issues. Read more about
    2025-10-29 : Cursor : Multi-Agents
    2025-10-29 : Cursor : Run up to eight agents in parallel on a single prompt. This uses git worktrees o
    2025-11-21 : Cursor : When creating plans, Cursor responds with clarifying questions to improve the pl
    2025-11-21 : Cursor : Improved Plan Mode
    2025-12-10 : Cursor : Move elements, update colors, test layouts, and experiment with CSS in real time
    2025-12-18 : Cursor : Shared agent transcripts
    2025-12-22 : Cursor : This includes the core agent, layout controls, viewing code diffs, and more. We
    2026-01-11 : Claude Code : Added `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` environment variable to disable all
    2026-01-14 : Claude Code : Added inline display of agent's final response in task notifications, making it
    2026-01-16 : Claude Code : Added `plansDirectory` setting to customize where plan files are stored
    2026-01-16 : Cursor : Use Plan mode to design your approach before coding. Cursor will ask clarifying
    2026-01-16 : Cursor : Ask mode in CLI
    2026-01-16 : Cursor : Plan mode in CLI
    2026-01-22 : Cursor : Cursor includes default subagents for researching your codebase, running termina
    2026-01-22 : Cursor : Agents are solving increasingly complex, long-running tasks across your codebase
    2026-01-22 : Cursor : Optionally, you can define custom subagents. Learn more in our docs.
    2026-01-22 : Cursor : Subagents are independent agents specialized to handle discrete parts of a paren
    2026-01-23 : Claude Code : Added env var `CLAUDE_CODE_ENABLE_TASKS`, set to `false` to keep the old system
    2026-01-27 : Claude Code : Added ability to delete tasks via the `TaskUpdate` tool
    2026-02-03 : Claude Code : Added token count, tool uses, and duration metrics to Task tool results
    2026-02-06 : Claude Code : Added support for restricting which sub-agents can be spawned via `Task(agent_ty
    2026-02-06 : Claude Code : Added `TeammateIdle` and `TaskCompleted` hook events for multi-agent workflows
    2026-02-12 : Cursor : Cursor's long-running agent is now available at cursor.com/agents for Ultra, Tea
    2026-02-12 : Cursor : In research preview and internal testing, long-running agents completed work tha
    2026-02-12 : Cursor : Cursor can now work autonomously over longer horizons to complete larger, more c
    2026-02-17 : Cursor : This release introduces plugins for extending Cursor, improvements to core agent
    2026-02-18 : Claude Code : Improved VS Code plan preview: auto-updates as Claude iterates, enables commenti
    2026-02-18 : Cursor : Plan mode improvements in CLI
    2026-02-18 : Cursor : When a plan is generated, the CLI now shows a persistent decision menu. You can
    2026-02-20 : Claude Code : Added support for `isolation: worktree` in agent definitions, allowing agents to
    2026-02-24 : Cursor : Cloud agents can now use the software they create to test changes and demo their
    2026-02-24 : Cursor : After onboarding onto your codebase, each agent runs in its own isolated VM with
    2026-02-24 : Cursor : Get started at cursor.com/onboard to watch the agent configure itself and record
    2026-02-26 : Cursor : Autofix runs cloud agents on their own machines to test changes and propose fixe
    2026-02-28 : Claude Code : Added HTTP hooks, which can POST JSON to a URL and receive JSON instead of runni
    2026-03-04 : Cursor : With Cursor ACP, developers who rely on JetBrains for Java and multilanguage sup
    2026-03-04 : Cursor : Cursor is now available in IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains
    2026-03-10 : Claude Code : Added optional description argument to `/plan` (e.g., `/plan fix the auth bug`)
    2026-03-25 : Cursor : Your codebase, build outputs, and secrets all stay on internal machines running
    2026-03-25 : Cursor : Try it out today by enabling self-hosted cloud agents in your Cursor Dashboard.
    2026-03-25 : Cursor : Cursor now supports self-hosted cloud agents that keep your code and tool execut
    2026-03-26 : Claude Code : Added `TaskCreated` hook that fires when a task is created via `TaskCreate`
    2026-04-01 : Claude Code : Added `PermissionDenied` hook that fires after auto mode classifier denials — re
    2026-04-01 : Claude Code : Added named subagents to `@` mention typeahead suggestions
    2026-04-02 : Cursor : Agents Window
    2026-04-02 : Cursor : It's simpler, more powerful, and centered around agents, while keeping the depth
    2026-04-02 : Cursor : To try the Agents Window, upgrade Cursor and type Cmd+Shift+P -> Agents Window.
    2026-04-08 : Claude Code : Added `● N running` indicator in `/agents` next to agent types with live subagen
    2026-04-09 : Claude Code : Added Monitor tool for streaming events from background scripts
    2026-04-10 : Claude Code : `/ultraplan` and other remote-session features now auto-create a default cloud e
    2026-04-13 : Cursor : This release introduces improvements to our Agents Window interface as part of C
    2026-04-13 : Cursor : Split your current view into panes to run and manage several agents in parallel.
    2026-04-14 : Cursor : Ask a quick side question without derailing the agent's main task. /btw allows y
    2026-04-22 : Claude Code : Agent frontmatter `mcpServers` are now loaded for main-thread agent sessions via
    2026-04-22 : Claude Code : Forked subagents can now be enabled on external builds by setting `CLAUDE_CODE_F
    2026-04-23 : Claude Code : `--print` mode now honors the agent's `tools:` and `disallowedTools:` frontmatte
    2026-04-24 : Cursor : This release introduces a new way to multitask with async subagents, an improved
    2026-04-24 : Cursor : If you already have messages in the queue, you can ask Cursor to multitask on th
    2026-04-24 : Cursor : Multitask in Agents Window
    2026-04-24 : Cursor : With /multitask, Cursor will run async subagents to parallelize your requests in
    2026-04-24 : Cursor : Worktrees in Agents Window
    2026-04-29 : Cursor : import { Agent } from "@cursor/sdk";
    2026-04-29 : Cursor : const agent = await Agent.create({
    2026-05-08 : Claude Code : Added `settings.autoMode.hard_deny` for auto mode classifier rules that block un
    2026-05-11 : Claude Code : Added agent view (Research Preview): a single list of every Claude Code session
    2026-05-11 : Cursor : Mention @Cursor in any Teams channel to delegate a task to a cloud agent or pull
    2026-05-12 : Claude Code : Improved Agent tool `subagent_type` matching to accept case- and separator-insen
    2026-05-12 : Claude Code : Updated agent color palette
    2026-05-13 : Claude Code : Added `claude agents --cwd <path>` to scope the session list to a directory
    2026-05-13 : Cursor : To take engineering tasks from start to finish, agents need a development enviro
    2026-05-13 : Cursor : Files, changes, canvases, PRs, browsers, and terminals can expand to fill the en
    2026-05-13 : Cursor : This release introduces quality-of-life improvements to the Agents Window.
    2026-05-13 : Cursor : Cloud agents and automations now support multi-repo environments, building off o
    2026-05-13 : Cursor : This release introduces new tools for teams to configure development environment
    2026-05-18 : Cursor : Composer 2.5 is now available in Cursor.
    2026-05-19 : Claude Code : Added `/resume` support for background sessions — sessions started via `claude -
    2026-05-19 : Claude Code : `claude agents` terminal tab title now shows the awaiting-input count so an alt-
    2026-05-19 : Claude Code : Added `agent_id` and `parent_agent_id` attributes to `claude_code.tool` OTEL spa
    2026-05-19 : Claude Code : Added `claude agents --json` to list live Claude sessions as JSON for scripting
    2026-05-19 : Claude Code : Added elapsed duration to background subagent completion notifications (e.g. "Ag
    2026-05-19 : Cursor : Assign work items to Cursor, or mention @Cursor in a comment to kick off a cloud
    2026-05-20 : Cursor : With /loop, Cursor can run a prompt repeatedly on a local schedule, until a cert
    2026-05-21 : Claude Code : Auto mode no longer suppresses `AskUserQuestion` when the user or a skill explic
    2026-05-28 : Claude Code : `claude agents`: PR column now shows `PR #N` for a single PR or `N PRs` for mult
    2026-05-28 : Claude Code : Introducing dynamic workflows: ask Claude to create a workflow and it orchestrat
    2026-05-29 : Claude Code : `claude agents`: the `agent` field in `settings.json` is now honored for dispatc
    2026-05-29 : Cursor : Auto-review is a new run mode that allows Cursor to work for longer with fewer a
    2026-05-29 : Cursor : Configure your run mode in Settings > Cursor Settings > Agents > Approvals & Exe
    2026-06-02 : Claude Code : Improved performance of opening recently-inactive background agent sessions in `
    2026-06-02 : Claude Code : `claude agents` rows now show `done/total` before the detail when work is fanned
    2026-06-04 : ChatGPT : Lockdown Mode is now available to all logged-in users across account types and w
    2026-06-04 : Cursor : Before this, exposing a custom capability meant standing up your own stdio or re
    2026-06-04 : Cursor : By default, a local SDK agent runs tool calls without asking for approval, since
    2026-06-05 : Cursor : Ask the agent to make one match the other, remove repeated content, or adjust a
    2026-06-10 : Claude Code : Sub-agents can now spawn their own sub-agents (up to 5 levels deep)
    2026-06-15 : Claude Code : Improved auto mode: subagent spawns are now evaluated by the classifier before l
    2026-06-15 : Claude Code : Nested `.claude/` directories: the agent, workflow, and output-style closest to
    2026-06-17 : Cursor : Cloud subagents with /in-cloud
    2026-06-17 : Cursor : Cloud environment setup
    2026-06-19 : Claude Code : Improved auto mode safety: destructive git commands (`git reset --hard`, `git ch
    2026-06-22 : Claude Code : Added `teammateMode: "iterm2"` setting with a warning when auto mode cannot find
    2026-06-22 : Claude Code : Added status filtering (press `f`) to the `/workflows` agent detail view
    2026-06-25 : Claude Code : Added auto-mode denial reasons to the transcript, the denial toast, and `/permis
    2026-06-25 : Claude Code : Added `autoMode.classifyAllShell` setting to route all Bash/PowerShell commands
    2026-06-26 : Claude Code : Improved `claude agents` completed list to fill available vertical space; on sho
    2026-06-29 : Cursor : Cloud agents run in isolated virtual machines with full development environments
    2026-07-01 : Claude Code : Subagents now run in the background by default, so Claude keeps working while th
    2026-07-01 : Claude Code : Added background agent notifications in `claude agents` — sessions that need inp
    2026-07-06 : Claude Code : Added a "Dynamic workflow size" setting in `/config` for controlling how large C
    2026-07-06 : Claude Code : Added `workflow.run_id` and `workflow.name` OpenTelemetry attributes to telemetr
    2026-07-06 : Claude Code : Improved `/workflows` agent list layout: wider titles, a dedicated time column,
    2026-07-07 : Claude Code : Improved subagent behavior: agents are now less likely to re-delegate their enti
    2026-07-08 : Claude Code : Added an auto mode rule that blocks tampering with session transcript files
    2026-07-08 : Claude Code : Improved agent view: sessions that edit, merge, comment on, or push to an existi
    2026-07-10 : Cursor : By default, side chats focus on reading, searching, and answering. Use them to a
    2026-07-10 : Cursor : This release makes it easier to stay in flow with side chats that run alongside
    2026-07-11 : Claude Code : Auto mode is now available without `CLAUDE_CODE_ENABLE_AUTO_MODE` opt-in on Bedr
    2026-07-11 : Claude Code : Improved agent view: blocked session peeks now lead with the question and show a
    2026-07-14 : Claude Code : Hardened the Agent tool against indirect prompt injection via content a subagent
    2026-07-14 : Claude Code : Added `CLAUDE_CODE_PROCESS_WRAPPER`: agent view and the background service now h
    2026-07-15 : Claude Code : Improved background agent result reporting — Claude now reports the status of st
    2026-07-15 : Claude Code : Added `--forward-subagent-text` flag and `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` env
    2026-07-17 : Claude Code : Added a per-session cap on subagent spawns (default 200, override with `CLAUDE_C
    2026-07-17 : Claude Code : Added `claude auto-mode reset` to restore the default auto-mode configuration, w
    2026-07-17 : Claude Code : `/fork` now copies your conversation into a new background session (its own row
    2026-07-17 : Cursor : Cursor now responds with a plan before it begins, so you can jump in and redirec
    2026-07-22 : Cursor : Auto mode is now powered by Cursor Router.
    2026-07-24 : Claude Code : Added the `workflowSizeGuideline` settings key so the advisory Dynamic workflow
    2026-07-28 : Cursor : Always-on cloud agents that build, test, and ship code while you keep working.
```
<!-- chronolog:end -->

## Change Cards
<!-- chronolog:begin region="cards" -->
- 2023-07-06 Cursor: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Welcome to the first nightly release! It comes with agents, which we aren't rele]]
- 2023-07-10 Cursor: [[Changes/Cursor/2023-07-10-this-nightly-build-comes-with-experimental-interface-agent-support|This nightly build comes with experimental interface agent support!]]
- 2023-07-10 Cursor: [[Changes/Cursor/2023-07-10-the-goal-you-write-an-interface-specification-and-an-agent-writes-both-the-tests|The goal: you write an interface specification, and an agent writes both the tes]]
- 2024-02-15 Cursor: [[Changes/Cursor/2024-02-15-interpreter-mode-we-ve-made-some-big-improvements-to-the-backend-powering-interp|Interpreter Mode: We've made some big improvements to the backend powering inter]]
- 2024-08-02 Cursor: [[Changes/Cursor/2024-08-02-concurrent-composers-support-composer-control-panel-and-various-bug-fixes-such-a|Concurrent composers support, composer control panel, and various bug fixes such]]
- 2024-12-17 Cursor: [[Changes/Cursor/2024-12-17-agent-auto-saves-changes-to-disk|Agent auto-saves changes to disk]]
- 2024-12-17 Cursor: [[Changes/Cursor/2024-12-17-docs-git-web-and-folder-are-now-available-in-the-agent|@docs, @git, @web, and @folder are now available in the agent]]
- 2025-01-23 Cursor: [[Changes/Cursor/2025-01-23-agent-sees-recent-changes-the-agent-can-use-a-tool-to-see-your-recent-changes-it|Agent sees recent changes: The agent can use a tool to see your recent changes.]]
- 2025-01-23 Cursor: [[Changes/Cursor/2025-01-23-cursor-rules-users-can-write-several-repository-level-rules-to-disk-in-the-curso|.cursor/rules: Users can write several repository-level rules to disk in the .cu]]
- 2025-04-15 Cursor: [[Changes/Cursor/2025-04-15-we-ve-also-fixed-a-long-standing-issue-where-always-attached-rules-now-persist-a|We’ve also fixed a long-standing issue where Always attached rules now persist a]]
- 2025-04-15 Cursor: [[Changes/Cursor/2025-04-15-for-auto-attached-rules-with-path-patterns-defined-agent-will-now-automatically|For Auto Attached rules with path patterns defined, Agent will now automatically]]
- 2025-04-15 Cursor: [[Changes/Cursor/2025-04-15-automated-and-improved-rules|Automated and improved rules]]
- 2025-05-15 Cursor: [[Changes/Cursor/2025-05-15-introducing-unified-request-based-pricing-max-mode-for-all-top-models-and-backgr|Introducing unified request-based pricing, Max Mode for all top models, and Back]]
- 2025-06-04 Cursor: [[Changes/Cursor/2025-06-04-this-release-brings-bugbot-for-code-review-a-first-look-at-memories-one-click-mc|This release brings Bugbot for code review, a first look at memories, one-click]]
- 2025-06-04 Cursor: [[Changes/Cursor/2025-06-04-background-agent-for-everyone|Background Agent for everyone]]
- 2025-06-12 Cursor: [[Changes/Cursor/2025-06-12-you-can-now-launch-background-agents-directly-from-slack-by-mentioning-cursor-ag|You can now launch Background Agents directly from Slack by mentioning @Cursor.]]
- 2025-06-12 Cursor: [[Changes/Cursor/2025-06-12-agents-run-remotely-in-a-secure-environment-and-you-ll-get-updates-directly-in-s|Agents run remotely in a secure environment and you'll get updates directly in S]]
- 2025-07-03 Cursor: [[Changes/Cursor/2025-07-03-agents-now-plan-ahead-with-structured-to-do-lists-making-long-horizon-tasks-easi|Agents now plan ahead with structured to-do lists, making long-horizon tasks eas]]
- 2025-07-03 Cursor: [[Changes/Cursor/2025-07-03-queued-messages|Queued messages]]
- 2025-07-03 Cursor: [[Changes/Cursor/2025-07-03-agent-to-dos|Agent To-dos]]
- 2025-07-29 Cursor: [[Changes/Cursor/2025-07-29-agents-can-now-use-your-native-terminal-a-new-terminal-will-be-created-when-need|Agents can now use your native terminal. A new terminal will be created when nee]]
- 2025-08-06 Cursor: [[Changes/Cursor/2025-08-06-more-agent-steerability|More Agent steerability]]
- 2025-08-06 Cursor: [[Changes/Cursor/2025-08-06-improved-agent-tools|Improved Agent tools]]
- 2025-08-06 Cursor: [[Changes/Cursor/2025-08-06-sending-messages-while-cursor-is-working-now-does-a-better-job-of-steering-the-a|Sending messages while Cursor is working now does a better job of steering the a]]
- 2025-08-21 Cursor: [[Changes/Cursor/2025-08-21-run-agents-in-linear|Run Agents in Linear]]
- 2025-08-21 Cursor: [[Changes/Cursor/2025-08-21-you-can-now-start-background-agents-directly-from-linear-delegate-tasks-to-curso|You can now start Background Agents directly from Linear. Delegate tasks to Curs]]
- 2025-08-21 Cursor: [[Changes/Cursor/2025-08-21-os-notifications-from-agent|OS notifications from Agent]]
- 2025-09-29 ChatGPT: [[Changes/ChatGPT/2025-09-29-we-re-introducing-instant-checkout-in-chatgpt-and-the-agentic-commerce-protocol|We’re introducing Instant Checkout in ChatGPT and the Agentic Commerce Protocol]]
- 2025-09-29 Cursor: [[Changes/Cursor/2025-09-29-cursor-can-now-write-detailed-plans-before-starting-complex-tasks-this-allows-ag|Cursor can now write detailed plans before starting complex tasks. This allows a]]
- 2025-09-29 Cursor: [[Changes/Cursor/2025-09-29-agent-can-take-screenshots-improve-ui-and-debug-client-issues-read-more-about-br|Agent can take screenshots, improve UI, and debug client issues. Read more about]]
- 2025-10-29 Cursor: [[Changes/Cursor/2025-10-29-multi-agents|Multi-Agents]]
- 2025-10-29 Cursor: [[Changes/Cursor/2025-10-29-run-up-to-eight-agents-in-parallel-on-a-single-prompt-this-uses-git-worktrees-or|Run up to eight agents in parallel on a single prompt. This uses git worktrees o]]
- 2025-11-21 Cursor: [[Changes/Cursor/2025-11-21-when-creating-plans-cursor-responds-with-clarifying-questions-to-improve-the-pla|When creating plans, Cursor responds with clarifying questions to improve the pl]]
- 2025-11-21 Cursor: [[Changes/Cursor/2025-11-21-improved-plan-mode|Improved Plan Mode]]
- 2025-12-10 Cursor: [[Changes/Cursor/2025-12-10-move-elements-update-colors-test-layouts-and-experiment-with-css-in-real-time-th|Move elements, update colors, test layouts, and experiment with CSS in real time]]
- 2025-12-18 Cursor: [[Changes/Cursor/2025-12-18-shared-agent-transcripts|Shared agent transcripts]]
- 2025-12-22 Cursor: [[Changes/Cursor/2025-12-22-this-includes-the-core-agent-layout-controls-viewing-code-diffs-and-more-we-will|This includes the core agent, layout controls, viewing code diffs, and more. We]]
- 2026-01-11 Claude Code: [[Changes/Claude Code/2026-01-11-added-claude-code-disable-background-tasks-environment-variable-to-disable-all-b|Added `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` environment variable to disable all]]
- 2026-01-14 Claude Code: [[Changes/Claude Code/2026-01-14-added-inline-display-of-agent-s-final-response-in-task-notifications-making-it-e|Added inline display of agent's final response in task notifications, making it]]
- 2026-01-16 Claude Code: [[Changes/Claude Code/2026-01-16-added-plansdirectory-setting-to-customize-where-plan-files-are-stored|Added `plansDirectory` setting to customize where plan files are stored]]
- 2026-01-16 Cursor: [[Changes/Cursor/2026-01-16-use-plan-mode-to-design-your-approach-before-coding-cursor-will-ask-clarifying-q|Use Plan mode to design your approach before coding. Cursor will ask clarifying]]
- 2026-01-16 Cursor: [[Changes/Cursor/2026-01-16-ask-mode-in-cli|Ask mode in CLI]]
- 2026-01-16 Cursor: [[Changes/Cursor/2026-01-16-plan-mode-in-cli|Plan mode in CLI]]
- 2026-01-22 Cursor: [[Changes/Cursor/2026-01-22-cursor-includes-default-subagents-for-researching-your-codebase-running-terminal|Cursor includes default subagents for researching your codebase, running termina]]
- 2026-01-22 Cursor: [[Changes/Cursor/2026-01-22-agents-are-solving-increasingly-complex-long-running-tasks-across-your-codebase|Agents are solving increasingly complex, long-running tasks across your codebase]]
- 2026-01-22 Cursor: [[Changes/Cursor/2026-01-22-optionally-you-can-define-custom-subagents-learn-more-in-our-docs|Optionally, you can define custom subagents. Learn more in our docs.]]
- 2026-01-22 Cursor: [[Changes/Cursor/2026-01-22-subagents-are-independent-agents-specialized-to-handle-discrete-parts-of-a-paren|Subagents are independent agents specialized to handle discrete parts of a paren]]
- 2026-01-23 Claude Code: [[Changes/Claude Code/2026-01-23-added-env-var-claude-code-enable-tasks-set-to-false-to-keep-the-old-system-tempo|Added env var `CLAUDE_CODE_ENABLE_TASKS`, set to `false` to keep the old system]]
- 2026-01-27 Claude Code: [[Changes/Claude Code/2026-01-27-added-ability-to-delete-tasks-via-the-taskupdate-tool|Added ability to delete tasks via the `TaskUpdate` tool]]
- 2026-02-03 Claude Code: [[Changes/Claude Code/2026-02-03-added-token-count-tool-uses-and-duration-metrics-to-task-tool-results|Added token count, tool uses, and duration metrics to Task tool results]]
- 2026-02-06 Claude Code: [[Changes/Claude Code/2026-02-06-added-support-for-restricting-which-sub-agents-can-be-spawned-via-task-agent-typ|Added support for restricting which sub-agents can be spawned via `Task(agent_ty]]
- 2026-02-06 Claude Code: [[Changes/Claude Code/2026-02-06-added-teammateidle-and-taskcompleted-hook-events-for-multi-agent-workflows|Added `TeammateIdle` and `TaskCompleted` hook events for multi-agent workflows]]
- 2026-02-12 Cursor: [[Changes/Cursor/2026-02-12-cursor-s-long-running-agent-is-now-available-at-cursor-com-agents-for-ultra-team|Cursor's long-running agent is now available at cursor.com/agents for Ultra, Tea]]
- 2026-02-12 Cursor: [[Changes/Cursor/2026-02-12-in-research-preview-and-internal-testing-long-running-agents-completed-work-that|In research preview and internal testing, long-running agents completed work tha]]
- 2026-02-12 Cursor: [[Changes/Cursor/2026-02-12-cursor-can-now-work-autonomously-over-longer-horizons-to-complete-larger-more-co|Cursor can now work autonomously over longer horizons to complete larger, more c]]
- 2026-02-17 Cursor: [[Changes/Cursor/2026-02-17-this-release-introduces-plugins-for-extending-cursor-improvements-to-core-agent|This release introduces plugins for extending Cursor, improvements to core agent]]
- 2026-02-18 Claude Code: [[Changes/Claude Code/2026-02-18-improved-vs-code-plan-preview-auto-updates-as-claude-iterates-enables-commenting|Improved VS Code plan preview: auto-updates as Claude iterates, enables commenti]]
- 2026-02-18 Cursor: [[Changes/Cursor/2026-02-18-plan-mode-improvements-in-cli|Plan mode improvements in CLI]]
- 2026-02-18 Cursor: [[Changes/Cursor/2026-02-18-when-a-plan-is-generated-the-cli-now-shows-a-persistent-decision-menu-you-can-ch|When a plan is generated, the CLI now shows a persistent decision menu. You can]]
- 2026-02-20 Claude Code: [[Changes/Claude Code/2026-02-20-added-support-for-isolation-worktree-in-agent-definitions-allowing-agents-to-dec|Added support for `isolation: worktree` in agent definitions, allowing agents to]]
- 2026-02-24 Cursor: [[Changes/Cursor/2026-02-24-cloud-agents-can-now-use-the-software-they-create-to-test-changes-and-demo-their|Cloud agents can now use the software they create to test changes and demo their]]
- 2026-02-24 Cursor: [[Changes/Cursor/2026-02-24-after-onboarding-onto-your-codebase-each-agent-runs-in-its-own-isolated-vm-with|After onboarding onto your codebase, each agent runs in its own isolated VM with]]
- 2026-02-24 Cursor: [[Changes/Cursor/2026-02-24-get-started-at-cursor-com-onboard-to-watch-the-agent-configure-itself-and-record|Get started at cursor.com/onboard to watch the agent configure itself and record]]
- 2026-02-26 Cursor: [[Changes/Cursor/2026-02-26-autofix-runs-cloud-agents-on-their-own-machines-to-test-changes-and-propose-fixe|Autofix runs cloud agents on their own machines to test changes and propose fixe]]
- 2026-02-28 Claude Code: [[Changes/Claude Code/2026-02-28-added-http-hooks-which-can-post-json-to-a-url-and-receive-json-instead-of-runnin|Added HTTP hooks, which can POST JSON to a URL and receive JSON instead of runni]]
- 2026-03-04 Cursor: [[Changes/Cursor/2026-03-04-with-cursor-acp-developers-who-rely-on-jetbrains-for-java-and-multilanguage-supp|With Cursor ACP, developers who rely on JetBrains for Java and multilanguage sup]]
- 2026-03-04 Cursor: [[Changes/Cursor/2026-03-04-cursor-is-now-available-in-intellij-idea-pycharm-webstorm-and-other-jetbrains-id|Cursor is now available in IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains]]
- 2026-03-10 Claude Code: [[Changes/Claude Code/2026-03-10-added-optional-description-argument-to-plan-e-g-plan-fix-the-auth-bug-that-enter|Added optional description argument to `/plan` (e.g., `/plan fix the auth bug`)]]
- 2026-03-25 Cursor: [[Changes/Cursor/2026-03-25-your-codebase-build-outputs-and-secrets-all-stay-on-internal-machines-running-in|Your codebase, build outputs, and secrets all stay on internal machines running]]
- 2026-03-25 Cursor: [[Changes/Cursor/2026-03-25-try-it-out-today-by-enabling-self-hosted-cloud-agents-in-your-cursor-dashboard-r|Try it out today by enabling self-hosted cloud agents in your Cursor Dashboard.]]
- 2026-03-25 Cursor: [[Changes/Cursor/2026-03-25-cursor-now-supports-self-hosted-cloud-agents-that-keep-your-code-and-tool-execut|Cursor now supports self-hosted cloud agents that keep your code and tool execut]]
- 2026-03-26 Claude Code: [[Changes/Claude Code/2026-03-26-added-taskcreated-hook-that-fires-when-a-task-is-created-via-taskcreate|Added `TaskCreated` hook that fires when a task is created via `TaskCreate`]]
- 2026-04-01 Claude Code: [[Changes/Claude Code/2026-04-01-added-permissiondenied-hook-that-fires-after-auto-mode-classifier-denials-return|Added `PermissionDenied` hook that fires after auto mode classifier denials — re]]
- 2026-04-01 Claude Code: [[Changes/Claude Code/2026-04-01-added-named-subagents-to-mention-typeahead-suggestions|Added named subagents to `@` mention typeahead suggestions]]
- 2026-04-02 Cursor: [[Changes/Cursor/2026-04-02-agents-window|Agents Window]]
- 2026-04-02 Cursor: [[Changes/Cursor/2026-04-02-it-s-simpler-more-powerful-and-centered-around-agents-while-keeping-the-depth-of|It's simpler, more powerful, and centered around agents, while keeping the depth]]
- 2026-04-02 Cursor: [[Changes/Cursor/2026-04-02-to-try-the-agents-window-upgrade-cursor-and-type-cmd-shift-p-agents-window|To try the Agents Window, upgrade Cursor and type Cmd+Shift+P -> Agents Window.]]
- 2026-04-08 Claude Code: [[Changes/Claude Code/2026-04-08-added-n-running-indicator-in-agents-next-to-agent-types-with-live-subagent-insta|Added `● N running` indicator in `/agents` next to agent types with live subagen]]
- 2026-04-09 Claude Code: [[Changes/Claude Code/2026-04-09-added-monitor-tool-for-streaming-events-from-background-scripts|Added Monitor tool for streaming events from background scripts]]
- 2026-04-10 Claude Code: [[Changes/Claude Code/2026-04-10-ultraplan-and-other-remote-session-features-now-auto-create-a-default-cloud-envi|`/ultraplan` and other remote-session features now auto-create a default cloud e]]
- 2026-04-13 Cursor: [[Changes/Cursor/2026-04-13-this-release-introduces-improvements-to-our-agents-window-interface-as-part-of-c|This release introduces improvements to our Agents Window interface as part of C]]
- 2026-04-13 Cursor: [[Changes/Cursor/2026-04-13-split-your-current-view-into-panes-to-run-and-manage-several-agents-in-parallel|Split your current view into panes to run and manage several agents in parallel.]]
- 2026-04-14 Cursor: [[Changes/Cursor/2026-04-14-ask-a-quick-side-question-without-derailing-the-agent-s-main-task-btw-allows-you|Ask a quick side question without derailing the agent's main task. /btw allows y]]
- 2026-04-22 Claude Code: [[Changes/Claude Code/2026-04-22-agent-frontmatter-mcpservers-are-now-loaded-for-main-thread-agent-sessions-via-a|Agent frontmatter `mcpServers` are now loaded for main-thread agent sessions via]]
- 2026-04-22 Claude Code: [[Changes/Claude Code/2026-04-22-forked-subagents-can-now-be-enabled-on-external-builds-by-setting-claude-code-fo|Forked subagents can now be enabled on external builds by setting `CLAUDE_CODE_F]]
- 2026-04-23 Claude Code: [[Changes/Claude Code/2026-04-23-print-mode-now-honors-the-agent-s-tools-and-disallowedtools-frontmatter-matching|`--print` mode now honors the agent's `tools:` and `disallowedTools:` frontmatte]]
- 2026-04-24 Cursor: [[Changes/Cursor/2026-04-24-this-release-introduces-a-new-way-to-multitask-with-async-subagents-an-improved|This release introduces a new way to multitask with async subagents, an improved]]
- 2026-04-24 Cursor: [[Changes/Cursor/2026-04-24-if-you-already-have-messages-in-the-queue-you-can-ask-cursor-to-multitask-on-the|If you already have messages in the queue, you can ask Cursor to multitask on th]]
- 2026-04-24 Cursor: [[Changes/Cursor/2026-04-24-multitask-in-agents-window|Multitask in Agents Window]]
- 2026-04-24 Cursor: [[Changes/Cursor/2026-04-24-with-multitask-cursor-will-run-async-subagents-to-parallelize-your-requests-inst|With /multitask, Cursor will run async subagents to parallelize your requests in]]
- 2026-04-24 Cursor: [[Changes/Cursor/2026-04-24-worktrees-in-agents-window|Worktrees in Agents Window]]
- 2026-04-29 Cursor: [[Changes/Cursor/2026-04-29-import-agent-from-cursor-sdk|import { Agent } from "@cursor/sdk";]]
- 2026-04-29 Cursor: [[Changes/Cursor/2026-04-29-const-agent-await-agent-create|const agent = await Agent.create({]]
- 2026-05-08 Claude Code: [[Changes/Claude Code/2026-05-08-added-settings-automode-hard-deny-for-auto-mode-classifier-rules-that-block-unco|Added `settings.autoMode.hard_deny` for auto mode classifier rules that block un]]
- 2026-05-11 Claude Code: [[Changes/Claude Code/2026-05-11-added-agent-view-research-preview-a-single-list-of-every-claude-code-session-run|Added agent view (Research Preview): a single list of every Claude Code session]]
- 2026-05-11 Cursor: [[Changes/Cursor/2026-05-11-mention-cursor-in-any-teams-channel-to-delegate-a-task-to-a-cloud-agent-or-pull|Mention @Cursor in any Teams channel to delegate a task to a cloud agent or pull]]
- 2026-05-12 Claude Code: [[Changes/Claude Code/2026-05-12-improved-agent-tool-subagent-type-matching-to-accept-case-and-separator-insensit|Improved Agent tool `subagent_type` matching to accept case- and separator-insen]]
- 2026-05-12 Claude Code: [[Changes/Claude Code/2026-05-12-updated-agent-color-palette|Updated agent color palette]]
- 2026-05-13 Claude Code: [[Changes/Claude Code/2026-05-13-added-claude-agents-cwd-path-to-scope-the-session-list-to-a-directory|Added `claude agents --cwd <path>` to scope the session list to a directory]]
- 2026-05-13 Cursor: [[Changes/Cursor/2026-05-13-to-take-engineering-tasks-from-start-to-finish-agents-need-a-development-environ|To take engineering tasks from start to finish, agents need a development enviro]]
- 2026-05-13 Cursor: [[Changes/Cursor/2026-05-13-files-changes-canvases-prs-browsers-and-terminals-can-expand-to-fill-the-entire|Files, changes, canvases, PRs, browsers, and terminals can expand to fill the en]]
- 2026-05-13 Cursor: [[Changes/Cursor/2026-05-13-this-release-introduces-quality-of-life-improvements-to-the-agents-window|This release introduces quality-of-life improvements to the Agents Window.]]
- 2026-05-13 Cursor: [[Changes/Cursor/2026-05-13-cloud-agents-and-automations-now-support-multi-repo-environments-building-off-ou|Cloud agents and automations now support multi-repo environments, building off o]]
- 2026-05-13 Cursor: [[Changes/Cursor/2026-05-13-this-release-introduces-new-tools-for-teams-to-configure-development-environment|This release introduces new tools for teams to configure development environment]]
- 2026-05-18 Cursor: [[Changes/Cursor/2026-05-18-composer-2-5-is-now-available-in-cursor|Composer 2.5 is now available in Cursor.]]
- 2026-05-19 Claude Code: [[Changes/Claude Code/2026-05-19-added-resume-support-for-background-sessions-sessions-started-via-claude-bg-or-a|Added `/resume` support for background sessions — sessions started via `claude -]]
- 2026-05-19 Claude Code: [[Changes/Claude Code/2026-05-19-claude-agents-terminal-tab-title-now-shows-the-awaiting-input-count-so-an-alt-ta|`claude agents` terminal tab title now shows the awaiting-input count so an alt-]]
- 2026-05-19 Claude Code: [[Changes/Claude Code/2026-05-19-added-agent-id-and-parent-agent-id-attributes-to-claude-code-tool-otel-spans-and|Added `agent_id` and `parent_agent_id` attributes to `claude_code.tool` OTEL spa]]
- 2026-05-19 Claude Code: [[Changes/Claude Code/2026-05-19-added-claude-agents-json-to-list-live-claude-sessions-as-json-for-scripting-tmux|Added `claude agents --json` to list live Claude sessions as JSON for scripting]]
- 2026-05-19 Claude Code: [[Changes/Claude Code/2026-05-19-added-elapsed-duration-to-background-subagent-completion-notifications-e-g-agent|Added elapsed duration to background subagent completion notifications (e.g. "Ag]]
- 2026-05-19 Cursor: [[Changes/Cursor/2026-05-19-assign-work-items-to-cursor-or-mention-cursor-in-a-comment-to-kick-off-a-cloud-a|Assign work items to Cursor, or mention @Cursor in a comment to kick off a cloud]]
- 2026-05-20 Cursor: [[Changes/Cursor/2026-05-20-with-loop-cursor-can-run-a-prompt-repeatedly-on-a-local-schedule-until-a-certain|With /loop, Cursor can run a prompt repeatedly on a local schedule, until a cert]]
- 2026-05-21 Claude Code: [[Changes/Claude Code/2026-05-21-auto-mode-no-longer-suppresses-askuserquestion-when-the-user-or-a-skill-explicit|Auto mode no longer suppresses `AskUserQuestion` when the user or a skill explic]]
- 2026-05-28 Claude Code: [[Changes/Claude Code/2026-05-28-claude-agents-pr-column-now-shows-pr-n-for-a-single-pr-or-n-prs-for-multiple|`claude agents`: PR column now shows `PR #N` for a single PR or `N PRs` for mult]]
- 2026-05-28 Claude Code: [[Changes/Claude Code/2026-05-28-introducing-dynamic-workflows-ask-claude-to-create-a-workflow-and-it-orchestrate|Introducing dynamic workflows: ask Claude to create a workflow and it orchestrat]]
- 2026-05-29 Claude Code: [[Changes/Claude Code/2026-05-29-claude-agents-the-agent-field-in-settings-json-is-now-honored-for-dispatched-ses|`claude agents`: the `agent` field in `settings.json` is now honored for dispatc]]
- 2026-05-29 Cursor: [[Changes/Cursor/2026-05-29-auto-review-is-a-new-run-mode-that-allows-cursor-to-work-for-longer-with-fewer-a|Auto-review is a new run mode that allows Cursor to work for longer with fewer a]]
- 2026-05-29 Cursor: [[Changes/Cursor/2026-05-29-configure-your-run-mode-in-settings-cursor-settings-agents-approvals-execution-y|Configure your run mode in Settings > Cursor Settings > Agents > Approvals & Exe]]
- 2026-06-02 Claude Code: [[Changes/Claude Code/2026-06-02-improved-performance-of-opening-recently-inactive-background-agent-sessions-in-c|Improved performance of opening recently-inactive background agent sessions in `]]
- 2026-06-02 Claude Code: [[Changes/Claude Code/2026-06-02-claude-agents-rows-now-show-done-total-before-the-detail-when-work-is-fanned-out|`claude agents` rows now show `done/total` before the detail when work is fanned]]
- 2026-06-04 ChatGPT: [[Changes/ChatGPT/2026-06-04-lockdown-mode-is-now-available-to-all-logged-in-users-across-account-types-and-w|Lockdown Mode is now available to all logged-in users across account types and w]]
- 2026-06-04 Cursor: [[Changes/Cursor/2026-06-04-before-this-exposing-a-custom-capability-meant-standing-up-your-own-stdio-or-rem|Before this, exposing a custom capability meant standing up your own stdio or re]]
- 2026-06-04 Cursor: [[Changes/Cursor/2026-06-04-by-default-a-local-sdk-agent-runs-tool-calls-without-asking-for-approval-since-t|By default, a local SDK agent runs tool calls without asking for approval, since]]
- 2026-06-05 Cursor: [[Changes/Cursor/2026-06-05-ask-the-agent-to-make-one-match-the-other-remove-repeated-content-or-adjust-a-gr|Ask the agent to make one match the other, remove repeated content, or adjust a]]
- 2026-06-10 Claude Code: [[Changes/Claude Code/2026-06-10-sub-agents-can-now-spawn-their-own-sub-agents-up-to-5-levels-deep|Sub-agents can now spawn their own sub-agents (up to 5 levels deep)]]
- 2026-06-15 Claude Code: [[Changes/Claude Code/2026-06-15-improved-auto-mode-subagent-spawns-are-now-evaluated-by-the-classifier-before-la|Improved auto mode: subagent spawns are now evaluated by the classifier before l]]
- 2026-06-15 Claude Code: [[Changes/Claude Code/2026-06-15-nested-claude-directories-the-agent-workflow-and-output-style-closest-to-the-wor|Nested `.claude/` directories: the agent, workflow, and output-style closest to]]
- 2026-06-17 Cursor: [[Changes/Cursor/2026-06-17-cloud-subagents-with-in-cloud|Cloud subagents with /in-cloud]]
- 2026-06-17 Cursor: [[Changes/Cursor/2026-06-17-cloud-environment-setup|Cloud environment setup]]
- 2026-06-19 Claude Code: [[Changes/Claude Code/2026-06-19-improved-auto-mode-safety-destructive-git-commands-git-reset-hard-git-checkout-g|Improved auto mode safety: destructive git commands (`git reset --hard`, `git ch]]
- 2026-06-22 Claude Code: [[Changes/Claude Code/2026-06-22-added-teammatemode-iterm2-setting-with-a-warning-when-auto-mode-cannot-find-the|Added `teammateMode: "iterm2"` setting with a warning when auto mode cannot find]]
- 2026-06-22 Claude Code: [[Changes/Claude Code/2026-06-22-added-status-filtering-press-f-to-the-workflows-agent-detail-view|Added status filtering (press `f`) to the `/workflows` agent detail view]]
- 2026-06-25 Claude Code: [[Changes/Claude Code/2026-06-25-added-auto-mode-denial-reasons-to-the-transcript-the-denial-toast-and-permission|Added auto-mode denial reasons to the transcript, the denial toast, and `/permis]]
- 2026-06-25 Claude Code: [[Changes/Claude Code/2026-06-25-added-automode-classifyallshell-setting-to-route-all-bash-powershell-commands-th|Added `autoMode.classifyAllShell` setting to route all Bash/PowerShell commands]]
- 2026-06-26 Claude Code: [[Changes/Claude Code/2026-06-26-improved-claude-agents-completed-list-to-fill-available-vertical-space-on-short|Improved `claude agents` completed list to fill available vertical space; on sho]]
- 2026-06-29 Cursor: [[Changes/Cursor/2026-06-29-cloud-agents-run-in-isolated-virtual-machines-with-full-development-environments|Cloud agents run in isolated virtual machines with full development environments]]
- 2026-07-01 Claude Code: [[Changes/Claude Code/2026-07-01-subagents-now-run-in-the-background-by-default-so-claude-keeps-working-while-the|Subagents now run in the background by default, so Claude keeps working while th]]
- 2026-07-01 Claude Code: [[Changes/Claude Code/2026-07-01-added-background-agent-notifications-in-claude-agents-sessions-that-need-input-o|Added background agent notifications in `claude agents` — sessions that need inp]]
- 2026-07-06 Claude Code: [[Changes/Claude Code/2026-07-06-added-a-dynamic-workflow-size-setting-in-config-for-controlling-how-large-claude|Added a "Dynamic workflow size" setting in `/config` for controlling how large C]]
- 2026-07-06 Claude Code: [[Changes/Claude Code/2026-07-06-added-workflow-run-id-and-workflow-name-opentelemetry-attributes-to-telemetry-em|Added `workflow.run_id` and `workflow.name` OpenTelemetry attributes to telemetr]]
- 2026-07-06 Claude Code: [[Changes/Claude Code/2026-07-06-improved-workflows-agent-list-layout-wider-titles-a-dedicated-time-column-shorte|Improved `/workflows` agent list layout: wider titles, a dedicated time column,]]
- 2026-07-07 Claude Code: [[Changes/Claude Code/2026-07-07-improved-subagent-behavior-agents-are-now-less-likely-to-re-delegate-their-entir|Improved subagent behavior: agents are now less likely to re-delegate their enti]]
- 2026-07-08 Claude Code: [[Changes/Claude Code/2026-07-08-added-an-auto-mode-rule-that-blocks-tampering-with-session-transcript-files|Added an auto mode rule that blocks tampering with session transcript files]]
- 2026-07-08 Claude Code: [[Changes/Claude Code/2026-07-08-improved-agent-view-sessions-that-edit-merge-comment-on-or-push-to-an-existing-p|Improved agent view: sessions that edit, merge, comment on, or push to an existi]]
- 2026-07-10 Cursor: [[Changes/Cursor/2026-07-10-by-default-side-chats-focus-on-reading-searching-and-answering-use-them-to-ask-c|By default, side chats focus on reading, searching, and answering. Use them to a]]
- 2026-07-10 Cursor: [[Changes/Cursor/2026-07-10-this-release-makes-it-easier-to-stay-in-flow-with-side-chats-that-run-alongside|This release makes it easier to stay in flow with side chats that run alongside]]
- 2026-07-11 Claude Code: [[Changes/Claude Code/2026-07-11-auto-mode-is-now-available-without-claude-code-enable-auto-mode-opt-in-on-bedroc|Auto mode is now available without `CLAUDE_CODE_ENABLE_AUTO_MODE` opt-in on Bedr]]
- 2026-07-11 Claude Code: [[Changes/Claude Code/2026-07-11-improved-agent-view-blocked-session-peeks-now-lead-with-the-question-and-show-a|Improved agent view: blocked session peeks now lead with the question and show a]]
- 2026-07-14 Claude Code: [[Changes/Claude Code/2026-07-14-hardened-the-agent-tool-against-indirect-prompt-injection-via-content-a-subagent|Hardened the Agent tool against indirect prompt injection via content a subagent]]
- 2026-07-14 Claude Code: [[Changes/Claude Code/2026-07-14-added-claude-code-process-wrapper-agent-view-and-the-background-service-now-hono|Added `CLAUDE_CODE_PROCESS_WRAPPER`: agent view and the background service now h]]
- 2026-07-15 Claude Code: [[Changes/Claude Code/2026-07-15-improved-background-agent-result-reporting-claude-now-reports-the-status-of-stil|Improved background agent result reporting — Claude now reports the status of st]]
- 2026-07-15 Claude Code: [[Changes/Claude Code/2026-07-15-added-forward-subagent-text-flag-and-claude-code-forward-subagent-text-environme|Added `--forward-subagent-text` flag and `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` env]]
- 2026-07-17 Claude Code: [[Changes/Claude Code/2026-07-17-added-a-per-session-cap-on-subagent-spawns-default-200-override-with-claude-code|Added a per-session cap on subagent spawns (default 200, override with `CLAUDE_C]]
- 2026-07-17 Claude Code: [[Changes/Claude Code/2026-07-17-added-claude-auto-mode-reset-to-restore-the-default-auto-mode-configuration-with|Added `claude auto-mode reset` to restore the default auto-mode configuration, w]]
- 2026-07-17 Claude Code: [[Changes/Claude Code/2026-07-17-fork-now-copies-your-conversation-into-a-new-background-session-its-own-row-in-c|`/fork` now copies your conversation into a new background session (its own row]]
- 2026-07-17 Cursor: [[Changes/Cursor/2026-07-17-cursor-now-responds-with-a-plan-before-it-begins-so-you-can-jump-in-and-redirect|Cursor now responds with a plan before it begins, so you can jump in and redirec]]
- 2026-07-22 Cursor: [[Changes/Cursor/2026-07-22-auto-mode-is-now-powered-by-cursor-router|Auto mode is now powered by Cursor Router.]]
- 2026-07-24 Claude Code: [[Changes/Claude Code/2026-07-24-added-the-workflowsizeguideline-settings-key-so-the-advisory-dynamic-workflow-si|Added the `workflowSizeGuideline` settings key so the advisory Dynamic workflow]]
- 2026-07-28 Cursor: [[Changes/Cursor/2026-07-28-always-on-cloud-agents-that-build-test-and-ship-code-while-you-keep-working|Always-on cloud agents that build, test, and ship code while you keep working.]]
<!-- chronolog:end -->