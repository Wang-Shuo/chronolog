---
card_id: claude-code-2026-06-15-05b30a
date: '2026-06-15'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1180
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-10-amazon-bedrock-now-reads-the-aws-region-from-aws-config-files-when-aws-region-is|claude-code-2026-06-10-3fd1c9]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: d32bb7ed2dfb3e1abcf859bef101aaa78499ac8d9342bc4b2f64462399a96efa
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-06-added-glob-pattern-support-in-deny-rule-tool-name-position-denies-all-tools-allo|claude-code-2026-06-06-cd06e2]]'
- '[[Changes/Claude Code/2026-06-10-added-a-search-bar-when-browsing-a-marketplace-s-plugins-in-plugin|claude-code-2026-06-10-128ad4]]'
- '[[Changes/Claude Code/2026-06-10-amazon-bedrock-now-reads-the-aws-region-from-aws-config-files-when-aws-region-is|claude-code-2026-06-10-3fd1c9]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-15-v2-1-178-github-339741361-902bc427|claude-code-2026-06-15-v2-1-178-github-339741361-902bc427]]'
theme: apps-integrations
type: change
---

# Skills in nested `.claude/skills` directories now load when working on files the

<!-- chronolog:begin region="description" -->
Skills in nested `.claude/skills` directories now load when working on files there; on a name clash, the nested skill appears as `<dir>:<name>` so both stay available
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Skills in nested `.claude/skills` directories now load when working on files there; on a name clash, the nested skill appears as `<dir>:<name>` so both stay available
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.178
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-10-amazon-bedrock-now-reads-the-aws-region-from-aws-config-files-when-aws-region-is|claude-code-2026-06-10-3fd1c9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1180
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes