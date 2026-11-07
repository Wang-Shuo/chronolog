---
card_id: lovable-2026-07-10-66ee67
date: '2026-07-10'
description: 'Lovable · 2026-07-10 · Account and Access: Members of Business and Enterprise
  workspaces that use [SAML single…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1198
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 9d16d2eb7998e5836bf6efd41d88af34a5e8bab3223ef5d62a44cde787274fe4
product: lovable
product_name: Lovable
record:
  card_id: lovable-2026-07-10-66ee67
  comparison: ''
  date: '2026-07-10'
  description: 'Lovable — Lovable updates — 2026-07-10: Members of Business and Enterprise
    workspaces that use [SAML single sign-on](https://docs.lovable.dev/features/business/sso.md)
    can now sign in by clicking the Lovable tile in their identity provider''s app
    portal, such as Okta or Microsoft Entra, instead of starting at lovable.dev.'
  evidence:
  - quote: Members of Business and Enterprise workspaces that use [SAML single sign-on](https://docs.lovable.dev/features/business/sso.md)
      can now sign in by clicking the Lovable tile in their identity provider's app
      portal, such as Okta or Microsoft Entra, instead of starting at lovable.dev.
    source_release: https://docs.lovable.dev/changelog
  - quote: Workspace admins and owners turn this on in the SAML provider setup under
      **Settings → Members & access → Identity**. The setup wizard now shows a dedicated
      IdP-initiated ACS URL to add to your identity provider, along with its requirements.
      Group restrictions are enforced the same way as standard SSO sign-in.
    source_release: https://docs.lovable.dev/changelog
  - quote: IdP-initiated sign-in works only while your workspace is the only one that
      has verified your email domain, and it turns off automatically if another workspace
      verifies the same domain. The SAML response must be signed and scoped to the
      SP Entity ID.
    source_release: https://docs.lovable.dev/changelog
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: lovable
  product_name: Lovable
  slug: sign-in-to-lovable-from-your-identity-provider-s-portal
  source_release: lovable-2026-07-10-2026-07-10-b0b0aa18
  source_type: lovable_changelog
  theme: account-access
  title: Sign in to Lovable from your identity provider's portal
  type: change
related_changes:
- '[[Changes/Lovable/2026-07-09-workspace-invitations-expire-after-30-days|Workspace
  invitations expire after 30 days]]'
- '[[Changes/Claude Code/2026-07-10-gateway-login-now-supports-anthropic-operated-public-gateway-endpoints|Gateway:
  /login now supports Anthropic-operated public gateway endpoints]]'
- '[[Changes/GitHub Copilot CLI/2026-07-10-2-account-and-access-changes-in-v1-0-70|2
  Account and Access changes in v1.0.70]]'
source_release: '[[Releases/Lovable/lovable-2026-07-10-2026-07-10-b0b0aa18|lovable-2026-07-10-2026-07-10-b0b0aa18]]'
source_type: lovable_changelog
theme: account-access
title: Sign in to Lovable from your identity provider's portal
type: change
---

<!-- chronolog:begin region="header" -->
# Sign in to Lovable from your identity provider's portal

**Lovable** · 2026-07-10 · [[Themes/account-access|Account and Access]] · Launch · [Official source](https://docs.lovable.dev/changelog) · from [[Releases/Lovable/lovable-2026-07-10-2026-07-10-b0b0aa18|Lovable updates — 2026-07-10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Members of Business and Enterprise workspaces that use [SAML single sign-on](https://docs.lovable.dev/features/business/sso.md) can now sign in by clicking the Lovable tile in their identity provider's app portal, such as Okta or Microsoft Entra, instead of starting at lovable.dev.
>
> Workspace admins and owners turn this on in the SAML provider setup under **Settings → Members & access → Identity**. The setup wizard now shows a dedicated IdP-initiated ACS URL to add to your identity provider, along with its requirements. Group restrictions are enforced the same way as standard SSO sign-in.
>
> IdP-initiated sign-in works only while your workspace is the only one that has verified your email domain, and it turns off automatically if another workspace verifies the same domain. The SAML response must be signed and scoped to the SP Entity ID.
>
> Source: https://docs.lovable.dev/changelog
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Lovable/2026-07-10-see-project-status-in-your-browser-tab|See project status in your browser tab]] · Editor Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-07-10 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-10-2-account-and-access-changes-in-v1-0-70|2 Account and Access changes in v1.0.70]]
- Later: 2026-07-13 · OpenClaw · [[Changes/OpenClaw/2026-07-13-69-account-and-access-changes-in-v2026-7-1|69 Account and Access changes in v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20lovable-2026-07-10-66ee67&body=Card%3A%20Changes%2FLovable%2F2026-07-10-sign-in-to-lovable-from-your-identity-provider-s-portal.md%0ACard%20ID%3A%20lovable-2026-07-10-66ee67%0ASource%3A%20https%3A%2F%2Fdocs.lovable.dev%2Fchangelog%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->