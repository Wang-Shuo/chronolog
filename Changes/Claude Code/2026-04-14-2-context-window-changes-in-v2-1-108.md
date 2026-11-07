---
card_id: claude-code-2026-04-14-b0ba97
date: '2026-04-14'
description: 'Claude Code · 2026-04-14 · Context Window: 2 changes in v2.1.108 — Added
  `ENABLE_PROMPT_CACHING_1H` env var to opt into 1-hour prompt cache TTL on API key…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2400
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a6fc1db301b7a7f505371ce77e74888b4c0066a1131711e266ab8866297422e9
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-14-b0ba97
  comparison: ''
  date: '2026-04-14'
  description: 'Claude Code — v2.1.108: 2 Context Window changes'
  evidence:
  - quote: Added `ENABLE_PROMPT_CACHING_1H` env var to opt into 1-hour prompt cache
      TTL on API key, Bedrock, Vertex, and Foundry (`ENABLE_PROMPT_CACHING_1H_BEDROCK`
      is deprecated but still honored), and `FORCE_PROMPT_CACHING_5M` to force 5-minute
      TTL
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.108
  - quote: Added recap feature to provide context when returning to a session, configurable
      in /config and manually invocable with /recap; force with `CLAUDE_CODE_ENABLE_AWAY_SUMMARY`
      if telemetry disabled.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.108
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-context-window-changes-in-v2-1-108
  source_release: claude-code-2026-04-14-v2-1-108-github-309009167-35123bd5
  source_type: github_releases
  theme: context-window
  title: 2 Context Window changes in v2.1.108
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-04-10-4-context-window-changes-in-rust-v0-119-0|4 Context
  Window changes in rust-v0.119.0]]'
- '[[Changes/Devin/2026-04-10-knowledge-search-auto-expand|Knowledge Search Auto-Expand]]'
- '[[Changes/Codex CLI/2026-04-11-3-context-window-changes-in-rust-v0-120-0|3 Context
  Window changes in rust-v0.120.0]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-14-v2-1-108-github-309009167-35123bd5|claude-code-2026-04-14-v2-1-108-github-309009167-35123bd5]]'
source_type: github_releases
theme: context-window
title: 2 Context Window changes in v2.1.108
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Context Window changes in v2.1.108

**Claude Code** · 2026-04-14 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.108) · from [[Releases/Claude Code/claude-code-2026-04-14-v2-1-108-github-309009167-35123bd5|v2.1.108]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `ENABLE_PROMPT_CACHING_1H` env var to opt into 1-hour prompt cache TTL on API key, Bedrock, Vertex, and Foundry (`ENABLE_PROMPT_CACHING_1H_BEDROCK` is deprecated but still honored), and `FORCE_PROMPT_CACHING_5M` to force 5-minute TTL

> Added recap feature to provide context when returning to a session, configurable in /config and manually invocable with /recap; force with `CLAUDE_CODE_ENABLE_AWAY_SUMMARY` if telemetry disabled.

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.108
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-14-2-safety-and-privacy-changes-in-v2-1-108|2 Safety and Privacy changes in v2.1.108]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-14-2-interface-experience-changes-in-v2-1-108|2 Interface Experience changes in v2.1.108]] · Interface Experience
- [[Changes/Claude Code/2026-04-14-reduced-memory-footprint-for-file-reads-edits-and-syntax-highlighting-by-loading|Reduced memory footprint for file reads, edits, and syntax highlighting by loading…]] · Reliability and Performance
- [[Changes/Claude Code/2026-04-14-improved-model-to-warn-before-switching-models-mid-conversation-since-the-next-r|Improved /model to warn before switching models mid-conversation, since the next…]] · Model Support
- [[Changes/Claude Code/2026-04-14-3-other-changes-in-v2-1-108|3 other changes in v2.1.108]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-04-11 · Codex CLI · [[Changes/Codex CLI/2026-04-11-3-context-window-changes-in-rust-v0-120-0|3 Context Window changes in rust-v0.120.0]]
- Later: 2026-04-14 · Gemini CLI · [[Changes/Gemini CLI/2026-04-14-2-context-window-changes-in-v0-38-0|2 Context Window changes in v0.38.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-14-b0ba97&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-14-2-context-window-changes-in-v2-1-108.md%0ACard%20ID%3A%20claude-code-2026-04-14-b0ba97%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.108%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->