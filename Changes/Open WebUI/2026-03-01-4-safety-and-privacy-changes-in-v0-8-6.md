---
card_id: open-webui-2026-03-01-9927a4
date: '2026-03-01'
description: "Open WebUI · 2026-03-01 · Safety and Privacy: 4 changes in v0.8.6 —
  \U0001F6E1️ **Docker image SBOM attestation.** Docker images now include a Software
  Bill of…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2042
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7159c819f5a9b61dffdf952142e8dd1a0bf303b1aaceede3a9bcb98699ed14a9
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-01-9927a4
  comparison: ''
  date: '2026-03-01'
  description: 'Open WebUI — v0.8.6: 4 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F6E1️ **Docker image SBOM attestation.** Docker images now include
      a Software Bill of Materials (SBOM) for vulnerability scanning and supply chain
      security compliance. [#21779](https://github.com/open-webui/open-webui/issues/21779),
      [Commit](https://github.com/open-webui/open-webui/commit/febc66ef2bb05606b59719e737ac5ad839002977)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F4E1 **Reporting-Endpoints security header.** Administrators can
      now configure a Reporting-Endpoints header via the REPORTING_ENDPOINTS environment
      variable to receive CSP violation reports directly, aiding in security policy
      debugging and hardening. [#21830](https://github.com/open-webui/open-webui/issues/21830)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F465 **Default group share permission.** Administrators can now
      configure the default sharing permission for new groups via the DEFAULT_GROUP_SHARE_PERMISSION
      environment variable, controlling whether anyone, no one, or only members can
      share to new groups. [Commit](https://github.com/open-webui/open-webui/commit/538501c88da034434bcd1969f15341dbbaf154e4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F464 **User sharing permission enforcement.** The user sharing option
      now correctly respects the USER_PERMISSIONS_ACCESS_GRANTS_ALLOW_USERS setting,
      fixing an issue where sharing to individual users was incorrectly allowed even
      when disabled. [#21856](https://github.com/open-webui/open-webui/pull/21856),
      [Commit](https://github.com/open-webui/open-webui/commit/acb21470241ed6fd3eb3f659f196f697c418d9e8),
      [Commit](https://github.com/open-webui/open-webui/commit/ace69bba7512dc0a653695f9e6311712dfabb640)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-safety-and-privacy-changes-in-v0-8-6
  source_release: open-webui-2026-03-01-v0-8-6-github-291846033-263bca05
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in v0.8.6
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-02-26-12800-fix-enforce-sandbox-envelope-for-zsh-fork-execution-bolinfest|♯12800
  fix: enforce sandbox envelope for zsh fork execution @bolinfest]]'
- '[[Changes/Gemini CLI/2026-02-27-6-safety-and-privacy-changes-in-v0-31-0|6 Safety
  and Privacy changes in v0.31.0]]'
- '[[Changes/Claude Code/2026-02-28-fixed-listener-leak-in-interactive-permission-handler-during-auto-approvals|Fixed
  listener leak in interactive permission handler during auto-approvals]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-01-v0-8-6-github-291846033-263bca05|open-webui-2026-03-01-v0-8-6-github-291846033-263bca05]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in v0.8.6
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in v0.8.6

**Open WebUI** · 2026-03-01 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.6) · from [[Releases/Open WebUI/open-webui-2026-03-01-v0-8-6-github-291846033-263bca05|v0.8.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🛡️ **Docker image SBOM attestation.** Docker images now include a Software Bill of Materials (SBOM) for vulnerability scanning and supply chain security compliance. [#21779](https://github.com/open-webui/open-webui/issues/21779), [Commit](https://github.com/open-webui/open-webui/commit/febc66ef2bb05606b59719e737ac5ad839002977)

> 📡 **Reporting-Endpoints security header.** Administrators can now configure a Reporting-Endpoints header via the REPORTING_ENDPOINTS environment variable to receive CSP violation reports directly, aiding in security policy debugging and hardening. [#21830](https://github.com/open-webui/open-webui/issues/21830)

> 👥 **Default group share permission.** Administrators can now configure the default sharing permission for new groups via the DEFAULT_GROUP_SHARE_PERMISSION environment variable, controlling whether anyone, no one, or only members can share to new groups. [Commit](https://github.com/open-webui/open-webui/commit/538501c88da034434bcd1969f15341dbbaf154e4)

> 👤 **User sharing permission enforcement.** The user sharing option now correctly respects the USER_PERMISSIONS_ACCESS_GRANTS_ALLOW_USERS setting, fixing an issue where sharing to individual users was incorrectly allowed even when disabled. [#21856](https://github.com/open-webui/open-webui/pull/21856), [Commit](https://github.com/open-webui/open-webui/commit/acb21470241ed6fd3eb3f659f196f697c418d9e8), [Commit](https://github.com/open-webui/open-webui/commit/ace69bba7512dc0a653695f9e6311712dfabb640)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-01-21-reliability-and-performance-changes-in-v0-8-6|21 Reliability and Performance changes in v0.8.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-01-2-search-and-browsing-changes-in-v0-8-6|2 Search and Browsing changes in v0.8.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-01-oauth-session-token-decryption-oauth-sessions-are-now-properly-detached-from-the|🔓 OAuth session token decryption. OAuth sessions are now properly detached…]] · Context Window
- [[Changes/Open WebUI/2026-03-01-individual-user-sharing-control-administrators-can-now-disable-individual-user-s|🔐 Individual user sharing control. Administrators can now disable individual…]] · Collaboration
- [[Changes/Open WebUI/2026-03-01-4-interface-experience-changes-in-v0-8-6|4 Interface Experience changes in v0.8.6]] · Interface Experience
- [[Changes/Open WebUI/2026-03-01-3-account-and-access-changes-in-v0-8-6|3 Account and Access changes in v0.8.6]] · Account and Access
- [[Changes/Open WebUI/2026-03-01-8-model-support-changes-in-v0-8-6|8 Model Support changes in v0.8.6]] · Model Support
- [[Changes/Open WebUI/2026-03-01-9-developer-workflow-changes-in-v0-8-6|9 Developer Workflow changes in v0.8.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-01-6-other-changes-in-v0-8-6|6 other changes in v0.8.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-02-28 · Claude Code · [[Changes/Claude Code/2026-02-28-fixed-listener-leak-in-interactive-permission-handler-during-auto-approvals|Fixed listener leak in interactive permission handler during auto-approvals]]
- Later: 2026-03-02 · Codex CLI · [[Changes/Codex CLI/2026-03-02-8-safety-and-privacy-changes-in-rust-v0-107-0|8 Safety and Privacy changes in rust-v0.107.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-01-9927a4&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-01-4-safety-and-privacy-changes-in-v0-8-6.md%0ACard%20ID%3A%20open-webui-2026-03-01-9927a4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->