---
card_id: codex-cli-2026-01-31-c696ec
date: '2026-01-31'
description: 'Codex CLI · 2026-01-31 · Safety and Privacy: 4 changes in 0.93.0 — #9992
  update pnpm to 10.28.2 to address security issues @mjr-openai'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2013
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 42f16c5eb07262dc653e63e3b381103c42abb4aa75d5e41d865202b76813a46d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-31-c696ec
  comparison: ''
  date: '2026-01-31'
  description: 'Codex CLI — 0.93.0: 4 Safety and Privacy changes'
  evidence:
  - quote: '#9992 update pnpm to 10.28.2 to address security issues @mjr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9797 remove sandbox globals. @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10008 enable live web search for DangerFullAccess sandbox policy @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10028 allow elevated sandbox to be enabled without base experimental
      flag @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-safety-and-privacy-changes-in-rust-v0-93-0
  source_release: codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in rust-v0.93.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-01-29-core-allow-media-src-data-url-for-small-audio-files-in-content-security-policy|Core
  Allow media-src data: URL for small audio files in Content Security Policy]]'
- '[[Changes/Claude Code/2026-01-30-permissions-now-respect-content-level-ask-over-tool-level-allow-previously-allow|Permissions
  now respect content-level ask over tool-level allow]]'
- '[[Changes/GitHub Copilot CLI/2026-01-30-acp-server-support-permission-flags-yolo-allow-all-etc-and-permissions-config|ACP
  server support permission flags: --yolo, --allow-all, etc. and permissions config]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8|codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in rust-v0.93.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in rust-v0.93.0

**Codex CLI** · 2026-01-31 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.93.0) · from [[Releases/Codex CLI/codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8|0.93.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #9992 update pnpm to 10.28.2 to address security issues @mjr-openai

> #9797 remove sandbox globals. @iceweasel-oai

> #10008 enable live web search for DangerFullAccess sandbox policy @sayan-oai

> #10028 allow elevated sandbox to be enabled without base experimental flag @iceweasel-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.93.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-31-6-context-window-changes-in-rust-v0-93-0|6 Context Window changes in rust-v0.93.0]] · Context Window
- [[Changes/Codex CLI/2026-01-31-6-memory-and-personalization-changes-in-rust-v0-93-0|6 Memory and Personalization changes in rust-v0.93.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-01-31-10191-chore-app-server-document-authmode-owenlin0|♯10191 chore(app-server): document AuthMode @owenlin0]] · Files and Data
- [[Changes/Codex CLI/2026-01-31-10011-really-fix-pwd-for-windows-codex-zip-iceweasel-oai|♯10011 really fix pwd for windows codex zip @iceweasel-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-31-9654-show-oauth-error-descriptions-in-callback-responses-blevy-oai|♯9654 Show OAuth error descriptions in callback responses @blevy-oai]] · Account and Access
- [[Changes/Codex CLI/2026-01-31-3-interface-experience-changes-in-rust-v0-93-0|3 Interface Experience changes in rust-v0.93.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-31-3-reliability-and-performance-changes-in-rust-v0-93-0|3 Reliability and Performance changes in rust-v0.93.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-01-31-10118-codex-cli-show-model-capacity-guidance-on-429-ccy-oai|♯10118 CodexCLI Show model-capacity guidance on 429 @ccy-oai]] · Model Support
- [[Changes/Codex CLI/2026-01-31-6-developer-workflow-changes-in-rust-v0-93-0|6 Developer Workflow changes in rust-v0.93.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-31-10030-clarify-external-editor-env-var-message-joshka-oai|♯10030 Clarify external editor env var message @joshka-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-01-31-smart-approvals-are-now-enabled-by-default-with-explicit-approval-prompts-for-mc|Smart approvals are now enabled by default, with explicit approval prompts for MCP…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-31-14-apps-and-integrations-changes-in-rust-v0-93-0|14 Apps and Integrations changes in rust-v0.93.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-31-3-search-and-browsing-changes-in-rust-v0-93-0|3 Search and Browsing changes in rust-v0.93.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-01-31-added-apps-to-browse-connectors-in-tui-and-insertion-for-app-prompts-9728|Added /apps to browse connectors in TUI and $ insertion for app prompts]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-31-97-other-changes-in-rust-v0-93-0|97 other changes in rust-v0.93.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-01-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-01-30-acp-server-support-permission-flags-yolo-allow-all-etc-and-permissions-config|ACP server support permission flags: --yolo, --allow-all, etc. and permissions config]]
- Later: 2026-02-02 · ElevenLabs · [[Changes/ElevenLabs/2026-02-02-workspaces|Workspaces]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-31-c696ec&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-31-4-safety-and-privacy-changes-in-rust-v0-93-0.md%0ACard%20ID%3A%20codex-cli-2026-01-31-c696ec%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.93.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->