---
card_id: claude-code-2026-09-23-ee57ae
date: '2026-09-23'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1285
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: cb587777b65171744e5d0ecf27a648fcca65030729183fcb51035da306914b22
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-23-ee57ae
  comparison: ''
  date: '2026-09-23'
  description: 'Claude Code — v2.1.281: Added `"attribution": false` in `settings.json`
    to hide all commit and PR attribution; older CLI versions skip a settings file
    that holds it, so keep the object form in files shared across versions'
  evidence:
  - quote: 'Added `"attribution": false` in `settings.json` to hide all commit and
      PR attribution; older CLI versions skip a settings file that holds it, so keep
      the object form in files shared across versions'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-attribution-false-in-settings-json-to-hide-all-commit-and-pr-attribution-o
  source_release: claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95
  source_type: github_releases
  theme: developer-workflow
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: 'Added `"attribution": false` in `settings.json` to hide all commit and PR
    attribution'
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-09-improved-the-bash-tool-s-description-guidance-so-claude-describes-what-a-command|claude-code-2026-09-09-b44608]]'
- '[[Changes/Claude Code/2026-09-11-added-otel-metrics-include-repository-to-tag-opentelemetry-metrics-and-events-wi|claude-code-2026-09-11-7141cf]]'
- '[[Changes/Claude Code/2026-09-17-added-syncing-of-the-skills-and-plugins-enabled-on-your-claude-ai-account-to-ter|claude-code-2026-09-17-ed0ee0]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95|claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95]]'
source_type: github_releases
theme: developer-workflow
title: 'Added "attribution": false in settings.json to hide all commit and PR attribution'
type: change
---

# Added `"attribution": false` in `settings.json` to hide all commit and PR attribution

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.281: Added `"attribution": false` in `settings.json` to hide all commit and PR attribution; older CLI versions skip a settings file that holds it, so keep the object form in files shared across versions
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `"attribution": false` in `settings.json` to hide all commit and PR attribution; older CLI versions skip a settings file that holds it, so keep the object form in files shared across versions
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1285
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes