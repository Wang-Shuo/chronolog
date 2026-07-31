---
card_id: claude-code-2026-05-06-58bd22
date: '2026-05-06'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1140
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-06-plugin-manifests-themes-and-monitors-should-now-be-declared-under-experimental-t|claude-code-2026-05-06-43315d]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 2deff53ce0219dfa7f1b3ea758422f57b90b4c92e8b50f8a20d5043a917931b4
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-04-plugin-dir-now-accepts-zip-plugin-archives-in-addition-to-directories|claude-code-2026-05-04-5bd676]]'
- '[[Changes/Claude Code/2026-05-04-mcp-now-shows-the-tool-count-for-connected-servers-and-flags-servers-that-connec|claude-code-2026-05-04-c7abbc]]'
- '[[Changes/Claude Code/2026-05-06-plugin-manifests-themes-and-monitors-should-now-be-declared-under-experimental-t|claude-code-2026-05-06-43315d]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-06-v2-1-132-github-318578987-ed60d664|claude-code-2026-05-06-v2-1-132-github-318578987-ed60d664]]'
theme: apps-integrations
type: change
---

# Added `CLAUDE_CODE_SESSION_ID` environment variable to the Bash tool subprocess

<!-- chronolog:begin region="description" -->
Added `CLAUDE_CODE_SESSION_ID` environment variable to the Bash tool subprocess environment, matching the `session_id` passed to hooks
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_CODE_SESSION_ID` environment variable to the Bash tool subprocess environment, matching the `session_id` passed to hooks
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.132
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-06-plugin-manifests-themes-and-monitors-should-now-be-declared-under-experimental-t|claude-code-2026-05-06-43315d]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1140
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes