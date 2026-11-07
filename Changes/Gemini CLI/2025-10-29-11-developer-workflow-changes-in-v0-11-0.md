---
card_id: gemini-cli-2025-10-29-702eda
date: '2025-10-29'
description: 'Gemini CLI · 2025-10-29 · Developer Workflow: 11 changes in Release
  v0.11.0 — feat(cli): Prevent queuing of slash and shell commands by @MJjainam in…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 956
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 42eaa19de11708b449407303f3aa6248a5e1bd2ee5ac1319c694a409680d20a6
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2025-10-29-702eda
  comparison: ''
  date: '2025-10-29'
  description: 'Gemini CLI — Release v0.11.0: 11 Developer Workflow changes'
  evidence:
  - quote: 'feat(cli): Prevent queuing of slash and shell commands by @MJjainam in
      https://github.com/google-gemini/gemini-cli/pull/11094'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
  - quote: Update shell tool call colors for confirmed actions by @miguelsolorio in
      https://github.com/google-gemini/gemini-cli/pull/11126
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
  - quote: Update package.json in include git dependency on Ink fork. by @jacob314
      in https://github.com/google-gemini/gemini-cli/pull/11330
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
  - quote: Revert "Update package.json in include git dependency on Ink fork." by
      @jakemac53 in https://github.com/google-gemini/gemini-cli/pull/11365
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
  - quote: 'feat(cli): Suppress slash command execution and suggestions in shell …
      by @MJjainam in https://github.com/google-gemini/gemini-cli/pull/11380'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
  - quote: Style slash command descriptions consistently by @scidomino in https://github.com/google-gemini/gemini-cli/pull/11395
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
  - quote: 'feat(logging): Centralize debug logging with a dedicated utility by @abhipatel12
      in https://github.com/google-gemini/gemini-cli/pull/11417'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
  - quote: 'refactor(tools): Migrate shell tool name to a centralized constant by
      @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/11418'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
  - quote: Making shell:true as default and adding -I to grep by @gsehgal in https://github.com/google-gemini/gemini-cli/pull/11448
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
  - quote: 'docs: require bug bash for major launches and clarify roles by @galz10
      in https://github.com/google-gemini/gemini-cli/pull/11384'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
  - quote: Remove errant console.debug log of config by @chrstnb in https://github.com/google-gemini/gemini-cli/pull/11579
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 11-developer-workflow-changes-in-v0-11-0
  source_release: gemini-cli-2025-10-29-v0-11-0-github-258016924-cf04d23a
  source_type: github_releases
  theme: developer-workflow
  title: 11 Developer Workflow changes in v0.11.0
  type: change
related_changes:
- '[[Changes/Cline/2025-10-27-add-linter-check-for-proto-files-and-add-auto-formatting-by-sjf-in-https-github|Add
  linter check for proto files and add auto-formatting]]'
- '[[Changes/Cursor/2025-10-29-improved-code-review|Improved Code Review]]'
- '[[Changes/Cursor/2025-10-29-3-developer-workflow-changes-in-2-0|3 Developer Workflow
  changes in 2.0]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2025-10-29-v0-11-0-github-258016924-cf04d23a|gemini-cli-2025-10-29-v0-11-0-github-258016924-cf04d23a]]'
source_type: github_releases
theme: developer-workflow
title: 11 Developer Workflow changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Developer Workflow changes in v0.11.0

**Gemini CLI** · 2025-10-29 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0) · from [[Releases/Gemini CLI/gemini-cli-2025-10-29-v0-11-0-github-258016924-cf04d23a|Release v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> feat(cli): Prevent queuing of slash and shell commands by @MJjainam in https://github.com/google-gemini/gemini-cli/pull/11094

> Update shell tool call colors for confirmed actions by @miguelsolorio in https://github.com/google-gemini/gemini-cli/pull/11126

> Update package.json in include git dependency on Ink fork. by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/11330

> Revert "Update package.json in include git dependency on Ink fork." by @jakemac53 in https://github.com/google-gemini/gemini-cli/pull/11365

> feat(cli): Suppress slash command execution and suggestions in shell … by @MJjainam in https://github.com/google-gemini/gemini-cli/pull/11380

> Style slash command descriptions consistently by @scidomino in https://github.com/google-gemini/gemini-cli/pull/11395

> feat(logging): Centralize debug logging with a dedicated utility by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/11417

> refactor(tools): Migrate shell tool name to a centralized constant by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/11418

> Making shell:true as default and adding -I to grep by @gsehgal in https://github.com/google-gemini/gemini-cli/pull/11448

> docs: require bug bash for major launches and clarify roles by @galz10 in https://github.com/google-gemini/gemini-cli/pull/11384

> Remove errant console.debug log of config by @chrstnb in https://github.com/google-gemini/gemini-cli/pull/11579

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2025-10-29-5-model-support-changes-in-v0-11-0|5 Model Support changes in v0.11.0]] · Model Support
- [[Changes/Gemini CLI/2025-10-29-refactor-logging-centralize-all-console-messaging-to-a-shared-logger-part-1-by-a|refactor(logging): Centralize all console messaging to a shared logger (part 1)]] · Collaboration
- [[Changes/Gemini CLI/2025-10-29-7-apps-and-integrations-changes-in-v0-11-0|7 Apps and Integrations changes in v0.11.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2025-10-29-feat-docs-add-initial-release-confidence-document-by-galz10-in-https-github-com|feat(docs): add initial release confidence document]] · Files and Data
- [[Changes/Gemini CLI/2025-10-29-2-automation-and-scheduling-changes-in-v0-11-0|2 Automation and Scheduling changes in v0.11.0]] · Automation and Scheduling
- [[Changes/Gemini CLI/2025-10-29-improve-rendering-of-todo-lists-by-scidomino-in-https-github-com-google-gemini-g|Improve rendering of ToDo lists]] · Interface Experience
- [[Changes/Gemini CLI/2025-10-29-chore-subagents-remove-legacy-subagent-code-by-abhipatel12-in-https-github-com-g|chore(subagents): Remove legacy subagent code]] · Agent Mode
- [[Changes/Gemini CLI/2025-10-29-pass-whole-extensions-rather-than-just-context-files-by-zbirkenbuel-in-https-git|Pass whole extensions rather than just context files]] · Context Window
- [[Changes/Gemini CLI/2025-10-29-5-editor-experience-changes-in-v0-11-0|5 Editor Experience changes in v0.11.0]] · Editor Experience
- [[Changes/Gemini CLI/2025-10-29-61-other-changes-in-v0-11-0|61 other changes in v0.11.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2025-10-29 · Cursor · [[Changes/Cursor/2025-10-29-3-developer-workflow-changes-in-2-0|3 Developer Workflow changes in 2.0]]
- Later: 2025-10-30 · Codex CLI · [[Changes/Codex CLI/2025-10-30-5-developer-workflow-changes-in-rust-v0-52-0|5 Developer Workflow changes in rust-v0.52.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2025-10-29-702eda&body=Card%3A%20Changes%2FGemini%20CLI%2F2025-10-29-11-developer-workflow-changes-in-v0-11-0.md%0ACard%20ID%3A%20gemini-cli-2025-10-29-702eda%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->