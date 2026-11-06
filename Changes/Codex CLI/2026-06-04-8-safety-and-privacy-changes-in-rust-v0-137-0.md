---
card_id: codex-cli-2026-06-04-f33c31
date: '2026-06-04'
description: 'Codex CLI · 2026-06-04 · Safety and Privacy: 8 changes in 0.137.0 —
  Platform reliability improved for macOS app launches and Windows SQLite startup,
  thread…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1145
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 10550fd675bab698407815084fa54a0583e3ea59016747a4e137bff89261b77e
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-04-f33c31
  comparison: ''
  date: '2026-06-04'
  description: 'Codex CLI — 0.137.0: 8 Safety and Privacy changes'
  evidence:
  - quote: 'Platform reliability improved for macOS app launches and Windows SQLite
      startup, thread resume, and sandbox setup refreshes (#25485, #25490, #25509,
      #25949).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: 'Permission requests and approvals now carry environment identity, and
      managed MITM proxying exports readable CA bundles to child commands (#25850,
      #25858, #25862, #22668).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: 'Added app-server docs and generated schema updates for monthly credit
      limits, remote-control RPCs, and environment-scoped permission approvals (#24812,
      #25675, #25785, #25862).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25739 core: derive built-in permission profiles from raw policies @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25850 Key request-permission grants by environment @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25862 Propagate permission approval environment id @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25943 config: remove dead profile sandbox fallback @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25926 config: express implicit sandbox defaults as permission profiles
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 8-safety-and-privacy-changes-in-rust-v0-137-0
  source_release: codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece
  source_type: github_releases
  theme: safety-privacy
  title: 8 Safety and Privacy changes in rust-v0.137.0
  type: change
related_changes:
- '[[Changes/Cursor/2026-06-03-enterprise-customers-can-now-manage-multiple-cursor-teams-from-one-place-with-di|Enterprise
  customers can now manage multiple Cursor teams from one place…]]'
- '[[Changes/ChatGPT/2026-06-04-lockdown-mode-is-now-available-to-all-logged-in-users-across-account-types-and-w|Lockdown
  Mode is now available to all logged-in users]]'
- '[[Changes/Claude Code/2026-06-04-fixed-org-managed-permission-rules-not-applying-for-the-entire-session-when-the|Fixed
  org-managed permission rules not applying for the entire session…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece|codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece]]'
source_type: github_releases
theme: safety-privacy
title: 8 Safety and Privacy changes in rust-v0.137.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Safety and Privacy changes in rust-v0.137.0

**Codex CLI** · 2026-06-04 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.137.0) · from [[Releases/Codex CLI/codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece|0.137.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Platform reliability improved for macOS app launches and Windows SQLite startup, thread resume, and sandbox setup refreshes (#25485, #25490, #25509, #25949).

> Permission requests and approvals now carry environment identity, and managed MITM proxying exports readable CA bundles to child commands (#25850, #25858, #25862, #22668).

> Added app-server docs and generated schema updates for monthly credit limits, remote-control RPCs, and environment-scoped permission approvals (#24812, #25675, #25785, #25862).

> #25739 core: derive built-in permission profiles from raw policies @bolinfest

> #25850 Key request-permission grants by environment @jif-oai

> #25862 Propagate permission approval environment id @jif-oai

> #25943 config: remove dead profile sandbox fallback @bolinfest

> #25926 config: express implicit sandbox defaults as permission profiles @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.137.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-04-6-developer-workflow-changes-in-rust-v0-137-0|6 Developer Workflow changes in rust-v0.137.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-04-25702-codex-enable-parallel-standalone-web-search-calls-sayan-oai|♯25702 codex enable parallel standalone web search calls @sayan-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-04-3-image-generation-changes-in-rust-v0-137-0|3 Image Generation changes in rust-v0.137.0]] · Image Generation
- [[Changes/Codex CLI/2026-06-04-2-interface-experience-changes-in-rust-v0-137-0|2 Interface Experience changes in rust-v0.137.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-04-19-apps-and-integrations-changes-in-rust-v0-137-0|19 Apps and Integrations changes in rust-v0.137.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-04-2-enterprise-and-administration-changes-in-rust-v0-137-0|2 Enterprise and Administration changes in rust-v0.137.0]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-06-04-local-session-history-is-safer-for-compressed-rollouts-renamed-titles-pathless-s|Local session history is safer for compressed rollouts, renamed titles, pathless…]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-06-04-4-collaboration-changes-in-rust-v0-137-0|4 Collaboration changes in rust-v0.137.0]] · Collaboration
- [[Changes/Codex CLI/2026-06-04-3-context-window-changes-in-rust-v0-137-0|3 Context Window changes in rust-v0.137.0]] · Context Window
- [[Changes/Codex CLI/2026-06-04-2-mobile-and-desktop-changes-in-rust-v0-137-0|2 Mobile and Desktop changes in rust-v0.137.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-04-12-agent-mode-changes-in-rust-v0-137-0|12 Agent Mode changes in rust-v0.137.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-04-25682-codex-document-out-of-line-test-module-convention-anp-oai|♯25682 codex document out-of-line test module convention @anp-oai]] · Files and Data
- [[Changes/Codex CLI/2026-06-04-3-model-support-changes-in-rust-v0-137-0|3 Model Support changes in rust-v0.137.0]] · Model Support
- [[Changes/Codex CLI/2026-06-04-69-other-changes-in-rust-v0-137-0|69 other changes in rust-v0.137.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-06-04 · Claude Code · [[Changes/Claude Code/2026-06-04-fixed-org-managed-permission-rules-not-applying-for-the-entire-session-when-the|Fixed org-managed permission rules not applying for the entire session…]]
- Later: 2026-06-04 · Cursor · [[Changes/Cursor/2026-06-04-custom-tools-056918|Custom tools]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-04-f33c31&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-04-8-safety-and-privacy-changes-in-rust-v0-137-0.md%0ACard%20ID%3A%20codex-cli-2026-06-04-f33c31%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.137.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->