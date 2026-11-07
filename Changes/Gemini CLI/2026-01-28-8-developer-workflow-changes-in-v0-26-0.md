---
card_id: gemini-cli-2026-01-28-0a17eb
date: '2026-01-28'
description: 'Gemini CLI · 2026-01-28 · Developer Workflow: 8 changes in Release v0.26.0
  — docs: clarify F12 to open debug console by @jackwotherspoon in…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2696
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7e8772f77611548cfcdb76846d4ca1c426b06837651068fbdd959637b1f755a4
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-01-28-0a17eb
  comparison: ''
  date: '2026-01-28'
  description: 'Gemini CLI — Release v0.26.0: 8 Developer Workflow changes'
  evidence:
  - quote: 'docs: clarify F12 to open debug console by @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/16570'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: Add timeout for shell-utils to prevent hangs. by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/16667
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: 'refactor(cli): unify shell confirmation dialogs by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/16828'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: Don't commit unless user asks us to. by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/16902
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: Stabilize the git evals by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/16989
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: Demote git evals to nightly run. by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/17030
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: 'feat: add /introspect slash command by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/17048'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: '[A2A] Disable checkpointing if git is not installed by @cocosheng-g in
      https://github.com/google-gemini/gemini-cli/pull/16896'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 8-developer-workflow-changes-in-v0-26-0
  source_release: gemini-cli-2026-01-28-v0-26-0-github-280517876-a39d31c9
  source_type: github_releases
  theme: developer-workflow
  title: 8 Developer Workflow changes in v0.26.0
  type: change
related_changes:
- '[[Changes/Raycast/2026-01-27-2-developer-workflow-changes-in-raycast-windows-0-43|2
  Developer Workflow changes in Raycast windows 0.43]]'
- '[[Changes/v0/2026-01-27-projects-connected-to-your-actual-app-with-code-environment-variables-deployment|Projects
  : connected to your actual app, with code, environment variables…]]'
- '[[Changes/Claude Code/2026-01-28-vscode-added-automatic-python-virtual-environment-activation-ensuring-python-and|VSCode
  Added automatic Python virtual environment activation, ensuring python…]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-01-28-v0-26-0-github-280517876-a39d31c9|gemini-cli-2026-01-28-v0-26-0-github-280517876-a39d31c9]]'
source_type: github_releases
theme: developer-workflow
title: 8 Developer Workflow changes in v0.26.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Developer Workflow changes in v0.26.0

**Gemini CLI** · 2026-01-28 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0) · from [[Releases/Gemini CLI/gemini-cli-2026-01-28-v0-26-0-github-280517876-a39d31c9|Release v0.26.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> docs: clarify F12 to open debug console by @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/16570

> Add timeout for shell-utils to prevent hangs. by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/16667

> refactor(cli): unify shell confirmation dialogs by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/16828

> Don't commit unless user asks us to. by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/16902

> Stabilize the git evals by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/16989

> Demote git evals to nightly run. by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/17030

> feat: add /introspect slash command by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/17048

> [A2A] Disable checkpointing if git is not installed by @cocosheng-g in https://github.com/google-gemini/gemini-cli/pull/16896

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-01-28-docs-update-project-context-and-pr-creator-workflow-by-ntaylormullen-in-https-gi|docs: update project context and pr-creator workflow]] · Projects and Workspaces
- [[Changes/Gemini CLI/2026-01-28-8-agent-mode-changes-in-v0-26-0|8 Agent Mode changes in v0.26.0]] · Agent Mode
- [[Changes/Gemini CLI/2026-01-28-12-automation-and-scheduling-changes-in-v0-26-0|12 Automation and Scheduling changes in v0.26.0]] · Automation and Scheduling
- [[Changes/Gemini CLI/2026-01-28-4-model-support-changes-in-v0-26-0|4 Model Support changes in v0.26.0]] · Model Support
- [[Changes/Gemini CLI/2026-01-28-remove-missing-sidebar-item-by-chrstnb-in-https-github-com-google-gemini-gemini|Remove missing sidebar item]] · Interface Experience
- [[Changes/Gemini CLI/2026-01-28-4-apps-and-integrations-changes-in-v0-26-0|4 Apps and Integrations changes in v0.26.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-01-28-feat-core-enhanced-anchored-iterative-context-compression-with-self-verification|feat(core): enhanced anchored iterative context compression with self-verification]] · Context Window
- [[Changes/Gemini CLI/2026-01-28-feat-admin-implement-admin-controls-polling-and-restart-prompt-by-skeshive-in-ht|feat(admin): implement admin controls polling and restart prompt]] · Enterprise and Administration
- [[Changes/Gemini CLI/2026-01-28-3-safety-and-privacy-changes-in-v0-26-0|3 Safety and Privacy changes in v0.26.0]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-01-28-48-other-changes-in-v0-26-0|48 other changes in v0.26.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-01-28 · Claude Code · [[Changes/Claude Code/2026-01-28-vscode-added-automatic-python-virtual-environment-activation-ensuring-python-and|VSCode Added automatic Python virtual environment activation, ensuring python…]]
- Later: 2026-01-28 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-01-28-skills-from-parent-directories-are-now-invocable-and-work-in-non-git-directories|Skills from parent directories are now invocable and work in non-git directories]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-01-28-0a17eb&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-01-28-8-developer-workflow-changes-in-v0-26-0.md%0ACard%20ID%3A%20gemini-cli-2026-01-28-0a17eb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.26.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->