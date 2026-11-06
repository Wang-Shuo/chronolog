---
card_id: open-webui-2024-11-19-a402d9
date: '2024-11-19'
description: "Open WebUI · 2024-11-19 · Model Support: 9 changes in v0.4.0 — **\U0001F510
  Group-Based Access Control**: Set granular access to models, knowledge, prompts,
  and tools…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 680
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6759cdc7b42e38af9b22ca94441a3c15758ca4125ceca5d0383ccb69abac8f16
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2024-11-19-a402d9
  comparison: ''
  date: '2024-11-19'
  description: 'Open WebUI — v0.4.0: 9 Model Support changes'
  evidence:
  - quote: "**\U0001F510 Group-Based Access Control**: Set granular access to models,
      knowledge, prompts, and tools based on user groups, allowing for more controlled
      and secure environments."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.4.0
  - quote: "**\U0001F6E0️ Group-Based User Permissions**: Easily manage workspace
      permissions. Grant users the ability to upload files, delete, edit, or create
      temporary chats, as well as define their ability to create models, knowledge,
      prompts, and tools."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.4.0
  - quote: "**\U0001F310 Enhanced OpenAI-Compatible Connections**: Added prefix ID
      support to avoid model ID clashes, with explicit model ID support for APIs lacking
      '/models' endpoint support, ensuring smooth operation with custom setups."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.4.0
  - quote: "**\U0001F3A8 Redesigned Model Workspace**: Freshly redesigned to improve
      usability for managing models across users and groups."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.4.0
  - quote: "**\U0001F504 Unified Reset for Models**: A one-click option has been introduced
      to reset and remove all models from the Admin Settings."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.4.0
  - quote: "**\U0001F6E0️ Manage Ollama Connections**: The \"Models\" section in Admin
      Settings has been relocated to Admin Settings > \"Connections\" > Ollama Connections.
      You can now manage Ollama instances via a dedicated \"Manage Ollama\" modal
      from \"Connections\", streamlining the setup and configuration of Ollama models."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.4.0
  - quote: "**\U0001F4CC Sticky Model Selection for New Chats**: The model chosen
      from a previous chat now persists when creating a new chat. If you click \"New
      Chat\" again from the new chat page, it will revert to your default model."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.4.0
  - quote: "**\U0001F4C2 Model List Reordering**: Temporarily removed and will be
      reintroduced in upcoming user group settings improvements."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.4.0
  - quote: '**⚙️ Default Model Setting**: Removed the ability to set a default model
      for users, will be reintroduced with user group settings in the future.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.4.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 9-model-support-changes-in-v0-4-0
  source_release: open-webui-2024-11-19-v0-4-0-github-186297307-d3ef790f
  source_type: github_releases
  theme: model-support
  title: 9 Model Support changes in v0.4.0
  type: change
related_changes:
- '[[Changes/Ollama/2024-11-15-2-model-support-changes-in-v0-4-2|2 Model Support changes
  in v0.4.2]]'
- '[[Changes/OpenHands/2024-11-15-add-a-general-utility-that-automatically-converts-function-calling-llm-requests|Add
  a general utility that automatically converts function-calling LLM requests…]]'
- '[[Changes/Dify/2024-11-18-10-model-support-changes-in-0-11-2|10 Model Support changes
  in 0.11.2]]'
source_release: '[[Releases/Open WebUI/open-webui-2024-11-19-v0-4-0-github-186297307-d3ef790f|open-webui-2024-11-19-v0-4-0-github-186297307-d3ef790f]]'
source_type: github_releases
theme: model-support
title: 9 Model Support changes in v0.4.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Model Support changes in v0.4.0

**Open WebUI** · 2024-11-19 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.4.0) · from [[Releases/Open WebUI/open-webui-2024-11-19-v0-4-0-github-186297307-d3ef790f|v0.4.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **🔐 Group-Based Access Control**: Set granular access to models, knowledge, prompts, and tools based on user groups, allowing for more controlled and secure environments.

> **🛠️ Group-Based User Permissions**: Easily manage workspace permissions. Grant users the ability to upload files, delete, edit, or create temporary chats, as well as define their ability to create models, knowledge, prompts, and tools.

> **🌐 Enhanced OpenAI-Compatible Connections**: Added prefix ID support to avoid model ID clashes, with explicit model ID support for APIs lacking '/models' endpoint support, ensuring smooth operation with custom setups.

> **🎨 Redesigned Model Workspace**: Freshly redesigned to improve usability for managing models across users and groups.

> **🔄 Unified Reset for Models**: A one-click option has been introduced to reset and remove all models from the Admin Settings.

> **🛠️ Manage Ollama Connections**: The "Models" section in Admin Settings has been relocated to Admin Settings > "Connections" > Ollama Connections. You can now manage Ollama instances via a dedicated "Manage Ollama" modal from "Connections", streamlining the setup and configuration of Ollama models.

> **📌 Sticky Model Selection for New Chats**: The model chosen from a previous chat now persists when creating a new chat. If you click "New Chat" again from the new chat page, it will revert to your default model.

> **📂 Model List Reordering**: Temporarily removed and will be reintroduced in upcoming user group settings improvements.

> **⚙️ Default Model Setting**: Removed the ability to set a default model for users, will be reintroduced with user group settings in the future.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.4.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2024-11-19-agentic-retrieval-improve-rag-accuracy-via-smart-pre-processing-of-chat-history|🗂️ Agentic Retrieval]] · Agent Mode
- [[Changes/Open WebUI/2024-11-19-user-settings-search-quickly-search-for-settings-fields-improving-ease-of-use-an|🔍 User Settings Search]] · Interface Experience
- [[Changes/Open WebUI/2024-11-19-duckduckgo-rate-limit-fix-addressed-issues-with-duckduckgo-search-integration-en|🔍 DuckDuckGo Rate Limit Fix]] · Reliability and Performance
- [[Changes/Open WebUI/2024-11-19-2-files-and-data-changes-in-v0-4-0|2 Files and Data changes in v0.4.0]] · Files and Data
- [[Changes/Open WebUI/2024-11-19-initial-setup-wizard-the-setup-process-now-explicitly-informs-users-that-they-ar|🛠️ Initial Setup Wizard]] · Account and Access
- [[Changes/Open WebUI/2024-11-19-youtube-video-attachments-fixed-issues-preventing-proper-loading-and-attachment|🎥 YouTube Video Attachments]] · Multimodal Input
- [[Changes/Open WebUI/2024-11-19-2-search-and-browsing-changes-in-v0-4-0|2 Search and Browsing changes in v0.4.0]] · Search and Browsing
- [[Changes/Open WebUI/2024-11-19-functions-moved-to-admin-panel-as-functions-operate-as-advanced-plugins-they-are|🛠️ Functions Moved to Admin Panel]] · Apps and Integrations
- [[Changes/Open WebUI/2024-11-19-2-collaboration-changes-in-v0-4-0|2 Collaboration changes in v0.4.0]] · Collaboration
- [[Changes/Open WebUI/2024-11-19-enhanced-translations-several-language-translations-including-ukrainian-norwegia|🌐 Enhanced Translations]] · Accessibility and Localization
- [[Changes/Open WebUI/2024-11-19-auto-selected-tools-in-model-editor-tools-enabled-through-the-model-editor-are-n|🔧 Auto-Selected Tools in Model Editor]] · Editor Experience
- [[Changes/Open WebUI/2024-11-19-2-safety-and-privacy-changes-in-v0-4-0|2 Safety and Privacy changes in v0.4.0]] · Safety and Privacy
- [[Changes/Open WebUI/2024-11-19-11-other-changes-in-v0-4-0|11 other changes in v0.4.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2024-11-18 · Dify · [[Changes/Dify/2024-11-18-10-model-support-changes-in-0-11-2|10 Model Support changes in 0.11.2]]
- Later: 2024-11-20 · Ollama · [[Changes/Ollama/2024-11-20-t-lu-3-https-ollama-com-library-tulu3-t-lu-3-is-a-leading-instruction-following|Tülu 3((source link) Tülu 3 is a leading instruction…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2024-11-19-a402d9&body=Card%3A%20Changes%2FOpen%20WebUI%2F2024-11-19-9-model-support-changes-in-v0-4-0.md%0ACard%20ID%3A%20open-webui-2024-11-19-a402d9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.4.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->