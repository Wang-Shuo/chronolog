---
card_id: claude-code-2026-03-17-6bb864
date: '2026-03-17'
description: 'Claude Code · 2026-03-17 · Reliability and Performance: 2 changes in
  v2.1.77 — Faster startup on macOS (~60ms) by reading keychain credentials in parallel
  with…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1188
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f92aa5a8c60b9cd570d0fff6d0f541ac6faed08892c97faecef805badcb1ca83
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-17-6bb864
  comparison: ''
  date: '2026-03-17'
  description: 'Claude Code — v2.1.77: 2 Reliability and Performance changes'
  evidence:
  - quote: Faster startup on macOS (~60ms) by reading keychain credentials in parallel
      with module loading
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
  - quote: Faster `--resume` on fork-heavy and very large sessions — up to 45% faster
      loading and ~100-150MB less peak memory
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-reliability-and-performance-changes-in-v2-1-77
  source_release: claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c
  source_type: github_releases
  theme: reliability-performance
  title: 2 Reliability and Performance changes in v2.1.77
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-10-improved-bash-command-parsing-by-switching-to-a-native-module-faster-initializat|Improved
  bash command parsing by switching to a native module]]'
- '[[Changes/Claude Code/2026-03-11-2-reliability-and-performance-changes-in-v2-1-73|2
  Reliability and Performance changes in v2.1.73]]'
- '[[Changes/Claude Code/2026-03-12-added-actionable-suggestions-to-context-command-identifies-context-heavy-tools-m|Added
  actionable suggestions to /context command]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c|claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c]]'
source_type: github_releases
theme: reliability-performance
title: 2 Reliability and Performance changes in v2.1.77
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Reliability and Performance changes in v2.1.77

**Claude Code** · 2026-03-17 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.77) · from [[Releases/Claude Code/claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c|v2.1.77]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Faster startup on macOS (~60ms) by reading keychain credentials in parallel with module loading

> Faster `--resume` on fork-heavy and very large sessions — up to 45% faster loading and ~100-150MB less peak memory

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-17-show-a-notice-when-apikeyhelper-takes-longer-than-10s-preventing-it-from-blockin|Show a notice when apiKeyHelper takes longer than 10s, preventing it from blocking…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-03-17-vscode-when-option-click-doesn-t-trigger-native-selection-on-macos-the-footer-no|VSCode When option+click doesn't trigger native selection on macOS, the footer now…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-03-17-vscode-improved-plan-preview-tab-titles-to-use-the-plan-s-heading-instead-of-cla|VSCode Improved plan preview tab titles to use the plan's heading instead…]] · Editor Experience
- [[Changes/Claude Code/2026-03-17-copy-now-accepts-an-optional-index-copy-n-copies-the-nth-latest-assistant-respon|/copy now accepts an optional index: /copy N copies the Nth-latest assistant response]] · Interface Experience
- [[Changes/Claude Code/2026-03-17-2-apps-and-integrations-changes-in-v2-1-77|2 Apps and Integrations changes in v2.1.77]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-17-background-bash-tasks-are-now-killed-if-output-exceeds-5gb-preventing-runaway-pr|Background bash tasks are now killed if output exceeds 5GB, preventing runaway…]] · Developer Workflow
- [[Changes/Claude Code/2026-03-17-3-safety-and-privacy-changes-in-v2-1-77|3 Safety and Privacy changes in v2.1.77]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-17-2-agent-mode-changes-in-v2-1-77|2 Agent Mode changes in v2.1.77]] · Agent Mode
- [[Changes/Claude Code/2026-03-17-increased-default-maximum-output-token-limits-for-claude-opus-4-6-to-64k-tokens|Increased default maximum output token limits for Claude Opus 4.6 to 64k tokens…]] · Model Support
- [[Changes/Claude Code/2026-03-17-3-other-changes-in-v2-1-77|3 other changes in v2.1.77]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-03-12 · Claude Code · [[Changes/Claude Code/2026-03-12-added-actionable-suggestions-to-context-command-identifies-context-heavy-tools-m|Added actionable suggestions to /context command]]
- Later: 2026-03-17 · Claude Code · [[Changes/Claude Code/2026-03-17-improved-memory-usage-and-startup-time-when-resuming-large-sessions|Improved memory usage and startup time when resuming large sessions]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-17-6bb864&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-17-2-reliability-and-performance-changes-in-v2-1-77.md%0ACard%20ID%3A%20claude-code-2026-03-17-6bb864%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.77%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->