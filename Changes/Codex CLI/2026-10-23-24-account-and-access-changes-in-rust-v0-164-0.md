---
card_id: codex-cli-2026-10-23-1e63e1
date: '2026-10-23'
description: 'Codex CLI · 2026-10-23 · Account and Access: 24 changes in 0.164.0 —
  Authenticate enterprise MCP connections using eligible Codex account grants or dedicated…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1303
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f441ab971298dd20c535e4eb5a5f477a983e66d741a0cef88dacabea79e0d68a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-23-1e63e1
  comparison: ''
  date: '2026-10-23'
  description: 'Codex CLI — 0.164.0: 24 Account and Access changes'
  evidence:
  - quote: 'Authenticate enterprise MCP connections using eligible Codex account grants
      or dedicated sign-in, including OAuth clients requiring secrets. (#55334, #55859,
      #56001)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: 'Windows HTTPS and WebSocket connections now handle proxy authentication
      challenges using the signed-in user’s Negotiate or NTLM credentials. (#55994,
      #56000)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54070 Expose gateway authentication as a reusable OAuth session API @smurching-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54079 Retire rejected MCP OAuth refresh tokens @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54170 Preserve ChatGPT authentication for Gov MCP servers @lsingh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54653 Prefer resource-specific scopes during MCP OAuth discovery @zamoshchin-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55296 Encapsulate Responses API proxy authentication @ee-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55320 Enable GitHub Actions OIDC authentication in the Responses API
      proxy @ee-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55397 Record OAuth provenance and login identity for account tokens @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55407 Clarify API key login and status messages @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55413 Share runtime authentication across requests and credential refreshes
      @cooper-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55546 Add scoped leases for persisted account OAuth grants @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55607 Propagate authentication header failures before sending requests
      @cooper-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55636 Add runtime assertion authentication modes and an auth provider
      @cooper-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55646 Guard auth persistence and reloads against concurrent login changes
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55680 Recheck account login ownership for enterprise MCP @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55698 Reuse Codex account grants for enterprise MCP authentication @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55701 Enable MCP OAuth refresh coordination by default @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55994 Add a Windows proxy authentication tunnel helper @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56000 Retry proxy CONNECT challenges with Windows authentication @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56001 Support confidential OAuth clients for enterprise-managed MCP auth
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56018 Avoid nested CLI startup in the MCP OAuth persistence test @goodman-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56023 Group Bedrock API key entry with other AWS sign-in methods @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56036 Add request-scoped OAuth credentials and session lifecycle APIs
      @smurching-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 24-account-and-access-changes-in-rust-v0-164-0
  source_release: codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d
  source_type: github_releases
  theme: account-access
  title: 24 Account and Access changes in rust-v0.164.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-20-4-account-and-access-changes-in-v1-0-101|4
  Account and Access changes in v1.0.101]]'
- '[[Changes/Claude Code/2026-10-21-2-account-and-access-changes-in-v2-1-307|2 Account
  and Access changes in v2.1.307]]'
- '[[Changes/OpenClaw/2026-10-22-mcp-sign-in-errors-now-give-a-safe-reason-and-tell-you-how-to-sign-in-or-fix-you|MCP
  sign-in errors now give a safe reason and tell you how to sign in or fix…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d|codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d]]'
source_type: github_releases
theme: account-access
title: 24 Account and Access changes in rust-v0.164.0
type: change
---

<!-- chronolog:begin region="header" -->
# 24 Account and Access changes in rust-v0.164.0

**Codex CLI** · 2026-10-23 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.164.0) · from [[Releases/Codex CLI/codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d|0.164.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Authenticate enterprise MCP connections using eligible Codex account grants or dedicated sign-in, including OAuth clients requiring secrets. (#55334, #55859, #56001)

> Windows HTTPS and WebSocket connections now handle proxy authentication challenges using the signed-in user’s Negotiate or NTLM credentials. (#55994, #56000)

> #54070 Expose gateway authentication as a reusable OAuth session API @smurching-oai

> #54079 Retire rejected MCP OAuth refresh tokens @mzeng-openai

> #54170 Preserve ChatGPT authentication for Gov MCP servers @lsingh-oai

> #54653 Prefer resource-specific scopes during MCP OAuth discovery @zamoshchin-openai

> #55296 Encapsulate Responses API proxy authentication @ee-oai

> #55320 Enable GitHub Actions OIDC authentication in the Responses API proxy @ee-oai

> #55397 Record OAuth provenance and login identity for account tokens @jif-oai

> #55407 Clarify API key login and status messages @fcoury-oai

> #55413 Share runtime authentication across requests and credential refreshes @cooper-oai

> #55546 Add scoped leases for persisted account OAuth grants @jif-oai

> #55607 Propagate authentication header failures before sending requests @cooper-oai

> #55636 Add runtime assertion authentication modes and an auth provider @cooper-oai

> #55646 Guard auth persistence and reloads against concurrent login changes @jif-oai

> #55680 Recheck account login ownership for enterprise MCP @jif-oai

> #55698 Reuse Codex account grants for enterprise MCP authentication @jif-oai

> #55701 Enable MCP OAuth refresh coordination by default @mzeng-openai

> #55994 Add a Windows proxy authentication tunnel helper @efrazer-oai

> #56000 Retry proxy CONNECT challenges with Windows authentication @efrazer-oai

> #56001 Support confidential OAuth clients for enterprise-managed MCP auth @jif-oai

> #56018 Avoid nested CLI startup in the MCP OAuth persistence test @goodman-oai

> #56023 Group Bedrock API key entry with other AWS sign-in methods @alexsong-oai

> #56036 Add request-scoped OAuth credentials and session lifecycle APIs @smurching-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.164.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-23-2-reliability-and-performance-changes-in-rust-v0-164-0|2 Reliability and Performance changes in rust-v0.164.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-10-23-8-collaboration-changes-in-rust-v0-164-0|8 Collaboration changes in rust-v0.164.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-23-4-memory-and-personalization-changes-in-rust-v0-164-0|4 Memory and Personalization changes in rust-v0.164.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-23-15-safety-and-privacy-changes-in-rust-v0-164-0|15 Safety and Privacy changes in rust-v0.164.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-23-13-agent-mode-changes-in-rust-v0-164-0|13 Agent Mode changes in rust-v0.164.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-23-2-image-generation-changes-in-rust-v0-164-0|2 Image Generation changes in rust-v0.164.0]] · Image Generation
- [[Changes/Codex CLI/2026-10-23-8-mobile-and-desktop-changes-in-rust-v0-164-0|8 Mobile and Desktop changes in rust-v0.164.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-23-18-context-window-changes-in-rust-v0-164-0|18 Context Window changes in rust-v0.164.0]] · Context Window
- [[Changes/Codex CLI/2026-10-23-30-apps-and-integrations-changes-in-rust-v0-164-0|30 Apps and Integrations changes in rust-v0.164.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-23-the-amazon-bedrock-setup-wizard-is-now-enabled-by-default-with-api-key-entry-gro|The Amazon Bedrock setup wizard is now enabled by default, with API key entry…]] · Account and Access
- [[Changes/Codex CLI/2026-10-23-9-interface-experience-changes-in-rust-v0-164-0|9 Interface Experience changes in rust-v0.164.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-23-9-model-support-changes-in-rust-v0-164-0|9 Model Support changes in rust-v0.164.0]] · Model Support
- [[Changes/Codex CLI/2026-10-23-14-developer-workflow-changes-in-rust-v0-164-0|14 Developer Workflow changes in rust-v0.164.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-23-3-voice-and-audio-changes-in-rust-v0-164-0|3 Voice and Audio changes in rust-v0.164.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-23-183-other-changes-in-rust-v0-164-0|183 other changes in rust-v0.164.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-10-22 · OpenClaw · [[Changes/OpenClaw/2026-10-22-mcp-sign-in-errors-now-give-a-safe-reason-and-tell-you-how-to-sign-in-or-fix-you|MCP sign-in errors now give a safe reason and tell you how to sign in or fix…]]
- Later: 2026-10-23 · Dify · [[Changes/Dify/2026-10-23-6-account-and-access-changes-in-1-18-0|6 Account and Access changes in 1.18.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-23-1e63e1&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-23-24-account-and-access-changes-in-rust-v0-164-0.md%0ACard%20ID%3A%20codex-cli-2026-10-23-1e63e1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.164.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->