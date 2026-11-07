---
card_id: open-webui-2025-08-21-98325a
date: '2025-08-21'
description: "Open WebUI · 2025-08-21 · Model Support: 7 changes in v0.6.23 — \U0001F5A5️
  **Improved Command List Visibility on Small Screens**: Resolved an issue where the
  top items…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 955
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8821334f6505671ae80e57c1ce500345b60909fac3a8733cf9226559bf1d41ff
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-21-98325a
  comparison: ''
  date: '2025-08-21'
  description: 'Open WebUI — v0.6.23: 7 Model Support changes'
  evidence:
  - quote: "\U0001F5A5️ **Improved Command List Visibility on Small Screens**: Resolved
      an issue where the top items in command lists (e.g., Knowledge Base, Models,
      Prompts) were hidden or overlapped by the header on smaller screen sizes or
      specific browser zoom levels. The command option lists now dynamically adjust
      their height, ensuring all items are fully visible and accessible with proper
      scrolling."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F6E0️ **Resolved Model Sorting TypeError with Null Names**: Fixed
      a \"TypeError\" that occurred in the \"/api/models\" endpoint when sorting models
      with null or missing names. The model sorting logic has been improved to gracefully
      handle such edge cases by ensuring that model IDs and names are treated as empty
      strings if their values are null or undefined, preventing comparison errors
      and improving API stability."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F6E0️ **Improved OpenAI Model List Handling for Null Names**: Fixed
      an edge case where some OpenAI-compatible API providers might return models
      with a null value for their 'name' field. This could lead to issues like broken
      model list sorting. The system now gracefully handles these instances by removing
      the null 'name' key, ensuring stable model retrieval and display."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F6E0️ **Improved Azure OpenAI GPT-5 Parameter Handling**: Fixed
      an issue with Azure OpenAI SDK parameter handling to correctly support GPT-5
      models. The 'max_tokens' parameter is now appropriately converted to 'max_completion_tokens'
      for GPT-5 models, ensuring consistent behavior and proper function execution
      similar to existing o-series models."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F6E0️ **Improved OpenAI API Base URL Handling**: Fixed an issue
      where a trailing slash in the 'OPENAI_API_BASE_URL' configuration could lead
      to models not being detected or the endpoint failing. The system now automatically
      removes trailing slashes from the configured URL, ensuring robust and consistent
      connections to OpenAI-compatible APIs."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F6E0️ **Resolved Model Sorting Errors with Null or Undefined Names**:
      Fixed multiple \"TypeError\" instances that occurred when attempting to sort
      model lists where model names were null or undefined. The sorting logic across
      various UI components (including Ollama model selection, leaderboard, and admin
      model settings) has been made more robust by gracefully handling absent model
      names, preventing crashes and ensuring consistent alphabetical sorting based
      on available name or ID."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F6C2 **Environment Variable for Admin Access Control**: The environment
      variable \"ENABLE_ADMIN_WORKSPACE_CONTENT_ACCESS\" has been renamed to \"BYPASS_ADMIN_ACCESS_CONTROL\".
      This new name more accurately reflects its function as a control to allow administrators
      to bypass model access restrictions. Users are encouraged to update their configurations
      to use the new variable name; existing configurations using the old name will
      still be honored for backward compatibility."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 7-model-support-changes-in-v0-6-23
  source_release: open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46
  source_type: github_releases
  theme: model-support
  title: 7 Model Support changes in v0.6.23
  type: change
related_changes:
- '[[Changes/Cline/2025-08-21-feat-sap-provider-show-deployed-models-from-the-ai-core-service-instance-alongsi|feat:
  sap provider - show deployed models from the ai core service instance…]]'
- '[[Changes/Cline/2025-08-21-removing-max-tokens-from-sonic-model-by-pashpashpash-in-https-github-com-cline-c|removing
  max tokens from sonic model]]'
- '[[Changes/Cursor/2025-08-21-2-model-support-changes-in-1-5|2 Model Support changes
  in 1.5]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46]]'
source_type: github_releases
theme: model-support
title: 7 Model Support changes in v0.6.23
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Model Support changes in v0.6.23

**Open WebUI** · 2025-08-21 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.23) · from [[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|v0.6.23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🖥️ **Improved Command List Visibility on Small Screens**: Resolved an issue where the top items in command lists (e.g., Knowledge Base, Models, Prompts) were hidden or overlapped by the header on smaller screen sizes or specific browser zoom levels. The command option lists now dynamically adjust their height, ensuring all items are fully visible and accessible with proper scrolling.

> 🛠️ **Resolved Model Sorting TypeError with Null Names**: Fixed a "TypeError" that occurred in the "/api/models" endpoint when sorting models with null or missing names. The model sorting logic has been improved to gracefully handle such edge cases by ensuring that model IDs and names are treated as empty strings if their values are null or undefined, preventing comparison errors and improving API stability.

> 🛠️ **Improved OpenAI Model List Handling for Null Names**: Fixed an edge case where some OpenAI-compatible API providers might return models with a null value for their 'name' field. This could lead to issues like broken model list sorting. The system now gracefully handles these instances by removing the null 'name' key, ensuring stable model retrieval and display.

> 🛠️ **Improved Azure OpenAI GPT-5 Parameter Handling**: Fixed an issue with Azure OpenAI SDK parameter handling to correctly support GPT-5 models. The 'max_tokens' parameter is now appropriately converted to 'max_completion_tokens' for GPT-5 models, ensuring consistent behavior and proper function execution similar to existing o-series models.

> 🛠️ **Improved OpenAI API Base URL Handling**: Fixed an issue where a trailing slash in the 'OPENAI_API_BASE_URL' configuration could lead to models not being detected or the endpoint failing. The system now automatically removes trailing slashes from the configured URL, ensuring robust and consistent connections to OpenAI-compatible APIs.

> 🛠️ **Resolved Model Sorting Errors with Null or Undefined Names**: Fixed multiple "TypeError" instances that occurred when attempting to sort model lists where model names were null or undefined. The sorting logic across various UI components (including Ollama model selection, leaderboard, and admin model settings) has been made more robust by gracefully handling absent model names, preventing crashes and ensuring consistent alphabetical sorting based on available name or ID.

> 🛂 **Environment Variable for Admin Access Control**: The environment variable "ENABLE_ADMIN_WORKSPACE_CONTENT_ACCESS" has been renamed to "BYPASS_ADMIN_ACCESS_CONTROL". This new name more accurately reflects its function as a control to allow administrators to bypass model access restrictions. Users are encouraged to update their configurations to use the new variable name; existing configurations using the old name will still be honored for backward compatibility.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-21-8-interface-experience-changes-in-v0-6-23|8 Interface Experience changes in v0.6.23]] · Interface Experience
- [[Changes/Open WebUI/2025-08-21-restored-message-toolbar-icons-for-empty-messages-with-files-fixed-an-issue-wher|🐛 Restored Message Toolbar Icons for Empty Messages with Files]] · Editor Experience
- [[Changes/Open WebUI/2025-08-21-3-search-and-browsing-changes-in-v0-6-23|3 Search and Browsing changes in v0.6.23]] · Search and Browsing
- [[Changes/Open WebUI/2025-08-21-resolved-silently-dropped-streaming-response-chunks-fixed-an-issue-where-the-fin|💬 Resolved Silently Dropped Streaming Response Chunks]] · Files and Data
- [[Changes/Open WebUI/2025-08-21-3-mobile-and-desktop-changes-in-v0-6-23|3 Mobile and Desktop changes in v0.6.23]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-08-21-6-reliability-and-performance-changes-in-v0-6-23|6 Reliability and Performance changes in v0.6.23]] · Reliability and Performance
- [[Changes/Open WebUI/2025-08-21-6-safety-and-privacy-changes-in-v0-6-23|6 Safety and Privacy changes in v0.6.23]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-21-2-voice-and-audio-changes-in-v0-6-23|2 Voice and Audio changes in v0.6.23]] · Voice and Audio
- [[Changes/Open WebUI/2025-08-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-08-21-2-accessibility-and-localization-changes-in-v0-6-23|2 Accessibility and Localization changes in v0.6.23]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-21-resolved-image-generation-api-size-parameter-issue-fixed-a-bug-where-the-api-v1|🖼️ Resolved Image Generation API Size Parameter Issue]] · Image Generation
- [[Changes/Open WebUI/2025-08-21-resolved-code-block-input-issue-with-shift-enter-fixed-a-bug-where-typing-three|📝 Resolved Code Block Input Issue with Shift+Enter]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-21-5-apps-and-integrations-changes-in-v0-6-23|5 Apps and Integrations changes in v0.6.23]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-21-3-account-and-access-changes-in-v0-6-23|3 Account and Access changes in v0.6.23]] · Account and Access
- [[Changes/Open WebUI/2025-08-21-23-other-changes-in-v0-6-23|23 other changes in v0.6.23]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-08-21 · Cursor · [[Changes/Cursor/2025-08-21-2-model-support-changes-in-1-5|2 Model Support changes in 1.5]]
- Later: 2025-08-25 · Ollama · [[Changes/Ollama/2025-08-25-3-model-support-changes-in-v0-11-7|3 Model Support changes in v0.11.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-21-98325a&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-21-7-model-support-changes-in-v0-6-23.md%0ACard%20ID%3A%20open-webui-2025-08-21-98325a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->