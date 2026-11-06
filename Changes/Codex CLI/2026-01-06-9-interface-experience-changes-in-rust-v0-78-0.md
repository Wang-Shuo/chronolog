---
card_id: codex-cli-2026-01-06-b6407c
date: '2026-01-06'
description: 'Codex CLI · 2026-01-06 · Interface Experience: 9 changes in 0.78.0 —
  Improve `tui2` transcript navigation with multi-click selection, a copy…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1093
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ef7247f2ed5288a937ad2aaa10ca46b92d16e3f936fef1d26f5069fc82f87cc3
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-06-b6407c
  comparison: ''
  date: '2026-01-06'
  description: 'Codex CLI — 0.78.0: 9 Interface Experience changes'
  evidence:
  - quote: 'Improve `tui2` transcript navigation with multi-click selection, a copy
      shortcut/affordance, and a draggable auto-hiding scrollbar. (#8462, #8471, #8728)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8419 fix(tui2): constrain transcript mouse selection bounds @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8449 fix(tui2): copy transcript selection outside viewport @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8462 feat(tui2): add copy selection shortcut + UI affordance @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8466 fix(tui2): start transcript selection on drag @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8471 feat(tui2): add multi-click transcript selection @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8693 perf(tui2): cache transcript view rendering @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8718 tui2: copy selection dismisses highlight @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8728 feat(tui2): transcript scrollbar (auto-hide + drag) @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-interface-experience-changes-in-rust-v0-78-0
  source_release: codex-cli-2026-01-06-rust-v0-78-0-github-274610568-c3df153a
  source_type: github_releases
  theme: interface-experience
  title: 9 Interface Experience changes in rust-v0.78.0
  type: change
related_changes:
- '[[Changes/Cline/2025-12-22-model-picker-favorites-ordering-star-toggle-and-keyboard-navigation-for-openrout|Model
  picker favorites ordering, star toggle, and keyboard navigation for OpenRouter…]]'
- '[[Changes/Cursor/2025-12-22-3-interface-experience-changes-in-2-3|3 Interface Experience
  changes in 2.3]]'
- '[[Changes/Cline/2026-01-06-show-notification-instead-of-opening-sidebar-on-update|Show
  notification instead of opening sidebar on update]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-06-rust-v0-78-0-github-274610568-c3df153a|codex-cli-2026-01-06-rust-v0-78-0-github-274610568-c3df153a]]'
source_type: github_releases
theme: interface-experience
title: 9 Interface Experience changes in rust-v0.78.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Interface Experience changes in rust-v0.78.0

**Codex CLI** · 2026-01-06 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.78.0) · from [[Releases/Codex CLI/codex-cli-2026-01-06-rust-v0-78-0-github-274610568-c3df153a|0.78.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improve `tui2` transcript navigation with multi-click selection, a copy shortcut/affordance, and a draggable auto-hiding scrollbar. (#8462, #8471, #8728)

> #8419 fix(tui2): constrain transcript mouse selection bounds @joshka-oai

> #8449 fix(tui2): copy transcript selection outside viewport @joshka-oai

> #8462 feat(tui2): add copy selection shortcut + UI affordance @joshka-oai

> #8466 fix(tui2): start transcript selection on drag @joshka-oai

> #8471 feat(tui2): add multi-click transcript selection @joshka-oai

> #8693 perf(tui2): cache transcript view rendering @joshka-oai

> #8718 tui2: copy selection dismisses highlight @joshka-oai

> #8728 feat(tui2): transcript scrollbar (auto-hide + drag) @joshka-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.78.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-06-3-safety-and-privacy-changes-in-rust-v0-78-0|3 Safety and Privacy changes in rust-v0.78.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-06-performance-tuning-for-tuis-cap-redraw-scheduling-and-reduce-unnecessary-rerende|Performance tuning for TUIs]] · Reliability and Performance
- [[Changes/Codex CLI/2026-01-06-8743-macos-load-config-requirements-from-mdm-gt-oai|♯8743 (MacOS) Load config requirements from MDM @gt-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-06-2-context-window-changes-in-rust-v0-78-0|2 Context Window changes in rust-v0.78.0]] · Context Window
- [[Changes/Codex CLI/2026-01-06-3-editor-experience-changes-in-rust-v0-78-0|3 Editor Experience changes in rust-v0.78.0]] · Editor Experience
- [[Changes/Codex CLI/2026-01-06-6-developer-workflow-changes-in-rust-v0-78-0|6 Developer Workflow changes in rust-v0.78.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-06-support-enterprise-managed-configuration-requirements-on-macos-via-an-mdm-provid|Support enterprise-managed configuration requirements on macOS via an MDM-provided…]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-01-06-5-model-support-changes-in-rust-v0-78-0|5 Model Support changes in rust-v0.78.0]] · Model Support
- [[Changes/Codex CLI/2026-01-06-8694-mcp-sanitize-mcp-tool-names-to-ensure-they-are-compatible-with-the-response|♯8694 MCP Sanitize MCP tool names to ensure they are compatible with the Responses…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-06-65-other-changes-in-rust-v0-78-0|65 other changes in rust-v0.78.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-01-06 · Cline · [[Changes/Cline/2026-01-06-show-notification-instead-of-opening-sidebar-on-update|Show notification instead of opening sidebar on update]]
- Later: 2026-01-07 · ChatGPT · [[Changes/ChatGPT/2026-01-07-health-appears-as-a-new-space-in-the-chatgpt-sidebar-if-you-ask-a-health-related|Health appears as a new space in the ChatGPT sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-06-b6407c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-06-9-interface-experience-changes-in-rust-v0-78-0.md%0ACard%20ID%3A%20codex-cli-2026-01-06-b6407c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.78.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->