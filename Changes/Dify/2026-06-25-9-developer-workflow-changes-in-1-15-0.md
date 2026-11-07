---
card_id: dify-2026-06-25-8d97a3
date: '2026-06-25'
description: 'Dify · 2026-06-25 · Developer Workflow: 9 changes in 1.15.0 — **difyctl
  — drive Dify from the command line** ([Docs](https://docs.dify.ai/en/cli/overview))'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1195
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a0949aa6a9be14c0967137f5acd1329de0a3024d9b460dc536b3d32e06f85634
product: dify
product_name: Dify
record:
  card_id: dify-2026-06-25-8d97a3
  comparison: ''
  date: '2026-06-25'
  description: 'Dify — 1.15.0: 9 Developer Workflow changes'
  evidence:
  - quote: '**difyctl — drive Dify from the command line** ([Docs](https://docs.dify.ai/en/cli/overview))'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'difyctl is a command-line client for Dify: you can now run apps and workflows
      straight from your terminal, so personal agents, scripts, and CI pipelines can
      invoke Dify workflows without opening the web UI (#37036)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: '> Back up the database before applying the migration. The command runs
      in dry-run mode by default; review the output before rerunning it with `--apply`.
      The migration is idempotent and can be safely rerun.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'chore: move API readiness reporting to terminal output by @hyoban in https://github.com/langgenius/dify/pull/36433'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'refactor(web): migrate debug-and-preview-panel-width to useSetLocalStorage
      by @shifang0511 in https://github.com/langgenius/dify/pull/36977'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'feat: update frontend code review skill by @lyzno1 in https://github.com/langgenius/dify/pull/37098'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'ci: add flag for linter by @asukaminato0721 in https://github.com/langgenius/dify/pull/37018'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'feat(cli): difyctl per-commit edge distribution via Cloudflare R2 by @GareArc
      in https://github.com/langgenius/dify/pull/37454'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'feat(cli): recover omitted and length-aware command suggestions by @lin-snow
      in https://github.com/langgenius/dify/pull/37624'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 9-developer-workflow-changes-in-1-15-0
  source_release: dify-2026-06-25-1-15-0-github-344699591-4dd01045
  source_type: github_releases
  theme: developer-workflow
  title: 9 Developer Workflow changes in 1.15.0
  type: change
related_changes:
- '[[Changes/Windsurf/2026-06-23-cli-and-devin-local|CLI and Devin Local]]'
- '[[Changes/GitHub Copilot CLI/2026-06-24-remove-syntax-highlighting-from-shell-commands-in-the-timeline|Remove
  syntax highlighting from shell commands in the timeline]]'
- '[[Changes/OpenCode/2026-06-24-3-developer-workflow-changes-in-v1-17-10|3 Developer
  Workflow changes in v1.17.10]]'
source_release: '[[Releases/Dify/dify-2026-06-25-1-15-0-github-344699591-4dd01045|dify-2026-06-25-1-15-0-github-344699591-4dd01045]]'
source_type: github_releases
theme: developer-workflow
title: 9 Developer Workflow changes in 1.15.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Developer Workflow changes in 1.15.0

**Dify** · 2026-06-25 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.15.0) · from [[Releases/Dify/dify-2026-06-25-1-15-0-github-344699591-4dd01045|1.15.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **difyctl — drive Dify from the command line** ([Docs](https://docs.dify.ai/en/cli/overview))

> difyctl is a command-line client for Dify: you can now run apps and workflows straight from your terminal, so personal agents, scripts, and CI pipelines can invoke Dify workflows without opening the web UI (#37036)

> > Back up the database before applying the migration. The command runs in dry-run mode by default; review the output before rerunning it with `--apply`. The migration is idempotent and can be safely rerun.

> chore: move API readiness reporting to terminal output by @hyoban in https://github.com/langgenius/dify/pull/36433

> refactor(web): migrate debug-and-preview-panel-width to useSetLocalStorage by @shifang0511 in https://github.com/langgenius/dify/pull/36977

> feat: update frontend code review skill by @lyzno1 in https://github.com/langgenius/dify/pull/37098

> ci: add flag for linter by @asukaminato0721 in https://github.com/langgenius/dify/pull/37018

> feat(cli): difyctl per-commit edge distribution via Cloudflare R2 by @GareArc in https://github.com/langgenius/dify/pull/37454

> feat(cli): recover omitted and length-aware command suggestions by @lin-snow in https://github.com/langgenius/dify/pull/37624

Source: https://github.com/langgenius/dify/releases/tag/1.15.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-06-25-6-interface-experience-changes-in-1-15-0|6 Interface Experience changes in 1.15.0]] · Interface Experience
- [[Changes/Dify/2026-06-25-38-agent-mode-changes-in-1-15-0|38 Agent Mode changes in 1.15.0]] · Agent Mode
- [[Changes/Dify/2026-06-25-14-safety-and-privacy-changes-in-1-15-0|14 Safety and Privacy changes in 1.15.0]] · Safety and Privacy
- [[Changes/Dify/2026-06-25-refactor-inject-session-into-audio-tts-by-myshkin451-in-https-github-com-langgen|refactor: inject session into audio TTS]] · Voice and Audio
- [[Changes/Dify/2026-06-25-2-reliability-and-performance-changes-in-1-15-0|2 Reliability and Performance changes in 1.15.0]] · Reliability and Performance
- [[Changes/Dify/2026-06-25-3-context-window-changes-in-1-15-0|3 Context Window changes in 1.15.0]] · Context Window
- [[Changes/Dify/2026-06-25-install-it-on-any-platform-macos-linux-windows-with-a-single-command-and-no-acce|Install it on any platform (macOS, Linux, Windows) with a single command and no…]] · Mobile and Desktop
- [[Changes/Dify/2026-06-25-numerous-web-ui-and-accessibility-focus-ring-polish-fixes|Numerous web UI and accessibility/focus-ring polish fixes]] · Accessibility and Localization
- [[Changes/Dify/2026-06-25-6-pricing-model-changes-in-1-15-0|6 Pricing Model changes in 1.15.0]] · Pricing Model
- [[Changes/Dify/2026-06-25-6-files-and-data-changes-in-1-15-0|6 Files and Data changes in 1.15.0]] · Files and Data
- [[Changes/Dify/2026-06-25-17-model-support-changes-in-1-15-0|17 Model Support changes in 1.15.0]] · Model Support
- [[Changes/Dify/2026-06-25-5-account-and-access-changes-in-1-15-0|5 Account and Access changes in 1.15.0]] · Account and Access
- [[Changes/Dify/2026-06-25-6-collaboration-changes-in-1-15-0|6 Collaboration changes in 1.15.0]] · Collaboration
- [[Changes/Dify/2026-06-25-27-apps-and-integrations-changes-in-1-15-0|27 Apps and Integrations changes in 1.15.0]] · Apps and Integrations
- [[Changes/Dify/2026-06-25-2-automation-and-scheduling-changes-in-1-15-0|2 Automation and Scheduling changes in 1.15.0]] · Automation and Scheduling
- [[Changes/Dify/2026-06-25-3-editor-experience-changes-in-1-15-0|3 Editor Experience changes in 1.15.0]] · Editor Experience
- [[Changes/Dify/2026-06-25-365-other-changes-in-1-15-0|365 other changes in 1.15.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-06-24 · OpenCode · [[Changes/OpenCode/2026-06-24-3-developer-workflow-changes-in-v1-17-10|3 Developer Workflow changes in v1.17.10]]
- Later: 2026-06-25 · Gemini CLI · [[Changes/Gemini CLI/2026-06-25-feat-add-eval-inventory-cli-command-and-reporting-logic-by-ved015-in-https-githu|feat: add eval:inventory CLI command and reporting logic]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-06-25-8d97a3&body=Card%3A%20Changes%2FDify%2F2026-06-25-9-developer-workflow-changes-in-1-15-0.md%0ACard%20ID%3A%20dify-2026-06-25-8d97a3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.15.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->