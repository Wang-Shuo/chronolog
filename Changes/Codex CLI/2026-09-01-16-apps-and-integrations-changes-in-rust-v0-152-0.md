---
card_id: codex-cli-2026-09-01-e4dad4
date: '2026-09-01'
description: 'Codex CLI · 2026-09-01 · Apps and Integrations: 16 changes in 0.152.0
  — Individual MCP tools support an `output_token_limit` setting, with consistent…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2818
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 81748d4483d17631140693b37d1fed9eb694af38c2248bf651a1837d1e45c337
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-01-e4dad4
  comparison: ''
  date: '2026-09-01'
  description: 'Codex CLI — 0.152.0: 16 Apps and Integrations changes'
  evidence:
  - quote: Individual MCP tools support an `output_token_limit` setting, with consistent
      truncation across session resumes. (#41421)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: 'MCP tools remain available through cache refreshes and remote plugin changes;
      authentication retries use refreshed helper-provided headers. (#41336, #41344,
      #41396, #41400)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: Plugin recommendations begin loading during startup, reducing delays before
      the first turn. (#41375)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41230 Apply app routing policy to unauthenticated plugin reads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41231 Instrument the loaded plugin cache @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41313 Decouple HTTP retry backoff from overload integration testing @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41336 Preserve cached MCP tools during binding capture @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41344 Use refreshed MCP tool caches during binding capture @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41375 Preload plugin recommendations during session startup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41396 Refresh runtimes for remote plugin state changes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41400 Refresh MCP HTTP helper headers after authorization failures @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41421 Support per-tool MCP output limits @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41432 Run executor hooks for interrupted turns @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41456 Support app targets in executor plugin hooks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41683 Set working directories for environment MCP tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41700 Support package-style MCP server names @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 16-apps-and-integrations-changes-in-rust-v0-152-0
  source_release: codex-cli-2026-09-01-rust-v0-152-0-github-380164108-cd339544
  source_type: github_releases
  theme: apps-integrations
  title: 16 Apps and Integrations changes in rust-v0.152.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-08-31-2-apps-and-integrations-changes-in-v2026-8-1|2 Apps
  and Integrations changes in v2026.8.1]]'
- '[[Changes/ChatGPT/2026-09-01-eligible-chatgpt-for-clinicians-users-in-the-united-states-can-now-use-healthcar|Healthcare
  Public Data in ChatGPT for Clinicians]]'
- '[[Changes/Claude Code/2026-09-01-2-apps-and-integrations-changes-in-v2-1-257|2
  Apps and Integrations changes in v2.1.257]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-01-rust-v0-152-0-github-380164108-cd339544|codex-cli-2026-09-01-rust-v0-152-0-github-380164108-cd339544]]'
source_type: github_releases
theme: apps-integrations
title: 16 Apps and Integrations changes in rust-v0.152.0
type: change
---

<!-- chronolog:begin region="header" -->
# 16 Apps and Integrations changes in rust-v0.152.0

**Codex CLI** · 2026-09-01 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.152.0) · from [[Releases/Codex CLI/codex-cli-2026-09-01-rust-v0-152-0-github-380164108-cd339544|0.152.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Individual MCP tools support an `output_token_limit` setting, with consistent truncation across session resumes. (#41421)

> MCP tools remain available through cache refreshes and remote plugin changes; authentication retries use refreshed helper-provided headers. (#41336, #41344, #41396, #41400)

> Plugin recommendations begin loading during startup, reducing delays before the first turn. (#41375)

> #41230 Apply app routing policy to unauthenticated plugin reads @copyberry

> #41231 Instrument the loaded plugin cache @copyberry

> #41313 Decouple HTTP retry backoff from overload integration testing @copyberry

> #41336 Preserve cached MCP tools during binding capture @copyberry

> #41344 Use refreshed MCP tool caches during binding capture @copyberry

> #41375 Preload plugin recommendations during session startup @copyberry

> #41396 Refresh runtimes for remote plugin state changes @copyberry

> #41400 Refresh MCP HTTP helper headers after authorization failures @copyberry

> #41421 Support per-tool MCP output limits @copyberry

> #41432 Run executor hooks for interrupted turns @copyberry

> #41456 Support app targets in executor plugin hooks @copyberry

> #41683 Set working directories for environment MCP tests @copyberry

> #41700 Support package-style MCP server names @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.152.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-01-5-collaboration-changes-in-rust-v0-152-0|5 Collaboration changes in rust-v0.152.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-01-4-agent-mode-changes-in-rust-v0-152-0|4 Agent Mode changes in rust-v0.152.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-01-41457-source-proactive-multi-agent-instructions-from-the-model-catalog-copyberry|♯41457 Source proactive multi-agent instructions from the model catalog @copyberry]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-09-01-6-model-support-changes-in-rust-v0-152-0|6 Model Support changes in rust-v0.152.0]] · Model Support
- [[Changes/Codex CLI/2026-09-01-rate-limit-banners-offer-actions-for-checking-usage-managing-credits-resetting-l|Rate-limit banners offer actions for checking usage, managing credits, resetting…]] · Pricing Model
- [[Changes/Codex CLI/2026-09-01-6-developer-workflow-changes-in-rust-v0-152-0|6 Developer Workflow changes in rust-v0.152.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-01-9-context-window-changes-in-rust-v0-152-0|9 Context Window changes in rust-v0.152.0]] · Context Window
- [[Changes/Codex CLI/2026-09-01-41227-use-compatible-powershell-for-elevated-windows-sandbox-commands-copyberry|♯41227 Use compatible PowerShell for elevated Windows sandbox commands @copyberry]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-01-2-account-and-access-changes-in-rust-v0-152-0|2 Account and Access changes in rust-v0.152.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-01-3-interface-experience-changes-in-rust-v0-152-0|3 Interface Experience changes in rust-v0.152.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-01-50-other-changes-in-rust-v0-152-0|50 other changes in rust-v0.152.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-01 · Claude Code · [[Changes/Claude Code/2026-09-01-2-apps-and-integrations-changes-in-v2-1-257|2 Apps and Integrations changes in v2.1.257]]
- Later: 2026-09-01 · Lovable · [[Changes/Lovable/2026-09-01-connect-a-tool-from-a-pasted-api-key|Connect a tool from a pasted API key]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-01-e4dad4&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-01-16-apps-and-integrations-changes-in-rust-v0-152-0.md%0ACard%20ID%3A%20codex-cli-2026-09-01-e4dad4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.152.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->