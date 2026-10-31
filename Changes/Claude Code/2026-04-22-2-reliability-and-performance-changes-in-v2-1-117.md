---
card_id: claude-code-2026-04-22-9261b4
date: '2026-04-22'
description: 'Claude Code · 2026-04-22 · Reliability and Performance: 2 changes in
  v2.1.117 — Native builds on macOS and Linux: the `Glob` and `Grep` tools are replaced
  by…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1224
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ba98ba1d3a3e8527968a8432b03edaa6e9dd12dc56a23aea28260b682fedef57
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-22-9261b4
  comparison: ''
  date: '2026-04-22'
  description: 'Claude Code — v2.1.117: 2 Reliability and Performance changes'
  evidence:
  - quote: 'Native builds on macOS and Linux: the `Glob` and `Grep` tools are replaced
      by embedded `bfs` and `ugrep` available through the Bash tool — faster searches
      without a separate tool round-trip (Windows and npm-installed builds unchanged)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.117
  - quote: 'Windows: cached `where.exe` executable lookups per process for faster
      subprocess launches'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.117
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-reliability-and-performance-changes-in-v2-1-117
  source_release: claude-code-2026-04-22-v2-1-117-github-311984967-1d917373
  source_type: github_releases
  theme: reliability-performance
  title: 2 Reliability and Performance changes in v2.1.117
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-14-reduced-memory-footprint-for-file-reads-edits-and-syntax-highlighting-by-loading|Reduced
  memory footprint for file reads, edits, and syntax highlighting by loading…]]'
- '[[Changes/Claude Code/2026-04-17-improved-ultrareview-faster-launch-with-parallelized-checks-diffstat-in-the-laun|Improved
  /ultrareview: faster launch with parallelized checks, diffstat…]]'
- '[[Changes/Claude Code/2026-04-20-resume-on-large-sessions-is-significantly-faster-up-to-67-on-40mb-sessions-and-h|/resume
  on large sessions is significantly faster (up to 67% on 40MB+ sessions)…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-22-v2-1-117-github-311984967-1d917373|claude-code-2026-04-22-v2-1-117-github-311984967-1d917373]]'
source_type: github_releases
theme: reliability-performance
title: 2 Reliability and Performance changes in v2.1.117
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Reliability and Performance changes in v2.1.117

**Claude Code** · 2026-04-22 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.117) · from [[Releases/Claude Code/claude-code-2026-04-22-v2-1-117-github-311984967-1d917373|v2.1.117]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Native builds on macOS and Linux: the `Glob` and `Grep` tools are replaced by embedded `bfs` and `ugrep` available through the Bash tool — faster searches without a separate tool round-trip (Windows and npm-installed builds unchanged)

> Windows: cached `where.exe` executable lookups per process for faster subprocess launches

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.117
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-22-2-developer-workflow-changes-in-v2-1-117|2 Developer Workflow changes in v2.1.117]] · Developer Workflow
- [[Changes/Claude Code/2026-04-22-4-apps-and-integrations-changes-in-v2-1-117|4 Apps and Integrations changes in v2.1.117]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-22-2-model-support-changes-in-v2-1-117|2 Model Support changes in v2.1.117]] · Model Support
- [[Changes/Claude Code/2026-04-22-opentelemetry-user-prompt-events-now-include-command-name-and-command-source-for|OpenTelemetry: user_prompt events now include command_name and command_source…]] · Pricing Model
- [[Changes/Claude Code/2026-04-22-2-agent-mode-changes-in-v2-1-117|2 Agent Mode changes in v2.1.117]] · Agent Mode
- [[Changes/Claude Code/2026-04-22-advisor-tool-experimental-dialog-now-carries-an-experimental-label-learn-more-li|Advisor Tool (experimental)]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-04-20 · Claude Code · [[Changes/Claude Code/2026-04-20-resume-on-large-sessions-is-significantly-faster-up-to-67-on-40mb-sessions-and-h|/resume on large sessions is significantly faster (up to 67% on 40MB+ sessions)…]]
- Later: 2026-04-28 · Claude Code · [[Changes/Claude Code/2026-04-28-faster-startup-after-upgrading-removed-the-recent-activity-panel-from-the-releas|Faster startup after upgrading]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-22-9261b4&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-22-2-reliability-and-performance-changes-in-v2-1-117.md%0ACard%20ID%3A%20claude-code-2026-04-22-9261b4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.117%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->