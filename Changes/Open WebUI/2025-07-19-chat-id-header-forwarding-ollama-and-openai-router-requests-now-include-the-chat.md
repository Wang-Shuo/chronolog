---
card_id: open-webui-2025-07-19-32ebba
date: '2025-07-19'
description: "Open WebUI · 2025-07-19 · Model Support: \U0001F4E1 **Chat ID Header
  Forwarding**: Ollama and OpenAI router requests now include the chat ID in request
  headers…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 922
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 1302d11d1f284cc1363a6f034fbe72d300162976ae64bb61bc9611abaf67cd3a
product: open-webui
product_name: Open WebUI
record:
  ai_generated: true
  card_id: open-webui-2025-07-19-32ebba
  comparison: ''
  confidence: low
  date: '2025-07-19'
  description: "Open WebUI — v0.6.17: \U0001F4E1 **Chat ID Header Forwarding**: Ollama
    and OpenAI router requests now include the chat ID in request headers, enabling
    better request correlation and debugging capabilities across AI model integrations."
  evidence:
  - quote: "\U0001F4E1 **Chat ID Header Forwarding**: Ollama and OpenAI router requests
      now include the chat ID in request headers, enabling better request correlation
      and debugging capabilities across AI model integrations."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.17
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: open-webui
  product_name: Open WebUI
  slug: chat-id-header-forwarding-ollama-and-openai-router-requests-now-include-the-chat
  source_release: open-webui-2025-07-19-v0-6-17-github-233695159-4b5cb15b
  source_type: github_releases
  theme: model-support
  theme_matches:
  - matched_terms:
    - integrations
    score: 50
    theme: apps-integrations
  - matched_terms:
    - debugging
    score: 50
    theme: developer-workflow
  - matched_terms:
    - model
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: "\U0001F4E1 **Chat ID Header Forwarding**"
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-07-19-as-of-https-github-com-openai-codex-pull-1594-we-now-stream-the-response-from-th|As
  of (source link) we now stream the response…]]'
- '[[Changes/Gemini CLI/2025-07-19-4-model-support-changes-in-v0-1-13|4 Model Support
  changes in v0.1.13]]'
- '[[Changes/LM Studio/2025-07-19-added-tool-calling-support-for-mistral-v13-tokenizer-models-with-proper-chat-tem|Added
  tool calling support for Mistral v13 tokenizer models (with proper chat templates)]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-07-19-v0-6-17-github-233695159-4b5cb15b|open-webui-2025-07-19-v0-6-17-github-233695159-4b5cb15b]]'
source_type: github_releases
theme: model-support
title: "\U0001F4E1 Chat ID Header Forwarding"
type: change
---

<!-- chronolog:begin region="header" -->
# 📡 **Chat ID Header Forwarding**

**Open WebUI** · 2025-07-19 · [[Themes/model-support|Model Support]] · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.17) · from [[Releases/Open WebUI/open-webui-2025-07-19-v0-6-17-github-233695159-4b5cb15b|v0.6.17]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> 📡 **Chat ID Header Forwarding**: Ollama and OpenAI router requests now include the chat ID in request headers, enabling better request correlation and debugging capabilities across AI model integrations.
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.17
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-07-19-2-accessibility-and-localization-changes-in-v0-6-17|2 Accessibility and Localization changes in v0.6.17]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-07-19-enhanced-reasoning-tag-processing-improved-and-expanded-reasoning-tag-parsing-to|🧠 Enhanced Reasoning Tag Processing]] · Developer Workflow
- [[Changes/Open WebUI/2025-07-19-cleaner-database-credentials-database-connection-no-longer-duplicates-in-credent|🧹 Cleaner Database Credentials]] · Apps and Integrations
- [[Changes/Open WebUI/2025-07-19-4-editor-experience-changes-in-v0-6-17|4 Editor Experience changes in v0.6.17]] · Editor Experience
- [[Changes/Open WebUI/2025-07-19-emoji-generation-error-handling-improved-error-handling-in-audio-router-and-fixe|😀 Emoji Generation Error Handling]] · Voice and Audio
- [[Changes/Open WebUI/2025-07-19-2-reliability-and-performance-changes-in-v0-6-17|2 Reliability and Performance changes in v0.6.17]] · Reliability and Performance
- [[Changes/Open WebUI/2025-07-19-file-deletion-now-removes-related-vector-data-when-files-are-deleted-from-storag|🧑💻 File Deletion Now Removes Related Vector Data]] · Search and Browsing
- [[Changes/Open WebUI/2025-07-19-chat-preview-in-search-when-searching-chats-instantly-preview-results-in-context|🔎 Chat Preview in Search]] · Context Window
- [[Changes/Open WebUI/2025-07-19-traceability-with-log-trace-and-span-ids-each-log-entry-now-carries-detailed-tra|🏷️ Traceability with Log Trace and Span IDs]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-07-19-user-group-add-remove-endpoints-effortlessly-add-or-remove-users-from-groups-wit|👥 User Group Add/Remove Endpoints]] · Collaboration
- [[Changes/Open WebUI/2025-07-19-2-safety-and-privacy-changes-in-v0-6-17|2 Safety and Privacy changes in v0.6.17]] · Safety and Privacy
- [[Changes/Open WebUI/2025-07-19-3-files-and-data-changes-in-v0-6-17|3 Files and Data changes in v0.6.17]] · Files and Data
- [[Changes/Open WebUI/2025-07-19-oauth-token-endpoint-authentication-method-added-configurable-oauth-token-endpoi|🔐 OAuth Token Endpoint Authentication Method]] · Account and Access
- [[Changes/Open WebUI/2025-07-19-3-interface-experience-changes-in-v0-6-17|3 Interface Experience changes in v0.6.17]] · Interface Experience
- [[Changes/Open WebUI/2025-07-19-10-other-changes-in-v0-6-17|10 other changes in v0.6.17]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-07-19 · LM Studio · [[Changes/LM Studio/2025-07-19-added-tool-calling-support-for-mistral-v13-tokenizer-models-with-proper-chat-tem|Added tool calling support for Mistral v13 tokenizer models (with proper chat templates)]]
- Later: 2025-07-22 · Cline · [[Changes/Cline/2025-07-22-separate-plan-act-model-settings-by-celestial-vault-in-https-github-com-cline-cl|Separate plan act model settings]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-07-19-32ebba&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-07-19-chat-id-header-forwarding-ollama-and-openai-router-requests-now-include-the-chat.md%0ACard%20ID%3A%20open-webui-2025-07-19-32ebba%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.17%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->