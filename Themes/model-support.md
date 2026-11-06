---
created: '2023-01-09'
date: '2026-11-06'
description: 'Research question: how do the tracked products add, choose between and
  retire models?'
machine_hash: 8c1fb8bc0b0008eca821dc6313756b0df03255f1d01e461b1fcea14ed95c86a7
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
theme: model-support
title: Model Support
---

<!-- chronolog:begin region="header" -->
# Model Support

860 tracked changes across Aider, ChatGPT, Claude Code, Cline, Codex CLI, Cursor, Gemini CLI, GitHub Copilot CLI, OpenHands and Windsurf · 2023-01-09 → 2026-11-06 · Codex CLI averages 8.0 cards per release, Gemini CLI 7.5, Claude Code 7.0, GitHub Copilot CLI 6.3, Cursor 4.0, OpenHands 3.8, Aider 3.7, Cline 3.0, Windsurf 2.6, ChatGPT 1.7
<!-- chronolog:end -->

## Research summary
<!-- chronolog:begin region="narrative" -->
**Research question: how do the tracked products add, choose between and retire models?**

ChatGPT's [2023-03-14 GPT-4 announcement](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#announcing-gpt-4-in-chatgpt) ([[Releases/ChatGPT/chatgpt-2023-03-14-announcing-gpt-4-in-chatgpt-43063370|archived]]) brings GPT-4 to Plus subscribers under a usage cap adjusted to demand. The [2025-08-07 GPT-5 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#gpt-5) ([[Releases/ChatGPT/chatgpt-2025-08-07-gpt-5-a50b91bc|archived]]) makes GPT-5 the default for all logged-in users as a single auto-switching system, with a model picker for paid tiers, and the [2025-08-12 update](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#gpt-5-updates) ([[Releases/ChatGPT/chatgpt-2025-08-12-gpt-5-updates-9aaeee46|archived]]) adds a choice between “Auto”, “Fast” and “Thinking”. Retirements arrive as dated notes: the [2026-02-13 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#retiring-gpt-4o-and-other-legacy-models) ([[Releases/ChatGPT/chatgpt-2026-02-13-retiring-gpt-4o-and-other-legacy-models-71b41b16|archived]]) retires GPT-4o, GPT-4.1, GPT-4.1 mini and OpenAI o4-mini from ChatGPT with no API change, and the [2026-09-14 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#changes-to-automatic-switching-to-thinking-in-chatgpt-plus-and-pro) ([[Releases/ChatGPT/chatgpt-2026-09-14-changes-to-automatic-switching-to-thinking-in-chatgpt-plus-and-p-54d16c58|archived]]) retires automatic switching from Instant to Thinking for Plus and Pro users, while ChatGPT can still switch automatically for safety purposes.

Cursor's [2023-03-30 release](https://cursor.com/changelog/0-1-12) ([[Releases/Cursor/cursor-2023-03-30-0-1-12-https-cursor-com-changelog-0-1-12-f3e1800c|archived]]) lets users plug in an OpenAI API key for unlimited requests at cost. The [2024-03-12 Claude support release](https://cursor.com/changelog/claude-support) ([[Releases/Cursor/cursor-2024-03-12-claude-support-https-cursor-com-changelog-claude-support-ed1eb90a|archived]]) lets Pro and Business users add claude-3-opus as a custom model, and the [2024-07-23 release](https://cursor.com/changelog/0-38-x) ([[Releases/Cursor/cursor-2024-07-23-0-38-x-https-cursor-com-changelog-0-38-x-e6d087df|archived]]) makes Claude 3.5 Sonnet the default model. [Cursor 2.0 on 2025-10-29](https://cursor.com/changelog/2-0) ([[Releases/Cursor/cursor-2025-10-29-2-0-https-cursor-com-changelog-2-0-66a8e76e|archived]]) introduces Composer, described as Cursor's first agentic coding model, and the [2026-07-22 release](https://cursor.com/changelog/router) ([[Releases/Cursor/cursor-2026-07-22-cursor-router-https-cursor-com-changelog-router-af8c2ac4|archived]]) adds Cursor Router, which sends each request to a frontier or a price-efficient model.

Claude Code announces models inside its releases: [v2.1.32 on 2026-02-05](https://github.com/anthropics/claude-code/releases/tag/v2.1.32) ([[Releases/Claude Code/claude-code-2026-02-05-v2-1-32-github-283457817-0910feb0|archived]]) makes Claude Opus 4.6 available, [v2.1.197 on 2026-06-30](https://github.com/anthropics/claude-code/releases/tag/v2.1.197) ([[Releases/Claude Code/claude-code-2026-06-30-v2-1-197-github-346856026-11e4aa1f|archived]]) makes Claude Sonnet 5 the default model with a native 1M-token context window, and [v2.1.280 on 2026-09-22](https://github.com/anthropics/claude-code/releases/tag/v2.1.280) ([[Releases/Claude Code/claude-code-2026-09-22-v2-1-280-github-393879189-1cf5db2b|archived]]) adds Claude Opus 5.5 as the default Opus model. Model controls grow alongside: [v2.1.76 on 2026-03-14](https://github.com/anthropics/claude-code/releases/tag/v2.1.76) ([[Releases/Claude Code/claude-code-2026-03-14-v2-1-76-github-296929324-94cd2ffc|archived]]) adds an `/effort` command, [v2.1.166 on 2026-06-06](https://github.com/anthropics/claude-code/releases/tag/v2.1.166) ([[Releases/Claude Code/claude-code-2026-06-06-v2-1-166-github-335118845-ef990727|archived]]) a `fallbackModel` setting with up to three fallback models, and [v2.1.196 on 2026-06-29](https://github.com/anthropics/claude-code/releases/tag/v2.1.196) ([[Releases/Claude Code/claude-code-2026-06-29-v2-1-196-github-346482381-e21be272|archived]]) organization default models set by admins.

**Uncertainty and scope:** this editorial summary covers ChatGPT, Claude Code and Cursor; the timeline includes all tracked products, Claude Code coverage starts on 2025-12-19, and announcement dates are not availability dates for every plan, region or provider, so a model's name, default status or price in one product says nothing about its quality or availability in another.
<!-- chronolog:end -->

## Key moments
<!-- chronolog:begin region="moments" -->
Selected automatically from launches and standalone announcements.

| Quarter | Aider | ChatGPT | Claude Code | Cline | Codex CLI | Cursor | Gemini CLI | GitHub Copilot CLI | OpenHands | Windsurf |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **First in archive** | <time datetime="2023-06-07">2023-06-07</time> [[Changes/Aider/2023-06-07-added-support-for-gpt-3-5-turbo-and-gpt-4-32k\|Added support for gpt-3.5-turbo and gpt-4-32k]] | <time datetime="2023-01-09">2023-01-09</time> [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr\|We made more improvements to the ChatGPT model!]] | <time datetime="2026-01-09">2026-01-09</time> [[Changes/Claude Code/2026-01-09-merged-slash-commands-and-skills-simplifying-the-mental-model-with-no-change-in\|Merged slash commands and skills, simplifying the mental model with no change in behavior]] | <time datetime="2024-08-11">2024-08-11</time> [[Changes/Cline/2024-08-11-adds-option-to-choose-other-claude-models-gpt-4o-deepseek-and-mistral-if-you-use\|Adds option to choose other Claude models…]] | <time datetime="2025-07-08">2025-07-08</time> [[Changes/Codex CLI/2025-07-08-makes-it-possible-to-configure-custom-http-headers-when-making-requests-to-model\|Makes it possible to configure custom HTTP headers when making requests to model providers]] | <time datetime="2023-03-30">2023-03-30</time> [[Changes/Cursor/2023-03-30-use-an-openai-api-key-for-unlimited-requests-at-cost-gpt-4-access-if-available\|Use an OpenAI API key for unlimited requests at cost (GPT-4 access if available)]] | <time datetime="2025-06-28">2025-06-28</time> [[Changes/Gemini CLI/2025-06-28-release-notes-at-https-github-com-google-gemini-gemini-cli-discussions-2301\|Release notes at: (source link)]] | <time datetime="2025-09-29">2025-09-29</time> [[Changes/GitHub Copilot CLI/2025-09-29-3-model-support-changes-in-v0-0-329\|3 Model Support changes in v0.0.329]] | <time datetime="2024-06-29">2024-06-29</time> [[Changes/OpenHands/2024-06-29-2-model-support-changes-in-0-7-0\|2 Model Support changes in 0.7.0]] | <time datetime="2025-04-14">2025-04-14</time> [[Changes/Windsurf/2025-04-14-gpt-4-1-available\|GPT 4.1 Available]] |
| 2026 Q4 | · | <time datetime="2026-10-07">2026-10-07</time> [[Changes/ChatGPT/2026-10-07-we-re-introducing-gpt-6-with-intelligent-ui-in-chatgpt-chatgpt-can-now-combine-t\|GPT-6 and Intelligent UI in ChatGPT]] | · | · | · | · | · | · | · | · |
| 2026 Q3 | · | <time datetime="2026-09-03">2026-09-03</time> [[Changes/ChatGPT/2026-09-03-today-we-re-introducing-gpt-6-astra-with-improvements-in-coding-research-compute-069f67\|Introducing GPT-6 Astra]] | <time datetime="2026-08-26">2026-08-26</time> [[Changes/Claude Code/2026-08-26-added-claude-api-cost-optimize-to-profile-an-existing-project-s-claude-api-spend\|Added /claude-api cost-optimize to profile an existing project's Claude API spend…]] | · | <time datetime="2026-09-09">2026-09-09</time> [[Changes/Codex CLI/2026-09-09-gpt-6-astra-is-now-available-in-the-model-picker-and-amazon-bedrock-catalogs-428\|GPT-6-Astra is now available in the model picker and Amazon Bedrock catalogs]] | <time datetime="2026-07-22">2026-07-22</time> [[Changes/Cursor/2026-07-22-optimization-modes-e62142\|Optimization modes]] | · | · | · | · |
| 2026 Q2 | · | <time datetime="2026-04-09">2026-04-09</time> [[Changes/ChatGPT/2026-04-09-today-we-re-releasing-gpt-5-3-instant-mini-in-chatgpt-it-replaces-gpt-5-instant\|GPT-5.3 Instant mini in ChatGPT]] | <time datetime="2026-06-30">2026-06-30</time> [[Changes/Claude Code/2026-06-30-introducing-claude-sonnet-5-now-the-default-model-in-claude-code-with-a-native-1\|Introducing Claude Sonnet 5]]<br><time datetime="2026-06-09">2026-06-09</time> [[Changes/Claude Code/2026-06-09-introducing-claude-fable-5-a-mythos-class-model-that-we-ve-made-safe-for-general\|Introducing Claude Fable 5: a Mythos-class model that we’ve made safe for general use]]<br><time datetime="2026-05-30">2026-05-30</time> [[Changes/Claude Code/2026-05-30-auto-mode-is-now-available-on-bedrock-vertex-and-foundry-for-opus-4-7-and-opus-4\|Auto mode is now available on Bedrock, Vertex, and Foundry for Opus 4.7 and Opus 4.8]]<br><time datetime="2026-04-16">2026-04-16</time> [[Changes/Claude Code/2026-04-16-auto-mode-is-now-available-for-max-subscribers-when-using-opus-4-7\|Auto mode is now available for Max subscribers when using Opus 4.7]] | · | · | <time datetime="2026-05-04">2026-05-04</time> [[Changes/Cursor/2026-05-04-model-access-controls-d2ba4f\|Model access controls]] | · | · | · | <time datetime="2026-04-08">2026-04-08</time> [[Changes/Windsurf/2026-04-08-adaptive-fix\|Adaptive Fix]]<br><time datetime="2026-04-07">2026-04-07</time> [[Changes/Windsurf/2026-04-07-adaptive-model-visibility\|Adaptive Model Visibility]]<br><time datetime="2026-04-06">2026-04-06</time> [[Changes/Windsurf/2026-04-06-adaptive-model-router\|Adaptive Model Router]] |
| 2026 Q1 | · | · | · | · | <time datetime="2026-02-05">2026-02-05</time> [[Changes/Codex CLI/2026-02-05-introducing-gpt-5-3-codex-learn-more-https-openai-com-index-introducing-gpt-5-3\|Introducing GPT-5.3-Codex]] | <time datetime="2026-01-22">2026-01-22</time> [[Changes/Cursor/2026-01-22-added-max-mode-on-off-to-toggle-max-mode-on-models-that-support-it-in-cli\|Added /max-mode on / off to toggle max mode on models that support it in CLI]]<br><time datetime="2026-01-08">2026-01-08</time> [[Changes/Cursor/2026-01-08-use-the-new-agent-models-command-list-models-flag-or-models-slash-command-to-lis\|Model list and selection]] | · | · | · | <time datetime="2026-02-25">2026-02-25</time> [[Changes/Windsurf/2026-02-25-new-model-picker\|New Model Picker]]<br><time datetime="2026-02-05">2026-02-05</time> [[Changes/Windsurf/2026-02-05-claude-opus-4-6\|Claude Opus 4.6]] |
| 2025 Q4 | · | <time datetime="2025-12-11">2025-12-11</time> [[Changes/ChatGPT/2025-12-11-today-we-re-releasing-gpt-5-2-the-next-upgrade-to-the-gpt-5-series-gpt-5-2-is-sm\|Today, we’re releasing GPT-5.2, the next upgrade to the GPT-5 series]] | archive begins <time datetime="2025-12-19">2025-12-19</time> | · | <time datetime="2025-12-18">2025-12-18</time> [[Changes/Codex CLI/2025-12-18-introducing-gpt-5-2-codex-our-latest-frontier-model-with-improvements-across-kno\|Introducing gpt-5.2-codex our latest frontier model with improvements across…]]<br><time datetime="2025-12-11">2025-12-11</time> [[Changes/Codex CLI/2025-12-11-introducing-gpt-5-2-our-latest-frontier-model-with-improvements-across-knowledge\|Introducing gpt-5.2 our latest frontier model with improvements across knowledge…]]<br><time datetime="2025-11-07">2025-11-07</time> [[Changes/Codex CLI/2025-11-07-introducing-our-new-model-gpt-5-codex-mini-a-more-compact-and-cost-efficient-ver\|Introducing our new model GPT-5-Codex-Mini]] | <time datetime="2025-10-29">2025-10-29</time> [[Changes/Cursor/2025-10-29-introducing-our-first-agentic-coding-model-composer-is-a-frontier-model-that-is\|Composer]] | · | <time datetime="2025-12-05">2025-12-05</time> [[Changes/GitHub Copilot CLI/2025-12-05-gpt-5-1-codex-max-is-now-available-in-github-copilot-cli\|GPT-5.1-Codex-Max is now available in GitHub Copilot CLI]]<br><time datetime="2025-11-24">2025-11-24</time> [[Changes/GitHub Copilot CLI/2025-11-24-opus-4-5-gpt-4-1-and-gpt-5-mini-are-now-available-in-github-copilot-cli\|Opus 4.5, GPT-4.1 and GPT-5-Mini are now available in GitHub Copilot CLI]]<br><time datetime="2025-11-18">2025-11-18</time> [[Changes/GitHub Copilot CLI/2025-11-18-gemini-3-pro-is-now-available-in-github-copilot-cli\|Gemini 3 Pro is now available in GitHub Copilot CLI]]<br><time datetime="2025-11-13">2025-11-13</time> [[Changes/GitHub Copilot CLI/2025-11-13-gpt-5-1-gpt-5-1-codex-and-gpt-5-1-codex-mini-are-now-available-in-github-copilot\|GPT-5.1, GPT-5.1-Codex, and GPT-5.1-Codex-Mini are now available in GitHub Copilot CLI]]<br><time datetime="2025-10-02">2025-10-02</time> [[Changes/GitHub Copilot CLI/2025-10-02-added-usage-slash-command-to-provide-stats-about-premium-request-usage-session-t\|Added /usage slash command to provide stats about Premium request usage, session…]] | · | · |
| 2025 Q2 → 2025 Q3 | · | · | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2025-06-30">2025-06-30</time> | · | archive begins <time datetime="2025-06-28">2025-06-28</time> | archive begins <time datetime="2025-09-26">2025-09-26</time> | · | archive begins <time datetime="2025-04-02">2025-04-02</time> |
| 2025 Q1 | <time datetime="2025-03-13">2025-03-13</time> [[Changes/Aider/2025-03-13-added-reasoning-effort-command-to-control-model-reasoning-level\|Added /reasoning-effort command to control model reasoning level]] | · | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> |

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
<summary>2026 · 450 entries (ChatGPT 37 · Claude Code 96 · Cline 68 · Codex CLI 86 · Cursor 14 · Gemini CLI 28 · GitHub Copilot CLI 89 · OpenHands 18 · Windsurf 14)</summary>

**2026-10**

- 2026-10-31 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-31-deprecated-fast-mode-for-opus-4-8-as-of-october-30-2026-it-will-be-removed-on-no|Deprecated fast mode for Opus 4.8 as of October 30, 2026]] · Policy
- 2026-10-07 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-10-07-we-re-introducing-gpt-6-with-intelligent-ui-in-chatgpt-chatgpt-can-now-combine-t|GPT-6 and Intelligent UI in ChatGPT]] · Launch

**2026-09**

- 2026-09-14 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-14-we-re-retiring-automatic-switching-from-instant-to-thinking-reasoning-for-chatgp|Changes to automatic switching to thinking in ChatGPT (Plus and Pro)]] · Policy
- 2026-09-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-09-gpt-6-astra-is-now-available-in-the-model-picker-and-amazon-bedrock-catalogs-428|GPT-6-Astra is now available in the model picker and Amazon Bedrock catalogs]] · Expansion
- 2026-09-03 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-03-today-we-re-introducing-gpt-6-astra-with-improvements-in-coding-research-compute-069f67|Introducing GPT-6 Astra]] · Launch

**2026-08**

- 2026-08-26 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-26-added-claude-api-cost-optimize-to-profile-an-existing-project-s-claude-api-spend|Added /claude-api cost-optimize to profile an existing project's Claude API spend…]] · Change

**2026-07**

- 2026-07-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-07-22-optimization-modes-e62142|Optimization modes]] · Launch

**2026-06**

- 2026-06-30 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-30-introducing-claude-sonnet-5-now-the-default-model-in-claude-code-with-a-native-1|Introducing Claude Sonnet 5]] · Launch
- 2026-06-26 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-26-as-of-june-26-2026-gpt-4-5-is-no-longer-available-in-chatgpt-including-for-custo|Retiring GPT-4.5]] · Policy
- 2026-06-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-19-added-a-warning-when-the-requested-model-is-deprecated-or-automatically-updated|Added a warning when the requested model is deprecated or automatically updated…]] · Policy
- 2026-06-12 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-12-as-of-june-12-2026-gpt-5-2-models-are-no-longer-available-in-chatgpt-this-applie|Retiring GPT-5.2 models]] · Policy
- 2026-06-09 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-09-introducing-claude-fable-5-a-mythos-class-model-that-we-ve-made-safe-for-general|Introducing Claude Fable 5: a Mythos-class model that we’ve made safe for general use]] · Launch

**2026-05**

- 2026-05-30 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-30-auto-mode-is-now-available-on-bedrock-vertex-and-foundry-for-opus-4-7-and-opus-4|Auto mode is now available on Bedrock, Vertex, and Foundry for Opus 4.7 and Opus 4.8]] · Expansion
- 2026-05-28 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-05-28-today-we-re-continuing-to-retire-older-models-with-limited-usage-in-chatgpt-so-w|Retiring OpenAI o3 and GPT-4.5]] · Policy
- 2026-05-12 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-12-display-a-warning-when-the-cli-version-is-deprecated-and-premium-model-access-ma|Display a warning when the CLI version is deprecated and premium model access may be lost]] · Policy
- 2026-05-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-04-model-access-controls-d2ba4f|Model access controls]] · Launch

**2026-04**

- 2026-04-16 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-16-auto-mode-is-now-available-for-max-subscribers-when-using-opus-4-7|Auto mode is now available for Max subscribers when using Opus 4.7]] · Expansion
- 2026-04-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-04-09-today-we-re-releasing-gpt-5-3-instant-mini-in-chatgpt-it-replaces-gpt-5-instant|GPT-5.3 Instant mini in ChatGPT]] · Launch
- 2026-04-08 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-04-08-adaptive-fix|Adaptive Fix]] · Launch
- 2026-04-07 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-04-07-adaptive-model-visibility|Adaptive Model Visibility]] · Launch
- 2026-04-06 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-04-06-adaptive-model-router|Adaptive Model Router]] · Launch
- 2026-04-06 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-04-06-introducing-adaptive|Introducing Adaptive]] · Launch

**2026-03**

- 2026-03-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-14-added-effort-slash-command-to-set-model-effort-level|Added /effort slash command to set model effort level]] · Change
- 2026-03-11 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-03-11-as-of-march-11-2026-gpt-5-1-models-are-no-longer-available-in-chatgpt-this-appli|Retiring GPT-5.1 models]] · Policy

**2026-02**

- 2026-02-25 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-02-25-new-model-picker|New Model Picker]] · Launch
- 2026-02-13 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-02-13-as-previously-announced-we-have-retired-gpt-4o-gpt-4-1-gpt-4-1-mini-and-openai-o|Retiring GPT-4o and other legacy models]] · Policy
- 2026-02-12 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-12-add-streamer-mode-to-hide-preview-model-names-and-quota-details-for-streaming|Add /streamer-mode to hide preview model names and quota details for streaming]] · Policy
- 2026-02-07 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-07-fast-mode-is-now-available-for-opus-4-6-learn-more-at-https-code-claude-com-docs|Fast mode is now available for Opus 4.6]] · Launch
- 2026-02-05 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-05-claude-opus-4-6-is-now-available|Claude Opus 4.6 is now available!]] · Launch
- 2026-02-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-05-introducing-gpt-5-3-codex-learn-more-https-openai-com-index-introducing-gpt-5-3|Introducing GPT-5.3-Codex]] · Launch
- 2026-02-05 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-02-05-claude-opus-4-6|Claude Opus 4.6]] · Launch
- 2026-02-05 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-02-05-new-models|New Models]] · Launch
- 2026-02-05 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-02-05-claude-opus-4-6-fast-mode|Claude Opus 4.6 (fast mode)]] · Launch
- 2026-02-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-04-added-websocket-side-rate-limit-signaling-via-a-new-codex-rate-limits-event-with|Added websocket-side rate limit signaling via a new codex.rate_limits event…]] · Policy

**2026-01**

- 2026-01-30 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-01-30-arena-mode|Arena Mode]] · Launch
- 2026-01-30 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-01-30-wave-14-arena-mode|Wave 14: Arena Mode]] · Launch
- 2026-01-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-01-29-on-february-13-2026-alongside-the-previously-announced-retirement-of-gpt-5-insta|Retiring GPT-4o and other legacy models]] · Policy
- 2026-01-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-01-22-added-max-mode-on-off-to-toggle-max-mode-on-models-that-support-it-in-cli|Added /max-mode on / off to toggle max mode on models that support it in CLI]] · Change
- 2026-01-20 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-01-20-we-re-rolling-out-an-age-prediction-model-on-chatgpt-consumer-plans-to-help-dete|Rolling out age prediction]] · Policy
- 2026-01-14 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-01-14-gpt-5-2-codex|GPT-5.2-Codex]] · Launch
- 2026-01-08 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-01-08-use-the-new-agent-models-command-list-models-flag-or-models-slash-command-to-lis|Model list and selection]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 409 (ChatGPT 26 · Claude Code 86 · Cline 68 · Codex CLI 83 · Cursor 10 · Gemini CLI 28 · GitHub Copilot CLI 87 · OpenHands 18 · Windsurf 3)</summary>

**2026-11**

- 2026-11-06 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-11-06-7-model-support-changes-in-rust-v0-167-0|7 Model Support changes in rust-v0.167.0]] · Digest
- 2026-11-06 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-11-06-33-model-support-changes-in-v1-0-106|33 Model Support changes in v1.0.106]] · Digest
- 2026-11-04 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-11-04-feat-cli-add-models-command-and-list-models-flag-for-model-discovery-by-urielefr|feat(cli): add models command and --list-models flag for model discovery]] · Change

**2026-10**

- 2026-10-30 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-30-2-model-support-changes-in-v2-1-314|2 Model Support changes in v2.1.314]] · Digest
- 2026-10-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-29-10-model-support-changes-in-rust-v0-166-0|10 Model Support changes in rust-v0.166.0]] · Digest
- 2026-10-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-27-3-model-support-changes-in-v2-1-312|3 Model Support changes in v2.1.312]] · Digest
- 2026-10-27 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-27-9-model-support-changes-in-rust-v0-165-0|9 Model Support changes in rust-v0.165.0]] · Digest
- 2026-10-27 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-10-27-add-banner-about-gemini-cli-not-being-optimized-for-gemini-4-by-srithreepo-in-ht|Add Banner about Gemini CLI not being optimized for Gemini 4]] · Change
- 2026-10-27 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-27-managed-model-fusion-now-starts-sessions-on-auto-and-applies-fusiontier-settings|Managed model "fusion" now starts sessions on Auto and applies fusionTier settings]] · Change
- 2026-10-27 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-10-27-refactor-settings-use-existing-model-profile-theme-aliases-by-enyst-in-https-git|refactor(settings): use existing model-profile theme aliases]] · Change
- 2026-10-26 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-10-26-gpt-6-1-terra-is-rolling-out-in-chatgpt-work-and-codex-it-supports-a-range-of-ta|GPT-6.1 Terra]] · Change
- 2026-10-26 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-26-5-model-support-changes-in-v2-1-311|5 Model Support changes in v2.1.311]] · Digest
- 2026-10-26 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-10-26-10-model-support-changes-in-v4-1-26|10 Model Support changes in v4.1.26]] · Digest
- 2026-10-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-23-9-model-support-changes-in-rust-v0-164-0|9 Model Support changes in rust-v0.164.0]] · Digest
- 2026-10-22 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-22-3-model-support-changes-in-v1-0-103|3 Model Support changes in v1.0.103]] · Digest
- 2026-10-21 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-21-prompt-mode-now-honors-managed-auto-model-selection-for-p-and-piped-stdin-runs|Prompt mode now honors managed Auto model selection for -p and piped stdin runs]] · Change
- 2026-10-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-20-8-model-support-changes-in-v1-0-101|8 Model Support changes in v1.0.101]] · Digest
- 2026-10-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-19-2-model-support-changes-in-v2-1-304|2 Model Support changes in v2.1.304]] · Digest
- 2026-10-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-19-3-model-support-changes-in-v1-0-100|3 Model Support changes in v1.0.100]] · Digest
- 2026-10-16 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-10-16-gpt-6-pro-in-the-chat-tab-now-offers|GPT-6 Pro in the chat tab now offers]] · Change
- 2026-10-16 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-16-improved-the-message-when-a-background-session-reopened-from-another-folder-has|Improved the message when a background session reopened from another folder has no…]] · Change
- 2026-10-16 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-10-16-4-model-support-changes-in-v4-1-25|4 Model Support changes in v4.1.25]] · Digest
- 2026-10-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-15-6-model-support-changes-in-rust-v0-163-0|6 Model Support changes in rust-v0.163.0]] · Digest
- 2026-10-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-14-2-model-support-changes-in-v2-1-299|2 Model Support changes in v2.1.299]] · Digest
- 2026-10-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-14-improved-the-note-claude-3-models-get-about-an-mentioned-pdf-so-they-less-often|Improved the note Claude 3 models get about an @-mentioned PDF, so they less often…]] · Change
- 2026-10-14 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-14-add-support-for-gemini-4-argon|Add support for Gemini 4 Argon]] · Change
- 2026-10-13 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-10-13-3-model-support-changes-in-v4-1-24|3 Model Support changes in v4.1.24]] · Digest
- 2026-10-12 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-12-2-model-support-changes-in-v1-0-96|2 Model Support changes in v1.0.96]] · Digest
- 2026-10-12 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-10-12-3-model-support-changes-in-v1-27-0|3 Model Support changes in v1.27.0]] · Digest
- 2026-10-09 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-09-claude-tag-changed-claude-in-slack-to-show-the-footer-with-the-session-link-mode|Claude Tag Changed Claude in Slack to show the footer with the session link, model…]] · Change
- 2026-10-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-08-3-model-support-changes-in-v2-1-295|3 Model Support changes in v2.1.295]] · Digest
- 2026-10-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-08-11-model-support-changes-in-rust-v0-162-0|11 Model Support changes in rust-v0.162.0]] · Digest
- 2026-10-08 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-08-add-claude-haiku-5-5-to-model-selection-and-model-completions|Add Claude Haiku 5.5 to model selection and --model completions]] · Change
- 2026-10-08 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-10-08-test-e2e-launch-the-same-model-profile-test-from-the-beta-profile-by-enyst-in-ht|test(e2e): launch the same-model profile test from the BETA profile]] · Change
- 2026-10-07 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-07-added-claude-haiku-5-5-claude-haiku-5-5-now-the-default-haiku-model-on-the-anthr|Added Claude Haiku 5.5 (claude-haiku-5-5), now the default Haiku model…]] · Change
- 2026-10-07 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-10-07-3-model-support-changes-in-v4-1-23|3 Model Support changes in v4.1.23]] · Digest
- 2026-10-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-07-9-model-support-changes-in-rust-v0-161-0|9 Model Support changes in rust-v0.161.0]] · Digest
- 2026-10-07 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-07-model-picker-updates-the-recommended-list-to-prioritize-gpt-6-1-sol-gpt-6-astra|Model picker updates the recommended list to prioritize GPT-6.1 Sol, GPT-6…]] · Change
- 2026-10-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-06-added-prompt-caching-to-model-complete-for-mods-prompt-and-system-take-blocks-of|Added prompt caching to $.model.complete for mods]] · Change
- 2026-10-06 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-10-06-7-model-support-changes-in-v1-25-0|7 Model Support changes in v1.25.0]] · Digest
- 2026-10-05 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-05-2-model-support-changes-in-v2-1-290|2 Model Support changes in v2.1.290]] · Digest
- 2026-10-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-05-2-model-support-changes-in-v1-0-92|2 Model Support changes in v1.0.92]] · Digest
- 2026-10-02 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-02-changed-the-client-side-auto-mode-classifier-to-ignore-an-anthropic-default-sonn|Changed the client-side auto mode classifier to ignore…]] · Change
- 2026-10-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-01-4-model-support-changes-in-v2-1-287|4 Model Support changes in v2.1.287]] · Digest
- 2026-10-01 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-01-5-model-support-changes-in-rust-v0-160-0|5 Model Support changes in rust-v0.160.0]] · Digest

**2026-09**

- 2026-09-30 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-30-changed-how-failed-api-requests-are-retried-one-limit-now-covers-a-whole-model-c|Changed how failed API requests are retried]] · Change
- 2026-09-30 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-09-30-6-model-support-changes-in-v4-1-22|6 Model Support changes in v4.1.22]] · Digest
- 2026-09-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-30-2-model-support-changes-in-v1-0-90|2 Model Support changes in v1.0.90]] · Digest
- 2026-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-29-gpt-6-1-sol-improves-on-gpt-6-sol-in-agentic-coding-computer-use-and-professiona-815850|GPT-6.1 Sol in ChatGPT Work and Codex]] · Change
- 2026-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-29-eligible-plus-and-pro-users-can-authorize-participating-apps-to-use-their-chatgp|Eligible Plus and Pro users can authorize participating apps to use their ChatGPT…]] · Change
- 2026-09-29 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-29-3-model-support-changes-in-v2-1-285|3 Model Support changes in v2.1.285]] · Digest
- 2026-09-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-29-3-model-support-changes-in-rust-v0-159-0|3 Model Support changes in rust-v0.159.0]] · Digest
- 2026-09-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-29-2-model-support-changes-in-rust-v0-159-1|2 Model Support changes in rust-v0.159.1]] · Digest
- 2026-09-29 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-09-29-feat-gemini-3-8-flash-3-5-flash-lite-by-davidapierce-in-https-github-com-google|Feat/gemini 3.8 flash 3.5 flash lite]] · Change
- 2026-09-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-28-6-model-support-changes-in-v2-1-284|6 Model Support changes in v2.1.284]] · Digest
- 2026-09-28 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-28-7-model-support-changes-in-rust-v0-158-0|7 Model Support changes in rust-v0.158.0]] · Digest
- 2026-09-28 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-28-5-model-support-changes-in-v1-0-89|5 Model Support changes in v1.0.89]] · Digest
- 2026-09-25 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-25-3-model-support-changes-in-v2-1-283|3 Model Support changes in v2.1.283]] · Digest
- 2026-09-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-25-8-model-support-changes-in-rust-v0-157-0|8 Model Support changes in rust-v0.157.0]] · Digest
- 2026-09-24 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-24-2-model-support-changes-in-v2-1-282|2 Model Support changes in v2.1.282]] · Digest
- 2026-09-24 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-09-24-3-model-support-changes-in-v4-1-21|3 Model Support changes in v4.1.21]] · Digest
- 2026-09-23 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-23-improved-interactive-startup-time-git-reads-startup-telemetry-and-the-bedrock-ve|Improved interactive startup time]] · Change
- 2026-09-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-23-2-model-support-changes-in-rust-v0-156-1|2 Model Support changes in rust-v0.156.1]] · Digest
- 2026-09-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-22-5-model-support-changes-in-v2-1-280|5 Model Support changes in v2.1.280]] · Digest
- 2026-09-22 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-09-22-3-model-support-changes-in-v4-1-20|3 Model Support changes in v4.1.20]] · Digest
- 2026-09-22 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-22-25-model-support-changes-in-rust-v0-156-0|25 Model Support changes in rust-v0.156.0]] · Digest
- 2026-09-22 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-09-22-test-strengthen-llm-profile-configuration-by-aivong-openhands-in-https-github-co|test: strengthen LLM profile configuration]] · Change
- 2026-09-21 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-21-enable-the-rubber-duck-agent-for-every-model-family-and-for-low-cost-tier-sessio|Enable the rubber-duck agent for every model family and for low-cost-tier session models]] · Change
- 2026-09-18 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-18-changed-fable-to-always-appear-in-model-on-the-anthropic-api-it-is-greyed-out-on|Changed Fable to always appear in /model on the Anthropic API]] · Change
- 2026-09-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-18-2-model-support-changes-in-rust-v0-155-1|2 Model Support changes in rust-v0.155.1]] · Digest
- 2026-09-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-17-2-model-support-changes-in-v2-1-274|2 Model Support changes in v2.1.274]] · Digest
- 2026-09-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-17-added-a-send-now-key-ctrl-enter-or-ctrl-x-ctrl-s-that-interrupts-the-current-tur|Added a send-now key (ctrl+enter, or ctrl+x ctrl+s) that interrupts the current turn…]] · Change
- 2026-09-17 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-09-17-13-model-support-changes-in-v4-1-19|13 Model Support changes in v4.1.19]] · Digest
- 2026-09-17 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-17-13-model-support-changes-in-rust-v0-155-0|13 Model Support changes in rust-v0.155.0]] · Digest
- 2026-09-17 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-17-expanded-reasoning-text-in-the-compact-timeline-is-no-longer-dimmed-so-it-is-as|Expanded reasoning text in the compact timeline is no longer dimmed, so it…]] · Change
- 2026-09-17 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-09-17-test-isolate-mock-llm-profiles-from-ambient-secrets-by-neubig-in-https-github-co|test: isolate Mock-LLM profiles from ambient secrets]] · Change
- 2026-09-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-16-13-model-support-changes-in-v1-0-85|13 Model Support changes in v1.0.85]] · Digest
- 2026-09-16 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-09-16-feat-add-gpt-6-astra-model-support-by-neubig-in-https-github-com-openhands-openh|feat: add GPT-6 Astra model support]] · Change
- 2026-09-15 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-15-changed-bug-and-feedback-reports-to-include-only-model-behavior-params-model-sys|Changed /bug and /feedback reports to include only model-behavior params…]] · Change
- 2026-09-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-14-2-model-support-changes-in-v2-1-271|2 Model Support changes in v2.1.271]] · Digest
- 2026-09-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-11-added-claude-code-gateway-model-discovery-timeout-ms-to-extend-the-llm-gateway-v|Added CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS to extend the LLM gateway…]] · Change
- 2026-09-10 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-10-2-model-support-changes-in-v2-1-268|2 Model Support changes in v2.1.268]] · Digest
- 2026-09-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-09-chatgpt-voice-can-now-use-gpt-5-6-or-gpt-6-astra-when-it-needs-to-search-or-reas-848954|ChatGPT Voice can now use GPT-5.6 or GPT-6 Astra when it needs to search or reason…]] · Change
- 2026-09-09 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-09-added-maxeffortlevel-setting-top-level-or-per-model-under-modelsettings-caps-the|Added maxEffortLevel setting (top-level or per model under modelSettings)]] · Change
- 2026-09-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-09-21-model-support-changes-in-rust-v0-154-0|21 Model Support changes in rust-v0.154.0]] · Digest
- 2026-09-09 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-09-09-feat-enable-llm-provider-connections-on-cloud-by-juanmichelini-in-https-github-c|feat: enable LLM provider connections on cloud]] · Change
- 2026-09-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-04-improved-the-model-picker-and-the-vs-code-model-pill-to-show-a-model-s-name-inst|Improved the /model picker and the VS Code model pill to show a model's name…]] · Change
- 2026-09-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-04-3-model-support-changes-in-rust-v0-153-3|3 Model Support changes in rust-v0.153.3]] · Digest
- 2026-09-04 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-04-3-model-support-changes-in-v1-0-83|3 Model Support changes in v1.0.83]] · Digest
- 2026-09-03 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-03-2-model-support-changes-in-v2-1-260|2 Model Support changes in v2.1.260]] · Digest
- 2026-09-03 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-03-2-model-support-changes-in-rust-v0-153-0|2 Model Support changes in rust-v0.153.0]] · Digest
- 2026-09-03 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-03-2-model-support-changes-in-rust-v0-153-1|2 Model Support changes in rust-v0.153.1]] · Digest
- 2026-09-03 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-03-2-model-support-changes-in-rust-v0-153-2|2 Model Support changes in rust-v0.153.2]] · Digest
- 2026-09-02 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-09-02-3-model-support-changes-in-v4-1-17|3 Model Support changes in v4.1.17]] · Digest
- 2026-09-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-01-6-model-support-changes-in-v2-1-257|6 Model Support changes in v2.1.257]] · Digest
- 2026-09-01 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-01-6-model-support-changes-in-rust-v0-152-0|6 Model Support changes in rust-v0.152.0]] · Digest
- 2026-09-01 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-01-guardian-approval-review-now-honors-node-repl-policies-provided-through-model-me|Guardian approval review now honors Node REPL policies provided through model metadata]] · Change

**2026-08**

- 2026-08-31 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-08-31-site-tools-use-webmcp-and-require-a-supported-account-model-and-webpage-they-are|Site tools use WebMCP and require a supported account, model, and webpage]] · Change
- 2026-08-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-29-3-model-support-changes-in-rust-v0-151-0|3 Model Support changes in rust-v0.151.0]] · Digest
- 2026-08-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-28-5-model-support-changes-in-v2-1-251|5 Model Support changes in v2.1.251]] · Digest
- 2026-08-27 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-27-4-model-support-changes-in-v1-0-81|4 Model Support changes in v1.0.81]] · Digest
- 2026-08-27 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-08-27-2-model-support-changes-in-v1-16-0|2 Model Support changes in v1.16.0]] · Digest
- 2026-08-26 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-26-credentials-embedded-in-git-remote-urls-are-now-redacted-from-the-workspace-info|Credentials embedded in git remote URLs are now redacted from the workspace…]] · Change
- 2026-08-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-26-10-model-support-changes-in-rust-v0-150-0|10 Model Support changes in rust-v0.150.0]] · Digest
- 2026-08-23 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-23-refresh-the-built-in-model-catalog-new-entries-include-claude-fable-5-grok-4-6-o|Refresh the built-in model catalog]] · Change
- 2026-08-22 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-22-restore-tool-calling-for-custom-openai-compatible-models-whose-capability-list-w|Restore tool calling for custom OpenAI-Compatible models whose capability list…]] · Change
- 2026-08-21 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-21-restore-tool-calling-for-custom-openai-compatible-models-whose-stored-capability|Restore tool calling for custom OpenAI-Compatible models whose stored capability…]] · Change
- 2026-08-21 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-21-3-model-support-changes-in-v4-1-11|3 Model Support changes in v4.1.11]] · Digest
- 2026-08-21 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-08-21-perf-batch-streamingdeltaevents-so-the-ui-keeps-up-with-fast-models-by-vascosch9|perf: batch StreamingDeltaEvents so the UI keeps up with fast models]] · Change
- 2026-08-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-20-6-model-support-changes-in-rust-v0-149-0|6 Model Support changes in rust-v0.149.0]] · Digest
- 2026-08-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-19-added-anthropic-default-model-environment-variable-sets-the-model-new-sessions-s|Added ANTHROPIC_DEFAULT_MODEL environment variable]] · Change
- 2026-08-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-18-18-model-support-changes-in-rust-v0-148-0|18 Model Support changes in rust-v0.148.0]] · Digest
- 2026-08-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-17-2-model-support-changes-in-v2-1-234|2 Model Support changes in v2.1.234]] · Digest
- 2026-08-17 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-08-17-feat-add-llm-pre-flight-validation-to-prevent-saving-misconfigured-profiles-by-n|feat: add LLM pre-flight validation to prevent saving misconfigured profiles]] · Change
- 2026-08-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-14-2-model-support-changes-in-v2-1-233|2 Model Support changes in v2.1.233]] · Digest
- 2026-08-14 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-14-2-model-support-changes-in-v4-1-10|2 Model Support changes in v4.1.10]] · Digest
- 2026-08-14 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-14-update-model-configurations|Update model configurations]] · Change
- 2026-08-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-11-changed-the-write-tool-so-newer-models-can-overwrite-an-existing-file-they-haven|Changed the Write tool so newer models can overwrite an existing file they haven't…]] · Change
- 2026-08-11 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-11-2-model-support-changes-in-v4-1-8|2 Model Support changes in v4.1.8]] · Digest
- 2026-08-11 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-08-11-2-model-support-changes-in-v0-55-1|2 Model Support changes in v0.55.1]] · Digest
- 2026-08-10 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-10-3-model-support-changes-in-v1-0-79|3 Model Support changes in v1.0.79]] · Digest
- 2026-08-09 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-09-retry-network-interruptions-that-happen-mid-stream-but-before-any-model-output-i|Retry network interruptions that happen mid-stream but before any model output…]] · Change
- 2026-08-07 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-07-changed-the-bash-tool-description-to-always-note-that-command-output-is-displaye|Changed the Bash tool description to always note that command output is displayed…]] · Change
- 2026-08-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-07-13-model-support-changes-in-rust-v0-147-0|13 Model Support changes in rust-v0.147.0]] · Digest
- 2026-08-07 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-08-07-feat-clarify-free-openhands-model-endpoints-by-juanmichelini-in-https-github-com|feat: clarify free OpenHands model endpoints]] · Change
- 2026-08-07 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-08-07-feat-show-per-run-llm-cost-in-the-activity-log-and-exports-by-hieptl-in-https-gi|feat: show per-run LLM cost in the Activity Log and exports]] · Change
- 2026-08-06 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-08-06-plus-and-pro-users-can-now-use-an-updated-gpt-5-6-sol-in-chatgpt-with-more-relia-397840|Updates to GPT‑5.6 in ChatGPT]] · Change
- 2026-08-06 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-06-2-model-support-changes-in-v4-1-6|2 Model Support changes in v4.1.6]] · Digest
- 2026-08-05 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-05-5-model-support-changes-in-v4-1-4|5 Model Support changes in v4.1.4]] · Digest
- 2026-08-05 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-05-explain-when-a-free-model-promotion-ends-requests-to-a-retired-free-model-now-sh|Explain when a free model promotion ends]] · Change
- 2026-08-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-05-37057-0-146-backport-safer-cyber-model-auto-review-defaults-anp-oai|♯37057 0.146 Backport safer cyber-model auto-review defaults @anp-oai]] · Change
- 2026-08-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-04-3-model-support-changes-in-v2-1-221|3 Model Support changes in v2.1.221]] · Digest
- 2026-08-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-04-improved-the-refusal-when-claude-tries-to-invoke-a-skill-with-disable-model-invo|Improved the refusal when Claude tries to invoke a skill with disable-model-invocation]] · Change
- 2026-08-03 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-03-the-allow-all-auto-safety-judge-model-is-no-longer-user-configurable-the-judge-m|The /allow-all auto safety-judge model is no longer user-configurable]] · Change
- 2026-08-02 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-02-4-model-support-changes-in-v4-1-3|4 Model Support changes in v4.1.3]] · Digest

**2026-07**

- 2026-07-31 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-07-31-legacy-bundle-legacy-extension-3fdc186f1-4-0-12-free-model-button-wording|Legacy bundle: legacy-extension @ 3fdc186f1 (4.0.12 + free-model button wording)]] · Change
- 2026-07-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-30-allow-reasoning-effort-to-be-omitted-so-the-server-can-select-the-default|Allow reasoning effort to be omitted so the server can select the default]] · Change
- 2026-07-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-30-2-model-support-changes-in-v1-0-76|2 Model Support changes in v1.0.76]] · Digest
- 2026-07-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-29-3-model-support-changes-in-rust-v0-146-0|3 Model Support changes in rust-v0.146.0]] · Digest
- 2026-07-28 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-07-28-add-support-for-free-cline-models-shown-as-free-in-the-model-picker-with-a-dedic|Add support for free Cline models, shown as "(free)" in the model picker…]] · Change
- 2026-07-28 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-07-28-2-model-support-changes-in-v0-53-0|2 Model Support changes in v0.53.0]] · Digest
- 2026-07-24 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-24-3-model-support-changes-in-v2-1-219|3 Model Support changes in v2.1.219]] · Digest
- 2026-07-24 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-07-24-2-model-support-changes-in-v4-0-11|2 Model Support changes in v4.0.11]] · Digest
- 2026-07-24 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-24-add-support-for-claude-opus-5|Add support for Claude Opus 5]] · Change
- 2026-07-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-23-2-model-support-changes-in-v1-0-74|2 Model Support changes in v1.0.74]] · Digest
- 2026-07-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-22-added-an-announcement-when-fast-mode-changes-as-a-result-of-switching-models-via|Added an announcement when fast mode changes as a result of switching models…]] · Change
- 2026-07-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-07-22-cursor-router-is-our-intelligent-model-router-it-analyzes-each-request-and-sends|Cursor Router is our intelligent model router]] · Change
- 2026-07-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-07-22-routed-model-can-be-displayed-or-hidden-hidden-by-default|Routed model can be displayed or hidden (hidden by default)]] · Change
- 2026-07-21 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-21-22-model-support-changes-in-rust-v0-145-0|22 Model Support changes in rust-v0.145.0]] · Digest
- 2026-07-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-20-preserve-pasted-prompt-content-when-changing-models-through-ctrl-x-model|Preserve pasted prompt content when changing models through Ctrl+X /model]] · Change
- 2026-07-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-18-3-model-support-changes-in-rust-v0-144-6|3 Model Support changes in rust-v0.144.6]] · Digest
- 2026-07-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-17-3-model-support-changes-in-v2-1-212|3 Model Support changes in v2.1.212]] · Digest
- 2026-07-16 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-07-16-add-gpt-5-6-chatgpt-subscription-models|Add GPT-5.6 ChatGPT subscription models]] · Change
- 2026-07-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-16-3-model-support-changes-in-v1-0-71|3 Model Support changes in v1.0.71]] · Digest
- 2026-07-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-14-improved-the-bash-powershell-tool-message-when-a-command-hits-its-timeout-and-is|Improved the Bash/PowerShell tool message when a command hits its timeout…]] · Change
- 2026-07-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-11-changed-bedrock-vertex-and-claude-platform-on-aws-to-default-to-claude-opus-4-8|Changed Bedrock, Vertex, and Claude Platform on AWS to default to Claude Opus 4.8]] · Change
- 2026-07-11 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-07-11-add-more-models-to-the-gcp-vertex-provider-plus-a-free-form-entry-option-in-the|Add more models to the GCP Vertex provider, plus a free-form entry option…]] · Change
- 2026-07-10 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-10-improved-code-review-findings-quality-on-claude-opus-4-8-across-all-effort-level|Improved /code-review findings quality on claude-opus-4-8 across all effort levels]] · Change
- 2026-07-10 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-10-4-model-support-changes-in-v1-0-70|4 Model Support changes in v1.0.70]] · Digest
- 2026-07-09 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-07-09-allow-selecting-cline-free-models-on-the-clinepass-provider-organized-into-subsc|Allow selecting Cline free models on the ClinePass provider, organized…]] · Change
- 2026-07-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-09-8-model-support-changes-in-rust-v0-144-0|8 Model Support changes in rust-v0.144.0]] · Digest
- 2026-07-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-08-14-model-support-changes-in-rust-v0-143-0|14 Model Support changes in rust-v0.143.0]] · Digest
- 2026-07-07 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-07-6-model-support-changes-in-v1-0-69|6 Model Support changes in v1.0.69]] · Digest
- 2026-07-06 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-07-06-we-re-rolling-out-gpt-5-5-instant-mini-in-chatgpt-it-replaces-gpt-5-3-instant-mi|GPT-5.5 Instant Mini in ChatGPT]] · Change
- 2026-07-06 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-07-06-4-model-support-changes-in-1-9-0|4 Model Support changes in 1.9.0]] · Digest
- 2026-07-03 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-03-claude-sonnet-5-sessions-no-longer-use-the-mid-conversation-system-role-for-harn|Claude Sonnet 5 sessions no longer use the mid-conversation system role for harness…]] · Change
- 2026-07-02 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-07-02-generalize-the-model-capability-warning-so-it-applies-more-broadly|Generalize the model capability warning so it applies more broadly]] · Change
- 2026-07-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-01-2-model-support-changes-in-v2-1-198|2 Model Support changes in v2.1.198]] · Digest
- 2026-07-01 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-01-add-support-for-the-kimi-k2-7-code-model|Add support for the kimi-k2.7-code model]] · Change

**2026-06**

- 2026-06-30 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-06-30-add-support-for-claude-sonnet-5-across-the-anthropic-bedrock-vertex-claude-code|Add support for Claude Sonnet 5 across the Anthropic, Bedrock, Vertex, Claude Code…]] · Change
- 2026-06-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-30-add-claude-sonnet-5-as-a-supported-model|Add Claude Sonnet 5 as a supported model]] · Change
- 2026-06-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-30-5-model-support-changes-in-v1-0-66|5 Model Support changes in v1.0.66]] · Digest
- 2026-06-29 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-29-added-support-for-organization-default-models-admins-set-it-in-the-org-console-i|Added support for organization default models]] · Change
- 2026-06-29 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-06-29-4-model-support-changes-in-v4-0-2|4 Model Support changes in v4.0.2]] · Digest
- 2026-06-26 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-06-26-2-model-support-changes-in-v4-0-0|2 Model Support changes in v4.0.0]] · Digest
- 2026-06-25 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-25-added-claude-code-assistant-response-opentelemetry-log-event-containing-the-mode|Added claude_code.assistant_response OpenTelemetry log event containing…]] · Change
- 2026-06-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-25-4-model-support-changes-in-rust-v0-142-2|4 Model Support changes in rust-v0.142.2]] · Digest
- 2026-06-24 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-24-we-re-updating-gpt-5-5-instant-our-most-used-model-in-chatgpt-to-improve-convers|GPT-5.5 Instant Update]] · Change
- 2026-06-24 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-24-2-model-support-changes-in-v1-0-65|2 Model Support changes in v1.0.65]] · Digest
- 2026-06-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-23-7-model-support-changes-in-v1-0-64|7 Model Support changes in v1.0.64]] · Digest
- 2026-06-22 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-22-3-model-support-changes-in-rust-v0-142-0|3 Model Support changes in rust-v0.142.0]] · Digest
- 2026-06-18 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-18-long-press-send-to-choose-a-model-android-users-on-paid-plans-can-now-long-press|Long-press send to choose a model]] · Change
- 2026-06-18 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-06-18-vertex-ai-model-mapping-fix-by-davidapierce-in-https-github-com-google-gemini-ge|Vertex ai model mapping fix]] · Change
- 2026-06-15 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-15-bug-now-requires-a-description-before-submitting-and-no-longer-uses-model-refusa|/bug now requires a description before submitting, and no longer uses…]] · Change
- 2026-06-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-15-4-model-support-changes-in-rust-v0-140-0|4 Model Support changes in rust-v0.140.0]] · Digest
- 2026-06-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-13-3-model-support-changes-in-v1-0-62|3 Model Support changes in v1.0.62]] · Digest
- 2026-06-12 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-12-added-enforceavailablemodels-managed-setting-when-enabled-the-availablemodels-al|Added enforceAvailableModels managed setting]] · Change
- 2026-06-11 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-06-11-handle-the-deepseek-v4-reasoning-format|Handle the DeepSeek V4 reasoning format]] · Change
- 2026-06-10 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-10-pro-extended-pro-plans-only|Pro Extended Pro plans only]] · Change
- 2026-06-10 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-10-extra-high-pro-plans-only|Extra High Pro plans only]] · Change
- 2026-06-10 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-10-pro-standard-pro-plans-only|Pro Standard Pro plans only]] · Change
- 2026-06-10 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-10-2-model-support-changes-in-v2-1-172|2 Model Support changes in v2.1.172]] · Digest
- 2026-06-10 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-06-10-transition-to-flash-ga-model-when-experiment-flag-is-present-by-davidapierce-in|Transition to flash GA model when experiment flag is present]] · Change
- 2026-06-10 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-06-10-added-llm-profiles-by-vascosch92-in-https-github-com-openhands-openhands-pull-14|Added LLM profiles]] · Change
- 2026-06-09 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-06-09-2-model-support-changes-in-v3-89-0|2 Model Support changes in v3.89.0]] · Digest
- 2026-06-09 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-09-3-model-support-changes-in-v1-0-61|3 Model Support changes in v1.0.61]] · Digest
- 2026-06-08 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-08-long-press-send-to-choose-a-model-users-on-paid-plans-can-now-long-press-the-sen|Long-press send to choose a model]] · Change
- 2026-06-08 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-08-added-a-disablebundledskills-setting-and-claude-code-disable-bundled-skills-envi|Added a disableBundledSkills setting and CLAUDE_CODE_DISABLE_BUNDLED_SKILLS…]] · Change
- 2026-06-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-08-6-model-support-changes-in-rust-v0-138-0|6 Model Support changes in rust-v0.138.0]] · Digest
- 2026-06-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-06-3-model-support-changes-in-v2-1-166|3 Model Support changes in v2.1.166]] · Digest
- 2026-06-05 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-06-05-3-model-support-changes-in-v3-88-0|3 Model Support changes in v3.88.0]] · Digest
- 2026-06-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-05-2-model-support-changes-in-v1-0-60|2 Model Support changes in v1.0.60]] · Digest
- 2026-06-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-04-3-model-support-changes-in-rust-v0-137-0|3 Model Support changes in rust-v0.137.0]] · Digest
- 2026-06-03 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-03-2-model-support-changes-in-v2-1-162|2 Model Support changes in v2.1.162]] · Digest
- 2026-06-03 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-06-03-add-minimax-m3-model-support|Add MiniMax M3 model support]] · Change
- 2026-06-02 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-02-removed-claude-code-opus-4-6-fast-mode-override-the-environment-variable-is-now|Removed CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE; the environment variable is now a no-op]] · Change
- 2026-06-01 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-01-5-model-support-changes-in-rust-v0-136-0|5 Model Support changes in rust-v0.136.0]] · Digest
- 2026-06-01 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-01-new-reasoning-after-tool-calls-appears-at-the-bottom-of-the-timeline-instead-of|New reasoning after tool calls appears at the bottom of the timeline instead…]] · Change

**2026-05**

- 2026-05-29 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-29-2-model-support-changes-in-v1-0-56|2 Model Support changes in v1.0.56]] · Digest
- 2026-05-28 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-05-28-we-re-updating-gpt-5-5-instant-in-chatgpt-and-the-api-to-improve-response-style|GPT-5.5 Instant Update]] · Change
- 2026-05-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-28-5-model-support-changes-in-v2-1-154|5 Model Support changes in v2.1.154]] · Digest
- 2026-05-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-28-model-now-saves-your-selection-as-the-default-for-new-sessions-matching-the-ide|/model now saves your selection as the default for new sessions (matching the IDE)]] · Change
- 2026-05-28 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-05-28-2-model-support-changes-in-v3-86-0|2 Model Support changes in v3.86.0]] · Digest
- 2026-05-28 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-28-3-model-support-changes-in-v1-0-55|3 Model Support changes in v1.0.55]] · Digest
- 2026-05-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-27-2-model-support-changes-in-v2-1-152|2 Model Support changes in v2.1.152]] · Digest
- 2026-05-27 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-27-refactor-decouple-auto-model-description-and-configuration-from-releasechannel-b|refactor: decouple auto model description and configuration from releaseChannel]] · Change
- 2026-05-25 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-05-25-4-model-support-changes-in-v3-85-0|4 Model Support changes in v3.85.0]] · Digest
- 2026-05-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-23-general-purpose-subagents-use-gpt-5-4-or-gpt-5-5-when-available|General-purpose subagents use GPT-5.4 or GPT-5.5 when available]] · Change
- 2026-05-22 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-22-2-model-support-changes-in-v0-43-0|2 Model Support changes in v0.43.0]] · Digest
- 2026-05-21 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-21-18868-add-mitm-hook-config-model-evawong-oai|♯18868 Add MITM hook config model @evawong-oai]] · Change
- 2026-05-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-20-23069-multiagent-trim-model-visible-description-cap-to-5-models-sayan-oai|♯23069 multiagent: trim model-visible description, cap to 5 models @sayan-oai]] · Change
- 2026-05-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-20-shell-tool-calls-succeed-even-when-the-model-omits-the-description-parameter|Shell tool calls succeed even when the model omits the description parameter]] · Change
- 2026-05-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-19-resumed-sessions-now-keep-the-model-they-were-using-instead-of-picking-up-anothe|Resumed sessions now keep the model they were using instead of picking up another…]] · Change
- 2026-05-19 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-05-19-add-sap-ai-core-support-for-additional-hosted-models|Add SAP AI Core support for additional hosted models]] · Change
- 2026-05-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-19-2-model-support-changes-in-v1-0-49|2 Model Support changes in v1.0.49]] · Digest
- 2026-05-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-18-4-model-support-changes-in-rust-v0-131-0|4 Model Support changes in rust-v0.131.0]] · Digest
- 2026-05-18 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-18-composer-2-5-includes-double-usage-for-the-first-week-see-our-model-docs-for-ful|Composer 2.5 includes double usage for the first week]] · Change
- 2026-05-18 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-18-it-s-a-substantial-improvement-in-intelligence-and-behavior-over-composer-2-it-i|It's a substantial improvement in intelligence and behavior over Composer 2]] · Change
- 2026-05-15 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-15-2-model-support-changes-in-v2-1-143|2 Model Support changes in v2.1.143]] · Digest
- 2026-05-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-14-2-model-support-changes-in-v2-1-142|2 Model Support changes in v2.1.142]] · Digest
- 2026-05-14 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-14-2-model-support-changes-in-v1-0-48|2 Model Support changes in v1.0.48]] · Digest
- 2026-05-13 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-05-13-enable-openrouter-prompt-cache-control-for-qwen-models|Enable OpenRouter prompt cache control for Qwen models]] · Change
- 2026-05-12 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-12-5-model-support-changes-in-v0-42-0|5 Model Support changes in v0.42.0]] · Digest
- 2026-05-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-11-compaction-prompt-now-asks-the-model-to-preserve-sensitive-user-instructions|Compaction prompt now asks the model to preserve sensitive user instructions]] · Change
- 2026-05-11 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-11-high-bugbot-spends-more-time-reasoning-reviews-are-more-expensive-and-take-longe|High: Bugbot spends more time reasoning]] · Change
- 2026-05-11 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-11-custom-describe-in-natural-language-when-bugbot-should-use-default-or-high-effor|Custom: Describe in natural language when Bugbot should use default or high effort]] · Change
- 2026-05-08 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-08-3-model-support-changes-in-v1-0-44|3 Model Support changes in v1.0.44]] · Digest
- 2026-05-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-07-4-model-support-changes-in-rust-v0-129-0|4 Model Support changes in rust-v0.129.0]] · Digest
- 2026-05-07 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-07-added-support-for-general-model-names-for-subagent-configuration-i-e-set-model-o|Added support for general model names for subagent configuration (i.e., set model]] · Change
- 2026-05-06 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-06-2-model-support-changes-in-v2-1-129|2 Model Support changes in v2.1.129]] · Digest
- 2026-05-05 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-05-05-we-re-rolling-out-gpt-5-5-instant-as-chatgpt-s-new-default-model-it-replaces-gpt|GPT-5.5 Instant in ChatGPT]] · Change
- 2026-05-05 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-05-3-model-support-changes-in-v0-41-0|3 Model Support changes in v0.41.0]] · Digest
- 2026-05-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-04-updated-model-picker-collapsed-duplicate-opus-4-7-entries-and-current-opus-now-s|Updated /model picker]] · Change
- 2026-05-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-01-2-model-support-changes-in-v2-1-126|2 Model Support changes in v2.1.126]] · Digest
- 2026-05-01 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-05-01-2-model-support-changes-in-v3-82-0|2 Model Support changes in v3.82.0]] · Digest
- 2026-05-01 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-01-2-model-support-changes-in-v1-0-40|2 Model Support changes in v1.0.40]] · Digest
- 2026-05-01 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-05-01-added-llm-model-on-conversation-cards-and-header-by-sjathin-in-https-github-com|Added LLM model on conversation cards and header]] · Change

**2026-04**

- 2026-04-30 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-30-10-model-support-changes-in-rust-v0-128-0|10 Model Support changes in rust-v0.128.0]] · Digest
- 2026-04-28 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-04-28-we-re-making-it-easier-to-choose-the-right-model-before-you-send-a-message-model|Easier model selection in ChatGPT]] · Change
- 2026-04-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-28-opentelemetry-added-stop-reason-gen-ai-response-finish-reasons-and-user-system-p|OpenTelemetry: added stop_reason, gen_ai.response.finish_reasons…]] · Change
- 2026-04-28 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-28-2-model-support-changes-in-v0-40-0|2 Model Support changes in v0.40.0]] · Digest
- 2026-04-27 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-27-2-model-support-changes-in-v1-0-37|2 Model Support changes in v1.0.37]] · Digest
- 2026-04-24 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-04-24-add-gpt-5-5-model-support-for-openai-codex-subscription-users|Add GPT-5.5 model support for OpenAI Codex subscription users]] · Change
- 2026-04-24 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-24-5-model-support-changes-in-rust-v0-125-0|5 Model Support changes in rust-v0.125.0]] · Digest
- 2026-04-24 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-24-claude-opus-4-6-now-uses-medium-reasoning-effort-by-default|Claude Opus 4.6 now uses medium reasoning effort by default]] · Change
- 2026-04-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-6-model-support-changes-in-rust-v0-123-0|6 Model Support changes in rust-v0.123.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-4-model-support-changes-in-rust-v0-124-0|4 Model Support changes in rust-v0.124.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-23-2-model-support-changes-in-v0-39-0|2 Model Support changes in v0.39.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-23-2-model-support-changes-in-v1-0-35|2 Model Support changes in v1.0.35]] · Digest
- 2026-04-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-22-2-model-support-changes-in-v2-1-117|2 Model Support changes in v2.1.117]] · Digest
- 2026-04-22 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-04-22-onboarding-flow-now-uses-dynamically-fetched-recommended-models-instead-of-a-har|Onboarding flow now uses dynamically fetched recommended models instead…]] · Change
- 2026-04-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-20-6-model-support-changes-in-rust-v0-122-0|6 Model Support changes in rust-v0.122.0]] · Digest
- 2026-04-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-20-ctrl-t-to-toggle-reasoning-display-is-now-listed-in-the-help-and-overlay|ctrl+t to toggle reasoning display is now listed in the /help and ? overlay]] · Change
- 2026-04-16 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-16-3-model-support-changes-in-v2-1-111|3 Model Support changes in v2.1.111]] · Digest
- 2026-04-16 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-04-16-add-claude-opus-4-7-model-support|Add Claude Opus 4.7 model support]] · Change
- 2026-04-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-16-add-support-for-claude-opus-4-7|Add support for Claude Opus 4.7]] · Change
- 2026-04-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-15-3-model-support-changes-in-rust-v0-121-0|3 Model Support changes in rust-v0.121.0]] · Digest
- 2026-04-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-14-improved-model-to-warn-before-switching-models-mid-conversation-since-the-next-r|Improved /model to warn before switching models mid-conversation, since the next…]] · Change
- 2026-04-14 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-04-14-trigger-the-model-picker-from-anywhere-to-switch-models-without-clearing-your-pr|Trigger the model picker from anywhere to switch models without clearing your prompt first]] · Change
- 2026-04-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-13-the-config-dir-flag-is-now-respected-when-selecting-the-active-model|The --config-dir flag is now respected when selecting the active model]] · Change
- 2026-04-10 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-10-5-model-support-changes-in-rust-v0-119-0|5 Model Support changes in rust-v0.119.0]] · Digest
- 2026-04-10 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-10-custom-agent-model-field-now-accepts-display-names-and-vendor-suffixes-from-vs-c|Custom agent model field now accepts display names and vendor suffixes from VS Code…]] · Change
- 2026-04-10 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-10-display-reasoning-token-usage-in-the-per-model-token-breakdown-when-nonzero|Display reasoning token usage in the per-model token breakdown when nonzero]] · Change
- 2026-04-08 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-08-5-model-support-changes-in-v0-37-0|5 Model Support changes in v0.37.0]] · Digest
- 2026-04-04 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-04-new-critic-agent-automatically-reviews-plans-and-complex-implementations-using-a|New Critic agent automatically reviews plans and complex implementations using…]] · Change
- 2026-04-01 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-01-usage-now-hides-redundant-current-week-sonnet-only-bar-for-pro-and-enterprise-pl|/usage now hides redundant "Current week (Sonnet only)" bar for Pro and Enterprise plans]] · Change
- 2026-04-01 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-01-7-model-support-changes-in-v0-36-0|7 Model Support changes in v0.36.0]] · Digest
- 2026-04-01 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-01-remove-support-for-gpt-5-1-codex-gpt-5-1-codex-mini-and-gpt-5-1-codex-max-models|Remove support for gpt-5.1-codex, gpt-5.1-codex-mini, and gpt-5.1-codex-max models]] · Change

**2026-03**

- 2026-03-31 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-31-5-model-support-changes-in-rust-v0-118-0|5 Model Support changes in rust-v0.118.0]] · Digest
- 2026-03-31 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-31-3-model-support-changes-in-v1-0-14|3 Model Support changes in v1.0.14]] · Digest
- 2026-03-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-30-2-model-support-changes-in-v1-0-13|2 Model Support changes in v1.0.13]] · Digest
- 2026-03-26 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-26-added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef|Added ANTHROPIC_DEFAULT{OPUS,SONNET,HAIKU}MODEL_SUPPORTS env vars to override…]] · Change
- 2026-03-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-26-3-model-support-changes-in-rust-v0-117-0|3 Model Support changes in rust-v0.117.0]] · Digest
- 2026-03-26 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-26-model-display-header-shows-the-active-reasoning-effort-level-e-g-high-next-to-th|Model display header shows the active reasoning effort level (e.g. "(high)") next…]] · Change
- 2026-03-24 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-24-7-model-support-changes-in-v0-35-0|7 Model Support changes in v0.35.0]] · Digest
- 2026-03-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-23-ensure-models-appear-in-picker-correctly-display-model-names-where-possible|Ensure models appear in picker correctly, display model names where possible]] · Change
- 2026-03-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-20-2-model-support-changes-in-v1-0-10|2 Model Support changes in v1.0.10]] · Digest
- 2026-03-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-19-added-effort-frontmatter-support-for-skills-and-slash-commands-to-override-the-m|Added effort frontmatter support for skills and slash commands to override…]] · Change
- 2026-03-19 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-03-19-3-model-support-changes-in-v3-74-0|3 Model Support changes in v3.74.0]] · Digest
- 2026-03-19 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-19-2-model-support-changes-in-rust-v0-116-0|2 Model Support changes in rust-v0.116.0]] · Digest
- 2026-03-18 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-03-18-we-re-rolling-out-gpt-5-4-mini-in-chatgpt-gpt-5-4-mini-is-available-to-free-and|GPT-5.4 mini in ChatGPT]] · Change
- 2026-03-17 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-03-17-instant-fast-responses-for-everyday-questions|Instant – fast responses for everyday questions]] · Change
- 2026-03-17 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-03-17-pro-the-most-advanced-reasoning-models|Pro – the most advanced reasoning models]] · Change
- 2026-03-17 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-03-17-thinking-deeper-reasoning-for-more-complex-tasks|Thinking – deeper reasoning for more complex tasks]] · Change
- 2026-03-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-17-increased-default-maximum-output-token-limits-for-claude-opus-4-6-to-64k-tokens|Increased default maximum output token limits for Claude Opus 4.6 to 64k tokens…]] · Change
- 2026-03-17 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-17-5-model-support-changes-in-v0-34-0|5 Model Support changes in v0.34.0]] · Digest
- 2026-03-17 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-17-2-model-support-changes-in-v1-0-7|2 Model Support changes in v1.0.7]] · Digest
- 2026-03-16 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-03-16-we-re-rolling-out-an-update-to-gpt-5-3-instant-that-improves-follow-up-tone-and|GPT-5.3 Instant update]] · Change
- 2026-03-16 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-03-16-added-w-b-inference-by-coreweave-as-a-new-api-provider-with-17-models|Added W&B Inference by CoreWeave as a new API provider with 17 models]] · Change
- 2026-03-16 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-16-5-model-support-changes-in-rust-v0-115-0|5 Model Support changes in rust-v0.115.0]] · Digest
- 2026-03-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-16-model-can-discover-and-use-tools-dynamically-with-tool-search-for-claude-models|Model can discover and use tools dynamically with tool search for Claude models]] · Change
- 2026-03-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-14-improved-model-fallback-notifications-now-always-visible-instead-of-hidden-behin|Improved model fallback notifications]] · Change
- 2026-03-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-13-setting-claude-sonnet-4-6-as-the-default-model-is-now-preserved-correctly|Setting claude-sonnet-4.6 as the default model is now preserved correctly]] · Change
- 2026-03-12 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-03-12-2-model-support-changes-in-v3-72-0|2 Model Support changes in v3.72.0]] · Digest
- 2026-03-11 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-11-2-model-support-changes-in-v2-1-73|2 Model Support changes in v2.1.73]] · Digest
- 2026-03-11 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-11-14135-tui-only-show-fast-status-for-gpt-5-4-pash-openai|♯14135 tui: only show fast status for gpt-5.4 @pash-openai]] · Change
- 2026-03-11 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-11-3-model-support-changes-in-v0-33-0|3 Model Support changes in v0.33.0]] · Digest
- 2026-03-11 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-11-2-model-support-changes-in-v1-0-4|2 Model Support changes in v1.0.4]] · Digest
- 2026-03-11 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-03-11-added-support-for-the-following-models-claude-opus-4-6-glm-4-7-claude-sonnet-4-6|Added support for the following models]] · Change
- 2026-03-10 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-10-14123-pass-on-save-info-to-model-ui-tweaks-won-openai|♯14123 pass on save info to model + ui tweaks @won-openai]] · Change
- 2026-03-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-08-13617-update-models-json-aibrahim-oai|♯13617 Update models.json @aibrahim-oai]] · Change
- 2026-03-06 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-03-06-added-gpt-5-4-models-for-chatgpt-subscription-users|Added GPT-5.4 models for ChatGPT subscription users]] · Change
- 2026-03-05 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-05-changed-sonnet-4-5-users-on-pro-max-team-premium-to-be-automatically-migrated-to|Changed Sonnet 4.5 users on Pro/Max/Team Premium to be automatically migrated…]] · Change
- 2026-03-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-05-2-model-support-changes-in-rust-v0-110-0|2 Model Support changes in rust-v0.110.0]] · Digest
- 2026-03-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-05-add-support-for-gpt-5-4-model|Add support for GPT-5.4 model]] · Change
- 2026-03-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-03-04-3-model-support-changes-in-v2-1-68|3 Model Support changes in v2.1.68]] · Digest
- 2026-03-04 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-03-04-2-model-support-changes-in-v3-70-0|2 Model Support changes in v3.70.0]] · Digest
- 2026-03-03 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-03-03-gpt-5-3-instant-delivers-more-accurate-answers-richer-and-better-contextualized|GPT-5.3 Instant Update]] · Change
- 2026-03-03 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-03-03-restore-gpt-oss-native-file-editing-on-openai-compatible-models|Restore GPT-OSS native file editing on OpenAI-compatible models]] · Change
- 2026-03-03 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-03-3-model-support-changes-in-v0-32-0|3 Model Support changes in v0.32.0]] · Digest
- 2026-03-03 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-03-2-model-support-changes-in-v0-0-421|2 Model Support changes in v0.0.421]] · Digest
- 2026-03-02 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-02-4-model-support-changes-in-rust-v0-107-0|4 Model Support changes in rust-v0.107.0]] · Digest

**2026-02**

- 2026-02-27 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-02-27-4-model-support-changes-in-v3-68-0|4 Model Support changes in v3.68.0]] · Digest
- 2026-02-27 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-27-11-model-support-changes-in-v0-31-0|11 Model Support changes in v0.31.0]] · Digest
- 2026-02-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-26-4-model-support-changes-in-rust-v0-106-0|4 Model Support changes in rust-v0.106.0]] · Digest
- 2026-02-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-25-6-model-support-changes-in-rust-v0-105-0|6 Model Support changes in rust-v0.105.0]] · Digest
- 2026-02-25 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-25-8-model-support-changes-in-v0-30-0|8 Model Support changes in v0.30.0]] · Digest
- 2026-02-24 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-24-the-model-picker-now-shows-human-readable-labels-e-g-sonnet-4-5-instead-of-raw-m|The /model picker now shows human-readable labels (e.g., "Sonnet 4.5") instead…]] · Change
- 2026-02-24 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-02-24-added-codex-5-3-model-support|Added Codex 5.3 model support]] · Change
- 2026-02-24 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-02-24-3-model-support-changes-in-v3-67-0|3 Model Support changes in v3.67.0]] · Digest
- 2026-02-24 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-24-streaming-response-size-counter-updates-continuously-during-tool-calls-and-reaso|Streaming response size counter updates continuously during tool calls…]] · Change
- 2026-02-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-23-plan-approval-menu-shows-model-curated-actions-with-a-recommended-option-highlig|Plan approval menu shows model-curated actions with a recommended option highlighted…]] · Change
- 2026-02-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-20-2-model-support-changes-in-v0-0-413|2 Model Support changes in v0.0.413]] · Digest
- 2026-02-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-19-2-model-support-changes-in-v2-1-49|2 Model Support changes in v2.1.49]] · Digest
- 2026-02-19 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-02-19-gemini-3-1-pro-preview|Gemini-3.1 Pro Preview]] · Change
- 2026-02-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-19-2-model-support-changes-in-v0-0-412|2 Model Support changes in v0.0.412]] · Digest
- 2026-02-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-18-2-model-support-changes-in-rust-v0-104-0|2 Model Support changes in rust-v0.104.0]] · Digest
- 2026-02-18 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-02-18-2-model-support-changes-in-cli-improvements-and-mermaid-ascii|2 Model Support changes in CLI Improvements and Mermaid ASCII…]] · Digest
- 2026-02-18 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-18-11-model-support-changes-in-v0-29-0|11 Model Support changes in v0.29.0]] · Digest
- 2026-02-18 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-02-18-add-minimax-m2-5-model-support-by-neubig-in-https-github-com-openhands-openhands|Add MiniMax-M2.5 model support]] · Change
- 2026-02-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-17-added-support-for-claude-sonnet-4-6|Added support for Claude Sonnet 4.6]] · Change
- 2026-02-17 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-17-11-model-support-changes-in-rust-v0-102-0|11 Model Support changes in rust-v0.102.0]] · Digest
- 2026-02-17 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-17-11699-chore-rm-remote-models-fflag-sayan-oai|♯11699 chore: rm remote models fflag @sayan-oai]] · Change
- 2026-02-17 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-17-2-model-support-changes-in-v0-0-411|2 Model Support changes in v0.0.411]] · Digest
- 2026-02-13 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-02-13-ui-ux-fixes-with-minimax-model-family|UI/UX fixes with minimax model family]] · Change
- 2026-02-12 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-02-12-2-model-support-changes-in-v3-58-0|2 Model Support changes in v3.58.0]] · Digest
- 2026-02-12 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-12-3-model-support-changes-in-rust-v0-101-0|3 Model Support changes in rust-v0.101.0]] · Digest
- 2026-02-12 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-12-4-model-support-changes-in-rust-v0-100-0|4 Model Support changes in rust-v0.100.0]] · Digest
- 2026-02-11 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-11-15-model-support-changes-in-rust-v0-99-0|15 Model Support changes in rust-v0.99.0]] · Digest
- 2026-02-11 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-11-2-model-support-changes-in-v0-0-407|2 Model Support changes in v0.0.407]] · Digest
- 2026-02-10 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-02-10-we-re-making-an-update-to-gpt-5-2-instant-in-chatgpt-and-the-api-that-improves-r|GPT-5.2 Instant Update]] · Change
- 2026-02-10 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-10-docs-document-gemini-cli-home-environment-variable-by-adamfweidman-in-https-gith|docs: document GEMINI_CLI_HOME environment variable]] · Change
- 2026-02-07 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-07-add-support-for-claude-opus-4-6-fast-preview|Add support for Claude Opus 4.6 Fast (Preview)]] · Change
- 2026-02-05 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-02-05-anthopic-opus-4-6|Anthopic Opus 4.6]] · Change
- 2026-02-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-05-2-model-support-changes-in-rust-v0-97-0|2 Model Support changes in rust-v0.97.0]] · Digest
- 2026-02-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-05-2-model-support-changes-in-rust-v0-98-0|2 Model Support changes in rust-v0.98.0]] · Digest
- 2026-02-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-05-add-support-for-claude-opus-4-6-model|Add support for claude-opus-4.6 model]] · Change
- 2026-02-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-05-2-model-support-changes-in-v0-0-403|2 Model Support changes in v0.0.403]] · Digest
- 2026-02-05 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-02-05-released-tab-v2-model-selector-to-all-users|Released Tab v2 model selector to all users]] · Change
- 2026-02-04 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-02-04-jan-10-2026-we-lowered-the-standard-and-light-thinking-time-as-we-observed-users-e93d5a|Jan 10, 2026: We lowered the Standard and Light thinking time as we observed users…]] · Change
- 2026-02-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-04-improved-system-prompts-to-more-clearly-guide-the-model-toward-using-dedicated-t|Improved system prompts to more clearly guide the model toward using dedicated tools…]] · Change
- 2026-02-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-04-2-model-support-changes-in-rust-v0-95-0|2 Model Support changes in rust-v0.95.0]] · Digest
- 2026-02-04 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-04-6-model-support-changes-in-v0-27-0|6 Model Support changes in v0.27.0]] · Digest
- 2026-02-03 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-03-changed-model-to-execute-immediately-instead-of-being-queued|Changed /model to execute immediately instead of being queued]] · Change
- 2026-02-03 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-03-improve-handling-of-chat-history-when-switching-between-model-families|Improve handling of chat history when switching between model families]] · Change
- 2026-02-02 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-02-10373-chore-core-gpt-5-2-codex-personality-template-dylan-hurd-oai|♯10373 chore(core) gpt-5.2-codex personality template @dylan-hurd-oai]] · Change

**2026-01**

- 2026-01-31 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-31-10118-codex-cli-show-model-capacity-guidance-on-429-ccy-oai|♯10118 CodexCLI Show model-capacity guidance on 429 @ccy-oai]] · Change
- 2026-01-30 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-30-litellm-fixed-thinking-configuration-not-appearing-for-reasoning-capable-models|_LiteLLM: Fixed thinking configuration not appearing for reasoning-capable models]] · Change
- 2026-01-30 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-30-litellm-fixed-thinking-configuration-not-appearing-for-reasoning-capable-models-c6cd73|_LiteLLM: Fixed thinking configuration not appearing for reasoning-capable models]] · Change
- 2026-01-30 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-30-litellm-fixed-thinking-configuration-not-appearing-for-reasoning-capable-models-cb84ce|_LiteLLM: Fixed thinking configuration not appearing for reasoning-capable models]] · Change
- 2026-01-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-30-acp-server-supports-changing-models-during-a-session|ACP server supports changing models during a session]] · Change
- 2026-01-28 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-28-2-model-support-changes-in-v3-55-0|2 Model Support changes in v3.55.0]] · Digest
- 2026-01-28 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-28-4-model-support-changes-in-v0-26-0|4 Model Support changes in v0.26.0]] · Digest
- 2026-01-27 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-27-3-model-support-changes-in-v3-54-0|3 Model Support changes in v3.54.0]] · Digest
- 2026-01-27 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-27-2-model-support-changes-in-rust-v0-92-0|2 Model Support changes in rust-v0.92.0]] · Digest
- 2026-01-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-25-5-model-support-changes-in-rust-v0-90-0|5 Model Support changes in rust-v0.90.0]] · Digest
- 2026-01-24 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-24-directory-path-uses-consistent-muted-text-color-with-git-branch-and-model-displa|Directory path uses consistent muted text color with git branch and model display]] · Change
- 2026-01-23 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-23-removed-grok-model-from-free-tier|Removed grok model from free tier]] · Change
- 2026-01-22 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-01-22-we-re-updating-gpt-5-2-instant-s-default-personality-to-be-more-conversational-a|5.2 Personality System Prompt Update]] · Change
- 2026-01-22 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-22-9597-feat-core-modelinfo-model-instructions-template-dylan-hurd-oai|♯9597 feat(core) ModelInfo.model_instructions_template @dylan-hurd-oai]] · Change
- 2026-01-22 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-22-add-models-as-alias-for-model-command|Add /models as alias for /model command]] · Change
- 2026-01-21 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-21-5-model-support-changes-in-rust-v0-88-0|5 Model Support changes in rust-v0.88.0]] · Digest
- 2026-01-21 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-21-6-model-support-changes-in-v0-25-0|6 Model Support changes in v0.25.0]] · Digest
- 2026-01-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-19-model-switching-from-codex-to-opus-preserves-conversation-history-correctly|Model switching from Codex to Opus preserves conversation history correctly]] · Change
- 2026-01-16 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-16-added-support-for-pretooluse-hooks-to-return-additionalcontext-to-the-model|Added support for PreToolUse hooks to return additionalContext to the model]] · Change
- 2026-01-16 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-16-9336-rename-model-turn-to-sampling-request-aibrahim-oai|♯9336 rename model turn to sampling request @aibrahim-oai]] · Change
- 2026-01-16 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-01-16-models-removed-use-model-to-see-all-models-or-select-a-model|/models removed. Use /model to see all models or select a model]] · Change
- 2026-01-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-16-3-model-support-changes-in-v0-0-384|3 Model Support changes in v0.0.384]] · Digest
- 2026-01-16 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-01-16-improvements-to-gpt-5-2-codex-harness|Improvements to GPT-5.2-Codex harness]] · Change
- 2026-01-15 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-15-adding-openai-gpt-5-2-codex-model-to-the-model-picker|Adding OpenAI gpt-5.2-codex model to the model picker]] · Change
- 2026-01-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-15-2-model-support-changes-in-rust-v0-85-0|2 Model Support changes in rust-v0.85.0]] · Digest
- 2026-01-14 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-14-add-gpt-5-2-codex-openai-model-support|Add gpt-5.2-codex OpenAI model support]] · Change
- 2026-01-14 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-14-8-model-support-changes-in-rust-v0-81-0|8 Model Support changes in rust-v0.81.0]] · Digest
- 2026-01-14 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-14-6-model-support-changes-in-v0-24-0|6 Model Support changes in v0.24.0]] · Digest
- 2026-01-14 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-14-add-support-for-gpt-5-2-codex-model|Add support for GPT-5.2-Codex model]] · Change
- 2026-01-14 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-01-14-1-13-8-gpt-5-2-codex-model-changelog-banner|1.13.8 GPT-5.2 Codex model changelog banner]] · Change
- 2026-01-13 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-13-phase-in-responses-api-usage-instead-of-defaulting-for-every-supported-model|Phase in Responses API usage instead of defaulting for every supported model]] · Change
- 2026-01-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-13-retrieving-models-handles-network-errors-from-firewalled-routes-gracefully-raise|Retrieving models handles network errors from firewalled routes gracefully, raises…]] · Change
- 2026-01-10 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-10-removing-minimax-2-1-from-free-model-list-as-the-free-trial-has-ended|Removing Minimax-2.1 from free model list as the free trial has ended]] · Change
- 2026-01-09 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-01-09-merged-slash-commands-and-skills-simplifying-the-mental-model-with-no-change-in|Merged slash commands and skills, simplifying the mental model with no change in behavior]] · Change
- 2026-01-09 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-09-2-model-support-changes-in-v3-48-0|2 Model Support changes in v3.48.0]] · Digest
- 2026-01-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-09-4-model-support-changes-in-rust-v0-80-0|4 Model Support changes in rust-v0.80.0]] · Digest
- 2026-01-08 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-08-large-tool-outputs-are-written-to-disk-and-models-are-encouraged-to-use-efficien|Large tool outputs are written to disk and models are encouraged to use efficient…]] · Change
- 2026-01-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-07-3-model-support-changes-in-rust-v0-79-0|3 Model Support changes in rust-v0.79.0]] · Digest
- 2026-01-07 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-07-3-model-support-changes-in-v0-23-0|3 Model Support changes in v0.23.0]] · Digest
- 2026-01-07 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-07-2-model-support-changes-in-v0-0-375|2 Model Support changes in v0.0.375]] · Digest
- 2026-01-06 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-01-06-3-model-support-changes-in-v3-47-0|3 Model Support changes in v3.47.0]] · Digest
- 2026-01-06 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-06-5-model-support-changes-in-rust-v0-78-0|5 Model Support changes in rust-v0.78.0]] · Digest
- 2026-01-02 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-02-model-picker-shows-clearer-message-with-settings-link-when-models-are-unavailabl|Model picker shows clearer message with settings link when models are unavailable]] · Change

</details>

</details>

<details class="disclosure">
<summary>2025 · 295 entries (Aider 17 · ChatGPT 32 · Cline 81 · Codex CLI 42 · Cursor 14 · Gemini CLI 35 · GitHub Copilot CLI 25 · OpenHands 20 · Windsurf 29)</summary>

**2025-12**

- 2025-12-27 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-12-27-gemini-3-flash|Gemini 3 Flash]] · Launch
- 2025-12-24 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-12-24-cascade-hooks|Cascade Hooks]] · Launch
- 2025-12-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-18-introducing-gpt-5-2-codex-our-latest-frontier-model-with-improvements-across-kno|Introducing gpt-5.2-codex our latest frontier model with improvements across…]] · Launch
- 2025-12-11 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-12-11-today-we-re-releasing-gpt-5-2-the-next-upgrade-to-the-gpt-5-series-gpt-5-2-is-sm|Today, we’re releasing GPT-5.2, the next upgrade to the GPT-5 series]] · Launch
- 2025-12-11 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-11-introducing-gpt-5-2-our-latest-frontier-model-with-improvements-across-knowledge|Introducing gpt-5.2 our latest frontier model with improvements across knowledge…]] · Launch
- 2025-12-11 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-12-11-gpt-5-2|GPT-5.2]] · Launch
- 2025-12-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-12-05-gpt-5-1-codex-max-is-now-available-in-github-copilot-cli|GPT-5.1-Codex-Max is now available in GitHub Copilot CLI]] · Launch
- 2025-12-04 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-12-04-gpt-5-1-codex-max|GPT-5.1-Codex Max]] · Launch

**2025-11**

- 2025-11-24 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-11-24-opus-4-5-gpt-4-1-and-gpt-5-mini-are-now-available-in-github-copilot-cli|Opus 4.5, GPT-4.1 and GPT-5-Mini are now available in GitHub Copilot CLI]] · Launch
- 2025-11-24 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-11-24-claude-opus-4-5|Claude Opus 4.5]] · Launch
- 2025-11-21 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-11-21-sonnet-4-5|Sonnet 4.5]] · Launch
- 2025-11-21 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-11-21-gemini-3-pro|Gemini 3 Pro]] · Launch
- 2025-11-21 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-11-21-ai-models|AI Models]] · Launch
- 2025-11-21 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-11-21-gpt-5-1-codex-and-codex-mini|GPT-5.1 Codex and Codex Mini]] · Launch
- 2025-11-18 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-11-18-gemini-3-pro-is-now-available-in-github-copilot-cli|Gemini 3 Pro is now available in GitHub Copilot CLI]] · Launch
- 2025-11-18 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-11-18-gemini-3-pro-preview|Gemini 3 Pro Preview]] · Launch
- 2025-11-14 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-11-14-gpt-5-1-priority-mode|GPT-5.1 Priority Mode]] · Launch
- 2025-11-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-11-13-gpt-5-1-gpt-5-1-codex-and-gpt-5-1-codex-mini-are-now-available-in-github-copilot|GPT-5.1, GPT-5.1-Codex, and GPT-5.1-Codex-Mini are now available in GitHub Copilot CLI]] · Launch
- 2025-11-13 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-11-13-gpt-5-1-and-gpt-5-1-codex|GPT-5.1 and GPT-5.1-Codex]] · Launch
- 2025-11-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-07-introducing-our-new-model-gpt-5-codex-mini-a-more-compact-and-cost-efficient-ver|Introducing our new model GPT-5-Codex-Mini]] · Launch
- 2025-11-05 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-11-05-you-can-now-interrupt-long-running-queries-such-as-deep-research-or-gpt-5-pro-to|Interrupt ChatGPT]] · Change

**2025-10**

- 2025-10-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-10-29-introducing-our-first-agentic-coding-model-composer-is-a-frontier-model-that-is|Composer]] · Launch
- 2025-10-29 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-10-29-plan-mode-in-background|Plan Mode in Background]] · Launch
- 2025-10-02 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-02-added-usage-slash-command-to-provide-stats-about-premium-request-usage-session-t|Added /usage slash command to provide stats about Premium request usage, session…]] · Change

**2025-09**

- 2025-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-09-29-opt-out-of-model-training-so-their-teen-s-conversations-won-t-be-used-to-improve|Opt out of model training, so their teen’s conversations won’t be used to improve…]] · Policy
- 2025-09-29 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-09-29-added-model-slash-command-to-easily-change-the-model-fixes-https-github-com-gith|Added /model slash command to easily change the model…]] · Change
- 2025-09-29 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-09-29-claude-sonnet-4-5|Claude Sonnet 4.5]] · Launch
- 2025-09-23 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-09-23-gpt-5-codex-is-now-in-windsurf|GPT-5-Codex is now in Windsurf!]] · Launch

**2025-08**

- 2025-08-12 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-08-12-gmail-google-calendar-and-google-contacts-are-now-available-to-connect-and-use-i-9ea6d6|Gmail, Google Calendar, and Google Contacts Connectors in ChatGPT (Pro)]] · Launch
- 2025-08-12 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-08-12-you-can-now-choose-between-auto-fast-and-thinking-for-gpt-5-most-users-will-want-f4c05b|GPT-5 Updates]] · Change
- 2025-08-07 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-08-07-gpt-5-available|GPT-5 Available]] · Launch
- 2025-08-06 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-08-06-separate-models-per-agent|Separate models per Agent]] · Launch

**2025-06**

- 2025-06-20 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-06-20-deprecation-warnings-in-cli-and-during-llm-api-calls-by-xingyaoww-in-https-githu|Deprecation Warnings in CLI and during LLM API calls by @xingyaoww…]] · Policy
- 2025-06-10 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-06-10-like-o1-pro-o3-pro-is-a-version-of-our-most-intelligent-model-o3-designed-to-thi-32668a|ChatGPT launches OpenAI o3-pro—available now for Pro users and in our API]] · Launch
- 2025-06-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-06-04-max-mode-is-now-available-for-gemini-2-5-flash|Max mode is now available for Gemini 2.5 Flash]] · Launch

**2025-05**

- 2025-05-22 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-05-22-byok-anthropic-key|BYOK (Anthropic Key)]] · Launch
- 2025-05-15 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-05-15-max-mode-for-all-top-models|Max Mode for all top models]] · Launch
- 2025-05-15 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-05-15-swe-1|SWE-1]] · Launch
- 2025-05-15 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-05-15-swe-1-lite|SWE-1-lite]] · Launch
- 2025-05-15 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-05-15-new-family-of-swe-1-models|New Family of SWE-1 Models]] · Launch
- 2025-05-14 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-05-14-gpt-4-1-mini-is-a-fast-capable-and-efficient-small-model-delivering-significant-722b7d|Introducing GPT-4.1 mini, replacing GPT-4o mini, in ChatGPT for all users]] · Launch
- 2025-05-07 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-05-07-cascade-ux-improvements|Cascade UX Improvements]] · Launch

**2025-04**

- 2025-04-27 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-04-27-misc|Misc]] · Launch
- 2025-04-16 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-04-16-today-we-re-releasing-openai-o3-and-o4-mini-the-latest-in-our-o-series-of-models|o3 and o4-mini in ChatGPT]] · Launch
- 2025-04-16 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-04-16-new-o4-mini-models-available-and-free-limited-time|New o4-mini models available and Free (Limited Time)]] · Launch
- 2025-04-16 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-04-16-o4-mini-available|o4-mini Available]] · Launch
- 2025-04-15 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-04-15-new-models|New models]] · Launch
- 2025-04-14 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-04-14-gpt-4-1-available|GPT 4.1 Available]] · Launch
- 2025-04-14 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-04-14-new-gpt-4-1-model-available-and-free-limited-time|New GPT 4.1 Model available and Free (Limited Time)]] · Launch
- 2025-04-10 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-04-10-effective-april-30-2025-gpt-4-will-be-retired-from-chatgpt-and-fully-replaced-by-d03b3b|Sunsetting GPT‑4 in ChatGPT]] · Policy

**2025-03**

- 2025-03-27 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-03-27-early-testers-say-that-the-model-seems-to-better-understand-the-implied-intent-b|“Fuzzy” improvements]] · Launch
- 2025-03-27 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-03-27-gpt-4o-has-further-improved-its-capability-to-tackle-complex-technical-and-codin|Smarter problem-solving in STEM and coding]] · Launch
- 2025-03-27 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-03-27-gpt-4o-is-now-more-adept-at-following-detailed-instructions-especially-for-promp|Enhanced instruction-following and formatting accuracy]] · Launch
- 2025-03-13 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-03-13-added-reasoning-effort-command-to-control-model-reasoning-level|Added /reasoning-effort command to control model reasoning level]] · Change

<details class="disclosure">
<summary>Fixes, digests and other changes · 241 (Aider 16 · ChatGPT 20 · Cline 81 · Codex CLI 39 · Cursor 8 · Gemini CLI 35 · GitHub Copilot CLI 19 · OpenHands 19 · Windsurf 4)</summary>

**2025-12**

- 2025-12-22 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-12-22-remove-glm-4-6-from-free-models|Remove GLM 4.6 from free models]] · Change
- 2025-12-22 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-12-22-5-model-support-changes-in-v3-46-0|5 Model Support changes in v3.46.0]] · Digest
- 2025-12-22 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-22-5-model-support-changes-in-v0-22-0|5 Model Support changes in v0.22.0]] · Digest
- 2025-12-21 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-21-3-model-support-changes-in-rust-v0-77-0|3 Model Support changes in rust-v0.77.0]] · Digest
- 2025-12-19 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-19-2-model-support-changes-in-rust-v0-76-0|2 Model Support changes in rust-v0.76.0]] · Digest
- 2025-12-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-12-19-enable-disabled-models-directly-in-cli-when-selecting-or-specifying-them|Enable disabled models directly in CLI when selecting or specifying them]] · Change
- 2025-12-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-18-6-model-support-changes-in-rust-v0-74-0|6 Model Support changes in rust-v0.74.0]] · Digest
- 2025-12-18 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-12-18-2-model-support-changes-in-v0-0-370|2 Model Support changes in v0.0.370]] · Digest
- 2025-12-17 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-12-17-polished-the-model-picker-ui-with-checkmarks-for-selected-models-tooltips-on-pla|Polished the model picker UI with checkmarks for selected models, tooltips…]] · Change
- 2025-12-17 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-12-17-2-model-support-changes-in-v3-45-0|2 Model Support changes in v3.45.0]] · Digest
- 2025-12-16 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-12-16-3-model-support-changes-in-v3-43-1|3 Model Support changes in v3.43.1]] · Digest
- 2025-12-16 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-16-6-model-support-changes-in-v0-21-0|6 Model Support changes in v0.21.0]] · Digest
- 2025-12-16 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-12-16-enabled-native-tool-calling-for-gemini-3-pro-preview-by-enyst-in-https-github-co|Enabled native tool calling for gemini-3-pro-preview]] · Change
- 2025-12-16 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-12-16-added-a-new-promo-label-to-llm-models-that-are-newly-available-or-have-special-d|Added a new "Promo" label to LLM models that are newly available or have special…]] · Change
- 2025-12-13 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-13-5-model-support-changes-in-rust-v0-72-0|5 Model Support changes in rust-v0.72.0]] · Digest
- 2025-12-11 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-12-11-11-model-support-changes-in-v3-41-0|11 Model Support changes in v3.41.0]] · Digest
- 2025-12-11 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-12-11-add-support-for-gpt-5-2|Add support for GPT-5.2]] · Change
- 2025-12-11 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-12-11-1-12-43-gpt-5-2-changelog-banner|1.12.43 GPT-5.2 changelog banner]] · Change
- 2025-12-10 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-10-3-model-support-changes-in-rust-v0-69-0|3 Model Support changes in rust-v0.69.0]] · Digest
- 2025-12-10 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-12-10-add-grep-tool-codex-models|Add grep tool Codex models]] · Change
- 2025-12-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-09-8-model-support-changes-in-rust-v0-66-0|8 Model Support changes in rust-v0.66.0]] · Digest
- 2025-12-09 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-09-7-model-support-changes-in-v0-20-0|7 Model Support changes in v0.20.0]] · Digest
- 2025-12-04 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-12-04-feat-set-default-thinking-level-for-gemini-3-pro-models-by-abeatrix-in-https-git|feat: set default thinking level for Gemini 3 Pro models]] · Change
- 2025-12-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-04-6-model-support-changes-in-rust-v0-65-0|6 Model Support changes in rust-v0.65.0]] · Digest
- 2025-12-04 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-12-04-1-12-39-gpt-5-1-codex-max-changelog-banner|1.12.39 GPT-5.1 Codex Max changelog banner]] · Change
- 2025-12-03 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-12-03-add-apply-patch-toolchain-for-openai-codex-models|Add apply_patch toolchain for OpenAI Codex models]] · Change
- 2025-12-02 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-12-02-4-model-support-changes-in-v3-39-0|4 Model Support changes in v3.39.0]] · Digest
- 2025-12-02 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-12-02-skip-reasoning-details-on-microwave-model-by-canvrno-in-https-github-com-cline-c|Skip reasoning_details on microwave model]] · Change
- 2025-12-02 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-02-2-model-support-changes-in-rust-v0-64-0|2 Model Support changes in rust-v0.64.0]] · Digest
- 2025-12-02 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-02-5-model-support-changes-in-v0-19-0|5 Model Support changes in v0.19.0]] · Digest

**2025-11**

- 2025-11-27 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-11-27-12-model-support-changes-in-v3-38-3|12 Model Support changes in v3.38.3]] · Digest
- 2025-11-26 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-26-6-model-support-changes-in-v0-18-0|6 Model Support changes in v0.18.0]] · Digest
- 2025-11-24 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-11-24-1-12-36-claude-opus-4-5-changelog-banner|1.12.36 Claude Opus 4.5 changelog banner]] · Change
- 2025-11-21 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-11-21-chatgpt-now-adds-more-inline-images-from-the-web-to-help-you-quickly-understand-83e5b8|More images in answers]] · Change
- 2025-11-21 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-21-chore-drop-model-max-output-tokens-by-jif-oai-in-https-github-com-openai-codex-p|chore: drop model_max_output_tokens]] · Change
- 2025-11-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-20-stop-model-migration-screen-after-first-time-6954-aibrahim-oai|stop model migration screen after first time]] · Change
- 2025-11-20 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-20-3-model-support-changes-in-v0-17-0|3 Model Support changes in v0.17.0]] · Digest
- 2025-11-19 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-11-19-today-we-re-updating-gpt-5-pro-to-gpt-5-1-pro-in-early-testing-users-consistentl-191826|GPT-5.1 Pro: Clearer, more capable answers for complex work]] · Change
- 2025-11-19 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-19-default-model-for-api-users-is-now-gpt-5-1-codex|Default model for API users is now gpt-5.1-codex]] · Change
- 2025-11-19 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-19-5-model-support-changes-in-rust-v0-59-0|5 Model Support changes in rust-v0.59.0]] · Digest
- 2025-11-18 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-11-18-6-model-support-changes-in-v3-38-0|6 Model Support changes in v3.38.0]] · Digest
- 2025-11-18 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-18-feat-launch-gemini-3-in-gemini-cli-by-skeshive-in-https-github-com-google-gemini|feat: launch Gemini 3 in Gemini CLI 🚀🚀🚀]] · Change
- 2025-11-14 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-11-14-feat-models-add-free-minimax-mimax-m2-model-to-the-model-picker-by-saoudrizwan-i|feat(models): Add free minimax/mimax-m2 model to the model picker]] · Change
- 2025-11-14 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-14-4-model-support-changes-in-v0-15-0|4 Model Support changes in v0.15.0]] · Digest
- 2025-11-14 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-11-14-recovery-release-to-fix-availability-of-gpt-5-1-gpt-5-1-codex-and-gpt-5-1-codex|Recovery release to fix availability of GPT-5.1, GPT-5.1-Codex…]] · Change
- 2025-11-13 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-11-13-8-model-support-changes-in-v3-37-0|8 Model Support changes in v3.37.0]] · Digest
- 2025-11-13 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-13-11-model-support-changes-in-rust-v0-58-0|11 Model Support changes in rust-v0.58.0]] · Digest
- 2025-11-12 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-11-12-we-re-updating-chatgpt-s-tone-controls-so-it-s-easier-to-make-responses-sound-th-d3a253|New tone and personalization controls]] · Change
- 2025-11-12 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-11-12-we-re-updating-gpt-5-to-gpt-5-1-instant-and-gpt-5-1-thinking-making-answers-both-d702c4|GPT-5.1 in ChatGPT]] · Change
- 2025-11-12 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-12-docs-add-model-documentation-by-jkcinouye-in-https-github-com-google-gemini-gemi|Docs: Add /model documentation]] · Change
- 2025-11-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-09-6351-promote-shell-config-tool-to-model-family-config|♯6351 – Promote shell config tool to model family config]] · Change
- 2025-11-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-07-3-model-support-changes-in-rust-v0-56-0|3 Model Support changes in rust-v0.56.0]] · Digest
- 2025-11-07 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-07-4-model-support-changes-in-v0-13-0|4 Model Support changes in v0.13.0]] · Digest
- 2025-11-06 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-11-06-complete-telemetry-attribution-for-model-provider-tracking-by-nickbaumann98-in-h|Complete telemetry attribution for model/provider tracking]] · Change
- 2025-11-04 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-11-04-feat-add-support-for-claude-4-5-sonnet-in-sap-ai-core-provider-by-wahajahmedkhan|feat: Add support for Claude 4.5 Sonnet in SAP AI Core provider]] · Change
- 2025-11-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-04-2-model-support-changes-in-rust-v0-54-0|2 Model Support changes in rust-v0.54.0]] · Digest
- 2025-11-04 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-04-2-model-support-changes-in-v0-12-0|2 Model Support changes in v0.12.0]] · Digest
- 2025-11-03 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-11-03-2-model-support-changes-in-v0-0-354|2 Model Support changes in v0.0.354]] · Digest

**2025-10**

- 2025-10-31 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-10-31-4-model-support-changes-in-v3-35-0|4 Model Support changes in v3.35.0]] · Digest
- 2025-10-30 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-30-5-model-support-changes-in-rust-v0-52-0|5 Model Support changes in rust-v0.52.0]] · Digest
- 2025-10-29 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-29-5-model-support-changes-in-v0-11-0|5 Model Support changes in v0.11.0]] · Digest
- 2025-10-27 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-10-27-3-model-support-changes-in-v3-34-1|3 Model Support changes in v3.34.1]] · Digest
- 2025-10-27 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-27-improve-error-message-from-model-model-command-when-using-an-unsupported-model|Improve error message from /model model command when using an unsupported model]] · Change
- 2025-10-24 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-24-improved-prompting-for-sonnet-4-5-to-reduce-the-number-of-intermediate-markdown|Improved prompting for Sonnet 4.5 to reduce the number of intermediate markdown…]] · Change
- 2025-10-23 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-10-23-6-model-support-changes-in-v3-34-0|6 Model Support changes in v3.34.0]] · Digest
- 2025-10-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-23-3-model-support-changes-in-rust-v0-48-0|3 Model Support changes in rust-v0.48.0]] · Digest
- 2025-10-22 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-10-22-we-re-updating-the-model-for-signed-out-users-to-gpt-5-instant-giving-more-peopl|We’re updating the model for signed-out users to GPT-5 Instant, giving more people…]] · Change
- 2025-10-22 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-22-3-model-support-changes-in-v0-10-0|3 Model Support changes in v0.10.0]] · Digest
- 2025-10-22 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-22-2-model-support-changes-in-v0-0-349|2 Model Support changes in v0.0.349]] · Digest
- 2025-10-18 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-18-added-list-of-supported-models-as-part-of-copilot-help-config-text|Added list of supported models as part of copilot help config text]] · Change
- 2025-10-16 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-10-16-3-model-support-changes-in-v3-33-0|3 Model Support changes in v3.33.0]] · Digest
- 2025-10-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-16-added-debug-logging-when-calls-to-model-result-in-copilot-api-errors-this-should|Added debug logging when calls to /model result in Copilot API errors]] · Change
- 2025-10-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-16-2-model-support-changes-in-v0-0-343|2 Model Support changes in v0.0.343]] · Digest
- 2025-10-15 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-15-3-model-support-changes-in-v0-9-0|3 Model Support changes in v0.9.0]] · Digest
- 2025-10-15 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-15-added-each-model-s-premium-request-multiplier-to-the-model-list-currently-all-ou|Added each model's premium request multiplier to the /model list…]] · Change
- 2025-10-10 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-10-improved-the-error-handling-in-the-model-picker-when-no-models-are-available-fix|Improved the error handling in the /model picker when no models are available…]] · Change
- 2025-10-08 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-10-08-update-local-models-docs-remove-emojis-from-docs-by-nickbaumann98-in-https-githu|Update local models docs & remove emojis from Docs]] · Change
- 2025-10-08 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-08-revert-get-around-the-initial-empty-response-from-gemini-2-5-flash-by-sandytao52|Revert "Get around the initial empty response from gemini-2.5-flash]] · Change
- 2025-10-07 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-07-5-model-support-changes-in-v0-8-0|5 Model Support changes in v0.8.0]] · Digest
- 2025-10-06 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-06-2-model-support-changes-in-rust-v0-45-0|2 Model Support changes in rust-v0.45.0]] · Digest
- 2025-10-03 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-10-03-we-re-updating-gpt-5-instant-to-better-recognize-and-support-people-in-moments-o-ea32fc|Updating GPT-5]] · Change
- 2025-10-03 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-03-6-model-support-changes-in-rust-v0-44-0|6 Model Support changes in rust-v0.44.0]] · Digest
- 2025-10-02 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-02-2-model-support-changes-in-v0-0-333|2 Model Support changes in v0.0.333]] · Digest
- 2025-10-01 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-01-4-model-support-changes-in-v0-7-0|4 Model Support changes in v0.7.0]] · Digest
- 2025-10-01 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-01-improved-the-model-s-list-to-ensure-that-a-user-only-sees-models-they-have-acces|Improved the /models list to ensure that a user only sees models they have access…]] · Change
- 2025-10-01 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-10-01-added-claude-sonnet-4-5-model-support|Added claude-sonnet-4-5 model support]] · Change

**2025-09**

- 2025-09-30 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-09-30-docs-update-documentation-for-claude-sonnet-4-5-release-by-nickbaumann98-in-http|docs: update documentation for Claude Sonnet 4.5 release]] · Change
- 2025-09-29 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-09-29-add-claude-sonnet-4-5-by-saoudrizwan-in-https-github-com-cline-cline-pull-6544|Add Claude Sonnet 4.5]] · Change
- 2025-09-29 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-09-29-3-model-support-changes-in-v0-0-329|3 Model Support changes in v0.0.329]] · Digest
- 2025-09-29 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-09-29-changed-the-default-model-back-to-sonnet-4-since-sonnet-4-5-hasn-t-rolled-out-to|Changed the default model back to Sonnet 4 since Sonnet 4.5 hasn't rolled out to all…]] · Change
- 2025-09-28 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-09-28-2-model-support-changes-in-v3-32-1|2 Model Support changes in v3.32.1]] · Digest
- 2025-09-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-26-4195-send-text-parameter-for-non-gpt-5-models-4195|♯4195 Send text parameter for non-gpt-5 models (♯4195)]] · Change
- 2025-09-25 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-09-25-refactor-append-stealth-models-on-readopenroutermodels-refreshopenroutermodels-b|refactor: append stealth models on readOpenRouterModels & refreshOpenRouterModels]] · Change
- 2025-09-25 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-09-25-set-claude-sonnet-output-token-limit|Set Claude Sonnet output token limit]] · Change
- 2025-09-24 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-24-6-model-support-changes-in-v0-6-0|6 Model Support changes in v0.6.0]] · Digest
- 2025-09-23 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-23-2-model-support-changes-in-rust-v0-40-0|2 Model Support changes in rust-v0.40.0]] · Digest
- 2025-09-19 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-09-19-add-code-supernova-stealth-model-by-saoudrizwan-in-https-github-com-cline-cline|Add code-supernova stealth model]] · Change
- 2025-09-18 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-09-18-we-re-improving-the-quality-and-latency-of-responses-of-the-version-of-advanced|Voice Updates]] · Change
- 2025-09-17 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-09-17-5-model-support-changes-in-toggle-thinking-time-in-the-message|5 Model Support changes in Toggle thinking time in the message…]] · Digest
- 2025-09-17 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-09-17-updated-baseten-provider-to-fetch-models-from-server|Updated Baseten provider to fetch models from server]] · Change
- 2025-09-17 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-17-3680-update-azure-model-provider-example-3680|♯3680 Update azure model provider example (♯3680)]] · Change
- 2025-09-17 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-17-refactor-centralize-and-improve-model-fallback-handling-by-abhipatel12-in-https|refactor: Centralize and improve model fallback handling]] · Change
- 2025-09-16 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-09-16-factuality-fewer-hallucinations-improving-answer-quality|Factuality: Fewer hallucinations, improving answer quality]] · Change
- 2025-09-15 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-15-16-model-support-changes-in-rust-v0-36-0|16 Model Support changes in rust-v0.36.0]] · Digest
- 2025-09-12 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-09-12-requesty-use-base-url-to-get-models-and-api-keys|Requesty: use base URL to get models and API keys]] · Change
- 2025-09-11 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-09-11-5-model-support-changes-in-v3-28-0|5 Model Support changes in v3.28.0]] · Digest
- 2025-09-10 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-10-2-model-support-changes-in-rust-v0-32-0|2 Model Support changes in rust-v0.32.0]] · Digest
- 2025-09-10 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-10-2799-persist-model-reasoning-changes-2799|♯2799 Persist model & reasoning changes (♯2799)]] · Change
- 2025-09-09 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-09-6-model-support-changes-in-v0-4-0|6 Model Support changes in v0.4.0]] · Digest
- 2025-09-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-08-3176-codex-respect-overrides-for-model-family-configuration-from-toml-file|♯3176 codex respect overrides for model family configuration from toml file]] · Change
- 2025-09-05 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-09-05-add-new-kimi-k2-model-to-groq-and-moonshot-providers|Add new Kimi K2 model to Groq and Moonshot providers]] · Change
- 2025-09-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-05-2-model-support-changes-in-rust-v0-30-0|2 Model Support changes in rust-v0.30.0]] · Digest
- 2025-09-04 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-04-5-model-support-changes-in-v0-3-0|5 Model Support changes in v0.3.0]] · Digest
- 2025-09-03 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-03-3071-use-experimental-reasoning-summary|♯3071 Use experimental reasoning summary]] · Change
- 2025-09-02 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-02-2-model-support-changes-in-rust-v0-28-0|2 Model Support changes in rust-v0.28.0]] · Digest
- 2025-09-02 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-09-02-added-llm-risk-analyzer-by-xingyaoww-in-https-github-com-all-hands-ai-openhands|Added LLM risk analyzer]] · Change

**2025-08**

- 2025-08-28 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-28-2-model-support-changes-in-v3-26-6|2 Model Support changes in v3.26.6]] · Digest
- 2025-08-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-26-5-model-support-changes-in-rust-v0-24-0|5 Model Support changes in rust-v0.24.0]] · Digest
- 2025-08-21 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-21-feat-sap-provider-show-deployed-models-from-the-ai-core-service-instance-alongsi|feat: sap provider - show deployed models from the ai core service instance…]] · Change
- 2025-08-21 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-21-removing-max-tokens-from-sonic-model-by-pashpashpash-in-https-github-com-cline-c|removing max tokens from sonic model]] · Change
- 2025-08-21 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-08-21-2-model-support-changes-in-1-5|2 Model Support changes in 1.5]] · Digest
- 2025-08-20 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-20-2-model-support-changes-in-v3-26-0|2 Model Support changes in v3.26.0]] · Digest
- 2025-08-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-20-4-model-support-changes-in-rust-v0-23-0|4 Model Support changes in rust-v0.23.0]] · Digest
- 2025-08-18 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-18-4-model-support-changes-in-v0-1-22|4 Model Support changes in v0.1.22]] · Digest
- 2025-08-15 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-08-15-we-re-making-gpt-5-s-default-personality-warmer-and-more-familiar-this-is-in-res-19a03e|GPT-5 Updates]] · Change
- 2025-08-15 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-15-add-support-for-200k-context-for-claude-sonnet-4-using-openrouter-cline-by-saoud|Add support for 200k context for claude sonnet 4 using openrouter/cline]] · Change
- 2025-08-14 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-14-28-model-support-changes-in-v0-1-21|28 Model Support changes in v0.1.21]] · Digest
- 2025-08-13 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-13-4-model-support-changes-in-v3-24-0|4 Model Support changes in v3.24.0]] · Digest
- 2025-08-13 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-08-13-3-model-support-changes-in-0-52-0|3 Model Support changes in 0.52.0]] · Digest
- 2025-08-12 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-12-https-github-com-openai-codex-pull-2183-include-output-truncation-message-in-too|(source link) Include output truncation message in tool…]] · Change
- 2025-08-12 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-12-7-model-support-changes-in-v0-1-19|7 Model Support changes in v0.1.19]] · Digest
- 2025-08-09 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-08-09-5-model-support-changes-in-v0-86-0|5 Model Support changes in v0.86.0]] · Digest
- 2025-08-07 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-08-07-gpt-5-is-slowly-rolling-out-to-all-users-on-chatgpt-plus-pro-team-and-free-plans-64a08c|GPT-5]] · Change
- 2025-08-07 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-07-pashpashpash-gpt-5-release-by-pashpashpash-in-https-github-com-cline-cline-pull|Pashpashpash/gpt 5 release]] · Change
- 2025-08-07 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-07-2-model-support-changes-in-rust-v0-15-0|2 Model Support changes in rust-v0.15.0]] · Digest
- 2025-08-06 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-06-3-model-support-changes-in-v3-20-11|3 Model Support changes in v3.20.11]] · Digest
- 2025-08-06 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-06-add-prompt-caching-for-opus-4-1-by-saoudrizwan-in-https-github-com-cline-cline-p|Add prompt caching for Opus 4.1]] · Change
- 2025-08-06 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-06-20-model-support-changes-in-v0-1-18|20 Model Support changes in v0.1.18]] · Digest
- 2025-08-05 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-05-adding-anthropic-opus-4-1-by-arafatkatze-in-https-github-com-cline-cline-pull-53|Adding Anthropic opus 4.1]] · Change
- 2025-08-05 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-05-introduces-the-oss-flag-so-codex-cli-can-be-used-with-the-new-open-weight-models|Introduces the --oss flag so Codex CLI can be used with the new open-weight models…]] · Change
- 2025-08-05 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-05-20-model-support-changes-in-v0-1-17|20 Model Support changes in v0.1.17]] · Digest
- 2025-08-02 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-02-20-model-support-changes-in-v0-1-16|20 Model Support changes in v0.1.16]] · Digest
- 2025-08-01 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-08-01-update-cerebras-models-by-arafatkatze-in-https-github-com-cline-cline-pull-5282|Update Cerebras models]] · Change

**2025-07**

- 2025-07-31 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-07-31-4-model-support-changes-in-v3-20-3|4 Model Support changes in v3.20.3]] · Digest
- 2025-07-30 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-30-11-model-support-changes-in-v0-1-15|11 Model Support changes in v0.1.15]] · Digest
- 2025-07-25 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-25-11-model-support-changes-in-v0-1-14|11 Model Support changes in v0.1.14]] · Digest
- 2025-07-24 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-07-24-2-model-support-changes-in-0-50-0|2 Model Support changes in 0.50.0]] · Digest
- 2025-07-23 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-07-23-adding-support-for-new-models-qwen-3-models-on-qwen-provider-by-arafatkatze-in-h|Adding support for new models Qwen 3 models on Qwen provider]] · Change
- 2025-07-22 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-07-22-separate-plan-act-model-settings-by-celestial-vault-in-https-github-com-cline-cl|Separate plan act model settings]] · Change
- 2025-07-19 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-07-19-as-of-https-github-com-openai-codex-pull-1594-we-now-stream-the-response-from-th|As of (source link) we now stream the response…]] · Change
- 2025-07-19 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-19-4-model-support-changes-in-v0-1-13|4 Model Support changes in v0.1.13]] · Digest
- 2025-07-16 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-07-16-added-openhands-provider-for-llm-through-openhands-cloud-by-xingyaoww-in-https-g|Added OpenHands provider for LLM through OpenHands Cloud]] · Change
- 2025-07-15 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-07-15-add-kimi-k2-as-trending-model-by-celestial-vault-in-https-github-com-cline-cline|Add kimi-k2 as trending model]] · Change
- 2025-07-11 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-11-5-model-support-changes-in-v0-1-10|5 Model Support changes in v0.1.10]] · Digest
- 2025-07-10 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-07-10-adding-thinking-token-config-to-gemini-2-5-pro-model-and-adding-gemini-2-5-flash|Adding Thinking Token Config to Gemini 2.5 pro model and adding gemini 2.5 flash preview]] · Change
- 2025-07-10 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-07-10-added-new-config-option-model-supports-reasoning-summaries-https-github-com-open|Added new config option]] · Change
- 2025-07-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-07-09-2-model-support-changes-in-rust-v0-4-0|2 Model Support changes in rust-v0.4.0]] · Digest
- 2025-07-08 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-07-08-sap-ai-core-small-bug-fix-and-reorder-models-by-schardosin-in-https-github-com-c|SAP AI Core small bug fix and reorder models]] · Change
- 2025-07-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-07-08-makes-it-possible-to-configure-custom-http-headers-when-making-requests-to-model|Makes it possible to configure custom HTTP headers when making requests to model providers]] · Change
- 2025-07-07 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-07-07-add-support-for-gemini-2-5-pro-and-flash-models-to-sap-ai-core-provider-by-tjand|Add support for Gemini 2.5 Pro and Flash models to SAP AI Core Provider]] · Change
- 2025-07-03 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-07-03-add-support-for-claude-sonnet-4-and-opus-4-model-in-sap-ai-core-provider-thanks|Add support for Claude Sonnet 4 and Opus 4 model in SAP AI Core provider…]] · Change
- 2025-07-03 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-07-03-improved-embeddings-for-semantic-search|Improved embeddings for semantic search]] · Change
- 2025-07-02 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-02-2-model-support-changes-in-v0-1-9|2 Model Support changes in v0.1.9]] · Digest
- 2025-07-02 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-07-02-updating-llm-settings-are-now-applied-to-existing-conversations-after-stopping-a|Updating LLM settings are now applied to existing conversations after stopping…]] · Change
- 2025-07-01 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-01-5-model-support-changes-in-v0-1-8|5 Model Support changes in v0.1.8]] · Digest

**2025-06**

- 2025-06-29 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-06-29-2-model-support-changes-in-v3-18-1|2 Model Support changes in v3.18.1]] · Digest
- 2025-06-28 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-06-28-release-notes-at-https-github-com-google-gemini-gemini-cli-discussions-2301|Release notes at: (source link)]] · Change
- 2025-06-28 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-06-28-release-notes-for-0-1-6-at-https-github-com-google-gemini-gemini-cli-discussions|Release Notes for 0.1.6 at (source link)]] · Change
- 2025-06-27 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-06-27-5-model-support-changes-in-v0-85-0|5 Model Support changes in v0.85.0]] · Digest
- 2025-06-26 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-06-26-3-model-support-changes-in-v3-18-0|3 Model Support changes in v3.18.0]] · Digest
- 2025-06-24 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-06-24-2-model-support-changes-in-0-46-0|2 Model Support changes in 0.46.0]] · Digest
- 2025-06-20 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-06-20-fixed-cli-displaying-incorrect-default-model-for-anthropic-provider-by-neubig-in|Fixed CLI displaying incorrect default model for Anthropic provider by @neubig…]] · Change
- 2025-06-16 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-06-16-enterprise-and-edu-users-can-also-now-choose-from-the-full-set-of-chatgpt-models-1ea372|Expanded Model Support for Custom GPTs]] · Change
- 2025-06-13 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-06-13-in-some-cases-a-chain-of-thought-reasoning-will-show-up-unexpectedly-for-simple|In some cases, a “chain of thought” reasoning will show up unexpectedly for simple queries]] · Change
- 2025-06-12 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-06-12-upload-files-and-access-model-selector-on-mobile|Upload files and access model selector on mobile]] · Change
- 2025-06-12 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-06-12-creators-can-now-choose-from-the-full-set-of-chatgpt-models-gpt-4o-o3-o4-mini-an-ad1adf|Creators can now choose from the full set of ChatGPT models…]] · Change
- 2025-06-12 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-06-12-4-model-support-changes-in-v3-17-13|4 Model Support changes in v3.17.13]] · Digest
- 2025-06-12 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-06-12-once-connected-try-it-in-any-channel-with-cursor-and-write-a-prompt-use-the-comm|Once connected, try it in any channel with @Cursor and write a prompt]] · Change
- 2025-06-10 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-06-10-free-grok-model-available-access-grok-3-completely-free-through-the-cline-provid|Free Grok Model Available! Access Grok 3 completely free through the Cline provider]] · Change
- 2025-06-10 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-06-10-prevented-llm-settings-reset-when-page-loses-focus-during-initial-setup-by-llama|Prevented LLM settings reset when page loses focus during initial setup]] · Change
- 2025-06-05 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-06-05-3-model-support-changes-in-v3-17-10|3 Model Support changes in v3.17.10]] · Digest
- 2025-06-05 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-06-05-add-support-for-gemini-2-5-pro-preview-06-05-model-to-vertex-ai-and-google-gemin|Add support for Gemini 2.5 Pro Preview 06-05 model to Vertex AI and Google Gemini…]] · Change
- 2025-06-03 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-06-03-5-model-support-changes-in-v3-17-9|5 Model Support changes in v3.17.9]] · Digest

**2025-05**

- 2025-05-30 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-05-30-6-model-support-changes-in-v0-84-0|6 Model Support changes in v0.84.0]] · Digest
- 2025-05-28 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-05-28-2-model-support-changes-in-v3-17-6|2 Model Support changes in v3.17.6]] · Digest
- 2025-05-22 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-05-22-add-support-for-anthropic-claude-sonnet-4-and-claude-opus-4-in-both-anthropic-an|Add support for Anthropic Claude Sonnet 4 and Claude Opus 4 in both Anthropic…]] · Change
- 2025-05-22 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-05-22-add-support-for-claude-4-models-sonnet-4-and-opus-4-in-aws-bedrock-and-vertex-ai|Add support for Claude 4 models (Sonnet 4 and Opus 4) in AWS Bedrock and Vertex AI…]] · Change
- 2025-05-22 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-05-22-2-model-support-changes-in-v3-17-1|2 Model Support changes in v3.17.1]] · Digest
- 2025-05-18 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-05-18-2-model-support-changes-in-v3-16-1|2 Model Support changes in v3.16.1]] · Digest
- 2025-05-14 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-05-14-since-its-launch-in-the-api-in-april-gpt-4-1-has-become-a-favorite-among-develop-286eb2|Releasing GPT-4.1 in ChatGPT for all paid users]] · Change
- 2025-05-14 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-05-14-2-model-support-changes-in-v3-15-4|2 Model Support changes in v3.15.4]] · Digest
- 2025-05-12 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-05-12-update-gemini-in-openrouter-cline-providers-to-use-implicit-caching|Update Gemini in OpenRouter/Cline providers to use implicit caching]] · Change
- 2025-05-12 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-05-12-enabled-prompt-caching-for-claude-3-7-sonnet-model-through-openrouter-by-polly20|Enabled prompt caching for claude-3.7-sonnet model through OpenRouter]] · Change
- 2025-05-10 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-05-10-7-model-support-changes-in-v3-15-0|7 Model Support changes in v3.15.0]] · Digest
- 2025-05-09 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-05-09-12-model-support-changes-in-v0-83-0|12 Model Support changes in v0.83.0]] · Digest
- 2025-05-03 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-05-03-5-model-support-changes-in-v3-14-0|5 Model Support changes in v3.14.0]] · Digest

**2025-04**

- 2025-04-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-04-29-we-ve-reverted-the-most-recent-update-to-gpt-4o-due-to-issues-with-overly-agreea-097503|Updates to GPT-4o]] · Change
- 2025-04-25 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-04-25-we-re-making-additional-improvements-to-gpt-4o-optimizing-when-it-saves-memories|Improvements to GPT-4o]] · Change
- 2025-04-25 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-04-25-add-prompt-caching-to-gemini-models-in-cline-openrouter-providers|Add prompt caching to gemini models in cline / openrouter providers]] · Change
- 2025-04-24 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-04-24-4-model-support-changes-in-v3-13-2|4 Model Support changes in v3.13.2]] · Digest
- 2025-04-19 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-04-19-4-model-support-changes-in-v3-13-0|4 Model Support changes in v3.13.0]] · Digest
- 2025-04-15 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-04-15-new-model-update-by-0xtoshii-in-https-github-com-cline-cline-pull-2892|NEW model update]] · Change
- 2025-04-14 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-04-14-6-model-support-changes-in-v0-82-0|6 Model Support changes in v0.82.0]] · Digest
- 2025-04-14 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-04-14-add-gpt-4-1-by-saoudrizwan-in-https-github-com-cline-cline-pull-2880|Add gpt-4.1]] · Change
- 2025-04-12 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-04-12-2-model-support-changes-in-v3-12-0|2 Model Support changes in v3.12.0]] · Digest
- 2025-04-10 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-04-10-add-support-for-xai-s-provider-s-grok-3-models|Add support for xAI's provider's Grok 3 models]] · Change
- 2025-04-06 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-04-06-add-recommended-models-for-cline-provider|Add recommended models for Cline provider]] · Change
- 2025-04-04 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-04-04-4-model-support-changes-in-v0-81-0|4 Model Support changes in v0.81.0]] · Digest
- 2025-04-04 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-04-04-add-gemini-2-5-pro-preview-03-25-to-google-provider|Add Gemini 2.5 Pro Preview 03-25 to Google Provider]] · Change
- 2025-04-02 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-04-02-2-model-support-changes-in-0-31-0|2 Model Support changes in 0.31.0]] · Digest
- 2025-04-01 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-04-01-3-model-support-changes-in-v3-8-5|3 Model Support changes in v3.8.5]] · Digest

**2025-03**

- 2025-03-31 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-03-31-3-model-support-changes-in-v0-80-0|3 Model Support changes in v0.80.0]] · Digest
- 2025-03-27 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-03-27-we-ve-made-improvements-to-gpt-4o-it-now-feels-more-intuitive-creative-and-colla|ChatGPT makes improvements to GPT-4o—it now feels more intuitive, creative…]] · Change
- 2025-03-26 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-03-26-4-model-support-changes-in-v3-8-3|4 Model Support changes in v3.8.3]] · Digest
- 2025-03-25 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-03-25-2-model-support-changes-in-v0-79-0|2 Model Support changes in v0.79.0]] · Digest
- 2025-03-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-03-23-2-model-support-changes-in-0-48-x|2 Model Support changes in 0.48.x]] · Digest
- 2025-03-21 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-03-21-6-model-support-changes-in-v0-78-0|6 Model Support changes in v0.78.0]] · Digest
- 2025-03-18 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-03-18-o1-and-o3-mini-now-offer-python-powered-data-analysis-in-chatgpt-you-can-now-ask-bfa530|o1 and o3-mini now offer Python-powered data analysis in ChatGPT]] · Change
- 2025-03-18 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-03-18-make-microagents-available-in-the-event-stream-as-recall-observations-accessible|Make microagents available in the event stream as recall observations…]] · Change
- 2025-03-13 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-03-13-2-model-support-changes-in-v0-77-0|2 Model Support changes in v0.77.0]] · Digest
- 2025-03-11 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-03-11-sonnet-3-7-thinking-we-ve-made-a-few-improvements-to-3-7-prompting-thinking-will|Sonnet 3.7 thinking: We've made a few improvements to 3.7 prompting]] · Change
- 2025-03-11 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-03-11-3-model-support-changes-in-0-47-x|3 Model Support changes in 0.47.x]] · Digest
- 2025-03-10 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-03-10-16-model-support-changes-in-v0-76-0|16 Model Support changes in v0.76.0]] · Digest
- 2025-03-10 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-03-10-2-model-support-changes-in-v3-6-9|2 Model Support changes in v3.6.9]] · Digest
- 2025-03-07 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-03-07-default-version-of-claude-is-now-claude-3-7-sonnet-20250219-by-tofarr-in-https-g|Default version of Claude is now claude-3-7-sonnet-20250219]] · Change
- 2025-03-06 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-03-06-add-new-gemini-models-to-gcp-vertex-thanks-shohei-ihaya-and-claude-models-asksag|Add new Gemini models to GCP Vertex (thanks @shohei-ihaya!) and Claude models…]] · Change
- 2025-03-04 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-03-04-4-model-support-changes-in-v0-75-0|4 Model Support changes in v0.75.0]] · Digest
- 2025-03-03 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-03-03-add-gemini-flash-models-to-vertex-provider-thanks-jpaodev|Add Gemini Flash models to Vertex provider (thanks @jpaodev!)]] · Change
- 2025-03-01 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-03-01-add-enable-extended-thinking-option-for-claude-3-7-sonnet-with-ability-to-set-di|Add 'Enable extended thinking' option for Claude 3.7 Sonnet, with ability to set…]] · Change

**2025-02**

- 2025-02-27 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-02-27-allow-selecting-the-claude-3-7-model-from-via-the-anthropic-provider-by-amanape|Allow selecting the Claude 3.7 model from via the Anthropic provider]] · Change
- 2025-02-19 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-02-19-better-error-when-llm-settings-do-not-exist-by-amanape-in-https-github-com-all-h|Better error when LLM settings do not exist]] · Change
- 2025-02-06 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-02-06-4-model-support-changes-in-v0-74-0|4 Model Support changes in v0.74.0]] · Digest
- 2025-02-04 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-02-04-2-model-support-changes-in-0-23-0|2 Model Support changes in 0.23.0]] · Digest

**2025-01**

- 2025-01-31 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-01-31-5-model-support-changes-in-v0-73-0|5 Model Support changes in v0.73.0]] · Digest
- 2025-01-30 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-01-30-save-last-used-api-model-when-switching-between-plan-and-act-for-users-that-like|Save last used API/model when switching between Plan and Act, for users that like…]] · Change
- 2025-01-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-01-23-deepseek-models-deepseek-r1-and-deepseek-v3-are-supported-in-0-45-and-0-44-you-c|Deepseek models: Deepseek R1 and Deepseek v3 are supported in 0.45 and 0.44]] · Change
- 2025-01-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-01-23-better-codebase-understanding-we-ve-trained-a-new-model-for-codebase-understandi|Better Codebase Understanding: We've trained a new model for Codebase Understanding]] · Change
- 2025-01-22 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-01-22-2-model-support-changes-in-0-21-0|2 Model Support changes in 0.21.0]] · Digest
- 2025-01-21 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-01-21-add-vs-code-lm-api-provider-to-run-models-provided-by-other-vs-code-extensions-e|Add VS Code LM API provider to run models provided by other VS Code extensions…]] · Change
- 2025-01-20 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-01-20-4-model-support-changes-in-v0-72-0|4 Model Support changes in v0.72.0]] · Digest
- 2025-01-10 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-01-10-2-model-support-changes-in-v0-71-0|2 Model Support changes in v0.71.0]] · Digest

</details>

</details>

<details class="disclosure">
<summary>2024 · 75 entries (Aider 45 · ChatGPT 3 · Cline 6 · Cursor 10 · OpenHands 11)</summary>

**2024-07**

- 2024-07-18 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2024-07-18-we-re-introducing-gpt-4o-mini-the-most-capable-and-cost-efficient-small-model-av-af297b|Introducing GPT-4o mini]] · Launch

**2024-05**

- 2024-05-13 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2024-05-13-gpt-4o-is-our-newest-flagship-model-that-provides-gpt-4-level-intelligence-that-297427|Introducing GPT-4o]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 73 (Aider 45 · ChatGPT 1 · Cline 6 · Cursor 10 · OpenHands 11)</summary>

**2024-12**

- 2024-12-26 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-12-26-3-model-support-changes-in-v0-70-0|3 Model Support changes in v0.70.0]] · Digest
- 2024-12-13 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-12-13-2-model-support-changes-in-v0-69-0|2 Model Support changes in v0.69.0]] · Digest
- 2024-12-13 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2024-12-13-projects-provide-a-new-way-to-group-files-and-chats-for-personal-use-simplifying|Projects provide a new way to group files and chats for personal use, simplifying…]] · Change
- 2024-12-10 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-12-10-4-model-support-changes-in-v0-68-0|4 Model Support changes in v0.68.0]] · Digest
- 2024-12-06 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-12-06-support-for-new-amazon-bedrock-nova-models|Support for new Amazon Bedrock Nova models]] · Change
- 2024-12-01 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-12-01-pdf-support-for-sonnet-and-gemini-models|PDF support for Sonnet and Gemini models]] · Change

**2024-11**

- 2024-11-26 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-11-26-added-alias-config-to-define-custom-model-aliases-https-aider-chat-docs-config-m|Added --alias config to define custom model…]] · Change
- 2024-11-21 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-11-21-7-model-support-changes-in-v0-64-0|7 Model Support changes in v0.64.0]] · Digest
- 2024-11-15 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-11-15-add-a-general-utility-that-automatically-converts-function-calling-llm-requests|Add a general utility that automatically converts function-calling LLM requests…]] · Change
- 2024-11-13 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-11-13-web-command-just-adds-the-page-to-the-chat-without-triggering-an-llm-response|/web command just adds the page to the chat, without triggering an LLM response]] · Change
- 2024-11-04 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-11-04-4-model-support-changes-in-v0-62-0|4 Model Support changes in v0.62.0]] · Digest
- 2024-11-01 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-11-01-2-model-support-changes-in-v0-61-0|2 Model Support changes in v0.61.0]] · Digest

**2024-10**

- 2024-10-31 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-10-31-support-prompt-caching-on-the-latest-claude-3-5-sonnet-20241022-by-xingyaoww-in|Support prompt caching on the latest claude-3-5-sonnet-20241022]] · Change
- 2024-10-28 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2024-10-28-cline-now-uses-anthropic-s-new-computer-use-https-www-anthropic-com-news-3-5-mod|Cline now uses Anthropic's new…]] · Change
- 2024-10-22 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-10-22-5-model-support-changes-in-v0-60-0|5 Model Support changes in v0.60.0]] · Digest
- 2024-10-09 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2024-10-09-4-model-support-changes-in-v2-0-0|4 Model Support changes in v2.0.0]] · Digest
- 2024-10-04 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-10-04-sanity-checks-the-editor-model-on-launch-now-same-as-main-and-weak-models|Sanity checks the --editor-model on launch now, same as main and weak models]] · Change

**2024-09**

- 2024-09-29 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-09-29-6-model-support-changes-in-v0-58-0|6 Model Support changes in v0.58.0]] · Digest
- 2024-09-26 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-09-26-display-full-model-name-in-settings-ui-3900-by-iaavas-in-https-github-com-all-ha|Display full model name in Settings UI (♯3900)]] · Change
- 2024-09-21 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-09-21-6-model-support-changes-in-v0-57-0|6 Model Support changes in v0.57.0]] · Digest
- 2024-09-20 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-09-20-reduced-safety-thresholds-for-gemini-by-tobitege-in-https-github-com-all-hands-a|Reduced safety thresholds for Gemini]] · Change
- 2024-09-14 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2024-09-14-update-this-feature-is-now-opt-in-in-v1-8-0-use-problems-in-the-textarea-automat|Update: This feature is now opt-in in v1.8.0 (use @problems in the textarea)]] · Change
- 2024-09-12 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2024-09-12-adds-support-for-azure-openai-and-google-gemini-free-for-up-to-15-requests-per-m|Adds support for Azure OpenAI and Google Gemini (free for up to 15 requests per minute!)]] · Change
- 2024-09-09 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-09-09-3-model-support-changes-in-v0-56-0|3 Model Support changes in v0.56.0]] · Digest
- 2024-09-04 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-09-04-3-model-support-changes-in-v0-55-0|3 Model Support changes in v0.55.0]] · Digest
- 2024-09-04 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-09-04-2-model-support-changes-in-0-9-2|2 Model Support changes in 0.9.2]] · Digest

**2024-08**

- 2024-08-29 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-08-29-2-model-support-changes-in-0-9-1|2 Model Support changes in 0.9.1]] · Digest
- 2024-08-28 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-08-28-4-model-support-changes-in-v0-54-0|4 Model Support changes in v0.54.0]] · Digest
- 2024-08-27 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-08-27-4-model-support-changes-in-v0-53-0|4 Model Support changes in v0.53.0]] · Digest
- 2024-08-23 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-08-23-default-openai-model-is-now-gpt-4o-2024-08-06|Default OpenAI model is now gpt-4o-2024-08-06]] · Change
- 2024-08-23 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-08-23-enhance-the-llm-class-with-async-support-by-tobitege-in-https-github-com-all-han|Enhance the LLM class with async support]] · Change
- 2024-08-20 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-08-20-prompt-caching-for-anthropic-models-with-cache-prompts|Prompt caching for Anthropic models with --cache-prompts]] · Change
- 2024-08-15 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2024-08-15-adds-support-for-prompt-caching-https-www-anthropic-com-news-prompt-caching-to-r|Adds support for Prompt Caching((source link)]] · Change
- 2024-08-13 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-08-13-infinite-output-for-deepseek-coder-mistral-models-in-addition-to-anthropic-s-mod|Infinite output for DeepSeek Coder, Mistral models in addition to Anthropic's models]] · Change
- 2024-08-11 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2024-08-11-adds-option-to-choose-other-claude-models-gpt-4o-deepseek-and-mistral-if-you-use|Adds option to choose other Claude models…]] · Change
- 2024-08-10 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-08-10-5-model-support-changes-in-v0-49-0|5 Model Support changes in v0.49.0]] · Digest
- 2024-08-06 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-08-06-3-model-support-changes-in-v0-48-0|3 Model Support changes in v0.48.0]] · Digest
- 2024-08-01 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-08-01-add-unit-tests-for-llm-init-function-by-neubig-in-https-github-com-opendevin-ope|Add unit tests for LLM init function]] · Change

**2024-07**

- 2024-07-31 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-07-31-added-strong-model-as-a-fallback-for-commit-messages-and-chat-summaries|Added strong model as a fallback for commit messages (and chat summaries)]] · Change
- 2024-07-29 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-07-29-fall-back-to-main-model-if-weak-model-is-unable-to-generate-a-commit-message|Fall back to main model if weak model is unable to generate a commit message]] · Change
- 2024-07-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-07-23-new-default-model-we-ve-made-claude-3-5-sonnet-the-default-model-for-users|New Default Model: We've made Claude 3.5 Sonnet the default model for users]] · Change
- 2024-07-19 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-07-19-4-model-support-changes-in-0-8-1|4 Model Support changes in 0.8.1]] · Digest
- 2024-07-18 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-07-18-gpt-4o-mini-scores-like-the-original-gpt-3-5-on-aider-s-code-editing-benchmark-u|GPT 4o mini scores like the original GPT 3.5 on aider's code editing benchmark…]] · Change
- 2024-07-16 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-07-16-simplified-output-of-models|Simplified output of --models]] · Change
- 2024-07-07 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-07-07-2-model-support-changes-in-v0-43-0|2 Model Support changes in v0.43.0]] · Digest
- 2024-07-05 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-07-05-3-model-support-changes-in-0-7-1|3 Model Support changes in 0.7.1]] · Digest
- 2024-07-01 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-07-01-4-model-support-changes-in-v0-41-0|4 Model Support changes in v0.41.0]] · Digest

**2024-06**

- 2024-06-29 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-06-29-2-model-support-changes-in-0-7-0|2 Model Support changes in 0.7.0]] · Digest
- 2024-06-24 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-06-24-2-model-support-changes-in-v0-40-0|2 Model Support changes in v0.40.0]] · Digest
- 2024-06-20 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-06-20-2-model-support-changes-in-v0-39-0|2 Model Support changes in v0.39.0]] · Digest
- 2024-06-08 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-06-08-update-0-35-1-disables-copilot-partial-accepts-by-default-and-makes-the-keybindi|UPDATE (0.35.1): Disables Copilot++ partial accepts by default and makes…]] · Change
- 2024-06-04 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-06-04-improved-prompts-when-no-files-have-been-added-to-chat-to-solicit-llm-file-sugge|Improved prompts when no files have been added to chat to solicit LLM file suggestions]] · Change

**2024-05**

- 2024-05-26 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-05-26-gemini-1-5-flash-is-available-in-long-context-mode|Gemini 1.5 Flash is available in long-context mode]] · Change
- 2024-05-26 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-05-26-gpt-4o-in-interpreter-mode|GPT-4o in Interpreter Mode]] · Change
- 2024-05-22 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-05-22-aider-automatically-lints-and-fixes-after-every-llm-edit|Aider automatically lints and fixes after every LLM edit]] · Change
- 2024-05-13 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-05-13-3-model-support-changes-in-v0-35-0|3 Model Support changes in v0.35.0]] · Digest
- 2024-05-10 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-05-10-added-explicit-model-settings-for-openrouter-anthropic-claude-3-opus-gpt-3-5-tur|Added explicit model settings for openrouter/anthropic/claude-3-opus, gpt-3.5-turbo]] · Change
- 2024-05-08 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-05-08-added-native-support-for-deepseek-models-https-aider-chat-docs-llms-html-deepsee|Added native support for Deepseek…]] · Change
- 2024-05-07 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-05-07-4-model-support-changes-in-v0-32-0|4 Model Support changes in v0.32.0]] · Digest
- 2024-05-02 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-05-02-switch-models-during-the-chat-with-model-name-and-search-the-list-of-available-m|Switch models during the chat with /model name and search the list of available…]] · Change

**2024-04**

- 2024-04-24 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-04-24-5-model-support-changes-in-v0-30-0|5 Model Support changes in v0.30.0]] · Digest
- 2024-04-21 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-04-21-4-model-support-changes-in-v0-29-0|4 Model Support changes in v0.29.0]] · Digest
- 2024-04-12 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-04-12-new-gpt-4-model-as-of-a-couple-of-days-ago-you-can-try-out-gpt-4-turbo-2024-04-0|New GPT-4 model: As of a couple of days ago, you can try out gpt-4-turbo-2024-04-09…]] · Change
- 2024-04-09 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-04-09-4-model-support-changes-in-v0-28-0|4 Model Support changes in v0.28.0]] · Digest

**2024-03**

- 2024-03-20 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-03-20-stable-claude-support-all-the-newest-claude-models-are-available-for-pro-and-api|Stable Claude Support]] · Change
- 2024-03-12 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-03-12-if-you-re-a-pro-or-business-user-you-can-add-claude-3-opus-as-a-custom-model-in|Claude Support]] · Change
- 2024-03-08 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-03-08-2-model-support-changes-in-v0-26-0|2 Model Support changes in v0.26.0]] · Digest

**2024-02**

- 2024-02-10 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-02-10-default-gpt-3-5-model-is-now-gpt-3-5-turbo-0125|Default GPT 3.5 model is now gpt-3.5-turbo-0125]] · Change
- 2024-02-03 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-02-03-added-support-for-model-gpt-4-0125-preview-and-openai-s-alias-model-gpt-4-turbo|Added support for --model gpt-4-0125-preview and OpenAI's alias…]] · Change

**2024-01**

- 2024-01-25 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-01-25-both-pro-and-api-key-users-can-also-try-out-gpt-4-0125-preview-by-configuring-th|Both pro and API key users can also try out gpt-4-0125-preview by configuring…]] · Change
- 2024-01-18 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-01-18-cursor-fast-this-is-a-new-model-available-in-command-k-and-chat-expect-it-to-be|"cursor-fast": This is a new model available in command-k and chat]] · Change
- 2024-01-15 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2024-01-15-cursor-fast-is-a-newly-trained-model-between-gpt-3-5-and-gpt-4-coding-capabiliti-bb4c11|Cursor-Fast is a newly trained model between gpt-3.5 and gpt-4 coding capabilities…]] · Change
- 2024-01-04 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-01-04-add-images-to-the-chat-to-automatically-use-gpt-4-vision-by-joshuavial|Add images to the chat to automatically use GPT-4 Vision, by @joshuavial]] · Change

</details>

</details>

<details class="disclosure">
<summary>2023 · 40 entries (Aider 17 · ChatGPT 13 · Cursor 10)</summary>

**2023-07**

- 2023-07-28 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-07-28-long-ai-completions-8c21b2|Long AI completions]] · Launch
- 2023-07-19 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-07-19-we-re-doubling-the-number-of-messages-chatgpt-plus-customers-can-send-with-gpt-4|Higher message limits for GPT-4]] · Policy

**2023-05**

- 2023-05-20 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-05-20-upgrades-to-gpt-4-e59675|Upgrades to GPT-4]] · Launch
- 2023-05-03 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-05-03-we-are-deprecating-the-legacy-gpt-3-5-model-on-may-10th-users-will-be-able-to-co|We are deprecating the Legacy (GPT-3.5) model on May 10th]] · Policy

**2023-03**

- 2023-03-14 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-03-14-we-re-excited-to-bring-gpt-4-our-latest-model-to-our-chatgpt-plus-subscribers-gp-7153e9|Announcing GPT-4 in ChatGPT]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 35 (Aider 17 · ChatGPT 10 · Cursor 8)</summary>

**2023-12**

- 2023-12-20 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-12-20-3-model-support-changes-in-v0-19-0|3 Model Support changes in v0.19.0]] · Digest
- 2023-12-16 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-12-16-ai-review-beta-this-is-a-new-experimental-feature-that-let-s-gpt-4-scan-your-git|AI Review (beta)]] · Change

**2023-11**

- 2023-11-17 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-11-17-3-model-support-changes-in-v0-18-0|3 Model Support changes in v0.18.0]] · Digest
- 2023-11-10 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-11-10-new-models-you-can-plug-in-your-api-key-to-try-out-the-newest-gpt-4-and-gpt-3-tu|New models: you can plug in your API key to try out the newest gpt-4 and gpt-3 turbo…]] · Change
- 2023-11-07 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-11-07-2-model-support-changes-in-v0-17-0|2 Model Support changes in v0.17.0]] · Digest

**2023-10**

- 2023-10-18 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-10-18-show-models-supported-by-api-key-if-requested-model-isn-t-available|Show models supported by api/key if requested model isn't available]] · Change
- 2023-10-17 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-10-17-browsing-which-we-re-launched-a-few-weeks-ago-is-moving-out-of-beta-plus-and-ent|Browsing is now out of beta]] · Change
- 2023-10-16 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-10-16-we-ve-integrated-dall-e-3-with-chatgpt-allowing-it-to-respond-to-your-requests-w-ad3caf|DALL·E 3 is now rolling out in beta]] · Change
- 2023-10-01 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-10-01-use-edit-in-the-chat-to-edit-a-whole-file-if-less-than-400-lines-expect-the-edit-78e4ac|Use /edit in the chat to edit a whole file (if less than 400 lines)]] · Change

**2023-09**

- 2023-09-30 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-09-30-show-models-supported-by-api-key-if-requested-model-isn-t-available|Show models supported by api/key if requested model isn't available]] · Change
- 2023-09-27 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-09-27-choose-browse-with-bing-in-the-selector-under-gpt-4|Choose Browse with Bing in the selector under GPT-4]] · Change

**2023-08**

- 2023-08-11 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-08-11-2-model-support-changes-in-v0-12-0|2 Model Support changes in v0.12.0]] · Digest
- 2023-08-08 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-08-08-defend-against-gpt-3-5-or-non-openai-models-suggesting-filenames-surrounded-by-a|Defend against GPT-3.5 or non-OpenAI models suggesting filenames surrounded by asterisks]] · Change
- 2023-08-03 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-08-03-we-re-rolling-out-a-bunch-of-small-updates-to-improve-the-chatgpt-experience-shi|Updates to ChatGPT]] · Change
- 2023-08-02 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-08-02-defend-against-gpt-3-5-or-non-openai-models-suggesting-filenames-surrounded-by-a|Defend against GPT-3.5 or non-OpenAI models suggesting filenames surrounded by asterisks]] · Change

**2023-07**

- 2023-07-24 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-07-24-benchmarked-https-aider-chat-docs-benchmarks-html-at-64-7-for-gpt-4-diff-no-regr|Benchmarked((source link) at 64.7% for gpt-4/diff…]] · Change
- 2023-07-22 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-07-22-benchmarked-https-aider-chat-docs-benchmarks-html-at-64-7-for-gpt-4-diff-no-regr|Benchmarked((source link) at 64.7% for gpt-4/diff…]] · Change
- 2023-07-16 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-07-16-support-for-the-openai-models-in-azure-https-aider-chat-docs-faq-html-azure|Support for the OpenAI models in Azure((source link)]] · Change
- 2023-07-12 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-07-12-3-model-support-changes-in-v0-8-3|3 Model Support changes in v0.8.3]] · Digest
- 2023-07-08 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-07-08-2-model-support-changes-in-v0-8-1|2 Model Support changes in v0.8.1]] · Digest
- 2023-07-08 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-07-08-3-model-support-changes-in-v0-8-2|3 Model Support changes in v0.8.2]] · Digest
- 2023-07-06 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-07-06-benchmark-comparing-code-editing-in-gpt-3-5-and-gpt-4-https-aider-chat-docs-benc|Benchmark comparing code editing in GPT-3.5…]] · Change

**2023-06**

- 2023-06-22 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-06-22-browsing-plus-users-can-now-use-browsing-to-get-comprehensive-answers-and-curren|Browsing: Plus users can now use Browsing to get comprehensive answers and current…]] · Change
- 2023-06-17 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-06-17-2-model-support-changes-in-v0-6-2|2 Model Support changes in v0.6.2]] · Digest
- 2023-06-07 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-06-07-added-support-for-gpt-3-5-turbo-and-gpt-4-32k|Added support for gpt-3.5-turbo and gpt-4-32k]] · Change
- 2023-06-01 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-06-01-check-out-the-more-tab-to-have-gpt-3-5-or-gpt-4-review-your-code-periodically-fo|AI Linting]] · Change

**2023-05**

- 2023-05-04 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-05-04-gpt-4-support-now-available-for-project-generation|GPT-4 support now available for project generation]] · Change

**2023-04**

- 2023-04-19 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-04-19-3-model-support-changes-in-0-2-6|3 Model Support changes in 0.2.6]] · Digest
- 2023-04-14 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-04-14-gpt-4-support|GPT-4 support]] · Change

**2023-03**

- 2023-03-30 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-03-30-use-an-openai-api-key-for-unlimited-requests-at-cost-gpt-4-access-if-available|Use an OpenAI API key for unlimited requests at cost (GPT-4 access if available)]] · Change
- 2023-03-23 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-03-23-third-party-plugins-an-experimental-model-that-knows-when-and-how-to-use-externa|Third-party plugins: An experimental model that knows when and how to use external plugins]] · Change
- 2023-03-23 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-03-23-code-interpreter-an-experimental-chatgpt-model-that-can-use-python-and-handles-u|Code Interpreter: An experimental ChatGPT model that can use Python, and handles…]] · Change

**2023-02**

- 2023-02-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-02-09-default-the-standard-chatgpt-model|Default: the standard ChatGPT model]] · Change

**2023-01**

- 2023-01-30 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-01-30-we-ve-upgraded-the-chatgpt-model-with-improved-factuality-and-mathematical-capab|Factuality and mathematical improvements]] · Change
- 2023-01-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]] · Change

</details>

</details>

</div>
<!-- chronolog:end -->