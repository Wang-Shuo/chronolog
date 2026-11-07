---
card_id: github-copilot-cli-2026-09-16-bc1bac
date: '2026-09-16'
description: 'GitHub Copilot CLI · 2026-09-16 · Apps and Integrations: 20 changes
  in 1.0.85 — Add `enable` and `disable` to `copilot plugin`, `copilot mcp` and `copilot…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1273
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d62ee7b4436e1e6fe2c9676bf5153403d1a88066a7b63b1002b18945fed77aaf
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-16-bc1bac
  comparison: ''
  date: '2026-09-16'
  description: 'GitHub Copilot CLI — 1.0.85: 20 Apps and Integrations changes'
  evidence:
  - quote: Add `enable` and `disable` to `copilot plugin`, `copilot mcp` and `copilot
      skill`, replacing `copilot plugins enable/disable --plugin|--mcp|--skill`
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Earlier messages remain visible when switching back to a background session
      with frequent hooks.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: MCP servers no longer fail to load when the CLI is connected to a running
      IDE. The in-process IDE bridge was rejected by config validation, which failed
      the plugin reload and restricted the session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: MCP turns continue even if tool list refresh fails after a tool change
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: MCP servers keep correct workspace source labels after trusting a folder
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Run sessionEnd hooks when /clear closes an interactive session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Plugin agents expand ${PLUGIN_ROOT} placeholders in mcp-servers frontmatter
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: A relative `--additional-mcp-config @<file>` path now resolves against
      the session working directory under `--resume=<id>` and `--worktree` instead
      of the launch directory, and `~/` expands.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Cancelling an MCP tool call now notifies the MCP server and cleanly ends
      the turn.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Computer Use now stays in sync across /computer and whole-plugin /plugin
      toggles.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Workspace .mcp.json servers load correctly after trusting a folder on startup
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Plugin-contributed agents discovered by the CLI can now be selected and
      run.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: MCP servers now see the same copilot-cli client identity when you add a
      server and when a session connects, carrying the shipped CLI version instead
      of 0.0.0
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Pressing Escape once cancels MCP inference approval prompts once
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: MCP reload summary shows servers still starting after timeout
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Configured hooks keep running after an extension restarts instead of silently
      stopping and later denying every tool call; the extension's own callback hooks
      resume once it re-registers
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Replace `copilot plugins install --skill [--scope project]` with `copilot
      skill add [--project]`; the `--scope` spelling is gone
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Remove the cross-kind `--kind`, `--scope`, `--mcp` and `--skill` flags
      from `copilot plugins`; use `copilot mcp` and `copilot skill`
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: '`copilot plugins list --json` now emits a flat array of plugins instead
      of the cross-kind `{ plugins, errors }` object; scripts reading `.plugins` must
      be updated'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: '`copilot plugins list` is now an alias of `copilot plugin list` and reports
      only plugins, no longer MCP servers, skills, instructions or LSP servers'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 20-apps-and-integrations-changes-in-v1-0-85
  source_release: github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9
  source_type: github_releases
  theme: apps-integrations
  title: 20 Apps and Integrations changes in v1.0.85
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-09-15-feat-extensions-harden-path-resolution-and-boundary-validation-in-extension-load|feat(extensions):
  harden path resolution and boundary validation in extension loader]]'
- '[[Changes/Lovable/2026-09-15-connect-your-app-to-power-bi|Connect your app to Power
  BI]]'
- '[[Changes/Claude/2026-09-16-claude-cowork-comes-to-every-conversation|Claude Cowork
  comes to every conversation]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9]]'
source_type: github_releases
theme: apps-integrations
title: 20 Apps and Integrations changes in v1.0.85
type: change
---

<!-- chronolog:begin region="header" -->
# 20 Apps and Integrations changes in v1.0.85

**GitHub Copilot CLI** · 2026-09-16 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.85) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|1.0.85]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add `enable` and `disable` to `copilot plugin`, `copilot mcp` and `copilot skill`, replacing `copilot plugins enable/disable --plugin|--mcp|--skill`

> Earlier messages remain visible when switching back to a background session with frequent hooks.

> MCP servers no longer fail to load when the CLI is connected to a running IDE. The in-process IDE bridge was rejected by config validation, which failed the plugin reload and restricted the session

> MCP turns continue even if tool list refresh fails after a tool change

> MCP servers keep correct workspace source labels after trusting a folder

> Run sessionEnd hooks when /clear closes an interactive session

> Plugin agents expand ${PLUGIN_ROOT} placeholders in mcp-servers frontmatter

> A relative `--additional-mcp-config @<file>` path now resolves against the session working directory under `--resume=<id>` and `--worktree` instead of the launch directory, and `~/` expands.

> Cancelling an MCP tool call now notifies the MCP server and cleanly ends the turn.

> Computer Use now stays in sync across /computer and whole-plugin /plugin toggles.

> Workspace .mcp.json servers load correctly after trusting a folder on startup

> Plugin-contributed agents discovered by the CLI can now be selected and run.

> MCP servers now see the same copilot-cli client identity when you add a server and when a session connects, carrying the shipped CLI version instead of 0.0.0

> Pressing Escape once cancels MCP inference approval prompts once

> MCP reload summary shows servers still starting after timeout

> Configured hooks keep running after an extension restarts instead of silently stopping and later denying every tool call; the extension's own callback hooks resume once it re-registers

> Replace `copilot plugins install --skill [--scope project]` with `copilot skill add [--project]`; the `--scope` spelling is gone

> Remove the cross-kind `--kind`, `--scope`, `--mcp` and `--skill` flags from `copilot plugins`; use `copilot mcp` and `copilot skill`

> `copilot plugins list --json` now emits a flat array of plugins instead of the cross-kind `{ plugins, errors }` object; scripts reading `.plugins` must be updated

> `copilot plugins list` is now an alias of `copilot plugin list` and reports only plugins, no longer MCP servers, skills, instructions or LSP servers

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.85
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-09-16-4-account-and-access-changes-in-v1-0-85|4 Account and Access changes in v1.0.85]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-09-16-6-developer-workflow-changes-in-v1-0-85|6 Developer Workflow changes in v1.0.85]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-09-16-9-editor-experience-changes-in-v1-0-85|9 Editor Experience changes in v1.0.85]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-09-16-speed-up-startup-when-resuming-an-existing-local-session-by-its-exact-uuid-with|Speed up startup when resuming an existing local session by its exact UUID with --resume]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-09-16-17-safety-and-privacy-changes-in-v1-0-85|17 Safety and Privacy changes in v1.0.85]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-09-16-13-model-support-changes-in-v1-0-85|13 Model Support changes in v1.0.85]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-09-16-usage-shows-per-model-ai-credit-consumption-in-usage-breakdowns|/usage shows per-model AI Credit consumption in usage breakdowns]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-09-16-3-memory-and-personalization-changes-in-v1-0-85|3 Memory and Personalization changes in v1.0.85]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-09-16-4-mobile-and-desktop-changes-in-v1-0-85|4 Mobile and Desktop changes in v1.0.85]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-09-16-add-json-to-copilot-plugin-list-copilot-plugin-marketplace-list-and-copilot-plug|Add --json to copilot plugin list, copilot plugin marketplace list…]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-09-16-3-context-window-changes-in-v1-0-85|3 Context Window changes in v1.0.85]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-09-16-2-agent-mode-changes-in-v1-0-85|2 Agent Mode changes in v1.0.85]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-09-16-share-notes-md-now-writes-the-exported-session-to-your-home-directory-instead-of|--share=~/notes.md now writes the exported session to your home directory instead…]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-09-16-when-session-history-is-truncated-or-compacted-just-as-a-turn-finishes-the-worki|When session history is truncated or compacted just as a turn finishes…]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-09-16-3-interface-experience-changes-in-v1-0-85|3 Interface Experience changes in v1.0.85]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-09-16-19-other-changes-in-v1-0-85|19 other changes in v1.0.85]] · Other changes
- [[Changes/GitHub Copilot CLI/2026-09-16-vim-mode-is-now-available-to-everyone-turn-it-on-with-vim-or-by-setting-editormo|Vim mode is now available to everyone]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-16 · Claude · [[Changes/Claude/2026-09-16-claude-cowork-comes-to-every-conversation|Claude Cowork comes to every conversation]]
- Later: 2026-09-16 · OpenHands · [[Changes/OpenHands/2026-09-16-9-apps-and-integrations-changes-in-v1-19-0|9 Apps and Integrations changes in v1.19.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-16-bc1bac&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-16-20-apps-and-integrations-changes-in-v1-0-85.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-16-bc1bac%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.85%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->