---
created: '2023-07-06'
date: '2026-10-14'
machine_hash: 8da6bf46ae9eccafd4294b73cf1561b03b4fdc8786e172b0563da47a1d2a5d55
modified: '2026-10-14'
products_involved:
- ChatGPT
- Claude Code
- Cursor
publication: active
status: official
tags:
- theme
- moc
theme: agent-mode
title: Agent Mode
---

# Theme: agent-mode

## Research summary
<!-- chronolog:begin region="narrative" -->
**Research question: what changed in delegated execution?**

Cursor's [2025-05-15 release](https://cursor.com/changelog/0-50) introduces Background Agent for parallel task execution. The [2025-06-04 release](https://cursor.com/changelog/1-0) expands access to the remote coding agent, with privacy-mode limitations at that time. This is a supported within-product expansion of the same named capability.

ChatGPT's [2026-07-09 Work announcement](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#introducing-chatgpt-work) describes longer research and creation tasks across apps and files, with user direction and approvals. [Dots on 2026-09-29](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#meet-your-dot) adds ongoing goals on a cloud computer, with plan and regional restrictions. These are general-work agents; they are not interchangeable with Cursor's repository-oriented remote coding agent.

Claude Code's [v2.1.296](https://github.com/anthropics/claude-code/releases/tag/v2.1.296) adds a workflow-subagent model setting and per-subagent auto-compaction. These are controls over an existing execution system, not its launch. Our dated Claude Code Releases coverage starts at v2.0.73, so its first appearance here cannot establish when agent functionality first existed.

**Uncertainty and scope:** tracked-products-only. Similar names and dates do not establish identical autonomy, reliability, adoption, or influence. The timeline below is a sequence of evidence, not a diffusion claim. Generic permission fixes and unrelated uses of “mode” do not by themselves qualify as agent capabilities.
<!-- chronolog:end -->

## Cross-Product Timeline
<!-- chronolog:begin region="timeline" -->
Scope: tracked-products-only. Entries show same-theme chronology; they do not establish equivalent capabilities, adoption, or causation.

### 2026

- 2026-10-14 · Claude Code: [[Changes/Claude Code/2026-10-14-added-ui-view-agentid-for-mods-shows-an-agent-s-transcript-in-the-main-view-when|Added USD .ui.view({ agentId }) for mods: shows an agent's transcript in the main]]
- 2026-10-09 · Claude Code: [[Changes/Claude Code/2026-10-09-added-claude-code-workflow-subagent-model-to-run-every-workflow-agent-on-one-mod|Added CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL to run every workflow agent on one m]]
- 2026-10-07 · Claude Code: [[Changes/Claude Code/2026-10-07-added-agenttype-to-the-subagentstatusline-payload-so-scripts-can-tell-custom-sub|Added agentType to the subagentStatusLine payload, so scripts can tell custo]]
- 2026-10-06 · Cursor: [[Changes/Cursor/2026-10-06-remote-control-doesn-t-move-your-agents-anywhere-it-keeps-running-on-your-comput|Remote control doesn't move your agents anywhere. It keeps running on your compu]]
- 2026-10-06 · Claude Code: [[Changes/Claude Code/2026-10-06-added-an-effort-parameter-to-the-agent-tool-so-claude-runs-a-sub-agent-at-the-ef|Added an effort parameter to the Agent tool, so Claude runs a sub-agent at the]]
- 2026-10-01 · Claude Code: [[Changes/Claude Code/2026-10-01-added-an-n-text-filter-to-the-agents-view-that-matches-session-names-and-tasks-a|Added an n:text filter to the agents view that matches session names and tas]]
- 2026-09-30 · Claude Code: [[Changes/Claude Code/2026-09-30-improved-replies-from-background-agents-to-your-messages-so-they-no-longer-open|Improved replies from background agents to your messages so they no longer open]]
- 2026-09-30 · Claude Code: [[Changes/Claude Code/2026-09-30-improved-send-now-ctrl-enter-in-a-subagent-s-view-it-now-moves-the-subagent-s-ru|Improved send now (ctrl+enter) in a subagent's view: it now moves the subagent's]]
- 2026-09-29 · ChatGPT: [[Changes/ChatGPT/2026-09-29-we-re-introducing-dots-always-on-agents-in-chatgpt-that-can-take-on-ongoing-work|We’re introducing dots: always-on agents in ChatGPT that can take on ongoing wor]]
- 2026-09-28 · Claude Code: [[Changes/Claude Code/2026-09-28-added-a-yes-but-ask-again-next-time-answer-to-auto-mode-s-prompt-before-a-read-o|Added a "Yes, but ask again next time" answer to auto mode's prompt before a rea]]
- 2026-09-19 · Claude Code: [[Changes/Claude Code/2026-09-19-added-an-auto-mode-server-row-to-status-showing-whether-this-session-s-auto-mode|Added an Auto mode server row to /status showing whether this session's auto]]
- 2026-09-18 · Claude Code: [[Changes/Claude Code/2026-09-18-added-agents-md-support-in-a-project-with-no-claude-md-claude-code-reads-agents|Added AGENTS.md support: in a project with no CLAUDE.md, Claude Code reads AGENT]]
- 2026-09-14 · Claude Code: [[Changes/Claude Code/2026-09-14-added-per-command-allowed-domains-to-bash-powershell-and-monitor-in-auto-mode-wi|Added per-command allowed_domains to Bash, PowerShell and Monitor in auto mode]]
- 2026-09-14 · Claude Code: [[Changes/Claude Code/2026-09-14-added-omitclaudemd-to-agent-frontmatter-and-agents-json-letting-custom-and-plugi|Added omitClaudeMd to agent frontmatter and --agents JSON, letting custom an]]
- 2026-09-10 · Cursor: [[Changes/Cursor/2026-09-10-tell-the-coordinator-agent-to-watch-a-slack-channel-run-on-a-schedule-or-follow|Tell the coordinator agent to watch a Slack channel, run on a schedule, or follo]]
- 2026-09-10 · Cursor: [[Changes/Cursor/2026-09-10-access-projects-from-the-left-hand-nav-the-coordinator-agent-in-a-project-doesn|Access Projects from the left-hand nav. The coordinator agent in a project doesn]]
- 2026-09-10 · Cursor: [[Changes/Cursor/2026-09-10-a-project-runs-on-its-own-computer-in-the-cloud-so-closing-your-laptop-doesn-t-s|A Project runs on its own computer in the cloud, so closing your laptop doesn't]]
- 2026-09-10 · Cursor: [[Changes/Cursor/2026-09-10-you-shouldn-t-have-to-onboard-an-agent-every-time-you-start-a-task-each-project|You shouldn't have to onboard an agent every time you start a task. Each Project]]
- 2026-09-04 · Claude Code: [[Changes/Claude Code/2026-09-04-added-append-subagent-system-prompt-file-to-read-the-subagent-system-prompt-from|Added --append-subagent-system-prompt-file to read the subagent system prompt]]
- 2026-09-02 · Cursor: [[Changes/Cursor/2026-09-02-your-codebase-build-outputs-and-secrets-all-stay-on-internal-machines-running-in|Your codebase, build outputs, and secrets all stay on internal machines running]]
- 2026-09-01 · Claude Code: [[Changes/Claude Code/2026-09-01-added-claude-code-subagent-model-force-to-apply-claude-code-subagent-model-or-th|Added CLAUDE_CODE_SUBAGENT_MODEL_FORCE to apply CLAUDE_CODE_SUBAGENT_MODEL (]]
- 2026-09-01 · Claude Code: [[Changes/Claude Code/2026-09-01-added-a-containment-escape-rule-to-auto-mode-so-cloud-metadata-credential-fetche|Added a Containment Escape rule to auto mode so cloud metadata-credential fetche]]
- 2026-08-28 · Claude Code: [[Changes/Claude Code/2026-08-28-added-live-streaming-of-a-foreground-subagent-s-tool-calls-and-results-to-remote|Added live streaming of a foreground subagent's tool calls and results to Remote]]
- 2026-08-27 · Cursor: [[Changes/Cursor/2026-08-27-cursor-now-port-forwards-your-cloud-agent-s-live-environment-straight-to-your-br|Cursor now port-forwards your cloud agent's live environment straight to your br]]
- 2026-08-27 · Cursor: [[Changes/Cursor/2026-08-27-cloud-agents-no-longer-require-a-connected-github-or-other-third-party-scm-provi|Cloud Agents no longer require a connected GitHub or other third-party SCM provi]]
- 2026-08-27 · Claude Code: [[Changes/Claude Code/2026-08-27-added-experimental-cachettl-5m-or-1h-to-agent-frontmatter-a-per-agent-prompt-cac|Added experimental.cacheTtl ("5m" or "1h") to agent frontmatter: a per-age]]
- 2026-08-19 · Cursor: [[Changes/Cursor/2026-08-19-we-re-continuing-to-improve-cloud-agents-and-the-cursor-harness-so-always-on-age|We're continuing to improve cloud agents and the Cursor harness so always-on age]]
- 2026-08-19 · Cursor: [[Changes/Cursor/2026-08-19-cursor-can-now-monitor-your-prs-watch-a-slack-thread-or-run-scheduled-tasks-curs|Cursor can now monitor your PRs, watch a Slack thread, or run scheduled tasks. C]]
- 2026-08-19 · Cursor: [[Changes/Cursor/2026-08-19-use-any-skill-as-a-custom-mode-a-skill-that-stays-pinned-in-the-chat-custom-mode|Use any skill as a Custom Mode: a skill that stays pinned in the chat. Custom mo]]
- 2026-08-19 · Cursor: [[Changes/Cursor/2026-08-19-with-this-release-cloud-agents-can-automatically-pick-up-work-in-response-to-eve|With this release, cloud agents can automatically pick up work in response to ev]]
- 2026-08-19 · Claude Code: [[Changes/Claude Code/2026-08-19-improved-auto-mode-monitor-allow-rules-are-now-set-aside-while-auto-mode-is-acti|Improved auto mode: Monitor allow rules are now set aside while auto mode is a]]
- 2026-08-13 · Cursor: [[Changes/Cursor/2026-08-13-use-your-install-command-for-anything-that-can-be-prepared-ahead-of-time-the-sta|Use your install command for anything that can be prepared ahead of time. The st]]
- 2026-08-13 · Cursor: [[Changes/Cursor/2026-08-13-when-a-bad-commit-or-dependency-update-breaks-your-environment-agents-keep-using|When a bad commit or dependency update breaks your environment, agents keep usin]]
- 2026-08-13 · Cursor: [[Changes/Cursor/2026-08-13-agents-do-their-best-work-when-they-start-in-a-ready-environment-repos-cloned-de|Agents do their best work when they start in a ready environment: repos cloned,]]
- 2026-08-13 · Cursor: [[Changes/Cursor/2026-08-13-cursor-runs-a-new-build-of-your-environment-regularly-when-a-build-succeeds-it-b|Cursor runs a new build of your environment regularly. When a build succeeds, it]]
- 2026-08-13 · Cursor: [[Changes/Cursor/2026-08-13-this-release-introduces-builds-ready-to-use-copies-of-your-development-environme|This release introduces builds: ready-to-use copies of your development environm]]
- 2026-08-13 · Claude Code: [[Changes/Claude Code/2026-08-13-subagent-forking-is-now-on-by-default-a-subagent-type-fork-subagent-inherits-the|Subagent forking is now on by default: a subagent_type: "fork" subagent inheri]]
- 2026-08-06 · Claude Code: [[Changes/Claude Code/2026-08-06-added-a-teleport-hint-in-cloud-sessions-showing-how-to-continue-locally-with-cla|Added a /teleport hint in cloud sessions showing how to continue locally with]]
- 2026-08-06 · Claude Code: [[Changes/Claude Code/2026-08-06-added-a-warning-when-workflow-agents-forked-skills-slash-commands-or-resumed-bac|Added a warning when workflow agents, forked skills, slash commands, or resumed]]
- 2026-07-28 · Cursor: [[Changes/Cursor/2026-07-28-always-on-cloud-agents-that-build-test-and-ship-code-while-you-keep-working|Always-on cloud agents that build, test, and ship code while you keep working.]]
- 2026-07-24 · Claude Code: [[Changes/Claude Code/2026-07-24-added-the-workflowsizeguideline-settings-key-so-the-advisory-dynamic-workflow-si|Added the workflowSizeGuideline settings key so the advisory Dynamic workflow]]
- 2026-07-22 · Cursor: [[Changes/Cursor/2026-07-22-auto-mode-is-now-powered-by-cursor-router|Auto mode is now powered by Cursor Router.]]
- 2026-07-17 · Cursor: [[Changes/Cursor/2026-07-17-cursor-now-responds-with-a-plan-before-it-begins-so-you-can-jump-in-and-redirect|Cursor now responds with a plan before it begins, so you can jump in and redirec]]
- 2026-07-17 · Claude Code: [[Changes/Claude Code/2026-07-17-fork-now-copies-your-conversation-into-a-new-background-session-its-own-row-in-c|/fork now copies your conversation into a new background session (its own row]]
- 2026-07-17 · Claude Code: [[Changes/Claude Code/2026-07-17-added-claude-auto-mode-reset-to-restore-the-default-auto-mode-configuration-with|Added claude auto-mode reset to restore the default auto-mode configuration, w]]
- 2026-07-17 · Claude Code: [[Changes/Claude Code/2026-07-17-added-a-per-session-cap-on-subagent-spawns-default-200-override-with-claude-code|Added a per-session cap on subagent spawns (default 200, override with CLAUDE_C]]
- 2026-07-15 · Claude Code: [[Changes/Claude Code/2026-07-15-added-forward-subagent-text-flag-and-claude-code-forward-subagent-text-environme|Added --forward-subagent-text flag and CLAUDE_CODE_FORWARD_SUBAGENT_TEXT env]]
- 2026-07-15 · Claude Code: [[Changes/Claude Code/2026-07-15-improved-background-agent-result-reporting-claude-now-reports-the-status-of-stil|Improved background agent result reporting — Claude now reports the status of st]]
- 2026-07-14 · Claude Code: [[Changes/Claude Code/2026-07-14-added-claude-code-process-wrapper-agent-view-and-the-background-service-now-hono|Added CLAUDE_CODE_PROCESS_WRAPPER: agent view and the background service now h]]
- 2026-07-14 · Claude Code: [[Changes/Claude Code/2026-07-14-hardened-the-agent-tool-against-indirect-prompt-injection-via-content-a-subagent|Hardened the Agent tool against indirect prompt injection via content a subagent]]
- 2026-07-11 · Claude Code: [[Changes/Claude Code/2026-07-11-improved-agent-view-blocked-session-peeks-now-lead-with-the-question-and-show-a|Improved agent view: blocked session peeks now lead with the question and show a]]
- 2026-07-11 · Claude Code: [[Changes/Claude Code/2026-07-11-auto-mode-is-now-available-without-claude-code-enable-auto-mode-opt-in-on-bedroc|Auto mode is now available without CLAUDE_CODE_ENABLE_AUTO_MODE opt-in on Bedr]]
- 2026-07-10 · Cursor: [[Changes/Cursor/2026-07-10-this-release-makes-it-easier-to-stay-in-flow-with-side-chats-that-run-alongside|This release makes it easier to stay in flow with side chats that run alongside]]
- 2026-07-10 · Cursor: [[Changes/Cursor/2026-07-10-by-default-side-chats-focus-on-reading-searching-and-answering-use-them-to-ask-c|By default, side chats focus on reading, searching, and answering. Use them to a]]
- 2026-07-09 · ChatGPT: [[Changes/ChatGPT/2026-07-09-chatgpt-work-is-an-agent-for-longer-more-involved-tasks-it-can-research-and-anal|ChatGPT Work is an agent for longer, more involved tasks. It can research and an]]
- 2026-07-08 · Claude Code: [[Changes/Claude Code/2026-07-08-improved-agent-view-sessions-that-edit-merge-comment-on-or-push-to-an-existing-p|Improved agent view: sessions that edit, merge, comment on, or push to an existi]]
- 2026-07-08 · Claude Code: [[Changes/Claude Code/2026-07-08-added-an-auto-mode-rule-that-blocks-tampering-with-session-transcript-files|Added an auto mode rule that blocks tampering with session transcript files]]
- 2026-07-07 · Claude Code: [[Changes/Claude Code/2026-07-07-improved-subagent-behavior-agents-are-now-less-likely-to-re-delegate-their-entir|Improved subagent behavior: agents are now less likely to re-delegate their enti]]
- 2026-07-06 · Claude Code: [[Changes/Claude Code/2026-07-06-improved-workflows-agent-list-layout-wider-titles-a-dedicated-time-column-shorte|Improved /workflows agent list layout: wider titles, a dedicated time column,]]
- 2026-07-06 · Claude Code: [[Changes/Claude Code/2026-07-06-added-workflow-run-id-and-workflow-name-opentelemetry-attributes-to-telemetry-em|Added workflow.run_id and workflow.name OpenTelemetry attributes to telemetr]]
- 2026-07-06 · Claude Code: [[Changes/Claude Code/2026-07-06-added-a-dynamic-workflow-size-setting-in-config-for-controlling-how-large-claude|Added a "Dynamic workflow size" setting in /config for controlling how large C]]
- 2026-07-01 · Claude Code: [[Changes/Claude Code/2026-07-01-added-background-agent-notifications-in-claude-agents-sessions-that-need-input-o|Added background agent notifications in claude agents — sessions that need inp]]
- 2026-07-01 · Claude Code: [[Changes/Claude Code/2026-07-01-subagents-now-run-in-the-background-by-default-so-claude-keeps-working-while-the|Subagents now run in the background by default, so Claude keeps working while th]]
- 2026-06-29 · Cursor: [[Changes/Cursor/2026-06-29-cloud-agents-run-in-isolated-virtual-machines-with-full-development-environments|Cloud agents run in isolated virtual machines with full development environments]]
- 2026-06-29 · Cursor: [[Changes/Cursor/2026-06-29-use-remote-control-in-the-agents-window-to-take-an-agent-you-re-running-on-your|Use Remote Control in the Agents Window to take an agent you're running on your]]
- 2026-06-26 · Claude Code: [[Changes/Claude Code/2026-06-26-improved-claude-agents-completed-list-to-fill-available-vertical-space-on-short|Improved claude agents completed list to fill available vertical space; on sho]]
- 2026-06-25 · Claude Code: [[Changes/Claude Code/2026-06-25-added-automode-classifyallshell-setting-to-route-all-bash-powershell-commands-th|Added autoMode.classifyAllShell setting to route all Bash/PowerShell commands]]
- 2026-06-25 · Claude Code: [[Changes/Claude Code/2026-06-25-added-auto-mode-denial-reasons-to-the-transcript-the-denial-toast-and-permission|Added auto-mode denial reasons to the transcript, the denial toast, and /permis]]
- 2026-06-22 · Claude Code: [[Changes/Claude Code/2026-06-22-added-status-filtering-press-f-to-the-workflows-agent-detail-view|Added status filtering (press f) to the /workflows agent detail view]]
- 2026-06-22 · Claude Code: [[Changes/Claude Code/2026-06-22-added-teammatemode-iterm2-setting-with-a-warning-when-auto-mode-cannot-find-the|Added teammateMode: "iterm2" setting with a warning when auto mode cannot find]]
- 2026-06-19 · Claude Code: [[Changes/Claude Code/2026-06-19-improved-auto-mode-safety-destructive-git-commands-git-reset-hard-git-checkout-g|Improved auto mode safety: destructive git commands (git reset --hard, git ch]]
- 2026-06-17 · Cursor: [[Changes/Cursor/2026-06-17-use-in-cloud-to-spin-up-a-cloud-subagent-in-its-own-vm-to-work-on-the-next-task|Use /in-cloud to spin up a cloud subagent in its own VM to work on the next task]]
- 2026-06-15 · Claude Code: [[Changes/Claude Code/2026-06-15-nested-claude-directories-the-agent-workflow-and-output-style-closest-to-the-wor|Nested .claude/ directories: the agent, workflow, and output-style closest to]]
- 2026-06-15 · Claude Code: [[Changes/Claude Code/2026-06-15-improved-auto-mode-subagent-spawns-are-now-evaluated-by-the-classifier-before-la|Improved auto mode: subagent spawns are now evaluated by the classifier before l]]
- 2026-06-10 · Cursor: [[Changes/Cursor/2026-06-10-available-in-cursor-3-7-and-on-cursor-com-agents-with-support-in-cli-coming-soon|Available in Cursor 3.7+ and on cursor.com/agents, with support in CLI coming so]]
- 2026-06-10 · Claude Code: [[Changes/Claude Code/2026-06-10-sub-agents-can-now-spawn-their-own-sub-agents-up-to-5-levels-deep|Sub-agents can now spawn their own sub-agents (up to 5 levels deep)]]
- 2026-06-05 · Cursor: [[Changes/Cursor/2026-06-05-ask-the-agent-to-make-one-match-the-other-remove-repeated-content-or-adjust-a-gr|Ask the agent to make one match the other, remove repeated content, or adjust a]]
- 2026-06-04 · Cursor: [[Changes/Cursor/2026-06-04-by-default-a-local-sdk-agent-runs-tool-calls-without-asking-for-approval-since-t|By default, a local SDK agent runs tool calls without asking for approval, since]]
- 2026-06-04 · Cursor: [[Changes/Cursor/2026-06-04-before-this-exposing-a-custom-capability-meant-standing-up-your-own-stdio-or-rem|Before this, exposing a custom capability meant standing up your own stdio or re]]
- 2026-06-02 · Claude Code: [[Changes/Claude Code/2026-06-02-claude-agents-rows-now-show-done-total-before-the-detail-when-work-is-fanned-out|claude agents rows now show done/total before the detail when work is fanned]]
- 2026-06-02 · Claude Code: [[Changes/Claude Code/2026-06-02-improved-performance-of-opening-recently-inactive-background-agent-sessions-in-c|Improved performance of opening recently-inactive background agent sessions in ]]
- 2026-05-29 · Cursor: [[Changes/Cursor/2026-05-29-configure-your-run-mode-in-settings-cursor-settings-agents-approvals-execution-y|Configure your run mode in Settings  Cursor Settings  Agents  Approvals & Exe]]
- 2026-05-29 · Cursor: [[Changes/Cursor/2026-05-29-auto-review-is-a-new-run-mode-that-allows-cursor-to-work-for-longer-with-fewer-a|Auto-review is a new run mode that allows Cursor to work for longer with fewer a]]
- 2026-05-29 · Claude Code: [[Changes/Claude Code/2026-05-29-claude-agents-the-agent-field-in-settings-json-is-now-honored-for-dispatched-ses|claude agents: the agent field in settings.json is now honored for dispatc]]
- 2026-05-28 · Claude Code: [[Changes/Claude Code/2026-05-28-introducing-dynamic-workflows-ask-claude-to-create-a-workflow-and-it-orchestrate|Introducing dynamic workflows: ask Claude to create a workflow and it orchestrat]]
- 2026-05-28 · Claude Code: [[Changes/Claude Code/2026-05-28-claude-agents-pr-column-now-shows-pr-n-for-a-single-pr-or-n-prs-for-multiple|claude agents: PR column now shows PR ♯N for a single PR or N PRs for mult]]
- 2026-05-21 · Claude Code: [[Changes/Claude Code/2026-05-21-auto-mode-no-longer-suppresses-askuserquestion-when-the-user-or-a-skill-explicit|Auto mode no longer suppresses AskUserQuestion when the user or a skill explic]]
- 2026-05-20 · Cursor: [[Changes/Cursor/2026-05-20-with-loop-cursor-can-run-a-prompt-repeatedly-on-a-local-schedule-until-a-certain|With /loop, Cursor can run a prompt repeatedly on a local schedule, until a cert]]
- 2026-05-20 · Cursor: [[Changes/Cursor/2026-05-20-use-the-loop-skill-for-local-long-running-agents-for-example-you-can-ask-it-to-c|Use the /loop skill for local long-running agents. For example, you can ask it t]]
- 2026-05-19 · Cursor: [[Changes/Cursor/2026-05-19-assign-work-items-to-cursor-or-mention-cursor-in-a-comment-to-kick-off-a-cloud-a|Assign work items to Cursor, or mention @Cursor in a comment to kick off a cloud]]
- 2026-05-19 · Claude Code: [[Changes/Claude Code/2026-05-19-added-elapsed-duration-to-background-subagent-completion-notifications-e-g-agent|Added elapsed duration to background subagent completion notifications (e.g. "Ag]]
- 2026-05-19 · Claude Code: [[Changes/Claude Code/2026-05-19-added-claude-agents-json-to-list-live-claude-sessions-as-json-for-scripting-tmux|Added claude agents --json to list live Claude sessions as JSON for scripting]]
- 2026-05-19 · Claude Code: [[Changes/Claude Code/2026-05-19-added-agent-id-and-parent-agent-id-attributes-to-claude-code-tool-otel-spans-and|Added agent_id and parent_agent_id attributes to claude_code.tool OTEL spa]]
- 2026-05-19 · Claude Code: [[Changes/Claude Code/2026-05-19-claude-agents-terminal-tab-title-now-shows-the-awaiting-input-count-so-an-alt-ta|claude agents terminal tab title now shows the awaiting-input count so an alt-]]
- 2026-05-19 · Claude Code: [[Changes/Claude Code/2026-05-19-added-resume-support-for-background-sessions-sessions-started-via-claude-bg-or-a|Added /resume support for background sessions — sessions started via claude -]]
- 2026-05-18 · Cursor: [[Changes/Cursor/2026-05-18-composer-2-5-is-now-available-in-cursor|Composer 2.5 is now available in Cursor.]]
- 2026-05-13 · Cursor: [[Changes/Cursor/2026-05-13-this-release-introduces-new-tools-for-teams-to-configure-development-environment|This release introduces new tools for teams to configure development environment]]
- 2026-05-13 · Cursor: [[Changes/Cursor/2026-05-13-this-includes-support-for-build-secrets-making-it-easy-to-securely-access-privat|This includes support for build secrets, making it easy to securely access priva]]
- 2026-05-13 · Cursor: [[Changes/Cursor/2026-05-13-cloud-agents-and-automations-now-support-multi-repo-environments-building-off-ou|Cloud agents and automations now support multi-repo environments, building off o]]
- 2026-05-13 · Cursor: [[Changes/Cursor/2026-05-13-this-release-introduces-quality-of-life-improvements-to-the-agents-window|This release introduces quality-of-life improvements to the Agents Window.]]
- 2026-05-13 · Cursor: [[Changes/Cursor/2026-05-13-files-changes-canvases-prs-browsers-and-terminals-can-expand-to-fill-the-entire|Files, changes, canvases, PRs, browsers, and terminals can expand to fill the en]]
- 2026-05-13 · Cursor: [[Changes/Cursor/2026-05-13-to-take-engineering-tasks-from-start-to-finish-agents-need-a-development-environ|To take engineering tasks from start to finish, agents need a development enviro]]
- 2026-05-13 · Claude Code: [[Changes/Claude Code/2026-05-13-added-claude-agents-cwd-path-to-scope-the-session-list-to-a-directory|Added claude agents --cwd path to scope the session list to a directory]]
- 2026-05-12 · Claude Code: [[Changes/Claude Code/2026-05-12-updated-agent-color-palette|Updated agent color palette]]
- 2026-05-12 · Claude Code: [[Changes/Claude Code/2026-05-12-improved-agent-tool-subagent-type-matching-to-accept-case-and-separator-insensit|Improved Agent tool subagent_type matching to accept case- and separator-insen]]
- 2026-05-11 · Cursor: [[Changes/Cursor/2026-05-11-mention-cursor-in-any-teams-channel-to-delegate-a-task-to-a-cloud-agent-or-pull|Mention @Cursor in any Teams channel to delegate a task to a cloud agent or pull]]
- 2026-05-11 · Claude Code: [[Changes/Claude Code/2026-05-11-added-agent-view-research-preview-a-single-list-of-every-claude-code-session-run|Added agent view (Research Preview): a single list of every Claude Code session]]
- 2026-04-24 · Cursor: [[Changes/Cursor/2026-04-24-we-ve-added-new-and-improved-worktrees-in-the-agents-window|We've added new and improved worktrees in the Agents Window.]]
- 2026-04-24 · Cursor: [[Changes/Cursor/2026-04-24-with-multitask-cursor-will-run-async-subagents-to-parallelize-your-requests-inst|With /multitask, Cursor will run async subagents to parallelize your requests in]]
- 2026-04-24 · Cursor: [[Changes/Cursor/2026-04-24-if-you-already-have-messages-in-the-queue-you-can-ask-cursor-to-multitask-on-the|If you already have messages in the queue, you can ask Cursor to multitask on th]]
- 2026-04-24 · Cursor: [[Changes/Cursor/2026-04-24-this-release-introduces-a-new-way-to-multitask-with-async-subagents-an-improved|This release introduces a new way to multitask with async subagents, an improved]]
- 2026-04-23 · Claude Code: [[Changes/Claude Code/2026-04-23-print-mode-now-honors-the-agent-s-tools-and-disallowedtools-frontmatter-matching|--print mode now honors the agent's tools: and disallowedTools: frontmatte]]
- 2026-04-22 · Claude Code: [[Changes/Claude Code/2026-04-22-forked-subagents-can-now-be-enabled-on-external-builds-by-setting-claude-code-fo|Forked subagents can now be enabled on external builds by setting CLAUDE_CODE_F]]
- 2026-04-22 · Claude Code: [[Changes/Claude Code/2026-04-22-agent-frontmatter-mcpservers-are-now-loaded-for-main-thread-agent-sessions-via-a|Agent frontmatter mcpServers are now loaded for main-thread agent sessions via]]
- 2026-04-14 · Cursor: [[Changes/Cursor/2026-04-14-ask-a-quick-side-question-without-derailing-the-agent-s-main-task-btw-allows-you|Ask a quick side question without derailing the agent's main task. /btw allows y]]
- 2026-04-13 · Cursor: [[Changes/Cursor/2026-04-13-split-your-current-view-into-panes-to-run-and-manage-several-agents-in-parallel|Split your current view into panes to run and manage several agents in parallel.]]
- 2026-04-13 · Cursor: [[Changes/Cursor/2026-04-13-this-release-introduces-improvements-to-our-agents-window-interface-as-part-of-c|This release introduces improvements to our Agents Window interface as part of C]]
- 2026-04-10 · Claude Code: [[Changes/Claude Code/2026-04-10-ultraplan-and-other-remote-session-features-now-auto-create-a-default-cloud-envi|/ultraplan and other remote-session features now auto-create a default cloud e]]
- 2026-04-09 · Claude Code: [[Changes/Claude Code/2026-04-09-added-monitor-tool-for-streaming-events-from-background-scripts|Added Monitor tool for streaming events from background scripts]]
- 2026-04-08 · Claude Code: [[Changes/Claude Code/2026-04-08-added-n-running-indicator-in-agents-next-to-agent-types-with-live-subagent-insta|Added ● N running indicator in /agents next to agent types with live subagen]]
- 2026-04-02 · Cursor: [[Changes/Cursor/2026-04-02-to-try-the-agents-window-upgrade-cursor-and-type-cmd-shift-p-agents-window|To try the Agents Window, upgrade Cursor and type Cmd+Shift+P - Agents Window.]]
- 2026-04-02 · Cursor: [[Changes/Cursor/2026-04-02-it-s-simpler-more-powerful-and-centered-around-agents-while-keeping-the-depth-of|It's simpler, more powerful, and centered around agents, while keeping the depth]]
- 2026-04-02 · Cursor: [[Changes/Cursor/2026-04-02-in-the-agents-window-you-can-use-design-mode-to-annotate-and-target-ui-elements|In the Agents Window, you can use Design Mode to annotate and target UI elements]]
- 2026-04-01 · Claude Code: [[Changes/Claude Code/2026-04-01-added-named-subagents-to-mention-typeahead-suggestions|Added named subagents to @ mention typeahead suggestions]]
- 2026-04-01 · Claude Code: [[Changes/Claude Code/2026-04-01-added-permissiondenied-hook-that-fires-after-auto-mode-classifier-denials-return|Added PermissionDenied hook that fires after auto mode classifier denials — re]]
- 2026-03-26 · Claude Code: [[Changes/Claude Code/2026-03-26-added-taskcreated-hook-that-fires-when-a-task-is-created-via-taskcreate|Added TaskCreated hook that fires when a task is created via TaskCreate]]
- 2026-03-25 · Cursor: [[Changes/Cursor/2026-03-25-cursor-now-supports-self-hosted-cloud-agents-that-keep-your-code-and-tool-execut|Cursor now supports self-hosted cloud agents that keep your code and tool execut]]
- 2026-03-25 · Cursor: [[Changes/Cursor/2026-03-25-your-codebase-build-outputs-and-secrets-all-stay-on-internal-machines-running-in|Your codebase, build outputs, and secrets all stay on internal machines running]]
- 2026-03-10 · Claude Code: [[Changes/Claude Code/2026-03-10-added-optional-description-argument-to-plan-e-g-plan-fix-the-auth-bug-that-enter|Added optional description argument to /plan (e.g., /plan fix the auth bug)]]
- 2026-03-04 · Cursor: [[Changes/Cursor/2026-03-04-cursor-is-now-available-in-intellij-idea-pycharm-webstorm-and-other-jetbrains-id|Cursor is now available in IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains]]
- 2026-03-04 · Cursor: [[Changes/Cursor/2026-03-04-with-cursor-acp-developers-who-rely-on-jetbrains-for-java-and-multilanguage-supp|With Cursor ACP, developers who rely on JetBrains for Java and multilanguage sup]]
- 2026-02-28 · Claude Code: [[Changes/Claude Code/2026-02-28-added-http-hooks-which-can-post-json-to-a-url-and-receive-json-instead-of-runnin|Added HTTP hooks, which can POST JSON to a URL and receive JSON instead of runni]]
- 2026-02-26 · Cursor: [[Changes/Cursor/2026-02-26-autofix-runs-cloud-agents-on-their-own-machines-to-test-changes-and-propose-fixe|Autofix runs cloud agents on their own machines to test changes and propose fixe]]
- 2026-02-24 · Cursor: [[Changes/Cursor/2026-02-24-get-started-at-cursor-com-onboard-to-watch-the-agent-configure-itself-and-record|Get started at cursor.com/onboard to watch the agent configure itself and record]]
- 2026-02-24 · Cursor: [[Changes/Cursor/2026-02-24-after-onboarding-onto-your-codebase-each-agent-runs-in-its-own-isolated-vm-with|After onboarding onto your codebase, each agent runs in its own isolated VM with]]
- 2026-02-24 · Cursor: [[Changes/Cursor/2026-02-24-cloud-agents-can-now-use-the-software-they-create-to-test-changes-and-demo-their|Cloud agents can now use the software they create to test changes and demo their]]
- 2026-02-20 · Claude Code: [[Changes/Claude Code/2026-02-20-added-support-for-isolation-worktree-in-agent-definitions-allowing-agents-to-dec|Added support for isolation: worktree in agent definitions, allowing agents to]]
- 2026-02-18 · Cursor: [[Changes/Cursor/2026-02-18-when-a-plan-is-generated-the-cli-now-shows-a-persistent-decision-menu-you-can-ch|When a plan is generated, the CLI now shows a persistent decision menu. You can]]
- 2026-02-18 · Claude Code: [[Changes/Claude Code/2026-02-18-improved-vs-code-plan-preview-auto-updates-as-claude-iterates-enables-commenting|Improved VS Code plan preview: auto-updates as Claude iterates, enables commenti]]
- 2026-02-17 · Cursor: [[Changes/Cursor/2026-02-17-this-release-introduces-plugins-for-extending-cursor-improvements-to-core-agent|This release introduces plugins for extending Cursor, improvements to core agent]]
- 2026-02-12 · Cursor: [[Changes/Cursor/2026-02-12-cursor-can-now-work-autonomously-over-longer-horizons-to-complete-larger-more-co|Cursor can now work autonomously over longer horizons to complete larger, more c]]
- 2026-02-12 · Cursor: [[Changes/Cursor/2026-02-12-in-research-preview-and-internal-testing-long-running-agents-completed-work-that|In research preview and internal testing, long-running agents completed work tha]]
- 2026-02-12 · Cursor: [[Changes/Cursor/2026-02-12-cursor-s-long-running-agent-is-now-available-at-cursor-com-agents-for-ultra-team|Cursor's long-running agent is now available at cursor.com/agents for Ultra, Tea]]
- 2026-02-06 · Claude Code: [[Changes/Claude Code/2026-02-06-added-teammateidle-and-taskcompleted-hook-events-for-multi-agent-workflows|Added TeammateIdle and TaskCompleted hook events for multi-agent workflows]]
- 2026-02-06 · Claude Code: [[Changes/Claude Code/2026-02-06-added-support-for-restricting-which-sub-agents-can-be-spawned-via-task-agent-typ|Added support for restricting which sub-agents can be spawned via Task(agent_ty]]
- 2026-02-03 · Claude Code: [[Changes/Claude Code/2026-02-03-added-token-count-tool-uses-and-duration-metrics-to-task-tool-results|Added token count, tool uses, and duration metrics to Task tool results]]
- 2026-01-27 · Claude Code: [[Changes/Claude Code/2026-01-27-added-ability-to-delete-tasks-via-the-taskupdate-tool|Added ability to delete tasks via the TaskUpdate tool]]
- 2026-01-23 · Claude Code: [[Changes/Claude Code/2026-01-23-added-env-var-claude-code-enable-tasks-set-to-false-to-keep-the-old-system-tempo|Added env var CLAUDE_CODE_ENABLE_TASKS, set to false to keep the old system]]
- 2026-01-22 · Cursor: [[Changes/Cursor/2026-01-22-subagents-are-independent-agents-specialized-to-handle-discrete-parts-of-a-paren|Subagents are independent agents specialized to handle discrete parts of a paren]]
- 2026-01-22 · Cursor: [[Changes/Cursor/2026-01-22-optionally-you-can-define-custom-subagents-learn-more-in-our-docs|Optionally, you can define custom subagents. Learn more in our docs.]]
- 2026-01-22 · Cursor: [[Changes/Cursor/2026-01-22-agents-are-solving-increasingly-complex-long-running-tasks-across-your-codebase|Agents are solving increasingly complex, long-running tasks across your codebase]]
- 2026-01-22 · Cursor: [[Changes/Cursor/2026-01-22-cursor-includes-default-subagents-for-researching-your-codebase-running-terminal|Cursor includes default subagents for researching your codebase, running termina]]
- 2026-01-16 · Cursor: [[Changes/Cursor/2026-01-16-use-plan-mode-to-design-your-approach-before-coding-cursor-will-ask-clarifying-q|Use Plan mode to design your approach before coding. Cursor will ask clarifying]]
- 2026-01-16 · Cursor: [[Changes/Cursor/2026-01-16-push-your-local-conversation-to-a-cloud-agent-and-let-it-keep-running-while-you|Push your local conversation to a Cloud Agent and let it keep running while you']]
- 2026-01-16 · Claude Code: [[Changes/Claude Code/2026-01-16-added-plansdirectory-setting-to-customize-where-plan-files-are-stored|Added plansDirectory setting to customize where plan files are stored]]
- 2026-01-14 · Claude Code: [[Changes/Claude Code/2026-01-14-added-inline-display-of-agent-s-final-response-in-task-notifications-making-it-e|Added inline display of agent's final response in task notifications, making it]]
- 2026-01-11 · Claude Code: [[Changes/Claude Code/2026-01-11-added-claude-code-disable-background-tasks-environment-variable-to-disable-all-b|Added CLAUDE_CODE_DISABLE_BACKGROUND_TASKS environment variable to disable all]]

### 2025

- 2025-12-22 · Cursor: [[Changes/Cursor/2025-12-22-this-includes-the-core-agent-layout-controls-viewing-code-diffs-and-more-we-will|This includes the core agent, layout controls, viewing code diffs, and more. We]]
- 2025-12-10 · Cursor: [[Changes/Cursor/2025-12-10-plan-mode-now-supports-inline-mermaid-diagrams-allowing-the-agent-to-automatical|Plan Mode now supports inline Mermaid diagrams, allowing the agent to automatica]]
- 2025-12-10 · Cursor: [[Changes/Cursor/2025-12-10-move-elements-update-colors-test-layouts-and-experiment-with-css-in-real-time-th|Move elements, update colors, test layouts, and experiment with CSS in real time]]
- 2025-11-21 · Cursor: [[Changes/Cursor/2025-11-21-when-creating-plans-cursor-responds-with-clarifying-questions-to-improve-the-pla|When creating plans, Cursor responds with clarifying questions to improve the pl]]
- 2025-11-21 · Cursor: [[Changes/Cursor/2025-11-21-all-grep-commands-run-by-the-agent-are-now-instant|All grep commands run by the agent are now instant.]]
- 2025-10-29 · Cursor: [[Changes/Cursor/2025-10-29-run-up-to-eight-agents-in-parallel-on-a-single-prompt-this-uses-git-worktrees-or|Run up to eight agents in parallel on a single prompt. This uses git worktrees o]]
- 2025-09-29 · Cursor: [[Changes/Cursor/2025-09-29-you-can-now-observe-control-and-extend-the-agent-loop-using-custom-scripts-hooks|You can now observe, control, and extend the Agent loop using custom scripts. Ho]]
- 2025-09-29 · Cursor: [[Changes/Cursor/2025-09-29-agent-can-take-screenshots-improve-ui-and-debug-client-issues-read-more-about-br|Agent can take screenshots, improve UI, and debug client issues. Read more about]]
- 2025-09-29 · Cursor: [[Changes/Cursor/2025-09-29-cursor-can-now-write-detailed-plans-before-starting-complex-tasks-this-allows-ag|Cursor can now write detailed plans before starting complex tasks. This allows a]]
- 2025-09-29 · ChatGPT: [[Changes/ChatGPT/2025-09-29-we-re-introducing-instant-checkout-in-chatgpt-and-the-agentic-commerce-protocol-8cbf19|We’re introducing Instant Checkout in ChatGPT and the Agentic Commerce Protocol]]
- 2025-08-21 · Cursor: [[Changes/Cursor/2025-08-21-get-native-os-notifications-when-an-agent-run-finishes-or-when-input-is-required|Get native OS notifications when an agent run finishes or when input is required]]
- 2025-08-21 · Cursor: [[Changes/Cursor/2025-08-21-you-can-now-start-background-agents-directly-from-linear-delegate-tasks-to-curso|You can now start Background Agents directly from Linear. Delegate tasks to Curs]]
- 2025-08-06 · Cursor: [[Changes/Cursor/2025-08-06-sending-messages-while-cursor-is-working-now-does-a-better-job-of-steering-the-a|Sending messages while Cursor is working now does a better job of steering the a]]
- 2025-07-29 · Cursor: [[Changes/Cursor/2025-07-29-agents-can-now-use-your-native-terminal-a-new-terminal-will-be-created-when-need|Agents can now use your native terminal. A new terminal will be created when nee]]
- 2025-07-03 · Cursor: [[Changes/Cursor/2025-07-03-the-agent-breaks-down-longer-tasks-with-dependencies-visible-to-you-in-chat-and|The agent breaks down longer tasks with dependencies, visible to you in chat and]]
- 2025-07-03 · Cursor: [[Changes/Cursor/2025-07-03-you-can-now-queue-follow-up-messages-for-agent-once-it-s-done-with-current-task|You can now queue follow-up messages for Agent once it's done with current task.]]
- 2025-07-03 · Cursor: [[Changes/Cursor/2025-07-03-agents-now-plan-ahead-with-structured-to-do-lists-making-long-horizon-tasks-easi|Agents now plan ahead with structured to-do lists, making long-horizon tasks eas]]
- 2025-06-12 · Cursor: [[Changes/Cursor/2025-06-12-agents-run-remotely-in-a-secure-environment-and-you-ll-get-updates-directly-in-s|Agents run remotely in a secure environment and you'll get updates directly in S]]
- 2025-06-12 · Cursor: [[Changes/Cursor/2025-06-12-you-can-now-launch-background-agents-directly-from-slack-by-mentioning-cursor-ag|You can now launch Background Agents directly from Slack by mentioning @Cursor.]]
- 2025-06-04 · Cursor: [[Changes/Cursor/2025-06-04-since-we-released-background-agent-our-remote-coding-agent-in-early-access-a-few|Since we released Background Agent, our remote coding agent, in early access a f]]
- 2025-06-04 · Cursor: [[Changes/Cursor/2025-06-04-this-release-brings-bugbot-for-code-review-a-first-look-at-memories-one-click-mc|This release brings Bugbot for code review, a first look at memories, one-click]]
- 2025-04-15 · Cursor: [[Changes/Cursor/2025-04-15-for-auto-attached-rules-with-path-patterns-defined-agent-will-now-automatically|For Auto Attached rules with path patterns defined, Agent will now automatically]]
- 2025-04-15 · Cursor: [[Changes/Cursor/2025-04-15-we-ve-also-fixed-a-long-standing-issue-where-always-attached-rules-now-persist-a|We’ve also fixed a long-standing issue where Always attached rules now persist a]]
- 2025-04-15 · Cursor: [[Changes/Cursor/2025-04-15-reviewing-agent-generated-code-is-now-easier-with-a-built-in-diff-view-at-the-en|Reviewing agent generated code is now easier with a built-in diff view at the en]]
- 2025-01-23 · Cursor: [[Changes/Cursor/2025-01-23-cursor-rules-users-can-write-several-repository-level-rules-to-disk-in-the-curso|.cursor/rules: Users can write several repository-level rules to disk in the .cu]]
- 2025-01-23 · Cursor: [[Changes/Cursor/2025-01-23-agent-sees-recent-changes-the-agent-can-use-a-tool-to-see-your-recent-changes-it|Agent sees recent changes: The agent can use a tool to see your recent changes.]]

### 2024

- 2024-12-17 · Cursor: [[Changes/Cursor/2024-12-17-docs-git-web-and-folder-are-now-available-in-the-agent|@docs, @git, @web, and @folder are now available in the agent]]
- 2024-12-17 · Cursor: [[Changes/Cursor/2024-12-17-agent-auto-saves-changes-to-disk|Agent auto-saves changes to disk]]
- 2024-08-02 · Cursor: [[Changes/Cursor/2024-08-02-concurrent-composers-support-composer-control-panel-and-various-bug-fixes-such-a|Concurrent composers support, composer control panel, and various bug fixes such]]
- 2024-02-15 · Cursor: [[Changes/Cursor/2024-02-15-interpreter-mode-we-ve-made-some-big-improvements-to-the-backend-powering-interp|Interpreter Mode: We've made some big improvements to the backend powering inter]]

### 2023

- 2023-07-10 · Cursor: [[Changes/Cursor/2023-07-10-the-goal-you-write-an-interface-specification-and-an-agent-writes-both-the-tests|The goal: you write an interface specification, and an agent writes both the tes]]
- 2023-07-10 · Cursor: [[Changes/Cursor/2023-07-10-this-nightly-build-comes-with-experimental-interface-agent-support|This nightly build comes with experimental interface agent support!]]
- 2023-07-06 · Cursor: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Welcome to the first nightly release! It comes with agents, which we aren't rele]]
<!-- chronolog:end -->

## Change Cards
<!-- chronolog:begin region="cards" -->
Active changes: 190. Use the dated links above to inspect each card.
<!-- chronolog:end -->