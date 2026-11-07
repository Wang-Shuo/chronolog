---
card_id: codex-cli-2026-02-11-0cb6cf
date: '2026-02-11'
description: 'Codex CLI · 2026-02-11 · Context Window: 6 changes in 0.99.0 — #10840
  Removed the "remote_compaction" feature flag @etraut-openai'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2338
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2ddd070667da74bbeb3ed3d22e09adcf6fadb4523ee33bb08e47fb2b05bf2d8d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-11-0cb6cf
  comparison: ''
  date: '2026-02-11'
  description: 'Codex CLI — 0.99.0: 6 Context Window changes'
  evidence:
  - quote: '#10840 Removed the "remote_compaction" feature flag @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10574 core: refresh developer instructions after compaction replacement
      history @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10927 Treat compaction failure as failure state @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11044 feat: include [experimental_network] in <environment_context> @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11132 core: account for all post-response items in auto-compact token
      checks @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11133 core: add focused diagnostics for remote compaction overflows @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-context-window-changes-in-rust-v0-99-0
  source_release: codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016
  source_type: github_releases
  theme: context-window
  title: 6 Context Window changes in rust-v0.99.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-05-2-context-window-changes-in-v2-1-32|2 Context
  Window changes in v2.1.32]]'
- '[[Changes/Codex CLI/2026-02-05-10692-fix-remote-compaction-estimator-payload-instruction-small-mismatch-charley|♯10692
  Fix remote compaction estimator/payload instruction small mismatch @charley-oai]]'
- '[[Changes/OpenCode/2026-02-10-desktop-fix-stale-context-in-prompt-input|Desktop
  Fix stale context in prompt input]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016|codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016]]'
source_type: github_releases
theme: context-window
title: 6 Context Window changes in rust-v0.99.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Context Window changes in rust-v0.99.0

**Codex CLI** · 2026-02-11 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.99.0) · from [[Releases/Codex CLI/codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016|0.99.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #10840 Removed the "remote_compaction" feature flag @etraut-openai

> #10574 core: refresh developer instructions after compaction replacement history @charley-oai

> #10927 Treat compaction failure as failure state @aibrahim-oai

> #11044 feat: include [experimental_network] in \<environment_context> @bolinfest

> #11132 core: account for all post-response items in auto-compact token checks @charley-oai

> #11133 core: add focused diagnostics for remote compaction overflows @charley-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.99.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-11-3-search-and-browsing-changes-in-rust-v0-99-0|3 Search and Browsing changes in rust-v0.99.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-02-11-9-developer-workflow-changes-in-rust-v0-99-0|9 Developer Workflow changes in rust-v0.99.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-11-13-apps-and-integrations-changes-in-rust-v0-99-0|13 Apps and Integrations changes in rust-v0.99.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-11-8-safety-and-privacy-changes-in-rust-v0-99-0|8 Safety and Privacy changes in rust-v0.99.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-11-7-memory-and-personalization-changes-in-rust-v0-99-0|7 Memory and Personalization changes in rust-v0.99.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-11-enterprise-admin-requirements-can-now-restrict-web-search-modes-and-define-netwo|Enterprise/admin requirements can now restrict web search modes and define network…]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-02-11-2-editor-experience-changes-in-rust-v0-99-0|2 Editor Experience changes in rust-v0.99.0]] · Editor Experience
- [[Changes/Codex CLI/2026-02-11-11294-chore-put-crypto-provider-logic-in-a-shared-crate-bolinfest|♯11294 chore: put crypto provider logic in a shared crate @bolinfest]] · Collaboration
- [[Changes/Codex CLI/2026-02-11-11336-always-expose-view-image-and-return-unsupported-image-input-error-aibrahim|♯11336 Always expose view_image and return unsupported image-input error @aibrahim-oai]] · Multimodal Input
- [[Changes/Codex CLI/2026-02-11-15-model-support-changes-in-rust-v0-99-0|15 Model Support changes in rust-v0.99.0]] · Model Support
- [[Changes/Codex CLI/2026-02-11-10-agent-mode-changes-in-rust-v0-99-0|10 Agent Mode changes in rust-v0.99.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-11-4-mobile-and-desktop-changes-in-rust-v0-99-0|4 Mobile and Desktop changes in rust-v0.99.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-11-8-interface-experience-changes-in-rust-v0-99-0|8 Interface Experience changes in rust-v0.99.0]] · Interface Experience
- [[Changes/Codex CLI/2026-02-11-added-statusline-to-configure-which-metadata-appears-in-the-tui-footer-interacti|Added /statusline to configure which metadata appears in the TUI footer interactively]] · Other changes
- [[Changes/Codex CLI/2026-02-11-116-other-changes-in-rust-v0-99-0|116 other changes in rust-v0.99.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-02-10 · OpenCode · [[Changes/OpenCode/2026-02-10-desktop-fix-stale-context-in-prompt-input|Desktop Fix stale context in prompt input]]
- Later: 2026-02-11 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-11-expose-session-context-in-session-list-sdk-response|Expose session context in session.list SDK response]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-11-0cb6cf&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-11-6-context-window-changes-in-rust-v0-99-0.md%0ACard%20ID%3A%20codex-cli-2026-02-11-0cb6cf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.99.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->