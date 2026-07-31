---
card_id: claude-code-2026-05-06-43315d
date: '2026-05-06'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1140
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-04-mcp-now-shows-the-tool-count-for-connected-servers-and-flags-servers-that-connec|claude-code-2026-05-04-c7abbc]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: f2201dc629b7ff726c533cf7532c2911e4ebd5b89602ca3b123148ab6c657a26
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-05-01-default-on-users-get-the-plugin-installed-by-default-but-can-opt-out|cursor-2026-05-01-e1fccb]]'
- '[[Changes/Claude Code/2026-05-04-plugin-dir-now-accepts-zip-plugin-archives-in-addition-to-directories|claude-code-2026-05-04-5bd676]]'
- '[[Changes/Claude Code/2026-05-04-mcp-now-shows-the-tool-count-for-connected-servers-and-flags-servers-that-connec|claude-code-2026-05-04-c7abbc]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-06-v2-1-129-github-317982632-ec56fc0f|claude-code-2026-05-06-v2-1-129-github-317982632-ec56fc0f]]'
theme: apps-integrations
type: change
---

# Plugin manifests: `themes` and `monitors` should now be declared under `"experim

<!-- chronolog:begin region="description" -->
Plugin manifests: `themes` and `monitors` should now be declared under `"experimental": { ... }`. Top-level declarations still work but `claude plugin validate` will warn
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Plugin manifests: `themes` and `monitors` should now be declared under `"experimental": { ... }`. Top-level declarations still work but `claude plugin validate` will warn
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.129
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-04-mcp-now-shows-the-tool-count-for-connected-servers-and-flags-servers-that-connec|claude-code-2026-05-04-c7abbc]]
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