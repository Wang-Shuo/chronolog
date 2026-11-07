---
card_id: codex-cli-2026-02-11-09cd77
date: '2026-02-11'
description: 'Codex CLI · 2026-02-11 · Developer Workflow: 9 changes in 0.99.0 — Running
  direct shell commands no longer interrupts an in-flight turn; commands can execute…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2710
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6f0497b418207e27ca95b45163b99b9e812f7af9be675b40019d4dc9370172ff
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-11-09cd77
  comparison: ''
  date: '2026-02-11'
  description: 'Codex CLI — 0.99.0: 9 Developer Workflow changes'
  evidence:
  - quote: Running direct shell commands no longer interrupts an in-flight turn; commands
      can execute concurrently when a turn is active. (#10513)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: Enable snapshotting of the shell environment and `rc` files (#11172)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: 'Reduced false approval mismatches for wrapped/heredoc shell commands and
      guarded against empty command lists in exec policy evaluation. (#10941, #11397)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10513 Allow user shell commands to run alongside active turns @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10909 Bootstrap shell commands via user shell snapshot @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11039 feat: include state of [experimental_network] in /debug-config
      output @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11172 chore: enable shell snapshot @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11231 feat: tie shell snapshot to cwd @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11397 fix(exec-policy) No empty command lists @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-developer-workflow-changes-in-rust-v0-99-0
  source_release: codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016
  source_type: github_releases
  theme: developer-workflow
  title: 9 Developer Workflow changes in rust-v0.99.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-02-10-13-developer-workflow-changes-in-v1-1-54|13 Developer
  Workflow changes in v1.1.54]]'
- '[[Changes/OpenCode/2026-02-10-desktop-disable-terminal-transparency|Desktop Disable
  terminal transparency]]'
- '[[Changes/v0/2026-02-10-added-support-for-nuxt-and-additional-frameworks-in-git-imports|Added
  support for Nuxt and additional frameworks in Git imports]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016|codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016]]'
source_type: github_releases
theme: developer-workflow
title: 9 Developer Workflow changes in rust-v0.99.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Developer Workflow changes in rust-v0.99.0

**Codex CLI** · 2026-02-11 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.99.0) · from [[Releases/Codex CLI/codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016|0.99.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Running direct shell commands no longer interrupts an in-flight turn; commands can execute concurrently when a turn is active. (#10513)

> Enable snapshotting of the shell environment and `rc` files (#11172)

> Reduced false approval mismatches for wrapped/heredoc shell commands and guarded against empty command lists in exec policy evaluation. (#10941, #11397)

> #10513 Allow user shell commands to run alongside active turns @jif-oai

> #10909 Bootstrap shell commands via user shell snapshot @jif-oai

> #11039 feat: include state of [experimental_network] in /debug-config output @bolinfest

> #11172 chore: enable shell snapshot @jif-oai

> #11231 feat: tie shell snapshot to cwd @jif-oai

> #11397 fix(exec-policy) No empty command lists @dylan-hurd-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.99.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-11-3-search-and-browsing-changes-in-rust-v0-99-0|3 Search and Browsing changes in rust-v0.99.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-02-11-6-context-window-changes-in-rust-v0-99-0|6 Context Window changes in rust-v0.99.0]] · Context Window
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
## Nearby in Developer Workflow

- Earlier: 2026-02-10 · v0 · [[Changes/v0/2026-02-10-added-support-for-nuxt-and-additional-frameworks-in-git-imports|Added support for Nuxt and additional frameworks in Git imports]]
- Later: 2026-02-11 · Dify · [[Changes/Dify/2026-02-11-please-use-the-following-command-instead-for-details-please-read-this-https-gith| Please use the following command instead]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-11-09cd77&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-11-9-developer-workflow-changes-in-rust-v0-99-0.md%0ACard%20ID%3A%20codex-cli-2026-02-11-09cd77%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.99.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->