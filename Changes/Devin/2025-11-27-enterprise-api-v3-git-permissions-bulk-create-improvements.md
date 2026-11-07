---
card_id: devin-2025-11-27-9db081
date: '2025-11-27'
description: 'Devin · 2025-11-27 · Enterprise and Administration: The Enterprise API
  v3 Git Permissions bulk create endpoint now accepts up to 200 permissions per request…'
diffusion:
  first_in_tracked: '[[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export
    members as CSV (for Enterprise Plans) Quickly download a list of the people…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2144
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 8dd6c5c294f4c6052476d21a6450e5345d4dcdea3b2ac7515e09c49d54b8e3f1
product: devin
product_name: Devin
record:
  card_id: devin-2025-11-27-9db081
  comparison: ''
  date: '2025-11-27'
  description: 'Devin — Devin updates — 2025-11-27: The Enterprise API v3 Git Permissions
    bulk create endpoint now accepts up to 200 permissions per request, increased
    from the previous limit of 100. Additionally, the endpoint now validates requests
    to prevent common configuration errors:'
  evidence:
  - quote: 'The Enterprise API v3 Git Permissions bulk create endpoint now accepts
      up to 200 permissions per request, increased from the previous limit of 100.
      Additionally, the endpoint now validates requests to prevent common configuration
      errors:'
    source_release: https://docs.devin.ai/release-notes/2025
  - quote: '**Duplicate detection**: Requests containing identical permissions (same
      connection, repository path, and group prefix) are now rejected with a clear
      error message listing the duplicates.'
    source_release: https://docs.devin.ai/release-notes/2025
  - quote: '**Overlap detection**: Requests containing a repository-specific permission
      that conflicts with a group prefix permission are now rejected. For example,
      adding both `group_prefix: "myorg"` and `repo_path: "myorg/repo1"` for the same
      connection will fail, since the group prefix already covers that repository.'
    source_release: https://docs.devin.ai/release-notes/2025
  - quote: These validations help maintain a clean and unambiguous permission model,
      preventing confusion about which permissions are active and avoiding unexpected
      behavior when managing permissions.
    source_release: https://docs.devin.ai/release-notes/2025
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: devin
  product_name: Devin
  slug: enterprise-api-v3-git-permissions-bulk-create-improvements
  source_release: devin-2025-11-27-2025-11-27-698fd842
  source_type: devin_changelog
  theme: enterprise-admin
  title: Enterprise API v3 Git Permissions Bulk Create Improvements
  type: change
related_changes:
- '[[Changes/Replit/2025-11-21-teams-and-enterprise|Teams and Enterprise]]'
- '[[Changes/Open WebUI/2025-11-24-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou|
  Looking for an Enterprise Plan((source link)]]'
- '[[Changes/Cline/2025-11-27-creates-and-refactor-enterprise-docs-by-juanpflores-in-https-github-com-cline-cl|Creates
  and Refactor Enterprise Docs]]'
source_release: '[[Releases/Devin/devin-2025-11-27-2025-11-27-698fd842|devin-2025-11-27-2025-11-27-698fd842]]'
source_type: devin_changelog
theme: enterprise-admin
title: Enterprise API v3 Git Permissions Bulk Create Improvements
type: change
---

<!-- chronolog:begin region="header" -->
# Enterprise API v3 Git Permissions Bulk Create Improvements

**Devin** · 2025-11-27 · [[Themes/enterprise-admin|Enterprise and Administration]] · Launch · [Official source](https://docs.devin.ai/release-notes/2025) · from [[Releases/Devin/devin-2025-11-27-2025-11-27-698fd842|Devin updates — 2025-11-27]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> The Enterprise API v3 Git Permissions bulk create endpoint now accepts up to 200 permissions per request, increased from the previous limit of 100. Additionally, the endpoint now validates requests to prevent common configuration errors:
>
> **Duplicate detection**: Requests containing identical permissions (same connection, repository path, and group prefix) are now rejected with a clear error message listing the duplicates.
>
> **Overlap detection**: Requests containing a repository-specific permission that conflicts with a group prefix permission are now rejected. For example, adding both `group_prefix: "myorg"` and `repo_path: "myorg/repo1"` for the same connection will fail, since the group prefix already covers that repository.
>
> These validations help maintain a clean and unambiguous permission model, preventing confusion about which permissions are active and avoiding unexpected behavior when managing permissions.
>
> Source: https://docs.devin.ai/release-notes/2025
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2025-11-27 · Cline · [[Changes/Cline/2025-11-27-creates-and-refactor-enterprise-docs-by-juanpflores-in-https-github-com-cline-cl|Creates and Refactor Enterprise Docs]]
- Later: 2025-12-02 · Cline · [[Changes/Cline/2025-12-02-add-enterprise-to-readme-by-reneehuang1-in-https-github-com-cline-cline-pull-758|add enterprise to readme]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-01-14 · Notion · [[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export members as CSV (for Enterprise Plans) Quickly download a list of the people…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20devin-2025-11-27-9db081&body=Card%3A%20Changes%2FDevin%2F2025-11-27-enterprise-api-v3-git-permissions-bulk-create-improvements.md%0ACard%20ID%3A%20devin-2025-11-27-9db081%0ASource%3A%20https%3A%2F%2Fdocs.devin.ai%2Frelease-notes%2F2025%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->