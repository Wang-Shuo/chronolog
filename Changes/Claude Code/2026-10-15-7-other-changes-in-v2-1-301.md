---
card_id: claude-code-2026-10-15-a69d03
date: '2026-10-15'
description: 'Claude Code · 2026-10-15 · Other changes: 7 changes in v2.1.301 — Added
  `CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS` so unattended retry mode…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2b9257de4311f01c276c5216a733e237cda9dd4c946a65e412b4dd20ebb75631
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-15-a69d03
  comparison: ''
  date: '2026-10-15'
  description: 'Claude Code — v2.1.301: 7 other changes'
  evidence:
  - quote: Added `CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS` so unattended
      retry mode (`CLAUDE_CODE_RETRY_WATCHDOG`) ends a request at a usage limit that
      resets too far away instead of waiting
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.301
  - quote: Added OpenTelemetry tracing guidance to the `claude-api` skill, including
      setting up trace destinations with the `ant` CLI
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.301
  - quote: 'Added the `%` motion to vim mode: jump to the matching bracket, alone
      or with d/c/y'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.301
  - quote: Added `classifier_category` to OpenTelemetry `tool_decision` events, naming
      the built-in rule a classifier block matched, when `OTEL_LOG_TOOL_DETAILS=1`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.301
  - quote: Changed a mod hook's `.catch` handler to run only when the hook throws
      or times out; events raised beneath the hook's own calls now skip that hook
      without asking its `.catch`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.301
  - quote: Changed a mod's `$.env.set` to resolve with `{}` once the variable is set
      or unset, or with `{ deny }` saying why when the write is not made
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.301
  - quote: '[VSCode] Added a "Get more usage" link to the usage-limit banner for Pro
      and Max plans in the VS Code and JetBrains panels'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.301
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 7-other-changes-in-v2-1-301
  source_release: claude-code-2026-10-15-v2-1-301-github-413913133-a3fb5b4e
  source_type: github_releases
  theme: uncategorized
  title: 7 other changes in v2.1.301
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-10-15-v2-1-301-github-413913133-a3fb5b4e|claude-code-2026-10-15-v2-1-301-github-413913133-a3fb5b4e]]'
source_type: github_releases
theme: uncategorized
title: 7 other changes in v2.1.301
type: change
---

<!-- chronolog:begin region="header" -->
# 7 other changes in v2.1.301

**Claude Code** · 2026-10-15 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.301) · from [[Releases/Claude Code/claude-code-2026-10-15-v2-1-301-github-413913133-a3fb5b4e|v2.1.301]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS` so unattended retry mode (`CLAUDE_CODE_RETRY_WATCHDOG`) ends a request at a usage limit that resets too far away instead of waiting

> Added OpenTelemetry tracing guidance to the `claude-api` skill, including setting up trace destinations with the `ant` CLI

> Added the `%` motion to vim mode: jump to the matching bracket, alone or with d/c/y

> Added `classifier_category` to OpenTelemetry `tool_decision` events, naming the built-in rule a classifier block matched, when `OTEL_LOG_TOOL_DETAILS=1`

> Changed a mod hook's `.catch` handler to run only when the hook throws or times out; events raised beneath the hook's own calls now skip that hook without asking its `.catch`

> Changed a mod's `$.env.set` to resolve with `{}` once the variable is set or unset, or with `{ deny }` saying why when the write is not made

> [VSCode] Added a "Get more usage" link to the usage-limit banner for Pro and Max plans in the VS Code and JetBrains panels

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.301
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-15-2-developer-workflow-changes-in-v2-1-301|2 Developer Workflow changes in v2.1.301]] · Developer Workflow
- [[Changes/Claude Code/2026-10-15-5-safety-and-privacy-changes-in-v2-1-301|5 Safety and Privacy changes in v2.1.301]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-15-2-interface-experience-changes-in-v2-1-301|2 Interface Experience changes in v2.1.301]] · Interface Experience
- [[Changes/Claude Code/2026-10-15-improved-artifacts-pages-claude-writes-now-paint-the-band-above-a-sticky-header|Improved artifacts: pages Claude writes now paint the band above a sticky header…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-15-improved-switching-to-a-model-with-a-smaller-context-window-a-conversation-too-l|Improved switching to a model with a smaller context window]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-15-a69d03&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-15-7-other-changes-in-v2-1-301.md%0ACard%20ID%3A%20claude-code-2026-10-15-a69d03%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.301%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->