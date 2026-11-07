---
card_id: codex-cli-2026-07-08-74b78d
date: '2026-07-08'
description: 'Codex CLI · 2026-07-08 · Safety and Privacy: 13 changes in 0.143.0 —
  Updated OpenSSL, Hono, fast-uri, quick-xml, and crossbeam-epoch to address security…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1179
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dd31fff9b40cce78e1e0f0d4bb8cbea48c8bd36d337c055009a833569ba6818e
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-08-74b78d
  comparison: ''
  date: '2026-07-08'
  description: 'Codex CLI — 0.143.0: 13 Safety and Privacy changes'
  evidence:
  - quote: 'Updated OpenSSL, Hono, fast-uri, quick-xml, and crossbeam-epoch to address
      security advisories. (#29487, #29650, #30941, #31308)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29473 Propagate safety buffering treatment metadata @fc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29358 Allow codex sandbox to consume MCP sandbox state @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29456 Prepare managed network sandbox context @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29671 [codex] Preserve proxy state for filesystem sandbox helpers @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29624 Preserve Windows sandbox identity during credential retry @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30095 cli: rename sandbox permission profile flag @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29941 core: expose permission profile to shell tools @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30317 Update security check wording @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30490 fix(tui): clear completed safety buffering prompt @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30491 Update safety check links @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30645 [codex] Update safety notice wording @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30941 fix: address quick-xml security advisories @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 13-safety-and-privacy-changes-in-rust-v0-143-0
  source_release: codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c
  source_type: github_releases
  theme: safety-privacy
  title: 13 Safety and Privacy changes in rust-v0.143.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-07-07-8-safety-and-privacy-changes-in-v1-0-69|8
  Safety and Privacy changes in v1.0.69]]'
- '[[Changes/v0/2026-07-07-5-safety-and-privacy-changes-in-grouped-tool-approvals-richer-mcp|5
  Safety and Privacy changes in Grouped tool approvals, richer MCP…]]'
- '[[Changes/Claude Code/2026-07-08-background-task-notifications-now-explicitly-state-that-no-human-input-has-occur|Background
  task notifications now explicitly state that no human input has occurred…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c|codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c]]'
source_type: github_releases
theme: safety-privacy
title: 13 Safety and Privacy changes in rust-v0.143.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Safety and Privacy changes in rust-v0.143.0

**Codex CLI** · 2026-07-08 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.143.0) · from [[Releases/Codex CLI/codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c|0.143.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Updated OpenSSL, Hono, fast-uri, quick-xml, and crossbeam-epoch to address security advisories. (#29487, #29650, #30941, #31308)

> #29473 Propagate safety buffering treatment metadata @fc-oai

> #29358 Allow codex sandbox to consume MCP sandbox state @jif-oai

> #29456 Prepare managed network sandbox context @jif-oai

> #29671 [codex] Preserve proxy state for filesystem sandbox helpers @iceweasel-oai

> #29624 Preserve Windows sandbox identity during credential retry @jif-oai

> #30095 cli: rename sandbox permission profile flag @bolinfest

> #29941 core: expose permission profile to shell tools @bolinfest

> #30317 Update security check wording @etraut-openai

> #30490 fix(tui): clear completed safety buffering prompt @fcoury-oai

> #30491 Update safety check links @etraut-openai

> #30645 [codex] Update safety notice wording @etraut-openai

> #30941 fix: address quick-xml security advisories @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.143.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-08-5-collaboration-changes-in-rust-v0-143-0|5 Collaboration changes in rust-v0.143.0]] · Collaboration
- [[Changes/Codex CLI/2026-07-08-5-account-and-access-changes-in-rust-v0-143-0|5 Account and Access changes in rust-v0.143.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-08-66-apps-and-integrations-changes-in-rust-v0-143-0|66 Apps and Integrations changes in rust-v0.143.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-08-14-model-support-changes-in-rust-v0-143-0|14 Model Support changes in rust-v0.143.0]] · Model Support
- [[Changes/Codex CLI/2026-07-08-10-agent-mode-changes-in-rust-v0-143-0|10 Agent Mode changes in rust-v0.143.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-08-27714-app-server-document-thread-and-turn-ids-are-uuid7-owenlin0|♯27714 app-server: document thread and turn IDs are UUID7 @owenlin0]] · Files and Data
- [[Changes/Codex CLI/2026-07-08-28593-codex-suppress-low-usage-remaining-warnings-when-credits-are-available-bro|♯28593 codex suppress low usage remaining warnings when credits are available…]] · Pricing Model
- [[Changes/Codex CLI/2026-07-08-12-context-window-changes-in-rust-v0-143-0|12 Context Window changes in rust-v0.143.0]] · Context Window
- [[Changes/Codex CLI/2026-07-08-30508-revert-make-auto-review-on-request-prompt-more-proactive-dylan-hurd-oai|♯30508 Revert "Make auto-review on-request prompt more proactive" @dylan-hurd-oai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-07-08-2-mobile-and-desktop-changes-in-rust-v0-143-0|2 Mobile and Desktop changes in rust-v0.143.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-08-3-editor-experience-changes-in-rust-v0-143-0|3 Editor Experience changes in rust-v0.143.0]] · Editor Experience
- [[Changes/Codex CLI/2026-07-08-7-developer-workflow-changes-in-rust-v0-143-0|7 Developer Workflow changes in rust-v0.143.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-08-3-image-generation-changes-in-rust-v0-143-0|3 Image Generation changes in rust-v0.143.0]] · Image Generation
- [[Changes/Codex CLI/2026-07-08-2-memory-and-personalization-changes-in-rust-v0-143-0|2 Memory and Personalization changes in rust-v0.143.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-08-remote-plugins-are-now-enabled-by-default-with-richer-catalog-rows-npm-marketpla|Remote plugins are now enabled by default, with richer catalog rows, npm marketplace…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-08-145-other-changes-in-rust-v0-143-0|145 other changes in rust-v0.143.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-08 · Claude Code · [[Changes/Claude Code/2026-07-08-background-task-notifications-now-explicitly-state-that-no-human-input-has-occur|Background task notifications now explicitly state that no human input has occurred…]]
- Later: 2026-07-09 · ChatGPT · [[Changes/ChatGPT/2026-07-09-on-desktop-work-can-use-local-files-and-desktop-apps-with-your-permission-the-bu-1e4d11|On desktop, Work can use local files and desktop apps with your permission]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-08-74b78d&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-08-13-safety-and-privacy-changes-in-rust-v0-143-0.md%0ACard%20ID%3A%20codex-cli-2026-07-08-74b78d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.143.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->