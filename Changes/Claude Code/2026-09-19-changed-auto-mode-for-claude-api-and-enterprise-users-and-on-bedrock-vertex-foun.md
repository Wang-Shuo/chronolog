---
card_id: claude-code-2026-09-19-0ddc26
date: '2026-09-19'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|chatgpt-2022-12-15-6d306d]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1374
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 27713ae5463eedf4f8490ad72c463be0fa4693a8a69acec6f9f66cad7259b2c3
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-19-0ddc26
  comparison: ''
  date: '2026-09-19'
  description: 'Claude Code — v2.1.278: Changed auto mode for Claude API and Enterprise
    users, and on Bedrock, Vertex, Foundry and gateways, to default to the server-side
    classifier, which does not charge for classifier overhead (`CLAUDE_CODE_AUTO_MODE_SERVER=0`
    opts out on Bedrock, Vertex, Foundry and gateways); warns on billed fallback.
    See https://code.claude.com/docs/en/auto-mode-classifier-billing'
  evidence:
  - quote: Changed auto mode for Claude API and Enterprise users, and on Bedrock,
      Vertex, Foundry and gateways, to default to the server-side classifier, which
      does not charge for classifier overhead (`CLAUDE_CODE_AUTO_MODE_SERVER=0` opts
      out on Bedrock, Vertex, Foundry and gateways); warns on billed fallback. See
      https://code.claude.com/docs/en/auto-mode-classifier-billing
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.278
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: changed-auto-mode-for-claude-api-and-enterprise-users-and-on-bedrock-vertex-foun
  source_release: claude-code-2026-09-19-v2-1-278-github-391877760-2958ad0a
  source_type: github_releases
  theme: pricing-model
  theme_matches:
  - matched_terms:
    - auto mode
    score: 60
    theme: agent-mode
  - matched_terms:
    - enterprise
    score: 50
    theme: enterprise-admin
  - matched_terms:
    - billing
    score: 50
    theme: pricing-model
  theme_resolution: manual-semantic-rule-v1
  title: Changed auto mode for Claude API and Enterprise users, and on Bedrock, Vertex…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-28-added-a-per-session-prompt-cache-line-to-cost-hit-ratio-misses-tokens-re-cached|claude-code-2026-08-28-3956b9]]'
- '[[Changes/ChatGPT/2026-09-09-pro-100-month-up-to-15-hours-with-gpt-live-1|chatgpt-2026-09-09-3e50fc]]'
- '[[Changes/Claude Code/2026-09-10-added-to-the-claude-apps-gateway-with-pricing-set-in-gateway-yaml-signed-in-clau|claude-code-2026-09-10-501aa5]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-19-v2-1-278-github-391877760-2958ad0a|claude-code-2026-09-19-v2-1-278-github-391877760-2958ad0a]]'
source_type: github_releases
theme: pricing-model
title: Changed auto mode for Claude API and Enterprise users, and on Bedrock, Vertex…
type: change
---

# Changed auto mode for Claude API and Enterprise users, and on Bedrock, Vertex…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.278: Changed auto mode for Claude API and Enterprise users, and on Bedrock, Vertex, Foundry and gateways, to default to the server-side classifier, which does not charge for classifier overhead (`CLAUDE_CODE_AUTO_MODE_SERVER=0` opts out on Bedrock, Vertex, Foundry and gateways); warns on billed fallback. See https://code.claude.com/docs/en/auto-mode-classifier-billing
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Changed auto mode for Claude API and Enterprise users, and on Bedrock, Vertex, Foundry and gateways, to default to the server-side classifier, which does not charge for classifier overhead (`CLAUDE_CODE_AUTO_MODE_SERVER=0` opts out on Bedrock, Vertex, Foundry and gateways); warns on billed fallback. See https://code.claude.com/docs/en/auto-mode-classifier-billing
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.278
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
- Lag Days: 1374
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes