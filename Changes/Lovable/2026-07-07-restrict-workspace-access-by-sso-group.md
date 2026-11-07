---
card_id: lovable-2026-07-07-1652b0
date: '2026-07-07'
description: 'Lovable · 2026-07-07 · Enterprise and Administration: Workspace owners
  and admins on Business and Enterprise plans can now map IdP groups to workspace
  roles…'
diffusion:
  first_in_tracked: '[[Changes/Gemini/2023-05-05-access-for-google-workspace-accounts|Access
    for Google Workspace accounts]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1159
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 37255f656310082d390ec687ce3b97c8908083ce797d3587846483dc379ea2a3
product: lovable
product_name: Lovable
record:
  card_id: lovable-2026-07-07-1652b0
  comparison: ''
  date: '2026-07-07'
  description: 'Lovable — Lovable updates — 2026-07-07: Workspace owners and admins
    on Business and Enterprise plans can now map IdP groups to workspace roles for
    their [SSO provider](https://docs.lovable.dev/features/business/sso.md).'
  evidence:
  - quote: Workspace owners and admins on Business and Enterprise plans can now map
      IdP groups to workspace roles for their [SSO provider](https://docs.lovable.dev/features/business/sso.md).
    source_release: https://docs.lovable.dev/changelog
  - quote: Open the provider from **Settings → Identity**, then use the **Groups**
      tab to map IdP groups to viewer, editor, or admin roles. When someone signs
      in through SSO, Lovable assigns the mapped role if their IdP group matches.
      Everyone else gets the default JIT role.
    source_release: https://docs.lovable.dev/changelog
  - quote: Turn on **Group restriction** to limit access to mapped groups only. Anyone
      without a matching IdP group is blocked from signing in, so map every group
      that needs access before turning it on.
    source_release: https://docs.lovable.dev/changelog
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: lovable
  product_name: Lovable
  slug: restrict-workspace-access-by-sso-group
  source_release: lovable-2026-07-07-2026-07-07-3495f67b
  source_type: lovable_changelog
  theme: enterprise-admin
  title: Restrict workspace access by SSO group
  type: change
related_changes:
- '[[Changes/Lovable/2026-07-01-restrict-who-can-download-project-code|Restrict who
  can download project code]]'
- '[[Changes/Lovable/2026-07-03-workspace-admins-and-owners-can-transfer-projects-again|Workspace
  admins and owners can transfer projects again]]'
- '[[Changes/OpenHands/2026-07-06-3-enterprise-and-administration-changes-in-1-9-0|3
  Enterprise and Administration changes in 1.9.0]]'
source_release: '[[Releases/Lovable/lovable-2026-07-07-2026-07-07-3495f67b|lovable-2026-07-07-2026-07-07-3495f67b]]'
source_type: lovable_changelog
theme: enterprise-admin
title: Restrict workspace access by SSO group
type: change
---

<!-- chronolog:begin region="header" -->
# Restrict workspace access by SSO group

**Lovable** · 2026-07-07 · [[Themes/enterprise-admin|Enterprise and Administration]] · Launch · [Official source](https://docs.lovable.dev/changelog) · from [[Releases/Lovable/lovable-2026-07-07-2026-07-07-3495f67b|Lovable updates — 2026-07-07]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Workspace owners and admins on Business and Enterprise plans can now map IdP groups to workspace roles for their [SSO provider](https://docs.lovable.dev/features/business/sso.md).
>
> Open the provider from **Settings → Identity**, then use the **Groups** tab to map IdP groups to viewer, editor, or admin roles. When someone signs in through SSO, Lovable assigns the mapped role if their IdP group matches. Everyone else gets the default JIT role.
>
> Turn on **Group restriction** to limit access to mapped groups only. Anyone without a matching IdP group is blocked from signing in, so map every group that needs access before turning it on.
>
> Source: https://docs.lovable.dev/changelog
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Lovable/2026-07-07-reorder-folders-shared-with-you|Reorder folders shared with you]] · Interface Experience
- [[Changes/Lovable/2026-07-07-app-connector-github-api|App connector: GitHub API]] · Apps and Integrations
- [[Changes/Lovable/2026-07-07-sign-in-with-sso-using-your-company-domain-or-provider-id|Sign in with SSO using your company domain or provider ID]] · Account and Access
- [[Changes/Lovable/2026-07-07-the-last-owner-cannot-leave-a-shared-folder|The last owner cannot leave a shared folder]] · Collaboration
- [[Changes/Lovable/2026-07-07-nano-banana-2-lite-image-model-for-ai-features-in-your-app|Nano Banana 2 Lite image model for AI features in your app]] · Model Support
- [[Changes/Lovable/2026-07-07-find-in-page-clipboard-and-location-in-the-desktop-app|Find in page, clipboard, and location in the desktop app]] · Mobile and Desktop
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2026-07-06 · OpenHands · [[Changes/OpenHands/2026-07-06-3-enterprise-and-administration-changes-in-1-9-0|3 Enterprise and Administration changes in 1.9.0]]
- Later: 2026-07-07 · OpenHands · [[Changes/OpenHands/2026-07-07-feat-enterprise-auth-super-admin-management-endpoint-grant-revoke-list-by-jpshac|feat(enterprise/auth): super-admin management endpoint (grant/revoke/list)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-05 · Gemini · [[Changes/Gemini/2023-05-05-access-for-google-workspace-accounts|Access for Google Workspace accounts]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20lovable-2026-07-07-1652b0&body=Card%3A%20Changes%2FLovable%2F2026-07-07-restrict-workspace-access-by-sso-group.md%0ACard%20ID%3A%20lovable-2026-07-07-1652b0%0ASource%3A%20https%3A%2F%2Fdocs.lovable.dev%2Fchangelog%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->