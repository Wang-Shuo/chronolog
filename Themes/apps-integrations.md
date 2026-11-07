---
created: '2023-03-23'
date: '2026-11-06'
description: 'Research question: how do the tracked products connect to outside tools,
  and in what unit do they package those connections?'
machine_hash: d20eea0d4f3d64b7ba9ea77d74efaf82f95a22667a1c11aa4a7a0eeb954b836d
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
- Granola
- Lovable
- Manus
- Ollama
- Open WebUI
- OpenClaw
- OpenCode
- OpenHands
- Replit
- Runway
- Suno
- Windsurf
- v0
publication: active
status: official
tags:
- theme
- moc
theme: apps-integrations
title: Apps and Integrations
---

<!-- chronolog:begin region="header" -->
# Apps and Integrations

1,471 tracked changes across Aider, ChatGPT, Claude, Claude Code, Cline, Codex CLI, Cursor, Dify, ElevenLabs, Gamma, Gemini, Gemini CLI, GitHub Copilot CLI, Google Antigravity, Granola, Lovable, Manus, Ollama, Open WebUI, OpenClaw, OpenCode, OpenHands, Replit, Runway, Suno, Windsurf and v0 · 2023-03-23 → 2026-11-06 · OpenClaw averages 18.4 cards per release, ElevenLabs 8.1, Codex CLI 8.0, Open WebUI 7.6, Gemini CLI 7.5, Dify 7.2, Claude Code 7.0, GitHub Copilot CLI 6.3, OpenCode 6.0, Google Antigravity 5.0, Replit 4.9, Cursor 4.0, Lovable 3.9, OpenHands 3.8, Aider 3.7, Cline 3.0, Ollama 3.0, v0 2.9, Windsurf 2.6, Suno 2.1, Gamma 1.8, ChatGPT 1.7, Gemini 1.5, Claude 1.3, Manus 1.2, Granola 1.0, Runway 1.0
<!-- chronolog:end -->

## Research summary
<!-- chronolog:begin region="narrative" -->
**Research question: how do the tracked products connect to outside tools, and in what unit do they package those connections?**

ChatGPT's [2023-03-23 plugins announcement](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#introducing-plugins-in-chatgpt) ([[Releases/ChatGPT/chatgpt-2023-03-23-introducing-plugins-in-chatgpt-8c6badc8|archived]]) introduces experimental plugins, tools designed for language models that access up-to-date information, run computations or use third-party services. The [2025-06-04 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#custom-connectors-via-model-context-protocol-pro-team-enterprise-edu) ([[Releases/ChatGPT/chatgpt-2025-06-04-custom-connectors-via-model-context-protocol-pro-team-enterprise-a1bc36f5|archived]]) lets admins and users build and deploy custom connectors to proprietary systems using the Model Context Protocol (MCP), and the [2025-12-18 app directory](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#introducing-the-app-directory-in-chatgpt) ([[Releases/ChatGPT/chatgpt-2025-12-18-introducing-the-app-directory-in-chatgpt-c4ab90ba|archived]]) lists connectors as apps. The [2026-07-09 Work announcement](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#introducing-chatgpt-work) ([[Releases/ChatGPT/chatgpt-2026-07-09-introducing-chatgpt-work-eff9f272|archived]]) replaces the App Directory with a Plugin Directory whose plugins package skills, apps and app templates, and the [2026-09-11 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#planned-custom-gpt-retirement-and-migration-to-plugins) ([[Releases/ChatGPT/chatgpt-2026-09-11-planned-custom-gpt-retirement-and-migration-to-plugins-05b21afb|archived]]) plans to retire custom GPTs, introduced on [2023-11-06](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#introducing-gpts) ([[Releases/ChatGPT/chatgpt-2023-11-06-introducing-gpts-3721c457|archived]]), with a migration path to plugins.

Cursor's [0.45 release on 2025-01-23](https://cursor.com/changelog/0-45-x) ([[Releases/Cursor/cursor-2025-01-23-0-45-x-https-cursor-com-changelog-0-45-x-c162d228|archived]]) adds MCP support, and [Cursor 1.0 on 2025-06-04](https://cursor.com/changelog/1-0) ([[Releases/Cursor/cursor-2025-06-04-1-0-https-cursor-com-changelog-1-0-237767ca|archived]]) adds one-click MCP setup with OAuth. The [2025-06-12 release](https://cursor.com/changelog/1-1) ([[Releases/Cursor/cursor-2025-06-12-1-1-https-cursor-com-changelog-1-1-0f0190fc|archived]]) lets teams launch Background Agents from Slack, where Cursor reads the whole thread before starting. The [2026-02-17 release](https://cursor.com/changelog/2-5) ([[Releases/Cursor/cursor-2026-02-17-2-5-https-cursor-com-changelog-2-5-82892320|archived]]) introduces plugins on the Cursor Marketplace, which package skills, subagents, MCP servers, hooks and rules into a single install, and the [2026-03-03 release](https://cursor.com/changelog/2-6) ([[Releases/Cursor/cursor-2026-03-03-2-6-https-cursor-com-changelog-2-6-0fa7f1a3|archived]]) adds MCP Apps with interactive interfaces such as Figma diagrams inside Cursor.

Claude Code's archive opens with a plugin marketplace in place: [v2.0.73 on 2025-12-19](https://github.com/anthropics/claude-code/releases/tag/v2.0.73) ([[Releases/Claude Code/claude-code-2025-12-19-v2-0-73-github-271620087-160adbe9|archived]]) adds search filtering to the plugin discover screen. [v2.1.16 on 2026-01-22](https://github.com/anthropics/claude-code/releases/tag/v2.1.16) ([[Releases/Claude Code/claude-code-2026-01-22-v2-1-16-github-279146529-0e5b3428|archived]]) adds native plugin management to the VS Code extension, [v2.1.198 on 2026-07-01](https://github.com/anthropics/claude-code/releases/tag/v2.1.198) ([[Releases/Claude Code/claude-code-2026-07-01-v2-1-198-github-347599701-9cec0dab|archived]]) makes Claude in Chrome generally available, and [v2.1.287 on 2026-10-01](https://github.com/anthropics/claude-code/releases/tag/v2.1.287) ([[Releases/Claude Code/claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87|archived]]) adds Claude Mods, through which plugins may modify deeper behavior.

**Uncertainty and scope:** this editorial summary covers ChatGPT, Claude Code and Cursor; the timeline includes all tracked products and Claude Code coverage starts on 2025-12-19, after its plugin system already existed, so shared words such as “plugin”, “app” and “connector” name each product's own packaging unit and do not indicate interoperable or equivalent integrations.
<!-- chronolog:end -->

## Key moments
<!-- chronolog:begin region="moments" -->
Selected automatically from launches and standalone announcements.

| Quarter | Aider | ChatGPT | Claude | Claude Code | Cline | Codex CLI | Cursor | Dify | ElevenLabs | Gamma | Gemini | Gemini CLI | GitHub Copilot CLI | Google Antigravity | Granola | Lovable | Manus | Ollama | Open WebUI | OpenClaw | OpenCode | OpenHands | Replit | Runway | Suno | Windsurf | v0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **First in archive** | <time datetime="2023-07-12">2023-07-12</time> [[Changes/Aider/2023-07-12-install-docs-link-to-neovim-plugin-https-github-com-joshuavial-aider-nvim-by-jos\|Install docs link to NeoVim plugin((source link)]] | <time datetime="2023-03-23">2023-03-23</time> [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581\|We are announcing experimental support for AI plugins in ChatGPT]] | <time datetime="2026-02-24">2026-02-24</time> [[Changes/Claude/2026-02-24-cowork-plugins-and-admin-controls\|Cowork plugins and admin controls]] | <time datetime="2025-12-19">2025-12-19</time> [[Changes/Claude Code/2025-12-19-2-apps-and-integrations-changes-in-v2-0-73\|2 Apps and Integrations changes in v2.0.73]] | <time datetime="2024-09-09">2024-09-09</time> [[Changes/Cline/2024-09-09-commands-now-run-directly-in-your-terminal-thanks-to-vscode-1-93-s-new-shell-int\|Commands now run directly in your terminal thanks to VSCode 1.93's new shell…]] | <time datetime="2025-07-19">2025-07-19</time> [[Changes/Codex CLI/2025-07-19-https-github-com-openai-codex-pull-1571-fixes-a-longstanding-issue-where-we-fail\|(source link) fixes a longstanding issue where we failed…]] | <time datetime="2023-05-04">2023-05-04</time> [[Changes/Cursor/2023-05-04-one-click-extension-import-from-vs-code-beta-as-a-highly-requested-feature-we-re\|One-Click Extension Import from VS Code (beta)]] | <time datetime="2023-05-25">2023-05-25</time> [[Changes/Dify/2023-05-25-3-apps-and-integrations-changes-in-0-2-2\|3 Apps and Integrations changes in 0.2.2]] | <time datetime="2025-04-07">2025-04-07</time> [[Changes/ElevenLabs/2025-04-07-text-to-speech\|Text to speech]] | <time datetime="2025-08-08">2025-08-08</time> [[Changes/Gamma/2025-08-08-we-ve-just-launched-our-generate-api-in-beta-for-gamma-pro-users-now-you-can-cre\|We’ve just launched our Generate API in beta for Gamma Pro users! Now you can…]] | <time datetime="2023-09-19">2023-09-19</time> [[Changes/Gemini/2023-09-19-bard-can-now-access-helpful-information-from-google-apps-and-services\|Bard can now access helpful information from Google apps and services]] | <time datetime="2025-07-01">2025-07-01</time> [[Changes/Gemini CLI/2025-07-01-feat-add-support-to-remote-mcp-servers-for-custom-http-headers-by-aspiers-in-htt\|feat: add support to remote MCP servers for custom HTTP headers]] | <time datetime="2025-10-08">2025-10-08</time> [[Changes/GitHub Copilot CLI/2025-10-08-added-validation-for-mcp-server-names-fixes-https-github-com-github-copilot-cli\|Added validation for MCP server names…]] | <time datetime="2025-12-04">2025-12-04</time> [[Changes/Google Antigravity/2025-12-04-google-one-integration\|Google One integration]] | <time datetime="2025-09-08">2025-09-08</time> [[Changes/Granola/2025-09-08-with-new-people-and-companies-views-plus-attio-and-zapier-integrations\|Three new features to help you build better customer relationships]] | <time datetime="2024-12-03">2024-12-03</time> [[Changes/Lovable/2024-12-03-introducing-feedback-lovable-dev-for-feature-and-integration-request\|Introducing feedback.lovable.dev for feature and integration request]] | <time datetime="2025-11-18">2025-11-18</time> [[Changes/Manus/2025-11-18-manus-can-now-perform-tasks-directly-in-your-browser-autonomously-it-securely-wo\|Introducing Manus Browser Operator]] | <time datetime="2023-08-10">2023-08-10</time> [[Changes/Ollama/2023-08-10-ollama-langchain-integration-https-python-langchain-com-docs-integrations-llms-o\|Ollama 🦜️🔗 LangChain…]] | <time datetime="2024-03-21">2024-03-21</time> [[Changes/Open WebUI/2024-03-21-webhook-integration-now-you-can-subscribe-to-new-user-sign-up-events-via-webhook\|🔗 Webhook Integration: Now you can subscribe to new user sign-up events via webhook]] | <time datetime="2026-06-30">2026-06-30</time> [[Changes/OpenClaw/2026-06-30-34-apps-and-integrations-changes-in-v2026-6-11\|34 Apps and Integrations changes in v2026.6.11]] | <time datetime="2025-12-29">2025-12-29</time> [[Changes/OpenCode/2025-12-29-core-install-local-plugin-dependencies-from-package-json\|Core Install local plugin dependencies from package.json]] | <time datetime="2024-06-04">2024-06-04</time> [[Changes/OpenHands/2024-06-04-2-apps-and-integrations-changes-in-0-6-1\|2 Apps and Integrations changes in 0.6.1]] | <time datetime="2024-12-13">2024-12-13</time> [[Changes/Replit/2024-12-13-more-beautiful-apps-improved-support-for-responsive-react-apps-allows-you-to-cre\|More Beautiful Apps: Improved support for responsive React apps allows you…]] | <time datetime="2025-10-14">2025-10-14</time> [[Changes/Runway/2025-10-14-apps-are-an-ever-growing-collection-of-use-case-specific-workflows-that-make-it\|Apps]] | <time datetime="2026-07-15">2026-07-15</time> [[Changes/Suno/2026-07-15-tap-the-icon-and-find-suno-in-your-imessage-app-extensions\|Tap the + icon and find Suno in your iMessage app extensions]] | <time datetime="2025-04-02">2025-04-02</time> [[Changes/Windsurf/2025-04-02-misc\|Misc]] | <time datetime="2025-10-31">2025-10-31</time> [[Changes/v0/2025-10-31-we-launched-a-new-integration-wizard-for-connecting-integrations-and-running-scr\|Integration Wizard]] |
| 2026 Q4 | · | · | · | · | · | · | <time datetime="2026-10-13">2026-10-13</time> [[Changes/Cursor/2026-10-13-apps-for-your-stack\|Apps for your stack]] | · | <time datetime="2026-10-19">2026-10-19</time> [[Changes/ElevenLabs/2026-10-19-sdk-releases\|SDK releases]]<br><time datetime="2026-10-12">2026-10-12</time> [[Changes/ElevenLabs/2026-10-12-sdk-releases\|SDK releases]] | <time datetime="2026-10-26">2026-10-26</time> [[Changes/Gamma/2026-10-26-introducing-gamma-5\|Introducing Gamma 5]] | <time datetime="2026-10-13">2026-10-13</time> [[Changes/Gemini/2026-10-13-an-easier-way-to-customize-how-gemini-works-for-you-and-more-connected-apps\|An easier way to customize how Gemini works for you and more connected apps]] | · | · | <time datetime="2026-10-29">2026-10-29</time> [[Changes/Google Antigravity/2026-10-29-partner-plugins-in-the-marketplace-and-plugin-sign-in\|Partner plugins in the Marketplace and plugin sign-in]]<br><time datetime="2026-10-28">2026-10-28</time> [[Changes/Google Antigravity/2026-10-28-conversation-navigator-and-third-party-tools-notice\|Conversation navigator and third party tools notice]] | · | <time datetime="2026-11-02">2026-11-02</time> [[Changes/Lovable/2026-11-02-connect-your-app-to-bamboohr\|Connect your app to BambooHR]]<br><time datetime="2026-10-27">2026-10-27</time> [[Changes/Lovable/2026-10-27-connect-your-app-to-scrive\|Connect your app to Scrive]] | · | · | · | · | <time datetime="2026-11-06">2026-11-06</time> [[Changes/OpenCode/2026-11-06-shared-mcp-connections\|Shared MCP Connections]]<br><time datetime="2026-10-30">2026-10-30</time> [[Changes/OpenCode/2026-10-30-managed-policy-integration-use-covers-integrations-only\|Managed policy: integration.use covers integrations only]] | · | <time datetime="2026-10-23">2026-10-23</time> [[Changes/Replit/2026-10-23-keep-your-apps-running-when-credits-run-out\|Keep your apps running when credits run out]]<br><time datetime="2026-10-02">2026-10-02</time> [[Changes/Replit/2026-10-02-jev-is-now-available-through-replit-ai-integrations\|Jev is now available through Replit AI Integrations]] | · | · | · | · |
| 2026 Q3 | · | <time datetime="2026-08-28">2026-08-28</time> [[Changes/ChatGPT/2026-08-28-you-can-now-connect-multiple-accounts-for-gmail-google-calendar-and-google-conta-b4c5da\|Connect multiple Google accounts to ChatGPT]] | <time datetime="2026-09-25">2026-09-25</time> [[Changes/Claude/2026-09-25-build-plugins-for-claude\|Build plugins for Claude]]<br><time datetime="2026-09-16">2026-09-16</time> [[Changes/Claude/2026-09-16-claude-cowork-comes-to-every-conversation\|Claude Cowork comes to every conversation]] | <time datetime="2026-09-17">2026-09-17</time> [[Changes/Claude Code/2026-09-17-added-plugin-install-plugin-marketplace-source-which-offers-to-add-the-marketpla\|Added /plugin install plugin --marketplace source, which offers to add…]] | · | <time datetime="2026-07-08">2026-07-08</time> [[Changes/Codex CLI/2026-07-08-remote-plugins-are-now-enabled-by-default-with-richer-catalog-rows-npm-marketpla\|Remote plugins are now enabled by default, with richer catalog rows, npm marketplace…]] | <time datetime="2026-09-23">2026-09-23</time> [[Changes/Cursor/2026-09-23-integrations\|Integrations]] | · | · | · | · | · | · | · | · | · | · | · | · | <time datetime="2026-09-19">2026-09-19</time> [[Changes/OpenClaw/2026-09-19-you-can-now-ask-btw-side-questions-about-photos-attached-to-the-current-message\|Ask /btw side questions about photos attached to the current message when using…]]<br><time datetime="2026-09-11">2026-09-11</time> [[Changes/OpenClaw/2026-09-11-you-can-now-search-installed-and-available-plugins-together-browse-by-purpose-an\|Search installed and available plugins together, browse by purpose, and keep…]] | · | · | · | <time datetime="2026-09-23">2026-09-23</time> [[Changes/Runway/2026-09-23-runway-mcp-is-now-available-on-cursor-s-marketplace-making-it-easy-to-bring-runw\|Runway MCP on Cursor]] | <time datetime="2026-09-02">2026-09-02</time> [[Changes/Suno/2026-09-02-copy-and-duplicate-plugins\|Copy and duplicate plugins]] | · | · |
| 2026 Q2 | · | · | · | · | · | · | · | · | · | · | · | · | <time datetime="2026-06-05">2026-06-05</time> [[Changes/GitHub Copilot CLI/2026-06-05-mcp-tools-added-or-removed-by-a-server-mid-turn-are-now-available-immediately-in\|MCP tools added or removed by a server mid-turn are now available immediately…]] | · | · | · | · | <time datetime="2026-04-12">2026-04-12</time> [[Changes/Ollama/2026-04-12-hermes-agent-https-docs-ollama-com-integrations-hermes-ollama-integration-guide\|Hermes agent((source link) Ollama integration guide…]] | · | archive begins <time datetime="2026-06-30">2026-06-30</time> | · | · | · | · | · | <time datetime="2026-06-16">2026-06-16</time> [[Changes/Windsurf/2026-06-16-devin-local\|Devin Local]] | · |
| 2026 Q1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | <span class="not-archived">not archived</span> | · | · | · | · | · | · | · |
| 2025 Q4 | · | · | · | archive begins <time datetime="2025-12-19">2025-12-19</time> | · | · | · | · | · | · | · | · | · | archive begins <time datetime="2025-11-18">2025-11-18</time> | · | · | <time datetime="2025-11-18">2025-11-18</time> [[Changes/Manus/2025-11-18-manus-can-now-perform-tasks-directly-in-your-browser-autonomously-it-securely-wo\|Introducing Manus Browser Operator]] | · | · | <span class="not-archived">not archived</span> | archive begins <time datetime="2025-12-19">2025-12-19</time> | · | · | · | · | · | <time datetime="2025-12-16">2025-12-16</time> [[Changes/v0/2025-12-16-you-can-now-connect-v0-to-your-linear-workspace-and-build-straight-from-your-bac\|Connect v0 to your Linear workspace and build straight from your backlog]] |
| 2025 Q2 → 2025 Q3 | · | · | archive begins <time datetime="2025-08-01">2025-08-01</time> | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2025-06-30">2025-06-30</time> | · | · | · | · | · | archive begins <time datetime="2025-06-28">2025-06-28</time> | archive begins <time datetime="2025-09-26">2025-09-26</time> | <span class="not-archived">not archived</span> | · | · | archive begins <time datetime="2025-05-11">2025-05-11</time> | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | · | · | · | archive begins <time datetime="2025-04-02">2025-04-02</time> | <span class="not-archived">not archived</span> |
| 2025 Q1 | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <time datetime="2025-02-19">2025-02-19</time> [[Changes/Cline/2025-02-19-introducing-mcp-marketplace-you-can-now-discover-and-install-the-best-mcp-server\|Introducing MCP Marketplace!]] | <span class="not-archived">not archived</span> | · | · | · | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | · | <span class="not-archived">not archived</span> | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | · | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |
| 2024 Q4 | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | · | <time datetime="2024-12-03">2024-12-03</time> [[Changes/Dify/2024-12-03-you-can-now-use-github-com-links-directly-for-dsls-instead-of-relying-on-raw-git\|Use github.com links directly for DSLs instead of relying on raw.githubusercontent.com]] | archive begins <time datetime="2024-10-13">2024-10-13</time> | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2024-12-03">2024-12-03</time> | <span class="not-archived">not archived</span> | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2024-12-13">2024-12-13</time> | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |

First in archive: each product's earliest tracked change in this theme. "·" marks a quarter without a key moment, and "not archived" a quarter before the product's archive begins. Archives begin: Aider 2023-06-07 · ChatGPT 2022-12-15 · Claude 2025-08-01 · Claude Code 2025-12-19 · Cline 2024-07-28 · Codex CLI 2025-06-30 · Cursor 2023-03-14 · Dify 2023-05-15 · ElevenLabs 2024-10-13 · Gamma 2024-02-14 · Gemini 2023-04-10 · Gemini CLI 2025-06-28 · GitHub Copilot CLI 2025-09-26 · Google Antigravity 2025-11-18 · Granola 2024-05-22 · Lovable 2024-12-03 · Manus 2025-05-11 · Ollama 2023-07-08 · Open WebUI 2024-02-23 · OpenClaw 2026-06-30 · OpenCode 2025-12-19 · OpenHands 2024-06-04 · Replit 2024-12-13 · Runway 2024-01-08 · Suno 2023-12-23 · Windsurf 2025-04-02 · v0 2025-10-01.
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
<label><input type="radio" name="timeline-product" id="tl-only-15"> Granola</label>
<label><input type="radio" name="timeline-product" id="tl-only-16"> Lovable</label>
<label><input type="radio" name="timeline-product" id="tl-only-17"> Manus</label>
<label><input type="radio" name="timeline-product" id="tl-only-18"> Ollama</label>
<label><input type="radio" name="timeline-product" id="tl-only-19"> Open WebUI</label>
<label><input type="radio" name="timeline-product" id="tl-only-20"> OpenClaw</label>
<label><input type="radio" name="timeline-product" id="tl-only-21"> OpenCode</label>
<label><input type="radio" name="timeline-product" id="tl-only-22"> OpenHands</label>
<label><input type="radio" name="timeline-product" id="tl-only-23"> Replit</label>
<label><input type="radio" name="timeline-product" id="tl-only-24"> Runway</label>
<label><input type="radio" name="timeline-product" id="tl-only-25"> Suno</label>
<label><input type="radio" name="timeline-product" id="tl-only-26"> Windsurf</label>
<label><input type="radio" name="timeline-product" id="tl-only-27"> v0</label>
</fieldset>

<details class="disclosure">
<summary>2026 · 1,001 entries (ChatGPT 25 · Claude 9 · Claude Code 157 · Cline 39 · Codex CLI 82 · Cursor 35 · Dify 17 · ElevenLabs 74 · Gamma 3 · Gemini 3 · Gemini CLI 24 · GitHub Copilot CLI 115 · Google Antigravity 25 · Lovable 115 · Ollama 17 · Open WebUI 18 · OpenClaw 25 · OpenCode 112 · OpenHands 25 · Replit 51 · Runway 4 · Suno 4 · Windsurf 8 · v0 14)</summary>

**2026-11**

- 2026-11-06 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-11-06-shared-mcp-connections|Shared MCP Connections]] · Launch
- 2026-11-06 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-11-06-gui-plugin-themes-and-new-slots|GUI Plugin Themes and New Slots]] · Launch
- 2026-11-02 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-11-02-connect-your-app-to-bamboohr|Connect your app to BambooHR]] · Launch

**2026-10**

- 2026-10-30 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-10-30-publish-interactive-artifacts|Publish Interactive Artifacts]] · Launch
- 2026-10-30 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-10-30-managed-policy-integration-use-covers-integrations-only|Managed policy: integration.use covers integrations only]] · Launch
- 2026-10-30 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-10-30-tui-plugins-require-opentui-0-8|TUI plugins require OpenTUI 0.8]] · Launch
- 2026-10-29 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-29-partner-plugins-in-the-marketplace-and-plugin-sign-in|Partner plugins in the Marketplace and plugin sign-in]] · Launch
- 2026-10-28 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-28-conversation-navigator-and-third-party-tools-notice|Conversation navigator and third party tools notice]] · Launch
- 2026-10-27 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-10-27-connect-your-app-to-scrive|Connect your app to Scrive]] · Launch
- 2026-10-27 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-10-27-add-experimental-image-and-decision-generation-apis-to-plugins-and-sdk|Add experimental image and decision generation APIs to plugins and sdk]] · Launch
- 2026-10-27 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-10-27-create-install-and-share-desktop-plugins-experimental|Create, install and share Desktop plugins (experimental)]] · Launch
- 2026-10-27 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-10-27-tui-plugins-require-opentui-0-7|TUI plugins require OpenTUI 0.7]] · Launch
- 2026-10-27 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-10-27-plugins-can-now-attach-and-update-keyed-session-instructions-with-ctx-session-in|Plugins can now attach and update keyed session instructions…]] · Launch
- 2026-10-27 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-10-27-opencode-ai-root-is-now-the-promise-api|opencode/ai root is now the Promise API]] · Launch
- 2026-10-26 · <span class="tl-product tl-p10">**Gamma**</span> · [[Changes/Gamma/2026-10-26-introducing-gamma-5|Introducing Gamma 5]] · Launch
- 2026-10-26 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-10-26-redesigned-connector-pages|Redesigned connector pages]] · Launch
- 2026-10-23 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-10-23-keep-your-apps-running-when-credits-run-out|Keep your apps running when credits run out]] · Launch
- 2026-10-20 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-20-plugin-sidebar-badges-window-shortcuts-and-reliability-fixes|Plugin sidebar badges, window shortcuts, and reliability fixes]] · Launch
- 2026-10-20 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-10-20-let-lovable-create-your-supabase-project|Let Lovable create your Supabase project]] · Launch
- 2026-10-20 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-10-20-app-chat-connectors-llamaparse-platform-and-n8n|App + chat connectors: LlamaParse Platform and n8n]] · Launch
- 2026-10-19 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-19-sdk-releases|SDK releases]] · Launch
- 2026-10-19 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-19-python-sdk|Python SDK]] · Launch
- 2026-10-19 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-10-19-connect-your-app-to-cube|Connect your app to Cube]] · Launch
- 2026-10-16 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-10-16-connect-your-app-to-pledge|Connect your app to Pledge]] · Launch
- 2026-10-14 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-10-14-connect-your-app-to-bing-webmaster-tools|Connect your app to Bing Webmaster Tools]] · Launch
- 2026-10-13 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-10-13-apps-for-your-stack|Apps for your stack]] · Launch
- 2026-10-13 · <span class="tl-product tl-p11">**Gemini**</span> · [[Changes/Gemini/2026-10-13-an-easier-way-to-customize-how-gemini-works-for-you-and-more-connected-apps|An easier way to customize how Gemini works for you and more connected apps]] · Launch
- 2026-10-13 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-10-13-approve-every-tool-from-a-chat-connector-at-once|Approve every tool from a chat connector at once]] · Launch
- 2026-10-12 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-12-sdk-releases|SDK releases]] · Launch
- 2026-10-12 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-10-12-connect-your-app-to-loops|Connect your app to Loops]] · Launch
- 2026-10-09 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-10-09-generate-a-secret-that-another-app-also-needs|Generate a secret that another app also needs]] · Launch
- 2026-10-08 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-10-08-app-chat-connectors-zendesk-neon-motherduck-oracle-autonomous-ai-database-ibm-db|App + chat connectors]] · Launch
- 2026-10-08 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-10-08-chat-connectors-loom|Chat connectors: Loom]] · Launch
- 2026-10-06 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-10-06-chat-connectors-excalidraw|Chat connectors: Excalidraw+]] · Launch
- 2026-10-06 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-10-06-connect-to-databricks-with-your-own-account|Connect to Databricks with your own account]] · Launch
- 2026-10-06 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-10-06-redesigned-model-list-for-the-built-in-ai-connector|Redesigned model list for the built-in AI connector]] · Launch
- 2026-10-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-05-swift-sdk|Swift SDK]] · Launch
- 2026-10-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-05-sdk-releases|SDK releases]] · Launch
- 2026-10-05 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-10-05-app-chat-connectors-beehiiv-and-ramp|App + chat connectors: beehiiv and Ramp]] · Launch
- 2026-10-02 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-10-02-jev-is-now-available-through-replit-ai-integrations|Jev is now available through Replit AI Integrations]] · Launch

**2026-09**

- 2026-09-29 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-09-29-lovable-mcp-now-works-with-muse-by-meta|Lovable MCP now works with Muse by Meta]] · Launch
- 2026-09-28 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-09-28-sdk-releases|SDK releases]] · Launch
- 2026-09-28 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-28-manage-install-plugins-in-agy|Manage & Install plugins in AGY]] · Launch
- 2026-09-28 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-28-you-can-now-discover-install-and-manage-plugins-within-the-customizations-tab-wi|Discover, install and manage plugins within the Customizations tab, with curated…]] · Change
- 2026-09-25 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2026-09-25-build-plugins-for-claude|Build plugins for Claude]] · Launch
- 2026-09-25 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-09-25-app-chat-connectors-discord-and-google-business-profile|App + chat connectors: Discord and Google Business Profile]] · Launch
- 2026-09-25 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-09-25-build-and-test-airwallex-integrations|Build and test Airwallex integrations]] · Launch
- 2026-09-25 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-09-25-create-replit-apps-through-muse|Create Replit apps through Muse]] · Launch
- 2026-09-25 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-09-25-build-apps-for-meta-devices|Build apps for Meta devices]] · Launch
- 2026-09-24 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-09-24-create-update-and-publish-storyblok-content-from-your-app|Create, update, and publish Storyblok content from your app]] · Launch
- 2026-09-23 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-09-23-integrations|Integrations]] · Launch
- 2026-09-23 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-09-23-app-chat-connectors-aws-api-azure-cloud-api-azure-graph-entra-api-google-cloud-a|App + chat connectors]] · Launch
- 2026-09-23 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-09-23-typo-tolerant-connector-search|Typo-tolerant connector search]] · Launch
- 2026-09-23 · <span class="tl-product tl-p24">**Runway**</span> · [[Changes/Runway/2026-09-23-runway-mcp-is-now-available-on-cursor-s-marketplace-making-it-easy-to-bring-runw|Runway MCP on Cursor]] · Launch
- 2026-09-22 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-09-22-connect-your-app-to-parallel|Connect your app to Parallel]] · Launch
- 2026-09-21 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-09-21-sdk-releases|SDK releases]] · Launch
- 2026-09-19 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-19-you-can-now-ask-btw-side-questions-about-photos-attached-to-the-current-message|Ask /btw side questions about photos attached to the current message when using…]] · Change
- 2026-09-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-17-added-plugin-install-plugin-marketplace-source-which-offers-to-add-the-marketpla|Added /plugin install plugin --marketplace source, which offers to add…]] · Change
- 2026-09-17 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-09-17-connect-your-app-to-the-lovable-api|Connect your app to the Lovable API]] · Launch
- 2026-09-16 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2026-09-16-claude-cowork-comes-to-every-conversation|Claude Cowork comes to every conversation]] · Launch
- 2026-09-15 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2026-09-15-launching-salesforce-in-claude-beta|Launching Salesforce in Claude (beta)]] · Launch
- 2026-09-15 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-09-15-connect-your-app-to-power-bi|Connect your app to Power BI]] · Launch
- 2026-09-14 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-09-14-sdk-releases|SDK releases]] · Launch
- 2026-09-11 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-11-we-re-planning-to-retire-custom-gpts-across-chatgpt-plans-and-provide-a-migratio|Planned custom GPT retirement and migration to plugins]] · Policy
- 2026-09-11 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-11-added-output-style-name-to-list-and-switch-output-styles-including-over-remote-c|Added /output-style name to list and switch output styles, including over Remote…]] · Change
- 2026-09-11 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-09-11-get-a-warning-when-another-lovable-project-already-uses-your-supabase-project|Get a warning when another Lovable project already uses your Supabase project]] · Launch
- 2026-09-11 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-09-11-connect-other-mcp-clients-to-the-lovable-mcp-server|Connect other MCP clients to the Lovable MCP server]] · Launch
- 2026-09-11 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-11-you-can-now-search-installed-and-available-plugins-together-browse-by-purpose-an|Search installed and available plugins together, browse by purpose, and keep…]] · Change
- 2026-09-11 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-09-11-use-managed-postgresql-in-databricks-apps|Use managed PostgreSQL in Databricks Apps]] · Launch
- 2026-09-11 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-09-11-use-replit-from-desktop-mcp-clients|Use Replit from desktop MCP clients]] · Launch
- 2026-09-10 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-09-10-chat-connectors-canva-and-wispr-flow|Chat connectors: Canva and Wispr Flow]] · Launch
- 2026-09-10 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-09-10-lovable-mcp-now-works-with-grok|Lovable MCP now works with Grok]] · Launch
- 2026-09-10 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-09-10-connect-your-app-to-cloudflare-api|Connect your app to Cloudflare API]] · Launch
- 2026-09-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-09-07-sdk-releases|SDK releases]] · Launch
- 2026-09-07 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-09-07-connect-your-app-to-gong|Connect your app to Gong]] · Launch
- 2026-09-07 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-09-07-connector-forms-are-split-into-collapsible-sections|Connector forms are split into collapsible sections]] · Launch
- 2026-09-03 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-03-added-reload-plugins-to-headless-sessions-so-it-appears-in-the-claude-code-deskt|Added /reload-plugins to headless sessions, so it appears in the Claude Code…]] · Change
- 2026-09-02 · <span class="tl-product tl-p25">**Suno**</span> · [[Changes/Suno/2026-09-02-copy-and-duplicate-plugins|Copy and duplicate plugins]] · Launch
- 2026-09-01 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-09-01-connect-a-tool-from-a-pasted-api-key|Connect a tool from a pasted API key]] · Launch

**2026-08**

- 2026-08-31 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-31-sdk-releases|SDK releases]] · Launch
- 2026-08-31 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-31-javascript-sdk|JavaScript SDK]] · Launch
- 2026-08-31 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-08-31-create-a-connector-for-any-api|Create a connector for any API]] · Launch
- 2026-08-28 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-08-28-you-can-now-connect-multiple-accounts-for-gmail-google-calendar-and-google-conta-b4c5da|Connect multiple Google accounts to ChatGPT]] · Change
- 2026-08-28 · <span class="tl-product tl-p10">**Gamma**</span> · [[Changes/Gamma/2026-08-28-build-more-with-gamma-s-api-and-connectors|Build more with Gamma’s API and connectors]] · Launch
- 2026-08-28 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-08-28-connect-your-app-to-gitlab-api|Connect your app to GitLab API]] · Launch
- 2026-08-28 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-08-28-connect-your-app-to-firebase-cloud-messaging|Connect your app to Firebase Cloud Messaging]] · Launch
- 2026-08-28 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-08-28-customize-connectors|Customize connectors]] · Launch
- 2026-08-28 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-08-28-integrations|Integrations]] · Launch
- 2026-08-26 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-08-26-connect-github-api-by-signing-in-with-your-github-account|Connect GitHub API by signing in with your GitHub account]] · Launch
- 2026-08-26 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-08-26-chat-with-lovable-in-slack|Chat with Lovable in Slack]] · Launch
- 2026-08-24 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-24-sdk-releases|SDK Releases]] · Launch
- 2026-08-24 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-24-javascript-sdk|JavaScript SDK]] · Launch
- 2026-08-24 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-08-24-add-an-mcp-registry-from-the-catalog-header|Add an MCP registry from the catalog header]] · Launch
- 2026-08-24 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-08-24-let-your-app-s-users-connect-their-own-github-account|Let your app's users connect their own GitHub account]] · Launch
- 2026-08-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-22-mcp-server|MCP server]] · Policy
- 2026-08-21 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-08-21-export-designs-from-figma-with-the-lovable-plugin|Export designs from Figma with the Lovable plugin]] · Launch
- 2026-08-20 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-08-20-sort-connectors-and-add-an-mcp-server-from-the-catalog-header|Sort connectors and add an MCP server from the catalog header]] · Launch
- 2026-08-19 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-08-19-per-user-access-for-amazon-redshift|Per-user access for Amazon Redshift]] · Launch
- 2026-08-19 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-08-19-lovable-can-use-your-connected-service-account-while-building|Lovable can use your connected service account while building]] · Launch
- 2026-08-17 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-08-17-app-extensions-for-cursor-repos|App extensions for Cursor repos]] · Launch
- 2026-08-17 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-08-17-settings|Settings]] · Launch
- 2026-08-17 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-17-sdk-releases|SDK Releases]] · Launch
- 2026-08-16 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-08-16-lovable-mcp-updates|Lovable MCP updates]] · Launch
- 2026-08-14 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-08-14-connect-more-mcp-servers|Connect more MCP servers]] · Launch
- 2026-08-14 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-08-14-use-replit-through-mcp|Use Replit through MCP]] · Launch
- 2026-08-14 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-08-14-integrations|Integrations]] · Launch
- 2026-08-13 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-08-13-build-dashboards-from-your-snowflake-semantic-views|Build dashboards from your Snowflake semantic views]] · Launch
- 2026-08-13 · <span class="tl-product tl-p24">**Runway**</span> · [[Changes/Runway/2026-08-13-ideogram-s-latest-image-model-is-now-available-in-runway-mcp-as-ideogram-4-for-t|Ideogram 4.0]] · Launch
- 2026-08-12 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-08-12-unpublish-several-projects-at-once|Unpublish several projects at once]] · Launch
- 2026-08-10 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-10-sdk-releases|SDK Releases]] · Launch
- 2026-08-10 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-10-mcp-server|MCP Server]] · Launch
- 2026-08-10 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-08-10-agent-integrations-for-workspace-published-apps|Agent integrations for workspace-published apps]] · Launch
- 2026-08-10 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-08-10-connect-mcp-servers-from-a-registry|Connect MCP servers from a registry]] · Launch
- 2026-08-06 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2026-08-06-skill-and-plugin-security-scanning-beta|Skill and plugin security scanning (beta)]] · Launch
- 2026-08-03 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-03-mcp-server|MCP Server]] · Launch
- 2026-08-03 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-03-sdk-releases|SDK Releases]] · Launch
- 2026-08-01 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-08-01-stopped-mcp-sse-connections-from-getting-stuck-in-reconnect-loops-after-server-e|Stopped MCP SSE connections from getting stuck in reconnect loops after server error…]] · Launch

**2026-07**

- 2026-07-31 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-31-lovable-mcp-updates|Lovable MCP updates]] · Launch
- 2026-07-31 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-07-31-connect-more-mcp-servers|Connect more MCP servers]] · Launch
- 2026-07-29 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-29-app-chat-connectors-amazon-redshift-and-microsoft-fabric|App + chat connectors: Amazon Redshift and Microsoft Fabric]] · Launch
- 2026-07-28 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-07-28-preview-tabs-mcp-timeouts-file-attachments-and-performance-fixes|Preview tabs, MCP timeouts, file attachments, and performance fixes]] · Launch
- 2026-07-28 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-28-upgrade-an-older-project-to-tanstack-start|Upgrade an older project to TanStack Start]] · Launch
- 2026-07-28 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-28-app-chat-connectors-google-analytics-and-xero|App + chat connectors: Google Analytics and Xero]] · Launch
- 2026-07-28 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-28-connect-pipedrive-in-one-click|Connect Pipedrive in one click]] · Launch
- 2026-07-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-07-27-sdk-releases|SDK Releases]] · Launch
- 2026-07-27 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-27-connect-your-app-to-posthog|Connect your app to PostHog]] · Launch
- 2026-07-27 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-27-pick-your-shopify-store-from-a-list|Pick your Shopify store from a list]] · Launch
- 2026-07-24 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-07-24-integrations|Integrations]] · Launch
- 2026-07-24 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-07-24-bring-more-slack-context-to-agent|Bring more Slack context to Agent]] · Launch
- 2026-07-23 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-23-let-your-app-s-users-connect-their-own-notion|Let your app's users connect their own Notion]] · Launch
- 2026-07-23 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-23-recommended-connectors-in-search|Recommended connectors in search]] · Launch
- 2026-07-22 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-22-bulk-edit-your-shopify-catalog-in-one-approval|Bulk-edit your Shopify catalog in one approval]] · Launch
- 2026-07-22 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-22-lovable-mcp-is-now-a-codex-plugin|Lovable MCP is now a Codex plugin]] · Launch
- 2026-07-21 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-21-app-connectors-apify-and-tally|App connectors: Apify and Tally]] · Launch
- 2026-07-20 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-07-20-sdk-releases|SDK Releases]] · Launch
- 2026-07-17 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-07-17-multi-repo-environment-support-4b706e|Multi-repo environment support]] · Launch
- 2026-07-17 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-07-17-integrations|Integrations]] · Launch
- 2026-07-16 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-16-reuse-your-workspace-identity-in-the-apps-you-build|Reuse your workspace identity in the apps you build]] · Launch
- 2026-07-16 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-16-connect-your-app-to-apollo-io|Connect your app to Apollo.io]] · Launch
- 2026-07-13 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-07-13-sdk-releases|SDK Releases]] · Launch
- 2026-07-13 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-13-connect-klipy-in-one-click-no-api-key|Connect KLIPY in one click, no API key]] · Launch
- 2026-07-13 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-13-mapbox-connector|Mapbox connector]] · Launch
- 2026-07-13 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-13-let-your-app-s-users-connect-their-own-accounts|Let your app's users connect their own accounts]] · Launch
- 2026-07-10 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-07-10-integrations|Integrations]] · Launch
- 2026-07-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-07-09-enterprise-and-edu-users-can-find-skills-under-plugins-in-the-sidebar-on-the-ski|Skills are now generally available]] · Launch
- 2026-07-09 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-09-app-connectors-dbt-semantic-layer-and-clickhouse|App connectors: dbt Semantic Layer and ClickHouse]] · Launch
- 2026-07-09 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-09-approve-connector-actions-before-they-run|Approve connector actions before they run]] · Launch
- 2026-07-09 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-09-connect-bigquery-with-your-google-account|Connect BigQuery with your Google account]] · Launch
- 2026-07-08 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-08-remote-plugins-are-now-enabled-by-default-with-richer-catalog-rows-npm-marketpla|Remote plugins are now enabled by default, with richer catalog rows, npm marketplace…]] · Change
- 2026-07-08 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-08-reference-a-connector-in-chat|Reference a connector in chat]] · Launch
- 2026-07-07 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2026-07-07-write-tools-for-the-microsoft-365-connector|Write tools for the Microsoft 365 connector]] · Launch
- 2026-07-07 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-07-app-connector-github-api|App connector: GitHub API]] · Launch
- 2026-07-06 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-07-06-sdk-releases|SDK Releases]] · Launch
- 2026-07-06 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-07-06-elevenagents|ElevenAgents]] · Launch
- 2026-07-06 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-07-06-added-a-code-mode-mcp-adapter-for-running-confined-orchestration-scripts-against|Added a code mode MCP adapter for running confined orchestration scripts against…]] · Launch
- 2026-07-03 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-07-03-integrations|Integrations]] · Launch
- 2026-07-02 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-02-connectors-page-in-projects|Connectors page in projects]] · Launch
- 2026-07-02 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-07-02-app-connector-wordpress-self-hosted|App connector: WordPress (self-hosted)]] · Launch
- 2026-07-01 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-01-claude-in-chrome-is-now-generally-available|Claude in Chrome is now generally available]] · Launch
- 2026-07-01 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-01-added-dataviz-skill-for-chart-and-dashboard-design-guidance-with-a-runnable-colo|Added /dataviz skill for chart and dashboard design guidance with a runnable…]] · Change

**2026-06**

- 2026-06-29 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-29-sdk-releases|SDK Releases]] · Launch
- 2026-06-29 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-29-app-connector-x|App connector: X]] · Launch
- 2026-06-26 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-26-app-connectors-klipy-and-logo-dev|App connectors: KLIPY and Logo.dev]] · Launch
- 2026-06-26 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-06-26-integrations|Integrations]] · Launch
- 2026-06-26 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-06-26-a-new-integrations-experience|A new Integrations experience]] · Launch
- 2026-06-26 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-06-26-use-replit-from-slack|Use Replit from Slack]] · Launch
- 2026-06-24 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-24-lovable-mcp-updates|Lovable MCP updates]] · Launch
- 2026-06-24 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-24-app-connector-calendly|App connector: Calendly]] · Launch
- 2026-06-24 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-06-24-added-mcp-server-instructions-to-session-context|Added MCP server instructions to session context]] · Launch
- 2026-06-23 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2026-06-23-delegate-work-to-claude-in-slack-with-claude-tag|Delegate work to Claude in Slack with Claude Tag]] · Launch
- 2026-06-23 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-23-set-up-okta-sso-and-scim-from-the-okta-app-catalog|Set up Okta SSO and SCIM from the Okta app catalog]] · Launch
- 2026-06-22 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-22-marketplace-leaderboard-654084|Marketplace leaderboard]] · Launch
- 2026-06-22 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-22-plugin-canvases|Plugin canvases]] · Launch
- 2026-06-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-22-python-sdk|Python SDK]] · Launch
- 2026-06-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-22-sdk-releases|SDK Releases]] · Launch
- 2026-06-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-22-mcp-server|MCP Server]] · Launch
- 2026-06-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-22-javascript-sdk|JavaScript SDK]] · Launch
- 2026-06-22 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-22-lovable-mcp-updates|Lovable MCP updates]] · Launch
- 2026-06-22 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-22-aikido-penetration-testing-is-now-available-on-all-plans|Aikido penetration testing is now available on all plans]] · Launch
- 2026-06-19 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-06-19-integrations|Integrations]] · Launch
- 2026-06-19 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-06-19-new-mcp-servers-apollo-and-black-forest-labs|New MCP servers: Apollo and Black Forest Labs]] · Launch
- 2026-06-19 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-06-19-use-replit-from-claude|Use Replit from Claude]] · Launch
- 2026-06-18 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-18-inspect-your-app-s-ai-activity|Inspect your app's AI activity]] · Launch
- 2026-06-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-17-added-config-key-value-syntax-to-set-any-setting-from-the-prompt-e-g-config-thin|Added /config key=value syntax to set any setting from the prompt…]] · Change
- 2026-06-17 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-17-build-in-lovable-from-claude|Build in Lovable from Claude]] · Launch
- 2026-06-17 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-17-app-connector-lightspeed|App connector: Lightspeed]] · Launch
- 2026-06-16 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-16-app-connectors-chargebee-gatewayapi-lexware-pipedrive-prestashop-sevdesk-wave-wi|App connectors: Chargebee, GatewayAPI, Lexware, Pipedrive, PrestaShop, Sevdesk…]] · Launch
- 2026-06-16 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-16-reference-web-pages-in-a-build-with-url-link|Reference web pages in a "Build with URL" link]] · Launch
- 2026-06-16 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2026-06-16-devin-local|Devin Local]] · Launch
- 2026-06-15 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-15-sdk-releases|SDK Releases]] · Launch
- 2026-06-15 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-15-packages|Packages]] · Launch
- 2026-06-15 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-15-app-connectors-aws-athena-and-replicate|App connectors: AWS Athena and Replicate]] · Launch
- 2026-06-14 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-06-14-mcp-servers-can-now-receive-the-current-workspace-as-a-client-root|MCP servers can now receive the current workspace as a client root]] · Launch
- 2026-06-12 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2026-06-12-edit-claude-s-drafts-in-place|Edit Claude’s drafts in place]] · Launch
- 2026-06-12 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-06-12-added-cwd-support-for-local-mcp-servers-so-they-can-start-from-a-workspace-relat|Added cwd support for local MCP servers so they can start from a workspace-relative…]] · Launch
- 2026-06-08 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-08-sdk-releases|SDK Releases]] · Launch
- 2026-06-05 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-05-mcp-tools-added-or-removed-by-a-server-mid-turn-are-now-available-immediately-in|MCP tools added or removed by a server mid-turn are now available immediately…]] · Launch
- 2026-06-05 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-06-05-build-data-apps-on-microsoft-fabric|Build data apps on Microsoft Fabric]] · Launch
- 2026-06-05 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-06-05-integrations|Integrations]] · Launch
- 2026-06-04 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-04-added-plugin-list-command-to-list-installed-plugins-with-enabled-disabled-filter|Added /plugin list command to list installed plugins…]] · Change
- 2026-06-03 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-03-configure-who-can-create-app-connector-connections|Configure who can create app connector connections]] · Launch
- 2026-06-03 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-03-connector-sidebar|Connector sidebar]] · Launch
- 2026-06-03 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-03-lovable-mcp-server-now-available-on-all-plans|Lovable MCP server now available on all plans]] · Launch
- 2026-06-01 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-01-sdk-releases|SDK Releases]] · Launch
- 2026-06-01 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-06-01-elevenagents|ElevenAgents]] · Launch
- 2026-06-01 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-06-01-app-connector-salesforce|App connector: Salesforce]] · Launch

**2026-05**

- 2026-05-30 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-05-30-sessions-can-now-store-custom-metadata-through-the-api-and-sdk|Sessions can now store custom metadata through the API and SDK]] · Launch
- 2026-05-29 · <span class="tl-product tl-p10">**Gamma**</span> · [[Changes/Gamma/2026-05-29-claude-and-chatgpt-connectors-just-got-smarter|Claude and ChatGPT connectors just got smarter]] · Launch
- 2026-05-29 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-05-29-integrations|Integrations]] · Launch
- 2026-05-28 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2026-05-28-enterprise-plans-can-manage-connector-access-with-custom-roles|Enterprise plans can manage connector access with custom roles]] · Launch
- 2026-05-28 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-05-28-app-connectors-algolia-linkedin-and-microsoft-sharepoint|App connectors: Algolia, LinkedIn, and Microsoft SharePoint]] · Launch
- 2026-05-28 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-05-28-acp-integrations-can-now-send-prompts-slash-commands-and-usage-updates-through-a|ACP integrations can now send prompts, slash commands, and usage updates through acp-next]] · Launch
- 2026-05-25 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-05-25-python-sdk|Python SDK]] · Launch
- 2026-05-25 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-05-25-javascript-sdk|JavaScript SDK]] · Launch
- 2026-05-25 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-05-25-sdk-releases|SDK Releases]] · Launch
- 2026-05-25 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-05-25-custom-mcp-servers-available-on-all-plans|Custom MCP servers available on all plans]] · Launch
- 2026-05-22 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-05-22-antigravity-ide-integration|Antigravity IDE integration]] · Launch
- 2026-05-22 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-05-22-integrations|Integrations]] · Launch
- 2026-05-22 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-05-22-two-new-connectors-quiver-ai-and-browserbase|Two new connectors: Quiver AI and Browserbase]] · Launch
- 2026-05-21 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-05-21-app-connectors-google-maps-platform-semrush-and-tiktok|App connectors: Google Maps Platform, Semrush, and TikTok]] · Launch
- 2026-05-19 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-05-19-cursor-is-now-available-in-jira|Cursor is now available in Jira]] · Launch
- 2026-05-19 · <span class="tl-product tl-p11">**Gemini**</span> · [[Changes/Gemini/2026-05-19-daily-brief-is-your-personalized-overview-of-what-matters-today|Daily Brief is your personalized overview of what matters today]] · Launch
- 2026-05-19 · <span class="tl-product tl-p11">**Gemini**</span> · [[Changes/Gemini/2026-05-19-gemini-can-connect-to-more-apps-starting-with-opentable-canva-and-instacart|Gemini can connect to more apps, starting with OpenTable, Canva, and Instacart]] · Launch
- 2026-05-18 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-05-18-sdk-releases|SDK Releases]] · Launch
- 2026-05-18 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-05-18-lovable-mcp-server-research-preview|Lovable MCP server (research preview)]] · Expansion
- 2026-05-18 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-05-18-chat-connectors-heygen|Chat connectors: HeyGen]] · Launch
- 2026-05-18 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-05-18-app-connectors-airtable-attention-brevo-google-search-console-granola-mailgun-no|App connectors: Airtable, Attention, Brevo, Google Search Console, Granola, Mailgun…]] · Launch
- 2026-05-18 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-05-18-tanstack-start-is-now-the-default-for-new-apps|TanStack Start is now the default for new apps]] · Launch
- 2026-05-18 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-05-18-chat-with-lovable-in-telegram|Chat with Lovable in Telegram]] · Launch
- 2026-05-15 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-05-15-integrations|Integrations]] · Launch
- 2026-05-15 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-05-15-nine-new-connectors-ready-to-use-out-of-the-box|Nine new connectors ready to use out of the box]] · Launch
- 2026-05-15 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-05-15-four-new-mcp-servers-in-the-directory|Four new MCP servers in the directory]] · Launch
- 2026-05-13 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-05-13-sdk-releases|SDK Releases]] · Launch
- 2026-05-11 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-11-added-goal-command-set-a-completion-condition-and-claude-keeps-working-across-tu|Added /goal command]] · Change
- 2026-05-10 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-05-10-tui-plugins-using-the-deprecated-api-command-api-keep-working-while-you-migrate|TUI plugins using the deprecated api.command API keep working while you migrate…]] · Policy
- 2026-05-08 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-05-08-speaker-notes-and-presenter-view-in-slide-decks|Speaker notes and Presenter view in Slide Decks]] · Launch
- 2026-05-04 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-05-04-sdk-releases|SDK Releases]] · Launch
- 2026-05-04 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-05-04-python-sdk|Python SDK]] · Launch
- 2026-05-04 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-05-04-javascript-sdk|JavaScript SDK]] · Launch
- 2026-05-01 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-05-01-replit-app-monitoring-keeps-an-eye-on-your-published-apps|Replit App Monitoring keeps an eye on your published apps]] · Launch

**2026-04**

- 2026-04-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-29-we-re-introducing-the-cursor-sdk-so-you-can-build-agents-with-the-same-runtime-h|Cursor introduces the Cursor SDK so you can build agents with the same runtime…]] · Launch
- 2026-04-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-27-sdk-releases|SDK Releases]] · Launch
- 2026-04-24 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-04-24-data-app-connectors-bigquery-databricks-snowflake|Data app connectors: BigQuery, Databricks, Snowflake]] · Launch
- 2026-04-24 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-04-24-email-and-workflow-app-connectors-inngest-resend|Email and workflow app connectors: Inngest, Resend]] · Launch
- 2026-04-24 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-04-24-business-app-connectors-asana-ashby-hubspot|Business app connectors: Asana, Ashby, HubSpot]] · Launch
- 2026-04-24 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-04-24-connector-updates|Connector updates]] · Launch
- 2026-04-24 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-04-24-productivity-app-connectors-google-workspace-microsoft-365|Productivity app connectors: Google Workspace, Microsoft 365]] · Launch
- 2026-04-24 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-04-24-saml-2-0-single-sign-on-for-your-apps|SAML 2.0 single sign-on for your apps]] · Launch
- 2026-04-24 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-04-24-chat-connectors-sentry-mcp|Chat connectors: Sentry MCP]] · Launch
- 2026-04-24 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-04-24-added-an-experimental-http-api-endpoint-for-mcp-server-status|Added an experimental HTTP API endpoint for MCP server status]] · Launch
- 2026-04-24 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-04-24-integrations|Integrations]] · Launch
- 2026-04-24 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-04-24-plaid-connector-is-live|Plaid connector is live]] · Launch
- 2026-04-23 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-added-mcp-verbose-for-full-mcp-server-diagnostics-resources-and-resource-templat|Added /mcp verbose for full MCP server diagnostics, resources, and resource…]] · Change
- 2026-04-20 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-20-sdk-releases|SDK Releases]] · Launch
- 2026-04-17 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-04-17-integrations|Integrations]] · Launch
- 2026-04-15 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-04-15-export-ai-sdk-telemetry-spans-to-otlp-trace-backends|Export AI SDK telemetry spans to OTLP trace backends]] · Launch
- 2026-04-15 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2026-04-15-additional-changes|Additional Changes]] · Launch
- 2026-04-13 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-13-sdk-releases|SDK Releases]] · Launch
- 2026-04-13 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-13-you-can-now-remote-control-your-cli-sessions-using-remote-or-remote|Remote control your CLI sessions using --remote or /remote]] · Change
- 2026-04-12 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-04-12-hermes-agent-https-docs-ollama-com-integrations-hermes-ollama-integration-guide|Hermes agent((source link) Ollama integration guide…]] · Launch
- 2026-04-10 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-04-10-revenuecat-app-store-connect-sync|RevenueCat App Store Connect sync]] · Launch
- 2026-04-10 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-04-10-connectors-available-on-all-paid-plans|Connectors available on all paid plans]] · Launch
- 2026-04-10 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-04-10-databricks-apps-integration|Databricks Apps integration]] · Launch
- 2026-04-10 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-04-10-integrations|Integrations]] · Launch
- 2026-04-08 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-08-give-bugbot-access-to-mcp-servers-for-additional-context-during-code-reviews-on|Bugbot MCP Support]] · Launch
- 2026-04-08 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-08-this-release-introduces-updates-to-bugbot-including-the-ability-to-self-improve|Cursor introduces updates to Bugbot including the ability to self-improve in real…]] · Launch
- 2026-04-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-07-python-sdk|Python SDK]] · Launch
- 2026-04-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-07-sdk-releases|SDK Releases]] · Launch
- 2026-04-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-07-javascript-sdk|JavaScript SDK]] · Launch
- 2026-04-02 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-04-02-app-connectors-aikido-gitlab-and-aws-s3|App connectors: Aikido, GitLab, and AWS S3]] · Launch
- 2026-04-02 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-04-02-chat-connectors-hex-confidence-and-posthog|Chat connectors: Hex, Confidence, and PostHog]] · Launch
- 2026-04-01 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-01-elevenagents-2b20f8|ElevenAgents]] · Launch
- 2026-04-01 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-04-01-sdk-releases|SDK Releases]] · Launch

**2026-03**

- 2026-03-26 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-26-the-app-server-backed-tui-is-now-enabled-by-default-and-the-plugin-app-rollout-f|The app-server-backed TUI is now enabled by default, and the plugin/app rollout…]] · Change
- 2026-03-25 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-03-25-linux-sandboxing-and-mcp-improvements|Linux Sandboxing and MCP Improvements]] · Policy
- 2026-03-23 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-23-workspaces|Workspaces]] · Launch
- 2026-03-23 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-23-sdk-releases|SDK Releases]] · Launch
- 2026-03-16 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-16-javascript-sdk|JavaScript SDK]] · Launch
- 2026-03-16 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-16-sdk-releases|SDK Releases]] · Launch
- 2026-03-16 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-03-16-app-connectors-twitch-twilio-linear-telegram-and-contentful|App connectors: Twitch, Twilio, Linear, Telegram, and Contentful]] · Launch
- 2026-03-16 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-03-16-chat-connectors-polar-and-sanity|Chat connectors: Polar and Sanity]] · Launch
- 2026-03-09 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-09-sdk-releases|SDK Releases]] · Launch
- 2026-03-09 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-09-music|Music]] · Launch
- 2026-03-09 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-09-extensions-are-now-available-as-an-experimental-feature-ask-copilot-to-write-cus|Extensions are now available as an experimental feature]] · Launch
- 2026-03-09 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2026-03-09-mcp|MCP]] · Launch
- 2026-03-06 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-03-06-gpt-codex-5-3-support-in-ai-integrations|GPT-Codex-5.3 support in AI Integrations]] · Launch
- 2026-03-06 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-03-06-connectors-and-ai-integrations-now-enabled-by-default-for-teams-and-enterprise|Connectors and AI Integrations now enabled by default for Teams and Enterprise]] · Launch
- 2026-03-06 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-03-06-revenuecat-integration-now-generally-available|RevenueCat integration now generally available]] · Launch
- 2026-03-05 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-05-added-reload-plugins-command-to-activate-pending-plugin-changes-without-restarti|Added /reload-plugins command to activate pending plugin changes without restarting]] · Change
- 2026-03-04 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-03-04-rework-workspace-integration-and-adaptor-interface|Rework workspace integration and adaptor interface]] · Launch
- 2026-03-03 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-03-03-mcp-apps-support-interactive-user-interfaces-like-charts-from-amplitude-diagrams|MCP Apps]] · Launch
- 2026-03-03 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-03-03-on-teams-and-enterprise-plans-admins-can-now-create-team-marketplaces-to-share-p|Team marketplaces for plugins]] · Launch
- 2026-03-02 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-02-javascript-sdk|JavaScript SDK]] · Launch
- 2026-03-02 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-02-python-sdk|Python SDK]] · Launch
- 2026-03-02 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-02-sdk-releases|SDK Releases]] · Launch

**2026-02**

- 2026-02-25 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2026-02-25-mcp-improvements|MCP Improvements]] · Launch
- 2026-02-24 · <span class="tl-product tl-p3">**Claude**</span> · [[Changes/Claude/2026-02-24-cowork-plugins-and-admin-controls|Cowork plugins and admin controls]] · Launch
- 2026-02-23 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-23-sdk-releases|SDK Releases]] · Launch
- 2026-02-23 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-23-python-sdk|Python SDK]] · Launch
- 2026-02-23 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-02-23-amplitude-mcp-available-as-a-chat-connector|Amplitude MCP available as a chat connector]] · Launch
- 2026-02-23 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-02-23-granola-mcp-available-as-a-chat-connector|Granola MCP available as a chat connector]] · Launch
- 2026-02-23 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-02-23-slack-available-as-an-app-connector|Slack available as an app connector]] · Launch
- 2026-02-23 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-02-23-lovable-cloud-updates|Lovable Cloud updates]] · Launch
- 2026-02-20 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-02-20-add-missing-id-sessionid-and-messageid-to-mcp-tool-attachments|Add missing id, sessionID, and messageID to MCP tool attachments]] · Launch
- 2026-02-20 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-02-20-razorpay-mcp-integration|Razorpay MCP integration]] · Expansion
- 2026-02-20 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-02-20-expanded-default-mcp-list|Expanded default MCP list]] · Launch
- 2026-02-17 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-02-17-plugins-on-the-cursor-marketplace-0cef65|Plugins on the Cursor Marketplace]] · Launch
- 2026-02-16 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-16-javascript-sdk|JavaScript SDK]] · Launch
- 2026-02-16 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-16-python-sdk|Python SDK]] · Launch
- 2026-02-16 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-16-sdk-releases|SDK Releases]] · Launch
- 2026-02-13 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-02-13-bitbucket-integration-improvements|Bitbucket integration improvements]] · Launch
- 2026-02-13 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-02-13-open-in-replit-button-beta|Open in Replit button (Beta)]] · Launch
- 2026-02-13 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-02-13-connection-reliability-improvements|Connection reliability improvements]] · Launch
- 2026-02-09 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-09-sdk-releases|SDK Releases]] · Launch
- 2026-02-05 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-02-05-custom-mcp-servers-on-all-paid-plans|Custom MCP servers on all paid plans]] · Launch
- 2026-02-05 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-02-05-load-user-plugins-after-built-in-plugins|Load user plugins after built-in plugins]] · Launch
- 2026-02-02 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-02-sdk-releases|SDK Releases]] · Launch

**2026-01**

- 2026-01-31 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-31-smart-approvals-are-now-enabled-by-default-with-explicit-approval-prompts-for-mc|Smart approvals are now enabled by default, with explicit approval prompts for MCP…]] · Change
- 2026-01-31 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-31-added-apps-to-browse-connectors-in-tui-and-insertion-for-app-prompts-9728|Added /apps to browse connectors in TUI and $ insertion for app prompts]] · Change
- 2026-01-26 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-26-sdk-releases|SDK Releases]] · Launch
- 2026-01-20 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-20-preserve-tool-input-from-running-state-for-mcp-tool-results|Preserve tool input from running state for MCP tool results]] · Launch
- 2026-01-19 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-19-modified-schemas|Modified Schemas]] · Launch
- 2026-01-19 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-19-sdk-releases|SDK Releases]] · Launch
- 2026-01-12 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-12-mcp-server|MCP Server]] · Launch
- 2026-01-12 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-12-sdk-releases|SDK Releases]] · Launch
- 2026-01-12 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-12-support-resource-content-type-in-mcp-tool-output|Support resource content type in MCP tool output]] · Launch
- 2026-01-11 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-11-ensure-codex-built-in-plugin-is-always-available|Ensure Codex built-in plugin is always available]] · Launch
- 2026-01-09 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-01-09-private-apps-for-free-accounts|Private apps for free accounts]] · Launch
- 2026-01-09 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2026-01-09-made-with-replit-badge|Made with Replit badge]] · Launch
- 2026-01-08 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-01-08-enable-and-disable-mcp-servers-on-the-fly-with-mcp-enable-and-mcp-disable-comman|Enabling MCP servers]] · Launch
- 2026-01-08 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-01-08-added-mcp-enable-mcp-disable-commands-to-manage-mcp-servers|Added /mcp enable, /mcp disable commands to manage MCP servers]] · Change
- 2026-01-08 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-01-08-this-release-introduces-new-cli-controls-for-models-mcp-management-rules-and-com|Cursor introduces new CLI controls for models, MCP management, rules and commands…]] · Launch
- 2026-01-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-05-sdk-releases|SDK Releases]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 668 (ChatGPT 22 · Claude Code 148 · Cline 39 · Codex CLI 77 · Cursor 18 · Dify 17 · ElevenLabs 2 · Gemini CLI 24 · GitHub Copilot CLI 112 · Google Antigravity 17 · Lovable 1 · Ollama 16 · Open WebUI 18 · OpenClaw 23 · OpenCode 86 · OpenHands 25 · Runway 2 · Suno 3 · Windsurf 4 · v0 14)</summary>

**2026-11**

- 2026-11-06 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-11-06-12-apps-and-integrations-changes-in-rust-v0-167-0|12 Apps and Integrations changes in rust-v0.167.0]] · Digest
- 2026-11-06 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-11-06-89-apps-and-integrations-changes-in-v1-0-106|89 Apps and Integrations changes in v1.0.106]] · Digest
- 2026-11-06 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-11-06-7-apps-and-integrations-changes-in-v2-2-6|7 Apps and Integrations changes in v2.2.6]] · Digest
- 2026-11-05 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-11-05-5-apps-and-integrations-changes-in-v2026-11-1|5 Apps and Integrations changes in v2026.11.1]] · Digest
- 2026-11-05 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-11-05-3-apps-and-integrations-changes-in-v1-36-0|3 Apps and Integrations changes in v1.36.0]] · Digest
- 2026-11-04 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-11-04-15-apps-and-integrations-changes-in-1-19-0|15 Apps and Integrations changes in 1.19.0]] · Digest
- 2026-11-03 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-11-03-2-apps-and-integrations-changes-in-hub-v2-29-0-voice-mode-remote|2 Apps and Integrations changes in HUB v2.29.0 — Voice mode, remote…]] · Digest
- 2026-11-03 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-11-03-mcp-apps-in-chat-tools-from-mcp-servers-that-come-with-an-interactive-app-now-sh|🧩 MCP Apps in chat. Tools from MCP servers that come with an interactive app now…]] · Change
- 2026-11-03 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-11-03-21-apps-and-integrations-changes-in-v2026-10-10|21 Apps and Integrations changes in v2026.10.10]] · Digest
- 2026-11-03 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-11-03-3-apps-and-integrations-changes-in-v1-35-0|3 Apps and Integrations changes in v1.35.0]] · Digest
- 2026-11-02 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-11-02-channel-integrations-asynchronous-channels-such-as-slack-telegram-intercom-gmail|Channel integrations: Asynchronous channels such as Slack, Telegram, Intercom…]] · Change

**2026-10**

- 2026-10-31 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-31-7-apps-and-integrations-changes-in-v2-1-316|7 Apps and Integrations changes in v2.1.316]] · Digest
- 2026-10-30 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-30-3-apps-and-integrations-changes-in-v2-1-314|3 Apps and Integrations changes in v2.1.314]] · Digest
- 2026-10-30 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-10-30-4-apps-and-integrations-changes-in-v2-2-5|4 Apps and Integrations changes in v2.2.5]] · Digest
- 2026-10-30 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-10-30-sdk-extended-client-experimental-persistentpty-update-to-rename-terminals-or-cle|SDK Extended client.experimental.persistentPty.update to rename terminals or clear…]] · Change
- 2026-10-30 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-10-30-10-apps-and-integrations-changes-in-v2-2-3|10 Apps and Integrations changes in v2.2.3]] · Digest
- 2026-10-29 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-29-22-apps-and-integrations-changes-in-rust-v0-166-0|22 Apps and Integrations changes in rust-v0.166.0]] · Digest
- 2026-10-29 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-29-2-apps-and-integrations-changes-in-hub-v2-28-2-partner-plugins|2 Apps and Integrations changes in HUB v2.28.2 — Partner plugins…]] · Digest
- 2026-10-29 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-10-29-2-apps-and-integrations-changes-in-v0-12-5|2 Apps and Integrations changes in v0.12.5]] · Digest
- 2026-10-29 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-29-2-apps-and-integrations-changes-in-v2026-10-9|2 Apps and Integrations changes in v2026.10.9]] · Digest
- 2026-10-29 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-10-29-3-apps-and-integrations-changes-in-v2-2-2|3 Apps and Integrations changes in v2.2.2]] · Digest
- 2026-10-29 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-10-29-5-apps-and-integrations-changes-in-v2-2-1|5 Apps and Integrations changes in v2.2.1]] · Digest
- 2026-10-28 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-28-a-plugin-s-page-now-shows-its-developer-and-version-with-links-to-its-website-an|A plugin's page now shows its developer and version, with links to its website…]] · Change
- 2026-10-28 · <span class="tl-product tl-p25">**Suno**</span> · [[Changes/Suno/2026-10-28-connect-suno-to-claude-chatgpt-claude-code-and-other-mcp-clients-then-create-mus|Connect Suno to Claude, ChatGPT, Claude Code and other MCP clients, then create…]] · Change
- 2026-10-27 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-27-2-apps-and-integrations-changes-in-v2-1-312|2 Apps and Integrations changes in v2.1.312]] · Digest
- 2026-10-27 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-27-10-apps-and-integrations-changes-in-rust-v0-165-0|10 Apps and Integrations changes in rust-v0.165.0]] · Digest
- 2026-10-27 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-27-interactive-and-sdk-autopilot-sessions-keep-waiting-for-attached-background-task|Interactive and SDK Autopilot sessions keep waiting for attached background tasks…]] · Change
- 2026-10-27 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-27-9-apps-and-integrations-changes-in-v2026-10-8|9 Apps and Integrations changes in v2026.10.8]] · Digest
- 2026-10-27 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-10-27-14-apps-and-integrations-changes-in-v2-2-0|14 Apps and Integrations changes in v2.2.0]] · Digest
- 2026-10-27 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-10-27-refactor-extensions-name-dialog-viewport-limits-by-enyst-in-https-github-com-ope|refactor(extensions): name dialog viewport limits]] · Change
- 2026-10-26 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-26-3-apps-and-integrations-changes-in-v2-1-311|3 Apps and Integrations changes in v2.1.311]] · Digest
- 2026-10-26 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-26-2-apps-and-integrations-changes-in-elevenlabs-updates-2026-10-26|2 Apps and Integrations changes in ElevenLabs updates — 2026-10-26]] · Digest
- 2026-10-25 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-10-25-5-apps-and-integrations-changes-in-v0-12-4|5 Apps and Integrations changes in v0.12.4]] · Digest
- 2026-10-24 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-24-7-apps-and-integrations-changes-in-v2026-10-7|7 Apps and Integrations changes in v2026.10.7]] · Digest
- 2026-10-23 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-23-2-apps-and-integrations-changes-in-v2-1-310|2 Apps and Integrations changes in v2.1.310]] · Digest
- 2026-10-23 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-23-30-apps-and-integrations-changes-in-rust-v0-164-0|30 Apps and Integrations changes in rust-v0.164.0]] · Digest
- 2026-10-23 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-10-23-14-apps-and-integrations-changes-in-1-18-0|14 Apps and Integrations changes in 1.18.0]] · Digest
- 2026-10-23 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-10-23-2-apps-and-integrations-changes-in-v1-32-0|2 Apps and Integrations changes in v1.32.0]] · Digest
- 2026-10-23 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2026-10-23-5-apps-and-integrations-changes-in-v3-11-212|5 Apps and Integrations changes in v3.11.212]] · Digest
- 2026-10-22 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-22-2-apps-and-integrations-changes-in-v2-1-309|2 Apps and Integrations changes in v2.1.309]] · Digest
- 2026-10-22 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-22-reuse-cached-local-mcp-tool-snapshots-across-registered-git-worktrees-in-one-rep|Reuse cached local MCP tool snapshots across registered Git worktrees in one repository]] · Change
- 2026-10-22 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-22-3-apps-and-integrations-changes-in-hub-v2-26-0-notifications-settings|3 Apps and Integrations changes in HUB v2.26.0 — Notifications settings…]] · Digest
- 2026-10-22 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-22-10-apps-and-integrations-changes-in-v2026-10-6|10 Apps and Integrations changes in v2026.10.6]] · Digest
- 2026-10-22 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-10-22-chore-bump-openhands-extensions-to-0-33-0-by-neubig-in-https-github-com-openhand|chore: bump @openhands/extensions to 0.33.0]] · Change
- 2026-10-21 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-21-3-apps-and-integrations-changes-in-v2-1-307|3 Apps and Integrations changes in v2.1.307]] · Digest
- 2026-10-21 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-21-2-apps-and-integrations-changes-in-v1-0-102|2 Apps and Integrations changes in v1.0.102]] · Digest
- 2026-10-20 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-20-4-apps-and-integrations-changes-in-v2-1-305|4 Apps and Integrations changes in v2.1.305]] · Digest
- 2026-10-20 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-20-4-apps-and-integrations-changes-in-v1-0-101|4 Apps and Integrations changes in v1.0.101]] · Digest
- 2026-10-20 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-20-project-folders-managed-by-ui-plugins-now-display-a-dedicated-plugin-badge-in-th|Project folders managed by UI plugins now display a dedicated plugin badge in the sidebar]] · Change
- 2026-10-20 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-10-20-2-apps-and-integrations-changes-in-v1-29-0|2 Apps and Integrations changes in v1.29.0]] · Digest
- 2026-10-19 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-19-8-apps-and-integrations-changes-in-v2-1-304|8 Apps and Integrations changes in v2.1.304]] · Digest
- 2026-10-19 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-19-10-apps-and-integrations-changes-in-v1-0-100|10 Apps and Integrations changes in v1.0.100]] · Digest
- 2026-10-19 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2026-10-19-connect-your-slack-workspace-to-v0-to-bring-team-conversations-into-your-work-wi|Connect your Slack workspace to v0 to bring team conversations into your work]] · Change
- 2026-10-18 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-18-3-apps-and-integrations-changes-in-v2026-10-5|3 Apps and Integrations changes in v2026.10.5]] · Digest
- 2026-10-16 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-10-16-improved-use-of-plugins-and-tools-to-carry-out-tasks|Improved use of plugins and tools to carry out tasks]] · Change
- 2026-10-16 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-16-3-apps-and-integrations-changes-in-v2-1-302|3 Apps and Integrations changes in v2.1.302]] · Digest
- 2026-10-16 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-16-maintenance-warnings-completed-plugin-upgrades-stop-leaving-stale-unfinished-war|Maintenance warnings]] · Change
- 2026-10-16 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2026-10-16-integration-icons-no-longer-fail-to-load-in-project-settings|Integration icons no longer fail to load in project settings]] · Change
- 2026-10-15 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-15-15-apps-and-integrations-changes-in-rust-v0-163-0|15 Apps and Integrations changes in rust-v0.163.0]] · Digest
- 2026-10-15 · <span class="tl-product tl-p24">**Runway**</span> · [[Changes/Runway/2026-10-15-remove-backgrounds-automatically-in-runway-mcp-with-birefnet-v2-it-detects-the-f|BiRefNet v2 Background Removal]] · Change
- 2026-10-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-14-7-apps-and-integrations-changes-in-v2-1-300|7 Apps and Integrations changes in v2.1.300]] · Digest
- 2026-10-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-14-19-apps-and-integrations-changes-in-v2-1-299|19 Apps and Integrations changes in v2.1.299]] · Digest
- 2026-10-14 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-14-2-apps-and-integrations-changes-in-v1-0-98|2 Apps and Integrations changes in v1.0.98]] · Digest
- 2026-10-14 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-10-14-2-apps-and-integrations-changes-in-v0-12-1|2 Apps and Integrations changes in v0.12.1]] · Digest
- 2026-10-13 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-10-13-an-mcp-server-or-hook-that-exits-before-reading-all-of-its-input-no-longer-crash|An MCP server or hook that exits before reading all of its input no longer crashes…]] · Change
- 2026-10-13 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-10-13-2-apps-and-integrations-changes-in-origin-app-marketplace|2 Apps and Integrations changes in Origin App Marketplace]] · Digest
- 2026-10-13 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-13-4-apps-and-integrations-changes-in-v1-0-97|4 Apps and Integrations changes in v1.0.97]] · Digest
- 2026-10-13 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-13-7-apps-and-integrations-changes-in-v2026-10-3|7 Apps and Integrations changes in v2026.10.3]] · Digest
- 2026-10-12 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-12-3-apps-and-integrations-changes-in-hub-v2-23-0-permissions-picker|3 Apps and Integrations changes in HUB v2.23.0 — Permissions picker…]] · Digest
- 2026-10-12 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-12-5-apps-and-integrations-changes-in-v2026-10-2|5 Apps and Integrations changes in v2026.10.2]] · Digest
- 2026-10-12 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-10-12-3-apps-and-integrations-changes-in-v1-27-0|3 Apps and Integrations changes in v1.27.0]] · Digest
- 2026-10-11 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-10-11-ollama-launch-claude-no-longer-shows-a-warning-about-claude-connectors-by-hoyyev|ollama launch claude no longer shows a warning about Claude connectors]] · Change
- 2026-10-10 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]] · Digest
- 2026-10-10 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-10-96-apps-and-integrations-changes-in-v2026-10-1|96 Apps and Integrations changes in v2026.10.1]] · Digest
- 2026-10-09 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-09-3-apps-and-integrations-changes-in-v2-1-296|3 Apps and Integrations changes in v2.1.296]] · Digest
- 2026-10-09 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-09-managed-plugin-setup-retries-hourly-or-after-policy-changes-instead-of-on-every|Managed plugin setup retries hourly or after policy changes instead of on every…]] · Change
- 2026-10-08 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-08-improved-how-prompt-hooks-on-stop-and-subagentstop-written-as-instructions-such|Improved how prompt hooks on Stop and SubagentStop written as instructions…]] · Change
- 2026-10-08 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-08-14-apps-and-integrations-changes-in-v2-1-295|14 Apps and Integrations changes in v2.1.295]] · Digest
- 2026-10-08 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-08-20-apps-and-integrations-changes-in-rust-v0-162-0|20 Apps and Integrations changes in rust-v0.162.0]] · Digest
- 2026-10-08 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-08-2-apps-and-integrations-changes-in-v1-0-94|2 Apps and Integrations changes in v1.0.94]] · Digest
- 2026-10-08 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-08-construct-and-display-custom-user-interfaces-inside-the-side-panel-as-part-of-in|Construct and display custom user interfaces inside the side panel as part…]] · Change
- 2026-10-08 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-10-08-readme-add-oxi-to-community-integrations-by-maziluiosif-in-https-github-com-olla|README: add oxi to community integrations]] · Change
- 2026-10-08 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-08-10-apps-and-integrations-changes-in-v2026-9-9|10 Apps and Integrations changes in v2026.9.9]] · Digest
- 2026-10-08 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-10-08-feat-apps-add-authenticated-backend-view-helper-by-neubig-in-https-github-com-op|feat(apps): add authenticated backend view helper]] · Change
- 2026-10-07 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-07-3-apps-and-integrations-changes-in-v2-1-293|3 Apps and Integrations changes in v2.1.293]] · Digest
- 2026-10-07 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-10-07-when-an-mcp-tool-returns-more-output-than-fits-in-context-cline-can-now-read-the|When an MCP tool returns more output than fits in context, Cline can now read the rest]] · Change
- 2026-10-07 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-07-5-apps-and-integrations-changes-in-rust-v0-161-0|5 Apps and Integrations changes in rust-v0.161.0]] · Digest
- 2026-10-07 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-07-2-apps-and-integrations-changes-in-v1-0-93|2 Apps and Integrations changes in v1.0.93]] · Digest
- 2026-10-06 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-06-9-apps-and-integrations-changes-in-v2-1-292|9 Apps and Integrations changes in v2.1.292]] · Digest
- 2026-10-06 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-10-06-chore-consume-extensions-0-27-0-by-henriquehirako-in-https-github-com-openhands|chore: consume Extensions 0.27.0]] · Change
- 2026-10-05 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-05-14-apps-and-integrations-changes-in-v2-1-290|14 Apps and Integrations changes in v2.1.290]] · Digest
- 2026-10-05 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-05-2-apps-and-integrations-changes-in-rust-v0-160-1|2 Apps and Integrations changes in rust-v0.160.1]] · Digest
- 2026-10-05 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-05-5-apps-and-integrations-changes-in-v1-0-92|5 Apps and Integrations changes in v1.0.92]] · Digest
- 2026-10-03 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-03-2-apps-and-integrations-changes-in-v2-1-289|2 Apps and Integrations changes in v2.1.289]] · Digest
- 2026-10-02 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-02-5-apps-and-integrations-changes-in-v2-1-288|5 Apps and Integrations changes in v2.1.288]] · Digest
- 2026-10-01 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-10-01-11-apps-and-integrations-changes-in-v2-1-287|11 Apps and Integrations changes in v2.1.287]] · Digest
- 2026-10-01 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-01-4-apps-and-integrations-changes-in-rust-v0-160-0|4 Apps and Integrations changes in rust-v0.160.0]] · Digest

**2026-09**

- 2026-09-30 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-30-11-apps-and-integrations-changes-in-v2-1-286|11 Apps and Integrations changes in v2.1.286]] · Digest
- 2026-09-30 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-30-3-apps-and-integrations-changes-in-v1-0-90|3 Apps and Integrations changes in v1.0.90]] · Digest
- 2026-09-30 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-30-36-apps-and-integrations-changes-in-v2026-9-7|36 Apps and Integrations changes in v2026.9.7]] · Digest
- 2026-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-29-this-is-a-limited-preview-with-participating-integrations-using-purchased-credit|This is a limited preview with participating integrations]] · Change
- 2026-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-29-plugins-can-now-include-interactive-panels-sidebar-views-and-viewers-or-editors-d0bd7e|Work with interactive plugin extensions]] · Change
- 2026-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-29-we-re-making-it-easier-to-bring-meeting-context-into-chatgpt-so-you-can-act-on-n|We’re making it easier to bring meeting context into ChatGPT so you can act on next…]] · Change
- 2026-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-29-supported-plugins-can-use-mcp-events-to-start-an-automation-when-something-chang-d9add6|Start automations from connected-app events]] · Change
- 2026-09-29 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-29-14-apps-and-integrations-changes-in-v2-1-285|14 Apps and Integrations changes in v2.1.285]] · Digest
- 2026-09-29 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-29-8-apps-and-integrations-changes-in-rust-v0-159-0|8 Apps and Integrations changes in rust-v0.159.0]] · Digest
- 2026-09-29 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-09-29-2-apps-and-integrations-changes-in-v0-62-0|2 Apps and Integrations changes in v0.62.0]] · Digest
- 2026-09-28 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-28-8-apps-and-integrations-changes-in-v2-1-284|8 Apps and Integrations changes in v2.1.284]] · Digest
- 2026-09-28 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-28-13-apps-and-integrations-changes-in-rust-v0-158-0|13 Apps and Integrations changes in rust-v0.158.0]] · Digest
- 2026-09-28 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-28-4-apps-and-integrations-changes-in-v1-0-89|4 Apps and Integrations changes in v1.0.89]] · Digest
- 2026-09-28 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-28-slash-commands-provided-by-plugins-now-show-their-plugin-name-in-the-menu-can-be|Slash commands provided by plugins now show their plugin name in the / menu, can…]] · Change
- 2026-09-28 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-09-28-core-mcp-browser-launch-failures-are-now-reported-when-the-launcher-exits-immedi|Core MCP browser launch failures are now reported when the launcher exits immediately]] · Change
- 2026-09-25 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-25-14-apps-and-integrations-changes-in-v2-1-283|14 Apps and Integrations changes in v2.1.283]] · Digest
- 2026-09-25 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-25-9-apps-and-integrations-changes-in-rust-v0-157-0|9 Apps and Integrations changes in rust-v0.157.0]] · Digest
- 2026-09-25 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-09-25-chore-deps-bump-openhands-extensions-to-0-24-0-by-devinvinson-in-https-github-co|chore(deps): bump @openhands/extensions to 0.24.0]] · Change
- 2026-09-24 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-24-8-apps-and-integrations-changes-in-v2-1-282|8 Apps and Integrations changes in v2.1.282]] · Digest
- 2026-09-23 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-23-17-apps-and-integrations-changes-in-v2-1-281|17 Apps and Integrations changes in v2.1.281]] · Digest
- 2026-09-23 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-23-58-apps-and-integrations-changes-in-v2026-9-6|58 Apps and Integrations changes in v2026.9.6]] · Digest
- 2026-09-22 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-22-8-apps-and-integrations-changes-in-v2-1-280|8 Apps and Integrations changes in v2.1.280]] · Digest
- 2026-09-22 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-22-42-apps-and-integrations-changes-in-rust-v0-156-0|42 Apps and Integrations changes in rust-v0.156.0]] · Digest
- 2026-09-22 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-22-6-apps-and-integrations-changes-in-v1-0-88|6 Apps and Integrations changes in v1.0.88]] · Digest
- 2026-09-22 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-09-22-test-cover-mcp-config-utilities-by-aivong-openhands-in-https-github-com-openhand|test: cover MCP config utilities]] · Change
- 2026-09-22 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-09-22-feat-test-remote-mcp-servers-on-cloud-backends-via-the-app-server-by-hieptl-in-h|feat: test remote MCP servers on cloud backends via the app server]] · Change
- 2026-09-22 · <span class="tl-product tl-p24">**Runway**</span> · [[Changes/Runway/2026-09-22-agents-in-runway-mcp-can-now-find-your-brand-kits-and-use-those-assets-as-refere|Brand Kits in Runway MCP]] · Change
- 2026-09-21 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-21-8-apps-and-integrations-changes-in-v1-0-87|8 Apps and Integrations changes in v1.0.87]] · Digest
- 2026-09-21 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-09-21-3-apps-and-integrations-changes-in-v0-11-4|3 Apps and Integrations changes in v0.11.4]] · Digest
- 2026-09-19 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-19-52-apps-and-integrations-changes-in-v2026-9-5|52 Apps and Integrations changes in v2026.9.5]] · Digest
- 2026-09-18 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-18-6-apps-and-integrations-changes-in-v2-1-277|6 Apps and Integrations changes in v2.1.277]] · Digest
- 2026-09-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-17-10-apps-and-integrations-changes-in-v2-1-274|10 Apps and Integrations changes in v2.1.274]] · Digest
- 2026-09-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-17-6-apps-and-integrations-changes-in-v2-1-275|6 Apps and Integrations changes in v2.1.275]] · Digest
- 2026-09-17 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-09-17-terminal-commands-that-succeed-without-printing-anything-git-add-a-on-a-clean-tr|Terminal commands that succeed without printing anything…]] · Change
- 2026-09-17 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-17-24-apps-and-integrations-changes-in-rust-v0-155-0|24 Apps and Integrations changes in rust-v0.155.0]] · Digest
- 2026-09-17 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-17-resuming-an-active-session-without-plugin-directory-discovery-or-working-directo|Resuming an active session without plugin-directory, discovery, or working-directory…]] · Change
- 2026-09-16 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-16-20-apps-and-integrations-changes-in-v1-0-85|20 Apps and Integrations changes in v1.0.85]] · Digest
- 2026-09-16 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-09-16-9-apps-and-integrations-changes-in-v1-19-0|9 Apps and Integrations changes in v1.19.0]] · Digest
- 2026-09-15 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-15-3-apps-and-integrations-changes-in-v2-1-273|3 Apps and Integrations changes in v2.1.273]] · Digest
- 2026-09-15 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-09-15-feat-extensions-harden-path-resolution-and-boundary-validation-in-extension-load|feat(extensions): harden path resolution and boundary validation in extension loader]] · Change
- 2026-09-14 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-14-for-new-health-plugin-connections-chatgpt-will-now-default-to-each-user-s-global|For new Health plugin connections, ChatGPT will now default to each user’s global…]] · Change
- 2026-09-14 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-14-you-can-change-your-health-permissions-anytime-in-settings-plugins-health-learn|You can change your Health permissions anytime in Settings → Plugins → Health]] · Change
- 2026-09-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-14-5-apps-and-integrations-changes-in-v2-1-271|5 Apps and Integrations changes in v2.1.271]] · Digest
- 2026-09-11 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-11-5-apps-and-integrations-changes-in-v2-1-269|5 Apps and Integrations changes in v2.1.269]] · Digest
- 2026-09-11 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-11-22-apps-and-integrations-changes-in-v2026-9-4|22 Apps and Integrations changes in v2026.9.4]] · Digest
- 2026-09-10 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-10-the-data-plugin-helps-you-analyze-connected-business-data-in-chatgpt-work-and-co|Data plugin in ChatGPT Work and Codex]] · Change
- 2026-09-10 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-10-7-apps-and-integrations-changes-in-v2-1-268|7 Apps and Integrations changes in v2.1.268]] · Digest
- 2026-09-10 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-09-10-12-apps-and-integrations-changes-in-1-17-1|12 Apps and Integrations changes in 1.17.1]] · Digest
- 2026-09-09 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-09-claude-tag-added-a-use-a-custom-connector-link-to-the-preset-connection-forms-in|Claude Tag Added a "Use a custom connector" link to the preset connection forms…]] · Change
- 2026-09-09 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-09-19-apps-and-integrations-changes-in-rust-v0-154-0|19 Apps and Integrations changes in rust-v0.154.0]] · Digest
- 2026-09-09 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-09-09-2-apps-and-integrations-changes-in-v1-18-30|2 Apps and Integrations changes in v1.18.30]] · Digest
- 2026-09-09 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-09-09-docs-remove-duplicate-openhands-extensions-bullet-in-development-md-by-imitater|docs: remove duplicate OpenHands/extensions bullet in DEVELOPMENT.md]] · Change
- 2026-09-08 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-08-4-apps-and-integrations-changes-in-v2-1-265|4 Apps and Integrations changes in v2.1.265]] · Digest
- 2026-09-08 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-08-23-apps-and-integrations-changes-in-v2026-9-3|23 Apps and Integrations changes in v2026.9.3]] · Digest
- 2026-09-05 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-05-35-apps-and-integrations-changes-in-v2026-9-2|35 Apps and Integrations changes in v2026.9.2]] · Digest
- 2026-09-04 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-04-vscode-added-an-add-server-form-and-a-remove-action-to-the-mcp-servers-dialog-so|VSCode Added an Add server form and a Remove action to the MCP servers dialog…]] · Change
- 2026-09-04 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-04-7-apps-and-integrations-changes-in-v1-0-83|7 Apps and Integrations changes in v1.0.83]] · Digest
- 2026-09-03 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-03-today-we-added-the-zendesk-and-onenote-plugins-in-the-plugin-directory-the-zende-012cbd|Zendesk & OneNote Plugins in ChatGPT and Codex Beta]] · Change
- 2026-09-03 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-03-4-apps-and-integrations-changes-in-v2-1-260|4 Apps and Integrations changes in v2.1.260]] · Digest
- 2026-09-03 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-03-18-apps-and-integrations-changes-in-rust-v0-153-0|18 Apps and Integrations changes in rust-v0.153.0]] · Digest
- 2026-09-03 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-03-26-apps-and-integrations-changes-in-v2026-9-1|26 Apps and Integrations changes in v2026.9.1]] · Digest
- 2026-09-02 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-02-5-apps-and-integrations-changes-in-v2-1-259|5 Apps and Integrations changes in v2.1.259]] · Digest
- 2026-09-02 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-09-02-2-apps-and-integrations-changes-in-v4-1-17|2 Apps and Integrations changes in v4.1.17]] · Digest
- 2026-09-01 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-01-eligible-chatgpt-for-clinicians-users-in-the-united-states-can-now-use-healthcar|Healthcare Public Data in ChatGPT for Clinicians]] · Change
- 2026-09-01 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-09-01-2-apps-and-integrations-changes-in-v2-1-257|2 Apps and Integrations changes in v2.1.257]] · Digest
- 2026-09-01 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-01-16-apps-and-integrations-changes-in-rust-v0-152-0|16 Apps and Integrations changes in rust-v0.152.0]] · Digest
- 2026-09-01 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-01-9-apps-and-integrations-changes-in-v2026-8-2|9 Apps and Integrations changes in v2026.8.2]] · Digest

**2026-08**

- 2026-08-31 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-08-31-2-apps-and-integrations-changes-in-v2026-8-1|2 Apps and Integrations changes in v2026.8.1]] · Digest
- 2026-08-29 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-29-11-apps-and-integrations-changes-in-rust-v0-151-0|11 Apps and Integrations changes in rust-v0.151.0]] · Digest
- 2026-08-28 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-28-4-apps-and-integrations-changes-in-v2-1-251|4 Apps and Integrations changes in v2.1.251]] · Digest
- 2026-08-28 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2026-08-28-2-apps-and-integrations-changes-in-gpt-5-6-sol-sign-in-inside-previews|2 Apps and Integrations changes in GPT-5.6 Sol, sign-in inside previews…]] · Digest
- 2026-08-27 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-27-improved-managed-settings-client-side-timeout-mcp-startup-mode-and-stream-watchd|Improved managed settings]] · Change
- 2026-08-27 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-27-12-apps-and-integrations-changes-in-v1-0-81|12 Apps and Integrations changes in v1.0.81]] · Digest
- 2026-08-27 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-08-27-feat-land-the-canvas-extensions-frontend-load-pages-sidebar-customize-by-hieptl|feat: land the Canvas Extensions frontend (load pages, sidebar, customize)]] · Change
- 2026-08-26 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-26-2-apps-and-integrations-changes-in-v2-1-247|2 Apps and Integrations changes in v2.1.247]] · Digest
- 2026-08-26 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-08-26-4-apps-and-integrations-changes-in-v4-1-16|4 Apps and Integrations changes in v4.1.16]] · Digest
- 2026-08-26 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-26-24-apps-and-integrations-changes-in-rust-v0-150-0|24 Apps and Integrations changes in rust-v0.150.0]] · Digest
- 2026-08-25 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-25-3-apps-and-integrations-changes-in-v2-1-246|3 Apps and Integrations changes in v2.1.246]] · Digest
- 2026-08-25 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-08-25-28-apps-and-integrations-changes-in-1-17-0|28 Apps and Integrations changes in 1.17.0]] · Digest
- 2026-08-25 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-21919-fix-typescript-strict-null-errors-in-integration-tests|SSR Agent Issue Fix (21919): Fix TypeScript strict-null errors in integration tests]] · Change
- 2026-08-25 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-08-25-4-apps-and-integrations-changes-in-v0-11-1|4 Apps and Integrations changes in v0.11.1]] · Digest
- 2026-08-24 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-08-24-model-context-protocol-mcp-and-custom-tool-execution-steps-now-display-structure|Model Context Protocol (MCP) and custom tool execution steps now display structured…]] · Change
- 2026-08-23 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-08-23-everything-here-lands-through-the-sdk-bundle-so-it-applies-to-windows-running-th|Everything here lands through the SDK bundle, so it applies to windows running that bundle]] · Change
- 2026-08-23 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-08-23-2-apps-and-integrations-changes-in-v4-1-15|2 Apps and Integrations changes in v4.1.15]] · Digest
- 2026-08-22 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-08-22-everything-here-lands-through-the-sdk-bundle-so-it-applies-to-windows-running-th|Everything here lands through the SDK bundle, so it applies to windows running that bundle]] · Change
- 2026-08-21 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-08-21-updated-plugin-recommendations-make-it-easier-to-find-tools-people-continue-to-u|Updated plugin recommendations make it easier to find tools people continue to use]] · Change
- 2026-08-21 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-08-21-plugin-availability-depends-on-your-plan-region-and-workspace-settings-desktop-i|Plugin availability depends on your plan, region, and workspace settings]] · Change
- 2026-08-21 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-08-21-find-more-useful-plugins-rankings-now-prioritize-plugins-people-keep-using-after|Find more useful plugins]] · Change
- 2026-08-21 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-21-2-apps-and-integrations-changes-in-v2-1-239|2 Apps and Integrations changes in v2.1.239]] · Digest
- 2026-08-21 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-08-21-2-apps-and-integrations-changes-in-v4-1-12|2 Apps and Integrations changes in v4.1.12]] · Digest
- 2026-08-21 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-08-21-2-apps-and-integrations-changes-in-v4-1-11|2 Apps and Integrations changes in v4.1.11]] · Digest
- 2026-08-21 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-08-21-2-apps-and-integrations-changes-in-v1-15-0|2 Apps and Integrations changes in v1.15.0]] · Digest
- 2026-08-20 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-08-20-use-apple-messages-from-codex-and-chatgpt-work-on-apple-silicon-macs-the-apple-m|Use Apple Messages from Codex and ChatGPT Work]] · Change
- 2026-08-20 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-20-6-apps-and-integrations-changes-in-v2-1-238|6 Apps and Integrations changes in v2.1.238]] · Digest
- 2026-08-20 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-20-33-apps-and-integrations-changes-in-rust-v0-149-0|33 Apps and Integrations changes in rust-v0.149.0]] · Digest
- 2026-08-20 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-08-20-refreshed-the-customizations-settings-screen-with-collapsible-sections-and-item|Refreshed the Customizations settings screen with collapsible sections and item…]] · Change
- 2026-08-19 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-19-sigterm-in-print-sdk-mode-no-longer-records-an-interrupted-turn-or-synthetic-too|SIGTERM in print/SDK mode no longer records an interrupted turn or synthetic tool…]] · Change
- 2026-08-18 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-18-57-apps-and-integrations-changes-in-rust-v0-148-0|57 Apps and Integrations changes in rust-v0.148.0]] · Digest
- 2026-08-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-17-remote-control-signing-this-computer-in-to-a-different-claude-ai-account-or-orga|Remote Control: signing this computer in to a different claude.ai account…]] · Change
- 2026-08-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-14-2-apps-and-integrations-changes-in-v2-1-233|2 Apps and Integrations changes in v2.1.233]] · Digest
- 2026-08-14 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-08-14-everything-in-this-release-lands-through-the-sdk-bundle-so-it-applies-to-windows|Everything in this release lands through the SDK bundle, so it applies to windows…]] · Change
- 2026-08-14 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2026-08-14-4-apps-and-integrations-changes-in-a-redesigned-sidebar-a-richer|4 Apps and Integrations changes in A redesigned sidebar, a richer…]] · Digest
- 2026-08-13 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-13-4-apps-and-integrations-changes-in-v2-1-232|4 Apps and Integrations changes in v2.1.232]] · Digest
- 2026-08-13 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-08-13-these-land-through-sdk-v0-0-74-and-therefore-apply-to-windows-running-the-sdk-bu|These land through SDK v0.0.74 and therefore apply to windows running the SDK…]] · Change
- 2026-08-13 · <span class="tl-product tl-p25">**Suno**</span> · [[Changes/Suno/2026-08-13-chat-bar-generate-instruments-and-vocals-create-new-and-totally-unique-plugins-a|Chat bar: Generate instruments and vocals, create new and totally unique plugins…]] · Change
- 2026-08-12 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-12-3-apps-and-integrations-changes-in-v2-1-229|3 Apps and Integrations changes in v2.1.229]] · Digest
- 2026-08-11 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-11-2-apps-and-integrations-changes-in-v2-1-228|2 Apps and Integrations changes in v2.1.228]] · Digest
- 2026-08-10 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-10-3-apps-and-integrations-changes-in-v1-0-79|3 Apps and Integrations changes in v1.0.79]] · Digest
- 2026-08-09 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-08-09-2-apps-and-integrations-changes-in-v4-1-7|2 Apps and Integrations changes in v4.1.7]] · Digest
- 2026-08-08 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-08-3-apps-and-integrations-changes-in-v2-1-225|3 Apps and Integrations changes in v2.1.225]] · Digest
- 2026-08-07 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-07-3-apps-and-integrations-changes-in-v2-1-224|3 Apps and Integrations changes in v2.1.224]] · Digest
- 2026-08-07 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-07-65-apps-and-integrations-changes-in-rust-v0-147-0|65 Apps and Integrations changes in rust-v0.147.0]] · Digest
- 2026-08-07 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-08-07-2-apps-and-integrations-changes-in-hub-v2-6-0-faster-long-conversations|2 Apps and Integrations changes in HUB v2.6.0 — Faster long conversations…]] · Digest
- 2026-08-07 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-08-07-faster-long-conversations-more-reliable-hooks-and-subagents|Faster long conversations, more reliable hooks and subagents]] · Change
- 2026-08-05 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-08-05-map-reasoning-settings-onto-a-shared-path-across-ai-sdk-providers-so-effort-leve|Map reasoning settings onto a shared path across AI SDK providers, so effort levels…]] · Change
- 2026-08-05 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-08-05-2-apps-and-integrations-changes-in-v4-1-4|2 Apps and Integrations changes in v4.1.4]] · Digest
- 2026-08-05 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-08-05-chore-bump-openhands-extensions-to-0-16-0-by-hieptl-in-https-github-com-openhand|chore: bump @openhands/extensions to 0.16.0]] · Change
- 2026-08-04 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-08-04-three-new-plugins-for-chatgpt-work-and-codex-help-students-and-educators-work-wi-e7aee9|Three new plugins for ChatGPT Work and Codex help students and educators work…]] · Change
- 2026-08-04 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-04-4-apps-and-integrations-changes-in-v2-1-221|4 Apps and Integrations changes in v2.1.221]] · Digest
- 2026-08-04 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-08-04-2-apps-and-integrations-changes-in-v2-1-222|2 Apps and Integrations changes in v2.1.222]] · Digest
- 2026-08-03 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-08-03-cursor-can-now-read-write-and-act-across-your-google-workspace|Google Workspace Plugins]] · Change
- 2026-08-03 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-03-4-apps-and-integrations-changes-in-v1-0-78|4 Apps and Integrations changes in v1.0.78]] · Digest
- 2026-08-03 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-08-03-chore-bump-openhands-extensions-to-0-13-0-by-hieptl-in-https-github-com-openhand|chore: bump @openhands/extensions to 0.13.0]] · Change

**2026-07**

- 2026-07-31 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-07-31-3-apps-and-integrations-changes-in-v4-1-0|3 Apps and Integrations changes in v4.1.0]] · Digest
- 2026-07-30 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-30-2-apps-and-integrations-changes-in-v1-0-76|2 Apps and Integrations changes in v1.0.76]] · Digest
- 2026-07-30 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-07-30-feat-enable-disable-an-installed-mcp-server-from-its-card-by-hieptl-in-https-git|feat: enable/disable an installed MCP server from its card]] · Change
- 2026-07-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-07-29-we-re-beginning-to-roll-out-sign-in-with-chatgpt-across-select-plugins-and-partn|Sign in with ChatGPT]] · Change
- 2026-07-29 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-29-47-apps-and-integrations-changes-in-rust-v0-146-0|47 Apps and Integrations changes in rust-v0.146.0]] · Digest
- 2026-07-28 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-07-28-plugins-mcp-servers-hooks-and-skills-to-extend-cursor-across-your-workflows|Plugins, MCP servers, hooks, and skills to extend Cursor across your workflows]] · Change
- 2026-07-28 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-07-28-10-apps-and-integrations-changes-in-1-16-1|10 Apps and Integrations changes in 1.16.1]] · Digest
- 2026-07-28 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-07-28-added-a-timeout-for-mcp-server-connections-and-tool-calls-to-prevent-the-agent-f|Added a timeout for MCP server connections and tool calls to prevent the agent…]] · Change
- 2026-07-28 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-07-28-2-apps-and-integrations-changes-in-v1-18-8|2 Apps and Integrations changes in v1.18.8]] · Digest
- 2026-07-28 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-07-28-core-restored-compatibility-with-legacy-mcp-sdk-clients|Core Restored compatibility with legacy MCP SDK clients]] · Change
- 2026-07-27 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-07-27-6-apps-and-integrations-changes-in-v0-11-0|6 Apps and Integrations changes in v0.11.0]] · Digest
- 2026-07-24 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-24-5-apps-and-integrations-changes-in-v2-1-219|5 Apps and Integrations changes in v2.1.219]] · Digest
- 2026-07-24 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-07-24-include-the-host-plugin-version-in-telemetry-events|Include the host plugin version in telemetry events]] · Change
- 2026-07-24 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-07-24-core-use-the-correct-prompt-cache-keys-for-each-sdk|Core Use the correct prompt cache keys for each SDK]] · Change
- 2026-07-23 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-23-3-apps-and-integrations-changes-in-v1-0-74|3 Apps and Integrations changes in v1.0.74]] · Digest
- 2026-07-23 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-07-23-improved-integrations-restored-claude-code-channels-fixed-anthropic-thinking-str|Improved integrations: restored Claude Code Channels, fixed Anthropic thinking…]] · Change
- 2026-07-22 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-22-3-apps-and-integrations-changes-in-v2-1-218|3 Apps and Integrations changes in v2.1.218]] · Digest
- 2026-07-21 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-21-capped-the-frontend-design-plugin-suggestion-tip-at-3-lifetime-impressions-inste|Capped the frontend-design plugin suggestion tip at 3 lifetime impressions instead…]] · Change
- 2026-07-21 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-21-44-apps-and-integrations-changes-in-rust-v0-145-0|44 Apps and Integrations changes in rust-v0.145.0]] · Digest
- 2026-07-21 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2026-07-21-3-apps-and-integrations-changes-in-slash-commands-the-shopify|3 Apps and Integrations changes in Slash commands, the Shopify…]] · Digest
- 2026-07-20 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-20-background-sessions-mcp-and-install-github-app-now-park-a-needs-input-request-in|Background sessions: /mcp and /install-github-app now park…]] · Change
- 2026-07-20 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-20-10-apps-and-integrations-changes-in-v1-0-72|10 Apps and Integrations changes in v1.0.72]] · Digest
- 2026-07-18 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-18-changed-sessionstart-hooks-to-report-source-fork-when-a-session-begins-as-a-fork|Changed SessionStart hooks to report source "fork" when a session begins as a fork…]] · Change
- 2026-07-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-17-mcp-tool-calls-running-longer-than-2-minutes-now-move-to-the-background-automati|MCP tool calls running longer than 2 minutes now move to the background…]] · Change
- 2026-07-17 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-07-17-cursor-in-slack-now-shares-a-plan-before-it-starts-runs-in-multi-repo-environmen|Cursor in Slack now shares a plan before it starts, runs in multi-repo environments…]] · Change
- 2026-07-17 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-07-17-24-apps-and-integrations-changes-in-1-16-0|24 Apps and Integrations changes in 1.16.0]] · Digest
- 2026-07-16 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-16-16-apps-and-integrations-changes-in-v1-0-71|16 Apps and Integrations changes in v1.0.71]] · Digest
- 2026-07-15 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-15-2-apps-and-integrations-changes-in-v2-1-211|2 Apps and Integrations changes in v2.1.211]] · Digest
- 2026-07-15 · <span class="tl-product tl-p25">**Suno**</span> · [[Changes/Suno/2026-07-15-tap-the-icon-and-find-suno-in-your-imessage-app-extensions|Tap the + icon and find Suno in your iMessage app extensions]] · Change
- 2026-07-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-14-3-apps-and-integrations-changes-in-v2-1-208|3 Apps and Integrations changes in v2.1.208]] · Digest
- 2026-07-13 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-07-13-213-apps-and-integrations-changes-in-v2026-7-1|213 Apps and Integrations changes in v2026.7.1]] · Digest
- 2026-07-11 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-11-2-apps-and-integrations-changes-in-v2-1-207|2 Apps and Integrations changes in v2.1.207]] · Digest
- 2026-07-11 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-07-11-2-apps-and-integrations-changes-in-v0-32-0|2 Apps and Integrations changes in v0.32.0]] · Digest
- 2026-07-10 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-10-9-apps-and-integrations-changes-in-v1-0-70|9 Apps and Integrations changes in v1.0.70]] · Digest
- 2026-07-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-07-09-we-re-also-replacing-the-app-directory-with-the-plugin-directory-existing-app-co|We’re also replacing the App Directory with the Plugin Directory]] · Change
- 2026-07-09 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-09-11-apps-and-integrations-changes-in-rust-v0-144-0|11 Apps and Integrations changes in rust-v0.144.0]] · Digest
- 2026-07-09 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-07-09-chore-bump-sdk-packages-to-v1-34-0-by-all-hands-bot-in-https-github-com-openhand|chore: bump SDK packages to v1.34.0]] · Change
- 2026-07-08 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-08-reserved-the-claude-browser-mcp-server-name-alongside-claude-preview-ahead-of-th|Reserved the "Claude Browser" MCP server name (alongside "Claude Preview") ahead…]] · Change
- 2026-07-08 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-08-66-apps-and-integrations-changes-in-rust-v0-143-0|66 Apps and Integrations changes in rust-v0.143.0]] · Digest
- 2026-07-08 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-07-08-chore-bump-sdk-packages-to-v1-33-0-by-all-hands-bot-in-https-github-com-openhand|chore: bump SDK packages to v1.33.0]] · Change
- 2026-07-07 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-07-2-apps-and-integrations-changes-in-v2-1-203|2 Apps and Integrations changes in v2.1.203]] · Digest
- 2026-07-07 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-07-7-apps-and-integrations-changes-in-v1-0-69|7 Apps and Integrations changes in v1.0.69]] · Digest
- 2026-07-07 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-07-07-2-apps-and-integrations-changes-in-1-9-1|2 Apps and Integrations changes in 1.9.1]] · Digest
- 2026-07-07 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2026-07-07-3-apps-and-integrations-changes-in-grouped-tool-approvals-richer-mcp|3 Apps and Integrations changes in Grouped tool approvals, richer MCP…]] · Digest
- 2026-07-06 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-06-improved-mcp-error-messages-clearer-error-when-a-server-config-has-url-but-no-ty|Improved MCP error messages]] · Change
- 2026-07-06 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-07-06-core-fixed-paginated-mcp-tool-catalogs-losing-tool-metadata-and-output-schema-va|Core Fixed paginated MCP tool catalogs losing tool metadata and output schema validation]] · Change
- 2026-07-06 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-07-06-7-apps-and-integrations-changes-in-1-9-0|7 Apps and Integrations changes in 1.9.0]] · Digest
- 2026-07-02 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-07-02-stacked-slash-skill-invocations-like-skill-a-skill-b-do-xyz-now-load-all-leading|Stacked slash-skill invocations like /skill-a /skill-b do XYZ now load all leading…]] · Change
- 2026-07-01 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-01-2-apps-and-integrations-changes-in-v1-0-68|2 Apps and Integrations changes in v1.0.68]] · Digest

**2026-06**

- 2026-06-30 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-30-9-apps-and-integrations-changes-in-v1-0-66|9 Apps and Integrations changes in v1.0.66]] · Digest
- 2026-06-30 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-30-allow-tool-calls-to-continue-when-hooks-time-out|Allow tool calls to continue when hooks time out]] · Change
- 2026-06-30 · <span class="tl-product tl-p20">**OpenClaw**</span> · [[Changes/OpenClaw/2026-06-30-34-apps-and-integrations-changes-in-v2026-6-11|34 Apps and Integrations changes in v2026.6.11]] · Digest
- 2026-06-30 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-06-30-8-apps-and-integrations-changes-in-v1-17-12|8 Apps and Integrations changes in v1.17.12]] · Digest
- 2026-06-29 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-29-remote-control-is-now-disabled-when-anthropic-base-url-points-at-a-non-anthropic|Remote Control is now disabled when ANTHROPIC_BASE_URL points at a non-Anthropic…]] · Change
- 2026-06-29 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-06-29-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Digest
- 2026-06-28 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-06-28-roll-the-stable-vs-code-extension-back-to-the-pre-sdk-migration-codebase-to-reso|Roll the stable VS Code extension back to the pre-SDK-migration codebase to resolve…]] · Change
- 2026-06-26 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-06-26-13-apps-and-integrations-changes-in-v4-0-0|13 Apps and Integrations changes in v4.0.0]] · Digest
- 2026-06-26 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2026-06-26-the-v0-mcp-server-adds-tools-to-create-find-and-read-chats-fetch-a-preview-and-s|The v0 MCP server adds tools to create, find, and read chats, fetch a preview…]] · Change
- 2026-06-25 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-25-2-apps-and-integrations-changes-in-v2-1-193|2 Apps and Integrations changes in v2.1.193]] · Digest
- 2026-06-25 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-25-9-apps-and-integrations-changes-in-rust-v0-142-2|9 Apps and Integrations changes in rust-v0.142.2]] · Digest
- 2026-06-25 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-06-25-27-apps-and-integrations-changes-in-1-15-0|27 Apps and Integrations changes in 1.15.0]] · Digest
- 2026-06-25 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-06-25-docs-redesign-docs-landing-and-integrations-overview-by-hoyyeva-in-https-github|docs: redesign docs landing and integrations overview]] · Change
- 2026-06-24 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-24-2-apps-and-integrations-changes-in-v2-1-191|2 Apps and Integrations changes in v2.1.191]] · Digest
- 2026-06-24 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-24-2-apps-and-integrations-changes-in-v1-0-65|2 Apps and Integrations changes in v1.0.65]] · Digest
- 2026-06-24 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-06-24-9-apps-and-integrations-changes-in-v1-17-10|9 Apps and Integrations changes in v1.17.10]] · Digest
- 2026-06-23 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-23-2-apps-and-integrations-changes-in-v2-1-187|2 Apps and Integrations changes in v2.1.187]] · Digest
- 2026-06-23 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-23-8-apps-and-integrations-changes-in-v1-0-64|8 Apps and Integrations changes in v1.0.64]] · Digest
- 2026-06-22 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-22-2-apps-and-integrations-changes-in-v2-1-186|2 Apps and Integrations changes in v2.1.186]] · Digest
- 2026-06-22 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-22-37-apps-and-integrations-changes-in-rust-v0-142-0|37 Apps and Integrations changes in rust-v0.142.0]] · Digest
- 2026-06-22 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-22-plugins-skills-and-mcps-let-you-customize-cursor-for-your-workflows-the-new-cust-241c4b|Plugins, skills, and MCPs let you customize Cursor for your workflows]] · Change
- 2026-06-22 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-06-22-2-apps-and-integrations-changes-in-ide-v2-1-1-model-quota-screen|2 Apps and Integrations changes in IDE v2.1.1 — Model quota screen…]] · Digest
- 2026-06-19 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-19-added-attribution-sessionurl-setting-to-omit-the-claude-ai-session-link-from-com|Added attribution.sessionUrl setting to omit the claude.ai session link…]] · Change
- 2026-06-18 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-18-17-apps-and-integrations-changes-in-rust-v0-141-0|17 Apps and Integrations changes in rust-v0.141.0]] · Digest
- 2026-06-18 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2026-06-18-made-mcp-registry-parsing-more-tolerant-of-old-and-inconsistent-schemas|Made MCP registry parsing more tolerant of old and inconsistent schemas]] · Change
- 2026-06-17 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-17-monitoring-tasks-can-search-the-web-and-check-connected-apps-for-changes-and-not|Monitoring tasks can search the web and check connected apps for changes and notify…]] · Change
- 2026-06-17 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-06-17-4-apps-and-integrations-changes-in-v1-17-8|4 Apps and Integrations changes in v1.17.8]] · Digest
- 2026-06-16 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-16-improved-plugin-loading-performance-in-remote-sessions|Improved plugin loading performance in remote sessions]] · Change
- 2026-06-16 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-16-2-apps-and-integrations-changes-in-v1-0-63|2 Apps and Integrations changes in v1.0.63]] · Digest
- 2026-06-16 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2026-06-16-outdated-this-entry-refers-to-the-devin-plugin-command-which-has-since-been-rena| Outdated: this entry refers to the devin plugin command, which has since…]] · Change
- 2026-06-16 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2026-06-16-improved-handling-for-less-common-mcp-server-features|Improved handling for less common MCP server features]] · Change
- 2026-06-15 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-15-2-apps-and-integrations-changes-in-v2-1-178|2 Apps and Integrations changes in v2.1.178]] · Digest
- 2026-06-15 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-15-35-apps-and-integrations-changes-in-rust-v0-140-0|35 Apps and Integrations changes in rust-v0.140.0]] · Digest
- 2026-06-14 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-06-14-4-apps-and-integrations-changes-in-v1-17-7|4 Apps and Integrations changes in v1.17.7]] · Digest
- 2026-06-13 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-13-8-apps-and-integrations-changes-in-v1-0-62|8 Apps and Integrations changes in v1.0.62]] · Digest
- 2026-06-13 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-06-13-4-apps-and-integrations-changes-in-v1-17-6-1|4 Apps and Integrations changes in v1.17.6 + 1]] · Digest
- 2026-06-12 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-06-12-4-apps-and-integrations-changes-in-v1-17-4|4 Apps and Integrations changes in v1.17.4]] · Digest
- 2026-06-11 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-06-11-2-apps-and-integrations-changes-in-v3-89-2|2 Apps and Integrations changes in v3.89.2]] · Digest
- 2026-06-11 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-06-11-restore-the-anthropic-provider-on-vs-code-1-123-and-later-where-the-updated-node|Restore the Anthropic provider on VS Code 1.123 and later, where the updated Node 24…]] · Change
- 2026-06-11 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-06-11-2-apps-and-integrations-changes-in-hub-v2-1-4-quota-screen-redesign|2 Apps and Integrations changes in HUB v2.1.4 — Quota Screen Redesign…]] · Digest
- 2026-06-10 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-10-3-apps-and-integrations-changes-in-v2-1-172|3 Apps and Integrations changes in v2.1.172]] · Digest
- 2026-06-10 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-06-10-7-apps-and-integrations-changes-in-v1-17-0|7 Apps and Integrations changes in v1.17.0]] · Digest
- 2026-06-10 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-06-10-2-apps-and-integrations-changes-in-v1-17-1|2 Apps and Integrations changes in v1.17.1]] · Digest
- 2026-06-09 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-09-8-apps-and-integrations-changes-in-rust-v0-139-0|8 Apps and Integrations changes in rust-v0.139.0]] · Digest
- 2026-06-09 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-09-4-apps-and-integrations-changes-in-v1-0-61|4 Apps and Integrations changes in v1.0.61]] · Digest
- 2026-06-08 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-08-19-apps-and-integrations-changes-in-rust-v0-138-0|19 Apps and Integrations changes in rust-v0.138.0]] · Digest
- 2026-06-08 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2026-06-08-4-apps-and-integrations-changes-in-changelog-update|4 Apps and Integrations changes in Changelog update]] · Digest
- 2026-06-07 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-06-07-ollama-launch-now-supports-hermes-desktop-a-native-desktop-interface-for-the-her|Ollama Launch now supports Hermes Desktop, a native desktop interface for the Hermes agent]] · Change
- 2026-06-06 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-06-added-glob-pattern-support-in-deny-rule-tool-name-position-denies-all-tools-allo|Added glob pattern support in deny rule tool-name position ("" denies all tools)]] · Change
- 2026-06-05 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-05-10-apps-and-integrations-changes-in-v1-0-60|10 Apps and Integrations changes in v1.0.60]] · Digest
- 2026-06-05 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-06-05-ollama-launch-omp-now-integrates-with-oh-my-pi-https-omp-sh-an-ai-coding-agent-w|ollama launch omp now integrates with Oh My Pi((source link) an AI coding…]] · Change
- 2026-06-05 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-06-05-2-apps-and-integrations-changes-in-v1-16-0|2 Apps and Integrations changes in v1.16.0]] · Digest
- 2026-06-04 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-04-2-apps-and-integrations-changes-in-v2-1-163|2 Apps and Integrations changes in v2.1.163]] · Digest
- 2026-06-04 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-04-19-apps-and-integrations-changes-in-rust-v0-137-0|19 Apps and Integrations changes in rust-v0.137.0]] · Digest
- 2026-06-04 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-04-we-ve-shipped-a-batch-of-new-functionality-across-the-typescript-and-python-sdks|We've shipped a batch of new functionality across the TypeScript and Python SDKs]] · Change
- 2026-06-04 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-06-04-2-apps-and-integrations-changes-in-custom-stores-custom-tools|2 Apps and Integrations changes in Custom stores, custom tools…]] · Digest
- 2026-06-04 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-06-04-added-cline-cli-integration-docs|Added Cline CLI integration docs]] · Change
- 2026-06-03 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-03-remote-control-now-shows-as-a-persistent-footer-pill-with-a-link-to-the-session|Remote Control now shows as a persistent footer pill (with a link to the session)…]] · Change
- 2026-06-02 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-02-mcp-now-collapses-claude-ai-connectors-you-ve-never-signed-in-to-behind-a-show-u|/mcp now collapses claude.ai connectors you've never signed in to behind…]] · Change
- 2026-06-02 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-06-02-removed-the-jetbrains-plugin-install-suggestion-from-startup|Removed the JetBrains plugin install suggestion from startup]] · Change
- 2026-06-01 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-01-20-apps-and-integrations-changes-in-rust-v0-136-0|20 Apps and Integrations changes in rust-v0.136.0]] · Digest
- 2026-06-01 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-01-5-apps-and-integrations-changes-in-v1-0-57|5 Apps and Integrations changes in v1.0.57]] · Digest
- 2026-06-01 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-06-01-4-apps-and-integrations-changes-in-v0-9-6|4 Apps and Integrations changes in v0.9.6]] · Digest

**2026-05**

- 2026-05-29 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-29-4-apps-and-integrations-changes-in-v2-1-157|4 Apps and Integrations changes in v2.1.157]] · Digest
- 2026-05-29 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-29-2-apps-and-integrations-changes-in-v1-0-56|2 Apps and Integrations changes in v1.0.56]] · Digest
- 2026-05-28 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-28-2-apps-and-integrations-changes-in-v2-1-153|2 Apps and Integrations changes in v2.1.153]] · Digest
- 2026-05-28 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-28-4-apps-and-integrations-changes-in-v2-1-154|4 Apps and Integrations changes in v2.1.154]] · Digest
- 2026-05-28 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-05-28-move-the-vs-code-extension-project-into-apps-vscode|Move the VS Code extension project into apps/vscode]] · Change
- 2026-05-28 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-28-14-apps-and-integrations-changes-in-rust-v0-135-0|14 Apps and Integrations changes in rust-v0.135.0]] · Digest
- 2026-05-28 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-28-10-apps-and-integrations-changes-in-v1-0-55|10 Apps and Integrations changes in v1.0.55]] · Digest
- 2026-05-27 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-27-4-apps-and-integrations-changes-in-v2-1-152|4 Apps and Integrations changes in v2.1.152]] · Digest
- 2026-05-27 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-27-docs-extensions-clarify-env-var-sanitization-policy-for-mcp-and-ext-by-galz10-in|docs(extensions): clarify env var sanitization policy for MCP and ext…]] · Change
- 2026-05-27 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-05-27-3-apps-and-integrations-changes-in-v1-15-11|3 Apps and Integrations changes in v1.15.11]] · Digest
- 2026-05-26 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-26-11-apps-and-integrations-changes-in-rust-v0-134-0|11 Apps and Integrations changes in rust-v0.134.0]] · Digest
- 2026-05-25 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-05-25-add-lg-task-uri-webhook-integration-for-lg-dashboard-flows|Add /lg-task URI webhook integration for LG dashboard flows]] · Change
- 2026-05-23 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-23-2-apps-and-integrations-changes-in-v1-0-52|2 Apps and Integrations changes in v1.0.52]] · Digest
- 2026-05-22 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-22-2-apps-and-integrations-changes-in-v2-1-149|2 Apps and Integrations changes in v2.1.149]] · Digest
- 2026-05-22 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-22-docs-extensions-refactor-releasing-guide-and-add-update-mechanisms-by-ruomengz-i|docs(extensions): refactor releasing guide and add update mechanisms]] · Change
- 2026-05-22 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-05-22-core-return-mcp-server-not-found-errors-from-the-http-api|Core Return MCP server not found errors from the HTTP API]] · Change
- 2026-05-21 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-21-20-apps-and-integrations-changes-in-rust-v0-133-0|20 Apps and Integrations changes in rust-v0.133.0]] · Digest
- 2026-05-21 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-05-21-added-a-migration-flow-that-allows-users-to-import-settings-extensions-and-keybi|Added a migration flow that allows users to import settings, extensions…]] · Change
- 2026-05-21 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-05-21-sdk-v2-global-event-streams-now-include-account-add-remove-and-switch-events|SDK V2 global event streams now include account add, remove, and switch events]] · Change
- 2026-05-20 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-20-9-apps-and-integrations-changes-in-rust-v0-132-0|9 Apps and Integrations changes in rust-v0.132.0]] · Digest
- 2026-05-20 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-20-4-apps-and-integrations-changes-in-v1-0-51|4 Apps and Integrations changes in v1.0.51]] · Digest
- 2026-05-20 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-05-20-3-apps-and-integrations-changes-in-v1-15-6|3 Apps and Integrations changes in v1.15.6]] · Digest
- 2026-05-19 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-19-plugin-discover-and-browse-screens-now-show-a-plugin-s-commands-agents-skills-ho|/plugin Discover and Browse screens now show a plugin's commands, agents, skills…]] · Change
- 2026-05-19 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-19-3-apps-and-integrations-changes-in-v2-1-144|3 Apps and Integrations changes in v2.1.144]] · Digest
- 2026-05-19 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-05-19-disable-the-mcp-restart-server-button-when-a-server-is-toggled-off|Disable the MCP "Restart Server" button when a server is toggled off]] · Change
- 2026-05-19 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-05-19-install-the-integration-from-cursor-integrations-you-need-cursor-admin-access-an|Install the integration from Cursor integrations]] · Change
- 2026-05-19 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-05-19-4-apps-and-integrations-changes-in-1-14-2|4 Apps and Integrations changes in 1.14.2]] · Digest
- 2026-05-19 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-19-9-apps-and-integrations-changes-in-v1-0-49|9 Apps and Integrations changes in v1.0.49]] · Digest
- 2026-05-18 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-18-56-apps-and-integrations-changes-in-rust-v0-131-0|56 Apps and Integrations changes in rust-v0.131.0]] · Digest
- 2026-05-18 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2026-05-18-improved-github-integration|Improved GitHub integration]] · Change
- 2026-05-18 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-05-18-core-fix-plugin-tools-using-ask-so-tool-calls-complete-correctly|Core Fix plugin tools using ask so tool calls complete correctly]] · Change
- 2026-05-15 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-15-3-apps-and-integrations-changes-in-v2-1-143|3 Apps and Integrations changes in v2.1.143]] · Digest
- 2026-05-15 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-05-15-2-apps-and-integrations-changes-in-v1-15-0|2 Apps and Integrations changes in v1.15.0]] · Digest
- 2026-05-15 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2026-05-15-the-built-with-v0-badge-respects-branding-settings-on-deployed-apps-and-the-prev|The "built with v0" badge respects branding settings on deployed apps…]] · Change
- 2026-05-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-14-3-apps-and-integrations-changes-in-v2-1-142|3 Apps and Integrations changes in v2.1.142]] · Digest
- 2026-05-14 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-14-auto-disable-the-built-in-github-mcp-server-in-azure-devops-only-workspaces-when|Auto-disable the built-in github-mcp-server in Azure DevOps-only workspaces…]] · Change
- 2026-05-13 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-13-added-claude-code-plugin-prefer-https-to-clone-github-plugin-sources-over-https|Added CLAUDE_CODE_PLUGIN_PREFER_HTTPS to clone GitHub plugin sources over HTTPS…]] · Change
- 2026-05-13 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-05-13-improved-mcp-auth-token-lifecycle-handling|Improved MCP auth token lifecycle handling]] · Change
- 2026-05-12 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-12-plugins-now-warn-when-a-default-component-folder-e-g-commands-is-silently-ignore|Plugins now warn when a default component folder (e.g. commands/) is silently…]] · Change
- 2026-05-12 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-05-12-4-apps-and-integrations-changes-in-1-14-1|4 Apps and Integrations changes in 1.14.1]] · Digest
- 2026-05-12 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-12-5-apps-and-integrations-changes-in-v0-42-0|5 Apps and Integrations changes in v0.42.0]] · Digest
- 2026-05-12 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-05-12-test-integration-test-hardening-by-dhiltgen-in-https-github-com-ollama-ollama-pu|test: integration test hardening]] · Change
- 2026-05-12 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2026-05-12-custom-auth-headers-for-connected-mcp-servers-no-longer-get-stripped-after-the-f|Custom auth headers for connected MCP servers no longer get stripped after the first…]] · Change
- 2026-05-11 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-11-8-apps-and-integrations-changes-in-v2-1-139|8 Apps and Integrations changes in v2.1.139]] · Digest
- 2026-05-11 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-05-11-get-started-by-installing-the-integration-in-the-cursor-dashboard-learn-more-in|Get started by installing the integration in the Cursor dashboard]] · Change
- 2026-05-11 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-11-opentelemetry-output-aligns-with-genai-semantic-conventions-mcp-tool-calls-now-u|OpenTelemetry output aligns with GenAI semantic conventions]] · Change
- 2026-05-10 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-05-10-2-apps-and-integrations-changes-in-v1-14-45|2 Apps and Integrations changes in v1.14.45]] · Digest
- 2026-05-10 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-05-10-3-apps-and-integrations-changes-in-v1-14-46|3 Apps and Integrations changes in v1.14.46]] · Digest
- 2026-05-09 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-05-09-3-apps-and-integrations-changes-in-v0-9-3|3 Apps and Integrations changes in v0.9.3]] · Digest
- 2026-05-08 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-08-changed-plugin-marketplace-removal-key-to-d-matching-delete-elsewhere-instead-of|Changed plugin marketplace removal key to d (matching delete elsewhere) instead…]] · Change
- 2026-05-08 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-08-8-apps-and-integrations-changes-in-rust-v0-130-0|8 Apps and Integrations changes in rust-v0.130.0]] · Digest
- 2026-05-07 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-07-2-apps-and-integrations-changes-in-v2-1-133|2 Apps and Integrations changes in v2.1.133]] · Digest
- 2026-05-07 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-07-39-apps-and-integrations-changes-in-rust-v0-129-0|39 Apps and Integrations changes in rust-v0.129.0]] · Digest
- 2026-05-07 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-05-07-made-mcp-connection-behavior-more-predictable-and-added-explicit-stale-token-cle|Made MCP connection behavior more predictable, and added explicit stale token…]] · Change
- 2026-05-07 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-05-07-2-apps-and-integrations-changes-in-v0-23-2|2 Apps and Integrations changes in v0.23.2]] · Digest
- 2026-05-06 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-06-added-claude-code-session-id-environment-variable-to-the-bash-tool-subprocess-en|Added CLAUDE_CODE_SESSION_ID environment variable to the Bash tool subprocess…]] · Change
- 2026-05-06 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-06-3-apps-and-integrations-changes-in-v2-1-129|3 Apps and Integrations changes in v2.1.129]] · Digest
- 2026-05-06 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-06-mcp-server-child-processes-e-g-started-via-npx-or-uvx-are-now-fully-terminated-w|MCP server child processes (e.g. started via npx or uvx) are now fully terminated…]] · Change
- 2026-05-06 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-06-2-apps-and-integrations-changes-in-v1-0-42|2 Apps and Integrations changes in v1.0.42]] · Digest
- 2026-05-05 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-05-2-apps-and-integrations-changes-in-v1-0-41|2 Apps and Integrations changes in v1.0.41]] · Digest
- 2026-05-04 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-05-04-6-apps-and-integrations-changes-in-v2-1-128|6 Apps and Integrations changes in v2.1.128]] · Digest
- 2026-05-04 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-05-04-core-show-real-server-error-messages-in-the-cli-and-sdk-instead-of-bare|Core Show real server error messages in the CLI and SDK instead of bare {}]] · Change
- 2026-05-01 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-01-6-apps-and-integrations-changes-in-v1-0-40|6 Apps and Integrations changes in v1.0.40]] · Digest
- 2026-05-01 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-05-01-core-invalid-remote-mcp-urls-now-fail-with-a-clear-error-instead-of-breaking-set|Core Invalid remote MCP URLs now fail with a clear error instead of breaking setup]] · Change
- 2026-05-01 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-05-01-2-apps-and-integrations-changes-in-1-7-0|2 Apps and Integrations changes in 1.7.0]] · Digest

**2026-04**

- 2026-04-30 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-30-37-apps-and-integrations-changes-in-rust-v0-128-0|37 Apps and Integrations changes in rust-v0.128.0]] · Digest
- 2026-04-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-29-run-npm-install-cursor-sdk-to-get-started-you-can-also-use-cursor-s-native-sdk-s-76fb76|Run npm install @cursor/sdk to get started]] · Change
- 2026-04-29 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-04-29-48-apps-and-integrations-changes-in-1-14-0|48 Apps and Integrations changes in 1.14.0]] · Digest
- 2026-04-28 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-28-2-apps-and-integrations-changes-in-v2-1-122|2 Apps and Integrations changes in v2.1.122]] · Digest
- 2026-04-28 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-28-6-apps-and-integrations-changes-in-v2-1-121|6 Apps and Integrations changes in v2.1.121]] · Digest
- 2026-04-28 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-28-2-apps-and-integrations-changes-in-v0-40-0|2 Apps and Integrations changes in v0.40.0]] · Digest
- 2026-04-28 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-04-28-aligned-the-desktop-app-s-launch-page-with-ollama-launch-integrations|Aligned the desktop app's launch page with ollama launch integrations]] · Change
- 2026-04-28 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-04-28-desktop-sync-state-loading-is-more-reliable-for-mcp-lsp-and-workspace-refreshes|Desktop Sync state loading is more reliable for MCP, LSP, and workspace refreshes]] · Change
- 2026-04-24 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-24-11-apps-and-integrations-changes-in-rust-v0-125-0|11 Apps and Integrations changes in rust-v0.125.0]] · Digest
- 2026-04-24 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-24-remote-command-shows-current-status-and-supports-remote-on-and-remote-off-to-tog|/remote command shows current status and supports /remote on and /remote off…]] · Change
- 2026-04-24 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-04-24-2-apps-and-integrations-changes-in-v0-9-2|2 Apps and Integrations changes in v0.9.2]] · Digest
- 2026-04-23 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-23-3-apps-and-integrations-changes-in-v2-1-119|3 Apps and Integrations changes in v2.1.119]] · Digest
- 2026-04-23 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-23-5-apps-and-integrations-changes-in-v2-1-118|5 Apps and Integrations changes in v2.1.118]] · Digest
- 2026-04-23 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-12-apps-and-integrations-changes-in-rust-v0-124-0|12 Apps and Integrations changes in rust-v0.124.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-9-apps-and-integrations-changes-in-rust-v0-123-0|9 Apps and Integrations changes in rust-v0.123.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-23-4-apps-and-integrations-changes-in-v0-39-0|4 Apps and Integrations changes in v0.39.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-23-3-apps-and-integrations-changes-in-v1-0-35|3 Apps and Integrations changes in v1.0.35]] · Digest
- 2026-04-23 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-04-23-openclaw-integration-now-bundles-ollama-s-web-search-plugin-in-openclaw|OpenClaw integration now bundles Ollama's web search plugin in OpenClaw]] · Change
- 2026-04-22 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-22-4-apps-and-integrations-changes-in-v2-1-117|4 Apps and Integrations changes in v2.1.117]] · Digest
- 2026-04-22 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-04-22-wire-up-remote-globalskills-from-enterprise-remote-config-with-full-ui-toggle-su|Wire up remote globalSkills from enterprise remote config with full UI, toggle…]] · Change
- 2026-04-21 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-04-21-4-apps-and-integrations-changes-in-v0-9-0|4 Apps and Integrations changes in v0.9.0]] · Digest
- 2026-04-21 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-04-21-2-apps-and-integrations-changes-in-v1-14-20|2 Apps and Integrations changes in v1.14.20]] · Digest
- 2026-04-20 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-20-2-apps-and-integrations-changes-in-v2-1-116|2 Apps and Integrations changes in v2.1.116]] · Digest
- 2026-04-20 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-20-28-apps-and-integrations-changes-in-rust-v0-122-0|28 Apps and Integrations changes in rust-v0.122.0]] · Digest
- 2026-04-19 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-04-19-2-apps-and-integrations-changes-in-v1-14-18-1|2 Apps and Integrations changes in v1.14.18 + 1]] · Digest
- 2026-04-17 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-04-17-core-let-plugin-tools-return-metadata-in-execute-results|Core Let plugin tools return metadata in execute results]] · Change
- 2026-04-16 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-16-2-apps-and-integrations-changes-in-v2-1-111|2 Apps and Integrations changes in v2.1.111]] · Digest
- 2026-04-16 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-16-2-apps-and-integrations-changes-in-v1-0-30|2 Apps and Integrations changes in v1.0.30]] · Digest
- 2026-04-16 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-16-mcp-migration-hint-now-links-to-documentation-with-platform-specific-instruction|MCP migration hint now links to documentation with platform-specific instructions…]] · Change
- 2026-04-16 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-16-3-apps-and-integrations-changes-in-v1-0-29|3 Apps and Integrations changes in v1.0.29]] · Digest
- 2026-04-16 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-04-16-2-apps-and-integrations-changes-in-v0-21-0|2 Apps and Integrations changes in v0.21.0]] · Digest
- 2026-04-16 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-04-16-2-apps-and-integrations-changes-in-v1-4-7|2 Apps and Integrations changes in v1.4.7]] · Digest
- 2026-04-15 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-15-4-apps-and-integrations-changes-in-v2-1-110|4 Apps and Integrations changes in v2.1.110]] · Digest
- 2026-04-15 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-15-9-apps-and-integrations-changes-in-rust-v0-121-0|9 Apps and Integrations changes in rust-v0.121.0]] · Digest
- 2026-04-15 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-15-add-copilot-plugin-marketplace-update-command-to-refresh-plugin-catalogs|Add copilot plugin marketplace update command to refresh plugin catalogs]] · Change
- 2026-04-15 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-04-15-4-apps-and-integrations-changes-in-v1-4-4|4 Apps and Integrations changes in v1.4.4]] · Digest
- 2026-04-14 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-14-2-apps-and-integrations-changes-in-v0-38-0|2 Apps and Integrations changes in v0.38.0]] · Digest
- 2026-04-14 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-14-4-apps-and-integrations-changes-in-v1-0-26|4 Apps and Integrations changes in v1.0.26]] · Digest
- 2026-04-13 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-13-3-apps-and-integrations-changes-in-v2-1-105|3 Apps and Integrations changes in v2.1.105]] · Digest
- 2026-04-13 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-13-5-apps-and-integrations-changes-in-v1-0-25|5 Apps and Integrations changes in v1.0.25]] · Digest
- 2026-04-11 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-11-4-apps-and-integrations-changes-in-rust-v0-120-0|4 Apps and Integrations changes in rust-v0.120.0]] · Digest
- 2026-04-10 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-10-4-apps-and-integrations-changes-in-v2-1-101|4 Apps and Integrations changes in v2.1.101]] · Digest
- 2026-04-10 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-10-19-apps-and-integrations-changes-in-rust-v0-119-0|19 Apps and Integrations changes in rust-v0.119.0]] · Digest
- 2026-04-10 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-10-pretooluse-hooks-now-respect-modifiedargs-updatedinput-and-additionalcontext-fie|preToolUse hooks now respect modifiedArgs/updatedInput, and additionalContext fields]] · Change
- 2026-04-10 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-10-migration-notice-for-vscode-mcp-json-now-includes-a-jq-command-to-migrate-your-c|Migration notice for .vscode/mcp.json now includes a jq command to migrate…]] · Change
- 2026-04-09 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-09-2-apps-and-integrations-changes-in-v2-1-98|2 Apps and Integrations changes in v2.1.98]] · Digest
- 2026-04-09 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-09-7-apps-and-integrations-changes-in-v1-0-22|7 Apps and Integrations changes in v1.0.22]] · Digest
- 2026-04-09 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-04-09-sdk-fix-the-generated-sdk-and-openapi-types-for-providers-and-session-shell-resp|SDK Fix the generated SDK and OpenAPI types for /providers and session shell responses]] · Change
- 2026-04-08 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-08-3-apps-and-integrations-changes-in-v0-37-0|3 Apps and Integrations changes in v0.37.0]] · Digest
- 2026-04-07 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-07-5-apps-and-integrations-changes-in-v2-1-94|5 Apps and Integrations changes in v2.1.94]] · Digest
- 2026-04-07 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-07-2-apps-and-integrations-changes-in-v1-0-21|2 Apps and Integrations changes in v1.0.21]] · Digest
- 2026-04-07 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-07-azure-openai-byok-defaults-to-the-ga-versionless-v1-route-when-no-api-version-is|Azure OpenAI BYOK defaults to the GA versionless v1 route when no API version…]] · Change
- 2026-04-06 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-06-2-apps-and-integrations-changes-in-v1-0-19|2 Apps and Integrations changes in v1.0.19]] · Digest
- 2026-04-06 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-04-06-extensions-fix-plugin-installs-from-npm-aliases-and-git-urls-including-windows-c|Extensions Fix plugin installs from npm aliases and git URLs, including Windows…]] · Change
- 2026-04-04 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-04-remote-control-session-names-now-use-your-hostname-as-the-default-prefix-e-g-myh|Remote Control session names now use your hostname as the default prefix…]] · Change
- 2026-04-04 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-04-04-3-apps-and-integrations-changes-in-v1-3-15-1|3 Apps and Integrations changes in v1.3.15 + 1]] · Digest
- 2026-04-02 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-02-4-apps-and-integrations-changes-in-v2-1-91|4 Apps and Integrations changes in v2.1.91]] · Digest
- 2026-04-02 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-04-02-2-apps-and-integrations-changes-in-3-0|2 Apps and Integrations changes in 3.0]] · Digest
- 2026-04-02 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-02-mcp-tool-calls-display-tool-name-and-parameter-summary-in-the-timeline|MCP tool calls display tool name and parameter summary in the timeline]] · Change
- 2026-04-01 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-01-3-apps-and-integrations-changes-in-v2-1-89|3 Apps and Integrations changes in v2.1.89]] · Digest
- 2026-04-01 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-04-01-2-apps-and-integrations-changes-in-v2-1-90|2 Apps and Integrations changes in v2.1.90]] · Digest
- 2026-04-01 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-01-5-apps-and-integrations-changes-in-v0-36-0|5 Apps and Integrations changes in v0.36.0]] · Digest
- 2026-04-01 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-01-5-apps-and-integrations-changes-in-v1-0-15|5 Apps and Integrations changes in v1.0.15]] · Digest

**2026-03**

- 2026-03-31 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-31-12-apps-and-integrations-changes-in-rust-v0-118-0|12 Apps and Integrations changes in rust-v0.118.0]] · Digest
- 2026-03-31 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-31-5-apps-and-integrations-changes-in-v1-0-14|5 Apps and Integrations changes in v1.0.14]] · Digest
- 2026-03-31 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-03-31-4-apps-and-integrations-changes-in-v1-3-12-2|4 Apps and Integrations changes in v1.3.12 + 2]] · Digest
- 2026-03-30 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-30-5-apps-and-integrations-changes-in-v1-0-13|5 Apps and Integrations changes in v1.0.13]] · Digest
- 2026-03-30 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-03-30-2-apps-and-integrations-changes-in-v1-3-9-1|2 Apps and Integrations changes in v1.3.9 + 1]] · Digest
- 2026-03-30 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2026-03-30-added-support-for-hooks-by-xingyaoww-in-https-github-com-openhands-openhands-pul|Added support for hooks]] · Change
- 2026-03-29 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-03-29-8-apps-and-integrations-changes-in-v1-3-6-2|8 Apps and Integrations changes in v1.3.6 + 2]] · Digest
- 2026-03-27 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-03-27-we-re-rolling-out-updated-box-notion-linear-and-dropbox-apps-in-chatgpt-these-up-9f6ee9|Updated Box, Notion, Linear, and Dropbox apps]] · Change
- 2026-03-27 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|Reduced startup event-loop stalls when many claude.ai MCP connectors are configured…]] · Change
- 2026-03-27 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-03-27-6-apps-and-integrations-changes-in-1-13-3|6 Apps and Integrations changes in 1.13.3]] · Digest
- 2026-03-26 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-26-5-apps-and-integrations-changes-in-v2-1-84|5 Apps and Integrations changes in v2.1.84]] · Digest
- 2026-03-26 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-26-4-apps-and-integrations-changes-in-v2-1-85|4 Apps and Integrations changes in v2.1.85]] · Digest
- 2026-03-26 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-26-57-apps-and-integrations-changes-in-rust-v0-117-0|57 Apps and Integrations changes in rust-v0.117.0]] · Digest
- 2026-03-26 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-26-4-apps-and-integrations-changes-in-v1-0-12|4 Apps and Integrations changes in v1.0.12]] · Digest
- 2026-03-25 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-03-25-google-s-file-connectors-in-chatgpt-are-now-unified-under-google-drive-providing|Google Drive app unification]] · Change
- 2026-03-25 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-25-6-apps-and-integrations-changes-in-v2-1-83|6 Apps and Integrations changes in v2.1.83]] · Digest
- 2026-03-25 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-03-25-openclaw-integration-improvements-for-gateway-checks|OpenClaw integration improvements for gateway checks]] · Change
- 2026-03-25 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-03-25-3-apps-and-integrations-changes-in-v0-8-11|3 Apps and Integrations changes in v0.8.11]] · Digest
- 2026-03-24 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-24-5-apps-and-integrations-changes-in-v0-35-0|5 Apps and Integrations changes in v0.35.0]] · Digest
- 2026-03-23 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-23-6-apps-and-integrations-changes-in-v1-0-11|6 Apps and Integrations changes in v1.0.11]] · Digest
- 2026-03-20 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-20-3-apps-and-integrations-changes-in-v2-1-81|3 Apps and Integrations changes in v2.1.81]] · Digest
- 2026-03-20 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-03-20-2-apps-and-integrations-changes-in-v3-75-0|2 Apps and Integrations changes in v3.75.0]] · Digest
- 2026-03-20 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-20-6-apps-and-integrations-changes-in-v1-0-10|6 Apps and Integrations changes in v1.0.10]] · Digest
- 2026-03-19 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-19-4-apps-and-integrations-changes-in-v2-1-80|4 Apps and Integrations changes in v2.1.80]] · Digest
- 2026-03-19 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-19-10-apps-and-integrations-changes-in-rust-v0-116-0|10 Apps and Integrations changes in rust-v0.116.0]] · Digest
- 2026-03-19 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-19-marketplace-and-plugin-installs-from-shortened-urls-e-g-aka-ms-links-now-work-co|Marketplace and plugin installs from shortened URLs (e.g., aka.ms links) now work…]] · Change
- 2026-03-18 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-18-2-apps-and-integrations-changes-in-v2-1-79|2 Apps and Integrations changes in v2.1.79]] · Digest
- 2026-03-18 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-03-18-4-apps-and-integrations-changes-in-1-13-2|4 Apps and Integrations changes in 1.13.2]] · Digest
- 2026-03-18 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-18-3-apps-and-integrations-changes-in-v1-0-8|3 Apps and Integrations changes in v1.0.8]] · Digest
- 2026-03-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-17-3-apps-and-integrations-changes-in-v2-1-78|3 Apps and Integrations changes in v2.1.78]] · Digest
- 2026-03-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-17-2-apps-and-integrations-changes-in-v2-1-77|2 Apps and Integrations changes in v2.1.77]] · Digest
- 2026-03-17 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-03-17-27-apps-and-integrations-changes-in-1-13-1|27 Apps and Integrations changes in 1.13.1]] · Digest
- 2026-03-17 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-17-4-apps-and-integrations-changes-in-v0-34-0|4 Apps and Integrations changes in v0.34.0]] · Digest
- 2026-03-17 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-17-add-experimental-sdk-session-apis-to-list-and-manage-skills-mcp-servers-and-plug|Add experimental SDK session APIs to list and manage skills, MCP servers…]] · Change
- 2026-03-17 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-03-17-docker-containers-spin-up-an-integration-as-a-pipeline-step-to-run-evals-test-pr|Docker/containers: spin up an integration as a pipeline step to run evals, test…]] · Change
- 2026-03-16 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-16-17-apps-and-integrations-changes-in-rust-v0-115-0|17 Apps and Integrations changes in rust-v0.115.0]] · Digest
- 2026-03-16 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-16-6-apps-and-integrations-changes-in-v1-0-6|6 Apps and Integrations changes in v1.0.6]] · Digest
- 2026-03-14 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-14-4-apps-and-integrations-changes-in-v2-1-76|4 Apps and Integrations changes in v2.1.76]] · Digest
- 2026-03-13 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-13-4-apps-and-integrations-changes-in-v1-0-5|4 Apps and Integrations changes in v1.0.5]] · Digest
- 2026-03-12 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-12-changed-plugin-dir-so-local-dev-copies-now-override-installed-marketplace-plugin|Changed --plugin-dir so local dev copies now override installed marketplace…]] · Change
- 2026-03-12 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-03-12-hooks-reintroduced-feature-toggle|Hooks: reintroduced feature toggle]] · Change
- 2026-03-12 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-03-12-2-apps-and-integrations-changes-in-v1-2-25|2 Apps and Integrations changes in v1.2.25]] · Digest
- 2026-03-11 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-11-8-apps-and-integrations-changes-in-rust-v0-114-0|8 Apps and Integrations changes in rust-v0.114.0]] · Digest
- 2026-03-11 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-03-11-we-ve-added-more-than-30-new-plugins-from-partners-such-as-atlassian-datadog-git-901313|New Plugins on the Cursor Marketplace]] · Change
- 2026-03-11 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-11-4-apps-and-integrations-changes-in-v0-33-0|4 Apps and Integrations changes in v0.33.0]] · Digest
- 2026-03-11 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-11-4-apps-and-integrations-changes-in-v1-0-4|4 Apps and Integrations changes in v1.0.4]] · Digest
- 2026-03-11 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2026-03-11-added-one-click-marketplace-integration-installation-for-ios-app|Added one-click marketplace integration installation for iOS app]] · Change
- 2026-03-10 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-10-3-apps-and-integrations-changes-in-v2-1-72|3 Apps and Integrations changes in v2.1.72]] · Digest
- 2026-03-10 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-10-11-apps-and-integrations-changes-in-rust-v0-113-0|11 Apps and Integrations changes in rust-v0.113.0]] · Digest
- 2026-03-09 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-09-4-apps-and-integrations-changes-in-v1-0-3|4 Apps and Integrations changes in v1.0.3]] · Digest
- 2026-03-08 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-08-2-apps-and-integrations-changes-in-rust-v0-112-0|2 Apps and Integrations changes in rust-v0.112.0]] · Digest
- 2026-03-08 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-03-08-core-fix-broken-mcp-toggling-in-tui|Core Fix broken MCP toggling in TUI]] · Change
- 2026-03-07 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-07-3-apps-and-integrations-changes-in-v2-1-71|3 Apps and Integrations changes in v2.1.71]] · Digest
- 2026-03-06 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-06-reduced-remote-control-poll-rate-to-once-per-10-minutes-while-connected-was-1-2s|Reduced Remote Control /poll rate to once per 10 minutes while connected…]] · Change
- 2026-03-06 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-03-06-handle-streamable-http-mcp-reconnects-more-reliably-after-disconnects|Handle streamable HTTP MCP reconnects more reliably after disconnects]] · Change
- 2026-03-05 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-03-05-7-apps-and-integrations-changes-in-v2-1-69|7 Apps and Integrations changes in v2.1.69]] · Digest
- 2026-03-05 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-05-7-apps-and-integrations-changes-in-rust-v0-110-0|7 Apps and Integrations changes in rust-v0.110.0]] · Digest
- 2026-03-05 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-05-5-apps-and-integrations-changes-in-rust-v0-111-0|5 Apps and Integrations changes in rust-v0.111.0]] · Digest
- 2026-03-05 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-05-11-apps-and-integrations-changes-in-v0-0-422|11 Apps and Integrations changes in v0.0.422]] · Digest
- 2026-03-05 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-03-05-sdk-update-sdk-package-json|SDK Update SDK package.json]] · Change
- 2026-03-04 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-03-04-updated-hooks-docs|Updated hooks docs]] · Change
- 2026-03-03 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-03-03-3-apps-and-integrations-changes-in-v3-69-0|3 Apps and Integrations changes in v3.69.0]] · Digest
- 2026-03-03 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-03-03-3-apps-and-integrations-changes-in-2-6|3 Apps and Integrations changes in 2.6]] · Digest
- 2026-03-03 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-03-3-apps-and-integrations-changes-in-v0-32-0|3 Apps and Integrations changes in v0.32.0]] · Digest
- 2026-03-03 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-03-7-apps-and-integrations-changes-in-v0-0-421|7 Apps and Integrations changes in v0.0.421]] · Digest
- 2026-03-03 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-03-03-2-apps-and-integrations-changes-in-v1-2-16|2 Apps and Integrations changes in v1.2.16]] · Digest
- 2026-03-02 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-02-3-apps-and-integrations-changes-in-rust-v0-107-0|3 Apps and Integrations changes in rust-v0.107.0]] · Digest
- 2026-03-02 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2026-03-02-2-apps-and-integrations-changes-in-bug-fixes-and-improvements-for-mar-2nd|2 Apps and Integrations changes in Bug fixes and improvements for Mar 2nd]] · Digest

**2026-02**

- 2026-02-28 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-28-added-enable-claudeai-mcp-servers-false-env-var-to-opt-out-from-making-claude-ai|Added ENABLE_CLAUDEAI_MCP_SERVERS=false env var to opt out from making claude.ai…]] · Change
- 2026-02-27 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-27-10-apps-and-integrations-changes-in-v0-31-0|10 Apps and Integrations changes in v0.31.0]] · Digest
- 2026-02-27 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-27-plugin-and-marketplace-git-repos-update-correctly-after-force-pushes-and-tag-bas|Plugin and marketplace git repos update correctly after force-pushes and tag-based…]] · Change
- 2026-02-27 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-27-3-apps-and-integrations-changes-in-v0-0-419|3 Apps and Integrations changes in v0.0.419]] · Digest
- 2026-02-25 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-02-25-sources-from-apps-paste-a-link-to-a-slack-channel-or-google-drive-file-or-folder|Sources from apps]] · Change
- 2026-02-25 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-25-expand-remote-control-to-more-users|Expand Remote Control to more users]] · Change
- 2026-02-25 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-25-13-apps-and-integrations-changes-in-rust-v0-105-0|13 Apps and Integrations changes in rust-v0.105.0]] · Digest
- 2026-02-25 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-25-8-apps-and-integrations-changes-in-v0-30-0|8 Apps and Integrations changes in v0.30.0]] · Digest
- 2026-02-25 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-25-plugin-agents-specified-as-file-paths-in-plugin-json-load-correctly|Plugin agents specified as file paths in plugin.json load correctly]] · Change
- 2026-02-25 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-25-3-apps-and-integrations-changes-in-v0-0-417|3 Apps and Integrations changes in v0.0.417]] · Digest
- 2026-02-24 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-24-4-apps-and-integrations-changes-in-v2-1-51|4 Apps and Integrations changes in v2.1.51]] · Digest
- 2026-02-24 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-02-24-add-mcp-enterprise-configuration-details|Add MCP enterprise configuration details]] · Change
- 2026-02-24 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-02-24-added-cline-sdk-api-interface-for-programmatic-access-to-cline-features-and-tool|Added Cline SDK API interface for programmatic access to Cline features and tools…]] · Change
- 2026-02-24 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-24-block-third-party-mcp-servers-when-the-copilot-mcp-policy-does-not-allow-them|Block third-party MCP servers when the Copilot MCP policy does not allow them]] · Change
- 2026-02-24 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-02-24-3-apps-and-integrations-changes-in-v1-2-11|3 Apps and Integrations changes in v1.2.11]] · Digest
- 2026-02-23 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-23-5-apps-and-integrations-changes-in-v0-0-415|5 Apps and Integrations changes in v0.0.415]] · Digest
- 2026-02-23 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-02-23-mcp-ssl-verification-fix-mcp-tool-connections-now-properly-respect-the-aiohttp-c|🔓 MCP SSL verification fix. MCP tool connections now properly respect…]] · Change
- 2026-02-21 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-21-explore-agent-can-now-use-github-mcp-tools-when-available|Explore agent can now use GitHub MCP tools when available]] · Change
- 2026-02-20 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-20-claude-code-simple-mode-now-also-disables-mcp-tools-attachments-hooks-and-claude|CLAUDE_CODE_SIMPLE mode now also disables MCP tools, attachments, hooks…]] · Change
- 2026-02-20 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-20-support-remote-plugin-sources-github-repos-and-git-urls-in-marketplace-json-plug|Support remote plugin sources (GitHub repos and git URLs) in marketplace.json plugin…]] · Change
- 2026-02-20 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-02-20-sdk-build-sdk-to-dist-instead-of-dist-src|SDK Build SDK to dist/ instead of dist/src]] · Change
- 2026-02-19 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-02-19-preview-diagrams-and-mini-apps-directly-in-chat|Preview diagrams and mini apps directly in chat]] · Change
- 2026-02-19 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-19-2-apps-and-integrations-changes-in-v2-1-49|2 Apps and Integrations changes in v2.1.49]] · Digest
- 2026-02-19 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-19-3-apps-and-integrations-changes-in-v0-0-412|3 Apps and Integrations changes in v0.0.412]] · Digest
- 2026-02-19 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-02-19-added-a-setting-to-enable-or-disable-terminal-integration|Added a setting to enable or disable terminal integration]] · Change
- 2026-02-19 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2026-02-19-ollama-launch-integration-will-now-always-show-the-model-picker|ollama launch integration will now always show the model picker]] · Change
- 2026-02-19 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-02-19-5-apps-and-integrations-changes-in-v1-2-7|5 Apps and Integrations changes in v1.2.7]] · Digest
- 2026-02-19 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-02-19-terminal-add-custom-tool-and-mcp-call-responses-that-are-visible-and-collapsible|Terminal Add custom tool and MCP call responses that are visible and collapsible]] · Change
- 2026-02-18 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-18-added-last-assistant-message-field-to-stop-and-subagentstop-hook-inputs-providin|Added last_assistant_message field to Stop and SubagentStop hook inputs, providing…]] · Change
- 2026-02-18 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-02-18-3-apps-and-integrations-changes-in-cli-improvements-and-mermaid-ascii|3 Apps and Integrations changes in CLI Improvements and Mermaid ASCII…]] · Digest
- 2026-02-18 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-18-5-apps-and-integrations-changes-in-v0-29-0|5 Apps and Integrations changes in v0.29.0]] · Digest
- 2026-02-17 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-17-2-apps-and-integrations-changes-in-v2-1-45|2 Apps and Integrations changes in v2.1.45]] · Digest
- 2026-02-17 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-17-15-apps-and-integrations-changes-in-rust-v0-102-0|15 Apps and Integrations changes in rust-v0.102.0]] · Digest
- 2026-02-17 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-17-11706-apps-expose-more-fields-from-apps-listing-endpoints-mzeng-openai|♯11706 apps Expose more fields from apps listing endpoints]] · Change
- 2026-02-17 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-17-2-apps-and-integrations-changes-in-v0-0-411|2 Apps and Integrations changes in v0.0.411]] · Digest
- 2026-02-16 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-02-16-core-bump-gitlab-provider-and-auth-plugin-for-mid-session-token-refresh|Core Bump GitLab provider and auth plugin for mid-session token refresh]] · Change
- 2026-02-14 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-14-3-apps-and-integrations-changes-in-v0-0-410|3 Apps and Integrations changes in v0.0.410]] · Digest
- 2026-02-14 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-02-14-2-apps-and-integrations-changes-in-v0-8-1|2 Apps and Integrations changes in v0.8.1]] · Digest
- 2026-02-13 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-02-13-core-add-tool-definition-hook-for-plugins-to-modify-tool-description-and-paramet|Core Add tool.definition hook for plugins to modify tool description and parameters]] · Change
- 2026-02-12 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-02-12-2-apps-and-integrations-changes-in-v3-58-0|2 Apps and Integrations changes in v3.58.0]] · Digest
- 2026-02-12 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-12-5-apps-and-integrations-changes-in-rust-v0-100-0|5 Apps and Integrations changes in rust-v0.100.0]] · Digest
- 2026-02-12 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-12-mcp-servers-respect-the-cwd-working-directory-property|MCP servers respect the cwd working directory property]] · Change
- 2026-02-12 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-12-2-apps-and-integrations-changes-in-v0-0-409|2 Apps and Integrations changes in v0.0.409]] · Digest
- 2026-02-12 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-02-12-6-apps-and-integrations-changes-in-v0-8-0|6 Apps and Integrations changes in v0.8.0]] · Digest
- 2026-02-12 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-02-12-core-use-promise-all-for-mcp-listtools-calls-to-improve-performance|Core Use Promise.all for MCP listTools calls to improve performance]] · Change
- 2026-02-12 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-02-12-core-expose-tool-arguments-in-shell-hook-for-plugin-visibility|Core Expose tool arguments in shell hook for plugin visibility]] · Change
- 2026-02-11 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-11-13-apps-and-integrations-changes-in-rust-v0-99-0|13 Apps and Integrations changes in rust-v0.99.0]] · Digest
- 2026-02-11 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-02-11-10-apps-and-integrations-changes-in-1-13-0|10 Apps and Integrations changes in 1.13.0]] · Digest
- 2026-02-11 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-11-3-apps-and-integrations-changes-in-v0-0-407|3 Apps and Integrations changes in v0.0.407]] · Digest
- 2026-02-11 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-02-11-sdk-encode-non-ascii-directory-paths-in-v1-sdk-http-headers|SDK Encode non-ASCII directory paths in v1 SDK HTTP headers]] · Change
- 2026-02-10 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-10-7-apps-and-integrations-changes-in-v0-28-0|7 Apps and Integrations changes in v0.28.0]] · Digest
- 2026-02-10 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-02-10-core-add-directory-parameter-to-plugin-client-for-multi-project-support|Core Add directory parameter to plugin client for multi-project support]] · Change
- 2026-02-07 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-07-4-apps-and-integrations-changes-in-v0-0-406|4 Apps and Integrations changes in v0.0.406]] · Digest
- 2026-02-06 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-06-added-plugin-name-to-skill-descriptions-and-skills-menu-for-better-discoverabili|Added plugin name to skill descriptions and /skills menu for better discoverability]] · Change
- 2026-02-05 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-02-05-skills-defined-in-claude-skills-within-additional-directories-add-dir-are-now-lo|Skills defined in .claude/skills/ within additional directories (--add-dir)…]] · Change
- 2026-02-05 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-05-6-apps-and-integrations-changes-in-rust-v0-97-0|6 Apps and Integrations changes in rust-v0.97.0]] · Digest
- 2026-02-05 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-05-plugin-and-marketplace-names-support-uppercase-letters|Plugin and marketplace names support uppercase letters]] · Change
- 2026-02-05 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-05-2-apps-and-integrations-changes-in-v0-0-404|2 Apps and Integrations changes in v0.0.404]] · Digest
- 2026-02-05 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-05-2-apps-and-integrations-changes-in-v0-0-403|2 Apps and Integrations changes in v0.0.403]] · Digest
- 2026-02-05 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-02-05-6-apps-and-integrations-changes-in-v1-1-52|6 Apps and Integrations changes in v1.1.52]] · Digest
- 2026-02-05 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-02-05-2-apps-and-integrations-changes-in-v1-1-53|2 Apps and Integrations changes in v1.1.53]] · Digest
- 2026-02-04 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-04-5-apps-and-integrations-changes-in-rust-v0-95-0|5 Apps and Integrations changes in rust-v0.95.0]] · Digest
- 2026-02-04 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-04-14-apps-and-integrations-changes-in-v0-27-0|14 Apps and Integrations changes in v0.27.0]] · Digest
- 2026-02-04 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-02-04-2-apps-and-integrations-changes-in-v1-1-50|2 Apps and Integrations changes in v1.1.50]] · Digest
- 2026-02-03 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-02-03-14-apps-and-integrations-changes-in-1-12-0|14 Apps and Integrations changes in 1.12.0]] · Digest
- 2026-02-03 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-03-3-apps-and-integrations-changes-in-v0-0-401|3 Apps and Integrations changes in v0.0.401]] · Digest
- 2026-02-03 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-03-4-apps-and-integrations-changes-in-v0-0-402|4 Apps and Integrations changes in v0.0.402]] · Digest
- 2026-02-03 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-02-03-2-apps-and-integrations-changes-in-v1-1-49|2 Apps and Integrations changes in v1.1.49]] · Digest

**2026-01**

- 2026-01-31 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-31-14-apps-and-integrations-changes-in-rust-v0-93-0|14 Apps and Integrations changes in rust-v0.93.0]] · Digest
- 2026-01-31 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-31-core-bump-ai-sdk-packages|Core Bump AI SDK packages]] · Change
- 2026-01-30 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-01-30-vscode-enabled-claude-in-chrome-integration|VSCode: Enabled Claude in Chrome integration]] · Change
- 2026-01-30 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-01-30-hooks-hook-scripts-now-run-from-the-workspace-repository-root-instead-of-filesys|Hooks: Hook scripts now run from the workspace repository root instead…]] · Change
- 2026-01-30 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-01-30-hooks-hook-scripts-now-run-from-the-workspace-repository-root-instead-of-filesys-9eb2c6|Hooks: Hook scripts now run from the workspace repository root instead…]] · Change
- 2026-01-30 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-01-30-hooks-hook-scripts-now-run-from-the-workspace-repository-root-instead-of-filesys-f43db5|Hooks: Hook scripts now run from the workspace repository root instead…]] · Change
- 2026-01-30 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-30-3-apps-and-integrations-changes-in-v0-0-400|3 Apps and Integrations changes in v0.0.400]] · Digest
- 2026-01-30 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-30-2-apps-and-integrations-changes-in-v1-1-47-2|2 Apps and Integrations changes in v1.1.47 + 2]] · Digest
- 2026-01-29 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-29-core-include-provider-id-in-sdk-cache-key-to-prevent-cache-collisions|Core Include provider ID in SDK cache key to prevent cache collisions]] · Change
- 2026-01-28 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-01-28-add-mcp-prompts-support-prompts-from-connected-mcp-servers-now-appear-in-slash-c|Add MCP prompts support - prompts from connected MCP servers now appear in slash…]] · Change
- 2026-01-28 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-28-4-apps-and-integrations-changes-in-v0-26-0|4 Apps and Integrations changes in v0.26.0]] · Digest
- 2026-01-28 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-28-mcp-show-server-name-displays-server-details-and-available-tools|/mcp show server-name displays server details and available tools]] · Change
- 2026-01-28 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-28-2-apps-and-integrations-changes-in-v1-1-40-1|2 Apps and Integrations changes in v1.1.40 + 1]] · Digest
- 2026-01-28 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-28-core-bump-plugin-version|Core Bump plugin version]] · Change
- 2026-01-28 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-28-core-add-worktree-to-plugin-tool-context|Core Add worktree to plugin tool context]] · Change
- 2026-01-27 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-01-27-changed-the-commit-push-pr-skill-to-automatically-post-pr-urls-to-slack-channels|Changed the /commit-push-pr skill to automatically post PR URLs to Slack channels…]] · Change
- 2026-01-27 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-27-refreshed-protocol-mcp-docs-to-reflect-thread-unarchive-and-the-updated-request|Refreshed protocol/MCP docs to reflect thread/unarchive and the updated…]] · Change
- 2026-01-27 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-27-2-apps-and-integrations-changes-in-v0-0-396|2 Apps and Integrations changes in v0.0.396]] · Digest
- 2026-01-26 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-26-3-apps-and-integrations-changes-in-v0-0-395|3 Apps and Integrations changes in v0.0.395]] · Digest
- 2026-01-25 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-25-3-apps-and-integrations-changes-in-rust-v0-90-0|3 Apps and Integrations changes in rust-v0.90.0]] · Digest
- 2026-01-25 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-25-2-apps-and-integrations-changes-in-v1-1-35|2 Apps and Integrations changes in v1.1.35]] · Digest
- 2026-01-24 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-24-plugin-skills-work-in-agent-responses|Plugin skills work in agent responses]] · Change
- 2026-01-23 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-01-23-2-apps-and-integrations-changes-in-v2-1-19|2 Apps and Integrations changes in v2.1.19]] · Digest
- 2026-01-23 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-23-2-apps-and-integrations-changes-in-v0-0-393|2 Apps and Integrations changes in v0.0.393]] · Digest
- 2026-01-22 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-01-22-vscode-added-native-plugin-management-support|VSCode Added native plugin management support]] · Change
- 2026-01-22 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-22-2-apps-and-integrations-changes-in-rust-v0-89-0|2 Apps and Integrations changes in rust-v0.89.0]] · Digest
- 2026-01-22 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-01-22-4-apps-and-integrations-changes-in-2-4|4 Apps and Integrations changes in 2.4]] · Digest
- 2026-01-22 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-22-2-apps-and-integrations-changes-in-v0-0-392|2 Apps and Integrations changes in v0.0.392]] · Digest
- 2026-01-22 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-22-custom-agents-with-mcp-servers-avoid-unnecessary-restarts|Custom agents with MCP servers avoid unnecessary restarts]] · Change
- 2026-01-22 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-22-2-apps-and-integrations-changes-in-v0-0-389|2 Apps and Integrations changes in v0.0.389]] · Digest
- 2026-01-22 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-22-core-add-chat-headers-hook-and-update-codex-and-copilot-plugins-to-use-it-thanks|Core Add chat.headers hook and update codex and copilot plugins to use…]] · Change
- 2026-01-22 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-22-core-print-mcp-stderr-to-opencode-log-file|Core Print MCP stderr to OpenCode log file]] · Change
- 2026-01-21 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-21-3-apps-and-integrations-changes-in-rust-v0-88-0|3 Apps and Integrations changes in rust-v0.88.0]] · Digest
- 2026-01-21 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-21-10-apps-and-integrations-changes-in-v0-25-0|10 Apps and Integrations changes in v0.25.0]] · Digest
- 2026-01-21 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2026-01-21-improved-integration-card-design-with-less-prominent-skip-button|Improved integration card design with less prominent skip button]] · Change
- 2026-01-20 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-01-20-2-apps-and-integrations-changes-in-v2-1-14|2 Apps and Integrations changes in v2.1.14]] · Digest
- 2026-01-20 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-20-enable-all-github-mcp-tools-flag-now-enables-read-write-github-mcp-tools|--enable-all-github-mcp-tools flag now enables read-write GitHub MCP tools]] · Change
- 2026-01-20 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-20-core-ensure-truncation-handling-applies-to-mcp-servers|Core Ensure truncation handling applies to MCP servers]] · Change
- 2026-01-19 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-19-extensions-add-use-github-token-to-example|Extensions Add use_github_token to example]] · Change
- 2026-01-16 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-16-accepting-an-mcp-elicitation-now-sends-an-empty-json-payload-instead-of-null-to|Accepting an MCP elicitation now sends an empty JSON payload instead of null…]] · Change
- 2026-01-16 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-16-3-apps-and-integrations-changes-in-rust-v0-87-0|3 Apps and Integrations changes in rust-v0.87.0]] · Digest
- 2026-01-16 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-16-mcp-servers-now-start-correctly-for-custom-agents|MCP servers now start correctly for custom agents]] · Change
- 2026-01-16 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-16-core-reinstall-plugins-when-cache-module-is-missing|Core Reinstall plugins when cache module is missing]] · Change
- 2026-01-16 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-16-3-apps-and-integrations-changes-in-v1-1-24|3 Apps and Integrations changes in v1.1.24]] · Digest
- 2026-01-15 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-15-9207-propagate-mcp-disabled-reason-gt-oai|♯9207 Propagate MCP disabled reason @gt-oai]] · Change
- 2026-01-15 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-01-15-4-apps-and-integrations-changes-in-1-11-4|4 Apps and Integrations changes in 1.11.4]] · Digest
- 2026-01-15 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-15-core-official-copilot-plugin|Core Official Copilot plugin]] · Change
- 2026-01-15 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-15-core-honor-per-server-mcp-timeouts|Core Honor per-server MCP timeouts]] · Change
- 2026-01-14 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-14-10-apps-and-integrations-changes-in-rust-v0-81-0|10 Apps and Integrations changes in rust-v0.81.0]] · Digest
- 2026-01-14 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-14-9-apps-and-integrations-changes-in-v0-24-0|9 Apps and Integrations changes in v0.24.0]] · Digest
- 2026-01-14 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-14-3-apps-and-integrations-changes-in-v1-1-19|3 Apps and Integrations changes in v1.1.19]] · Digest
- 2026-01-14 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-14-sdk-add-missing-metadata-and-ask-definitions-to-toolcontext-type|SDK Add missing metadata() and ask() definitions to ToolContext type]] · Change
- 2026-01-13 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-01-13-2-apps-and-integrations-changes-in-v2-1-6|2 Apps and Integrations changes in v2.1.6]] · Digest
- 2026-01-13 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2026-01-13-13-apps-and-integrations-changes-in-1-11-3|13 Apps and Integrations changes in 1.11.3]] · Digest
- 2026-01-13 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-13-terminal-actually-modify-opencode-config-when-adding-mcp-servers-with-mcp-add-co|Terminal Actually modify OpenCode config when adding MCP servers with mcp add command]] · Change
- 2026-01-12 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-12-core-bump-copilot-plugin-version|Core Bump Copilot plugin version]] · Change
- 2026-01-12 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-12-core-improve-error-handling-for-built-in-plugin-installation-failures|Core Improve error handling for built-in plugin installation failures]] · Change
- 2026-01-10 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-01-10-2-apps-and-integrations-changes-in-v3-49-0|2 Apps and Integrations changes in v3.49.0]] · Digest
- 2026-01-09 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2026-01-09-2-apps-and-integrations-changes-in-v2-1-2|2 Apps and Integrations changes in v2.1.2]] · Digest
- 2026-01-09 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-09-2-apps-and-integrations-changes-in-rust-v0-80-0|2 Apps and Integrations changes in rust-v0.80.0]] · Digest
- 2026-01-09 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2026-01-09-3-apps-and-integrations-changes-in-v0-7-0|3 Apps and Integrations changes in v0.7.0]] · Digest
- 2026-01-09 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-09-2-apps-and-integrations-changes-in-v1-1-10|2 Apps and Integrations changes in v1.1.10]] · Digest
- 2026-01-08 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2026-01-08-mcp-server-names-with-spaces-are-now-supported-in-all-mcp-commands|MCP server names with spaces are now supported in all /mcp commands]] · Change
- 2026-01-08 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2026-01-08-improved-the-error-message-when-an-enterprise-user-adds-an-integration-they-don|Improved the error message when an Enterprise user adds an integration they don't…]] · Change
- 2026-01-07 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-07-5-apps-and-integrations-changes-in-v0-23-0|5 Apps and Integrations changes in v0.23.0]] · Digest
- 2026-01-07 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-07-shutdown-mcp-servers-after-subagent-execution-completes|Shutdown MCP servers after subagent execution completes]] · Change
- 2026-01-06 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2026-01-06-exclude-binary-files-without-extensions-from-diffs|Exclude binary files without extensions from diffs]] · Change
- 2026-01-06 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-06-8694-mcp-sanitize-mcp-tool-names-to-ensure-they-are-compatible-with-the-response|♯8694 MCP Sanitize MCP tool names to ensure they are compatible with the Responses…]] · Change
- 2026-01-06 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-06-desktop-add-single-instance-plugin-to-prevent-multiple-desktop-windows|Desktop Add single-instance plugin to prevent multiple desktop windows]] · Change
- 2026-01-05 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-05-terminal-add-description-for-mcp-command-in-documentation|Terminal Add description for MCP command in documentation]] · Change
- 2026-01-04 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2026-01-04-18-apps-and-integrations-changes-in-v1-1-1|18 Apps and Integrations changes in v1.1.1]] · Digest
- 2026-01-02 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-02-mcp-server-type-help-text-displays-correct-options|MCP server type help text displays correct options]] · Change

</details>

</details>

<details class="disclosure">
<summary>2025 · 363 entries (Aider 1 · ChatGPT 10 · Claude Code 1 · Cline 42 · Codex CLI 32 · Cursor 16 · Dify 30 · ElevenLabs 53 · Gamma 3 · Gemini 3 · Gemini CLI 32 · GitHub Copilot CLI 9 · Google Antigravity 1 · Granola 1 · Lovable 18 · Manus 1 · Ollama 3 · Open WebUI 28 · OpenCode 5 · OpenHands 16 · Replit 39 · Runway 2 · Windsurf 11 · v0 6)</summary>

**2025-12**

- 2025-12-31 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2025-12-31-default-to-ai-sdk-openai-compatible-when-no-npm-package-is-provided|Default to ai-sdk/openai-compatible when no npm package is provided]] · Launch
- 2025-12-26 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-12-26-replit-rewind-2025|Replit Rewind 2025]] · Launch
- 2025-12-26 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-12-26-replit-chatgpt-app|Replit ChatGPT App]] · Launch
- 2025-12-23 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-12-23-lovable-chatgpt-app|Lovable ChatGPT app]] · Launch
- 2025-12-23 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-12-23-connectors-elevenlabs-perplexity-and-firecrawl|Connectors: ElevenLabs, Perplexity, and Firecrawl]] · Launch
- 2025-12-19 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-12-19-custom-mcp-server-icons|Custom MCP Server Icons]] · Launch
- 2025-12-18 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-12-18-you-can-now-browse-and-add-approved-apps-in-the-new-app-directory-apps-let-you-w|Introducing the app directory in ChatGPT]] · Launch
- 2025-12-16 · <span class="tl-product tl-p11">**Gemini**</span> · [[Changes/Gemini/2025-12-16-introducing-a-new-kind-of-gem|Introducing a new kind of Gem]] · Launch
- 2025-12-16 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2025-12-16-you-can-now-connect-v0-to-your-linear-workspace-and-build-straight-from-your-bac|Connect v0 to your Linear workspace and build straight from your backlog]] · Change
- 2025-12-15 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-12-15-sdk-releases|SDK Releases]] · Launch
- 2025-12-15 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-12-15-whatsapp-integration|WhatsApp Integration]] · Launch
- 2025-12-15 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-12-15-whatsapp-integration-fdcc9d|WhatsApp Integration]] · Launch
- 2025-12-12 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-12-12-agent-now-supports-custom-mcp-servers|Agent now supports custom MCP servers]] · Launch
- 2025-12-12 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-12-12-plaid-connector-for-enterprise|Plaid Connector for Enterprise]] · Launch
- 2025-12-10 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-12-10-miro-mcp-available-as-a-chat-connector|Miro MCP available as a chat connector]] · Launch
- 2025-12-10 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-12-10-support-for-unauthenticated-mcp-servers|Support for unauthenticated MCP servers]] · Launch
- 2025-12-10 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-12-10-manage-tool-permissions-for-chat-connectors|Manage tool permissions for chat connectors]] · Launch
- 2025-12-10 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-12-10-connectors-hub-formerly-integrations|Connectors hub (formerly Integrations)]] · Launch
- 2025-12-10 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2025-12-10-mcp-servers|MCP Servers]] · Launch
- 2025-12-10 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2025-12-10-cascade-hooks-on-user-prompts|Cascade Hooks on User Prompts]] · Launch
- 2025-12-08 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-12-08-sdk-releases|SDK Releases]] · Launch
- 2025-12-08 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-12-08-javascript-sdk|JavaScript SDK]] · Launch
- 2025-12-08 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-12-08-python-sdk|Python SDK]] · Launch
- 2025-12-03 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2025-12-03-you-can-now-bring-your-own-mcps-to-v0|Bring your own MCPs]] · Change

**2025-11**

- 2025-11-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-27-workspaces-88d227|Workspaces]] · Launch
- 2025-11-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-27-javascript-sdk|JavaScript SDK]] · Launch
- 2025-11-26 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-11-26-shopify-integration-improvements|Shopify integration improvements]] · Launch
- 2025-11-26 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-11-26-mcp-servers|MCP servers]] · Launch
- 2025-11-26 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-11-26-integrations-hub|Integrations hub]] · Launch
- 2025-11-21 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-21-packages|Packages]] · Launch
- 2025-11-21 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-21-sdk-releases|SDK Releases]] · Launch
- 2025-11-21 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-11-21-enterprise-data-warehouse-connectors|Enterprise data warehouse connectors]] · Expansion
- 2025-11-21 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-11-21-enhanced-atlassian-connectors|Enhanced Atlassian connectors]] · Launch
- 2025-11-21 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-11-21-new-connector-todoist|New connector: Todoist]] · Launch
- 2025-11-21 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2025-11-21-mcp-servers|MCP Servers]] · Launch
- 2025-11-18 · <span class="tl-product tl-p17">**Manus**</span> · [[Changes/Manus/2025-11-18-manus-can-now-perform-tasks-directly-in-your-browser-autonomously-it-securely-wo|Introducing Manus Browser Operator]] · Launch
- 2025-11-16 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-11-16-azure-marketplace-integration|Azure Marketplace integration]] · Launch
- 2025-11-13 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2025-11-13-cascade-hooks|Cascade Hooks]] · Launch
- 2025-11-13 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2025-11-13-mcp-improvements|MCP Improvements]] · Launch
- 2025-11-12 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-12-api-integration-triggers|API Integration Triggers]] · Launch
- 2025-11-12 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-12-sdk-releases|SDK Releases]] · Launch
- 2025-11-07 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-11-07-connectors-support-for-remixing|Connectors support for remixing]] · Launch
- 2025-11-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-05-twilio-integration|Twilio Integration]] · Launch
- 2025-11-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-05-python-sdk|Python SDK]] · Launch
- 2025-11-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-05-mcp-servers|MCP Servers]] · Launch
- 2025-11-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-05-sdk-releases|SDK Releases]] · Launch
- 2025-11-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-05-javascript-sdk|JavaScript SDK]] · Launch
- 2025-11-05 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-05-mcp-tool-configuration|MCP Tool Configuration]] · Launch
- 2025-11-05 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-11-05-lovable-shopify-integration|Lovable × Shopify Integration]] · Launch
- 2025-11-04 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-04-5956-parse-the-azure-openai-rate-limit-message-5956|♯5956 Parse the Azure OpenAI rate limit message (♯5956)]] · Policy
- 2025-11-04 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2025-11-04-mcp-enhancements|MCP Enhancements]] · Launch

**2025-10**

- 2025-10-31 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-10-31-salesforce-and-clickup-connectors|Salesforce and ClickUp connectors]] · Launch
- 2025-10-31 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-10-31-slash-command-connector-discovery|Slash command connector discovery]] · Launch
- 2025-10-31 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-10-31-zendesk-connector|Zendesk connector]] · Launch
- 2025-10-31 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-10-31-agentmail-connector|Agentmail connector]] · Launch
- 2025-10-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-27-mcp-servers|MCP Servers]] · Launch
- 2025-10-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-27-sdk-releases|SDK Releases]] · Launch
- 2025-10-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-27-python-sdk|Python SDK]] · Launch
- 2025-10-27 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-27-javascript-sdk|JavaScript SDK]] · Launch
- 2025-10-20 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-20-sdk-releases|SDK Releases]] · Launch
- 2025-10-17 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-10-17-build-mode-redesign-for-react-apps|Build mode redesign for React apps]] · Launch
- 2025-10-17 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-10-17-clickup-integration|ClickUp integration]] · Launch
- 2025-10-15 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2025-10-15-experimental-support-for-vulkan-is-now-available-when-you-build-locally-from-sou|Experimental support for Vulkan is now available when you build locally from source]] · Launch
- 2025-10-14 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-14-sdk-releases|SDK Releases]] · Launch
- 2025-10-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-07-javascript-sdk|JavaScript SDK]] · Launch
- 2025-10-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-07-python-sdk|Python SDK]] · Launch
- 2025-10-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-07-sdk-releases|SDK Releases]] · Launch
- 2025-10-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-07-mcp-server|MCP Server]] · Launch
- 2025-10-06 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-10-06-turn-your-files-into-apps|Turn your files into apps]] · Launch
- 2025-10-06 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-10-06-stripe-integration|Stripe integration]] · Launch
- 2025-10-03 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-10-03-connectors-platform-launch|Connectors platform launch]] · Launch
- 2025-10-03 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-10-03-git-source-control-enhancements|Git source control enhancements]] · Launch
- 2025-10-03 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-10-03-connectors-admin-management|Connectors admin management]] · Launch
- 2025-10-03 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-10-03-vercel-import-integration|Vercel import integration]] · Launch

**2025-09**

- 2025-09-29 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-29-javascript-sdk|JavaScript SDK]] · Launch
- 2025-09-29 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-29-packages|Packages]] · Launch
- 2025-09-29 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-29-sdk-releases|SDK Releases]] · Launch
- 2025-09-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-22-deprecated-endpoints|Deprecated Endpoints]] · Policy
- 2025-09-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-22-javascript-sdk|JavaScript SDK]] · Launch
- 2025-09-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-22-python-sdk|Python SDK]] · Launch
- 2025-09-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-22-new-endpoints|New Endpoints]] · Policy
- 2025-09-22 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-22-sdk-releases|SDK Releases]] · Launch
- 2025-09-19 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-09-19-mobile-connectors-support|Mobile connectors support]] · Launch
- 2025-09-15 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-15-packages|Packages]] · Launch
- 2025-09-15 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-15-mcp-server|MCP Server]] · Launch
- 2025-09-15 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-15-sdk-releases|SDK Releases]] · Launch
- 2025-09-12 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-09-12-mcp-resources-support|MCP Resources support]] · Launch
- 2025-09-12 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-09-12-app-connectors-and-integrations|App connectors and integrations]] · Launch
- 2025-09-08 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-08-mcp-server|MCP Server]] · Launch
- 2025-09-08 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-08-sdk-releases|SDK Releases]] · Launch
- 2025-09-05 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-09-05-gcp-marketplace-integration|GCP Marketplace integration]] · Launch
- 2025-09-01 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-01-sdk-releases|SDK Releases]] · Launch
- 2025-09-01 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-09-01-mcp-server|MCP Server]] · Launch
- 2025-09-01 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-09-01-smarter-seo-for-new-apps|Smarter SEO for new apps]] · Launch

**2025-08**

- 2025-08-29 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-08-29-shareable-app-creation-links|Shareable app creation links]] · Launch
- 2025-08-21 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-08-21-cursor-now-supports-mcp-elicitation-a-new-feature-in-the-mcp-spec-that-allows-se|Support for MCP elicitation]] · Launch
- 2025-08-13 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-08-13-gmail-google-calendar-and-google-contacts-connectors-in-chatgpt-are-now-availabl-e34de4|Gmail, Google Calendar, and Google Contacts Connectors in ChatGPT (Plus)]] · Expansion
- 2025-08-11 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-08-11-sdks|SDKs]] · Launch
- 2025-08-11 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-08-11-real-time-analytics-on-your-lovable-apps|Real-time analytics on your Lovable apps]] · Launch
- 2025-08-04 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-08-04-sdk-releases|SDK Releases]] · Launch

**2025-07**

- 2025-07-28 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-28-sdks|SDKs]] · Launch
- 2025-07-25 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-07-25-domains-improvements|Domains improvements]] · Launch
- 2025-07-17 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2025-07-17-deeper-browser-integration|Deeper Browser integration]] · Launch
- 2025-07-14 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-14-sdks|SDKs]] · Launch
- 2025-07-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-07-07-conversation-enhancements|Conversation Enhancements]] · Launch

**2025-06**

- 2025-06-30 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-30-sdks|SDKs]] · Launch
- 2025-06-27 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-06-27-new-landing-page-for-viewer-seats|New landing page for viewer seats]] · Launch
- 2025-06-17 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-17-workspaces|Workspaces]] · Launch
- 2025-06-17 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-17-agents-platform-mcp-servers|Agents Platform - MCP Servers]] · Launch
- 2025-06-12 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-06-12-agents-understand-context-6b73fc|Agents understand context]] · Launch
- 2025-06-08 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-08-sdks|SDKs]] · Launch

**2025-05**

- 2025-05-30 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-05-30-stripe-checkout-release|Stripe Checkout release]] · Launch
- 2025-05-15 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-05-15-the-github-connector-is-now-available-globally-to-plus-pro-team-users-including|GitHub connector for deep research]] · Expansion
- 2025-05-15 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-05-15-refreshed-inline-edit-cmd-ctrl-k-with-agent-integration|Refreshed Inline Edit (Cmd/Ctrl+K) with Agent integration]] · Launch
- 2025-05-09 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-05-09-paypal-checkout-integration|PayPal checkout integration]] · Launch
- 2025-05-09 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-05-09-notion-integration|Notion integration]] · Launch
- 2025-05-07 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2025-05-07-cascade-plugins|Cascade Plugins]] · Launch

**2025-04**

- 2025-04-18 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-04-18-smarter-integrations-matching|Smarter integrations matching]] · Launch
- 2025-04-15 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-04-15-images-in-mcp|Images in MCP]] · Launch
- 2025-04-11 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-04-11-app-idea-generator-for-logged-out-visitors|App idea generator for logged-out visitors]] · Launch
- 2025-04-07 · <span class="tl-product tl-p9">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-04-07-text-to-speech|Text to speech]] · Launch
- 2025-04-02 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2025-04-02-misc|Misc]] · Launch

**2025-03**

- 2025-03-13 · <span class="tl-product tl-p11">**Gemini**</span> · [[Changes/Gemini/2025-03-13-gemini-with-2-0-flash-thinking-experimental-is-now-even-better-at-completing-com|Gemini with 2.0 Flash Thinking (experimental) is now even better at completing…]] · Launch

**2025-02**

- 2025-02-21 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-02-21-one-click-deploy-for-assistant|One-click deploy for Assistant]] · Launch
- 2025-02-21 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-02-21-replit-grok|Replit 🤝 Grok]] · Launch
- 2025-02-19 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-02-19-introducing-mcp-marketplace-you-can-now-discover-and-install-the-best-mcp-server|Introducing MCP Marketplace!]] · Launch
- 2025-02-12 · <span class="tl-product tl-p11">**Gemini**</span> · [[Changes/Gemini/2025-02-12-priority-access-with-gemini-advanced-ask-gemini-to-look-back-at-past-chats-for-m|Priority access with Gemini Advanced]] · Launch

**2025-01**

- 2025-01-31 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-01-31-repl-app|Repl - App]] · Launch
- 2025-01-24 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-01-24-assistant-workflows|Assistant + Workflows]] · Launch
- 2025-01-17 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-01-17-sendgrid-integration|SendGrid integration]] · Launch
- 2025-01-10 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-01-10-slack-integration|Slack integration]] · Launch
- 2025-01-03 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-01-03-xai-integration|xAI integration]] · Launch
- 2025-01-03 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2025-01-03-react-by-default|React by default]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 230 (Aider 1 · ChatGPT 7 · Claude Code 1 · Cline 41 · Codex CLI 31 · Cursor 11 · Dify 30 · Gamma 3 · Gemini CLI 32 · GitHub Copilot CLI 9 · Google Antigravity 1 · Granola 1 · Lovable 4 · Ollama 2 · Open WebUI 28 · OpenCode 4 · OpenHands 16 · Runway 2 · Windsurf 2 · v0 4)</summary>

**2025-12**

- 2025-12-31 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2025-12-31-3-apps-and-integrations-changes-in-v1-0-219|3 Apps and Integrations changes in v1.0.219]] · Digest
- 2025-12-31 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2025-12-31-core-display-mcp-tag-for-prompts-in-autocomplete-but-not-in-prompt|Core Display MCP tag for prompts in autocomplete but not in prompt]] · Change
- 2025-12-30 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-12-30-enable-copilot-spaces-tools-in-github-mcp-server|Enable Copilot Spaces tools in GitHub MCP Server]] · Change
- 2025-12-30 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2025-12-30-core-expose-server-url-to-plugins|Core Expose server URL to plugins]] · Change
- 2025-12-30 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2025-12-30-added-forgejo-integration-by-johba37-in-https-github-com-openhands-openhands-pul|Added Forgejo integration]] · Change
- 2025-12-29 · <span class="tl-product tl-p21">**OpenCode**</span> · [[Changes/OpenCode/2025-12-29-core-install-local-plugin-dependencies-from-package-json|Core Install local plugin dependencies from package.json]] · Change
- 2025-12-25 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-12-25-12-apps-and-integrations-changes-in-1-11-2|12 Apps and Integrations changes in 1.11.2]] · Digest
- 2025-12-22 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-12-22-2-apps-and-integrations-changes-in-2-3|2 Apps and Integrations changes in 2.3]] · Digest
- 2025-12-22 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-22-3-apps-and-integrations-changes-in-v0-22-0|3 Apps and Integrations changes in v0.22.0]] · Digest
- 2025-12-21 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-12-21-2-apps-and-integrations-changes-in-v0-6-42|2 Apps and Integrations changes in v0.6.42]] · Digest
- 2025-12-19 · <span class="tl-product tl-p4">**Claude Code**</span> · [[Changes/Claude Code/2025-12-19-2-apps-and-integrations-changes-in-v2-0-73|2 Apps and Integrations changes in v2.0.73]] · Digest
- 2025-12-18 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-18-2-apps-and-integrations-changes-in-rust-v0-74-0|2 Apps and Integrations changes in rust-v0.74.0]] · Digest
- 2025-12-18 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-12-18-2-apps-and-integrations-changes-in-v0-0-370|2 Apps and Integrations changes in v0.0.370]] · Digest
- 2025-12-16 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-16-9-apps-and-integrations-changes-in-v0-21-0|9 Apps and Integrations changes in v0.21.0]] · Digest
- 2025-12-16 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2025-12-16-added-azure-devops-integration-support-by-zerofltexx-in-https-github-com-openhan|Added Azure DevOps integration support]] · Change
- 2025-12-15 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-15-7962-docs-update-the-docs-for-openai-codex-shell-tool-mcp|♯7962 docs: update the docs for @openai/codex-shell-tool-mcp]] · Change
- 2025-12-13 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-13-2-apps-and-integrations-changes-in-rust-v0-72-0|2 Apps and Integrations changes in rust-v0.72.0]] · Digest
- 2025-12-12 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-12-12-6-apps-and-integrations-changes-in-1-11-1|6 Apps and Integrations changes in 1.11.1]] · Digest
- 2025-12-11 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-12-11-7-apps-and-integrations-changes-in-v3-41-0|7 Apps and Integrations changes in v3.41.0]] · Digest
- 2025-12-11 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-12-11-16-apps-and-integrations-changes-in-1-11-0|16 Apps and Integrations changes in 1.11.0]] · Digest
- 2025-12-10 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-10-7817-fix-upgrade-modelcontextprotocol-sdk-to-1-24-0|♯7817 fix: Upgrade @modelcontextprotocol/sdk to ^1.24.0]] · Change
- 2025-12-10 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-12-10-system-notification-actions-for-terminal-and-mcp-approval-rejection|System notification actions for terminal and MCP approval/rejection]] · Change
- 2025-12-09 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-09-3-apps-and-integrations-changes-in-rust-v0-66-0|3 Apps and Integrations changes in rust-v0.66.0]] · Digest
- 2025-12-09 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-09-8-apps-and-integrations-changes-in-v0-20-0|8 Apps and Integrations changes in v0.20.0]] · Digest
- 2025-12-09 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2025-12-09-2-apps-and-integrations-changes-in-bug-fixes-and-improvements-for-dec-9th|2 Apps and Integrations changes in Bug fixes and improvements for Dec 9th]] · Digest
- 2025-12-04 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-12-04-added-subpages-and-content-to-hooks-by-jl-codes-in-https-github-com-cline-cline|added subpages and content to hooks]] · Change
- 2025-12-04 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-04-2-apps-and-integrations-changes-in-rust-v0-65-0|2 Apps and Integrations changes in rust-v0.65.0]] · Digest
- 2025-12-04 · <span class="tl-product tl-p14">**Google Antigravity**</span> · [[Changes/Google Antigravity/2025-12-04-google-one-integration|Google One integration]] · Change
- 2025-12-04 · <span class="tl-product tl-p24">**Runway**</span> · [[Changes/Runway/2025-12-04-turn-your-workflows-into-apps-you-can-share-with-your-workspace|Publish Workflows as Apps]] · Change
- 2025-12-02 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-12-02-feat-cerebras-add-x-cerebras-3rd-party-integration-header-by-sebastiand-cerebras|feat(cerebras): add X-Cerebras-3rd-Party-Integration header]] · Change
- 2025-12-02 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-02-3-apps-and-integrations-changes-in-rust-v0-64-0|3 Apps and Integrations changes in rust-v0.64.0]] · Digest
- 2025-12-02 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-02-9-apps-and-integrations-changes-in-v0-19-0|9 Apps and Integrations changes in v0.19.0]] · Digest
- 2025-12-02 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-12-02-2-apps-and-integrations-changes-in-v0-6-41|2 Apps and Integrations changes in v0.6.41]] · Digest

**2025-11**

- 2025-11-27 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-11-27-feat-hooks-implement-taskcomplete-hook-by-candieduniverse-in-https-github-com-cl|feat(hooks): Implement TaskComplete hook]] · Change
- 2025-11-26 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-11-26-5-apps-and-integrations-changes-in-1-10-1|5 Apps and Integrations changes in 1.10.1]] · Digest
- 2025-11-26 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-26-feat-zed-integration-use-default-model-routing-for-zed-integration-by-benbrandt|feat(zed-integration): Use default model routing for Zed integration]] · Change
- 2025-11-25 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-11-25-tool-servers-and-mcp-connections-now-support-function-name-filtering-allowing-ad|🔌 Tool servers and MCP connections now support function name filtering, allowing…]] · Change
- 2025-11-25 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2025-11-25-build-apps-in-v0-with-your-snowflake-data|Snowflake Integration]] · Change
- 2025-11-24 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-11-24-mcp-servers-work-in-prompt-mode|MCP servers work in --prompt mode]] · Change
- 2025-11-24 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-11-24-4-apps-and-integrations-changes-in-v0-6-37|4 Apps and Integrations changes in v0.6.37]] · Digest
- 2025-11-21 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-11-21-project-level-hooks-are-now-supported|Project level hooks are now supported]] · Change
- 2025-11-20 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-20-3-apps-and-integrations-changes-in-rust-v0-61-0|3 Apps and Integrations changes in rust-v0.61.0]] · Digest
- 2025-11-20 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-20-3-apps-and-integrations-changes-in-v0-17-0|3 Apps and Integrations changes in v0.17.0]] · Digest
- 2025-11-19 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-19-5-apps-and-integrations-changes-in-rust-v0-59-0|5 Apps and Integrations changes in rust-v0.59.0]] · Digest
- 2025-11-18 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-11-18-feat-upgrade-sap-ai-sdk-js-packages-major-version-by-yuvalman-in-https-github-co|feat: upgrade sap ai-sdk-js packages major version]] · Change
- 2025-11-14 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-14-3-apps-and-integrations-changes-in-v0-15-0|3 Apps and Integrations changes in v0.15.0]] · Digest
- 2025-11-13 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-11-13-3-apps-and-integrations-changes-in-v3-37-0|3 Apps and Integrations changes in v3.37.0]] · Digest
- 2025-11-13 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-13-6425-fix-sdk-documentation-replace-file-diffs-with-file-change-notifications-8b8|♯6425 — Fix SDK documentation]] · Change
- 2025-11-13 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-11-13-7-apps-and-integrations-changes-in-1-10-0|7 Apps and Integrations changes in 1.10.0]] · Digest
- 2025-11-10 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2025-11-10-stripe-is-now-a-native-integration-in-v0|Stripe Integration]] · Change
- 2025-11-09 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-09-6353-app-server-add-auth-v2-doc-update-codex-mcp-interface-section|♯6353 – App-server: add auth v2 doc & update Codex MCP interface section]] · Change
- 2025-11-07 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-11-07-add-mcp-tool-usage-to-glm-prompt-by-canvrno-in-https-github-com-cline-cline-pull|Add MCP tool usage to GLM prompt]] · Change
- 2025-11-07 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-07-6237-add-modelreasoningeffort-option-to-typescript-sdk|♯6237 Add modelReasoningEffort option to TypeScript SDK]] · Change
- 2025-11-07 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-07-9-apps-and-integrations-changes-in-v0-13-0|9 Apps and Integrations changes in v0.13.0]] · Digest
- 2025-11-06 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-11-06-8-apps-and-integrations-changes-in-v3-36-0|8 Apps and Integrations changes in v3.36.0]] · Digest
- 2025-11-06 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-11-06-2-apps-and-integrations-changes-in-v0-6-35|2 Apps and Integrations changes in v0.6.35]] · Digest
- 2025-11-05 · <span class="tl-product tl-p10">**Gamma**</span> · [[Changes/Gamma/2025-11-05-official-make-com-integration-https-www-make-com-en-integrations-gamma-app-for-n|Official Make. com integration((source link)]] · Change
- 2025-11-04 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-11-04-3-apps-and-integrations-changes-in-v3-35-1|3 Apps and Integrations changes in v3.35.1]] · Digest
- 2025-11-04 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-04-2-apps-and-integrations-changes-in-v0-12-0|2 Apps and Integrations changes in v0.12.0]] · Digest
- 2025-11-03 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-11-03-2-apps-and-integrations-changes-in-v0-0-354|2 Apps and Integrations changes in v0.0.354]] · Digest

**2025-10**

- 2025-10-31 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-10-31-5-apps-and-integrations-changes-in-v3-35-0|5 Apps and Integrations changes in v3.35.0]] · Digest
- 2025-10-31 · <span class="tl-product tl-p27">**v0**</span> · [[Changes/v0/2025-10-31-we-launched-a-new-integration-wizard-for-connecting-integrations-and-running-scr|Integration Wizard]] · Change
- 2025-10-30 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-30-11-apps-and-integrations-changes-in-rust-v0-52-0|11 Apps and Integrations changes in rust-v0.52.0]] · Digest
- 2025-10-29 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-29-7-apps-and-integrations-changes-in-v0-11-0|7 Apps and Integrations changes in v0.11.0]] · Digest
- 2025-10-27 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-27-improve-handling-of-mcp-tools-containing-slashes|Improve handling of MCP tools containing slashes]] · Change
- 2025-10-25 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-25-3-apps-and-integrations-changes-in-rust-v0-50-0|3 Apps and Integrations changes in rust-v0.50.0]] · Digest
- 2025-10-23 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-10-23-3-apps-and-integrations-changes-in-v3-34-0|3 Apps and Integrations changes in v3.34.0]] · Digest
- 2025-10-23 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-23-11-apps-and-integrations-changes-in-rust-v0-48-0|11 Apps and Integrations changes in rust-v0.48.0]] · Digest
- 2025-10-22 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-10-22-12-apps-and-integrations-changes-in-1-9-2|12 Apps and Integrations changes in 1.9.2]] · Digest
- 2025-10-22 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-22-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Digest
- 2025-10-18 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-18-enabled-github-mcp-server-in-prompt-mode|Enabled GitHub MCP server in prompt mode]] · Change
- 2025-10-17 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2025-10-17-improved-diagnostics-for-third-party-extensions|Improved diagnostics for third party extensions]] · Change
- 2025-10-16 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-10-16-9-apps-and-integrations-changes-in-v3-33-0|9 Apps and Integrations changes in v3.33.0]] · Digest
- 2025-10-15 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-15-3-apps-and-integrations-changes-in-v0-9-0|3 Apps and Integrations changes in v0.9.0]] · Digest
- 2025-10-14 · <span class="tl-product tl-p24">**Runway**</span> · [[Changes/Runway/2025-10-14-apps-are-an-ever-growing-collection-of-use-case-specific-workflows-that-make-it|Apps]] · Change
- 2025-10-13 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-10-13-we-re-rolling-out-two-new-ways-to-bring-slack-and-chatgpt-together-a-connector-t-be2213|Slack connector and app]] · Change
- 2025-10-13 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-13-3-apps-and-integrations-changes-in-v0-0-340|3 Apps and Integrations changes in v0.0.340]] · Digest
- 2025-10-10 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-10-improved-argument-input-to-mcp-servers-in-mcp-add-previously-users-had-to-use-co|Improved argument input to MCP servers in /mcp add -- previously, users had to use…]] · Change
- 2025-10-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-10-09-we-re-adding-notion-and-linear-as-synced-connectors-for-pro-users-so-you-can-sec|Adding Notion & Linear synced connectors]] · Change
- 2025-10-09 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-09-6-apps-and-integrations-changes-in-rust-v0-46-0|6 Apps and Integrations changes in rust-v0.46.0]] · Digest
- 2025-10-08 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-10-08-move-mcp-marketplace-catalog-from-global-state-to-disk-cache-by-celestial-vault|Move MCP marketplace catalog from global state to disk cache]] · Change
- 2025-10-08 · <span class="tl-product tl-p13">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-08-added-validation-for-mcp-server-names-fixes-https-github-com-github-copilot-cli|Added validation for MCP server names…]] · Change
- 2025-10-07 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-07-14-apps-and-integrations-changes-in-v0-8-0|14 Apps and Integrations changes in v0.8.0]] · Digest
- 2025-10-07 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-10-07-3-apps-and-integrations-changes-in-v0-6-33|3 Apps and Integrations changes in v0.6.33]] · Digest
- 2025-10-03 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-03-17-apps-and-integrations-changes-in-rust-v0-44-0|17 Apps and Integrations changes in rust-v0.44.0]] · Digest
- 2025-10-01 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-01-11-apps-and-integrations-changes-in-v0-7-0|11 Apps and Integrations changes in v0.7.0]] · Digest
- 2025-10-01 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2025-10-01-added-configurable-timeout-settings-for-shttp-mcp-servers-to-prevent-tool-calls|Added configurable timeout settings for SHTTP MCP servers to prevent tool calls…]] · Change

**2025-09**

- 2025-09-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-09-29-4-apps-and-integrations-changes-in-1-7|4 Apps and Integrations changes in 1.7]] · Digest
- 2025-09-29 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-09-29-5-apps-and-integrations-changes-in-1-9-1|5 Apps and Integrations changes in 1.9.1]] · Digest
- 2025-09-29 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-09-29-3-apps-and-integrations-changes-in-v0-6-32|3 Apps and Integrations changes in v0.6.32]] · Digest
- 2025-09-26 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-26-4-apps-and-integrations-changes-in-rust-v0-42-0|4 Apps and Integrations changes in rust-v0.42.0]] · Digest
- 2025-09-25 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-09-25-rename-mcp-tab-installed-to-configure-by-saoudrizwan-in-https-github-com-cline-c|Rename MCP tab 'Installed' to 'Configure']] · Change
- 2025-09-25 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-09-25-4-apps-and-integrations-changes-in-v0-6-31|4 Apps and Integrations changes in v0.6.31]] · Digest
- 2025-09-24 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-24-5-apps-and-integrations-changes-in-v0-6-0|5 Apps and Integrations changes in v0.6.0]] · Digest
- 2025-09-23 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-23-2-apps-and-integrations-changes-in-rust-v0-40-0|2 Apps and Integrations changes in rust-v0.40.0]] · Digest
- 2025-09-22 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-09-22-12-apps-and-integrations-changes-in-1-9-0|12 Apps and Integrations changes in 1.9.0]] · Digest
- 2025-09-20 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-09-20-feat-oca-ui-add-oca-provider-with-model-picker-and-auth-integration-by-nihar-ora|feat(oca-ui): add OCA provider with model picker and auth integration]] · Change
- 2025-09-17 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-17-6-apps-and-integrations-changes-in-v0-5-3|6 Apps and Integrations changes in v0.5.3]] · Digest
- 2025-09-17 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-09-17-2-apps-and-integrations-changes-in-v0-6-29|2 Apps and Integrations changes in v0.6.29]] · Digest
- 2025-09-17 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-09-17-onedrive-integration-was-fixed-after-recent-breakage-restoring-reliable-account|☁️ OneDrive integration was fixed after recent breakage, restoring reliable account…]] · Change
- 2025-09-15 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-15-5-apps-and-integrations-changes-in-rust-v0-36-0|5 Apps and Integrations changes in rust-v0.36.0]] · Digest
- 2025-09-12 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-09-12-2-apps-and-integrations-changes-in-1-6|2 Apps and Integrations changes in 1.6]] · Digest
- 2025-09-11 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-09-11-added-dify-ai-api-integration|Added Dify.ai API Integration]] · Change
- 2025-09-10 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-10-2-apps-and-integrations-changes-in-rust-v0-32-0|2 Apps and Integrations changes in rust-v0.32.0]] · Digest
- 2025-09-10 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-10-3395-set-a-user-agent-suffix-when-used-as-a-mcp-server-3395|♯3395 Set a user agent suffix when used as a mcp server (♯3395)]] · Change
- 2025-09-09 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-09-5-apps-and-integrations-changes-in-v0-4-0|5 Apps and Integrations changes in v0.4.0]] · Digest
- 2025-09-09 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-09-09-a-provider-toggle-in-connection-settings-now-allows-users-to-manually-specify-az|☁️ A provider toggle in connection settings now allows users to manually specify…]] · Change
- 2025-09-08 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-08-4-apps-and-integrations-changes-in-rust-v0-31-0|4 Apps and Integrations changes in rust-v0.31.0]] · Digest
- 2025-09-08 · <span class="tl-product tl-p15">**Granola**</span> · [[Changes/Granola/2025-09-08-with-new-people-and-companies-views-plus-attio-and-zapier-integrations|Three new features to help you build better customer relationships]] · Change
- 2025-09-05 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-05-4-apps-and-integrations-changes-in-rust-v0-30-0|4 Apps and Integrations changes in rust-v0.30.0]] · Digest
- 2025-09-04 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-04-17-apps-and-integrations-changes-in-v0-3-0|17 Apps and Integrations changes in v0.3.0]] · Digest
- 2025-09-03 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-09-03-4-apps-and-integrations-changes-in-1-8-1|4 Apps and Integrations changes in 1.8.1]] · Digest

**2025-08**

- 2025-08-29 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-29-3-apps-and-integrations-changes-in-rust-v0-26-0|3 Apps and Integrations changes in rust-v0.26.0]] · Digest
- 2025-08-29 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-29-mcp-stability-drop-mutexes-earlier-and-avoid-lock-ordering-pitfalls|MCP stability: drop mutexes earlier and avoid lock ordering pitfalls]] · Change
- 2025-08-29 · <span class="tl-product tl-p10">**Gamma**</span> · [[Changes/Gamma/2025-08-29-now-you-can-connect-gamma-to-8-000-apps-with-our-new-zapier-integration|Now you can connect Gamma to 8,000+ apps with our new Zapier integration]] · Change
- 2025-08-28 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-08-28-configurable-file-upload-processing-mode-added-process-in-background-query-param|📁 Configurable File Upload Processing Mode]] · Change
- 2025-08-27 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-08-27-11-apps-and-integrations-changes-in-1-8-0|11 Apps and Integrations changes in 1.8.0]] · Digest
- 2025-08-27 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-27-2-apps-and-integrations-changes-in-v0-2-0|2 Apps and Integrations changes in v0.2.0]] · Digest
- 2025-08-26 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-26-5-apps-and-integrations-changes-in-rust-v0-24-0|5 Apps and Integrations changes in rust-v0.24.0]] · Digest
- 2025-08-22 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-08-22-tool-server-loading-and-visibility-restored-resolved-an-issue-where-connected-to|🛠️ Tool Server Loading and Visibility Restored]] · Change
- 2025-08-21 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-08-21-feat-telemetry-add-mcp-tool-usage-tracking-by-nighttrek-in-https-github-com-clin|feat(telemetry): Add MCP tool usage tracking]] · Change
- 2025-08-21 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-08-21-5-apps-and-integrations-changes-in-v0-6-23|5 Apps and Integrations changes in v0.6.23]] · Digest
- 2025-08-20 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-08-20-2-apps-and-integrations-changes-in-v3-26-0|2 Apps and Integrations changes in v3.26.0]] · Digest
- 2025-08-20 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-20-5-apps-and-integrations-changes-in-rust-v0-23-0|5 Apps and Integrations changes in rust-v0.23.0]] · Digest
- 2025-08-20 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2025-08-20-2-apps-and-integrations-changes-in-0-54-0|2 Apps and Integrations changes in 0.54.0]] · Digest
- 2025-08-18 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-18-4-apps-and-integrations-changes-in-v0-1-22|4 Apps and Integrations changes in v0.1.22]] · Digest
- 2025-08-14 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-14-41-apps-and-integrations-changes-in-v0-1-21|41 Apps and Integrations changes in v0.1.21]] · Digest
- 2025-08-13 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-08-13-add-an-endpoint-to-the-hostbridge-for-integration-testing-by-sjf-in-https-github|Add an endpoint to the HostBridge for integration testing]] · Change
- 2025-08-13 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-13-3-apps-and-integrations-changes-in-v0-1-20|3 Apps and Integrations changes in v0.1.20]] · Digest
- 2025-08-12 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-12-https-github-com-openai-codex-pull-1975-add-json-schema-sanitization-for-mcp-too|(source link) add JSON schema sanitization for MCP tools…]] · Change
- 2025-08-12 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-12-10-apps-and-integrations-changes-in-v0-1-19|10 Apps and Integrations changes in v0.1.19]] · Digest
- 2025-08-11 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-08-11-6-apps-and-integrations-changes-in-1-7-2|6 Apps and Integrations changes in 1.7.2]] · Digest
- 2025-08-09 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-08-09-7-apps-and-integrations-changes-in-v0-6-19|7 Apps and Integrations changes in v0.6.19]] · Digest
- 2025-08-08 · <span class="tl-product tl-p10">**Gamma**</span> · [[Changes/Gamma/2025-08-08-we-ve-just-launched-our-generate-api-in-beta-for-gamma-pro-users-now-you-can-cre|We’ve just launched our Generate API in beta for Gamma Pro users! Now you can…]] · Change
- 2025-08-06 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-06-26-apps-and-integrations-changes-in-v0-1-18|26 Apps and Integrations changes in v0.1.18]] · Digest
- 2025-08-05 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-05-24-apps-and-integrations-changes-in-v0-1-17|24 Apps and Integrations changes in v0.1.17]] · Digest
- 2025-08-04 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-08-04-refactor-use-mcp-icon-in-the-navbar-and-update-styling-by-sjf-in-https-github-co|refactor: Use MCP icon in the navbar and update styling]] · Change
- 2025-08-02 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-02-21-apps-and-integrations-changes-in-v0-1-16|21 Apps and Integrations changes in v0.1.16]] · Digest

**2025-07**

- 2025-07-31 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-07-31-2-apps-and-integrations-changes-in-v3-20-3|2 Apps and Integrations changes in v3.20.3]] · Digest
- 2025-07-31 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2025-07-31-add-mcp-support-for-cli-by-ryanhoangt-in-https-github-com-all-hands-ai-openhands|Add MCP support for CLI]] · Change
- 2025-07-30 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-30-19-apps-and-integrations-changes-in-v0-1-15|19 Apps and Integrations changes in v0.1.15]] · Digest
- 2025-07-29 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-07-29-extension-marketplace-supports-custom-urls|Extension marketplace supports custom URLs]] · Change
- 2025-07-28 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-07-28-2-apps-and-integrations-changes-in-1-7-1|2 Apps and Integrations changes in 1.7.1]] · Digest
- 2025-07-25 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-25-18-apps-and-integrations-changes-in-v0-1-14|18 Apps and Integrations changes in v0.1.14]] · Digest
- 2025-07-24 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-07-24-pro-users-can-now-utilize-chat-search-with-hubspot-and-custom-connectors-mcp-in-b9b682|Chat search for HubSpot and custom connectors (MCP) (Pro)]] · Change
- 2025-07-24 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2025-07-24-2-apps-and-integrations-changes-in-0-50-0|2 Apps and Integrations changes in 0.50.0]] · Digest
- 2025-07-23 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-07-23-numerous-fixes-to-codex-mcp|Numerous fixes to codex mcp]] · Change
- 2025-07-23 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-07-23-10-apps-and-integrations-changes-in-1-7-0|10 Apps and Integrations changes in 1.7.0]] · Digest
- 2025-07-19 · <span class="tl-product tl-p6">**Codex CLI**</span> · [[Changes/Codex CLI/2025-07-19-https-github-com-openai-codex-pull-1571-fixes-a-longstanding-issue-where-we-fail|(source link) fixes a longstanding issue where we failed…]] · Change
- 2025-07-19 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-19-12-apps-and-integrations-changes-in-v0-1-13|12 Apps and Integrations changes in v0.1.13]] · Digest
- 2025-07-19 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-07-19-cleaner-database-credentials-database-connection-no-longer-duplicates-in-credent|🧹 Cleaner Database Credentials]] · Change
- 2025-07-16 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2025-07-16-added-cli-vscode-integration-by-enyst-in-https-github-com-all-hands-ai-openhands|Added CLI/VSCode integration]] · Change
- 2025-07-15 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-07-15-add-markdown-parsing-to-mcp-responses-by-celestial-vault-in-https-github-com-cli|Add markdown parsing to MCP responses]] · Change
- 2025-07-11 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-11-6-apps-and-integrations-changes-in-v0-1-10|6 Apps and Integrations changes in v0.1.10]] · Digest
- 2025-07-10 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-07-10-10-apps-and-integrations-changes-in-1-6-0|10 Apps and Integrations changes in 1.6.0]] · Digest
- 2025-07-08 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-07-08-update-the-no-vscode-postmessage-eslint-rule-to-check-for-any-of-the-vscode-sdk|Update the no-vscode-postmessage eslint rule to check for any of the vscode SDK…]] · Change
- 2025-07-08 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-07-08-migrate-download-mcp-response-to-proto-by-celestial-vault-in-https-github-com-cl|migrate download MCP response to proto]] · Change
- 2025-07-03 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-07-03-2-apps-and-integrations-changes-in-1-2|2 Apps and Integrations changes in 1.2]] · Digest
- 2025-07-02 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-07-02-7-apps-and-integrations-changes-in-1-5-1|7 Apps and Integrations changes in 1.5.1]] · Digest
- 2025-07-02 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-02-add-excludedtools-to-extensions-by-scidomino-in-https-github-com-google-gemini-g|Add excludedTools to extensions]] · Change
- 2025-07-02 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2025-07-02-add-nativemind-to-community-integrations-by-xukecheng-in-https-github-com-ollama|Add NativeMind to Community Integrations]] · Change
- 2025-07-02 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2025-07-02-disabled-jupyter-plugin-by-default-in-cli-runtime-by-li-boxuan-in-https-github-c|Disabled Jupyter plugin by default in CLI runtime]] · Change
- 2025-07-01 · <span class="tl-product tl-p12">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-01-feat-add-support-to-remote-mcp-servers-for-custom-http-headers-by-aspiers-in-htt|feat: add support to remote MCP servers for custom HTTP headers]] · Change

**2025-06**

- 2025-06-25 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-06-25-11-apps-and-integrations-changes-in-1-5-0|11 Apps and Integrations changes in 1.5.0]] · Digest
- 2025-06-24 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-06-24-pro-users-are-now-able-to-use-chat-search-connectors-in-addition-to-deep-researc-9d5a85|Chat search connectors (Pro)]] · Change
- 2025-06-20 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2025-06-20-3-apps-and-integrations-changes-in-0-44-0|3 Apps and Integrations changes in 0.44.0]] · Digest
- 2025-06-20 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2025-06-20-slack-integration-beta-with-cloud-openhands-malhotra5-in-https-github-com-all-ha|Slack Integration (Beta) with Cloud OpenHands @malhotra5…]] · Change
- 2025-06-20 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2025-06-20-2-apps-and-integrations-changes-in-0-45-0|2 Apps and Integrations changes in 0.45.0]] · Digest
- 2025-06-16 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-06-16-2-apps-and-integrations-changes-in-1-4-3|2 Apps and Integrations changes in 1.4.3]] · Digest
- 2025-06-16 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-06-16-ldap-group-synchronization-experimental-automatically-sync-user-groups-from-your|🗂️ LDAP Group Synchronization (Experimental)]] · Change
- 2025-06-12 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-06-12-2-apps-and-integrations-changes-in-v3-17-13|2 Apps and Integrations changes in v3.17.13]] · Digest
- 2025-06-11 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-06-11-6-apps-and-integrations-changes-in-1-4-2|6 Apps and Integrations changes in 1.4.2]] · Digest
- 2025-06-10 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-06-10-add-collapsible-mcp-response-panels-to-keep-conversations-focused-on-the-main-ai|Add collapsible MCP response panels to keep conversations focused on the main AI…]] · Change
- 2025-06-10 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-06-10-openai-compatible-embeddings-endpoint-introducing-a-fully-openai-style-api-embed|🧩 OpenAI-Compatible Embeddings Endpoint]] · Change
- 2025-06-09 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2025-06-09-if-you-have-feedback-please-create-an-issue-on-github-with-the-app-label-these-a|If you have feedback, please create an issue on GitHub with the app label]] · Change
- 2025-06-05 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-06-05-add-support-for-streamable-mcp-servers|Add support for streamable MCP servers]] · Change
- 2025-06-05 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2025-06-05-2-apps-and-integrations-changes-in-0-41-0|2 Apps and Integrations changes in 0.41.0]] · Digest
- 2025-06-04 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-06-04-supported-connectors-google-drive-sharepoint-dropbox-box-outlook-gmail-google-ca|Supported connectors: Google Drive, SharePoint, Dropbox, Box, Outlook, Gmail, Google…]] · Change
- 2025-06-04 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-06-04-admin-published-connectors-appear-in-the-connector-list-for-all-users|Admin-published connectors appear in the connector list for all users]] · Change
- 2025-06-04 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-06-04-admins-and-users-can-now-build-and-deploy-custom-connectors-to-proprietary-syste|Admins and users can now build and deploy custom connectors to proprietary systems…]] · Change
- 2025-06-01 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2025-06-01-2-apps-and-integrations-changes-in-0-40-0|2 Apps and Integrations changes in 0.40.0]] · Digest

**2025-05**

- 2025-05-29 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-05-29-azure-openai-embedding-support-you-can-now-select-azure-openai-endpoints-for-tex|🟦 Azure OpenAI Embedding Support]] · Change
- 2025-05-27 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-05-27-5-apps-and-integrations-changes-in-1-4-1|5 Apps and Integrations changes in 1.4.1]] · Digest
- 2025-05-26 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-05-26-4-apps-and-integrations-changes-in-v0-6-11|4 Apps and Integrations changes in v0.6.11]] · Digest
- 2025-05-22 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-05-22-add-integration-with-nebius-ai-studio-as-a-new-provider-thanks-aktsvigun|Add integration with Nebius AI Studio as a new provider (Thanks @Aktsvigun!)]] · Change
- 2025-05-19 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-05-19-2-apps-and-integrations-changes-in-v0-6-10|2 Apps and Integrations changes in v0.6.10]] · Digest
- 2025-05-16 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-05-16-add-tailwind-css-intellisense-to-the-recommended-extensions-list|Add Tailwind CSS IntelliSense to the recommended extensions list]] · Change
- 2025-05-15 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-05-15-5-apps-and-integrations-changes-in-1-4-0|5 Apps and Integrations changes in 1.4.0]] · Digest
- 2025-05-12 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2025-05-12-2-apps-and-integrations-changes-in-0-38-0|2 Apps and Integrations changes in 0.38.0]] · Digest
- 2025-05-10 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-05-10-external-reranker-support-for-knowledge-base-search-supercharge-your-retrieval-a|🏆 External Reranker Support for Knowledge Base Search]] · Change
- 2025-05-10 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-05-10-external-reranker-integration-functionality-restored-external-reranker-integrati|🤖 External Reranker Integration Functionality Restored]] · Change
- 2025-05-05 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-05-05-2-apps-and-integrations-changes-in-v0-6-6|2 Apps and Integrations changes in v0.6.6]] · Digest
- 2025-05-03 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-05-03-refactor-message-handling-to-not-show-the-mcp-view-of-the-server-modal|Refactor message handling to not show the MCP View of the server modal]] · Change

**2025-04**

- 2025-04-28 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-04-28-7-apps-and-integrations-changes-in-1-3-1|7 Apps and Integrations changes in 1.3.1]] · Digest
- 2025-04-25 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-04-25-add-download-counts-to-mcp-marketplace-items|Add download counts to MCP marketplace items]] · Change
- 2025-04-23 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-04-23-12-apps-and-integrations-changes-in-1-3-0|12 Apps and Integrations changes in 1.3.0]] · Digest
- 2025-04-19 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-04-19-add-ability-for-models-that-support-it-to-receive-image-responses-from-mcp-serve|Add ability for models that support it to receive image responses from MCP servers…]] · Change
- 2025-04-16 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2025-04-16-added-support-for-mcp-servers-natively-via-codeactagent-by-ducphamle2-in-https-g|Added support for MCP servers natively via CodeActAgent]] · Change
- 2025-04-13 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-04-13-openapi-yaml-format-support-external-tools-can-now-use-yaml-format-openapi-specs|📄 OpenAPI YAML Format Support]] · Change
- 2025-04-12 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-04-12-add-settings-button-to-mcp-popover-to-easily-modify-installed-servers|Add settings button to MCP popover to easily modify installed servers]] · Change
- 2025-04-09 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-04-09-6-apps-and-integrations-changes-in-1-2-0|6 Apps and Integrations changes in 1.2.0]] · Digest
- 2025-04-08 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-04-08-add-modal-in-the-chat-area-to-more-easily-enable-or-disable-mcp-servers|Add modal in the chat area to more easily enable or disable MCP servers]] · Change
- 2025-04-07 · <span class="tl-product tl-p26">**Windsurf**</span> · [[Changes/Windsurf/2025-04-07-increased-stability-around-mcp-sse-connections|Increased stability around MCP SSE connections]] · Change
- 2025-04-04 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-04-04-add-a-tab-for-configuring-local-mcp-servers|Add a tab for configuring local MCP Servers]] · Change
- 2025-04-04 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-04-04-upgraded-the-stripe-integration-https-docs-lovable-dev-integrations-stripe-md|Upgraded the Stripe integration((source link)]] · Change
- 2025-04-01 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-04-01-3-apps-and-integrations-changes-in-v3-8-5|3 Apps and Integrations changes in v3.8.5]] · Digest
- 2025-04-01 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-04-01-2-apps-and-integrations-changes-in-v0-6-0|2 Apps and Integrations changes in v0.6.0]] · Digest

**2025-03**

- 2025-03-23 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-03-23-2-apps-and-integrations-changes-in-v3-8-0|2 Apps and Integrations changes in v3.8.0]] · Digest
- 2025-03-23 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-03-23-3-apps-and-integrations-changes-in-0-48-x|3 Apps and Integrations changes in 0.48.x]] · Digest
- 2025-03-21 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-03-21-added-git-commit-verify-flag-default-false-to-control-whether-git-commit-hooks-a|Added --git-commit-verify flag (default]] · Change
- 2025-03-21 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-03-21-github-plugin-installation-resolved-an-import-dsl-issue-that-blocked-the-install|GitHub Plugin Installation]] · Change
- 2025-03-18 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-03-18-enhanced-integration-of-pg-bigm-for-keyword-search-in-pgvector-by-utsumi-fj-in-1|Enhanced Integration of pg_bigm for Keyword Search in pgvector by @utsumi-fj in ♯13876]] · Change
- 2025-03-11 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-03-11-mcp-added-global-server-configuration-with-cursor-mcp-json-and-support-for-envir|MCP: Added global server configuration with ~/.cursor/mcp.json and support…]] · Change
- 2025-03-11 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-03-11-8-apps-and-integrations-changes-in-1-0-1|8 Apps and Integrations changes in 1.0.1]] · Digest
- 2025-03-03 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-03-03-add-timeout-option-to-mcp-servers|Add timeout option to MCP servers]] · Change
- 2025-03-01 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-03-01-2-apps-and-integrations-changes-in-v3-5-0|2 Apps and Integrations changes in v3.5.0]] · Digest

**2025-02**

- 2025-02-28 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-02-28-9-apps-and-integrations-changes-in-1-0-0|9 Apps and Integrations changes in 1.0.0]] · Digest
- 2025-02-27 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-02-27-2-apps-and-integrations-changes-in-v0-5-17|2 Apps and Integrations changes in v0.5.17]] · Digest
- 2025-02-19 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-02-19-2-apps-and-integrations-changes-in-0-46-x|2 Apps and Integrations changes in 0.46.x]] · Digest
- 2025-02-19 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2025-02-19-mcp-improvements|MCP improvements]] · Change
- 2025-02-12 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-02-12-3-apps-and-integrations-changes-in-lovable-updates-2025-02-12|3 Apps and Integrations changes in Lovable updates — 2025-02-12]] · Digest
- 2025-02-07 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-02-07-add-azure-openai-api-version-2024-12-01-preview-by-kei-yamazaki-in-https-github|add azure openai api version 2024-12-01-preview]] · Change
- 2025-02-05 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2025-02-05-exa-search-engine-integration-a-new-search-provider-has-been-added-allowing-user|🔗 Exa Search Engine Integration]] · Change

**2025-01**

- 2025-01-30 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-01-30-add-advanced-settings-to-remove-mcp-prompts-from-requests-to-save-tokens-enable|Add Advanced Settings to remove MCP prompts from requests to save tokens…]] · Change
- 2025-01-29 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2025-01-29-improved-performance-of-github-api-integration-by-using-modern-async-http-client|Improved performance of GitHub API integration by using modern async HTTP client]] · Change
- 2025-01-28 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-01-28-support-for-resend-has-improved-with-the-transition-to-the-node-sdk|Support for Resend has improved with the transition to the Node SDK]] · Change
- 2025-01-21 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2025-01-21-add-on-off-toggle-for-mcp-servers-to-disable-them-when-not-in-use-and-auto-appro|Add on/off toggle for MCP servers to disable them when not in use, and auto-approve…]] · Change
- 2025-01-13 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-01-13-2-apps-and-integrations-changes-in-0-15-1|2 Apps and Integrations changes in 0.15.1]] · Digest
- 2025-01-07 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2025-01-07-feat-add-filter-to-show-only-apps-created-by-the-user-by-miya-in-https-github-co|feat: Add filter to show only apps created by the user]] · Change
- 2025-01-06 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2025-01-06-github-integration-outage-https-lovable-dev-news-github-incident-2025-01-02|GitHub Integration Outage((source link)]] · Change

</details>

</details>

<details class="disclosure">
<summary>2024 · 73 entries (Aider 1 · ChatGPT 2 · Cline 3 · Cursor 3 · Dify 32 · Gemini 2 · Lovable 1 · Ollama 1 · Open WebUI 16 · OpenHands 8 · Replit 4)</summary>

**2024-12**

- 2024-12-27 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2024-12-27-integrations|Integrations]] · Launch
- 2024-12-20 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2024-12-20-integration-visibility|Integration visibility]] · Launch
- 2024-12-13 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2024-12-13-build-beautiful-apps|Build Beautiful Apps]] · Launch
- 2024-12-03 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-12-03-you-can-now-use-github-com-links-directly-for-dsls-instead-of-relying-on-raw-git|Use github.com links directly for DSLs instead of relying on raw.githubusercontent.com]] · Change
- 2024-12-03 · <span class="tl-product tl-p16">**Lovable**</span> · [[Changes/Lovable/2024-12-03-introducing-feedback-lovable-dev-for-feature-and-integration-request|Introducing feedback.lovable.dev for feature and integration request]] · Launch
- 2024-12-02 · <span class="tl-product tl-p11">**Gemini**</span> · [[Changes/Gemini/2024-12-02-expanding-workspace-extensions-to-more-languages-keep-and-tasks|Expanding Workspace extensions to more languages: Keep and Tasks]] · Expansion

**2024-10**

- 2024-10-06 · <span class="tl-product tl-p11">**Gemini**</span> · [[Changes/Gemini/2024-10-06-gemini-can-access-helpful-information-from-more-apps-and-services|Gemini can access helpful information from more apps and services]] · Launch

**2024-05**

- 2024-05-27 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-05-27-you-can-now-publish-your-ai-workflow-in-dify-as-a-reusable-tool-this-allows-for|Publish your AI workflow in Dify as a reusable tool]] · Change

**2024-01**

- 2024-01-10 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2024-01-10-the-store-features-a-diverse-range-of-gpts-developed-by-our-partners-and-the-com-71db32|Discover what’s trending in the GPT Store]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 64 (Aider 1 · ChatGPT 1 · Cline 3 · Cursor 3 · Dify 30 · Ollama 1 · Open WebUI 16 · OpenHands 8 · Replit 1)</summary>

**2024-12**

- 2024-12-31 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2024-12-31-2-apps-and-integrations-changes-in-v0-5-3|2 Apps and Integrations changes in v0.5.3]] · Digest
- 2024-12-27 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2024-12-27-pipelines-outlet-hook-registration-addressed-an-issue-where-outlet-hooks-for-pip|🔗 Pipelines Outlet Hook Registration]] · Change
- 2024-12-25 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2024-12-25-notification-webhook-integration-get-alerts-via-webhooks-even-when-your-tab-is-c|🌐 Notification Webhook Integration]] · Change
- 2024-12-18 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2024-12-18-enable-or-disable-for-reading-files-directories-editing-files-executing-terminal|Enable or disable for]] · Change
- 2024-12-18 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-12-18-opendal-integration-introducing-apache-opendal-https-github-com-apache-opendal-t|OpenDAL Integration: Introducing Apache…]] · Change
- 2024-12-16 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-12-16-features-integration-of-apache-opendal-https-github-com-apache-opendal-storage-f|Features integration of Apache OpenDAL((source link) storage…]] · Change
- 2024-12-13 · <span class="tl-product tl-p23">**Replit**</span> · [[Changes/Replit/2024-12-13-more-beautiful-apps-improved-support-for-responsive-react-apps-allows-you-to-cre|More Beautiful Apps: Improved support for responsive React apps allows you…]] · Change
- 2024-12-12 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2024-12-12-3-apps-and-integrations-changes-in-v2-2-0|3 Apps and Integrations changes in v2.2.0]] · Digest
- 2024-12-09 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-12-09-2-apps-and-integrations-changes-in-0-13-2|2 Apps and Integrations changes in 0.13.2]] · Digest

**2024-11**

- 2024-11-25 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-11-25-feat-add-a-minimal-separator-between-pinned-apps-and-unpinned-apps-in-the-explor|feat: add a minimal separator between pinned apps and unpinned apps in the explore page]] · Change
- 2024-11-19 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2024-11-19-functions-moved-to-admin-panel-as-functions-operate-as-advanced-plugins-they-are|🛠️ Functions Moved to Admin Panel]] · Change
- 2024-11-11 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-11-11-gitlab-tools-integration-amp-up-your-devops-with-the-integration-of-gitlab-tools|GitLab Tools Integration]] · Change
- 2024-11-05 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-11-05-3-apps-and-integrations-changes-in-0-11-0|3 Apps and Integrations changes in 0.11.0]] · Digest
- 2024-11-04 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-11-04-easily-apply-file-edits-from-chatgpt-claude-or-other-web-apps|Easily apply file edits from ChatGPT, Claude or other web apps]] · Change
- 2024-11-04 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2024-11-04-discoverybench-openhands-integration-by-ethan0456-in-https-github-com-all-hands|DiscoveryBench OpenHands Integration]] · Change

**2024-10**

- 2024-10-28 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-10-28-text-to-image-with-stable-diffusion-3-5-bring-your-text-to-life-with-the-new-sta|Text-to-Image with Stable-Diffusion 3.5: Bring your text to life with the new…]] · Change
- 2024-10-26 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2024-10-26-feedback-export-enhancements-feedback-history-data-can-now-be-exported-to-json-a|🔧 Feedback Export Enhancements]] · Change
- 2024-10-23 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-10-23-feat-tools-refactor-the-base-table-plugin-by-hgnulb-in-https-github-com-langgeni|feat(Tools): Refactor the base table plugin]] · Change
- 2024-10-14 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-10-14-4-apps-and-integrations-changes-in-0-9-2|4 Apps and Integrations changes in 0.9.2]] · Digest
- 2024-10-07 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2024-10-07-knowledge-feature-reimagined-documents-feature-now-more-performant-with-a-better|📚 Knowledge Feature]] · Change
- 2024-10-07 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2024-10-07-web-and-youtube-attachment-fix-resolved-an-issue-where-attaching-web-links-and-y|🖥️ Web and YouTube Attachment Fix]] · Change

**2024-09**

- 2024-09-30 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-09-30-3-apps-and-integrations-changes-in-0-9-0|3 Apps and Integrations changes in 0.9.0]] · Digest
- 2024-09-26 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2024-09-26-ollama-embed-form-data-adjusted-the-integration-inaccuracies-in-the-embed-form-d|📋 Ollama /embed Form Data]] · Change
- 2024-09-20 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-09-20-python-sdk-add-knowledgebaseclient-and-the-corresponding-test-cases-by-twisker-i|Python SDK Add KnowledgeBaseClient and the corresponding test cases]] · Change
- 2024-09-19 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2024-09-19-3-apps-and-integrations-changes-in-v0-3-22|3 Apps and Integrations changes in v0.3.22]] · Digest
- 2024-09-12 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-09-12-2-apps-and-integrations-changes-in-0-8-1|2 Apps and Integrations changes in 0.8.1]] · Digest
- 2024-09-09 · <span class="tl-product tl-p5">**Cline**</span> · [[Changes/Cline/2024-09-09-commands-now-run-directly-in-your-terminal-thanks-to-vscode-1-93-s-new-shell-int|Commands now run directly in your terminal thanks to VSCode 1.93's new shell…]] · Change
- 2024-09-04 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2024-09-04-automatic-rewrite-of-import-statements-in-tools-functions-tool-and-function-scri|🔄 Automatic Rewrite of Import Statements in Tools & Functions]] · Change
- 2024-09-03 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-09-03-4-apps-and-integrations-changes-in-0-7-3|4 Apps and Integrations changes in 0.7.3]] · Digest

**2024-08**

- 2024-08-19 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-08-19-custom-app-icons-personalize-your-apps-with-custom-icons-by-xuzuodong-in-7196-ht|Custom App Icons]] · Change
- 2024-08-14 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2024-08-14-integration-testing-improvements-modified-how-cypress-integration-tests-detect-c|🚧 Integration Testing Improvements]] · Change
- 2024-08-07 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2024-08-07-non-streaming-support-for-functions-plugin-fixed-a-functionality-issue-with-the|🔧 Non-Streaming Support for Functions Plugin]] · Change

**2024-07**

- 2024-07-27 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2024-07-27-2-apps-and-integrations-changes-in-0-8-2|2 Apps and Integrations changes in 0.8.2]] · Digest
- 2024-07-23 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-07-23-3-apps-and-integrations-changes-in-0-6-15|3 Apps and Integrations changes in 0.6.15]] · Digest
- 2024-07-19 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2024-07-19-5-apps-and-integrations-changes-in-0-8-1|5 Apps and Integrations changes in 0.8.1]] · Digest
- 2024-07-15 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-07-15-2-apps-and-integrations-changes-in-0-6-14|2 Apps and Integrations changes in 0.6.14]] · Digest
- 2024-07-13 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2024-07-13-2-apps-and-integrations-changes-in-0-8-0|2 Apps and Integrations changes in 0.8.0]] · Digest
- 2024-07-09 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2024-07-09-apache-tika-integration-added-support-for-using-apache-tika-as-a-document-loader|📄 Apache Tika Integration]] · Change
- 2024-07-08 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-07-08-2-apps-and-integrations-changes-in-0-6-13|2 Apps and Integrations changes in 0.6.13]] · Digest
- 2024-07-05 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2024-07-05-chore-deps-dev-bump-typescript-eslint-eslint-plugin-from-7-14-1-to-7-15-0-in-fro|chore(deps-dev): bump @typescript-eslint/eslint-plugin from 7.14.1 to 7.15.0 in /frontend]] · Change
- 2024-07-03 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2024-07-03-docs-management-go-to-cursor-settings-features-docs-to-re-index-your-docs|Docs management! Go to Cursor Settings  Features  Docs to re-index your docs]] · Change

**2024-06**

- 2024-06-29 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2024-06-29-10-apps-and-integrations-changes-in-0-7-0|10 Apps and Integrations changes in 0.7.0]] · Digest
- 2024-06-28 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-06-28-tracing-with-langsmith-and-langfuse-now-you-can-trace-your-apps-traffic-with-lan|Tracing with LangSmith and Langfuse]] · Change
- 2024-06-27 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2024-06-27-functions-feature-you-can-now-utilize-functions-like-filters-middleware-and-pipe|✨ "Functions" Feature]] · Change
- 2024-06-14 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-06-14-chore-add-some-new-api-version-for-azure-openai-by-leslie2046-in-https-github-co|chore:add some new api version for azure openai]] · Change
- 2024-06-07 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2024-06-07-ollama-can-now-be-accessed-from-local-apps-built-with-electron-and-tauri-as-well|Ollama can now be accessed from local apps built with Electron and Tauri, as well…]] · Change
- 2024-06-05 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2024-06-05-bump-typescript-eslint-eslint-plugin-from-7-11-0-to-7-12-0-in-frontend-by-depend|Bump @typescript-eslint/eslint-plugin from 7.11.0 to 7.12.0 in /frontend]] · Change
- 2024-06-04 · <span class="tl-product tl-p22">**OpenHands**</span> · [[Changes/OpenHands/2024-06-04-2-apps-and-integrations-changes-in-0-6-1|2 Apps and Integrations changes in 0.6.1]] · Digest
- 2024-06-02 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2024-06-02-usage-monitoring-with-langfuse-track-and-analyze-usage-statistics-with-langfuse|📊 Usage Monitoring with Langfuse]] · Change

**2024-05**

- 2024-05-16 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2024-05-16-upload-the-latest-file-versions-directly-from-google-drive-microsoft-onedrive-pe-70f6a3|Upload the latest file versions directly from Google Drive, Microsoft OneDrive…]] · Change
- 2024-05-13 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-05-13-4-apps-and-integrations-changes-in-0-6-8|4 Apps and Integrations changes in 0.6.8]] · Digest
- 2024-05-09 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-05-09-3-apps-and-integrations-changes-in-0-6-7|3 Apps and Integrations changes in 0.6.7]] · Digest
- 2024-05-02 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-05-02-2-apps-and-integrations-changes-in-0-6-6|2 Apps and Integrations changes in 0.6.6]] · Digest

**2024-04**

- 2024-04-22 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-04-22-2-apps-and-integrations-changes-in-0-6-4|2 Apps and Integrations changes in 0.6.4]] · Digest
- 2024-04-08 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-04-08-2-apps-and-integrations-changes-in-0-6-0|2 Apps and Integrations changes in 0.6.0]] · Digest

**2024-03**

- 2024-03-21 · <span class="tl-product tl-p19">**Open WebUI**</span> · [[Changes/Open WebUI/2024-03-21-webhook-integration-now-you-can-subscribe-to-new-user-sign-up-events-via-webhook|🔗 Webhook Integration: Now you can subscribe to new user sign-up events via webhook]] · Change
- 2024-03-19 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-03-19-feat-add-api-version-selection-for-azure-openai-apis-by-leslie2046-in-https-gith|feat:add api-version selection for azure openai APIs]] · Change

**2024-02**

- 2024-02-19 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-02-19-chore-add-type-files-and-unit-test-ci-for-node-js-sdk-by-tseian-in-https-github|Chore: Add type files and unit test ci for Node.js SDK]] · Change
- 2024-02-06 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-02-06-3-apps-and-integrations-changes-in-0-5-4|3 Apps and Integrations changes in 0.5.4]] · Digest
- 2024-02-01 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-02-01-2-apps-and-integrations-changes-in-0-5-3|2 Apps and Integrations changes in 0.5.3]] · Digest

**2024-01**

- 2024-01-25 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2024-01-25-update-0-24-3-0-24-4-adds-ability-to-configure-openai-base-url-fixes-getcursor-c|UPDATE (0.24.3-0.24.4): Adds ability to configure OpenAI base URL, fixes…]] · Change
- 2024-01-24 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-01-24-5-apps-and-integrations-changes-in-0-5-0|5 Apps and Integrations changes in 0.5.0]] · Digest
- 2024-01-15 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2024-01-15-supports-newer-version-of-python-extension|Supports newer version of python extension]] · Change
- 2024-01-11 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2024-01-11-2-apps-and-integrations-changes-in-0-4-5|2 Apps and Integrations changes in 0.4.5]] · Digest

</details>

</details>

<details class="disclosure">
<summary>2023 · 34 entries (Aider 1 · ChatGPT 5 · Cursor 17 · Dify 9 · Gemini 1 · Ollama 1)</summary>

**2023-11**

- 2023-11-06 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-11-06-you-can-now-create-custom-versions-of-chatgpt-that-combine-instructions-extra-kn-5c0997|Introducing GPTs]] · Launch

**2023-09**

- 2023-09-19 · <span class="tl-product tl-p11">**Gemini**</span> · [[Changes/Gemini/2023-09-19-bard-can-now-access-helpful-information-from-google-apps-and-services|Bard can now access helpful information from Google apps and services]] · Launch

**2023-06**

- 2023-06-09 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-06-09-you-can-now-have-the-ai-read-documentation-on-your-behalf-this-will-improve-it-s|Show the AI documentation]] · Change

**2023-05**

- 2023-05-24 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-05-24-browse-with-bing-we-ve-integrated-the-browsing-feature-currently-in-beta-for-pai|Bing Plugin]] · Launch
- 2023-05-17 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-05-17-you-can-pin-custom-extensions-to-your-activity-bar-in-the-top-left|Activity Bar pinning]] · Launch

**2023-03**

- 2023-03-23 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 28 (Aider 1 · ChatGPT 2 · Cursor 15 · Dify 9 · Ollama 1)</summary>

**2023-12**

- 2023-12-16 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-12-16-copilot-we-ve-continued-to-improve-the-copilot-ghost-text-experience-surprisingl|Copilot++: We've continued to improve the Copilot++ ghost text experience]] · Change

**2023-11**

- 2023-11-21 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2023-11-21-feat-remove-plugin-page-by-zxhlyh-in-https-github-com-langgenius-dify-pull-1544|feat: remove plugin page]] · Change
- 2023-11-15 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-11-15-now-based-on-vs-code-1-84-2-notably-this-fixes-a-few-notebook-bugs-and-ensures-t|New upstream]] · Change
- 2023-11-15 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-11-15-cursor-is-now-based-on-vs-code-1-84-2-notably-this-fixes-a-few-notebook-bugs-and|Cursor is now based on VS Code 1.84.2]] · Change
- 2023-11-13 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2023-11-13-2-apps-and-integrations-changes-in-0-3-30|2 Apps and Integrations changes in 0.3.30]] · Digest

**2023-10**

- 2023-10-20 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-10-20-cursor-is-now-based-on-vs-code-1-83-1-this-ensures-that-the-newest-versions-of-a|Cursor is now based on VS Code 1.83.1]] · Change

**2023-09**

- 2023-09-17 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-09-17-we-point-to-a-different-marketplace-for-downloading-extensions-and-use-a-fork-of|Cursor Python and Cursor Marketplace]] · Change
- 2023-09-11 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-09-11-we-serve-extensions-now-using-cursor-s-extension-marketplace|Cursor Marketplace]] · Change
- 2023-09-09 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2023-09-09-chore-handle-workspace-apps-scrollbar-by-iamjoel-in-https-github-com-langgenius|chore: handle workspace apps scrollbar]] · Change

**2023-08**

- 2023-08-14 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2023-08-14-add-ruby-s-sdk-implement-code-by-benjaminx-in-https-github-com-langgenius-dify-p|Add Ruby's SDK implement code]] · Change
- 2023-08-10 · <span class="tl-product tl-p18">**Ollama**</span> · [[Changes/Ollama/2023-08-10-ollama-langchain-integration-https-python-langchain-com-docs-integrations-llms-o|Ollama 🦜️🔗 LangChain…]] · Change

**2023-07**

- 2023-07-28 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-07-28-more-robust-extension-handling-you-can-now-use-pre-release-extensions-again|More robust extension handling]] · Change
- 2023-07-18 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2023-07-18-feat-add-ruby-sdk-by-crazywoola-in-https-github-com-langgenius-dify-pull-583|Feat/add ruby sdk]] · Change
- 2023-07-14 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2023-07-14-chat-apps-can-be-embedded-into-webpages|Chat apps can be embedded into webpages 💻]] · Change
- 2023-07-12 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-07-12-install-docs-link-to-neovim-plugin-https-github-com-joshuavial-aider-nvim-by-jos|Install docs link to NeoVim plugin((source link)]] · Change
- 2023-07-07 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-07-07-improved-the-add-new-doc-experience|Improved the "@Add new doc" experience]] · Change
- 2023-07-07 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-07-07-makes-it-clearer-which-docs-are-being-looked-at-by-the-ai-c07254|Makes it clearer which docs are being looked at by the AI]] · Change
- 2023-07-07 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-07-07-importing-vs-code-extensions-now-takes-into-account-enabled-disabled|Importing VS Code extensions now takes into account enabled/disabled]] · Change
- 2023-07-03 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-07-03-also-cursor-s-ai-will-now-use-popular-documentation-to-improve-the-answers-to-yo|Also, Cursor's AI will now use popular documentation to improve the answers…]] · Change

**2023-06**

- 2023-06-27 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-06-27-cursor-deep-linking-works-now-so-you-should-be-able-to-log-in-to-extensions|cursor:// deep linking works now, so you should be able to log in to extensions]] · Change
- 2023-06-27 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-06-27-better-support-for-extensions-specifically-re-enables-the-welcomeview|Better support for extensions (specifically re-enables the welcomeView)]] · Change
- 2023-06-19 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2023-06-19-dataset-support-integration-with-notion|📃 Dataset support integration with Notion]] · Change
- 2023-06-16 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-06-16-we-ve-added-support-for-using-your-azure-openai-credentials-also-small-improveme|Azure Support]] · Change
- 2023-06-09 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2023-06-09-feat-npm-sdk-to-2-0-to-fix-steaming-problem-by-iamjoel-in-https-github-com-langg|feat: npm sdk to 2.0 to fix steaming problem]] · Change

**2023-05**

- 2023-05-25 · <span class="tl-product tl-p8">**Dify**</span> · [[Changes/Dify/2023-05-25-3-apps-and-integrations-changes-in-0-2-2|3 Apps and Integrations changes in 0.2.2]] · Digest
- 2023-05-12 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-05-12-plugins-try-a-new-version-of-chatgpt-that-knows-when-and-how-to-use-third-party|Plugins: Try a new version of ChatGPT that knows when and how to use third-party…]] · Change
- 2023-05-12 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-05-12-in-the-plugins-dropdown-click-plugin-store-to-install-and-enable-new-plugins|In the “Plugins” dropdown, click “Plugin Store” to install and enable new plugins]] · Change
- 2023-05-04 · <span class="tl-product tl-p7">**Cursor**</span> · [[Changes/Cursor/2023-05-04-one-click-extension-import-from-vs-code-beta-as-a-highly-requested-feature-we-re|One-Click Extension Import from VS Code (beta)]] · Change

</details>

</details>

</div>
<!-- chronolog:end -->