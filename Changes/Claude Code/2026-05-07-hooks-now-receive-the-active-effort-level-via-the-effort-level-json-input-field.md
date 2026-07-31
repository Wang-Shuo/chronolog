---
card_id: claude-code-2026-05-07-3826e7
date: '2026-05-07'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1141
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-06-added-plugin-url-url-flag-to-fetch-a-plugin-zip-archive-from-a-url-for-the-curre|claude-code-2026-05-06-acc535]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 443f08c7fbcb8c1a79db41e731dd790c75b15eaf248fb2e78c2051095ccc825b
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-06-plugin-manifests-themes-and-monitors-should-now-be-declared-under-experimental-t|claude-code-2026-05-06-43315d]]'
- '[[Changes/Claude Code/2026-05-06-added-claude-code-session-id-environment-variable-to-the-bash-tool-subprocess-en|claude-code-2026-05-06-58bd22]]'
- '[[Changes/Claude Code/2026-05-06-added-plugin-url-url-flag-to-fetch-a-plugin-zip-archive-from-a-url-for-the-curre|claude-code-2026-05-06-acc535]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-07-v2-1-133-github-319164825-08653677|claude-code-2026-05-07-v2-1-133-github-319164825-08653677]]'
theme: apps-integrations
type: change
---

# Hooks now receive the active effort level via the `effort.level` JSON input fiel

<!-- chronolog:begin region="description" -->
Hooks now receive the active effort level via the `effort.level` JSON input field and the `$CLAUDE_EFFORT` environment variable, and Bash tool commands can read `$CLAUDE_EFFORT`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Hooks now receive the active effort level via the `effort.level` JSON input field and the `$CLAUDE_EFFORT` environment variable, and Bash tool commands can read `$CLAUDE_EFFORT`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.133
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-06-added-plugin-url-url-flag-to-fetch-a-plugin-zip-archive-from-a-url-for-the-curre|claude-code-2026-05-06-acc535]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1141
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes