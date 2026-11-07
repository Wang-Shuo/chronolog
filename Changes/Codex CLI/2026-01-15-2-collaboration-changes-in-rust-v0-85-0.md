---
card_id: codex-cli-2026-01-15-0f6c33
date: '2026-01-15'
description: 'Codex CLI · 2026-01-15 · Collaboration: 2 changes in 0.85.0 — App-server
  v2 now emits collaboration tool calls as item events in the turn stream, so clients…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create
    a team here: (source link)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2561
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: eb749b077a223e1ab7046de38ad7c3620c6ddca714c58a837c0dd2f6be57a107
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
- '[[Changes/GitHub Copilot CLI/2026-01-07-add-share-and-share-gist-flags-for-session-sharing-in-non-interactive-mode|Add
  --share and --share-gist flags for session sharing in non-interactive mode]]'
- '[[Changes/OpenCode/2026-01-11-core-extract-external-directory-validation-to-shared-utility-to-reduce-code-dupl|Core
  Extract external directory validation to shared utility to reduce code…]]'
- '[[Changes/Microsoft 365 Copilot/2026-01-13-connect-microsoft-365-copilot-with-guru-for-enhanced-insights-web-microsoft-365|Connect
  Microsoft 365 Copilot with Guru for enhanced insights…]]'
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

- Earlier: 2026-01-13 · Microsoft 365 Copilot · [[Changes/Microsoft 365 Copilot/2026-01-13-connect-microsoft-365-copilot-with-guru-for-enhanced-insights-web-microsoft-365|Connect Microsoft 365 Copilot with Guru for enhanced insights…]]
- Later: 2026-01-15 · Granola · [[Changes/Granola/2026-01-15-granola-now-works-seamlessly-for-the-tens-of-millions-of-people-who-work-on-team|Sign in with Microsoft is here]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-01-11 · Descript · [[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create a team here: (source link)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-15-0f6c33&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-15-2-collaboration-changes-in-rust-v0-85-0.md%0ACard%20ID%3A%20codex-cli-2026-01-15-0f6c33%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.85.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->