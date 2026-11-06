---
card_id: codex-cli-2026-06-18-c2cadb
date: '2026-06-18'
description: 'Codex CLI · 2026-06-18 · Memory and Personalization: 3 changes in 0.141.0
  — Reduced latency and memory use in large, tool-heavy sessions by caching tool search…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1064
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 90797986c89b9fbda0f4981b4a52bde922d1c340ff1f6951c24d84c65fc9a762
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-18-c2cadb
  comparison: ''
  date: '2026-06-18'
  description: 'Codex CLI — 0.141.0: 3 Memory and Personalization changes'
  evidence:
  - quote: 'Reduced latency and memory use in large, tool-heavy sessions by caching
      tool search and eliminating repeated request and history copies. (#27258, #27813,
      #28306, #28309, #28313, #28323, #28327)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28164 [codex] simplify memory read metrics @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28285 guardian: isolate review context from skills and memories @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-memory-and-personalization-changes-in-rust-v0-141-0
  source_release: codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75
  source_type: github_releases
  theme: memory
  title: 3 Memory and Personalization changes in rust-v0.141.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-06-13-allow-sdk-clients-to-configure-session-memory-through-session-create-and-session|Allow
  SDK clients to configure session memory through session.create and session.resume]]'
- '[[Changes/Codex CLI/2026-06-15-27129-feat-use-provider-defaults-for-memory-models-celia-oai|♯27129
  feat: use provider defaults for memory models @celia-oai]]'
- '[[Changes/Claude Code/2026-06-17-changed-the-improved-n-memories-line-to-no-longer-list-individual-files-outside|Changed
  the Improved N memories line to no longer list individual files outside…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75|codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75]]'
source_type: github_releases
theme: memory
title: 3 Memory and Personalization changes in rust-v0.141.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Memory and Personalization changes in rust-v0.141.0

**Codex CLI** · 2026-06-18 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.141.0) · from [[Releases/Codex CLI/codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75|0.141.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Reduced latency and memory use in large, tool-heavy sessions by caching tool search and eliminating repeated request and history copies. (#27258, #27813, #28306, #28309, #28313, #28323, #28327)

> #28164 [codex] simplify memory read metrics @pakrym-oai

> #28285 guardian: isolate review context from skills and memories @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.141.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-18-7-safety-and-privacy-changes-in-rust-v0-141-0|7 Safety and Privacy changes in rust-v0.141.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-18-5-agent-mode-changes-in-rust-v0-141-0|5 Agent Mode changes in rust-v0.141.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-18-7-developer-workflow-changes-in-rust-v0-141-0|7 Developer Workflow changes in rust-v0.141.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-18-tls-connections-now-support-p-521-certificate-signatures-commonly-used-by-enterp|TLS connections now support P-521 certificate signatures commonly used by enterprise…]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-06-18-28257-support-staging-oauth-client-id-overrides-apanasenko-oai|♯28257 Support staging OAuth client ID overrides @apanasenko-oai]] · Account and Access
- [[Changes/Codex CLI/2026-06-18-2-context-window-changes-in-rust-v0-141-0|2 Context Window changes in rust-v0.141.0]] · Context Window
- [[Changes/Codex CLI/2026-06-18-17-apps-and-integrations-changes-in-rust-v0-141-0|17 Apps and Integrations changes in rust-v0.141.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-18-28143-feat-app-server-expose-rate-limit-reset-credits-jayp-oai|♯28143 feat(app-server): expose rate-limit reset credits @jayp-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-06-18-42-other-changes-in-rust-v0-141-0|42 other changes in rust-v0.141.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-06-17 · Claude Code · [[Changes/Claude Code/2026-06-17-changed-the-improved-n-memories-line-to-no-longer-list-individual-files-outside|Changed the Improved N memories line to no longer list individual files outside…]]
- Later: 2026-06-18 · Cursor · [[Changes/Cursor/2026-06-18-you-can-now-delete-memory-files-in-the-ui-or-prompt-your-automation-to-delete-ou|Delete memory files in the UI, or prompt your automation to delete outdated memories…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-18-c2cadb&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-18-3-memory-and-personalization-changes-in-rust-v0-141-0.md%0ACard%20ID%3A%20codex-cli-2026-06-18-c2cadb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.141.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->