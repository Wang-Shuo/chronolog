---
card_id: lovable-2026-09-11-6d254c
date: '2026-09-11'
description: 'Lovable · 2026-09-11 · Enterprise and Administration: Workspace admins
  and owners on Business and Enterprise plans can now edit the connection settings
  of an…'
diffusion:
  first_in_tracked: '[[Changes/Gemini/2023-05-05-access-for-google-workspace-accounts|Access
    for Google Workspace accounts]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1225
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 234279b2739a74be60be65779d132906957b6ed5031c68fb80bbf9f361a6c73a
product: lovable
product_name: Lovable
record:
  card_id: lovable-2026-09-11-6d254c
  comparison: ''
  date: '2026-09-11'
  description: 'Lovable — Lovable updates — 2026-09-11: Workspace admins and owners
    on Business and Enterprise plans can now edit the connection settings of an existing
    [SSO provider](https://docs.lovable.dev/features/business/sso.md#manage-an-existing-sso-provider).
    Open the provider in your workspace''s identity settings and use its **Connection**
    tab to change the SAML sign-on URL, the signing certificates, or the OIDC client
    secret.'
  evidence:
  - quote: Workspace admins and owners on Business and Enterprise plans can now edit
      the connection settings of an existing [SSO provider](https://docs.lovable.dev/features/business/sso.md#manage-an-existing-sso-provider).
      Open the provider in your workspace's identity settings and use its **Connection**
      tab to change the SAML sign-on URL, the signing certificates, or the OIDC client
      secret.
    source_release: https://docs.lovable.dev/changelog
  - quote: You can now add several signing certificates to a SAML provider. Lovable
      accepts sign-ins signed with any of them, so you can add your identity provider's
      new certificate before it takes effect and remove the old one afterwards.
    source_release: https://docs.lovable.dev/changelog
  - quote: For an OIDC provider, you can now record when the client secret expires,
      and the **Connection** tab shows how long the secret remains valid.
    source_release: https://docs.lovable.dev/changelog
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: lovable
  product_name: Lovable
  slug: edit-an-sso-provider-s-connection-settings
  source_release: lovable-2026-09-11-2026-09-11-fe1ab3d8
  source_type: lovable_changelog
  theme: enterprise-admin
  theme_matches:
  - matched_terms:
    - admins
    - enterprise
    score: 100
    theme: enterprise-admin
  - matched_terms:
    - tab
    score: 50
    theme: editor-experience
  title: Edit an SSO provider's connection settings
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-10-box-dropbox-and-sharepoint-integrations-are-now-rolling-out-to-go-plus-pro-busin|Box,
  Dropbox, and SharePoint integrations are now rolling out to Go, Plus, Pro…]]'
- '[[Changes/Claude/2026-09-10-smart-reports-beta|Smart reports (beta)]]'
- '[[Changes/Lovable/2026-09-11-lock-workspace-membership-to-your-identity-provider|Lock
  workspace membership to your identity provider]]'
source_release: '[[Releases/Lovable/lovable-2026-09-11-2026-09-11-fe1ab3d8|lovable-2026-09-11-2026-09-11-fe1ab3d8]]'
source_type: lovable_changelog
theme: enterprise-admin
title: Edit an SSO provider's connection settings
type: change
---

<!-- chronolog:begin region="header" -->
# Edit an SSO provider's connection settings

**Lovable** · 2026-09-11 · [[Themes/enterprise-admin|Enterprise and Administration]] · Launch · [Official source](https://docs.lovable.dev/changelog) · from [[Releases/Lovable/lovable-2026-09-11-2026-09-11-fe1ab3d8|Lovable updates — 2026-09-11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Workspace admins and owners on Business and Enterprise plans can now edit the connection settings of an existing [SSO provider](https://docs.lovable.dev/features/business/sso.md#manage-an-existing-sso-provider). Open the provider in your workspace's identity settings and use its **Connection** tab to change the SAML sign-on URL, the signing certificates, or the OIDC client secret.
>
> You can now add several signing certificates to a SAML provider. Lovable accepts sign-ins signed with any of them, so you can add your identity provider's new certificate before it takes effect and remove the old one afterwards.
>
> For an OIDC provider, you can now record when the client secret expires, and the **Connection** tab shows how long the secret remains valid.
>
> Source: https://docs.lovable.dev/changelog
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Lovable/2026-09-11-get-a-warning-when-another-lovable-project-already-uses-your-supabase-project|Get a warning when another Lovable project already uses your Supabase project]] · Apps and Integrations
- [[Changes/Lovable/2026-09-11-preview-a-remixable-project-without-signing-in|Preview a remixable project without signing in]] · Interface Experience
- [[Changes/Lovable/2026-09-11-require-two-factor-authentication-for-your-workspace|Require two-factor authentication for your workspace]] · Account and Access
- [[Changes/Lovable/2026-09-11-preview-pdf-attachments-in-chat|Preview PDF attachments in chat]] · Context Window
- [[Changes/Lovable/2026-09-11-lock-workspace-membership-to-your-identity-provider|Lock workspace membership to your identity provider]] · Enterprise and Administration
- [[Changes/Lovable/2026-09-11-connect-other-mcp-clients-to-the-lovable-mcp-server|Connect other MCP clients to the Lovable MCP server]] · Apps and Integrations
- [[Changes/Lovable/2026-09-11-clearer-sharing-settings-for-connections|Clearer sharing settings for connections]] · Collaboration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2026-09-10 · Claude · [[Changes/Claude/2026-09-10-smart-reports-beta|Smart reports (beta)]]
- Later: 2026-09-11 · Replit · [[Changes/Replit/2026-09-11-retrieve-prompt-text-for-compliance-workflows|Retrieve prompt text for compliance workflows]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-05 · Gemini · [[Changes/Gemini/2023-05-05-access-for-google-workspace-accounts|Access for Google Workspace accounts]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20lovable-2026-09-11-6d254c&body=Card%3A%20Changes%2FLovable%2F2026-09-11-edit-an-sso-provider-s-connection-settings.md%0ACard%20ID%3A%20lovable-2026-09-11-6d254c%0ASource%3A%20https%3A%2F%2Fdocs.lovable.dev%2Fchangelog%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->