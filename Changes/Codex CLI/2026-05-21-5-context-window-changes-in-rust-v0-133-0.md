---
card_id: codex-cli-2026-05-21-7c8676
date: '2026-05-21'
description: 'Codex CLI · 2026-05-21 · Context Window: 5 changes in 0.133.0 — Preserved
  raw code-mode exec output unless an explicit output token limit is requested. (#23564)'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1113
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7a36a2c6dc05fe12c0aaa2e50a4abe8440c6192b7828f37a87cf469e43124eb4
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-21-7c8676
  comparison: ''
  date: '2026-05-21'
  description: 'Codex CLI — 0.133.0: 5 Context Window changes'
  evidence:
  - quote: Preserved raw code-mode exec output unless an explicit output token limit
      is requested. (#23564)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23352 Preserve context baselines for full-history agent forks @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22870 Add `body_after_prefix` auto-compact token limit scope @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23451 Add timeout for remote compaction requests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23634 runtime: use install context for bundled bwrap @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-context-window-changes-in-rust-v0-133-0
  source_release: codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc
  source_type: github_releases
  theme: context-window
  title: 5 Context Window changes in rust-v0.133.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-19-document-attachment-paths-are-included-in-context-so-the-agent-can-reference-pas|Document
  attachment paths are included in context so the agent can reference pasted…]]'
- '[[Changes/GitHub Copilot CLI/2026-05-20-customizable-status-line-in-the-terminal-footer-displays-session-info-such-as-mo|Customizable
  status line in the terminal footer displays session info such as model…]]'
- '[[Changes/OpenCode/2026-05-20-core-zed-editor-context-now-only-activates-inside-zed-terminals|Core
  Zed editor context now only activates inside Zed terminals]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc|codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc]]'
source_type: github_releases
theme: context-window
title: 5 Context Window changes in rust-v0.133.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Context Window changes in rust-v0.133.0

**Codex CLI** · 2026-05-21 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.133.0) · from [[Releases/Codex CLI/codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc|0.133.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Preserved raw code-mode exec output unless an explicit output token limit is requested. (#23564)

> #23352 Preserve context baselines for full-history agent forks @jif-oai

> #22870 Add `body_after_prefix` auto-compact token limit scope @jif-oai

> #23451 Add timeout for remote compaction requests @jif-oai

> #23634 runtime: use install context for bundled bwrap @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.133.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-21-7-agent-mode-changes-in-rust-v0-133-0|7 Agent Mode changes in rust-v0.133.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-21-20-apps-and-integrations-changes-in-rust-v0-133-0|20 Apps and Integrations changes in rust-v0.133.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-21-3-developer-workflow-changes-in-rust-v0-133-0|3 Developer Workflow changes in rust-v0.133.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-21-18868-add-mitm-hook-config-model-evawong-oai|♯18868 Add MITM hook config model @evawong-oai]] · Model Support
- [[Changes/Codex CLI/2026-05-21-23578-fix-app-server-speed-up-shutdown-fcoury-oai|♯23578 fix(app-server): speed up shutdown @fcoury-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-05-21-17-safety-and-privacy-changes-in-rust-v0-133-0|17 Safety and Privacy changes in rust-v0.133.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-21-79-other-changes-in-rust-v0-133-0|79 other changes in rust-v0.133.0]] · Other changes
- [[Changes/Codex CLI/2026-05-21-goals-are-now-enabled-by-default-backed-by-dedicated-storage-and-track-progress|Goals are now enabled by default, backed by dedicated storage, and track progress…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-05-20 · OpenCode · [[Changes/OpenCode/2026-05-20-core-zed-editor-context-now-only-activates-inside-zed-terminals|Core Zed editor context now only activates inside Zed terminals]]
- Later: 2026-05-22 · Claude Code · [[Changes/Claude Code/2026-05-22-improved-feedback-reports-to-include-the-conversation-that-happened-before-conte|Improved /feedback reports to include the conversation that happened before…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-21-7c8676&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-21-5-context-window-changes-in-rust-v0-133-0.md%0ACard%20ID%3A%20codex-cli-2026-05-21-7c8676%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.133.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->