---
card_id: claude-code-2026-02-18-d8f750
date: '2026-02-18'
description: 'Claude Code · 2026-02-18 · Reliability and Performance: 5 changes in
  v2.1.47 — Improved memory usage in long-running sessions by releasing API stream
  buffers…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1161
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b1453ecf9d770344cd4851907b666cfa03ffb984cb0bfe985d3ae1bd1d5378b9
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-02-18-d8f750
  comparison: ''
  date: '2026-02-18'
  description: 'Claude Code — v2.1.47: 5 Reliability and Performance changes'
  evidence:
  - quote: Improved memory usage in long-running sessions by releasing API stream
      buffers, agent context, and skill state after use
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.47
  - quote: Improved startup performance by deferring SessionStart hook execution,
      reducing time-to-interactive by ~500ms.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.47
  - quote: Improved performance of `@` file mentions - file suggestions now appear
      faster by pre-warming the index on startup and using session-based caching with
      background refresh.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.47
  - quote: Improved memory usage by trimming agent task message history after tasks
      complete
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.47
  - quote: Improved memory usage during long agent sessions by eliminating O(n²) message
      accumulation in progress updates
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.47
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-reliability-and-performance-changes-in-v2-1-47
  source_release: claude-code-2026-02-18-v2-1-47-github-287886320-98b6e931
  source_type: github_releases
  theme: reliability-performance
  title: 5 Reliability and Performance changes in v2.1.47
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-02-13-performance-improvements-we-ve-made-multiple-performance-enhancements-to-improve|Performance
  improvements]]'
- '[[Changes/Claude Code/2026-02-17-improved-memory-usage-for-shell-commands-that-produce-large-output-rss-no-longer|Improved
  memory usage for shell commands that produce large output]]'
- '[[Changes/Cursor/2026-02-17-2-reliability-and-performance-changes-in-2-5|2 Reliability
  and Performance changes in 2.5]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-18-v2-1-47-github-287886320-98b6e931|claude-code-2026-02-18-v2-1-47-github-287886320-98b6e931]]'
source_type: github_releases
theme: reliability-performance
title: 5 Reliability and Performance changes in v2.1.47
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Reliability and Performance changes in v2.1.47

**Claude Code** · 2026-02-18 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.47) · from [[Releases/Claude Code/claude-code-2026-02-18-v2-1-47-github-287886320-98b6e931|v2.1.47]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved memory usage in long-running sessions by releasing API stream buffers, agent context, and skill state after use

> Improved startup performance by deferring SessionStart hook execution, reducing time-to-interactive by ~500ms.

> Improved performance of `@` file mentions - file suggestions now appear faster by pre-warming the index on startup and using session-based caching with background refresh.

> Improved memory usage by trimming agent task message history after tasks complete

> Improved memory usage during long agent sessions by eliminating O(n²) message accumulation in progress updates

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.47
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-02-18-3-interface-experience-changes-in-v2-1-47|3 Interface Experience changes in v2.1.47]] · Interface Experience
- [[Changes/Claude Code/2026-02-18-2-agent-mode-changes-in-v2-1-47|2 Agent Mode changes in v2.1.47]] · Agent Mode
- [[Changes/Claude Code/2026-02-18-the-rename-command-now-updates-the-terminal-tab-title-by-default-anthropics-clau|The /rename command now updates the terminal tab title by default…]] · Developer Workflow
- [[Changes/Claude Code/2026-02-18-added-last-assistant-message-field-to-stop-and-subagentstop-hook-inputs-providin|Added last_assistant_message field to Stop and SubagentStop hook inputs, providing…]] · Apps and Integrations
- [[Changes/Claude Code/2026-02-18-2-safety-and-privacy-changes-in-v2-1-47|2 Safety and Privacy changes in v2.1.47]] · Safety and Privacy
- [[Changes/Claude Code/2026-02-18-3-other-changes-in-v2-1-47|3 other changes in v2.1.47]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-02-17 · Cursor · [[Changes/Cursor/2026-02-17-2-reliability-and-performance-changes-in-2-5|2 Reliability and Performance changes in 2.5]]
- Later: 2026-02-18 · Cursor · [[Changes/Cursor/2026-02-18-auto-updates-now-run-in-the-background-for-faster-time-to-interactive|Auto-updates now run in the background for faster time-to-interactive]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-02-18-d8f750&body=Card%3A%20Changes%2FClaude%20Code%2F2026-02-18-5-reliability-and-performance-changes-in-v2-1-47.md%0ACard%20ID%3A%20claude-code-2026-02-18-d8f750%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.47%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->