---
card_id: codex-cli-2026-09-25-fd7c4e
date: '2026-09-25'
description: 'Codex CLI · 2026-09-25 · Account and Access: 5 changes in 0.157.0 —
  #47158 Harden gateway OAuth credential persistence and error redaction @alexsong-oai'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2250
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 89831d141e092e38383d2b704b2a50726907c464c97f85cd47f0ed7cde371880
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-25-fd7c4e
  comparison: ''
  date: '2026-09-25'
  description: 'Codex CLI — 0.157.0: 5 Account and Access changes'
  evidence:
  - quote: '#47158 Harden gateway OAuth credential persistence and error redaction
      @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47170 Add explicit gateway login control and authentication status @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47207 Add explicit gateway OAuth sign-in to app-server @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47326 Restrict MCP OAuth authorization endpoints to HTTP(S) @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47413 Cache decrypted gateway OAuth secrets per backend @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-account-and-access-changes-in-rust-v0-157-0
  source_release: codex-cli-2026-09-25-rust-v0-157-0-github-396234532-e8248ab3
  source_type: github_releases
  theme: account-access
  title: 5 Account and Access changes in rust-v0.157.0
  type: change
related_changes:
- '[[Changes/Devin/2026-09-23-bring-your-own-oauth-setup-guides-for-microsoft-365-and-google-workspace-mcps|Bring-Your-Own
  OAuth Setup Guides for Microsoft 365 and Google Workspace MCPs]]'
- '[[Changes/OpenClaw/2026-09-23-17-account-and-access-changes-in-v2026-9-6|17 Account
  and Access changes in v2026.9.6]]'
- '[[Changes/Qoder/2026-09-23-network-proxy-added-support-for-http-https-proxy-urls-containing-a-username-and|Network
  proxy: Added support for HTTP/HTTPS proxy URLs containing a username…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-25-rust-v0-157-0-github-396234532-e8248ab3|codex-cli-2026-09-25-rust-v0-157-0-github-396234532-e8248ab3]]'
source_type: github_releases
theme: account-access
title: 5 Account and Access changes in rust-v0.157.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Account and Access changes in rust-v0.157.0

**Codex CLI** · 2026-09-25 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.157.0) · from [[Releases/Codex CLI/codex-cli-2026-09-25-rust-v0-157-0-github-396234532-e8248ab3|0.157.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #47158 Harden gateway OAuth credential persistence and error redaction @alexsong-oai

> #47170 Add explicit gateway login control and authentication status @alexsong-oai

> #47207 Add explicit gateway OAuth sign-in to app-server @alexsong-oai

> #47326 Restrict MCP OAuth authorization endpoints to HTTP(S) @viyatb-oai

> #47413 Cache decrypted gateway OAuth secrets per backend @charliemarsh-oai

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
- [[Changes/Codex CLI/2026-09-25-4-developer-workflow-changes-in-rust-v0-157-0|4 Developer Workflow changes in rust-v0.157.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-25-2-search-and-browsing-changes-in-rust-v0-157-0|2 Search and Browsing changes in rust-v0.157.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-09-25-13-agent-mode-changes-in-rust-v0-157-0|13 Agent Mode changes in rust-v0.157.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-25-70-other-changes-in-rust-v0-157-0|70 other changes in rust-v0.157.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-09-23 · Qoder · [[Changes/Qoder/2026-09-23-network-proxy-added-support-for-http-https-proxy-urls-containing-a-username-and|Network proxy: Added support for HTTP/HTTPS proxy URLs containing a username…]]
- Later: 2026-09-28 · Claude Code · [[Changes/Claude Code/2026-09-28-added-mcp-reconnect-all-in-the-interactive-terminal-to-retry-every-mcp-server-th|Added /mcp reconnect all in the interactive terminal to retry every MCP server…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-25-fd7c4e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-25-5-account-and-access-changes-in-rust-v0-157-0.md%0ACard%20ID%3A%20codex-cli-2026-09-25-fd7c4e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.157.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->