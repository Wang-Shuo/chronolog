---
card_id: codex-cli-2026-04-20-93861e
date: '2026-04-20'
description: 'Codex CLI · 2026-04-20 · Context Window: 10 changes in 0.122.0 — Plan
  Mode can start implementation in a fresh context, with context-usage shown before…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1082
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5eaae2af8c278c219038e1f2b820d49b42d0fe5068e8fcb36223ea1f77c6b76e
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-20-93861e
  comparison: ''
  date: '2026-04-20'
  description: 'Codex CLI — 0.122.0: 10 Context Window changes'
  evidence:
  - quote: 'Plan Mode can start implementation in a fresh context, with context-usage
      shown before deciding whether to carry the planning thread forward (#17499,
      #18573).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: Resumed and forked app-server threads now replay token usage immediately
      so context/status UI starts with the restored state (#18023).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17958 Support remote compaction for Azure responses providers @ivanmurashko'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17896 Clarify realtime v2 context and handoff messages @bxie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18054 fix(tui): remove duplicate context statusline item @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18172 [codex] Make realtime startup context truncation deterministic
      @bxie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17825 [codex] Revoke ChatGPT tokens on logout @sashank-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17499 feat(tui): add clear-context plan implementation @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18382 Add max context window model metadata @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18573 feat(tui): show context used in plan implementation prompt @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 10-context-window-changes-in-rust-v0-122-0
  source_release: codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e
  source_type: github_releases
  theme: context-window
  title: 10 Context Window changes in rust-v0.122.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-04-15-4-context-window-changes-in-rust-v0-121-0|4 Context
  Window changes in rust-v0.121.0]]'
- '[[Changes/GitHub Copilot CLI/2026-04-16-add-statusline-command-with-footer-alias-to-customize-which-items-appear-in-the|Add
  /statusline command (with /footer alias) to customize which items appear…]]'
- '[[Changes/GitHub Copilot CLI/2026-04-17-3-context-window-changes-in-v1-0-32|3 Context
  Window changes in v1.0.32]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e|codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e]]'
source_type: github_releases
theme: context-window
title: 10 Context Window changes in rust-v0.122.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Context Window changes in rust-v0.122.0

**Codex CLI** · 2026-04-20 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.122.0) · from [[Releases/Codex CLI/codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e|0.122.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Plan Mode can start implementation in a fresh context, with context-usage shown before deciding whether to carry the planning thread forward (#17499, #18573).

> Resumed and forked app-server threads now replay token usage immediately so context/status UI starts with the restored state (#18023).

> #17958 Support remote compaction for Azure responses providers @ivanmurashko

> #17896 Clarify realtime v2 context and handoff messages @bxie-openai

> #18054 fix(tui): remove duplicate context statusline item @etraut-openai

> #18172 [codex] Make realtime startup context truncation deterministic @bxie-openai

> #17825 [codex] Revoke ChatGPT tokens on logout @sashank-oai

> #17499 feat(tui): add clear-context plan implementation @fcoury-oai

> #18382 Add max context window model metadata @aibrahim-oai

> #18573 feat(tui): show context used in plan implementation prompt @fcoury-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.122.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-20-6-developer-workflow-changes-in-rust-v0-122-0|6 Developer Workflow changes in rust-v0.122.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-20-tool-discovery-and-image-generation-are-now-enabled-by-default-with-higher-detai|Tool discovery and image generation are now enabled by default, with higher-detail…]] · Image Generation
- [[Changes/Codex CLI/2026-04-20-17153-launch-image-generation-by-default-won-openai|♯17153 Launch image generation by default @won-openai]] · Image Generation
- [[Changes/Codex CLI/2026-04-20-10-agent-mode-changes-in-rust-v0-122-0|10 Agent Mode changes in rust-v0.122.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-20-6-model-support-changes-in-rust-v0-122-0|6 Model Support changes in rust-v0.122.0]] · Model Support
- [[Changes/Codex CLI/2026-04-20-4-memory-and-personalization-changes-in-rust-v0-122-0|4 Memory and Personalization changes in rust-v0.122.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-20-18398-refactor-use-cloneable-async-channels-for-shared-receivers-bolinfest|♯18398 refactor: use cloneable async channels for shared receivers @bolinfest]] · Collaboration
- [[Changes/Codex CLI/2026-04-20-28-apps-and-integrations-changes-in-rust-v0-122-0|28 Apps and Integrations changes in rust-v0.122.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-20-plugin-workflows-now-include-tabbed-browsing-inline-enable-disable-toggles-marke|Plugin workflows now include tabbed browsing, inline enable/disable toggles…]] · Search and Browsing
- [[Changes/Codex CLI/2026-04-20-9-safety-and-privacy-changes-in-rust-v0-122-0|9 Safety and Privacy changes in rust-v0.122.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-20-2-interface-experience-changes-in-rust-v0-122-0|2 Interface Experience changes in rust-v0.122.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-20-2-mobile-and-desktop-changes-in-rust-v0-122-0|2 Mobile and Desktop changes in rust-v0.122.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-20-100-other-changes-in-rust-v0-122-0|100 other changes in rust-v0.122.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-04-17 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-17-3-context-window-changes-in-v1-0-32|3 Context Window changes in v1.0.32]]
- Later: 2026-04-23 · Codex CLI · [[Changes/Codex CLI/2026-04-23-18794-organize-context-fragments-pakrym-oai|♯18794 Organize context fragments @pakrym-oai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-20-93861e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-20-10-context-window-changes-in-rust-v0-122-0.md%0ACard%20ID%3A%20codex-cli-2026-04-20-93861e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.122.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->