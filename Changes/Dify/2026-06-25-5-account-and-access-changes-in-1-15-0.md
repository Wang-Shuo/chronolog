---
card_id: dify-2026-06-25-d7bcfc
date: '2026-06-25'
description: 'Dify · 2026-06-25 · Account and Access: 5 changes in 1.15.0 — Invalidated
  credential cache after OAuth refresh (#37630)'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1183
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 70f36e83fc6363c7c84740e759917d897fc8952c384f9b125db6cea6620d6e5e
product: dify
product_name: Dify
record:
  card_id: dify-2026-06-25-d7bcfc
  comparison: ''
  date: '2026-06-25'
  description: 'Dify — 1.15.0: 5 Account and Access changes'
  evidence:
  - quote: Invalidated credential cache after OAuth refresh (#37630)
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: '`ENABLE_OAUTH_BEARER` (`docker/envs/core-services/shared.env.example`)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: OAuth access tokens (`ENABLE_OAUTH_BEARER`)
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'refactor(api): migrate tenant/user via DI: apikey, extension, data_source_bearer,
      oauth_server by @cqjjjzr in https://github.com/langgenius/dify/pull/36660'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'refactor(tests): use caplog in web login tests by @lin-hongkuan in https://github.com/langgenius/dify/pull/37889'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 5-account-and-access-changes-in-1-15-0
  source_release: dify-2026-06-25-1-15-0-github-344699591-4dd01045
  source_type: github_releases
  theme: account-access
  title: 5 Account and Access changes in 1.15.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-25-added-a-startup-notice-when-mcp-servers-need-authentication-pointing-at-mcp|Added
  a startup notice when MCP servers need authentication, pointing at /mcp]]'
- '[[Changes/Codex CLI/2026-06-25-macos-authentication-clients-can-honor-system-proxy-pac-and-wpad-settings-when-r|macOS
  authentication clients can honor system proxy, PAC, and WPAD settings…]]'
- '[[Changes/Codex CLI/2026-06-25-added-opt-in-windows-system-proxy-support-for-authentication-including-pac-wpad|Added
  opt-in Windows system proxy support for authentication, including PAC, WPAD…]]'
source_release: '[[Releases/Dify/dify-2026-06-25-1-15-0-github-344699591-4dd01045|dify-2026-06-25-1-15-0-github-344699591-4dd01045]]'
source_type: github_releases
theme: account-access
title: 5 Account and Access changes in 1.15.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Account and Access changes in 1.15.0

**Dify** · 2026-06-25 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.15.0) · from [[Releases/Dify/dify-2026-06-25-1-15-0-github-344699591-4dd01045|1.15.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Invalidated credential cache after OAuth refresh (#37630)

> `ENABLE_OAUTH_BEARER` (`docker/envs/core-services/shared.env.example`)

> OAuth access tokens (`ENABLE_OAUTH_BEARER`)

> refactor(api): migrate tenant/user via DI: apikey, extension, data_source_bearer, oauth_server by @cqjjjzr in https://github.com/langgenius/dify/pull/36660

> refactor(tests): use caplog in web login tests by @lin-hongkuan in https://github.com/langgenius/dify/pull/37889

Source: https://github.com/langgenius/dify/releases/tag/1.15.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-06-25-6-interface-experience-changes-in-1-15-0|6 Interface Experience changes in 1.15.0]] · Interface Experience
- [[Changes/Dify/2026-06-25-38-agent-mode-changes-in-1-15-0|38 Agent Mode changes in 1.15.0]] · Agent Mode
- [[Changes/Dify/2026-06-25-14-safety-and-privacy-changes-in-1-15-0|14 Safety and Privacy changes in 1.15.0]] · Safety and Privacy
- [[Changes/Dify/2026-06-25-refactor-inject-session-into-audio-tts-by-myshkin451-in-https-github-com-langgen|refactor: inject session into audio TTS]] · Voice and Audio
- [[Changes/Dify/2026-06-25-2-reliability-and-performance-changes-in-1-15-0|2 Reliability and Performance changes in 1.15.0]] · Reliability and Performance
- [[Changes/Dify/2026-06-25-3-context-window-changes-in-1-15-0|3 Context Window changes in 1.15.0]] · Context Window
- [[Changes/Dify/2026-06-25-install-it-on-any-platform-macos-linux-windows-with-a-single-command-and-no-acce|Install it on any platform (macOS, Linux, Windows) with a single command and no…]] · Mobile and Desktop
- [[Changes/Dify/2026-06-25-numerous-web-ui-and-accessibility-focus-ring-polish-fixes|Numerous web UI and accessibility/focus-ring polish fixes]] · Accessibility and Localization
- [[Changes/Dify/2026-06-25-6-pricing-model-changes-in-1-15-0|6 Pricing Model changes in 1.15.0]] · Pricing Model
- [[Changes/Dify/2026-06-25-9-developer-workflow-changes-in-1-15-0|9 Developer Workflow changes in 1.15.0]] · Developer Workflow
- [[Changes/Dify/2026-06-25-6-files-and-data-changes-in-1-15-0|6 Files and Data changes in 1.15.0]] · Files and Data
- [[Changes/Dify/2026-06-25-17-model-support-changes-in-1-15-0|17 Model Support changes in 1.15.0]] · Model Support
- [[Changes/Dify/2026-06-25-6-collaboration-changes-in-1-15-0|6 Collaboration changes in 1.15.0]] · Collaboration
- [[Changes/Dify/2026-06-25-27-apps-and-integrations-changes-in-1-15-0|27 Apps and Integrations changes in 1.15.0]] · Apps and Integrations
- [[Changes/Dify/2026-06-25-2-automation-and-scheduling-changes-in-1-15-0|2 Automation and Scheduling changes in 1.15.0]] · Automation and Scheduling
- [[Changes/Dify/2026-06-25-3-editor-experience-changes-in-1-15-0|3 Editor Experience changes in 1.15.0]] · Editor Experience
- [[Changes/Dify/2026-06-25-365-other-changes-in-1-15-0|365 other changes in 1.15.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-06-25 · Codex CLI · [[Changes/Codex CLI/2026-06-25-added-opt-in-windows-system-proxy-support-for-authentication-including-pac-wpad|Added opt-in Windows system proxy support for authentication, including PAC, WPAD…]]
- Later: 2026-06-25 · Google Antigravity · [[Changes/Google Antigravity/2026-06-25-enabled-automatic-saving-of-refreshed-oauth-tokens-to-the-os-keyring-to-reduce-a|Enabled automatic saving of refreshed OAuth tokens to the OS keyring to reduce…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-06-25-d7bcfc&body=Card%3A%20Changes%2FDify%2F2026-06-25-5-account-and-access-changes-in-1-15-0.md%0ACard%20ID%3A%20dify-2026-06-25-d7bcfc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.15.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->