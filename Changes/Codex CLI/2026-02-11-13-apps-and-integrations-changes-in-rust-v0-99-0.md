---
card_id: codex-cli-2026-02-11-1b6770
date: '2026-02-11'
description: 'Codex CLI · 2026-02-11 · Apps and Integrations: 13 changes in 0.99.0
  — Required MCP servers now fail fast during start/resume flows instead of continuing
  in a…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2616
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6b9d248caae9caf3de2d197cc90b23cc8e2a9a9a55acf853265ab99109d12c0b
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-11-1b6770
  comparison: ''
  date: '2026-02-11'
  description: 'Codex CLI — 0.99.0: 13 Apps and Integrations changes'
  evidence:
  - quote: Required MCP servers now fail fast during start/resume flows instead of
      continuing in a broken state. (#10902)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#9691 Add hooks implementation and wire up to `notify` @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10902 Handle required MCP startup failures across components @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10938 Mark Config.apps as experimental, correct schema generation issue
      @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10710 Process-group cleanup for stdio MCP servers to prevent orphan process
      storms @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10994 [apps] Improve app loading. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10924 [apps] Add gated instructions for Apps. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11263 test: deflake nextest child-process leak in MCP harnesses @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11279 [apps] Add thread_id param to optionally load thread config for
      apps feature check. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11191 feat: add connector capabilities to sub-agents @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11311 Extract hooks into dedicated crate @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11249 [apps] Improve app installation flow. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11346 Sanitize MCP image output for text-only models @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 13-apps-and-integrations-changes-in-rust-v0-99-0
  source_release: codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016
  source_type: github_releases
  theme: apps-integrations
  title: 13 Apps and Integrations changes in rust-v0.99.0
  type: change
related_changes:
- '[[Changes/Microsoft 365 Copilot/2026-02-10-connect-copilot-to-github-server-with-copilot-connector-web-microsoft-365-copilo|Connect
  Copilot to GitHub Server with Copilot Connector…]]'
- '[[Changes/Microsoft 365 Copilot/2026-02-10-query-miro-boards-and-diagrams-with-copilot-connectors-web-microsoft-365-copilot|Query
  Miro boards and diagrams with Copilot connectors…]]'
- '[[Changes/OpenCode/2026-02-10-core-add-directory-parameter-to-plugin-client-for-multi-project-support|Core
  Add directory parameter to plugin client for multi-project support]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016|codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016]]'
source_type: github_releases
theme: apps-integrations
title: 13 Apps and Integrations changes in rust-v0.99.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Apps and Integrations changes in rust-v0.99.0

**Codex CLI** · 2026-02-11 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.99.0) · from [[Releases/Codex CLI/codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016|0.99.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Required MCP servers now fail fast during start/resume flows instead of continuing in a broken state. (#10902)

> #9691 Add hooks implementation and wire up to `notify` @gt-oai

> #10902 Handle required MCP startup failures across components @jif-oai

> #10938 Mark Config.apps as experimental, correct schema generation issue @canvrno-oai

> #10710 Process-group cleanup for stdio MCP servers to prevent orphan process storms @etraut-openai

> #10994 [apps] Improve app loading. @mzeng-openai

> #10924 [apps] Add gated instructions for Apps. @mzeng-openai

> #11263 test: deflake nextest child-process leak in MCP harnesses @joshka-oai

> #11279 [apps] Add thread_id param to optionally load thread config for apps feature check. @mzeng-openai

> #11191 feat: add connector capabilities to sub-agents @jif-oai

> #11311 Extract hooks into dedicated crate @jif-oai

> #11249 [apps] Improve app installation flow. @mzeng-openai

> #11346 Sanitize MCP image output for text-only models @aibrahim-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.99.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-11-3-search-and-browsing-changes-in-rust-v0-99-0|3 Search and Browsing changes in rust-v0.99.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-02-11-9-developer-workflow-changes-in-rust-v0-99-0|9 Developer Workflow changes in rust-v0.99.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-11-6-context-window-changes-in-rust-v0-99-0|6 Context Window changes in rust-v0.99.0]] · Context Window
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
## Nearby in Apps and Integrations

- Earlier: 2026-02-10 · OpenCode · [[Changes/OpenCode/2026-02-10-core-add-directory-parameter-to-plugin-client-for-multi-project-support|Core Add directory parameter to plugin client for multi-project support]]
- Later: 2026-02-11 · Dify · [[Changes/Dify/2026-02-11-10-apps-and-integrations-changes-in-1-13-0|10 Apps and Integrations changes in 1.13.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-11-1b6770&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-11-13-apps-and-integrations-changes-in-rust-v0-99-0.md%0ACard%20ID%3A%20codex-cli-2026-02-11-1b6770%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.99.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->