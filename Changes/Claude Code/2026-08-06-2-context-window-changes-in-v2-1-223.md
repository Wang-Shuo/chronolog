---
card_id: claude-code-2026-08-06-a8460a
date: '2026-08-06'
description: 'Claude Code · 2026-08-06 · Context Window: 2 changes in v2.1.223 — Changed
  `CLAUDE_CODE_DISABLE_1M_CONTEXT` to hold every Claude model with a native 1M window…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1190
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 18b590a652b982130bb742448fffe23865228e75ce11cb85ba7e4d177e253796
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-06-a8460a
  comparison: ''
  date: '2026-08-06'
  description: 'Claude Code — v2.1.223: 2 Context Window changes'
  evidence:
  - quote: Changed `CLAUDE_CODE_DISABLE_1M_CONTEXT` to hold every Claude model with
      a native 1M window to 200K via auto-compaction, not just a fixed list; a startup
      warning now appears when auto-compaction isn't holding the session to 200K
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.223
  - quote: Changed auto-compact to keep sessions on unrecognized model IDs within
      the assumed context window instead of letting them grow past it; set `CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT=1`
      to restore the previous behavior
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.223
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-context-window-changes-in-v2-1-223
  source_release: claude-code-2026-08-06-v2-1-223-github-365870283-03a5b13d
  source_type: github_releases
  theme: context-window
  title: 2 Context Window changes in v2.1.223
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-22-changed-skills-with-context-fork-to-run-in-the-background-by-default-opt-out-per|Changed
  skills with context: fork to run in the background by default]]'
- '[[Changes/ChatGPT/2026-08-04-if-you-paste-more-than-10k-characters-into-the-composer-chatgpt-will-automatical-1bd022|If
  you paste more than 10k characters into the composer, ChatGPT will automatically…]]'
- '[[Changes/Claude Code/2026-08-04-improved-stats-panel-to-count-cache-tokens-in-its-token-totals-with-a-breakdown|Improved
  Stats panel to count cache tokens in its token totals, with a breakdown…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-06-v2-1-223-github-365870283-03a5b13d|claude-code-2026-08-06-v2-1-223-github-365870283-03a5b13d]]'
source_type: github_releases
theme: context-window
title: 2 Context Window changes in v2.1.223
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Context Window changes in v2.1.223

**Claude Code** · 2026-08-06 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.223) · from [[Releases/Claude Code/claude-code-2026-08-06-v2-1-223-github-365870283-03a5b13d|v2.1.223]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changed `CLAUDE_CODE_DISABLE_1M_CONTEXT` to hold every Claude model with a native 1M window to 200K via auto-compaction, not just a fixed list; a startup warning now appears when auto-compaction isn't holding the session to 200K

> Changed auto-compact to keep sessions on unrecognized model IDs within the assumed context window instead of letting them grow past it; set `CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT=1` to restore the previous behavior

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.223
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-06-2-developer-workflow-changes-in-v2-1-223|2 Developer Workflow changes in v2.1.223]] · Developer Workflow
- [[Changes/Claude Code/2026-08-06-2-agent-mode-changes-in-v2-1-223|2 Agent Mode changes in v2.1.223]] · Agent Mode
- [[Changes/Claude Code/2026-08-06-3-safety-and-privacy-changes-in-v2-1-223|3 Safety and Privacy changes in v2.1.223]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-08-04 · Claude Code · [[Changes/Claude Code/2026-08-04-improved-stats-panel-to-count-cache-tokens-in-its-token-totals-with-a-breakdown|Improved Stats panel to count cache tokens in its token totals, with a breakdown…]]
- Later: 2026-08-11 · Claude Code · [[Changes/Claude Code/2026-08-11-improved-compaction-progress-the-retry-countdown-and-stall-hint-now-appear-durin|Improved compaction progress]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-06-a8460a&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-06-2-context-window-changes-in-v2-1-223.md%0ACard%20ID%3A%20claude-code-2026-08-06-a8460a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.223%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->