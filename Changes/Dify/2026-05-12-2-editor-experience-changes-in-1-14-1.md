---
card_id: dify-2026-05-12-12511f
date: '2026-05-12'
description: 'Dify · 2026-05-12 · Editor Experience: 2 changes in v1.14.1 - Security
  hardening, workflow stability, and cleaner self-hosted deployments — **Dify UI…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1155
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bad57d7303899527fc6f29d252cf40e81d9b39d06f99a36ae17cbd927530027b
product: dify
product_name: Dify
record:
  card_id: dify-2026-05-12-12511f
  comparison: ''
  date: '2026-05-12'
  description: 'Dify — v1.14.1 - Security hardening, workflow stability, and cleaner
    self-hosted deployments: 2 Editor Experience changes'
  evidence:
  - quote: '**Dify UI migration** — continued migration from legacy overlays, tooltips,
      drawers, selects, tags, and searchable pickers to `@langgenius/dify-ui` primitives,
      including new Drawer, Tabs, ToggleGroup, Autocomplete, and Combobox support.
      Thanks @lyzno1 and @CodingOnStar in [#35675](https://github.com/langgenius/dify/pull/35675),
      [#35715](https://github.com/langgenius/dify/pull/35715), [#35720](https://github.com/langgenius/dify/pull/35720),
      [#35721](https://github.com/langgenius/dify/pull/35721), [#35774](https://github.com/langgenius/dify/pull/35774),
      [#35785](https://github.com/langgenius/dify/pull/35785), [#35787](https://github.com/langgenius/dify/pull/35787),
      [#35792](https://github.com/langgenius/dify/pull/35792), [#35825](https://github.com/langgenius/dify/pull/35825),
      [#35868](https://github.com/langgenius/dify/pull/35868), [#35881](https://github.com/langgenius/dify/pull/35881),
      [#35892](https://github.com/langgenius/dify/pull/35892), [#35896](https://github.com/langgenius/dify/pull/35896),
      [#35917](https://github.com/langgenius/dify/pull/35917), [#35961](https://github.com/langgenius/dify/pull/35961),
      [#35962](https://github.com/langgenius/dify/pull/35962), [#35963](https://github.com/langgenius/dify/pull/35963),
      [#35965](https://github.com/langgenius/dify/pull/35965), [#35976](https://github.com/langgenius/dify/pull/35976),
      [#35982](https://github.com/langgenius/dify/pull/35982), and [#36066](https://github.com/langgenius/dify/pull/36066).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  - quote: 'feat: add dify-ui autocomplete and combobox by @lyzno1 in https://github.com/langgenius/dify/pull/35868'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 2-editor-experience-changes-in-1-14-1
  source_release: dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e
  source_type: github_releases
  theme: editor-experience
  title: 2 Editor Experience changes in 1.14.1
  type: change
related_changes:
- "[[Changes/Open WebUI/2026-05-10-url-parser-ssrf-bypass-url-validation-now-rejects-backslash-tab-cr-and-lf-charac|\U0001F6E1️
  URL parser SSRF bypass. URL validation now rejects backslash, tab, CR, and LF…]]"
- '[[Changes/OpenCode/2026-05-10-core-added-a-built-in-customize-opencode-skill-so-opencode-config-edits-are-less|Core
  Added a built-in customize-opencode skill so opencode config edits are less…]]'
- '[[Changes/Claude Code/2026-05-11-vscode-press-cmd-ctrl-shift-t-to-reopen-the-most-recently-closed-session-tab-con|VSCode
  Press Cmd/Ctrl+Shift+T to reopen the most recently closed session tab…]]'
source_release: '[[Releases/Dify/dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e|dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e]]'
source_type: github_releases
theme: editor-experience
title: 2 Editor Experience changes in 1.14.1
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Editor Experience changes in 1.14.1

**Dify** · 2026-05-12 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.14.1) · from [[Releases/Dify/dify-2026-05-12-1-14-1-github-321018473-9e9e1d9e|v1.14.1 - Security hardening, workflow stability, and cleaner self-hosted deployments]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Dify UI migration** — continued migration from legacy overlays, tooltips, drawers, selects, tags, and searchable pickers to `@langgenius/dify-ui` primitives, including new Drawer, Tabs, ToggleGroup, Autocomplete, and Combobox support. Thanks @lyzno1 and @CodingOnStar in [#35675](https://github.com/langgenius/dify/pull/35675), [#35715](https://github.com/langgenius/dify/pull/35715), [#35720](https://github.com/langgenius/dify/pull/35720), [#35721](https://github.com/langgenius/dify/pull/35721), [#35774](https://github.com/langgenius/dify/pull/35774), [#35785](https://github.com/langgenius/dify/pull/35785), [#35787](https://github.com/langgenius/dify/pull/35787), [#35792](https://github.com/langgenius/dify/pull/35792), [#35825](https://github.com/langgenius/dify/pull/35825), [#35868](https://github.com/langgenius/dify/pull/35868), [#35881](https://github.com/langgenius/dify/pull/35881), [#35892](https://github.com/langgenius/dify/pull/35892), [#35896](https://github.com/langgenius/dify/pull/35896), [#35917](https://github.com/langgenius/dify/pull/35917), [#35961](https://github.com/langgenius/dify/pull/35961), [#35962](https://github.com/langgenius/dify/pull/35962), [#35963](https://github.com/langgenius/dify/pull/35963), [#35965](https://github.com/langgenius/dify/pull/35965), [#35976](https://github.com/langgenius/dify/pull/35976), [#35982](https://github.com/langgenius/dify/pull/35982), and [#36066](https://github.com/langgenius/dify/pull/36066).

> feat: add dify-ui autocomplete and combobox by @lyzno1 in https://github.com/langgenius/dify/pull/35868

Source: https://github.com/langgenius/dify/releases/tag/1.14.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

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
- [[Changes/Dify/2026-05-12-8-interface-experience-changes-in-1-14-1|8 Interface Experience changes in 1.14.1]] · Interface Experience
- [[Changes/Dify/2026-05-12-112-other-changes-in-1-14-1|112 other changes in 1.14.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-05-11 · Claude Code · [[Changes/Claude Code/2026-05-11-vscode-press-cmd-ctrl-shift-t-to-reopen-the-most-recently-closed-session-tab-con|VSCode Press Cmd/Ctrl+Shift+T to reopen the most recently closed session tab…]]
- Later: 2026-05-12 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-12-read-only-gh-cli-commands-list-view-status-diff-etc-are-auto-approved-without-pr|Read-only gh CLI commands (list, view, status, diff, etc.) are auto-approved without…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-05-12-12511f&body=Card%3A%20Changes%2FDify%2F2026-05-12-2-editor-experience-changes-in-1-14-1.md%0ACard%20ID%3A%20dify-2026-05-12-12511f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.14.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->