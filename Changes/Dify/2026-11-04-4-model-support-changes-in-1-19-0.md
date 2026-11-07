---
card_id: dify-2026-11-04-2c2597
date: '2026-11-04'
description: 'Dify · 2026-11-04 · Model Support: 4 changes in v1.19.0 - Trace Your
  Workflows, Layer by Layer — ![Langfuse trace tree showing a workflow, nested Middle
  and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1395
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dd5a6e7fa31de191bff74d76bcda0c494d65479171f0f29978be01b00dcbf96c
product: dify
product_name: Dify
record:
  card_id: dify-2026-11-04-2c2597
  comparison: ''
  date: '2026-11-04'
  description: 'Dify — v1.19.0 - Trace Your Workflows, Layer by Layer: 4 Model Support
    changes'
  evidence:
  - quote: '![Langfuse trace tree showing a workflow, nested Middle and Child Workflow
      Tools, and the selected LLM call with formatted prompts and responses](https://raw.githubusercontent.com/langgenius/dify/dcfb52e62726c91b43db20f3c087acf285428df1/docs/assets/pr-44673-langfuse-nested-prompts.jpg)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '*From the outer workflow to a nested LLM call: the execution tree and
      formatted messages, together in Langfuse. Screenshot from [#44673](https://github.com/langgenius/dify/pull/44673).*'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: Restore structured-output fallback for models without native support and
      preserve JSON booleans instead of converting them to strings. (#44962)
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'Allow current Qwen flash models in Agent v2 and refresh suggested model
      patterns. Omit empty optional Agent variable inputs, and accept legacy comma-separated
      values for multiple-select tool parameters. (#44873, #44748, #45058)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 4-model-support-changes-in-1-19-0
  source_release: dify-2026-11-04-1-19-0-github-433629888-738006ec
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in 1.19.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-11-03-2-model-support-changes-in-v0-40-14|2 Model Support
  changes in v0.40.14]]'
- '[[Changes/Open WebUI/2026-11-03-4-model-support-changes-in-v0-13-0|4 Model Support
  changes in v0.13.0]]'
- '[[Changes/OpenClaw/2026-11-03-17-model-support-changes-in-v2026-10-10|17 Model
  Support changes in v2026.10.10]]'
source_release: '[[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|dify-2026-11-04-1-19-0-github-433629888-738006ec]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in 1.19.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in 1.19.0

**Dify** · 2026-11-04 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.19.0) · from [[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|v1.19.0 - Trace Your Workflows, Layer by Layer]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ![Langfuse trace tree showing a workflow, nested Middle and Child Workflow Tools, and the selected LLM call with formatted prompts and responses](https://raw.githubusercontent.com/langgenius/dify/dcfb52e62726c91b43db20f3c087acf285428df1/docs/assets/pr-44673-langfuse-nested-prompts.jpg)

> *From the outer workflow to a nested LLM call: the execution tree and formatted messages, together in Langfuse. Screenshot from [#44673](https://github.com/langgenius/dify/pull/44673).*

> Restore structured-output fallback for models without native support and preserve JSON booleans instead of converting them to strings. (#44962)

> Allow current Qwen flash models in Agent v2 and refresh suggested model patterns. Omit empty optional Agent variable inputs, and accept legacy comma-separated values for multiple-select tool parameters. (#44873, #44748, #45058)

Source: https://github.com/langgenius/dify/releases/tag/1.19.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-11-04-stop-serializing-the-entire-prompt-history-into-every-agent-llm-gateway-response|Stop serializing the entire prompt history into every Agent LLM gateway response chunk]] · Multimodal Input
- [[Changes/Dify/2026-11-04-4-collaboration-changes-in-1-19-0|4 Collaboration changes in 1.19.0]] · Collaboration
- [[Changes/Dify/2026-11-04-15-apps-and-integrations-changes-in-1-19-0|15 Apps and Integrations changes in 1.19.0]] · Apps and Integrations
- [[Changes/Dify/2026-11-04-3-automation-and-scheduling-changes-in-1-19-0|3 Automation and Scheduling changes in 1.19.0]] · Automation and Scheduling
- [[Changes/Dify/2026-11-04-2-developer-workflow-changes-in-1-19-0|2 Developer Workflow changes in 1.19.0]] · Developer Workflow
- [[Changes/Dify/2026-11-04-6-files-and-data-changes-in-1-19-0|6 Files and Data changes in 1.19.0]] · Files and Data
- [[Changes/Dify/2026-11-04-3-pricing-model-changes-in-1-19-0|3 Pricing Model changes in 1.19.0]] · Pricing Model
- [[Changes/Dify/2026-11-04-3-editor-experience-changes-in-1-19-0|3 Editor Experience changes in 1.19.0]] · Editor Experience
- [[Changes/Dify/2026-11-04-2-voice-and-audio-changes-in-1-19-0|2 Voice and Audio changes in 1.19.0]] · Voice and Audio
- [[Changes/Dify/2026-11-04-4-safety-and-privacy-changes-in-1-19-0|4 Safety and Privacy changes in 1.19.0]] · Safety and Privacy
- [[Changes/Dify/2026-11-04-workspace-controls-enabling-or-disabling-provider-models-requires-an-owner-or-ad|Workspace controls: enabling or disabling provider models requires an owner…]] · Enterprise and Administration
- [[Changes/Dify/2026-11-04-summary-strong-improvements-editing-accessibility-performance-and-operations-str|summarystrongImprovements · editing, accessibility, performance…]] · Accessibility and Localization
- [[Changes/Dify/2026-11-04-2-interface-experience-changes-in-1-19-0|2 Interface Experience changes in 1.19.0]] · Interface Experience
- [[Changes/Dify/2026-11-04-6-context-window-changes-in-1-19-0|6 Context Window changes in 1.19.0]] · Context Window
- [[Changes/Dify/2026-11-04-14-agent-mode-changes-in-1-19-0|14 Agent Mode changes in 1.19.0]] · Agent Mode
- [[Changes/Dify/2026-11-04-2-account-and-access-changes-in-1-19-0|2 Account and Access changes in 1.19.0]] · Account and Access
- [[Changes/Dify/2026-11-04-66-other-changes-in-1-19-0|66 other changes in 1.19.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-11-03 · OpenClaw · [[Changes/OpenClaw/2026-11-03-17-model-support-changes-in-v2026-10-10|17 Model Support changes in v2026.10.10]]
- Later: 2026-11-04 · Gemini CLI · [[Changes/Gemini CLI/2026-11-04-feat-cli-add-models-command-and-list-models-flag-for-model-discovery-by-urielefr|feat(cli): add models command and --list-models flag for model discovery]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-11-04-2c2597&body=Card%3A%20Changes%2FDify%2F2026-11-04-4-model-support-changes-in-1-19-0.md%0ACard%20ID%3A%20dify-2026-11-04-2c2597%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.19.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->