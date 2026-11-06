---
card_id: github-copilot-cli-2026-06-09-51dca8
date: '2026-06-09'
description: 'GitHub Copilot CLI · 2026-06-09 · Account and Access: MCP OAuth re-authentication
  correctly uses the saved OAuth client ID for remote servers'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1167
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 8bca08a8727f93914ac449d2fce94ace9ed265453cd1351819e6f701c86b29d1
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-09-51dca8
  comparison: ''
  date: '2026-06-09'
  description: 'GitHub Copilot CLI — 1.0.61: MCP OAuth re-authentication correctly
    uses the saved OAuth client ID for remote servers'
  evidence:
  - quote: MCP OAuth re-authentication correctly uses the saved OAuth client ID for
      remote servers
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.61
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: mcp-oauth-re-authentication-correctly-uses-the-saved-oauth-client-id-for-remote
  source_release: github-copilot-cli-2026-06-09-v1-0-61-github-336905979-4d0a69f2
  source_type: github_releases
  theme: account-access
  theme_matches:
  - matched_terms:
    - authentication
    - oauth
    score: 100
    theme: account-access
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  title: MCP OAuth re-authentication correctly uses the saved OAuth client ID for
    remote servers
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-08-improved-the-error-message-shown-when-your-organization-has-disabled-api-key-aut|Improved
  the error message shown when your organization has disabled API key…]]'
- '[[Changes/Codex CLI/2026-06-08-2-account-and-access-changes-in-rust-v0-138-0|2
  Account and Access changes in rust-v0.138.0]]'
- '[[Changes/v0/2026-06-08-2-account-and-access-changes-in-changelog-update|2 Account
  and Access changes in Changelog update]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-09-v1-0-61-github-336905979-4d0a69f2|github-copilot-cli-2026-06-09-v1-0-61-github-336905979-4d0a69f2]]'
source_type: github_releases
theme: account-access
title: MCP OAuth re-authentication correctly uses the saved OAuth client ID for remote
  servers
type: change
---

<!-- chronolog:begin region="header" -->
# MCP OAuth re-authentication correctly uses the saved OAuth client ID for remote servers

**GitHub Copilot CLI** · 2026-06-09 · [[Themes/account-access|Account and Access]] · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.61) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-09-v1-0-61-github-336905979-4d0a69f2|1.0.61]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> MCP OAuth re-authentication correctly uses the saved OAuth client ID for remote servers
>
> Source: https://github.com/github/copilot-cli/releases/tag/v1.0.61
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-09-2-interface-experience-changes-in-v1-0-61|2 Interface Experience changes in v1.0.61]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-09-grep-searches-in-large-monorepos-use-an-indexed-search-engine-for-significantly|Grep searches in large monorepos use an indexed search engine for significantly…]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-09-6-developer-workflow-changes-in-v1-0-61|6 Developer Workflow changes in v1.0.61]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-09-3-model-support-changes-in-v1-0-61|3 Model Support changes in v1.0.61]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-09-3-agent-mode-changes-in-v1-0-61|3 Agent Mode changes in v1.0.61]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-09-2-search-and-browsing-changes-in-v1-0-61|2 Search and Browsing changes in v1.0.61]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-06-09-use-natural-language-with-every-and-after-to-schedule-tasks-using-cron-expressio|Use natural language with /every and /after to schedule tasks using cron…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-09-4-editor-experience-changes-in-v1-0-61|4 Editor Experience changes in v1.0.61]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-09-resuming-a-local-session-with-memory-disabled-no-longer-crashes-the-ui-to-a-blan|Resuming a local session with memory disabled no longer crashes the UI to a blank screen]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-06-09-pasted-images-no-longer-leak-into-the-main-prompt-after-a-permission-dialog-clos|Pasted images no longer leak into the main prompt after a permission dialog closes]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-09-4-apps-and-integrations-changes-in-v1-0-61|4 Apps and Integrations changes in v1.0.61]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-09-8-other-changes-in-v1-0-61|8 other changes in v1.0.61]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-06-08 · v0 · [[Changes/v0/2026-06-08-2-account-and-access-changes-in-changelog-update|2 Account and Access changes in Changelog update]]
- Later: 2026-06-13 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-13-remote-mcp-oauth-servers-start-only-once-per-matching-config-instead-of-restarti|Remote MCP OAuth servers start only once per matching config instead of restarting…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-09-51dca8&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-09-mcp-oauth-re-authentication-correctly-uses-the-saved-oauth-client-id-for-remote.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-09-51dca8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.61%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->