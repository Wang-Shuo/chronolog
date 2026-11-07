---
card_id: codex-cli-2026-03-26-aa1e60
date: '2026-03-26'
description: 'Codex CLI · 2026-03-26 · Account and Access: 4 changes in 0.117.0 —
  ChatGPT login in `tui_app_server` now opens the local browser again, cancels cleanly
  on…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2067
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: aba7836d9051bbea17f6e83c600d760957451ddceeefb4f7673bc6bba1bbd96f
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-26-aa1e60
  comparison: ''
  date: '2026-03-26'
  description: 'Codex CLI — 0.117.0: 4 Account and Access changes'
  evidence:
  - quote: 'ChatGPT login in `tui_app_server` now opens the local browser again, cancels
      cleanly on `Ctrl+C`, and no longer fails startup when you''re logged out. (#15672,
      #15673, #15670)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15150 Move auth code into login crate @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15672 tui_app_server: open ChatGPT login in the local browser @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15673 tui_app_server: cancel active login before Ctrl+C exit @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-account-and-access-changes-in-rust-v0-117-0
  source_release: codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6
  source_type: github_releases
  theme: account-access
  title: 4 Account and Access changes in rust-v0.117.0
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-03-25-improved-mcp-authentication|Improved MCP
  authentication]]'
- '[[Changes/Open WebUI/2026-03-25-11-account-and-access-changes-in-v0-8-11|11 Account
  and Access changes in v0.8.11]]'
- '[[Changes/Claude Code/2026-03-26-mcp-oauth-now-follows-rfc-9728-protected-resource-metadata-discovery-to-find-the|MCP
  OAuth now follows RFC 9728 Protected Resource Metadata discovery to find…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6|codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6]]'
source_type: github_releases
theme: account-access
title: 4 Account and Access changes in rust-v0.117.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Account and Access changes in rust-v0.117.0

**Codex CLI** · 2026-03-26 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.117.0) · from [[Releases/Codex CLI/codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6|0.117.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ChatGPT login in `tui_app_server` now opens the local browser again, cancels cleanly on `Ctrl+C`, and no longer fails startup when you're logged out. (#15672, #15673, #15670)

> #15150 Move auth code into login crate @aibrahim-oai

> #15672 tui_app_server: open ChatGPT login in the local browser @etraut-openai

> #15673 tui_app_server: cancel active login before Ctrl+C exit @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.117.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-26-19-developer-workflow-changes-in-rust-v0-117-0|19 Developer Workflow changes in rust-v0.117.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-26-15789-treat-chatgpt-hc-plan-as-enterprise-arnavdugar-openai|♯15789 Treat ChatGPT hc plan as Enterprise @arnavdugar-openai]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-03-26-the-app-server-backed-tui-is-now-enabled-by-default-and-the-plugin-app-rollout-f|The app-server-backed TUI is now enabled by default, and the plugin/app rollout…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-26-plugins-are-now-a-first-class-workflow-codex-can-sync-product-scoped-plugins-at|Plugins are now a first-class workflow]] · Search and Browsing
- [[Changes/Codex CLI/2026-03-26-2-image-generation-changes-in-rust-v0-117-0|2 Image Generation changes in rust-v0.117.0]] · Image Generation
- [[Changes/Codex CLI/2026-03-26-15579-increase-voice-space-hold-timeout-to-1s-aibrahim-oai|♯15579 Increase voice space hold timeout to 1s @aibrahim-oai]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-26-2-automation-and-scheduling-changes-in-rust-v0-117-0|2 Automation and Scheduling changes in rust-v0.117.0]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-03-26-5-context-window-changes-in-rust-v0-117-0|5 Context Window changes in rust-v0.117.0]] · Context Window
- [[Changes/Codex CLI/2026-03-26-14945-feat-tui-restore-composer-history-in-app-server-tui-fcoury|♯14945 feat(tui): restore composer history in app-server tui @fcoury]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-03-26-15480-use-shift-left-to-edit-queued-messages-in-tmux-charley-oai|♯15480 Use Shift+Left to edit queued messages in tmux @charley-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-03-26-3-interface-experience-changes-in-rust-v0-117-0|3 Interface Experience changes in rust-v0.117.0]] · Interface Experience
- [[Changes/Codex CLI/2026-03-26-19-agent-mode-changes-in-rust-v0-117-0|19 Agent Mode changes in rust-v0.117.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-26-57-apps-and-integrations-changes-in-rust-v0-117-0|57 Apps and Integrations changes in rust-v0.117.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-26-3-mobile-and-desktop-changes-in-rust-v0-117-0|3 Mobile and Desktop changes in rust-v0.117.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-26-5-safety-and-privacy-changes-in-rust-v0-117-0|5 Safety and Privacy changes in rust-v0.117.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-26-3-model-support-changes-in-rust-v0-117-0|3 Model Support changes in rust-v0.117.0]] · Model Support
- [[Changes/Codex CLI/2026-03-26-15175-chore-morpheus-does-not-generate-memories-jif-oai|♯15175 chore: morpheus does not generate memories @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-26-117-other-changes-in-rust-v0-117-0|117 other changes in rust-v0.117.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-mcp-oauth-now-follows-rfc-9728-protected-resource-metadata-discovery-to-find-the|MCP OAuth now follows RFC 9728 Protected Resource Metadata discovery to find…]]
- Later: 2026-03-26 · OpenCode · [[Changes/OpenCode/2026-03-26-2-account-and-access-changes-in-v1-3-3|2 Account and Access changes in v1.3.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-26-aa1e60&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-26-4-account-and-access-changes-in-rust-v0-117-0.md%0ACard%20ID%3A%20codex-cli-2026-03-26-aa1e60%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.117.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->