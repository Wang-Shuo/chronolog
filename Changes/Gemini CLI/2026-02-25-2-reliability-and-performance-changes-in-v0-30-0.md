---
card_id: gemini-cli-2026-02-25-cae5b5
date: '2026-02-25'
description: 'Gemini CLI · 2026-02-25 · Reliability and Performance: 2 changes in
  Release v0.30.0 — Revert "fix(mcp): ensure MCP transport is closed to prevent memory
  leaks"…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1168
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3be96cf56ec698482bc099274dc2832994d23de90066ed8c3ac27a7cb4843217
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-02-25-cae5b5
  comparison: ''
  date: '2026-02-25'
  description: 'Gemini CLI — Release v0.30.0: 2 Reliability and Performance changes'
  evidence:
  - quote: 'Revert "fix(mcp): ensure MCP transport is closed to prevent memory leaks"
      by @skeshive in https://github.com/google-gemini/gemini-cli/pull/18771'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.30.0
  - quote: Add autoconfigure memory usage setting to the dialog by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/18510
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.30.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 2-reliability-and-performance-changes-in-v0-30-0
  source_release: gemini-cli-2026-02-25-v0-30-0-github-290144121-620926b3
  source_type: github_releases
  theme: reliability-performance
  title: 2 Reliability and Performance changes in v0.30.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-02-20-improve-code-search-speed-in-large-repos|Improve
  code search speed in large repos]]'
- '[[Changes/Cline/2026-02-24-preconnect-websocket-to-reduce-response-latency|Preconnect
  websocket to reduce response latency]]'
- '[[Changes/Codex CLI/2026-02-25-3-reliability-and-performance-changes-in-rust-v0-105-0|3
  Reliability and Performance changes in rust-v0.105.0]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-02-25-v0-30-0-github-290144121-620926b3|gemini-cli-2026-02-25-v0-30-0-github-290144121-620926b3]]'
source_type: github_releases
theme: reliability-performance
title: 2 Reliability and Performance changes in v0.30.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Reliability and Performance changes in v0.30.0

**Gemini CLI** · 2026-02-25 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.30.0) · from [[Releases/Gemini CLI/gemini-cli-2026-02-25-v0-30-0-github-290144121-620926b3|Release v0.30.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Revert "fix(mcp): ensure MCP transport is closed to prevent memory leaks" by @skeshive in https://github.com/google-gemini/gemini-cli/pull/18771

> Add autoconfigure memory usage setting to the dialog by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/18510

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.30.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-02-25-feat-plan-document-and-validate-plan-mode-policy-overrides-by-jerop-in-https-git|feat(plan): document and validate Plan Mode policy overrides]] · Files and Data
- [[Changes/Gemini CLI/2026-02-25-8-model-support-changes-in-v0-30-0|8 Model Support changes in v0.30.0]] · Model Support
- [[Changes/Gemini CLI/2026-02-25-2-context-window-changes-in-v0-30-0|2 Context Window changes in v0.30.0]] · Context Window
- [[Changes/Gemini CLI/2026-02-25-enable-in-cli-extension-management-commands-for-team-by-chrstnb-in-https-github|Enable in-CLI extension management commands for team]] · Collaboration
- [[Changes/Gemini CLI/2026-02-25-test-evals-mark-all-save-memory-evals-as-usually-passes-due-to-unreliability-by|test(evals): mark all save_memory evals as USUALLY_PASSES due to unreliability]] · Memory and Personalization
- [[Changes/Gemini CLI/2026-02-25-8-apps-and-integrations-changes-in-v0-30-0|8 Apps and Integrations changes in v0.30.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-02-25-refactor-core-adopt-coretoolcallstatus-enum-for-type-safety-by-jerop-in-https-gi|refactor(core): adopt CoreToolCallStatus enum for type safety]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-02-25-perf-ui-optimize-table-rendering-by-memoizing-styled-characters-by-devr0306-in-h|perf(ui): optimize table rendering by memoizing styled characters]] · Interface Experience
- [[Changes/Gemini CLI/2026-02-25-3-developer-workflow-changes-in-v0-30-0|3 Developer Workflow changes in v0.30.0]] · Developer Workflow
- [[Changes/Gemini CLI/2026-02-25-4-agent-mode-changes-in-v0-30-0|4 Agent Mode changes in v0.30.0]] · Agent Mode
- [[Changes/Gemini CLI/2026-02-25-feat-plan-hide-plan-write-and-edit-operations-on-plans-in-plan-mode-by-jerop-in|feat(plan): hide plan write and edit operations on plans in Plan Mode]] · Editor Experience
- [[Changes/Gemini CLI/2026-02-25-feat-admin-add-admin-controls-documentation-by-skeshive-in-https-github-com-goog|feat(admin): Add admin controls documentation]] · Enterprise and Administration
- [[Changes/Gemini CLI/2026-02-25-introduce-limits-for-search-results-by-gundermanc-in-https-github-com-google-gem|Introduce limits for search results]] · Search and Browsing
- [[Changes/Gemini CLI/2026-02-25-53-other-changes-in-v0-30-0|53 other changes in v0.30.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-02-25 · Codex CLI · [[Changes/Codex CLI/2026-02-25-3-reliability-and-performance-changes-in-rust-v0-105-0|3 Reliability and Performance changes in rust-v0.105.0]]
- Later: 2026-02-26 · Claude Code · [[Changes/Claude Code/2026-02-26-improved-memory-usage-in-multi-agent-sessions-by-releasing-completed-subagent-ta|Improved memory usage in multi-agent sessions by releasing completed subagent task state]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-02-25-cae5b5&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-02-25-2-reliability-and-performance-changes-in-v0-30-0.md%0ACard%20ID%3A%20gemini-cli-2026-02-25-cae5b5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.30.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->