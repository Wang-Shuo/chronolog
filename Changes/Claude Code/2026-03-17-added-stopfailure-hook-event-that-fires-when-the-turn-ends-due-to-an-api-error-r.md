---
card_id: claude-code-2026-03-17-331b63
date: '2026-03-17'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1090
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-14-added-mcp-elicitation-support-mcp-servers-can-now-request-structured-input-mid-t|claude-code-2026-03-14-928360]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 419730ff49129f4b4cfb3c3ef1f5bce6f0ce140b732fbd96cde68d6c8f81c872
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-12-changed-plugin-dir-so-local-dev-copies-now-override-installed-marketplace-plugin|claude-code-2026-03-12-f0c0b4]]'
- '[[Changes/Claude Code/2026-03-14-added-new-elicitation-and-elicitationresult-hooks-to-intercept-and-override-resp|claude-code-2026-03-14-00facb]]'
- '[[Changes/Claude Code/2026-03-14-added-mcp-elicitation-support-mcp-servers-can-now-request-structured-input-mid-t|claude-code-2026-03-14-928360]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-17-v2-1-78-github-298204446-1f2c1721|claude-code-2026-03-17-v2-1-78-github-298204446-1f2c1721]]'
theme: apps-integrations
type: change
---

# Added `StopFailure` hook event that fires when the turn ends due to an API error

<!-- chronolog:begin region="description" -->
Added `StopFailure` hook event that fires when the turn ends due to an API error (rate limit, auth failure, etc.)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `StopFailure` hook event that fires when the turn ends due to an API error (rate limit, auth failure, etc.)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.78
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-14-added-mcp-elicitation-support-mcp-servers-can-now-request-structured-input-mid-t|claude-code-2026-03-14-928360]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1090
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes