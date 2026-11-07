---
card_id: codex-cli-2026-10-07-a2045e
date: '2026-10-07'
description: 'Codex CLI · 2026-10-07 · Account and Access: 10 changes in 0.161.0 —
  Sign in to MCP servers from an active terminal session with `/mcp login <name>`.
  (#49290)'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1287
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bb0476d1cb1d5c2bf89e83e3e32dfc6e56a63f2242f0d9c80ea7e42f57bdb8de
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-07-a2045e
  comparison: ''
  date: '2026-10-07'
  description: 'Codex CLI — 0.161.0: 10 Account and Access changes'
  evidence:
  - quote: Sign in to MCP servers from an active terminal session with `/mcp login
      <name>`. (#49290)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: 'Daybreak is opt-in through `--enable cli_daybreak` or `features.cli_daybreak=true`;
      `daybreak=true` alone is insufficient. By default, controls and indicators are
      hidden, `/daybreak` is unavailable, and automatic Cyber routing is omitted—even
      for saved Daybreak threads. Saved preferences remain intact. Opt-in routing
      requires eligible ChatGPT sign-in, the OpenAI provider, and advertised model/program
      support. (#49856, #49858, #49859, #49861, #51207)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: Authentication guidance now accounts for keyring storage instead of implying
      credentials always reside in `auth.json`. (#49361)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49276 Enable enterprise MCP sign-in and account-scoped grant cleanup
      @nicksteele-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49290 Add `/mcp login <name>` to the TUI @nicksteele-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49361 Clarify credential storage wording across authentication UI and
      docs @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49392 Add attributed MCP OAuth credential storage telemetry @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49432 Preserve bootstrap discovery across authentication changes @cooper-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49624 Use server authentication for explicit remote session commands
      @cooper-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49987 Add renewable EMA HTTP authentication and credential versioning
      @nicksteele-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 10-account-and-access-changes-in-rust-v0-161-0
  source_release: codex-cli-2026-10-07-rust-v0-161-0-github-405921402-d1f93f55
  source_type: github_releases
  theme: account-access
  title: 10 Account and Access changes in rust-v0.161.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-03-2-account-and-access-changes-in-v2026-9-8|2 Account
  and Access changes in v2026.9.8]]'
- '[[Changes/Claude Code/2026-10-05-3-account-and-access-changes-in-v2-1-290|3 Account
  and Access changes in v2.1.290]]'
- '[[Changes/GitHub Copilot CLI/2026-10-05-3-account-and-access-changes-in-v1-0-92|3
  Account and Access changes in v1.0.92]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-07-rust-v0-161-0-github-405921402-d1f93f55|codex-cli-2026-10-07-rust-v0-161-0-github-405921402-d1f93f55]]'
source_type: github_releases
theme: account-access
title: 10 Account and Access changes in rust-v0.161.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Account and Access changes in rust-v0.161.0

**Codex CLI** · 2026-10-07 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.161.0) · from [[Releases/Codex CLI/codex-cli-2026-10-07-rust-v0-161-0-github-405921402-d1f93f55|0.161.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Sign in to MCP servers from an active terminal session with `/mcp login <name>`. (#49290)

> Daybreak is opt-in through `--enable cli_daybreak` or `features.cli_daybreak=true`; `daybreak=true` alone is insufficient. By default, controls and indicators are hidden, `/daybreak` is unavailable, and automatic Cyber routing is omitted—even for saved Daybreak threads. Saved preferences remain intact. Opt-in routing requires eligible ChatGPT sign-in, the OpenAI provider, and advertised model/program support. (#49856, #49858, #49859, #49861, #51207)

> Authentication guidance now accounts for keyring storage instead of implying credentials always reside in `auth.json`. (#49361)

> #49276 Enable enterprise MCP sign-in and account-scoped grant cleanup @nicksteele-oai

> #49290 Add `/mcp login <name>` to the TUI @nicksteele-oai

> #49361 Clarify credential storage wording across authentication UI and docs @celia-oai

> #49392 Add attributed MCP OAuth credential storage telemetry @celia-oai

> #49432 Preserve bootstrap discovery across authentication changes @cooper-oai

> #49624 Use server authentication for explicit remote session commands @cooper-oai

> #49987 Add renewable EMA HTTP authentication and credential versioning @nicksteele-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.161.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-07-10-developer-workflow-changes-in-rust-v0-161-0|10 Developer Workflow changes in rust-v0.161.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-07-3-search-and-browsing-changes-in-rust-v0-161-0|3 Search and Browsing changes in rust-v0.161.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-10-07-9-safety-and-privacy-changes-in-rust-v0-161-0|9 Safety and Privacy changes in rust-v0.161.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-07-5-apps-and-integrations-changes-in-rust-v0-161-0|5 Apps and Integrations changes in rust-v0.161.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-07-49856-support-daybreak-selection-in-codex-exec-etraut-openai|♯49856 Support Daybreak selection in codex exec @etraut-openai]] · Interface Experience
- [[Changes/Codex CLI/2026-10-07-9-model-support-changes-in-rust-v0-161-0|9 Model Support changes in rust-v0.161.0]] · Model Support
- [[Changes/Codex CLI/2026-10-07-49876-remove-personality-plumbing-from-the-tui-etraut-openai|♯49876 Remove personality plumbing from the TUI @etraut-openai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-07-49473-use-the-rmcp-sdk-for-enterprise-managed-token-exchanges-nicksteele-oai|♯49473 Use the rmcp SDK for enterprise-managed token exchanges @nicksteele-oai]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-10-07-9-agent-mode-changes-in-rust-v0-161-0|9 Agent Mode changes in rust-v0.161.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-07-4-voice-and-audio-changes-in-rust-v0-161-0|4 Voice and Audio changes in rust-v0.161.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-07-9-context-window-changes-in-rust-v0-161-0|9 Context Window changes in rust-v0.161.0]] · Context Window
- [[Changes/Codex CLI/2026-10-07-2-collaboration-changes-in-rust-v0-161-0|2 Collaboration changes in rust-v0.161.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-07-93-other-changes-in-rust-v0-161-0|93 other changes in rust-v0.161.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-10-05 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-05-3-account-and-access-changes-in-v1-0-92|3 Account and Access changes in v1.0.92]]
- Later: 2026-10-07 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-07-2-account-and-access-changes-in-v1-0-93|2 Account and Access changes in v1.0.93]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-07-a2045e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-07-10-account-and-access-changes-in-rust-v0-161-0.md%0ACard%20ID%3A%20codex-cli-2026-10-07-a2045e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.161.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->