---
card_id: krea-2026-08-27-e63f18
date: '2026-08-27'
description: 'Krea · 2026-08-27 · Enterprise and Administration: **Enterprise workspaces
  can now pull per-job usage data with `GET /usage`.** The endpoint returns the…'
diffusion:
  first_in_tracked: '[[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export
    members as CSV (for Enterprise Plans) Quickly download a list of the people…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2417
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: de56a57f10b14d5dcf703f0c972f6d7e5fb64ed8327931a74c9e9a3280f1714f
product: krea
product_name: Krea
record:
  card_id: krea-2026-08-27-e63f18
  comparison: ''
  date: '2026-08-27'
  description: 'Krea — MiniMax H3 and H3 Max, Gemini Omni Flash 1.1, and a workspace
    usage API: **Enterprise workspaces can now pull per-job usage data with `GET /usage`.**
    The endpoint returns the workspace''s completed metered jobs in a time window,
    newest first, ready to feed your own reporting pipeline.'
  evidence:
  - quote: '**Enterprise workspaces can now pull per-job usage data with `GET /usage`.**
      The endpoint returns the workspace''s completed metered jobs in a time window,
      newest first, ready to feed your own reporting pipeline.'
    source_release: https://www.krea.ai/docs/changelog
  - quote: Each record includes the job ID, job type, the member who ran it, the completion
      time, and `compute_units`, the same quantity the in-app usage page shows.
    source_release: https://www.krea.ai/docs/changelog
  - quote: Scope the window with `start_date` and `end_date`. A window holding more
      than 30,000 jobs returns a `400`, so split large pulls into shorter windows.
    source_release: https://www.krea.ai/docs/changelog
  - quote: Requires a workspace service API key on a plan with the usage API entitlement.
    source_release: https://www.krea.ai/docs/changelog
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: krea
  product_name: Krea
  slug: workspace-usage-api
  source_release: krea-2026-08-27-2026-08-27-minimax-h3-and-h3-max-gemini-omni-flash-1-1-and-a-wor-7350de0b
  source_type: krea_changelog
  theme: enterprise-admin
  title: Workspace usage API
  type: change
related_changes:
- '[[Changes/Lovable/2026-08-26-record-who-is-behind-each-commit-lovable-pushes|Record
  who is behind each commit Lovable pushes]]'
- '[[Changes/Lovable/2026-08-26-workspace-build-secrets-appear-in-your-project-s-secrets-list|Workspace
  build secrets appear in your project''s secrets list]]'
- '[[Changes/GitHub Copilot CLI/2026-08-27-2-enterprise-and-administration-changes-in-v1-0-81|2
  Enterprise and Administration changes in v1.0.81]]'
source_release: '[[Releases/Krea/krea-2026-08-27-2026-08-27-minimax-h3-and-h3-max-gemini-omni-flash-1-1-and-a-wor-7350de0b|krea-2026-08-27-2026-08-27-minimax-h3-and-h3-max-gemini-omni-flash-1-1-and-a-wor-7350de0b]]'
source_type: krea_changelog
theme: enterprise-admin
title: Workspace usage API
type: change
---

<!-- chronolog:begin region="header" -->
# Workspace usage API

**Krea** · 2026-08-27 · [[Themes/enterprise-admin|Enterprise and Administration]] · Launch · [Official source](https://www.krea.ai/docs/changelog) · from [[Releases/Krea/krea-2026-08-27-2026-08-27-minimax-h3-and-h3-max-gemini-omni-flash-1-1-and-a-wor-7350de0b|MiniMax H3 and H3 Max, Gemini Omni Flash 1.1, and a workspace usage API]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Enterprise workspaces can now pull per-job usage data with `GET /usage`.** The endpoint returns the workspace's completed metered jobs in a time window, newest first, ready to feed your own reporting pipeline.
>
> Each record includes the job ID, job type, the member who ran it, the completion time, and `compute_units`, the same quantity the in-app usage page shows.
>
> Scope the window with `start_date` and `end_date`. A window holding more than 30,000 jobs returns a `400`, so split large pulls into shorter windows.
>
> Requires a workspace service API key on a plan with the usage API entitlement.
>
> Source: https://www.krea.ai/docs/changelog
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Krea/2026-08-27-gemini-omni-flash-1-1|Gemini Omni Flash 1.1]] · Model Support
- [[Changes/Krea/2026-08-27-minimax-h3-and-minimax-h3-max|MiniMax H3 and MiniMax H3 Max]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2026-08-27 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-08-27-2-enterprise-and-administration-changes-in-v1-0-81|2 Enterprise and Administration changes in v1.0.81]]
- Later: 2026-08-28 · Wispr Flow · [[Changes/Wispr Flow/2026-08-28-for-teams-enterprise-desktop|For Teams & Enterprise: (Desktop)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-01-14 · Notion · [[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export members as CSV (for Enterprise Plans) Quickly download a list of the people…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20krea-2026-08-27-e63f18&body=Card%3A%20Changes%2FKrea%2F2026-08-27-workspace-usage-api.md%0ACard%20ID%3A%20krea-2026-08-27-e63f18%0ASource%3A%20https%3A%2F%2Fwww.krea.ai%2Fdocs%2Fchangelog%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->