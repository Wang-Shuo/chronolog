---
card_id: dify-2026-03-27-c42571
date: '2026-03-27'
description: 'Dify · 2026-03-27 · Safety and Privacy: 6 changes in v1.13.3 — > The
  Sandbox image used by Dify v1.13.3 expects the following Python and Node.js paths.'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2068
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e1b072cc7a85baace31d104c3bbf9dd51f6fe8694551743b48a594edd8878570
product: dify
product_name: Dify
record:
  card_id: dify-2026-03-27-c42571
  comparison: ''
  date: '2026-03-27'
  description: 'Dify — v1.13.3: 6 Safety and Privacy changes'
  evidence:
  - quote: '> The Sandbox image used by Dify v1.13.3 expects the following Python
      and Node.js paths.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.3
  - quote: '> If you upgraded from an older Docker Compose deployment and already
      have `docker/volumes/sandbox/conf/config.yaml`, update it on the host machine:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.3
  - quote: '> Do not edit the file inside the sandbox container. The directory `docker/volumes/sandbox/conf`
      is mounted into the container as `/conf`, so host changes persist after container
      restarts.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.3
  - quote: 'test: migrate dataset permission tests to testcontainers by @Desel72 in
      https://github.com/langgenius/dify/pull/33906'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.3
  - quote: 'fix(sdk): patch flatted vulnerability in nodejs client lockfile by @lyzno1
      in https://github.com/langgenius/dify/pull/33996'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.3
  - quote: 'chore: bump Dify to 1.13.3 and sandbox to 0.2.13 by @laipz8200 in https://github.com/langgenius/dify/pull/34079'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 6-safety-and-privacy-changes-in-1-13-3
  source_release: dify-2026-03-27-1-13-3-github-302258183-3ff73e84
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in 1.13.3
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-03-26-5-safety-and-privacy-changes-in-rust-v0-117-0|5
  Safety and Privacy changes in rust-v0.117.0]]'
- '[[Changes/OpenCode/2026-03-26-core-respect-agent-permission-configuration-for-todowrite-tool|Core
  Respect agent permission configuration for todowrite tool]]'
- '[[Changes/Claude Code/2026-03-27-fixed-official-marketplace-plugin-scripts-failing-with-permission-denied-on-maco|Fixed
  official marketplace plugin scripts failing…]]'
source_release: '[[Releases/Dify/dify-2026-03-27-1-13-3-github-302258183-3ff73e84|dify-2026-03-27-1-13-3-github-302258183-3ff73e84]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in 1.13.3
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in 1.13.3

**Dify** · 2026-03-27 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.13.3) · from [[Releases/Dify/dify-2026-03-27-1-13-3-github-302258183-3ff73e84|v1.13.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> > The Sandbox image used by Dify v1.13.3 expects the following Python and Node.js paths.

> > If you upgraded from an older Docker Compose deployment and already have `docker/volumes/sandbox/conf/config.yaml`, update it on the host machine:

> > Do not edit the file inside the sandbox container. The directory `docker/volumes/sandbox/conf` is mounted into the container as `/conf`, so host changes persist after container restarts.

> test: migrate dataset permission tests to testcontainers by @Desel72 in https://github.com/langgenius/dify/pull/33906

> fix(sdk): patch flatted vulnerability in nodejs client lockfile by @lyzno1 in https://github.com/langgenius/dify/pull/33996

> chore: bump Dify to 1.13.3 and sandbox to 0.2.13 by @laipz8200 in https://github.com/langgenius/dify/pull/34079

Source: https://github.com/langgenius/dify/releases/tag/1.13.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-03-27-refactor-workspace-optimize-workspaces-plan-resolution-for-saas-and-enterprise-w|refactor(workspace): optimize /workspaces plan resolution for SaaS and enterprise…]] · Enterprise and Administration
- [[Changes/Dify/2026-03-27-3-pricing-model-changes-in-1-13-3|3 Pricing Model changes in 1.13.3]] · Pricing Model
- [[Changes/Dify/2026-03-27-6-apps-and-integrations-changes-in-1-13-3|6 Apps and Integrations changes in 1.13.3]] · Apps and Integrations
- [[Changes/Dify/2026-03-27-3-interface-experience-changes-in-1-13-3|3 Interface Experience changes in 1.13.3]] · Interface Experience
- [[Changes/Dify/2026-03-27-test-workflow-reorganize-specs-into-tests-and-align-with-shared-test-infrastruct|test(workflow): reorganize specs into tests and align with shared test infrastructure]] · Collaboration
- [[Changes/Dify/2026-03-27-feat-workflow-add-selection-context-menu-helpers-and-integrate-with-context-menu|feat(workflow): add selection context menu helpers and integrate with context menu…]] · Context Window
- [[Changes/Dify/2026-03-27-2-editor-experience-changes-in-1-13-3|2 Editor Experience changes in 1.13.3]] · Editor Experience
- [[Changes/Dify/2026-03-27-7-model-support-changes-in-1-13-3|7 Model Support changes in 1.13.3]] · Model Support
- [[Changes/Dify/2026-03-27-4-files-and-data-changes-in-1-13-3|4 Files and Data changes in 1.13.3]] · Files and Data
- [[Changes/Dify/2026-03-27-4-agent-mode-changes-in-1-13-3|4 Agent Mode changes in 1.13.3]] · Agent Mode
- [[Changes/Dify/2026-03-27-2-account-and-access-changes-in-1-13-3|2 Account and Access changes in 1.13.3]] · Account and Access
- [[Changes/Dify/2026-03-27-2-reliability-and-performance-changes-in-1-13-3|2 Reliability and Performance changes in 1.13.3]] · Reliability and Performance
- [[Changes/Dify/2026-03-27-152-other-changes-in-1-13-3|152 other changes in 1.13.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-27 · Claude Code · [[Changes/Claude Code/2026-03-27-fixed-official-marketplace-plugin-scripts-failing-with-permission-denied-on-maco|Fixed official marketplace plugin scripts failing…]]
- Later: 2026-03-27 · Open WebUI · [[Changes/Open WebUI/2026-03-27-terminal-server-connection-security-terminal-server-verification-and-policy-savi|🔒 Terminal server connection security. Terminal server verification and policy…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-03-27-c42571&body=Card%3A%20Changes%2FDify%2F2026-03-27-6-safety-and-privacy-changes-in-1-13-3.md%0ACard%20ID%3A%20dify-2026-03-27-c42571%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.13.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->