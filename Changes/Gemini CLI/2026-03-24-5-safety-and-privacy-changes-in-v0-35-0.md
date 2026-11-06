---
card_id: gemini-cli-2026-03-24-fe8427
date: '2026-03-24'
description: 'Gemini CLI · 2026-03-24 · Safety and Privacy: 5 changes in Release v0.35.0
  — feat(core): integrate SandboxManager to sandbox all process-spawning tools by…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1073
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dae107a9b3ae7ab64c6b4a50b665441c5a6165d8032de63b7d6226afc462659e
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-03-24-fe8427
  comparison: ''
  date: '2026-03-24'
  description: 'Gemini CLI — Release v0.35.0: 5 Safety and Privacy changes'
  evidence:
  - quote: 'feat(core): integrate SandboxManager to sandbox all process-spawning tools
      by @galz10 in https://github.com/google-gemini/gemini-cli/pull/22231'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
  - quote: 'feat(security): add disableAlwaysAllow setting to disable auto-approvals
      by @galz10 in https://github.com/google-gemini/gemini-cli/pull/21941'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
  - quote: Linux sandbox bubblewrap by @DavidAPierce in https://github.com/google-gemini/gemini-cli/pull/22680
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
  - quote: 'feat(core): implement Stage 2 security and consistency improvements for
      web_fetch by @aishaneeshah in https://github.com/google-gemini/gemini-cli/pull/22217'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
  - quote: Linux sandbox seccomp by @DavidAPierce in https://github.com/google-gemini/gemini-cli/pull/22815
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 5-safety-and-privacy-changes-in-v0-35-0
  source_release: gemini-cli-2026-03-24-v0-35-0-github-300868580-f6f9b621
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in v0.35.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-18-fixed-custom-status-line-showing-nothing-when-workspace-trust-is-blocking-it|Fixed
  custom status line showing nothing when workspace trust is blocking it]]'
- '[[Changes/Codex CLI/2026-03-19-8-safety-and-privacy-changes-in-rust-v0-116-0|8
  Safety and Privacy changes in rust-v0.116.0]]'
- '[[Changes/Claude Code/2026-03-20-2-safety-and-privacy-changes-in-v2-1-81|2 Safety
  and Privacy changes in v2.1.81]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-03-24-v0-35-0-github-300868580-f6f9b621|gemini-cli-2026-03-24-v0-35-0-github-300868580-f6f9b621]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in v0.35.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in v0.35.0

**Gemini CLI** · 2026-03-24 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0) · from [[Releases/Gemini CLI/gemini-cli-2026-03-24-v0-35-0-github-300868580-f6f9b621|Release v0.35.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> feat(core): integrate SandboxManager to sandbox all process-spawning tools by @galz10 in https://github.com/google-gemini/gemini-cli/pull/22231

> feat(security): add disableAlwaysAllow setting to disable auto-approvals by @galz10 in https://github.com/google-gemini/gemini-cli/pull/21941

> Linux sandbox bubblewrap by @DavidAPierce in https://github.com/google-gemini/gemini-cli/pull/22680

> feat(core): implement Stage 2 security and consistency improvements for web_fetch by @aishaneeshah in https://github.com/google-gemini/gemini-cli/pull/22217

> Linux sandbox seccomp by @DavidAPierce in https://github.com/google-gemini/gemini-cli/pull/22815

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-03-24-refactor-core-align-jit-memory-placement-with-tiered-context-model-by-sandytao52|refactor(core): align JIT memory placement with tiered context model]] · Memory and Personalization
- [[Changes/Gemini CLI/2026-03-24-docs-cli-add-custom-keybinding-documentation-by-scidomino-in-https-github-com-go|docs(cli): add custom keybinding documentation]] · Interface Experience
- [[Changes/Gemini CLI/2026-03-24-docs-document-npm-deprecation-warnings-as-safe-to-ignore-by-h30s-in-https-github|docs: document npm deprecation warnings as safe to ignore]] · Files and Data
- [[Changes/Gemini CLI/2026-03-24-2-context-window-changes-in-v0-35-0|2 Context Window changes in v0.35.0]] · Context Window
- [[Changes/Gemini CLI/2026-03-24-10-agent-mode-changes-in-v0-35-0|10 Agent Mode changes in v0.35.0]] · Agent Mode
- [[Changes/Gemini CLI/2026-03-24-feat-skills-improve-async-pr-review-workflow-and-logging-by-mattkorwel-in-https|feat(skills): improve async-pr-review workflow and logging]] · Developer Workflow
- [[Changes/Gemini CLI/2026-03-24-5-apps-and-integrations-changes-in-v0-35-0|5 Apps and Integrations changes in v0.35.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-03-24-docs-core-add-authentication-guide-for-remote-subagents-by-adamfweidman-in-https|docs(core): add authentication guide for remote subagents]] · Account and Access
- [[Changes/Gemini CLI/2026-03-24-7-model-support-changes-in-v0-35-0|7 Model Support changes in v0.35.0]] · Model Support
- [[Changes/Gemini CLI/2026-03-24-feat-telemetry-add-clearcut-instrumentation-for-ai-credits-billing-events-by-gsq|feat(telemetry): add Clearcut instrumentation for AI credits billing events]] · Pricing Model
- [[Changes/Gemini CLI/2026-03-24-2-automation-and-scheduling-changes-in-v0-35-0|2 Automation and Scheduling changes in v0.35.0]] · Automation and Scheduling
- [[Changes/Gemini CLI/2026-03-24-58-other-changes-in-v0-35-0|58 other changes in v0.35.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-20 · Claude Code · [[Changes/Claude Code/2026-03-20-2-safety-and-privacy-changes-in-v2-1-81|2 Safety and Privacy changes in v2.1.81]]
- Later: 2026-03-25 · Claude Code · [[Changes/Claude Code/2026-03-25-2-safety-and-privacy-changes-in-v2-1-83|2 Safety and Privacy changes in v2.1.83]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-03-24-fe8427&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-03-24-5-safety-and-privacy-changes-in-v0-35-0.md%0ACard%20ID%3A%20gemini-cli-2026-03-24-fe8427%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.35.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->