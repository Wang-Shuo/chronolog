---
card_id: opencode-2026-03-22-6c1d93
date: '2026-03-22'
description: 'OpenCode · 2026-03-22 · Account and Access: 4 changes in v1.3.0 — Important
  Multistep Authentication : TUI and Desktop both support multistep authentication…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2063
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 35cad38279b70abd9923af7cf9d51e578be9982c4ac001975d433d159b2f5642
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-03-22-6c1d93
  comparison: ''
  date: '2026-03-22'
  description: 'OpenCode — v1.3.0: 4 Account and Access changes'
  evidence:
  - quote: 'Important Multistep Authentication : TUI and Desktop both support multistep
      authentication flows which means providers like Github Copilot for Enterprise
      deployments now work as intended'
    source_release: https://opencode.ai/changelog/v1.3.0
  - quote: 'Desktop App Improvements Console Login : Fixed console device login to
      properly handle pending authorization states, ensuring the login process continues
      polling instead of failing while waiting for approval.'
    source_release: https://opencode.ai/changelog/v1.3.0
  - quote: 'Authentication & Account Stale Credentials : Fixed stale server URL and
      email on re-login. Previously, logging into a different server could fail due
      to cached credentials from a previous environment.'
    source_release: https://opencode.ai/changelog/v1.3.0
  - quote: 'Authentication & Account Codex Access : OAuth plan users can now access
      codex instructions freely without the previous whitelisting restrictions.'
    source_release: https://opencode.ai/changelog/v1.3.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: opencode
  product_name: OpenCode
  slug: 4-account-and-access-changes-in-v1-3-0
  source_release: opencode-2026-03-22-v1-3-0-00955596
  source_type: opencode_changelog
  theme: account-access
  title: 4 Account and Access changes in v1.3.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-03-19-app-server-tui-now-supports-device-code-chatgpt-sign-in-during-onboarding-and-ca|App-server
  TUI now supports device-code ChatGPT sign-in during onboarding and can…]]'
- '[[Changes/Claude Code/2026-03-20-updated-mcp-oauth-to-support-client-id-metadata-document-cimd-sep-991-for-server|Updated
  MCP OAuth to support Client ID Metadata Document (CIMD / SEP-991)…]]'
- '[[Changes/GitHub Copilot CLI/2026-03-20-login-device-flow-works-correctly-in-codespaces-and-remote-terminal-environments|/login
  device flow works correctly in Codespaces and remote terminal environments]]'
source_release: '[[Releases/OpenCode/opencode-2026-03-22-v1-3-0-00955596|opencode-2026-03-22-v1-3-0-00955596]]'
source_type: opencode_changelog
theme: account-access
title: 4 Account and Access changes in v1.3.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Account and Access changes in v1.3.0

**OpenCode** · 2026-03-22 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://opencode.ai/changelog/v1.3.0) · from [[Releases/OpenCode/opencode-2026-03-22-v1-3-0-00955596|v1.3.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Important Multistep Authentication : TUI and Desktop both support multistep authentication flows which means providers like Github Copilot for Enterprise deployments now work as intended

> Desktop App Improvements Console Login : Fixed console device login to properly handle pending authorization states, ensuring the login process continues polling instead of failing while waiting for approval.

> Authentication & Account Stale Credentials : Fixed stale server URL and email on re-login. Previously, logging into a different server could fail due to cached credentials from a previous environment.

> Authentication & Account Codex Access : OAuth plan users can now access codex instructions freely without the previous whitelisting restrictions.

Source: https://opencode.ai/changelog/v1.3.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-03-22-2-collaboration-changes-in-v1-3-0|2 Collaboration changes in v1.3.0]] · Collaboration
- [[Changes/OpenCode/2026-03-22-2-developer-workflow-changes-in-v1-3-0|2 Developer Workflow changes in v1.3.0]] · Developer Workflow
- [[Changes/OpenCode/2026-03-22-3-model-support-changes-in-v1-3-0|3 Model Support changes in v1.3.0]] · Model Support
- [[Changes/OpenCode/2026-03-22-5-mobile-and-desktop-changes-in-v1-3-0|5 Mobile and Desktop changes in v1.3.0]] · Mobile and Desktop
- [[Changes/OpenCode/2026-03-22-3-editor-experience-changes-in-v1-3-0|3 Editor Experience changes in v1.3.0]] · Editor Experience
- [[Changes/OpenCode/2026-03-22-ui-ux-improvements-agent-skill-ordering-more-consistent-ai-responses-with-improv|UI/UX Improvements Agent & Skill Ordering]] · Agent Mode
- [[Changes/OpenCode/2026-03-22-3-interface-experience-changes-in-v1-3-0|3 Interface Experience changes in v1.3.0]] · Interface Experience
- [[Changes/OpenCode/2026-03-22-removed-anthropic-oauth-plugin-see|Removed anthropic oauth plugin, see]] · Account and Access
- [[Changes/OpenCode/2026-03-22-providers-models-xai-responses-api-improved-xai-reasoning-models-performance-in|Providers & Models xAI Responses API]] · Reliability and Performance
- [[Changes/OpenCode/2026-03-22-2-context-window-changes-in-v1-3-0|2 Context Window changes in v1.3.0]] · Context Window
- [[Changes/OpenCode/2026-03-22-8-other-changes-in-v1-3-0|8 other changes in v1.3.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-03-20 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-20-login-device-flow-works-correctly-in-codespaces-and-remote-terminal-environments|/login device flow works correctly in Codespaces and remote terminal environments]]
- Later: 2026-03-23 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-23-mcp-oauth-authentication-works-with-mcp-servers-like-the-atlassian-rovo-mcp-serv|MCP OAuth authentication works with MCP servers like the Atlassian Rovo MCP Server…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-03-22-6c1d93&body=Card%3A%20Changes%2FOpenCode%2F2026-03-22-4-account-and-access-changes-in-v1-3-0.md%0ACard%20ID%3A%20opencode-2026-03-22-6c1d93%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv1.3.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->