---
card_id: codex-cli-2026-01-14-859c22
date: '2026-01-14'
description: 'Codex CLI · 2026-01-14 · Safety and Privacy: 5 changes in 0.81.0 — Linux
  sandbox can mount paths read-only to better protect files from writes. (#9112)'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1004
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8cf5de5fbead6f30294544a687c9666ae1969405fa01838c453c98c6c3b7575b
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-14-859c22
  comparison: ''
  date: '2026-01-14'
  description: 'Codex CLI — 0.81.0: 5 Safety and Privacy changes'
  evidence:
  - quote: Linux sandbox can mount paths read-only to better protect files from writes.
      (#9112)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: Windows correctly prompts before unsafe commands when running with a read-only
      sandbox policy. (#9117)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8961 Assemble sandbox/approval/network prompts dynamically @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9134 fix(windows-sandbox-rs) bump SETUP_VERSION @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9112 feat: add support for read-only bind mounts in the linux sandbox
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-safety-and-privacy-changes-in-rust-v0-81-0
  source_release: codex-cli-2026-01-14-rust-v0-81-0-github-276819252-cf63dc40
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in rust-v0.81.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-01-13-terminal-add-fullscreen-view-to-permission-prompt|Terminal
  Add fullscreen view to permission prompt]]'
- '[[Changes/OpenCode/2026-01-13-2-safety-and-privacy-changes-in-v1-1-16|2 Safety
  and Privacy changes in v1.1.16]]'
- '[[Changes/Claude Code/2026-01-14-2-safety-and-privacy-changes-in-v2-1-7|2 Safety
  and Privacy changes in v2.1.7]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-14-rust-v0-81-0-github-276819252-cf63dc40|codex-cli-2026-01-14-rust-v0-81-0-github-276819252-cf63dc40]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in rust-v0.81.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in rust-v0.81.0

**Codex CLI** · 2026-01-14 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.81.0) · from [[Releases/Codex CLI/codex-cli-2026-01-14-rust-v0-81-0-github-276819252-cf63dc40|0.81.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Linux sandbox can mount paths read-only to better protect files from writes. (#9112)

> Windows correctly prompts before unsafe commands when running with a read-only sandbox policy. (#9117)

> #8961 Assemble sandbox/approval/network prompts dynamically @aibrahim-oai

> #9134 fix(windows-sandbox-rs) bump SETUP_VERSION @dylan-hurd-oai

> #9112 feat: add support for read-only bind mounts in the linux sandbox @viyatb-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.81.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-14-2-agent-mode-changes-in-rust-v0-81-0|2 Agent Mode changes in rust-v0.81.0]] · Agent Mode
- [[Changes/Codex CLI/2026-01-14-2-interface-experience-changes-in-rust-v0-81-0|2 Interface Experience changes in rust-v0.81.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-14-10-apps-and-integrations-changes-in-rust-v0-81-0|10 Apps and Integrations changes in rust-v0.81.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-14-5-developer-workflow-changes-in-rust-v0-81-0|5 Developer Workflow changes in rust-v0.81.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-14-2-account-and-access-changes-in-rust-v0-81-0|2 Account and Access changes in rust-v0.81.0]] · Account and Access
- [[Changes/Codex CLI/2026-01-14-2-mobile-and-desktop-changes-in-rust-v0-81-0|2 Mobile and Desktop changes in rust-v0.81.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-14-9020-fix-tui-document-paste-burst-state-machine-joshka-oai|♯9020 fix(tui): document paste-burst state machine @joshka-oai]] · Files and Data
- [[Changes/Codex CLI/2026-01-14-8-model-support-changes-in-rust-v0-81-0|8 Model Support changes in rust-v0.81.0]] · Model Support
- [[Changes/Codex CLI/2026-01-14-2-editor-experience-changes-in-rust-v0-81-0|2 Editor Experience changes in rust-v0.81.0]] · Editor Experience
- [[Changes/Codex CLI/2026-01-14-72-other-changes-in-rust-v0-81-0|72 other changes in rust-v0.81.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-01-14 · Claude Code · [[Changes/Claude Code/2026-01-14-2-safety-and-privacy-changes-in-v2-1-7|2 Safety and Privacy changes in v2.1.7]]
- Later: 2026-01-14 · Gemini CLI · [[Changes/Gemini CLI/2026-01-14-7-safety-and-privacy-changes-in-v0-24-0|7 Safety and Privacy changes in v0.24.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-14-859c22&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-14-5-safety-and-privacy-changes-in-rust-v0-81-0.md%0ACard%20ID%3A%20codex-cli-2026-01-14-859c22%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.81.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->