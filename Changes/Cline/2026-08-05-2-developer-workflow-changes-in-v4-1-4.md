---
card_id: cline-2026-08-05-59f9fd
date: '2026-08-05'
description: 'Cline · 2026-08-05 · Developer Workflow: 2 changes in v4.1.4 — Hard-block
  file-editing shell commands in plan mode instead of relying on prompting alone…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1236
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ed73c35422ab1769e9e60ce92f9d6f86ae2b7fcaba94ddf24c4370859916b50e
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
- '[[Changes/Cline/2026-08-02-2-developer-workflow-changes-in-v4-1-3|2 Developer Workflow
  changes in v4.1.3]]'
- '[[Changes/GitHub Copilot CLI/2026-08-03-2-developer-workflow-changes-in-v1-0-78|2
  Developer Workflow changes in v1.0.78]]'
- '[[Changes/Claude Code/2026-08-04-3-developer-workflow-changes-in-v2-1-221|3 Developer
  Workflow changes in v2.1.221]]'
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

- Earlier: 2026-08-04 · Claude Code · [[Changes/Claude Code/2026-08-04-3-developer-workflow-changes-in-v2-1-221|3 Developer Workflow changes in v2.1.221]]
- Later: 2026-08-06 · Claude Code · [[Changes/Claude Code/2026-08-06-2-developer-workflow-changes-in-v2-1-223|2 Developer Workflow changes in v2.1.223]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-08-05-59f9fd&body=Card%3A%20Changes%2FCline%2F2026-08-05-2-developer-workflow-changes-in-v4-1-4.md%0ACard%20ID%3A%20cline-2026-08-05-59f9fd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->