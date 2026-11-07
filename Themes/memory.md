---
created: '2023-07-20'
date: '2026-11-06'
description: 'Research question: what do the tracked products remember between sessions,
  and how do users control it?'
machine_hash: 14a5b93dec898a3995d6865216c00183e427dc1dd22a37f235f7801e844b8cfc
modified: '2026-11-06'
products_involved:
- AnythingLLM
- ChatGPT
- Claude
- Claude Code
- Cline
- Codex CLI
- Cursor
- Descript
- Devin
- Dify
- ElevenLabs
- Gemini
- Gemini CLI
- GitHub Copilot CLI
- Google Antigravity
- HeyGen
- Kimi Code
- Krea
- LM Studio
- Lovable
- Microsoft 365 Copilot
- Midjourney
- Notion
- Open WebUI
- OpenClaw
- OpenCode
- OpenHands
- Qoder
- Raycast
- Replit
- Superwhisper
- Windsurf
- v0
publication: active
status: official
tags:
- theme
- moc
theme: memory
title: Memory and Personalization
---

<!-- chronolog:begin region="header" -->
# Memory and Personalization

360 tracked changes across AnythingLLM, ChatGPT, Claude, Claude Code, Cline, Codex CLI, Cursor, Descript, Devin, Dify, ElevenLabs, Gemini, Gemini CLI, GitHub Copilot CLI, Google Antigravity, HeyGen, Kimi Code, Krea, LM Studio, Lovable, Microsoft 365 Copilot, Midjourney, Notion, Open WebUI, OpenClaw, OpenCode, OpenHands, Qoder, Raycast, Replit, Superwhisper, Windsurf and v0 · 2023-07-20 → 2026-11-06 · OpenClaw averages 18.4 cards per release, Microsoft 365 Copilot 11.2, ElevenLabs 8.1, Codex CLI 8.0, Open WebUI 7.6, Gemini CLI 7.5, Devin 7.5, AnythingLLM 7.3, Dify 7.2, Claude Code 7.0, GitHub Copilot CLI 6.3, OpenCode 6.0, HeyGen 5.3, Raycast 5.2, Google Antigravity 5.0, Replit 4.9, Kimi Code 4.5, Qoder 4.2, Cursor 4.0, Lovable 3.9, OpenHands 3.8, Notion 3.6, LM Studio 3.3, Cline 3.0, Krea 3.0, Descript 2.9, v0 2.9, Midjourney 2.7, Windsurf 2.6, Superwhisper 2.1, ChatGPT 1.7, Gemini 1.5, Claude 1.3
<!-- chronolog:end -->

## Research summary
<!-- chronolog:begin region="narrative" -->
**Research question: what do the tracked products remember between sessions, and how do users control it?**

ChatGPT's [2023-07-20 custom instructions beta](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#custom-instructions-are-rolling-out-in-beta) ([[Releases/ChatGPT/chatgpt-2023-07-20-custom-instructions-are-rolling-out-in-beta-bf9360b9|archived]]) lets users set preferences once to steer future conversations. The [2024-02-13 memory test](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#memory-and-new-controls-for-chatgpt) ([[Releases/ChatGPT/chatgpt-2024-02-13-memory-and-new-controls-for-chatgpt-2fd43ded|archived]]) remembers things discussed across all chats; users can tell ChatGPT what to remember or forget, ask what it remembers, or turn memory off. The [2025-05-08 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#enhanced-memory-in-chatgpt-including-eu-on-pluspro) ([[Releases/ChatGPT/chatgpt-2025-05-08-enhanced-memory-in-chatgpt-including-eu-on-plus-pro-b6107d35|archived]]) rolls out enhanced memory, enabled through the Reference Chat History setting and off by default, to all Plus and Pro users including the EU; the [2025-08-22 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#project-only-memory) ([[Releases/ChatGPT/chatgpt-2025-08-22-project-only-memory-3424a221|archived]]) adds project-only memory, which keeps a project's context inside that project; and the [2025-10-15 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#chatgpt-can-now-automatically-manage-saved-memories-so-its-even-better-at-remembering-whats-important-to-you) ([[Releases/ChatGPT/chatgpt-2025-10-15-chatgpt-can-now-automatically-manage-saved-memories-so-it-s-even-00bd082a|archived]]) has ChatGPT manage saved memories automatically by keeping the most relevant details prioritized.

Cursor's [1.0 release on 2025-06-04](https://cursor.com/changelog/1-0) ([[Releases/Cursor/cursor-2025-06-04-1-0-https-cursor-com-changelog-1-0-237767ca|archived]]) introduces Memories as a beta: Cursor remembers facts from conversations, stored per project for each individual. The [2025-07-03 release](https://cursor.com/changelog/1-2) ([[Releases/Cursor/cursor-2025-07-03-1-2-https-cursor-com-changelog-1-2-27872f5d|archived]]) makes Memories generally available with user approval for background-generated memories, and the [2026-03-05 Automations release](https://cursor.com/changelog/03-05-26) ([[Releases/Cursor/cursor-2026-03-05-automations-https-cursor-com-changelog-03-05-26-be367422|archived]]) gives automation agents a memory tool that learns from past runs.

Claude Code's [v2.1.32 on 2026-02-05](https://github.com/anthropics/claude-code/releases/tag/v2.1.32) ([[Releases/Claude Code/claude-code-2026-02-05-v2-1-32-github-283457817-0910feb0|archived]]) has Claude record and recall memories automatically as it works, [v2.1.33 on 2026-02-06](https://github.com/anthropics/claude-code/releases/tag/v2.1.33) ([[Releases/Claude Code/claude-code-2026-02-06-v2-1-33-github-283581096-0f5b01a0|archived]]) adds a `memory` frontmatter field that gives agents persistent memory at user, project or local scope, and [v2.1.59 on 2026-02-26](https://github.com/anthropics/claude-code/releases/tag/v2.1.59) ([[Releases/Claude Code/claude-code-2026-02-26-v2-1-59-github-290659389-9e2d6217|archived]]) saves useful context to auto-memory, managed with `/memory`.

**Uncertainty and scope:** this editorial summary covers ChatGPT, Claude Code and Cursor; the timeline includes all tracked products, Claude Code coverage starts on 2025-12-19 and ChatGPT memory rollouts vary by plan and region; the theme also collects personalization settings and unrelated uses of “memory” such as RAM use, and the announcements do not measure what a product retains or how reliably it recalls it.
<!-- chronolog:end -->

## Key moments
<!-- chronolog:begin region="moments" -->
Selected automatically from launches and standalone announcements.

| Quarter | AnythingLLM | ChatGPT | Claude | Claude Code | Cline | Codex CLI | Cursor | Descript | Devin | Dify | ElevenLabs | Gemini | Gemini CLI | GitHub Copilot CLI | Google Antigravity | HeyGen | Kimi Code | Krea | LM Studio | Lovable | Microsoft 365 Copilot | Midjourney | Notion | Open WebUI | OpenClaw | OpenCode | OpenHands | Qoder | Raycast | Replit | Superwhisper | Windsurf | v0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **First in archive** | <time datetime="2025-08-15">2025-08-15</time> [[Changes/AnythingLLM/2025-08-15-well-now-we-have-the-best-of-both-worlds-documents-are-scoped-to-a-workspace-thr\|Well, now we have the best of both worlds]] | <time datetime="2023-07-20">2023-07-20</time> [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c\|Custom instructions are rolling out in beta]] | <time datetime="2025-09-11">2025-09-11</time> [[Changes/Claude/2025-09-11-claude-s-memory-on-team-plans-and-incognito-chats-for-free-pro-max-and-team-plan\|Claude’s memory on Team plans and incognito chats for free, Pro, Max, and Team plans]] | <time datetime="2026-02-05">2026-02-05</time> [[Changes/Claude Code/2026-02-05-claude-now-automatically-records-and-recalls-memories-as-it-works\|Claude now automatically records and recalls memories as it works]] | <time datetime="2024-07-28">2024-07-28</time> [[Changes/Cline/2024-07-28-quality-of-life-improvements-like-markdown-rendering-memory-optimizations-better\|Quality of life improvements like markdown rendering, memory optimizations, better…]] | <time datetime="2025-09-23">2025-09-23</time> [[Changes/Codex CLI/2025-09-23-new-review-commands-review-specific-commit-against-a-base-branch-or-custom-instr\|New /review commands…]] | <time datetime="2025-02-19">2025-02-19</time> [[Changes/Cursor/2025-02-19-0-46-9-memory-and-performances-fixes-composer-chat-remembers-your-last-mode-sele\|0.46.9: Memory and performances fixes, composer/chat remembers your last mode…]] | <time datetime="2023-12-05">2023-12-05</time> [[Changes/Descript/2023-12-05-command-e-https-help-descript-com-hc-en-us-articles-10255582172173-keyboard-shor\|Command…]] | <time datetime="2026-09-30">2026-09-30</time> [[Changes/Devin/2026-09-30-context-tab\|Context Tab]] | <time datetime="2024-01-05">2024-01-05</time> [[Changes/Dify/2024-01-05-feat-optimize-memory-invoke-error-output-by-takatost-in-https-github-com-langgen\|feat: optimize memory & invoke error output]] | <time datetime="2025-07-14">2025-07-14</time> [[Changes/ElevenLabs/2025-07-14-elevencreative-studio\|ElevenCreative Studio]] | <time datetime="2026-03-26">2026-03-26</time> [[Changes/Gemini/2026-03-26-make-the-switch-seamlessly-bring-your-ai-memories-and-chat-history-to-gemini\|Make the switch: Seamlessly bring your AI memories and chat history to Gemini]] | <time datetime="2025-07-25">2025-07-25</time> [[Changes/Gemini CLI/2025-07-25-feat-memory-make-directory-search-limit-on-memory-discovery-configurable-with-se\|feat(memory): make directory search limit on memory discovery configurable…]] | <time datetime="2026-01-16">2026-01-16</time> [[Changes/GitHub Copilot CLI/2026-01-16-inject-repo-memories-in-the-prompt-and-add-memory-storage-tool-to-remember-facts\|Inject repo memories in the prompt and add memory storage tool to remember facts…]] | <time datetime="2026-09-15">2026-09-15</time> [[Changes/Google Antigravity/2026-09-15-conversations-with-very-long-histories-now-load-faster-and-use-less-memory\|Conversations with very long histories now load faster and use less memory]] | <time datetime="2026-06-02">2026-06-02</time> [[Changes/HeyGen/2026-06-02-personal-settings-contains-settings-that-apply-only-to-the-individual-user-inclu\|Personal Settings contains settings that apply only to the individual user…]] | <time datetime="2026-06-24">2026-06-24</time> [[Changes/Kimi Code/2026-06-24-read-large-text-files-in-bounded-memory-and-read-tail-lines-without-scanning-who\|Read large text files in bounded memory and read tail lines without scanning whole files]] | <time datetime="2026-10-20">2026-10-20</time> [[Changes/Krea/2026-10-20-smarter-agent-upgrade-suggestions-and-edit-model-memory\|Smarter Agent upgrade suggestions and Edit model memory]] | <time datetime="2025-03-27">2025-03-27</time> [[Changes/LM Studio/2025-03-27-2-memory-and-personalization-changes-in-lm-studio-0-3-14\|2 Memory and Personalization changes in LM Studio 0.3.14]] | <time datetime="2026-05-18">2026-05-18</time> [[Changes/Lovable/2026-05-18-security-memory\|Security memory]] | <time datetime="2026-01-27">2026-01-27</time> [[Changes/Microsoft 365 Copilot/2026-01-27-improve-relevance-and-personalization-by-connecting-user-identities-across-data\|Improve relevance and personalization by connecting user identities across data…]] | <time datetime="2024-03-13">2024-03-13</time> [[Changes/Midjourney/2024-03-13-our-team-is-also-working-on-new-special-features-like-model-personalization-that\|Our team is also working on new special features like model personalization…]] | <time datetime="2024-06-18">2024-06-18</time> [[Changes/Notion/2024-06-18-unlock-your-company-s-memory\|Unlock your company’s memory]] | <time datetime="2024-05-19">2024-05-19</time> [[Changes/Open WebUI/2024-05-19-experimental-memory-feature-manually-input-personal-information-you-want-llms-to\|🧠 Experimental Memory Feature]] | <time datetime="2026-06-30">2026-06-30</time> [[Changes/OpenClaw/2026-06-30-26-memory-and-personalization-changes-in-v2026-6-11\|26 Memory and Personalization changes in v2026.6.11]] | <time datetime="2026-01-28">2026-01-28</time> [[Changes/OpenCode/2026-01-28-2-memory-and-personalization-changes-in-v1-1-37\|2 Memory and Personalization changes in v1.1.37]] | <time datetime="2024-07-05">2024-07-05</time> [[Changes/OpenHands/2024-07-05-ci-for-colima-modify-cpu-count-and-memory-by-smartmanoj-in-https-github-com-open\|CI: For colima, modify CPU count and memory]] | <time datetime="2026-10-14">2026-10-14</time> [[Changes/Qoder/2026-10-14-remote-ssh-select-git-branches-in-remote-sessions-and-import-qoder-ide-task-hist\|Remote SSH: Select Git branches in remote sessions and import Qoder IDE task…]] | <time datetime="2026-03-27">2026-03-27</time> [[Changes/Raycast/2026-03-27-ai-chat-added-memory-to-make-chats-more-personal\|AI Chat: Added memory to make chats more personal]] | <time datetime="2026-02-20">2026-02-20</time> [[Changes/Replit/2026-02-20-background-memory-compression\|Background memory compression]] | <time datetime="2025-10-24">2025-10-24</time> [[Changes/Superwhisper/2025-10-24-record-from-system-audio-now-uses-less-data-memory\|Record from system audio now uses less data & memory]] | <time datetime="2025-04-02">2025-04-02</time> [[Changes/Windsurf/2025-04-02-improvements-to-memories\|Improvements to Memories]] | <time datetime="2025-10-06">2025-10-06</time> [[Changes/v0/2025-10-06-custom-instructions-are-now-available-in-v0-use-preset-instructions-like-be-conc\|Custom Instructions]] |
| 2026 Q4 | · | · | · | · | · | · | · | · | <time datetime="2026-10-19">2026-10-19</time> [[Changes/Devin/2026-10-19-turn-off-nightly-memory-dreaming\|Turn Off Nightly Memory Dreaming]]<br><time datetime="2026-10-09">2026-10-09</time> [[Changes/Devin/2026-10-09-memory-and-dreaming\|Memory and dreaming]] | · | · | · | · | · | · | · | · | <time datetime="2026-10-20">2026-10-20</time> [[Changes/Krea/2026-10-20-smarter-agent-upgrade-suggestions-and-edit-model-memory\|Smarter Agent upgrade suggestions and Edit model memory]] | · | <time datetime="2026-11-04">2026-11-04</time> [[Changes/Lovable/2026-11-04-dreaming-lovable-keeps-its-memory-up-to-date\|Dreaming: Lovable keeps its memory up to date]]<br><time datetime="2026-10-30">2026-10-30</time> [[Changes/Lovable/2026-10-30-lovable-remembers-what-you-tell-it\|Lovable remembers what you tell it]] | · | <time datetime="2026-10-08">2026-10-08</time> [[Changes/Midjourney/2026-10-08-organization-improvements\|ORGANIZATION IMPROVEMENTS]] | · | · | · | · | · | · | <time datetime="2026-10-12">2026-10-12</time> [[Changes/Raycast/2026-10-12-cloud-sync-v2\|Cloud Sync v2]] | · | · | · | · |
| 2026 Q3 | · | <time datetime="2026-08-14">2026-08-14</time> [[Changes/ChatGPT/2026-08-14-you-can-now-change-a-project-s-memory-setting-after-you-create-it-open-the-proje-b36ffe\|Edit memory settings for existing projects]] | <time datetime="2026-08-25">2026-08-25</time> [[Changes/Claude/2026-08-25-memory-in-claude-cowork-editable-topics-and-a-sensitive-topics-setting\|Memory in Claude Cowork, editable topics, and a sensitive topics setting]]<br><time datetime="2026-07-09">2026-07-09</time> [[Changes/Claude/2026-07-09-a-new-way-to-reflect-with-claude\|A new way to reflect with Claude]] | · | · | · | · | · | <time datetime="2026-09-30">2026-09-30</time> [[Changes/Devin/2026-09-30-context-tab\|Context Tab]] | · | · | · | · | · | · | · | · | · | · | · | · | <time datetime="2026-08-21">2026-08-21</time> [[Changes/Midjourney/2026-08-21-settings\|Settings]]<br><time datetime="2026-07-24">2026-07-24</time> [[Changes/Midjourney/2026-07-24-we-are-launching-our-v8-2-image-model-today-this-update-focuses-on-aesthetics-an\|Midjourney launches our V8.2 image model today]] | · | · | · | · | · | archive begins <time datetime="2026-08-27">2026-08-27</time> | <time datetime="2026-09-11">2026-09-11</time> [[Changes/Raycast/2026-09-11-projects-6239fd\|Projects]]<br><time datetime="2026-09-11">2026-09-11</time> [[Changes/Raycast/2026-09-11-projects\|Projects]] | · | · | <time datetime="2026-07-29">2026-07-29</time> [[Changes/Windsurf/2026-07-29-devin-local-8ab9ef\|Devin Local]]<br><time datetime="2026-07-29">2026-07-29</time> [[Changes/Windsurf/2026-07-29-devin-local\|Devin Local]] | · |
| 2026 Q2 | · | <time datetime="2026-06-12">2026-06-12</time> [[Changes/ChatGPT/2026-06-12-you-can-now-delete-the-memories-shown-on-your-memory-summary-page-and-turn-memor-f16782\|Additional controls for memory summary]] | · | · | · | · | <time datetime="2026-06-18">2026-06-18</time> [[Changes/Cursor/2026-06-18-you-can-now-delete-memory-files-in-the-ui-or-prompt-your-automation-to-delete-ou\|Delete memory files in the UI, or prompt your automation to delete outdated memories…]] | · | · | · | <time datetime="2026-04-20">2026-04-20</time> [[Changes/ElevenLabs/2026-04-20-elevenagents-d2ebb2\|ElevenAgents]] | · | · | · | · | · | archive begins <time datetime="2026-05-26">2026-05-26</time> | archive begins <time datetime="2026-04-14">2026-04-14</time> | · | <time datetime="2026-05-18">2026-05-18</time> [[Changes/Lovable/2026-05-18-security-memory\|Security memory]] | · | · | · | · | archive begins <time datetime="2026-06-30">2026-06-30</time> | · | · | <span class="not-archived">not archived</span> | · | · | · | · | · |
| 2026 Q1 | · | · | · | · | · | · | · | · | · | · | · | <time datetime="2026-03-26">2026-03-26</time> [[Changes/Gemini/2026-03-26-make-the-switch-seamlessly-bring-your-ai-memories-and-chat-history-to-gemini\|Make the switch: Seamlessly bring your AI memories and chat history to Gemini]] | · | · | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | · | <time datetime="2026-01-27">2026-01-27</time> [[Changes/Microsoft 365 Copilot/2026-01-27-improve-relevance-and-personalization-by-connecting-user-identities-across-data\|Improve relevance and personalization by connecting user identities across data…]] | · | <time datetime="2026-01-20">2026-01-20</time> [[Changes/Notion/2026-01-20-new-models-same-memory\|New models, same memory]] | · | <span class="not-archived">not archived</span> | · | · | <span class="not-archived">not archived</span> | · | <time datetime="2026-02-20">2026-02-20</time> [[Changes/Replit/2026-02-20-background-memory-compression\|Background memory compression]] | · | · | · |
| 2025 Q4 | · | · | · | archive begins <time datetime="2025-12-19">2025-12-19</time> | · | · | · | · | · | · | · | · | · | · | archive begins <time datetime="2025-11-18">2025-11-18</time> | archive begins <time datetime="2025-11-29">2025-11-29</time> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | · | <span class="not-archived">not archived</span> | · | · | · | <span class="not-archived">not archived</span> | archive begins <time datetime="2025-12-19">2025-12-19</time> | · | <span class="not-archived">not archived</span> | · | · | · | · | <time datetime="2025-10-06">2025-10-06</time> [[Changes/v0/2025-10-06-custom-instructions-are-now-available-in-v0-use-preset-instructions-like-be-conc\|Custom Instructions]] |
| 2025 Q3 | · | · | archive begins <time datetime="2025-08-01">2025-08-01</time> | <span class="not-archived">not archived</span> | · | · | <time datetime="2025-07-03">2025-07-03</time> [[Changes/Cursor/2025-07-03-memories-is-now-ga-since-1-0-we-ve-improved-memory-generation-quality-added-in-e\|Memories (now GA)]] | · | · | · | <time datetime="2025-07-14">2025-07-14</time> [[Changes/ElevenLabs/2025-07-14-elevencreative-studio\|ElevenCreative Studio]] | · | · | archive begins <time datetime="2025-09-26">2025-09-26</time> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | · | <span class="not-archived">not archived</span> | · | <time datetime="2025-09-18">2025-09-18</time> [[Changes/Notion/2025-09-18-personalize-your-agent-s-instructions-and-memory\|Personalize your Agent’s instructions and memory]] | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | · | · | · | · | <span class="not-archived">not archived</span> |
| 2024 Q3 → 2025 Q2 | archive begins <time datetime="2024-07-26">2024-07-26</time> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-07-28">2024-07-28</time> | archive begins <time datetime="2025-06-30">2025-06-30</time> | · | · | · | · | archive begins <time datetime="2024-10-13">2024-10-13</time> | · | archive begins <time datetime="2025-06-28">2025-06-28</time> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-10-22">2024-10-22</time> | archive begins <time datetime="2024-12-03">2024-12-03</time> | <span class="not-archived">not archived</span> | · | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2024-12-13">2024-12-13</time> | · | archive begins <time datetime="2025-04-02">2025-04-02</time> | <span class="not-archived">not archived</span> |
| 2024 Q2 | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | · | archive begins <time datetime="2024-05-13">2024-05-13</time> | <time datetime="2024-04-25">2024-04-25</time> [[Changes/Dify/2024-04-25-you-can-now-enable-memory-in-the-llm-node-within-your-chatflow-and-customize-the\|Enable memory in the LLM node within your chatflow, and customize the query prompt…]] | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-06-04">2024-06-04</time> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |

First in archive: each product's earliest tracked change in this theme. "·" marks a quarter without a key moment, and "not archived" a quarter before the product's archive begins. Archives begin: AnythingLLM 2024-07-26 · ChatGPT 2022-12-15 · Claude 2025-08-01 · Claude Code 2025-12-19 · Cline 2024-07-28 · Codex CLI 2025-06-30 · Cursor 2023-03-14 · Descript 2018-07-07 · Devin 2024-05-13 · Dify 2023-05-15 · ElevenLabs 2024-10-13 · Gemini 2023-04-10 · Gemini CLI 2025-06-28 · GitHub Copilot CLI 2025-09-26 · Google Antigravity 2025-11-18 · HeyGen 2025-11-29 · Kimi Code 2026-05-26 · Krea 2026-04-14 · LM Studio 2024-10-22 · Lovable 2024-12-03 · Microsoft 365 Copilot 2026-01-13 · Midjourney 2024-03-07 · Notion 2020-01-09 · Open WebUI 2024-02-23 · OpenClaw 2026-06-30 · OpenCode 2025-12-19 · OpenHands 2024-06-04 · Qoder 2026-08-27 · Raycast 2020-08-03 · Replit 2024-12-13 · Superwhisper 2023-08-03 · Windsurf 2025-04-02 · v0 2025-10-01.
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
<label><input type="radio" name="timeline-product" id="tl-only-1"> AnythingLLM</label>
<label><input type="radio" name="timeline-product" id="tl-only-2"> ChatGPT</label>
<label><input type="radio" name="timeline-product" id="tl-only-3"> Claude</label>
<label><input type="radio" name="timeline-product" id="tl-only-4"> Claude Code</label>
<label><input type="radio" name="timeline-product" id="tl-only-5"> Cline</label>
<label><input type="radio" name="timeline-product" id="tl-only-6"> Codex CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-7"> Cursor</label>
<label><input type="radio" name="timeline-product" id="tl-only-8"> Descript</label>
<label><input type="radio" name="timeline-product" id="tl-only-9"> Devin</label>
<label><input type="radio" name="timeline-product" id="tl-only-10"> Dify</label>
<label><input type="radio" name="timeline-product" id="tl-only-11"> ElevenLabs</label>
<label><input type="radio" name="timeline-product" id="tl-only-12"> Gemini</label>
<label><input type="radio" name="timeline-product" id="tl-only-13"> Gemini CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-14"> GitHub Copilot CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-15"> Google Antigravity</label>
<label><input type="radio" name="timeline-product" id="tl-only-16"> HeyGen</label>
<label><input type="radio" name="timeline-product" id="tl-only-17"> Kimi Code</label>
<label><input type="radio" name="timeline-product" id="tl-only-18"> Krea</label>
<label><input type="radio" name="timeline-product" id="tl-only-19"> LM Studio</label>
<label><input type="radio" name="timeline-product" id="tl-only-20"> Lovable</label>
<label><input type="radio" name="timeline-product" id="tl-only-21"> Microsoft 365 Copilot</label>
<label><input type="radio" name="timeline-product" id="tl-only-22"> Midjourney</label>
<label><input type="radio" name="timeline-product" id="tl-only-23"> Notion</label>
<label><input type="radio" name="timeline-product" id="tl-only-24"> Open WebUI</label>
<label><input type="radio" name="timeline-product" id="tl-only-25"> OpenClaw</label>
<label><input type="radio" name="timeline-product" id="tl-only-26"> OpenCode</label>
<label><input type="radio" name="timeline-product" id="tl-only-27"> OpenHands</label>
<label><input type="radio" name="timeline-product" id="tl-only-28"> Qoder</label>
<label><input type="radio" name="timeline-product" id="tl-only-29"> Raycast</label>
<label><input type="radio" name="timeline-product" id="tl-only-30"> Replit</label>
<label><input type="radio" name="timeline-product" id="tl-only-31"> Superwhisper</label>
<label><input type="radio" name="timeline-product" id="tl-only-32"> Windsurf</label>
<label><input type="radio" name="timeline-product" id="tl-only-33"> v0</label>
</fieldset>

<details class="disclosure">
<summary>2026 · 261 entries (AnythingLLM 1 · ChatGPT 18 · Claude 4 · Claude Code 20 · Cline 2 · Codex CLI 53 · Cursor 1 · Devin 3 · Dify 6 · ElevenLabs 1 · Gemini 1 · Gemini CLI 16 · GitHub Copilot CLI 30 · Google Antigravity 1 · HeyGen 2 · Kimi Code 4 · Krea 1 · LM Studio 1 · Lovable 3 · Microsoft 365 Copilot 1 · Midjourney 12 · Notion 1 · Open WebUI 20 · OpenClaw 23 · OpenCode 7 · OpenHands 1 · Qoder 1 · Raycast 19 · Replit 1 · Superwhisper 1 · Windsurf 2 · v0 4)</summary>

**2026-11**

- 2026-11-04 · <span class="tl-product tl-p20">**Lovable**</span> · [[Changes/Lovable/2026-11-04-dreaming-lovable-keeps-its-memory-up-to-date|Dreaming: Lovable keeps its memory up to date]] · Launch

**2026-10**

- 2026-10-30 · <span class="tl-product tl-p20">**Lovable**</span> · [[Changes/Lovable/2026-10-30-lovable-remembers-what-you-tell-it|Lovable remembers what you tell it]] · Launch
- 2026-10-20 · <span class="tl-product tl-p18">**Krea**</span> · [[Changes/Krea/2026-10-20-smarter-agent-upgrade-suggestions-and-edit-model-memory|Smarter Agent upgrade suggestions and Edit model memory]] · Launch
- 2026-10-19 · <span class="tl-product tl-p9">**Devin**</span> · [[Changes/Devin/2026-10-19-turn-off-nightly-memory-dreaming|Turn Off Nightly Memory Dreaming]] · Launch
- 2026-10-14 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-10-14-memory-reindex-rate-limits-reindexing-memories-from-the-admin-reindex-knowledge|🧮 Memory reindex rate limits. Reindexing memories, from the admin Reindex…]] · Policy
- 2026-10-12 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-10-12-cloud-sync-v2|Cloud Sync v2]] · Launch
- 2026-10-09 · <span class="tl-product tl-p9">**Devin**</span> · [[Changes/Devin/2026-10-09-memory-and-dreaming|Memory and dreaming]] · Launch
- 2026-10-08 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2026-10-08-organization-improvements|ORGANIZATION IMPROVEMENTS]] · Launch

**2026-09**

- 2026-09-30 · <span class="tl-product tl-p9">**Devin**</span> · [[Changes/Devin/2026-09-30-context-tab|Context Tab]] · Launch
- 2026-09-11 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-09-11-projects|Projects]] · Launch
- 2026-09-11 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-09-11-projects-6239fd|Projects]] · Launch

**2026-08**

- 2026-08-25 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2026-08-25-memory-in-claude-cowork-editable-topics-and-a-sensitive-topics-setting|Memory in Claude Cowork, editable topics, and a sensitive topics setting]] · Launch
- 2026-08-21 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2026-08-21-settings|Settings]] · Launch
- 2026-08-14 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-08-14-you-can-now-change-a-project-s-memory-setting-after-you-create-it-open-the-proje-b36ffe|Edit memory settings for existing projects]] · Change

**2026-07**

- 2026-07-29 · <span class="tl-product tl-p32">**Windsurf**</span> · [[Changes/Windsurf/2026-07-29-devin-local|Devin Local]] · Launch
- 2026-07-29 · <span class="tl-product tl-p32">**Windsurf**</span> · [[Changes/Windsurf/2026-07-29-devin-local-8ab9ef|Devin Local]] · Launch
- 2026-07-24 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2026-07-24-we-are-launching-our-v8-2-image-model-today-this-update-focuses-on-aesthetics-an|Midjourney launches our V8.2 image model today]] · Launch
- 2026-07-09 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2026-07-09-a-new-way-to-reflect-with-claude|A new way to reflect with Claude]] · Launch

**2026-06**

- 2026-06-18 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-18-you-can-now-delete-memory-files-in-the-ui-or-prompt-your-automation-to-delete-ou|Delete memory files in the UI, or prompt your automation to delete outdated memories…]] · Change
- 2026-06-12 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-12-you-can-now-delete-the-memories-shown-on-your-memory-summary-page-and-turn-memor-f16782|Additional controls for memory summary]] · Change

**2026-05**

- 2026-05-18 · <span class="tl-product tl-p20">**Lovable**</span> · [[Changes/Lovable/2026-05-18-security-memory|Security memory]] · Launch

**2026-04**

- 2026-04-20 · <span class="tl-product tl-p11">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-20-elevenagents-d2ebb2|ElevenAgents]] · Launch

**2026-03**

- 2026-03-26 · <span class="tl-product tl-p12">**Gemini**</span> · [[Changes/Gemini/2026-03-26-make-the-switch-seamlessly-bring-your-ai-memories-and-chat-history-to-gemini|Make the switch: Seamlessly bring your AI memories and chat history to Gemini]] · Launch
- 2026-03-17 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-03-17-we-re-sunsetting-the-preset-nerdy-base-style-to-simplify-options-and-improve-res|Sunsetting the “Nerdy” base style]] · Policy
- 2026-03-17 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2026-03-17-other-tips-and-tricks|Other Tips and Tricks]] · Launch
- 2026-03-02 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2026-03-02-memory-for-free-users|Memory for free users]] · Expansion

**2026-02**

- 2026-02-20 · <span class="tl-product tl-p30">**Replit**</span> · [[Changes/Replit/2026-02-20-background-memory-compression|Background memory compression]] · Launch

**2026-01**

- 2026-01-27 · <span class="tl-product tl-p21">**Microsoft 365 Copilot**</span> · [[Changes/Microsoft 365 Copilot/2026-01-27-improve-relevance-and-personalization-by-connecting-user-identities-across-data|Improve relevance and personalization by connecting user identities across data…]] · Launch
- 2026-01-20 · <span class="tl-product tl-p23">**Notion**</span> · [[Changes/Notion/2026-01-20-new-models-same-memory|New models, same memory]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 232 (AnythingLLM 1 · ChatGPT 15 · Claude 1 · Claude Code 20 · Cline 2 · Codex CLI 53 · Dify 6 · Gemini CLI 16 · GitHub Copilot CLI 30 · Google Antigravity 1 · HeyGen 2 · Kimi Code 4 · LM Studio 1 · Midjourney 8 · Open WebUI 19 · OpenClaw 23 · OpenCode 7 · OpenHands 1 · Qoder 1 · Raycast 16 · Superwhisper 1 · v0 4)</summary>

**2026-11**

- 2026-11-06 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-11-06-2-memory-and-personalization-changes-in-rust-v0-167-0|2 Memory and Personalization changes in rust-v0.167.0]] · Digest
- 2026-11-06 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-11-06-10-memory-and-personalization-changes-in-v1-0-106|10 Memory and Personalization changes in v1.0.106]] · Digest
- 2026-11-05 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-11-05-5-memory-and-personalization-changes-in-v2026-11-1|5 Memory and Personalization changes in v2026.11.1]] · Digest
- 2026-11-03 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-11-03-15-memory-and-personalization-changes-in-v2026-10-10|15 Memory and Personalization changes in v2026.10.10]] · Digest

**2026-10**

- 2026-10-30 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-10-30-account-switching-is-rolling-out-to-the-chatgpt-ios-and-android-apps-you-can-sta|Account switching on iOS and Android]] · Change
- 2026-10-29 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-29-2-memory-and-personalization-changes-in-rust-v0-166-0|2 Memory and Personalization changes in rust-v0.166.0]] · Digest
- 2026-10-29 · <span class="tl-product tl-p19">**LM Studio**</span> · [[Changes/LM Studio/2026-10-29-mac-added-maximum-memory-and-neural-engine-prefill-controls-for-splash-models|Mac Added maximum-memory and Neural Engine Prefill controls for Splash models]] · Change
- 2026-10-29 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-10-29-2-memory-and-personalization-changes-in-v0-12-5|2 Memory and Personalization changes in v0.12.5]] · Digest
- 2026-10-28 · <span class="tl-product tl-p17">**Kimi Code**</span> · [[Changes/Kimi Code/2026-10-28-web-sessions-now-unload-from-memory-after-30-minutes-idle-and-resume-transparent|Web sessions now unload from memory after 30 minutes idle and resume transparently…]] · Change
- 2026-10-28 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-10-28-ai-chat-long-chats-now-open-scroll-and-stream-replies-faster-while-using-less-me|AI Chat : Long chats now open, scroll, and stream replies faster while using less memory]] · Change
- 2026-10-28 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-10-28-ai-chat-long-chats-now-open-scroll-and-stream-replies-faster-while-using-less-me-e1c669|AI Chat : Long chats now open, scroll, and stream replies faster while using less memory]] · Change
- 2026-10-27 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-27-5-memory-and-personalization-changes-in-rust-v0-165-0|5 Memory and Personalization changes in rust-v0.165.0]] · Digest
- 2026-10-27 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-27-4-memory-and-personalization-changes-in-v2026-10-8|4 Memory and Personalization changes in v2026.10.8]] · Digest
- 2026-10-27 · <span class="tl-product tl-p26">**OpenCode**</span> · [[Changes/OpenCode/2026-10-27-8-memory-and-personalization-changes-in-v2-2-0|8 Memory and Personalization changes in v2.2.0]] · Digest
- 2026-10-24 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-24-2-memory-and-personalization-changes-in-v2026-10-7|2 Memory and Personalization changes in v2026.10.7]] · Digest
- 2026-10-23 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-23-4-memory-and-personalization-changes-in-rust-v0-164-0|4 Memory and Personalization changes in rust-v0.164.0]] · Digest
- 2026-10-23 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2026-10-23-3-memory-and-personalization-changes-in-1-18-0|3 Memory and Personalization changes in 1.18.0]] · Digest
- 2026-10-22 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-22-4-memory-and-personalization-changes-in-v2026-10-6|4 Memory and Personalization changes in v2026.10.6]] · Digest
- 2026-10-22 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-10-22-this-update-brings-new-commands-useful-improvements-and-plenty-of-fixes-across-r|This update brings new commands, useful improvements, and plenty of fixes across Raycast]] · Change
- 2026-10-22 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-10-22-this-update-brings-new-commands-useful-improvements-and-plenty-of-fixes-across-r-e70c05|This update brings new commands, useful improvements, and plenty of fixes across Raycast]] · Change
- 2026-10-18 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-18-memory-search-recognizes-more-accented-and-korean-spellings-and-keeps-keyword-se|Memory search recognizes more accented and Korean spellings and keeps keyword search…]] · Change
- 2026-10-16 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-10-16-built-in-tools-turned-back-on-stay-on-a-built-in-tool-such-as-memory-that-is-off|🧰 Built-in tools turned back on stay on. A built-in tool such as Memory…]] · Change
- 2026-10-16 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-16-schedule-inspection-during-recovery-updates-and-doctor-can-continue-when-optiona|Schedule inspection during recovery]] · Change
- 2026-10-16 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-10-16-this-update-is-about-speed-file-search-returns-results-up-to-6-faster-and-handle|This update is about speed]] · Change
- 2026-10-16 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-10-16-this-update-is-about-speed-file-search-returns-results-up-to-6-faster-and-handle-838564|This update is about speed]] · Change
- 2026-10-16 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-10-16-lighter-at-startup-raycast-uses-about-20-less-memory-at-launch-and-starts-faster|Lighter at startup : Raycast uses about 20% less memory at launch and starts faster]] · Change
- 2026-10-16 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-10-16-lighter-at-startup-raycast-uses-about-20-less-memory-at-launch-and-starts-faster-bbc58a|Lighter at startup : Raycast uses about 20% less memory at launch and starts faster]] · Change
- 2026-10-15 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-15-codex-can-run-independent-read-only-tools-in-parallel-including-skill-memory-and|Codex can run independent read-only tools in parallel, including skill, memory…]] · Change
- 2026-10-14 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-10-14-memory-in-automations-automations-now-get-the-memory-tools-when-the-user-has-mem|🧠 Memory in automations. Automations now get the memory tools when the user has…]] · Change
- 2026-10-14 · <span class="tl-product tl-p28">**Qoder**</span> · [[Changes/Qoder/2026-10-14-remote-ssh-select-git-branches-in-remote-sessions-and-import-qoder-ide-task-hist|Remote SSH: Select Git branches in remote sessions and import Qoder IDE task…]] · Change
- 2026-10-13 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-13-5-memory-and-personalization-changes-in-v2026-10-3|5 Memory and Personalization changes in v2026.10.3]] · Digest
- 2026-10-12 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-12-4-memory-and-personalization-changes-in-v2026-10-2|4 Memory and Personalization changes in v2026.10.2]] · Digest
- 2026-10-12 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-10-12-2-memory-and-personalization-changes-in-raycast-ios-1-4-0|2 Memory and Personalization changes in Raycast ios 1.4.0]] · Digest
- 2026-10-10 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2 Memory and Personalization changes in v0.12.0]] · Digest
- 2026-10-10 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-10-13-memory-and-personalization-changes-in-v2026-10-1|13 Memory and Personalization changes in v2026.10.1]] · Digest
- 2026-10-09 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-10-09-file-search-improved-cpu-and-memory-utilization-file-search-should-now-use-rough|File Search : Improved CPU and memory utilization]] · Change
- 2026-10-09 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-10-09-we-made-more-memory-and-performance-improvements-ai-chat-notes-and-settings-now|We made more memory and performance improvements]] · Change
- 2026-10-09 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-10-09-2-memory-and-personalization-changes-in-raycast-macos-2-7|2 Memory and Personalization changes in Raycast macos 2.7]] · Digest
- 2026-10-08 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-08-51223-remove-legacy-personality-template-metadata-rhan-oai|♯51223 Remove legacy personality template metadata @rhan-oai]] · Change
- 2026-10-08 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-08-2-memory-and-personalization-changes-in-v2026-9-9|2 Memory and Personalization changes in v2026.9.9]] · Digest
- 2026-10-07 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-07-49876-remove-personality-plumbing-from-the-tui-etraut-openai|♯49876 Remove personality plumbing from the TUI @etraut-openai]] · Change
- 2026-10-05 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-10-05-file-search-the-file-indexer-uses-about-60-less-memory-when-it-updates-its-index|File Search : The file indexer uses about 60% less memory when it updates its index]] · Change
- 2026-10-05 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-10-05-file-search-the-file-indexer-uses-about-60-less-memory-when-it-updates-its-index-ee1d12|File Search : The file indexer uses about 60% less memory when it updates its index]] · Change
- 2026-10-03 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-03-2-memory-and-personalization-changes-in-v2026-9-8|2 Memory and Personalization changes in v2026.9.8]] · Digest
- 2026-10-01 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-10-01-virtually-try-on-clothing-and-accessories-a-try-on-button-will-appear-on-product|Virtually try on clothing and accessories]] · Change
- 2026-10-01 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-01-improved-memory-the-left-and-right-arrow-keys-now-flip-its-on-off-settings-such|Improved /memory: the left and right arrow keys now flip its on/off settings, such…]] · Change
- 2026-10-01 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-01-49000-isolate-the-memory-startup-metadata-test-from-git-enrichment-jif-oai|♯49000 Isolate the memory startup metadata test from Git enrichment @jif-oai]] · Change

**2026-09**

- 2026-09-30 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-30-15-memory-and-personalization-changes-in-v2026-9-7|15 Memory and Personalization changes in v2026.9.7]] · Digest
- 2026-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-29-pages-follow-space-s-availability-and-sharing-settings-sharing-a-page-does-not-g|Pages follow Space’s availability and sharing settings]] · Change
- 2026-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-29-you-can-use-your-chatgpt-account-to-sign-in-to-participating-products-without-cr|Sign in to other products with ChatGPT]] · Change
- 2026-09-29 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-29-changed-memory-so-that-auto-memory-can-no-longer-be-turned-on-from-a-background|Changed /memory so that Auto-memory can no longer be turned on from a background…]] · Change
- 2026-09-28 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-28-improved-auto-memory-loading-invisible-characters-and-tags-that-imitate-claude-c|Improved auto-memory loading]] · Change
- 2026-09-28 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-28-3-memory-and-personalization-changes-in-rust-v0-158-0|3 Memory and Personalization changes in rust-v0.158.0]] · Digest
- 2026-09-28 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-28-add-support-for-claude-code-rule-files-in-claude-rules-as-custom-instructions|Add support for Claude Code rule files in .claude/rules as custom instructions]] · Change
- 2026-09-25 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-25-improved-lists-in-help-hooks-copy-chrome-memory-ide-release-notes-rewind-diff-re|Improved lists in /help, /hooks, /copy, /chrome, /memory, /ide…]] · Change
- 2026-09-23 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-23-23-memory-and-personalization-changes-in-v2026-9-6|23 Memory and Personalization changes in v2026.9.6]] · Digest
- 2026-09-22 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-22-6-memory-and-personalization-changes-in-rust-v0-156-0|6 Memory and Personalization changes in rust-v0.156.0]] · Digest
- 2026-09-22 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-22-resuming-large-local-sessions-keeps-transcript-memory-bounded-for-smoother-cli-p|Resuming large local sessions keeps transcript memory bounded for smoother CLI performance]] · Change
- 2026-09-21 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-21-tear-down-the-processes-an-internal-git-command-started-when-it-times-out-so-a-s|Tear down the processes an internal git command started when it times out, so a slow…]] · Change
- 2026-09-21 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-09-21-6-memory-and-personalization-changes-in-v0-11-4|6 Memory and Personalization changes in v0.11.4]] · Digest
- 2026-09-19 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-19-31-memory-and-personalization-changes-in-v2026-9-5|31 Memory and Personalization changes in v2026.9.5]] · Digest
- 2026-09-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-17-vscode-added-viewing-editing-and-deleting-a-saved-memory-inside-the-memory-dialo|VSCode Added viewing, editing and deleting a saved memory inside the Memory dialog]] · Change
- 2026-09-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-17-vscode-added-memory-and-instructions-entries-to-the-customize-menu-memory-shows|VSCode Added Memory and Instructions entries to the Customize menu]] · Change
- 2026-09-17 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-17-7-memory-and-personalization-changes-in-rust-v0-155-0|7 Memory and Personalization changes in rust-v0.155.0]] · Digest
- 2026-09-16 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-16-3-memory-and-personalization-changes-in-v1-0-85|3 Memory and Personalization changes in v1.0.85]] · Digest
- 2026-09-15 · <span class="tl-product tl-p15">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-15-conversations-with-very-long-histories-now-load-faster-and-use-less-memory|Conversations with very long histories now load faster and use less memory]] · Change
- 2026-09-11 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-11-14-memory-and-personalization-changes-in-v2026-9-4|14 Memory and Personalization changes in v2026.9.4]] · Digest
- 2026-09-10 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-10-2-memory-and-personalization-changes-in-v2-1-268|2 Memory and Personalization changes in v2.1.268]] · Digest
- 2026-09-10 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2026-09-10-2-memory-and-personalization-changes-in-1-17-1|2 Memory and Personalization changes in 1.17.1]] · Digest
- 2026-09-09 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-09-2-memory-and-personalization-changes-in-rust-v0-154-0|2 Memory and Personalization changes in rust-v0.154.0]] · Digest
- 2026-09-08 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-08-10-memory-and-personalization-changes-in-v2026-9-3|10 Memory and Personalization changes in v2026.9.3]] · Digest
- 2026-09-05 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-05-21-memory-and-personalization-changes-in-v2026-9-2|21 Memory and Personalization changes in v2026.9.2]] · Digest
- 2026-09-04 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-04-long-running-sessions-on-linux-return-freed-memory-to-the-system-instead-of-hold|Long-running sessions on Linux return freed memory to the system instead of holding…]] · Change
- 2026-09-04 · <span class="tl-product tl-p31">**Superwhisper**</span> · [[Changes/Superwhisper/2026-09-04-lower-memory-use-during-long-recordings|Lower memory use during long recordings]] · Change
- 2026-09-03 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-03-19-memory-and-personalization-changes-in-v2026-9-1|19 Memory and Personalization changes in v2026.9.1]] · Digest
- 2026-09-01 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-01-4-memory-and-personalization-changes-in-v2026-8-2|4 Memory and Personalization changes in v2026.8.2]] · Digest

**2026-08**

- 2026-08-31 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-08-31-memory-an-eligible-personal-claw-can-recall-relevant-context-from-that-agent-s-o|Memory - An eligible personal Claw can recall relevant context from that agent's…]] · Change
- 2026-08-27 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-08-27-3-memory-and-personalization-changes-in-more-controls-in-temporary-chat|3 Memory and Personalization changes in More controls in temporary chat]] · Digest
- 2026-08-27 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-08-27-we-re-rolling-out-new-controls-in-temporary-chat-you-can-now-choose-to-personali|ChatGPT rolls out new controls in temporary chat]] · Change
- 2026-08-27 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-27-ship-mcp-2026-07-28-support-to-cli-sdk-ide-and-in-memory-clients|Ship MCP 2026-07-28 support to CLI, SDK, IDE, and in-memory clients]] · Change
- 2026-08-27 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2026-08-27-using-personalization-moodboards-and-srefs-moodboards-srefs-may-work-best-with-s|Using personalization, moodboards and srefs…]] · Change
- 2026-08-26 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-26-3-memory-and-personalization-changes-in-rust-v0-150-0|3 Memory and Personalization changes in rust-v0.150.0]] · Digest
- 2026-08-25 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-08-25-8-memory-and-personalization-changes-in-v0-11-1|8 Memory and Personalization changes in v0.11.1]] · Digest
- 2026-08-20 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-08-20-use-computer-history-in-more-regions-computer-history-is-now-available-in-the-ee|Use Computer History in more regions]] · Change
- 2026-08-20 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-20-updated-the-bundled-claude-api-skill-for-the-managed-agents-aug-19-release-web-s|Updated the bundled claude-api skill for the Managed Agents Aug 19 release]] · Change
- 2026-08-20 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-20-2-memory-and-personalization-changes-in-rust-v0-149-0|2 Memory and Personalization changes in rust-v0.149.0]] · Digest
- 2026-08-14 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-08-14-we-ve-made-it-easier-to-study-with-interactive-quizzes-manage-project-memory-and|ChatGPT makes it easier to study with interactive quizzes, manage project memory…]] · Change
- 2026-08-14 · <span class="tl-product tl-p33">**v0**</span> · [[Changes/v0/2026-08-14-reduced-the-web-client-s-memory-use-by-clearing-preview-iframes-blob-and-audio-u|Reduced the web client's memory use by clearing preview iframes, blob and audio…]] · Change
- 2026-08-13 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-13-cowork-sessions-no-longer-inline-external-imports-from-user-scope-memory-files|Cowork sessions no longer inline external @-imports from user-scope memory files]] · Change
- 2026-08-07 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-07-36140-wait-for-memory-consolidation-shutdown-before-finishing-jobs-copyberry|♯36140 Wait for memory consolidation shutdown before finishing jobs @copyberry]] · Change
- 2026-08-07 · <span class="tl-product tl-p16">**HeyGen**</span> · [[Changes/HeyGen/2026-08-07-when-users-enable-generate-script-with-ai-they-can-now-specify-the-script-s-goal|When users enable Generate Script with AI , they can now specify the script’s goal…]] · Change

**2026-07**

- 2026-07-31 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-07-31-remove-vestigial-mcp-server-key-machinery-from-mcphub-native-mcp-tool-calls-now|Remove vestigial MCP server-key machinery from McpHub]] · Change
- 2026-07-30 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-30-a-userpromptsubmitted-hook-returning-a-non-string-value-for-modifiedprompt-modif|A userPromptSubmitted hook returning a non-string value for modifiedPrompt…]] · Change
- 2026-07-29 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-29-35530-track-model-and-personality-in-world-state-copyberry|♯35530 Track model and personality in world state @copyberry]] · Change
- 2026-07-29 · <span class="tl-product tl-p27">**OpenHands**</span> · [[Changes/OpenHands/2026-07-29-feat-add-persistent-agent-memory-toggle-by-hieptl-in-https-github-com-openhands|feat: add persistent agent memory toggle]] · Change
- 2026-07-28 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2026-07-28-test-use-sqlite-sessions-in-core-memory-by-asukaminato0721-in-https-github-com-l|test: use SQLite sessions in core memory]] · Change
- 2026-07-27 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-07-27-7-memory-and-personalization-changes-in-v0-11-0|7 Memory and Personalization changes in v0.11.0]] · Digest
- 2026-07-24 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2026-07-24-personalization-will-understand-your-personal-taste-much-better-especially-if-yo|Personalization will "understand" your personal taste much better]] · Change
- 2026-07-24 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2026-07-24-creating-personalization-profiles-for-v8-2-now-has-a-much-larger-and-improved-po|Creating personalization profiles for V8.2 now has a much larger and improved pool…]] · Change
- 2026-07-21 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-21-11-memory-and-personalization-changes-in-rust-v0-145-0|11 Memory and Personalization changes in rust-v0.145.0]] · Digest
- 2026-07-21 · <span class="tl-product tl-p33">**v0**</span> · [[Changes/v0/2026-07-21-design-systems-personal-scope-imports-save-to-your-own-memory-the-selector-reset|Design systems: personal-scope imports save to your own memory, the selector resets…]] · Change
- 2026-07-18 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-18-added-an-iso-modified-timestamp-to-memory-file-frontmatter|Added an ISO modified timestamp to memory file frontmatter]] · Change
- 2026-07-17 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2026-07-17-perf-memory-batch-load-message-files-in-tokenbuffermemory-to-remove-n-1-queries|perf(memory): batch-load message files in TokenBufferMemory to remove N+1 queries]] · Change
- 2026-07-16 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-16-refresh-memory-context-after-30-minutes-in-long-lived-sessions|Refresh memory context after 30 minutes in long-lived sessions]] · Change
- 2026-07-15 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-07-15-we-re-increasing-the-character-limit-for-custom-instructions-in-chatgpt-plus-pro|Increased custom instructions limit]] · Change
- 2026-07-15 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-15-improved-the-memory-index-over-limit-warning-to-measure-only-loaded-content-excl|Improved the memory index over-limit warning to measure only loaded content…]] · Change
- 2026-07-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-14-memory-writes-that-leave-a-memory-md-index-over-its-read-limit-now-produce-an-ex|Memory writes that leave a MEMORY.md index over its read limit now produce…]] · Change
- 2026-07-13 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-07-13-136-memory-and-personalization-changes-in-v2026-7-1|136 Memory and Personalization changes in v2026.7.1]] · Digest
- 2026-07-10 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2026-07-10-updated-memory-for-claude|Updated memory for Claude]] · Change
- 2026-07-08 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-08-2-memory-and-personalization-changes-in-rust-v0-143-0|2 Memory and Personalization changes in rust-v0.143.0]] · Digest
- 2026-07-08 · <span class="tl-product tl-p17">**Kimi Code**</span> · [[Changes/Kimi Code/2026-07-08-progressive-tool-disclosure-select-tools-experimental-compaction-now-discards-th|Progressive tool disclosure (select_tools, experimental)]] · Change
- 2026-07-07 · <span class="tl-product tl-p33">**v0**</span> · [[Changes/v0/2026-07-07-team-members-with-v0-edit-access-can-manage-team-skills-and-memories-without-a-v|Team members with v0 edit access can manage team skills and memories without…]] · Change
- 2026-07-02 · <span class="tl-product tl-p17">**Kimi Code**</span> · [[Changes/Kimi Code/2026-07-02-release-pasted-images-and-streaming-timers-once-they-are-no-longer-shown-so-memo|Release pasted images and streaming timers once they are no longer shown, so memory…]] · Change
- 2026-07-01 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-07-01-2-memory-and-personalization-changes-in-v0-10-2|2 Memory and Personalization changes in v0.10.2]] · Digest

**2026-06**

- 2026-06-30 · <span class="tl-product tl-p25">**OpenClaw**</span> · [[Changes/OpenClaw/2026-06-30-26-memory-and-personalization-changes-in-v2026-6-11|26 Memory and Personalization changes in v2026.6.11]] · Digest
- 2026-06-29 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-06-29-5-memory-and-personalization-changes-in-v0-10-0|5 Memory and Personalization changes in v0.10.0]] · Digest
- 2026-06-24 · <span class="tl-product tl-p17">**Kimi Code**</span> · [[Changes/Kimi Code/2026-06-24-read-large-text-files-in-bounded-memory-and-read-tail-lines-without-scanning-who|Read large text files in bounded memory and read tail lines without scanning whole files]] · Change
- 2026-06-22 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-22-improved-memory-the-agent-is-now-reminded-to-compact-its-memory-md-index-when-ne|Improved memory: the agent is now reminded to compact its MEMORY.md index…]] · Change
- 2026-06-18 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-18-3-memory-and-personalization-changes-in-rust-v0-141-0|3 Memory and Personalization changes in rust-v0.141.0]] · Digest
- 2026-06-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-17-changed-the-improved-n-memories-line-to-no-longer-list-individual-files-outside|Changed the Improved N memories line to no longer list individual files outside…]] · Change
- 2026-06-15 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-15-27129-feat-use-provider-defaults-for-memory-models-celia-oai|♯27129 feat: use provider defaults for memory models @celia-oai]] · Change
- 2026-06-13 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-13-allow-sdk-clients-to-configure-session-memory-through-session-create-and-session|Allow SDK clients to configure session memory through session.create and session.resume]] · Change
- 2026-06-09 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-09-26821-codex-exclude-external-tool-output-from-memories-rka-oai|♯26821 codex Exclude external tool output from memories @rka-oai]] · Change
- 2026-06-09 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-09-resuming-a-local-session-with-memory-disabled-no-longer-crashes-the-ui-to-a-blan|Resuming a local session with memory disabled no longer crashes the UI to a blank screen]] · Change
- 2026-06-08 · <span class="tl-product tl-p33">**v0**</span> · [[Changes/v0/2026-06-08-team-plan-members-can-set-custom-instructions|Team plan members can set custom instructions]] · Change
- 2026-06-04 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-04-we-ve-upgraded-memory-so-chatgpt-can-better-keep-your-context-up-to-date-helping-9a48f3|Memory that stays more up to date]] · Change
- 2026-06-02 · <span class="tl-product tl-p16">**HeyGen**</span> · [[Changes/HeyGen/2026-06-02-personal-settings-contains-settings-that-apply-only-to-the-individual-user-inclu|Personal Settings contains settings that apply only to the individual user…]] · Change
- 2026-06-01 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-01-2-memory-and-personalization-changes-in-rust-v0-136-0|2 Memory and Personalization changes in rust-v0.136.0]] · Digest
- 2026-06-01 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-06-01-2-memory-and-personalization-changes-in-v0-9-6|2 Memory and Personalization changes in v0.9.6]] · Digest

**2026-05**

- 2026-05-28 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-28-8-memory-and-personalization-changes-in-rust-v0-135-0|8 Memory and Personalization changes in rust-v0.135.0]] · Digest
- 2026-05-28 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-28-vote-memory-tool-calls-are-throttled-per-response-and-per-interaction-to-prevent|vote_memory tool calls are throttled per response and per interaction to prevent…]] · Change
- 2026-05-27 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-27-chore-clean-up-launched-memory-features-by-sandytao520-in-https-github-com-googl|chore: clean up launched memory features]] · Change
- 2026-05-27 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2026-05-27-activating-a-niji-6-or-v6-personalization-profile-no-longer-immediately-deselect|Activating a Niji 6 or V6 Personalization profile no longer immediately deselects it]] · Change
- 2026-05-26 · <span class="tl-product tl-p1">**AnythingLLM**</span> · [[Changes/AnythingLLM/2026-05-26-10-memory-and-personalization-changes-in-v1-13-0|10 Memory and Personalization changes in v1.13.0]] · Digest
- 2026-05-26 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-26-22915-3-of-4-tui-route-feature-and-memory-toggles-through-app-server-etraut-open|♯22915 3 of 4 tui: route feature and memory toggles through app server @etraut-openai]] · Change
- 2026-05-22 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-22-2-memory-and-personalization-changes-in-v0-43-0|2 Memory and Personalization changes in v0.43.0]] · Digest
- 2026-05-20 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-20-2-memory-and-personalization-changes-in-rust-v0-132-0|2 Memory and Personalization changes in rust-v0.132.0]] · Digest
- 2026-05-20 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-20-memory-show-displays-documentation-links-for-learning-about-and-managing-copilot|/memory show displays documentation links for learning about and managing Copilot Memory]] · Change
- 2026-05-19 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2026-05-19-workflow-execution-reliability-restored-tracing-after-hitl-workflow-resume-impro|Workflow execution reliability]] · Change
- 2026-05-19 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-19-2-memory-and-personalization-changes-in-v1-0-49|2 Memory and Personalization changes in v1.0.49]] · Digest
- 2026-05-18 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-18-4-memory-and-personalization-changes-in-rust-v0-131-0|4 Memory and Personalization changes in rust-v0.131.0]] · Digest
- 2026-05-12 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-12-feat-memory-add-auto-memory-inbox-flow-with-canonical-patch-contract-by-sandytao|feat(memory): add Auto Memory inbox flow with canonical-patch contract]] · Change
- 2026-05-09 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-05-09-faster-memory-query-performance-per-user-memory-lookups-and-deletions-now-run-mu|⚡ Faster memory query performance. Per-user memory lookups and deletions now run…]] · Change
- 2026-05-08 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-05-08-import-add-support-for-importing-ai-extension-custom-instructions|Import : Add support for importing AI extension custom instructions]] · Change
- 2026-05-07 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-07-16-memory-and-personalization-changes-in-rust-v0-129-0|16 Memory and Personalization changes in rust-v0.129.0]] · Digest
- 2026-05-05 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-05-05-starting-today-we-re-rolling-out-memory-improvements-to-chatgpt-plus-and-pro-use|Memory sources and more personalized responses in ChatGPT]] · Change
- 2026-05-05 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-05-feat-memory-persist-auto-memory-scratchpad-for-skill-extraction-by-sandytao520-i|feat(memory): persist auto-memory scratchpad for skill extraction]] · Change
- 2026-05-04 · <span class="tl-product tl-p26">**OpenCode**</span> · [[Changes/OpenCode/2026-05-04-core-prevent-large-diffs-from-using-unbounded-memory|Core Prevent large diffs from using unbounded memory]] · Change

**2026-04**

- 2026-04-30 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-30-12-memory-and-personalization-changes-in-rust-v0-128-0|12 Memory and Personalization changes in rust-v0.128.0]] · Digest
- 2026-04-28 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-28-refactor-memory-replace-memorymanageragent-with-prompt-driven-memory-editing-acr|refactor(memory): replace MemoryManagerAgent with prompt-driven memory editing…]] · Change
- 2026-04-24 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-04-24-improve-cline-core-memory-diagnostics-used-by-the-extension-runtime|Improve cline-core memory diagnostics used by the extension runtime]] · Change
- 2026-04-24 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-24-custom-instruction-files-in-gitignored-directories-e-g-github-instructions-now-l|Custom instruction files in .gitignored directories (e.g., .github/instructions/)…]] · Change
- 2026-04-24 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-04-24-2-memory-and-personalization-changes-in-v0-9-2|2 Memory and Personalization changes in v0.9.2]] · Digest
- 2026-04-23 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-18973-chore-prep-memories-for-ab-jif-oai|♯18973 chore: prep memories for AB @jif-oai]] · Change
- 2026-04-23 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-18858-stabilize-debug-clear-memories-integration-test-jif-oai|♯18858 Stabilize debug clear memories integration test @jif-oai]] · Change
- 2026-04-23 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-23-4-memory-and-personalization-changes-in-v0-39-0|4 Memory and Personalization changes in v0.39.0]] · Digest
- 2026-04-22 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-04-22-sometimes-you-just-want-the-right-answer-as-quickly-as-possible-we-re-rolling-ou|Fast answers in ChatGPT]] · Change
- 2026-04-21 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-04-21-7-memory-and-personalization-changes-in-v0-9-0|7 Memory and Personalization changes in v0.9.0]] · Digest
- 2026-04-20 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-20-4-memory-and-personalization-changes-in-rust-v0-122-0|4 Memory and Personalization changes in rust-v0.122.0]] · Digest
- 2026-04-16 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-16-custom-instructions-and-skills-refresh-from-disk-after-clear-or-new|Custom instructions and skills refresh from disk after /clear or /new]] · Change
- 2026-04-16 · <span class="tl-product tl-p26">**OpenCode**</span> · [[Changes/OpenCode/2026-04-16-core-the-bash-tool-uses-less-memory-on-large-command-output|Core The bash tool uses less memory on large command output]] · Change
- 2026-04-15 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-15-9-memory-and-personalization-changes-in-rust-v0-121-0|9 Memory and Personalization changes in rust-v0.121.0]] · Digest
- 2026-04-14 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-14-2-memory-and-personalization-changes-in-v0-38-0|2 Memory and Personalization changes in v0.38.0]] · Digest
- 2026-04-13 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-13-custom-instruction-files-preserve-special-characters-like-and-placeholders|Custom instruction files preserve special characters like & and placeholders]] · Change
- 2026-04-10 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-10-2-memory-and-personalization-changes-in-rust-v0-119-0|2 Memory and Personalization changes in rust-v0.119.0]] · Digest
- 2026-04-10 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-10-agent-no-longer-hangs-on-the-first-turn-when-the-memory-backend-is-unavailable|Agent no longer hangs on the first turn when the memory backend is unavailable]] · Change
- 2026-04-08 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-08-2-memory-and-personalization-changes-in-v0-37-0|2 Memory and Personalization changes in v0.37.0]] · Digest
- 2026-04-08 · <span class="tl-product tl-p26">**OpenCode**</span> · [[Changes/OpenCode/2026-04-08-core-reduced-typescript-lsp-memory-use-by-using-the-native-project-config|Core Reduced TypeScript LSP memory use by using the native project config]] · Change
- 2026-04-01 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-01-3-memory-and-personalization-changes-in-v0-36-0|3 Memory and Personalization changes in v0.36.0]] · Digest

**2026-03**

- 2026-03-27 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-27-memory-filenames-in-the-saved-n-memories-notice-now-highlight-on-hover-and-open|Memory filenames in the "Saved N memories" notice now highlight on hover and open on click]] · Change
- 2026-03-27 · <span class="tl-product tl-p29">**Raycast**</span> · [[Changes/Raycast/2026-03-27-ai-chat-added-memory-to-make-chats-more-personal|AI Chat: Added memory to make chats more personal]] · Change
- 2026-03-26 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-26-15175-chore-morpheus-does-not-generate-memories-jif-oai|♯15175 chore: morpheus does not generate memories @jif-oai]] · Change
- 2026-03-25 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-03-25-4-memory-and-personalization-changes-in-v0-8-11|4 Memory and Personalization changes in v0.8.11]] · Digest
- 2026-03-24 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-24-refactor-core-align-jit-memory-placement-with-tiered-context-model-by-sandytao52|refactor(core): align JIT memory placement with tiered context model]] · Change
- 2026-03-19 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-19-4-memory-and-personalization-changes-in-rust-v0-116-0|4 Memory and Personalization changes in rust-v0.116.0]] · Digest
- 2026-03-17 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2026-03-17-4-memory-and-personalization-changes-in-1-13-1|4 Memory and Personalization changes in 1.13.1]] · Digest
- 2026-03-17 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-17-docs-document-tool-exclusion-from-memory-via-deny-policy-by-abhijit-2592-in-http|docs: document tool exclusion from memory via deny policy]] · Change
- 2026-03-16 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-16-14493-memories-focus-write-prompts-on-user-preferences-andi-oai|♯14493 memories: focus write prompts on user preferences @andi-oai]] · Change
- 2026-03-16 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-16-custom-instruction-file-paths-load-correctly-when-using-copilot-custom-instructi|Custom instruction file paths load correctly when using COPILOT_CUSTOM_INSTRUCTIONS_DIRS]] · Change
- 2026-03-13 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-13-memory-storage-errors-now-indicate-when-repository-doesn-t-exist-or-you-lack-wri|Memory storage errors now indicate when repository doesn't exist or you lack write access]] · Change
- 2026-03-12 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-12-added-automemorydirectory-setting-to-configure-a-custom-directory-for-auto-memor|Added autoMemoryDirectory setting to configure a custom directory for auto-memory…]] · Change
- 2026-03-12 · <span class="tl-product tl-p26">**OpenCode**</span> · [[Changes/OpenCode/2026-03-12-core-multiple-jdtls-lsps-eating-memory-in-java-monorepos|Core Multiple jdtls LSPs eating memory in Java monorepos]] · Change
- 2026-03-11 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-11-feat-implement-slash-command-handling-in-acp-for-memory-init-extensions-and-rest|feat: Implement slash command handling in ACP for /memory,/init,/extensions…]] · Change
- 2026-03-10 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-10-13734-feat-prune-old-memories-in-db-jif-oai|♯13734 feat: prune old memories in DB @jif-oai]] · Change
- 2026-03-08 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-03-08-system-metrics-via-opentelemetry-administrators-can-now-monitor-python-runtime-a|📡 System metrics via OpenTelemetry. Administrators can now monitor Python…]] · Change
- 2026-03-05 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-05-5-memory-and-personalization-changes-in-rust-v0-110-0|5 Memory and Personalization changes in rust-v0.110.0]] · Digest
- 2026-03-02 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-02-6-memory-and-personalization-changes-in-rust-v0-107-0|6 Memory and Personalization changes in rust-v0.107.0]] · Digest

**2026-02**

- 2026-02-28 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-28-project-configs-auto-memory-now-shared-across-git-worktrees-of-the-same-reposito|Project configs & auto memory now shared across git worktrees of the same repository]] · Change
- 2026-02-26 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-26-claude-automatically-saves-useful-context-to-auto-memory-manage-with-memory|Claude automatically saves useful context to auto-memory]] · Change
- 2026-02-26 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-26-3-memory-and-personalization-changes-in-rust-v0-106-0|3 Memory and Personalization changes in rust-v0.106.0]] · Digest
- 2026-02-26 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2026-02-26-we-ve-added-personalization-and-moodboards-to-niji-7-our-anime-image-model|Midjourney adds Personalization and Moodboards to niji 7 (our anime image model)]] · Change
- 2026-02-26 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2026-02-26-we-ve-got-a-new-personalization-interface-on-web|We've got a new personalization interface on web]] · Change
- 2026-02-26 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2026-02-26-this-lets-you-make-personalization-profiles-by-clicking-and-scrolling-through-a|This lets you make personalization profiles by clicking and scrolling through a list…]] · Change
- 2026-02-25 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-25-9-memory-and-personalization-changes-in-rust-v0-105-0|9 Memory and Personalization changes in rust-v0.105.0]] · Digest
- 2026-02-25 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-25-test-evals-mark-all-save-memory-evals-as-usually-passes-due-to-unreliability-by|test(evals): mark all save_memory evals as USUALLY_PASSES due to unreliability]] · Change
- 2026-02-23 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-02-23-2-memory-and-personalization-changes-in-v0-8-4|2 Memory and Personalization changes in v0.8.4]] · Digest
- 2026-02-20 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2026-02-20-we-re-now-in-the-final-round-of-the-v8-image-rating-party|We're now in the FINAL ROUND of the V8 image rating party]] · Change
- 2026-02-19 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-19-2-memory-and-personalization-changes-in-v0-0-412|2 Memory and Personalization changes in v0.0.412]] · Digest
- 2026-02-19 · <span class="tl-product tl-p26">**OpenCode**</span> · [[Changes/OpenCode/2026-02-19-core-make-read-tool-more-memory-efficient|Core Make read tool more memory efficient]] · Change
- 2026-02-18 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-18-2-memory-and-personalization-changes-in-v0-29-0|2 Memory and Personalization changes in v0.29.0]] · Digest
- 2026-02-17 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-17-4-memory-and-personalization-changes-in-rust-v0-102-0|4 Memory and Personalization changes in rust-v0.102.0]] · Digest
- 2026-02-17 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-17-2-memory-and-personalization-changes-in-v0-0-411|2 Memory and Personalization changes in v0.0.411]] · Digest
- 2026-02-17 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-02-17-faster-model-filtering-model-access-control-filtering-no-longer-makes-a-redundan|⚡ Faster model filtering. Model access control filtering no longer makes…]] · Change
- 2026-02-14 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-14-reduced-memory-growth-in-long-sessions-by-evicting-transient-events-after-compac|Reduced memory growth in long sessions by evicting transient events after compaction]] · Change
- 2026-02-12 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-12-11-memory-and-personalization-changes-in-rust-v0-100-0|11 Memory and Personalization changes in rust-v0.100.0]] · Digest
- 2026-02-12 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-12-6-memory-and-personalization-changes-in-rust-v0-101-0|6 Memory and Personalization changes in rust-v0.101.0]] · Digest
- 2026-02-12 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-02-12-2-memory-and-personalization-changes-in-v0-8-0|2 Memory and Personalization changes in v0.8.0]] · Digest
- 2026-02-11 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-11-7-memory-and-personalization-changes-in-rust-v0-99-0|7 Memory and Personalization changes in rust-v0.99.0]] · Digest
- 2026-02-11 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-11-add-instructions-command-to-view-and-toggle-custom-instruction-files|Add /instructions command to view and toggle custom instruction files]] · Change
- 2026-02-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-02-09-we-re-beginning-to-roll-out-a-test-for-ads-in-chatgpt-in-the-u-s-for-logged-in-a|Testing ads in ChatGPT (Free, Go)]] · Change
- 2026-02-06 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-06-added-memory-frontmatter-field-support-for-agents-enabling-persistent-memory-wit|Added memory frontmatter field support for agents, enabling persistent memory…]] · Change
- 2026-02-05 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-05-claude-now-automatically-records-and-recalls-memories-as-it-works|Claude now automatically records and recalls memories as it works]] · Change
- 2026-02-05 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-05-4-memory-and-personalization-changes-in-rust-v0-97-0|4 Memory and Personalization changes in rust-v0.97.0]] · Digest
- 2026-02-05 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-05-2-memory-and-personalization-changes-in-rust-v0-98-0|2 Memory and Personalization changes in rust-v0.98.0]] · Digest
- 2026-02-02 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-02-7-memory-and-personalization-changes-in-rust-v0-94-0|7 Memory and Personalization changes in rust-v0.94.0]] · Digest

**2026-01**

- 2026-01-31 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-31-6-memory-and-personalization-changes-in-rust-v0-93-0|6 Memory and Personalization changes in rust-v0.93.0]] · Digest
- 2026-01-30 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-30-better-handle-large-results-from-grep-and-glob-tools-to-avoid-memory-issues|Better handle large results from grep and glob tools to avoid memory issues]] · Change
- 2026-01-28 · <span class="tl-product tl-p26">**OpenCode**</span> · [[Changes/OpenCode/2026-01-28-2-memory-and-personalization-changes-in-v1-1-37|2 Memory and Personalization changes in v1.1.37]] · Digest
- 2026-01-27 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-27-9718-feat-tui-personality-dylan-hurd-oai|♯9718 feat(tui) /personality @dylan-hurd-oai]] · Change
- 2026-01-25 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-25-9674-feat-app-server-expose-personality-dylan-hurd-oai|♯9674 feat(app-server) Expose personality @dylan-hurd-oai]] · Change
- 2026-01-24 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-24-memory-loading-errors-are-handled-gracefully-without-user-warnings|Memory loading errors are handled gracefully without user warnings]] · Change
- 2026-01-23 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-23-memory-loading-no-longer-warns-when-outside-a-git-repository|Memory loading no longer warns when outside a Git repository]] · Change
- 2026-01-22 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-22-9644-feat-core-update-personality-on-turn-dylan-hurd-oai|♯9644 feat(core) update Personality on turn @dylan-hurd-oai]] · Change
- 2026-01-22 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-22-show-warning-when-repository-memory-fails-to-load|Show warning when repository memory fails to load]] · Change
- 2026-01-21 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-21-9459-feat-personality-introduce-model-personality-config-dylan-hurd-oai|♯9459 feat(personality) introduce model_personality config @dylan-hurd-oai]] · Change
- 2026-01-21 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-21-feat-a2a-introduce-memory-command-for-a2a-server-by-cocosheng-g-in-https-github|feat(a2a): Introduce /memory command for a2a server]] · Change
- 2026-01-19 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-19-3-memory-and-personalization-changes-in-v0-0-385|3 Memory and Personalization changes in v0.0.385]] · Digest
- 2026-01-16 · <span class="tl-product tl-p14">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-16-inject-repo-memories-in-the-prompt-and-add-memory-storage-tool-to-remember-facts|Inject repo memories in the prompt and add memory storage tool to remember facts…]] · Change
- 2026-01-15 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-01-15-when-reference-chat-history-is-enabled-chatgpt-can-now-more-reliably-find-specif|Improved memory for finding details from past chats (Plus & Pro)]] · Change
- 2026-01-09 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2026-01-09-2-memory-and-personalization-changes-in-v0-7-0|2 Memory and Personalization changes in v0.7.0]] · Digest
- 2026-01-07 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-01-07-we-re-starting-to-roll-out-health-a-dedicated-space-in-chatgpt-for-health-and-we|We’re starting to roll out Health, a dedicated space in ChatGPT for health…]] · Change
- 2026-01-07 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-07-feat-core-implement-jit-context-memory-loading-and-ui-sync-by-sandytao520-in-htt|feat(core): Implement JIT context memory loading and UI sync]] · Change

</details>

</details>

<details class="disclosure">
<summary>2025 · 67 entries (AnythingLLM 1 · ChatGPT 22 · Claude 3 · Codex CLI 1 · Cursor 3 · Dify 3 · ElevenLabs 1 · Gemini CLI 11 · LM Studio 3 · Midjourney 6 · Notion 1 · Open WebUI 5 · OpenHands 3 · Superwhisper 1 · Windsurf 2 · v0 1)</summary>

**2025-10**

- 2025-10-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-10-29-chatgpt-pulse-is-now-available-on-web-and-rolling-out-to-atlas-for-pro-users-wit|ChatGPT Pulse on Web]] · Expansion
- 2025-10-23 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2025-10-23-claude-s-memory-on-max-and-pro-plans|Claude’s memory on Max and Pro plans]] · Launch
- 2025-10-06 · <span class="tl-product tl-p33">**v0**</span> · [[Changes/v0/2025-10-06-custom-instructions-are-now-available-in-v0-use-preset-instructions-like-be-conc|Custom Instructions]] · Launch

**2025-09**

- 2025-09-25 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-09-25-we-re-launching-an-early-preview-of-chatgpt-pulse-for-pro-users-on-ios-and-andro-cf8064|Introducing ChatGPT Pulse for Pro users]] · Launch
- 2025-09-18 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2025-09-18-claude-s-memory-on-enterprise-plans|Claude’s memory on Enterprise plans]] · Launch
- 2025-09-18 · <span class="tl-product tl-p23">**Notion**</span> · [[Changes/Notion/2025-09-18-personalize-your-agent-s-instructions-and-memory|Personalize your Agent’s instructions and memory]] · Launch
- 2025-09-11 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2025-09-11-claude-s-memory-on-team-plans-and-incognito-chats-for-free-pro-max-and-team-plan|Claude’s memory on Team plans and incognito chats for free, Pro, Max, and Team plans]] · Launch

**2025-08**

- 2025-08-22 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-08-22-an-improvement-to-projects-is-now-available-when-creating-a-project-users-have-t-87f79a|An improvement to projects is now available]] · Launch

**2025-07**

- 2025-07-30 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2025-07-30-personalized-feeds-for-images-and-video|Personalized feeds for images and video]] · Launch
- 2025-07-14 · <span class="tl-product tl-p11">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-14-elevencreative-studio|ElevenCreative Studio]] · Launch
- 2025-07-03 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-07-03-memories-is-now-ga-since-1-0-we-ve-improved-memory-generation-quality-added-in-e|Memories (now GA)]] · Launch

**2025-06**

- 2025-06-04 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-06-04-memories|Memories]] · Launch
- 2025-06-03 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-06-03-opt-in-reminders-e08369|Opt‑in reminders]] · Launch

**2025-05**

- 2025-05-01 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2025-05-01-more-about-omni-reference|More about Omni-Reference]] · Launch

**2025-04**

- 2025-04-04 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2025-04-04-v7-is-the-first-model-to-have-model-personalization-turned-on-by-default|V7 is the first model to have model personalization turned on by default]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 52 (AnythingLLM 1 · ChatGPT 18 · Codex CLI 1 · Cursor 1 · Dify 3 · Gemini CLI 11 · LM Studio 3 · Midjourney 3 · Open WebUI 5 · OpenHands 3 · Superwhisper 1 · Windsurf 2)</summary>

**2025-12**

- 2025-12-22 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-12-22-today-we-re-rolling-out-your-year-with-chatgpt-an-optional-personalized-end-of-y-740eb1|Your Year with ChatGPT]] · Change
- 2025-12-21 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2025-12-21-channel-image-upload-handling-was-optimized-to-process-and-store-compressed-imag|🖼️ Channel image upload handling was optimized to process and store compressed…]] · Change
- 2025-12-19 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-12-19-in-addition-to-selecting-a-base-style-and-tone-preset-like-candid-and-friendly-y-21da79|New detailed characteristic controls]] · Change
- 2025-12-16 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-16-chore-tests-remove-obsolete-test-for-hierarchical-memory-by-pareshjoshij-in-http|chore(tests): remove obsolete test for hierarchical memory]] · Change

**2025-11**

- 2025-11-24 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-11-24-shopping-research-is-a-new-interactive-experience-that-helps-you-find-the-right-0a021d|Shopping research in ChatGPT]] · Change
- 2025-11-07 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-11-07-previously-changes-you-made-to-your-chatgpt-personality-or-custom-instructions-o|Personality and custom instructions now apply to all chats]] · Change
- 2025-11-07 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-07-feat-core-implement-granular-memory-loaders-for-jit-architecture-by-abhipatel12|feat(core): Implement granular memory loaders for JIT architecture]] · Change

**2025-10**

- 2025-10-30 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-10-30-longer-memory-for-more-personalized-responses|Longer memory for more personalized responses]] · Change
- 2025-10-28 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-10-28-longer-memory-for-more-personalized-responses|Longer memory for more personalized responses]] · Change
- 2025-10-24 · <span class="tl-product tl-p31">**Superwhisper**</span> · [[Changes/Superwhisper/2025-10-24-record-from-system-audio-now-uses-less-data-memory|Record from system audio now uses less data & memory]] · Change
- 2025-10-22 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-22-part-4-6-feat-telemetry-add-memory-monitor-with-activity-aware-recording-and-tes|Part 4/6 feat(telemetry): add memory monitor with activity-aware recording and tests]] · Change
- 2025-10-15 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-10-15-chatgpt-now-manages-saved-memories-automatically-by-keeping-the-most-relevant-de-997f64|ChatGPT can now automatically manage saved memories so it’s even better…]] · Change
- 2025-10-14 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-10-14-longer-memory-for-more-personalized-responses-775c35|Longer memory for more personalized responses]] · Change
- 2025-10-08 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-10-08-longer-memory-for-more-personalized-responses-8c6877|Longer memory for more personalized responses]] · Change
- 2025-10-02 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2025-10-02-heya-everyone-we-re-doing-a-ranking-party-for-styles|Heya everyone, we're doing a ranking party for styles !]] · Change
- 2025-10-02 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2025-10-02-ps-the-bottom-of-every-style-has-an-sref-code-and-a-button-the-top-1000-raters-g|PS: The bottom of every style has an --sref code and a ❤️ button]] · Change

**2025-09**

- 2025-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-09-29-turn-off-memory-so-chatgpt-won-t-save-and-use-memories-when-responding|Turn off memory, so ChatGPT won’t save and use memories when responding]] · Change
- 2025-09-24 · <span class="tl-product tl-p19">**LM Studio**</span> · [[Changes/LM Studio/2025-09-24-2-memory-and-personalization-changes-in-lm-studio-0-3-27|2 Memory and Personalization changes in LM Studio 0.3.27]] · Digest
- 2025-09-23 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-23-new-review-commands-review-specific-commit-against-a-base-branch-or-custom-instr|New /review commands…]] · Change
- 2025-09-22 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-09-22-longer-memory-for-more-personalized-responses|Longer memory for more personalized responses]] · Change
- 2025-09-15 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-09-15-personalization-no-longer-opens-in-a-separate-modal-you-can-manage-personalizati|Personalization settings are now in Settings]] · Change
- 2025-09-04 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-04-2-memory-and-personalization-changes-in-v0-3-0|2 Memory and Personalization changes in v0.3.0]] · Digest

**2025-08**

- 2025-08-28 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2025-08-28-pdf-export-content-mismatch-fixed-resolved-an-issue-where-exporting-a-pdf-of-one|📄 PDF Export Content Mismatch Fixed]] · Change
- 2025-08-28 · <span class="tl-product tl-p32">**Windsurf**</span> · [[Changes/Windsurf/2025-08-28-memory-improvements|Memory improvements]] · Change
- 2025-08-18 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-08-18-longer-memory-for-more-personalized-responses-4644fd|Longer memory for more personalized responses]] · Change
- 2025-08-15 · <span class="tl-product tl-p1">**AnythingLLM**</span> · [[Changes/AnythingLLM/2025-08-15-well-now-we-have-the-best-of-both-worlds-documents-are-scoped-to-a-workspace-thr|Well, now we have the best of both worlds]] · Change
- 2025-08-14 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-14-3-memory-and-personalization-changes-in-v0-1-21|3 Memory and Personalization changes in v0.1.21]] · Digest
- 2025-08-12 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-12-feat-drop-load-memory-from-include-directories-option-from-cli-args-by-y-okt-in|feat: drop load-memory-from-include-directories option from cli args]] · Change
- 2025-08-11 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2025-08-11-chore-remove-unused-variable-pruned-memory-by-hyongtao-db-in-https-github-com-la|Chore: remove unused variable pruned_memory]] · Change
- 2025-08-09 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2025-08-09-enhanced-memory-stability-and-security-refactored-memory-update-and-delete-opera|🧠 Enhanced Memory Stability and Security]] · Change
- 2025-08-06 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-06-2-memory-and-personalization-changes-in-v0-1-18|2 Memory and Personalization changes in v0.1.18]] · Digest
- 2025-08-05 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-05-2-memory-and-personalization-changes-in-v0-1-17|2 Memory and Personalization changes in v0.1.17]] · Digest
- 2025-08-02 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-02-2-memory-and-personalization-changes-in-v0-1-16|2 Memory and Personalization changes in v0.1.16]] · Digest

**2025-07**

- 2025-07-30 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-30-feat-memory-make-directory-search-limit-on-memory-discovery-configurable-with-se|feat(memory): make directory search limit on memory discovery configurable…]] · Change
- 2025-07-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-07-29-personalize-responses-based-on-your-past-chats-if-memory-is-on-using-examples-an|Personalize responses based on your past chats if memory is on, using examples…]] · Change
- 2025-07-25 · <span class="tl-product tl-p13">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-25-feat-memory-make-directory-search-limit-on-memory-discovery-configurable-with-se|feat(memory): make directory search limit on memory discovery configurable…]] · Change
- 2025-07-16 · <span class="tl-product tl-p27">**OpenHands**</span> · [[Changes/OpenHands/2025-07-16-introduced-new-memory-ui-feature-by-amanape-in-https-github-com-all-hands-ai-ope|Introduced new Memory UI feature]] · Change

**2025-06**

- 2025-06-12 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-06-12-improvements-to-memory-to-reference-past-chats-in-a-project|Improvements to memory to reference past chats in a project]] · Change

**2025-05**

- 2025-05-29 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2025-05-29-refined-memory-error-handling-enhanced-stability-during-memory-related-operation|🧠 Refined Memory Error Handling]] · Change
- 2025-05-26 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2025-05-26-2-memory-and-personalization-changes-in-v0-6-11|2 Memory and Personalization changes in v0.6.11]] · Digest
- 2025-05-23 · <span class="tl-product tl-p19">**LM Studio**</span> · [[Changes/LM Studio/2025-05-23-add-offload-kv-cache-to-gpu-memory-option-to-model-load-options-and-gpu-settings|Add "Offload KV Cache to GPU Memory" option to model load options and GPU settings]] · Change
- 2025-05-08 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-05-08-saved-memories-and-chat-history-are-offered-only-to-plus-and-pro-accounts-free-t|Saved memories and Chat history are offered only to Plus and Pro…]] · Change
- 2025-05-08 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-05-08-enhanced-memory-rolling-out-to-all-plus-and-pro-users-including-the-eu-the-new-m|Enhanced memory rolling out to all Plus and Pro users (including the EU)]] · Change

**2025-04**

- 2025-04-16 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-04-16-chatgpt-can-also-use-memories-to-inform-search-queries-when-chatgpt-searches-the|Memory with Search]] · Change
- 2025-04-09 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2025-04-09-feat-agent-node-add-memory-by-nov1c444-in-https-github-com-langgenius-dify-pull|feat: agent node add memory]] · Change
- 2025-04-02 · <span class="tl-product tl-p32">**Windsurf**</span> · [[Changes/Windsurf/2025-04-02-improvements-to-memories|Improvements to Memories]] · Change

**2025-03**

- 2025-03-31 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2025-03-31-we-re-now-in-round-3-of-the-v7-image-rating-party|We're now in ROUND 3 of the V7 image rating party]] · Change
- 2025-03-27 · <span class="tl-product tl-p19">**LM Studio**</span> · [[Changes/LM Studio/2025-03-27-2-memory-and-personalization-changes-in-lm-studio-0-3-14|2 Memory and Personalization changes in LM Studio 0.3.14]] · Digest

**2025-02**

- 2025-02-24 · <span class="tl-product tl-p27">**OpenHands**</span> · [[Changes/OpenHands/2025-02-24-enable-memory-condensation-from-settings-page-by-csmith49-in-https-github-com-al|Enable memory condensation from settings page]] · Change
- 2025-02-19 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-02-19-0-46-9-memory-and-performances-fixes-composer-chat-remembers-your-last-mode-sele|0.46.9: Memory and performances fixes, composer/chat remembers your last mode…]] · Change

**2025-01**

- 2025-01-07 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2025-01-07-database-and-memory-optimizations-that-not-only-improve-performance-but-they-ll|Database and memory optimizations that not only improve performance but they'll…]] · Change
- 2025-01-07 · <span class="tl-product tl-p27">**OpenHands**</span> · [[Changes/OpenHands/2025-01-07-developer-mode-now-defaults-to-storing-data-on-the-filesystem-instead-of-in-memo|Developer mode now defaults to storing data on the filesystem instead of in-memory…]] · Change

</details>

</details>

<details class="disclosure">
<summary>2024 · 28 entries (ChatGPT 2 · Cline 2 · Dify 8 · Midjourney 11 · Notion 1 · Open WebUI 2 · OpenHands 2)</summary>

**2024-12**

- 2024-12-16 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2024-12-16-flagship-features|Flagship features]] · Launch
- 2024-12-16 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2024-12-16-more-features-information|More Features / Information]] · Launch
- 2024-12-16 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2024-12-16-we-re-releasing-an-early-version-of-our-new-model-personalization-infrastructure|we’re releasing an early version of our new model personalization infrastructure today]] · Launch

**2024-07**

- 2024-07-13 · <span class="tl-product tl-p27">**OpenHands**</span> · [[Changes/OpenHands/2024-07-13-arch-deprecating-recall-action-and-search-memory-by-xingyaoww-in-https-github-co|arch: deprecating recall action and search_memory]] · Policy

**2024-06**

- 2024-06-18 · <span class="tl-product tl-p23">**Notion**</span> · [[Changes/Notion/2024-06-18-unlock-your-company-s-memory|Unlock your company’s memory]] · Launch
- 2024-06-12 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2024-06-12-what-is-model-personalization|What is Model Personalization?]] · Launch
- 2024-06-12 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2024-06-12-model-personalization-requirements|Model Personalization Requirements]] · Launch
- 2024-06-12 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2024-06-12-please-note|PLEASE NOTE]] · Launch
- 2024-06-12 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2024-06-12-how-do-i-use-model-personalization|How do I use Model Personalization?]] · Launch
- 2024-06-12 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2024-06-12-we-re-releasing-an-early-test-version-of-model-personalization-today-here-s-how|We're releasing an early test version of model personalization today]] · Launch

**2024-04**

- 2024-04-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2024-04-29-memory-is-now-available-to-all-chatgpt-plus-users-except-in-europe-korea-where-w-4db29a|Memory is now available to Plus users]] · Expansion
- 2024-04-25 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2024-04-25-you-can-now-enable-memory-in-the-llm-node-within-your-chatflow-and-customize-the|Enable memory in the LLM node within your chatflow, and customize the query prompt…]] · Change

<details class="disclosure">
<summary>Fixes, digests and other changes · 16 (ChatGPT 1 · Cline 2 · Dify 7 · Midjourney 3 · Open WebUI 2 · OpenHands 1)</summary>

**2024-11**

- 2024-11-26 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2024-11-26-llm-memory-processing-corrected-errors-in-llm-memory-handling-11103-and-11106|LLM Memory Processing: Corrected errors in LLM memory handling]] · Change

**2024-10**

- 2024-10-23 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2024-10-23-custom-icon-restoration-we-ve-reintroduced-the-flexibility-and-personalization-o|Custom Icon Restoration]] · Change

**2024-09**

- 2024-09-06 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2024-09-06-personalization-for-the-niji-anime-model-is-available-today|Personalization for Niji]] · Change

**2024-08**

- 2024-08-14 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2024-08-14-enhancing-llm-memory-with-conversation-variables-and-variable-assigners-https-di|Enhancing LLM Memory with Conversation Variables and Variable…]] · Change
- 2024-08-11 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2024-08-11-adds-option-to-add-custom-instructions-to-the-end-of-the-system-prompt|Adds option to add custom instructions to the end of the system prompt]] · Change

**2024-07**

- 2024-07-28 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2024-07-28-quality-of-life-improvements-like-markdown-rendering-memory-optimizations-better|Quality of life improvements like markdown rendering, memory optimizations, better…]] · Change
- 2024-07-08 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2024-07-08-2-memory-and-personalization-changes-in-0-6-13|2 Memory and Personalization changes in 0.6.13]] · Digest
- 2024-07-05 · <span class="tl-product tl-p27">**OpenHands**</span> · [[Changes/OpenHands/2024-07-05-ci-for-colima-modify-cpu-count-and-memory-by-smartmanoj-in-https-github-com-open|CI: For colima, modify CPU count and memory]] · Change

**2024-06**

- 2024-06-17 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2024-06-17-editable-memories-adds-the-capability-to-modify-memories|🧠 Editable Memories: Adds the capability to modify memories]] · Change
- 2024-06-14 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2024-06-14-2-memory-and-personalization-changes-in-0-6-11|2 Memory and Personalization changes in 0.6.11]] · Digest

**2024-05**

- 2024-05-19 · <span class="tl-product tl-p24">**Open WebUI**</span> · [[Changes/Open WebUI/2024-05-19-experimental-memory-feature-manually-input-personal-information-you-want-llms-to|🧠 Experimental Memory Feature]] · Change

**2024-04**

- 2024-04-08 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2024-04-08-compared-to-the-regular-workflow-app-type-chatflow-adds-chat-specific-features-s|Compared to the regular Workflow app type, Chatflow adds chat-specific features such…]] · Change

**2024-03**

- 2024-03-21 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2024-03-21-these-ratings-help-improve-our-algorithms-populate-the-explore-page-and-also-wil|These ratings help improve our algorithms, populate the explore page, and also will…]] · Change
- 2024-03-13 · <span class="tl-product tl-p22">**Midjourney**</span> · [[Changes/Midjourney/2024-03-13-our-team-is-also-working-on-new-special-features-like-model-personalization-that|Our team is also working on new special features like model personalization…]] · Change

**2024-02**

- 2024-02-13 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2024-02-13-we-re-testing-memory-with-chatgpt-remembering-things-you-discuss-across-all-chat-9872c8|Memory and new controls for ChatGPT]] · Change

**2024-01**

- 2024-01-05 · <span class="tl-product tl-p10">**Dify**</span> · [[Changes/Dify/2024-01-05-feat-optimize-memory-invoke-error-output-by-takatost-in-https-github-com-langgen|feat: optimize memory & invoke error output]] · Change

</details>

</details>

<details class="disclosure" open>
<summary>2023 · 4 entries (ChatGPT 3 · Descript 1)</summary>

**2023-08**

- 2023-08-21 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-08-21-custom-instructions-are-now-available-to-users-in-the-european-union-united-king-cfc1d5|Custom instructions are now available to users in the EU & UK]] · Expansion
- 2023-08-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-08-09-custom-instructions-are-now-available-to-chatgpt-users-on-the-free-plan-except-f-963d1e|Custom instructions are now available to free users]] · Expansion

<details class="disclosure">
<summary>Fixes, digests and other changes · 2 (ChatGPT 1 · Descript 1)</summary>

**2023-12**

- 2023-12-05 · <span class="tl-product tl-p8">**Descript**</span> · [[Changes/Descript/2023-12-05-command-e-https-help-descript-com-hc-en-us-articles-10255582172173-keyboard-shor|Command…]] · Change

**2023-07**

- 2023-07-20 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]] · Change

</details>

</details>

</div>
<!-- chronolog:end -->