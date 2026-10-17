---
created: '2023-07-06'
date: '2026-10-14'
description: 'Research question: what changed in delegated execution?'
machine_hash: 5ac783bd5b83cce474e3cf931eadbd0e614e31b9eb320b9c43a6e670fea8578e
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

<!-- chronolog:begin region="header" -->
# Agent Mode

247 tracked changes across ChatGPT, Claude Code and Cursor · 2023-07-06 → 2026-10-14 · Claude Code averages 6.9 cards per release, Cursor 4.0, ChatGPT 1.7
<!-- chronolog:end -->

## Research summary
<!-- chronolog:begin region="narrative" -->
**Research question: what changed in delegated execution?**

Cursor's [2025-05-15 release](https://cursor.com/changelog/0-50) introduces Background Agent for parallel task execution. The [2025-06-04 release](https://cursor.com/changelog/1-0) expands access to the remote coding agent, with privacy-mode limitations at that time. This is a supported within-product expansion of the same named capability.

ChatGPT's [2026-07-09 Work announcement](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#introducing-chatgpt-work) describes longer research and creation tasks across apps and files, with user direction and approvals. [Dots on 2026-09-29](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#meet-your-dot) adds ongoing goals on a cloud computer, with plan and regional restrictions. These are general-work agents; they are not interchangeable with Cursor's repository-oriented remote coding agent.

Claude Code's [v2.1.296](https://github.com/anthropics/claude-code/releases/tag/v2.1.296) adds a workflow-subagent model setting and per-subagent auto-compaction. These are controls over an existing execution system, not its launch. Our dated Claude Code Releases coverage starts at v2.0.73, so its first appearance here cannot establish when agent functionality first existed.

**Uncertainty and scope:** tracked-products-only. Similar names and dates do not establish identical autonomy, reliability, adoption, or influence. The timeline below is a sequence of evidence, not a diffusion claim. Generic permission fixes and unrelated uses of “mode” do not by themselves qualify as agent capabilities.
<!-- chronolog:end -->

## Key moments
<!-- chronolog:begin region="moments" -->
Auto-selected; edit `key_moments` in editorial.yaml to curate.

| Quarter | ChatGPT | Claude Code | Cursor |
| --- | --- | --- | --- |
| 2026 Q4 | · | 2026-10-05 [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-url-to-set-up-the-managed-agents-pattern\|Added /claude-api managed-agents-onboard url to set up the Managed Agents…]] | 2026-10-06 [[Changes/Cursor/2026-10-06-remote-control-doesn-t-move-your-agents-anywhere-it-keeps-running-on-your-comput\|Agents keep running on your computer]] |
| 2026 Q3 | 2026-09-29 [[Changes/ChatGPT/2026-09-29-we-re-introducing-dots-always-on-agents-in-chatgpt-that-can-take-on-ongoing-work-24bef5\|ChatGPT introduces dots]] | 2026-08-13 [[Changes/Claude Code/2026-08-13-subagent-forking-is-now-on-by-default-a-subagent-type-fork-subagent-inherits-the\|Subagent forking is now on by default]]<br>2026-07-11 [[Changes/Claude Code/2026-07-11-auto-mode-is-now-available-without-claude-code-enable-auto-mode-opt-in-on-bedroc\|Auto mode is now available without CLAUDE_CODE_ENABLE_AUTO_MODE opt-in on Bedrock…]] | 2026-09-10 [[Changes/Cursor/2026-09-10-a-project-runs-on-its-own-computer-in-the-cloud-so-closing-your-laptop-doesn-t-s\|Powered by Cloud Agents]]<br>2026-09-02 [[Changes/Cursor/2026-09-02-run-on-your-sandboxes\|Run on your sandboxes]]<br>2026-08-27 [[Changes/Cursor/2026-08-27-cursor-now-port-forwards-your-cloud-agent-s-live-environment-straight-to-your-br\|A live preview, right in the browser]]<br>2026-08-19 [[Changes/Cursor/2026-08-19-custom-modes\|Custom modes]]<br>2026-08-17 [[Changes/Cursor/2026-08-17-agents-in-every-repo\|Agents in every repo]] |
| 2026 Q2 | · | 2026-05-28 [[Changes/Claude Code/2026-05-28-introducing-dynamic-workflows-ask-claude-to-create-a-workflow-and-it-orchestrate\|Introducing dynamic workflows]]<br>2026-05-19 [[Changes/Claude Code/2026-05-19-added-resume-support-for-background-sessions-sessions-started-via-claude-bg-or-a\|Added /resume support for background sessions]] | 2026-06-29 [[Changes/Cursor/2026-06-29-remote-control-3ec330\|Remote Control]] |
| 2026 Q1 | · | · | 2026-02-17 [[Changes/Cursor/2026-02-17-async-subagents\|Async subagents]] |
| 2025 Q4 | · | · | 2025-12-18 [[Changes/Cursor/2025-12-18-shared-agent-transcripts-164030\|Shared agent transcripts]] |
| 2025 Q3 | 2025-09-29 [[Changes/ChatGPT/2025-09-29-we-re-introducing-instant-checkout-in-chatgpt-and-the-agentic-commerce-protocol-8cbf19\|ChatGPT introduces Instant Checkout and the Agentic Commerce Protocol that powers…]] | · | 2025-09-29 [[Changes/Cursor/2025-09-29-hooks-beta\|Hooks (beta)]] |
| 2025 Q2 | · | · | 2025-06-04 [[Changes/Cursor/2025-06-04-agent-in-jupyter-notebooks\|Agent in Jupyter Notebooks]] |
| 2025 Q1 | · | · | 2025-03-23 [[Changes/Cursor/2025-03-23-built-in-modes-custom-modes-beta\|Built-in modes & custom modes (beta)]] |
<!-- chronolog:end -->

<!-- chronolog:begin region="scope" -->
> [!info]- How to read this timeline
> Scope: tracked-products-only. Entries show same-theme chronology; they do not establish equivalent capabilities, adoption, or causation.
<!-- chronolog:end -->

## Timeline
<!-- chronolog:begin region="timeline" -->
### 2026 · 191 entries (ChatGPT 2 · Claude Code 115 · Cursor 74)

#### 2026-10

- 2026-10-14 · **Claude Code** · [[Changes/Claude Code/2026-10-14-5-agent-mode-changes-in-v2-1-299|5 Agent Mode changes in v2.1.299]] · Digest
- 2026-10-14 · **Claude Code** · [[Changes/Claude Code/2026-10-14-3-agent-mode-changes-in-v2-1-300|3 Agent Mode changes in v2.1.300]] · Digest
- 2026-10-09 · **Claude Code** · [[Changes/Claude Code/2026-10-09-3-agent-mode-changes-in-v2-1-296|3 Agent Mode changes in v2.1.296]] · Digest
- 2026-10-08 · **Claude Code** · [[Changes/Claude Code/2026-10-08-3-agent-mode-changes-in-v2-1-295|3 Agent Mode changes in v2.1.295]] · Digest
- 2026-10-07 · **Claude Code** · [[Changes/Claude Code/2026-10-07-2-agent-mode-changes-in-v2-1-293|2 Agent Mode changes in v2.1.293]] · Digest
- 2026-10-06 · **Claude Code** · [[Changes/Claude Code/2026-10-06-3-agent-mode-changes-in-v2-1-292|3 Agent Mode changes in v2.1.292]] · Digest
- 2026-10-06 · **Cursor** · [[Changes/Cursor/2026-10-06-remote-control-doesn-t-move-your-agents-anywhere-it-keeps-running-on-your-comput|Agents keep running on your computer]] · Launch
- 2026-10-05 · **Claude Code** · [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-url-to-set-up-the-managed-agents-pattern|Added /claude-api managed-agents-onboard url to set up the Managed Agents…]]
- 2026-10-05 · **Claude Code** · [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-quickstart-name-to-build-a-console-quick|Added /claude-api managed-agents-onboard quickstart-name to build a Console…]]
- 2026-10-05 · **Claude Code** · [[Changes/Claude Code/2026-10-05-4-agent-mode-changes-in-v2-1-290|4 Agent Mode changes in v2.1.290]] · Digest
- 2026-10-02 · **Claude Code** · [[Changes/Claude Code/2026-10-02-4-agent-mode-changes-in-v2-1-288|4 Agent Mode changes in v2.1.288]] · Digest
- 2026-10-01 · **Claude Code** · [[Changes/Claude Code/2026-10-01-4-agent-mode-changes-in-v2-1-287|4 Agent Mode changes in v2.1.287]] · Digest

#### 2026-09

- 2026-09-30 · **Claude Code** · [[Changes/Claude Code/2026-09-30-6-agent-mode-changes-in-v2-1-286|6 Agent Mode changes in v2.1.286]] · Digest
- 2026-09-29 · **ChatGPT** · [[Changes/ChatGPT/2026-09-29-we-re-introducing-dots-always-on-agents-in-chatgpt-that-can-take-on-ongoing-work-24bef5|ChatGPT introduces dots]] · Launch
- 2026-09-29 · **Claude Code** · [[Changes/Claude Code/2026-09-29-2-agent-mode-changes-in-v2-1-285|2 Agent Mode changes in v2.1.285]] · Digest
- 2026-09-28 · **Claude Code** · [[Changes/Claude Code/2026-09-28-added-a-yes-but-ask-again-next-time-answer-to-auto-mode-s-prompt-before-a-read-o|Added a "Yes, but ask again next time" answer to auto mode's prompt before a read…]]
- 2026-09-25 · **Claude Code** · [[Changes/Claude Code/2026-09-25-improved-startup-claude-p-and-claude-code-remote-no-longer-load-the-interactive|Improved startup: claude -p and Claude Code Remote no longer load the interactive…]]
- 2026-09-24 · **Claude Code** · [[Changes/Claude Code/2026-09-24-2-agent-mode-changes-in-v2-1-282|2 Agent Mode changes in v2.1.282]] · Digest
- 2026-09-23 · **Claude Code** · [[Changes/Claude Code/2026-09-23-9-agent-mode-changes-in-v2-1-281|9 Agent Mode changes in v2.1.281]] · Digest
- 2026-09-23 · **Cursor** · [[Changes/Cursor/2026-09-23-when-rollouts-detects-a-regression-it-names-the-change-it-suspects-and-notifies|When Rollouts detects a regression, it names the change it suspects and notifies…]]
- 2026-09-22 · **Claude Code** · [[Changes/Claude Code/2026-09-22-2-agent-mode-changes-in-v2-1-280|2 Agent Mode changes in v2.1.280]] · Digest
- 2026-09-19 · **Claude Code** · [[Changes/Claude Code/2026-09-19-added-an-auto-mode-server-row-to-status-showing-whether-this-session-s-auto-mode|Added an Auto mode server row to /status showing whether this session's auto…]]
- 2026-09-18 · **Claude Code** · [[Changes/Claude Code/2026-09-18-4-agent-mode-changes-in-v2-1-277|4 Agent Mode changes in v2.1.277]] · Digest
- 2026-09-17 · **Claude Code** · [[Changes/Claude Code/2026-09-17-vscode-improved-the-agent-map-the-pill-counts-running-agents-and-turns-red-after|VSCode Improved the agent map]]
- 2026-09-15 · **Claude Code** · [[Changes/Claude Code/2026-09-15-changed-auto-mode-on-bedrock-vertex-and-foundry-to-use-the-local-classifier-by-d|Changed auto mode on Bedrock, Vertex and Foundry to use the local classifier…]]
- 2026-09-14 · **Claude Code** · [[Changes/Claude Code/2026-09-14-7-agent-mode-changes-in-v2-1-271|7 Agent Mode changes in v2.1.271]] · Digest
- 2026-09-11 · **Claude Code** · [[Changes/Claude Code/2026-09-11-2-agent-mode-changes-in-v2-1-269|2 Agent Mode changes in v2.1.269]] · Digest
- 2026-09-10 · **Claude Code** · [[Changes/Claude Code/2026-09-10-improved-auto-mode-denials-the-message-claude-receives-now-names-the-rule-that-b|Improved auto mode denials]]
- 2026-09-10 · **Cursor** · [[Changes/Cursor/2026-09-10-a-project-runs-on-its-own-computer-in-the-cloud-so-closing-your-laptop-doesn-t-s|Powered by Cloud Agents]] · Launch
- 2026-09-10 · **Cursor** · [[Changes/Cursor/2026-09-10-subscriptions|Subscriptions]] · Launch
- 2026-09-08 · **Claude Code** · [[Changes/Claude Code/2026-09-08-improved-workflows-agent-detail-tool-calls-are-marked-running-failed-or-done-the|Improved /workflows agent detail]]
- 2026-09-04 · **Claude Code** · [[Changes/Claude Code/2026-09-04-2-agent-mode-changes-in-v2-1-261|2 Agent Mode changes in v2.1.261]] · Digest
- 2026-09-03 · **Claude Code** · [[Changes/Claude Code/2026-09-03-2-agent-mode-changes-in-v2-1-260|2 Agent Mode changes in v2.1.260]] · Digest
- 2026-09-02 · **Claude Code** · [[Changes/Claude Code/2026-09-02-2-agent-mode-changes-in-v2-1-259|2 Agent Mode changes in v2.1.259]] · Digest
- 2026-09-02 · **Cursor** · [[Changes/Cursor/2026-09-02-run-on-your-sandboxes|Run on your sandboxes]] · Launch
- 2026-09-02 · **Cursor** · [[Changes/Cursor/2026-09-02-cursor-supports-self-hosted-machines-which-let-you-keep-tool-execution-entirely|Cursor supports self-hosted machines, which let you keep tool execution entirely…]]
- 2026-09-01 · **Claude Code** · [[Changes/Claude Code/2026-09-01-5-agent-mode-changes-in-v2-1-257|5 Agent Mode changes in v2.1.257]] · Digest

#### 2026-08

- 2026-08-28 · **Claude Code** · [[Changes/Claude Code/2026-08-28-4-agent-mode-changes-in-v2-1-251|4 Agent Mode changes in v2.1.251]] · Digest
- 2026-08-27 · **Claude Code** · [[Changes/Claude Code/2026-08-27-3-agent-mode-changes-in-v2-1-248|3 Agent Mode changes in v2.1.248]] · Digest
- 2026-08-27 · **Cursor** · [[Changes/Cursor/2026-08-27-cloud-agents-no-longer-require-a-connected-github-or-other-third-party-scm-provi|Cloud Agents no longer require a connected GitHub or other third-party SCM provider…]]
- 2026-08-27 · **Cursor** · [[Changes/Cursor/2026-08-27-cursor-now-port-forwards-your-cloud-agent-s-live-environment-straight-to-your-br|A live preview, right in the browser]] · Launch
- 2026-08-25 · **Claude Code** · [[Changes/Claude Code/2026-08-25-improved-subagent-results-a-subagent-that-stops-at-its-maxturns-limit-now-return|Improved subagent results]]
- 2026-08-21 · **Claude Code** · [[Changes/Claude Code/2026-08-21-2-agent-mode-changes-in-v2-1-239|2 Agent Mode changes in v2.1.239]] · Digest
- 2026-08-19 · **Claude Code** · [[Changes/Claude Code/2026-08-19-4-agent-mode-changes-in-v2-1-236|4 Agent Mode changes in v2.1.236]] · Digest
- 2026-08-19 · **Cursor** · [[Changes/Cursor/2026-08-19-custom-modes|Custom modes]] · Launch
- 2026-08-19 · **Cursor** · [[Changes/Cursor/2026-08-19-we-re-continuing-to-improve-cloud-agents-and-the-cursor-harness-so-always-on-age-1d1294|We're continuing to improve cloud agents and the Cursor harness so always-on agents…]]
- 2026-08-19 · **Cursor** · [[Changes/Cursor/2026-08-19-subscriptions|Subscriptions]] · Launch
- 2026-08-19 · **Cursor** · [[Changes/Cursor/2026-08-19-steering-improvements|Steering improvements]] · Launch
- 2026-08-19 · **Cursor** · [[Changes/Cursor/2026-08-19-subagents-on-their-own-machines|Subagents on their own machines]] · Launch
- 2026-08-19 · **Cursor** · [[Changes/Cursor/2026-08-19-goal|/goal]] · Launch
- 2026-08-17 · **Claude Code** · [[Changes/Claude Code/2026-08-17-removed-the-redundant-allowed-by-auto-mode-classifier-line-that-auto-mode-showed|Removed the redundant "Allowed by auto mode classifier" line that auto mode showed…]]
- 2026-08-17 · **Cursor** · [[Changes/Cursor/2026-08-17-agents-in-every-repo|Agents in every repo]] · Launch
- 2026-08-14 · **Claude Code** · [[Changes/Claude Code/2026-08-14-improved-claude-self-hosted-runner-session-start-time-the-session-branch-is-now|Improved claude self-hosted-runner session start time]]
- 2026-08-13 · **Claude Code** · [[Changes/Claude Code/2026-08-13-4-agent-mode-changes-in-v2-1-232|4 Agent Mode changes in v2.1.232]] · Digest
- 2026-08-13 · **Claude Code** · [[Changes/Claude Code/2026-08-13-subagent-forking-is-now-on-by-default-a-subagent-type-fork-subagent-inherits-the|Subagent forking is now on by default]]
- 2026-08-13 · **Cursor** · [[Changes/Cursor/2026-08-13-2-agent-mode-changes-in-08-13-26|2 Agent Mode changes in 08.13.26]] · Digest
- 2026-08-13 · **Cursor** · [[Changes/Cursor/2026-08-13-agents-do-their-best-work-when-they-start-in-a-ready-environment-repos-cloned-de-6161c7|Agents do their best work when they start in a ready environment]]
- 2026-08-13 · **Cursor** · [[Changes/Cursor/2026-08-13-when-a-bad-commit-or-dependency-update-breaks-your-environment-agents-keep-using|More resilient agent runs]] · Launch
- 2026-08-12 · **Claude Code** · [[Changes/Claude Code/2026-08-12-improved-workflow-fan-outs-to-stagger-same-prefix-sibling-agents-so-subsequent-a|Improved workflow fan-outs to stagger same-prefix sibling agents so subsequent…]]
- 2026-08-07 · **Claude Code** · [[Changes/Claude Code/2026-08-07-removed-the-200-subagent-per-session-spawn-cap-long-running-sessions-no-longer-r|Removed the 200-subagent-per-session spawn cap]]
- 2026-08-06 · **Claude Code** · [[Changes/Claude Code/2026-08-06-2-agent-mode-changes-in-v2-1-223|2 Agent Mode changes in v2.1.223]] · Digest

#### 2026-07

- 2026-07-29 · **Cursor** · [[Changes/Cursor/2026-07-29-inbox|Inbox]] · Launch
- 2026-07-28 · **Cursor** · [[Changes/Cursor/2026-07-28-always-on-cloud-agents-that-build-test-and-ship-code-while-you-keep-working-725c7c|Always-on cloud agents that build, test, and ship code while you keep working]]
- 2026-07-24 · **Claude Code** · [[Changes/Claude Code/2026-07-24-4-agent-mode-changes-in-v2-1-219|4 Agent Mode changes in v2.1.219]] · Digest
- 2026-07-22 · **Claude Code** · [[Changes/Claude Code/2026-07-22-changed-plan-mode-with-auto-to-no-longer-prompt-for-bash-commands-the-static-ana|Changed plan mode with auto to no longer prompt for Bash commands the static…]]
- 2026-07-22 · **Cursor** · [[Changes/Cursor/2026-07-22-auto-mode-is-now-powered-by-cursor-router|Auto mode is now powered by Cursor Router]]
- 2026-07-21 · **Claude Code** · [[Changes/Claude Code/2026-07-21-2-agent-mode-changes-in-v2-1-217|2 Agent Mode changes in v2.1.217]] · Digest
- 2026-07-18 · **Claude Code** · [[Changes/Claude Code/2026-07-18-added-reasoning-effort-to-the-subagentstatusline-payload-so-custom-agent-rows-ca|Added reasoning effort to the subagentStatusLine payload, so custom agent rows can…]]
- 2026-07-17 · **Claude Code** · [[Changes/Claude Code/2026-07-17-7-agent-mode-changes-in-v2-1-212|7 Agent Mode changes in v2.1.212]] · Digest
- 2026-07-15 · **Claude Code** · [[Changes/Claude Code/2026-07-15-2-agent-mode-changes-in-v2-1-211|2 Agent Mode changes in v2.1.211]] · Digest
- 2026-07-14 · **Claude Code** · [[Changes/Claude Code/2026-07-14-4-agent-mode-changes-in-v2-1-208|4 Agent Mode changes in v2.1.208]] · Digest
- 2026-07-14 · **Claude Code** · [[Changes/Claude Code/2026-07-14-3-agent-mode-changes-in-v2-1-210|3 Agent Mode changes in v2.1.210]] · Digest
- 2026-07-11 · **Claude Code** · [[Changes/Claude Code/2026-07-11-2-agent-mode-changes-in-v2-1-207|2 Agent Mode changes in v2.1.207]] · Digest
- 2026-07-11 · **Claude Code** · [[Changes/Claude Code/2026-07-11-auto-mode-is-now-available-without-claude-code-enable-auto-mode-opt-in-on-bedroc|Auto mode is now available without CLAUDE_CODE_ENABLE_AUTO_MODE opt-in on Bedrock…]]
- 2026-07-10 · **Claude Code** · [[Changes/Claude Code/2026-07-10-2-agent-mode-changes-in-v2-1-206|2 Agent Mode changes in v2.1.206]] · Digest
- 2026-07-10 · **Cursor** · [[Changes/Cursor/2026-07-10-new-cloud-agent-hooks|New cloud agent hooks]] · Launch
- 2026-07-10 · **Cursor** · [[Changes/Cursor/2026-07-10-this-release-makes-it-easier-to-stay-in-flow-with-side-chats-that-run-alongside|Cursor makes it easier to stay in flow with side chats that run alongside your main…]]
- 2026-07-09 · **ChatGPT** · [[Changes/ChatGPT/2026-07-09-chatgpt-work-is-an-agent-for-longer-more-involved-tasks-it-can-research-and-anal|ChatGPT Work is an agent for longer, more involved tasks]]
- 2026-07-08 · **Claude Code** · [[Changes/Claude Code/2026-07-08-3-agent-mode-changes-in-v2-1-205|3 Agent Mode changes in v2.1.205]] · Digest
- 2026-07-07 · **Claude Code** · [[Changes/Claude Code/2026-07-07-2-agent-mode-changes-in-v2-1-203|2 Agent Mode changes in v2.1.203]] · Digest
- 2026-07-06 · **Claude Code** · [[Changes/Claude Code/2026-07-06-3-agent-mode-changes-in-v2-1-202|3 Agent Mode changes in v2.1.202]] · Digest
- 2026-07-01 · **Claude Code** · [[Changes/Claude Code/2026-07-01-5-agent-mode-changes-in-v2-1-198|5 Agent Mode changes in v2.1.198]] · Digest

#### 2026-06

- 2026-06-29 · **Claude Code** · [[Changes/Claude Code/2026-06-29-2-agent-mode-changes-in-v2-1-196|2 Agent Mode changes in v2.1.196]] · Digest
- 2026-06-29 · **Cursor** · [[Changes/Cursor/2026-06-29-remote-control-3ec330|Remote Control]] · Launch
- 2026-06-29 · **Cursor** · [[Changes/Cursor/2026-06-29-live-activities-and-push-notifications|Live Activities and push notifications]] · Launch
- 2026-06-26 · **Claude Code** · [[Changes/Claude Code/2026-06-26-improved-claude-agents-completed-list-to-fill-available-vertical-space-on-short|Improved claude agents completed list to fill available vertical space]]
- 2026-06-25 · **Claude Code** · [[Changes/Claude Code/2026-06-25-3-agent-mode-changes-in-v2-1-193|3 Agent Mode changes in v2.1.193]] · Digest
- 2026-06-22 · **Claude Code** · [[Changes/Claude Code/2026-06-22-2-agent-mode-changes-in-v2-1-186|2 Agent Mode changes in v2.1.186]] · Digest
- 2026-06-19 · **Claude Code** · [[Changes/Claude Code/2026-06-19-improved-auto-mode-safety-destructive-git-commands-git-reset-hard-git-checkout-g|Improved auto mode safety]]
- 2026-06-17 · **Claude Code** · [[Changes/Claude Code/2026-06-17-improved-the-subagent-panel-idle-subagents-auto-hide-after-30s-the-list-caps-at|Improved the subagent panel]]
- 2026-06-17 · **Cursor** · [[Changes/Cursor/2026-06-17-handoff-between-local-and-cloud|Handoff between local and cloud]] · Launch
- 2026-06-17 · **Cursor** · [[Changes/Cursor/2026-06-17-cloud-subagents-with-in-cloud-eb7958|Cloud subagents with /in-cloud]] · Launch
- 2026-06-15 · **Claude Code** · [[Changes/Claude Code/2026-06-15-2-agent-mode-changes-in-v2-1-178|2 Agent Mode changes in v2.1.178]] · Digest
- 2026-06-10 · **Claude Code** · [[Changes/Claude Code/2026-06-10-sub-agents-can-now-spawn-their-own-sub-agents-up-to-5-levels-deep|Sub-agents can now spawn their own sub-agents (up to 5 levels deep)]]
- 2026-06-08 · **Claude Code** · [[Changes/Claude Code/2026-06-08-2-agent-mode-changes-in-v2-1-169|2 Agent Mode changes in v2.1.169]] · Digest
- 2026-06-06 · **Claude Code** · [[Changes/Claude Code/2026-06-06-claude-agents-typing-a-url-into-the-list-now-filters-to-the-session-whose-first|claude agents: typing a URL into the list now filters to the session whose first…]]
- 2026-06-05 · **Cursor** · [[Changes/Cursor/2026-06-05-ask-the-agent-to-make-one-match-the-other-remove-repeated-content-or-adjust-a-gr|Multi-select elements]] · Launch
- 2026-06-04 · **Claude Code** · [[Changes/Claude Code/2026-06-04-2-agent-mode-changes-in-v2-1-163|2 Agent Mode changes in v2.1.163]] · Digest
- 2026-06-04 · **Cursor** · [[Changes/Cursor/2026-06-04-added-the-ability-for-agents-to-embed-buttons-in-canvases-that-will-run-a-specif|Added the ability for agents to embed buttons in canvases that will run a specific…]]
- 2026-06-04 · **Cursor** · [[Changes/Cursor/2026-06-04-jsonl-and-custom-stores|JSONL and custom stores]] · Launch
- 2026-06-04 · **Cursor** · [[Changes/Cursor/2026-06-04-auto-review|Auto-review]] · Launch
- 2026-06-04 · **Cursor** · [[Changes/Cursor/2026-06-04-nested-subagents|Nested subagents]] · Launch
- 2026-06-04 · **Cursor** · [[Changes/Cursor/2026-06-04-5-agent-mode-changes-in-custom-stores-custom-tools|5 Agent Mode changes in Custom stores, custom tools…]] · Digest
- 2026-06-02 · **Claude Code** · [[Changes/Claude Code/2026-06-02-improved-performance-of-opening-recently-inactive-background-agent-sessions-in-c|Improved performance of opening recently-inactive background agent sessions…]]
- 2026-06-02 · **Claude Code** · [[Changes/Claude Code/2026-06-02-claude-agents-rows-now-show-done-total-before-the-detail-when-work-is-fanned-out|claude agents rows now show done/total before the detail when work is fanned out]]

#### 2026-05

- 2026-05-29 · **Claude Code** · [[Changes/Claude Code/2026-05-29-claude-agents-the-agent-field-in-settings-json-is-now-honored-for-dispatched-ses|claude agents: the agent field in settings.json is now honored for dispatched…]]
- 2026-05-29 · **Cursor** · [[Changes/Cursor/2026-05-29-auto-review-is-a-new-run-mode-that-allows-cursor-to-work-for-longer-with-fewer-a-61df08|Auto-review Run Mode]]
- 2026-05-28 · **Claude Code** · [[Changes/Claude Code/2026-05-28-4-agent-mode-changes-in-v2-1-154|4 Agent Mode changes in v2.1.154]] · Digest
- 2026-05-28 · **Claude Code** · [[Changes/Claude Code/2026-05-28-3-agent-mode-changes-in-v2-1-153|3 Agent Mode changes in v2.1.153]] · Digest
- 2026-05-28 · **Claude Code** · [[Changes/Claude Code/2026-05-28-introducing-dynamic-workflows-ask-claude-to-create-a-workflow-and-it-orchestrate|Introducing dynamic workflows]] · Launch
- 2026-05-27 · **Claude Code** · [[Changes/Claude Code/2026-05-27-2-agent-mode-changes-in-v2-1-152|2 Agent Mode changes in v2.1.152]] · Digest
- 2026-05-21 · **Claude Code** · [[Changes/Claude Code/2026-05-21-auto-mode-no-longer-suppresses-askuserquestion-when-the-user-or-a-skill-explicit|Auto mode no longer suppresses AskUserQuestion when the user or a skill explicitly…]]
- 2026-05-20 · **Cursor** · [[Changes/Cursor/2026-05-20-loop-skill|/loop skill]] · Launch
- 2026-05-19 · **Claude Code** · [[Changes/Claude Code/2026-05-19-added-resume-support-for-background-sessions-sessions-started-via-claude-bg-or-a|Added /resume support for background sessions]]
- 2026-05-19 · **Claude Code** · [[Changes/Claude Code/2026-05-19-3-agent-mode-changes-in-v2-1-144|3 Agent Mode changes in v2.1.144]] · Digest
- 2026-05-19 · **Claude Code** · [[Changes/Claude Code/2026-05-19-3-agent-mode-changes-in-v2-1-145|3 Agent Mode changes in v2.1.145]] · Digest
- 2026-05-19 · **Cursor** · [[Changes/Cursor/2026-05-19-assign-work-items-to-cursor-or-mention-cursor-in-a-comment-to-kick-off-a-cloud-a-1c05f0|Assign work items to Cursor, or mention @Cursor in a comment to kick off a cloud agent]]
- 2026-05-18 · **Cursor** · [[Changes/Cursor/2026-05-18-composer-2-5-is-now-available-in-cursor|Composer 2.5 is now available in Cursor]] · Launch
- 2026-05-15 · **Claude Code** · [[Changes/Claude Code/2026-05-15-2-agent-mode-changes-in-v2-1-143|2 Agent Mode changes in v2.1.143]] · Digest
- 2026-05-14 · **Claude Code** · [[Changes/Claude Code/2026-05-14-improved-hook-configuration-error-configuring-a-prompt-or-agent-type-hook-for-se|Improved hook configuration error]]
- 2026-05-13 · **Claude Code** · [[Changes/Claude Code/2026-05-13-4-agent-mode-changes-in-v2-1-141|4 Agent Mode changes in v2.1.141]] · Digest
- 2026-05-13 · **Cursor** · [[Changes/Cursor/2026-05-13-improved-agent-led-environment-setup|Improved agent-led environment setup]]
- 2026-05-13 · **Cursor** · [[Changes/Cursor/2026-05-13-this-release-introduces-quality-of-life-improvements-to-the-agents-window|Cursor introduces quality-of-life improvements to the Agents Window]] · Launch
- 2026-05-13 · **Cursor** · [[Changes/Cursor/2026-05-13-cloud-agents-and-automations-now-support-multi-repo-environments-building-off-ou|Multi-repo environments]] · Launch
- 2026-05-13 · **Cursor** · [[Changes/Cursor/2026-05-13-to-take-engineering-tasks-from-start-to-finish-agents-need-a-development-environ-e47512|To take engineering tasks from start to finish, agents need a development…]]
- 2026-05-12 · **Claude Code** · [[Changes/Claude Code/2026-05-12-2-agent-mode-changes-in-v2-1-140|2 Agent Mode changes in v2.1.140]] · Digest
- 2026-05-11 · **Claude Code** · [[Changes/Claude Code/2026-05-11-2-agent-mode-changes-in-v2-1-139|2 Agent Mode changes in v2.1.139]] · Digest
- 2026-05-07 · **Cursor** · [[Changes/Cursor/2026-05-07-added-the-ability-to-control-explore-subagent-behavior-from-settings-choose-a-sp|Added the ability to control Explore subagent behavior from settings]]
- 2026-05-04 · **Claude Code** · [[Changes/Claude Code/2026-05-04-auto-mode-when-the-classifier-can-t-evaluate-an-action-the-error-now-includes-a|Auto mode: when the classifier can't evaluate an action, the error now includes…]]

#### 2026-04

- 2026-04-29 · **Cursor** · [[Changes/Cursor/2026-04-29-3-agent-mode-changes-in-build-programmatic-agents|3 Agent Mode changes in Build programmatic agents…]] · Digest
- 2026-04-28 · **Claude Code** · [[Changes/Claude Code/2026-04-28-2-agent-mode-changes-in-v2-1-121|2 Agent Mode changes in v2.1.121]] · Digest
- 2026-04-24 · **Cursor** · [[Changes/Cursor/2026-04-24-multi-root-workspaces-in-agents-window|Multi-root workspaces in Agents Window]] · Launch
- 2026-04-24 · **Cursor** · [[Changes/Cursor/2026-04-24-worktrees-in-agents-window-44e81c|Worktrees in Agents Window]] · Launch
- 2026-04-24 · **Cursor** · [[Changes/Cursor/2026-04-24-this-release-introduces-a-new-way-to-multitask-with-async-subagents-an-improved|Cursor introduces a new way to multitask with async subagents, an improved worktrees…]] · Launch
- 2026-04-24 · **Cursor** · [[Changes/Cursor/2026-04-24-multitask-in-agents-window-9bc7ed|Multitask in Agents Window]] · Launch
- 2026-04-23 · **Claude Code** · [[Changes/Claude Code/2026-04-23-2-agent-mode-changes-in-v2-1-118|2 Agent Mode changes in v2.1.118]] · Digest
- 2026-04-23 · **Claude Code** · [[Changes/Claude Code/2026-04-23-2-agent-mode-changes-in-v2-1-119|2 Agent Mode changes in v2.1.119]] · Digest
- 2026-04-22 · **Claude Code** · [[Changes/Claude Code/2026-04-22-2-agent-mode-changes-in-v2-1-117|2 Agent Mode changes in v2.1.117]] · Digest
- 2026-04-20 · **Claude Code** · [[Changes/Claude Code/2026-04-20-2-agent-mode-changes-in-v2-1-116|2 Agent Mode changes in v2.1.116]] · Digest
- 2026-04-17 · **Claude Code** · [[Changes/Claude Code/2026-04-17-subagents-that-stall-mid-stream-now-fail-with-a-clear-error-after-10-minutes-ins|Subagents that stall mid-stream now fail with a clear error after 10 minutes instead…]]
- 2026-04-16 · **Claude Code** · [[Changes/Claude Code/2026-04-16-auto-mode-no-longer-requires-enable-auto-mode|Auto mode no longer requires --enable-auto-mode]]
- 2026-04-14 · **Cursor** · [[Changes/Cursor/2026-04-14-ask-a-quick-side-question-without-derailing-the-agent-s-main-task-btw-allows-you|/btw support in CLI]] · Launch
- 2026-04-13 · **Cursor** · [[Changes/Cursor/2026-04-13-tiled-layout-2f03f6|Tiled layout]] · Launch
- 2026-04-13 · **Cursor** · [[Changes/Cursor/2026-04-13-this-release-introduces-improvements-to-our-agents-window-interface-as-part-of-c|Cursor introduces improvements to our Agents Window interface as part of Cursor 3]] · Launch
- 2026-04-13 · **Cursor** · [[Changes/Cursor/2026-04-13-branch-selection-in-empty-state|Branch selection in empty state]] · Launch
- 2026-04-13 · **Cursor** · [[Changes/Cursor/2026-04-13-3-agent-mode-changes-in-3-1|3 Agent Mode changes in 3.1]] · Digest
- 2026-04-10 · **Claude Code** · [[Changes/Claude Code/2026-04-10-ultraplan-and-other-remote-session-features-now-auto-create-a-default-cloud-envi|/ultraplan and other remote-session features now auto-create a default cloud…]]
- 2026-04-09 · **Claude Code** · [[Changes/Claude Code/2026-04-09-3-agent-mode-changes-in-v2-1-98|3 Agent Mode changes in v2.1.98]] · Digest
- 2026-04-08 · **Claude Code** · [[Changes/Claude Code/2026-04-08-2-agent-mode-changes-in-v2-1-97|2 Agent Mode changes in v2.1.97]] · Digest
- 2026-04-02 · **Cursor** · [[Changes/Cursor/2026-04-02-4-agent-mode-changes-in-3-0|4 Agent Mode changes in 3.0]] · Digest
- 2026-04-02 · **Cursor** · [[Changes/Cursor/2026-04-02-design-mode|Design Mode]] · Launch
- 2026-04-02 · **Cursor** · [[Changes/Cursor/2026-04-02-agents-window-da5689|Agents Window]] · Launch
- 2026-04-01 · **Claude Code** · [[Changes/Claude Code/2026-04-01-3-agent-mode-changes-in-v2-1-89|3 Agent Mode changes in v2.1.89]] · Digest

#### 2026-03

- 2026-03-27 · **Claude Code** · [[Changes/Claude Code/2026-03-27-auto-mode-now-shows-unavailable-for-your-plan-when-disabled-by-plan-restrictions|Auto mode now shows "unavailable for your plan" when disabled by plan restrictions…]]
- 2026-03-26 · **Claude Code** · [[Changes/Claude Code/2026-03-26-2-agent-mode-changes-in-v2-1-84|2 Agent Mode changes in v2.1.84]] · Digest
- 2026-03-25 · **Claude Code** · [[Changes/Claude Code/2026-03-25-agents-can-now-declare-initialprompt-in-frontmatter-to-auto-submit-a-first-turn|Agents can now declare initialPrompt in frontmatter to auto-submit a first turn]]
- 2026-03-25 · **Cursor** · [[Changes/Cursor/2026-03-25-cursor-now-supports-self-hosted-cloud-agents-that-keep-your-code-and-tool-execut-e411f3|Self-hosted Cloud Agents]]
- 2026-03-17 · **Claude Code** · [[Changes/Claude Code/2026-03-17-2-agent-mode-changes-in-v2-1-77|2 Agent Mode changes in v2.1.77]] · Digest
- 2026-03-14 · **Claude Code** · [[Changes/Claude Code/2026-03-14-improved-background-agent-behavior-killing-a-background-agent-now-preserves-its|Improved background agent behavior]]
- 2026-03-10 · **Claude Code** · [[Changes/Claude Code/2026-03-10-2-agent-mode-changes-in-v2-1-72|2 Agent Mode changes in v2.1.72]] · Digest
- 2026-03-05 · **Claude Code** · [[Changes/Claude Code/2026-03-05-2-agent-mode-changes-in-v2-1-69|2 Agent Mode changes in v2.1.69]] · Digest
- 2026-03-04 · **Cursor** · [[Changes/Cursor/2026-03-04-cursor-is-now-available-in-intellij-idea-pycharm-webstorm-and-other-jetbrains-id-2dc9cd|Cursor is now available in IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains…]]
- 2026-03-03 · **Cursor** · [[Changes/Cursor/2026-03-03-improved-reliability-for-longer-running-agent-sessions|Improved reliability for longer-running agent sessions]]

#### 2026-02

- 2026-02-28 · **Claude Code** · [[Changes/Claude Code/2026-02-28-added-http-hooks-which-can-post-json-to-a-url-and-receive-json-instead-of-runnin|Added HTTP hooks, which can POST JSON to a URL and receive JSON instead of running…]]
- 2026-02-26 · **Cursor** · [[Changes/Cursor/2026-02-26-autofix-runs-cloud-agents-on-their-own-machines-to-test-changes-and-propose-fixe|Autofix runs cloud agents on their own machines to test changes and propose fixes…]]
- 2026-02-24 · **Cursor** · [[Changes/Cursor/2026-02-24-cloud-agents-can-now-use-the-software-they-create-to-test-changes-and-demo-their-c922e9|Cloud Agents with Computer Use]]
- 2026-02-20 · **Claude Code** · [[Changes/Claude Code/2026-02-20-2-agent-mode-changes-in-v2-1-50|2 Agent Mode changes in v2.1.50]] · Digest
- 2026-02-18 · **Claude Code** · [[Changes/Claude Code/2026-02-18-2-agent-mode-changes-in-v2-1-47|2 Agent Mode changes in v2.1.47]] · Digest
- 2026-02-18 · **Cursor** · [[Changes/Cursor/2026-02-18-2-agent-mode-changes-in-cli-improvements-and-mermaid-ascii|2 Agent Mode changes in CLI Improvements and Mermaid ASCII…]] · Digest
- 2026-02-17 · **Cursor** · [[Changes/Cursor/2026-02-17-async-subagents|Async subagents]] · Launch
- 2026-02-17 · **Cursor** · [[Changes/Cursor/2026-02-17-6-agent-mode-changes-in-2-5|6 Agent Mode changes in 2.5]] · Digest
- 2026-02-17 · **Cursor** · [[Changes/Cursor/2026-02-17-this-release-introduces-plugins-for-extending-cursor-improvements-to-core-agent|Cursor introduces plugins for extending Cursor, improvements to core agent…]] · Launch
- 2026-02-12 · **Cursor** · [[Changes/Cursor/2026-02-12-cursor-can-now-work-autonomously-over-longer-horizons-to-complete-larger-more-co-48843c|Long-running Agents in Research Preview]]
- 2026-02-06 · **Claude Code** · [[Changes/Claude Code/2026-02-06-2-agent-mode-changes-in-v2-1-33|2 Agent Mode changes in v2.1.33]] · Digest
- 2026-02-05 · **Claude Code** · [[Changes/Claude Code/2026-02-05-updated-resume-to-re-use-agent-value-specified-in-previous-conversation-by-defau|Updated --resume to re-use --agent value specified in previous conversation by default]]
- 2026-02-03 · **Claude Code** · [[Changes/Claude Code/2026-02-03-added-token-count-tool-uses-and-duration-metrics-to-task-tool-results|Added token count, tool uses, and duration metrics to Task tool results]]

#### 2026-01

- 2026-01-27 · **Claude Code** · [[Changes/Claude Code/2026-01-27-2-agent-mode-changes-in-v2-1-20|2 Agent Mode changes in v2.1.20]] · Digest
- 2026-01-23 · **Claude Code** · [[Changes/Claude Code/2026-01-23-added-env-var-claude-code-enable-tasks-set-to-false-to-keep-the-old-system-tempo|Added env var CLAUDE_CODE_ENABLE_TASKS, set to false to keep the old system…]]
- 2026-01-22 · **Cursor** · [[Changes/Cursor/2026-01-22-skills|Skills]] · Launch
- 2026-01-22 · **Cursor** · [[Changes/Cursor/2026-01-22-4-agent-mode-changes-in-2-4|4 Agent Mode changes in 2.4]] · Digest
- 2026-01-22 · **Cursor** · [[Changes/Cursor/2026-01-22-agents-are-solving-increasingly-complex-long-running-tasks-across-your-codebase|Agents are solving increasingly complex, long-running tasks across your codebase]]
- 2026-01-22 · **Cursor** · [[Changes/Cursor/2026-01-22-subagents|Subagents]] · Launch
- 2026-01-22 · **Cursor** · [[Changes/Cursor/2026-01-22-clarification-questions-from-the-agent|Clarification questions from the agent]] · Launch
- 2026-01-16 · **Claude Code** · [[Changes/Claude Code/2026-01-16-added-plansdirectory-setting-to-customize-where-plan-files-are-stored|Added plansDirectory setting to customize where plan files are stored]]
- 2026-01-16 · **Cursor** · [[Changes/Cursor/2026-01-16-push-your-local-conversation-to-a-cloud-agent-and-let-it-keep-running-while-you|Handoff to Cloud Agents]] · Launch
- 2026-01-16 · **Cursor** · [[Changes/Cursor/2026-01-16-use-plan-mode-to-design-your-approach-before-coding-cursor-will-ask-clarifying-q|Plan mode in CLI]] · Launch
- 2026-01-16 · **Cursor** · [[Changes/Cursor/2026-01-16-added-hooks-for-session-start-end-prompt-and-stop-for-customizing-agent-lifecycl|Added hooks for session start/end, prompt, and stop for customizing agent lifecycle events]]
- 2026-01-14 · **Claude Code** · [[Changes/Claude Code/2026-01-14-added-inline-display-of-agent-s-final-response-in-task-notifications-making-it-e|Added inline display of agent's final response in task notifications, making…]]
- 2026-01-11 · **Claude Code** · [[Changes/Claude Code/2026-01-11-added-claude-code-disable-background-tasks-environment-variable-to-disable-all-b|Added CLAUDE_CODE_DISABLE_BACKGROUND_TASKS environment variable to disable all…]]
- 2026-01-09 · **Claude Code** · [[Changes/Claude Code/2026-01-09-added-agent-type-to-sessionstart-hook-input-populated-if-agent-is-specified|Added agent_type to SessionStart hook input, populated if --agent is specified]]
- 2026-01-08 · **Cursor** · [[Changes/Cursor/2026-01-08-new-agent-command-is-now-the-primary-cli-entrypoint-cursor-agent-remains-as-a-ba|New agent command is now the primary CLI entrypoint. cursor-agent remains…]]

### 2025 · 51 entries (ChatGPT 2 · Cursor 49)

#### 2025-12

- 2025-12-22 · **Cursor** · [[Changes/Cursor/2025-12-22-2-agent-mode-changes-in-2-3|2 Agent Mode changes in 2.3]] · Digest
- 2025-12-22 · **Cursor** · [[Changes/Cursor/2025-12-22-this-includes-the-core-agent-layout-controls-viewing-code-diffs-and-more-we-will|This includes the core agent, layout controls, viewing code diffs, and more]]
- 2025-12-18 · **Cursor** · [[Changes/Cursor/2025-12-18-shared-agent-transcripts-164030|Shared agent transcripts]] · Launch
- 2025-12-18 · **Cursor** · [[Changes/Cursor/2025-12-18-linux-sandboxing-for-agents|Linux sandboxing for agents]] · Launch
- 2025-12-18 · **Cursor** · [[Changes/Cursor/2025-12-18-service-accounts|Service accounts]] · Launch
- 2025-12-10 · **Cursor** · [[Changes/Cursor/2025-12-10-plan-mode-now-supports-inline-mermaid-diagrams-allowing-the-agent-to-automatical|Plan Mode improvements]] · Launch
- 2025-12-10 · **Cursor** · [[Changes/Cursor/2025-12-10-multi-agent-judging|Multi-agent judging]] · Launch
- 2025-12-10 · **Cursor** · [[Changes/Cursor/2025-12-10-agent-plans-are-now-files-that-can-be-edited-with-normal-tools|Agent plans are now files that can be edited with normal tools]]

#### 2025-11

- 2025-11-21 · **Cursor** · [[Changes/Cursor/2025-11-21-instant-grep-beta|Instant Grep (Beta)]] · Launch
- 2025-11-21 · **Cursor** · [[Changes/Cursor/2025-11-21-2-agent-mode-changes-in-2-1|2 Agent Mode changes in 2.1]] · Digest

#### 2025-10

- 2025-10-29 · **Cursor** · [[Changes/Cursor/2025-10-29-improved-agent-harness|Improved Agent Harness]]
- 2025-10-29 · **Cursor** · [[Changes/Cursor/2025-10-29-background-agents-have-been-renamed-to-cloud-agents|Background Agents have been renamed to Cloud Agents]]
- 2025-10-29 · **Cursor** · [[Changes/Cursor/2025-10-29-cloud-agents|Cloud Agents]] · Launch
- 2025-10-29 · **Cursor** · [[Changes/Cursor/2025-10-29-multi-agents-bb4f56|Multi-Agents]] · Launch

#### 2025-09

- 2025-09-29 · **ChatGPT** · [[Changes/ChatGPT/2025-09-29-we-re-introducing-instant-checkout-in-chatgpt-and-the-agentic-commerce-protocol-8cbf19|ChatGPT introduces Instant Checkout and the Agentic Commerce Protocol that powers…]] · Launch
- 2025-09-29 · **ChatGPT** · [[Changes/ChatGPT/2025-09-29-agentic-commerce-protocol|Agentic Commerce Protocol]] · Launch
- 2025-09-29 · **Cursor** · [[Changes/Cursor/2025-09-29-hooks-beta|Hooks (beta)]] · Launch
- 2025-09-29 · **Cursor** · [[Changes/Cursor/2025-09-29-cursor-can-now-write-detailed-plans-before-starting-complex-tasks-this-allows-ag|Plan Mode]] · Launch
- 2025-09-29 · **Cursor** · [[Changes/Cursor/2025-09-29-monitor-agents-from-menubar|Monitor Agents from menubar]] · Launch
- 2025-09-29 · **Cursor** · [[Changes/Cursor/2025-09-29-5-agent-mode-changes-in-1-7|5 Agent Mode changes in 1.7]] · Digest
- 2025-09-29 · **Cursor** · [[Changes/Cursor/2025-09-29-agent-can-take-screenshots-improve-ui-and-debug-client-issues-read-more-about-br|Browser Controls]] · Launch
- 2025-09-29 · **Cursor** · [[Changes/Cursor/2025-09-29-image-file-support-for-agent|Image file support for Agent]] · Launch
- 2025-09-12 · **Cursor** · [[Changes/Cursor/2025-09-12-3-agent-mode-changes-in-1-6|3 Agent Mode changes in 1.6]] · Digest

#### 2025-08

- 2025-08-21 · **Cursor** · [[Changes/Cursor/2025-08-21-you-can-now-start-background-agents-directly-from-linear-delegate-tasks-to-curso|Run Agents in Linear]] · Launch
- 2025-08-21 · **Cursor** · [[Changes/Cursor/2025-08-21-get-native-os-notifications-when-an-agent-run-finishes-or-when-input-is-required|OS notifications from Agent]] · Launch
- 2025-08-06 · **Cursor** · [[Changes/Cursor/2025-08-06-improved-agent-tools-488891|Improved Agent tools]]
- 2025-08-06 · **Cursor** · [[Changes/Cursor/2025-08-06-github-support-for-background-agents|GitHub support for Background Agents]] · Launch
- 2025-08-06 · **Cursor** · [[Changes/Cursor/2025-08-06-faster-background-agent-startup|Faster Background Agent startup]]
- 2025-08-06 · **Cursor** · [[Changes/Cursor/2025-08-06-sidebar-for-all-agents|Sidebar for all Agents]] · Launch
- 2025-08-06 · **Cursor** · [[Changes/Cursor/2025-08-06-sending-messages-while-cursor-is-working-now-does-a-better-job-of-steering-the-a|More Agent steerability]] · Launch

#### 2025-07

- 2025-07-29 · **Cursor** · [[Changes/Cursor/2025-07-29-agents-can-now-use-your-native-terminal-a-new-terminal-will-be-created-when-need|Share terminal with Agent]] · Launch
- 2025-07-29 · **Cursor** · [[Changes/Cursor/2025-07-29-2-agent-mode-changes-in-1-3|2 Agent Mode changes in 1.3]] · Digest
- 2025-07-03 · **Cursor** · [[Changes/Cursor/2025-07-03-let-agent-resolve-merge-conflicts|Let Agent resolve merge conflicts]] · Launch
- 2025-07-03 · **Cursor** · [[Changes/Cursor/2025-07-03-agent-to-dos-3ffa24|Agent To-dos]] · Launch
- 2025-07-03 · **Cursor** · [[Changes/Cursor/2025-07-03-you-can-now-queue-follow-up-messages-for-agent-once-it-s-done-with-current-task|Queued messages]] · Launch
- 2025-07-03 · **Cursor** · [[Changes/Cursor/2025-07-03-2-agent-mode-changes-in-1-2|2 Agent Mode changes in 1.2]] · Digest
- 2025-07-03 · **Cursor** · [[Changes/Cursor/2025-07-03-background-agent-improvements|Background Agent improvements]] · Launch

#### 2025-06

- 2025-06-12 · **Cursor** · [[Changes/Cursor/2025-06-12-you-can-now-launch-background-agents-directly-from-slack-by-mentioning-cursor-ag|Launch Background Agents directly from Slack by mentioning @Cursor]]
- 2025-06-12 · **Cursor** · [[Changes/Cursor/2025-06-12-improved-background-agent-reliability|Improved Background Agent reliability]]
- 2025-06-04 · **Cursor** · [[Changes/Cursor/2025-06-04-open-background-agent-control-panel-with-cmd-ctrl-e|Open Background Agent control panel with Cmd/Ctrl+E]]
- 2025-06-04 · **Cursor** · [[Changes/Cursor/2025-06-04-agent-in-jupyter-notebooks|Agent in Jupyter Notebooks]] · Launch
- 2025-06-04 · **Cursor** · [[Changes/Cursor/2025-06-04-background-agent-for-everyone-8b35dc|Background Agent for everyone]] · Launch
- 2025-06-04 · **Cursor** · [[Changes/Cursor/2025-06-04-this-release-brings-bugbot-for-code-review-a-first-look-at-memories-one-click-mc|Cursor brings Bugbot for code review, a first look at memories, one-click MCP setup…]] · Launch

#### 2025-05

- 2025-05-15 · **Cursor** · [[Changes/Cursor/2025-05-15-fast-edits-for-long-files-with-agent|Fast edits for long files with Agent]] · Launch
- 2025-05-15 · **Cursor** · [[Changes/Cursor/2025-05-15-background-agent-preview|Background Agent (Preview)]] · Launch

#### 2025-04

- 2025-04-15 · **Cursor** · [[Changes/Cursor/2025-04-15-reviewing-agent-generated-code-is-now-easier-with-a-built-in-diff-view-at-the-en|Making reviews easier]] · Launch

#### 2025-03

- 2025-03-23 · **Cursor** · [[Changes/Cursor/2025-03-23-built-in-modes-custom-modes-beta|Built-in modes & custom modes (beta)]] · Launch

#### 2025-02

- 2025-02-19 · **Cursor** · [[Changes/Cursor/2025-02-19-agent-is-ready-agent-is-now-the-default-mode-bringing-a-more-powerful-and-unifie|Agent is ready: Agent is now the default mode, bringing a more powerful and unified…]]
- 2025-02-19 · **Cursor** · [[Changes/Cursor/2025-02-19-agent-tool-limit-upon-reaching-the-25-tool-call-limit-you-can-press-continue-to|Agent tool limit]]

#### 2025-01

- 2025-01-23 · **Cursor** · [[Changes/Cursor/2025-01-23-agent-sees-recent-changes-the-agent-can-use-a-tool-to-see-your-recent-changes-it|Agent sees recent changes: The agent can use a tool to see your recent changes]]
- 2025-01-23 · **Cursor** · [[Changes/Cursor/2025-01-23-cursor-rules-users-can-write-several-repository-level-rules-to-disk-in-the-curso|.cursor/rules: Users can write several repository-level rules to disk…]]

### 2024 · 2 entries (Cursor 2)

#### 2024-08

- 2024-08-02 · **Cursor** · [[Changes/Cursor/2024-08-02-concurrent-composers-support-composer-control-panel-and-various-bug-fixes-such-a|Concurrent composers support, composer control panel, and various bug fixes such…]]

#### 2024-02

- 2024-02-15 · **Cursor** · [[Changes/Cursor/2024-02-15-interpreter-mode-we-ve-made-some-big-improvements-to-the-backend-powering-interp|Interpreter Mode: We've made some big improvements to the backend powering…]]

### 2023 · 3 entries (Cursor 3)

#### 2023-07

- 2023-07-10 · **Cursor** · [[Changes/Cursor/2023-07-10-this-nightly-build-comes-with-experimental-interface-agent-support|This nightly build comes with experimental interface agent support!]]
- 2023-07-10 · **Cursor** · [[Changes/Cursor/2023-07-10-the-goal-you-write-an-interface-specification-and-an-agent-writes-both-the-tests|The goal: you write an interface specification, and an agent writes both the tests…]]
- 2023-07-06 · **Cursor** · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->