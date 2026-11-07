---
card_id: dify-2026-10-23-0e585d
date: '2026-10-23'
description: 'Dify · 2026-10-23 · Developer Workflow: | `RESPECT_XFORWARD_HEADERS_ENABLED`
  | Standalone API default remains `false`; bundled Compose explicitly enables it…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2964
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: b3230bb022372558ff0b6912eb2bb5af95802880526094400d920deb10545672
product: dify
product_name: Dify
record:
  card_id: dify-2026-10-23-0e585d
  comparison: ''
  date: '2026-10-23'
  description: 'Dify — v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow
    Visibility: | `RESPECT_XFORWARD_HEADERS_ENABLED` | Standalone API default remains
    `false`; bundled Compose explicitly enables it for API/WebSocket services behind
    Nginx. Settings supplied only through `shared.env` are overridden. Move an intentional
    override to `docker/.env`, the invoking shell, or a Compose override. |'
  evidence:
  - quote: '| `RESPECT_XFORWARD_HEADERS_ENABLED` | Standalone API default remains
      `false`; bundled Compose explicitly enables it for API/WebSocket services behind
      Nginx. Settings supplied only through `shared.env` are overridden. Move an intentional
      override to `docker/.env`, the invoking shell, or a Compose override. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: dify
  product_name: Dify
  slug: respect-xforward-headers-enabled-standalone-api-default-remains-false-bundled-co
  source_release: dify-2026-10-23-1-18-0-github-421489030-879b0613
  source_type: github_releases
  theme: developer-workflow
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: '| `RESPECT_XFORWARD_HEADERS_ENABLED` | Standalone API default remains `false`'
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-23-code-review-improved-the-code-review-admin-section-to-retry-the-first-load-and-s|Code
  Review Improved the Code Review admin section to retry the first load…]]'
- '[[Changes/Codex CLI/2026-10-23-14-developer-workflow-changes-in-rust-v0-164-0|14
  Developer Workflow changes in rust-v0.164.0]]'
- '[[Changes/Devin/2026-10-23-turn-on-automatic-reviews-from-a-pull-request|Turn on
  Automatic Reviews from a Pull Request]]'
source_release: '[[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|dify-2026-10-23-1-18-0-github-421489030-879b0613]]'
source_type: github_releases
theme: developer-workflow
title: ' /  RESPECT_XFORWARD_HEADERS_ENABLED  /  Standalone API default remains false'
type: change
---

<!-- chronolog:begin region="header" -->
# | `RESPECT_XFORWARD_HEADERS_ENABLED` | Standalone API default remains `false`

**Dify** · 2026-10-23 · [[Themes/developer-workflow|Developer Workflow]] · [Official source](https://github.com/langgenius/dify/releases/tag/1.18.0) · from [[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow Visibility]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> | `RESPECT_XFORWARD_HEADERS_ENABLED` | Standalone API default remains `false`; bundled Compose explicitly enables it for API/WebSocket services behind Nginx. Settings supplied only through `shared.env` are overridden. Move an intentional override to `docker/.env`, the invoking shell, or a Compose override. |
>
> Source: https://github.com/langgenius/dify/releases/tag/1.18.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-10-23-3-memory-and-personalization-changes-in-1-18-0|3 Memory and Personalization changes in 1.18.0]] · Memory and Personalization
- [[Changes/Dify/2026-10-23-3-accessibility-and-localization-changes-in-1-18-0|3 Accessibility and Localization changes in 1.18.0]] · Accessibility and Localization
- [[Changes/Dify/2026-10-23-3-context-window-changes-in-1-18-0|3 Context Window changes in 1.18.0]] · Context Window
- [[Changes/Dify/2026-10-23-operations-archive-storage-supports-configurable-s3-addressing-style-the-api-ima|Operations: archive storage supports configurable S3 addressing style]] · Model Support
- [[Changes/Dify/2026-10-23-2-interface-experience-changes-in-1-18-0|2 Interface Experience changes in 1.18.0]] · Interface Experience
- [[Changes/Dify/2026-10-23-3-editor-experience-changes-in-1-18-0|3 Editor Experience changes in 1.18.0]] · Editor Experience
- [[Changes/Dify/2026-10-23-32-agent-mode-changes-in-1-18-0|32 Agent Mode changes in 1.18.0]] · Agent Mode
- [[Changes/Dify/2026-10-23-11-safety-and-privacy-changes-in-1-18-0|11 Safety and Privacy changes in 1.18.0]] · Safety and Privacy
- [[Changes/Dify/2026-10-23-14-apps-and-integrations-changes-in-1-18-0|14 Apps and Integrations changes in 1.18.0]] · Apps and Integrations
- [[Changes/Dify/2026-10-23-6-account-and-access-changes-in-1-18-0|6 Account and Access changes in 1.18.0]] · Account and Access
- [[Changes/Dify/2026-10-23-2-reliability-and-performance-changes-in-1-18-0|2 Reliability and Performance changes in 1.18.0]] · Reliability and Performance
- [[Changes/Dify/2026-10-23-5-collaboration-changes-in-1-18-0|5 Collaboration changes in 1.18.0]] · Collaboration
- [[Changes/Dify/2026-10-23-8-files-and-data-changes-in-1-18-0|8 Files and Data changes in 1.18.0]] · Files and Data
- [[Changes/Dify/2026-10-23-2-automation-and-scheduling-changes-in-1-18-0|2 Automation and Scheduling changes in 1.18.0]] · Automation and Scheduling
- [[Changes/Dify/2026-10-23-81-other-changes-in-1-18-0|81 other changes in 1.18.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-10-23 · Devin · [[Changes/Devin/2026-10-23-turn-on-automatic-reviews-from-a-pull-request|Turn on Automatic Reviews from a Pull Request]]
- Later: 2026-10-23 · Windsurf · [[Changes/Windsurf/2026-10-23-4-developer-workflow-changes-in-v3-11-212|4 Developer Workflow changes in v3.11.212]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-10-23-0e585d&body=Card%3A%20Changes%2FDify%2F2026-10-23-respect-xforward-headers-enabled-standalone-api-default-remains-false-bundled-co.md%0ACard%20ID%3A%20dify-2026-10-23-0e585d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.18.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->