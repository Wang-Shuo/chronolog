---
card_id: github-copilot-cli-2026-04-13-4ac570
date: '2026-04-13'
description: 'GitHub Copilot CLI · 2026-04-13 · Account and Access: /logout shows
  a warning when signed in via gh CLI, PAT, API key, or environment variable, since
  /logout…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1110
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: b3665021f17a87fd49fbe5a3b00b87dab118b24092fbedb7e2d214b25f1b58be
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-04-13-4ac570
  comparison: ''
  date: '2026-04-13'
  description: 'GitHub Copilot CLI — 1.0.25: /logout shows a warning when signed in
    via gh CLI, PAT, API key, or environment variable, since /logout only manages
    OAuth sessions'
  evidence:
  - quote: /logout shows a warning when signed in via gh CLI, PAT, API key, or environment
      variable, since /logout only manages OAuth sessions
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.25
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: logout-shows-a-warning-when-signed-in-via-gh-cli-pat-api-key-or-environment-vari
  source_release: github-copilot-cli-2026-04-13-v1-0-25-github-308357690-3753e85b
  source_type: github_releases
  theme: account-access
  title: /logout shows a warning when signed in via gh CLI, PAT, API key, or environment…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-09-added-interactive-google-vertex-ai-setup-wizard-accessible-from-the-login-screen|Added
  interactive Google Vertex AI setup wizard accessible from the login screen…]]'
- '[[Changes/GitHub Copilot CLI/2026-04-09-support-bearer-token-authentication-for-byok-anthropic-models|Support
  bearer token authentication for BYOK Anthropic models]]'
- '[[Changes/Codex CLI/2026-04-10-2-account-and-access-changes-in-rust-v0-119-0|2
  Account and Access changes in rust-v0.119.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-04-13-v1-0-25-github-308357690-3753e85b|github-copilot-cli-2026-04-13-v1-0-25-github-308357690-3753e85b]]'
source_type: github_releases
theme: account-access
title: /logout shows a warning when signed in via gh CLI, PAT, API key, or environment…
type: change
---

<!-- chronolog:begin region="header" -->
# /logout shows a warning when signed in via gh CLI, PAT, API key, or environment…

**GitHub Copilot CLI** · 2026-04-13 · [[Themes/account-access|Account and Access]] · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.25) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-04-13-v1-0-25-github-308357690-3753e85b|1.0.25]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> /logout shows a warning when signed in via gh CLI, PAT, API key, or environment variable, since /logout only manages OAuth sessions
>
> Source: https://github.com/github/copilot-cli/releases/tag/v1.0.25
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-04-13-persist-resolved-model-in-session-history-and-defer-model-changes-during-active|Persist resolved model in session history and defer model changes during active turns]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-04-13-2-interface-experience-changes-in-v1-0-25|2 Interface Experience changes in v1.0.25]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-04-13-the-config-dir-flag-is-now-respected-when-selecting-the-active-model|The --config-dir flag is now respected when selecting the active model]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-04-13-custom-instruction-files-preserve-special-characters-like-and-placeholders|Custom instruction files preserve special characters like & and placeholders]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-04-13-2-collaboration-changes-in-v1-0-25|2 Collaboration changes in v1.0.25]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-04-13-5-apps-and-integrations-changes-in-v1-0-25|5 Apps and Integrations changes in v1.0.25]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-04-13-you-can-now-remote-control-your-cli-sessions-using-remote-or-remote|Remote control your CLI sessions using --remote or /remote]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-04-13-4-other-changes-in-v1-0-25|4 other changes in v1.0.25]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-04-10 · Codex CLI · [[Changes/Codex CLI/2026-04-10-2-account-and-access-changes-in-rust-v0-119-0|2 Account and Access changes in rust-v0.119.0]]
- Later: 2026-04-14 · Gemini CLI · [[Changes/Gemini CLI/2026-04-14-docs-update-mcp-server-oauth-redirect-port-documentation-by-adamfweidman-in-http|docs: update MCP server OAuth redirect port documentation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-04-13-4ac570&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-04-13-logout-shows-a-warning-when-signed-in-via-gh-cli-pat-api-key-or-environment-vari.md%0ACard%20ID%3A%20github-copilot-cli-2026-04-13-4ac570%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.25%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->