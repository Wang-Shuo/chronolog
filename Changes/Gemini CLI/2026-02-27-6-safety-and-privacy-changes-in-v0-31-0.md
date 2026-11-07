---
card_id: gemini-cli-2026-02-27-712b70
date: '2026-02-27'
description: 'Gemini CLI · 2026-02-27 · Safety and Privacy: 6 changes in Release v0.31.0
  — feat(cli): enhance folder trust with configuration discovery and security warnings…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2040
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8672ddc22621a4c14400cdf6004c2e03248e1b2c779f2504671f1ecee69c37f4
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-02-27-712b70
  comparison: ''
  date: '2026-02-27'
  description: 'Gemini CLI — Release v0.31.0: 6 Safety and Privacy changes'
  evidence:
  - quote: 'feat(cli): enhance folder trust with configuration discovery and security
      warnings by @galz10 in https://github.com/google-gemini/gemini-cli/pull/19492'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.31.0
  - quote: 'security: strip deceptive Unicode characters from terminal output by @ehedlund
      in https://github.com/google-gemini/gemini-cli/pull/19026'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.31.0
  - quote: 'security: implement deceptive URL detection and disclosure in tool confirmations
      by @ehedlund in https://github.com/google-gemini/gemini-cli/pull/19288'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.31.0
  - quote: 'fix(core): restore auth consent in headless mode and add unit tests by
      @ehedlund in https://github.com/google-gemini/gemini-cli/pull/19689'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.31.0
  - quote: fix critical dep vulnerability by @scidomino in https://github.com/google-gemini/gemini-cli/pull/20087
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.31.0
  - quote: 'feat(security): Introduce Conseca framework by @shrishabh in https://github.com/google-gemini/gemini-cli/pull/13193'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.31.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 6-safety-and-privacy-changes-in-v0-31-0
  source_release: gemini-cli-2026-02-27-v0-31-0-github-291545882-debd3ec1
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v0.31.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-02-25-9-safety-and-privacy-changes-in-rust-v0-105-0|9
  Safety and Privacy changes in rust-v0.105.0]]'
- '[[Changes/Gemini CLI/2026-02-25-refactor-core-adopt-coretoolcallstatus-enum-for-type-safety-by-jerop-in-https-gi|refactor(core):
  adopt CoreToolCallStatus enum for type safety]]'
- '[[Changes/Codex CLI/2026-02-26-12800-fix-enforce-sandbox-envelope-for-zsh-fork-execution-bolinfest|♯12800
  fix: enforce sandbox envelope for zsh fork execution @bolinfest]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-02-27-v0-31-0-github-291545882-debd3ec1|gemini-cli-2026-02-27-v0-31-0-github-291545882-debd3ec1]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in v0.31.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v0.31.0

**Gemini CLI** · 2026-02-27 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.31.0) · from [[Releases/Gemini CLI/gemini-cli-2026-02-27-v0-31-0-github-291545882-debd3ec1|Release v0.31.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> feat(cli): enhance folder trust with configuration discovery and security warnings by @galz10 in https://github.com/google-gemini/gemini-cli/pull/19492

> security: strip deceptive Unicode characters from terminal output by @ehedlund in https://github.com/google-gemini/gemini-cli/pull/19026

> security: implement deceptive URL detection and disclosure in tool confirmations by @ehedlund in https://github.com/google-gemini/gemini-cli/pull/19288

> fix(core): restore auth consent in headless mode and add unit tests by @ehedlund in https://github.com/google-gemini/gemini-cli/pull/19689

> fix critical dep vulnerability by @scidomino in https://github.com/google-gemini/gemini-cli/pull/20087

> feat(security): Introduce Conseca framework by @shrishabh in https://github.com/google-gemini/gemini-cli/pull/13193

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.31.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-02-27-11-model-support-changes-in-v0-31-0|11 Model Support changes in v0.31.0]] · Model Support
- [[Changes/Gemini CLI/2026-02-27-feat-cli-add-macos-run-event-notifications-interactive-only-by-lyalindotcom-in-h|feat(cli): add macOS run-event notifications (interactive only)]] · Mobile and Desktop
- [[Changes/Gemini CLI/2026-02-27-migrate-core-render-util-to-use-xterm-js-as-part-of-the-rendering-loop-by-jacob3|Migrate core render util to use xterm.js as part of the rendering loop]] · Automation and Scheduling
- [[Changes/Gemini CLI/2026-02-27-feat-telemetry-add-context-breakdown-to-api-response-event-by-sandytao520-in-htt|feat(telemetry): Add context breakdown to API response event]] · Context Window
- [[Changes/Gemini CLI/2026-02-27-feat-browser-implement-experimental-browser-agent-by-gsquared94-in-https-github|feat(browser): implement experimental browser agent]] · Agent Mode
- [[Changes/Gemini CLI/2026-02-27-3-account-and-access-changes-in-v0-31-0|3 Account and Access changes in v0.31.0]] · Account and Access
- [[Changes/Gemini CLI/2026-02-27-feat-cli-include-dir-add-directories-in-autocomplete-suggestions-by-jasmeetsb-in|feat(cli): include /dir add directories in @ autocomplete suggestions]] · Editor Experience
- [[Changes/Gemini CLI/2026-02-27-2-interface-experience-changes-in-v0-31-0|2 Interface Experience changes in v0.31.0]] · Interface Experience
- [[Changes/Gemini CLI/2026-02-27-10-apps-and-integrations-changes-in-v0-31-0|10 Apps and Integrations changes in v0.31.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-02-27-4-developer-workflow-changes-in-v0-31-0|4 Developer Workflow changes in v0.31.0]] · Developer Workflow
- [[Changes/Gemini CLI/2026-02-27-71-other-changes-in-v0-31-0|71 other changes in v0.31.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-02-26 · Codex CLI · [[Changes/Codex CLI/2026-02-26-12800-fix-enforce-sandbox-envelope-for-zsh-fork-execution-bolinfest|♯12800 fix: enforce sandbox envelope for zsh fork execution @bolinfest]]
- Later: 2026-02-28 · Claude Code · [[Changes/Claude Code/2026-02-28-fixed-listener-leak-in-interactive-permission-handler-during-auto-approvals|Fixed listener leak in interactive permission handler during auto-approvals]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-02-27-712b70&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-02-27-6-safety-and-privacy-changes-in-v0-31-0.md%0ACard%20ID%3A%20gemini-cli-2026-02-27-712b70%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.31.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->