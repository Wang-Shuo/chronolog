---
card_id: github-copilot-cli-2026-06-13-c01194
date: '2026-06-13'
description: 'GitHub Copilot CLI · 2026-06-13 · Account and Access: Remote MCP OAuth
  servers start only once per matching config instead of restarting for each subagent'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1171
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 9c7994598cd6ef137e86c48dbd25bc33c745692e5784b072dcfd9b669a25ab03
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-13-c01194
  comparison: ''
  date: '2026-06-13'
  description: 'GitHub Copilot CLI — 1.0.62: Remote MCP OAuth servers start only once
    per matching config instead of restarting for each subagent'
  evidence:
  - quote: Remote MCP OAuth servers start only once per matching config instead of
      restarting for each subagent
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: remote-mcp-oauth-servers-start-only-once-per-matching-config-instead-of-restarti
  source_release: github-copilot-cli-2026-06-13-v1-0-62-github-339039020-f6ff7e5e
  source_type: github_releases
  theme: account-access
  theme_matches:
  - matched_terms:
    - oauth
    score: 50
    theme: account-access
  - matched_terms:
    - subagent
    score: 50
    theme: agent-mode
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  theme_resolution: manual-semantic-rule-v1
  title: Remote MCP OAuth servers start only once per matching config instead of restarting…
  type: change
related_changes:
- '[[Changes/v0/2026-06-08-2-account-and-access-changes-in-changelog-update|2 Account
  and Access changes in Changelog update]]'
- '[[Changes/GitHub Copilot CLI/2026-06-09-mcp-oauth-re-authentication-correctly-uses-the-saved-oauth-client-id-for-remote|MCP
  OAuth re-authentication correctly uses the saved OAuth client ID for remote servers]]'
- '[[Changes/OpenCode/2026-06-12-core-added-connector-based-authentication-flows-and-support-for-stored-provider|Core
  Added connector-based authentication flows and support for stored provider…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-13-v1-0-62-github-339039020-f6ff7e5e|github-copilot-cli-2026-06-13-v1-0-62-github-339039020-f6ff7e5e]]'
source_type: github_releases
theme: account-access
title: Remote MCP OAuth servers start only once per matching config instead of restarting…
type: change
---

<!-- chronolog:begin region="header" -->
# Remote MCP OAuth servers start only once per matching config instead of restarting…

**GitHub Copilot CLI** · 2026-06-13 · [[Themes/account-access|Account and Access]] · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.62) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-13-v1-0-62-github-339039020-f6ff7e5e|1.0.62]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Remote MCP OAuth servers start only once per matching config instead of restarting for each subagent
>
> Source: https://github.com/github/copilot-cli/releases/tag/v1.0.62
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-13-8-apps-and-integrations-changes-in-v1-0-62|8 Apps and Integrations changes in v1.0.62]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-13-speed-up-branch-and-head-detection-in-warm-sessions|Speed up branch and HEAD detection in warm sessions]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-13-4-agent-mode-changes-in-v1-0-62|4 Agent Mode changes in v1.0.62]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-13-every-and-after-can-now-schedule-slash-commands-e-g-every-1d-chronicle-standup|/every and /after can now schedule slash commands (e.g. /every 1d /chronicle standup)]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-13-voice-runtime-download-dialog-no-longer-reopens-in-a-loop-after-an-install-failu|Voice runtime download dialog no longer reopens in a loop after an install failure]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-06-13-2-safety-and-privacy-changes-in-v1-0-62|2 Safety and Privacy changes in v1.0.62]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-13-2-editor-experience-changes-in-v1-0-62|2 Editor Experience changes in v1.0.62]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-13-honor-max-output-tokens-for-byok-responses-providers|Honor max_output_tokens for BYOK Responses providers]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-06-13-git-commands-no-longer-flash-a-console-window-on-windows|Git commands no longer flash a console window on Windows]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-06-13-allow-sdk-clients-to-configure-session-memory-through-session-create-and-session|Allow SDK clients to configure session memory through session.create and session.resume]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-06-13-3-interface-experience-changes-in-v1-0-62|3 Interface Experience changes in v1.0.62]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-13-3-model-support-changes-in-v1-0-62|3 Model Support changes in v1.0.62]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-13-improve-color-contrast-in-github-themes-to-meet-wcag-aa-accessibility-standards|Improve color contrast in GitHub themes to meet WCAG AA accessibility standards]] · Accessibility and Localization
- [[Changes/GitHub Copilot CLI/2026-06-13-6-developer-workflow-changes-in-v1-0-62|6 Developer Workflow changes in v1.0.62]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-13-14-other-changes-in-v1-0-62|14 other changes in v1.0.62]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-06-12 · OpenCode · [[Changes/OpenCode/2026-06-12-core-added-connector-based-authentication-flows-and-support-for-stored-provider|Core Added connector-based authentication flows and support for stored provider…]]
- Later: 2026-06-13 · OpenCode · [[Changes/OpenCode/2026-06-13-added-external-browser-oauth-for-the-snowflake-cortex-provider|Added external browser OAuth for the Snowflake Cortex provider]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-13-c01194&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-13-remote-mcp-oauth-servers-start-only-once-per-matching-config-instead-of-restarti.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-13-c01194%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.62%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->