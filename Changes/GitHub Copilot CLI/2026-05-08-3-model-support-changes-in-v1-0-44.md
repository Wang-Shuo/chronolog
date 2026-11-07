---
card_id: github-copilot-cli-2026-05-08-1d7a0c
date: '2026-05-08'
description: 'GitHub Copilot CLI · 2026-05-08 · Model Support: 3 changes in 1.0.44
  — userPromptSubmitted hooks can now handle requests directly, bypassing the LLM
  and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1215
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bbd22cd48fa3a96d7f86c22a329e3976ce9d587763e9c828afe7ca70b90e986a
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-05-08-1d7a0c
  comparison: ''
  date: '2026-05-08'
  description: 'GitHub Copilot CLI — 1.0.44: 3 Model Support changes'
  evidence:
  - quote: userPromptSubmitted hooks can now handle requests directly, bypassing the
      LLM and returning a response without making a model call
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.44
  - quote: Effort level applies correctly when switching models via the /model picker
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.44
  - quote: Timeline shows the resolved model for rubber-duck sub-agents (e.g. Rubber-duck(claude-opus-4.7))
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.44
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 3-model-support-changes-in-v1-0-44
  source_release: github-copilot-cli-2026-05-08-v1-0-44-github-319701730-20ae02a8
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v1.0.44
  type: change
related_changes:
- '[[Changes/Cursor/2026-05-07-added-support-for-general-model-names-for-subagent-configuration-i-e-set-model-o|Added
  support for general model names for subagent configuration (i.e., set model]]'
- '[[Changes/OpenCode/2026-05-07-extensions-acp-clients-now-restore-the-last-model-mode-and-effort-when-loading-s|Extensions
  ACP clients now restore the last model, mode, and effort when loading…]]'
- '[[Changes/OpenCode/2026-05-07-3-model-support-changes-in-v1-14-40|3 Model Support
  changes in v1.14.40]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-08-v1-0-44-github-319701730-20ae02a8|github-copilot-cli-2026-05-08-v1-0-44-github-319701730-20ae02a8]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v1.0.44
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v1.0.44

**GitHub Copilot CLI** · 2026-05-08 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.44) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-08-v1-0-44-github-319701730-20ae02a8|1.0.44]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> userPromptSubmitted hooks can now handle requests directly, bypassing the LLM and returning a response without making a model call

> Effort level applies correctly when switching models via the /model picker

> Timeline shows the resolved model for rubber-duck sub-agents (e.g. Rubber-duck(claude-opus-4.7))

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.44
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-05-08-2-developer-workflow-changes-in-v1-0-44|2 Developer Workflow changes in v1.0.44]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-05-08-project-info-remains-visible-in-slash-command-picker-when-no-results-match|Project info remains visible in slash command picker when no results match]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-05-08-faster-user-list-and-user-switch-for-multi-account-users|Faster /user list and /user switch for multi-account users]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-05-08-2-editor-experience-changes-in-v1-0-44|2 Editor Experience changes in v1.0.44]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-05-08-pressing-ctrl-c-while-a-permission-prompt-is-pending-no-longer-causes-the-cli-to|Pressing Ctrl+C while a permission prompt is pending no longer causes the CLI to hang]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-05-08-4-other-changes-in-v1-0-44|4 other changes in v1.0.44]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-05-07 · OpenCode · [[Changes/OpenCode/2026-05-07-3-model-support-changes-in-v1-14-40|3 Model Support changes in v1.14.40]]
- Later: 2026-05-09 · Open WebUI · [[Changes/Open WebUI/2026-05-09-9-model-support-changes-in-v0-9-3|9 Model Support changes in v0.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-05-08-1d7a0c&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-05-08-3-model-support-changes-in-v1-0-44.md%0ACard%20ID%3A%20github-copilot-cli-2026-05-08-1d7a0c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.44%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->