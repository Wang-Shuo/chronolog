---
card_id: codex-cli-2026-01-15-0f6c33
date: '2026-01-15'
description: 'Codex CLI · 2026-01-15 · Collaboration: 2 changes in 0.85.0 — App-server
  v2 now emits collaboration tool calls as item events in the turn stream, so clients…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 967
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3b8e16268218d850fa21db3309168d7cd3966ae6d7ecc0e353cf82fdf3ed5338
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-15-0f6c33
  comparison: ''
  date: '2026-01-15'
  description: 'Codex CLI — 0.85.0: 2 Collaboration changes'
  evidence:
  - quote: App-server v2 now emits collaboration tool calls as item events in the
      turn stream, so clients can render agent coordination in real time. (#9213)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.85.0
  - quote: 'Collaboration tools gained richer agent control: `spawn_agent` accepts
      an agent role preset, and `send_input` can optionally interrupt a running agent
      before delivering the message. (#9275, #9276)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.85.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 2-collaboration-changes-in-rust-v0-85-0
  source_release: codex-cli-2026-01-15-rust-v0-85-0-github-277157618-2b62da73
  source_type: github_releases
  theme: collaboration
  title: 2 Collaboration changes in rust-v0.85.0
  type: change
related_changes:
- '[[Changes/Cline/2025-12-16-migrate-whatsnewmodal-to-new-shared-dialogue-component|Migrate
  WhatsNewModal to new shared dialogue component]]'
- '[[Changes/Codex CLI/2025-12-18-8221-change-team-to-buisness-and-add-education|♯8221
  Change “Team” to “Buisness” and add Education]]'
- '[[Changes/GitHub Copilot CLI/2026-01-07-add-share-and-share-gist-flags-for-session-sharing-in-non-interactive-mode|Add
  --share and --share-gist flags for session sharing in non-interactive mode]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-15-rust-v0-85-0-github-277157618-2b62da73|codex-cli-2026-01-15-rust-v0-85-0-github-277157618-2b62da73]]'
source_type: github_releases
theme: collaboration
title: 2 Collaboration changes in rust-v0.85.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Collaboration changes in rust-v0.85.0

**Codex CLI** · 2026-01-15 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.85.0) · from [[Releases/Codex CLI/codex-cli-2026-01-15-rust-v0-85-0-github-277157618-2b62da73|0.85.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server v2 now emits collaboration tool calls as item events in the turn stream, so clients can render agent coordination in real time. (#9213)

> Collaboration tools gained richer agent control: `spawn_agent` accepts an agent role preset, and `send_input` can optionally interrupt a running agent before delivering the message. (#9275, #9276)

Source: https://github.com/openai/codex/releases/tag/rust-v0.85.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-15-9207-propagate-mcp-disabled-reason-gt-oai|♯9207 Propagate MCP disabled reason @gt-oai]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-15-revert-linux-sandboxing-now-falls-back-to-landlock-only-restrictions-when-user-n|revert Linux sandboxing now falls back to Landlock-only restrictions when user…]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-15-9275-feat-add-agent-roles-to-collab-tools-jif-oai|♯9275 feat: add agent roles to collab tools @jif-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-01-15-2-model-support-changes-in-rust-v0-85-0|2 Model Support changes in rust-v0.85.0]] · Model Support
- [[Changes/Codex CLI/2026-01-15-9-other-changes-in-rust-v0-85-0|9 other changes in rust-v0.85.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Collaboration

- Earlier: 2026-01-07 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-01-07-add-share-and-share-gist-flags-for-session-sharing-in-non-interactive-mode|Add --share and --share-gist flags for session sharing in non-interactive mode]]
- Later: 2026-01-16 · Codex CLI · [[Changes/Codex CLI/2026-01-16-collaboration-wait-calls-can-block-on-multiple-ids-in-one-request-simplifying-mu|Collaboration wait calls can block on multiple IDs in one request, simplifying…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-24 · ChatGPT · [[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-15-0f6c33&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-15-2-collaboration-changes-in-rust-v0-85-0.md%0ACard%20ID%3A%20codex-cli-2026-01-15-0f6c33%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.85.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->