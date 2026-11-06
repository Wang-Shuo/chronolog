---
card_id: codex-cli-2026-05-28-53704c
date: '2026-05-28'
description: 'Codex CLI · 2026-05-28 · Memory and Personalization: 8 changes in 0.135.0
  — Moved memory runtime state into a dedicated SQLite database. (#24591)'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1043
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 53cf3068d520bd8842544b1134c18fc20671e10a0749e5f2c0d3cade8b132650
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-28-53704c
  comparison: ''
  date: '2026-05-28'
  description: 'Codex CLI — 0.135.0: 8 Memory and Personalization changes'
  evidence:
  - quote: Moved memory runtime state into a dedicated SQLite database. (#24591)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24555 chore: drop orphaned codex memories MCP crate @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24558 chore: move memory prompt builder into extension @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24562 Add ad-hoc memory note tool @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24567 Wire metrics client into memories extension @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24583 Add memory tool call metrics to memories extension @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24600 feat: gate dedicated memories tools in config @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24591 Move memory state to a dedicated SQLite DB @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 8-memory-and-personalization-changes-in-rust-v0-135-0
  source_release: codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b
  source_type: github_releases
  theme: memory
  title: 8 Memory and Personalization changes in rust-v0.135.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-05-22-2-memory-and-personalization-changes-in-v0-43-0|2
  Memory and Personalization changes in v0.43.0]]'
- '[[Changes/Codex CLI/2026-05-26-22915-3-of-4-tui-route-feature-and-memory-toggles-through-app-server-etraut-open|♯22915
  3 of 4 tui: route feature and memory toggles through app server @etraut-openai]]'
- '[[Changes/Gemini CLI/2026-05-27-chore-clean-up-launched-memory-features-by-sandytao520-in-https-github-com-googl|chore:
  clean up launched memory features]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b|codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b]]'
source_type: github_releases
theme: memory
title: 8 Memory and Personalization changes in rust-v0.135.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Memory and Personalization changes in rust-v0.135.0

**Codex CLI** · 2026-05-28 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.135.0) · from [[Releases/Codex CLI/codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b|0.135.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Moved memory runtime state into a dedicated SQLite database. (#24591)

> #24555 chore: drop orphaned codex memories MCP crate @jif-oai

> #24558 chore: move memory prompt builder into extension @jif-oai

> #24562 Add ad-hoc memory note tool @jif-oai

> #24567 Wire metrics client into memories extension @jif-oai

> #24583 Add memory tool call metrics to memories extension @jif-oai

> #24600 feat: gate dedicated memories tools in config @jif-oai

> #24591 Move memory state to a dedicated SQLite DB @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.135.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-28-4-context-window-changes-in-rust-v0-135-0|4 Context Window changes in rust-v0.135.0]] · Context Window
- [[Changes/Codex CLI/2026-05-28-14-apps-and-integrations-changes-in-rust-v0-135-0|14 Apps and Integrations changes in rust-v0.135.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-28-24714-fix-auto-review-skip-legacy-notify-for-auto-review-threads-dylan-hurd-oai|♯24714 fix(auto-review) skip legacy notify for auto review threads @dylan-hurd-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-05-28-5-mobile-and-desktop-changes-in-rust-v0-135-0|5 Mobile and Desktop changes in rust-v0.135.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-28-slash-command-completion-now-preserves-existing-draft-text-for-commands-that-acc|Slash-command completion now preserves existing draft text for commands that accept…]] · Editor Experience
- [[Changes/Codex CLI/2026-05-28-7-safety-and-privacy-changes-in-rust-v0-135-0|7 Safety and Privacy changes in rust-v0.135.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-28-codex-doctor-now-reports-richer-environment-git-terminal-app-server-and-thread-i|codex doctor now reports richer environment, Git, terminal, app-server, and thread…]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-28-63-other-changes-in-rust-v0-135-0|63 other changes in rust-v0.135.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-05-27 · Gemini CLI · [[Changes/Gemini CLI/2026-05-27-chore-clean-up-launched-memory-features-by-sandytao520-in-https-github-com-googl|chore: clean up launched memory features]]
- Later: 2026-05-28 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-28-vote-memory-tool-calls-are-throttled-per-response-and-per-interaction-to-prevent|vote_memory tool calls are throttled per response and per interaction to prevent…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-28-53704c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-28-8-memory-and-personalization-changes-in-rust-v0-135-0.md%0ACard%20ID%3A%20codex-cli-2026-05-28-53704c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.135.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->