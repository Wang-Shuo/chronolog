---
card_id: claude-code-2026-03-17-8bb9c0
date: '2026-03-17'
description: 'Claude Code · 2026-03-17 · Reliability and Performance: Faster `--resume`
  on fork-heavy and very large sessions — up to 45% faster loading and ~100-150MB
  less…'
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
kind: change
machine_hash: 38d65b44ded58ca2c65865b3919796c34cca9fc3d51fb5238f3dcccd73332eeb
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-17-8bb9c0
  comparison: ''
  date: '2026-03-17'
  description: 'Claude Code — v2.1.77: Faster `--resume` on fork-heavy and very large
    sessions — up to 45% faster loading and ~100-150MB less peak memory'
  evidence:
  - quote: Faster `--resume` on fork-heavy and very large sessions — up to 45% faster
      loading and ~100-150MB less peak memory
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: faster-resume-on-fork-heavy-and-very-large-sessions-up-to-45-faster-loading-and
  source_release: claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c
  source_type: github_releases
  theme: reliability-performance
  theme_matches:
  - matched_terms:
    - memory
    score: 110
    theme: memory
  - matched_terms:
    - faster
    score: 50
    theme: reliability-performance
  theme_resolution: manual-semantic-rule-v2
  title: Faster `--resume` on fork-heavy and very large sessions
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-06-3-reliability-and-performance-changes-in-v2-1-70|3
  Reliability and Performance changes in v2.1.70]]'
- '[[Changes/Claude Code/2026-03-10-improved-bash-command-parsing-by-switching-to-a-native-module-faster-initializat|Improved
  bash command parsing by switching to a native module]]'
- '[[Changes/Claude Code/2026-03-11-improved-ide-detection-speed-at-startup|Improved
  IDE detection speed at startup]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c|claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c]]'
source_type: github_releases
theme: reliability-performance
title: Faster --resume on fork-heavy and very large sessions
type: change
---

<!-- chronolog:begin region="header" -->
# Faster `--resume` on fork-heavy and very large sessions

**Claude Code** · 2026-03-17 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.77) · from [[Releases/Claude Code/claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c|v2.1.77]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Faster `--resume` on fork-heavy and very large sessions — up to 45% faster loading and ~100-150MB less peak memory
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-17-show-a-notice-when-apikeyhelper-takes-longer-than-10s-preventing-it-from-blockin|Show a notice when apiKeyHelper takes longer than 10s, preventing it from blocking…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-03-17-vscode-improved-plan-preview-tab-titles-to-use-the-plan-s-heading-instead-of-cla|VSCode Improved plan preview tab titles to use the plan's heading instead…]] · Editor Experience
- [[Changes/Claude Code/2026-03-17-copy-now-accepts-an-optional-index-copy-n-copies-the-nth-latest-assistant-respon|/copy now accepts an optional index: /copy N copies the Nth-latest assistant response]] · Interface Experience
- [[Changes/Claude Code/2026-03-17-2-apps-and-integrations-changes-in-v2-1-77|2 Apps and Integrations changes in v2.1.77]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-17-background-bash-tasks-are-now-killed-if-output-exceeds-5gb-preventing-runaway-pr|Background bash tasks are now killed if output exceeds 5GB, preventing runaway…]] · Developer Workflow
- [[Changes/Claude Code/2026-03-17-3-safety-and-privacy-changes-in-v2-1-77|3 Safety and Privacy changes in v2.1.77]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-17-2-mobile-and-desktop-changes-in-v2-1-77|2 Mobile and Desktop changes in v2.1.77]] · Mobile and Desktop
- [[Changes/Claude Code/2026-03-17-2-agent-mode-changes-in-v2-1-77|2 Agent Mode changes in v2.1.77]] · Agent Mode
- [[Changes/Claude Code/2026-03-17-increased-default-maximum-output-token-limits-for-claude-opus-4-6-to-64k-tokens|Increased default maximum output token limits for Claude Opus 4.6 to 64k tokens…]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-03-11 · Claude Code · [[Changes/Claude Code/2026-03-11-improved-ide-detection-speed-at-startup|Improved IDE detection speed at startup]]
- Later: 2026-03-17 · Claude Code · [[Changes/Claude Code/2026-03-17-improved-memory-usage-and-startup-time-when-resuming-large-sessions|Improved memory usage and startup time when resuming large sessions]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-17-8bb9c0&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-17-faster-resume-on-fork-heavy-and-very-large-sessions-up-to-45-faster-loading-and.md%0ACard%20ID%3A%20claude-code-2026-03-17-8bb9c0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.77%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->