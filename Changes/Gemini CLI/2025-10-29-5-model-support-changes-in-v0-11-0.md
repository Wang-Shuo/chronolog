---
card_id: gemini-cli-2025-10-29-0ab269
date: '2025-10-29'
description: 'Gemini CLI · 2025-10-29 · Model Support: 5 changes in Release v0.11.0
  — include extension name in `gemini mcp list` command by @jakemac53 in…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1024
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5df9efabaca2d5c5804d31ccd2fc2cae10fcb83b2aa844d9d4036666c08eaa25
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2025-10-29-0ab269
  comparison: ''
  date: '2025-10-29'
  description: 'Gemini CLI — Release v0.11.0: 5 Model Support changes'
  evidence:
  - quote: include extension name in `gemini mcp list` command by @jakemac53 in https://github.com/google-gemini/gemini-cli/pull/11263
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
  - quote: Update docs to specifying GEMINI_SYSTEM_MD and GEMINI_WRITE_SYSTEM_MD instructions
      by @anj-s in https://github.com/google-gemini/gemini-cli/pull/9953
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
  - quote: 'chore: do not retry the model request if the user has aborted the request
      by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/11224'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
  - quote: Per-Auth Method Feature Flag for Model Routing by @mrcabbage972 in https://github.com/google-gemini/gemini-cli/pull/11333
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
  - quote: Revert "Per-Auth Method Feature Flag for Model Routing (#11333)" by @abhipatel12
      in https://github.com/google-gemini/gemini-cli/pull/11597
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 5-model-support-changes-in-v0-11-0
  source_release: gemini-cli-2025-10-29-v0-11-0-github-258016924-cf04d23a
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in v0.11.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2025-10-27-improve-error-message-from-model-model-command-when-using-an-unsupported-model|Improve
  error message from /model model command when using an unsupported model]]'
- '[[Changes/Cursor/2025-10-29-introducing-our-first-agentic-coding-model-composer-is-a-frontier-model-that-is|Composer]]'
- '[[Changes/Cursor/2025-10-29-plan-mode-in-background|Plan Mode in Background]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2025-10-29-v0-11-0-github-258016924-cf04d23a|gemini-cli-2025-10-29-v0-11-0-github-258016924-cf04d23a]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in v0.11.0

**Gemini CLI** · 2025-10-29 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0) · from [[Releases/Gemini CLI/gemini-cli-2025-10-29-v0-11-0-github-258016924-cf04d23a|Release v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> include extension name in `gemini mcp list` command by @jakemac53 in https://github.com/google-gemini/gemini-cli/pull/11263

> Update docs to specifying GEMINI_SYSTEM_MD and GEMINI_WRITE_SYSTEM_MD instructions by @anj-s in https://github.com/google-gemini/gemini-cli/pull/9953

> chore: do not retry the model request if the user has aborted the request by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/11224

> Per-Auth Method Feature Flag for Model Routing by @mrcabbage972 in https://github.com/google-gemini/gemini-cli/pull/11333

> Revert "Per-Auth Method Feature Flag for Model Routing (#11333)" by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/11597

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2025-10-29-refactor-logging-centralize-all-console-messaging-to-a-shared-logger-part-1-by-a|refactor(logging): Centralize all console messaging to a shared logger (part 1)]] · Collaboration
- [[Changes/Gemini CLI/2025-10-29-7-apps-and-integrations-changes-in-v0-11-0|7 Apps and Integrations changes in v0.11.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2025-10-29-feat-docs-add-initial-release-confidence-document-by-galz10-in-https-github-com|feat(docs): add initial release confidence document]] · Files and Data
- [[Changes/Gemini CLI/2025-10-29-11-developer-workflow-changes-in-v0-11-0|11 Developer Workflow changes in v0.11.0]] · Developer Workflow
- [[Changes/Gemini CLI/2025-10-29-2-automation-and-scheduling-changes-in-v0-11-0|2 Automation and Scheduling changes in v0.11.0]] · Automation and Scheduling
- [[Changes/Gemini CLI/2025-10-29-improve-rendering-of-todo-lists-by-scidomino-in-https-github-com-google-gemini-g|Improve rendering of ToDo lists]] · Interface Experience
- [[Changes/Gemini CLI/2025-10-29-chore-subagents-remove-legacy-subagent-code-by-abhipatel12-in-https-github-com-g|chore(subagents): Remove legacy subagent code]] · Agent Mode
- [[Changes/Gemini CLI/2025-10-29-pass-whole-extensions-rather-than-just-context-files-by-zbirkenbuel-in-https-git|Pass whole extensions rather than just context files]] · Context Window
- [[Changes/Gemini CLI/2025-10-29-5-editor-experience-changes-in-v0-11-0|5 Editor Experience changes in v0.11.0]] · Editor Experience
- [[Changes/Gemini CLI/2025-10-29-61-other-changes-in-v0-11-0|61 other changes in v0.11.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-10-29 · Cursor · [[Changes/Cursor/2025-10-29-plan-mode-in-background|Plan Mode in Background]]
- Later: 2025-10-29 · Ollama · [[Changes/Ollama/2025-10-29-4-model-support-changes-in-v0-12-7|4 Model Support changes in v0.12.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2025-10-29-0ab269&body=Card%3A%20Changes%2FGemini%20CLI%2F2025-10-29-5-model-support-changes-in-v0-11-0.md%0ACard%20ID%3A%20gemini-cli-2025-10-29-0ab269%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->