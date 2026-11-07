---
card_id: dify-2026-05-12-ff90b8
date: '2026-05-12'
description: 'Dify · 2026-05-12 · Interface Experience: 8 changes in v1.14.1 - Security
  hardening, workflow stability, and cleaner self-hosted deployments — **Workflow…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2585
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1d78fa9c783c595c152e24598feb0b0b358cf48fc5c38137bbf6e29b60eb2a32
product: dify
product_name: Dify
record:
  card_id: dify-2026-05-12-ff90b8
  comparison: ''
  date: '2026-05-12'
  description: 'Dify — v1.14.1 - Security hardening, workflow stability, and cleaner
    self-hosted deployments: 8 Interface Experience changes'
  evidence:
  - quote: '**Workflow authoring polish** — fixed variable reference picker behavior
      for sub-variables, workflow node title overflow, condition operator popovers,
      workflow checklist semantics, and KB metadata filter field selection. Thanks
      @iamjoel, @hjlarry, @lyzno1, and @shawny011717 in [#35732](https://github.com/langgenius/dify/pull/35732),
      [#35740](https://github.com/langgenius/dify/pull/35740), [#35828](https://github.com/langgenius/dify/pull/35828),
      [#36006](https://github.com/langgenius/dify/pull/36006), and [#34149](https://github.com/langgenius/dify/pull/34149).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  - quote: '**Knowledge-base image rendering** — fixed image rendering failures in
      the knowledge base. Thanks @FFXN in [#35914](https://github.com/langgenius/dify/pull/35914).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  - quote: '**Dataset metadata filters** — preserve dataset metadata filters in API
      paths and fix KB metadata filter field selection. Thanks @princepal9120 and
      @shawny011717 in [#35700](https://github.com/langgenius/dify/pull/35700) and
      [#34149](https://github.com/langgenius/dify/pull/34149).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  - quote: '**Overlay and navigation reliability** — restored app navigation create
      submenu interaction, fixed transfer workspace dropdown display, normalized overlay
      control, aligned Tailwind v4 CSS migration, forwarded CSP nonce to the theme
      script, and aligned tag filter dropdown icons. Thanks @hjlarry, @iamjoel, and
      @lyzno1 in [#35681](https://github.com/langgenius/dify/pull/35681), [#35876](https://github.com/langgenius/dify/pull/35876),
      [#35832](https://github.com/langgenius/dify/pull/35832), [#35829](https://github.com/langgenius/dify/pull/35829),
      [#35960](https://github.com/langgenius/dify/pull/35960), and [#36041](https://github.com/langgenius/dify/pull/36041).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  - quote: 'refactor(web): migrate rich tooltip overlays by @lyzno1 in https://github.com/langgenius/dify/pull/35675'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  - quote: 'refactor(web): migrate legacy tooltip to infotip by @lyzno1 in https://github.com/langgenius/dify/pull/35774'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  - quote: 'refactor(web): migrate workflow node actions menu by @lyzno1 in https://github.com/langgenius/dify/pull/35785'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  - quote: 'refactor(web): migrate legacy tooltip callers by @lyzno1 in https://github.com/langgenius/dify/pull/35961'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 8-interface-experience-changes-in-1-14-1
  source_release: dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e
  source_type: github_releases
  theme: interface-experience
  title: 8 Interface Experience changes in 1.14.1
  type: change
related_changes:
- '[[Changes/OpenCode/2026-05-09-3-interface-experience-changes-in-v1-14-44-2|3 Interface
  Experience changes in v1.14.44 + 2]]'
- '[[Changes/Open WebUI/2026-05-10-2-interface-experience-changes-in-v0-9-5|2 Interface
  Experience changes in v0.9.5]]'
- '[[Changes/Claude Code/2026-05-11-added-transcript-view-navigation-for-keyboard-shortcuts-to-jump-between-user-pro|Added
  transcript view navigation]]'
source_release: '[[Releases/Dify/dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e|dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e]]'
source_type: github_releases
theme: interface-experience
title: 8 Interface Experience changes in 1.14.1
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Interface Experience changes in 1.14.1

**Dify** · 2026-05-12 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.14.1) · from [[Releases/Dify/dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e|v1.14.1 - Security hardening, workflow stability, and cleaner self-hosted deployments]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Workflow authoring polish** — fixed variable reference picker behavior for sub-variables, workflow node title overflow, condition operator popovers, workflow checklist semantics, and KB metadata filter field selection. Thanks @iamjoel, @hjlarry, @lyzno1, and @shawny011717 in [#35732](https://github.com/langgenius/dify/pull/35732), [#35740](https://github.com/langgenius/dify/pull/35740), [#35828](https://github.com/langgenius/dify/pull/35828), [#36006](https://github.com/langgenius/dify/pull/36006), and [#34149](https://github.com/langgenius/dify/pull/34149).

> **Knowledge-base image rendering** — fixed image rendering failures in the knowledge base. Thanks @FFXN in [#35914](https://github.com/langgenius/dify/pull/35914).

> **Dataset metadata filters** — preserve dataset metadata filters in API paths and fix KB metadata filter field selection. Thanks @princepal9120 and @shawny011717 in [#35700](https://github.com/langgenius/dify/pull/35700) and [#34149](https://github.com/langgenius/dify/pull/34149).

> **Overlay and navigation reliability** — restored app navigation create submenu interaction, fixed transfer workspace dropdown display, normalized overlay control, aligned Tailwind v4 CSS migration, forwarded CSP nonce to the theme script, and aligned tag filter dropdown icons. Thanks @hjlarry, @iamjoel, and @lyzno1 in [#35681](https://github.com/langgenius/dify/pull/35681), [#35876](https://github.com/langgenius/dify/pull/35876), [#35832](https://github.com/langgenius/dify/pull/35832), [#35829](https://github.com/langgenius/dify/pull/35829), [#35960](https://github.com/langgenius/dify/pull/35960), and [#36041](https://github.com/langgenius/dify/pull/36041).

> refactor(web): migrate rich tooltip overlays by @lyzno1 in https://github.com/langgenius/dify/pull/35675

> refactor(web): migrate legacy tooltip to infotip by @lyzno1 in https://github.com/langgenius/dify/pull/35774

> refactor(web): migrate workflow node actions menu by @lyzno1 in https://github.com/langgenius/dify/pull/35785

> refactor(web): migrate legacy tooltip callers by @lyzno1 in https://github.com/langgenius/dify/pull/35961

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
- [[Changes/Dify/2026-05-12-4-apps-and-integrations-changes-in-1-14-1|4 Apps and Integrations changes in 1.14.1]] · Apps and Integrations
- [[Changes/Dify/2026-05-12-human-input-exposed-selected-action-values-for-human-in-the-loop-flows-thanks-bl|Human input — exposed selected action values for Human-in-the-loop flows]] · Automation and Scheduling
- [[Changes/Dify/2026-05-12-refactor-auth-update-oauth-button-and-settings-modal-for-improved-state-manageme|refactor(auth): update OAuth button and settings modal for improved state management…]] · Account and Access
- [[Changes/Dify/2026-05-12-workflow-stability-restored-workflow-version-loading-through-the-backend-api-fix|Workflow stability — restored workflow-version loading through the backend API…]] · Reliability and Performance
- [[Changes/Dify/2026-05-12-112-other-changes-in-1-14-1|112 other changes in 1.14.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-05-11 · Claude Code · [[Changes/Claude Code/2026-05-11-added-transcript-view-navigation-for-keyboard-shortcuts-to-jump-between-user-pro|Added transcript view navigation]]
- Later: 2026-05-12 · Gemini CLI · [[Changes/Gemini CLI/2026-05-12-test-evals-add-behavioral-eval-for-file-creation-and-write-file-tool-selection-b|test(evals): add behavioral eval for file creation and write_file tool selection]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-05-12-ff90b8&body=Card%3A%20Changes%2FDify%2F2026-05-12-8-interface-experience-changes-in-1-14-1.md%0ACard%20ID%3A%20dify-2026-05-12-ff90b8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.14.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->