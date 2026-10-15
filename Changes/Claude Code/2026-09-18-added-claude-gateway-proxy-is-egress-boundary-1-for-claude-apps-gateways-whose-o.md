---
card_id: claude-code-2026-09-18-1d1508
date: '2026-09-18'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-you-can-join-the-waitlist-to-try-plugins-here|chatgpt-2023-03-23-872ff0]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1275
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: b1f82866337137dfb3a485a5968c398e5343da724aba7555156f43b8a2218bd5
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-18-1d1508
  comparison: ''
  date: '2026-09-18'
  description: 'Claude Code — v2.1.277: Added `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1`
    for Claude apps gateways whose only egress is a forward proxy: every outbound
    request hands the proxy the hostname instead of resolving it locally'
  evidence:
  - quote: 'Added `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1` for Claude apps gateways
      whose only egress is a forward proxy: every outbound request hands the proxy
      the hostname instead of resolving it locally'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-claude-gateway-proxy-is-egress-boundary-1-for-claude-apps-gateways-whose-o
  source_release: claude-code-2026-09-18-v2-1-277-github-391616593-06a20f36
  source_type: github_releases
  theme: apps-integrations
  title: Added `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1` for Claude apps gateways
    whose…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-17-added-store-connect-timeout-seconds-to-the-claude-apps-gateway-config-to-lengthe|claude-code-2026-09-17-494f3b]]'
- '[[Changes/Claude Code/2026-09-17-added-claude-code-mcp-startup-wait-ms-to-bound-how-long-the-first-non-interactiv|claude-code-2026-09-17-4b0f38]]'
- '[[Changes/Claude Code/2026-09-17-added-plugin-install-plugin-marketplace-source-which-offers-to-add-the-marketpla|claude-code-2026-09-17-f354ad]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-18-v2-1-277-github-391616593-06a20f36|claude-code-2026-09-18-v2-1-277-github-391616593-06a20f36]]'
source_type: github_releases
theme: apps-integrations
title: Added CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1 for Claude apps gateways whose…
type: change
---

# Added `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1` for Claude apps gateways whose…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.277: Added `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1` for Claude apps gateways whose only egress is a forward proxy: every outbound request hands the proxy the hostname instead of resolving it locally
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1` for Claude apps gateways whose only egress is a forward proxy: every outbound request hands the proxy the hostname instead of resolving it locally
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/ChatGPT/2023-03-23-you-can-join-the-waitlist-to-try-plugins-here|chatgpt-2023-03-23-872ff0]]
- Lag Days: 1275
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes