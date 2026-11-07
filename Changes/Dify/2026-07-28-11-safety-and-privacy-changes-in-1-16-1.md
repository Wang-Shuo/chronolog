---
card_id: dify-2026-07-28-14a430
date: '2026-07-28'
description: 'Dify · 2026-07-28 · Safety and Privacy: 11 changes in v1.16.1 - Bug
  Fixes and Security Enhancements — Fixed permission selector semantics (#39269)'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2191
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 529ae0d77c4d9aa581282b79368ecf7c3e11b060f75807b60509ca2bb78e017b
product: dify
product_name: Dify
record:
  card_id: dify-2026-07-28-14a430
  comparison: ''
  date: '2026-07-28'
  description: 'Dify — v1.16.1 - Bug Fixes and Security Enhancements: 11 Safety and
    Privacy changes'
  evidence:
  - quote: Fixed permission selector semantics (#39269)
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: The Agent local sandbox now runs behind a dedicated Squid forward proxy
      with strict ACL rules, preventing the sandbox from reaching internal services
      directly. Only the `/files/` endpoint on the API and `/agent-stub/` on agent_backend
      are permitted, both protected with short-lived access tokens. This significantly
      reduces the blast radius of arbitrary code execution in the agent sandbox. (#39544)
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: Patched React Server Components DoS vulnerability (#39539)
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: '**Agent sandbox network isolation**: `local_sandbox` is moved off the
      `default` network to dedicated `agent_sandbox_network` + `local_sandbox_proxy_network`.
      A new `agent_ssrf_proxy` service (Squid) is added.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'fix(web): restore permission selector semantics by @lyzno1 in https://github.com/langgenius/dify/pull/39269'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'chore: when dataset permission is not all team, update rbac config to…
      by @fatelei in https://github.com/langgenius/dify/pull/39227'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'refactor(web): remove permission catalog service hooks by @lyzno1 in https://github.com/langgenius/dify/pull/39342'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'chore: Update permission tip across i18n locales by @WTW0313 in https://github.com/langgenius/dify/pull/39406'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'feat: gate cloud analytics behind cookie consent by @CodingOnStar in https://github.com/langgenius/dify/pull/39408'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'feat: gate agent management behind the agent.manage permission by @GareArc
      in https://github.com/langgenius/dify/pull/39330'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'feat(agent): add a squid proxy for agent sandbox by @wylswz in https://github.com/langgenius/dify/pull/39544'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 11-safety-and-privacy-changes-in-1-16-1
  source_release: dify-2026-07-28-1-16-1-github-360820489-855a9365
  source_type: github_releases
  theme: safety-privacy
  title: 11 Safety and Privacy changes in 1.16.1
  type: change
related_changes:
- '[[Changes/Lovable/2026-07-23-payments-is-always-visible-in-your-project|Payments
  is always visible in your project]]'
- '[[Changes/Claude Code/2026-07-24-2-safety-and-privacy-changes-in-v2-1-219|2 Safety
  and Privacy changes in v2.1.219]]'
- '[[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety
  and Privacy changes in v0.11.0]]'
source_release: '[[Releases/Dify/dify-2026-07-28-1-16-1-github-360820489-855a9365|dify-2026-07-28-1-16-1-github-360820489-855a9365]]'
source_type: github_releases
theme: safety-privacy
title: 11 Safety and Privacy changes in 1.16.1
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Safety and Privacy changes in 1.16.1

**Dify** · 2026-07-28 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.16.1) · from [[Releases/Dify/dify-2026-07-28-1-16-1-github-360820489-855a9365|v1.16.1 - Bug Fixes and Security Enhancements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed permission selector semantics (#39269)

> The Agent local sandbox now runs behind a dedicated Squid forward proxy with strict ACL rules, preventing the sandbox from reaching internal services directly. Only the `/files/` endpoint on the API and `/agent-stub/` on agent_backend are permitted, both protected with short-lived access tokens. This significantly reduces the blast radius of arbitrary code execution in the agent sandbox. (#39544)

> Patched React Server Components DoS vulnerability (#39539)

> **Agent sandbox network isolation**: `local_sandbox` is moved off the `default` network to dedicated `agent_sandbox_network` + `local_sandbox_proxy_network`. A new `agent_ssrf_proxy` service (Squid) is added.

> fix(web): restore permission selector semantics by @lyzno1 in https://github.com/langgenius/dify/pull/39269

> chore: when dataset permission is not all team, update rbac config to… by @fatelei in https://github.com/langgenius/dify/pull/39227

> refactor(web): remove permission catalog service hooks by @lyzno1 in https://github.com/langgenius/dify/pull/39342

> chore: Update permission tip across i18n locales by @WTW0313 in https://github.com/langgenius/dify/pull/39406

> feat: gate cloud analytics behind cookie consent by @CodingOnStar in https://github.com/langgenius/dify/pull/39408

> feat: gate agent management behind the agent.manage permission by @GareArc in https://github.com/langgenius/dify/pull/39330

> feat(agent): add a squid proxy for agent sandbox by @wylswz in https://github.com/langgenius/dify/pull/39544

Source: https://github.com/langgenius/dify/releases/tag/1.16.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-07-28-6-model-support-changes-in-1-16-1|6 Model Support changes in 1.16.1]] · Model Support
- [[Changes/Dify/2026-07-28-refactor-agents-simplify-repository-context-by-lyzno1-in-https-github-com-langge|refactor(agents): simplify repository context]] · Context Window
- [[Changes/Dify/2026-07-28-3-files-and-data-changes-in-1-16-1|3 Files and Data changes in 1.16.1]] · Files and Data
- [[Changes/Dify/2026-07-28-3-collaboration-changes-in-1-16-1|3 Collaboration changes in 1.16.1]] · Collaboration
- [[Changes/Dify/2026-07-28-2-accessibility-and-localization-changes-in-1-16-1|2 Accessibility and Localization changes in 1.16.1]] · Accessibility and Localization
- [[Changes/Dify/2026-07-28-10-interface-experience-changes-in-1-16-1|10 Interface Experience changes in 1.16.1]] · Interface Experience
- [[Changes/Dify/2026-07-28-4-developer-workflow-changes-in-1-16-1|4 Developer Workflow changes in 1.16.1]] · Developer Workflow
- [[Changes/Dify/2026-07-28-lightweight-recent-apps-endpoint-new-get-console-api-apps-recent-endpoint-reduce|Lightweight recent apps endpoint]] · Reliability and Performance
- [[Changes/Dify/2026-07-28-feat-web-locate-workflow-nodes-by-node-id-in-the-workflow-editor-by-ruanimal-in|feat(web): locate workflow nodes by node_id in the workflow editor]] · Editor Experience
- [[Changes/Dify/2026-07-28-6-account-and-access-changes-in-1-16-1|6 Account and Access changes in 1.16.1]] · Account and Access
- [[Changes/Dify/2026-07-28-test-use-sqlite-sessions-in-core-memory-by-asukaminato0721-in-https-github-com-l|test: use SQLite sessions in core memory]] · Memory and Personalization
- [[Changes/Dify/2026-07-28-you-can-now-click-a-node-id-in-workflow-run-logs-or-error-messages-to-locate-and|Click a node_id in workflow run logs or error messages to locate and highlight…]] · Files and Data
- [[Changes/Dify/2026-07-28-10-apps-and-integrations-changes-in-1-16-1|10 Apps and Integrations changes in 1.16.1]] · Apps and Integrations
- [[Changes/Dify/2026-07-28-returned-400-instead-of-500-when-file-field-is-missing-from-audio-to-text-endpoi|Returned 400 instead of 500 when file field is missing from audio-to-text…]] · Voice and Audio
- [[Changes/Dify/2026-07-28-24-agent-mode-changes-in-1-16-1|24 Agent Mode changes in 1.16.1]] · Agent Mode
- [[Changes/Dify/2026-07-28-2-pricing-model-changes-in-1-16-1|2 Pricing Model changes in 1.16.1]] · Pricing Model
- [[Changes/Dify/2026-07-28-2-enterprise-and-administration-changes-in-1-16-1|2 Enterprise and Administration changes in 1.16.1]] · Enterprise and Administration
- [[Changes/Dify/2026-07-28-167-other-changes-in-1-16-1|167 other changes in 1.16.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-27 · Open WebUI · [[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety and Privacy changes in v0.11.0]]
- Later: 2026-07-28 · Gemini CLI · [[Changes/Gemini CLI/2026-07-28-fix-a2a-server-enforce-workspace-trust-and-task-isolation-to-prevent-rce-by-luis|fix(a2a-server): enforce workspace trust and task isolation to prevent RCE]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-07-28-14a430&body=Card%3A%20Changes%2FDify%2F2026-07-28-11-safety-and-privacy-changes-in-1-16-1.md%0ACard%20ID%3A%20dify-2026-07-28-14a430%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.16.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->