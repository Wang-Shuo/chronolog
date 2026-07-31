---
card_id: claude-code-2026-04-04-a16052
date: '2026-04-04'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  lag_days: 1101
  role: follower
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-26-mcp-oauth-now-follows-rfc-9728-protected-resource-metadata-discovery-to-find-the|claude-code-2026-03-26-137bc1]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 82cff7dbcc447c8af28acef52338ce858e6a455151265cdfa0da2479524e403e
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-11-added-actionable-guidance-when-oauth-login-or-connectivity-checks-fail-due-to-ss|claude-code-2026-03-11-5a9b80]]'
- '[[Changes/Claude Code/2026-03-18-added-console-flag-to-claude-auth-login-for-anthropic-console-api-billing-authen|claude-code-2026-03-18-43d796]]'
- '[[Changes/Claude Code/2026-03-26-mcp-oauth-now-follows-rfc-9728-protected-resource-metadata-discovery-to-find-the|claude-code-2026-03-26-137bc1]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-04-v2-1-92-github-305189904-2eb020f5|claude-code-2026-04-04-v2-1-92-github-305189904-2eb020f5]]'
theme: account-access
type: change
---

# Added interactive Bedrock setup wizard accessible from the login screen when sel

<!-- chronolog:begin region="description" -->
Added interactive Bedrock setup wizard accessible from the login screen when selecting "3rd-party platform" — guides you through AWS authentication, region configuration, credential verification, and model pinning
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added interactive Bedrock setup wizard accessible from the login screen when selecting "3rd-party platform" — guides you through AWS authentication, region configuration, credential verification, and model pinning
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.92
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-26-mcp-oauth-now-follows-rfc-9728-protected-resource-metadata-discovery-to-find-the|claude-code-2026-03-26-137bc1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: account-access
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]
- Lag Days: 1101
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes