---
card_id: claude-code-2026-09-19-0ddc26
date: '2026-09-19'
description: 'Claude Code · 2026-09-19 · Pricing Model: Changed auto mode for Claude
  API and Enterprise users, and on Bedrock, Vertex, Foundry and gateways, to default
  to…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily
    limit: To ensure a high-quality experience for all ChatGPT users, we…]]'
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
machine_hash: 953cb2ce8d68b4a027a022dc7d95f595b49dca1f62e5d7e37666c4bfc910cc9b
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
- '[[Changes/Claude Code/2026-08-28-added-a-per-session-prompt-cache-line-to-cost-hit-ratio-misses-tokens-re-cached|Added
  a per-session prompt-cache line to /cost…]]'
- '[[Changes/ChatGPT/2026-09-09-pro-100-month-up-to-15-hours-with-gpt-live-1|Pro ($100/month):
  Up to 15 hours with GPT-Live-1]]'
- '[[Changes/Claude Code/2026-09-10-added-to-the-claude-apps-gateway-with-pricing-set-in-gateway-yaml-signed-in-clau|Added
  to the Claude apps gateway]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-19-v2-1-278-github-391877760-2958ad0a|claude-code-2026-09-19-v2-1-278-github-391877760-2958ad0a]]'
source_type: github_releases
theme: pricing-model
title: Changed auto mode for Claude API and Enterprise users, and on Bedrock, Vertex…
type: change
---

<!-- chronolog:begin region="header" -->
# Changed auto mode for Claude API and Enterprise users, and on Bedrock, Vertex…

**Claude Code** · 2026-09-19 · [[Themes/pricing-model|Pricing Model]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.278) · from [[Releases/Claude Code/claude-code-2026-09-19-v2-1-278-github-391877760-2958ad0a|v2.1.278]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Changed auto mode for Claude API and Enterprise users, and on Bedrock, Vertex, Foundry and gateways, to default to the server-side classifier, which does not charge for classifier overhead (`CLAUDE_CODE_AUTO_MODE_SERVER=0` opts out on Bedrock, Vertex, Foundry and gateways); warns on billed fallback. See https://code.claude.com/docs/en/auto-mode-classifier-billing
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.278
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-19-added-an-auto-mode-server-row-to-status-showing-whether-this-session-s-auto-mode|Added an Auto mode server row to /status showing whether this session's auto…]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-09-10 · Claude Code · [[Changes/Claude Code/2026-09-10-added-to-the-claude-apps-gateway-with-pricing-set-in-gateway-yaml-signed-in-clau|Added to the Claude apps gateway]]
- Later: 2026-09-28 · Claude Code · [[Changes/Claude Code/2026-09-28-added-dollar-amounts-to-the-claude-apps-gateway-spend-limit-in-usage-and-the-sta|Added dollar amounts to the Claude apps gateway spend limit in /usage…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily limit: To ensure a high-quality experience for all ChatGPT users, we…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-19-0ddc26&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-19-changed-auto-mode-for-claude-api-and-enterprise-users-and-on-bedrock-vertex-foun.md%0ACard%20ID%3A%20claude-code-2026-09-19-0ddc26%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.278%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->