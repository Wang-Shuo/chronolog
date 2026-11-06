---
card_id: codex-cli-2026-04-11-d11b81
date: '2026-04-11'
description: 'Codex CLI · 2026-04-11 · Other changes: 23 changes in 0.120.0 — Custom
  TUI status lines can include the renamed thread title (#17187)'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5b24f9d4cf05e45ddf6d39180e3074c6b2eb5609fe2a7dc41dfde9b8ebbb2c96
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-11-d11b81
  comparison: ''
  date: '2026-04-11'
  description: 'Codex CLI — 0.120.0: 23 other changes'
  evidence:
  - quote: Custom TUI status lines can include the renamed thread title (#17187)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: Updated app-server protocol documentation for the new `/clear` SessionStart
      source (#17073)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: Made rollout recording more reliable by retrying failed flushes and surfacing
      durability failures instead of dropping buffered items (#17214)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: Improved Guardian follow-up efficiency by sending transcript deltas instead
      of repeatedly resending full history (#17269)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: Added stable Guardian review IDs across app-server events and internal
      approval state (#17298)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#17267 Stop Realtime V2 response.done delegation @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#17189 Emit live hook prompts before raw-event filtering @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#17288 Install rustls provider for remote websocket client @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#16969 Option to Notify Workspace Owner When Usage Limit is Reached @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#17280 Extract realtime input task handlers @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#17249 adding parent_thread_id in guardian @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#17210 Add output_schema to code mode render @vivi'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#16344 feat: move exec-server ownership @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#17214 feat: make rollout recorder reliable against errors @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#17269 feat(guardian): send only transcript deltas on guardian followups
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#17306 Queue Realtime V2 response.create while active @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#17352 fix: main @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#17363 Strengthen realtime backend delegation prompt @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#17073 Support clear SessionStart source @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#17298 fix(guardian, app-server): introduce guardian review ids @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#17391 Revert "Option to Notify Workspace Owner When Usage Limit is Reached"
      @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#17371 app-server: add pipelined config rpc regression test @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  - quote: '#17055 feat(analytics): add guardian review event schema @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.120.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 23-other-changes-in-rust-v0-120-0
  source_release: codex-cli-2026-04-11-rust-v0-120-0-github-307789275-437473b9
  source_type: github_releases
  theme: uncategorized
  title: 23 other changes in rust-v0.120.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-11-rust-v0-120-0-github-307789275-437473b9|codex-cli-2026-04-11-rust-v0-120-0-github-307789275-437473b9]]'
source_type: github_releases
theme: uncategorized
title: 23 other changes in rust-v0.120.0
type: change
---

<!-- chronolog:begin region="header" -->
# 23 other changes in rust-v0.120.0

**Codex CLI** · 2026-04-11 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.120.0) · from [[Releases/Codex CLI/codex-cli-2026-04-11-rust-v0-120-0-github-307789275-437473b9|0.120.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Custom TUI status lines can include the renamed thread title (#17187)

> Updated app-server protocol documentation for the new `/clear` SessionStart source (#17073)

> Made rollout recording more reliable by retrying failed flushes and surfacing durability failures instead of dropping buffered items (#17214)

> Improved Guardian follow-up efficiency by sending transcript deltas instead of repeatedly resending full history (#17269)

> Added stable Guardian review IDs across app-server events and internal approval state (#17298)

> #17267 Stop Realtime V2 response.done delegation @aibrahim-oai

> #17189 Emit live hook prompts before raw-event filtering @abhinav-oai

> #17288 Install rustls provider for remote websocket client @etraut-openai

> #16969 Option to Notify Workspace Owner When Usage Limit is Reached @richardopenai

> #17280 Extract realtime input task handlers @aibrahim-oai

> #17249 adding parent_thread_id in guardian @won-openai

> #17210 Add output_schema to code mode render @vivi

> #16344 feat: move exec-server ownership @jif-oai

> #17214 feat: make rollout recorder reliable against errors @jif-oai

> #17269 feat(guardian): send only transcript deltas on guardian followups @owenlin0

> #17306 Queue Realtime V2 response.create while active @aibrahim-oai

> #17352 fix: main @jif-oai

> #17363 Strengthen realtime backend delegation prompt @aibrahim-oai

> #17073 Support clear SessionStart source @abhinav-oai

> #17298 fix(guardian, app-server): introduce guardian review ids @owenlin0

> #17391 Revert "Option to Notify Workspace Owner When Usage Limit is Reached" @shijie-oai

> #17371 app-server: add pipelined config rpc regression test @euroelessar

> #17055 feat(analytics): add guardian review event schema @owenlin0

Source: https://github.com/openai/codex/releases/tag/rust-v0.120.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-11-3-context-window-changes-in-rust-v0-120-0|3 Context Window changes in rust-v0.120.0]] · Context Window
- [[Changes/Codex CLI/2026-04-11-2-interface-experience-changes-in-rust-v0-120-0|2 Interface Experience changes in rust-v0.120.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-11-4-apps-and-integrations-changes-in-rust-v0-120-0|4 Apps and Integrations changes in rust-v0.120.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-11-4-safety-and-privacy-changes-in-rust-v0-120-0|4 Safety and Privacy changes in rust-v0.120.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-11-4-agent-mode-changes-in-rust-v0-120-0|4 Agent Mode changes in rust-v0.120.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-11-sessionstart-hooks-can-distinguish-sessions-created-by-clear-from-fresh-startup|SessionStart hooks can distinguish sessions created by /clear from fresh startup…]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-04-11-2-search-and-browsing-changes-in-rust-v0-120-0|2 Search and Browsing changes in rust-v0.120.0]] · Search and Browsing
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-11-d11b81&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-11-23-other-changes-in-rust-v0-120-0.md%0ACard%20ID%3A%20codex-cli-2026-04-11-d11b81%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.120.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->