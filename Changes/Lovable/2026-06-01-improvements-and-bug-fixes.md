---
card_id: lovable-2026-06-01-b81e41
date: '2026-06-01'
description: 'Lovable · 2026-06-01 · Safety and Privacy: **App login methods moved
  to *Privacy & security***. Workspace admins and owners on Business and Enterprise
  plans…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2134
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: b4856d0974086f354f03c2041e0d6570d651c2b60554e95257ab371a47ae0797
product: lovable
product_name: Lovable
record:
  card_id: lovable-2026-06-01-b81e41
  comparison: ''
  date: '2026-06-01'
  description: 'Lovable — Lovable updates — 2026-06-01: **App login methods moved
    to *Privacy & security***. Workspace admins and owners on Business and Enterprise
    plans can manage the policy for blocking app sign-in providers from *Settings
    → Privacy & security → [App login methods](https://docs.lovable.dev/features/privacy-and-security-settings.md#app-login-methods)*.
    Functionality is unchanged.'
  evidence:
  - quote: '**App login methods moved to *Privacy & security***. Workspace admins
      and owners on Business and Enterprise plans can manage the policy for blocking
      app sign-in providers from *Settings → Privacy & security → [App login methods](https://docs.lovable.dev/features/privacy-and-security-settings.md#app-login-methods)*.
      Functionality is unchanged.'
    source_release: https://docs.lovable.dev/changelog
  - quote: '**SCIM badge in *Settings → People*.** Members provisioned through SCIM
      now show a small SCIM badge next to their name. Enterprise admins can quickly
      tell which seats are managed by their identity provider and which were invited
      manually, making access reviews and support escalations easier.'
    source_release: https://docs.lovable.dev/changelog
  - quote: '**Session-based SSO login**. Fixed a gap where users in single sign-on
      (SSO) enforced workspaces could still sign in with email and password, bypassing
      the identity provider. SSO sessions are now validated on every request, so deprovisioned
      users lose access immediately.'
    source_release: https://docs.lovable.dev/changelog
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: lovable
  product_name: Lovable
  slug: improvements-and-bug-fixes
  source_release: lovable-2026-06-01-2026-06-01-63e7e167
  source_type: lovable_changelog
  theme: safety-privacy
  theme_matches:
  - matched_terms:
    - login
    - sign in
    score: 110
    theme: account-access
  - matched_terms:
    - admins
    - enterprise
    score: 100
    theme: enterprise-admin
  - matched_terms:
    - privacy
    - security
    score: 100
    theme: safety-privacy
  theme_resolution: manual-semantic-rule-v2
  title: Improvements and bug fixes
  type: change
related_changes:
- '[[Changes/Synthesia/2026-05-29-members-on-free-and-restricted-licenses-can-now-edit-scripts-and-add-screen-reco|Let
  free workspace members help you edit]]'
- '[[Changes/Codex CLI/2026-06-01-11-safety-and-privacy-changes-in-rust-v0-136-0|11
  Safety and Privacy changes in rust-v0.136.0]]'
- '[[Changes/Lovable/2026-06-01-automatic-fixes-for-basic-scan-findings|Automatic
  fixes for Basic scan findings]]'
source_release: '[[Releases/Lovable/lovable-2026-06-01-2026-06-01-63e7e167|lovable-2026-06-01-2026-06-01-63e7e167]]'
source_type: lovable_changelog
theme: safety-privacy
title: Improvements and bug fixes
type: change
---

<!-- chronolog:begin region="header" -->
# Improvements and bug fixes

**Lovable** · 2026-06-01 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://docs.lovable.dev/changelog) · from [[Releases/Lovable/lovable-2026-06-01-2026-06-01-63e7e167|Lovable updates — 2026-06-01]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **App login methods moved to *Privacy & security***. Workspace admins and owners on Business and Enterprise plans can manage the policy for blocking app sign-in providers from *Settings → Privacy & security → [App login methods](https://docs.lovable.dev/features/privacy-and-security-settings.md#app-login-methods)*. Functionality is unchanged.
>
> **SCIM badge in *Settings → People*.** Members provisioned through SCIM now show a small SCIM badge next to their name. Enterprise admins can quickly tell which seats are managed by their identity provider and which were invited manually, making access reviews and support escalations easier.
>
> **Session-based SSO login**. Fixed a gap where users in single sign-on (SSO) enforced workspaces could still sign in with email and password, bypassing the identity provider. SSO sessions are now validated on every request, so deprovisioned users lose access immediately.
>
> Source: https://docs.lovable.dev/changelog
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Lovable/2026-06-01-app-connector-salesforce|App connector: Salesforce]] · Apps and Integrations
- [[Changes/Lovable/2026-06-01-automatic-fixes-for-basic-scan-findings|Automatic fixes for Basic scan findings]] · Safety and Privacy
- [[Changes/Lovable/2026-06-01-security-scan-profiles|Security scan profiles]] · Safety and Privacy
- [[Changes/Lovable/2026-06-01-scheduled-security-scans-enterprise|Scheduled security scans (Enterprise)]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-06-01 · Codex CLI · [[Changes/Codex CLI/2026-06-01-11-safety-and-privacy-changes-in-rust-v0-136-0|11 Safety and Privacy changes in rust-v0.136.0]]
- Later: 2026-06-01 · Open WebUI · [[Changes/Open WebUI/2026-06-01-7-safety-and-privacy-changes-in-v0-9-6|7 Safety and Privacy changes in v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20lovable-2026-06-01-b81e41&body=Card%3A%20Changes%2FLovable%2F2026-06-01-improvements-and-bug-fixes.md%0ACard%20ID%3A%20lovable-2026-06-01-b81e41%0ASource%3A%20https%3A%2F%2Fdocs.lovable.dev%2Fchangelog%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->