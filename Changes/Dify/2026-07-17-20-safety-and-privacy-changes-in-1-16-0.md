---
card_id: dify-2026-07-17-0f07d5
date: '2026-07-17'
description: 'Dify · 2026-07-17 · Safety and Privacy: 20 changes in v1.16.0 — Today,
  we are launching Dify Agent. Like other leading agents, it runs in a Linux sandbox.
  This…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2180
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 54e13d53967d016f2e1a00dd4f0bb63d239aab934c013762f0ae504d3a05a548
product: dify
product_name: Dify
record:
  card_id: dify-2026-07-17-0f07d5
  comparison: ''
  date: '2026-07-17'
  description: 'Dify — v1.16.0: 20 Safety and Privacy changes'
  evidence:
  - quote: 'Today, we are launching Dify Agent. Like other leading agents, it runs
      in a Linux sandbox. This release includes:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: We also provide an agent that helps you build Dify Agents. Through conversation,
      it can configure the Linux sandbox environment, install required packages, and
      create new Skills and files that your Dify Agent can use later.
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'Fixed editor permission issues: editors can now view logs, no longer query
      billing subscriptions, and can no longer manage members'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: Fixed plugin provider cache stampedes, marketplace installation callbacks,
      and plugin permission settings
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'This release includes several security hardening fixes, some of which
      were addressed after the 1.16.0-rc1 release:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '**SQL injection**: Closed a SQL injection vulnerability and enhanced SQL
      query safety with metadata key validation'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '**Sandbox enforcement**: Chatflow API now checks workflow_id and sandbox
      plan; sandbox plan will not execute special workflows'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `SHELLCTL_ENABLE_PATH_ISOLATION` | `true` | `docker/envs/core-services/local-sandbox.env.example`
      | Enable path isolation in shellctl |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'New services: `agent_backend` (`langgenius/dify-agent-backend:1.16.0`)
      and `local_sandbox` (`langgenius/dify-agent-local-sandbox:1.16.0`)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'chore(i18n): update role management permission keys for multiple languages
      by @WTW0313 in https://github.com/langgenius/dify/pull/38186'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'fix: update documentation links in permission set and role modals by @WTW0313
      in https://github.com/langgenius/dify/pull/38188'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat: support dataset permission migrate to rbac by @fatelei in https://github.com/langgenius/dify/pull/38166'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'fix: debug plugin permission setting not work by @hjlarry in https://github.com/langgenius/dify/pull/38197'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat(api): add sandbox info endpoint for Agent App conversations by @linw1995
      in https://github.com/langgenius/dify/pull/38390'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'chore: update editor permission by @fatelei in https://github.com/langgenius/dify/pull/38505'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat: ee agent sandbox support by @wylswz in https://github.com/langgenius/dify/pull/38528'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'chore: sandbox plan should not execution special workflow by @hjlarry
      in https://github.com/langgenius/dify/pull/38662'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test: use sqlite3 session in test_credential_permission_service by @asukaminato0721
      in https://github.com/langgenius/dify/pull/38711'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat: when knowledge permission is all team need update rbac setttings
      by @fatelei in https://github.com/langgenius/dify/pull/38911'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'chore: chatflow api should check workflow_id and sandbox plan by @hjlarry
      in https://github.com/langgenius/dify/pull/38892'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 20-safety-and-privacy-changes-in-1-16-0
  source_release: dify-2026-07-17-1-16-0-github-355594285-636849e9
  source_type: github_releases
  theme: safety-privacy
  title: 20 Safety and Privacy changes in 1.16.0
  type: change
related_changes:
- '[[Changes/Lovable/2026-07-16-choose-which-wiz-policies-run-during-security-scans|Choose
  which Wiz policies run during security scans]]'
- '[[Changes/Raycast/2026-07-16-apple-shortcuts-fixed-running-shortcuts-requiring-already-provided-automation-pe|Apple
  Shortcuts: Fixed running shortcuts requiring already provided automation permission]]'
- '[[Changes/Claude Code/2026-07-17-3-safety-and-privacy-changes-in-v2-1-212|3 Safety
  and Privacy changes in v2.1.212]]'
source_release: '[[Releases/Dify/dify-2026-07-17-1-16-0-github-355594285-636849e9|dify-2026-07-17-1-16-0-github-355594285-636849e9]]'
source_type: github_releases
theme: safety-privacy
title: 20 Safety and Privacy changes in 1.16.0
type: change
---

<!-- chronolog:begin region="header" -->
# 20 Safety and Privacy changes in 1.16.0

**Dify** · 2026-07-17 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.16.0) · from [[Releases/Dify/dify-2026-07-17-1-16-0-github-355594285-636849e9|v1.16.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Today, we are launching Dify Agent. Like other leading agents, it runs in a Linux sandbox. This release includes:

> We also provide an agent that helps you build Dify Agents. Through conversation, it can configure the Linux sandbox environment, install required packages, and create new Skills and files that your Dify Agent can use later.

> Fixed editor permission issues: editors can now view logs, no longer query billing subscriptions, and can no longer manage members

> Fixed plugin provider cache stampedes, marketplace installation callbacks, and plugin permission settings

> This release includes several security hardening fixes, some of which were addressed after the 1.16.0-rc1 release:

> **SQL injection**: Closed a SQL injection vulnerability and enhanced SQL query safety with metadata key validation

> **Sandbox enforcement**: Chatflow API now checks workflow_id and sandbox plan; sandbox plan will not execute special workflows

> | `SHELLCTL_ENABLE_PATH_ISOLATION` | `true` | `docker/envs/core-services/local-sandbox.env.example` | Enable path isolation in shellctl |

> New services: `agent_backend` (`langgenius/dify-agent-backend:1.16.0`) and `local_sandbox` (`langgenius/dify-agent-local-sandbox:1.16.0`)

> chore(i18n): update role management permission keys for multiple languages by @WTW0313 in https://github.com/langgenius/dify/pull/38186

> fix: update documentation links in permission set and role modals by @WTW0313 in https://github.com/langgenius/dify/pull/38188

> feat: support dataset permission migrate to rbac by @fatelei in https://github.com/langgenius/dify/pull/38166

> fix: debug plugin permission setting not work by @hjlarry in https://github.com/langgenius/dify/pull/38197

> feat(api): add sandbox info endpoint for Agent App conversations by @linw1995 in https://github.com/langgenius/dify/pull/38390

> chore: update editor permission by @fatelei in https://github.com/langgenius/dify/pull/38505

> feat: ee agent sandbox support by @wylswz in https://github.com/langgenius/dify/pull/38528

> chore: sandbox plan should not execution special workflow by @hjlarry in https://github.com/langgenius/dify/pull/38662

> test: use sqlite3 session in test_credential_permission_service by @asukaminato0721 in https://github.com/langgenius/dify/pull/38711

> feat: when knowledge permission is all team need update rbac setttings by @fatelei in https://github.com/langgenius/dify/pull/38911

> chore: chatflow api should check workflow_id and sandbox plan by @hjlarry in https://github.com/langgenius/dify/pull/38892

Source: https://github.com/langgenius/dify/releases/tag/1.16.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-07-17-agent-app-enters-open-beta-and-is-now-enabled-by-default-for-all-users-it-introd|Agent App enters open beta and is now enabled by default for all users]] · Safety and Privacy
- [[Changes/Dify/2026-07-17-16-context-window-changes-in-1-16-0|16 Context Window changes in 1.16.0]] · Context Window
- [[Changes/Dify/2026-07-17-perf-memory-batch-load-message-files-in-tokenbuffermemory-to-remove-n-1-queries|perf(memory): batch-load message files in TokenBufferMemory to remove N+1 queries]] · Memory and Personalization
- [[Changes/Dify/2026-07-17-8-account-and-access-changes-in-1-16-0|8 Account and Access changes in 1.16.0]] · Account and Access
- [[Changes/Dify/2026-07-17-4-editor-experience-changes-in-1-16-0|4 Editor Experience changes in 1.16.0]] · Editor Experience
- [[Changes/Dify/2026-07-17-3-voice-and-audio-changes-in-1-16-0|3 Voice and Audio changes in 1.16.0]] · Voice and Audio
- [[Changes/Dify/2026-07-17-4-collaboration-changes-in-1-16-0|4 Collaboration changes in 1.16.0]] · Collaboration
- [[Changes/Dify/2026-07-17-3-developer-workflow-changes-in-1-16-0|3 Developer Workflow changes in 1.16.0]] · Developer Workflow
- [[Changes/Dify/2026-07-17-24-apps-and-integrations-changes-in-1-16-0|24 Apps and Integrations changes in 1.16.0]] · Apps and Integrations
- [[Changes/Dify/2026-07-17-2-automation-and-scheduling-changes-in-1-16-0|2 Automation and Scheduling changes in 1.16.0]] · Automation and Scheduling
- [[Changes/Dify/2026-07-17-2-interface-experience-changes-in-1-16-0|2 Interface Experience changes in 1.16.0]] · Interface Experience
- [[Changes/Dify/2026-07-17-2-files-and-data-changes-in-1-16-0|2 Files and Data changes in 1.16.0]] · Files and Data
- [[Changes/Dify/2026-07-17-12-model-support-changes-in-1-16-0|12 Model Support changes in 1.16.0]] · Model Support
- [[Changes/Dify/2026-07-17-chore-improve-workflow-generator-accessibility-and-api-contracts-by-crazywoola-i|chore: Improve workflow generator accessibility and API contracts]] · Accessibility and Localization
- [[Changes/Dify/2026-07-17-2-enterprise-and-administration-changes-in-1-16-0|2 Enterprise and Administration changes in 1.16.0]] · Enterprise and Administration
- [[Changes/Dify/2026-07-17-3-reliability-and-performance-changes-in-1-16-0|3 Reliability and Performance changes in 1.16.0]] · Reliability and Performance
- [[Changes/Dify/2026-07-17-64-agent-mode-changes-in-1-16-0|64 Agent Mode changes in 1.16.0]] · Agent Mode
- [[Changes/Dify/2026-07-17-5-pricing-model-changes-in-1-16-0|5 Pricing Model changes in 1.16.0]] · Pricing Model
- [[Changes/Dify/2026-07-17-237-other-changes-in-1-16-0|237 other changes in 1.16.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-17 · Claude Code · [[Changes/Claude Code/2026-07-17-3-safety-and-privacy-changes-in-v2-1-212|3 Safety and Privacy changes in v2.1.212]]
- Later: 2026-07-18 · Claude Code · [[Changes/Claude Code/2026-07-18-9-safety-and-privacy-changes-in-v2-1-214|9 Safety and Privacy changes in v2.1.214]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-07-17-0f07d5&body=Card%3A%20Changes%2FDify%2F2026-07-17-20-safety-and-privacy-changes-in-1-16-0.md%0ACard%20ID%3A%20dify-2026-07-17-0f07d5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.16.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->