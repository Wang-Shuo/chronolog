---
card_id: github-copilot-cli-2026-03-30-b002db
date: '2026-03-30'
description: 'GitHub Copilot CLI · 2026-03-30 · Safety and Privacy: MCP servers using
  Microsoft Entra ID authentication no longer show the consent screen on every login'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2071
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 1e55fb94371aa8a1beb7c49a9a14da6dbc608c4e96f7b96a9ee93e39fb678764
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-03-30-b002db
  comparison: ''
  date: '2026-03-30'
  description: 'GitHub Copilot CLI — 1.0.13: MCP servers using Microsoft Entra ID
    authentication no longer show the consent screen on every login'
  evidence:
  - quote: MCP servers using Microsoft Entra ID authentication no longer show the
      consent screen on every login
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.13
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: mcp-servers-using-microsoft-entra-id-authentication-no-longer-show-the-consent-s
  source_release: github-copilot-cli-2026-03-30-v1-0-13-github-303313822-db3397e2
  source_type: github_releases
  theme: safety-privacy
  theme_matches:
  - matched_terms:
    - authentication
    - login
    score: 100
    theme: account-access
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  theme_resolution: manual-semantic-rule-v2
  title: MCP servers using Microsoft Entra ID authentication no longer show the consent…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-27-fixed-official-marketplace-plugin-scripts-failing-with-permission-denied-on-maco|Fixed
  official marketplace plugin scripts failing…]]'
- '[[Changes/Dify/2026-03-27-6-safety-and-privacy-changes-in-1-13-3|6 Safety and Privacy
  changes in 1.13.3]]'
- "[[Changes/Open WebUI/2026-03-27-terminal-server-connection-security-terminal-server-verification-and-policy-savi|\U0001F512
  Terminal server connection security. Terminal server verification and policy…]]"
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-30-v1-0-13-github-303313822-db3397e2|github-copilot-cli-2026-03-30-v1-0-13-github-303313822-db3397e2]]'
source_type: github_releases
theme: safety-privacy
title: MCP servers using Microsoft Entra ID authentication no longer show the consent…
type: change
---

<!-- chronolog:begin region="header" -->
# MCP servers using Microsoft Entra ID authentication no longer show the consent…

**GitHub Copilot CLI** · 2026-03-30 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.13) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-30-v1-0-13-github-303313822-db3397e2|1.0.13]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> MCP servers using Microsoft Entra ID authentication no longer show the consent screen on every login
>
> Source: https://github.com/github/copilot-cli/releases/tag/v1.0.13
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-03-30-grep-and-glob-search-results-return-promptly-when-a-timeout-is-reached|Grep and glob search results return promptly when a timeout is reached]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-03-30-mcp-server-oauth-authentication-works-when-the-cli-runs-in-acp-mode|MCP server OAuth authentication works when the CLI runs in ACP mode]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-03-30-2-interface-experience-changes-in-v1-0-13|2 Interface Experience changes in v1.0.13]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-03-30-5-apps-and-integrations-changes-in-v1-0-13|5 Apps and Integrations changes in v1.0.13]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-03-30-2-developer-workflow-changes-in-v1-0-13|2 Developer Workflow changes in v1.0.13]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-03-30-2-model-support-changes-in-v1-0-13|2 Model Support changes in v1.0.13]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-03-30-2-reliability-and-performance-changes-in-v1-0-13|2 Reliability and Performance changes in v1.0.13]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-03-30-5-other-changes-in-v1-0-13|5 other changes in v1.0.13]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-27 · Open WebUI · [[Changes/Open WebUI/2026-03-27-terminal-server-connection-security-terminal-server-verification-and-policy-savi|🔒 Terminal server connection security. Terminal server verification and policy…]]
- Later: 2026-03-30 · OpenHands · [[Changes/OpenHands/2026-03-30-added-clear-command-for-v1-conversations-typing-clear-in-the-chat-creates-a-new|Added /clear command for V1 conversations]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-03-30-b002db&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-03-30-mcp-servers-using-microsoft-entra-id-authentication-no-longer-show-the-consent-s.md%0ACard%20ID%3A%20github-copilot-cli-2026-03-30-b002db%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.13%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->