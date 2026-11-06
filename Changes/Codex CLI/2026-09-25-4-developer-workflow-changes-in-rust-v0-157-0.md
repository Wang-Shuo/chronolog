---
card_id: codex-cli-2026-09-25-9edf5b
date: '2026-09-25'
description: 'Codex CLI · 2026-09-25 · Developer Workflow: 4 changes in 0.157.0 —
  Improved terminal rendering with Unicode bullets, checkboxes, aligned equations,
  and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1287
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 43377135c436c28621f8b4b7f7f6842949d6128325a32c7a65148a28b9080528
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-25-9edf5b
  comparison: ''
  date: '2026-09-25'
  description: 'Codex CLI — 0.157.0: 4 Developer Workflow changes'
  evidence:
  - quote: 'Improved terminal rendering with Unicode bullets, checkboxes, aligned
      equations, and optimization notation. (#47191, #47322)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: 'Respected tmux mouse settings and restored native scrollback for Terminal.app
      over SSH in automatic screen mode. (#47399, #47417)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47360 Preserve user prompt URL destinations across terminal widths @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47417 Use native scrollback for Terminal.app over SSH in auto mode @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-developer-workflow-changes-in-rust-v0-157-0
  source_release: codex-cli-2026-09-25-rust-v0-157-0-github-396234532-e8248ab3
  source_type: github_releases
  theme: developer-workflow
  title: 4 Developer Workflow changes in rust-v0.157.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-24-changed-windows-wsl-managed-settings-so-an-admin-policy-that-is-present-but-inva|Changed
  Windows/WSL managed settings so an admin policy that is present but invalid…]]'
- '[[Changes/Cline/2026-09-24-a-command-that-prints-nothing-no-longer-shows-a-raw-json-blob-like-query-git-add|A
  command that prints nothing no longer shows a raw JSON blob like…]]'
- '[[Changes/Claude Code/2026-09-25-3-developer-workflow-changes-in-v2-1-283|3 Developer
  Workflow changes in v2.1.283]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-25-rust-v0-157-0-github-396234532-e8248ab3|codex-cli-2026-09-25-rust-v0-157-0-github-396234532-e8248ab3]]'
source_type: github_releases
theme: developer-workflow
title: 4 Developer Workflow changes in rust-v0.157.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Developer Workflow changes in rust-v0.157.0

**Codex CLI** · 2026-09-25 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.157.0) · from [[Releases/Codex CLI/codex-cli-2026-09-25-rust-v0-157-0-github-396234532-e8248ab3|0.157.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved terminal rendering with Unicode bullets, checkboxes, aligned equations, and optimization notation. (#47191, #47322)

> Respected tmux mouse settings and restored native scrollback for Terminal.app over SSH in automatic screen mode. (#47399, #47417)

> #47360 Preserve user prompt URL destinations across terminal widths @fcoury-oai

> #47417 Use native scrollback for Terminal.app over SSH in auto mode @fcoury-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.157.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-25-9-apps-and-integrations-changes-in-rust-v0-157-0|9 Apps and Integrations changes in rust-v0.157.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-25-47411-apply-shared-network-policy-throughout-embedded-codex-startup-acrognale-oa|♯47411 Apply shared network policy throughout embedded Codex startup @acrognale-oai]] · Collaboration
- [[Changes/Codex CLI/2026-09-25-6-context-window-changes-in-rust-v0-157-0|6 Context Window changes in rust-v0.157.0]] · Context Window
- [[Changes/Codex CLI/2026-09-25-47086-format-analytics-credit-usage-with-consistent-decimal-precision-fcoury-oai|♯47086 Format analytics credit usage with consistent decimal precision @fcoury-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-09-25-2-safety-and-privacy-changes-in-rust-v0-157-0|2 Safety and Privacy changes in rust-v0.157.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-25-8-model-support-changes-in-rust-v0-157-0|8 Model Support changes in rust-v0.157.0]] · Model Support
- [[Changes/Codex CLI/2026-09-25-9-interface-experience-changes-in-rust-v0-157-0|9 Interface Experience changes in rust-v0.157.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-25-added-retries-for-transient-file-upload-failures-and-increased-the-upload-timeou|Added retries for transient file-upload failures and increased the upload timeout…]] · Files and Data
- [[Changes/Codex CLI/2026-09-25-47327-preserve-image-generation-request-ids-on-failure-chrisdong-oai|♯47327 Preserve image generation request IDs on failure @chrisdong-oai]] · Image Generation
- [[Changes/Codex CLI/2026-09-25-5-voice-and-audio-changes-in-rust-v0-157-0|5 Voice and Audio changes in rust-v0.157.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-25-2-search-and-browsing-changes-in-rust-v0-157-0|2 Search and Browsing changes in rust-v0.157.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-09-25-13-agent-mode-changes-in-rust-v0-157-0|13 Agent Mode changes in rust-v0.157.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-25-5-account-and-access-changes-in-rust-v0-157-0|5 Account and Access changes in rust-v0.157.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-25-70-other-changes-in-rust-v0-157-0|70 other changes in rust-v0.157.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-25 · Claude Code · [[Changes/Claude Code/2026-09-25-3-developer-workflow-changes-in-v2-1-283|3 Developer Workflow changes in v2.1.283]]
- Later: 2026-09-28 · Claude Code · [[Changes/Claude Code/2026-09-28-changed-recap-to-decline-with-a-short-notice-when-it-arrives-relayed-from-a-chat|Changed /recap to decline with a short notice when it arrives relayed from a chat…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-25-9edf5b&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-25-4-developer-workflow-changes-in-rust-v0-157-0.md%0ACard%20ID%3A%20codex-cli-2026-09-25-9edf5b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.157.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->