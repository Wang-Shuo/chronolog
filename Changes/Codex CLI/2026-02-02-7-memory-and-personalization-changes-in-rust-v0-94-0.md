---
card_id: codex-cli-2026-02-02-688c27
date: '2026-02-02'
description: 'Codex CLI · 2026-02-02 · Memory and Personalization: 7 changes in 0.94.0
  — Personality configuration is now stable: default is friendly, the config key is…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 928
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 58c0336fcb3ee7b219f1f7c3c03bb5b42b1b71494a45788d152c421839c09b89
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-02-688c27
  comparison: ''
  date: '2026-02-02'
  description: 'Codex CLI — 0.94.0: 7 Memory and Personalization changes'
  evidence:
  - quote: 'Personality configuration is now stable: default is friendly, the config
      key is `personality`, and existing settings migrate forward. (#10305, #10314,
      #10310, #10307)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.94.0
  - quote: '#10306 chore(app-server) add personality update test @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.94.0
  - quote: '#10305 chore(core) Default to friendly personality @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.94.0
  - quote: '#10307 feat(core,tui,app-server) personality migration @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.94.0
  - quote: '#10314 chore(config) Rename config setting to personality @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.94.0
  - quote: '#10310 chore(features) Personality => Stable @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.94.0
  - quote: '#10375 fix(personality) prompt patch @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.94.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-memory-and-personalization-changes-in-rust-v0-94-0
  source_release: codex-cli-2026-02-02-rust-v0-94-0-github-282298678-d5cec340
  source_type: github_releases
  theme: memory
  title: 7 Memory and Personalization changes in rust-v0.94.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-01-27-9718-feat-tui-personality-dylan-hurd-oai|♯9718 feat(tui)
  /personality @dylan-hurd-oai]]'
- '[[Changes/GitHub Copilot CLI/2026-01-30-better-handle-large-results-from-grep-and-glob-tools-to-avoid-memory-issues|Better
  handle large results from grep and glob tools to avoid memory issues]]'
- '[[Changes/Codex CLI/2026-01-31-6-memory-and-personalization-changes-in-rust-v0-93-0|6
  Memory and Personalization changes in rust-v0.93.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-02-rust-v0-94-0-github-282298678-d5cec340|codex-cli-2026-02-02-rust-v0-94-0-github-282298678-d5cec340]]'
source_type: github_releases
theme: memory
title: 7 Memory and Personalization changes in rust-v0.94.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Memory and Personalization changes in rust-v0.94.0

**Codex CLI** · 2026-02-02 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.94.0) · from [[Releases/Codex CLI/codex-cli-2026-02-02-rust-v0-94-0-github-282298678-d5cec340|0.94.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Personality configuration is now stable: default is friendly, the config key is `personality`, and existing settings migrate forward. (#10305, #10314, #10310, #10307)

> #10306 chore(app-server) add personality update test @dylan-hurd-oai

> #10305 chore(core) Default to friendly personality @dylan-hurd-oai

> #10307 feat(core,tui,app-server) personality migration @dylan-hurd-oai

> #10314 chore(config) Rename config setting to personality @dylan-hurd-oai

> #10310 chore(features) Personality => Stable @dylan-hurd-oai

> #10375 fix(personality) prompt patch @dylan-hurd-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.94.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-02-2-context-window-changes-in-rust-v0-94-0|2 Context Window changes in rust-v0.94.0]] · Context Window
- [[Changes/Codex CLI/2026-02-02-2-interface-experience-changes-in-rust-v0-94-0|2 Interface Experience changes in rust-v0.94.0]] · Interface Experience
- [[Changes/Codex CLI/2026-02-02-10373-chore-core-gpt-5-2-codex-personality-template-dylan-hurd-oai|♯10373 chore(core) gpt-5.2-codex personality template @dylan-hurd-oai]] · Model Support
- [[Changes/Codex CLI/2026-02-02-2-agent-mode-changes-in-rust-v0-94-0|2 Agent Mode changes in rust-v0.94.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-02-plan-mode-is-now-enabled-by-default-with-updated-interaction-guidance-in-the-pla|Plan mode is now enabled by default with updated interaction guidance in the plan prompt]] · Other changes
- [[Changes/Codex CLI/2026-02-02-20-other-changes-in-rust-v0-94-0|20 other changes in rust-v0.94.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-01-31 · Codex CLI · [[Changes/Codex CLI/2026-01-31-6-memory-and-personalization-changes-in-rust-v0-93-0|6 Memory and Personalization changes in rust-v0.93.0]]
- Later: 2026-02-05 · Claude Code · [[Changes/Claude Code/2026-02-05-claude-now-automatically-records-and-recalls-memories-as-it-works|Claude now automatically records and recalls memories as it works]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-02-688c27&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-02-7-memory-and-personalization-changes-in-rust-v0-94-0.md%0ACard%20ID%3A%20codex-cli-2026-02-02-688c27%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.94.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->