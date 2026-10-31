---
created: '2023-01-09'
date: '2026-10-31'
description: 'Research question: how do the tracked products add, choose between and
  retire models?'
machine_hash: e930d8637d5fc505624e3a9b111ce782676d908d71b9c69a0b0deb092c30819e
modified: '2026-10-31'
products_involved:
- ChatGPT
- Claude Code
- Cursor
publication: active
status: official
tags:
- theme
- moc
theme: model-support
title: Model Support
---

<!-- chronolog:begin region="header" -->
# Model Support

229 tracked changes across ChatGPT, Claude Code and Cursor · 2023-01-09 → 2026-10-31 · Claude Code averages 7.0 cards per release, Cursor 4.0, ChatGPT 1.7
<!-- chronolog:end -->

## Research summary
<!-- chronolog:begin region="narrative" -->
**Research question: how do the tracked products add, choose between and retire models?**

ChatGPT's [2023-03-14 GPT-4 announcement](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#announcing-gpt-4-in-chatgpt) ([[Releases/ChatGPT/chatgpt-2023-03-14-announcing-gpt-4-in-chatgpt-43063370|archived]]) brings GPT-4 to Plus subscribers under a usage cap adjusted to demand. The [2025-08-07 GPT-5 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#gpt-5) ([[Releases/ChatGPT/chatgpt-2025-08-07-gpt-5-a50b91bc|archived]]) makes GPT-5 the default for all logged-in users as a single auto-switching system, with a model picker for paid tiers, and the [2025-08-12 update](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#gpt-5-updates) ([[Releases/ChatGPT/chatgpt-2025-08-12-gpt-5-updates-9aaeee46|archived]]) adds a choice between “Auto”, “Fast” and “Thinking”. Retirements arrive as dated notes: the [2026-02-13 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#retiring-gpt-4o-and-other-legacy-models) ([[Releases/ChatGPT/chatgpt-2026-02-13-retiring-gpt-4o-and-other-legacy-models-71b41b16|archived]]) retires GPT-4o, GPT-4.1, GPT-4.1 mini and OpenAI o4-mini from ChatGPT with no API change, and the [2026-09-14 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#changes-to-automatic-switching-to-thinking-in-chatgpt-plus-and-pro) ([[Releases/ChatGPT/chatgpt-2026-09-14-changes-to-automatic-switching-to-thinking-in-chatgpt-plus-and-p-54d16c58|archived]]) retires automatic switching from Instant to Thinking for Plus and Pro users, while ChatGPT can still switch automatically for safety purposes.

Cursor's [2023-03-30 release](https://cursor.com/changelog/0-1-12) ([[Releases/Cursor/cursor-2023-03-30-0-1-12-https-cursor-com-changelog-0-1-12-f3e1800c|archived]]) lets users plug in an OpenAI API key for unlimited requests at cost. The [2024-03-12 Claude support release](https://cursor.com/changelog/claude-support) ([[Releases/Cursor/cursor-2024-03-12-claude-support-https-cursor-com-changelog-claude-support-ed1eb90a|archived]]) lets Pro and Business users add claude-3-opus as a custom model, and the [2024-07-23 release](https://cursor.com/changelog/0-38-x) ([[Releases/Cursor/cursor-2024-07-23-0-38-x-https-cursor-com-changelog-0-38-x-e6d087df|archived]]) makes Claude 3.5 Sonnet the default model. [Cursor 2.0 on 2025-10-29](https://cursor.com/changelog/2-0) ([[Releases/Cursor/cursor-2025-10-29-2-0-https-cursor-com-changelog-2-0-66a8e76e|archived]]) introduces Composer, described as Cursor's first agentic coding model, and the [2026-07-22 release](https://cursor.com/changelog/router) ([[Releases/Cursor/cursor-2026-07-22-cursor-router-https-cursor-com-changelog-router-af8c2ac4|archived]]) adds Cursor Router, which sends each request to a frontier or a price-efficient model.

Claude Code announces models inside its releases: [v2.1.32 on 2026-02-05](https://github.com/anthropics/claude-code/releases/tag/v2.1.32) ([[Releases/Claude Code/claude-code-2026-02-05-v2-1-32-github-283457817-0910feb0|archived]]) makes Claude Opus 4.6 available, [v2.1.197 on 2026-06-30](https://github.com/anthropics/claude-code/releases/tag/v2.1.197) ([[Releases/Claude Code/claude-code-2026-06-30-v2-1-197-github-346856026-11e4aa1f|archived]]) makes Claude Sonnet 5 the default model with a native 1M-token context window, and [v2.1.280 on 2026-09-22](https://github.com/anthropics/claude-code/releases/tag/v2.1.280) ([[Releases/Claude Code/claude-code-2026-09-22-v2-1-280-github-393879189-1cf5db2b|archived]]) adds Claude Opus 5.5 as the default Opus model. Model controls grow alongside: [v2.1.76 on 2026-03-14](https://github.com/anthropics/claude-code/releases/tag/v2.1.76) ([[Releases/Claude Code/claude-code-2026-03-14-v2-1-76-github-296929324-94cd2ffc|archived]]) adds an `/effort` command, [v2.1.166 on 2026-06-06](https://github.com/anthropics/claude-code/releases/tag/v2.1.166) ([[Releases/Claude Code/claude-code-2026-06-06-v2-1-166-github-335118845-ef990727|archived]]) a `fallbackModel` setting with up to three fallback models, and [v2.1.196 on 2026-06-29](https://github.com/anthropics/claude-code/releases/tag/v2.1.196) ([[Releases/Claude Code/claude-code-2026-06-29-v2-1-196-github-346482381-e21be272|archived]]) organization default models set by admins.

**Uncertainty and scope:** the record covers the three tracked products only, Claude Code coverage starts on 2025-12-19, and announcement dates are not availability dates for every plan, region or provider, so a model's name, default status or price in one product says nothing about its quality or availability in another.
<!-- chronolog:end -->

## Key moments
<!-- chronolog:begin region="moments" -->
Selected automatically from launches and standalone announcements.

| Quarter | ChatGPT | Claude Code | Cursor |
| --- | --- | --- | --- |
| 2026 Q4 | 2026-10-07 [[Changes/ChatGPT/2026-10-07-we-re-introducing-gpt-6-with-intelligent-ui-in-chatgpt-chatgpt-can-now-combine-t\|GPT-6 and Intelligent UI in ChatGPT]] | · | · |
| 2026 Q3 | 2026-09-03 [[Changes/ChatGPT/2026-09-03-today-we-re-introducing-gpt-6-astra-with-improvements-in-coding-research-compute-069f67\|Introducing GPT-6 Astra]] | 2026-08-26 [[Changes/Claude Code/2026-08-26-added-claude-api-cost-optimize-to-profile-an-existing-project-s-claude-api-spend\|Added /claude-api cost-optimize to profile an existing project's Claude API spend…]] | 2026-07-22 [[Changes/Cursor/2026-07-22-optimization-modes-e62142\|Optimization modes]] |
| 2026 Q2 | 2026-04-09 [[Changes/ChatGPT/2026-04-09-today-we-re-releasing-gpt-5-3-instant-mini-in-chatgpt-it-replaces-gpt-5-instant\|GPT-5.3 Instant mini in ChatGPT]] | 2026-06-30 [[Changes/Claude Code/2026-06-30-introducing-claude-sonnet-5-now-the-default-model-in-claude-code-with-a-native-1\|Introducing Claude Sonnet 5]]<br>2026-06-09 [[Changes/Claude Code/2026-06-09-introducing-claude-fable-5-a-mythos-class-model-that-we-ve-made-safe-for-general\|Introducing Claude Fable 5: a Mythos-class model that we’ve made safe for general use]]<br>2026-05-30 [[Changes/Claude Code/2026-05-30-auto-mode-is-now-available-on-bedrock-vertex-and-foundry-for-opus-4-7-and-opus-4\|Auto mode is now available on Bedrock, Vertex, and Foundry for Opus 4.7 and Opus 4.8]]<br>2026-04-16 [[Changes/Claude Code/2026-04-16-auto-mode-is-now-available-for-max-subscribers-when-using-opus-4-7\|Auto mode is now available for Max subscribers when using Opus 4.7]] | 2026-05-04 [[Changes/Cursor/2026-05-04-model-access-controls-d2ba4f\|Model access controls]] |
| 2026 Q1 | · | 2026-03-14 [[Changes/Claude Code/2026-03-14-added-effort-slash-command-to-set-model-effort-level\|Added /effort slash command to set model effort level]]<br>2026-02-07 [[Changes/Claude Code/2026-02-07-fast-mode-is-now-available-for-opus-4-6-learn-more-at-https-code-claude-com-docs\|Fast mode is now available for Opus 4.6]]<br>2026-02-05 [[Changes/Claude Code/2026-02-05-claude-opus-4-6-is-now-available\|Claude Opus 4.6 is now available!]] | 2026-01-22 [[Changes/Cursor/2026-01-22-added-max-mode-on-off-to-toggle-max-mode-on-models-that-support-it-in-cli\|Added /max-mode on / off to toggle max mode on models that support it in CLI]]<br>2026-01-08 [[Changes/Cursor/2026-01-08-use-the-new-agent-models-command-list-models-flag-or-models-slash-command-to-lis\|Model list and selection]] |
| 2025 Q4 | 2025-12-11 [[Changes/ChatGPT/2025-12-11-today-we-re-releasing-gpt-5-2-the-next-upgrade-to-the-gpt-5-series-gpt-5-2-is-sm\|Today, we’re releasing GPT-5.2, the next upgrade to the GPT-5 series]] | · | 2025-10-29 [[Changes/Cursor/2025-10-29-introducing-our-first-agentic-coding-model-composer-is-a-frontier-model-that-is\|Composer]] |
| 2025 Q3 | 2025-08-12 [[Changes/ChatGPT/2025-08-12-gmail-google-calendar-and-google-contacts-are-now-available-to-connect-and-use-i-9ea6d6\|Gmail, Google Calendar, and Google Contacts Connectors in ChatGPT (Pro)]] | · | 2025-08-06 [[Changes/Cursor/2025-08-06-separate-models-per-agent\|Separate models per Agent]] |
| 2025 Q2 | 2025-06-10 [[Changes/ChatGPT/2025-06-10-like-o1-pro-o3-pro-is-a-version-of-our-most-intelligent-model-o3-designed-to-thi-32668a\|ChatGPT launches OpenAI o3-pro—available now for Pro users and in our API]]<br>2025-05-14 [[Changes/ChatGPT/2025-05-14-gpt-4-1-mini-is-a-fast-capable-and-efficient-small-model-delivering-significant-722b7d\|Introducing GPT-4.1 mini, replacing GPT-4o mini, in ChatGPT for all users]]<br>2025-04-16 [[Changes/ChatGPT/2025-04-16-today-we-re-releasing-openai-o3-and-o4-mini-the-latest-in-our-o-series-of-models\|o3 and o4-mini in ChatGPT]] | · | 2025-06-04 [[Changes/Cursor/2025-06-04-max-mode-is-now-available-for-gemini-2-5-flash\|Max mode is now available for Gemini 2.5 Flash]]<br>2025-05-15 [[Changes/Cursor/2025-05-15-max-mode-for-all-top-models\|Max Mode for all top models]]<br>2025-04-15 [[Changes/Cursor/2025-04-15-new-models\|New models]] |
| 2025 Q1 | 2025-03-27 [[Changes/ChatGPT/2025-03-27-early-testers-say-that-the-model-seems-to-better-understand-the-implied-intent-b\|“Fuzzy” improvements]] | · | · |
| 2024 Q3 | 2024-07-18 [[Changes/ChatGPT/2024-07-18-we-re-introducing-gpt-4o-mini-the-most-capable-and-cost-efficient-small-model-av-af297b\|Introducing GPT-4o mini]] | · | · |
| 2024 Q2 | 2024-05-13 [[Changes/ChatGPT/2024-05-13-gpt-4o-is-our-newest-flagship-model-that-provides-gpt-4-level-intelligence-that-297427\|Introducing GPT-4o]] | · | · |
| 2023 Q3 | · | · | 2023-07-28 [[Changes/Cursor/2023-07-28-long-ai-completions-8c21b2\|Long AI completions]] |
| 2023 Q2 | · | · | 2023-05-20 [[Changes/Cursor/2023-05-20-upgrades-to-gpt-4-e59675\|Upgrades to GPT-4]] |
<!-- chronolog:end -->

<!-- chronolog:begin region="scope" -->
> [!info]- How to read this timeline
> Scope: tracked-products-only. Entries show same-theme chronology; they do not establish equivalent capabilities, adoption, or causation.
<!-- chronolog:end -->

## Timeline
<!-- chronolog:begin region="timeline" -->
> [!info]- 2026 · 147 entries (ChatGPT 37 · Claude Code 96 · Cursor 14)
> **2026-10**
>
> - 2026-10-31 · **Claude Code** · [[Changes/Claude Code/2026-10-31-deprecated-fast-mode-for-opus-4-8-as-of-october-30-2026-it-will-be-removed-on-no|Deprecated fast mode for Opus 4.8 as of October 30, 2026]] · Policy
> - 2026-10-30 · **Claude Code** · [[Changes/Claude Code/2026-10-30-2-model-support-changes-in-v2-1-314|2 Model Support changes in v2.1.314]] · Digest
> - 2026-10-27 · **Claude Code** · [[Changes/Claude Code/2026-10-27-3-model-support-changes-in-v2-1-312|3 Model Support changes in v2.1.312]] · Digest
> - 2026-10-26 · **ChatGPT** · [[Changes/ChatGPT/2026-10-26-gpt-6-1-terra-is-rolling-out-in-chatgpt-work-and-codex-it-supports-a-range-of-ta|GPT-6.1 Terra]]
> - 2026-10-26 · **Claude Code** · [[Changes/Claude Code/2026-10-26-5-model-support-changes-in-v2-1-311|5 Model Support changes in v2.1.311]] · Digest
> - 2026-10-19 · **Claude Code** · [[Changes/Claude Code/2026-10-19-2-model-support-changes-in-v2-1-304|2 Model Support changes in v2.1.304]] · Digest
> - 2026-10-16 · **ChatGPT** · [[Changes/ChatGPT/2026-10-16-gpt-6-pro-in-the-chat-tab-now-offers|GPT-6 Pro in the chat tab now offers]]
> - 2026-10-16 · **Claude Code** · [[Changes/Claude Code/2026-10-16-improved-the-message-when-a-background-session-reopened-from-another-folder-has|Improved the message when a background session reopened from another folder has no…]]
> - 2026-10-14 · **Claude Code** · [[Changes/Claude Code/2026-10-14-2-model-support-changes-in-v2-1-299|2 Model Support changes in v2.1.299]] · Digest
> - 2026-10-14 · **Claude Code** · [[Changes/Claude Code/2026-10-14-improved-the-note-claude-3-models-get-about-an-mentioned-pdf-so-they-less-often|Improved the note Claude 3 models get about an @-mentioned PDF, so they less often…]]
> - 2026-10-09 · **Claude Code** · [[Changes/Claude Code/2026-10-09-claude-tag-changed-claude-in-slack-to-show-the-footer-with-the-session-link-mode|Claude Tag Changed Claude in Slack to show the footer with the session link, model…]]
> - 2026-10-08 · **Claude Code** · [[Changes/Claude Code/2026-10-08-3-model-support-changes-in-v2-1-295|3 Model Support changes in v2.1.295]] · Digest
> - 2026-10-07 · **ChatGPT** · [[Changes/ChatGPT/2026-10-07-we-re-introducing-gpt-6-with-intelligent-ui-in-chatgpt-chatgpt-can-now-combine-t|GPT-6 and Intelligent UI in ChatGPT]] · Launch
> - 2026-10-07 · **Claude Code** · [[Changes/Claude Code/2026-10-07-added-claude-haiku-5-5-claude-haiku-5-5-now-the-default-haiku-model-on-the-anthr|Added Claude Haiku 5.5 (claude-haiku-5-5), now the default Haiku model…]]
> - 2026-10-06 · **Claude Code** · [[Changes/Claude Code/2026-10-06-added-prompt-caching-to-model-complete-for-mods-prompt-and-system-take-blocks-of|Added prompt caching to $.model.complete for mods]]
> - 2026-10-05 · **Claude Code** · [[Changes/Claude Code/2026-10-05-2-model-support-changes-in-v2-1-290|2 Model Support changes in v2.1.290]] · Digest
> - 2026-10-02 · **Claude Code** · [[Changes/Claude Code/2026-10-02-changed-the-client-side-auto-mode-classifier-to-ignore-an-anthropic-default-sonn|Changed the client-side auto mode classifier to ignore…]]
> - 2026-10-01 · **Claude Code** · [[Changes/Claude Code/2026-10-01-4-model-support-changes-in-v2-1-287|4 Model Support changes in v2.1.287]] · Digest
>
> **2026-09**
>
> - 2026-09-30 · **Claude Code** · [[Changes/Claude Code/2026-09-30-changed-how-failed-api-requests-are-retried-one-limit-now-covers-a-whole-model-c|Changed how failed API requests are retried]]
> - 2026-09-29 · **ChatGPT** · [[Changes/ChatGPT/2026-09-29-gpt-6-1-sol-improves-on-gpt-6-sol-in-agentic-coding-computer-use-and-professiona-815850|GPT-6.1 Sol in ChatGPT Work and Codex]]
> - 2026-09-29 · **ChatGPT** · [[Changes/ChatGPT/2026-09-29-eligible-plus-and-pro-users-can-authorize-participating-apps-to-use-their-chatgp|Eligible Plus and Pro users can authorize participating apps to use their ChatGPT…]]
> - 2026-09-29 · **Claude Code** · [[Changes/Claude Code/2026-09-29-3-model-support-changes-in-v2-1-285|3 Model Support changes in v2.1.285]] · Digest
> - 2026-09-28 · **Claude Code** · [[Changes/Claude Code/2026-09-28-6-model-support-changes-in-v2-1-284|6 Model Support changes in v2.1.284]] · Digest
> - 2026-09-25 · **Claude Code** · [[Changes/Claude Code/2026-09-25-3-model-support-changes-in-v2-1-283|3 Model Support changes in v2.1.283]] · Digest
> - 2026-09-24 · **Claude Code** · [[Changes/Claude Code/2026-09-24-2-model-support-changes-in-v2-1-282|2 Model Support changes in v2.1.282]] · Digest
> - 2026-09-23 · **Claude Code** · [[Changes/Claude Code/2026-09-23-improved-interactive-startup-time-git-reads-startup-telemetry-and-the-bedrock-ve|Improved interactive startup time]]
> - 2026-09-22 · **Claude Code** · [[Changes/Claude Code/2026-09-22-5-model-support-changes-in-v2-1-280|5 Model Support changes in v2.1.280]] · Digest
> - 2026-09-18 · **Claude Code** · [[Changes/Claude Code/2026-09-18-changed-fable-to-always-appear-in-model-on-the-anthropic-api-it-is-greyed-out-on|Changed Fable to always appear in /model on the Anthropic API]]
> - 2026-09-17 · **Claude Code** · [[Changes/Claude Code/2026-09-17-2-model-support-changes-in-v2-1-274|2 Model Support changes in v2.1.274]] · Digest
> - 2026-09-17 · **Claude Code** · [[Changes/Claude Code/2026-09-17-added-a-send-now-key-ctrl-enter-or-ctrl-x-ctrl-s-that-interrupts-the-current-tur|Added a send-now key (ctrl+enter, or ctrl+x ctrl+s) that interrupts the current turn…]]
> - 2026-09-15 · **Claude Code** · [[Changes/Claude Code/2026-09-15-changed-bug-and-feedback-reports-to-include-only-model-behavior-params-model-sys|Changed /bug and /feedback reports to include only model-behavior params…]]
> - 2026-09-14 · **ChatGPT** · [[Changes/ChatGPT/2026-09-14-we-re-retiring-automatic-switching-from-instant-to-thinking-reasoning-for-chatgp|Changes to automatic switching to thinking in ChatGPT (Plus and Pro)]] · Policy
> - 2026-09-14 · **Claude Code** · [[Changes/Claude Code/2026-09-14-2-model-support-changes-in-v2-1-271|2 Model Support changes in v2.1.271]] · Digest
> - 2026-09-11 · **Claude Code** · [[Changes/Claude Code/2026-09-11-added-claude-code-gateway-model-discovery-timeout-ms-to-extend-the-llm-gateway-v|Added CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS to extend the LLM gateway…]]
> - 2026-09-10 · **Claude Code** · [[Changes/Claude Code/2026-09-10-2-model-support-changes-in-v2-1-268|2 Model Support changes in v2.1.268]] · Digest
> - 2026-09-09 · **ChatGPT** · [[Changes/ChatGPT/2026-09-09-chatgpt-voice-can-now-use-gpt-5-6-or-gpt-6-astra-when-it-needs-to-search-or-reas-848954|ChatGPT Voice can now use GPT-5.6 or GPT-6 Astra when it needs to search or reason…]]
> - 2026-09-09 · **Claude Code** · [[Changes/Claude Code/2026-09-09-added-maxeffortlevel-setting-top-level-or-per-model-under-modelsettings-caps-the|Added maxEffortLevel setting (top-level or per model under modelSettings)]]
> - 2026-09-04 · **Claude Code** · [[Changes/Claude Code/2026-09-04-improved-the-model-picker-and-the-vs-code-model-pill-to-show-a-model-s-name-inst|Improved the /model picker and the VS Code model pill to show a model's name…]]
> - 2026-09-03 · **ChatGPT** · [[Changes/ChatGPT/2026-09-03-today-we-re-introducing-gpt-6-astra-with-improvements-in-coding-research-compute-069f67|Introducing GPT-6 Astra]] · Launch
> - 2026-09-03 · **Claude Code** · [[Changes/Claude Code/2026-09-03-2-model-support-changes-in-v2-1-260|2 Model Support changes in v2.1.260]] · Digest
> - 2026-09-01 · **Claude Code** · [[Changes/Claude Code/2026-09-01-6-model-support-changes-in-v2-1-257|6 Model Support changes in v2.1.257]] · Digest
>
> **2026-08**
>
> - 2026-08-31 · **ChatGPT** · [[Changes/ChatGPT/2026-08-31-site-tools-use-webmcp-and-require-a-supported-account-model-and-webpage-they-are|Site tools use WebMCP and require a supported account, model, and webpage]]
> - 2026-08-28 · **Claude Code** · [[Changes/Claude Code/2026-08-28-5-model-support-changes-in-v2-1-251|5 Model Support changes in v2.1.251]] · Digest
> - 2026-08-26 · **Claude Code** · [[Changes/Claude Code/2026-08-26-added-claude-api-cost-optimize-to-profile-an-existing-project-s-claude-api-spend|Added /claude-api cost-optimize to profile an existing project's Claude API spend…]]
> - 2026-08-19 · **Claude Code** · [[Changes/Claude Code/2026-08-19-added-anthropic-default-model-environment-variable-sets-the-model-new-sessions-s|Added ANTHROPIC_DEFAULT_MODEL environment variable]]
> - 2026-08-17 · **Claude Code** · [[Changes/Claude Code/2026-08-17-2-model-support-changes-in-v2-1-234|2 Model Support changes in v2.1.234]] · Digest
> - 2026-08-14 · **Claude Code** · [[Changes/Claude Code/2026-08-14-2-model-support-changes-in-v2-1-233|2 Model Support changes in v2.1.233]] · Digest
> - 2026-08-11 · **Claude Code** · [[Changes/Claude Code/2026-08-11-changed-the-write-tool-so-newer-models-can-overwrite-an-existing-file-they-haven|Changed the Write tool so newer models can overwrite an existing file they haven't…]]
> - 2026-08-07 · **Claude Code** · [[Changes/Claude Code/2026-08-07-changed-the-bash-tool-description-to-always-note-that-command-output-is-displaye|Changed the Bash tool description to always note that command output is displayed…]]
> - 2026-08-06 · **ChatGPT** · [[Changes/ChatGPT/2026-08-06-plus-and-pro-users-can-now-use-an-updated-gpt-5-6-sol-in-chatgpt-with-more-relia-397840|Updates to GPT‑5.6 in ChatGPT]]
> - 2026-08-04 · **Claude Code** · [[Changes/Claude Code/2026-08-04-3-model-support-changes-in-v2-1-221|3 Model Support changes in v2.1.221]] · Digest
> - 2026-08-04 · **Claude Code** · [[Changes/Claude Code/2026-08-04-improved-the-refusal-when-claude-tries-to-invoke-a-skill-with-disable-model-invo|Improved the refusal when Claude tries to invoke a skill with disable-model-invocation]]
>
> **2026-07**
>
> - 2026-07-24 · **Claude Code** · [[Changes/Claude Code/2026-07-24-3-model-support-changes-in-v2-1-219|3 Model Support changes in v2.1.219]] · Digest
> - 2026-07-22 · **Claude Code** · [[Changes/Claude Code/2026-07-22-added-an-announcement-when-fast-mode-changes-as-a-result-of-switching-models-via|Added an announcement when fast mode changes as a result of switching models…]]
> - 2026-07-22 · **Cursor** · [[Changes/Cursor/2026-07-22-cursor-router-is-our-intelligent-model-router-it-analyzes-each-request-and-sends|Cursor Router is our intelligent model router]]
> - 2026-07-22 · **Cursor** · [[Changes/Cursor/2026-07-22-routed-model-can-be-displayed-or-hidden-hidden-by-default|Routed model can be displayed or hidden (hidden by default)]]
> - 2026-07-22 · **Cursor** · [[Changes/Cursor/2026-07-22-optimization-modes-e62142|Optimization modes]] · Launch
> - 2026-07-17 · **Claude Code** · [[Changes/Claude Code/2026-07-17-3-model-support-changes-in-v2-1-212|3 Model Support changes in v2.1.212]] · Digest
> - 2026-07-14 · **Claude Code** · [[Changes/Claude Code/2026-07-14-improved-the-bash-powershell-tool-message-when-a-command-hits-its-timeout-and-is|Improved the Bash/PowerShell tool message when a command hits its timeout…]]
> - 2026-07-11 · **Claude Code** · [[Changes/Claude Code/2026-07-11-changed-bedrock-vertex-and-claude-platform-on-aws-to-default-to-claude-opus-4-8|Changed Bedrock, Vertex, and Claude Platform on AWS to default to Claude Opus 4.8]]
> - 2026-07-10 · **Claude Code** · [[Changes/Claude Code/2026-07-10-improved-code-review-findings-quality-on-claude-opus-4-8-across-all-effort-level|Improved /code-review findings quality on claude-opus-4-8 across all effort levels]]
> - 2026-07-06 · **ChatGPT** · [[Changes/ChatGPT/2026-07-06-we-re-rolling-out-gpt-5-5-instant-mini-in-chatgpt-it-replaces-gpt-5-3-instant-mi|GPT-5.5 Instant Mini in ChatGPT]]
> - 2026-07-03 · **Claude Code** · [[Changes/Claude Code/2026-07-03-claude-sonnet-5-sessions-no-longer-use-the-mid-conversation-system-role-for-harn|Claude Sonnet 5 sessions no longer use the mid-conversation system role for harness…]]
> - 2026-07-01 · **Claude Code** · [[Changes/Claude Code/2026-07-01-2-model-support-changes-in-v2-1-198|2 Model Support changes in v2.1.198]] · Digest
>
> **2026-06**
>
> - 2026-06-30 · **Claude Code** · [[Changes/Claude Code/2026-06-30-introducing-claude-sonnet-5-now-the-default-model-in-claude-code-with-a-native-1|Introducing Claude Sonnet 5]] · Launch
> - 2026-06-29 · **Claude Code** · [[Changes/Claude Code/2026-06-29-added-support-for-organization-default-models-admins-set-it-in-the-org-console-i|Added support for organization default models]]
> - 2026-06-26 · **ChatGPT** · [[Changes/ChatGPT/2026-06-26-as-of-june-26-2026-gpt-4-5-is-no-longer-available-in-chatgpt-including-for-custo|Retiring GPT-4.5]] · Policy
> - 2026-06-25 · **Claude Code** · [[Changes/Claude Code/2026-06-25-added-claude-code-assistant-response-opentelemetry-log-event-containing-the-mode|Added claude_code.assistant_response OpenTelemetry log event containing…]]
> - 2026-06-24 · **ChatGPT** · [[Changes/ChatGPT/2026-06-24-we-re-updating-gpt-5-5-instant-our-most-used-model-in-chatgpt-to-improve-convers|GPT-5.5 Instant Update]]
> - 2026-06-19 · **Claude Code** · [[Changes/Claude Code/2026-06-19-added-a-warning-when-the-requested-model-is-deprecated-or-automatically-updated|Added a warning when the requested model is deprecated or automatically updated…]] · Policy
> - 2026-06-18 · **ChatGPT** · [[Changes/ChatGPT/2026-06-18-long-press-send-to-choose-a-model-android-users-on-paid-plans-can-now-long-press|Long-press send to choose a model]]
> - 2026-06-15 · **Claude Code** · [[Changes/Claude Code/2026-06-15-bug-now-requires-a-description-before-submitting-and-no-longer-uses-model-refusa|/bug now requires a description before submitting, and no longer uses…]]
> - 2026-06-12 · **ChatGPT** · [[Changes/ChatGPT/2026-06-12-as-of-june-12-2026-gpt-5-2-models-are-no-longer-available-in-chatgpt-this-applie|Retiring GPT-5.2 models]] · Policy
> - 2026-06-12 · **Claude Code** · [[Changes/Claude Code/2026-06-12-added-enforceavailablemodels-managed-setting-when-enabled-the-availablemodels-al|Added enforceAvailableModels managed setting]]
> - 2026-06-10 · **ChatGPT** · [[Changes/ChatGPT/2026-06-10-pro-extended-pro-plans-only|Pro Extended Pro plans only]]
> - 2026-06-10 · **ChatGPT** · [[Changes/ChatGPT/2026-06-10-extra-high-pro-plans-only|Extra High Pro plans only]]
> - 2026-06-10 · **ChatGPT** · [[Changes/ChatGPT/2026-06-10-pro-standard-pro-plans-only|Pro Standard Pro plans only]]
> - 2026-06-10 · **Claude Code** · [[Changes/Claude Code/2026-06-10-2-model-support-changes-in-v2-1-172|2 Model Support changes in v2.1.172]] · Digest
> - 2026-06-09 · **Claude Code** · [[Changes/Claude Code/2026-06-09-introducing-claude-fable-5-a-mythos-class-model-that-we-ve-made-safe-for-general|Introducing Claude Fable 5: a Mythos-class model that we’ve made safe for general use]] · Launch
> - 2026-06-08 · **ChatGPT** · [[Changes/ChatGPT/2026-06-08-long-press-send-to-choose-a-model-users-on-paid-plans-can-now-long-press-the-sen|Long-press send to choose a model]]
> - 2026-06-08 · **Claude Code** · [[Changes/Claude Code/2026-06-08-added-a-disablebundledskills-setting-and-claude-code-disable-bundled-skills-envi|Added a disableBundledSkills setting and CLAUDE_CODE_DISABLE_BUNDLED_SKILLS…]]
> - 2026-06-06 · **Claude Code** · [[Changes/Claude Code/2026-06-06-3-model-support-changes-in-v2-1-166|3 Model Support changes in v2.1.166]] · Digest
> - 2026-06-03 · **Claude Code** · [[Changes/Claude Code/2026-06-03-2-model-support-changes-in-v2-1-162|2 Model Support changes in v2.1.162]] · Digest
> - 2026-06-02 · **Claude Code** · [[Changes/Claude Code/2026-06-02-removed-claude-code-opus-4-6-fast-mode-override-the-environment-variable-is-now|Removed CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE; the environment variable is now a no-op]]
>
> **2026-05**
>
> - 2026-05-30 · **Claude Code** · [[Changes/Claude Code/2026-05-30-auto-mode-is-now-available-on-bedrock-vertex-and-foundry-for-opus-4-7-and-opus-4|Auto mode is now available on Bedrock, Vertex, and Foundry for Opus 4.7 and Opus 4.8]]
> - 2026-05-28 · **ChatGPT** · [[Changes/ChatGPT/2026-05-28-today-we-re-continuing-to-retire-older-models-with-limited-usage-in-chatgpt-so-w|Retiring OpenAI o3 and GPT-4.5]] · Policy
> - 2026-05-28 · **ChatGPT** · [[Changes/ChatGPT/2026-05-28-we-re-updating-gpt-5-5-instant-in-chatgpt-and-the-api-to-improve-response-style|GPT-5.5 Instant Update]]
> - 2026-05-28 · **Claude Code** · [[Changes/Claude Code/2026-05-28-5-model-support-changes-in-v2-1-154|5 Model Support changes in v2.1.154]] · Digest
> - 2026-05-28 · **Claude Code** · [[Changes/Claude Code/2026-05-28-model-now-saves-your-selection-as-the-default-for-new-sessions-matching-the-ide|/model now saves your selection as the default for new sessions (matching the IDE)]]
> - 2026-05-27 · **Claude Code** · [[Changes/Claude Code/2026-05-27-2-model-support-changes-in-v2-1-152|2 Model Support changes in v2.1.152]] · Digest
> - 2026-05-19 · **Claude Code** · [[Changes/Claude Code/2026-05-19-resumed-sessions-now-keep-the-model-they-were-using-instead-of-picking-up-anothe|Resumed sessions now keep the model they were using instead of picking up another…]]
> - 2026-05-18 · **Cursor** · [[Changes/Cursor/2026-05-18-composer-2-5-includes-double-usage-for-the-first-week-see-our-model-docs-for-ful|Composer 2.5 includes double usage for the first week]]
> - 2026-05-18 · **Cursor** · [[Changes/Cursor/2026-05-18-it-s-a-substantial-improvement-in-intelligence-and-behavior-over-composer-2-it-i|It's a substantial improvement in intelligence and behavior over Composer 2]]
> - 2026-05-15 · **Claude Code** · [[Changes/Claude Code/2026-05-15-2-model-support-changes-in-v2-1-143|2 Model Support changes in v2.1.143]] · Digest
> - 2026-05-14 · **Claude Code** · [[Changes/Claude Code/2026-05-14-2-model-support-changes-in-v2-1-142|2 Model Support changes in v2.1.142]] · Digest
> - 2026-05-11 · **Claude Code** · [[Changes/Claude Code/2026-05-11-compaction-prompt-now-asks-the-model-to-preserve-sensitive-user-instructions|Compaction prompt now asks the model to preserve sensitive user instructions]]
> - 2026-05-11 · **Cursor** · [[Changes/Cursor/2026-05-11-high-bugbot-spends-more-time-reasoning-reviews-are-more-expensive-and-take-longe|High: Bugbot spends more time reasoning]]
> - 2026-05-11 · **Cursor** · [[Changes/Cursor/2026-05-11-custom-describe-in-natural-language-when-bugbot-should-use-default-or-high-effor|Custom: Describe in natural language when Bugbot should use default or high effort]]
> - 2026-05-07 · **Cursor** · [[Changes/Cursor/2026-05-07-added-support-for-general-model-names-for-subagent-configuration-i-e-set-model-o|Added support for general model names for subagent configuration (i.e., set model]]
> - 2026-05-06 · **Claude Code** · [[Changes/Claude Code/2026-05-06-2-model-support-changes-in-v2-1-129|2 Model Support changes in v2.1.129]] · Digest
> - 2026-05-05 · **ChatGPT** · [[Changes/ChatGPT/2026-05-05-we-re-rolling-out-gpt-5-5-instant-as-chatgpt-s-new-default-model-it-replaces-gpt|GPT-5.5 Instant in ChatGPT]]
> - 2026-05-04 · **Claude Code** · [[Changes/Claude Code/2026-05-04-updated-model-picker-collapsed-duplicate-opus-4-7-entries-and-current-opus-now-s|Updated /model picker]]
> - 2026-05-04 · **Cursor** · [[Changes/Cursor/2026-05-04-model-access-controls-d2ba4f|Model access controls]] · Launch
> - 2026-05-01 · **Claude Code** · [[Changes/Claude Code/2026-05-01-2-model-support-changes-in-v2-1-126|2 Model Support changes in v2.1.126]] · Digest
>
> **2026-04**
>
> - 2026-04-28 · **ChatGPT** · [[Changes/ChatGPT/2026-04-28-we-re-making-it-easier-to-choose-the-right-model-before-you-send-a-message-model|Easier model selection in ChatGPT]]
> - 2026-04-28 · **Claude Code** · [[Changes/Claude Code/2026-04-28-opentelemetry-added-stop-reason-gen-ai-response-finish-reasons-and-user-system-p|OpenTelemetry: added stop_reason, gen_ai.response.finish_reasons…]]
> - 2026-04-22 · **Claude Code** · [[Changes/Claude Code/2026-04-22-2-model-support-changes-in-v2-1-117|2 Model Support changes in v2.1.117]] · Digest
> - 2026-04-16 · **Claude Code** · [[Changes/Claude Code/2026-04-16-3-model-support-changes-in-v2-1-111|3 Model Support changes in v2.1.111]] · Digest
> - 2026-04-16 · **Claude Code** · [[Changes/Claude Code/2026-04-16-auto-mode-is-now-available-for-max-subscribers-when-using-opus-4-7|Auto mode is now available for Max subscribers when using Opus 4.7]]
> - 2026-04-14 · **Claude Code** · [[Changes/Claude Code/2026-04-14-improved-model-to-warn-before-switching-models-mid-conversation-since-the-next-r|Improved /model to warn before switching models mid-conversation, since the next…]]
> - 2026-04-14 · **Cursor** · [[Changes/Cursor/2026-04-14-trigger-the-model-picker-from-anywhere-to-switch-models-without-clearing-your-pr|Trigger the model picker from anywhere to switch models without clearing your prompt first]]
> - 2026-04-09 · **ChatGPT** · [[Changes/ChatGPT/2026-04-09-today-we-re-releasing-gpt-5-3-instant-mini-in-chatgpt-it-replaces-gpt-5-instant|GPT-5.3 Instant mini in ChatGPT]] · Launch
> - 2026-04-01 · **Claude Code** · [[Changes/Claude Code/2026-04-01-usage-now-hides-redundant-current-week-sonnet-only-bar-for-pro-and-enterprise-pl|/usage now hides redundant "Current week (Sonnet only)" bar for Pro and Enterprise plans]]
>
> **2026-03**
>
> - 2026-03-26 · **Claude Code** · [[Changes/Claude Code/2026-03-26-added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef|Added ANTHROPIC_DEFAULT{OPUS,SONNET,HAIKU}MODEL_SUPPORTS env vars to override…]]
> - 2026-03-19 · **Claude Code** · [[Changes/Claude Code/2026-03-19-added-effort-frontmatter-support-for-skills-and-slash-commands-to-override-the-m|Added effort frontmatter support for skills and slash commands to override…]]
> - 2026-03-18 · **ChatGPT** · [[Changes/ChatGPT/2026-03-18-we-re-rolling-out-gpt-5-4-mini-in-chatgpt-gpt-5-4-mini-is-available-to-free-and|GPT-5.4 mini in ChatGPT]]
> - 2026-03-17 · **ChatGPT** · [[Changes/ChatGPT/2026-03-17-instant-fast-responses-for-everyday-questions|Instant – fast responses for everyday questions]]
> - 2026-03-17 · **ChatGPT** · [[Changes/ChatGPT/2026-03-17-pro-the-most-advanced-reasoning-models|Pro – the most advanced reasoning models]]
> - 2026-03-17 · **ChatGPT** · [[Changes/ChatGPT/2026-03-17-thinking-deeper-reasoning-for-more-complex-tasks|Thinking – deeper reasoning for more complex tasks]]
> - 2026-03-17 · **Claude Code** · [[Changes/Claude Code/2026-03-17-increased-default-maximum-output-token-limits-for-claude-opus-4-6-to-64k-tokens|Increased default maximum output token limits for Claude Opus 4.6 to 64k tokens…]]
> - 2026-03-16 · **ChatGPT** · [[Changes/ChatGPT/2026-03-16-we-re-rolling-out-an-update-to-gpt-5-3-instant-that-improves-follow-up-tone-and|GPT-5.3 Instant update]]
> - 2026-03-14 · **Claude Code** · [[Changes/Claude Code/2026-03-14-added-effort-slash-command-to-set-model-effort-level|Added /effort slash command to set model effort level]]
> - 2026-03-14 · **Claude Code** · [[Changes/Claude Code/2026-03-14-improved-model-fallback-notifications-now-always-visible-instead-of-hidden-behin|Improved model fallback notifications]]
> - 2026-03-11 · **ChatGPT** · [[Changes/ChatGPT/2026-03-11-as-of-march-11-2026-gpt-5-1-models-are-no-longer-available-in-chatgpt-this-appli|Retiring GPT-5.1 models]] · Policy
> - 2026-03-11 · **Claude Code** · [[Changes/Claude Code/2026-03-11-2-model-support-changes-in-v2-1-73|2 Model Support changes in v2.1.73]] · Digest
> - 2026-03-05 · **Claude Code** · [[Changes/Claude Code/2026-03-05-changed-sonnet-4-5-users-on-pro-max-team-premium-to-be-automatically-migrated-to|Changed Sonnet 4.5 users on Pro/Max/Team Premium to be automatically migrated…]]
> - 2026-03-04 · **Claude Code** · [[Changes/Claude Code/2026-03-04-3-model-support-changes-in-v2-1-68|3 Model Support changes in v2.1.68]] · Digest
> - 2026-03-03 · **ChatGPT** · [[Changes/ChatGPT/2026-03-03-gpt-5-3-instant-delivers-more-accurate-answers-richer-and-better-contextualized|GPT-5.3 Instant Update]]
>
> **2026-02**
>
> - 2026-02-24 · **Claude Code** · [[Changes/Claude Code/2026-02-24-the-model-picker-now-shows-human-readable-labels-e-g-sonnet-4-5-instead-of-raw-m|The /model picker now shows human-readable labels (e.g., "Sonnet 4.5") instead…]]
> - 2026-02-19 · **Claude Code** · [[Changes/Claude Code/2026-02-19-2-model-support-changes-in-v2-1-49|2 Model Support changes in v2.1.49]] · Digest
> - 2026-02-18 · **Cursor** · [[Changes/Cursor/2026-02-18-2-model-support-changes-in-cli-improvements-and-mermaid-ascii|2 Model Support changes in CLI Improvements and Mermaid ASCII…]] · Digest
> - 2026-02-17 · **Claude Code** · [[Changes/Claude Code/2026-02-17-added-support-for-claude-sonnet-4-6|Added support for Claude Sonnet 4.6]]
> - 2026-02-13 · **ChatGPT** · [[Changes/ChatGPT/2026-02-13-as-previously-announced-we-have-retired-gpt-4o-gpt-4-1-gpt-4-1-mini-and-openai-o|Retiring GPT-4o and other legacy models]] · Policy
> - 2026-02-10 · **ChatGPT** · [[Changes/ChatGPT/2026-02-10-we-re-making-an-update-to-gpt-5-2-instant-in-chatgpt-and-the-api-that-improves-r|GPT-5.2 Instant Update]]
> - 2026-02-07 · **Claude Code** · [[Changes/Claude Code/2026-02-07-fast-mode-is-now-available-for-opus-4-6-learn-more-at-https-code-claude-com-docs|Fast mode is now available for Opus 4.6]] · Launch
> - 2026-02-05 · **Claude Code** · [[Changes/Claude Code/2026-02-05-claude-opus-4-6-is-now-available|Claude Opus 4.6 is now available!]] · Launch
> - 2026-02-04 · **ChatGPT** · [[Changes/ChatGPT/2026-02-04-jan-10-2026-we-lowered-the-standard-and-light-thinking-time-as-we-observed-users-e93d5a|Jan 10, 2026: We lowered the Standard and Light thinking time as we observed users…]]
> - 2026-02-04 · **Claude Code** · [[Changes/Claude Code/2026-02-04-improved-system-prompts-to-more-clearly-guide-the-model-toward-using-dedicated-t|Improved system prompts to more clearly guide the model toward using dedicated tools…]]
> - 2026-02-03 · **Claude Code** · [[Changes/Claude Code/2026-02-03-changed-model-to-execute-immediately-instead-of-being-queued|Changed /model to execute immediately instead of being queued]]
>
> **2026-01**
>
> - 2026-01-29 · **ChatGPT** · [[Changes/ChatGPT/2026-01-29-on-february-13-2026-alongside-the-previously-announced-retirement-of-gpt-5-insta|Retiring GPT-4o and other legacy models]] · Policy
> - 2026-01-22 · **ChatGPT** · [[Changes/ChatGPT/2026-01-22-we-re-updating-gpt-5-2-instant-s-default-personality-to-be-more-conversational-a|5.2 Personality System Prompt Update]]
> - 2026-01-22 · **Cursor** · [[Changes/Cursor/2026-01-22-added-max-mode-on-off-to-toggle-max-mode-on-models-that-support-it-in-cli|Added /max-mode on / off to toggle max mode on models that support it in CLI]]
> - 2026-01-20 · **ChatGPT** · [[Changes/ChatGPT/2026-01-20-we-re-rolling-out-an-age-prediction-model-on-chatgpt-consumer-plans-to-help-dete|Rolling out age prediction]] · Policy
> - 2026-01-16 · **Claude Code** · [[Changes/Claude Code/2026-01-16-added-support-for-pretooluse-hooks-to-return-additionalcontext-to-the-model|Added support for PreToolUse hooks to return additionalContext to the model]]
> - 2026-01-16 · **Cursor** · [[Changes/Cursor/2026-01-16-models-removed-use-model-to-see-all-models-or-select-a-model|/models removed. Use /model to see all models or select a model]]
> - 2026-01-09 · **Claude Code** · [[Changes/Claude Code/2026-01-09-merged-slash-commands-and-skills-simplifying-the-mental-model-with-no-change-in|Merged slash commands and skills, simplifying the mental model with no change in behavior]]
> - 2026-01-08 · **Cursor** · [[Changes/Cursor/2026-01-08-use-the-new-agent-models-command-list-models-flag-or-models-slash-command-to-lis|Model list and selection]] · Launch

> [!info]- 2025 · 46 entries (ChatGPT 32 · Cursor 14)
> **2025-12**
>
> - 2025-12-11 · **ChatGPT** · [[Changes/ChatGPT/2025-12-11-today-we-re-releasing-gpt-5-2-the-next-upgrade-to-the-gpt-5-series-gpt-5-2-is-sm|Today, we’re releasing GPT-5.2, the next upgrade to the GPT-5 series]] · Launch
>
> **2025-11**
>
> - 2025-11-21 · **ChatGPT** · [[Changes/ChatGPT/2025-11-21-chatgpt-now-adds-more-inline-images-from-the-web-to-help-you-quickly-understand-83e5b8|More images in answers]]
> - 2025-11-19 · **ChatGPT** · [[Changes/ChatGPT/2025-11-19-today-we-re-updating-gpt-5-pro-to-gpt-5-1-pro-in-early-testing-users-consistentl-191826|GPT-5.1 Pro: Clearer, more capable answers for complex work]]
> - 2025-11-12 · **ChatGPT** · [[Changes/ChatGPT/2025-11-12-we-re-updating-chatgpt-s-tone-controls-so-it-s-easier-to-make-responses-sound-th-d3a253|New tone and personalization controls]]
> - 2025-11-12 · **ChatGPT** · [[Changes/ChatGPT/2025-11-12-we-re-updating-gpt-5-to-gpt-5-1-instant-and-gpt-5-1-thinking-making-answers-both-d702c4|GPT-5.1 in ChatGPT]]
> - 2025-11-05 · **ChatGPT** · [[Changes/ChatGPT/2025-11-05-you-can-now-interrupt-long-running-queries-such-as-deep-research-or-gpt-5-pro-to|Interrupt ChatGPT]]
>
> **2025-10**
>
> - 2025-10-29 · **Cursor** · [[Changes/Cursor/2025-10-29-introducing-our-first-agentic-coding-model-composer-is-a-frontier-model-that-is|Composer]] · Launch
> - 2025-10-29 · **Cursor** · [[Changes/Cursor/2025-10-29-plan-mode-in-background|Plan Mode in Background]] · Launch
> - 2025-10-22 · **ChatGPT** · [[Changes/ChatGPT/2025-10-22-we-re-updating-the-model-for-signed-out-users-to-gpt-5-instant-giving-more-peopl|We’re updating the model for signed-out users to GPT-5 Instant, giving more people…]]
> - 2025-10-03 · **ChatGPT** · [[Changes/ChatGPT/2025-10-03-we-re-updating-gpt-5-instant-to-better-recognize-and-support-people-in-moments-o-ea32fc|Updating GPT-5]]
>
> **2025-09**
>
> - 2025-09-29 · **ChatGPT** · [[Changes/ChatGPT/2025-09-29-opt-out-of-model-training-so-their-teen-s-conversations-won-t-be-used-to-improve|Opt out of model training, so their teen’s conversations won’t be used to improve…]] · Policy
> - 2025-09-18 · **ChatGPT** · [[Changes/ChatGPT/2025-09-18-we-re-improving-the-quality-and-latency-of-responses-of-the-version-of-advanced|Voice Updates]]
> - 2025-09-17 · **ChatGPT** · [[Changes/ChatGPT/2025-09-17-5-model-support-changes-in-toggle-thinking-time-in-the-message|5 Model Support changes in Toggle thinking time in the message…]] · Digest
> - 2025-09-16 · **ChatGPT** · [[Changes/ChatGPT/2025-09-16-factuality-fewer-hallucinations-improving-answer-quality|Factuality: Fewer hallucinations, improving answer quality]]
>
> **2025-08**
>
> - 2025-08-21 · **Cursor** · [[Changes/Cursor/2025-08-21-2-model-support-changes-in-1-5|2 Model Support changes in 1.5]] · Digest
> - 2025-08-15 · **ChatGPT** · [[Changes/ChatGPT/2025-08-15-we-re-making-gpt-5-s-default-personality-warmer-and-more-familiar-this-is-in-res-19a03e|GPT-5 Updates]]
> - 2025-08-12 · **ChatGPT** · [[Changes/ChatGPT/2025-08-12-gmail-google-calendar-and-google-contacts-are-now-available-to-connect-and-use-i-9ea6d6|Gmail, Google Calendar, and Google Contacts Connectors in ChatGPT (Pro)]] · Launch
> - 2025-08-12 · **ChatGPT** · [[Changes/ChatGPT/2025-08-12-you-can-now-choose-between-auto-fast-and-thinking-for-gpt-5-most-users-will-want-f4c05b|GPT-5 Updates]]
> - 2025-08-07 · **ChatGPT** · [[Changes/ChatGPT/2025-08-07-gpt-5-is-slowly-rolling-out-to-all-users-on-chatgpt-plus-pro-team-and-free-plans-64a08c|GPT-5]]
> - 2025-08-06 · **Cursor** · [[Changes/Cursor/2025-08-06-separate-models-per-agent|Separate models per Agent]] · Launch
>
> **2025-07**
>
> - 2025-07-03 · **Cursor** · [[Changes/Cursor/2025-07-03-improved-embeddings-for-semantic-search|Improved embeddings for semantic search]]
>
> **2025-06**
>
> - 2025-06-16 · **ChatGPT** · [[Changes/ChatGPT/2025-06-16-enterprise-and-edu-users-can-also-now-choose-from-the-full-set-of-chatgpt-models-1ea372|Expanded Model Support for Custom GPTs]]
> - 2025-06-13 · **ChatGPT** · [[Changes/ChatGPT/2025-06-13-in-some-cases-a-chain-of-thought-reasoning-will-show-up-unexpectedly-for-simple|In some cases, a “chain of thought” reasoning will show up unexpectedly for simple queries]]
> - 2025-06-12 · **ChatGPT** · [[Changes/ChatGPT/2025-06-12-upload-files-and-access-model-selector-on-mobile|Upload files and access model selector on mobile]]
> - 2025-06-12 · **ChatGPT** · [[Changes/ChatGPT/2025-06-12-creators-can-now-choose-from-the-full-set-of-chatgpt-models-gpt-4o-o3-o4-mini-an-ad1adf|Creators can now choose from the full set of ChatGPT models…]]
> - 2025-06-12 · **Cursor** · [[Changes/Cursor/2025-06-12-once-connected-try-it-in-any-channel-with-cursor-and-write-a-prompt-use-the-comm|Once connected, try it in any channel with @Cursor and write a prompt]]
> - 2025-06-10 · **ChatGPT** · [[Changes/ChatGPT/2025-06-10-like-o1-pro-o3-pro-is-a-version-of-our-most-intelligent-model-o3-designed-to-thi-32668a|ChatGPT launches OpenAI o3-pro—available now for Pro users and in our API]] · Launch
> - 2025-06-04 · **Cursor** · [[Changes/Cursor/2025-06-04-max-mode-is-now-available-for-gemini-2-5-flash|Max mode is now available for Gemini 2.5 Flash]] · Launch
>
> **2025-05**
>
> - 2025-05-15 · **Cursor** · [[Changes/Cursor/2025-05-15-max-mode-for-all-top-models|Max Mode for all top models]] · Launch
> - 2025-05-14 · **ChatGPT** · [[Changes/ChatGPT/2025-05-14-since-its-launch-in-the-api-in-april-gpt-4-1-has-become-a-favorite-among-develop-286eb2|Releasing GPT-4.1 in ChatGPT for all paid users]]
> - 2025-05-14 · **ChatGPT** · [[Changes/ChatGPT/2025-05-14-gpt-4-1-mini-is-a-fast-capable-and-efficient-small-model-delivering-significant-722b7d|Introducing GPT-4.1 mini, replacing GPT-4o mini, in ChatGPT for all users]] · Launch
>
> **2025-04**
>
> - 2025-04-29 · **ChatGPT** · [[Changes/ChatGPT/2025-04-29-we-ve-reverted-the-most-recent-update-to-gpt-4o-due-to-issues-with-overly-agreea-097503|Updates to GPT-4o]]
> - 2025-04-25 · **ChatGPT** · [[Changes/ChatGPT/2025-04-25-we-re-making-additional-improvements-to-gpt-4o-optimizing-when-it-saves-memories|Improvements to GPT-4o]]
> - 2025-04-16 · **ChatGPT** · [[Changes/ChatGPT/2025-04-16-today-we-re-releasing-openai-o3-and-o4-mini-the-latest-in-our-o-series-of-models|o3 and o4-mini in ChatGPT]] · Launch
> - 2025-04-15 · **Cursor** · [[Changes/Cursor/2025-04-15-new-models|New models]] · Launch
> - 2025-04-10 · **ChatGPT** · [[Changes/ChatGPT/2025-04-10-effective-april-30-2025-gpt-4-will-be-retired-from-chatgpt-and-fully-replaced-by-d03b3b|Sunsetting GPT‑4 in ChatGPT]] · Policy
>
> **2025-03**
>
> - 2025-03-27 · **ChatGPT** · [[Changes/ChatGPT/2025-03-27-we-ve-made-improvements-to-gpt-4o-it-now-feels-more-intuitive-creative-and-colla|ChatGPT makes improvements to GPT-4o—it now feels more intuitive, creative…]]
> - 2025-03-27 · **ChatGPT** · [[Changes/ChatGPT/2025-03-27-early-testers-say-that-the-model-seems-to-better-understand-the-implied-intent-b|“Fuzzy” improvements]] · Launch
> - 2025-03-27 · **ChatGPT** · [[Changes/ChatGPT/2025-03-27-gpt-4o-has-further-improved-its-capability-to-tackle-complex-technical-and-codin|Smarter problem-solving in STEM and coding]] · Launch
> - 2025-03-27 · **ChatGPT** · [[Changes/ChatGPT/2025-03-27-gpt-4o-is-now-more-adept-at-following-detailed-instructions-especially-for-promp|Enhanced instruction-following and formatting accuracy]] · Launch
> - 2025-03-23 · **Cursor** · [[Changes/Cursor/2025-03-23-2-model-support-changes-in-0-48-x|2 Model Support changes in 0.48.x]] · Digest
> - 2025-03-18 · **ChatGPT** · [[Changes/ChatGPT/2025-03-18-o1-and-o3-mini-now-offer-python-powered-data-analysis-in-chatgpt-you-can-now-ask-bfa530|o1 and o3-mini now offer Python-powered data analysis in ChatGPT]]
> - 2025-03-11 · **Cursor** · [[Changes/Cursor/2025-03-11-sonnet-3-7-thinking-we-ve-made-a-few-improvements-to-3-7-prompting-thinking-will|Sonnet 3.7 thinking: We've made a few improvements to 3.7 prompting]]
> - 2025-03-11 · **Cursor** · [[Changes/Cursor/2025-03-11-3-model-support-changes-in-0-47-x|3 Model Support changes in 0.47.x]] · Digest
>
> **2025-01**
>
> - 2025-01-23 · **Cursor** · [[Changes/Cursor/2025-01-23-deepseek-models-deepseek-r1-and-deepseek-v3-are-supported-in-0-45-and-0-44-you-c|Deepseek models: Deepseek R1 and Deepseek v3 are supported in 0.45 and 0.44]]
> - 2025-01-23 · **Cursor** · [[Changes/Cursor/2025-01-23-better-codebase-understanding-we-ve-trained-a-new-model-for-codebase-understandi|Better Codebase Understanding: We've trained a new model for Codebase Understanding]]

> [!info]- 2024 · 13 entries (ChatGPT 3 · Cursor 10)
> **2024-12**
>
> - 2024-12-13 · **ChatGPT** · [[Changes/ChatGPT/2024-12-13-projects-provide-a-new-way-to-group-files-and-chats-for-personal-use-simplifying|Projects provide a new way to group files and chats for personal use, simplifying…]]
>
> **2024-07**
>
> - 2024-07-23 · **Cursor** · [[Changes/Cursor/2024-07-23-new-default-model-we-ve-made-claude-3-5-sonnet-the-default-model-for-users|New Default Model: We've made Claude 3.5 Sonnet the default model for users]]
> - 2024-07-18 · **ChatGPT** · [[Changes/ChatGPT/2024-07-18-we-re-introducing-gpt-4o-mini-the-most-capable-and-cost-efficient-small-model-av-af297b|Introducing GPT-4o mini]] · Launch
>
> **2024-06**
>
> - 2024-06-08 · **Cursor** · [[Changes/Cursor/2024-06-08-update-0-35-1-disables-copilot-partial-accepts-by-default-and-makes-the-keybindi|UPDATE (0.35.1): Disables Copilot++ partial accepts by default and makes…]]
>
> **2024-05**
>
> - 2024-05-26 · **Cursor** · [[Changes/Cursor/2024-05-26-gemini-1-5-flash-is-available-in-long-context-mode|Gemini 1.5 Flash is available in long-context mode]]
> - 2024-05-26 · **Cursor** · [[Changes/Cursor/2024-05-26-gpt-4o-in-interpreter-mode|GPT-4o in Interpreter Mode]]
> - 2024-05-13 · **ChatGPT** · [[Changes/ChatGPT/2024-05-13-gpt-4o-is-our-newest-flagship-model-that-provides-gpt-4-level-intelligence-that-297427|Introducing GPT-4o]] · Launch
>
> **2024-04**
>
> - 2024-04-12 · **Cursor** · [[Changes/Cursor/2024-04-12-new-gpt-4-model-as-of-a-couple-of-days-ago-you-can-try-out-gpt-4-turbo-2024-04-0|New GPT-4 model: As of a couple of days ago, you can try out gpt-4-turbo-2024-04-09…]]
>
> **2024-03**
>
> - 2024-03-20 · **Cursor** · [[Changes/Cursor/2024-03-20-stable-claude-support-all-the-newest-claude-models-are-available-for-pro-and-api|Stable Claude Support]]
> - 2024-03-12 · **Cursor** · [[Changes/Cursor/2024-03-12-if-you-re-a-pro-or-business-user-you-can-add-claude-3-opus-as-a-custom-model-in|Claude Support]]
>
> **2024-01**
>
> - 2024-01-25 · **Cursor** · [[Changes/Cursor/2024-01-25-both-pro-and-api-key-users-can-also-try-out-gpt-4-0125-preview-by-configuring-th|Both pro and API key users can also try out gpt-4-0125-preview by configuring…]]
> - 2024-01-18 · **Cursor** · [[Changes/Cursor/2024-01-18-cursor-fast-this-is-a-new-model-available-in-command-k-and-chat-expect-it-to-be|"cursor-fast": This is a new model available in command-k and chat]]
> - 2024-01-15 · **Cursor** · [[Changes/Cursor/2024-01-15-cursor-fast-is-a-newly-trained-model-between-gpt-3-5-and-gpt-4-coding-capabiliti-bb4c11|Cursor-Fast is a newly trained model between gpt-3.5 and gpt-4 coding capabilities…]]

> [!info]- 2023 · 23 entries (ChatGPT 13 · Cursor 10)
> **2023-12**
>
> - 2023-12-16 · **Cursor** · [[Changes/Cursor/2023-12-16-ai-review-beta-this-is-a-new-experimental-feature-that-let-s-gpt-4-scan-your-git|AI Review (beta)]]
>
> **2023-11**
>
> - 2023-11-10 · **Cursor** · [[Changes/Cursor/2023-11-10-new-models-you-can-plug-in-your-api-key-to-try-out-the-newest-gpt-4-and-gpt-3-tu|New models: you can plug in your API key to try out the newest gpt-4 and gpt-3 turbo…]]
>
> **2023-10**
>
> - 2023-10-17 · **ChatGPT** · [[Changes/ChatGPT/2023-10-17-browsing-which-we-re-launched-a-few-weeks-ago-is-moving-out-of-beta-plus-and-ent|Browsing is now out of beta]]
> - 2023-10-16 · **ChatGPT** · [[Changes/ChatGPT/2023-10-16-we-ve-integrated-dall-e-3-with-chatgpt-allowing-it-to-respond-to-your-requests-w-ad3caf|DALL·E 3 is now rolling out in beta]]
> - 2023-10-01 · **Cursor** · [[Changes/Cursor/2023-10-01-use-edit-in-the-chat-to-edit-a-whole-file-if-less-than-400-lines-expect-the-edit-78e4ac|Use /edit in the chat to edit a whole file (if less than 400 lines)]]
>
> **2023-09**
>
> - 2023-09-27 · **ChatGPT** · [[Changes/ChatGPT/2023-09-27-choose-browse-with-bing-in-the-selector-under-gpt-4|Choose Browse with Bing in the selector under GPT-4]]
>
> **2023-08**
>
> - 2023-08-03 · **ChatGPT** · [[Changes/ChatGPT/2023-08-03-we-re-rolling-out-a-bunch-of-small-updates-to-improve-the-chatgpt-experience-shi|Updates to ChatGPT]]
>
> **2023-07**
>
> - 2023-07-28 · **Cursor** · [[Changes/Cursor/2023-07-28-long-ai-completions-8c21b2|Long AI completions]] · Launch
> - 2023-07-19 · **ChatGPT** · [[Changes/ChatGPT/2023-07-19-we-re-doubling-the-number-of-messages-chatgpt-plus-customers-can-send-with-gpt-4|Higher message limits for GPT-4]] · Policy
>
> **2023-06**
>
> - 2023-06-22 · **ChatGPT** · [[Changes/ChatGPT/2023-06-22-browsing-plus-users-can-now-use-browsing-to-get-comprehensive-answers-and-curren|Browsing: Plus users can now use Browsing to get comprehensive answers and current…]]
> - 2023-06-01 · **Cursor** · [[Changes/Cursor/2023-06-01-check-out-the-more-tab-to-have-gpt-3-5-or-gpt-4-review-your-code-periodically-fo|AI Linting]]
>
> **2023-05**
>
> - 2023-05-20 · **Cursor** · [[Changes/Cursor/2023-05-20-upgrades-to-gpt-4-e59675|Upgrades to GPT-4]] · Launch
> - 2023-05-04 · **Cursor** · [[Changes/Cursor/2023-05-04-gpt-4-support-now-available-for-project-generation|GPT-4 support now available for project generation]]
> - 2023-05-03 · **ChatGPT** · [[Changes/ChatGPT/2023-05-03-we-are-deprecating-the-legacy-gpt-3-5-model-on-may-10th-users-will-be-able-to-co|We are deprecating the Legacy (GPT-3.5) model on May 10th]] · Policy
>
> **2023-04**
>
> - 2023-04-19 · **Cursor** · [[Changes/Cursor/2023-04-19-3-model-support-changes-in-0-2-6|3 Model Support changes in 0.2.6]] · Digest
> - 2023-04-14 · **Cursor** · [[Changes/Cursor/2023-04-14-gpt-4-support|GPT-4 support]]
>
> **2023-03**
>
> - 2023-03-30 · **Cursor** · [[Changes/Cursor/2023-03-30-use-an-openai-api-key-for-unlimited-requests-at-cost-gpt-4-access-if-available|Use an OpenAI API key for unlimited requests at cost (GPT-4 access if available)]]
> - 2023-03-23 · **ChatGPT** · [[Changes/ChatGPT/2023-03-23-third-party-plugins-an-experimental-model-that-knows-when-and-how-to-use-externa|Third-party plugins: An experimental model that knows when and how to use external plugins]]
> - 2023-03-23 · **ChatGPT** · [[Changes/ChatGPT/2023-03-23-code-interpreter-an-experimental-chatgpt-model-that-can-use-python-and-handles-u|Code Interpreter: An experimental ChatGPT model that can use Python, and handles…]]
> - 2023-03-14 · **ChatGPT** · [[Changes/ChatGPT/2023-03-14-we-re-excited-to-bring-gpt-4-our-latest-model-to-our-chatgpt-plus-subscribers-gp-7153e9|Announcing GPT-4 in ChatGPT]] · Launch
>
> **2023-02**
>
> - 2023-02-09 · **ChatGPT** · [[Changes/ChatGPT/2023-02-09-default-the-standard-chatgpt-model|Default: the standard ChatGPT model]]
>
> **2023-01**
>
> - 2023-01-30 · **ChatGPT** · [[Changes/ChatGPT/2023-01-30-we-ve-upgraded-the-chatgpt-model-with-improved-factuality-and-mathematical-capab|Factuality and mathematical improvements]]
> - 2023-01-09 · **ChatGPT** · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->