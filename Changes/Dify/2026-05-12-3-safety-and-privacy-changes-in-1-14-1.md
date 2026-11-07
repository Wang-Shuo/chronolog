---
card_id: dify-2026-05-12-7cf47b
date: '2026-05-12'
description: 'Dify · 2026-05-12 · Safety and Privacy: 3 changes in v1.14.1 - Security
  hardening, workflow stability, and cleaner self-hosted deployments — v1.14.1 is
  a patch…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2114
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b3313ad06119756177c7d2e7500ebbcf0c3da8df8b37547aee6614188a781477
product: dify
product_name: Dify
record:
  card_id: dify-2026-05-12-7cf47b
  comparison: ''
  date: '2026-05-12'
  description: 'Dify — v1.14.1 - Security hardening, workflow stability, and cleaner
    self-hosted deployments: 3 Safety and Privacy changes'
  evidence:
  - quote: v1.14.1 is a patch release focused on security hardening, workflow and
      knowledge-base stability, deployment cleanup, and continued UI platform migration
      after v1.14.0.
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  - quote: '**Dependency security** — upgraded LiteLLM for CVE-2026-42208 and refreshed
      several backend dependencies, including `urllib3`, `gunicorn`, `gitpython`,
      `mako`, Google SDK packages, storage libraries, and OpenTelemetry exporter packages.
      Thanks @crazywoola in [#35953](https://github.com/langgenius/dify/pull/35953),
      [#35779](https://github.com/langgenius/dify/pull/35779), [#35791](https://github.com/langgenius/dify/pull/35791),
      [#35863](https://github.com/langgenius/dify/pull/35863), [#35864](https://github.com/langgenius/dify/pull/35864),
      [#35958](https://github.com/langgenius/dify/pull/35958), [#36011](https://github.com/langgenius/dify/pull/36011),
      [#36012](https://github.com/langgenius/dify/pull/36012), [#36013](https://github.com/langgenius/dify/pull/36013),
      [#36017](https://github.com/langgenius/dify/pull/36017), and [#36050](https://github.com/langgenius/dify/pull/36050).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  - quote: 'test: migrate plugin permission tests to testcontainers by @escape0707
      in https://github.com/langgenius/dify/pull/35884'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 3-safety-and-privacy-changes-in-1-14-1
  source_release: dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in 1.14.1
  type: change
related_changes:
- '[[Changes/OpenCode/2026-05-10-core-read-tool-permission-rules-now-match-worktree-relative-paths-so-read-allowl|Core
  Read tool permission rules now match worktree-relative paths, so read…]]'
- '[[Changes/Claude Code/2026-05-11-fixed-skill-name-permission-rules-the-wildcard-form-now-works-as-a-prefix-match|Fixed
  Skill(name ) permission rules]]'
- '[[Changes/GitHub Copilot CLI/2026-05-11-sessions-with-extension-permission-prompts-can-be-resumed-without-a-session-file|Sessions
  with extension permission prompts can be resumed without…]]'
source_release: '[[Releases/Dify/dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e|dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in 1.14.1
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in 1.14.1

**Dify** · 2026-05-12 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.14.1) · from [[Releases/Dify/dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e|v1.14.1 - Security hardening, workflow stability, and cleaner self-hosted deployments]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> v1.14.1 is a patch release focused on security hardening, workflow and knowledge-base stability, deployment cleanup, and continued UI platform migration after v1.14.0.

> **Dependency security** — upgraded LiteLLM for CVE-2026-42208 and refreshed several backend dependencies, including `urllib3`, `gunicorn`, `gitpython`, `mako`, Google SDK packages, storage libraries, and OpenTelemetry exporter packages. Thanks @crazywoola in [#35953](https://github.com/langgenius/dify/pull/35953), [#35779](https://github.com/langgenius/dify/pull/35779), [#35791](https://github.com/langgenius/dify/pull/35791), [#35863](https://github.com/langgenius/dify/pull/35863), [#35864](https://github.com/langgenius/dify/pull/35864), [#35958](https://github.com/langgenius/dify/pull/35958), [#36011](https://github.com/langgenius/dify/pull/36011), [#36012](https://github.com/langgenius/dify/pull/36012), [#36013](https://github.com/langgenius/dify/pull/36013), [#36017](https://github.com/langgenius/dify/pull/36017), and [#36050](https://github.com/langgenius/dify/pull/36050).

> test: migrate plugin permission tests to testcontainers by @escape0707 in https://github.com/langgenius/dify/pull/35884

Source: https://github.com/langgenius/dify/releases/tag/1.14.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-05-12-2-editor-experience-changes-in-1-14-1|2 Editor Experience changes in 1.14.1]] · Editor Experience
- [[Changes/Dify/2026-05-12-2-enterprise-and-administration-changes-in-1-14-1|2 Enterprise and Administration changes in 1.14.1]] · Enterprise and Administration
- [[Changes/Dify/2026-05-12-document-indexing-skip-empty-documents-before-vector-embedding-and-validate-miss|Document indexing — skip empty documents before vector embedding and validate…]] · Files and Data
- [[Changes/Dify/2026-05-12-refactor-web-migrate-workflow-panel-context-menu-primitive-by-lyzno1-in-https-gi|refactor(web): migrate workflow panel context menu primitive]] · Context Window
- [[Changes/Dify/2026-05-12-accessibility-and-semantics-improved-web-accessibility-removed-unnecessary-data|Accessibility and semantics]] · Accessibility and Localization
- [[Changes/Dify/2026-05-12-audio-and-transcript-behavior-explicitly-resume-audiocontext-and-play-audio-on-f|Audio and transcript behavior]] · Voice and Audio
- [[Changes/Dify/2026-05-12-2-model-support-changes-in-1-14-1|2 Model Support changes in 1.14.1]] · Model Support
- [[Changes/Dify/2026-05-12-refactor-web-migrate-subscription-create-modal-to-dialog-by-lyzno1-in-https-gith|refactor(web): migrate subscription create modal to dialog]] · Pricing Model
- [[Changes/Dify/2026-05-12-chore-web-refresh-agent-skills-by-hyoban-in-https-github-com-langgenius-dify-pul|chore(web): refresh agent skills]] · Agent Mode
- [[Changes/Dify/2026-05-12-4-apps-and-integrations-changes-in-1-14-1|4 Apps and Integrations changes in 1.14.1]] · Apps and Integrations
- [[Changes/Dify/2026-05-12-human-input-exposed-selected-action-values-for-human-in-the-loop-flows-thanks-bl|Human input — exposed selected action values for Human-in-the-loop flows]] · Automation and Scheduling
- [[Changes/Dify/2026-05-12-refactor-auth-update-oauth-button-and-settings-modal-for-improved-state-manageme|refactor(auth): update OAuth button and settings modal for improved state management…]] · Account and Access
- [[Changes/Dify/2026-05-12-workflow-stability-restored-workflow-version-loading-through-the-backend-api-fix|Workflow stability — restored workflow-version loading through the backend API…]] · Reliability and Performance
- [[Changes/Dify/2026-05-12-8-interface-experience-changes-in-1-14-1|8 Interface Experience changes in 1.14.1]] · Interface Experience
- [[Changes/Dify/2026-05-12-112-other-changes-in-1-14-1|112 other changes in 1.14.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-11 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-11-sessions-with-extension-permission-prompts-can-be-resumed-without-a-session-file|Sessions with extension permission prompts can be resumed without…]]
- Later: 2026-05-12 · Gemini CLI · [[Changes/Gemini CLI/2026-05-12-3-safety-and-privacy-changes-in-v0-42-0|3 Safety and Privacy changes in v0.42.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-05-12-7cf47b&body=Card%3A%20Changes%2FDify%2F2026-05-12-3-safety-and-privacy-changes-in-1-14-1.md%0ACard%20ID%3A%20dify-2026-05-12-7cf47b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.14.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->