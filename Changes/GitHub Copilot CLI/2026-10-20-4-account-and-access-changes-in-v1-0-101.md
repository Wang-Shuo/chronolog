---
card_id: github-copilot-cli-2026-10-20-1eb7da
date: '2026-10-20'
description: 'GitHub Copilot CLI · 2026-10-20 · Account and Access: 4 changes in 1.0.101
  — Headless and SDK sessions without an OAuth handler skip MCP connections when saved…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1300
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0f812f67a470d43bb59e5e83bb5ff4e0b5c4669b2a4a01db9f32b442865f5e55
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-10-20-1eb7da
  comparison: ''
  date: '2026-10-20'
  description: 'GitHub Copilot CLI — 1.0.101: 4 Account and Access changes'
  evidence:
  - quote: Headless and SDK sessions without an OAuth handler skip MCP connections
      when saved tokens require sign-in, while renewable grants still connect.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.101
  - quote: Explicit Entra MCP sign-in now recovers from rejected cached tokens by
      continuing to interactive sign-in.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.101
  - quote: Cancel abandoned Microsoft sign-in flows so retries start cleanly
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.101
  - quote: Shared MCP auth errors point to your client's sign-in settings; CLI authentication
      warnings still show /mcp auth.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.101
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 4-account-and-access-changes-in-v1-0-101
  source_release: github-copilot-cli-2026-10-20-v1-0-101-github-418747415-a1bf6298
  source_type: github_releases
  theme: account-access
  title: 4 Account and Access changes in v1.0.101
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-19-3-account-and-access-changes-in-v1-0-100|3
  Account and Access changes in v1.0.100]]'
- '[[Changes/ChatGPT/2026-10-20-locked-chats-let-you-keep-selected-conversations-in-your-account-while-hiding-th|Introducing
  locked chats]]'
- '[[Changes/Claude Code/2026-10-20-vscode-changed-the-message-shown-when-a-session-does-not-start-in-time-and-no-ho|VSCode
  Changed the message shown when a session does not start in time and no hook…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-10-20-v1-0-101-github-418747415-a1bf6298|github-copilot-cli-2026-10-20-v1-0-101-github-418747415-a1bf6298]]'
source_type: github_releases
theme: account-access
title: 4 Account and Access changes in v1.0.101
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Account and Access changes in v1.0.101

**GitHub Copilot CLI** · 2026-10-20 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.101) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-10-20-v1-0-101-github-418747415-a1bf6298|1.0.101]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Headless and SDK sessions without an OAuth handler skip MCP connections when saved tokens require sign-in, while renewable grants still connect.

> Explicit Entra MCP sign-in now recovers from rejected cached tokens by continuing to interactive sign-in.

> Cancel abandoned Microsoft sign-in flows so retries start cleanly

> Shared MCP auth errors point to your client's sign-in settings; CLI authentication warnings still show /mcp auth.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.101
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-10-20-2-developer-workflow-changes-in-v1-0-101|2 Developer Workflow changes in v1.0.101]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-10-20-8-model-support-changes-in-v1-0-101|8 Model Support changes in v1.0.101]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-10-20-model-picker-marks-your-administrator-managed-model-as-the-default-when-it-is-av|Model picker marks your administrator-managed model as the default when it is available]] · Enterprise and Administration
- [[Changes/GitHub Copilot CLI/2026-10-20-switching-only-reasoning-effort-no-longer-forces-compaction-in-over-budget-sessi|Switching only reasoning effort no longer forces compaction in over-budget sessions]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-10-20-macos-sandboxed-commands-can-connect-directly-to-localhost-tcp-services-when-loc|macOS sandboxed commands can connect directly to localhost TCP services when local…]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-10-20-4-apps-and-integrations-changes-in-v1-0-101|4 Apps and Integrations changes in v1.0.101]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-10-20-permission-approval-prompts-explain-escalation-causes-and-show-a-request-specifi|Permission approval prompts explain escalation causes and show a request-specific…]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-10-20-8-other-changes-in-v1-0-101|8 other changes in v1.0.101]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-10-20 · Claude Code · [[Changes/Claude Code/2026-10-20-vscode-changed-the-message-shown-when-a-session-does-not-start-in-time-and-no-ho|VSCode Changed the message shown when a session does not start in time and no hook…]]
- Later: 2026-10-21 · Claude Code · [[Changes/Claude Code/2026-10-21-2-account-and-access-changes-in-v2-1-307|2 Account and Access changes in v2.1.307]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-10-20-1eb7da&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-10-20-4-account-and-access-changes-in-v1-0-101.md%0ACard%20ID%3A%20github-copilot-cli-2026-10-20-1eb7da%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.101%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->