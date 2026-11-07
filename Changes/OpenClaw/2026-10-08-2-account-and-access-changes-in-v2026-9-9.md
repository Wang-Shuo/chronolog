---
card_id: openclaw-2026-10-08-4139f4
date: '2026-10-08'
description: 'OpenClaw · 2026-10-08 · Account and Access: 2 changes in v2026.9.9 —
  MCP sign-in changes. Background refresh preserves saved credentials when a server
  changes…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2263
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ed59e1c864150b0f354d9ac3de12ec5500c714eee208b08a11c71de918d7d396
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-08-4139f4
  comparison: ''
  date: '2026-10-08'
  description: 'OpenClaw — v2026.9.9: 2 Account and Access changes'
  evidence:
  - quote: 'MCP sign-in changes. Background refresh preserves saved credentials when
      a server changes its sign-in provider. An explicit sign-in can register with
      the new provider; unused registrations with an outdated callback can also be
      replaced. #166341 , with contributions from @RomneyDa , @Patrick-Erichsen ,
      @steipete and @vincentkoc .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'MCP sign-in. OAuth login and token refresh refuse redirects that would
      send credentials to another origin. If a custom provider now fails with that
      refusal, configure direct token or registration endpoints. Ordinary MCP resource
      redirects keep their existing behavior. #138263 by @mmaps , with prior work
      and coauthorship by @hansraj316 .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 2-account-and-access-changes-in-v2026-9-9
  source_release: openclaw-2026-10-08-v2026-9-9-933614cc
  source_type: openclaw_changelog
  theme: account-access
  title: 2 Account and Access changes in v2026.9.9
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-07-2-account-and-access-changes-in-v1-0-93|2
  Account and Access changes in v1.0.93]]'
- '[[Changes/Claude Code/2026-10-08-added-support-for-forceloginmethod-gateway-and-forcelogingatewayurl-in-your-own|Added
  support for forceLoginMethod: "gateway" and forceLoginGatewayUrl…]]'
- '[[Changes/Codex CLI/2026-10-08-2-account-and-access-changes-in-rust-v0-162-0|2
  Account and Access changes in rust-v0.162.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|openclaw-2026-10-08-v2026-9-9-933614cc]]'
source_type: openclaw_changelog
theme: account-access
title: 2 Account and Access changes in v2026.9.9
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Account and Access changes in v2026.9.9

**OpenClaw** · 2026-10-08 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.9) · from [[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|v2026.9.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> MCP sign-in changes. Background refresh preserves saved credentials when a server changes its sign-in provider. An explicit sign-in can register with the new provider; unused registrations with an outdated callback can also be replaced. #166341 , with contributions from @RomneyDa , @Patrick-Erichsen , @steipete and @vincentkoc .

> MCP sign-in. OAuth login and token refresh refuse redirects that would send credentials to another origin. If a custom provider now fails with that refusal, configure direct token or registration endpoints. Ordinary MCP resource redirects keep their existing behavior. #138263 by @mmaps , with prior work and coauthorship by @hansraj316 .

Source: https://docs.openclaw.ai/releases/2026.9.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-08-4-agent-mode-changes-in-v2026-9-9|4 Agent Mode changes in v2026.9.9]] · Agent Mode
- [[Changes/OpenClaw/2026-10-08-model-retries-and-context-one-shot-model-requests-through-the-gateway-retain-the|Model retries and context]] · Context Window
- [[Changes/OpenClaw/2026-10-08-2-voice-and-audio-changes-in-v2026-9-9|2 Voice and Audio changes in v2026.9.9]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-08-3-developer-workflow-changes-in-v2026-9-9|3 Developer Workflow changes in v2026.9.9]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-08-windows-mxc-sandbox-the-optional-mxc-sandbox-can-start-and-run-tools-on-compatib|Windows MXC sandbox]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-08-claude-haiku-5-5-you-can-select-haiku-5-5-through-the-anthropic-api-and-claude-c|Claude Haiku 5.5. You can select Haiku 5.5 through the Anthropic API and Claude CLI]] · Pricing Model
- [[Changes/OpenClaw/2026-10-08-4-interface-experience-changes-in-v2026-9-9|4 Interface Experience changes in v2026.9.9]] · Interface Experience
- [[Changes/OpenClaw/2026-10-08-10-apps-and-integrations-changes-in-v2026-9-9|10 Apps and Integrations changes in v2026.9.9]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-08-2-enterprise-and-administration-changes-in-v2026-9-9|2 Enterprise and Administration changes in v2026.9.9]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-08-4-model-support-changes-in-v2026-9-9|4 Model Support changes in v2026.9.9]] · Model Support
- [[Changes/OpenClaw/2026-10-08-3-mobile-and-desktop-changes-in-v2026-9-9|3 Mobile and Desktop changes in v2026.9.9]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-08-feishu-attachments-files-sent-with-captions-or-together-in-feishu-lark-posts-rea|Feishu attachments]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-08-2-memory-and-personalization-changes-in-v2026-9-9|2 Memory and Personalization changes in v2026.9.9]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-08-2-automation-and-scheduling-changes-in-v2026-9-9|2 Automation and Scheduling changes in v2026.9.9]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-08-september-database-compatibility-upgrading-from-september-stable-keeps-shared-da|September database compatibility]] · Collaboration
- [[Changes/OpenClaw/2026-10-08-24-other-changes-in-v2026-9-9|24 other changes in v2026.9.9]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-10-08 · Codex CLI · [[Changes/Codex CLI/2026-10-08-2-account-and-access-changes-in-rust-v0-162-0|2 Account and Access changes in rust-v0.162.0]]
- Later: 2026-10-09 · Claude Code · [[Changes/Claude Code/2026-10-09-improved-the-errors-for-a-refused-cloud-session-they-now-say-why-your-organizati|Improved the errors for a refused cloud session]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-08-4139f4&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-08-2-account-and-access-changes-in-v2026-9-9.md%0ACard%20ID%3A%20openclaw-2026-10-08-4139f4%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->