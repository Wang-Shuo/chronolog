---
card_id: dify-2026-05-12-b0cd7a
date: '2026-05-12'
description: 'Dify · 2026-05-12 · Apps and Integrations: 4 changes in v1.14.1 - Security
  hardening, workflow stability, and cleaner self-hosted deployments — **Workflow…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2706
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6d60cb1da40c6840a8a74a81458b1b50703fba96866f07d3c9d435b12663462d
product: dify
product_name: Dify
record:
  card_id: dify-2026-05-12-b0cd7a
  comparison: ''
  date: '2026-05-12'
  description: 'Dify — v1.14.1 - Security hardening, workflow stability, and cleaner
    self-hosted deployments: 4 Apps and Integrations changes'
  evidence:
  - quote: '**Workflow execution correctness** — preserved single-run input variable
      types, fixed `structured_output_enabled` validation, fixed file-preview URL
      handling in node output display, and unblocked plugin model selector tools on
      v1.14.0 workflows. Thanks @Jingyi-Dify, @fatelei, @shawny011717, and @sawyer-shi
      in [#35710](https://github.com/langgenius/dify/pull/35710), [#35747](https://github.com/langgenius/dify/pull/35747),
      [#34150](https://github.com/langgenius/dify/pull/34150), and [#35794](https://github.com/langgenius/dify/pull/35794).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  - quote: '**Upload filename handling** — clean upload filenames parsed from URLs
      and avoid doubled dots when standardizing datasource file extensions. Thanks
      @jonathanchang31 and @Beandon13 in [#35706](https://github.com/langgenius/dify/pull/35706)
      and [#35808](https://github.com/langgenius/dify/pull/35808).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  - quote: '**Explore categories** — Explore recommended apps now support multiple
      configurable categories and adjustable category order. Thanks @hjlarry in [#35723](https://github.com/langgenius/dify/pull/35723).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  - quote: 'refactor(apps): simplify query state and debounce URL writes by @lyzno1
      in https://github.com/langgenius/dify/pull/36043'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 4-apps-and-integrations-changes-in-1-14-1
  source_release: dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in 1.14.1
  type: change
related_changes:
- '[[Changes/Cursor/2026-05-11-get-started-by-installing-the-integration-in-the-cursor-dashboard-learn-more-in|Get
  started by installing the integration in the Cursor dashboard]]'
- '[[Changes/GitHub Copilot CLI/2026-05-11-opentelemetry-output-aligns-with-genai-semantic-conventions-mcp-tool-calls-now-u|OpenTelemetry
  output aligns with GenAI semantic conventions]]'
- '[[Changes/Claude Code/2026-05-12-plugins-now-warn-when-a-default-component-folder-e-g-commands-is-silently-ignore|Plugins
  now warn when a default component folder (e.g. commands/) is silently…]]'
source_release: '[[Releases/Dify/dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e|dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in 1.14.1
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in 1.14.1

**Dify** · 2026-05-12 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.14.1) · from [[Releases/Dify/dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e|v1.14.1 - Security hardening, workflow stability, and cleaner self-hosted deployments]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Workflow execution correctness** — preserved single-run input variable types, fixed `structured_output_enabled` validation, fixed file-preview URL handling in node output display, and unblocked plugin model selector tools on v1.14.0 workflows. Thanks @Jingyi-Dify, @fatelei, @shawny011717, and @sawyer-shi in [#35710](https://github.com/langgenius/dify/pull/35710), [#35747](https://github.com/langgenius/dify/pull/35747), [#34150](https://github.com/langgenius/dify/pull/34150), and [#35794](https://github.com/langgenius/dify/pull/35794).

> **Upload filename handling** — clean upload filenames parsed from URLs and avoid doubled dots when standardizing datasource file extensions. Thanks @jonathanchang31 and @Beandon13 in [#35706](https://github.com/langgenius/dify/pull/35706) and [#35808](https://github.com/langgenius/dify/pull/35808).

> **Explore categories** — Explore recommended apps now support multiple configurable categories and adjustable category order. Thanks @hjlarry in [#35723](https://github.com/langgenius/dify/pull/35723).

> refactor(apps): simplify query state and debounce URL writes by @lyzno1 in https://github.com/langgenius/dify/pull/36043

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
- [[Changes/Dify/2026-05-12-3-safety-and-privacy-changes-in-1-14-1|3 Safety and Privacy changes in 1.14.1]] · Safety and Privacy
- [[Changes/Dify/2026-05-12-refactor-web-migrate-subscription-create-modal-to-dialog-by-lyzno1-in-https-gith|refactor(web): migrate subscription create modal to dialog]] · Pricing Model
- [[Changes/Dify/2026-05-12-chore-web-refresh-agent-skills-by-hyoban-in-https-github-com-langgenius-dify-pul|chore(web): refresh agent skills]] · Agent Mode
- [[Changes/Dify/2026-05-12-human-input-exposed-selected-action-values-for-human-in-the-loop-flows-thanks-bl|Human input — exposed selected action values for Human-in-the-loop flows]] · Automation and Scheduling
- [[Changes/Dify/2026-05-12-refactor-auth-update-oauth-button-and-settings-modal-for-improved-state-manageme|refactor(auth): update OAuth button and settings modal for improved state management…]] · Account and Access
- [[Changes/Dify/2026-05-12-workflow-stability-restored-workflow-version-loading-through-the-backend-api-fix|Workflow stability — restored workflow-version loading through the backend API…]] · Reliability and Performance
- [[Changes/Dify/2026-05-12-8-interface-experience-changes-in-1-14-1|8 Interface Experience changes in 1.14.1]] · Interface Experience
- [[Changes/Dify/2026-05-12-112-other-changes-in-1-14-1|112 other changes in 1.14.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-12 · Claude Code · [[Changes/Claude Code/2026-05-12-plugins-now-warn-when-a-default-component-folder-e-g-commands-is-silently-ignore|Plugins now warn when a default component folder (e.g. commands/) is silently…]]
- Later: 2026-05-12 · Gemini CLI · [[Changes/Gemini CLI/2026-05-12-5-apps-and-integrations-changes-in-v0-42-0|5 Apps and Integrations changes in v0.42.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-05-12-b0cd7a&body=Card%3A%20Changes%2FDify%2F2026-05-12-4-apps-and-integrations-changes-in-1-14-1.md%0ACard%20ID%3A%20dify-2026-05-12-b0cd7a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.14.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->