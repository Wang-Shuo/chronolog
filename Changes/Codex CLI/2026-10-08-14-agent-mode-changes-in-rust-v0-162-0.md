---
card_id: codex-cli-2026-10-08-a6f7c9
date: '2026-10-08'
description: 'Codex CLI · 2026-10-08 · Agent Mode: 14 changes in 0.162.0 — Pin tasks
  in the agent Command Center with `p` and keep them in a shared Pinned group when…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1190
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b4294b41a85f1ce2073fa463d452ba074173c4cd6ccf26200019fc5182c73aed
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-08-a6f7c9
  comparison: ''
  date: '2026-10-08'
  description: 'Codex CLI — 0.162.0: 14 Agent Mode changes'
  evidence:
  - quote: Pin tasks in the agent Command Center with `p` and keep them in a shared
      Pinned group when supported by the server. (#51500)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50082 Enable dynamic tool inheritance for fresh V2 subagents @ke-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50087 Preserve queued agent mail across session eviction @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51064 Ignore stale refresh responses in agents overview tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51206 Record initialization analytics for resumed subagents @peilin-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51249 Handle partial answers consistently across agent workflows @rb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51329 Remove partial-history subagent forks @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51331 Track sub-agent result delivery outcomes @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51332 Record multi-agent wait duration by outcome @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51333 Record the multi-agent version in turn analytics @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51355 Add bounded diagnostics for agent spawn failures @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51463 Record resolved model and reasoning effort in sub-agent activity
      @sdcoffey'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51500 Add shared task pinning to the agent command center @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51515 Expose detailed agent tree shutdown failure reports @keitht-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 14-agent-mode-changes-in-rust-v0-162-0
  source_release: codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db
  source_type: github_releases
  theme: agent-mode
  title: 14 Agent Mode changes in rust-v0.162.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-07-clicking-a-truncated-compact-shell-command-expands-it|Clicking
  a truncated compact shell command expands it]]'
- '[[Changes/Google Antigravity/2026-10-07-2-agent-mode-changes-in-hub-v2-21-1-advanced-search|2
  Agent Mode changes in HUB v2.21.1 — Advanced Search…]]'
- '[[Changes/Claude Code/2026-10-08-4-agent-mode-changes-in-v2-1-295|4 Agent Mode
  changes in v2.1.295]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db|codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db]]'
source_type: github_releases
theme: agent-mode
title: 14 Agent Mode changes in rust-v0.162.0
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Agent Mode changes in rust-v0.162.0

**Codex CLI** · 2026-10-08 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.162.0) · from [[Releases/Codex CLI/codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db|0.162.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Pin tasks in the agent Command Center with `p` and keep them in a shared Pinned group when supported by the server. (#51500)

> #50082 Enable dynamic tool inheritance for fresh V2 subagents @ke-oai

> #50087 Preserve queued agent mail across session eviction @jif-oai

> #51064 Ignore stale refresh responses in agents overview tests @jif-oai

> #51206 Record initialization analytics for resumed subagents @peilin-openai

> #51249 Handle partial answers consistently across agent workflows @rb-oai

> #51329 Remove partial-history subagent forks @jif-oai

> #51331 Track sub-agent result delivery outcomes @jif-oai

> #51332 Record multi-agent wait duration by outcome @jif-oai

> #51333 Record the multi-agent version in turn analytics @jif-oai

> #51355 Add bounded diagnostics for agent spawn failures @jif-oai

> #51463 Record resolved model and reasoning effort in sub-agent activity @sdcoffey

> #51500 Add shared task pinning to the agent command center @etraut-openai

> #51515 Expose detailed agent tree shutdown failure reports @keitht-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.162.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-08-51223-remove-legacy-personality-template-metadata-rhan-oai|♯51223 Remove legacy personality template metadata @rhan-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-08-3-reliability-and-performance-changes-in-rust-v0-162-0|3 Reliability and Performance changes in rust-v0.162.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-10-08-2-voice-and-audio-changes-in-rust-v0-162-0|2 Voice and Audio changes in rust-v0.162.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-08-10-context-window-changes-in-rust-v0-162-0|10 Context Window changes in rust-v0.162.0]] · Context Window
- [[Changes/Codex CLI/2026-10-08-50216-use-the-shared-text-editor-for-command-center-task-renaming-bc-openai|♯50216 Use the shared text editor for command-center task renaming @bc-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-10-08-13-safety-and-privacy-changes-in-rust-v0-162-0|13 Safety and Privacy changes in rust-v0.162.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-08-20-apps-and-integrations-changes-in-rust-v0-162-0|20 Apps and Integrations changes in rust-v0.162.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-08-50384-allow-opting-into-16-kib-arm64-code-pages-for-macos-signing-chess-oai|♯50384 Allow opting into 16 KiB ARM64 code pages for macOS signing @chess-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-08-8-interface-experience-changes-in-rust-v0-162-0|8 Interface Experience changes in rust-v0.162.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-08-12-developer-workflow-changes-in-rust-v0-162-0|12 Developer Workflow changes in rust-v0.162.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-08-11-model-support-changes-in-rust-v0-162-0|11 Model Support changes in rust-v0.162.0]] · Model Support
- [[Changes/Codex CLI/2026-10-08-2-account-and-access-changes-in-rust-v0-162-0|2 Account and Access changes in rust-v0.162.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-08-2-collaboration-changes-in-rust-v0-162-0|2 Collaboration changes in rust-v0.162.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-08-137-other-changes-in-rust-v0-162-0|137 other changes in rust-v0.162.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-08 · Claude Code · [[Changes/Claude Code/2026-10-08-4-agent-mode-changes-in-v2-1-295|4 Agent Mode changes in v2.1.295]]
- Later: 2026-10-08 · OpenClaw · [[Changes/OpenClaw/2026-10-08-4-agent-mode-changes-in-v2026-9-9|4 Agent Mode changes in v2026.9.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-08-a6f7c9&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-08-14-agent-mode-changes-in-rust-v0-162-0.md%0ACard%20ID%3A%20codex-cli-2026-10-08-a6f7c9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.162.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->