---
card_id: codex-cli-2026-05-07-eda8b1
date: '2026-05-07'
description: 'Codex CLI · 2026-05-07 · Memory and Personalization: 16 changes in 0.129.0
  — #20600 chore: allow memories edition @jif-oai'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1022
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e6158b3bd7171d9a90985d241e253b4c462ba9abbb48102b2ab5f1ee49c58036
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-07-eda8b1
  comparison: ''
  date: '2026-05-07'
  description: 'Codex CLI — 0.129.0: 16 Memory and Personalization changes'
  evidence:
  - quote: '#20600 chore: allow memories edition @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20606 feat: seed ad-hoc memory extension instructions @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20622 feat: memories mcp v1 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20986 feat: add line offsets to memory read MCP @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20991 feat: add max_lines to memories MCP read @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20993 feat: paginate MCP memories list @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20994 feat: make memories MCP list shallow @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20996 feat: paginate memories MCP search results @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20997 feat: add context lines to memories MCP search @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21004 feat: support multi-query memories search @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21012 memories/mcp: generate tool schemas with schemars @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21010 memories-mcp: reject symlink traversal in local backend @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21201 memories-mcp: hide dot paths from list, read, and search @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21204 feat: support windowed multi-query memory search @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21205 feat: add normalized matching to memory search @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21214 chore: spawn MCP for memories @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 16-memory-and-personalization-changes-in-rust-v0-129-0
  source_release: codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e
  source_type: github_releases
  theme: memory
  title: 16 Memory and Personalization changes in rust-v0.129.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-04-30-12-memory-and-personalization-changes-in-rust-v0-128-0|12
  Memory and Personalization changes in rust-v0.128.0]]'
- '[[Changes/ChatGPT/2026-05-05-starting-today-we-re-rolling-out-memory-improvements-to-chatgpt-plus-and-pro-use|Memory
  sources and more personalized responses in ChatGPT]]'
- '[[Changes/Gemini CLI/2026-05-05-feat-memory-persist-auto-memory-scratchpad-for-skill-extraction-by-sandytao520-i|feat(memory):
  persist auto-memory scratchpad for skill extraction]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e|codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e]]'
source_type: github_releases
theme: memory
title: 16 Memory and Personalization changes in rust-v0.129.0
type: change
---

<!-- chronolog:begin region="header" -->
# 16 Memory and Personalization changes in rust-v0.129.0

**Codex CLI** · 2026-05-07 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.129.0) · from [[Releases/Codex CLI/codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e|0.129.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #20600 chore: allow memories edition @jif-oai

> #20606 feat: seed ad-hoc memory extension instructions @jif-oai

> #20622 feat: memories mcp v1 @jif-oai

> #20986 feat: add line offsets to memory read MCP @jif-oai

> #20991 feat: add max_lines to memories MCP read @jif-oai

> #20993 feat: paginate MCP memories list @jif-oai

> #20994 feat: make memories MCP list shallow @jif-oai

> #20996 feat: paginate memories MCP search results @jif-oai

> #20997 feat: add context lines to memories MCP search @jif-oai

> #21004 feat: support multi-query memories search @jif-oai

> #21012 memories/mcp: generate tool schemas with schemars @jif-oai

> #21010 memories-mcp: reject symlink traversal in local backend @jif-oai

> #21201 memories-mcp: hide dot paths from list, read, and search @jif-oai

> #21204 feat: support windowed multi-query memory search @jif-oai

> #21205 feat: add normalized matching to memory search @jif-oai

> #21214 chore: spawn MCP for memories @jif-oai

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
- [[Changes/Codex CLI/2026-05-07-11-safety-and-privacy-changes-in-rust-v0-129-0|11 Safety and Privacy changes in rust-v0.129.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-07-2-reliability-and-performance-changes-in-rust-v0-129-0|2 Reliability and Performance changes in rust-v0.129.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-05-07-137-other-changes-in-rust-v0-129-0|137 other changes in rust-v0.129.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-05-05 · Gemini CLI · [[Changes/Gemini CLI/2026-05-05-feat-memory-persist-auto-memory-scratchpad-for-skill-extraction-by-sandytao520-i|feat(memory): persist auto-memory scratchpad for skill extraction]]
- Later: 2026-05-09 · Open WebUI · [[Changes/Open WebUI/2026-05-09-faster-memory-query-performance-per-user-memory-lookups-and-deletions-now-run-mu|⚡ Faster memory query performance. Per-user memory lookups and deletions now run…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-07-eda8b1&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-07-16-memory-and-personalization-changes-in-rust-v0-129-0.md%0ACard%20ID%3A%20codex-cli-2026-05-07-eda8b1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.129.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->