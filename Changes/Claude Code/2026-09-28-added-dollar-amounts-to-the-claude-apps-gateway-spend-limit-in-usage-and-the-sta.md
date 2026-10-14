---
card_id: claude-code-2026-09-28-ce7703
date: '2026-09-28'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|chatgpt-2022-12-15-6d306d]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1383
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: 64c074c74e3715223bbe0c155ff79674632ba0241b85cb62250a92e9d726b500
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-28-ce7703
  comparison: ''
  date: '2026-09-28'
  description: 'Claude Code — v2.1.284: Added dollar amounts to the Claude apps gateway
    spend limit in `/usage` and the status line (for example "$271.40 / $500.00 spent
    this month") when the gateway runs this version or later; the status line''s `rate_limits.spend_limit`
    also gains `used_usd`, `limit_usd` and `period`'
  evidence:
  - quote: Added dollar amounts to the Claude apps gateway spend limit in `/usage`
      and the status line (for example "$271.40 / $500.00 spent this month") when
      the gateway runs this version or later; the status line's `rate_limits.spend_limit`
      also gains `used_usd`, `limit_usd` and `period`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-dollar-amounts-to-the-claude-apps-gateway-spend-limit-in-usage-and-the-sta
  source_release: claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49
  source_type: github_releases
  theme: pricing-model
  theme_matches:
  - matched_terms:
    - status line
    score: 60
    theme: interface-experience
  - matched_terms:
    - apps
    score: 50
    theme: apps-integrations
  theme_resolution: manual-semantic-rule-v2
  title: Added dollar amounts to the Claude apps gateway spend limit in `/usage` and
    the
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-09-pro-100-month-up-to-15-hours-with-gpt-live-1|chatgpt-2026-09-09-3e50fc]]'
- '[[Changes/Claude Code/2026-09-10-added-to-the-claude-apps-gateway-with-pricing-set-in-gateway-yaml-signed-in-clau|claude-code-2026-09-10-501aa5]]'
- '[[Changes/Claude Code/2026-09-19-changed-auto-mode-for-claude-api-and-enterprise-users-and-on-bedrock-vertex-foun|claude-code-2026-09-19-0ddc26]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49]]'
source_type: github_releases
theme: pricing-model
title: Added dollar amounts to the Claude apps gateway spend limit in /usage and the
type: change
---

# Added dollar amounts to the Claude apps gateway spend limit in `/usage` and the

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.284: Added dollar amounts to the Claude apps gateway spend limit in `/usage` and the status line (for example "$271.40 / $500.00 spent this month") when the gateway runs this version or later; the status line's `rate_limits.spend_limit` also gains `used_usd`, `limit_usd` and `period`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added dollar amounts to the Claude apps gateway spend limit in `/usage` and the status line (for example "$271.40 / $500.00 spent this month") when the gateway runs this version or later; the status line's `rate_limits.spend_limit` also gains `used_usd`, `limit_usd` and `period`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: pricing-model
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|chatgpt-2022-12-15-6d306d]]
- Lag Days: 1383
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes