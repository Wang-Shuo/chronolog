---
card_id: claude-code-2026-01-23-c5183e
date: '2026-01-23'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 932
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-01-16-added-plansdirectory-setting-to-customize-where-plan-files-are-stored|claude-code-2026-01-16-16bbe2]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: c482eaf1b89e516f0ba28e2295e4acf654d3936554d547bd736813c6aeb40ca8
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-01-22-agents-are-solving-increasingly-complex-long-running-tasks-across-your-codebase|cursor-2026-01-22-5cc8fc]]'
- '[[Changes/Cursor/2026-01-22-optionally-you-can-define-custom-subagents-learn-more-in-our-docs|cursor-2026-01-22-fba709]]'
- '[[Changes/Cursor/2026-01-22-subagents-are-independent-agents-specialized-to-handle-discrete-parts-of-a-paren|cursor-2026-01-22-fd4ab1]]'
source_release: '[[Releases/Claude Code/claude-code-2026-01-23-v2-1-19-github-279515857-4e1f7640|claude-code-2026-01-23-v2-1-19-github-279515857-4e1f7640]]'
theme: agent-mode
type: change
---

# Added env var `CLAUDE_CODE_ENABLE_TASKS`, set to `false` to keep the old system

<!-- chronolog:begin region="description" -->
Added env var `CLAUDE_CODE_ENABLE_TASKS`, set to `false` to keep the old system temporarily
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added env var `CLAUDE_CODE_ENABLE_TASKS`, set to `false` to keep the old system temporarily
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.19
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-01-16-added-plansdirectory-setting-to-customize-where-plan-files-are-stored|claude-code-2026-01-16-16bbe2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 932
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes