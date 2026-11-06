---
card_id: github-copilot-cli-2026-06-30-88e34d
date: '2026-06-30'
description: 'GitHub Copilot CLI · 2026-06-30 · Account and Access: 6 changes in 1.0.66
  — Properly recover MCP host-delegated connections when OAuth tokens expire or need…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1188
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9414fb2fe6c22ae8779b50c279f808e638841cb58ff898af47a4b603da681d20
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-30-88e34d
  comparison: ''
  date: '2026-06-30'
  description: 'GitHub Copilot CLI — 1.0.66: 6 Account and Access changes'
  evidence:
  - quote: Properly recover MCP host-delegated connections when OAuth tokens expire
      or need broader scopes
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: MCP tools on OAuth-authenticated remote servers now recover automatically
      after a mid-session token expiry, matching the existing OIDC retry behaviour.
      A 401 during a tool call triggers a non-interactive reconnect, and servers needing
      interactive re-auth are retried at the start of the next turn.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Pass a task to /worktree (e.g. 'fix the login redirect') to name the branch
      for that task and run the sentence as the first prompt in the new worktree
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Added runtime telemetry for the MCP host token-injection OAuth flow, recording
      when an OAuth broadcast is emitted to the host and how the host responds (token
      or cancelled) with response latency
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Quit cleanly with Ctrl+D during startup before authentication completes
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Refresh MCP server headers automatically after authentication changes
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 6-account-and-access-changes-in-v1-0-66
  source_release: github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740
  source_type: github_releases
  theme: account-access
  title: 6 Account and Access changes in v1.0.66
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-06-25-macos-authentication-clients-can-honor-system-proxy-pac-and-wpad-settings-when-r|macOS
  authentication clients can honor system proxy, PAC, and WPAD settings…]]'
- '[[Changes/Codex CLI/2026-06-25-added-opt-in-windows-system-proxy-support-for-authentication-including-pac-wpad|Added
  opt-in Windows system proxy support for authentication, including PAC, WPAD…]]'
- '[[Changes/GitHub Copilot CLI/2026-06-30-mcp-oauth-against-microsoft-entra-servers-behind-a-tenant-vanity-domain-e-g-copi|MCP
  OAuth against Microsoft Entra servers behind a tenant vanity domain…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740|github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740]]'
source_type: github_releases
theme: account-access
title: 6 Account and Access changes in v1.0.66
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Account and Access changes in v1.0.66

**GitHub Copilot CLI** · 2026-06-30 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.66) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740|1.0.66]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Properly recover MCP host-delegated connections when OAuth tokens expire or need broader scopes

> MCP tools on OAuth-authenticated remote servers now recover automatically after a mid-session token expiry, matching the existing OIDC retry behaviour. A 401 during a tool call triggers a non-interactive reconnect, and servers needing interactive re-auth are retried at the start of the next turn.

> Pass a task to /worktree (e.g. 'fix the login redirect') to name the branch for that task and run the sentence as the first prompt in the new worktree

> Added runtime telemetry for the MCP host token-injection OAuth flow, recording when an OAuth broadcast is emitted to the host and how the host responds (token or cancelled) with response latency

> Quit cleanly with Ctrl+D during startup before authentication completes

> Refresh MCP server headers automatically after authentication changes

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.66
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-30-2-editor-experience-changes-in-v1-0-66|2 Editor Experience changes in v1.0.66]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-30-voice-mode-turns-itself-off-when-the-engine-fails-to-start-at-boot|Voice mode turns itself off when the engine fails to start at boot]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-06-30-perform-tokenizer-warmup-in-parallel-on-a-background-thread-for-better-startup-p|Perform tokenizer warmup in parallel on a background thread for better startup performance]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-30-2-collaboration-changes-in-v1-0-66|2 Collaboration changes in v1.0.66]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-06-30-pr-auto-now-starts-a-self-paced-loop-that-fixes-one-thing-per-run-and-paces-itse|/pr auto now starts a self-paced loop that fixes one thing per run and paces itself…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-30-3-interface-experience-changes-in-v1-0-66|3 Interface Experience changes in v1.0.66]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-30-9-apps-and-integrations-changes-in-v1-0-66|9 Apps and Integrations changes in v1.0.66]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-30-match-the-terminal-text-color-to-the-github-theme-canvas|Match the terminal text color to the GitHub theme canvas]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-06-30-21-developer-workflow-changes-in-v1-0-66|21 Developer Workflow changes in v1.0.66]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-30-configure-subagent-concurrency-and-depth-limits-in-settings-usage-based-billing|Configure subagent concurrency and depth limits in /settings (usage-based billing users)]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-06-30-2-mobile-and-desktop-changes-in-v1-0-66|2 Mobile and Desktop changes in v1.0.66]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-06-30-3-safety-and-privacy-changes-in-v1-0-66|3 Safety and Privacy changes in v1.0.66]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-30-recover-corrupted-session-history-on-load|Recover corrupted session history on load]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-06-30-8-agent-mode-changes-in-v1-0-66|8 Agent Mode changes in v1.0.66]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-30-keep-session-store-searches-and-context-lookups-responsive|Keep session-store searches and context lookups responsive]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-06-30-5-model-support-changes-in-v1-0-66|5 Model Support changes in v1.0.66]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-30-33-other-changes-in-v1-0-66|33 other changes in v1.0.66]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-mcp-oauth-against-microsoft-entra-servers-behind-a-tenant-vanity-domain-e-g-copi|MCP OAuth against Microsoft Entra servers behind a tenant vanity domain…]]
- Later: 2026-07-01 · Claude Code · [[Changes/Claude Code/2026-07-01-login-now-opens-the-sign-in-dialog-from-the-claude-agents-view-instead-of-saying|/login now opens the sign-in dialog from the claude agents view instead…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-30-88e34d&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-30-6-account-and-access-changes-in-v1-0-66.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-30-88e34d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.66%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->