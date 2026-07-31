---
card_id: claude-code-2026-03-12-f0c0b4
date: '2026-03-12'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1085
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-10-added-claude-plugins-as-an-alias-for-claude-plugin|claude-code-2026-03-10-f60eaf]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 4fa8e2ebe0f4f1c03e2ea8e4d94b439ad4d36d44971ec73538fb59075e1b691d
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-10-added-claude-plugins-as-an-alias-for-claude-plugin|claude-code-2026-03-10-f60eaf]]'
- '[[Changes/Cursor/2026-03-11-try-out-the-new-plugins-at-cursor-com-marketplace-or-read-more-in-our-announceme|cursor-2026-03-11-868a6a]]'
- '[[Changes/Cursor/2026-03-11-we-ve-added-more-than-30-new-plugins-from-partners-such-as-atlassian-datadog-git|cursor-2026-03-11-d051e9]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-12-v2-1-74-github-295929475-2ee971ae|claude-code-2026-03-12-v2-1-74-github-295929475-2ee971ae]]'
theme: apps-integrations
type: change
---

# Changed `--plugin-dir` so local dev copies now override installed marketplace pl

<!-- chronolog:begin region="description" -->
Changed `--plugin-dir` so local dev copies now override installed marketplace plugins with the same name (unless that plugin is force-enabled by managed settings)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Changed `--plugin-dir` so local dev copies now override installed marketplace plugins with the same name (unless that plugin is force-enabled by managed settings)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.74
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-10-added-claude-plugins-as-an-alias-for-claude-plugin|claude-code-2026-03-10-f60eaf]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1085
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes