---
created: '2023-07-06'
date: '2026-11-06'
description: 'Research question: what changed in delegated execution?'
machine_hash: 8d4bbe9d36e7abdc73ec5e70fcd5af8de555558538677ecdb69e41ab8065edc6
modified: '2026-11-06'
products_involved:
- Aider
- ChatGPT
- Claude
- Claude Code
- Cline
- Codex CLI
- Cursor
- Dify
- ElevenLabs
- Gamma
- Gemini
- Gemini CLI
- GitHub Copilot CLI
- Google Antigravity
- Lovable
- Manus
- Ollama
- Open WebUI
- OpenClaw
- OpenCode
- OpenHands
- Replit
- Runway
- Windsurf
- v0
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

1,135 tracked changes across Aider, ChatGPT, Claude, Claude Code, Cline, Codex CLI, Cursor, Dify, ElevenLabs, Gamma, Gemini, Gemini CLI, GitHub Copilot CLI, Google Antigravity, Lovable, Manus, Ollama, Open WebUI, OpenClaw, OpenCode, OpenHands, Replit, Runway, Windsurf and v0 · 2023-07-06 → 2026-11-06 · OpenClaw averages 18.4 cards per release, ElevenLabs 8.1, Codex CLI 8.0, Open WebUI 7.6, Gemini CLI 7.5, Dify 7.2, Claude Code 7.0, GitHub Copilot CLI 6.3, OpenCode 6.0, Google Antigravity 5.0, Replit 4.9, Cursor 4.0, Lovable 3.9, OpenHands 3.8, Aider 3.7, Cline 3.0, Ollama 3.0, v0 2.9, Windsurf 2.6, Gamma 1.8, ChatGPT 1.7, Gemini 1.5, Claude 1.3, Manus 1.2, Runway 1.0
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
| Quarter | Aider | ChatGPT | Claude | Claude Code | Cline | Codex CLI | Cursor | Dify | ElevenLabs | Gamma | Gemini | Gemini CLI | GitHub Copilot CLI | Google Antigravity | Lovable | Manus | Ollama | Open WebUI | OpenClaw | OpenCode | OpenHands | Replit | Runway | Windsurf | v0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **First in archive** | <time datetime="2024-08-27">2024-08-27</time> [[Changes/Aider/2024-08-27-improved-shell-command-prompting\|Improved shell command prompting]] | <time datetime="2025-09-29">2025-09-29</time> [[Changes/ChatGPT/2025-09-29-we-re-introducing-instant-checkout-in-chatgpt-and-the-agentic-commerce-protocol-8cbf19\|ChatGPT introduces Instant Checkout and the Agentic Commerce Protocol that powers…]] | <time datetime="2025-12-18">2025-12-18</time> [[Changes/Claude/2025-12-18-skills-for-organizations-partners-and-the-ecosystem\|Skills for organizations, partners, and the ecosystem]] | <time datetime="2026-01-09">2026-01-09</time> [[Changes/Claude Code/2026-01-09-added-agent-type-to-sessionstart-hook-input-populated-if-agent-is-specified\|Added agent_type to SessionStart hook input, populated if --agent is specified]] | <time datetime="2025-04-09">2025-04-09</time> [[Changes/Cline/2025-04-09-add-new-create-new-task-tool-to-let-cline-start-a-new-task-autonomously\|Add new 'Create New Task' tool to let Cline start a new task autonomously!]] | <time datetime="2025-07-19">2025-07-19</time> [[Changes/Codex CLI/2025-07-19-https-github-com-openai-codex-pull-1589-changes-ctrl-d-so-it-only-exits-the-tui\|(source link) changes ctrl-d so it only exits the TUI…]] | <time datetime="2023-07-06">2023-07-06</time> [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas\|Agents, new docs]] | <time datetime="2023-07-18">2023-07-18</time> [[Changes/Dify/2023-07-18-feat-hide-password-setting-and-invitation-link-in-cloud-version-by-jzongkvo-in-h\|Feat: hide password setting and invitation link in cloud version]] | <time datetime="2024-10-13">2024-10-13</time> [[Changes/ElevenLabs/2024-10-13-agents-platform-beta-agents-platform-is-now-in-beta\|Agents Platform Beta: Agents Platform is now in beta]] | <time datetime="2025-09-16">2025-09-16</time> [[Changes/Gamma/2025-09-16-gamma-agent-your-ai-design-partner-that-does-it-all\|Gamma Agent: Your AI design partner that does it all]] | <time datetime="2025-11-18">2025-11-18</time> [[Changes/Gemini/2025-11-18-gemini-agent-is-now-available-on-the-web-to-google-ai-ultra-subscribers-18-in-th\|Gemini Agent is now available on the web, to Google AI Ultra subscribers 18+ in the US]] | <time datetime="2025-07-19">2025-07-19</time> [[Changes/Gemini CLI/2025-07-19-3-agent-mode-changes-in-v0-1-13\|3 Agent Mode changes in v0.1.13]] | <time datetime="2025-10-01">2025-10-01</time> [[Changes/GitHub Copilot CLI/2025-10-01-improved-the-experience-of-writing-prompts-while-the-agent-is-running-up-down-ar\|Improved the experience of writing prompts while the agent is running -- up/down…]] | <time datetime="2025-11-18">2025-11-18</time> [[Changes/Google Antigravity/2025-11-18-google-antigravity\|Google Antigravity]] | <time datetime="2025-08-11">2025-08-11</time> [[Changes/Lovable/2025-08-11-agent-mode-is-the-new-default-mode\|Agent Mode is the new default mode]] | <time datetime="2025-06-11">2025-06-11</time> [[Changes/Manus/2025-06-11-start-free-by-asking-any-question-and-get-instant-answers-need-more-power-one-cl\|Introducing Manus FREE Chat Mode!]] | <time datetime="2024-07-02">2024-07-02</time> [[Changes/Ollama/2024-07-02-2-agent-mode-changes-in-v0-2-0\|2 Agent Mode changes in v0.2.0]] | <time datetime="2024-09-04">2024-09-04</time> [[Changes/Open WebUI/2024-09-04-user-agent-in-comfyui-added-default-headers-in-comfyui-to-fix-access-issues-impr\|🛠️ User Agent in ComfyUI]] | <time datetime="2026-06-30">2026-06-30</time> [[Changes/OpenClaw/2026-06-30-32-agent-mode-changes-in-v2026-6-11\|32 Agent Mode changes in v2026.6.11]] | <time datetime="2025-12-30">2025-12-30</time> [[Changes/OpenCode/2025-12-30-desktop-more-defensive-agent-access-in-desktop-application\|Desktop More defensive agent access in desktop application]] | <time datetime="2024-06-29">2024-06-29</time> [[Changes/OpenHands/2024-06-29-3-agent-mode-changes-in-0-7-0\|3 Agent Mode changes in 0.7.0]] | <time datetime="2024-12-13">2024-12-13</time> [[Changes/Replit/2024-12-13-2-agent-mode-changes-in-replit-updates-2024-12-13\|2 Agent Mode changes in Replit updates — 2024-12-13]] | <time datetime="2026-06-25">2026-06-25</time> [[Changes/Runway/2026-06-25-make-marketing-that-drives-revenue-runway-agent-creates-entire-campaigns-analyze\|Agent 2.0]] | <time datetime="2025-10-23">2025-10-23</time> [[Changes/Windsurf/2025-10-23-support-and-fixes-for-agents-md\|Support and fixes for AGENTS.md]] | <time datetime="2025-12-09">2025-12-09</time> [[Changes/v0/2025-12-09-v0-has-now-automatically-updated-every-react2shell-vulnerable-project-deployed-w\|React2Shell Vulnerability Patch]] |
| 2026 Q3 | · | <time datetime="2026-09-29">2026-09-29</time> [[Changes/ChatGPT/2026-09-29-we-re-introducing-dots-always-on-agents-in-chatgpt-that-can-take-on-ongoing-work-24bef5\|ChatGPT introduces dots]]<br><time datetime="2026-07-09">2026-07-09</time> [[Changes/ChatGPT/2026-07-09-chatgpt-work-is-an-agent-for-longer-more-involved-tasks-it-can-research-and-anal\|ChatGPT Work is an agent for longer, more involved tasks]] | · | <time datetime="2026-07-11">2026-07-11</time> [[Changes/Claude Code/2026-07-11-auto-mode-is-now-available-without-claude-code-enable-auto-mode-opt-in-on-bedroc\|Auto mode is now available without CLAUDE_CODE_ENABLE_AUTO_MODE opt-in on Bedrock…]] | · | · | <time datetime="2026-09-10">2026-09-10</time> [[Changes/Cursor/2026-09-10-a-project-runs-on-its-own-computer-in-the-cloud-so-closing-your-laptop-doesn-t-s\|Powered by Cloud Agents]] | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · |
| 2026 Q2 | · | · | · | <time datetime="2026-06-10">2026-06-10</time> [[Changes/Claude Code/2026-06-10-sub-agents-can-now-spawn-their-own-sub-agents-up-to-5-levels-deep\|Sub-agents can now spawn their own sub-agents (up to 5 levels deep)]]<br><time datetime="2026-05-28">2026-05-28</time> [[Changes/Claude Code/2026-05-28-introducing-dynamic-workflows-ask-claude-to-create-a-workflow-and-it-orchestrate\|Introducing dynamic workflows]]<br><time datetime="2026-04-16">2026-04-16</time> [[Changes/Claude Code/2026-04-16-auto-mode-no-longer-requires-enable-auto-mode\|Auto mode no longer requires --enable-auto-mode]] | · | · | · | · | · | · | · | · | · | · | · | · | · | · | archive begins <time datetime="2026-06-30">2026-06-30</time> | · | · | · | · | · | · |
| 2026 Q1 | · | · | · | · | · | · | <time datetime="2026-01-22">2026-01-22</time> [[Changes/Cursor/2026-01-22-subagents\|Subagents]] | · | · | · | · | · | · | · | · | · | · | · | <span class="not-archived">not archived</span> | · | · | · | · | · | · |
| 2025 Q4 | · | · | · | archive begins <time datetime="2025-12-19">2025-12-19</time> | · | · | <time datetime="2025-10-29">2025-10-29</time> [[Changes/Cursor/2025-10-29-multi-agents-bb4f56\|Multi-Agents]] | · | · | · | · | · | · | archive begins <time datetime="2025-11-18">2025-11-18</time> | · | · | · | · | <span class="not-archived">not archived</span> | archive begins <time datetime="2025-12-19">2025-12-19</time> | · | · | · | · | archive begins <time datetime="2025-10-01">2025-10-01</time> |
| 2025 Q3 | · | <time datetime="2025-09-29">2025-09-29</time> [[Changes/ChatGPT/2025-09-29-we-re-introducing-instant-checkout-in-chatgpt-and-the-agentic-commerce-protocol-8cbf19\|ChatGPT introduces Instant Checkout and the Agentic Commerce Protocol that powers…]] | archive begins <time datetime="2025-08-01">2025-08-01</time> | <span class="not-archived">not archived</span> | · | · | · | · | · | · | · | · | archive begins <time datetime="2025-09-26">2025-09-26</time> | <span class="not-archived">not archived</span> | · | · | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | · | · | · | <span class="not-archived">not archived</span> |
| 2025 Q2 | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2025-06-30">2025-06-30</time> | <time datetime="2025-06-04">2025-06-04</time> [[Changes/Cursor/2025-06-04-background-agent-for-everyone-8b35dc\|Background Agent for everyone]]<br><time datetime="2025-05-15">2025-05-15</time> [[Changes/Cursor/2025-05-15-background-agent-preview\|Background Agent (Preview)]] | · | · | · | · | archive begins <time datetime="2025-06-28">2025-06-28</time> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2025-05-11">2025-05-11</time> | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | · | · | archive begins <time datetime="2025-04-02">2025-04-02</time> | <span class="not-archived">not archived</span> |
| 2025 Q1 | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <time datetime="2025-02-19">2025-02-19</time> [[Changes/Cursor/2025-02-19-agent-is-ready-agent-is-now-the-default-mode-bringing-a-more-powerful-and-unifie\|Agent is ready: Agent is now the default mode, bringing a more powerful and unified…]] | · | · | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |
| 2023 Q4 → 2024 Q4 | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-07-28">2024-07-28</time> | <span class="not-archived">not archived</span> | · | · | archive begins <time datetime="2024-10-13">2024-10-13</time> | archive begins <time datetime="2024-02-14">2024-02-14</time> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-12-03">2024-12-03</time> | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2024-02-23">2024-02-23</time> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-06-04">2024-06-04</time> | archive begins <time datetime="2024-12-13">2024-12-13</time> | archive begins <time datetime="2024-01-08">2024-01-08</time> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |
| 2023 Q3 | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <time datetime="2023-07-06">2023-07-06</time> [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas\|Agents, new docs]] | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | archive begins <time datetime="2023-07-08">2023-07-08</time> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |

First in archive: each product's earliest tracked change in this theme. "·" marks a quarter without a key moment, and "not archived" a quarter before the product's archive begins. Archives begin: Aider 2023-06-07 · ChatGPT 2022-12-15 · Claude 2025-08-01 · Claude Code 2025-12-19 · Cline 2024-07-28 · Codex CLI 2025-06-30 · Cursor 2023-03-14 · Dify 2023-05-15 · ElevenLabs 2024-10-13 · Gamma 2024-02-14 · Gemini 2023-04-10 · Gemini CLI 2025-06-28 · GitHub Copilot CLI 2025-09-26 · Google Antigravity 2025-11-18 · Lovable 2024-12-03 · Manus 2025-05-11 · Ollama 2023-07-08 · Open WebUI 2024-02-23 · OpenClaw 2026-06-30 · OpenCode 2025-12-19 · OpenHands 2024-06-04 · Replit 2024-12-13 · Runway 2024-01-08 · Windsurf 2025-04-02 · v0 2025-10-01.
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
<label><input type="radio" name="timeline-product" id="tl-only-3"> Claude</label>
<label><input type="radio" name="timeline-product" id="tl-only-4"> Claude Code</label>
<label><input type="radio" name="timeline-product" id="tl-only-5"> Cline</label>
<label><input type="radio" name="timeline-product" id="tl-only-6"> Codex CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-7"> Cursor</label>
<label><input type="radio" name="timeline-product" id="tl-only-8"> Dify</label>
<label><input type="radio" name="timeline-product" id="tl-only-9"> ElevenLabs</label>
<label><input type="radio" name="timeline-product" id="tl-only-10"> Gamma</label>
<label><input type="radio" name="timeline-product" id="tl-only-11"> Gemini</label>
<label><input type="radio" name="timeline-product" id="tl-only-12"> Gemini CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-13"> GitHub Copilot CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-14"> Google Antigravity</label>
<label><input type="radio" name="timeline-product" id="tl-only-15"> Lovable</label>
<label><input type="radio" name="timeline-product" id="tl-only-16"> Manus</label>
<label><input type="radio" name="timeline-product" id="tl-only-17"> Ollama</label>
<label><input type="radio" name="timeline-product" id="tl-only-18"> Open WebUI</label>
<label><input type="radio" name="timeline-product" id="tl-only-19"> OpenClaw</label>
<label><input type="radio" name="timeline-product" id="tl-only-20"> OpenCode</label>
<label><input type="radio" name="timeline-product" id="tl-only-21"> OpenHands</label>
<label><input type="radio" name="timeline-product" id="tl-only-22"> Replit</label>
<label><input type="radio" name="timeline-product" id="tl-only-23"> Runway</label>
<label><input type="radio" name="timeline-product" id="tl-only-24"> Windsurf</label>
<label><input type="radio" name="timeline-product" id="tl-only-25"> v0</label>
</fieldset>

<details class="disclosure">
<summary>2026 · 788 entries (ChatGPT 3 · Claude 2 · Claude Code 126 · Cline 12 · Codex CLI 72 · Cursor 89 · Dify 15 · ElevenLabs 98 · Gamma 1 · Gemini 1 · Gemini CLI 26 · GitHub Copilot CLI 82 · Google Antigravity 34 · Lovable 16 · Ollama 15 · Open WebUI 7 · OpenClaw 25 · OpenCode 58 · OpenHands 26 · Replit 53 · Runway 8 · Windsurf 10 · v0 9)</summary>

**2026-11**

- 2026-11-03 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2026-11-03-lovable-follows-agents-md-files-in-your-project-s-subfolders|Lovable follows AGENTS.md files in your project's subfolders]] · Launch
- 2026-11-03 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-11-03-you-can-now-work-directly-in-a-folder-on-another-computer-connected-to-openclaw|Work directly in a folder on another computer connected to OpenClaw]] · Change
- 2026-11-02 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-11-02-elevenlabs-cli|ElevenLabs CLI]] · Launch
- 2026-11-02 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-11-02-analysis-items-api|Analysis items API]] · Launch
- 2026-11-02 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-11-02-elevenagents|ElevenAgents]] · Launch
- 2026-11-02 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-11-02-workspaces|Workspaces]] · Launch

**2026-10**

- 2026-10-30 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-10-30-guided-claude-agent-setup|Guided Claude Agent Setup]] · Launch
- 2026-10-30 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-10-30-contribute-to-your-company-codebase-with-cloud-agents|Contribute to your company codebase with Cloud Agents]] · Launch
- 2026-10-30 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-10-30-message-and-create-chats-with-agent|Message and create chats with Agent]] · Launch
- 2026-10-27 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-27-you-can-now-attach-files-of-any-type-such-as-videos-design-files-or-programs-up|Attach files of any type, such as videos, design files, or programs, up to 20 MB]] · Change
- 2026-10-26 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-26-knowledge-base-crawl-exclusions|Knowledge base crawl exclusions]] · Launch
- 2026-10-26 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-26-elevenagents|ElevenAgents]] · Launch
- 2026-10-23 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-10-23-stripe-atlas-on-replit|Stripe Atlas on Replit]] · Launch
- 2026-10-23 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-10-23-monitoring-agent|Monitoring Agent]] · Launch
- 2026-10-23 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-10-23-create-and-update-skills-with-agent|Create and update skills with Agent]] · Launch
- 2026-10-23 · <span class="tl-product tl-p24">**Windsurf**</span> · [[Changes/Windsurf/2026-10-23-new-agent-window|New Agent Window]] · Launch
- 2026-10-21 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2026-10-21-claude-duet-research-preview-for-pro-and-max-plans|Claude Duet research preview for Pro and Max plans]] · Launch
- 2026-10-20 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-10-20-deploy-agents-wherever-you-need-them|Deploy agents wherever you need them]] · Launch
- 2026-10-20 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-10-20-evals|Evals]] · Launch
- 2026-10-20 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-10-20-agents-as-code|Agents as code]] · Launch
- 2026-10-19 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-19-added-claude-api-managed-agents-secure-which-compares-a-managed-agents-agent-s-s|Added /claude-api managed-agents-secure, which compares a Managed Agents agent's…]] · Change
- 2026-10-19 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-19-javascript-sdk|JavaScript SDK]] · Launch
- 2026-10-19 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-19-elevenagents-b18b24|ElevenAgents]] · Launch
- 2026-10-19 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-19-elevenagents-ee74ab|ElevenAgents]] · Launch
- 2026-10-16 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-10-16-environments-api|Environments API]] · Launch
- 2026-10-16 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-10-16-canvases-from-cloud-agents|Canvases from cloud agents]] · Launch
- 2026-10-15 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-15-you-can-now-type-compact-to-summarize-a-long-conversation-so-far-and-free-up-roo|Type /compact to summarize a long conversation so far and free up room for the agent…]] · Change
- 2026-10-13 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2026-10-13-let-browser-agents-use-your-app|Let browser agents use your app]] · Launch
- 2026-10-12 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-12-elevenagents|ElevenAgents]] · Launch
- 2026-10-12 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-12-elevenagents-545be2|ElevenAgents]] · Launch
- 2026-10-12 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-12-you-can-now-attach-zip-archives-to-a-prompt-and-the-agent-unpacks-them-with-its|Attach .zip archives to a prompt, and the agent unpacks them with its tools]] · Change
- 2026-10-06 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-10-06-you-can-now-see-and-reply-to-the-local-agents-running-on-your-computer-from-the|See and reply to the local agents running on your computer from the Cursor iOS app]] · Change
- 2026-10-06 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-10-06-remote-control-doesn-t-move-your-agents-anywhere-it-keeps-running-on-your-comput|Agents keep running on your computer]] · Launch
- 2026-10-06 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-10-06-added-canonical-redirects-and-json-and-markdown-data-formats-for-agent-readable|Added canonical redirects and JSON and Markdown data formats for agent-readable stats]] · Launch
- 2026-10-05 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-url-to-set-up-the-managed-agents-pattern|Added /claude-api managed-agents-onboard url to set up the Managed Agents…]] · Change
- 2026-10-05 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-quickstart-name-to-build-a-console-quick|Added /claude-api managed-agents-onboard quickstart-name to build a Console…]] · Change
- 2026-10-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-05-elevenagents|ElevenAgents]] · Launch
- 2026-10-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-05-elevenagents-5bf5b0|ElevenAgents]] · Launch
- 2026-10-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-05-elevenagents-ceeb34|ElevenAgents]] · Launch

**2026-09**

- 2026-09-30 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-30-message-subagents-directly-export-markdown-as-pdf-and-conversation-only-undo|Message subagents directly, export Markdown as PDF, and conversation-only undo]] · Launch
- 2026-09-30 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-30-you-can-now-send-a-message-directly-to-a-subagent-from-the-message-box-without-g|Send a message directly to a subagent from the message box, without going through…]] · Change
- 2026-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-29-we-re-introducing-dots-always-on-agents-in-chatgpt-that-can-take-on-ongoing-work-24bef5|ChatGPT introduces dots]] · Launch
- 2026-09-28 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-09-28-elevenagents|ElevenAgents]] · Launch
- 2026-09-22 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-22-windows-subsystem-for-linux-office-attachments-and-live-subagent-cards|Windows Subsystem for Linux, Office attachments, and live subagent cards]] · Launch
- 2026-09-22 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-22-plan-before-you-build|Plan before you build]] · Launch
- 2026-09-21 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-09-21-elevenagents|ElevenAgents]] · Launch
- 2026-09-21 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-09-21-elevenagents-d15bdd|ElevenAgents]] · Launch
- 2026-09-21 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2026-09-21-manage-agent-permissions-from-your-account-settings|Manage agent permissions from your account settings]] · Launch
- 2026-09-19 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-19-you-can-now-set-the-approval-reviewer-s-reasoning-and-optional-fast-mode-indepen|Set the approval reviewer's reasoning and optional Fast mode independently…]] · Change
- 2026-09-18 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-09-18-connect-custom-apis-to-agent|Connect custom APIs to Agent]] · Launch
- 2026-09-14 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-09-14-elevenagents|ElevenAgents]] · Launch
- 2026-09-14 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-09-14-elevenagents-d9e798|ElevenAgents]] · Launch
- 2026-09-10 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-09-10-a-project-runs-on-its-own-computer-in-the-cloud-so-closing-your-laptop-doesn-t-s|Powered by Cloud Agents]] · Launch
- 2026-09-10 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-09-10-subscriptions|Subscriptions]] · Launch
- 2026-09-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-09-07-javascript-sdk|JavaScript SDK]] · Launch
- 2026-09-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-09-07-elevenagents|ElevenAgents]] · Launch
- 2026-09-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-09-07-python-sdk|Python SDK]] · Launch
- 2026-09-05 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-05-swarm-is-now-available-to-eligible-agents-without-a-separate-enablement-step-so|Swarm is now available to eligible agents without a separate enablement step…]] · Launch
- 2026-09-04 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-09-04-understand-app-usage-with-project-analytics|Understand app usage with Project Analytics]] · Launch
- 2026-09-04 · <span class="tl-product tl-p23">**Runway**</span> · [[Changes/Runway/2026-09-04-team-is-a-new-self-serve-plan-for-small-teams-that-create-together-in-runway-eve|Introducing Team Plan]] · Launch
- 2026-09-02 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-09-02-run-on-your-sandboxes|Run on your sandboxes]] · Launch
- 2026-09-02 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-09-02-computer-use-on-linux-and-mac|Computer use on Linux and Mac]] · Launch

**2026-08**

- 2026-08-31 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-31-elevenlabs-cli|ElevenLabs CLI]] · Launch
- 2026-08-31 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-31-elevenagents|ElevenAgents]] · Launch
- 2026-08-28 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-08-28-find-your-first-customers-with-growth-skills|Find your first customers with Growth Skills]] · Launch
- 2026-08-28 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-08-28-agent|Agent]] · Launch
- 2026-08-27 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-08-27-cursor-now-port-forwards-your-cloud-agent-s-live-environment-straight-to-your-br|A live preview, right in the browser]] · Launch
- 2026-08-26 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2026-08-26-add-your-app-to-slack-as-an-agent|Add your app to Slack as an agent]] · Launch
- 2026-08-24 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-24-elevenagents|ElevenAgents]] · Launch
- 2026-08-24 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-24-procedures|Procedures]] · Launch
- 2026-08-21 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-08-21-surface-failed-subagent-tool-calls-with-a-resumable-task-id|Surface failed subagent tool calls with a resumable task_id]] · Launch
- 2026-08-21 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-08-21-agent|Agent]] · Launch
- 2026-08-21 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-08-21-steer-agent-while-working|Steer Agent while working]] · Launch
- 2026-08-19 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-08-19-custom-modes|Custom modes]] · Launch
- 2026-08-19 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-08-19-subscriptions|Subscriptions]] · Launch
- 2026-08-19 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-08-19-steering-improvements|Steering improvements]] · Launch
- 2026-08-19 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-08-19-subagents-on-their-own-machines|Subagents on their own machines]] · Launch
- 2026-08-19 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-08-19-goal|/goal]] · Launch
- 2026-08-17 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-08-17-agents-in-every-repo|Agents in every repo]] · Launch
- 2026-08-17 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-17-elevenagents|ElevenAgents]] · Launch
- 2026-08-17 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-17-elevenagents-fdc84e|ElevenAgents]] · Launch
- 2026-08-14 · <span class="tl-product tl-p17">**Ollama**</span> · [[Changes/Ollama/2026-08-14-this-release-adds-the-support-of-qwen-3-8-27b-https-ollama-com-library-qwen3-8-q|Ollama adds the support of Qwen 3.8 27B((source link)]] · Launch
- 2026-08-14 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-08-14-ask-for-inline-charts|Ask for inline charts]] · Launch
- 2026-08-13 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-13-subagent-forking-is-now-on-by-default-a-subagent-type-fork-subagent-inherits-the|Subagent forking is now on by default]] · Change
- 2026-08-13 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-08-13-when-a-bad-commit-or-dependency-update-breaks-your-environment-agents-keep-using|More resilient agent runs]] · Launch
- 2026-08-10 · <span class="tl-product tl-p17">**Ollama**</span> · [[Changes/Ollama/2026-08-10-muse-glimmer-is-now-available-on-all-platforms-muse-glimmer-can-power-coding-age|Muse Glimmer is now available on all platforms]] · Launch
- 2026-08-07 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-08-07-agent|Agent]] · Launch
- 2026-08-03 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-03-elevenagents|ElevenAgents]] · Launch
- 2026-08-03 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-03-packages|Packages]] · Launch

**2026-07**

- 2026-07-31 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-07-31-agent|Agent]] · Launch
- 2026-07-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-07-29-on-iphone-and-ipad-the-review-screen-now-covers-the-full-pr-comments-checks-and|A full review surface]] · Launch
- 2026-07-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-07-29-inbox|Inbox]] · Launch
- 2026-07-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-07-27-elevenagents|ElevenAgents]] · Launch
- 2026-07-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-07-27-elevenagents-9c1cea|ElevenAgents]] · Launch
- 2026-07-20 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-07-20-cli|CLI]] · Launch
- 2026-07-20 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-07-20-elevenagents|ElevenAgents]] · Launch
- 2026-07-15 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2026-07-15-let-ai-assistants-use-your-published-app|Let AI assistants use your published app]] · Launch
- 2026-07-14 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2026-07-14-see-images-videos-and-files-the-agent-works-with-in-chat|See images, videos, and files the agent works with in chat]] · Launch
- 2026-07-13 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-07-13-python-sdk|Python SDK]] · Launch
- 2026-07-13 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-07-13-elevenagents|ElevenAgents]] · Launch
- 2026-07-13 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-07-13-javascript-sdk|JavaScript SDK]] · Launch
- 2026-07-11 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-11-auto-mode-is-now-available-without-claude-code-enable-auto-mode-opt-in-on-bedroc|Auto mode is now available without CLAUDE_CODE_ENABLE_AUTO_MODE opt-in on Bedrock…]] · Expansion
- 2026-07-10 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-07-10-new-cloud-agent-hooks|New cloud agent hooks]] · Launch
- 2026-07-10 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-07-10-connect-excalidraw-to-agent|Connect Excalidraw to Agent]] · Launch
- 2026-07-10 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-07-10-editors-can-answer-agent-s-questions|Editors can answer Agent's questions]] · Launch
- 2026-07-06 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-07-06-cli|CLI]] · Launch
- 2026-07-06 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-07-06-elevenagents-c38b88|ElevenAgents]] · Launch
- 2026-07-06 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-07-06-elevenagents-f45a54|ElevenAgents]] · Policy
- 2026-07-03 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-07-03-sell-in-your-app-with-whop|Sell in your app with Whop]] · Launch
- 2026-07-02 · <span class="tl-product tl-p23">**Runway**</span> · [[Changes/Runway/2026-07-02-introducing-agent-skills-build-an-ad-campaign-create-a-commercial-localize-your|Runway Agent Skills]] · Launch

**2026-06**

- 2026-06-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-29-cloud-agents-on-mobile-1bc371|Cloud agents on mobile]] · Launch
- 2026-06-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-29-remote-control-3ec330|Remote Control]] · Launch
- 2026-06-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-29-live-activities-and-push-notifications|Live Activities and push notifications]] · Launch
- 2026-06-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-29-cursor-for-ios-is-now-available-in-public-beta-on-all-paid-plans-launch-and-mana|Cursor for iOS is now available in public beta on all paid plans]] · Launch
- 2026-06-29 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-29-elevenagents|ElevenAgents]] · Launch
- 2026-06-29 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-29-elevenagents-a80e26|ElevenAgents]] · Launch
- 2026-06-29 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-29-elevenagents-d1c29a|ElevenAgents]] · Launch
- 2026-06-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-22-elevenagents|ElevenAgents]] · Launch
- 2026-06-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-22-elevenagents-c51c4d|ElevenAgents]] · Launch
- 2026-06-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-22-elevenagents-ee09f3|ElevenAgents]] · Launch
- 2026-06-19 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-06-19-agent|Agent]] · Launch
- 2026-06-17 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-17-handoff-between-local-and-cloud|Handoff between local and cloud]] · Launch
- 2026-06-17 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-17-this-release-introduces-updates-to-cloud-agents-in-the-agents-window-of-the-curs|Cursor introduces updates to cloud agents in the Agents Window of the Cursor desktop app]] · Launch
- 2026-06-17 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-17-cloud-subagents-with-in-cloud-eb7958|Cloud subagents with /in-cloud]] · Launch
- 2026-06-15 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-15-elevenagents|ElevenAgents]] · Launch
- 2026-06-12 · <span class="tl-product tl-p10">**Gamma**</span> · [[Changes/Gamma/2026-06-12-edit-on-the-go|Edit on the go]] · Launch
- 2026-06-12 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-06-12-block-malicious-packages-with-package-firewall|Block malicious packages with Package Firewall]] · Launch
- 2026-06-12 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-06-12-customize-agent-with-workspace-instructions-and-skills|Customize Agent with workspace instructions and skills]] · Launch
- 2026-06-12 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-06-12-agent|Agent]] · Launch
- 2026-06-10 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-06-10-let-subagents-use-their-own-configured-permissions-again|Let subagents use their own configured permissions again]] · Launch
- 2026-06-09 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2026-06-09-publish-from-chat|Publish from chat]] · Launch
- 2026-06-08 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-08-elevenagents|ElevenAgents]] · Launch
- 2026-06-05 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-05-ask-the-agent-to-make-one-match-the-other-remove-repeated-content-or-adjust-a-gr|Multi-select elements]] · Launch
- 2026-06-05 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-06-05-agent|Agent]] · Launch
- 2026-06-05 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-06-05-improve-your-search-ranking-with-seo-agent|Improve your search ranking with SEO Agent]] · Launch
- 2026-06-05 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-06-05-sell-physical-products-with-shopify|Sell physical products with Shopify]] · Launch
- 2026-06-04 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-04-jsonl-and-custom-stores|JSONL and custom stores]] · Launch
- 2026-06-04 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-04-auto-review|Auto-review]] · Launch
- 2026-06-04 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-04-nested-subagents|Nested subagents]] · Launch

**2026-05**

- 2026-05-29 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-05-29-agent|Agent]] · Launch
- 2026-05-29 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-05-29-agent-can-generate-music-sound-effects-and-speech|Agent can generate music, sound effects, and speech]] · Launch
- 2026-05-28 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-28-introducing-dynamic-workflows-ask-claude-to-create-a-workflow-and-it-orchestrate|Introducing dynamic workflows]] · Launch
- 2026-05-27 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2026-05-27-subagents|Subagents]] · Launch
- 2026-05-27 · <span class="tl-product tl-p24">**Windsurf**</span> · [[Changes/Windsurf/2026-05-27-devin-local|Devin Local]] · Launch
- 2026-05-25 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-05-25-elevenagents|ElevenAgents]] · Launch
- 2026-05-22 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-05-22-agent-suggests-power-mode-when-you-re-stuck|Agent suggests Power Mode when you're stuck]] · Launch
- 2026-05-22 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-05-22-agent-settings-stay-yours-in-shared-projects|Agent settings stay yours in shared projects]] · Launch
- 2026-05-22 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-05-22-agent|Agent]] · Launch
- 2026-05-20 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-05-20-loop-skill|/loop skill]] · Launch
- 2026-05-19 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-19-added-resume-support-for-background-sessions-sessions-started-via-claude-bg-or-a|Added /resume support for background sessions]] · Change
- 2026-05-19 · <span class="tl-product tl-p11">**Gemini**</span> · [[Changes/Gemini/2026-05-19-gemini-spark-is-your-24-7-personal-ai-agent|Gemini Spark is your 24/7 personal AI agent]] · Launch
- 2026-05-18 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-05-18-composer-2-5-is-now-available-in-cursor|Composer 2.5 is now available in Cursor]] · Launch
- 2026-05-18 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-05-18-elevenagents|ElevenAgents]] · Launch
- 2026-05-18 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-05-18-elevenagents-ddcb34|ElevenAgents]] · Launch
- 2026-05-18 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2026-05-18-build-and-plan-mode-switch|Build and Plan mode switch]] · Launch
- 2026-05-15 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-05-15-added-experimental-background-subagents-so-tasks-can-keep-running-while-you-cont|Added experimental background subagents so tasks can keep running while you continue…]] · Launch
- 2026-05-15 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-05-15-agent|Agent]] · Launch
- 2026-05-13 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-05-13-this-release-introduces-quality-of-life-improvements-to-the-agents-window|Cursor introduces quality-of-life improvements to the Agents Window]] · Launch
- 2026-05-13 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-05-13-cloud-agents-and-automations-now-support-multi-repo-environments-building-off-ou|Multi-repo environments]] · Launch
- 2026-05-13 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-05-13-packages|Packages]] · Launch
- 2026-05-08 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-05-08-new-animated-icons-for-agent-modes|New animated icons for Agent modes]] · Launch
- 2026-05-08 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-05-08-agent|Agent]] · Launch
- 2026-05-08 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-05-08-agent-accepts-svg-uploads|Agent accepts SVG uploads]] · Launch
- 2026-05-06 · <span class="tl-product tl-p24">**Windsurf**</span> · [[Changes/Windsurf/2026-05-06-agent-command-center|Agent Command Center]] · Launch
- 2026-05-01 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-05-01-create-full-slide-decks-with-agent|Create full Slide Decks with Agent]] · Launch
- 2026-05-01 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-05-01-agent|Agent]] · Launch

**2026-04**

- 2026-04-29 · <span class="tl-product tl-p24">**Windsurf**</span> · [[Changes/Windsurf/2026-04-29-devin-agent-in-windsurf|Devin Agent in Windsurf]] · Launch
- 2026-04-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-27-swift-sdk|Swift SDK]] · Launch
- 2026-04-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-27-packages|Packages]] · Launch
- 2026-04-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-27-elevenagents-e7cc6e|ElevenAgents]] · Launch
- 2026-04-24 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-24-multi-root-workspaces-in-agents-window|Multi-root workspaces in Agents Window]] · Launch
- 2026-04-24 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-24-worktrees-in-agents-window-44e81c|Worktrees in Agents Window]] · Launch
- 2026-04-24 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-24-this-release-introduces-a-new-way-to-multitask-with-async-subagents-an-improved|Cursor introduces a new way to multitask with async subagents, an improved worktrees…]] · Launch
- 2026-04-24 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-24-multitask-in-agents-window-9bc7ed|Multitask in Agents Window]] · Launch
- 2026-04-24 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-04-24-agent|Agent]] · Launch
- 2026-04-24 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-04-24-cve-auto-protect-patches-critical-vulnerabilities-automatically|CVE Auto-Protect patches critical vulnerabilities automatically]] · Launch
- 2026-04-20 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-20-elevenagents|ElevenAgents]] · Launch
- 2026-04-17 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-04-17-agent-suggests-follow-up-tasks|Agent suggests follow-up tasks]] · Launch
- 2026-04-17 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-04-17-agent|Agent]] · Launch
- 2026-04-17 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-04-17-new-agent-modes-dropdown|New Agent modes dropdown]] · Launch
- 2026-04-17 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-04-17-replit-agent-on-google-cloud-marketplace|Replit Agent on Google Cloud Marketplace]] · Launch
- 2026-04-15 · <span class="tl-product tl-p24">**Windsurf**</span> · [[Changes/Windsurf/2026-04-15-devin-in-windsurf|Devin in Windsurf]] · Launch
- 2026-04-15 · <span class="tl-product tl-p24">**Windsurf**</span> · [[Changes/Windsurf/2026-04-15-agent-command-center|Agent Command Center]] · Launch
- 2026-04-14 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-14-ask-a-quick-side-question-without-derailing-the-agent-s-main-task-btw-allows-you|/btw support in CLI]] · Launch
- 2026-04-13 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-13-tiled-layout-2f03f6|Tiled layout]] · Launch
- 2026-04-13 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-13-this-release-introduces-improvements-to-our-agents-window-interface-as-part-of-c|Cursor introduces improvements to our Agents Window interface as part of Cursor 3]] · Launch
- 2026-04-13 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-13-branch-selection-in-empty-state|Branch selection in empty state]] · Launch
- 2026-04-13 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-13-elevenagents|ElevenAgents]] · Launch
- 2026-04-10 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-04-10-agent|Agent]] · Launch
- 2026-04-10 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-04-10-recreate-any-ui-from-a-screenshot|Recreate any UI from a screenshot]] · Launch
- 2026-04-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-07-new-endpoints|New Endpoints]] · Launch
- 2026-04-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-07-elevenagents|ElevenAgents]] · Launch
- 2026-04-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-07-elevenagents-e46dc6|ElevenAgents]] · Launch
- 2026-04-07 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-04-07-agent-permissions|Agent Permissions]] · Launch
- 2026-04-03 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-04-03-agent|Agent]] · Launch
- 2026-04-02 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-02-design-mode|Design Mode]] · Launch
- 2026-04-02 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-02-agents-window-da5689|Agents Window]] · Launch
- 2026-04-02 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2026-04-02-ai-powered-visual-edits|AI-powered visual edits]] · Launch
- 2026-04-01 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-01-elevenagents|ElevenAgents]] · Launch
- 2026-04-01 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-01-packages|Packages]] · Launch
- 2026-04-01 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-01-new-endpoints|New Endpoints]] · Launch

**2026-03**

- 2026-03-23 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-23-elevenagents|ElevenAgents]] · Launch
- 2026-03-23 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-23-python-sdk|Python SDK]] · Launch
- 2026-03-20 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-03-20-empty-project-creation|Empty project creation]] · Launch
- 2026-03-17 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2026-03-17-control-cowork-from-your-phone-with-a-persistent-thread-research-preview-for-pro|Control Cowork from your phone with a persistent thread (research preview for Pro/Max)]] · Launch
- 2026-03-16 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-16-elevenagents|ElevenAgents]] · Launch
- 2026-03-13 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-03-13-agent|Agent]] · Launch
- 2026-03-13 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-03-13-introducing-replit-agent-4|Introducing Replit Agent 4]] · Launch
- 2026-03-09 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-09-python-sdk|Python SDK]] · Launch
- 2026-03-09 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-09-elevenagents-63860d|ElevenAgents]] · Launch
- 2026-03-09 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-09-elevencreative-studio|ElevenCreative Studio]] · Launch
- 2026-03-09 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-09-javascript-sdk|JavaScript SDK]] · Launch
- 2026-03-04 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-03-04-cursor-is-now-available-in-intellij-idea-pycharm-webstorm-and-other-jetbrains-id-2dc9cd|Cursor is now available in IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains…]] · Expansion
- 2026-03-02 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-02-you-can-now-fork-a-thread-into-sub-agents-making-it-easier-to-branch-work-withou|Fork a thread into sub-agents, making it easier to branch work without leaving…]] · Change
- 2026-03-02 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-02-new-schemas|New Schemas]] · Launch
- 2026-03-02 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-02-elevenagents-bb56b9|ElevenAgents]] · Launch

**2026-02**

- 2026-02-23 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-23-elevenagents|ElevenAgents]] · Launch
- 2026-02-20 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-02-20-production-deployment-logs-access|Production deployment logs access]] · Launch
- 2026-02-17 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-02-17-async-subagents|Async subagents]] · Launch
- 2026-02-17 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-02-17-this-release-introduces-plugins-for-extending-cursor-improvements-to-core-agent|Cursor introduces plugins for extending Cursor, improvements to core agent…]] · Launch
- 2026-02-16 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-16-widget-packages|Widget Packages]] · Launch
- 2026-02-16 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-16-elevenagents|ElevenAgents]] · Launch
- 2026-02-16 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-16-elevenagents-31304c|ElevenAgents]] · Launch
- 2026-02-16 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-16-new-endpoints|New Endpoints]] · Launch
- 2026-02-13 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-02-13-agent-production-sql-database-access|Agent production SQL database access]] · Launch
- 2026-02-12 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-02-12-support-claude-agent-sdk-style-structured-outputs-in-the-opencode-sdk|Support Claude agent SDK-style structured outputs in the OpenCode SDK]] · Launch
- 2026-02-09 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-09-agents-platform|Agents Platform]] · Launch
- 2026-02-09 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-09-agents-platform-7f0c0d|Agents Platform]] · Launch
- 2026-02-06 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-02-06-agent-inbox|Agent Inbox]] · Launch
- 2026-02-05 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2026-02-05-disconnect-shopify-stores|Disconnect Shopify stores]] · Launch
- 2026-02-05 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2026-02-05-new-agent-and-chat-ui|New agent and chat UI]] · Launch
- 2026-02-04 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-02-04-document-the-built-in-agents|Document the built-in agents]] · Launch
- 2026-02-02 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-02-python-sdk|Python SDK]] · Launch
- 2026-02-02 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-02-javascript-sdk|JavaScript SDK]] · Launch
- 2026-02-02 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-02-agents-platform|Agents Platform]] · Launch
- 2026-02-02 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-02-agents-platform-fb792c|Agents Platform]] · Launch

**2026-01**

- 2026-01-28 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-28-prevent-agents-md-from-being-loaded-multiple-times-during-parallel-tool-executio|Prevent AGENTS.md from being loaded multiple times during parallel tool execution]] · Launch
- 2026-01-26 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-26-python-sdk|Python SDK]] · Launch
- 2026-01-26 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-26-agents-platform|Agents Platform]] · Launch
- 2026-01-26 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-26-javascript-sdk|JavaScript SDK]] · Launch
- 2026-01-26 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-26-new-endpoints|New Endpoints]] · Launch
- 2026-01-26 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-26-agents-platform-89c04a|Agents Platform]] · Launch
- 2026-01-26 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-26-new-schemas|New Schemas]] · Launch
- 2026-01-23 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-01-23-rulessync-support-for-replit-md|RulesSync support for replit.md]] · Launch
- 2026-01-22 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-01-22-skills|Skills]] · Launch
- 2026-01-22 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-01-22-subagents|Subagents]] · Launch
- 2026-01-22 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-01-22-clarification-questions-from-the-agent|Clarification questions from the agent]] · Launch
- 2026-01-22 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-22-mark-subagent-sessions-as-agent-initiated-to-exclude-them-from-quota-limits|Mark subagent sessions as agent-initiated to exclude them from quota limits]] · Policy
- 2026-01-19 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-19-agents-platform|Agents Platform]] · Launch
- 2026-01-19 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-19-new-endpoints|New Endpoints]] · Launch
- 2026-01-19 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-19-agents-platform-97d485|Agents Platform]] · Launch
- 2026-01-16 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-01-16-push-your-local-conversation-to-a-cloud-agent-and-let-it-keep-running-while-you|Handoff to Cloud Agents]] · Launch
- 2026-01-16 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-01-16-use-plan-mode-to-design-your-approach-before-coding-cursor-will-ask-clarifying-q|Plan mode in CLI]] · Launch
- 2026-01-16 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2026-01-16-smarter-agent-capabilities|Smarter agent capabilities]] · Launch
- 2026-01-16 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-01-16-redesigned-tool-calls-ui-in-agent-chat|Redesigned tool calls UI in Agent chat]] · Launch
- 2026-01-15 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-15-ensure-agent-exists-before-processing-title-in-session-summary|Ensure agent exists before processing title in session summary]] · Launch
- 2026-01-14 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-14-do-not-allow-agent-to-ask-custom-less-questions|Do not allow agent to ask custom-less questions]] · Launch
- 2026-01-13 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-01-13-agent-skills|Agent Skills]] · Launch
- 2026-01-13 · <span class="tl-product tl-p24">**Windsurf**</span> · [[Changes/Windsurf/2026-01-13-new-features-and-improvements|New Features and Improvements]] · Launch
- 2026-01-12 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-12-agents-platform|Agents Platform]] · Launch
- 2026-01-12 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-12-agents-platform-dbe011|Agents Platform]] · Launch
- 2026-01-09 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2026-01-09-ai-command-in-shell|AI command in Shell]] · Launch
- 2026-01-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-05-agents-platform|Agents Platform]] · Launch
- 2026-01-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-05-agents-platform-bdcd71|Agents Platform]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 524 (ChatGPT 2 · Claude Code 119 · Cline 12 · Codex CLI 71 · Cursor 34 · Dify 15 · ElevenLabs 2 · Gemini CLI 26 · GitHub Copilot CLI 82 · Google Antigravity 25 · Lovable 3 · Ollama 13 · Open WebUI 7 · OpenClaw 22 · OpenCode 47 · OpenHands 26 · Runway 6 · Windsurf 3 · v0 9)</summary>

**2026-11**

- 2026-11-06 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-11-06-6-agent-mode-changes-in-rust-v0-167-0|6 Agent Mode changes in rust-v0.167.0]] · Digest
- 2026-11-06 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-11-06-34-agent-mode-changes-in-v1-0-106|34 Agent Mode changes in v1.0.106]] · Digest
- 2026-11-06 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-11-06-2-agent-mode-changes-in-v2-2-6|2 Agent Mode changes in v2.2.6]] · Digest
- 2026-11-05 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-11-05-4-agent-mode-changes-in-v2026-11-1|4 Agent Mode changes in v2026.11.1]] · Digest
- 2026-11-05 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-11-05-2-agent-mode-changes-in-v1-36-0|2 Agent Mode changes in v1.36.0]] · Digest
- 2026-11-04 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-11-04-14-agent-mode-changes-in-1-19-0|14 Agent Mode changes in 1.19.0]] · Digest
- 2026-11-03 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-11-03-remote-agents-are-starting-to-roll-out-to-google-ai-ultra-and-pro-subscribers-co|Remote agents are starting to roll out to Google AI Ultra and Pro subscribers]] · Change
- 2026-11-03 · <span class="tl-product tl-p17">**Ollama**</span> · [[Changes/Ollama/2026-11-03-xiaomi-mimo-s-mimo-v2-6-https-ollama-com-library-mimo-v2-6-a-9b-model-built-for|Xiaomi MiMo's mimo-v2.6((source link) a 9B model built…]] · Change
- 2026-11-03 · <span class="tl-product tl-p18">**Open WebUI**</span> · [[Changes/Open WebUI/2026-11-03-no-sub-agent-limits-by-default-the-sub-agent-limits-in-admin-settings-and-throug|🔓 No sub-agent limits by default. The sub-agent limits in Admin Settings…]] · Change
- 2026-11-03 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-11-03-9-agent-mode-changes-in-v2026-10-10|9 Agent Mode changes in v2026.10.10]] · Digest
- 2026-11-03 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-11-03-3-agent-mode-changes-in-v1-35-0|3 Agent Mode changes in v1.35.0]] · Digest
- 2026-11-02 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-11-02-8-agent-mode-changes-in-elevenlabs-updates-2026-11-02|8 Agent Mode changes in ElevenLabs updates — 2026-11-02]] · Digest

**2026-10**

- 2026-10-31 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-31-2-agent-mode-changes-in-v2-1-316|2 Agent Mode changes in v2.1.316]] · Digest
- 2026-10-30 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-30-3-agent-mode-changes-in-v2-1-314|3 Agent Mode changes in v2.1.314]] · Digest
- 2026-10-29 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-29-7-agent-mode-changes-in-rust-v0-166-0|7 Agent Mode changes in rust-v0.166.0]] · Digest
- 2026-10-29 · <span class="tl-product tl-p18">**Open WebUI**</span> · [[Changes/Open WebUI/2026-10-29-photos-for-sub-agents-models-can-now-hand-a-photo-attached-in-the-chat-to-a-sub|🤖 Photos for sub-agents. Models can now hand a photo attached in the chat…]] · Change
- 2026-10-29 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-29-2-agent-mode-changes-in-v2026-10-9|2 Agent Mode changes in v2026.10.9]] · Digest
- 2026-10-29 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-10-29-core-add-opt-in-scheduled-prompts-through-schedule-agent-tools-and-experimental|Core Add opt-in scheduled prompts through /schedule , agent tools…]] · Change
- 2026-10-27 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-27-2-agent-mode-changes-in-v2-1-312|2 Agent Mode changes in v2.1.312]] · Digest
- 2026-10-27 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-27-4-agent-mode-changes-in-rust-v0-165-0|4 Agent Mode changes in rust-v0.165.0]] · Digest
- 2026-10-27 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-27-3-agent-mode-changes-in-hub-v2-28-0-built-in-browser|3 Agent Mode changes in HUB v2.28.0 — Built-in browser…]] · Digest
- 2026-10-27 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-27-7-agent-mode-changes-in-v2026-10-8|7 Agent Mode changes in v2026.10.8]] · Digest
- 2026-10-27 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-10-27-2-agent-mode-changes-in-v2-2-0|2 Agent Mode changes in v2.2.0]] · Digest
- 2026-10-27 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-10-27-feat-verify-stand-in-for-digitalocean-so-managed-agents-can-be-verified-by-enyst|feat(verify): stand in for DigitalOcean so Managed Agents can be verified]] · Change
- 2026-10-26 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-26-2-agent-mode-changes-in-v2-1-311|2 Agent Mode changes in v2.1.311]] · Digest
- 2026-10-26 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-26-9-agent-mode-changes-in-elevenlabs-updates-2026-10-26|9 Agent Mode changes in ElevenLabs updates — 2026-10-26]] · Digest
- 2026-10-26 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-26-added-drag-and-drop-support-for-files-or-screenshots-directly-onto-the-agent-pan|Added drag-and-drop support for files or screenshots directly onto the Agent panel]] · Change
- 2026-10-26 · <span class="tl-product tl-p24">**Windsurf**</span> · [[Changes/Windsurf/2026-10-26-the-status-bar-no-longer-disappears-after-you-switch-from-agent-mode-to-ide-mode|The status bar no longer disappears after you switch from Agent mode to IDE mode]] · Change
- 2026-10-24 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-24-8-agent-mode-changes-in-v2026-10-7|8 Agent Mode changes in v2026.10.7]] · Digest
- 2026-10-23 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-23-2-agent-mode-changes-in-v2-1-310|2 Agent Mode changes in v2.1.310]] · Digest
- 2026-10-23 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-23-13-agent-mode-changes-in-rust-v0-164-0|13 Agent Mode changes in rust-v0.164.0]] · Digest
- 2026-10-23 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-10-23-32-agent-mode-changes-in-1-18-0|32 Agent Mode changes in 1.18.0]] · Digest
- 2026-10-23 · <span class="tl-product tl-p24">**Windsurf**</span> · [[Changes/Windsurf/2026-10-23-3-agent-mode-changes-in-v3-11-212|3 Agent Mode changes in v3.11.212]] · Digest
- 2026-10-22 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-22-changed-the-claude-api-skill-to-build-managed-agents-subagent-teams-on-multiagen|Changed the /claude-api skill to build Managed Agents subagent teams…]] · Change
- 2026-10-22 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-22-3-agent-mode-changes-in-v2026-10-6|3 Agent Mode changes in v2026.10.6]] · Digest
- 2026-10-22 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-10-22-chore-bump-agent-server-to-1-57-0-by-all-hands-bot-in-https-github-com-openhands|chore: bump agent-server to 1.57.0]] · Change
- 2026-10-21 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-21-improved-fork-subagents-launched-together-each-is-now-told-which-launch-is-its-o|Improved fork subagents launched together]] · Change
- 2026-10-20 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-10-20-the-agent-sdk-is-generally-available-today-read-the-docs-and-get-started|The Agent SDK is generally available today]] · Change
- 2026-10-20 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-10-20-the-agent-sdk-is-available-today-it-allows-you-to-define-an-agent-as-a-folder-of|The Agent SDK is available today]] · Change
- 2026-10-20 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-10-20-5-agent-mode-changes-in-v1-29-0|5 Agent Mode changes in v1.29.0]] · Digest
- 2026-10-19 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-19-2-agent-mode-changes-in-v2-1-304|2 Agent Mode changes in v2.1.304]] · Digest
- 2026-10-19 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-19-2-agent-mode-changes-in-v1-0-100|2 Agent Mode changes in v1.0.100]] · Digest
- 2026-10-19 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-10-19-3-agent-mode-changes-in-v1-28-0|3 Agent Mode changes in v1.28.0]] · Digest
- 2026-10-19 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-10-19-chore-bump-agent-server-to-1-56-0-by-all-hands-bot-in-https-github-com-openhands|chore: bump agent-server to 1.56.0]] · Change
- 2026-10-18 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-18-2-agent-mode-changes-in-v2026-10-5|2 Agent Mode changes in v2026.10.5]] · Digest
- 2026-10-16 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-10-16-multiple-agents-that-can-work-on-different-parts-of-a-task-in-parallel-you-can-f|Multiple agents that can work on different parts of a task in parallel]] · Change
- 2026-10-16 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-16-6-agent-mode-changes-in-v2-1-302|6 Agent Mode changes in v2.1.302]] · Digest
- 2026-10-16 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-16-2-agent-mode-changes-in-v2026-10-4|2 Agent Mode changes in v2026.10.4]] · Digest
- 2026-10-15 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-15-14-agent-mode-changes-in-rust-v0-163-0|14 Agent Mode changes in rust-v0.163.0]] · Digest
- 2026-10-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-14-5-agent-mode-changes-in-v2-1-299|5 Agent Mode changes in v2.1.299]] · Digest
- 2026-10-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-14-3-agent-mode-changes-in-v2-1-300|3 Agent Mode changes in v2.1.300]] · Digest
- 2026-10-14 · <span class="tl-product tl-p17">**Ollama**</span> · [[Changes/Ollama/2026-10-14-a-compact-sibling-nemotron-3-5-bolt-https-ollama-com-library-nemotron-3-5-bolt-d|A compact sibling, Nemotron 3.5…]] · Change
- 2026-10-13 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-13-3-agent-mode-changes-in-v1-0-97|3 Agent Mode changes in v1.0.97]] · Digest
- 2026-10-12 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-12-subagent-launches-now-show-as-a-one-line-row-with-a-live-status-icon-like-other|Subagent launches now show as a one-line row with a live status icon, like other…]] · Change
- 2026-10-12 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-12-5-agent-mode-changes-in-v2026-10-2|5 Agent Mode changes in v2026.10.2]] · Digest
- 2026-10-12 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-10-12-4-agent-mode-changes-in-v1-27-0|4 Agent Mode changes in v1.27.0]] · Digest
- 2026-10-10 · <span class="tl-product tl-p18">**Open WebUI**</span> · [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]] · Digest
- 2026-10-10 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-10-27-agent-mode-changes-in-v2026-10-1|27 Agent Mode changes in v2026.10.1]] · Digest
- 2026-10-09 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-09-3-agent-mode-changes-in-v2-1-296|3 Agent Mode changes in v2.1.296]] · Digest
- 2026-10-08 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-08-4-agent-mode-changes-in-v2-1-295|4 Agent Mode changes in v2.1.295]] · Digest
- 2026-10-08 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-08-14-agent-mode-changes-in-rust-v0-162-0|14 Agent Mode changes in rust-v0.162.0]] · Digest
- 2026-10-08 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-08-4-agent-mode-changes-in-v2026-9-9|4 Agent Mode changes in v2026.9.9]] · Digest
- 2026-10-07 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-07-2-agent-mode-changes-in-v2-1-293|2 Agent Mode changes in v2.1.293]] · Digest
- 2026-10-07 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-07-9-agent-mode-changes-in-rust-v0-161-0|9 Agent Mode changes in rust-v0.161.0]] · Digest
- 2026-10-07 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-07-clicking-a-truncated-compact-shell-command-expands-it|Clicking a truncated compact shell command expands it]] · Change
- 2026-10-07 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-07-2-agent-mode-changes-in-hub-v2-21-1-advanced-search|2 Agent Mode changes in HUB v2.21.1 — Advanced Search…]] · Digest
- 2026-10-06 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-06-3-agent-mode-changes-in-v2-1-292|3 Agent Mode changes in v2.1.292]] · Digest
- 2026-10-06 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-10-06-4-agent-mode-changes-in-v1-25-0|4 Agent Mode changes in v1.25.0]] · Digest
- 2026-10-05 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-05-4-agent-mode-changes-in-v2-1-290|4 Agent Mode changes in v2.1.290]] · Digest
- 2026-10-05 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-05-5-agent-mode-changes-in-v1-0-92|5 Agent Mode changes in v1.0.92]] · Digest
- 2026-10-03 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-03-4-agent-mode-changes-in-v2026-9-8|4 Agent Mode changes in v2026.9.8]] · Digest
- 2026-10-02 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-02-4-agent-mode-changes-in-v2-1-288|4 Agent Mode changes in v2.1.288]] · Digest
- 2026-10-01 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-01-4-agent-mode-changes-in-v2-1-287|4 Agent Mode changes in v2.1.287]] · Digest
- 2026-10-01 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-01-6-agent-mode-changes-in-rust-v0-160-0|6 Agent Mode changes in rust-v0.160.0]] · Digest

**2026-09**

- 2026-09-30 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-30-6-agent-mode-changes-in-v2-1-286|6 Agent Mode changes in v2.1.286]] · Digest
- 2026-09-30 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-30-auto-approval-now-takes-into-account-messages-you-type-while-the-agent-is-workin|Auto-approval now takes into account messages you type while the agent is working…]] · Change
- 2026-09-30 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-30-33-agent-mode-changes-in-v2026-9-7|33 Agent Mode changes in v2026.9.7]] · Digest
- 2026-09-29 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-29-2-agent-mode-changes-in-v2-1-285|2 Agent Mode changes in v2.1.285]] · Digest
- 2026-09-29 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-29-48190-bound-agent-message-board-sse-frames-before-parsing-jif-oai|♯48190 Bound agent message board SSE frames before parsing @jif-oai]] · Change
- 2026-09-28 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-28-added-a-yes-but-ask-again-next-time-answer-to-auto-mode-s-prompt-before-a-read-o|Added a "Yes, but ask again next time" answer to auto mode's prompt before a read…]] · Change
- 2026-09-28 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-28-11-agent-mode-changes-in-rust-v0-158-0|11 Agent Mode changes in rust-v0.158.0]] · Digest
- 2026-09-28 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-28-queue-exit-commands-while-an-agent-response-is-still-running|Queue exit commands while an agent response is still running]] · Change
- 2026-09-28 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-28-2-agent-mode-changes-in-hub-v2-18-1-manage-install-plugins|2 Agent Mode changes in HUB v2.18.1 — Manage & Install plugins…]] · Digest
- 2026-09-25 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-25-improved-startup-claude-p-and-claude-code-remote-no-longer-load-the-interactive|Improved startup: claude -p and Claude Code Remote no longer load the interactive…]] · Change
- 2026-09-25 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-25-13-agent-mode-changes-in-rust-v0-157-0|13 Agent Mode changes in rust-v0.157.0]] · Digest
- 2026-09-25 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-09-25-docs-correct-outdated-cloud-proxy-rule-2-in-agents-md-by-juanmichelini-in-https|docs: correct outdated cloud-proxy Rule 2 in AGENTS.md]] · Change
- 2026-09-24 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-24-2-agent-mode-changes-in-v2-1-282|2 Agent Mode changes in v2.1.282]] · Digest
- 2026-09-23 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-23-10-agent-mode-changes-in-v2-1-281|10 Agent Mode changes in v2.1.281]] · Digest
- 2026-09-23 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-09-23-when-rollouts-detects-a-regression-it-names-the-change-it-suspects-and-notifies|When Rollouts detects a regression, it names the change it suspects and notifies…]] · Change
- 2026-09-23 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-23-41-agent-mode-changes-in-v2026-9-6|41 Agent Mode changes in v2026.9.6]] · Digest
- 2026-09-22 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-22-2-agent-mode-changes-in-v2-1-280|2 Agent Mode changes in v2.1.280]] · Digest
- 2026-09-22 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-09-22-2-agent-mode-changes-in-v4-1-20|2 Agent Mode changes in v4.1.20]] · Digest
- 2026-09-22 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-22-34-agent-mode-changes-in-rust-v0-156-0|34 Agent Mode changes in rust-v0.156.0]] · Digest
- 2026-09-22 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-22-2-agent-mode-changes-in-v1-0-88|2 Agent Mode changes in v1.0.88]] · Digest
- 2026-09-22 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-22-2-agent-mode-changes-in-hub-v2-16-0-windows-subsystem|2 Agent Mode changes in HUB v2.16.0 — Windows Subsystem…]] · Digest
- 2026-09-22 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-22-4-agent-mode-changes-in-hub-v2-17-0-plan-before-you-build|4 Agent Mode changes in HUB v2.17.0 — Plan before you build]] · Digest
- 2026-09-22 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-09-22-docs-refresh-agents-md-guidance-by-all-hands-bot-in-https-github-com-openhands-o|docs: refresh AGENTS.md guidance]] · Change
- 2026-09-21 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-21-show-live-elapsed-time-for-execution-subagents-in-timeline-entries|Show live elapsed time for execution subagents in timeline entries]] · Change
- 2026-09-19 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-19-added-an-auto-mode-server-row-to-status-showing-whether-this-session-s-auto-mode|Added an Auto mode server row to /status showing whether this session's auto…]] · Change
- 2026-09-19 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-19-72-agent-mode-changes-in-v2026-9-5|72 Agent Mode changes in v2026.9.5]] · Digest
- 2026-09-18 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-18-4-agent-mode-changes-in-v2-1-277|4 Agent Mode changes in v2.1.277]] · Digest
- 2026-09-18 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-18-3-agent-mode-changes-in-hub-v2-15-0-custom-agent-controls|3 Agent Mode changes in HUB v2.15.0 — Custom agent controls…]] · Digest
- 2026-09-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-17-vscode-improved-the-agent-map-the-pill-counts-running-agents-and-turns-red-after|VSCode Improved the agent map]] · Change
- 2026-09-17 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-09-17-task-history-no-longer-goes-blank-when-a-task-spawns-many-subagents-subagent-row|Task history no longer goes blank when a task spawns many subagents]] · Change
- 2026-09-17 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-17-9-agent-mode-changes-in-rust-v0-155-0|9 Agent Mode changes in rust-v0.155.0]] · Digest
- 2026-09-17 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-09-17-2-agent-mode-changes-in-v1-20-0|2 Agent Mode changes in v1.20.0]] · Digest
- 2026-09-16 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-16-2-agent-mode-changes-in-v1-0-85|2 Agent Mode changes in v1.0.85]] · Digest
- 2026-09-16 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-09-16-2-agent-mode-changes-in-v1-19-0|2 Agent Mode changes in v1.19.0]] · Digest
- 2026-09-15 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-15-changed-auto-mode-on-bedrock-vertex-and-foundry-to-use-the-local-classifier-by-d|Changed auto mode on Bedrock, Vertex and Foundry to use the local classifier…]] · Change
- 2026-09-15 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-15-the-agent-s-temporary-scratch-files-are-no-longer-watched-synced-or-shown-in-the|The agent's temporary scratch files are no longer watched, synced, or shown…]] · Change
- 2026-09-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-14-7-agent-mode-changes-in-v2-1-271|7 Agent Mode changes in v2.1.271]] · Digest
- 2026-09-11 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-11-2-agent-mode-changes-in-v2-1-269|2 Agent Mode changes in v2.1.269]] · Digest
- 2026-09-11 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-11-25-agent-mode-changes-in-v2026-9-4|25 Agent Mode changes in v2026.9.4]] · Digest
- 2026-09-10 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-10-improved-auto-mode-denials-the-message-claude-receives-now-names-the-rule-that-b|Improved auto mode denials]] · Change
- 2026-09-10 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-09-10-42-agent-mode-changes-in-1-17-1|42 Agent Mode changes in 1.17.1]] · Digest
- 2026-09-10 · <span class="tl-product tl-p23">**Runway**</span> · [[Changes/Runway/2026-09-10-agent-can-now-create-and-edit-brand-kits-for-you-right-in-the-conversation-group|Agent Brand Kits]] · Change
- 2026-09-09 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-09-6-agent-mode-changes-in-rust-v0-154-0|6 Agent Mode changes in rust-v0.154.0]] · Digest
- 2026-09-09 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-09-2-agent-mode-changes-in-hub-v2-13-0-introducing-new-documents|2 Agent Mode changes in HUB v2.13.0 — Introducing new Documents…]] · Digest
- 2026-09-08 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-08-improved-workflows-agent-detail-tool-calls-are-marked-running-failed-or-done-the|Improved /workflows agent detail]] · Change
- 2026-09-08 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-08-16-agent-mode-changes-in-v2026-9-3|16 Agent Mode changes in v2026.9.3]] · Digest
- 2026-09-05 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-05-34-agent-mode-changes-in-v2026-9-2|34 Agent Mode changes in v2026.9.2]] · Digest
- 2026-09-04 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-04-2-agent-mode-changes-in-v2-1-261|2 Agent Mode changes in v2.1.261]] · Digest
- 2026-09-04 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-04-stopping-a-timed-out-shell-command-now-lets-queued-messages-run-and-sessions-ret|Stopping a timed-out shell command now lets queued messages run and sessions return…]] · Change
- 2026-09-03 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-03-2-agent-mode-changes-in-v2-1-260|2 Agent Mode changes in v2.1.260]] · Digest
- 2026-09-03 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-03-4-agent-mode-changes-in-rust-v0-153-0|4 Agent Mode changes in rust-v0.153.0]] · Digest
- 2026-09-03 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-03-14-agent-mode-changes-in-v2026-9-1|14 Agent Mode changes in v2026.9.1]] · Digest
- 2026-09-02 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-02-2-agent-mode-changes-in-v2-1-259|2 Agent Mode changes in v2.1.259]] · Digest
- 2026-09-02 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-09-02-aborting-a-task-now-also-cancels-the-delegated-subagents-and-teammates-it-spawne|Aborting a task now also cancels the delegated subagents and teammates it spawned…]] · Change
- 2026-09-02 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-09-02-cursor-supports-self-hosted-machines-which-let-you-keep-tool-execution-entirely|Cursor supports self-hosted machines, which let you keep tool execution entirely…]] · Change
- 2026-09-02 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-02-introduced-the-boost-slash-command-to-enhance-thinking-effort-by-using-a-multi-a|Introduced the /boost slash command to enhance thinking effort by using…]] · Change
- 2026-09-01 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-01-5-agent-mode-changes-in-v2-1-257|5 Agent Mode changes in v2.1.257]] · Digest
- 2026-09-01 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-01-4-agent-mode-changes-in-rust-v0-152-0|4 Agent Mode changes in rust-v0.152.0]] · Digest
- 2026-09-01 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-01-11-agent-mode-changes-in-v2026-8-2|11 Agent Mode changes in v2026.8.2]] · Digest

**2026-08**

- 2026-08-29 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-29-2-agent-mode-changes-in-rust-v0-151-0|2 Agent Mode changes in rust-v0.151.0]] · Digest
- 2026-08-28 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-28-4-agent-mode-changes-in-v2-1-251|4 Agent Mode changes in v2.1.251]] · Digest
- 2026-08-27 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-27-3-agent-mode-changes-in-v2-1-248|3 Agent Mode changes in v2.1.248]] · Digest
- 2026-08-27 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-08-27-cloud-agents-no-longer-require-a-connected-github-or-other-third-party-scm-provi|Cloud Agents no longer require a connected GitHub or other third-party SCM provider…]] · Change
- 2026-08-27 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-27-8-agent-mode-changes-in-v1-0-81|8 Agent Mode changes in v1.0.81]] · Digest
- 2026-08-27 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-08-27-4-agent-mode-changes-in-v1-16-0|4 Agent Mode changes in v1.16.0]] · Digest
- 2026-08-26 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-26-14-agent-mode-changes-in-rust-v0-150-0|14 Agent Mode changes in rust-v0.150.0]] · Digest
- 2026-08-26 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-08-26-3-agent-mode-changes-in-hub-v2-11-0-generative-ui-and-ui|3 Agent Mode changes in HUB v2.11.0 — Generative UI and UI…]] · Digest
- 2026-08-25 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-25-improved-subagent-results-a-subagent-that-stops-at-its-maxturns-limit-now-return|Improved subagent results]] · Change
- 2026-08-25 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-08-25-53-agent-mode-changes-in-1-17-0|53 Agent Mode changes in 1.17.0]] · Digest
- 2026-08-25 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-08-25-8-agent-mode-changes-in-v0-57-0|8 Agent Mode changes in v0.57.0]] · Digest
- 2026-08-25 · <span class="tl-product tl-p18">**Open WebUI**</span> · [[Changes/Open WebUI/2026-08-25-files-for-delegated-tasks-a-task-handed-to-a-sub-agent-can-now-carry-the-attachm|🤝 Files for delegated tasks. A task handed to a sub-agent can now carry…]] · Change
- 2026-08-22 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-08-22-carry-session-and-client-identity-into-langfuse-traces-for-hub-backed-and-delega|Carry session and client identity into Langfuse traces for Hub-backed…]] · Change
- 2026-08-21 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-21-2-agent-mode-changes-in-v2-1-239|2 Agent Mode changes in v2.1.239]] · Digest
- 2026-08-21 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-08-21-core-surface-resumable-subagent-failures-instead-of-returning-an-empty-result|Core Surface resumable subagent failures instead of returning an empty result]] · Change
- 2026-08-21 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-08-21-feat-add-llm-provider-connections-ui-local-agent-server-by-juanmichelini-in-http|feat: add LLM provider-connections UI (local agent-server)]] · Change
- 2026-08-20 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-20-12-agent-mode-changes-in-rust-v0-149-0|12 Agent Mode changes in rust-v0.149.0]] · Digest
- 2026-08-20 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-08-20-3-agent-mode-changes-in-hub-v2-9-1-remote-control-faster|3 Agent Mode changes in HUB v2.9.1 — Remote Control, faster…]] · Digest
- 2026-08-19 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-19-4-agent-mode-changes-in-v2-1-236|4 Agent Mode changes in v2.1.236]] · Digest
- 2026-08-19 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-08-19-we-re-continuing-to-improve-cloud-agents-and-the-cursor-harness-so-always-on-age-1d1294|We're continuing to improve cloud agents and the Cursor harness so always-on agents…]] · Change
- 2026-08-18 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-18-12-agent-mode-changes-in-rust-v0-148-0|12 Agent Mode changes in rust-v0.148.0]] · Digest
- 2026-08-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-17-removed-the-redundant-allowed-by-auto-mode-classifier-line-that-auto-mode-showed|Removed the redundant "Allowed by auto mode classifier" line that auto mode showed…]] · Change
- 2026-08-17 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-08-17-docs-agents-add-a-repository-map-clarifying-what-belongs-where-by-smolpaws-in-ht|docs(agents): add a repository map clarifying what belongs where]] · Change
- 2026-08-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-14-improved-claude-self-hosted-runner-session-start-time-the-session-branch-is-now|Improved claude self-hosted-runner session start time]] · Change
- 2026-08-14 · <span class="tl-product tl-p17">**Ollama**</span> · [[Changes/Ollama/2026-08-14-2-agent-mode-changes-in-v0-32-11|2 Agent Mode changes in v0.32.11]] · Digest
- 2026-08-14 · <span class="tl-product tl-p25">**v0**</span> · [[Changes/v0/2026-08-14-the-paused-agent-timeout-card-shows-resuming-and-resumed-states|The paused-agent timeout card shows Resuming and Resumed states]] · Change
- 2026-08-13 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-13-4-agent-mode-changes-in-v2-1-232|4 Agent Mode changes in v2.1.232]] · Digest
- 2026-08-13 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-08-13-2-agent-mode-changes-in-08-13-26|2 Agent Mode changes in 08.13.26]] · Digest
- 2026-08-13 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-08-13-agents-do-their-best-work-when-they-start-in-a-ready-environment-repos-cloned-de-6161c7|Agents do their best work when they start in a ready environment]] · Change
- 2026-08-13 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-08-13-chore-enforce-typed-openhands-typescript-client-for-agent-server-api-calls-no-ad|chore: enforce typed @openhands/typescript-client for agent-server API calls…]] · Change
- 2026-08-12 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-12-improved-workflow-fan-outs-to-stagger-same-prefix-sibling-agents-so-subsequent-a|Improved workflow fan-outs to stagger same-prefix sibling agents so subsequent…]] · Change
- 2026-08-12 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-08-12-reduced-typing-lag-while-the-agent-streams-responses|Reduced typing lag while the agent streams responses]] · Change
- 2026-08-11 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-11-removed-the-outdated-note-about-auto-mode-sessions-costing-slightly-more-from-th|Removed the outdated note about auto mode sessions costing slightly more…]] · Change
- 2026-08-11 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-08-11-2-agent-mode-changes-in-v0-55-1|2 Agent Mode changes in v0.55.1]] · Digest
- 2026-08-11 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-08-11-ensured-that-local-web-servers-started-by-the-agent-are-reachable-from-your-host|Ensured that local web servers started by the agent are reachable from your host machine]] · Change
- 2026-08-11 · <span class="tl-product tl-p17">**Ollama**</span> · [[Changes/Ollama/2026-08-11-nvidia-nemotron-3-5-lightning-https-ollama-com-library-nemotron-3-5-lightning-is|NVIDIA Nemotron 3.5 Lightning((source link)]] · Change
- 2026-08-11 · <span class="tl-product tl-p23">**Runway**</span> · [[Changes/Runway/2026-08-11-agent-sessions-now-live-inside-projects-so-you-can-start-a-session-directly-from|Projects + Brand Kits in Agent]] · Change
- 2026-08-10 · <span class="tl-product tl-p17">**Ollama**</span> · [[Changes/Ollama/2026-08-10-2-agent-mode-changes-in-v0-32-7|2 Agent Mode changes in v0.32.7]] · Digest
- 2026-08-10 · <span class="tl-product tl-p17">**Ollama**</span> · [[Changes/Ollama/2026-08-10-for-a-lighter-weight-coding-agent-try-pi-https-pi-dev|For a lighter-weight coding agent, try Pi((source link)]] · Change
- 2026-08-07 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-07-removed-the-200-subagent-per-session-spawn-cap-long-running-sessions-no-longer-r|Removed the 200-subagent-per-session spawn cap]] · Change
- 2026-08-07 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-07-17-agent-mode-changes-in-rust-v0-147-0|17 Agent Mode changes in rust-v0.147.0]] · Digest
- 2026-08-07 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-08-07-2-agent-mode-changes-in-hub-v2-6-0-faster-long-conversations|2 Agent Mode changes in HUB v2.6.0 — Faster long conversations…]] · Digest
- 2026-08-07 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-08-07-feat-add-a-typed-agent-action-for-launching-local-or-cloud-child-conversations-b|feat: add a typed agent action for launching local or Cloud child conversations]] · Change
- 2026-08-06 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-06-2-agent-mode-changes-in-v2-1-223|2 Agent Mode changes in v2.1.223]] · Digest
- 2026-08-06 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-08-06-feat-pr-generator-agent-implement-antigravity-agent-runner-and-prompt-templates|feat(pr-generator-agent): implement Antigravity agent runner and prompt templates …]] · Change
- 2026-08-03 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-03-a-run-whose-prompt-is-piped-over-stdin-now-treats-its-sessionend-hook-the-same-w|A run whose prompt is piped over stdin now treats its sessionEnd hook the same way…]] · Change
- 2026-08-03 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-08-03-3-agent-mode-changes-in-v1-9-0|3 Agent Mode changes in v1.9.0]] · Digest

**2026-07**

- 2026-07-31 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-07-31-reduced-typing-lag-while-the-agent-streams-responses|Reduced typing lag while the agent streams responses]] · Change
- 2026-07-30 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-30-2-agent-mode-changes-in-v1-0-76|2 Agent Mode changes in v1.0.76]] · Digest
- 2026-07-30 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-07-30-docs-refresh-agents-md-guidance-by-all-hands-bot-in-https-github-com-openhands-o|docs: refresh AGENTS.md guidance]] · Change
- 2026-07-29 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-29-11-agent-mode-changes-in-rust-v0-146-0|11 Agent Mode changes in rust-v0.146.0]] · Digest
- 2026-07-29 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-07-29-feat-always-show-the-llm-selector-move-agent-profile-switching-to-the-tools-menu|feat: always show the LLM selector; move agent-profile switching to the tools menu]] · Change
- 2026-07-28 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-07-28-always-on-cloud-agents-that-build-test-and-ship-code-while-you-keep-working-725c7c|Always-on cloud agents that build, test, and ship code while you keep working]] · Change
- 2026-07-28 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-07-28-24-agent-mode-changes-in-1-16-1|24 Agent Mode changes in 1.16.1]] · Digest
- 2026-07-28 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-07-28-2-agent-mode-changes-in-hub-v2-4-3-preview-tabs-mcp|2 Agent Mode changes in HUB v2.4.3 — Preview tabs, MCP…]] · Digest
- 2026-07-28 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-07-28-this-release-migration-was-performed-by-an-ai-agent-openhands-on-behalf-of-the-u|This release migration was performed by an AI agent (OpenHands) on behalf of the user]] · Change
- 2026-07-27 · <span class="tl-product tl-p18">**Open WebUI**</span> · [[Changes/Open WebUI/2026-07-27-sub-agents-administrators-can-now-enable-sub-agents-which-let-a-model-hand-parts|🤖 Sub-agents. Administrators can now enable sub-agents, which let a model hand…]] · Change
- 2026-07-24 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-24-4-agent-mode-changes-in-v2-1-219|4 Agent Mode changes in v2.1.219]] · Digest
- 2026-07-24 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-07-24-desktop-keep-the-prompt-input-agent-toggle-in-sync|Desktop Keep the prompt input agent toggle in sync]] · Change
- 2026-07-23 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-23-3-agent-mode-changes-in-v1-0-74|3 Agent Mode changes in v1.0.74]] · Digest
- 2026-07-23 · <span class="tl-product tl-p23">**Runway**</span> · [[Changes/Runway/2026-07-23-agent-can-now-build-and-run-entire-workflows-for-you-just-describe-what-you-want|Agent Workflows]] · Change
- 2026-07-22 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-22-changed-plan-mode-with-auto-to-no-longer-prompt-for-bash-commands-the-static-ana|Changed plan mode with auto to no longer prompt for Bash commands the static…]] · Change
- 2026-07-22 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-07-22-auto-mode-is-now-powered-by-cursor-router|Auto mode is now powered by Cursor Router]] · Change
- 2026-07-21 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-21-2-agent-mode-changes-in-v2-1-217|2 Agent Mode changes in v2.1.217]] · Digest
- 2026-07-21 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-21-20-agent-mode-changes-in-rust-v0-145-0|20 Agent Mode changes in rust-v0.145.0]] · Digest
- 2026-07-21 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-21-2-agent-mode-changes-in-v1-0-73|2 Agent Mode changes in v1.0.73]] · Digest
- 2026-07-21 · <span class="tl-product tl-p25">**v0**</span> · [[Changes/v0/2026-07-21-agent-auto-pushes-retry-after-rebasing-when-a-push-is-rejected-as-non-fast-forwa|Agent auto-pushes retry after rebasing when a push is rejected as non-fast-forward…]] · Change
- 2026-07-20 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-20-3-agent-mode-changes-in-v1-0-72|3 Agent Mode changes in v1.0.72]] · Digest
- 2026-07-18 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-18-added-reasoning-effort-to-the-subagentstatusline-payload-so-custom-agent-rows-ca|Added reasoning effort to the subagentStatusLine payload, so custom agent rows can…]] · Change
- 2026-07-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-17-7-agent-mode-changes-in-v2-1-212|7 Agent Mode changes in v2.1.212]] · Digest
- 2026-07-17 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-07-17-64-agent-mode-changes-in-1-16-0|64 Agent Mode changes in 1.16.0]] · Digest
- 2026-07-16 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-16-8-agent-mode-changes-in-v1-0-71|8 Agent Mode changes in v1.0.71]] · Digest
- 2026-07-16 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-07-16-desktop-fixed-custom-agent-selector-visibility-when-custom-agents-are-available|Desktop Fixed custom agent selector visibility when custom agents are available]] · Change
- 2026-07-15 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-15-2-agent-mode-changes-in-v2-1-211|2 Agent Mode changes in v2.1.211]] · Digest
- 2026-07-15 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-07-15-core-stopped-subagents-from-launching-nested-subagents-by-default-with-a-configu|Core Stopped subagents from launching nested subagents by default…]] · Change
- 2026-07-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-14-4-agent-mode-changes-in-v2-1-208|4 Agent Mode changes in v2.1.208]] · Digest
- 2026-07-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-14-3-agent-mode-changes-in-v2-1-210|3 Agent Mode changes in v2.1.210]] · Digest
- 2026-07-13 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-13-2-agent-mode-changes-in-rust-v0-144-2|2 Agent Mode changes in rust-v0.144.2]] · Digest
- 2026-07-13 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-07-13-2-agent-mode-changes-in-hub-v2-3-0-queued-messages-plain|2 Agent Mode changes in HUB v2.3.0 — Queued messages, plain…]] · Digest
- 2026-07-13 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-07-13-132-agent-mode-changes-in-v2026-7-1|132 Agent Mode changes in v2026.7.1]] · Digest
- 2026-07-11 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-11-2-agent-mode-changes-in-v2-1-207|2 Agent Mode changes in v2.1.207]] · Digest
- 2026-07-11 · <span class="tl-product tl-p17">**Ollama**</span> · [[Changes/Ollama/2026-07-11-2-agent-mode-changes-in-v0-32-0|2 Agent Mode changes in v0.32.0]] · Digest
- 2026-07-10 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-10-2-agent-mode-changes-in-v2-1-206|2 Agent Mode changes in v2.1.206]] · Digest
- 2026-07-10 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-07-10-this-release-makes-it-easier-to-stay-in-flow-with-side-chats-that-run-alongside|Cursor makes it easier to stay in flow with side chats that run alongside your main…]] · Change
- 2026-07-10 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-10-3-agent-mode-changes-in-v1-0-70|3 Agent Mode changes in v1.0.70]] · Digest
- 2026-07-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-07-09-chatgpt-work-is-an-agent-for-longer-more-involved-tasks-it-can-research-and-anal|ChatGPT Work is an agent for longer, more involved tasks]] · Change
- 2026-07-09 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-09-4-agent-mode-changes-in-rust-v0-144-0|4 Agent Mode changes in rust-v0.144.0]] · Digest
- 2026-07-09 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-07-09-desktop-updated-sub-agent-task-rows-to-match-the-v2-session-design-more-closely|Desktop Updated sub-agent task rows to match the v2 session design more closely]] · Change
- 2026-07-09 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-07-09-feat-enterprise-agent-profiles-on-the-cloud-saas-backend-15044-by-simonrosenberg|feat(enterprise): Agent Profiles on the cloud/SaaS backend (♯15044)]] · Change
- 2026-07-08 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-08-3-agent-mode-changes-in-v2-1-205|3 Agent Mode changes in v2.1.205]] · Digest
- 2026-07-08 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-08-10-agent-mode-changes-in-rust-v0-143-0|10 Agent Mode changes in rust-v0.143.0]] · Digest
- 2026-07-08 · <span class="tl-product tl-p23">**Runway**</span> · [[Changes/Runway/2026-07-08-agent-can-now-build-custom-skills-for-you-ask-it-to-create-one-from-scratch-or-t|Custom Agent Skills]] · Change
- 2026-07-07 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-07-2-agent-mode-changes-in-v2-1-203|2 Agent Mode changes in v2.1.203]] · Digest
- 2026-07-07 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-07-double-press-esc-now-interrupts-the-running-main-turn-flushing-queued-messages-o|Double-press Esc now interrupts the running main turn (flushing queued messages)…]] · Change
- 2026-07-06 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-06-3-agent-mode-changes-in-v2-1-202|3 Agent Mode changes in v2.1.202]] · Digest
- 2026-07-06 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-07-06-9-agent-mode-changes-in-1-9-0|9 Agent Mode changes in 1.9.0]] · Digest
- 2026-07-06 · <span class="tl-product tl-p23">**Runway**</span> · [[Changes/Runway/2026-07-06-agent-can-now-read-pdfs-you-upload-pulling-their-content-directly-into-generatio|PDF Input for Agent]] · Change
- 2026-07-01 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-01-5-agent-mode-changes-in-v2-1-198|5 Agent Mode changes in v2.1.198]] · Digest
- 2026-07-01 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-01-3-agent-mode-changes-in-v1-0-68|3 Agent Mode changes in v1.0.68]] · Digest

**2026-06**

- 2026-06-30 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-30-2-agent-mode-changes-in-v1-0-67|2 Agent Mode changes in v1.0.67]] · Digest
- 2026-06-30 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-30-8-agent-mode-changes-in-v1-0-66|8 Agent Mode changes in v1.0.66]] · Digest
- 2026-06-30 · <span class="tl-product tl-p19">**OpenClaw**</span> · [[Changes/OpenClaw/2026-06-30-32-agent-mode-changes-in-v2026-6-11|32 Agent Mode changes in v2026.6.11]] · Digest
- 2026-06-29 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-29-2-agent-mode-changes-in-v2-1-196|2 Agent Mode changes in v2.1.196]] · Digest
- 2026-06-29 · <span class="tl-product tl-p18">**Open WebUI**</span> · [[Changes/Open WebUI/2026-06-29-client-user-agent-forwarded-to-model-backends-the-browser-s-user-agent-is-now-pa|🪪 Client User-Agent forwarded to model backends. The browser's User-Agent is now…]] · Change
- 2026-06-26 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-26-improved-claude-agents-completed-list-to-fill-available-vertical-space-on-short|Improved claude agents completed list to fill available vertical space]] · Change
- 2026-06-26 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-06-26-temporarily-disable-subagents-in-the-vs-code-extension-while-the-sdk-backed-expe|Temporarily disable subagents in the VS Code extension while the SDK-backed…]] · Change
- 2026-06-26 · <span class="tl-product tl-p25">**v0**</span> · [[Changes/v0/2026-06-26-2-agent-mode-changes-in-platform-api-v2-mcp-chat-tools|2 Agent Mode changes in Platform API v2, MCP chat tools…]] · Digest
- 2026-06-25 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-25-3-agent-mode-changes-in-v2-1-193|3 Agent Mode changes in v2.1.193]] · Digest
- 2026-06-25 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-06-25-38-agent-mode-changes-in-1-15-0|38 Agent Mode changes in 1.15.0]] · Digest
- 2026-06-25 · <span class="tl-product tl-p23">**Runway**</span> · [[Changes/Runway/2026-06-25-make-marketing-that-drives-revenue-runway-agent-creates-entire-campaigns-analyze|Agent 2.0]] · Change
- 2026-06-24 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-24-4-agent-mode-changes-in-v1-0-65|4 Agent Mode changes in v1.0.65]] · Digest
- 2026-06-23 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-23-6-agent-mode-changes-in-v1-0-64|6 Agent Mode changes in v1.0.64]] · Digest
- 2026-06-22 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-22-2-agent-mode-changes-in-v2-1-186|2 Agent Mode changes in v2.1.186]] · Digest
- 2026-06-22 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-22-14-agent-mode-changes-in-rust-v0-142-0|14 Agent Mode changes in rust-v0.142.0]] · Digest
- 2026-06-22 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-06-22-new-entries-in-the-sensitive-paths-list-vscode-and-cache-are-now-recognized-as-s|New entries in the sensitive paths list]] · Change
- 2026-06-21 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-06-21-core-honor-configured-agent-step-limits-by-forcing-a-final-text-response-instead|Core Honor configured agent step limits by forcing a final text response instead…]] · Change
- 2026-06-19 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-19-improved-auto-mode-safety-destructive-git-commands-git-reset-hard-git-checkout-g|Improved auto mode safety]] · Change
- 2026-06-19 · <span class="tl-product tl-p25">**v0**</span> · [[Changes/v0/2026-06-19-annotations-mode-lets-you-click-elements-in-the-preview-to-drop-numbered-comment|Annotations mode lets you click elements in the preview to drop numbered comments…]] · Change
- 2026-06-18 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-18-5-agent-mode-changes-in-rust-v0-141-0|5 Agent Mode changes in rust-v0.141.0]] · Digest
- 2026-06-18 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-06-18-2-agent-mode-changes-in-v0-47-0|2 Agent Mode changes in v0.47.0]] · Digest
- 2026-06-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-17-improved-the-subagent-panel-idle-subagents-auto-hide-after-30s-the-list-caps-at|Improved the subagent panel]] · Change
- 2026-06-16 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-16-agent-mode-is-tracked-per-session-so-it-no-longer-carries-over-when-you-create-c|Agent mode is tracked per session, so it no longer carries over when you create…]] · Change
- 2026-06-15 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-15-2-agent-mode-changes-in-v2-1-178|2 Agent Mode changes in v2.1.178]] · Digest
- 2026-06-15 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-15-11-agent-mode-changes-in-rust-v0-140-0|11 Agent Mode changes in rust-v0.140.0]] · Digest
- 2026-06-13 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-13-4-agent-mode-changes-in-v1-0-62|4 Agent Mode changes in v1.0.62]] · Digest
- 2026-06-11 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-06-11-3-agent-mode-changes-in-hub-v2-1-4-quota-screen-redesign|3 Agent Mode changes in HUB v2.1.4 — Quota Screen Redesign…]] · Digest
- 2026-06-10 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-10-sub-agents-can-now-spawn-their-own-sub-agents-up-to-5-levels-deep|Sub-agents can now spawn their own sub-agents (up to 5 levels deep)]] · Change
- 2026-06-10 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-06-10-desktop-hidden-agents-no-longer-get-cycled-accidentally|Desktop Hidden agents no longer get cycled accidentally]] · Change
- 2026-06-10 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-06-10-2-agent-mode-changes-in-1-8-0|2 Agent Mode changes in 1.8.0]] · Digest
- 2026-06-09 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-09-5-agent-mode-changes-in-rust-v0-139-0|5 Agent Mode changes in rust-v0.139.0]] · Digest
- 2026-06-09 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-09-3-agent-mode-changes-in-v1-0-61|3 Agent Mode changes in v1.0.61]] · Digest
- 2026-06-08 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-08-2-agent-mode-changes-in-v2-1-169|2 Agent Mode changes in v2.1.169]] · Digest
- 2026-06-08 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-08-8-agent-mode-changes-in-rust-v0-138-0|8 Agent Mode changes in rust-v0.138.0]] · Digest
- 2026-06-08 · <span class="tl-product tl-p25">**v0**</span> · [[Changes/v0/2026-06-08-2-agent-mode-changes-in-changelog-update|2 Agent Mode changes in Changelog update]] · Digest
- 2026-06-06 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-06-claude-agents-typing-a-url-into-the-list-now-filters-to-the-session-whose-first|claude agents: typing a URL into the list now filters to the session whose first…]] · Change
- 2026-06-05 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-05-2-agent-mode-changes-in-v1-0-60|2 Agent Mode changes in v1.0.60]] · Digest
- 2026-06-05 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-06-05-core-added-skill-discovery-and-file-based-agent-loading|Core Added skill discovery and file-based agent loading]] · Change
- 2026-06-05 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-06-05-core-running-subagents-can-now-be-sent-to-the-background-so-you-can-keep-working|Core Running subagents can now be sent to the background so you can keep working]] · Change
- 2026-06-04 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-04-2-agent-mode-changes-in-v2-1-163|2 Agent Mode changes in v2.1.163]] · Digest
- 2026-06-04 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-04-12-agent-mode-changes-in-rust-v0-137-0|12 Agent Mode changes in rust-v0.137.0]] · Digest
- 2026-06-04 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-04-added-the-ability-for-agents-to-embed-buttons-in-canvases-that-will-run-a-specif|Added the ability for agents to embed buttons in canvases that will run a specific…]] · Change
- 2026-06-04 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-04-with-canvases-agents-can-create-interactive-artifacts-like-dashboards-reports-an|With canvases, agents can create interactive artifacts like dashboards, reports…]] · Change
- 2026-06-04 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-04-5-agent-mode-changes-in-custom-stores-custom-tools|5 Agent Mode changes in Custom stores, custom tools…]] · Digest
- 2026-06-03 · <span class="tl-product tl-p17">**Ollama**</span> · [[Changes/Ollama/2026-06-03-nemotron-3-ultra-https-ollama-com-library-nemotron-3-ultra-nvidia-nemotron-3-ult|Nemotron-3-Ultra((source link) NVIDIA Nemotron 3…]] · Change
- 2026-06-02 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-02-improved-performance-of-opening-recently-inactive-background-agent-sessions-in-c|Improved performance of opening recently-inactive background agent sessions…]] · Change
- 2026-06-02 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-02-claude-agents-rows-now-show-done-total-before-the-detail-when-work-is-fanned-out|claude agents rows now show done/total before the detail when work is fanned out]] · Change
- 2026-06-01 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-01-3-agent-mode-changes-in-rust-v0-136-0|3 Agent Mode changes in rust-v0.136.0]] · Digest
- 2026-06-01 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-01-canceling-a-running-shell-command-ctrl-c-on-a-command-or-aborting-an-agent-comma|Canceling a running shell command (Ctrl+C on a !command, or aborting an agent command]] · Change

**2026-05**

- 2026-05-29 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-29-claude-agents-the-agent-field-in-settings-json-is-now-honored-for-dispatched-ses|claude agents: the agent field in settings.json is now honored for dispatched…]] · Change
- 2026-05-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-05-29-auto-review-is-a-new-run-mode-that-allows-cursor-to-work-for-longer-with-fewer-a-61df08|Auto-review Run Mode]] · Change
- 2026-05-29 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-29-add-builtinagents-rubberduck-setting-to-enable-or-disable-the-rubber-duck-agent|Add builtInAgents.rubberDuck setting to enable or disable the rubber duck agent…]] · Change
- 2026-05-28 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-28-4-agent-mode-changes-in-v2-1-154|4 Agent Mode changes in v2.1.154]] · Digest
- 2026-05-28 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-28-3-agent-mode-changes-in-v2-1-153|3 Agent Mode changes in v2.1.153]] · Digest
- 2026-05-28 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-28-24714-fix-auto-review-skip-legacy-notify-for-auto-review-threads-dylan-hurd-oai|♯24714 fix(auto-review) skip legacy notify for auto review threads @dylan-hurd-oai]] · Change
- 2026-05-28 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-28-3-agent-mode-changes-in-v1-0-55|3 Agent Mode changes in v1.0.55]] · Digest
- 2026-05-27 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-27-2-agent-mode-changes-in-v2-1-152|2 Agent Mode changes in v2.1.152]] · Digest
- 2026-05-27 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-27-4-agent-mode-changes-in-v0-44-0|4 Agent Mode changes in v0.44.0]] · Digest
- 2026-05-27 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-05-27-core-experimental-background-agents-now-push-updates-without-polling|Core Experimental background agents now push updates without polling]] · Change
- 2026-05-26 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-26-3-agent-mode-changes-in-rust-v0-134-0|3 Agent Mode changes in rust-v0.134.0]] · Digest
- 2026-05-23 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-23-custom-agents-support-opt-in-deferred-tool-loading-via-deferred-tool-loading-in|Custom agents support opt-in deferred tool loading via deferred-tool-loading…]] · Change
- 2026-05-22 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-22-2-agent-mode-changes-in-v0-43-0|2 Agent Mode changes in v0.43.0]] · Digest
- 2026-05-21 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-21-auto-mode-no-longer-suppresses-askuserquestion-when-the-user-or-a-skill-explicit|Auto mode no longer suppresses AskUserQuestion when the user or a skill explicitly…]] · Change
- 2026-05-21 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-21-7-agent-mode-changes-in-rust-v0-133-0|7 Agent Mode changes in rust-v0.133.0]] · Digest
- 2026-05-20 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-20-23147-make-multi-agent-v2-tool-namespace-configurable-jif-oai|♯23147 Make multi-agent v2 tool namespace configurable @jif-oai]] · Change
- 2026-05-20 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-20-remote-command-can-now-be-used-while-the-agent-is-working|/remote command can now be used while the agent is working]] · Change
- 2026-05-20 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-05-20-core-agent-and-command-names-now-resolve-correctly-from-relative-config-paths|Core Agent and command names now resolve correctly from relative config paths]] · Change
- 2026-05-19 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-19-3-agent-mode-changes-in-v2-1-144|3 Agent Mode changes in v2.1.144]] · Digest
- 2026-05-19 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-19-3-agent-mode-changes-in-v2-1-145|3 Agent Mode changes in v2.1.145]] · Digest
- 2026-05-19 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-05-19-assign-work-items-to-cursor-or-mention-cursor-in-a-comment-to-kick-off-a-cloud-a-1c05f0|Assign work items to Cursor, or mention @Cursor in a comment to kick off a cloud agent]] · Change
- 2026-05-19 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-05-19-3-agent-mode-changes-in-1-14-2|3 Agent Mode changes in 1.14.2]] · Digest
- 2026-05-19 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-19-4-agent-mode-changes-in-v1-0-49|4 Agent Mode changes in v1.0.49]] · Digest
- 2026-05-18 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-18-9-agent-mode-changes-in-rust-v0-131-0|9 Agent Mode changes in rust-v0.131.0]] · Digest
- 2026-05-17 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-05-17-core-hid-background-subagent-task-instructions-unless-experimental-background-mo|Core Hid background subagent task instructions unless experimental background mode…]] · Change
- 2026-05-16 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-05-16-terminal-fixed-opencode-run-agent-resolving-project-local-agents|Terminal Fixed opencode run --agent resolving project-local agents]] · Change
- 2026-05-15 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-15-2-agent-mode-changes-in-v2-1-143|2 Agent Mode changes in v2.1.143]] · Digest
- 2026-05-15 · <span class="tl-product tl-p25">**v0**</span> · [[Changes/v0/2026-05-15-2-agent-mode-changes-in-claude-opus-4-7-fast-agent-browser|2 Agent Mode changes in Claude Opus 4.7 Fast, agent browser…]] · Digest
- 2026-05-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-14-improved-hook-configuration-error-configuring-a-prompt-or-agent-type-hook-for-se|Improved hook configuration error]] · Change
- 2026-05-14 · <span class="tl-product tl-p17">**Ollama**</span> · [[Changes/Ollama/2026-05-14-for-difficult-coding-and-agentic-tasks|For difficult coding and agentic tasks]] · Change
- 2026-05-13 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-13-4-agent-mode-changes-in-v2-1-141|4 Agent Mode changes in v2.1.141]] · Digest
- 2026-05-13 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-05-13-improved-agent-led-environment-setup|Improved agent-led environment setup]] · Change
- 2026-05-13 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-05-13-to-take-engineering-tasks-from-start-to-finish-agents-need-a-development-environ-e47512|To take engineering tasks from start to finish, agents need a development…]] · Change
- 2026-05-13 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-13-resume-supports-copilot-cloud-agent-sessions-where-the-agent-hasn-t-pushed-any-c|--resume supports Copilot cloud agent sessions where the agent hasn't pushed any…]] · Change
- 2026-05-12 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-12-2-agent-mode-changes-in-v2-1-140|2 Agent Mode changes in v2.1.140]] · Digest
- 2026-05-12 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-05-12-chore-web-refresh-agent-skills-by-hyoban-in-https-github-com-langgenius-dify-pul|chore(web): refresh agent skills]] · Change
- 2026-05-12 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-12-2-agent-mode-changes-in-v0-42-0|2 Agent Mode changes in v0.42.0]] · Digest
- 2026-05-11 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-11-2-agent-mode-changes-in-v2-1-139|2 Agent Mode changes in v2.1.139]] · Digest
- 2026-05-11 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-05-11-mention-cursor-in-any-teams-channel-to-delegate-a-task-to-a-cloud-agent-or-pull-d30c31|Mention @Cursor in any Teams channel to delegate a task to a cloud agent or pull…]] · Change
- 2026-05-11 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-11-agentstop-hook-now-fires-correctly-when-the-agent-stops-via-task-complete|agentStop hook now fires correctly when the agent stops via task_complete]] · Change
- 2026-05-10 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-05-10-core-fixed-a-plan-mode-security-bypass-where-subagents-could-ignore-parent-agent|Core Fixed a Plan Mode security bypass where subagents could ignore parent-agent…]] · Change
- 2026-05-09 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-05-09-core-added-the-scout-agent-for-repo-research-docs-lookup-and-dependency-source-i|Core Added the Scout agent for repo research, docs lookup, and dependency-source…]] · Change
- 2026-05-07 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-07-5-agent-mode-changes-in-rust-v0-129-0|5 Agent Mode changes in rust-v0.129.0]] · Digest
- 2026-05-07 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-05-07-added-the-ability-to-control-explore-subagent-behavior-from-settings-choose-a-sp|Added the ability to control Explore subagent behavior from settings]] · Change
- 2026-05-07 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-05-07-terminal-fix-agent-create-to-use-the-agents-path|Terminal Fix /agent create to use the /agents path]] · Change
- 2026-05-06 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-06-add-rubber-duck-agent-for-gpt-sessions-powered-by-claude-available-in-experiment|Add rubber-duck agent for GPT sessions, powered by Claude (available in /experimental)]] · Change
- 2026-05-06 · <span class="tl-product tl-p24">**Windsurf**</span> · [[Changes/Windsurf/2026-05-06-improved-reliability-of-devin-local-agent|Improved reliability of Devin Local agent]] · Change
- 2026-05-05 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-05-feat-core-enhance-shell-command-validation-and-add-core-tools-allowlist-by-galz1|feat(core): enhance shell command validation and add core tools allowlist]] · Change
- 2026-05-05 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-05-add-experimental-mcp-tasks-support-mcp-tools-with-tasksupport-required-run-as-no|Add experimental MCP Tasks support]] · Change
- 2026-05-04 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-04-auto-mode-when-the-classifier-can-t-evaluate-an-action-the-error-now-includes-a|Auto mode: when the classifier can't evaluate an action, the error now includes…]] · Change
- 2026-05-04 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-05-04-core-improve-shell-command-handling-for-bash-powershell-and-cmd-sessions|Core Improve shell command handling for Bash, PowerShell, and cmd sessions]] · Change
- 2026-05-01 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-01-3-agent-mode-changes-in-v1-0-40|3 Agent Mode changes in v1.0.40]] · Digest

**2026-04**

- 2026-04-30 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-30-19-agent-mode-changes-in-rust-v0-128-0|19 Agent Mode changes in rust-v0.128.0]] · Digest
- 2026-04-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-29-3-agent-mode-changes-in-build-programmatic-agents|3 Agent Mode changes in Build programmatic agents…]] · Digest
- 2026-04-29 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-04-29-2-agent-mode-changes-in-1-14-0|2 Agent Mode changes in 1.14.0]] · Digest
- 2026-04-28 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-28-2-agent-mode-changes-in-v2-1-121|2 Agent Mode changes in v2.1.121]] · Digest
- 2026-04-28 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-28-3-agent-mode-changes-in-v0-40-0|3 Agent Mode changes in v0.40.0]] · Digest
- 2026-04-28 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-28-press-ctrl-x-b-to-move-the-current-running-task-or-shell-command-to-the-backgrou|Press ctrl+x → b to move the current running task or shell command to the background]] · Change
- 2026-04-27 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-04-27-core-added-a-configurable-default-shell-for-terminals-and-agent-shell-commands-w|Core Added a configurable default shell for terminals and agent shell commands…]] · Change
- 2026-04-26 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-04-26-core-sent-an-opencode-version-user-agent-header-with-http-requests|Core Sent an opencode/version User-Agent header with HTTP requests]] · Change
- 2026-04-24 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-24-5-agent-mode-changes-in-rust-v0-125-0|5 Agent Mode changes in rust-v0.125.0]] · Digest
- 2026-04-24 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-24-custom-agents-skills-and-commands-from-claude-are-no-longer-loaded-by-the-copilo|Custom agents, skills, and commands from ~/.claude/ are no longer loaded…]] · Change
- 2026-04-23 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-23-2-agent-mode-changes-in-v2-1-118|2 Agent Mode changes in v2.1.118]] · Digest
- 2026-04-23 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-23-2-agent-mode-changes-in-v2-1-119|2 Agent Mode changes in v2.1.119]] · Digest
- 2026-04-23 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-8-agent-mode-changes-in-rust-v0-123-0|8 Agent Mode changes in rust-v0.123.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-11-agent-mode-changes-in-rust-v0-124-0|11 Agent Mode changes in rust-v0.124.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-23-6-agent-mode-changes-in-v0-39-0|6 Agent Mode changes in v0.39.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-23-7-agent-mode-changes-in-v1-0-35|7 Agent Mode changes in v1.0.35]] · Digest
- 2026-04-22 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-22-2-agent-mode-changes-in-v2-1-117|2 Agent Mode changes in v2.1.117]] · Digest
- 2026-04-22 · <span class="tl-product tl-p17">**Ollama**</span> · [[Changes/Ollama/2026-04-22-kimi-cli-with-kimi-k2-6-excels-at-long-horizon-agentic-execution-tasks-through-a|Kimi CLI with Kimi K2.6 excels at long horizon agentic execution tasks through…]] · Change
- 2026-04-21 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-04-21-desktop-added-a-setting-to-hide-the-session-progress-bar-while-the-agent-is-work|Desktop Added a setting to hide the session progress bar while the agent is working]] · Change
- 2026-04-20 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-20-2-agent-mode-changes-in-v2-1-116|2 Agent Mode changes in v2.1.116]] · Digest
- 2026-04-20 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-20-10-agent-mode-changes-in-rust-v0-122-0|10 Agent Mode changes in rust-v0.122.0]] · Digest
- 2026-04-20 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-20-2-agent-mode-changes-in-v1-0-33|2 Agent Mode changes in v1.0.33]] · Digest
- 2026-04-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-17-subagents-that-stall-mid-stream-now-fail-with-a-clear-error-after-10-minutes-ins|Subagents that stall mid-stream now fail with a clear error after 10 minutes instead…]] · Change
- 2026-04-17 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-17-attach-supported-document-files-to-prompts-for-the-agent-to-read-and-reason-abou|Attach supported document files to prompts for the agent to read and reason about]] · Change
- 2026-04-16 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-16-auto-mode-no-longer-requires-enable-auto-mode|Auto mode no longer requires --enable-auto-mode]] · Change
- 2026-04-16 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-16-background-agent-completion-notifications-are-not-sent-redundantly-when-read-age|Background agent completion notifications are not sent redundantly when read_agent…]] · Change
- 2026-04-16 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-16-agent-correctly-identifies-repository-owner-from-git-remote-url-rather-than-loca|Agent correctly identifies repository owner from git remote URL rather than local username]] · Change
- 2026-04-15 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-15-7-agent-mode-changes-in-rust-v0-121-0|7 Agent Mode changes in rust-v0.121.0]] · Digest
- 2026-04-14 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-14-6-agent-mode-changes-in-v0-38-0|6 Agent Mode changes in v0.38.0]] · Digest
- 2026-04-13 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-13-3-agent-mode-changes-in-3-1|3 Agent Mode changes in 3.1]] · Digest
- 2026-04-11 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-11-4-agent-mode-changes-in-rust-v0-120-0|4 Agent Mode changes in rust-v0.120.0]] · Digest
- 2026-04-10 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-10-ultraplan-and-other-remote-session-features-now-auto-create-a-default-cloud-envi|/ultraplan and other remote-session features now auto-create a default cloud…]] · Change
- 2026-04-10 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-10-13-agent-mode-changes-in-rust-v0-119-0|13 Agent Mode changes in rust-v0.119.0]] · Digest
- 2026-04-10 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-10-add-mode-autopilot-and-plan-flags-to-start-the-cli-directly-in-a-specific-agent|Add --mode, --autopilot, and --plan flags to start the CLI directly in a specific…]] · Change
- 2026-04-09 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-09-3-agent-mode-changes-in-v2-1-98|3 Agent Mode changes in v2.1.98]] · Digest
- 2026-04-09 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-09-3-agent-mode-changes-in-v1-0-22|3 Agent Mode changes in v1.0.22]] · Digest
- 2026-04-08 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-08-2-agent-mode-changes-in-v2-1-97|2 Agent Mode changes in v2.1.97]] · Digest
- 2026-04-08 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-08-11-agent-mode-changes-in-v0-37-0|11 Agent Mode changes in v0.37.0]] · Digest
- 2026-04-07 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-07-spinner-no-longer-appears-stuck-when-a-long-running-async-shell-command-is-activ|Spinner no longer appears stuck when a long-running async shell command is active]] · Change
- 2026-04-07 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-07-spinner-stays-active-until-background-agents-and-shell-commands-finish-and-user|Spinner stays active until background agents and shell commands finish, and user…]] · Change
- 2026-04-07 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-04-07-new-agent-permissions-system-accessible-in-settings|New agent permissions system accessible in settings]] · Change
- 2026-04-06 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-06-2-agent-mode-changes-in-v1-0-19|2 Agent Mode changes in v1.0.19]] · Digest
- 2026-04-03 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-03-built-in-skills-are-now-included-with-the-cli-starting-with-a-guide-for-customiz|Built-in skills are now included with the CLI, starting with a guide for customizing…]] · Change
- 2026-04-02 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-02-4-agent-mode-changes-in-3-0|4 Agent Mode changes in 3.0]] · Digest
- 2026-04-01 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-01-3-agent-mode-changes-in-v2-1-89|3 Agent Mode changes in v2.1.89]] · Digest
- 2026-04-01 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-04-01-exclude-new-task-tool-from-system-prompt-in-yolo-headless-mode|Exclude new_task tool from system prompt in yolo/headless mode]] · Change
- 2026-04-01 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-01-10-agent-mode-changes-in-v0-36-0|10 Agent Mode changes in v0.36.0]] · Digest

**2026-03**

- 2026-03-31 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-31-4-agent-mode-changes-in-rust-v0-118-0|4 Agent Mode changes in rust-v0.118.0]] · Digest
- 2026-03-31 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-03-31-core-subagent-tool-calls-stay-clickable-while-they-are-pending|Core Subagent tool calls stay clickable while they are pending]] · Change
- 2026-03-27 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-27-auto-mode-now-shows-unavailable-for-your-plan-when-disabled-by-plan-restrictions|Auto mode now shows "unavailable for your plan" when disabled by plan restrictions…]] · Change
- 2026-03-27 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-03-27-4-agent-mode-changes-in-1-13-3|4 Agent Mode changes in 1.13.3]] · Digest
- 2026-03-26 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-26-2-agent-mode-changes-in-v2-1-84|2 Agent Mode changes in v2.1.84]] · Digest
- 2026-03-26 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-26-19-agent-mode-changes-in-rust-v0-117-0|19 Agent Mode changes in rust-v0.117.0]] · Digest
- 2026-03-26 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-26-resume-session-restores-the-previously-selected-custom-agent|Resume session restores the previously selected custom agent]] · Change
- 2026-03-26 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-03-26-desktop-fix-agent-normalization-in-desktop-app|Desktop Fix agent normalization in desktop app]] · Change
- 2026-03-25 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-25-agents-can-now-declare-initialprompt-in-frontmatter-to-auto-submit-a-first-turn|Agents can now declare initialPrompt in frontmatter to auto-submit a first turn]] · Change
- 2026-03-25 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-03-25-cursor-now-supports-self-hosted-cloud-agents-that-keep-your-code-and-tool-execut-e411f3|Self-hosted Cloud Agents]] · Change
- 2026-03-25 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-03-25-various-layout-and-ux-improvements-in-the-agent-manager|Various layout and UX improvements in the agent manager]] · Change
- 2026-03-24 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-24-10-agent-mode-changes-in-v0-35-0|10 Agent Mode changes in v0.35.0]] · Digest
- 2026-03-23 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-23-2-agent-mode-changes-in-v1-0-11|2 Agent Mode changes in v1.0.11]] · Digest
- 2026-03-22 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-03-22-ui-ux-improvements-agent-skill-ordering-more-consistent-ai-responses-with-improv|UI/UX Improvements Agent & Skill Ordering]] · Change
- 2026-03-19 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-19-5-agent-mode-changes-in-rust-v0-116-0|5 Agent Mode changes in rust-v0.116.0]] · Digest
- 2026-03-18 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-18-2-agent-mode-changes-in-v1-0-8|2 Agent Mode changes in v1.0.8]] · Digest
- 2026-03-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-17-2-agent-mode-changes-in-v2-1-77|2 Agent Mode changes in v2.1.77]] · Digest
- 2026-03-17 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-03-17-5-agent-mode-changes-in-1-13-1|5 Agent Mode changes in 1.13.1]] · Digest
- 2026-03-17 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-17-7-agent-mode-changes-in-v0-34-0|7 Agent Mode changes in v0.34.0]] · Digest
- 2026-03-17 · <span class="tl-product tl-p17">**Ollama**</span> · [[Changes/Ollama/2026-03-17-you-can-ask-your-openclaw-to-run-tasks-using-claude-with-subagents|You can ask your OpenClaw to run tasks using claude with subagents]] · Change
- 2026-03-16 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-16-16-agent-mode-changes-in-rust-v0-115-0|16 Agent Mode changes in rust-v0.115.0]] · Digest
- 2026-03-16 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-16-5-agent-mode-changes-in-v1-0-6|5 Agent Mode changes in v1.0.6]] · Digest
- 2026-03-16 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-03-16-core-ensure-that-compaction-message-is-tracked-as-agent-initiated|Core Ensure that compaction message is tracked as agent initiated]] · Change
- 2026-03-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-14-improved-background-agent-behavior-killing-a-background-agent-now-preserves-its|Improved background agent behavior]] · Change
- 2026-03-13 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-13-send-follow-up-messages-to-background-agents-with-the-write-agent-tool-for-multi|Send follow-up messages to background agents with the write_agent tool…]] · Change
- 2026-03-12 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-03-12-added-github-copilot-instructions-md-for-coding-agents|Added .github/copilot-instructions.md for coding agents]] · Change
- 2026-03-12 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-03-12-core-improve-skill-presentation-to-agent-to-increase-likelihood-of-skill-invocat|Core Improve skill presentation to agent to increase likelihood of skill invocations]] · Change
- 2026-03-11 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-11-6-agent-mode-changes-in-v0-33-0|6 Agent Mode changes in v0.33.0]] · Digest
- 2026-03-11 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-11-2-agent-mode-changes-in-v1-0-4|2 Agent Mode changes in v1.0.4]] · Digest
- 2026-03-11 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2026-03-11-2-agent-mode-changes-in-1-5-0|2 Agent Mode changes in 1.5.0]] · Digest
- 2026-03-10 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-10-2-agent-mode-changes-in-v2-1-72|2 Agent Mode changes in v2.1.72]] · Digest
- 2026-03-05 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-05-2-agent-mode-changes-in-v2-1-69|2 Agent Mode changes in v2.1.69]] · Digest
- 2026-03-05 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-05-13-agent-mode-changes-in-rust-v0-110-0|13 Agent Mode changes in rust-v0.110.0]] · Digest
- 2026-03-05 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-05-automatic-notifications-when-background-shell-commands-and-agents-complete|Automatic notifications when background shell commands and agents complete]] · Change
- 2026-03-04 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-03-04-subagent-stream-retry-delay-increased-to-reduce-noise-from-transient-failures|Subagent stream retry delay increased to reduce noise from transient failures]] · Change
- 2026-03-03 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-03-03-add-user-agent-header-to-requests-sent-to-the-cline-backend|Add User-Agent header to requests sent to the Cline backend]] · Change
- 2026-03-03 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-03-03-improved-reliability-for-longer-running-agent-sessions|Improved reliability for longer-running agent sessions]] · Change
- 2026-03-03 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-03-3-agent-mode-changes-in-v0-32-0|3 Agent Mode changes in v0.32.0]] · Digest
- 2026-03-03 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-03-shell-command-output-on-windows-no-longer-renders-as-no-changes-detected-in-the|Shell command output on Windows no longer renders as "No changes detected" in the timeline]] · Change
- 2026-03-02 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-02-2-agent-mode-changes-in-rust-v0-107-0|2 Agent Mode changes in rust-v0.107.0]] · Digest

**2026-02**

- 2026-02-28 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-28-added-http-hooks-which-can-post-json-to-a-url-and-receive-json-instead-of-runnin|Added HTTP hooks, which can POST JSON to a URL and receive JSON instead of running…]] · Change
- 2026-02-27 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-27-feat-browser-implement-experimental-browser-agent-by-gsquared94-in-https-github|feat(browser): implement experimental browser agent]] · Change
- 2026-02-27 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-27-cli-spinner-stops-and-final-agent-response-is-visible-after-agent-finishes-work|CLI spinner stops and final agent response is visible after agent finishes work]] · Change
- 2026-02-26 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-26-5-agent-mode-changes-in-rust-v0-106-0|5 Agent Mode changes in rust-v0.106.0]] · Digest
- 2026-02-26 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-02-26-autofix-runs-cloud-agents-on-their-own-machines-to-test-changes-and-propose-fixe|Autofix runs cloud agents on their own machines to test changes and propose fixes…]] · Change
- 2026-02-25 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-25-18-agent-mode-changes-in-rust-v0-105-0|18 Agent Mode changes in rust-v0.105.0]] · Digest
- 2026-02-25 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-25-4-agent-mode-changes-in-v0-30-0|4 Agent Mode changes in v0.30.0]] · Digest
- 2026-02-25 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-25-agent-protected-from-accidentally-killing-itself|Agent protected from accidentally killing itself]] · Change
- 2026-02-24 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-02-24-3-agent-mode-changes-in-v3-67-0|3 Agent Mode changes in v3.67.0]] · Digest
- 2026-02-24 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-02-24-cloud-agents-can-now-use-the-software-they-create-to-test-changes-and-demo-their-c922e9|Cloud Agents with Computer Use]] · Change
- 2026-02-23 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-23-2-agent-mode-changes-in-v0-0-415|2 Agent Mode changes in v0.0.415]] · Digest
- 2026-02-23 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2026-02-23-file-edits-now-persist-when-stopping-the-agent-so-you-can-resume-work-without-lo|File edits now persist when stopping the agent, so you can resume work without…]] · Change
- 2026-02-23 · <span class="tl-product tl-p18">**Open WebUI**</span> · [[Changes/Open WebUI/2026-02-23-api-tools-fix-the-api-v1-chat-completions-endpoint-now-properly-respects-caller|🛠️ API tools fix. The /api/v1/chat/completions endpoint now properly respects…]] · Change
- 2026-02-20 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-20-2-agent-mode-changes-in-v2-1-50|2 Agent Mode changes in v2.1.50]] · Digest
- 2026-02-20 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-02-20-core-remove-user-agent-header-assertion-from-llm-test-to-fix-failing-test|Core Remove User-Agent header assertion from LLM test to fix failing test]] · Change
- 2026-02-19 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-19-3-agent-mode-changes-in-v0-0-412|3 Agent Mode changes in v0.0.412]] · Digest
- 2026-02-19 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-02-19-core-migrate-agent-ts-from-bun-file-to-filesystem-module|Core Migrate agent.ts from Bun.file() to Filesystem module]] · Change
- 2026-02-18 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-18-2-agent-mode-changes-in-v2-1-47|2 Agent Mode changes in v2.1.47]] · Digest
- 2026-02-18 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-18-protocol-core-now-carry-distinct-approval-ids-for-command-approvals-to-support-m|Protocol/core now carry distinct approval IDs for command approvals to support…]] · Change
- 2026-02-18 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-02-18-2-agent-mode-changes-in-cli-improvements-and-mermaid-ascii|2 Agent Mode changes in CLI Improvements and Mermaid ASCII…]] · Digest
- 2026-02-18 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-18-8-agent-mode-changes-in-v0-29-0|8 Agent Mode changes in v0.29.0]] · Digest
- 2026-02-17 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-17-7-agent-mode-changes-in-rust-v0-102-0|7 Agent Mode changes in rust-v0.102.0]] · Digest
- 2026-02-17 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-02-17-6-agent-mode-changes-in-2-5|6 Agent Mode changes in 2.5]] · Digest
- 2026-02-12 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-02-12-subagent-replace-legacy-subagents-with-the-native-use-subagents-tool|Subagent: replace legacy subagents with the native use_subagents tool]] · Change
- 2026-02-12 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-12-2-agent-mode-changes-in-rust-v0-100-0|2 Agent Mode changes in rust-v0.100.0]] · Digest
- 2026-02-12 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-02-12-cursor-can-now-work-autonomously-over-longer-horizons-to-complete-larger-more-co-48843c|Long-running Agents in Research Preview]] · Change
- 2026-02-12 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-12-subagents-return-complete-responses|Subagents return complete responses]] · Change
- 2026-02-11 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-11-10-agent-mode-changes-in-rust-v0-99-0|10 Agent Mode changes in rust-v0.99.0]] · Digest
- 2026-02-11 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-02-11-flexible-delivery-methods-human-input-forms-can-be-delivered-via-webapp-or-email|Flexible Delivery Methods: Human input forms can be delivered…]] · Change
- 2026-02-11 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-11-3-agent-mode-changes-in-v0-0-407|3 Agent Mode changes in v0.0.407]] · Digest
- 2026-02-10 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-10-4-agent-mode-changes-in-v0-28-0|4 Agent Mode changes in v0.28.0]] · Digest
- 2026-02-10 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-02-10-4-agent-mode-changes-in-v1-1-54|4 Agent Mode changes in v1.1.54]] · Digest
- 2026-02-06 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-06-2-agent-mode-changes-in-v2-1-33|2 Agent Mode changes in v2.1.33]] · Digest
- 2026-02-05 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-05-updated-resume-to-re-use-agent-value-specified-in-previous-conversation-by-defau|Updated --resume to re-use --agent value specified in previous conversation by default]] · Change
- 2026-02-05 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-05-10649-fix-test-shell-command-interruption-flake-gt-oai|♯10649 Fix test_shell_command_interruption flake @gt-oai]] · Change
- 2026-02-05 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-05-support-comma-separated-tools-in-custom-agent-frontmatter|Support comma-separated tools in custom agent frontmatter]] · Change
- 2026-02-05 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-05-2-agent-mode-changes-in-v0-0-404|2 Agent Mode changes in v0.0.404]] · Digest
- 2026-02-05 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2026-02-05-extended-processing-time-per-request-for-the-lovable-agent-up-to-15-minutes-supp|Extended processing time per request for the Lovable agent, up to 15 minutes…]] · Change
- 2026-02-04 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-04-4-agent-mode-changes-in-rust-v0-95-0|4 Agent Mode changes in rust-v0.95.0]] · Digest
- 2026-02-04 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-04-15-agent-mode-changes-in-v0-27-0|15 Agent Mode changes in v0.27.0]] · Digest
- 2026-02-04 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-02-04-core-prioritize-opencode-config-dir-for-agents-md|Core Prioritize OPENCODE_CONFIG_DIR for AGENTS.md]] · Change
- 2026-02-04 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-02-04-2-agent-mode-changes-in-v1-1-50|2 Agent Mode changes in v1.1.50]] · Digest
- 2026-02-03 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-03-added-token-count-tool-uses-and-duration-metrics-to-task-tool-results|Added token count, tool uses, and duration metrics to Task tool results]] · Change
- 2026-02-03 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-02-03-9-agent-mode-changes-in-1-12-0|9 Agent Mode changes in 1.12.0]] · Digest
- 2026-02-03 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-03-4-agent-mode-changes-in-v0-0-402|4 Agent Mode changes in v0.0.402]] · Digest
- 2026-02-03 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-03-support-agents-skills-directory-for-auto-loading-skills|Support .agents/skills directory for auto-loading skills]] · Change
- 2026-02-03 · <span class="tl-product tl-p17">**Ollama**</span> · [[Changes/Ollama/2026-02-03-ollama-launch-will-now-work-run-subagents-when-using-ollama-launch-claude|ollama launch will now work run subagents when using ollama launch claude]] · Change
- 2026-02-03 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-02-03-4-agent-mode-changes-in-v1-1-49|4 Agent Mode changes in v1.1.49]] · Digest
- 2026-02-02 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-02-2-agent-mode-changes-in-rust-v0-94-0|2 Agent Mode changes in rust-v0.94.0]] · Digest

**2026-01**

- 2026-01-29 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-29-2-agent-mode-changes-in-v0-0-399|2 Agent Mode changes in v0.0.399]] · Digest
- 2026-01-28 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-28-8-agent-mode-changes-in-v0-26-0|8 Agent Mode changes in v0.26.0]] · Digest
- 2026-01-28 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-28-add-acp-flag-to-start-as-agent-client-protocol-server|Add --acp flag to start as Agent Client Protocol server]] · Change
- 2026-01-28 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-28-3-agent-mode-changes-in-v1-1-37|3 Agent Mode changes in v1.1.37]] · Digest
- 2026-01-27 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-01-27-2-agent-mode-changes-in-v2-1-20|2 Agent Mode changes in v2.1.20]] · Digest
- 2026-01-27 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-27-9818-feat-rebase-multi-agent-tui-on-config-snapshot-jif-oai|♯9818 feat: rebase multi-agent tui on config_snapshot @jif-oai]] · Change
- 2026-01-27 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-27-3-agent-mode-changes-in-v0-0-396|3 Agent Mode changes in v0.0.396]] · Digest
- 2026-01-26 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-26-load-local-shell-configuration-in-agent-sessions|Load local shell configuration in agent sessions]] · Change
- 2026-01-25 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-25-2-agent-mode-changes-in-rust-v0-91-0|2 Agent Mode changes in rust-v0.91.0]] · Digest
- 2026-01-25 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-25-2-agent-mode-changes-in-rust-v0-90-0|2 Agent Mode changes in rust-v0.90.0]] · Digest
- 2026-01-25 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-25-2-agent-mode-changes-in-v1-1-35|2 Agent Mode changes in v1.1.35]] · Digest
- 2026-01-23 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-01-23-added-env-var-claude-code-enable-tasks-set-to-false-to-keep-the-old-system-tempo|Added env var CLAUDE_CODE_ENABLE_TASKS, set to false to keep the old system…]] · Change
- 2026-01-23 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-23-add-support-for-ghe-cloud-ghe-com-remote-custom-agents|Add support for GHE Cloud (\.ghe.com) remote custom agents]] · Change
- 2026-01-22 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-22-9650-chore-tweak-agents-md-dylan-hurd-oai|♯9650 chore: tweak AGENTS.md @dylan-hurd-oai]] · Change
- 2026-01-22 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-01-22-4-agent-mode-changes-in-2-4|4 Agent Mode changes in 2.4]] · Digest
- 2026-01-22 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-01-22-agents-are-solving-increasingly-complex-long-running-tasks-across-your-codebase|Agents are solving increasingly complex, long-running tasks across your codebase]] · Change
- 2026-01-22 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-22-2-agent-mode-changes-in-v0-0-389|2 Agent Mode changes in v0.0.389]] · Digest
- 2026-01-21 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-21-2-agent-mode-changes-in-rust-v0-88-0|2 Agent Mode changes in rust-v0.88.0]] · Digest
- 2026-01-21 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-21-13-agent-mode-changes-in-v0-25-0|13 Agent Mode changes in v0.25.0]] · Digest
- 2026-01-21 · <span class="tl-product tl-p25">**v0**</span> · [[Changes/v0/2026-01-21-added-ai-sdk-v6-support-for-agents|Added AI SDK v6 support for agents]] · Change
- 2026-01-20 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-20-2-agent-mode-changes-in-v1-1-28|2 Agent Mode changes in v1.1.28]] · Digest
- 2026-01-19 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-19-mcp-server-management-when-swapping-between-custom-agents-with-agent|MCP server management when swapping between custom agents with /agent]] · Change
- 2026-01-19 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-19-core-restore-persisted-model-and-agent-when-loading-acp-session|Core Restore persisted model and agent when loading ACP session]] · Change
- 2026-01-16 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-01-16-added-plansdirectory-setting-to-customize-where-plan-files-are-stored|Added plansDirectory setting to customize where plan files are stored]] · Change
- 2026-01-16 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-01-16-added-hooks-for-session-start-end-prompt-and-stop-for-customizing-agent-lifecycl|Added hooks for session start/end, prompt, and stop for customizing agent lifecycle events]] · Change
- 2026-01-16 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-16-2-agent-mode-changes-in-v0-0-384|2 Agent Mode changes in v0.0.384]] · Digest
- 2026-01-16 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2026-01-16-vitest-is-now-included-in-the-react-template-enabling-the-agent-to-write-and-run|Vitest is now included in the React template, enabling the agent to write…]] · Change
- 2026-01-16 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-16-3-agent-mode-changes-in-v1-1-24|3 Agent Mode changes in v1.1.24]] · Digest
- 2026-01-15 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-15-9275-feat-add-agent-roles-to-collab-tools-jif-oai|♯9275 feat: add agent roles to collab tools @jif-oai]] · Change
- 2026-01-15 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-15-core-ensure-frontmatter-can-process-same-content-as-other-agents|Core Ensure frontmatter can process same content as other agents]] · Change
- 2026-01-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-01-14-added-inline-display-of-agent-s-final-response-in-task-notifications-making-it-e|Added inline display of agent's final response in task notifications, making…]] · Change
- 2026-01-14 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-14-2-agent-mode-changes-in-rust-v0-81-0|2 Agent Mode changes in rust-v0.81.0]] · Digest
- 2026-01-14 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-14-10-agent-mode-changes-in-v0-24-0|10 Agent Mode changes in v0.24.0]] · Digest
- 2026-01-14 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-14-3-agent-mode-changes-in-v1-1-19|3 Agent Mode changes in v1.1.19]] · Digest
- 2026-01-14 · <span class="tl-product tl-p25">**v0**</span> · [[Changes/v0/2026-01-14-improved-agent-error-handling|Improved agent error handling]] · Change
- 2026-01-13 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-01-13-3-agent-mode-changes-in-1-11-3|3 Agent Mode changes in 1.11.3]] · Digest
- 2026-01-13 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-13-3-agent-mode-changes-in-v0-0-380|3 Agent Mode changes in v0.0.380]] · Digest
- 2026-01-13 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-01-13-agent-skills-now-available-in-antigravity|Agent Skills now available in Antigravity]] · Change
- 2026-01-11 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-01-11-added-claude-code-disable-background-tasks-environment-variable-to-disable-all-b|Added CLAUDE_CODE_DISABLE_BACKGROUND_TASKS environment variable to disable all…]] · Change
- 2026-01-10 · <span class="tl-product tl-p17">**Ollama**</span> · [[Changes/Ollama/2026-01-10-ollama-run-experimental-cli-will-now-open-a-new-ollama-cli-that-includes-an-agen|ollama run --experimental CLI will now open a new Ollama CLI that includes…]] · Change
- 2026-01-09 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-01-09-added-agent-type-to-sessionstart-hook-input-populated-if-agent-is-specified|Added agent_type to SessionStart hook input, populated if --agent is specified]] · Change
- 2026-01-09 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-01-09-add-skills-system-for-reusable-on-demand-agent-instructions|Add Skills system for reusable, on-demand agent instructions]] · Change
- 2026-01-09 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-09-2-agent-mode-changes-in-rust-v0-80-0|2 Agent Mode changes in rust-v0.80.0]] · Digest
- 2026-01-08 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-01-08-new-agent-command-is-now-the-primary-cli-entrypoint-cursor-agent-remains-as-a-ba|New agent command is now the primary CLI entrypoint. cursor-agent remains…]] · Change
- 2026-01-08 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-08-task-tool-subagents-can-now-process-images|Task tool subagents can now process images]] · Change
- 2026-01-08 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-08-core-simplify-task-tool-subagent-filtering|Core Simplify task tool subagent filtering]] · Change
- 2026-01-08 · <span class="tl-product tl-p25">**v0**</span> · [[Changes/v0/2026-01-08-improved-how-large-inputs-are-stored-in-the-agent-s-filesystem-for-better-recall|Improved how large inputs are stored in the agent's filesystem for better recall]] · Change
- 2026-01-07 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-07-4-agent-mode-changes-in-rust-v0-79-0|4 Agent Mode changes in rust-v0.79.0]] · Digest
- 2026-01-07 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-07-3-agent-mode-changes-in-v0-23-0|3 Agent Mode changes in v0.23.0]] · Digest
- 2026-01-07 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-07-3-agent-mode-changes-in-v1-1-6|3 Agent Mode changes in v1.1.6]] · Digest
- 2026-01-06 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-06-3-agent-mode-changes-in-v1-1-4|3 Agent Mode changes in v1.1.4]] · Digest
- 2026-01-05 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-05-core-transform-agent-improvements-and-optimizations|Core Transform agent improvements and optimizations]] · Change
- 2026-01-04 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-04-4-agent-mode-changes-in-v1-1-1|4 Agent Mode changes in v1.1.1]] · Digest
- 2026-01-02 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-02-built-in-subagents-for-exploring-and-managing-tasks|Built-in subagents for exploring and managing tasks]] · Change
- 2026-01-01 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2026-01-01-2-agent-mode-changes-in-v1-0-223-1|2 Agent Mode changes in v1.0.223 + 1]] · Digest

</details>

</details>

<details class="disclosure">
<summary>2025 · 298 entries (ChatGPT 2 · Claude 1 · Cline 5 · Codex CLI 18 · Cursor 50 · Dify 15 · ElevenLabs 110 · Gamma 2 · Gemini 1 · Gemini CLI 19 · GitHub Copilot CLI 5 · Google Antigravity 3 · Lovable 3 · Manus 3 · OpenCode 3 · OpenHands 17 · Replit 38 · Windsurf 2 · v0 1)</summary>

**2025-12**

- 2025-12-23 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2025-12-23-tasks|Tasks]] · Launch
- 2025-12-18 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2025-12-18-skills-for-organizations-partners-and-the-ecosystem|Skills for organizations, partners, and the ecosystem]] · Launch
- 2025-12-18 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-12-18-shared-agent-transcripts-164030|Shared agent transcripts]] · Launch
- 2025-12-18 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-12-18-linux-sandboxing-for-agents|Linux sandboxing for agents]] · Launch
- 2025-12-18 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-12-18-service-accounts|Service accounts]] · Launch
- 2025-12-16 · <span class="tl-product tl-p24">**Windsurf**</span> · [[Changes/Windsurf/2025-12-16-agents-tool-execution|Agents & Tool Execution]] · Launch
- 2025-12-15 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-12-15-agents-platform|Agents Platform]] · Launch
- 2025-12-15 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-12-15-agents-platform-ef857c|Agents Platform]] · Launch
- 2025-12-10 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-12-10-plan-mode-now-supports-inline-mermaid-diagrams-allowing-the-agent-to-automatical|Plan Mode improvements]] · Launch
- 2025-12-10 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-12-10-multi-agent-judging|Multi-agent judging]] · Launch
- 2025-12-08 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-12-08-agents-platform|Agents Platform]] · Launch
- 2025-12-08 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-12-08-new-endpoints|New Endpoints]] · Launch
- 2025-12-08 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-12-08-agents-platform-d0503f|Agents Platform]] · Launch
- 2025-12-08 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-12-08-lists-and-sorting|Lists and Sorting]] · Launch
- 2025-12-05 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-12-05-build-full-stack-mobile-apps-with-agent|Build full-stack mobile apps with Agent]] · Launch

**2025-11**

- 2025-11-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-27-agents-platform|Agents Platform]] · Launch
- 2025-11-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-27-agents-platform-d37ef7|Agents Platform]] · Launch
- 2025-11-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-27-python-sdk|Python SDK]] · Launch
- 2025-11-21 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-11-21-instant-grep-beta|Instant Grep (Beta)]] · Launch
- 2025-11-21 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-21-agents-platform|Agents Platform]] · Launch
- 2025-11-21 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-21-agents-platform-bffd62|Agents Platform]] · Launch
- 2025-11-20 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2025-11-20-nano-banana-pro|Nano Banana Pro]] · Launch
- 2025-11-18 · <span class="tl-product tl-p11">**Gemini**</span> · [[Changes/Gemini/2025-11-18-gemini-agent-is-now-available-on-the-web-to-google-ai-ultra-subscribers-18-in-th|Gemini Agent is now available on the web, to Google AI Ultra subscribers 18+ in the US]] · Expansion
- 2025-11-18 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2025-11-18-google-antigravity|Google Antigravity]] · Launch
- 2025-11-12 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-12-turn-and-conversation-configuration|Turn and Conversation Configuration]] · Launch
- 2025-11-12 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-12-agent-configuration|Agent Configuration]] · Launch
- 2025-11-12 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-12-testing|Testing]] · Launch
- 2025-11-12 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-12-agents-platform|Agents Platform]] · Launch
- 2025-11-12 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-12-agents-platform-e67d7a|Agents Platform]] · Launch
- 2025-11-12 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-12-agents-packages|Agents Packages]] · Launch
- 2025-11-07 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-11-07-animated-agent-icon|Animated agent icon]] · Launch
- 2025-11-07 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-11-07-at-symbol-filename-support-in-agent|At symbol filename support in Agent]] · Launch
- 2025-11-07 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-11-07-agent-tools-dropdown-in-planning-flow|Agent tools dropdown in planning flow]] · Launch
- 2025-11-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-05-agents-platform|Agents Platform]] · Launch
- 2025-11-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-05-agents|Agents]] · Launch
- 2025-11-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-05-agents-platform-acf28a|Agents Platform]] · Launch
- 2025-11-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-05-agents-packages|Agents Packages]] · Policy
- 2025-11-05 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2025-11-05-show-the-agent-what-you-mean|Show the agent what you mean]] · Launch

**2025-10**

- 2025-10-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-10-29-browser-ga-1124ce|Browser (GA)]] · Launch
- 2025-10-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-10-29-cloud-agents|Cloud Agents]] · Launch
- 2025-10-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-10-29-multi-agents-bb4f56|Multi-Agents]] · Launch
- 2025-10-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-27-agents-platform|Agents Platform]] · Launch
- 2025-10-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-27-agents-platform-b53aea|Agents Platform]] · Launch
- 2025-10-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-27-agents-cli|Agents CLI]] · Launch
- 2025-10-24 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-10-24-build-score-rating-system|Build Score rating system]] · Launch
- 2025-10-20 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-20-agents-cli|Agents CLI]] · Launch
- 2025-10-20 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-20-agents-platform|Agents Platform]] · Launch
- 2025-10-20 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-20-javascript-sdk|JavaScript SDK]] · Launch
- 2025-10-20 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-20-python-sdk|Python SDK]] · Launch
- 2025-10-14 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-14-client-packages|Client Packages]] · Launch
- 2025-10-14 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-14-javascript-sdk|JavaScript SDK]] · Launch
- 2025-10-14 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-14-agents-platform|Agents Platform]] · Launch
- 2025-10-14 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-14-python-sdk|Python SDK]] · Launch
- 2025-10-10 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-10-10-webview-logging-experience|Webview logging experience]] · Launch
- 2025-10-10 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-10-10-agent-usage-cost-visibility|Agent usage cost visibility]] · Launch
- 2025-10-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-07-agents-platform|Agents Platform]] · Launch
- 2025-10-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-07-agents-platform-821aa5|Agents Platform]] · Launch
- 2025-10-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-07-agents-platform-f78196|Agents Platform]] · Launch
- 2025-10-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-07-websocket-events|WebSocket Events]] · Launch

**2025-09**

- 2025-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-09-29-we-re-introducing-instant-checkout-in-chatgpt-and-the-agentic-commerce-protocol-8cbf19|ChatGPT introduces Instant Checkout and the Agentic Commerce Protocol that powers…]] · Launch
- 2025-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-09-29-agentic-commerce-protocol|Agentic Commerce Protocol]] · Launch
- 2025-09-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-09-29-hooks-beta|Hooks (beta)]] · Launch
- 2025-09-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-09-29-cursor-can-now-write-detailed-plans-before-starting-complex-tasks-this-allows-ag|Plan Mode]] · Launch
- 2025-09-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-09-29-monitor-agents-from-menubar|Monitor Agents from menubar]] · Launch
- 2025-09-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-09-29-agent-can-take-screenshots-improve-ui-and-debug-client-issues-read-more-about-br|Browser Controls]] · Launch
- 2025-09-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-09-29-image-file-support-for-agent|Image file support for Agent]] · Launch
- 2025-09-29 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-29-agents-platform|Agents Platform]] · Launch
- 2025-09-29 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-29-agents-platform-7144f6|Agents Platform]] · Launch
- 2025-09-26 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-09-26-agent-playground-testing-improvements|Agent playground testing improvements]] · Launch
- 2025-09-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-22-agents-platform|Agents Platform]] · Launch
- 2025-09-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-22-package-updates|Package Updates]] · Launch
- 2025-09-19 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-09-19-autonomy-level-control-for-agent|Autonomy level control for Agent]] · Launch
- 2025-09-16 · <span class="tl-product tl-p10">**Gamma**</span> · [[Changes/Gamma/2025-09-16-gamma-agent-your-ai-design-partner-that-does-it-all|Gamma Agent: Your AI design partner that does it all]] · Launch
- 2025-09-15 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-15-agents-platform|Agents Platform]] · Launch
- 2025-09-12 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-09-12-agents-automations-beta|Agents & Automations (beta)]] · Launch
- 2025-09-12 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-09-12-agent-3-launch|Agent 3 Launch]] · Launch
- 2025-09-08 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-08-agents-platform|Agents Platform]] · Launch
- 2025-09-05 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-09-05-general-agent|General Agent]] · Launch
- 2025-09-05 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-09-05-plan-mode|Plan mode]] · Launch
- 2025-09-01 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-01-agents-platform|Agents Platform]] · Launch
- 2025-09-01 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-01-agents-platform-e79cb5|Agents Platform]] · Launch

**2025-08**

- 2025-08-29 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-08-29-agent-infrastructure-upgrades|Agent infrastructure upgrades]] · Launch
- 2025-08-25 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-08-25-sdk-releases|SDK Releases]] · Launch
- 2025-08-25 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-08-25-elevenlabs-agent-testing|ElevenLabs agent Testing]] · Launch
- 2025-08-25 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-08-25-agents-platform|Agents Platform]] · Launch
- 2025-08-21 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-08-21-you-can-now-start-background-agents-directly-from-linear-delegate-tasks-to-curso|Run Agents in Linear]] · Launch
- 2025-08-21 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-08-21-get-native-os-notifications-when-an-agent-run-finishes-or-when-input-is-required|OS notifications from Agent]] · Launch
- 2025-08-11 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-08-11-agents-platform|Agents Platform]] · Launch
- 2025-08-11 · <span class="tl-product tl-p15">**Lovable**</span> · [[Changes/Lovable/2025-08-11-agent-mode-is-the-new-default-mode|Agent Mode is the new default mode]] · Launch
- 2025-08-06 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-08-06-github-support-for-background-agents|GitHub support for Background Agents]] · Launch
- 2025-08-06 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-08-06-sidebar-for-all-agents|Sidebar for all Agents]] · Launch
- 2025-08-06 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-08-06-sending-messages-while-cursor-is-working-now-does-a-better-job-of-steering-the-a|More Agent steerability]] · Launch
- 2025-08-04 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-08-04-agents-platform|Agents Platform]] · Launch
- 2025-08-04 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-08-04-agents-platform-core|Agents Platform Core]] · Launch
- 2025-08-04 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-08-04-operation-id-improvements|Operation ID Improvements]] · Launch
- 2025-08-04 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-08-04-agents-platform-df3387|Agents Platform]] · Launch
- 2025-08-01 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-08-01-agent-now-has-access-to-replit-docs|Agent now has access to Replit Docs]] · Launch

**2025-07**

- 2025-07-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-07-29-agents-can-now-use-your-native-terminal-a-new-terminal-will-be-created-when-need|Share terminal with Agent]] · Launch
- 2025-07-28 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-28-agents-platform|Agents Platform]] · Launch
- 2025-07-28 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-28-agents-platform-504721|Agents Platform]] · Launch
- 2025-07-25 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-07-25-queue|Queue]] · Launch
- 2025-07-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-22-agents-platform|Agents Platform]] · Launch
- 2025-07-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-22-agents-platform-32a4c5|Agents Platform]] · Launch
- 2025-07-14 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-14-agents-platform|Agents Platform]] · Launch
- 2025-07-14 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-14-agents-platform-d9d1f0|Agents Platform]] · Launch
- 2025-07-11 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-07-11-agent-multi-tool-calling-upgrade|Agent multi-tool calling upgrade]] · Launch
- 2025-07-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-07-tool-configuration|Tool Configuration]] · Launch
- 2025-07-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-07-workspace-resources|Workspace Resources]] · Launch
- 2025-07-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-07-widget-improvements|Widget Improvements]] · Launch
- 2025-07-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-07-agents-platform|Agents Platform]] · Launch
- 2025-07-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-07-enhanced-sip-trunk-support|Enhanced SIP Trunk Support]] · Launch
- 2025-07-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-07-agent-transfers|Agent Transfers]] · Launch
- 2025-07-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-07-sdks|SDKs]] · Launch
- 2025-07-04 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-07-04-custom-agent-instructions|Custom Agent Instructions]] · Launch
- 2025-07-03 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-07-03-let-agent-resolve-merge-conflicts|Let Agent resolve merge conflicts]] · Launch
- 2025-07-03 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-07-03-agent-to-dos-3ffa24|Agent To-dos]] · Launch
- 2025-07-03 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-07-03-you-can-now-queue-follow-up-messages-for-agent-once-it-s-done-with-current-task|Queued messages]] · Launch
- 2025-07-03 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-07-03-background-agent-improvements|Background Agent improvements]] · Launch

**2025-06**

- 2025-06-27 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-06-27-agent-system-prompt-optimization|Agent system prompt optimization]] · Launch
- 2025-06-27 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-06-27-new-app-creation-experience|New app creation experience]] · Launch
- 2025-06-23 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-23-agents-platform|Agents Platform]] · Launch
- 2025-06-23 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-23-tools-migration|Tools migration]] · Policy
- 2025-06-23 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-23-sdks|SDKs]] · Launch
- 2025-06-23 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-23-agents-platform-8fab02|Agents Platform]] · Launch
- 2025-06-23 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-23-agents-platform-c72fe1|Agents Platform]] · Launch
- 2025-06-17 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-17-agents-platform|Agents Platform]] · Launch
- 2025-06-17 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-17-agents-platform-e180ce|Agents Platform]] · Launch
- 2025-06-12 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-06-12-you-can-now-launch-background-agents-directly-from-slack-by-mentioning-cursor-ag|Launch Background Agents directly from Slack by mentioning @Cursor]] · Change
- 2025-06-11 · <span class="tl-product tl-p16">**Manus**</span> · [[Changes/Manus/2025-06-11-start-free-by-asking-any-question-and-get-instant-answers-need-more-power-one-cl|Introducing Manus FREE Chat Mode!]] · Launch
- 2025-06-08 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-08-agents-platform|Agents Platform]] · Launch
- 2025-06-08 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-08-agents-platform-5c0653|Agents Platform]] · Launch
- 2025-06-08 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-08-agents-platform-ce4a03|Agents Platform]] · Launch
- 2025-06-06 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-06-06-new-agent-entrypoints-in-workspace|New Agent entrypoints in workspace]] · Launch
- 2025-06-04 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-06-04-agent-in-jupyter-notebooks|Agent in Jupyter Notebooks]] · Launch
- 2025-06-04 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-06-04-background-agent-for-everyone-8b35dc|Background Agent for everyone]] · Launch
- 2025-06-04 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-06-04-this-release-brings-bugbot-for-code-review-a-first-look-at-memories-one-click-mc|Cursor brings Bugbot for code review, a first look at memories, one-click MCP setup…]] · Launch
- 2025-06-01 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-01-agents-platform|Agents Platform]] · Launch
- 2025-06-01 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-01-agents-platform-dedb85|Agents Platform]] · Launch

**2025-05**

- 2025-05-30 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-05-30-preview-empty-state-improvements|Preview empty state improvements]] · Launch
- 2025-05-26 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-05-26-agents-platform|Agents Platform]] · Launch
- 2025-05-26 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-05-26-agents-platform-bec9ee|Agents Platform]] · Launch
- 2025-05-19 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-05-19-agents-platform|Agents Platform]] · Launch
- 2025-05-19 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-05-19-agents-platform-e84d3e|Agents Platform]] · Launch
- 2025-05-16 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-05-16-ask-agent-to-add-a-database|Ask Agent to add a database]] · Launch
- 2025-05-15 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-05-15-fast-edits-for-long-files-with-agent|Fast edits for long files with Agent]] · Launch
- 2025-05-15 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-05-15-background-agent-preview|Background Agent (Preview)]] · Launch
- 2025-05-12 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-05-12-agents-platform|Agents Platform]] · Launch

**2025-04**

- 2025-04-28 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-04-28-new-endpoints|New Endpoints]] · Launch
- 2025-04-28 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-04-28-agents-platform|Agents Platform]] · Launch
- 2025-04-28 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-04-28-agents-platform-4b369f|Agents Platform]] · Launch
- 2025-04-28 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-04-28-agents-platform-6b1e4d|Agents Platform]] · Launch
- 2025-04-25 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-04-25-mobile-app-agent-tour-and-deployments-in-dock|Mobile app Agent tour and deployments in dock]] · Launch
- 2025-04-21 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-04-21-agents-platform|Agents Platform]] · Launch
- 2025-04-21 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-04-21-agents-platform-acb364|Agents Platform]] · Launch
- 2025-04-18 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-04-18-streamlined-agent-progress-ux|Streamlined Agent progress UX]] · Launch
- 2025-04-15 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-04-15-reviewing-agent-generated-code-is-now-easier-with-a-built-in-diff-view-at-the-en|Making reviews easier]] · Launch
- 2025-04-14 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-04-14-agents-platform|Agents Platform]] · Launch
- 2025-04-14 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-04-14-agents-platform-a7909d|Agents Platform]] · Launch
- 2025-04-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-04-07-agents-platform|Agents Platform]] · Launch
- 2025-04-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-04-07-agents-platform-b2e925|Agents Platform]] · Launch
- 2025-04-04 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-04-04-agent-reliability-improvements|Agent reliability improvements]] · Launch

**2025-03**

- 2025-03-31 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-03-31-agents-platform|Agents Platform]] · Launch
- 2025-03-31 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-03-31-agents-platform-3fb293|Agents Platform]] · Launch
- 2025-03-28 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-03-28-agent-v2-is-now-available|Agent v2 is now available]] · Launch
- 2025-03-24 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-03-24-agents-platform|Agents Platform]] · Launch
- 2025-03-24 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-03-24-agents-platform-e22490|Agents Platform]] · Launch
- 2025-03-23 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-03-23-built-in-modes-custom-modes-beta|Built-in modes & custom modes (beta)]] · Launch
- 2025-03-21 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-03-21-agent-timeline-messages|Agent timeline messages]] · Launch
- 2025-03-17 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-03-17-agents-platform|Agents Platform]] · Launch
- 2025-03-17 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-03-17-agents-platform-4355e7|Agents Platform]] · Launch
- 2025-03-10 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-03-10-agents-platform|Agents Platform]] · Launch
- 2025-03-10 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-03-10-agents-platform-c12c49|Agents Platform]] · Launch
- 2025-03-10 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-03-10-removed-endpoints|Removed Endpoints]] · Launch
- 2025-03-03 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-03-03-agents-platform|Agents Platform]] · Launch

**2025-02**

- 2025-02-28 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-02-28-deployment-improvements|Deployment improvements]] · Launch
- 2025-02-28 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-02-28-agent-v2|Agent v2]] · Launch
- 2025-02-25 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-02-25-agents-platform|Agents Platform]] · Launch
- 2025-02-17 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-02-17-agents-platform|Agents Platform]] · Launch
- 2025-02-17 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-02-17-api|API]] · Launch
- 2025-02-14 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-02-14-agent-updates|Agent updates]] · Launch
- 2025-02-10 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-02-10-agents-platform|Agents Platform]] · Launch
- 2025-02-07 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-02-07-agent-actions|Agent actions]] · Launch
- 2025-02-07 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-02-07-agent-is-now-free-to-try|Agent is now free to try]] · Launch
- 2025-02-07 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-02-07-new-replit-app-cover-pages|New Replit App cover pages]] · Launch
- 2025-02-04 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-02-04-agents-platform|Agents Platform]] · Launch

**2025-01**

- 2025-01-31 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-01-31-more-performant-agent-in-asia|More performant Agent in Asia]] · Launch
- 2025-01-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-01-27-agents-platform|Agents Platform]] · Launch
- 2025-01-16 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-01-16-agents-platform|Agents Platform]] · Launch
- 2025-01-10 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-01-10-agent-and-assistant-improvements|Agent and Assistant improvements]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 109 (Cline 5 · Codex CLI 18 · Cursor 18 · Dify 15 · ElevenLabs 1 · Gamma 1 · Gemini CLI 19 · GitHub Copilot CLI 5 · Google Antigravity 1 · Manus 2 · OpenCode 3 · OpenHands 17 · Replit 2 · Windsurf 1 · v0 1)</summary>

**2025-12**

- 2025-12-31 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2025-12-31-core-add-debug-agent-subcommand-to-test-agents-in-isolation|Core Add debug agent subcommand to test agents in isolation]] · Change
- 2025-12-31 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2025-12-31-core-cleaner-view-for-subagents-hint-text|Core Cleaner view for subagents hint text]] · Change
- 2025-12-30 · <span class="tl-product tl-p20">**OpenCode**</span> · [[Changes/OpenCode/2025-12-30-desktop-more-defensive-agent-access-in-desktop-application|Desktop More defensive agent access in desktop application]] · Change
- 2025-12-29 · <span class="tl-product tl-p16">**Manus**</span> · [[Changes/Manus/2025-12-29-manus-is-joining-meta-nothing-changes-for-you-same-team-same-product-same-commit|Manus's next step]] · Change
- 2025-12-25 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-12-25-2-agent-mode-changes-in-1-11-2|2 Agent Mode changes in 1.11.2]] · Digest
- 2025-12-22 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-12-22-2-agent-mode-changes-in-2-3|2 Agent Mode changes in 2.3]] · Digest
- 2025-12-22 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-12-22-this-includes-the-core-agent-layout-controls-viewing-code-diffs-and-more-we-will|This includes the core agent, layout controls, viewing code diffs, and more]] · Change
- 2025-12-22 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-22-send-the-model-and-cli-version-with-the-user-agent-by-gundermanc-in-https-github|Send the model and CLI version with the user agent]] · Change
- 2025-12-18 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-18-3-agent-mode-changes-in-rust-v0-74-0|3 Agent Mode changes in rust-v0.74.0]] · Digest
- 2025-12-16 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-12-16-new-openhands-1-0-0-using-the-new-software-agent-sdk-https-github-com-openhands|New OpenHands 1.0.0 using the new…]] · Change
- 2025-12-15 · <span class="tl-product tl-p16">**Manus**</span> · [[Changes/Manus/2025-12-15-we-ve-just-released-a-major-upgrade-with-a-new-flagship-agent-manus-1-6-max-plus|Welcome Manus 1.6]] · Change
- 2025-12-11 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-12-11-2-agent-mode-changes-in-1-11-0|2 Agent Mode changes in 1.11.0]] · Digest
- 2025-12-10 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-12-10-agent-plans-are-now-files-that-can-be-edited-with-normal-tools|Agent plans are now files that can be edited with normal tools]] · Change
- 2025-12-09 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-09-7729-feat-add-is-mutating-detection-for-shell-command-handler-jif-oai|♯7729 feat: add is-mutating detection for shell command handler @jif-oai]] · Change
- 2025-12-09 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-09-feat-a2a-urgent-fix-process-modelinfo-agent-message-by-cocosheng-g-in-https-gith|feat(a2a): Urgent fix - Process modelInfo agent message]] · Change
- 2025-12-09 · <span class="tl-product tl-p25">**v0**</span> · [[Changes/v0/2025-12-09-v0-has-now-automatically-updated-every-react2shell-vulnerable-project-deployed-w|React2Shell Vulnerability Patch]] · Change
- 2025-12-03 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-12-03-add-infer-property-to-control-custom-agent-tool-visibility|Add infer property to control custom agent tool visibility]] · Change
- 2025-12-02 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-02-powershell-apply-patch-parsing-is-corrected-and-apply-patch-tests-now-cover-shel|PowerShell apply_patch parsing is corrected, and apply_patch tests now cover…]] · Change

**2025-11**

- 2025-11-21 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-11-21-2-agent-mode-changes-in-2-1|2 Agent Mode changes in 2.1]] · Digest
- 2025-11-20 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2025-11-20-agent-can-now-create-scratch-directories-if-no-workspaces-are-open|Agent can now create scratch directories if no workspaces are open]] · Change
- 2025-11-19 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-19-2-agent-mode-changes-in-rust-v0-59-0|2 Agent Mode changes in rust-v0.59.0]] · Digest
- 2025-11-13 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-11-13-feat-add-agents-md-support-by-saoudrizwan-in-https-github-com-cline-cline-pull-7|feat: add AGENTS.md support]] · Change
- 2025-11-13 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-13-6510-feat-shell-command-tool-29364f3a9|♯6510 — feat: shell_command tool (29364f3a9)]] · Change
- 2025-11-13 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-11-13-these-trigger-features-are-only-available-for-workflows-chatflow-agent-and-basic|These trigger features are only available for Workflows]] · Change
- 2025-11-12 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-12-2-agent-mode-changes-in-v0-14-0|2 Agent Mode changes in v0.14.0]] · Digest
- 2025-11-12 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-11-12-3-agent-mode-changes-in-v0-0-355|3 Agent Mode changes in v0.0.355]] · Digest
- 2025-11-07 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-07-3-agent-mode-changes-in-v0-13-0|3 Agent Mode changes in v0.13.0]] · Digest
- 2025-11-04 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-04-add-regression-tests-for-shell-command-parsing-by-cornmander-in-https-github-com|Add regression tests for shell command parsing]] · Change
- 2025-11-03 · <span class="tl-product tl-p10">**Gamma**</span> · [[Changes/Gamma/2025-11-03-now-when-you-edit-an-ai-generated-image-with-agent-those-changes-are-automatical|Now when you edit an AI-generated image with Agent, those changes are automatically…]] · Change
- 2025-11-03 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-11-03-custom-agents-with-special-characters-in-filenames-no-longer-fail|Custom agents with special characters in filenames no longer fail]] · Change

**2025-10**

- 2025-10-30 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-30-3-agent-mode-changes-in-rust-v0-52-0|3 Agent Mode changes in rust-v0.52.0]] · Digest
- 2025-10-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-10-29-improved-agent-harness|Improved Agent Harness]] · Change
- 2025-10-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-10-29-background-agents-have-been-renamed-to-cloud-agents|Background Agents have been renamed to Cloud Agents]] · Change
- 2025-10-29 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-29-chore-subagents-remove-legacy-subagent-code-by-abhipatel12-in-https-github-com-g|chore(subagents): Remove legacy subagent code]] · Change
- 2025-10-28 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-28-2-agent-mode-changes-in-v0-0-353|2 Agent Mode changes in v0.0.353]] · Digest
- 2025-10-23 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-23-2-agent-mode-changes-in-rust-v0-48-0|2 Agent Mode changes in rust-v0.48.0]] · Digest
- 2025-10-23 · <span class="tl-product tl-p24">**Windsurf**</span> · [[Changes/Windsurf/2025-10-23-support-and-fixes-for-agents-md|Support and fixes for AGENTS.md]] · Change
- 2025-10-22 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-10-22-4-agent-mode-changes-in-1-9-2|4 Agent Mode changes in 1.9.2]] · Digest
- 2025-10-22 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-22-feat-core-add-telemetry-for-subagent-execution-by-abhipatel12-in-https-github-co|feat(core): add telemetry for subagent execution]] · Change
- 2025-10-17 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-17-agent-override-file-5215|Agent override file (♯5215)]] · Change
- 2025-10-16 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-10-16-2-agent-mode-changes-in-v3-33-0|2 Agent Mode changes in v3.33.0]] · Digest
- 2025-10-15 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-15-3-agent-mode-changes-in-v0-9-0|3 Agent Mode changes in v0.9.0]] · Digest
- 2025-10-07 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-07-2-agent-mode-changes-in-v0-8-0|2 Agent Mode changes in v0.8.0]] · Digest
- 2025-10-03 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-03-5-agent-mode-changes-in-rust-v0-44-0|5 Agent Mode changes in rust-v0.44.0]] · Digest
- 2025-10-01 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-01-improved-the-experience-of-writing-prompts-while-the-agent-is-running-up-down-ar|Improved the experience of writing prompts while the agent is running -- up/down…]] · Change

**2025-09**

- 2025-09-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-09-29-6-agent-mode-changes-in-1-7|6 Agent Mode changes in 1.7]] · Digest
- 2025-09-29 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-09-29-2-agent-mode-changes-in-1-9-1|2 Agent Mode changes in 1.9.1]] · Digest
- 2025-09-18 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-18-2-agent-mode-changes-in-rust-v0-39-0|2 Agent Mode changes in rust-v0.39.0]] · Digest
- 2025-09-17 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-17-feat-core-only-summarize-long-tool-output-for-shell-command-by-sandytao520-in-ht|feat(core): Only summarize long tool output for shell command]] · Change
- 2025-09-12 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-09-12-3-agent-mode-changes-in-1-6|3 Agent Mode changes in 1.6]] · Digest
- 2025-09-10 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-10-3436-make-user-agent-optional-3436|♯3436 Make user_agent optional (♯3436)]] · Change
- 2025-09-09 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-09-09-2-agent-mode-changes-in-0-56-0|2 Agent Mode changes in 0.56.0]] · Digest
- 2025-09-05 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-05-3-agent-mode-changes-in-rust-v0-30-0|3 Agent Mode changes in rust-v0.30.0]] · Digest
- 2025-09-04 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-04-feat-subagent-enable-incremental-output-streaming-by-allenhutchison-in-https-git|feat(subagent): Enable incremental output streaming]] · Change
- 2025-09-03 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-03-3089-docs-update-link-to-https-agents-md|♯3089 Docs: update link to (source link)]] · Change
- 2025-09-02 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-02-4-agent-mode-changes-in-rust-v0-28-0|4 Agent Mode changes in rust-v0.28.0]] · Digest

**2025-08**

- 2025-08-29 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-29-2848-chore-try-to-make-it-easier-to-debug-the-flakiness-of-test-shell-command-ap|♯2848 chore: try to make it easier to debug the flakiness…]] · Change
- 2025-08-29 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-29-2-agent-mode-changes-in-rust-v0-27-0|2 Agent Mode changes in rust-v0.27.0]] · Digest
- 2025-08-27 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-08-27-5-agent-mode-changes-in-1-8-0|5 Agent Mode changes in 1.8.0]] · Digest
- 2025-08-26 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-26-5-agent-mode-changes-in-rust-v0-24-0|5 Agent Mode changes in rust-v0.24.0]] · Digest
- 2025-08-21 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-08-21-adding-task-progress-param-to-the-summarize-task-tool-call-by-0xtoshii-in-https|adding task_progress param to the summarize task tool call]] · Change
- 2025-08-20 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-08-20-added-a-new-feedback-reason-the-agent-didn-t-finish-the-job-by-xingyaoww-in-http|Added a new feedback reason: "The agent didn't finish the job"]] · Change
- 2025-08-14 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-14-7-agent-mode-changes-in-v0-1-21|7 Agent Mode changes in v0.1.21]] · Digest
- 2025-08-13 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-08-13-enhanced-the-cli-interface-by-adding-proper-markdown-rendering-for-agent-message|Enhanced the CLI interface by adding proper markdown rendering for agent messages…]] · Change
- 2025-08-12 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-12-feat-agent-introduce-foundational-subagent-architecture-by-abhipatel12-in-https|feat(agent): Introduce Foundational Subagent Architecture]] · Change
- 2025-08-06 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-08-06-improved-agent-tools-488891|Improved Agent tools]] · Change
- 2025-08-06 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-08-06-faster-background-agent-startup|Faster Background Agent startup]] · Change
- 2025-08-06 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-06-6-agent-mode-changes-in-v0-1-18|6 Agent Mode changes in v0.1.18]] · Digest
- 2025-08-05 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-05-6-agent-mode-changes-in-v0-1-17|6 Agent Mode changes in v0.1.17]] · Digest
- 2025-08-02 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-02-6-agent-mode-changes-in-v0-1-16|6 Agent Mode changes in v0.1.16]] · Digest

**2025-07**

- 2025-07-31 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-07-31-improved-the-resolver-summary-generation-by-instructing-the-agent-to-focus-only|Improved the resolver summary generation by instructing the agent to focus only…]] · Change
- 2025-07-30 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-30-6-agent-mode-changes-in-v0-1-15|6 Agent Mode changes in v0.1.15]] · Digest
- 2025-07-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-07-29-2-agent-mode-changes-in-1-3|2 Agent Mode changes in 1.3]] · Digest
- 2025-07-25 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-25-5-agent-mode-changes-in-v0-1-14|5 Agent Mode changes in v0.1.14]] · Digest
- 2025-07-24 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-07-24-2-agent-mode-changes-in-0-50-0|2 Agent Mode changes in 0.50.0]] · Digest
- 2025-07-23 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-07-23-2-agent-mode-changes-in-1-7-0|2 Agent Mode changes in 1.7.0]] · Digest
- 2025-07-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-22-2-agent-mode-changes-in-elevenlabs-updates-2025-07-22|2 Agent Mode changes in ElevenLabs updates — 2025-07-22]] · Digest
- 2025-07-19 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-07-19-https-github-com-openai-codex-pull-1589-changes-ctrl-d-so-it-only-exits-the-tui|(source link) changes ctrl-d so it only exits the TUI…]] · Change
- 2025-07-19 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-19-3-agent-mode-changes-in-v0-1-13|3 Agent Mode changes in v0.1.13]] · Digest
- 2025-07-10 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-07-10-feat-retain-llm-setting-for-agent-node-by-fdb02983rhy-in-https-github-com-langge|feat: Retain llm setting for agent node]] · Change
- 2025-07-03 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-07-03-2-agent-mode-changes-in-1-2|2 Agent Mode changes in 1.2]] · Digest

**2025-06**

- 2025-06-20 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-06-20-fixed-incorrect-tracking-for-cost-and-token-usage-for-main-agent-and-delegates-b|Fixed incorrect tracking for cost and token usage for main agent and delegates]] · Change
- 2025-06-12 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-06-12-improved-background-agent-reliability|Improved Background Agent reliability]] · Change
- 2025-06-11 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-06-11-4-agent-mode-changes-in-1-4-2|4 Agent Mode changes in 1.4.2]] · Digest
- 2025-06-10 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-06-10-ensured-prs-opened-by-agent-is-properly-tracked-in-conversation-metadata-by-malh|Ensured PRs opened by agent is properly tracked in conversation metadata]] · Change
- 2025-06-04 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-06-04-open-background-agent-control-panel-with-cmd-ctrl-e|Open Background Agent control panel with Cmd/Ctrl+E]] · Change

**2025-05**

- 2025-05-20 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-05-20-2-agent-mode-changes-in-0-39-0|2 Agent Mode changes in 0.39.0]] · Digest
- 2025-05-15 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-05-15-imagine-if-every-idea-could-become-an-ai-agent-with-dify-if-you-can-ask-it-you-c|Imagine if every idea could become an AI agent]] · Change
- 2025-05-12 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-05-12-added-the-ability-for-the-agent-to-save-browser-screenshots-as-image-files-by-xi|Added the ability for the agent to save browser screenshots as image files]] · Change
- 2025-05-01 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-05-01-added-support-for-agent-pause-and-resume-functionality-in-the-cli-by-pandukamudi|Added support for agent pause and resume functionality in the CLI]] · Change

**2025-04**

- 2025-04-24 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-04-24-improve-prompting-for-new-task-tool|Improve prompting for new task tool]] · Change
- 2025-04-23 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-04-23-3-agent-mode-changes-in-1-3-0|3 Agent Mode changes in 1.3.0]] · Digest
- 2025-04-23 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-04-23-improved-logic-to-prevent-agent-from-getting-stuck-by-rbren-in-https-github-com|Improved logic to prevent agent from getting stuck]] · Change
- 2025-04-10 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-04-10-prompt-agent-to-follow-existing-pr-template-when-create-new-pr-by-xingyaoww-in-h|Prompt agent to follow existing PR template when create new PR]] · Change
- 2025-04-09 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-04-09-add-new-create-new-task-tool-to-let-cline-start-a-new-task-autonomously|Add new 'Create New Task' tool to let Cline start a new task autonomously!]] · Change
- 2025-04-04 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-04-04-better-icons|Better icons]] · Change

**2025-03**

- 2025-03-18 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-03-18-feat-add-click-away-and-mounting-logic-to-agent-setting-component-by-fdb02983rhy|feat: add click-away and mounting logic to agent setting component]] · Change
- 2025-03-10 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-03-10-improve-agent-loop-tracking-by-rbren-in-https-github-com-all-hands-ai-openhands|Improve agent loop tracking]] · Change
- 2025-03-07 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-03-07-3-agent-mode-changes-in-0-28-0|3 Agent Mode changes in 0.28.0]] · Digest

**2025-02**

- 2025-02-28 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-02-28-we-ve-introduced-a-new-agent-node-in-workflow-where-the-agent-s-behavior-can-now|We've introduced a new Agent node in Workflow, where the agent's behavior can now…]] · Change
- 2025-02-21 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2025-02-21-improved-international-character-support-in-screenshots|Improved international character support in screenshots]] · Change
- 2025-02-19 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-02-19-agent-is-ready-agent-is-now-the-default-mode-bringing-a-more-powerful-and-unifie|Agent is ready: Agent is now the default mode, bringing a more powerful and unified…]] · Change
- 2025-02-19 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-02-19-agent-tool-limit-upon-reaching-the-25-tool-call-limit-you-can-press-continue-to|Agent tool limit]] · Change
- 2025-02-07 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-02-07-2-agent-mode-changes-in-0-15-3|2 Agent Mode changes in 0.15.3]] · Digest

**2025-01**

- 2025-01-23 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-01-23-agent-sees-recent-changes-the-agent-can-use-a-tool-to-see-your-recent-changes-it|Agent sees recent changes: The agent can use a tool to see your recent changes]] · Change
- 2025-01-23 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-01-23-cursor-rules-users-can-write-several-repository-level-rules-to-disk-in-the-curso|.cursor/rules: Users can write several repository-level rules to disk…]] · Change
- 2025-01-22 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-01-22-agent-log-formatting-tweaked-deepseek-s-api-response-handling-to-fix-format-issu|Agent Log Formatting]] · Change
- 2025-01-22 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-01-22-when-connecting-to-a-github-repo-the-agent-now-explicitly-knows-which-repo-was-c|When connecting to a GitHub repo, the agent now explicitly knows which repo…]] · Change
- 2025-01-07 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2025-01-07-added-ratelimiterror-status-on-ui-and-agent-state-by-rkat7-in-https-github-com-a|Added RateLimitError status on UI and Agent state]] · Change

</details>

</details>

<details class="disclosure">
<summary>2024 · 43 entries (Aider 2 · Cursor 2 · Dify 13 · ElevenLabs 2 · Ollama 1 · Open WebUI 3 · OpenHands 13 · Replit 7)</summary>

**2024-12**

- 2024-12-27 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2024-12-27-agent-improvements|Agent improvements]] · Launch
- 2024-12-27 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2024-12-27-database-polish|Database polish]] · Launch
- 2024-12-20 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2024-12-20-database-notifications|Database notifications]] · Launch
- 2024-12-20 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2024-12-20-recommendation-system|Recommendation system]] · Launch
- 2024-12-13 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2024-12-13-usage-updates-you-ll-love|Usage Updates You’ll Love]] · Policy
- 2024-12-13 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2024-12-13-rapid-scraping-screenshots|Rapid Scraping / Screenshots]] · Launch

**2024-11**

- 2024-11-29 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2024-11-29-api|API]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 36 (Aider 2 · Cursor 2 · Dify 13 · ElevenLabs 1 · Ollama 1 · Open WebUI 3 · OpenHands 13 · Replit 1)</summary>

**2024-12**

- 2024-12-25 · <span class="tl-product tl-p18">**Open WebUI**</span> · [[Changes/Open WebUI/2024-12-25-true-asynchronous-chat-support-create-chats-navigate-away-and-return-anytime-wit|💬 True Asynchronous Chat Support]] · Change
- 2024-12-19 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2024-12-19-agent-gets-stuck-in-closing-and-server-won-t-die-by-tofarr-in-https-github-com-a|Agent gets stuck in closing and server won't die]] · Change
- 2024-12-17 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2024-12-17-let-user-continue-when-the-agent-gets-stuck-in-a-loop-ui-only-by-enyst-in-https|Let user continue when the agent gets stuck in a loop (UI-only)]] · Change
- 2024-12-13 · <span class="tl-product tl-p22">**Replit**</span> · [[Changes/Replit/2024-12-13-2-agent-mode-changes-in-replit-updates-2024-12-13|2 Agent Mode changes in Replit updates — 2024-12-13]] · Digest
- 2024-12-10 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-12-10-updated-shell-command-prompt|Updated shell command prompt]] · Change
- 2024-12-06 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2024-12-06-2-agent-mode-changes-in-0-15-1|2 Agent Mode changes in 0.15.1]] · Digest

**2024-11**

- 2024-11-25 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-11-25-for-instance-you-can-upload-a-pdf-report-and-let-the-agent-automatically-analyze|For instance, you can upload a PDF report and let the Agent automatically analyze…]] · Change
- 2024-11-19 · <span class="tl-product tl-p18">**Open WebUI**</span> · [[Changes/Open WebUI/2024-11-19-agentic-retrieval-improve-rag-accuracy-via-smart-pre-processing-of-chat-history|🗂️ Agentic Retrieval]] · Change
- 2024-11-08 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2024-11-08-2-agent-mode-changes-in-0-13-0|2 Agent Mode changes in 0.13.0]] · Digest

**2024-10**

- 2024-10-22 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2024-10-22-improvements-to-agent-editing-using-llm-by-xingyaoww-in-https-github-com-all-han|Improvements to Agent Editing using LLM]] · Change
- 2024-10-14 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-10-14-external-knowledge-and-retrievals-addressing-issues-in-agent-retrieval-and-entry|External Knowledge and Retrievals: Addressing issues in agent retrieval…]] · Change
- 2024-10-13 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2024-10-13-agents-platform-beta-agents-platform-is-now-in-beta|Agents Platform Beta: Agents Platform is now in beta]] · Change

**2024-09**

- 2024-09-30 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-09-30-2-agent-mode-changes-in-0-9-0|2 Agent Mode changes in 0.9.0]] · Digest
- 2024-09-10 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-09-10-refactor-api-core-improve-type-hints-and-apply-ruff-formatter-in-agent-runner-an|refactor(api/core): Improve type hints and apply ruff formatter in agent runner…]] · Change
- 2024-09-04 · <span class="tl-product tl-p18">**Open WebUI**</span> · [[Changes/Open WebUI/2024-09-04-user-agent-in-comfyui-added-default-headers-in-comfyui-to-fix-access-issues-impr|🛠️ User Agent in ComfyUI]] · Change
- 2024-09-04 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2024-09-04-files-display-updated-content-after-agent-edit-by-amanape-in-https-github-com-al|Files display updated content after agent edit]] · Change

**2024-08**

- 2024-08-29 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2024-08-29-specialize-codeact-into-micro-agents-by-xingyaoww-in-https-github-com-all-hands|Specialize CodeAct into micro agents]] · Change
- 2024-08-27 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-08-27-improved-shell-command-prompting|Improved shell command prompting]] · Change
- 2024-08-23 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2024-08-23-4-agent-mode-changes-in-0-9-0|4 Agent Mode changes in 0.9.0]] · Digest
- 2024-08-14 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-08-14-feat-agent-app-support-generate-prompt-by-iamjoel-in-https-github-com-langgenius|feat: agent app support generate prompt]] · Change
- 2024-08-02 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2024-08-02-concurrent-composers-support-composer-control-panel-and-various-bug-fixes-such-a|Concurrent composers support, composer control panel, and various bug fixes such…]] · Change
- 2024-08-01 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2024-08-01-2-agent-mode-changes-in-0-8-3|2 Agent Mode changes in 0.8.3]] · Digest

**2024-07**

- 2024-07-27 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2024-07-27-4-agent-mode-changes-in-0-8-2|4 Agent Mode changes in 0.8.2]] · Digest
- 2024-07-13 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2024-07-13-3-agent-mode-changes-in-0-8-0|3 Agent Mode changes in 0.8.0]] · Digest
- 2024-07-05 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2024-07-05-2-agent-mode-changes-in-0-7-1|2 Agent Mode changes in 0.7.1]] · Digest
- 2024-07-02 · <span class="tl-product tl-p17">**Ollama**</span> · [[Changes/Ollama/2024-07-02-2-agent-mode-changes-in-v0-2-0|2 Agent Mode changes in v0.2.0]] · Digest

**2024-06**

- 2024-06-29 · <span class="tl-product tl-p21">**OpenHands**</span> · [[Changes/OpenHands/2024-06-29-3-agent-mode-changes-in-0-7-0|3 Agent Mode changes in 0.7.0]] · Digest

**2024-04**

- 2024-04-22 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-04-22-2-agent-mode-changes-in-0-6-4|2 Agent Mode changes in 0.6.4]] · Digest
- 2024-04-11 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-04-11-4-agent-mode-changes-in-0-6-2|4 Agent Mode changes in 0.6.2]] · Digest
- 2024-04-08 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-04-08-we-also-moved-the-agent-data-within-the-database-execute-the-below-script-to-com|We also moved the agent data within the database, Execute the below…]] · Change

**2024-03**

- 2024-03-04 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-03-04-refactor-remove-unused-codes-move-core-agent-module-into-dataset-retrieval-featu|refactor: remove unused codes, move core/agent module into dataset retrieval feature]] · Change

**2024-02**

- 2024-02-28 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-02-28-2-agent-mode-changes-in-0-5-7|2 Agent Mode changes in 0.5.7]] · Digest
- 2024-02-15 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2024-02-15-interpreter-mode-we-ve-made-some-big-improvements-to-the-backend-powering-interp|Interpreter Mode: We've made some big improvements to the backend powering…]] · Change

**2024-01**

- 2024-01-25 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-01-25-feat-create-app-show-agent-type-tip-by-iamjoel-in-https-github-com-langgenius-di|feat: create app show agent type tip]] · Change
- 2024-01-24 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-01-24-4-agent-mode-changes-in-0-5-0|4 Agent Mode changes in 0.5.0]] · Digest
- 2024-01-02 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-01-02-expanded-inference-support-xorbit-inference-now-includes-chat-mode-models-and-th|Expanded Inference Support: Xorbit Inference now includes chat mode models…]] · Change

</details>

</details>

<details class="disclosure">
<summary>2023 · 6 entries (Cursor 3 · Dify 3)</summary>

**2023-08**

- 2023-08-23 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2023-08-23-feat-optimize-error-record-in-agent-by-takatost-in-https-github-com-langgenius-d|feat: optimize error record in agent]] · Change

**2023-07**

- 2023-07-27 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2023-07-27-3-agent-mode-changes-in-0-3-11|3 Agent Mode changes in 0.3.11]] · Digest
- 2023-07-18 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2023-07-18-feat-hide-password-setting-and-invitation-link-in-cloud-version-by-jzongkvo-in-h|Feat: hide password setting and invitation link in cloud version]] · Change
- 2023-07-10 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-07-10-this-nightly-build-comes-with-experimental-interface-agent-support|This nightly build comes with experimental interface agent support!]] · Change
- 2023-07-10 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-07-10-the-goal-you-write-an-interface-specification-and-an-agent-writes-both-the-tests|The goal: you write an interface specification, and an agent writes both the tests…]] · Change
- 2023-07-06 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]] · Change

</details>

</div>
<!-- chronolog:end -->