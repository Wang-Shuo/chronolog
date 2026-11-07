---
card_id: codex-cli-2026-05-18-3ed557
date: '2026-05-18'
description: 'Codex CLI · 2026-05-18 · Memory and Personalization: 4 changes in 0.131.0
  — Continued extracting extension and tool internals, including shared tool contracts…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1033
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: eb4423e0fa48c3ab52e1e4335d577400e53e1f8b0aac0c2e37fccd42d94cdbc1
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-18-3ed557
  comparison: ''
  date: '2026-05-18'
  description: 'Codex CLI — 0.131.0: 4 Memory and Personalization changes'
  evidence:
  - quote: 'Continued extracting extension and tool internals, including shared tool
      contracts plus guardian and memory extension plumbing. (#21736, #21737, #21738,
      #22138, #22147, #22216, #22258, #22344, #22476, #22480, #22485, #22498)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22498 feat: memories ext @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22500 refactor: split memories extension crate modules @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22841 Move memory prompt injection to app-server extension @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-memory-and-personalization-changes-in-rust-v0-131-0
  source_release: codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d
  source_type: github_releases
  theme: memory
  title: 4 Memory and Personalization changes in rust-v0.131.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-07-16-memory-and-personalization-changes-in-rust-v0-129-0|16
  Memory and Personalization changes in rust-v0.129.0]]'
- '[[Changes/Open WebUI/2026-05-09-faster-memory-query-performance-per-user-memory-lookups-and-deletions-now-run-mu|⚡
  Faster memory query performance. Per-user memory lookups and deletions now run…]]'
- '[[Changes/Gemini CLI/2026-05-12-feat-memory-add-auto-memory-inbox-flow-with-canonical-patch-contract-by-sandytao|feat(memory):
  add Auto Memory inbox flow with canonical-patch contract]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d|codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d]]'
source_type: github_releases
theme: memory
title: 4 Memory and Personalization changes in rust-v0.131.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Memory and Personalization changes in rust-v0.131.0

**Codex CLI** · 2026-05-18 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.131.0) · from [[Releases/Codex CLI/codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d|0.131.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Continued extracting extension and tool internals, including shared tool contracts plus guardian and memory extension plumbing. (#21736, #21737, #21738, #22138, #22147, #22216, #22258, #22344, #22476, #22480, #22485, #22498)

> #22498 feat: memories ext @jif-oai

> #22500 refactor: split memories extension crate modules @jif-oai

> #22841 Move memory prompt injection to app-server extension @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.131.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-18-5-account-and-access-changes-in-rust-v0-131-0|5 Account and Access changes in rust-v0.131.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-18-17-safety-and-privacy-changes-in-rust-v0-131-0|17 Safety and Privacy changes in rust-v0.131.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-18-9-agent-mode-changes-in-rust-v0-131-0|9 Agent Mode changes in rust-v0.131.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-18-5-interface-experience-changes-in-rust-v0-131-0|5 Interface Experience changes in rust-v0.131.0]] · Interface Experience
- [[Changes/Codex CLI/2026-05-18-12-developer-workflow-changes-in-rust-v0-131-0|12 Developer Workflow changes in rust-v0.131.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-18-56-apps-and-integrations-changes-in-rust-v0-131-0|56 Apps and Integrations changes in rust-v0.131.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-18-21954-fix-goal-update-and-add-goal-edit-command-in-tui-etraut-openai|♯21954 Fix goal update and add /goal edit command in TUI @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-05-18-10-mobile-and-desktop-changes-in-rust-v0-131-0|10 Mobile and Desktop changes in rust-v0.131.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-18-7-context-window-changes-in-rust-v0-131-0|7 Context Window changes in rust-v0.131.0]] · Context Window
- [[Changes/Codex CLI/2026-05-18-3-collaboration-changes-in-rust-v0-131-0|3 Collaboration changes in rust-v0.131.0]] · Collaboration
- [[Changes/Codex CLI/2026-05-18-4-model-support-changes-in-rust-v0-131-0|4 Model Support changes in rust-v0.131.0]] · Model Support
- [[Changes/Codex CLI/2026-05-18-155-other-changes-in-rust-v0-131-0|155 other changes in rust-v0.131.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-05-12 · Gemini CLI · [[Changes/Gemini CLI/2026-05-12-feat-memory-add-auto-memory-inbox-flow-with-canonical-patch-contract-by-sandytao|feat(memory): add Auto Memory inbox flow with canonical-patch contract]]
- Later: 2026-05-18 · Lovable · [[Changes/Lovable/2026-05-18-security-memory|Security memory]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-18-3ed557&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-18-4-memory-and-personalization-changes-in-rust-v0-131-0.md%0ACard%20ID%3A%20codex-cli-2026-05-18-3ed557%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.131.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->