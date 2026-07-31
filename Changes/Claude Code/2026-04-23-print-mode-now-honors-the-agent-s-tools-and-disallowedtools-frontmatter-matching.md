---
card_id: claude-code-2026-04-23-5a8186
date: '2026-04-23'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1022
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-22-forked-subagents-can-now-be-enabled-on-external-builds-by-setting-claude-code-fo|claude-code-2026-04-22-9b1eed]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: d55a4eacf2241a3cf93682e3dba83175db44154994cad10b7d7009b5101fa85f
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-04-14-ask-a-quick-side-question-without-derailing-the-agent-s-main-task-btw-allows-you|cursor-2026-04-14-37f69f]]'
- '[[Changes/Claude Code/2026-04-22-agent-frontmatter-mcpservers-are-now-loaded-for-main-thread-agent-sessions-via-a|claude-code-2026-04-22-50e627]]'
- '[[Changes/Claude Code/2026-04-22-forked-subagents-can-now-be-enabled-on-external-builds-by-setting-claude-code-fo|claude-code-2026-04-22-9b1eed]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-23-v2-1-119-github-312949780-573724e7|claude-code-2026-04-23-v2-1-119-github-312949780-573724e7]]'
theme: agent-mode
type: change
---

# `--print` mode now honors the agent's `tools:` and `disallowedTools:` frontmatte

<!-- chronolog:begin region="description" -->
`--print` mode now honors the agent's `tools:` and `disallowedTools:` frontmatter, matching interactive-mode behavior
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `--print` mode now honors the agent's `tools:` and `disallowedTools:` frontmatter, matching interactive-mode behavior
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.119
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-22-forked-subagents-can-now-be-enabled-on-external-builds-by-setting-claude-code-fo|claude-code-2026-04-22-9b1eed]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1022
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes