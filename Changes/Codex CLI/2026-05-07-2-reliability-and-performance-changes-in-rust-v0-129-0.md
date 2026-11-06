---
card_id: codex-cli-2026-05-07-f46d09
date: '2026-05-07'
description: 'Codex CLI · 2026-05-07 · Reliability and Performance: 2 changes in 0.129.0
  — `/copy` works better in tmux, Alt+Enter and modified Delete/Backspace keys behave…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1239
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 380f75dd923a4c9a31ed71c2a5b793bacf3d83ed849ed72cced00dc56050d1d1
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-07-f46d09
  comparison: ''
  date: '2026-05-07'
  description: 'Codex CLI — 0.129.0: 2 Reliability and Performance changes'
  evidence:
  - quote: '`/copy` works better in tmux, Alt+Enter and modified Delete/Backspace
      keys behave correctly, and Windows typing/paste latency was reduced. (#20207,
      #20535, #21058, #18914)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20815 Speed up /side parent restore replay @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 2-reliability-and-performance-changes-in-rust-v0-129-0
  source_release: codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e
  source_type: github_releases
  theme: reliability-performance
  title: 2 Reliability and Performance changes in rust-v0.129.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-05-improve-stability-on-windows-by-working-around-a-v8-crash-in-node-24-x|Improve
  stability on Windows by working around a V8 crash in Node 24.x]]'
- '[[Changes/Claude Code/2026-05-06-updated-the-tui-fullscreen-startup-banner-to-describe-additional-renderer-benefi|Updated
  the /tui fullscreen startup banner to describe additional renderer…]]'
- '[[Changes/Claude Code/2026-05-07-improved-memory-usage-by-releasing-warm-spare-background-workers-under-memory-pr|Improved
  memory usage by releasing warm-spare background workers under memory pressure]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e|codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e]]'
source_type: github_releases
theme: reliability-performance
title: 2 Reliability and Performance changes in rust-v0.129.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Reliability and Performance changes in rust-v0.129.0

**Codex CLI** · 2026-05-07 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.129.0) · from [[Releases/Codex CLI/codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e|0.129.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `/copy` works better in tmux, Alt+Enter and modified Delete/Backspace keys behave correctly, and Windows typing/paste latency was reduced. (#20207, #20535, #21058, #18914)

> #20815 Speed up /side parent restore replay @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.129.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-07-5-agent-mode-changes-in-rust-v0-129-0|5 Agent Mode changes in rust-v0.129.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-07-39-apps-and-integrations-changes-in-rust-v0-129-0|39 Apps and Integrations changes in rust-v0.129.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-07-3-mobile-and-desktop-changes-in-rust-v0-129-0|3 Mobile and Desktop changes in rust-v0.129.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-07-3-collaboration-changes-in-rust-v0-129-0|3 Collaboration changes in rust-v0.129.0]] · Collaboration
- [[Changes/Codex CLI/2026-05-07-20065-feat-tui-redesign-session-picker-fcoury-oai|♯20065 feat(tui): redesign session picker @fcoury-oai]] · Interface Experience
- [[Changes/Codex CLI/2026-05-07-4-model-support-changes-in-rust-v0-129-0|4 Model Support changes in rust-v0.129.0]] · Model Support
- [[Changes/Codex CLI/2026-05-07-4-editor-experience-changes-in-rust-v0-129-0|4 Editor Experience changes in rust-v0.129.0]] · Editor Experience
- [[Changes/Codex CLI/2026-05-07-5-developer-workflow-changes-in-rust-v0-129-0|5 Developer Workflow changes in rust-v0.129.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-07-2-account-and-access-changes-in-rust-v0-129-0|2 Account and Access changes in rust-v0.129.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-07-7-context-window-changes-in-rust-v0-129-0|7 Context Window changes in rust-v0.129.0]] · Context Window
- [[Changes/Codex CLI/2026-05-07-tui-startup-and-accessibility-were-tightened-by-bounding-terminal-probes-clearin|TUI startup and accessibility were tightened by bounding terminal probes, clearing…]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-05-07-21379-document-codex-git-commit-attribution-config-henzelmann-oai|♯21379 Document Codex git commit attribution config @henzelmann-oai]] · Files and Data
- [[Changes/Codex CLI/2026-05-07-21054-rollout-store-web-search-and-mcp-tool-calls-owenlin0|♯21054 rollout: store web search and mcp tool calls @owenlin0]] · Search and Browsing
- [[Changes/Codex CLI/2026-05-07-16-memory-and-personalization-changes-in-rust-v0-129-0|16 Memory and Personalization changes in rust-v0.129.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-07-11-safety-and-privacy-changes-in-rust-v0-129-0|11 Safety and Privacy changes in rust-v0.129.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-07-137-other-changes-in-rust-v0-129-0|137 other changes in rust-v0.129.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-05-07 · Claude Code · [[Changes/Claude Code/2026-05-07-improved-memory-usage-by-releasing-warm-spare-background-workers-under-memory-pr|Improved memory usage by releasing warm-spare background workers under memory pressure]]
- Later: 2026-05-07 · Cursor · [[Changes/Cursor/2026-05-07-pin-skills-as-quick-actions|Pin skills as quick actions]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-07-f46d09&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-07-2-reliability-and-performance-changes-in-rust-v0-129-0.md%0ACard%20ID%3A%20codex-cli-2026-05-07-f46d09%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.129.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->