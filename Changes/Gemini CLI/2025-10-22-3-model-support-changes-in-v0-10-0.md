---
card_id: gemini-cli-2025-10-22-3d7384
date: '2025-10-22'
description: 'Gemini CLI · 2025-10-22 · Model Support: 3 changes in Release v0.10.0
  — chore: Extract ''.gemini'' to GEMINI_DIR constant by @terrydkim in…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1017
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d5365df8c248f559720ea53c52d974d1f7fc4ceed522301872f91d9be53946c5
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2025-10-22-3d7384
  comparison: ''
  date: '2025-10-22'
  description: 'Gemini CLI — Release v0.10.0: 3 Model Support changes'
  evidence:
  - quote: 'chore: Extract ''.gemini'' to GEMINI_DIR constant by @terrydkim in https://github.com/google-gemini/gemini-cli/pull/10540'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.10.0
  - quote: 'Revert "fix: handle request retries and model fallback correctly" by @gsquared94
      in https://github.com/google-gemini/gemini-cli/pull/11164'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.10.0
  - quote: Enable Model Routing by @mrcabbage972 in https://github.com/google-gemini/gemini-cli/pull/11154
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 3-model-support-changes-in-v0-10-0
  source_release: gemini-cli-2025-10-22-v0-10-0-github-256434073-b3dd91c0
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v0.10.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2025-10-16-2-model-support-changes-in-v0-0-343|2 Model
  Support changes in v0.0.343]]'
- '[[Changes/GitHub Copilot CLI/2025-10-18-added-list-of-supported-models-as-part-of-copilot-help-config-text|Added
  list of supported models as part of copilot help config text]]'
- '[[Changes/ChatGPT/2025-10-22-we-re-updating-the-model-for-signed-out-users-to-gpt-5-instant-giving-more-peopl|We’re
  updating the model for signed-out users to GPT-5 Instant, giving more people…]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2025-10-22-v0-10-0-github-256434073-b3dd91c0|gemini-cli-2025-10-22-v0-10-0-github-256434073-b3dd91c0]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v0.10.0

**Gemini CLI** · 2025-10-22 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.10.0) · from [[Releases/Gemini CLI/gemini-cli-2025-10-22-v0-10-0-github-256434073-b3dd91c0|Release v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> chore: Extract '.gemini' to GEMINI_DIR constant by @terrydkim in https://github.com/google-gemini/gemini-cli/pull/10540

> Revert "fix: handle request retries and model fallback correctly" by @gsquared94 in https://github.com/google-gemini/gemini-cli/pull/11164

> Enable Model Routing by @mrcabbage972 in https://github.com/google-gemini/gemini-cli/pull/11154

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.10.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2025-10-22-refactor-core-migrate-web-search-tool-to-tool-names-by-abhipatel12-in-https-gith|refactor(core): migrate web search tool to tool-names]] · Search and Browsing
- [[Changes/Gemini CLI/2025-10-22-document-all-settings-with-showindialog-true-by-scidomino-in-https-github-com-go|document all settings with showInDialog: true]] · Files and Data
- [[Changes/Gemini CLI/2025-10-22-feat-core-add-telemetry-for-subagent-execution-by-abhipatel12-in-https-github-co|feat(core): add telemetry for subagent execution]] · Agent Mode
- [[Changes/Gemini CLI/2025-10-22-6-developer-workflow-changes-in-v0-10-0|6 Developer Workflow changes in v0.10.0]] · Developer Workflow
- [[Changes/Gemini CLI/2025-10-22-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2025-10-22-2-safety-and-privacy-changes-in-v0-10-0|2 Safety and Privacy changes in v0.10.0]] · Safety and Privacy
- [[Changes/Gemini CLI/2025-10-22-2-context-window-changes-in-v0-10-0|2 Context Window changes in v0.10.0]] · Context Window
- [[Changes/Gemini CLI/2025-10-22-part-4-6-feat-telemetry-add-memory-monitor-with-activity-aware-recording-and-tes|Part 4/6 feat(telemetry): add memory monitor with activity-aware recording and tests]] · Memory and Personalization
- [[Changes/Gemini CLI/2025-10-22-2-interface-experience-changes-in-v0-10-0|2 Interface Experience changes in v0.10.0]] · Interface Experience
- [[Changes/Gemini CLI/2025-10-22-4-editor-experience-changes-in-v0-10-0|4 Editor Experience changes in v0.10.0]] · Editor Experience
- [[Changes/Gemini CLI/2025-10-22-show-notification-in-screen-reader-mode-by-chrstnb-in-https-github-com-google-ge|Show notification in screen reader mode]] · Accessibility and Localization
- [[Changes/Gemini CLI/2025-10-22-51-other-changes-in-v0-10-0|51 other changes in v0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-10-22 · ChatGPT · [[Changes/ChatGPT/2025-10-22-we-re-updating-the-model-for-signed-out-users-to-gpt-5-instant-giving-more-peopl|We’re updating the model for signed-out users to GPT-5 Instant, giving more people…]]
- Later: 2025-10-22 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-10-22-2-model-support-changes-in-v0-0-349|2 Model Support changes in v0.0.349]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2025-10-22-3d7384&body=Card%3A%20Changes%2FGemini%20CLI%2F2025-10-22-3-model-support-changes-in-v0-10-0.md%0ACard%20ID%3A%20gemini-cli-2025-10-22-3d7384%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->