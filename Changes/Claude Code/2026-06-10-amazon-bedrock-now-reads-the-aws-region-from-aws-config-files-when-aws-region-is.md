---
card_id: claude-code-2026-06-10-3fd1c9
date: '2026-06-10'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1175
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-10-added-a-search-bar-when-browsing-a-marketplace-s-plugins-in-plugin|claude-code-2026-06-10-128ad4]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: c1b7d987095132e66f0cc421608373abb5f7f1ae27c4f7184d71ea5b2ab04a72
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-06-04-we-ve-shipped-a-batch-of-new-functionality-across-the-typescript-and-python-sdks|cursor-2026-06-04-73350b]]'
- '[[Changes/Claude Code/2026-06-06-added-glob-pattern-support-in-deny-rule-tool-name-position-denies-all-tools-allo|claude-code-2026-06-06-cd06e2]]'
- '[[Changes/Claude Code/2026-06-10-added-a-search-bar-when-browsing-a-marketplace-s-plugins-in-plugin|claude-code-2026-06-10-128ad4]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-10-v2-1-172-github-337412034-dc68562c|claude-code-2026-06-10-v2-1-172-github-337412034-dc68562c]]'
theme: apps-integrations
type: change
---

# Amazon Bedrock now reads the AWS region from `~/.aws` config files when `AWS_REG

<!-- chronolog:begin region="description" -->
Amazon Bedrock now reads the AWS region from `~/.aws` config files when `AWS_REGION` isn't set, matching AWS SDK precedence; `/status` shows where the region came from
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Amazon Bedrock now reads the AWS region from `~/.aws` config files when `AWS_REGION` isn't set, matching AWS SDK precedence; `/status` shows where the region came from
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.172
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-10-added-a-search-bar-when-browsing-a-marketplace-s-plugins-in-plugin|claude-code-2026-06-10-128ad4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1175
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes