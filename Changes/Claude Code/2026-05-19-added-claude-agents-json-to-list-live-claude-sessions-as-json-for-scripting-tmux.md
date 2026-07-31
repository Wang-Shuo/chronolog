---
card_id: claude-code-2026-05-19-9159e4
date: '2026-05-19'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1048
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-19-added-agent-id-and-parent-agent-id-attributes-to-claude-code-tool-otel-spans-and|claude-code-2026-05-19-78d620]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: eddff195506174a26cf29b8181fc6a7a6745887acb2b34eed287ba64d78f298c
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-19-added-resume-support-for-background-sessions-sessions-started-via-claude-bg-or-a|claude-code-2026-05-19-215520]]'
- '[[Changes/Claude Code/2026-05-19-claude-agents-terminal-tab-title-now-shows-the-awaiting-input-count-so-an-alt-ta|claude-code-2026-05-19-2f1483]]'
- '[[Changes/Claude Code/2026-05-19-added-agent-id-and-parent-agent-id-attributes-to-claude-code-tool-otel-spans-and|claude-code-2026-05-19-78d620]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-19-v2-1-145-github-325388499-227a5ce4|claude-code-2026-05-19-v2-1-145-github-325388499-227a5ce4]]'
theme: agent-mode
type: change
---

# Added `claude agents --json` to list live Claude sessions as JSON for scripting

<!-- chronolog:begin region="description" -->
Added `claude agents --json` to list live Claude sessions as JSON for scripting (tmux-resurrect, status bars, session pickers)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `claude agents --json` to list live Claude sessions as JSON for scripting (tmux-resurrect, status bars, session pickers)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.145
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-19-added-agent-id-and-parent-agent-id-attributes-to-claude-code-tool-otel-spans-and|claude-code-2026-05-19-78d620]]
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