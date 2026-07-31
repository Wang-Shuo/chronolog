---
card_id: claude-code-2026-02-06-15e27b
date: '2026-02-06'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 946
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-02-03-added-token-count-tool-uses-and-duration-metrics-to-task-tool-results|claude-code-2026-02-03-7185c1]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: 065c87fc948641d1c2b57c99994c115251e9edae5ba79a236f4df8fc005397fc
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-01-23-added-env-var-claude-code-enable-tasks-set-to-false-to-keep-the-old-system-tempo|claude-code-2026-01-23-c5183e]]'
- '[[Changes/Claude Code/2026-01-27-added-ability-to-delete-tasks-via-the-taskupdate-tool|claude-code-2026-01-27-030c0c]]'
- '[[Changes/Claude Code/2026-02-03-added-token-count-tool-uses-and-duration-metrics-to-task-tool-results|claude-code-2026-02-03-7185c1]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-06-v2-1-33-github-283581096-0f5b01a0|claude-code-2026-02-06-v2-1-33-github-283581096-0f5b01a0]]'
theme: agent-mode
type: change
---

# Added support for restricting which sub-agents can be spawned via `Task(agent_ty

<!-- chronolog:begin region="description" -->
Added support for restricting which sub-agents can be spawned via `Task(agent_type)` syntax in agent "tools" frontmatter
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added support for restricting which sub-agents can be spawned via `Task(agent_type)` syntax in agent "tools" frontmatter
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.33
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-02-03-added-token-count-tool-uses-and-duration-metrics-to-task-tool-results|claude-code-2026-02-03-7185c1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 946
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes