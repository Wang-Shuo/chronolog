---
card_id: opencode-2026-10-27-0fe1fa
date: '2026-10-27'
description: 'OpenCode · 2026-10-27 · Model Support: 13 changes in v2.2.0 — Core Let
  custom model configuration set a model type.'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1387
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: df07bf3e50f3c30efa72c269098d53fd78d2ca4c704e48021c03281bfa44c8cf
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-10-27-0fe1fa
  comparison: ''
  date: '2026-10-27'
  description: 'OpenCode — v2.2.0: 13 Model Support changes'
  evidence:
  - quote: Core Let custom model configuration set a model type.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Let model-list API requests filter by type.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Replace experimental evaluations with Decision APIs in the AI pkg,
      including OpenAI Decisions, System One, and Cloudflare Run models.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Resolve model details once per prompt step.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Add GPT-6.1 Terra and GPT-6.1 Terra Fast to Sign in with ChatGPT.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Desktop Improve command, session, and model search lists with sticky sections.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Skip unavailable models.dev API entrypoints instead of failing model
      catalog updates.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Avoid warming a session while its model request is running.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Keep the models catalog fresh without redownloading it when unchanged.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Preserve streamed text and reasoning that arrive after an OpenAI Chat
      finish reason.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Avoid unnecessary Azure model updates when endpoint transforms make
      no change.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Desktop Return focus to the prompt after keyboard model selection.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Desktop Keep the composer model's provider and session-model resolution
      consistent with the TUI.
    source_release: https://opencode.ai/changelog/v2.2.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: opencode
  product_name: OpenCode
  slug: 13-model-support-changes-in-v2-2-0
  source_release: opencode-2026-10-27-v2-2-0-f60b51f1
  source_type: opencode_changelog
  theme: model-support
  title: 13 Model Support changes in v2.2.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-27-managed-model-fusion-now-starts-sessions-on-auto-and-applies-fusiontier-settings|Managed
  model "fusion" now starts sessions on Auto and applies fusionTier settings]]'
- '[[Changes/Ollama/2026-10-27-speculative-decoding-now-supports-dflash2-draft-models-on-mlx|Speculative
  decoding now supports DFlash2 draft models on MLX]]'
- '[[Changes/OpenClaw/2026-10-27-6-model-support-changes-in-v2026-10-8|6 Model Support
  changes in v2026.10.8]]'
source_release: '[[Releases/OpenCode/opencode-2026-10-27-v2-2-0-f60b51f1|opencode-2026-10-27-v2-2-0-f60b51f1]]'
source_type: opencode_changelog
theme: model-support
title: 13 Model Support changes in v2.2.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Model Support changes in v2.2.0

**OpenCode** · 2026-10-27 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://opencode.ai/changelog/v2.2.0) · from [[Releases/OpenCode/opencode-2026-10-27-v2-2-0-f60b51f1|v2.2.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Core Let custom model configuration set a model type.

> Core Let model-list API requests filter by type.

> Core Replace experimental evaluations with Decision APIs in the AI pkg, including OpenAI Decisions, System One, and Cloudflare Run models.

> Core Resolve model details once per prompt step.

> Core Add GPT-6.1 Terra and GPT-6.1 Terra Fast to Sign in with ChatGPT.

> Desktop Improve command, session, and model search lists with sticky sections.

> Core Skip unavailable models.dev API entrypoints instead of failing model catalog updates.

> Core Avoid warming a session while its model request is running.

> Core Keep the models catalog fresh without redownloading it when unchanged.

> Core Preserve streamed text and reasoning that arrive after an OpenAI Chat finish reason.

> Core Avoid unnecessary Azure model updates when endpoint transforms make no change.

> Desktop Return focus to the prompt after keyboard model selection.

> Desktop Keep the composer model's provider and session-model resolution consistent with the TUI.

Source: https://opencode.ai/changelog/v2.2.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-10-27-73-mobile-and-desktop-changes-in-v2-2-0|73 Mobile and Desktop changes in v2.2.0]] · Mobile and Desktop
- [[Changes/OpenCode/2026-10-27-core-preserve-literal-0-and-arguments-text-in-custom-command-input|Core Preserve literal $0 and $ARGUMENTS text in custom command input]] · Pricing Model
- [[Changes/OpenCode/2026-10-27-add-experimental-image-and-decision-generation-apis-to-plugins-and-sdk|Add experimental image and decision generation APIs to plugins and sdk]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-2-search-and-browsing-changes-in-v2-2-0|2 Search and Browsing changes in v2.2.0]] · Search and Browsing
- [[Changes/OpenCode/2026-10-27-create-install-and-share-desktop-plugins-experimental|Create, install and share Desktop plugins (experimental)]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-10-interface-experience-changes-in-v2-2-0|10 Interface Experience changes in v2.2.0]] · Interface Experience
- [[Changes/OpenCode/2026-10-27-3-context-window-changes-in-v2-2-0|3 Context Window changes in v2.2.0]] · Context Window
- [[Changes/OpenCode/2026-10-27-restored-the-todo-tool-in-desktop-via-opt-in|Restored the Todo tool in desktop via opt-in]] · Mobile and Desktop
- [[Changes/OpenCode/2026-10-27-tui-plugins-require-opentui-0-7|TUI plugins require OpenTUI 0.7]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-8-memory-and-personalization-changes-in-v2-2-0|8 Memory and Personalization changes in v2.2.0]] · Memory and Personalization
- [[Changes/OpenCode/2026-10-27-14-apps-and-integrations-changes-in-v2-2-0|14 Apps and Integrations changes in v2.2.0]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-core-honor-shared-parallel-tool-call-and-service-tier-settings-for-groq|Core Honor shared parallel tool-call and service-tier settings for Groq]] · Collaboration
- [[Changes/OpenCode/2026-10-27-2-voice-and-audio-changes-in-v2-2-0|2 Voice and Audio changes in v2.2.0]] · Voice and Audio
- [[Changes/OpenCode/2026-10-27-refreshed-the-desktop-app-experience|Refreshed the desktop app experience]] · Mobile and Desktop
- [[Changes/OpenCode/2026-10-27-2-safety-and-privacy-changes-in-v2-2-0|2 Safety and Privacy changes in v2.2.0]] · Safety and Privacy
- [[Changes/OpenCode/2026-10-27-core-coordinate-oauth-credential-refreshes-across-locations-and-processes|Core Coordinate OAuth credential refreshes across locations and processes]] · Account and Access
- [[Changes/OpenCode/2026-10-27-5-editor-experience-changes-in-v2-2-0|5 Editor Experience changes in v2.2.0]] · Editor Experience
- [[Changes/OpenCode/2026-10-27-plugins-can-now-attach-and-update-keyed-session-instructions-with-ctx-session-in|Plugins can now attach and update keyed session instructions…]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-add-configurable-prompt-cache-ttls-per-provider-model|Add configurable prompt cache TTLs per provider/model]] · Model Support
- [[Changes/OpenCode/2026-10-27-2-agent-mode-changes-in-v2-2-0|2 Agent Mode changes in v2.2.0]] · Agent Mode
- [[Changes/OpenCode/2026-10-27-3-projects-and-workspaces-changes-in-v2-2-0|3 Projects and Workspaces changes in v2.2.0]] · Projects and Workspaces
- [[Changes/OpenCode/2026-10-27-opencode-ai-root-is-now-the-promise-api|opencode/ai root is now the Promise API]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-13-developer-workflow-changes-in-v2-2-0|13 Developer Workflow changes in v2.2.0]] · Developer Workflow
- [[Changes/OpenCode/2026-10-27-6-reliability-and-performance-changes-in-v2-2-0|6 Reliability and Performance changes in v2.2.0]] · Reliability and Performance
- [[Changes/OpenCode/2026-10-27-31-other-changes-in-v2-2-0|31 other changes in v2.2.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-27 · OpenClaw · [[Changes/OpenClaw/2026-10-27-6-model-support-changes-in-v2026-10-8|6 Model Support changes in v2026.10.8]]
- Later: 2026-10-27 · OpenHands · [[Changes/OpenHands/2026-10-27-refactor-settings-use-existing-model-profile-theme-aliases-by-enyst-in-https-git|refactor(settings): use existing model-profile theme aliases]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-10-27-0fe1fa&body=Card%3A%20Changes%2FOpenCode%2F2026-10-27-13-model-support-changes-in-v2-2-0.md%0ACard%20ID%3A%20opencode-2026-10-27-0fe1fa%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv2.2.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->