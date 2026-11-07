---
card_id: cline-2026-08-05-59f9fd
date: '2026-08-05'
description: 'Cline · 2026-08-05 · Developer Workflow: 2 changes in v4.1.4 — Hard-block
  file-editing shell commands in plan mode instead of relying on prompting alone…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2885
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d2ce128b84157316921dfd436ce6822ed3c4fbfe663232736657dec8dd8ecf87
product: cline
product_name: Cline
record:
  card_id: cline-2026-08-05-59f9fd
  comparison: ''
  date: '2026-08-05'
  description: 'Cline — v4.1.4: 2 Developer Workflow changes'
  evidence:
  - quote: Hard-block file-editing shell commands in plan mode instead of relying
      on prompting alone. Read-only investigation still works, but file manipulation,
      in-place editors, redirection to files, mutating git subcommands, and package
      installs are refused.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.4
  - quote: Stop treating a turn that completes with a plan as a failed turn when a
      plan-blocked command was its only tool call. The turn no longer ends in the
      error state with a Retry footer, and toggling to Act correctly re-runs the presented
      plan instead of appearing to do nothing.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 2-developer-workflow-changes-in-v4-1-4
  source_release: cline-2026-08-05-v4-1-4-github-365446897-8becc947
  source_type: github_releases
  theme: developer-workflow
  title: 2 Developer Workflow changes in v4.1.4
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-08-03-2-developer-workflow-changes-in-v1-0-78|2
  Developer Workflow changes in v1.0.78]]'
- '[[Changes/Claude Code/2026-08-04-3-developer-workflow-changes-in-v2-1-221|3 Developer
  Workflow changes in v2.1.221]]'
- '[[Changes/OpenCode/2026-08-04-terminal-github-pull-request-reviews-now-include-the-pull-request-number-and-url|Terminal
  GitHub pull request reviews now include the pull request number and URL…]]'
source_release: '[[Releases/Cline/cline-2026-08-05-v4-1-4-github-365446897-8becc947|cline-2026-08-05-v4-1-4-github-365446897-8becc947]]'
source_type: github_releases
theme: developer-workflow
title: 2 Developer Workflow changes in v4.1.4
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Developer Workflow changes in v4.1.4

**Cline** · 2026-08-05 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.4) · from [[Releases/Cline/cline-2026-08-05-v4-1-4-github-365446897-8becc947|v4.1.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hard-block file-editing shell commands in plan mode instead of relying on prompting alone. Read-only investigation still works, but file manipulation, in-place editors, redirection to files, mutating git subcommands, and package installs are refused.

> Stop treating a turn that completes with a plan as a failed turn when a plan-blocked command was its only tool call. The turn no longer ends in the error state with a Retry footer, and toggling to Act correctly re-runs the presented plan instead of appearing to do nothing.

Source: https://github.com/cline/cline/releases/tag/v4.1.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-08-05-recover-from-running-out-of-context-instead-of-failing-with-a-raw-provider-error|Recover from running out of context instead of failing with a raw provider error]] · Context Window
- [[Changes/Cline/2026-08-05-3-interface-experience-changes-in-v4-1-4|3 Interface Experience changes in v4.1.4]] · Interface Experience
- [[Changes/Cline/2026-08-05-2-apps-and-integrations-changes-in-v4-1-4|2 Apps and Integrations changes in v4.1.4]] · Apps and Integrations
- [[Changes/Cline/2026-08-05-5-model-support-changes-in-v4-1-4|5 Model Support changes in v4.1.4]] · Model Support
- [[Changes/Cline/2026-08-05-5-other-changes-in-v4-1-4|5 other changes in v4.1.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-08-04 · OpenCode · [[Changes/OpenCode/2026-08-04-terminal-github-pull-request-reviews-now-include-the-pull-request-number-and-url|Terminal GitHub pull request reviews now include the pull request number and URL…]]
- Later: 2026-08-05 · Kimi Code · [[Changes/Kimi Code/2026-08-05-add-bug-as-an-alias-for-the-feedback-slash-command-type-bug-to-submit-feedback|Add /bug as an alias for the /feedback slash command]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-08-05-59f9fd&body=Card%3A%20Changes%2FCline%2F2026-08-05-2-developer-workflow-changes-in-v4-1-4.md%0ACard%20ID%3A%20cline-2026-08-05-59f9fd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->