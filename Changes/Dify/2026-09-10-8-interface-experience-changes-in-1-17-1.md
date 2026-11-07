---
card_id: dify-2026-09-10-2110b1
date: '2026-09-10'
description: 'Dify · 2026-09-10 · Interface Experience: 8 changes in v1.17.1 - Bug
  Fixes and Improvements — Plugin authors now have public profile pages at…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2706
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 83a77e844d842ed1ef3b37f98bc1b1aa63b4c0e83462e29f2b4d81c34906d983
product: dify
product_name: Dify
record:
  card_id: dify-2026-09-10-2110b1
  comparison: ''
  date: '2026-09-10'
  description: 'Dify — v1.17.1 - Bug Fixes and Improvements: 8 Interface Experience
    changes'
  evidence:
  - quote: Plugin authors now have public profile pages at `/marketplace/creator/<handle>`,
      listing their creations with a publisher sidebar, reachable from a new Creator
      Center entry in the sidebar help menu. The marketplace homepage was rebuilt
      around a hero, a banner carousel, sticky search, catalog tabs, and tag/language
      filters, with a stacked-and-swipeable mobile layout. Bundles are no longer mixed
      into plugin categories. (#41538)
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Workflows containing legacy Agent nodes could not be published** once
      Agent V2 was enabled, because publish validation could not resolve the legacy
      validator. They publish again, while legacy Agent nodes stay hidden from the
      node picker. (#41368)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**The Web Apps sidebar was repainting every loaded app on every navigation.**
      Moving the list to cursor pagination in 1.17.0 dropped its virtualizer, so every
      page fetched stayed mounted in the main nav and survived route changes. On a
      workspace with 427 installed apps, clicking through the top-level nav spent
      1,068 ms of 3.06 s compositing across 12,112 paint records — roughly 7.5 fps
      — with the cost in paint rather than script. The list is virtualized again,
      now on a single always-virtualized render path. (#41397)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Runtime and toolchain updates** — React 19.3 with browser-only rendering
      (#42093), Next.js 16.3.3 (#41262), Node.js 24 LTS (#41573), pnpm 12.3.4 (#42005),
      Jotai v3 (#42036), base-ui 1.8.0 (#41820). Node 24 and pnpm 12.3.4 are now required
      to build the web frontend from source.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'perf(web): virtualize the Web Apps sidebar list again by @BenjaminX in
      https://github.com/langgenius/dify/pull/41397'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(api): decouple onboarding and notification services by @41tair
      in https://github.com/langgenius/dify/pull/40759'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(web): migrate external API selection input by @lyzno1 in https://github.com/langgenius/dify/pull/41610'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'chore(web): upgrade React to 19.3 and adopt browser-only rendering by
      @lyzno1 in https://github.com/langgenius/dify/pull/42093'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 8-interface-experience-changes-in-1-17-1
  source_release: dify-2026-09-10-1-17-1-github-386157159-e472b6fe
  source_type: github_releases
  theme: interface-experience
  title: 8 Interface Experience changes in 1.17.1
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-09-09-5-interface-experience-changes-in-hub-v2-13-0-introducing-new-documents|5
  Interface Experience changes in HUB v2.13.0 — Introducing new Documents…]]'
- '[[Changes/Lovable/2026-09-09-redesigned-chat-actions-menu-in-projects|Redesigned
  Chat actions menu in projects]]'
- '[[Changes/Claude Code/2026-09-10-2-interface-experience-changes-in-v2-1-268|2 Interface
  Experience changes in v2.1.268]]'
source_release: '[[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|dify-2026-09-10-1-17-1-github-386157159-e472b6fe]]'
source_type: github_releases
theme: interface-experience
title: 8 Interface Experience changes in 1.17.1
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Interface Experience changes in 1.17.1

**Dify** · 2026-09-10 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.1) · from [[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|v1.17.1 - Bug Fixes and Improvements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Plugin authors now have public profile pages at `/marketplace/creator/<handle>`, listing their creations with a publisher sidebar, reachable from a new Creator Center entry in the sidebar help menu. The marketplace homepage was rebuilt around a hero, a banner carousel, sticky search, catalog tabs, and tag/language filters, with a stacked-and-swipeable mobile layout. Bundles are no longer mixed into plugin categories. (#41538)

> **Workflows containing legacy Agent nodes could not be published** once Agent V2 was enabled, because publish validation could not resolve the legacy validator. They publish again, while legacy Agent nodes stay hidden from the node picker. (#41368)

> **The Web Apps sidebar was repainting every loaded app on every navigation.** Moving the list to cursor pagination in 1.17.0 dropped its virtualizer, so every page fetched stayed mounted in the main nav and survived route changes. On a workspace with 427 installed apps, clicking through the top-level nav spent 1,068 ms of 3.06 s compositing across 12,112 paint records — roughly 7.5 fps — with the cost in paint rather than script. The list is virtualized again, now on a single always-virtualized render path. (#41397)

> **Runtime and toolchain updates** — React 19.3 with browser-only rendering (#42093), Next.js 16.3.3 (#41262), Node.js 24 LTS (#41573), pnpm 12.3.4 (#42005), Jotai v3 (#42036), base-ui 1.8.0 (#41820). Node 24 and pnpm 12.3.4 are now required to build the web frontend from source.

> perf(web): virtualize the Web Apps sidebar list again by @BenjaminX in https://github.com/langgenius/dify/pull/41397

> refactor(api): decouple onboarding and notification services by @41tair in https://github.com/langgenius/dify/pull/40759

> refactor(web): migrate external API selection input by @lyzno1 in https://github.com/langgenius/dify/pull/41610

> chore(web): upgrade React to 19.3 and adopt browser-only rendering by @lyzno1 in https://github.com/langgenius/dify/pull/42093

Source: https://github.com/langgenius/dify/releases/tag/1.17.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-09-10-4-pricing-model-changes-in-1-17-1|4 Pricing Model changes in 1.17.1]] · Pricing Model
- [[Changes/Dify/2026-09-10-3-automation-and-scheduling-changes-in-1-17-1|3 Automation and Scheduling changes in 1.17.1]] · Automation and Scheduling
- [[Changes/Dify/2026-09-10-76-model-support-changes-in-1-17-1|76 Model Support changes in 1.17.1]] · Model Support
- [[Changes/Dify/2026-09-10-42-agent-mode-changes-in-1-17-1|42 Agent Mode changes in 1.17.1]] · Agent Mode
- [[Changes/Dify/2026-09-10-4-developer-workflow-changes-in-1-17-1|4 Developer Workflow changes in 1.17.1]] · Developer Workflow
- [[Changes/Dify/2026-09-10-3-collaboration-changes-in-1-17-1|3 Collaboration changes in 1.17.1]] · Collaboration
- [[Changes/Dify/2026-09-10-2-memory-and-personalization-changes-in-1-17-1|2 Memory and Personalization changes in 1.17.1]] · Memory and Personalization
- [[Changes/Dify/2026-09-10-16-safety-and-privacy-changes-in-1-17-1|16 Safety and Privacy changes in 1.17.1]] · Safety and Privacy
- [[Changes/Dify/2026-09-10-13-files-and-data-changes-in-1-17-1|13 Files and Data changes in 1.17.1]] · Files and Data
- [[Changes/Dify/2026-09-10-skill-packages-built-on-windows-failed-with-a-misleading-error-a-skill-md-using|Skill packages built on Windows failed with a misleading error. A SKILL.md…]] · Mobile and Desktop
- [[Changes/Dify/2026-09-10-12-apps-and-integrations-changes-in-1-17-1|12 Apps and Integrations changes in 1.17.1]] · Apps and Integrations
- [[Changes/Dify/2026-09-10-6-account-and-access-changes-in-1-17-1|6 Account and Access changes in 1.17.1]] · Account and Access
- [[Changes/Dify/2026-09-10-3-multimodal-input-changes-in-1-17-1|3 Multimodal Input changes in 1.17.1]] · Multimodal Input
- [[Changes/Dify/2026-09-10-6-editor-experience-changes-in-1-17-1|6 Editor Experience changes in 1.17.1]] · Editor Experience
- [[Changes/Dify/2026-09-10-3-accessibility-and-localization-changes-in-1-17-1|3 Accessibility and Localization changes in 1.17.1]] · Accessibility and Localization
- [[Changes/Dify/2026-09-10-a-plugin-could-exhaust-worker-memory-with-one-declared-number-the-blob-chunk-mer|A plugin could exhaust worker memory with one declared number. The blob chunk…]] · Reliability and Performance
- [[Changes/Dify/2026-09-10-6-context-window-changes-in-1-17-1|6 Context Window changes in 1.17.1]] · Context Window
- [[Changes/Dify/2026-09-10-205-other-changes-in-1-17-1|205 other changes in 1.17.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-09-10 · Claude Code · [[Changes/Claude Code/2026-09-10-2-interface-experience-changes-in-v2-1-268|2 Interface Experience changes in v2.1.268]]
- Later: 2026-09-11 · Claude Code · [[Changes/Claude Code/2026-09-11-3-interface-experience-changes-in-v2-1-269|3 Interface Experience changes in v2.1.269]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-09-10-2110b1&body=Card%3A%20Changes%2FDify%2F2026-09-10-8-interface-experience-changes-in-1-17-1.md%0ACard%20ID%3A%20dify-2026-09-10-2110b1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->