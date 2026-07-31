---
card_id: claude-code-2026-05-01-6897b7
date: '2026-05-01'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-conversation-history-you-ll-soon-be-able-to-view-past-conversations-with-chatgpt|chatgpt-2022-12-15-23a232]]'
  lag_days: 1233
  role: follower
  scope: tracked-products-only
  theme: projects-workspaces
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-14-added-n-name-name-cli-flag-to-set-a-display-name-for-the-session-at-startup|claude-code-2026-03-14-75b9e4]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: b81e6752501ad5dec59065b1ae7ce89dd1335565f7b865f209dac9294a2724f2
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-02-25-sources-from-chats-save-useful-chatgpt-responses-into-your-project-so-great-outp|chatgpt-2026-02-25-21a801]]'
- '[[Changes/Claude Code/2026-03-06-improved-rename-to-work-while-claude-is-processing-instead-of-being-silently-que|claude-code-2026-03-06-836c05]]'
- '[[Changes/Claude Code/2026-03-14-added-n-name-name-cli-flag-to-set-a-display-name-for-the-session-at-startup|claude-code-2026-03-14-75b9e4]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb|claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb]]'
theme: projects-workspaces
type: change
---

# - Added `claude project purge [path]` to delete all Claude Code state for a proj

<!-- chronolog:begin region="description" -->
- Added `claude project purge [path]` to delete all Claude Code state for a project (transcripts, tasks, file history, config entry) — supports `--dry-run`, `-y/--yes`, `-i/--interactive`, and `--all`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> - Added `claude project purge [path]` to delete all Claude Code state for a project (transcripts, tasks, file history, config entry) — supports `--dry-run`, `-y/--yes`, `-i/--interactive`, and `--all`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-14-added-n-name-name-cli-flag-to-set-a-display-name-for-the-session-at-startup|claude-code-2026-03-14-75b9e4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: projects-workspaces
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2022-12-15-conversation-history-you-ll-soon-be-able-to-view-past-conversations-with-chatgpt|chatgpt-2022-12-15-23a232]]
- Lag Days: 1233
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes