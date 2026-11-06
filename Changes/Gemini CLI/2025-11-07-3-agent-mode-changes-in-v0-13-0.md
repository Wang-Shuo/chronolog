---
card_id: gemini-cli-2025-11-07-7d9f53
date: '2025-11-07'
description: 'Gemini CLI · 2025-11-07 · Agent Mode: 3 changes in Release v0.13.0 —
  Enforce timeout for subagents by @silviojr in…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 855
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 98600d3fec6a1238add5fa5adcfd7d57a5ac787f91894d6b7dae5fd2aa7bdb50
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2025-11-07-7d9f53
  comparison: ''
  date: '2025-11-07'
  description: 'Gemini CLI — Release v0.13.0: 3 Agent Mode changes'
  evidence:
  - quote: Enforce timeout for subagents by @silviojr in https://github.com/google-gemini/gemini-cli/pull/12232
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.13.0
  - quote: Grants subagent a recovery turn for when it hits TIMEOUT, MAX_TURNS or
      NO_TOOL_CALL failures. by @silviojr in https://github.com/google-gemini/gemini-cli/pull/12344
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.13.0
  - quote: Log recovery events (nudges) that happens inside the subagent by @silviojr
      in https://github.com/google-gemini/gemini-cli/pull/12408
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.13.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 3-agent-mode-changes-in-v0-13-0
  source_release: gemini-cli-2025-11-07-v0-13-0-github-260462305-15cfa0b7
  source_type: github_releases
  theme: agent-mode
  title: 3 Agent Mode changes in v0.13.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-10-30-3-agent-mode-changes-in-rust-v0-52-0|3 Agent Mode
  changes in rust-v0.52.0]]'
- '[[Changes/GitHub Copilot CLI/2025-11-03-custom-agents-with-special-characters-in-filenames-no-longer-fail|Custom
  agents with special characters in filenames no longer fail]]'
- '[[Changes/Gemini CLI/2025-11-04-add-regression-tests-for-shell-command-parsing-by-cornmander-in-https-github-com|Add
  regression tests for shell command parsing]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2025-11-07-v0-13-0-github-260462305-15cfa0b7|gemini-cli-2025-11-07-v0-13-0-github-260462305-15cfa0b7]]'
source_type: github_releases
theme: agent-mode
title: 3 Agent Mode changes in v0.13.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Agent Mode changes in v0.13.0

**Gemini CLI** · 2025-11-07 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.13.0) · from [[Releases/Gemini CLI/gemini-cli-2025-11-07-v0-13-0-github-260462305-15cfa0b7|Release v0.13.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Enforce timeout for subagents by @silviojr in https://github.com/google-gemini/gemini-cli/pull/12232

> Grants subagent a recovery turn for when it hits TIMEOUT, MAX_TURNS or NO_TOOL_CALL failures. by @silviojr in https://github.com/google-gemini/gemini-cli/pull/12344

> Log recovery events (nudges) that happens inside the subagent by @silviojr in https://github.com/google-gemini/gemini-cli/pull/12408

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.13.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2025-11-07-fixing-minor-formatting-issues-in-quota-and-pricing-md-by-hyangah-in-https-githu|fixing minor formatting issues in quota-and-pricing.md]] · Pricing Model
- [[Changes/Gemini CLI/2025-11-07-2-account-and-access-changes-in-v0-13-0|2 Account and Access changes in v0.13.0]] · Account and Access
- [[Changes/Gemini CLI/2025-11-07-feat-prevent-self-imports-and-fix-build-loop-by-mattkorwel-in-https-github-com-g|feat: Prevent self-imports and fix build loop]] · Automation and Scheduling
- [[Changes/Gemini CLI/2025-11-07-feat-core-implement-granular-memory-loaders-for-jit-architecture-by-abhipatel12|feat(core): Implement granular memory loaders for JIT architecture]] · Memory and Personalization
- [[Changes/Gemini CLI/2025-11-07-4-model-support-changes-in-v0-13-0|4 Model Support changes in v0.13.0]] · Model Support
- [[Changes/Gemini CLI/2025-11-07-only-show-screen-reader-notice-once-by-chrstnb-in-https-github-com-google-gemini|Only show screen reader notice once]] · Accessibility and Localization
- [[Changes/Gemini CLI/2025-11-07-4-interface-experience-changes-in-v0-13-0|4 Interface Experience changes in v0.13.0]] · Interface Experience
- [[Changes/Gemini CLI/2025-11-07-9-apps-and-integrations-changes-in-v0-13-0|9 Apps and Integrations changes in v0.13.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2025-11-07-remove-context-percentage-in-footer-by-default-by-abhipatel12-in-https-github-co|Remove context percentage in footer by default]] · Context Window
- [[Changes/Gemini CLI/2025-11-07-refactor-todo-improve-performance-and-readability-of-todo-component-by-miguelsol|refactor(todo): improve performance and readability of todo component]] · Reliability and Performance
- [[Changes/Gemini CLI/2025-11-07-enable-codebase-investigator-by-default-for-preview-by-silviojr-in-https-github|enable codebase investigator by default for preview]] · Editor Experience
- [[Changes/Gemini CLI/2025-11-07-5-developer-workflow-changes-in-v0-13-0|5 Developer Workflow changes in v0.13.0]] · Developer Workflow
- [[Changes/Gemini CLI/2025-11-07-migrate-console-error-to-coreevents-debugger-for-sandbox-logger-chatrecordingser|migrate console.error to coreEvents/debugger for sandbox, logger, chatRecordingService]] · Safety and Privacy
- [[Changes/Gemini CLI/2025-11-07-55-other-changes-in-v0-13-0|55 other changes in v0.13.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2025-11-04 · Gemini CLI · [[Changes/Gemini CLI/2025-11-04-add-regression-tests-for-shell-command-parsing-by-cornmander-in-https-github-com|Add regression tests for shell command parsing]]
- Later: 2025-11-12 · Gemini CLI · [[Changes/Gemini CLI/2025-11-12-2-agent-mode-changes-in-v0-14-0|2 Agent Mode changes in v0.14.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2025-11-07-7d9f53&body=Card%3A%20Changes%2FGemini%20CLI%2F2025-11-07-3-agent-mode-changes-in-v0-13-0.md%0ACard%20ID%3A%20gemini-cli-2025-11-07-7d9f53%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.13.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->