---
card_id: github-copilot-cli-2026-07-10-c641f0
date: '2026-07-10'
description: 'GitHub Copilot CLI · 2026-07-10 · Safety and Privacy: 5 changes in 1.0.70
  — Add --sandbox and --no-sandbox flags to turn the OS-level shell sandbox on or
  off…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1181
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a5e5767c35336d45bda275689d2c032472c375daecc62eb88cba4b8acbe20365
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-07-10-c641f0
  comparison: ''
  date: '2026-07-10'
  description: 'GitHub Copilot CLI — 1.0.70: 5 Safety and Privacy changes'
  evidence:
  - quote: Add --sandbox and --no-sandbox flags to turn the OS-level shell sandbox
      on or off for the current session only, without changing your saved sandbox
      setting (useful with -p)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.70
  - quote: Declining an extension's permission prompt no longer disables tool approvals
      for the rest of the session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.70
  - quote: Restore tool event ordering so permission prompts appear after tool start
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.70
  - quote: Dismiss other pending read and fetch sandbox-bypass prompts after you disable
      the sandbox
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.70
  - quote: Mark locally-spawned MCP servers that run inside the sandbox in `/mcp list`
      (e.g. `connected (sandboxed)`)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.70
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 5-safety-and-privacy-changes-in-v1-0-70
  source_release: github-copilot-cli-2026-07-10-v1-0-70-github-351853788-0192ae35
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in v1.0.70
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-07-09-on-desktop-work-can-use-local-files-and-desktop-apps-with-your-permission-the-bu-1e4d11|On
  desktop, Work can use local files and desktop apps with your permission]]'
- '[[Changes/Codex CLI/2026-07-09-4-safety-and-privacy-changes-in-rust-v0-144-0|4
  Safety and Privacy changes in rust-v0.144.0]]'
- '[[Changes/Claude Code/2026-07-10-fixed-permission-prompt-tool-pointing-at-an-mcp-server-crashing-with-mcp-tool-no|Fixed
  --permission-prompt-tool pointing at an MCP server crashing…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-10-v1-0-70-github-351853788-0192ae35|github-copilot-cli-2026-07-10-v1-0-70-github-351853788-0192ae35]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in v1.0.70
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in v1.0.70

**GitHub Copilot CLI** · 2026-07-10 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.70) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-10-v1-0-70-github-351853788-0192ae35|1.0.70]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add --sandbox and --no-sandbox flags to turn the OS-level shell sandbox on or off for the current session only, without changing your saved sandbox setting (useful with -p)

> Declining an extension's permission prompt no longer disables tool approvals for the rest of the session

> Restore tool event ordering so permission prompts appear after tool start

> Dismiss other pending read and fetch sandbox-bypass prompts after you disable the sandbox

> Mark locally-spawned MCP servers that run inside the sandbox in `/mcp list` (e.g. `connected (sandboxed)`)

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.70
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-07-10-3-developer-workflow-changes-in-v1-0-70|3 Developer Workflow changes in v1.0.70]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-07-10-long-running-sessions-refresh-enterprise-managed-settings-hourly|Long-running sessions refresh enterprise managed settings hourly]] · Enterprise and Administration
- [[Changes/GitHub Copilot CLI/2026-07-10-4-model-support-changes-in-v1-0-70|4 Model Support changes in v1.0.70]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-07-10-4-interface-experience-changes-in-v1-0-70|4 Interface Experience changes in v1.0.70]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-07-10-2-editor-experience-changes-in-v1-0-70|2 Editor Experience changes in v1.0.70]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-07-10-press-tab-to-switch-the-context-window-in-model|Press Tab to switch the context window in /model]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-07-10-9-apps-and-integrations-changes-in-v1-0-70|9 Apps and Integrations changes in v1.0.70]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-07-10-2-account-and-access-changes-in-v1-0-70|2 Account and Access changes in v1.0.70]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-07-10-3-agent-mode-changes-in-v1-0-70|3 Agent Mode changes in v1.0.70]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-07-10-12-other-changes-in-v1-0-70|12 other changes in v1.0.70]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-10 · Claude Code · [[Changes/Claude Code/2026-07-10-fixed-permission-prompt-tool-pointing-at-an-mcp-server-crashing-with-mcp-tool-no|Fixed --permission-prompt-tool pointing at an MCP server crashing…]]
- Later: 2026-07-11 · Claude Code · [[Changes/Claude Code/2026-07-11-2-safety-and-privacy-changes-in-v2-1-207|2 Safety and Privacy changes in v2.1.207]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-07-10-c641f0&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-07-10-5-safety-and-privacy-changes-in-v1-0-70.md%0ACard%20ID%3A%20github-copilot-cli-2026-07-10-c641f0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.70%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->