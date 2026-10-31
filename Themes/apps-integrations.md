---
created: '2023-03-23'
date: '2026-10-30'
description: 'Research question: how do the tracked products connect to outside tools,
  and in what unit do they package those connections?'
machine_hash: cd096380a295e9ed9221bf98ac90a957a468a39dc1ebccf2d00237645c42601e
modified: '2026-10-30'
products_involved:
- ChatGPT
- Claude Code
- Cursor
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

266 tracked changes across ChatGPT, Claude Code and Cursor · 2023-03-23 → 2026-10-30 · Claude Code averages 7.0 cards per release, Cursor 4.0, ChatGPT 1.7
<!-- chronolog:end -->

## Research summary
<!-- chronolog:begin region="narrative" -->
**Research question: how do the tracked products connect to outside tools, and in what unit do they package those connections?**

ChatGPT's [2023-03-23 plugins announcement](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#introducing-plugins-in-chatgpt) ([[Releases/ChatGPT/chatgpt-2023-03-23-introducing-plugins-in-chatgpt-8c6badc8|archived]]) introduces experimental plugins, tools designed for language models that access up-to-date information, run computations or use third-party services. The [2025-06-04 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#custom-connectors-via-model-context-protocol-pro-team-enterprise-edu) ([[Releases/ChatGPT/chatgpt-2025-06-04-custom-connectors-via-model-context-protocol-pro-team-enterprise-a1bc36f5|archived]]) lets admins and users build and deploy custom connectors to proprietary systems using the Model Context Protocol (MCP), and the [2025-12-18 app directory](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#introducing-the-app-directory-in-chatgpt) ([[Releases/ChatGPT/chatgpt-2025-12-18-introducing-the-app-directory-in-chatgpt-c4ab90ba|archived]]) lists connectors as apps. The [2026-07-09 Work announcement](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#introducing-chatgpt-work) ([[Releases/ChatGPT/chatgpt-2026-07-09-introducing-chatgpt-work-eff9f272|archived]]) replaces the App Directory with a Plugin Directory whose plugins package skills, apps and app templates, and the [2026-09-11 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#planned-custom-gpt-retirement-and-migration-to-plugins) ([[Releases/ChatGPT/chatgpt-2026-09-11-planned-custom-gpt-retirement-and-migration-to-plugins-05b21afb|archived]]) plans to retire custom GPTs, introduced on [2023-11-06](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#introducing-gpts) ([[Releases/ChatGPT/chatgpt-2023-11-06-introducing-gpts-3721c457|archived]]), with a migration path to plugins.

Cursor's [0.45 release on 2025-01-23](https://cursor.com/changelog/0-45-x) ([[Releases/Cursor/cursor-2025-01-23-0-45-x-https-cursor-com-changelog-0-45-x-c162d228|archived]]) adds MCP support, and [Cursor 1.0 on 2025-06-04](https://cursor.com/changelog/1-0) ([[Releases/Cursor/cursor-2025-06-04-1-0-https-cursor-com-changelog-1-0-237767ca|archived]]) adds one-click MCP setup with OAuth. The [2025-06-12 release](https://cursor.com/changelog/1-1) ([[Releases/Cursor/cursor-2025-06-12-1-1-https-cursor-com-changelog-1-1-0f0190fc|archived]]) lets teams launch Background Agents from Slack, where Cursor reads the whole thread before starting. The [2026-02-17 release](https://cursor.com/changelog/2-5) ([[Releases/Cursor/cursor-2026-02-17-2-5-https-cursor-com-changelog-2-5-82892320|archived]]) introduces plugins on the Cursor Marketplace, which package skills, subagents, MCP servers, hooks and rules into a single install, and the [2026-03-03 release](https://cursor.com/changelog/2-6) ([[Releases/Cursor/cursor-2026-03-03-2-6-https-cursor-com-changelog-2-6-0fa7f1a3|archived]]) adds MCP Apps with interactive interfaces such as Figma diagrams inside Cursor.

Claude Code's archive opens with a plugin marketplace in place: [v2.0.73 on 2025-12-19](https://github.com/anthropics/claude-code/releases/tag/v2.0.73) ([[Releases/Claude Code/claude-code-2025-12-19-v2-0-73-github-271620087-160adbe9|archived]]) adds search filtering to the plugin discover screen. [v2.1.16 on 2026-01-22](https://github.com/anthropics/claude-code/releases/tag/v2.1.16) ([[Releases/Claude Code/claude-code-2026-01-22-v2-1-16-github-279146529-0e5b3428|archived]]) adds native plugin management to the VS Code extension, [v2.1.198 on 2026-07-01](https://github.com/anthropics/claude-code/releases/tag/v2.1.198) ([[Releases/Claude Code/claude-code-2026-07-01-v2-1-198-github-347599701-9cec0dab|archived]]) makes Claude in Chrome generally available, and [v2.1.287 on 2026-10-01](https://github.com/anthropics/claude-code/releases/tag/v2.1.287) ([[Releases/Claude Code/claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87|archived]]) adds Claude Mods, through which plugins may modify deeper behavior.

**Uncertainty and scope:** the record covers the three tracked products only and Claude Code coverage starts on 2025-12-19, after its plugin system already existed, so shared words such as “plugin”, “app” and “connector” name each product's own packaging unit and do not indicate interoperable or equivalent integrations.
<!-- chronolog:end -->

## Key moments
<!-- chronolog:begin region="moments" -->
Auto-selected; edit `key_moments` in editorial.yaml to curate.

| Quarter | ChatGPT | Claude Code | Cursor |
| --- | --- | --- | --- |
| 2026 Q4 | · | · | 2026-10-13 [[Changes/Cursor/2026-10-13-apps-for-your-stack\|Apps for your stack]] |
| 2026 Q3 | 2026-08-28 [[Changes/ChatGPT/2026-08-28-you-can-now-connect-multiple-accounts-for-gmail-google-calendar-and-google-conta-b4c5da\|Connect multiple Google accounts to ChatGPT]]<br>2026-07-09 [[Changes/ChatGPT/2026-07-09-enterprise-and-edu-users-can-find-skills-under-plugins-in-the-sidebar-on-the-ski\|Skills are now generally available]] | 2026-09-17 [[Changes/Claude Code/2026-09-17-added-plugin-install-plugin-marketplace-source-which-offers-to-add-the-marketpla\|Added /plugin install plugin --marketplace source, which offers to add…]]<br>2026-09-11 [[Changes/Claude Code/2026-09-11-added-output-style-name-to-list-and-switch-output-styles-including-over-remote-c\|Added /output-style name to list and switch output styles, including over Remote…]]<br>2026-09-03 [[Changes/Claude Code/2026-09-03-added-reload-plugins-to-headless-sessions-so-it-appears-in-the-claude-code-deskt\|Added /reload-plugins to headless sessions, so it appears in the Claude Code…]]<br>2026-07-01 [[Changes/Claude Code/2026-07-01-claude-in-chrome-is-now-generally-available\|Claude in Chrome is now generally available]] | 2026-09-23 [[Changes/Cursor/2026-09-23-integrations\|Integrations]]<br>2026-08-17 [[Changes/Cursor/2026-08-17-app-extensions-for-cursor-repos\|App extensions for Cursor repos]]<br>2026-07-17 [[Changes/Cursor/2026-07-17-multi-repo-environment-support-4b706e\|Multi-repo environment support]] |
| 2026 Q2 | · | 2026-06-17 [[Changes/Claude Code/2026-06-17-added-config-key-value-syntax-to-set-any-setting-from-the-prompt-e-g-config-thin\|Added /config key=value syntax to set any setting from the prompt…]]<br>2026-06-04 [[Changes/Claude Code/2026-06-04-added-plugin-list-command-to-list-installed-plugins-with-enabled-disabled-filter\|Added /plugin list command to list installed plugins…]]<br>2026-05-11 [[Changes/Claude Code/2026-05-11-added-goal-command-set-a-completion-condition-and-claude-keeps-working-across-tu\|Added /goal command]] | 2026-06-22 [[Changes/Cursor/2026-06-22-plugin-canvases\|Plugin canvases]]<br>2026-05-19 [[Changes/Cursor/2026-05-19-cursor-is-now-available-in-jira\|Cursor is now available in Jira]]<br>2026-04-29 [[Changes/Cursor/2026-04-29-we-re-introducing-the-cursor-sdk-so-you-can-build-agents-with-the-same-runtime-h\|Cursor introduces the Cursor SDK so you can build agents with the same runtime…]]<br>2026-04-08 [[Changes/Cursor/2026-04-08-give-bugbot-access-to-mcp-servers-for-additional-context-during-code-reviews-on\|Bugbot MCP Support]] |
| 2026 Q1 | · | 2026-03-05 [[Changes/Claude Code/2026-03-05-added-reload-plugins-command-to-activate-pending-plugin-changes-without-restarti\|Added /reload-plugins command to activate pending plugin changes without restarting]] | 2026-03-03 [[Changes/Cursor/2026-03-03-mcp-apps-support-interactive-user-interfaces-like-charts-from-amplitude-diagrams\|MCP Apps]] |
| 2025 Q4 | 2025-12-18 [[Changes/ChatGPT/2025-12-18-you-can-now-browse-and-add-approved-apps-in-the-new-app-directory-apps-let-you-w\|Introducing the app directory in ChatGPT]] | · | · |
| 2025 Q3 | 2025-08-13 [[Changes/ChatGPT/2025-08-13-gmail-google-calendar-and-google-contacts-connectors-in-chatgpt-are-now-availabl-e34de4\|Gmail, Google Calendar, and Google Contacts Connectors in ChatGPT (Plus)]] | · | 2025-09-12 [[Changes/Cursor/2025-09-12-mcp-resources-support\|MCP Resources support]] |
| 2025 Q2 | 2025-05-15 [[Changes/ChatGPT/2025-05-15-the-github-connector-is-now-available-globally-to-plus-pro-team-users-including\|GitHub connector for deep research]] | · | 2025-06-12 [[Changes/Cursor/2025-06-12-agents-understand-context-6b73fc\|Agents understand context]] |
| 2024 Q1 | 2024-01-10 [[Changes/ChatGPT/2024-01-10-the-store-features-a-diverse-range-of-gpts-developed-by-our-partners-and-the-com-71db32\|Discover what’s trending in the GPT Store]] | · | · |
| 2023 Q4 | 2023-11-06 [[Changes/ChatGPT/2023-11-06-you-can-now-create-custom-versions-of-chatgpt-that-combine-instructions-extra-kn-5c0997\|Introducing GPTs]] | · | · |
| 2023 Q2 | 2023-05-24 [[Changes/ChatGPT/2023-05-24-browse-with-bing-we-ve-integrated-the-browsing-feature-currently-in-beta-for-pai\|Bing Plugin]] | · | 2023-05-17 [[Changes/Cursor/2023-05-17-you-can-pin-custom-extensions-to-your-activity-bar-in-the-top-left\|Activity Bar pinning]] |
| 2023 Q1 | 2023-03-23 [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581\|We are announcing experimental support for AI plugins in ChatGPT]] | · | · |
<!-- chronolog:end -->

<!-- chronolog:begin region="scope" -->
> [!info]- How to read this timeline
> Scope: tracked-products-only. Entries show same-theme chronology; they do not establish equivalent capabilities, adoption, or causation.
<!-- chronolog:end -->

## Timeline
<!-- chronolog:begin region="timeline" -->
### 2026 · 212 entries (ChatGPT 23 · Claude Code 156 · Cursor 33)

#### 2026-10

- 2026-10-30 · **Claude Code** · [[Changes/Claude Code/2026-10-30-3-apps-and-integrations-changes-in-v2-1-314|3 Apps and Integrations changes in v2.1.314]] · Digest
- 2026-10-27 · **Claude Code** · [[Changes/Claude Code/2026-10-27-2-apps-and-integrations-changes-in-v2-1-312|2 Apps and Integrations changes in v2.1.312]] · Digest
- 2026-10-26 · **Claude Code** · [[Changes/Claude Code/2026-10-26-3-apps-and-integrations-changes-in-v2-1-311|3 Apps and Integrations changes in v2.1.311]] · Digest
- 2026-10-23 · **Claude Code** · [[Changes/Claude Code/2026-10-23-2-apps-and-integrations-changes-in-v2-1-310|2 Apps and Integrations changes in v2.1.310]] · Digest
- 2026-10-22 · **Claude Code** · [[Changes/Claude Code/2026-10-22-2-apps-and-integrations-changes-in-v2-1-309|2 Apps and Integrations changes in v2.1.309]] · Digest
- 2026-10-21 · **Claude Code** · [[Changes/Claude Code/2026-10-21-3-apps-and-integrations-changes-in-v2-1-307|3 Apps and Integrations changes in v2.1.307]] · Digest
- 2026-10-20 · **Claude Code** · [[Changes/Claude Code/2026-10-20-3-apps-and-integrations-changes-in-v2-1-305|3 Apps and Integrations changes in v2.1.305]] · Digest
- 2026-10-19 · **Claude Code** · [[Changes/Claude Code/2026-10-19-8-apps-and-integrations-changes-in-v2-1-304|8 Apps and Integrations changes in v2.1.304]] · Digest
- 2026-10-16 · **ChatGPT** · [[Changes/ChatGPT/2026-10-16-improved-use-of-plugins-and-tools-to-carry-out-tasks|Improved use of plugins and tools to carry out tasks]]
- 2026-10-16 · **Claude Code** · [[Changes/Claude Code/2026-10-16-3-apps-and-integrations-changes-in-v2-1-302|3 Apps and Integrations changes in v2.1.302]] · Digest
- 2026-10-14 · **Claude Code** · [[Changes/Claude Code/2026-10-14-7-apps-and-integrations-changes-in-v2-1-300|7 Apps and Integrations changes in v2.1.300]] · Digest
- 2026-10-14 · **Claude Code** · [[Changes/Claude Code/2026-10-14-19-apps-and-integrations-changes-in-v2-1-299|19 Apps and Integrations changes in v2.1.299]] · Digest
- 2026-10-13 · **Cursor** · [[Changes/Cursor/2026-10-13-2-apps-and-integrations-changes-in-origin-app-marketplace|2 Apps and Integrations changes in Origin App Marketplace]] · Digest
- 2026-10-13 · **Cursor** · [[Changes/Cursor/2026-10-13-apps-for-your-stack|Apps for your stack]] · Launch
- 2026-10-09 · **Claude Code** · [[Changes/Claude Code/2026-10-09-3-apps-and-integrations-changes-in-v2-1-296|3 Apps and Integrations changes in v2.1.296]] · Digest
- 2026-10-08 · **Claude Code** · [[Changes/Claude Code/2026-10-08-improved-how-prompt-hooks-on-stop-and-subagentstop-written-as-instructions-such|Improved how prompt hooks on Stop and SubagentStop written as instructions…]]
- 2026-10-08 · **Claude Code** · [[Changes/Claude Code/2026-10-08-14-apps-and-integrations-changes-in-v2-1-295|14 Apps and Integrations changes in v2.1.295]] · Digest
- 2026-10-07 · **Claude Code** · [[Changes/Claude Code/2026-10-07-3-apps-and-integrations-changes-in-v2-1-293|3 Apps and Integrations changes in v2.1.293]] · Digest
- 2026-10-06 · **Claude Code** · [[Changes/Claude Code/2026-10-06-9-apps-and-integrations-changes-in-v2-1-292|9 Apps and Integrations changes in v2.1.292]] · Digest
- 2026-10-05 · **Claude Code** · [[Changes/Claude Code/2026-10-05-14-apps-and-integrations-changes-in-v2-1-290|14 Apps and Integrations changes in v2.1.290]] · Digest
- 2026-10-03 · **Claude Code** · [[Changes/Claude Code/2026-10-03-2-apps-and-integrations-changes-in-v2-1-289|2 Apps and Integrations changes in v2.1.289]] · Digest
- 2026-10-02 · **Claude Code** · [[Changes/Claude Code/2026-10-02-5-apps-and-integrations-changes-in-v2-1-288|5 Apps and Integrations changes in v2.1.288]] · Digest
- 2026-10-01 · **Claude Code** · [[Changes/Claude Code/2026-10-01-11-apps-and-integrations-changes-in-v2-1-287|11 Apps and Integrations changes in v2.1.287]] · Digest

#### 2026-09

- 2026-09-30 · **Claude Code** · [[Changes/Claude Code/2026-09-30-11-apps-and-integrations-changes-in-v2-1-286|11 Apps and Integrations changes in v2.1.286]] · Digest
- 2026-09-29 · **ChatGPT** · [[Changes/ChatGPT/2026-09-29-plugins-can-now-include-interactive-panels-sidebar-views-and-viewers-or-editors-d0bd7e|Work with interactive plugin extensions]]
- 2026-09-29 · **ChatGPT** · [[Changes/ChatGPT/2026-09-29-we-re-making-it-easier-to-bring-meeting-context-into-chatgpt-so-you-can-act-on-n|We’re making it easier to bring meeting context into ChatGPT so you can act on next…]]
- 2026-09-29 · **ChatGPT** · [[Changes/ChatGPT/2026-09-29-supported-plugins-can-use-mcp-events-to-start-an-automation-when-something-chang-d9add6|Start automations from connected-app events]]
- 2026-09-29 · **Claude Code** · [[Changes/Claude Code/2026-09-29-14-apps-and-integrations-changes-in-v2-1-285|14 Apps and Integrations changes in v2.1.285]] · Digest
- 2026-09-28 · **Claude Code** · [[Changes/Claude Code/2026-09-28-9-apps-and-integrations-changes-in-v2-1-284|9 Apps and Integrations changes in v2.1.284]] · Digest
- 2026-09-25 · **Claude Code** · [[Changes/Claude Code/2026-09-25-14-apps-and-integrations-changes-in-v2-1-283|14 Apps and Integrations changes in v2.1.283]] · Digest
- 2026-09-24 · **Claude Code** · [[Changes/Claude Code/2026-09-24-8-apps-and-integrations-changes-in-v2-1-282|8 Apps and Integrations changes in v2.1.282]] · Digest
- 2026-09-23 · **Claude Code** · [[Changes/Claude Code/2026-09-23-18-apps-and-integrations-changes-in-v2-1-281|18 Apps and Integrations changes in v2.1.281]] · Digest
- 2026-09-23 · **Cursor** · [[Changes/Cursor/2026-09-23-integrations|Integrations]] · Launch
- 2026-09-22 · **Claude Code** · [[Changes/Claude Code/2026-09-22-8-apps-and-integrations-changes-in-v2-1-280|8 Apps and Integrations changes in v2.1.280]] · Digest
- 2026-09-18 · **Claude Code** · [[Changes/Claude Code/2026-09-18-6-apps-and-integrations-changes-in-v2-1-277|6 Apps and Integrations changes in v2.1.277]] · Digest
- 2026-09-17 · **Claude Code** · [[Changes/Claude Code/2026-09-17-10-apps-and-integrations-changes-in-v2-1-274|10 Apps and Integrations changes in v2.1.274]] · Digest
- 2026-09-17 · **Claude Code** · [[Changes/Claude Code/2026-09-17-6-apps-and-integrations-changes-in-v2-1-275|6 Apps and Integrations changes in v2.1.275]] · Digest
- 2026-09-17 · **Claude Code** · [[Changes/Claude Code/2026-09-17-added-plugin-install-plugin-marketplace-source-which-offers-to-add-the-marketpla|Added /plugin install plugin --marketplace source, which offers to add…]]
- 2026-09-15 · **Claude Code** · [[Changes/Claude Code/2026-09-15-3-apps-and-integrations-changes-in-v2-1-273|3 Apps and Integrations changes in v2.1.273]] · Digest
- 2026-09-14 · **ChatGPT** · [[Changes/ChatGPT/2026-09-14-for-new-health-plugin-connections-chatgpt-will-now-default-to-each-user-s-global|For new Health plugin connections, ChatGPT will now default to each user’s global…]]
- 2026-09-14 · **ChatGPT** · [[Changes/ChatGPT/2026-09-14-you-can-change-your-health-permissions-anytime-in-settings-plugins-health-learn|You can change your Health permissions anytime in Settings → Plugins → Health]]
- 2026-09-14 · **Claude Code** · [[Changes/Claude Code/2026-09-14-5-apps-and-integrations-changes-in-v2-1-271|5 Apps and Integrations changes in v2.1.271]] · Digest
- 2026-09-11 · **ChatGPT** · [[Changes/ChatGPT/2026-09-11-we-re-planning-to-retire-custom-gpts-across-chatgpt-plans-and-provide-a-migratio|Planned custom GPT retirement and migration to plugins]] · Policy
- 2026-09-11 · **Claude Code** · [[Changes/Claude Code/2026-09-11-5-apps-and-integrations-changes-in-v2-1-269|5 Apps and Integrations changes in v2.1.269]] · Digest
- 2026-09-11 · **Claude Code** · [[Changes/Claude Code/2026-09-11-added-output-style-name-to-list-and-switch-output-styles-including-over-remote-c|Added /output-style name to list and switch output styles, including over Remote…]]
- 2026-09-10 · **ChatGPT** · [[Changes/ChatGPT/2026-09-10-the-data-plugin-helps-you-analyze-connected-business-data-in-chatgpt-work-and-co|Data plugin in ChatGPT Work and Codex]]
- 2026-09-10 · **Claude Code** · [[Changes/Claude Code/2026-09-10-7-apps-and-integrations-changes-in-v2-1-268|7 Apps and Integrations changes in v2.1.268]] · Digest
- 2026-09-09 · **Claude Code** · [[Changes/Claude Code/2026-09-09-claude-tag-added-a-use-a-custom-connector-link-to-the-preset-connection-forms-in|Claude Tag Added a "Use a custom connector" link to the preset connection forms…]]
- 2026-09-08 · **Claude Code** · [[Changes/Claude Code/2026-09-08-4-apps-and-integrations-changes-in-v2-1-265|4 Apps and Integrations changes in v2.1.265]] · Digest
- 2026-09-04 · **Claude Code** · [[Changes/Claude Code/2026-09-04-vscode-added-an-add-server-form-and-a-remove-action-to-the-mcp-servers-dialog-so|VSCode Added an Add server form and a Remove action to the MCP servers dialog…]]
- 2026-09-03 · **ChatGPT** · [[Changes/ChatGPT/2026-09-03-today-we-added-the-zendesk-and-onenote-plugins-in-the-plugin-directory-the-zende-012cbd|Zendesk & OneNote Plugins in ChatGPT and Codex Beta]]
- 2026-09-03 · **Claude Code** · [[Changes/Claude Code/2026-09-03-4-apps-and-integrations-changes-in-v2-1-260|4 Apps and Integrations changes in v2.1.260]] · Digest
- 2026-09-03 · **Claude Code** · [[Changes/Claude Code/2026-09-03-added-reload-plugins-to-headless-sessions-so-it-appears-in-the-claude-code-deskt|Added /reload-plugins to headless sessions, so it appears in the Claude Code…]]
- 2026-09-02 · **Claude Code** · [[Changes/Claude Code/2026-09-02-5-apps-and-integrations-changes-in-v2-1-259|5 Apps and Integrations changes in v2.1.259]] · Digest
- 2026-09-01 · **ChatGPT** · [[Changes/ChatGPT/2026-09-01-eligible-chatgpt-for-clinicians-users-in-the-united-states-can-now-use-healthcar|Healthcare Public Data in ChatGPT for Clinicians]]
- 2026-09-01 · **Claude Code** · [[Changes/Claude Code/2026-09-01-2-apps-and-integrations-changes-in-v2-1-257|2 Apps and Integrations changes in v2.1.257]] · Digest

#### 2026-08

- 2026-08-28 · **ChatGPT** · [[Changes/ChatGPT/2026-08-28-you-can-now-connect-multiple-accounts-for-gmail-google-calendar-and-google-conta-b4c5da|Connect multiple Google accounts to ChatGPT]]
- 2026-08-28 · **Claude Code** · [[Changes/Claude Code/2026-08-28-4-apps-and-integrations-changes-in-v2-1-251|4 Apps and Integrations changes in v2.1.251]] · Digest
- 2026-08-27 · **Claude Code** · [[Changes/Claude Code/2026-08-27-improved-managed-settings-client-side-timeout-mcp-startup-mode-and-stream-watchd|Improved managed settings]]
- 2026-08-26 · **Claude Code** · [[Changes/Claude Code/2026-08-26-2-apps-and-integrations-changes-in-v2-1-247|2 Apps and Integrations changes in v2.1.247]] · Digest
- 2026-08-25 · **Claude Code** · [[Changes/Claude Code/2026-08-25-3-apps-and-integrations-changes-in-v2-1-246|3 Apps and Integrations changes in v2.1.246]] · Digest
- 2026-08-21 · **ChatGPT** · [[Changes/ChatGPT/2026-08-21-updated-plugin-recommendations-make-it-easier-to-find-tools-people-continue-to-u|Updated plugin recommendations make it easier to find tools people continue to use]]
- 2026-08-21 · **ChatGPT** · [[Changes/ChatGPT/2026-08-21-plugin-availability-depends-on-your-plan-region-and-workspace-settings-desktop-i|Plugin availability depends on your plan, region, and workspace settings]]
- 2026-08-21 · **Claude Code** · [[Changes/Claude Code/2026-08-21-2-apps-and-integrations-changes-in-v2-1-239|2 Apps and Integrations changes in v2.1.239]] · Digest
- 2026-08-20 · **ChatGPT** · [[Changes/ChatGPT/2026-08-20-use-apple-messages-from-codex-and-chatgpt-work-on-apple-silicon-macs-the-apple-m|Use Apple Messages from Codex and ChatGPT Work]]
- 2026-08-20 · **Claude Code** · [[Changes/Claude Code/2026-08-20-6-apps-and-integrations-changes-in-v2-1-238|6 Apps and Integrations changes in v2.1.238]] · Digest
- 2026-08-19 · **Claude Code** · [[Changes/Claude Code/2026-08-19-sigterm-in-print-sdk-mode-no-longer-records-an-interrupted-turn-or-synthetic-too|SIGTERM in print/SDK mode no longer records an interrupted turn or synthetic tool…]]
- 2026-08-17 · **Claude Code** · [[Changes/Claude Code/2026-08-17-2-apps-and-integrations-changes-in-v2-1-234|2 Apps and Integrations changes in v2.1.234]] · Digest
- 2026-08-17 · **Cursor** · [[Changes/Cursor/2026-08-17-app-extensions-for-cursor-repos|App extensions for Cursor repos]] · Launch
- 2026-08-17 · **Cursor** · [[Changes/Cursor/2026-08-17-settings|Settings]] · Launch
- 2026-08-14 · **Claude Code** · [[Changes/Claude Code/2026-08-14-2-apps-and-integrations-changes-in-v2-1-233|2 Apps and Integrations changes in v2.1.233]] · Digest
- 2026-08-13 · **Claude Code** · [[Changes/Claude Code/2026-08-13-4-apps-and-integrations-changes-in-v2-1-232|4 Apps and Integrations changes in v2.1.232]] · Digest
- 2026-08-12 · **Claude Code** · [[Changes/Claude Code/2026-08-12-3-apps-and-integrations-changes-in-v2-1-229|3 Apps and Integrations changes in v2.1.229]] · Digest
- 2026-08-11 · **Claude Code** · [[Changes/Claude Code/2026-08-11-2-apps-and-integrations-changes-in-v2-1-228|2 Apps and Integrations changes in v2.1.228]] · Digest
- 2026-08-08 · **Claude Code** · [[Changes/Claude Code/2026-08-08-3-apps-and-integrations-changes-in-v2-1-225|3 Apps and Integrations changes in v2.1.225]] · Digest
- 2026-08-07 · **Claude Code** · [[Changes/Claude Code/2026-08-07-3-apps-and-integrations-changes-in-v2-1-224|3 Apps and Integrations changes in v2.1.224]] · Digest
- 2026-08-04 · **ChatGPT** · [[Changes/ChatGPT/2026-08-04-three-new-plugins-for-chatgpt-work-and-codex-help-students-and-educators-work-wi-e7aee9|Three new plugins for ChatGPT Work and Codex help students and educators work…]]
- 2026-08-04 · **Claude Code** · [[Changes/Claude Code/2026-08-04-4-apps-and-integrations-changes-in-v2-1-221|4 Apps and Integrations changes in v2.1.221]] · Digest
- 2026-08-04 · **Claude Code** · [[Changes/Claude Code/2026-08-04-2-apps-and-integrations-changes-in-v2-1-222|2 Apps and Integrations changes in v2.1.222]] · Digest
- 2026-08-03 · **Cursor** · [[Changes/Cursor/2026-08-03-cursor-can-now-read-write-and-act-across-your-google-workspace|Google Workspace Plugins]]

#### 2026-07

- 2026-07-29 · **ChatGPT** · [[Changes/ChatGPT/2026-07-29-we-re-beginning-to-roll-out-sign-in-with-chatgpt-across-select-plugins-and-partn|Sign in with ChatGPT]]
- 2026-07-28 · **Cursor** · [[Changes/Cursor/2026-07-28-plugins-mcp-servers-hooks-and-skills-to-extend-cursor-across-your-workflows|Plugins, MCP servers, hooks, and skills to extend Cursor across your workflows]]
- 2026-07-24 · **Claude Code** · [[Changes/Claude Code/2026-07-24-5-apps-and-integrations-changes-in-v2-1-219|5 Apps and Integrations changes in v2.1.219]] · Digest
- 2026-07-22 · **Claude Code** · [[Changes/Claude Code/2026-07-22-3-apps-and-integrations-changes-in-v2-1-218|3 Apps and Integrations changes in v2.1.218]] · Digest
- 2026-07-21 · **Claude Code** · [[Changes/Claude Code/2026-07-21-capped-the-frontend-design-plugin-suggestion-tip-at-3-lifetime-impressions-inste|Capped the frontend-design plugin suggestion tip at 3 lifetime impressions instead…]]
- 2026-07-20 · **Claude Code** · [[Changes/Claude Code/2026-07-20-background-sessions-mcp-and-install-github-app-now-park-a-needs-input-request-in|Background sessions: /mcp and /install-github-app now park…]]
- 2026-07-18 · **Claude Code** · [[Changes/Claude Code/2026-07-18-changed-sessionstart-hooks-to-report-source-fork-when-a-session-begins-as-a-fork|Changed SessionStart hooks to report source "fork" when a session begins as a fork…]]
- 2026-07-17 · **Claude Code** · [[Changes/Claude Code/2026-07-17-2-apps-and-integrations-changes-in-v2-1-212|2 Apps and Integrations changes in v2.1.212]] · Digest
- 2026-07-17 · **Cursor** · [[Changes/Cursor/2026-07-17-cursor-in-slack-now-shares-a-plan-before-it-starts-runs-in-multi-repo-environmen|Cursor in Slack now shares a plan before it starts, runs in multi-repo environments…]]
- 2026-07-17 · **Cursor** · [[Changes/Cursor/2026-07-17-multi-repo-environment-support-4b706e|Multi-repo environment support]] · Launch
- 2026-07-15 · **Claude Code** · [[Changes/Claude Code/2026-07-15-2-apps-and-integrations-changes-in-v2-1-211|2 Apps and Integrations changes in v2.1.211]] · Digest
- 2026-07-14 · **Claude Code** · [[Changes/Claude Code/2026-07-14-3-apps-and-integrations-changes-in-v2-1-208|3 Apps and Integrations changes in v2.1.208]] · Digest
- 2026-07-11 · **Claude Code** · [[Changes/Claude Code/2026-07-11-2-apps-and-integrations-changes-in-v2-1-207|2 Apps and Integrations changes in v2.1.207]] · Digest
- 2026-07-09 · **ChatGPT** · [[Changes/ChatGPT/2026-07-09-we-re-also-replacing-the-app-directory-with-the-plugin-directory-existing-app-co|We’re also replacing the App Directory with the Plugin Directory]]
- 2026-07-09 · **ChatGPT** · [[Changes/ChatGPT/2026-07-09-enterprise-and-edu-users-can-find-skills-under-plugins-in-the-sidebar-on-the-ski|Skills are now generally available]] · Launch
- 2026-07-08 · **Claude Code** · [[Changes/Claude Code/2026-07-08-reserved-the-claude-browser-mcp-server-name-alongside-claude-preview-ahead-of-th|Reserved the "Claude Browser" MCP server name (alongside "Claude Preview") ahead…]]
- 2026-07-07 · **Claude Code** · [[Changes/Claude Code/2026-07-07-2-apps-and-integrations-changes-in-v2-1-203|2 Apps and Integrations changes in v2.1.203]] · Digest
- 2026-07-06 · **Claude Code** · [[Changes/Claude Code/2026-07-06-improved-mcp-error-messages-clearer-error-when-a-server-config-has-url-but-no-ty|Improved MCP error messages]]
- 2026-07-02 · **Claude Code** · [[Changes/Claude Code/2026-07-02-stacked-slash-skill-invocations-like-skill-a-skill-b-do-xyz-now-load-all-leading|Stacked slash-skill invocations like /skill-a /skill-b do XYZ now load all leading…]]
- 2026-07-01 · **Claude Code** · [[Changes/Claude Code/2026-07-01-claude-in-chrome-is-now-generally-available|Claude in Chrome is now generally available]] · Launch
- 2026-07-01 · **Claude Code** · [[Changes/Claude Code/2026-07-01-added-dataviz-skill-for-chart-and-dashboard-design-guidance-with-a-runnable-colo|Added /dataviz skill for chart and dashboard design guidance with a runnable…]]

#### 2026-06

- 2026-06-29 · **Claude Code** · [[Changes/Claude Code/2026-06-29-remote-control-is-now-disabled-when-anthropic-base-url-points-at-a-non-anthropic|Remote Control is now disabled when ANTHROPIC_BASE_URL points at a non-Anthropic…]]
- 2026-06-25 · **Claude Code** · [[Changes/Claude Code/2026-06-25-2-apps-and-integrations-changes-in-v2-1-193|2 Apps and Integrations changes in v2.1.193]] · Digest
- 2026-06-24 · **Claude Code** · [[Changes/Claude Code/2026-06-24-2-apps-and-integrations-changes-in-v2-1-191|2 Apps and Integrations changes in v2.1.191]] · Digest
- 2026-06-23 · **Claude Code** · [[Changes/Claude Code/2026-06-23-2-apps-and-integrations-changes-in-v2-1-187|2 Apps and Integrations changes in v2.1.187]] · Digest
- 2026-06-22 · **Claude Code** · [[Changes/Claude Code/2026-06-22-2-apps-and-integrations-changes-in-v2-1-186|2 Apps and Integrations changes in v2.1.186]] · Digest
- 2026-06-22 · **Cursor** · [[Changes/Cursor/2026-06-22-plugins-skills-and-mcps-let-you-customize-cursor-for-your-workflows-the-new-cust-241c4b|Plugins, skills, and MCPs let you customize Cursor for your workflows]]
- 2026-06-22 · **Cursor** · [[Changes/Cursor/2026-06-22-plugin-canvases|Plugin canvases]] · Launch
- 2026-06-19 · **Claude Code** · [[Changes/Claude Code/2026-06-19-added-attribution-sessionurl-setting-to-omit-the-claude-ai-session-link-from-com|Added attribution.sessionUrl setting to omit the claude.ai session link…]]
- 2026-06-17 · **ChatGPT** · [[Changes/ChatGPT/2026-06-17-monitoring-tasks-can-search-the-web-and-check-connected-apps-for-changes-and-not|Monitoring tasks can search the web and check connected apps for changes and notify…]]
- 2026-06-17 · **Claude Code** · [[Changes/Claude Code/2026-06-17-added-config-key-value-syntax-to-set-any-setting-from-the-prompt-e-g-config-thin|Added /config key=value syntax to set any setting from the prompt…]]
- 2026-06-16 · **Claude Code** · [[Changes/Claude Code/2026-06-16-improved-plugin-loading-performance-in-remote-sessions|Improved plugin loading performance in remote sessions]]
- 2026-06-15 · **Claude Code** · [[Changes/Claude Code/2026-06-15-2-apps-and-integrations-changes-in-v2-1-178|2 Apps and Integrations changes in v2.1.178]] · Digest
- 2026-06-10 · **Claude Code** · [[Changes/Claude Code/2026-06-10-3-apps-and-integrations-changes-in-v2-1-172|3 Apps and Integrations changes in v2.1.172]] · Digest
- 2026-06-06 · **Claude Code** · [[Changes/Claude Code/2026-06-06-added-glob-pattern-support-in-deny-rule-tool-name-position-denies-all-tools-allo|Added glob pattern support in deny rule tool-name position ("" denies all tools)]]
- 2026-06-04 · **Claude Code** · [[Changes/Claude Code/2026-06-04-2-apps-and-integrations-changes-in-v2-1-163|2 Apps and Integrations changes in v2.1.163]] · Digest
- 2026-06-04 · **Claude Code** · [[Changes/Claude Code/2026-06-04-added-plugin-list-command-to-list-installed-plugins-with-enabled-disabled-filter|Added /plugin list command to list installed plugins…]]
- 2026-06-04 · **Cursor** · [[Changes/Cursor/2026-06-04-we-ve-shipped-a-batch-of-new-functionality-across-the-typescript-and-python-sdks|We've shipped a batch of new functionality across the TypeScript and Python SDKs]]
- 2026-06-04 · **Cursor** · [[Changes/Cursor/2026-06-04-2-apps-and-integrations-changes-in-custom-stores-custom-tools|2 Apps and Integrations changes in Custom stores, custom tools…]] · Digest
- 2026-06-03 · **Claude Code** · [[Changes/Claude Code/2026-06-03-remote-control-now-shows-as-a-persistent-footer-pill-with-a-link-to-the-session|Remote Control now shows as a persistent footer pill (with a link to the session)…]]
- 2026-06-02 · **Claude Code** · [[Changes/Claude Code/2026-06-02-mcp-now-collapses-claude-ai-connectors-you-ve-never-signed-in-to-behind-a-show-u|/mcp now collapses claude.ai connectors you've never signed in to behind…]]
- 2026-06-02 · **Claude Code** · [[Changes/Claude Code/2026-06-02-removed-the-jetbrains-plugin-install-suggestion-from-startup|Removed the JetBrains plugin install suggestion from startup]]

#### 2026-05

- 2026-05-29 · **Claude Code** · [[Changes/Claude Code/2026-05-29-4-apps-and-integrations-changes-in-v2-1-157|4 Apps and Integrations changes in v2.1.157]] · Digest
- 2026-05-28 · **Claude Code** · [[Changes/Claude Code/2026-05-28-2-apps-and-integrations-changes-in-v2-1-153|2 Apps and Integrations changes in v2.1.153]] · Digest
- 2026-05-28 · **Claude Code** · [[Changes/Claude Code/2026-05-28-4-apps-and-integrations-changes-in-v2-1-154|4 Apps and Integrations changes in v2.1.154]] · Digest
- 2026-05-27 · **Claude Code** · [[Changes/Claude Code/2026-05-27-4-apps-and-integrations-changes-in-v2-1-152|4 Apps and Integrations changes in v2.1.152]] · Digest
- 2026-05-22 · **Claude Code** · [[Changes/Claude Code/2026-05-22-2-apps-and-integrations-changes-in-v2-1-149|2 Apps and Integrations changes in v2.1.149]] · Digest
- 2026-05-19 · **Claude Code** · [[Changes/Claude Code/2026-05-19-plugin-discover-and-browse-screens-now-show-a-plugin-s-commands-agents-skills-ho|/plugin Discover and Browse screens now show a plugin's commands, agents, skills…]]
- 2026-05-19 · **Claude Code** · [[Changes/Claude Code/2026-05-19-3-apps-and-integrations-changes-in-v2-1-144|3 Apps and Integrations changes in v2.1.144]] · Digest
- 2026-05-19 · **Cursor** · [[Changes/Cursor/2026-05-19-cursor-is-now-available-in-jira|Cursor is now available in Jira]] · Launch
- 2026-05-19 · **Cursor** · [[Changes/Cursor/2026-05-19-install-the-integration-from-cursor-integrations-you-need-cursor-admin-access-an|Install the integration from Cursor integrations]]
- 2026-05-15 · **Claude Code** · [[Changes/Claude Code/2026-05-15-3-apps-and-integrations-changes-in-v2-1-143|3 Apps and Integrations changes in v2.1.143]] · Digest
- 2026-05-14 · **Claude Code** · [[Changes/Claude Code/2026-05-14-3-apps-and-integrations-changes-in-v2-1-142|3 Apps and Integrations changes in v2.1.142]] · Digest
- 2026-05-13 · **Claude Code** · [[Changes/Claude Code/2026-05-13-2-apps-and-integrations-changes-in-v2-1-141|2 Apps and Integrations changes in v2.1.141]] · Digest
- 2026-05-13 · **Cursor** · [[Changes/Cursor/2026-05-13-improved-mcp-auth-token-lifecycle-handling|Improved MCP auth token lifecycle handling]]
- 2026-05-12 · **Claude Code** · [[Changes/Claude Code/2026-05-12-plugins-now-warn-when-a-default-component-folder-e-g-commands-is-silently-ignore|Plugins now warn when a default component folder (e.g. commands/) is silently…]]
- 2026-05-11 · **Claude Code** · [[Changes/Claude Code/2026-05-11-added-goal-command-set-a-completion-condition-and-claude-keeps-working-across-tu|Added /goal command]]
- 2026-05-11 · **Claude Code** · [[Changes/Claude Code/2026-05-11-8-apps-and-integrations-changes-in-v2-1-139|8 Apps and Integrations changes in v2.1.139]] · Digest
- 2026-05-11 · **Cursor** · [[Changes/Cursor/2026-05-11-get-started-by-installing-the-integration-in-the-cursor-dashboard-learn-more-in|Get started by installing the integration in the Cursor dashboard]]
- 2026-05-08 · **Claude Code** · [[Changes/Claude Code/2026-05-08-changed-plugin-marketplace-removal-key-to-d-matching-delete-elsewhere-instead-of|Changed plugin marketplace removal key to d (matching delete elsewhere) instead…]]
- 2026-05-07 · **Claude Code** · [[Changes/Claude Code/2026-05-07-2-apps-and-integrations-changes-in-v2-1-133|2 Apps and Integrations changes in v2.1.133]] · Digest
- 2026-05-07 · **Cursor** · [[Changes/Cursor/2026-05-07-made-mcp-connection-behavior-more-predictable-and-added-explicit-stale-token-cle|Made MCP connection behavior more predictable, and added explicit stale token…]]
- 2026-05-06 · **Claude Code** · [[Changes/Claude Code/2026-05-06-added-claude-code-session-id-environment-variable-to-the-bash-tool-subprocess-en|Added CLAUDE_CODE_SESSION_ID environment variable to the Bash tool subprocess…]]
- 2026-05-06 · **Claude Code** · [[Changes/Claude Code/2026-05-06-3-apps-and-integrations-changes-in-v2-1-129|3 Apps and Integrations changes in v2.1.129]] · Digest
- 2026-05-04 · **Claude Code** · [[Changes/Claude Code/2026-05-04-6-apps-and-integrations-changes-in-v2-1-128|6 Apps and Integrations changes in v2.1.128]] · Digest

#### 2026-04

- 2026-04-29 · **Cursor** · [[Changes/Cursor/2026-04-29-we-re-introducing-the-cursor-sdk-so-you-can-build-agents-with-the-same-runtime-h|Cursor introduces the Cursor SDK so you can build agents with the same runtime…]] · Launch
- 2026-04-29 · **Cursor** · [[Changes/Cursor/2026-04-29-run-npm-install-cursor-sdk-to-get-started-you-can-also-use-cursor-s-native-sdk-s-76fb76|Run npm install @cursor/sdk to get started]]
- 2026-04-28 · **Claude Code** · [[Changes/Claude Code/2026-04-28-2-apps-and-integrations-changes-in-v2-1-122|2 Apps and Integrations changes in v2.1.122]] · Digest
- 2026-04-28 · **Claude Code** · [[Changes/Claude Code/2026-04-28-6-apps-and-integrations-changes-in-v2-1-121|6 Apps and Integrations changes in v2.1.121]] · Digest
- 2026-04-23 · **Claude Code** · [[Changes/Claude Code/2026-04-23-3-apps-and-integrations-changes-in-v2-1-119|3 Apps and Integrations changes in v2.1.119]] · Digest
- 2026-04-23 · **Claude Code** · [[Changes/Claude Code/2026-04-23-5-apps-and-integrations-changes-in-v2-1-118|5 Apps and Integrations changes in v2.1.118]] · Digest
- 2026-04-22 · **Claude Code** · [[Changes/Claude Code/2026-04-22-4-apps-and-integrations-changes-in-v2-1-117|4 Apps and Integrations changes in v2.1.117]] · Digest
- 2026-04-20 · **Claude Code** · [[Changes/Claude Code/2026-04-20-2-apps-and-integrations-changes-in-v2-1-116|2 Apps and Integrations changes in v2.1.116]] · Digest
- 2026-04-16 · **Claude Code** · [[Changes/Claude Code/2026-04-16-2-apps-and-integrations-changes-in-v2-1-111|2 Apps and Integrations changes in v2.1.111]] · Digest
- 2026-04-15 · **Claude Code** · [[Changes/Claude Code/2026-04-15-4-apps-and-integrations-changes-in-v2-1-110|4 Apps and Integrations changes in v2.1.110]] · Digest
- 2026-04-13 · **Claude Code** · [[Changes/Claude Code/2026-04-13-3-apps-and-integrations-changes-in-v2-1-105|3 Apps and Integrations changes in v2.1.105]] · Digest
- 2026-04-10 · **Claude Code** · [[Changes/Claude Code/2026-04-10-4-apps-and-integrations-changes-in-v2-1-101|4 Apps and Integrations changes in v2.1.101]] · Digest
- 2026-04-09 · **Claude Code** · [[Changes/Claude Code/2026-04-09-2-apps-and-integrations-changes-in-v2-1-98|2 Apps and Integrations changes in v2.1.98]] · Digest
- 2026-04-08 · **Cursor** · [[Changes/Cursor/2026-04-08-give-bugbot-access-to-mcp-servers-for-additional-context-during-code-reviews-on|Bugbot MCP Support]] · Launch
- 2026-04-08 · **Cursor** · [[Changes/Cursor/2026-04-08-this-release-introduces-updates-to-bugbot-including-the-ability-to-self-improve|Cursor introduces updates to Bugbot including the ability to self-improve in real…]] · Launch
- 2026-04-07 · **Claude Code** · [[Changes/Claude Code/2026-04-07-5-apps-and-integrations-changes-in-v2-1-94|5 Apps and Integrations changes in v2.1.94]] · Digest
- 2026-04-04 · **Claude Code** · [[Changes/Claude Code/2026-04-04-remote-control-session-names-now-use-your-hostname-as-the-default-prefix-e-g-myh|Remote Control session names now use your hostname as the default prefix…]]
- 2026-04-02 · **Claude Code** · [[Changes/Claude Code/2026-04-02-4-apps-and-integrations-changes-in-v2-1-91|4 Apps and Integrations changes in v2.1.91]] · Digest
- 2026-04-02 · **Cursor** · [[Changes/Cursor/2026-04-02-2-apps-and-integrations-changes-in-3-0|2 Apps and Integrations changes in 3.0]] · Digest
- 2026-04-01 · **Claude Code** · [[Changes/Claude Code/2026-04-01-3-apps-and-integrations-changes-in-v2-1-89|3 Apps and Integrations changes in v2.1.89]] · Digest
- 2026-04-01 · **Claude Code** · [[Changes/Claude Code/2026-04-01-2-apps-and-integrations-changes-in-v2-1-90|2 Apps and Integrations changes in v2.1.90]] · Digest

#### 2026-03

- 2026-03-27 · **ChatGPT** · [[Changes/ChatGPT/2026-03-27-we-re-rolling-out-updated-box-notion-linear-and-dropbox-apps-in-chatgpt-these-up-9f6ee9|Updated Box, Notion, Linear, and Dropbox apps]]
- 2026-03-27 · **Claude Code** · [[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|Reduced startup event-loop stalls when many claude.ai MCP connectors are configured…]]
- 2026-03-26 · **Claude Code** · [[Changes/Claude Code/2026-03-26-5-apps-and-integrations-changes-in-v2-1-84|5 Apps and Integrations changes in v2.1.84]] · Digest
- 2026-03-26 · **Claude Code** · [[Changes/Claude Code/2026-03-26-4-apps-and-integrations-changes-in-v2-1-85|4 Apps and Integrations changes in v2.1.85]] · Digest
- 2026-03-25 · **ChatGPT** · [[Changes/ChatGPT/2026-03-25-google-s-file-connectors-in-chatgpt-are-now-unified-under-google-drive-providing|Google Drive app unification]]
- 2026-03-25 · **Claude Code** · [[Changes/Claude Code/2026-03-25-6-apps-and-integrations-changes-in-v2-1-83|6 Apps and Integrations changes in v2.1.83]] · Digest
- 2026-03-20 · **Claude Code** · [[Changes/Claude Code/2026-03-20-3-apps-and-integrations-changes-in-v2-1-81|3 Apps and Integrations changes in v2.1.81]] · Digest
- 2026-03-19 · **Claude Code** · [[Changes/Claude Code/2026-03-19-4-apps-and-integrations-changes-in-v2-1-80|4 Apps and Integrations changes in v2.1.80]] · Digest
- 2026-03-18 · **Claude Code** · [[Changes/Claude Code/2026-03-18-2-apps-and-integrations-changes-in-v2-1-79|2 Apps and Integrations changes in v2.1.79]] · Digest
- 2026-03-17 · **Claude Code** · [[Changes/Claude Code/2026-03-17-3-apps-and-integrations-changes-in-v2-1-78|3 Apps and Integrations changes in v2.1.78]] · Digest
- 2026-03-17 · **Claude Code** · [[Changes/Claude Code/2026-03-17-2-apps-and-integrations-changes-in-v2-1-77|2 Apps and Integrations changes in v2.1.77]] · Digest
- 2026-03-14 · **Claude Code** · [[Changes/Claude Code/2026-03-14-4-apps-and-integrations-changes-in-v2-1-76|4 Apps and Integrations changes in v2.1.76]] · Digest
- 2026-03-12 · **Claude Code** · [[Changes/Claude Code/2026-03-12-changed-plugin-dir-so-local-dev-copies-now-override-installed-marketplace-plugin|Changed --plugin-dir so local dev copies now override installed marketplace…]]
- 2026-03-11 · **Cursor** · [[Changes/Cursor/2026-03-11-we-ve-added-more-than-30-new-plugins-from-partners-such-as-atlassian-datadog-git-901313|New Plugins on the Cursor Marketplace]]
- 2026-03-10 · **Claude Code** · [[Changes/Claude Code/2026-03-10-3-apps-and-integrations-changes-in-v2-1-72|3 Apps and Integrations changes in v2.1.72]] · Digest
- 2026-03-07 · **Claude Code** · [[Changes/Claude Code/2026-03-07-3-apps-and-integrations-changes-in-v2-1-71|3 Apps and Integrations changes in v2.1.71]] · Digest
- 2026-03-06 · **Claude Code** · [[Changes/Claude Code/2026-03-06-reduced-remote-control-poll-rate-to-once-per-10-minutes-while-connected-was-1-2s|Reduced Remote Control /poll rate to once per 10 minutes while connected…]]
- 2026-03-05 · **Claude Code** · [[Changes/Claude Code/2026-03-05-added-reload-plugins-command-to-activate-pending-plugin-changes-without-restarti|Added /reload-plugins command to activate pending plugin changes without restarting]]
- 2026-03-05 · **Claude Code** · [[Changes/Claude Code/2026-03-05-7-apps-and-integrations-changes-in-v2-1-69|7 Apps and Integrations changes in v2.1.69]] · Digest
- 2026-03-03 · **Cursor** · [[Changes/Cursor/2026-03-03-3-apps-and-integrations-changes-in-2-6|3 Apps and Integrations changes in 2.6]] · Digest
- 2026-03-03 · **Cursor** · [[Changes/Cursor/2026-03-03-mcp-apps-support-interactive-user-interfaces-like-charts-from-amplitude-diagrams|MCP Apps]] · Launch

#### 2026-02

- 2026-02-28 · **Claude Code** · [[Changes/Claude Code/2026-02-28-added-enable-claudeai-mcp-servers-false-env-var-to-opt-out-from-making-claude-ai|Added ENABLE_CLAUDEAI_MCP_SERVERS=false env var to opt out from making claude.ai…]]
- 2026-02-25 · **ChatGPT** · [[Changes/ChatGPT/2026-02-25-sources-from-apps-paste-a-link-to-a-slack-channel-or-google-drive-file-or-folder|Sources from apps]]
- 2026-02-25 · **Claude Code** · [[Changes/Claude Code/2026-02-25-expand-remote-control-to-more-users|Expand Remote Control to more users]]
- 2026-02-24 · **Claude Code** · [[Changes/Claude Code/2026-02-24-4-apps-and-integrations-changes-in-v2-1-51|4 Apps and Integrations changes in v2.1.51]] · Digest
- 2026-02-20 · **Claude Code** · [[Changes/Claude Code/2026-02-20-claude-code-simple-mode-now-also-disables-mcp-tools-attachments-hooks-and-claude|CLAUDE_CODE_SIMPLE mode now also disables MCP tools, attachments, hooks…]]
- 2026-02-19 · **ChatGPT** · [[Changes/ChatGPT/2026-02-19-preview-diagrams-and-mini-apps-directly-in-chat|Preview diagrams and mini apps directly in chat]]
- 2026-02-19 · **Claude Code** · [[Changes/Claude Code/2026-02-19-2-apps-and-integrations-changes-in-v2-1-49|2 Apps and Integrations changes in v2.1.49]] · Digest
- 2026-02-18 · **Claude Code** · [[Changes/Claude Code/2026-02-18-added-last-assistant-message-field-to-stop-and-subagentstop-hook-inputs-providin|Added last_assistant_message field to Stop and SubagentStop hook inputs, providing…]]
- 2026-02-18 · **Cursor** · [[Changes/Cursor/2026-02-18-3-apps-and-integrations-changes-in-cli-improvements-and-mermaid-ascii|3 Apps and Integrations changes in CLI Improvements and Mermaid ASCII…]] · Digest
- 2026-02-17 · **Claude Code** · [[Changes/Claude Code/2026-02-17-2-apps-and-integrations-changes-in-v2-1-45|2 Apps and Integrations changes in v2.1.45]] · Digest
- 2026-02-17 · **Cursor** · [[Changes/Cursor/2026-02-17-plugins-on-the-cursor-marketplace-0cef65|Plugins on the Cursor Marketplace]] · Launch
- 2026-02-06 · **Claude Code** · [[Changes/Claude Code/2026-02-06-added-plugin-name-to-skill-descriptions-and-skills-menu-for-better-discoverabili|Added plugin name to skill descriptions and /skills menu for better discoverability]]
- 2026-02-05 · **Claude Code** · [[Changes/Claude Code/2026-02-05-skills-defined-in-claude-skills-within-additional-directories-add-dir-are-now-lo|Skills defined in .claude/skills/ within additional directories (--add-dir)…]]

#### 2026-01

- 2026-01-30 · **Claude Code** · [[Changes/Claude Code/2026-01-30-vscode-enabled-claude-in-chrome-integration|VSCode: Enabled Claude in Chrome integration]]
- 2026-01-27 · **Claude Code** · [[Changes/Claude Code/2026-01-27-changed-the-commit-push-pr-skill-to-automatically-post-pr-urls-to-slack-channels|Changed the /commit-push-pr skill to automatically post PR URLs to Slack channels…]]
- 2026-01-23 · **Claude Code** · [[Changes/Claude Code/2026-01-23-2-apps-and-integrations-changes-in-v2-1-19|2 Apps and Integrations changes in v2.1.19]] · Digest
- 2026-01-22 · **Claude Code** · [[Changes/Claude Code/2026-01-22-vscode-added-native-plugin-management-support|VSCode Added native plugin management support]]
- 2026-01-22 · **Cursor** · [[Changes/Cursor/2026-01-22-4-apps-and-integrations-changes-in-2-4|4 Apps and Integrations changes in 2.4]] · Digest
- 2026-01-20 · **Claude Code** · [[Changes/Claude Code/2026-01-20-2-apps-and-integrations-changes-in-v2-1-14|2 Apps and Integrations changes in v2.1.14]] · Digest
- 2026-01-13 · **Claude Code** · [[Changes/Claude Code/2026-01-13-2-apps-and-integrations-changes-in-v2-1-6|2 Apps and Integrations changes in v2.1.6]] · Digest
- 2026-01-09 · **Claude Code** · [[Changes/Claude Code/2026-01-09-2-apps-and-integrations-changes-in-v2-1-2|2 Apps and Integrations changes in v2.1.2]] · Digest
- 2026-01-08 · **Cursor** · [[Changes/Cursor/2026-01-08-enable-and-disable-mcp-servers-on-the-fly-with-mcp-enable-and-mcp-disable-comman|Enabling MCP servers]] · Launch
- 2026-01-08 · **Cursor** · [[Changes/Cursor/2026-01-08-added-mcp-enable-mcp-disable-commands-to-manage-mcp-servers|Added /mcp enable, /mcp disable commands to manage MCP servers]]
- 2026-01-08 · **Cursor** · [[Changes/Cursor/2026-01-08-this-release-introduces-new-cli-controls-for-models-mcp-management-rules-and-com|Cursor introduces new CLI controls for models, MCP management, rules and commands…]] · Launch
- 2026-01-08 · **Cursor** · [[Changes/Cursor/2026-01-08-mcp-server-names-with-spaces-are-now-supported-in-all-mcp-commands|MCP server names with spaces are now supported in all /mcp commands]]

### 2025 · 27 entries (ChatGPT 10 · Claude Code 1 · Cursor 16)

#### 2025-12

- 2025-12-22 · **Cursor** · [[Changes/Cursor/2025-12-22-2-apps-and-integrations-changes-in-2-3|2 Apps and Integrations changes in 2.3]] · Digest
- 2025-12-19 · **Claude Code** · [[Changes/Claude Code/2025-12-19-2-apps-and-integrations-changes-in-v2-0-73|2 Apps and Integrations changes in v2.0.73]] · Digest
- 2025-12-18 · **ChatGPT** · [[Changes/ChatGPT/2025-12-18-you-can-now-browse-and-add-approved-apps-in-the-new-app-directory-apps-let-you-w|Introducing the app directory in ChatGPT]] · Launch
- 2025-12-10 · **Cursor** · [[Changes/Cursor/2025-12-10-system-notification-actions-for-terminal-and-mcp-approval-rejection|System notification actions for terminal and MCP approval/rejection]]

#### 2025-11

- 2025-11-21 · **Cursor** · [[Changes/Cursor/2025-11-21-project-level-hooks-are-now-supported|Project level hooks are now supported]]

#### 2025-10

- 2025-10-13 · **ChatGPT** · [[Changes/ChatGPT/2025-10-13-we-re-rolling-out-two-new-ways-to-bring-slack-and-chatgpt-together-a-connector-t-be2213|Slack connector and app]]
- 2025-10-09 · **ChatGPT** · [[Changes/ChatGPT/2025-10-09-we-re-adding-notion-and-linear-as-synced-connectors-for-pro-users-so-you-can-sec|Adding Notion & Linear synced connectors]]

#### 2025-09

- 2025-09-29 · **Cursor** · [[Changes/Cursor/2025-09-29-4-apps-and-integrations-changes-in-1-7|4 Apps and Integrations changes in 1.7]] · Digest
- 2025-09-12 · **Cursor** · [[Changes/Cursor/2025-09-12-2-apps-and-integrations-changes-in-1-6|2 Apps and Integrations changes in 1.6]] · Digest
- 2025-09-12 · **Cursor** · [[Changes/Cursor/2025-09-12-mcp-resources-support|MCP Resources support]] · Launch

#### 2025-08

- 2025-08-21 · **Cursor** · [[Changes/Cursor/2025-08-21-cursor-now-supports-mcp-elicitation-a-new-feature-in-the-mcp-spec-that-allows-se|Support for MCP elicitation]] · Launch
- 2025-08-13 · **ChatGPT** · [[Changes/ChatGPT/2025-08-13-gmail-google-calendar-and-google-contacts-connectors-in-chatgpt-are-now-availabl-e34de4|Gmail, Google Calendar, and Google Contacts Connectors in ChatGPT (Plus)]]

#### 2025-07

- 2025-07-29 · **Cursor** · [[Changes/Cursor/2025-07-29-extension-marketplace-supports-custom-urls|Extension marketplace supports custom URLs]]
- 2025-07-24 · **ChatGPT** · [[Changes/ChatGPT/2025-07-24-pro-users-can-now-utilize-chat-search-with-hubspot-and-custom-connectors-mcp-in-b9b682|Chat search for HubSpot and custom connectors (MCP) (Pro)]]
- 2025-07-03 · **Cursor** · [[Changes/Cursor/2025-07-03-2-apps-and-integrations-changes-in-1-2|2 Apps and Integrations changes in 1.2]] · Digest

#### 2025-06

- 2025-06-24 · **ChatGPT** · [[Changes/ChatGPT/2025-06-24-pro-users-are-now-able-to-use-chat-search-connectors-in-addition-to-deep-researc-9d5a85|Chat search connectors (Pro)]]
- 2025-06-12 · **Cursor** · [[Changes/Cursor/2025-06-12-agents-understand-context-6b73fc|Agents understand context]] · Launch
- 2025-06-04 · **ChatGPT** · [[Changes/ChatGPT/2025-06-04-supported-connectors-google-drive-sharepoint-dropbox-box-outlook-gmail-google-ca|Supported connectors: Google Drive, SharePoint, Dropbox, Box, Outlook, Gmail, Google…]]
- 2025-06-04 · **ChatGPT** · [[Changes/ChatGPT/2025-06-04-admin-published-connectors-appear-in-the-connector-list-for-all-users|Admin-published connectors appear in the connector list for all users]]
- 2025-06-04 · **ChatGPT** · [[Changes/ChatGPT/2025-06-04-admins-and-users-can-now-build-and-deploy-custom-connectors-to-proprietary-syste|Admins and users can now build and deploy custom connectors to proprietary systems…]]

#### 2025-05

- 2025-05-15 · **ChatGPT** · [[Changes/ChatGPT/2025-05-15-the-github-connector-is-now-available-globally-to-plus-pro-team-users-including|GitHub connector for deep research]]
- 2025-05-15 · **Cursor** · [[Changes/Cursor/2025-05-15-refreshed-inline-edit-cmd-ctrl-k-with-agent-integration|Refreshed Inline Edit (Cmd/Ctrl+K) with Agent integration]] · Launch

#### 2025-04

- 2025-04-15 · **Cursor** · [[Changes/Cursor/2025-04-15-images-in-mcp|Images in MCP]] · Launch

#### 2025-03

- 2025-03-23 · **Cursor** · [[Changes/Cursor/2025-03-23-3-apps-and-integrations-changes-in-0-48-x|3 Apps and Integrations changes in 0.48.x]] · Digest
- 2025-03-11 · **Cursor** · [[Changes/Cursor/2025-03-11-mcp-added-global-server-configuration-with-cursor-mcp-json-and-support-for-envir|MCP: Added global server configuration with ~/.cursor/mcp.json and support…]]

#### 2025-02

- 2025-02-19 · **Cursor** · [[Changes/Cursor/2025-02-19-2-apps-and-integrations-changes-in-0-46-x|2 Apps and Integrations changes in 0.46.x]] · Digest
- 2025-02-19 · **Cursor** · [[Changes/Cursor/2025-02-19-mcp-improvements|MCP improvements]]

### 2024 · 5 entries (ChatGPT 2 · Cursor 3)

#### 2024-07

- 2024-07-03 · **Cursor** · [[Changes/Cursor/2024-07-03-docs-management-go-to-cursor-settings-features-docs-to-re-index-your-docs|Docs management! Go to Cursor Settings  Features  Docs to re-index your docs]]

#### 2024-05

- 2024-05-16 · **ChatGPT** · [[Changes/ChatGPT/2024-05-16-upload-the-latest-file-versions-directly-from-google-drive-microsoft-onedrive-pe-70f6a3|Upload the latest file versions directly from Google Drive, Microsoft OneDrive…]]

#### 2024-01

- 2024-01-25 · **Cursor** · [[Changes/Cursor/2024-01-25-update-0-24-3-0-24-4-adds-ability-to-configure-openai-base-url-fixes-getcursor-c|UPDATE (0.24.3-0.24.4): Adds ability to configure OpenAI base URL, fixes…]]
- 2024-01-15 · **Cursor** · [[Changes/Cursor/2024-01-15-supports-newer-version-of-python-extension|Supports newer version of python extension]]
- 2024-01-10 · **ChatGPT** · [[Changes/ChatGPT/2024-01-10-the-store-features-a-diverse-range-of-gpts-developed-by-our-partners-and-the-com-71db32|Discover what’s trending in the GPT Store]] · Launch

### 2023 · 22 entries (ChatGPT 5 · Cursor 17)

#### 2023-12

- 2023-12-16 · **Cursor** · [[Changes/Cursor/2023-12-16-copilot-we-ve-continued-to-improve-the-copilot-ghost-text-experience-surprisingl|Copilot++: We've continued to improve the Copilot++ ghost text experience]]

#### 2023-11

- 2023-11-15 · **Cursor** · [[Changes/Cursor/2023-11-15-now-based-on-vs-code-1-84-2-notably-this-fixes-a-few-notebook-bugs-and-ensures-t|New upstream]]
- 2023-11-15 · **Cursor** · [[Changes/Cursor/2023-11-15-cursor-is-now-based-on-vs-code-1-84-2-notably-this-fixes-a-few-notebook-bugs-and|Cursor is now based on VS Code 1.84.2]]
- 2023-11-06 · **ChatGPT** · [[Changes/ChatGPT/2023-11-06-you-can-now-create-custom-versions-of-chatgpt-that-combine-instructions-extra-kn-5c0997|Introducing GPTs]] · Launch

#### 2023-10

- 2023-10-20 · **Cursor** · [[Changes/Cursor/2023-10-20-cursor-is-now-based-on-vs-code-1-83-1-this-ensures-that-the-newest-versions-of-a|Cursor is now based on VS Code 1.83.1]]

#### 2023-09

- 2023-09-17 · **Cursor** · [[Changes/Cursor/2023-09-17-we-point-to-a-different-marketplace-for-downloading-extensions-and-use-a-fork-of|Cursor Python and Cursor Marketplace]]
- 2023-09-11 · **Cursor** · [[Changes/Cursor/2023-09-11-we-serve-extensions-now-using-cursor-s-extension-marketplace|Cursor Marketplace]]

#### 2023-07

- 2023-07-28 · **Cursor** · [[Changes/Cursor/2023-07-28-more-robust-extension-handling-you-can-now-use-pre-release-extensions-again|More robust extension handling]]
- 2023-07-07 · **Cursor** · [[Changes/Cursor/2023-07-07-improved-the-add-new-doc-experience|Improved the "@Add new doc" experience]]
- 2023-07-07 · **Cursor** · [[Changes/Cursor/2023-07-07-makes-it-clearer-which-docs-are-being-looked-at-by-the-ai-c07254|Makes it clearer which docs are being looked at by the AI]]
- 2023-07-07 · **Cursor** · [[Changes/Cursor/2023-07-07-importing-vs-code-extensions-now-takes-into-account-enabled-disabled|Importing VS Code extensions now takes into account enabled/disabled]]
- 2023-07-03 · **Cursor** · [[Changes/Cursor/2023-07-03-also-cursor-s-ai-will-now-use-popular-documentation-to-improve-the-answers-to-yo|Also, Cursor's AI will now use popular documentation to improve the answers…]]

#### 2023-06

- 2023-06-27 · **Cursor** · [[Changes/Cursor/2023-06-27-cursor-deep-linking-works-now-so-you-should-be-able-to-log-in-to-extensions|cursor:// deep linking works now, so you should be able to log in to extensions]]
- 2023-06-27 · **Cursor** · [[Changes/Cursor/2023-06-27-better-support-for-extensions-specifically-re-enables-the-welcomeview|Better support for extensions (specifically re-enables the welcomeView)]]
- 2023-06-16 · **Cursor** · [[Changes/Cursor/2023-06-16-we-ve-added-support-for-using-your-azure-openai-credentials-also-small-improveme|Azure Support]]
- 2023-06-09 · **Cursor** · [[Changes/Cursor/2023-06-09-you-can-now-have-the-ai-read-documentation-on-your-behalf-this-will-improve-it-s|Show the AI documentation]]

#### 2023-05

- 2023-05-24 · **ChatGPT** · [[Changes/ChatGPT/2023-05-24-browse-with-bing-we-ve-integrated-the-browsing-feature-currently-in-beta-for-pai|Bing Plugin]] · Launch
- 2023-05-17 · **Cursor** · [[Changes/Cursor/2023-05-17-you-can-pin-custom-extensions-to-your-activity-bar-in-the-top-left|Activity Bar pinning]] · Launch
- 2023-05-12 · **ChatGPT** · [[Changes/ChatGPT/2023-05-12-plugins-try-a-new-version-of-chatgpt-that-knows-when-and-how-to-use-third-party|Plugins: Try a new version of ChatGPT that knows when and how to use third-party…]]
- 2023-05-12 · **ChatGPT** · [[Changes/ChatGPT/2023-05-12-in-the-plugins-dropdown-click-plugin-store-to-install-and-enable-new-plugins|In the “Plugins” dropdown, click “Plugin Store” to install and enable new plugins]]
- 2023-05-04 · **Cursor** · [[Changes/Cursor/2023-05-04-one-click-extension-import-from-vs-code-beta-as-a-highly-requested-feature-we-re|One-Click Extension Import from VS Code (beta)]]

#### 2023-03

- 2023-03-23 · **ChatGPT** · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]] · Launch
<!-- chronolog:end -->