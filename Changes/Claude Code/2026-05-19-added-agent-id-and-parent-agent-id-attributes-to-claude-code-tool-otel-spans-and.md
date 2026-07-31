---
card_id: claude-code-2026-05-19-78d620
date: '2026-05-19'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1048
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-19-claude-agents-terminal-tab-title-now-shows-the-awaiting-input-count-so-an-alt-ta|claude-code-2026-05-19-2f1483]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: 2e1c4e571f8925367069d9d127bce57f905975ae00757712301c801ca2e2479e
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-05-18-composer-2-5-is-now-available-in-cursor|cursor-2026-05-18-3afa8e]]'
- '[[Changes/Claude Code/2026-05-19-added-resume-support-for-background-sessions-sessions-started-via-claude-bg-or-a|claude-code-2026-05-19-215520]]'
- '[[Changes/Claude Code/2026-05-19-claude-agents-terminal-tab-title-now-shows-the-awaiting-input-count-so-an-alt-ta|claude-code-2026-05-19-2f1483]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-19-v2-1-145-github-325388499-227a5ce4|claude-code-2026-05-19-v2-1-145-github-325388499-227a5ce4]]'
theme: agent-mode
type: change
---

# Added `agent_id` and `parent_agent_id` attributes to `claude_code.tool` OTEL spa

<!-- chronolog:begin region="description" -->
Added `agent_id` and `parent_agent_id` attributes to `claude_code.tool` OTEL spans, and fixed trace parenting so background subagent spans nest under the dispatching Agent tool span
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `agent_id` and `parent_agent_id` attributes to `claude_code.tool` OTEL spans, and fixed trace parenting so background subagent spans nest under the dispatching Agent tool span
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.145
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-19-claude-agents-terminal-tab-title-now-shows-the-awaiting-input-count-so-an-alt-ta|claude-code-2026-05-19-2f1483]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1048
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes