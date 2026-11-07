---
card_id: open-webui-2025-08-09-c7f6c4
date: '2025-08-09'
description: "Open WebUI · 2025-08-09 · Model Support: 11 changes in v0.6.19 — \U0001F4D1
  **Tabbed View for Multi-Model Responses**: You can now enable a new tabbed interface
  to view…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 943
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0a42eec4319e66a7bea6855f861108b17feca827e5fdbedef2d7ead67f7ab4d8
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-09-c7f6c4
  comparison: ''
  date: '2025-08-09'
  description: 'Open WebUI — v0.6.19: 11 Model Support changes'
  evidence:
  - quote: "\U0001F4D1 **Tabbed View for Multi-Model Responses**: You can now enable
      a new tabbed interface to view responses from multiple models. Instead of side-scrolling
      cards, this compact view organizes each model's response into its own tab, making
      it easier to compare outputs and saving vertical space. This feature can be
      toggled on or off in Interface settings."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F4CC **Quick Model Unpin Shortcut**: You can now quickly unpin a
      model by holding the Shift key and hovering over it to reveal an instant unpin
      button, streamlining your workspace customization."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F5C4️ **Comprehensive Model Configuration Management**: Administrators
      can now export the entire model configuration to a file and use a new declarative
      sync endpoint to manage models in bulk. This powerful feature enables seamless
      backups, migrations, and state replication across multiple instances."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F4C1 **Folder Knowledge Processing Restored**: Fixed a bug where
      files uploaded to folder and model knowledge bases were not being extracted
      or analyzed for Retrieval-Augmented Generation (RAG) when the 'Max Upload Count'
      setting was empty, ensuring seamless document processing and knowledge augmentation."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F9E0 **Custom Model Knowledge Base Updates Recognized**: Fixed a
      bug where custom models linked to to knowledge bases did not automatically recognize
      newly added files to those knowledge bases. Models now correctly incorporate
      the latest information from updated knowledge collections."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '✨ **More Descriptive OpenAI Router Errors**: The OpenAI-compatible API
      router now propagates detailed upstream error messages instead of returning
      a generic ''Bad Request''. This provides clear, actionable feedback for developers
      and API users, making it significantly easier to debug and resolve issues with
      model requests.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F916 **Title Generation Compatibility for GPT-5 Models**: Added
      support for 'gpt-5' models in the payload handler, which correctly converts
      the deprecated 'max_tokens' parameter to 'max_completion_tokens'. This resolves
      title generation failures and ensures seamless operation with the latest generation
      of models."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '⚙️ **Correct API ''finish_reason'' in Streaming Responses**: Fixed an
      issue where intermediate ''reasoning_content'' chunks in streaming API responses
      incorrectly reported a ''finish_reason'' of ''stop''. The ''finish_reason''
      is now correctly set to ''null'' for these chunks, ensuring compatibility with
      third-party applications that rely on this field.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '↕️ **Improved Pinned Models Drag-and-Drop Behavior**: The drag-and-drop
      functionality for reordering pinned models is now explicitly disabled on mobile
      devices, ensuring better usability and preventing potential UI conflicts or
      unexpected behavior.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F517 **Corrected \"Discover\" Links**: The \"Discover\" links for
      models, prompts, tools, and functions now point to their specific, relevant
      pages on openwebui.com, improving content discovery for users."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '⏱️ **Refined Display of AI Thought Duration**: Adjusted the display logic
      for AI thought (reasoning) durations to more accurately show very short thought
      times as "less than a second," improving clarity in AI process feedback.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 11-model-support-changes-in-v0-6-19
  source_release: open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243
  source_type: github_releases
  theme: model-support
  title: 11 Model Support changes in v0.6.19
  type: change
related_changes:
- '[[Changes/Ollama/2025-08-07-openai-always-provide-reasoning-by-drifkin-in-https-github-com-ollama-ollama-pul|openai:
  always provide reasoning]]'
- '[[Changes/Windsurf/2025-08-07-gpt-5-available|GPT-5 Available]]'
- '[[Changes/Aider/2025-08-09-5-model-support-changes-in-v0-86-0|5 Model Support changes
  in v0.86.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243|open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243]]'
source_type: github_releases
theme: model-support
title: 11 Model Support changes in v0.6.19
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Model Support changes in v0.6.19

**Open WebUI** · 2025-08-09 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.19) · from [[Releases/Open WebUI/open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243|v0.6.19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📑 **Tabbed View for Multi-Model Responses**: You can now enable a new tabbed interface to view responses from multiple models. Instead of side-scrolling cards, this compact view organizes each model's response into its own tab, making it easier to compare outputs and saving vertical space. This feature can be toggled on or off in Interface settings.

> 📌 **Quick Model Unpin Shortcut**: You can now quickly unpin a model by holding the Shift key and hovering over it to reveal an instant unpin button, streamlining your workspace customization.

> 🗄️ **Comprehensive Model Configuration Management**: Administrators can now export the entire model configuration to a file and use a new declarative sync endpoint to manage models in bulk. This powerful feature enables seamless backups, migrations, and state replication across multiple instances.

> 📁 **Folder Knowledge Processing Restored**: Fixed a bug where files uploaded to folder and model knowledge bases were not being extracted or analyzed for Retrieval-Augmented Generation (RAG) when the 'Max Upload Count' setting was empty, ensuring seamless document processing and knowledge augmentation.

> 🧠 **Custom Model Knowledge Base Updates Recognized**: Fixed a bug where custom models linked to to knowledge bases did not automatically recognize newly added files to those knowledge bases. Models now correctly incorporate the latest information from updated knowledge collections.

> ✨ **More Descriptive OpenAI Router Errors**: The OpenAI-compatible API router now propagates detailed upstream error messages instead of returning a generic 'Bad Request'. This provides clear, actionable feedback for developers and API users, making it significantly easier to debug and resolve issues with model requests.

> 🤖 **Title Generation Compatibility for GPT-5 Models**: Added support for 'gpt-5' models in the payload handler, which correctly converts the deprecated 'max_tokens' parameter to 'max_completion_tokens'. This resolves title generation failures and ensures seamless operation with the latest generation of models.

> ⚙️ **Correct API 'finish_reason' in Streaming Responses**: Fixed an issue where intermediate 'reasoning_content' chunks in streaming API responses incorrectly reported a 'finish_reason' of 'stop'. The 'finish_reason' is now correctly set to 'null' for these chunks, ensuring compatibility with third-party applications that rely on this field.

> ↕️ **Improved Pinned Models Drag-and-Drop Behavior**: The drag-and-drop functionality for reordering pinned models is now explicitly disabled on mobile devices, ensuring better usability and preventing potential UI conflicts or unexpected behavior.

> 🔗 **Corrected "Discover" Links**: The "Discover" links for models, prompts, tools, and functions now point to their specific, relevant pages on openwebui.com, improving content discovery for users.

> ⏱️ **Refined Display of AI Thought Duration**: Adjusted the display logic for AI thought (reasoning) durations to more accurately show very short thought times as "less than a second," improving clarity in AI process feedback.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-09-7-apps-and-integrations-changes-in-v0-6-19|7 Apps and Integrations changes in v0.6.19]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-09-2-editor-experience-changes-in-v0-6-19|2 Editor Experience changes in v0.6.19]] · Editor Experience
- [[Changes/Open WebUI/2025-08-09-3-enterprise-and-administration-changes-in-v0-6-19|3 Enterprise and Administration changes in v0.6.19]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-08-09-2-mobile-and-desktop-changes-in-v0-6-19|2 Mobile and Desktop changes in v0.6.19]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-08-09-2-search-and-browsing-changes-in-v0-6-19|2 Search and Browsing changes in v0.6.19]] · Search and Browsing
- [[Changes/Open WebUI/2025-08-09-customizable-floating-quick-actions-with-tool-support-take-full-control-of-your|✍️ Customizable Floating Quick Actions with Tool Support]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-08-09-15-reliability-and-performance-changes-in-v0-6-19|15 Reliability and Performance changes in v0.6.19]] · Reliability and Performance
- [[Changes/Open WebUI/2025-08-09-2-files-and-data-changes-in-v0-6-19|2 Files and Data changes in v0.6.19]] · Files and Data
- [[Changes/Open WebUI/2025-08-09-folder-system-prompt-variables-restored-fixed-a-bug-where-prompt-variables-e-g-c|📁 Folder System Prompt Variables Restored]] · Context Window
- [[Changes/Open WebUI/2025-08-09-admin-first-whisper-language-priority-the-global-whisper-language-setting-now-ac|🗣️ Admin-First Whisper Language Priority]] · Voice and Audio
- [[Changes/Open WebUI/2025-08-09-2-developer-workflow-changes-in-v0-6-19|2 Developer Workflow changes in v0.6.19]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-09-enhanced-memory-stability-and-security-refactored-memory-update-and-delete-opera|🧠 Enhanced Memory Stability and Security]] · Memory and Personalization
- [[Changes/Open WebUI/2025-08-09-4-account-and-access-changes-in-v0-6-19|4 Account and Access changes in v0.6.19]] · Account and Access
- [[Changes/Open WebUI/2025-08-09-10-safety-and-privacy-changes-in-v0-6-19|10 Safety and Privacy changes in v0.6.19]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-09-3-collaboration-changes-in-v0-6-19|3 Collaboration changes in v0.6.19]] · Collaboration
- [[Changes/Open WebUI/2025-08-09-3-accessibility-and-localization-changes-in-v0-6-19|3 Accessibility and Localization changes in v0.6.19]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-09-13-interface-experience-changes-in-v0-6-19|13 Interface Experience changes in v0.6.19]] · Interface Experience
- [[Changes/Open WebUI/2025-08-09-29-other-changes-in-v0-6-19|29 other changes in v0.6.19]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-08-09 · Aider · [[Changes/Aider/2025-08-09-5-model-support-changes-in-v0-86-0|5 Model Support changes in v0.86.0]]
- Later: 2025-08-10 · Open WebUI · [[Changes/Open WebUI/2025-08-10-chat-completion-model-id-error-resolved-a-critical-issue-where-chat-completions|🐞 Chat Completion 'model_id' Error]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-09-c7f6c4&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-09-11-model-support-changes-in-v0-6-19.md%0ACard%20ID%3A%20open-webui-2025-08-09-c7f6c4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->