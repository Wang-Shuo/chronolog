---
created: '2023-07-06'
date: '2026-11-06'
description: 'Research question: what changed in delegated execution?'
machine_hash: 3468141b53671d40ffc7cbd3d0f0afbfeee5ca3ec15eff7517716502c95bcbeb
modified: '2026-11-06'
products_involved:
- Aider
- ChatGPT
- Claude Code
- Cline
- Codex CLI
- Cursor
- Gemini CLI
- GitHub Copilot CLI
- OpenHands
- Windsurf
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

584 tracked changes across Aider, ChatGPT, Claude Code, Cline, Codex CLI, Cursor, Gemini CLI, GitHub Copilot CLI, OpenHands and Windsurf · 2023-07-06 → 2026-11-06 · Codex CLI averages 8.0 cards per release, Gemini CLI 7.5, Claude Code 7.0, GitHub Copilot CLI 6.3, Cursor 4.0, OpenHands 3.8, Aider 3.7, Cline 3.0, Windsurf 2.6, ChatGPT 1.7
<!-- chronolog:end -->

## Research summary
<!-- chronolog:begin region="narrative" -->
**Research question: what changed in delegated execution?**

Cursor's [2025-05-15 release](https://cursor.com/changelog/0-50) ([[Releases/Cursor/cursor-2025-05-15-0-50-https-cursor-com-changelog-0-50-dc290998|archived]]) introduces Background Agent for parallel task execution. The [2025-06-04 release](https://cursor.com/changelog/1-0) ([[Releases/Cursor/cursor-2025-06-04-1-0-https-cursor-com-changelog-1-0-237767ca|archived]]) expands access to the same remote coding agent, with privacy-mode limitations at that time, a within-product expansion of one named capability.

ChatGPT's [2026-07-09 Work announcement](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#introducing-chatgpt-work) ([[Releases/ChatGPT/chatgpt-2026-07-09-introducing-chatgpt-work-eff9f272|archived]]) describes longer research and creation tasks across apps and files, with user direction and approvals. [Dots on 2026-09-29](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#meet-your-dot) ([[Releases/ChatGPT/chatgpt-2026-09-29-meet-your-dot-8b9f914b|archived]]) adds ongoing goals on a cloud computer, with plan and regional restrictions. Both are general-work agents, a different scope from Cursor's repository-oriented remote coding agent.

Claude Code's [v2.1.296 on 2026-10-09](https://github.com/anthropics/claude-code/releases/tag/v2.1.296) ([[Releases/Claude Code/claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a|archived]]) adds a workflow-subagent model setting and per-subagent auto-compaction, controls over an execution system that already exists.

**Uncertainty and scope:** this editorial summary covers ChatGPT, Claude Code and Cursor; the timeline includes all tracked products and Claude Code coverage starts at v2.0.73 (2025-12-19), so a first appearance here does not date when agent functionality first existed; similar names and dates do not establish identical autonomy, reliability, adoption or influence, the timeline below is a sequence of evidence rather than a diffusion claim, and generic permission fixes or unrelated uses of “mode” do not count as agent capabilities.
<!-- chronolog:end -->

## Key moments
<!-- chronolog:begin region="moments" -->
| Quarter | Aider | ChatGPT | Claude Code | Cline | Codex CLI | Cursor | Gemini CLI | GitHub Copilot CLI | OpenHands | Windsurf |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **First in archive** | <time datetime="2024-08-27">2024-08-27</time> [[Changes/Aider/2024-08-27-improved-shell-command-prompting\|Improved shell command prompting]] | <time datetime="2025-09-29">2025-09-29</time> [[Changes/ChatGPT/2025-09-29-we-re-introducing-instant-checkout-in-chatgpt-and-the-agentic-commerce-protocol-8cbf19\|ChatGPT introduces Instant Checkout and the Agentic Commerce Protocol that powers…]] | <time datetime="2026-01-09">2026-01-09</time> [[Changes/Claude Code/2026-01-09-added-agent-type-to-sessionstart-hook-input-populated-if-agent-is-specified\|Added agent_type to SessionStart hook input, populated if --agent is specified]] | <time datetime="2025-04-09">2025-04-09</time> [[Changes/Cline/2025-04-09-add-new-create-new-task-tool-to-let-cline-start-a-new-task-autonomously\|Add new 'Create New Task' tool to let Cline start a new task autonomously!]] | <time datetime="2025-07-19">2025-07-19</time> [[Changes/Codex CLI/2025-07-19-https-github-com-openai-codex-pull-1589-changes-ctrl-d-so-it-only-exits-the-tui\|(source link) changes ctrl-d so it only exits the TUI…]] | <time datetime="2023-07-06">2023-07-06</time> [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas\|Agents, new docs]] | <time datetime="2025-07-19">2025-07-19</time> [[Changes/Gemini CLI/2025-07-19-3-agent-mode-changes-in-v0-1-13\|3 Agent Mode changes in v0.1.13]] | <time datetime="2025-10-01">2025-10-01</time> [[Changes/GitHub Copilot CLI/2025-10-01-improved-the-experience-of-writing-prompts-while-the-agent-is-running-up-down-ar\|Improved the experience of writing prompts while the agent is running -- up/down…]] | <time datetime="2024-06-29">2024-06-29</time> [[Changes/OpenHands/2024-06-29-3-agent-mode-changes-in-0-7-0\|3 Agent Mode changes in 0.7.0]] | <time datetime="2025-10-23">2025-10-23</time> [[Changes/Windsurf/2025-10-23-support-and-fixes-for-agents-md\|Support and fixes for AGENTS.md]] |
| 2026 Q3 | · | <time datetime="2026-09-29">2026-09-29</time> [[Changes/ChatGPT/2026-09-29-we-re-introducing-dots-always-on-agents-in-chatgpt-that-can-take-on-ongoing-work-24bef5\|ChatGPT introduces dots]]<br><time datetime="2026-07-09">2026-07-09</time> [[Changes/ChatGPT/2026-07-09-chatgpt-work-is-an-agent-for-longer-more-involved-tasks-it-can-research-and-anal\|ChatGPT Work is an agent for longer, more involved tasks]] | <time datetime="2026-07-11">2026-07-11</time> [[Changes/Claude Code/2026-07-11-auto-mode-is-now-available-without-claude-code-enable-auto-mode-opt-in-on-bedroc\|Auto mode is now available without CLAUDE_CODE_ENABLE_AUTO_MODE opt-in on Bedrock…]] | · | · | <time datetime="2026-09-10">2026-09-10</time> [[Changes/Cursor/2026-09-10-a-project-runs-on-its-own-computer-in-the-cloud-so-closing-your-laptop-doesn-t-s\|Powered by Cloud Agents]] | · | · | · | · |
| 2026 Q2 | · | · | <time datetime="2026-06-10">2026-06-10</time> [[Changes/Claude Code/2026-06-10-sub-agents-can-now-spawn-their-own-sub-agents-up-to-5-levels-deep\|Sub-agents can now spawn their own sub-agents (up to 5 levels deep)]]<br><time datetime="2026-05-28">2026-05-28</time> [[Changes/Claude Code/2026-05-28-introducing-dynamic-workflows-ask-claude-to-create-a-workflow-and-it-orchestrate\|Introducing dynamic workflows]]<br><time datetime="2026-04-16">2026-04-16</time> [[Changes/Claude Code/2026-04-16-auto-mode-no-longer-requires-enable-auto-mode\|Auto mode no longer requires --enable-auto-mode]] | · | · | · | · | · | · | · |
| 2026 Q1 | · | · | · | · | · | <time datetime="2026-01-22">2026-01-22</time> [[Changes/Cursor/2026-01-22-subagents\|Subagents]] | · | · | · | · |
| 2025 Q4 | · | · | archive begins <time datetime="2025-12-19">2025-12-19</time> | · | · | <time datetime="2025-10-29">2025-10-29</time> [[Changes/Cursor/2025-10-29-multi-agents-bb4f56\|Multi-Agents]] | · | · | · | · |
| 2025 Q3 | · | <time datetime="2025-09-29">2025-09-29</time> [[Changes/ChatGPT/2025-09-29-we-re-introducing-instant-checkout-in-chatgpt-and-the-agentic-commerce-protocol-8cbf19\|ChatGPT introduces Instant Checkout and the Agentic Commerce Protocol that powers…]] | <span class="not-archived">not archived</span> | · | · | · | · | archive begins <time datetime="2025-09-26">2025-09-26</time> | · | · |
| 2025 Q2 | · | · | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2025-06-30">2025-06-30</time> | <time datetime="2025-06-04">2025-06-04</time> [[Changes/Cursor/2025-06-04-background-agent-for-everyone-8b35dc\|Background Agent for everyone]]<br><time datetime="2025-05-15">2025-05-15</time> [[Changes/Cursor/2025-05-15-background-agent-preview\|Background Agent (Preview)]] | archive begins <time datetime="2025-06-28">2025-06-28</time> | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2025-04-02">2025-04-02</time> |
| 2025 Q1 | · | · | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <time datetime="2025-02-19">2025-02-19</time> [[Changes/Cursor/2025-02-19-agent-is-ready-agent-is-now-the-default-mode-bringing-a-more-powerful-and-unifie\|Agent is ready: Agent is now the default mode, bringing a more powerful and unified…]] | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> |
| 2023 Q4 → 2024 Q4 | · | · | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-07-28">2024-07-28</time> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-06-04">2024-06-04</time> | <span class="not-archived">not archived</span> |
| 2023 Q3 | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <time datetime="2023-07-06">2023-07-06</time> [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas\|Agents, new docs]] | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |

First in archive: each product's earliest tracked change in this theme. "·" marks a quarter without a key moment, and "not archived" a quarter before the product's archive begins. Archives begin: Aider 2023-06-07 · ChatGPT 2022-12-15 · Claude Code 2025-12-19 · Cline 2024-07-28 · Codex CLI 2025-06-30 · Cursor 2023-03-14 · Gemini CLI 2025-06-28 · GitHub Copilot CLI 2025-09-26 · OpenHands 2024-06-04 · Windsurf 2025-04-02.
<!-- chronolog:end -->

<!-- chronolog:begin region="scope" -->
<details class="disclosure">
<summary>How to read this timeline</summary>

Scope: tracked-products-only. Entries show same-theme chronology; they do not establish equivalent capabilities, adoption, or causation.

</details>
<!-- chronolog:end -->

## Timeline
<!-- chronolog:begin region="timeline" -->
<div class="timeline">

Launches, expansions, pricing and policy changes and standalone announcements come first in each year; fixes, digests and other changes are folded beneath them.

<fieldset class="timeline-filter">
<legend>Show</legend>
<label><input type="radio" name="timeline-product" id="tl-only-all" checked> All</label>
<label><input type="radio" name="timeline-product" id="tl-only-1"> Aider</label>
<label><input type="radio" name="timeline-product" id="tl-only-2"> ChatGPT</label>
<label><input type="radio" name="timeline-product" id="tl-only-3"> Claude Code</label>
<label><input type="radio" name="timeline-product" id="tl-only-4"> Cline</label>
<label><input type="radio" name="timeline-product" id="tl-only-5"> Codex CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-6"> Cursor</label>
<label><input type="radio" name="timeline-product" id="tl-only-7"> Gemini CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-8"> GitHub Copilot CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-9"> OpenHands</label>
<label><input type="radio" name="timeline-product" id="tl-only-10"> Windsurf</label>
</fieldset>

<details class="disclosure">
<summary>2026 · 446 entries (ChatGPT 3 · Claude Code 126 · Cline 12 · Codex CLI 72 · Cursor 89 · Gemini CLI 26 · GitHub Copilot CLI 82 · OpenHands 26 · Windsurf 10)</summary>

**2026-10**

- 2026-10-23 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-10-23-new-agent-window|New Agent Window]] · Launch
- 2026-10-20 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-10-20-deploy-agents-wherever-you-need-them|Deploy agents wherever you need them]] · Launch
- 2026-10-20 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-10-20-evals|Evals]] · Launch
- 2026-10-20 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-10-20-agents-as-code|Agents as code]] · Launch
- 2026-10-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-19-added-claude-api-managed-agents-secure-which-compares-a-managed-agents-agent-s-s|Added /claude-api managed-agents-secure, which compares a Managed Agents agent's…]] · Change
- 2026-10-16 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-10-16-environments-api|Environments API]] · Launch
- 2026-10-16 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-10-16-canvases-from-cloud-agents|Canvases from cloud agents]] · Launch
- 2026-10-06 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-10-06-you-can-now-see-and-reply-to-the-local-agents-running-on-your-computer-from-the|See and reply to the local agents running on your computer from the Cursor iOS app]] · Change
- 2026-10-06 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-10-06-remote-control-doesn-t-move-your-agents-anywhere-it-keeps-running-on-your-comput|Agents keep running on your computer]] · Launch
- 2026-10-05 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-url-to-set-up-the-managed-agents-pattern|Added /claude-api managed-agents-onboard url to set up the Managed Agents…]] · Change
- 2026-10-05 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-quickstart-name-to-build-a-console-quick|Added /claude-api managed-agents-onboard quickstart-name to build a Console…]] · Change

**2026-09**

- 2026-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-29-we-re-introducing-dots-always-on-agents-in-chatgpt-that-can-take-on-ongoing-work-24bef5|ChatGPT introduces dots]] · Launch
- 2026-09-10 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-09-10-a-project-runs-on-its-own-computer-in-the-cloud-so-closing-your-laptop-doesn-t-s|Powered by Cloud Agents]] · Launch
- 2026-09-10 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-09-10-subscriptions|Subscriptions]] · Launch
- 2026-09-02 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-09-02-run-on-your-sandboxes|Run on your sandboxes]] · Launch
- 2026-09-02 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-09-02-computer-use-on-linux-and-mac|Computer use on Linux and Mac]] · Launch

**2026-08**

- 2026-08-27 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-08-27-cursor-now-port-forwards-your-cloud-agent-s-live-environment-straight-to-your-br|A live preview, right in the browser]] · Launch
- 2026-08-19 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-08-19-custom-modes|Custom modes]] · Launch
- 2026-08-19 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-08-19-subscriptions|Subscriptions]] · Launch
- 2026-08-19 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-08-19-steering-improvements|Steering improvements]] · Launch
- 2026-08-19 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-08-19-subagents-on-their-own-machines|Subagents on their own machines]] · Launch
- 2026-08-19 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-08-19-goal|/goal]] · Launch
- 2026-08-17 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-08-17-agents-in-every-repo|Agents in every repo]] · Launch
- 2026-08-13 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-13-subagent-forking-is-now-on-by-default-a-subagent-type-fork-subagent-inherits-the|Subagent forking is now on by default]] · Change
- 2026-08-13 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-08-13-when-a-bad-commit-or-dependency-update-breaks-your-environment-agents-keep-using|More resilient agent runs]] · Launch

**2026-07**

- 2026-07-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-07-29-on-iphone-and-ipad-the-review-screen-now-covers-the-full-pr-comments-checks-and|A full review surface]] · Launch
- 2026-07-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-07-29-inbox|Inbox]] · Launch
- 2026-07-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-11-auto-mode-is-now-available-without-claude-code-enable-auto-mode-opt-in-on-bedroc|Auto mode is now available without CLAUDE_CODE_ENABLE_AUTO_MODE opt-in on Bedrock…]] · Expansion
- 2026-07-10 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-07-10-new-cloud-agent-hooks|New cloud agent hooks]] · Launch

**2026-06**

- 2026-06-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-29-cloud-agents-on-mobile-1bc371|Cloud agents on mobile]] · Launch
- 2026-06-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-29-remote-control-3ec330|Remote Control]] · Launch
- 2026-06-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-29-live-activities-and-push-notifications|Live Activities and push notifications]] · Launch
- 2026-06-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-29-cursor-for-ios-is-now-available-in-public-beta-on-all-paid-plans-launch-and-mana|Cursor for iOS is now available in public beta on all paid plans]] · Launch
- 2026-06-17 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-17-handoff-between-local-and-cloud|Handoff between local and cloud]] · Launch
- 2026-06-17 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-17-this-release-introduces-updates-to-cloud-agents-in-the-agents-window-of-the-curs|Cursor introduces updates to cloud agents in the Agents Window of the Cursor desktop app]] · Launch
- 2026-06-17 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-17-cloud-subagents-with-in-cloud-eb7958|Cloud subagents with /in-cloud]] · Launch
- 2026-06-05 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-05-ask-the-agent-to-make-one-match-the-other-remove-repeated-content-or-adjust-a-gr|Multi-select elements]] · Launch
- 2026-06-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-04-jsonl-and-custom-stores|JSONL and custom stores]] · Launch
- 2026-06-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-04-auto-review|Auto-review]] · Launch
- 2026-06-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-04-nested-subagents|Nested subagents]] · Launch

**2026-05**

- 2026-05-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-28-introducing-dynamic-workflows-ask-claude-to-create-a-workflow-and-it-orchestrate|Introducing dynamic workflows]] · Launch
- 2026-05-27 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-05-27-devin-local|Devin Local]] · Launch
- 2026-05-20 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-20-loop-skill|/loop skill]] · Launch
- 2026-05-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-19-added-resume-support-for-background-sessions-sessions-started-via-claude-bg-or-a|Added /resume support for background sessions]] · Change
- 2026-05-18 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-18-composer-2-5-is-now-available-in-cursor|Composer 2.5 is now available in Cursor]] · Launch
- 2026-05-13 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-13-this-release-introduces-quality-of-life-improvements-to-the-agents-window|Cursor introduces quality-of-life improvements to the Agents Window]] · Launch
- 2026-05-13 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-13-cloud-agents-and-automations-now-support-multi-repo-environments-building-off-ou|Multi-repo environments]] · Launch
- 2026-05-06 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-05-06-agent-command-center|Agent Command Center]] · Launch

**2026-04**

- 2026-04-29 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-04-29-devin-agent-in-windsurf|Devin Agent in Windsurf]] · Launch
- 2026-04-24 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-24-multi-root-workspaces-in-agents-window|Multi-root workspaces in Agents Window]] · Launch
- 2026-04-24 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-24-worktrees-in-agents-window-44e81c|Worktrees in Agents Window]] · Launch
- 2026-04-24 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-24-this-release-introduces-a-new-way-to-multitask-with-async-subagents-an-improved|Cursor introduces a new way to multitask with async subagents, an improved worktrees…]] · Launch
- 2026-04-24 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-24-multitask-in-agents-window-9bc7ed|Multitask in Agents Window]] · Launch
- 2026-04-15 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-04-15-devin-in-windsurf|Devin in Windsurf]] · Launch
- 2026-04-15 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-04-15-agent-command-center|Agent Command Center]] · Launch
- 2026-04-14 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-14-ask-a-quick-side-question-without-derailing-the-agent-s-main-task-btw-allows-you|/btw support in CLI]] · Launch
- 2026-04-13 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-13-tiled-layout-2f03f6|Tiled layout]] · Launch
- 2026-04-13 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-13-this-release-introduces-improvements-to-our-agents-window-interface-as-part-of-c|Cursor introduces improvements to our Agents Window interface as part of Cursor 3]] · Launch
- 2026-04-13 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-13-branch-selection-in-empty-state|Branch selection in empty state]] · Launch
- 2026-04-02 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-02-design-mode|Design Mode]] · Launch
- 2026-04-02 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-02-agents-window-da5689|Agents Window]] · Launch

**2026-03**

- 2026-03-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-03-04-cursor-is-now-available-in-intellij-idea-pycharm-webstorm-and-other-jetbrains-id-2dc9cd|Cursor is now available in IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains…]] · Expansion
- 2026-03-02 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-02-you-can-now-fork-a-thread-into-sub-agents-making-it-easier-to-branch-work-withou|Fork a thread into sub-agents, making it easier to branch work without leaving…]] · Change

**2026-02**

- 2026-02-17 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-02-17-async-subagents|Async subagents]] · Launch
- 2026-02-17 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-02-17-this-release-introduces-plugins-for-extending-cursor-improvements-to-core-agent|Cursor introduces plugins for extending Cursor, improvements to core agent…]] · Launch

**2026-01**

- 2026-01-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-01-22-skills|Skills]] · Launch
- 2026-01-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-01-22-subagents|Subagents]] · Launch
- 2026-01-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-01-22-clarification-questions-from-the-agent|Clarification questions from the agent]] · Launch
- 2026-01-16 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-01-16-push-your-local-conversation-to-a-cloud-agent-and-let-it-keep-running-while-you|Handoff to Cloud Agents]] · Launch
- 2026-01-16 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-01-16-use-plan-mode-to-design-your-approach-before-coding-cursor-will-ask-clarifying-q|Plan mode in CLI]] · Launch
- 2026-01-13 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-01-13-new-features-and-improvements|New Features and Improvements]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 375 (ChatGPT 2 · Claude Code 119 · Cline 12 · Codex CLI 71 · Cursor 34 · Gemini CLI 26 · GitHub Copilot CLI 82 · OpenHands 26 · Windsurf 3)</summary>

**2026-11**

- 2026-11-06 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-11-06-6-agent-mode-changes-in-rust-v0-167-0|6 Agent Mode changes in rust-v0.167.0]] · Digest
- 2026-11-06 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-11-06-34-agent-mode-changes-in-v1-0-106|34 Agent Mode changes in v1.0.106]] · Digest
- 2026-11-05 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-11-05-2-agent-mode-changes-in-v1-36-0|2 Agent Mode changes in v1.36.0]] · Digest
- 2026-11-03 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-11-03-3-agent-mode-changes-in-v1-35-0|3 Agent Mode changes in v1.35.0]] · Digest

**2026-10**

- 2026-10-31 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-31-2-agent-mode-changes-in-v2-1-316|2 Agent Mode changes in v2.1.316]] · Digest
- 2026-10-30 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-30-3-agent-mode-changes-in-v2-1-314|3 Agent Mode changes in v2.1.314]] · Digest
- 2026-10-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-29-7-agent-mode-changes-in-rust-v0-166-0|7 Agent Mode changes in rust-v0.166.0]] · Digest
- 2026-10-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-27-2-agent-mode-changes-in-v2-1-312|2 Agent Mode changes in v2.1.312]] · Digest
- 2026-10-27 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-27-4-agent-mode-changes-in-rust-v0-165-0|4 Agent Mode changes in rust-v0.165.0]] · Digest
- 2026-10-27 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-10-27-feat-verify-stand-in-for-digitalocean-so-managed-agents-can-be-verified-by-enyst|feat(verify): stand in for DigitalOcean so Managed Agents can be verified]] · Change
- 2026-10-26 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-26-2-agent-mode-changes-in-v2-1-311|2 Agent Mode changes in v2.1.311]] · Digest
- 2026-10-26 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-10-26-the-status-bar-no-longer-disappears-after-you-switch-from-agent-mode-to-ide-mode|The status bar no longer disappears after you switch from Agent mode to IDE mode]] · Change
- 2026-10-23 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-23-2-agent-mode-changes-in-v2-1-310|2 Agent Mode changes in v2.1.310]] · Digest
- 2026-10-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-23-13-agent-mode-changes-in-rust-v0-164-0|13 Agent Mode changes in rust-v0.164.0]] · Digest
- 2026-10-23 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-10-23-3-agent-mode-changes-in-v3-11-212|3 Agent Mode changes in v3.11.212]] · Digest
- 2026-10-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-22-changed-the-claude-api-skill-to-build-managed-agents-subagent-teams-on-multiagen|Changed the /claude-api skill to build Managed Agents subagent teams…]] · Change
- 2026-10-22 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-10-22-chore-bump-agent-server-to-1-57-0-by-all-hands-bot-in-https-github-com-openhands|chore: bump agent-server to 1.57.0]] · Change
- 2026-10-21 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-21-improved-fork-subagents-launched-together-each-is-now-told-which-launch-is-its-o|Improved fork subagents launched together]] · Change
- 2026-10-20 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-10-20-the-agent-sdk-is-generally-available-today-read-the-docs-and-get-started|The Agent SDK is generally available today]] · Change
- 2026-10-20 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-10-20-the-agent-sdk-is-available-today-it-allows-you-to-define-an-agent-as-a-folder-of|The Agent SDK is available today]] · Change
- 2026-10-20 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-10-20-5-agent-mode-changes-in-v1-29-0|5 Agent Mode changes in v1.29.0]] · Digest
- 2026-10-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-19-2-agent-mode-changes-in-v2-1-304|2 Agent Mode changes in v2.1.304]] · Digest
- 2026-10-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-19-2-agent-mode-changes-in-v1-0-100|2 Agent Mode changes in v1.0.100]] · Digest
- 2026-10-19 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-10-19-3-agent-mode-changes-in-v1-28-0|3 Agent Mode changes in v1.28.0]] · Digest
- 2026-10-19 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-10-19-chore-bump-agent-server-to-1-56-0-by-all-hands-bot-in-https-github-com-openhands|chore: bump agent-server to 1.56.0]] · Change
- 2026-10-16 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-10-16-multiple-agents-that-can-work-on-different-parts-of-a-task-in-parallel-you-can-f|Multiple agents that can work on different parts of a task in parallel]] · Change
- 2026-10-16 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-16-6-agent-mode-changes-in-v2-1-302|6 Agent Mode changes in v2.1.302]] · Digest
- 2026-10-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-15-14-agent-mode-changes-in-rust-v0-163-0|14 Agent Mode changes in rust-v0.163.0]] · Digest
- 2026-10-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-14-5-agent-mode-changes-in-v2-1-299|5 Agent Mode changes in v2.1.299]] · Digest
- 2026-10-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-14-3-agent-mode-changes-in-v2-1-300|3 Agent Mode changes in v2.1.300]] · Digest
- 2026-10-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-13-3-agent-mode-changes-in-v1-0-97|3 Agent Mode changes in v1.0.97]] · Digest
- 2026-10-12 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-10-12-4-agent-mode-changes-in-v1-27-0|4 Agent Mode changes in v1.27.0]] · Digest
- 2026-10-09 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-09-3-agent-mode-changes-in-v2-1-296|3 Agent Mode changes in v2.1.296]] · Digest
- 2026-10-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-08-4-agent-mode-changes-in-v2-1-295|4 Agent Mode changes in v2.1.295]] · Digest
- 2026-10-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-08-14-agent-mode-changes-in-rust-v0-162-0|14 Agent Mode changes in rust-v0.162.0]] · Digest
- 2026-10-07 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-07-2-agent-mode-changes-in-v2-1-293|2 Agent Mode changes in v2.1.293]] · Digest
- 2026-10-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-07-9-agent-mode-changes-in-rust-v0-161-0|9 Agent Mode changes in rust-v0.161.0]] · Digest
- 2026-10-07 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-07-clicking-a-truncated-compact-shell-command-expands-it|Clicking a truncated compact shell command expands it]] · Change
- 2026-10-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-06-3-agent-mode-changes-in-v2-1-292|3 Agent Mode changes in v2.1.292]] · Digest
- 2026-10-06 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-10-06-4-agent-mode-changes-in-v1-25-0|4 Agent Mode changes in v1.25.0]] · Digest
- 2026-10-05 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-05-4-agent-mode-changes-in-v2-1-290|4 Agent Mode changes in v2.1.290]] · Digest
- 2026-10-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-05-5-agent-mode-changes-in-v1-0-92|5 Agent Mode changes in v1.0.92]] · Digest
- 2026-10-02 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-02-4-agent-mode-changes-in-v2-1-288|4 Agent Mode changes in v2.1.288]] · Digest
- 2026-10-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-01-4-agent-mode-changes-in-v2-1-287|4 Agent Mode changes in v2.1.287]] · Digest
- 2026-10-01 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-01-6-agent-mode-changes-in-rust-v0-160-0|6 Agent Mode changes in rust-v0.160.0]] · Digest

**2026-09**

- 2026-09-30 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-30-6-agent-mode-changes-in-v2-1-286|6 Agent Mode changes in v2.1.286]] · Digest
- 2026-09-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-30-auto-approval-now-takes-into-account-messages-you-type-while-the-agent-is-workin|Auto-approval now takes into account messages you type while the agent is working…]] · Change
- 2026-09-29 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-29-2-agent-mode-changes-in-v2-1-285|2 Agent Mode changes in v2.1.285]] · Digest
- 2026-09-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-29-48190-bound-agent-message-board-sse-frames-before-parsing-jif-oai|♯48190 Bound agent message board SSE frames before parsing @jif-oai]] · Change
- 2026-09-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-28-added-a-yes-but-ask-again-next-time-answer-to-auto-mode-s-prompt-before-a-read-o|Added a "Yes, but ask again next time" answer to auto mode's prompt before a read…]] · Change
- 2026-09-28 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-28-11-agent-mode-changes-in-rust-v0-158-0|11 Agent Mode changes in rust-v0.158.0]] · Digest
- 2026-09-28 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-28-queue-exit-commands-while-an-agent-response-is-still-running|Queue exit commands while an agent response is still running]] · Change
- 2026-09-25 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-25-improved-startup-claude-p-and-claude-code-remote-no-longer-load-the-interactive|Improved startup: claude -p and Claude Code Remote no longer load the interactive…]] · Change
- 2026-09-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-25-13-agent-mode-changes-in-rust-v0-157-0|13 Agent Mode changes in rust-v0.157.0]] · Digest
- 2026-09-25 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-09-25-docs-correct-outdated-cloud-proxy-rule-2-in-agents-md-by-juanmichelini-in-https|docs: correct outdated cloud-proxy Rule 2 in AGENTS.md]] · Change
- 2026-09-24 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-24-2-agent-mode-changes-in-v2-1-282|2 Agent Mode changes in v2.1.282]] · Digest
- 2026-09-23 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-23-10-agent-mode-changes-in-v2-1-281|10 Agent Mode changes in v2.1.281]] · Digest
- 2026-09-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-09-23-when-rollouts-detects-a-regression-it-names-the-change-it-suspects-and-notifies|When Rollouts detects a regression, it names the change it suspects and notifies…]] · Change
- 2026-09-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-22-2-agent-mode-changes-in-v2-1-280|2 Agent Mode changes in v2.1.280]] · Digest
- 2026-09-22 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-09-22-2-agent-mode-changes-in-v4-1-20|2 Agent Mode changes in v4.1.20]] · Digest
- 2026-09-22 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-22-34-agent-mode-changes-in-rust-v0-156-0|34 Agent Mode changes in rust-v0.156.0]] · Digest
- 2026-09-22 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-22-2-agent-mode-changes-in-v1-0-88|2 Agent Mode changes in v1.0.88]] · Digest
- 2026-09-22 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-09-22-docs-refresh-agents-md-guidance-by-all-hands-bot-in-https-github-com-openhands-o|docs: refresh AGENTS.md guidance]] · Change
- 2026-09-21 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-21-show-live-elapsed-time-for-execution-subagents-in-timeline-entries|Show live elapsed time for execution subagents in timeline entries]] · Change
- 2026-09-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-19-added-an-auto-mode-server-row-to-status-showing-whether-this-session-s-auto-mode|Added an Auto mode server row to /status showing whether this session's auto…]] · Change
- 2026-09-18 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-18-4-agent-mode-changes-in-v2-1-277|4 Agent Mode changes in v2.1.277]] · Digest
- 2026-09-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-17-vscode-improved-the-agent-map-the-pill-counts-running-agents-and-turns-red-after|VSCode Improved the agent map]] · Change
- 2026-09-17 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-09-17-task-history-no-longer-goes-blank-when-a-task-spawns-many-subagents-subagent-row|Task history no longer goes blank when a task spawns many subagents]] · Change
- 2026-09-17 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-17-9-agent-mode-changes-in-rust-v0-155-0|9 Agent Mode changes in rust-v0.155.0]] · Digest
- 2026-09-17 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-09-17-2-agent-mode-changes-in-v1-20-0|2 Agent Mode changes in v1.20.0]] · Digest
- 2026-09-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-16-2-agent-mode-changes-in-v1-0-85|2 Agent Mode changes in v1.0.85]] · Digest
- 2026-09-16 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-09-16-2-agent-mode-changes-in-v1-19-0|2 Agent Mode changes in v1.19.0]] · Digest
- 2026-09-15 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-15-changed-auto-mode-on-bedrock-vertex-and-foundry-to-use-the-local-classifier-by-d|Changed auto mode on Bedrock, Vertex and Foundry to use the local classifier…]] · Change
- 2026-09-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-14-7-agent-mode-changes-in-v2-1-271|7 Agent Mode changes in v2.1.271]] · Digest
- 2026-09-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-11-2-agent-mode-changes-in-v2-1-269|2 Agent Mode changes in v2.1.269]] · Digest
- 2026-09-10 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-10-improved-auto-mode-denials-the-message-claude-receives-now-names-the-rule-that-b|Improved auto mode denials]] · Change
- 2026-09-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-09-6-agent-mode-changes-in-rust-v0-154-0|6 Agent Mode changes in rust-v0.154.0]] · Digest
- 2026-09-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-08-improved-workflows-agent-detail-tool-calls-are-marked-running-failed-or-done-the|Improved /workflows agent detail]] · Change
- 2026-09-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-04-2-agent-mode-changes-in-v2-1-261|2 Agent Mode changes in v2.1.261]] · Digest
- 2026-09-04 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-04-stopping-a-timed-out-shell-command-now-lets-queued-messages-run-and-sessions-ret|Stopping a timed-out shell command now lets queued messages run and sessions return…]] · Change
- 2026-09-03 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-03-2-agent-mode-changes-in-v2-1-260|2 Agent Mode changes in v2.1.260]] · Digest
- 2026-09-03 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-03-4-agent-mode-changes-in-rust-v0-153-0|4 Agent Mode changes in rust-v0.153.0]] · Digest
- 2026-09-02 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-02-2-agent-mode-changes-in-v2-1-259|2 Agent Mode changes in v2.1.259]] · Digest
- 2026-09-02 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-09-02-aborting-a-task-now-also-cancels-the-delegated-subagents-and-teammates-it-spawne|Aborting a task now also cancels the delegated subagents and teammates it spawned…]] · Change
- 2026-09-02 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-09-02-cursor-supports-self-hosted-machines-which-let-you-keep-tool-execution-entirely|Cursor supports self-hosted machines, which let you keep tool execution entirely…]] · Change
- 2026-09-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-01-5-agent-mode-changes-in-v2-1-257|5 Agent Mode changes in v2.1.257]] · Digest
- 2026-09-01 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-01-4-agent-mode-changes-in-rust-v0-152-0|4 Agent Mode changes in rust-v0.152.0]] · Digest

**2026-08**

- 2026-08-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-29-2-agent-mode-changes-in-rust-v0-151-0|2 Agent Mode changes in rust-v0.151.0]] · Digest
- 2026-08-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-28-4-agent-mode-changes-in-v2-1-251|4 Agent Mode changes in v2.1.251]] · Digest
- 2026-08-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-27-3-agent-mode-changes-in-v2-1-248|3 Agent Mode changes in v2.1.248]] · Digest
- 2026-08-27 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-08-27-cloud-agents-no-longer-require-a-connected-github-or-other-third-party-scm-provi|Cloud Agents no longer require a connected GitHub or other third-party SCM provider…]] · Change
- 2026-08-27 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-27-8-agent-mode-changes-in-v1-0-81|8 Agent Mode changes in v1.0.81]] · Digest
- 2026-08-27 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-08-27-4-agent-mode-changes-in-v1-16-0|4 Agent Mode changes in v1.16.0]] · Digest
- 2026-08-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-26-14-agent-mode-changes-in-rust-v0-150-0|14 Agent Mode changes in rust-v0.150.0]] · Digest
- 2026-08-25 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-25-improved-subagent-results-a-subagent-that-stops-at-its-maxturns-limit-now-return|Improved subagent results]] · Change
- 2026-08-25 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-08-25-8-agent-mode-changes-in-v0-57-0|8 Agent Mode changes in v0.57.0]] · Digest
- 2026-08-22 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-22-carry-session-and-client-identity-into-langfuse-traces-for-hub-backed-and-delega|Carry session and client identity into Langfuse traces for Hub-backed…]] · Change
- 2026-08-21 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-21-2-agent-mode-changes-in-v2-1-239|2 Agent Mode changes in v2.1.239]] · Digest
- 2026-08-21 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-08-21-feat-add-llm-provider-connections-ui-local-agent-server-by-juanmichelini-in-http|feat: add LLM provider-connections UI (local agent-server)]] · Change
- 2026-08-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-20-12-agent-mode-changes-in-rust-v0-149-0|12 Agent Mode changes in rust-v0.149.0]] · Digest
- 2026-08-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-19-4-agent-mode-changes-in-v2-1-236|4 Agent Mode changes in v2.1.236]] · Digest
- 2026-08-19 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-08-19-we-re-continuing-to-improve-cloud-agents-and-the-cursor-harness-so-always-on-age-1d1294|We're continuing to improve cloud agents and the Cursor harness so always-on agents…]] · Change
- 2026-08-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-18-12-agent-mode-changes-in-rust-v0-148-0|12 Agent Mode changes in rust-v0.148.0]] · Digest
- 2026-08-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-17-removed-the-redundant-allowed-by-auto-mode-classifier-line-that-auto-mode-showed|Removed the redundant "Allowed by auto mode classifier" line that auto mode showed…]] · Change
- 2026-08-17 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-08-17-docs-agents-add-a-repository-map-clarifying-what-belongs-where-by-smolpaws-in-ht|docs(agents): add a repository map clarifying what belongs where]] · Change
- 2026-08-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-14-improved-claude-self-hosted-runner-session-start-time-the-session-branch-is-now|Improved claude self-hosted-runner session start time]] · Change
- 2026-08-13 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-13-4-agent-mode-changes-in-v2-1-232|4 Agent Mode changes in v2.1.232]] · Digest
- 2026-08-13 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-08-13-2-agent-mode-changes-in-08-13-26|2 Agent Mode changes in 08.13.26]] · Digest
- 2026-08-13 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-08-13-agents-do-their-best-work-when-they-start-in-a-ready-environment-repos-cloned-de-6161c7|Agents do their best work when they start in a ready environment]] · Change
- 2026-08-13 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-08-13-chore-enforce-typed-openhands-typescript-client-for-agent-server-api-calls-no-ad|chore: enforce typed @openhands/typescript-client for agent-server API calls…]] · Change
- 2026-08-12 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-12-improved-workflow-fan-outs-to-stagger-same-prefix-sibling-agents-so-subsequent-a|Improved workflow fan-outs to stagger same-prefix sibling agents so subsequent…]] · Change
- 2026-08-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-11-removed-the-outdated-note-about-auto-mode-sessions-costing-slightly-more-from-th|Removed the outdated note about auto mode sessions costing slightly more…]] · Change
- 2026-08-11 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-08-11-2-agent-mode-changes-in-v0-55-1|2 Agent Mode changes in v0.55.1]] · Digest
- 2026-08-07 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-07-removed-the-200-subagent-per-session-spawn-cap-long-running-sessions-no-longer-r|Removed the 200-subagent-per-session spawn cap]] · Change
- 2026-08-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-07-17-agent-mode-changes-in-rust-v0-147-0|17 Agent Mode changes in rust-v0.147.0]] · Digest
- 2026-08-07 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-08-07-feat-add-a-typed-agent-action-for-launching-local-or-cloud-child-conversations-b|feat: add a typed agent action for launching local or Cloud child conversations]] · Change
- 2026-08-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-06-2-agent-mode-changes-in-v2-1-223|2 Agent Mode changes in v2.1.223]] · Digest
- 2026-08-06 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-08-06-feat-pr-generator-agent-implement-antigravity-agent-runner-and-prompt-templates|feat(pr-generator-agent): implement Antigravity agent runner and prompt templates …]] · Change
- 2026-08-03 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-03-a-run-whose-prompt-is-piped-over-stdin-now-treats-its-sessionend-hook-the-same-w|A run whose prompt is piped over stdin now treats its sessionEnd hook the same way…]] · Change
- 2026-08-03 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-08-03-3-agent-mode-changes-in-v1-9-0|3 Agent Mode changes in v1.9.0]] · Digest

**2026-07**

- 2026-07-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-30-2-agent-mode-changes-in-v1-0-76|2 Agent Mode changes in v1.0.76]] · Digest
- 2026-07-30 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-07-30-docs-refresh-agents-md-guidance-by-all-hands-bot-in-https-github-com-openhands-o|docs: refresh AGENTS.md guidance]] · Change
- 2026-07-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-29-11-agent-mode-changes-in-rust-v0-146-0|11 Agent Mode changes in rust-v0.146.0]] · Digest
- 2026-07-29 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-07-29-feat-always-show-the-llm-selector-move-agent-profile-switching-to-the-tools-menu|feat: always show the LLM selector; move agent-profile switching to the tools menu]] · Change
- 2026-07-28 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-07-28-always-on-cloud-agents-that-build-test-and-ship-code-while-you-keep-working-725c7c|Always-on cloud agents that build, test, and ship code while you keep working]] · Change
- 2026-07-28 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-07-28-this-release-migration-was-performed-by-an-ai-agent-openhands-on-behalf-of-the-u|This release migration was performed by an AI agent (OpenHands) on behalf of the user]] · Change
- 2026-07-24 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-24-4-agent-mode-changes-in-v2-1-219|4 Agent Mode changes in v2.1.219]] · Digest
- 2026-07-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-23-3-agent-mode-changes-in-v1-0-74|3 Agent Mode changes in v1.0.74]] · Digest
- 2026-07-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-22-changed-plan-mode-with-auto-to-no-longer-prompt-for-bash-commands-the-static-ana|Changed plan mode with auto to no longer prompt for Bash commands the static…]] · Change
- 2026-07-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-07-22-auto-mode-is-now-powered-by-cursor-router|Auto mode is now powered by Cursor Router]] · Change
- 2026-07-21 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-21-2-agent-mode-changes-in-v2-1-217|2 Agent Mode changes in v2.1.217]] · Digest
- 2026-07-21 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-21-20-agent-mode-changes-in-rust-v0-145-0|20 Agent Mode changes in rust-v0.145.0]] · Digest
- 2026-07-21 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-21-2-agent-mode-changes-in-v1-0-73|2 Agent Mode changes in v1.0.73]] · Digest
- 2026-07-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-20-3-agent-mode-changes-in-v1-0-72|3 Agent Mode changes in v1.0.72]] · Digest
- 2026-07-18 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-18-added-reasoning-effort-to-the-subagentstatusline-payload-so-custom-agent-rows-ca|Added reasoning effort to the subagentStatusLine payload, so custom agent rows can…]] · Change
- 2026-07-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-17-7-agent-mode-changes-in-v2-1-212|7 Agent Mode changes in v2.1.212]] · Digest
- 2026-07-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-16-8-agent-mode-changes-in-v1-0-71|8 Agent Mode changes in v1.0.71]] · Digest
- 2026-07-15 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-15-2-agent-mode-changes-in-v2-1-211|2 Agent Mode changes in v2.1.211]] · Digest
- 2026-07-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-14-4-agent-mode-changes-in-v2-1-208|4 Agent Mode changes in v2.1.208]] · Digest
- 2026-07-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-14-3-agent-mode-changes-in-v2-1-210|3 Agent Mode changes in v2.1.210]] · Digest
- 2026-07-13 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-13-2-agent-mode-changes-in-rust-v0-144-2|2 Agent Mode changes in rust-v0.144.2]] · Digest
- 2026-07-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-11-2-agent-mode-changes-in-v2-1-207|2 Agent Mode changes in v2.1.207]] · Digest
- 2026-07-10 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-10-2-agent-mode-changes-in-v2-1-206|2 Agent Mode changes in v2.1.206]] · Digest
- 2026-07-10 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-07-10-this-release-makes-it-easier-to-stay-in-flow-with-side-chats-that-run-alongside|Cursor makes it easier to stay in flow with side chats that run alongside your main…]] · Change
- 2026-07-10 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-10-3-agent-mode-changes-in-v1-0-70|3 Agent Mode changes in v1.0.70]] · Digest
- 2026-07-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-07-09-chatgpt-work-is-an-agent-for-longer-more-involved-tasks-it-can-research-and-anal|ChatGPT Work is an agent for longer, more involved tasks]] · Change
- 2026-07-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-09-4-agent-mode-changes-in-rust-v0-144-0|4 Agent Mode changes in rust-v0.144.0]] · Digest
- 2026-07-09 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-07-09-feat-enterprise-agent-profiles-on-the-cloud-saas-backend-15044-by-simonrosenberg|feat(enterprise): Agent Profiles on the cloud/SaaS backend (♯15044)]] · Change
- 2026-07-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-08-3-agent-mode-changes-in-v2-1-205|3 Agent Mode changes in v2.1.205]] · Digest
- 2026-07-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-08-10-agent-mode-changes-in-rust-v0-143-0|10 Agent Mode changes in rust-v0.143.0]] · Digest
- 2026-07-07 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-07-2-agent-mode-changes-in-v2-1-203|2 Agent Mode changes in v2.1.203]] · Digest
- 2026-07-07 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-07-double-press-esc-now-interrupts-the-running-main-turn-flushing-queued-messages-o|Double-press Esc now interrupts the running main turn (flushing queued messages)…]] · Change
- 2026-07-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-06-3-agent-mode-changes-in-v2-1-202|3 Agent Mode changes in v2.1.202]] · Digest
- 2026-07-06 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-07-06-9-agent-mode-changes-in-1-9-0|9 Agent Mode changes in 1.9.0]] · Digest
- 2026-07-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-01-5-agent-mode-changes-in-v2-1-198|5 Agent Mode changes in v2.1.198]] · Digest
- 2026-07-01 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-01-3-agent-mode-changes-in-v1-0-68|3 Agent Mode changes in v1.0.68]] · Digest

**2026-06**

- 2026-06-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-30-2-agent-mode-changes-in-v1-0-67|2 Agent Mode changes in v1.0.67]] · Digest
- 2026-06-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-30-8-agent-mode-changes-in-v1-0-66|8 Agent Mode changes in v1.0.66]] · Digest
- 2026-06-29 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-29-2-agent-mode-changes-in-v2-1-196|2 Agent Mode changes in v2.1.196]] · Digest
- 2026-06-26 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-26-improved-claude-agents-completed-list-to-fill-available-vertical-space-on-short|Improved claude agents completed list to fill available vertical space]] · Change
- 2026-06-26 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-06-26-temporarily-disable-subagents-in-the-vs-code-extension-while-the-sdk-backed-expe|Temporarily disable subagents in the VS Code extension while the SDK-backed…]] · Change
- 2026-06-25 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-25-3-agent-mode-changes-in-v2-1-193|3 Agent Mode changes in v2.1.193]] · Digest
- 2026-06-24 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-24-4-agent-mode-changes-in-v1-0-65|4 Agent Mode changes in v1.0.65]] · Digest
- 2026-06-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-23-6-agent-mode-changes-in-v1-0-64|6 Agent Mode changes in v1.0.64]] · Digest
- 2026-06-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-22-2-agent-mode-changes-in-v2-1-186|2 Agent Mode changes in v2.1.186]] · Digest
- 2026-06-22 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-22-14-agent-mode-changes-in-rust-v0-142-0|14 Agent Mode changes in rust-v0.142.0]] · Digest
- 2026-06-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-19-improved-auto-mode-safety-destructive-git-commands-git-reset-hard-git-checkout-g|Improved auto mode safety]] · Change
- 2026-06-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-18-5-agent-mode-changes-in-rust-v0-141-0|5 Agent Mode changes in rust-v0.141.0]] · Digest
- 2026-06-18 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-06-18-2-agent-mode-changes-in-v0-47-0|2 Agent Mode changes in v0.47.0]] · Digest
- 2026-06-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-17-improved-the-subagent-panel-idle-subagents-auto-hide-after-30s-the-list-caps-at|Improved the subagent panel]] · Change
- 2026-06-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-16-agent-mode-is-tracked-per-session-so-it-no-longer-carries-over-when-you-create-c|Agent mode is tracked per session, so it no longer carries over when you create…]] · Change
- 2026-06-15 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-15-2-agent-mode-changes-in-v2-1-178|2 Agent Mode changes in v2.1.178]] · Digest
- 2026-06-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-15-11-agent-mode-changes-in-rust-v0-140-0|11 Agent Mode changes in rust-v0.140.0]] · Digest
- 2026-06-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-13-4-agent-mode-changes-in-v1-0-62|4 Agent Mode changes in v1.0.62]] · Digest
- 2026-06-10 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-10-sub-agents-can-now-spawn-their-own-sub-agents-up-to-5-levels-deep|Sub-agents can now spawn their own sub-agents (up to 5 levels deep)]] · Change
- 2026-06-10 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-06-10-2-agent-mode-changes-in-1-8-0|2 Agent Mode changes in 1.8.0]] · Digest
- 2026-06-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-09-5-agent-mode-changes-in-rust-v0-139-0|5 Agent Mode changes in rust-v0.139.0]] · Digest
- 2026-06-09 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-09-3-agent-mode-changes-in-v1-0-61|3 Agent Mode changes in v1.0.61]] · Digest
- 2026-06-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-08-2-agent-mode-changes-in-v2-1-169|2 Agent Mode changes in v2.1.169]] · Digest
- 2026-06-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-08-8-agent-mode-changes-in-rust-v0-138-0|8 Agent Mode changes in rust-v0.138.0]] · Digest
- 2026-06-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-06-claude-agents-typing-a-url-into-the-list-now-filters-to-the-session-whose-first|claude agents: typing a URL into the list now filters to the session whose first…]] · Change
- 2026-06-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-05-2-agent-mode-changes-in-v1-0-60|2 Agent Mode changes in v1.0.60]] · Digest
- 2026-06-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-04-2-agent-mode-changes-in-v2-1-163|2 Agent Mode changes in v2.1.163]] · Digest
- 2026-06-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-04-12-agent-mode-changes-in-rust-v0-137-0|12 Agent Mode changes in rust-v0.137.0]] · Digest
- 2026-06-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-04-added-the-ability-for-agents-to-embed-buttons-in-canvases-that-will-run-a-specif|Added the ability for agents to embed buttons in canvases that will run a specific…]] · Change
- 2026-06-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-04-with-canvases-agents-can-create-interactive-artifacts-like-dashboards-reports-an|With canvases, agents can create interactive artifacts like dashboards, reports…]] · Change
- 2026-06-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-06-04-5-agent-mode-changes-in-custom-stores-custom-tools|5 Agent Mode changes in Custom stores, custom tools…]] · Digest
- 2026-06-02 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-02-improved-performance-of-opening-recently-inactive-background-agent-sessions-in-c|Improved performance of opening recently-inactive background agent sessions…]] · Change
- 2026-06-02 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-02-claude-agents-rows-now-show-done-total-before-the-detail-when-work-is-fanned-out|claude agents rows now show done/total before the detail when work is fanned out]] · Change
- 2026-06-01 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-01-3-agent-mode-changes-in-rust-v0-136-0|3 Agent Mode changes in rust-v0.136.0]] · Digest
- 2026-06-01 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-01-canceling-a-running-shell-command-ctrl-c-on-a-command-or-aborting-an-agent-comma|Canceling a running shell command (Ctrl+C on a !command, or aborting an agent command]] · Change

**2026-05**

- 2026-05-29 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-29-claude-agents-the-agent-field-in-settings-json-is-now-honored-for-dispatched-ses|claude agents: the agent field in settings.json is now honored for dispatched…]] · Change
- 2026-05-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-29-auto-review-is-a-new-run-mode-that-allows-cursor-to-work-for-longer-with-fewer-a-61df08|Auto-review Run Mode]] · Change
- 2026-05-29 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-29-add-builtinagents-rubberduck-setting-to-enable-or-disable-the-rubber-duck-agent|Add builtInAgents.rubberDuck setting to enable or disable the rubber duck agent…]] · Change
- 2026-05-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-28-4-agent-mode-changes-in-v2-1-154|4 Agent Mode changes in v2.1.154]] · Digest
- 2026-05-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-28-3-agent-mode-changes-in-v2-1-153|3 Agent Mode changes in v2.1.153]] · Digest
- 2026-05-28 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-28-24714-fix-auto-review-skip-legacy-notify-for-auto-review-threads-dylan-hurd-oai|♯24714 fix(auto-review) skip legacy notify for auto review threads @dylan-hurd-oai]] · Change
- 2026-05-28 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-28-3-agent-mode-changes-in-v1-0-55|3 Agent Mode changes in v1.0.55]] · Digest
- 2026-05-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-27-2-agent-mode-changes-in-v2-1-152|2 Agent Mode changes in v2.1.152]] · Digest
- 2026-05-27 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-27-4-agent-mode-changes-in-v0-44-0|4 Agent Mode changes in v0.44.0]] · Digest
- 2026-05-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-26-3-agent-mode-changes-in-rust-v0-134-0|3 Agent Mode changes in rust-v0.134.0]] · Digest
- 2026-05-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-23-custom-agents-support-opt-in-deferred-tool-loading-via-deferred-tool-loading-in|Custom agents support opt-in deferred tool loading via deferred-tool-loading…]] · Change
- 2026-05-22 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-22-2-agent-mode-changes-in-v0-43-0|2 Agent Mode changes in v0.43.0]] · Digest
- 2026-05-21 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-21-auto-mode-no-longer-suppresses-askuserquestion-when-the-user-or-a-skill-explicit|Auto mode no longer suppresses AskUserQuestion when the user or a skill explicitly…]] · Change
- 2026-05-21 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-21-7-agent-mode-changes-in-rust-v0-133-0|7 Agent Mode changes in rust-v0.133.0]] · Digest
- 2026-05-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-20-23147-make-multi-agent-v2-tool-namespace-configurable-jif-oai|♯23147 Make multi-agent v2 tool namespace configurable @jif-oai]] · Change
- 2026-05-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-20-remote-command-can-now-be-used-while-the-agent-is-working|/remote command can now be used while the agent is working]] · Change
- 2026-05-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-19-3-agent-mode-changes-in-v2-1-144|3 Agent Mode changes in v2.1.144]] · Digest
- 2026-05-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-19-3-agent-mode-changes-in-v2-1-145|3 Agent Mode changes in v2.1.145]] · Digest
- 2026-05-19 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-19-assign-work-items-to-cursor-or-mention-cursor-in-a-comment-to-kick-off-a-cloud-a-1c05f0|Assign work items to Cursor, or mention @Cursor in a comment to kick off a cloud agent]] · Change
- 2026-05-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-19-4-agent-mode-changes-in-v1-0-49|4 Agent Mode changes in v1.0.49]] · Digest
- 2026-05-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-18-9-agent-mode-changes-in-rust-v0-131-0|9 Agent Mode changes in rust-v0.131.0]] · Digest
- 2026-05-15 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-15-2-agent-mode-changes-in-v2-1-143|2 Agent Mode changes in v2.1.143]] · Digest
- 2026-05-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-14-improved-hook-configuration-error-configuring-a-prompt-or-agent-type-hook-for-se|Improved hook configuration error]] · Change
- 2026-05-13 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-13-4-agent-mode-changes-in-v2-1-141|4 Agent Mode changes in v2.1.141]] · Digest
- 2026-05-13 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-13-improved-agent-led-environment-setup|Improved agent-led environment setup]] · Change
- 2026-05-13 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-13-to-take-engineering-tasks-from-start-to-finish-agents-need-a-development-environ-e47512|To take engineering tasks from start to finish, agents need a development…]] · Change
- 2026-05-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-13-resume-supports-copilot-cloud-agent-sessions-where-the-agent-hasn-t-pushed-any-c|--resume supports Copilot cloud agent sessions where the agent hasn't pushed any…]] · Change
- 2026-05-12 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-12-2-agent-mode-changes-in-v2-1-140|2 Agent Mode changes in v2.1.140]] · Digest
- 2026-05-12 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-12-2-agent-mode-changes-in-v0-42-0|2 Agent Mode changes in v0.42.0]] · Digest
- 2026-05-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-11-2-agent-mode-changes-in-v2-1-139|2 Agent Mode changes in v2.1.139]] · Digest
- 2026-05-11 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-11-mention-cursor-in-any-teams-channel-to-delegate-a-task-to-a-cloud-agent-or-pull-d30c31|Mention @Cursor in any Teams channel to delegate a task to a cloud agent or pull…]] · Change
- 2026-05-11 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-11-agentstop-hook-now-fires-correctly-when-the-agent-stops-via-task-complete|agentStop hook now fires correctly when the agent stops via task_complete]] · Change
- 2026-05-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-07-5-agent-mode-changes-in-rust-v0-129-0|5 Agent Mode changes in rust-v0.129.0]] · Digest
- 2026-05-07 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-07-added-the-ability-to-control-explore-subagent-behavior-from-settings-choose-a-sp|Added the ability to control Explore subagent behavior from settings]] · Change
- 2026-05-06 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-06-add-rubber-duck-agent-for-gpt-sessions-powered-by-claude-available-in-experiment|Add rubber-duck agent for GPT sessions, powered by Claude (available in /experimental)]] · Change
- 2026-05-06 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-05-06-improved-reliability-of-devin-local-agent|Improved reliability of Devin Local agent]] · Change
- 2026-05-05 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-05-feat-core-enhance-shell-command-validation-and-add-core-tools-allowlist-by-galz1|feat(core): enhance shell command validation and add core tools allowlist]] · Change
- 2026-05-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-05-add-experimental-mcp-tasks-support-mcp-tools-with-tasksupport-required-run-as-no|Add experimental MCP Tasks support]] · Change
- 2026-05-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-04-auto-mode-when-the-classifier-can-t-evaluate-an-action-the-error-now-includes-a|Auto mode: when the classifier can't evaluate an action, the error now includes…]] · Change
- 2026-05-01 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-01-3-agent-mode-changes-in-v1-0-40|3 Agent Mode changes in v1.0.40]] · Digest

**2026-04**

- 2026-04-30 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-30-19-agent-mode-changes-in-rust-v0-128-0|19 Agent Mode changes in rust-v0.128.0]] · Digest
- 2026-04-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-29-3-agent-mode-changes-in-build-programmatic-agents|3 Agent Mode changes in Build programmatic agents…]] · Digest
- 2026-04-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-28-2-agent-mode-changes-in-v2-1-121|2 Agent Mode changes in v2.1.121]] · Digest
- 2026-04-28 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-28-3-agent-mode-changes-in-v0-40-0|3 Agent Mode changes in v0.40.0]] · Digest
- 2026-04-28 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-28-press-ctrl-x-b-to-move-the-current-running-task-or-shell-command-to-the-backgrou|Press ctrl+x → b to move the current running task or shell command to the background]] · Change
- 2026-04-24 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-24-5-agent-mode-changes-in-rust-v0-125-0|5 Agent Mode changes in rust-v0.125.0]] · Digest
- 2026-04-24 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-24-custom-agents-skills-and-commands-from-claude-are-no-longer-loaded-by-the-copilo|Custom agents, skills, and commands from ~/.claude/ are no longer loaded…]] · Change
- 2026-04-23 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-23-2-agent-mode-changes-in-v2-1-118|2 Agent Mode changes in v2.1.118]] · Digest
- 2026-04-23 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-23-2-agent-mode-changes-in-v2-1-119|2 Agent Mode changes in v2.1.119]] · Digest
- 2026-04-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-8-agent-mode-changes-in-rust-v0-123-0|8 Agent Mode changes in rust-v0.123.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-11-agent-mode-changes-in-rust-v0-124-0|11 Agent Mode changes in rust-v0.124.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-23-6-agent-mode-changes-in-v0-39-0|6 Agent Mode changes in v0.39.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-23-7-agent-mode-changes-in-v1-0-35|7 Agent Mode changes in v1.0.35]] · Digest
- 2026-04-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-22-2-agent-mode-changes-in-v2-1-117|2 Agent Mode changes in v2.1.117]] · Digest
- 2026-04-20 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-20-2-agent-mode-changes-in-v2-1-116|2 Agent Mode changes in v2.1.116]] · Digest
- 2026-04-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-20-10-agent-mode-changes-in-rust-v0-122-0|10 Agent Mode changes in rust-v0.122.0]] · Digest
- 2026-04-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-20-2-agent-mode-changes-in-v1-0-33|2 Agent Mode changes in v1.0.33]] · Digest
- 2026-04-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-17-subagents-that-stall-mid-stream-now-fail-with-a-clear-error-after-10-minutes-ins|Subagents that stall mid-stream now fail with a clear error after 10 minutes instead…]] · Change
- 2026-04-17 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-17-attach-supported-document-files-to-prompts-for-the-agent-to-read-and-reason-abou|Attach supported document files to prompts for the agent to read and reason about]] · Change
- 2026-04-16 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-16-auto-mode-no-longer-requires-enable-auto-mode|Auto mode no longer requires --enable-auto-mode]] · Change
- 2026-04-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-16-background-agent-completion-notifications-are-not-sent-redundantly-when-read-age|Background agent completion notifications are not sent redundantly when read_agent…]] · Change
- 2026-04-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-16-agent-correctly-identifies-repository-owner-from-git-remote-url-rather-than-loca|Agent correctly identifies repository owner from git remote URL rather than local username]] · Change
- 2026-04-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-15-7-agent-mode-changes-in-rust-v0-121-0|7 Agent Mode changes in rust-v0.121.0]] · Digest
- 2026-04-14 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-14-6-agent-mode-changes-in-v0-38-0|6 Agent Mode changes in v0.38.0]] · Digest
- 2026-04-13 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-13-3-agent-mode-changes-in-3-1|3 Agent Mode changes in 3.1]] · Digest
- 2026-04-11 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-11-4-agent-mode-changes-in-rust-v0-120-0|4 Agent Mode changes in rust-v0.120.0]] · Digest
- 2026-04-10 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-10-ultraplan-and-other-remote-session-features-now-auto-create-a-default-cloud-envi|/ultraplan and other remote-session features now auto-create a default cloud…]] · Change
- 2026-04-10 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-10-13-agent-mode-changes-in-rust-v0-119-0|13 Agent Mode changes in rust-v0.119.0]] · Digest
- 2026-04-10 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-10-add-mode-autopilot-and-plan-flags-to-start-the-cli-directly-in-a-specific-agent|Add --mode, --autopilot, and --plan flags to start the CLI directly in a specific…]] · Change
- 2026-04-09 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-09-3-agent-mode-changes-in-v2-1-98|3 Agent Mode changes in v2.1.98]] · Digest
- 2026-04-09 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-09-3-agent-mode-changes-in-v1-0-22|3 Agent Mode changes in v1.0.22]] · Digest
- 2026-04-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-08-2-agent-mode-changes-in-v2-1-97|2 Agent Mode changes in v2.1.97]] · Digest
- 2026-04-08 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-08-11-agent-mode-changes-in-v0-37-0|11 Agent Mode changes in v0.37.0]] · Digest
- 2026-04-07 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-07-spinner-no-longer-appears-stuck-when-a-long-running-async-shell-command-is-activ|Spinner no longer appears stuck when a long-running async shell command is active]] · Change
- 2026-04-07 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-07-spinner-stays-active-until-background-agents-and-shell-commands-finish-and-user|Spinner stays active until background agents and shell commands finish, and user…]] · Change
- 2026-04-06 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-06-2-agent-mode-changes-in-v1-0-19|2 Agent Mode changes in v1.0.19]] · Digest
- 2026-04-03 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-03-built-in-skills-are-now-included-with-the-cli-starting-with-a-guide-for-customiz|Built-in skills are now included with the CLI, starting with a guide for customizing…]] · Change
- 2026-04-02 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-02-4-agent-mode-changes-in-3-0|4 Agent Mode changes in 3.0]] · Digest
- 2026-04-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-01-3-agent-mode-changes-in-v2-1-89|3 Agent Mode changes in v2.1.89]] · Digest
- 2026-04-01 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-04-01-exclude-new-task-tool-from-system-prompt-in-yolo-headless-mode|Exclude new_task tool from system prompt in yolo/headless mode]] · Change
- 2026-04-01 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-01-10-agent-mode-changes-in-v0-36-0|10 Agent Mode changes in v0.36.0]] · Digest

**2026-03**

- 2026-03-31 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-31-4-agent-mode-changes-in-rust-v0-118-0|4 Agent Mode changes in rust-v0.118.0]] · Digest
- 2026-03-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-27-auto-mode-now-shows-unavailable-for-your-plan-when-disabled-by-plan-restrictions|Auto mode now shows "unavailable for your plan" when disabled by plan restrictions…]] · Change
- 2026-03-26 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-26-2-agent-mode-changes-in-v2-1-84|2 Agent Mode changes in v2.1.84]] · Digest
- 2026-03-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-26-19-agent-mode-changes-in-rust-v0-117-0|19 Agent Mode changes in rust-v0.117.0]] · Digest
- 2026-03-26 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-26-resume-session-restores-the-previously-selected-custom-agent|Resume session restores the previously selected custom agent]] · Change
- 2026-03-25 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-25-agents-can-now-declare-initialprompt-in-frontmatter-to-auto-submit-a-first-turn|Agents can now declare initialPrompt in frontmatter to auto-submit a first turn]] · Change
- 2026-03-25 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-03-25-cursor-now-supports-self-hosted-cloud-agents-that-keep-your-code-and-tool-execut-e411f3|Self-hosted Cloud Agents]] · Change
- 2026-03-24 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-24-10-agent-mode-changes-in-v0-35-0|10 Agent Mode changes in v0.35.0]] · Digest
- 2026-03-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-23-2-agent-mode-changes-in-v1-0-11|2 Agent Mode changes in v1.0.11]] · Digest
- 2026-03-19 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-19-5-agent-mode-changes-in-rust-v0-116-0|5 Agent Mode changes in rust-v0.116.0]] · Digest
- 2026-03-18 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-18-2-agent-mode-changes-in-v1-0-8|2 Agent Mode changes in v1.0.8]] · Digest
- 2026-03-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-17-2-agent-mode-changes-in-v2-1-77|2 Agent Mode changes in v2.1.77]] · Digest
- 2026-03-17 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-17-7-agent-mode-changes-in-v0-34-0|7 Agent Mode changes in v0.34.0]] · Digest
- 2026-03-16 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-16-16-agent-mode-changes-in-rust-v0-115-0|16 Agent Mode changes in rust-v0.115.0]] · Digest
- 2026-03-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-16-5-agent-mode-changes-in-v1-0-6|5 Agent Mode changes in v1.0.6]] · Digest
- 2026-03-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-14-improved-background-agent-behavior-killing-a-background-agent-now-preserves-its|Improved background agent behavior]] · Change
- 2026-03-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-13-send-follow-up-messages-to-background-agents-with-the-write-agent-tool-for-multi|Send follow-up messages to background agents with the write_agent tool…]] · Change
- 2026-03-12 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-03-12-added-github-copilot-instructions-md-for-coding-agents|Added .github/copilot-instructions.md for coding agents]] · Change
- 2026-03-11 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-11-6-agent-mode-changes-in-v0-33-0|6 Agent Mode changes in v0.33.0]] · Digest
- 2026-03-11 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-11-2-agent-mode-changes-in-v1-0-4|2 Agent Mode changes in v1.0.4]] · Digest
- 2026-03-11 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-03-11-2-agent-mode-changes-in-1-5-0|2 Agent Mode changes in 1.5.0]] · Digest
- 2026-03-10 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-10-2-agent-mode-changes-in-v2-1-72|2 Agent Mode changes in v2.1.72]] · Digest
- 2026-03-05 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-05-2-agent-mode-changes-in-v2-1-69|2 Agent Mode changes in v2.1.69]] · Digest
- 2026-03-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-05-13-agent-mode-changes-in-rust-v0-110-0|13 Agent Mode changes in rust-v0.110.0]] · Digest
- 2026-03-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-05-automatic-notifications-when-background-shell-commands-and-agents-complete|Automatic notifications when background shell commands and agents complete]] · Change
- 2026-03-04 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-03-04-subagent-stream-retry-delay-increased-to-reduce-noise-from-transient-failures|Subagent stream retry delay increased to reduce noise from transient failures]] · Change
- 2026-03-03 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-03-03-add-user-agent-header-to-requests-sent-to-the-cline-backend|Add User-Agent header to requests sent to the Cline backend]] · Change
- 2026-03-03 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-03-03-improved-reliability-for-longer-running-agent-sessions|Improved reliability for longer-running agent sessions]] · Change
- 2026-03-03 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-03-3-agent-mode-changes-in-v0-32-0|3 Agent Mode changes in v0.32.0]] · Digest
- 2026-03-03 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-03-shell-command-output-on-windows-no-longer-renders-as-no-changes-detected-in-the|Shell command output on Windows no longer renders as "No changes detected" in the timeline]] · Change
- 2026-03-02 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-02-2-agent-mode-changes-in-rust-v0-107-0|2 Agent Mode changes in rust-v0.107.0]] · Digest

**2026-02**

- 2026-02-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-28-added-http-hooks-which-can-post-json-to-a-url-and-receive-json-instead-of-runnin|Added HTTP hooks, which can POST JSON to a URL and receive JSON instead of running…]] · Change
- 2026-02-27 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-27-feat-browser-implement-experimental-browser-agent-by-gsquared94-in-https-github|feat(browser): implement experimental browser agent]] · Change
- 2026-02-27 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-27-cli-spinner-stops-and-final-agent-response-is-visible-after-agent-finishes-work|CLI spinner stops and final agent response is visible after agent finishes work]] · Change
- 2026-02-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-26-5-agent-mode-changes-in-rust-v0-106-0|5 Agent Mode changes in rust-v0.106.0]] · Digest
- 2026-02-26 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-02-26-autofix-runs-cloud-agents-on-their-own-machines-to-test-changes-and-propose-fixe|Autofix runs cloud agents on their own machines to test changes and propose fixes…]] · Change
- 2026-02-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-25-18-agent-mode-changes-in-rust-v0-105-0|18 Agent Mode changes in rust-v0.105.0]] · Digest
- 2026-02-25 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-25-4-agent-mode-changes-in-v0-30-0|4 Agent Mode changes in v0.30.0]] · Digest
- 2026-02-25 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-25-agent-protected-from-accidentally-killing-itself|Agent protected from accidentally killing itself]] · Change
- 2026-02-24 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-02-24-3-agent-mode-changes-in-v3-67-0|3 Agent Mode changes in v3.67.0]] · Digest
- 2026-02-24 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-02-24-cloud-agents-can-now-use-the-software-they-create-to-test-changes-and-demo-their-c922e9|Cloud Agents with Computer Use]] · Change
- 2026-02-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-23-2-agent-mode-changes-in-v0-0-415|2 Agent Mode changes in v0.0.415]] · Digest
- 2026-02-20 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-20-2-agent-mode-changes-in-v2-1-50|2 Agent Mode changes in v2.1.50]] · Digest
- 2026-02-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-19-3-agent-mode-changes-in-v0-0-412|3 Agent Mode changes in v0.0.412]] · Digest
- 2026-02-18 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-18-2-agent-mode-changes-in-v2-1-47|2 Agent Mode changes in v2.1.47]] · Digest
- 2026-02-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-18-protocol-core-now-carry-distinct-approval-ids-for-command-approvals-to-support-m|Protocol/core now carry distinct approval IDs for command approvals to support…]] · Change
- 2026-02-18 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-02-18-2-agent-mode-changes-in-cli-improvements-and-mermaid-ascii|2 Agent Mode changes in CLI Improvements and Mermaid ASCII…]] · Digest
- 2026-02-18 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-18-8-agent-mode-changes-in-v0-29-0|8 Agent Mode changes in v0.29.0]] · Digest
- 2026-02-17 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-17-7-agent-mode-changes-in-rust-v0-102-0|7 Agent Mode changes in rust-v0.102.0]] · Digest
- 2026-02-17 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-02-17-6-agent-mode-changes-in-2-5|6 Agent Mode changes in 2.5]] · Digest
- 2026-02-12 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-02-12-subagent-replace-legacy-subagents-with-the-native-use-subagents-tool|Subagent: replace legacy subagents with the native use_subagents tool]] · Change
- 2026-02-12 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-12-2-agent-mode-changes-in-rust-v0-100-0|2 Agent Mode changes in rust-v0.100.0]] · Digest
- 2026-02-12 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-02-12-cursor-can-now-work-autonomously-over-longer-horizons-to-complete-larger-more-co-48843c|Long-running Agents in Research Preview]] · Change
- 2026-02-12 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-12-subagents-return-complete-responses|Subagents return complete responses]] · Change
- 2026-02-11 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-11-10-agent-mode-changes-in-rust-v0-99-0|10 Agent Mode changes in rust-v0.99.0]] · Digest
- 2026-02-11 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-11-3-agent-mode-changes-in-v0-0-407|3 Agent Mode changes in v0.0.407]] · Digest
- 2026-02-10 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-10-4-agent-mode-changes-in-v0-28-0|4 Agent Mode changes in v0.28.0]] · Digest
- 2026-02-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-06-2-agent-mode-changes-in-v2-1-33|2 Agent Mode changes in v2.1.33]] · Digest
- 2026-02-05 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-05-updated-resume-to-re-use-agent-value-specified-in-previous-conversation-by-defau|Updated --resume to re-use --agent value specified in previous conversation by default]] · Change
- 2026-02-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-05-10649-fix-test-shell-command-interruption-flake-gt-oai|♯10649 Fix test_shell_command_interruption flake @gt-oai]] · Change
- 2026-02-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-05-support-comma-separated-tools-in-custom-agent-frontmatter|Support comma-separated tools in custom agent frontmatter]] · Change
- 2026-02-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-05-2-agent-mode-changes-in-v0-0-404|2 Agent Mode changes in v0.0.404]] · Digest
- 2026-02-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-04-4-agent-mode-changes-in-rust-v0-95-0|4 Agent Mode changes in rust-v0.95.0]] · Digest
- 2026-02-04 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-04-15-agent-mode-changes-in-v0-27-0|15 Agent Mode changes in v0.27.0]] · Digest
- 2026-02-03 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-03-added-token-count-tool-uses-and-duration-metrics-to-task-tool-results|Added token count, tool uses, and duration metrics to Task tool results]] · Change
- 2026-02-03 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-03-4-agent-mode-changes-in-v0-0-402|4 Agent Mode changes in v0.0.402]] · Digest
- 2026-02-03 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-03-support-agents-skills-directory-for-auto-loading-skills|Support .agents/skills directory for auto-loading skills]] · Change
- 2026-02-02 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-02-2-agent-mode-changes-in-rust-v0-94-0|2 Agent Mode changes in rust-v0.94.0]] · Digest

**2026-01**

- 2026-01-29 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-29-2-agent-mode-changes-in-v0-0-399|2 Agent Mode changes in v0.0.399]] · Digest
- 2026-01-28 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-28-8-agent-mode-changes-in-v0-26-0|8 Agent Mode changes in v0.26.0]] · Digest
- 2026-01-28 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-28-add-acp-flag-to-start-as-agent-client-protocol-server|Add --acp flag to start as Agent Client Protocol server]] · Change
- 2026-01-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-27-2-agent-mode-changes-in-v2-1-20|2 Agent Mode changes in v2.1.20]] · Digest
- 2026-01-27 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-27-9818-feat-rebase-multi-agent-tui-on-config-snapshot-jif-oai|♯9818 feat: rebase multi-agent tui on config_snapshot @jif-oai]] · Change
- 2026-01-27 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-27-3-agent-mode-changes-in-v0-0-396|3 Agent Mode changes in v0.0.396]] · Digest
- 2026-01-26 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-26-load-local-shell-configuration-in-agent-sessions|Load local shell configuration in agent sessions]] · Change
- 2026-01-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-25-2-agent-mode-changes-in-rust-v0-91-0|2 Agent Mode changes in rust-v0.91.0]] · Digest
- 2026-01-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-25-2-agent-mode-changes-in-rust-v0-90-0|2 Agent Mode changes in rust-v0.90.0]] · Digest
- 2026-01-23 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-23-added-env-var-claude-code-enable-tasks-set-to-false-to-keep-the-old-system-tempo|Added env var CLAUDE_CODE_ENABLE_TASKS, set to false to keep the old system…]] · Change
- 2026-01-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-23-add-support-for-ghe-cloud-ghe-com-remote-custom-agents|Add support for GHE Cloud (\.ghe.com) remote custom agents]] · Change
- 2026-01-22 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-22-9650-chore-tweak-agents-md-dylan-hurd-oai|♯9650 chore: tweak AGENTS.md @dylan-hurd-oai]] · Change
- 2026-01-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-01-22-4-agent-mode-changes-in-2-4|4 Agent Mode changes in 2.4]] · Digest
- 2026-01-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-01-22-agents-are-solving-increasingly-complex-long-running-tasks-across-your-codebase|Agents are solving increasingly complex, long-running tasks across your codebase]] · Change
- 2026-01-22 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-22-2-agent-mode-changes-in-v0-0-389|2 Agent Mode changes in v0.0.389]] · Digest
- 2026-01-21 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-21-2-agent-mode-changes-in-rust-v0-88-0|2 Agent Mode changes in rust-v0.88.0]] · Digest
- 2026-01-21 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-21-13-agent-mode-changes-in-v0-25-0|13 Agent Mode changes in v0.25.0]] · Digest
- 2026-01-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-19-mcp-server-management-when-swapping-between-custom-agents-with-agent|MCP server management when swapping between custom agents with /agent]] · Change
- 2026-01-16 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-16-added-plansdirectory-setting-to-customize-where-plan-files-are-stored|Added plansDirectory setting to customize where plan files are stored]] · Change
- 2026-01-16 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-01-16-added-hooks-for-session-start-end-prompt-and-stop-for-customizing-agent-lifecycl|Added hooks for session start/end, prompt, and stop for customizing agent lifecycle events]] · Change
- 2026-01-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-16-2-agent-mode-changes-in-v0-0-384|2 Agent Mode changes in v0.0.384]] · Digest
- 2026-01-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-15-9275-feat-add-agent-roles-to-collab-tools-jif-oai|♯9275 feat: add agent roles to collab tools @jif-oai]] · Change
- 2026-01-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-14-added-inline-display-of-agent-s-final-response-in-task-notifications-making-it-e|Added inline display of agent's final response in task notifications, making…]] · Change
- 2026-01-14 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-14-2-agent-mode-changes-in-rust-v0-81-0|2 Agent Mode changes in rust-v0.81.0]] · Digest
- 2026-01-14 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-14-10-agent-mode-changes-in-v0-24-0|10 Agent Mode changes in v0.24.0]] · Digest
- 2026-01-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-13-3-agent-mode-changes-in-v0-0-380|3 Agent Mode changes in v0.0.380]] · Digest
- 2026-01-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-11-added-claude-code-disable-background-tasks-environment-variable-to-disable-all-b|Added CLAUDE_CODE_DISABLE_BACKGROUND_TASKS environment variable to disable all…]] · Change
- 2026-01-09 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-09-added-agent-type-to-sessionstart-hook-input-populated-if-agent-is-specified|Added agent_type to SessionStart hook input, populated if --agent is specified]] · Change
- 2026-01-09 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-09-add-skills-system-for-reusable-on-demand-agent-instructions|Add Skills system for reusable, on-demand agent instructions]] · Change
- 2026-01-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-09-2-agent-mode-changes-in-rust-v0-80-0|2 Agent Mode changes in rust-v0.80.0]] · Digest
- 2026-01-08 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-01-08-new-agent-command-is-now-the-primary-cli-entrypoint-cursor-agent-remains-as-a-ba|New agent command is now the primary CLI entrypoint. cursor-agent remains…]] · Change
- 2026-01-08 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-08-task-tool-subagents-can-now-process-images|Task tool subagents can now process images]] · Change
- 2026-01-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-07-4-agent-mode-changes-in-rust-v0-79-0|4 Agent Mode changes in rust-v0.79.0]] · Digest
- 2026-01-07 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-07-3-agent-mode-changes-in-v0-23-0|3 Agent Mode changes in v0.23.0]] · Digest
- 2026-01-02 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-02-built-in-subagents-for-exploring-and-managing-tasks|Built-in subagents for exploring and managing tasks]] · Change

</details>

</details>

<details class="disclosure">
<summary>2025 · 118 entries (ChatGPT 2 · Cline 5 · Codex CLI 18 · Cursor 50 · Gemini CLI 19 · GitHub Copilot CLI 5 · OpenHands 17 · Windsurf 2)</summary>

**2025-12**

- 2025-12-18 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-12-18-shared-agent-transcripts-164030|Shared agent transcripts]] · Launch
- 2025-12-18 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-12-18-linux-sandboxing-for-agents|Linux sandboxing for agents]] · Launch
- 2025-12-18 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-12-18-service-accounts|Service accounts]] · Launch
- 2025-12-16 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-12-16-agents-tool-execution|Agents & Tool Execution]] · Launch
- 2025-12-10 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-12-10-plan-mode-now-supports-inline-mermaid-diagrams-allowing-the-agent-to-automatical|Plan Mode improvements]] · Launch
- 2025-12-10 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-12-10-multi-agent-judging|Multi-agent judging]] · Launch

**2025-11**

- 2025-11-21 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-11-21-instant-grep-beta|Instant Grep (Beta)]] · Launch

**2025-10**

- 2025-10-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-10-29-browser-ga-1124ce|Browser (GA)]] · Launch
- 2025-10-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-10-29-cloud-agents|Cloud Agents]] · Launch
- 2025-10-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-10-29-multi-agents-bb4f56|Multi-Agents]] · Launch

**2025-09**

- 2025-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-09-29-we-re-introducing-instant-checkout-in-chatgpt-and-the-agentic-commerce-protocol-8cbf19|ChatGPT introduces Instant Checkout and the Agentic Commerce Protocol that powers…]] · Launch
- 2025-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-09-29-agentic-commerce-protocol|Agentic Commerce Protocol]] · Launch
- 2025-09-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-09-29-hooks-beta|Hooks (beta)]] · Launch
- 2025-09-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-09-29-cursor-can-now-write-detailed-plans-before-starting-complex-tasks-this-allows-ag|Plan Mode]] · Launch
- 2025-09-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-09-29-monitor-agents-from-menubar|Monitor Agents from menubar]] · Launch
- 2025-09-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-09-29-agent-can-take-screenshots-improve-ui-and-debug-client-issues-read-more-about-br|Browser Controls]] · Launch
- 2025-09-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-09-29-image-file-support-for-agent|Image file support for Agent]] · Launch

**2025-08**

- 2025-08-21 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-08-21-you-can-now-start-background-agents-directly-from-linear-delegate-tasks-to-curso|Run Agents in Linear]] · Launch
- 2025-08-21 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-08-21-get-native-os-notifications-when-an-agent-run-finishes-or-when-input-is-required|OS notifications from Agent]] · Launch
- 2025-08-06 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-08-06-github-support-for-background-agents|GitHub support for Background Agents]] · Launch
- 2025-08-06 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-08-06-sidebar-for-all-agents|Sidebar for all Agents]] · Launch
- 2025-08-06 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-08-06-sending-messages-while-cursor-is-working-now-does-a-better-job-of-steering-the-a|More Agent steerability]] · Launch

**2025-07**

- 2025-07-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-07-29-agents-can-now-use-your-native-terminal-a-new-terminal-will-be-created-when-need|Share terminal with Agent]] · Launch
- 2025-07-03 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-07-03-let-agent-resolve-merge-conflicts|Let Agent resolve merge conflicts]] · Launch
- 2025-07-03 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-07-03-agent-to-dos-3ffa24|Agent To-dos]] · Launch
- 2025-07-03 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-07-03-you-can-now-queue-follow-up-messages-for-agent-once-it-s-done-with-current-task|Queued messages]] · Launch
- 2025-07-03 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-07-03-background-agent-improvements|Background Agent improvements]] · Launch

**2025-06**

- 2025-06-12 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-06-12-you-can-now-launch-background-agents-directly-from-slack-by-mentioning-cursor-ag|Launch Background Agents directly from Slack by mentioning @Cursor]] · Change
- 2025-06-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-06-04-agent-in-jupyter-notebooks|Agent in Jupyter Notebooks]] · Launch
- 2025-06-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-06-04-background-agent-for-everyone-8b35dc|Background Agent for everyone]] · Launch
- 2025-06-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-06-04-this-release-brings-bugbot-for-code-review-a-first-look-at-memories-one-click-mc|Cursor brings Bugbot for code review, a first look at memories, one-click MCP setup…]] · Launch

**2025-05**

- 2025-05-15 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-05-15-fast-edits-for-long-files-with-agent|Fast edits for long files with Agent]] · Launch
- 2025-05-15 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-05-15-background-agent-preview|Background Agent (Preview)]] · Launch

**2025-04**

- 2025-04-15 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-04-15-reviewing-agent-generated-code-is-now-easier-with-a-built-in-diff-view-at-the-en|Making reviews easier]] · Launch

**2025-03**

- 2025-03-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-03-23-built-in-modes-custom-modes-beta|Built-in modes & custom modes (beta)]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 83 (Cline 5 · Codex CLI 18 · Cursor 18 · Gemini CLI 19 · GitHub Copilot CLI 5 · OpenHands 17 · Windsurf 1)</summary>

**2025-12**

- 2025-12-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-12-22-2-agent-mode-changes-in-2-3|2 Agent Mode changes in 2.3]] · Digest
- 2025-12-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-12-22-this-includes-the-core-agent-layout-controls-viewing-code-diffs-and-more-we-will|This includes the core agent, layout controls, viewing code diffs, and more]] · Change
- 2025-12-22 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-22-send-the-model-and-cli-version-with-the-user-agent-by-gundermanc-in-https-github|Send the model and CLI version with the user agent]] · Change
- 2025-12-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-18-3-agent-mode-changes-in-rust-v0-74-0|3 Agent Mode changes in rust-v0.74.0]] · Digest
- 2025-12-16 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-12-16-new-openhands-1-0-0-using-the-new-software-agent-sdk-https-github-com-openhands|New OpenHands 1.0.0 using the new…]] · Change
- 2025-12-10 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-12-10-agent-plans-are-now-files-that-can-be-edited-with-normal-tools|Agent plans are now files that can be edited with normal tools]] · Change
- 2025-12-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-09-7729-feat-add-is-mutating-detection-for-shell-command-handler-jif-oai|♯7729 feat: add is-mutating detection for shell command handler @jif-oai]] · Change
- 2025-12-09 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-09-feat-a2a-urgent-fix-process-modelinfo-agent-message-by-cocosheng-g-in-https-gith|feat(a2a): Urgent fix - Process modelInfo agent message]] · Change
- 2025-12-03 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-12-03-add-infer-property-to-control-custom-agent-tool-visibility|Add infer property to control custom agent tool visibility]] · Change
- 2025-12-02 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-02-powershell-apply-patch-parsing-is-corrected-and-apply-patch-tests-now-cover-shel|PowerShell apply_patch parsing is corrected, and apply_patch tests now cover…]] · Change

**2025-11**

- 2025-11-21 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-11-21-2-agent-mode-changes-in-2-1|2 Agent Mode changes in 2.1]] · Digest
- 2025-11-19 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-19-2-agent-mode-changes-in-rust-v0-59-0|2 Agent Mode changes in rust-v0.59.0]] · Digest
- 2025-11-13 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-11-13-feat-add-agents-md-support-by-saoudrizwan-in-https-github-com-cline-cline-pull-7|feat: add AGENTS.md support]] · Change
- 2025-11-13 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-13-6510-feat-shell-command-tool-29364f3a9|♯6510 — feat: shell_command tool (29364f3a9)]] · Change
- 2025-11-12 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-12-2-agent-mode-changes-in-v0-14-0|2 Agent Mode changes in v0.14.0]] · Digest
- 2025-11-12 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-11-12-3-agent-mode-changes-in-v0-0-355|3 Agent Mode changes in v0.0.355]] · Digest
- 2025-11-07 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-07-3-agent-mode-changes-in-v0-13-0|3 Agent Mode changes in v0.13.0]] · Digest
- 2025-11-04 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-04-add-regression-tests-for-shell-command-parsing-by-cornmander-in-https-github-com|Add regression tests for shell command parsing]] · Change
- 2025-11-03 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-11-03-custom-agents-with-special-characters-in-filenames-no-longer-fail|Custom agents with special characters in filenames no longer fail]] · Change

**2025-10**

- 2025-10-30 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-30-3-agent-mode-changes-in-rust-v0-52-0|3 Agent Mode changes in rust-v0.52.0]] · Digest
- 2025-10-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-10-29-improved-agent-harness|Improved Agent Harness]] · Change
- 2025-10-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-10-29-background-agents-have-been-renamed-to-cloud-agents|Background Agents have been renamed to Cloud Agents]] · Change
- 2025-10-29 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-29-chore-subagents-remove-legacy-subagent-code-by-abhipatel12-in-https-github-com-g|chore(subagents): Remove legacy subagent code]] · Change
- 2025-10-28 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-28-2-agent-mode-changes-in-v0-0-353|2 Agent Mode changes in v0.0.353]] · Digest
- 2025-10-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-23-2-agent-mode-changes-in-rust-v0-48-0|2 Agent Mode changes in rust-v0.48.0]] · Digest
- 2025-10-23 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-10-23-support-and-fixes-for-agents-md|Support and fixes for AGENTS.md]] · Change
- 2025-10-22 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-22-feat-core-add-telemetry-for-subagent-execution-by-abhipatel12-in-https-github-co|feat(core): add telemetry for subagent execution]] · Change
- 2025-10-17 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-17-agent-override-file-5215|Agent override file (♯5215)]] · Change
- 2025-10-16 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-10-16-2-agent-mode-changes-in-v3-33-0|2 Agent Mode changes in v3.33.0]] · Digest
- 2025-10-15 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-15-3-agent-mode-changes-in-v0-9-0|3 Agent Mode changes in v0.9.0]] · Digest
- 2025-10-07 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-07-2-agent-mode-changes-in-v0-8-0|2 Agent Mode changes in v0.8.0]] · Digest
- 2025-10-03 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-03-5-agent-mode-changes-in-rust-v0-44-0|5 Agent Mode changes in rust-v0.44.0]] · Digest
- 2025-10-01 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-01-improved-the-experience-of-writing-prompts-while-the-agent-is-running-up-down-ar|Improved the experience of writing prompts while the agent is running -- up/down…]] · Change

**2025-09**

- 2025-09-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-09-29-6-agent-mode-changes-in-1-7|6 Agent Mode changes in 1.7]] · Digest
- 2025-09-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-18-2-agent-mode-changes-in-rust-v0-39-0|2 Agent Mode changes in rust-v0.39.0]] · Digest
- 2025-09-17 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-17-feat-core-only-summarize-long-tool-output-for-shell-command-by-sandytao520-in-ht|feat(core): Only summarize long tool output for shell command]] · Change
- 2025-09-12 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-09-12-3-agent-mode-changes-in-1-6|3 Agent Mode changes in 1.6]] · Digest
- 2025-09-10 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-10-3436-make-user-agent-optional-3436|♯3436 Make user_agent optional (♯3436)]] · Change
- 2025-09-09 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-09-09-2-agent-mode-changes-in-0-56-0|2 Agent Mode changes in 0.56.0]] · Digest
- 2025-09-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-05-3-agent-mode-changes-in-rust-v0-30-0|3 Agent Mode changes in rust-v0.30.0]] · Digest
- 2025-09-04 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-04-feat-subagent-enable-incremental-output-streaming-by-allenhutchison-in-https-git|feat(subagent): Enable incremental output streaming]] · Change
- 2025-09-03 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-03-3089-docs-update-link-to-https-agents-md|♯3089 Docs: update link to (source link)]] · Change
- 2025-09-02 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-02-4-agent-mode-changes-in-rust-v0-28-0|4 Agent Mode changes in rust-v0.28.0]] · Digest

**2025-08**

- 2025-08-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-29-2848-chore-try-to-make-it-easier-to-debug-the-flakiness-of-test-shell-command-ap|♯2848 chore: try to make it easier to debug the flakiness…]] · Change
- 2025-08-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-29-2-agent-mode-changes-in-rust-v0-27-0|2 Agent Mode changes in rust-v0.27.0]] · Digest
- 2025-08-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-26-5-agent-mode-changes-in-rust-v0-24-0|5 Agent Mode changes in rust-v0.24.0]] · Digest
- 2025-08-21 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-21-adding-task-progress-param-to-the-summarize-task-tool-call-by-0xtoshii-in-https|adding task_progress param to the summarize task tool call]] · Change
- 2025-08-20 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-08-20-added-a-new-feedback-reason-the-agent-didn-t-finish-the-job-by-xingyaoww-in-http|Added a new feedback reason: "The agent didn't finish the job"]] · Change
- 2025-08-14 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-14-7-agent-mode-changes-in-v0-1-21|7 Agent Mode changes in v0.1.21]] · Digest
- 2025-08-13 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-08-13-enhanced-the-cli-interface-by-adding-proper-markdown-rendering-for-agent-message|Enhanced the CLI interface by adding proper markdown rendering for agent messages…]] · Change
- 2025-08-12 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-12-feat-agent-introduce-foundational-subagent-architecture-by-abhipatel12-in-https|feat(agent): Introduce Foundational Subagent Architecture]] · Change
- 2025-08-06 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-08-06-improved-agent-tools-488891|Improved Agent tools]] · Change
- 2025-08-06 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-08-06-faster-background-agent-startup|Faster Background Agent startup]] · Change
- 2025-08-06 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-06-6-agent-mode-changes-in-v0-1-18|6 Agent Mode changes in v0.1.18]] · Digest
- 2025-08-05 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-05-6-agent-mode-changes-in-v0-1-17|6 Agent Mode changes in v0.1.17]] · Digest
- 2025-08-02 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-02-6-agent-mode-changes-in-v0-1-16|6 Agent Mode changes in v0.1.16]] · Digest

**2025-07**

- 2025-07-31 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-07-31-improved-the-resolver-summary-generation-by-instructing-the-agent-to-focus-only|Improved the resolver summary generation by instructing the agent to focus only…]] · Change
- 2025-07-30 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-30-6-agent-mode-changes-in-v0-1-15|6 Agent Mode changes in v0.1.15]] · Digest
- 2025-07-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-07-29-2-agent-mode-changes-in-1-3|2 Agent Mode changes in 1.3]] · Digest
- 2025-07-25 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-25-5-agent-mode-changes-in-v0-1-14|5 Agent Mode changes in v0.1.14]] · Digest
- 2025-07-24 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-07-24-2-agent-mode-changes-in-0-50-0|2 Agent Mode changes in 0.50.0]] · Digest
- 2025-07-19 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-07-19-https-github-com-openai-codex-pull-1589-changes-ctrl-d-so-it-only-exits-the-tui|(source link) changes ctrl-d so it only exits the TUI…]] · Change
- 2025-07-19 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-19-3-agent-mode-changes-in-v0-1-13|3 Agent Mode changes in v0.1.13]] · Digest
- 2025-07-03 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-07-03-2-agent-mode-changes-in-1-2|2 Agent Mode changes in 1.2]] · Digest

**2025-06**

- 2025-06-20 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-06-20-fixed-incorrect-tracking-for-cost-and-token-usage-for-main-agent-and-delegates-b|Fixed incorrect tracking for cost and token usage for main agent and delegates]] · Change
- 2025-06-12 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-06-12-improved-background-agent-reliability|Improved Background Agent reliability]] · Change
- 2025-06-10 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-06-10-ensured-prs-opened-by-agent-is-properly-tracked-in-conversation-metadata-by-malh|Ensured PRs opened by agent is properly tracked in conversation metadata]] · Change
- 2025-06-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-06-04-open-background-agent-control-panel-with-cmd-ctrl-e|Open Background Agent control panel with Cmd/Ctrl+E]] · Change

**2025-05**

- 2025-05-20 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-05-20-2-agent-mode-changes-in-0-39-0|2 Agent Mode changes in 0.39.0]] · Digest
- 2025-05-12 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-05-12-added-the-ability-for-the-agent-to-save-browser-screenshots-as-image-files-by-xi|Added the ability for the agent to save browser screenshots as image files]] · Change
- 2025-05-01 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-05-01-added-support-for-agent-pause-and-resume-functionality-in-the-cli-by-pandukamudi|Added support for agent pause and resume functionality in the CLI]] · Change

**2025-04**

- 2025-04-24 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-04-24-improve-prompting-for-new-task-tool|Improve prompting for new task tool]] · Change
- 2025-04-23 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-04-23-improved-logic-to-prevent-agent-from-getting-stuck-by-rbren-in-https-github-com|Improved logic to prevent agent from getting stuck]] · Change
- 2025-04-10 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-04-10-prompt-agent-to-follow-existing-pr-template-when-create-new-pr-by-xingyaoww-in-h|Prompt agent to follow existing PR template when create new PR]] · Change
- 2025-04-09 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-04-09-add-new-create-new-task-tool-to-let-cline-start-a-new-task-autonomously|Add new 'Create New Task' tool to let Cline start a new task autonomously!]] · Change

**2025-03**

- 2025-03-10 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-03-10-improve-agent-loop-tracking-by-rbren-in-https-github-com-all-hands-ai-openhands|Improve agent loop tracking]] · Change
- 2025-03-07 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-03-07-3-agent-mode-changes-in-0-28-0|3 Agent Mode changes in 0.28.0]] · Digest

**2025-02**

- 2025-02-19 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-02-19-agent-is-ready-agent-is-now-the-default-mode-bringing-a-more-powerful-and-unifie|Agent is ready: Agent is now the default mode, bringing a more powerful and unified…]] · Change
- 2025-02-19 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-02-19-agent-tool-limit-upon-reaching-the-25-tool-call-limit-you-can-press-continue-to|Agent tool limit]] · Change

**2025-01**

- 2025-01-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-01-23-agent-sees-recent-changes-the-agent-can-use-a-tool-to-see-your-recent-changes-it|Agent sees recent changes: The agent can use a tool to see your recent changes]] · Change
- 2025-01-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-01-23-cursor-rules-users-can-write-several-repository-level-rules-to-disk-in-the-curso|.cursor/rules: Users can write several repository-level rules to disk…]] · Change
- 2025-01-22 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-01-22-when-connecting-to-a-github-repo-the-agent-now-explicitly-knows-which-repo-was-c|When connecting to a GitHub repo, the agent now explicitly knows which repo…]] · Change
- 2025-01-07 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-01-07-added-ratelimiterror-status-on-ui-and-agent-state-by-rkat7-in-https-github-com-a|Added RateLimitError status on UI and Agent state]] · Change

</details>

</details>

<details class="disclosure">
<summary>2024 · 17 entries (Aider 2 · Cursor 2 · OpenHands 13)</summary>

**2024-12**

- 2024-12-19 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-12-19-agent-gets-stuck-in-closing-and-server-won-t-die-by-tofarr-in-https-github-com-a|Agent gets stuck in closing and server won't die]] · Change
- 2024-12-17 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-12-17-let-user-continue-when-the-agent-gets-stuck-in-a-loop-ui-only-by-enyst-in-https|Let user continue when the agent gets stuck in a loop (UI-only)]] · Change
- 2024-12-10 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-12-10-updated-shell-command-prompt|Updated shell command prompt]] · Change
- 2024-12-06 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-12-06-2-agent-mode-changes-in-0-15-1|2 Agent Mode changes in 0.15.1]] · Digest

**2024-11**

- 2024-11-08 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-11-08-2-agent-mode-changes-in-0-13-0|2 Agent Mode changes in 0.13.0]] · Digest

**2024-10**

- 2024-10-22 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-10-22-improvements-to-agent-editing-using-llm-by-xingyaoww-in-https-github-com-all-han|Improvements to Agent Editing using LLM]] · Change

**2024-09**

- 2024-09-04 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-09-04-files-display-updated-content-after-agent-edit-by-amanape-in-https-github-com-al|Files display updated content after agent edit]] · Change

**2024-08**

- 2024-08-29 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-08-29-specialize-codeact-into-micro-agents-by-xingyaoww-in-https-github-com-all-hands|Specialize CodeAct into micro agents]] · Change
- 2024-08-27 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-08-27-improved-shell-command-prompting|Improved shell command prompting]] · Change
- 2024-08-23 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-08-23-4-agent-mode-changes-in-0-9-0|4 Agent Mode changes in 0.9.0]] · Digest
- 2024-08-02 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-08-02-concurrent-composers-support-composer-control-panel-and-various-bug-fixes-such-a|Concurrent composers support, composer control panel, and various bug fixes such…]] · Change
- 2024-08-01 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-08-01-2-agent-mode-changes-in-0-8-3|2 Agent Mode changes in 0.8.3]] · Digest

**2024-07**

- 2024-07-27 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-07-27-4-agent-mode-changes-in-0-8-2|4 Agent Mode changes in 0.8.2]] · Digest
- 2024-07-13 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-07-13-3-agent-mode-changes-in-0-8-0|3 Agent Mode changes in 0.8.0]] · Digest
- 2024-07-05 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-07-05-2-agent-mode-changes-in-0-7-1|2 Agent Mode changes in 0.7.1]] · Digest

**2024-06**

- 2024-06-29 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-06-29-3-agent-mode-changes-in-0-7-0|3 Agent Mode changes in 0.7.0]] · Digest

**2024-02**

- 2024-02-15 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-02-15-interpreter-mode-we-ve-made-some-big-improvements-to-the-backend-powering-interp|Interpreter Mode: We've made some big improvements to the backend powering…]] · Change

</details>

<details class="disclosure" open>
<summary>2023 · 3 entries (Cursor 3)</summary>

**2023-07**

- 2023-07-10 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-07-10-this-nightly-build-comes-with-experimental-interface-agent-support|This nightly build comes with experimental interface agent support!]] · Change
- 2023-07-10 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-07-10-the-goal-you-write-an-interface-specification-and-an-agent-writes-both-the-tests|The goal: you write an interface specification, and an agent writes both the tests…]] · Change
- 2023-07-06 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]] · Change

</details>

</div>
<!-- chronolog:end -->