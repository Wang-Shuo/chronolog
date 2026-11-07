---
card_id: github-copilot-cli-2026-09-04-2f3d14
date: '2026-09-04'
description: 'GitHub Copilot CLI · 2026-09-04 · Apps and Integrations: 7 changes in
  1.0.83 — MCP tools remain callable after MCP server restarts'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1261
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 30887360fd6fcd633a3e1064cba71a348ca27d9a2b0d4d690b1fea0cc8eb40d5
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-04-2f3d14
  comparison: ''
  date: '2026-09-04'
  description: 'GitHub Copilot CLI — 1.0.83: 7 Apps and Integrations changes'
  evidence:
  - quote: MCP tools remain callable after MCP server restarts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: MCP servers configured by your agent stay available after built-in sub-agent
      turns.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: Enterprise-denied MCP servers can no longer start before the managed allow/deny
      policy resolves; server startup now waits for the managed-settings fetch instead
      of racing it
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: A relative `--add-dir` or `--plugin-dir` path now resolves against the
      session's working directory under `--resume=<id>` and `--worktree`, instead
      of the directory the CLI was launched from. Relative values are also resolved
      after `-C` is applied, so `-C` no longer has to precede either option on the
      command line
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: MCP servers contributed by a plugin are no longer labelled "User" in the
      MCP dashboard, and a server from a bundled plugin is now shown as built-in and
      names the plugin it came from.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: '`/mcp config` and the MCP add/edit/authenticate forms now open in the
      plugins dashboard instead of a separate MCP manager, so closing a form returns
      to the server list.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: Plugin list commands and /plugin now show bundled built-in plugins.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 7-apps-and-integrations-changes-in-v1-0-83
  source_release: github-copilot-cli-2026-09-04-v1-0-83-github-382838246-6f996d9c
  source_type: github_releases
  theme: apps-integrations
  title: 7 Apps and Integrations changes in v1.0.83
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-03-18-apps-and-integrations-changes-in-rust-v0-153-0|18
  Apps and Integrations changes in rust-v0.153.0]]'
- '[[Changes/OpenClaw/2026-09-03-26-apps-and-integrations-changes-in-v2026-9-1|26
  Apps and Integrations changes in v2026.9.1]]'
- '[[Changes/Claude Code/2026-09-04-vscode-added-an-add-server-form-and-a-remove-action-to-the-mcp-servers-dialog-so|VSCode
  Added an Add server form and a Remove action to the MCP servers dialog…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-04-v1-0-83-github-382838246-6f996d9c|github-copilot-cli-2026-09-04-v1-0-83-github-382838246-6f996d9c]]'
source_type: github_releases
theme: apps-integrations
title: 7 Apps and Integrations changes in v1.0.83
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Apps and Integrations changes in v1.0.83

**GitHub Copilot CLI** · 2026-09-04 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.83) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-04-v1-0-83-github-382838246-6f996d9c|1.0.83]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> MCP tools remain callable after MCP server restarts

> MCP servers configured by your agent stay available after built-in sub-agent turns.

> Enterprise-denied MCP servers can no longer start before the managed allow/deny policy resolves; server startup now waits for the managed-settings fetch instead of racing it

> A relative `--add-dir` or `--plugin-dir` path now resolves against the session's working directory under `--resume=<id>` and `--worktree`, instead of the directory the CLI was launched from. Relative values are also resolved after `-C` is applied, so `-C` no longer has to precede either option on the command line

> MCP servers contributed by a plugin are no longer labelled "User" in the MCP dashboard, and a server from a bundled plugin is now shown as built-in and names the plugin it came from.

> `/mcp config` and the MCP add/edit/authenticate forms now open in the plugins dashboard instead of a separate MCP manager, so closing a form returns to the server list.

> Plugin list commands and /plugin now show bundled built-in plugins.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.83
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-09-04-long-running-sessions-on-linux-return-freed-memory-to-the-system-instead-of-hold|Long-running sessions on Linux return freed memory to the system instead of holding…]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-09-04-enterprise-admins-can-pin-sign-in-to-approved-github-organizations-with-the-forc|Enterprise admins can pin sign-in to approved GitHub organizations…]] · Enterprise and Administration
- [[Changes/GitHub Copilot CLI/2026-09-04-2-editor-experience-changes-in-v1-0-83|2 Editor Experience changes in v1.0.83]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-09-04-3-model-support-changes-in-v1-0-83|3 Model Support changes in v1.0.83]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-09-04-detect-the-herdr-terminal-multiplexer-instead-of-mistaking-it-for-tmux-so-the-ki|Detect the herdr terminal multiplexer instead of mistaking it for tmux, so the Kitty…]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-09-04-exporting-a-resumed-session-with-share-or-share-gist-writes-the-whole-transcript|Exporting a resumed session with --share or --share-gist writes the whole transcript…]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-09-04-5-safety-and-privacy-changes-in-v1-0-83|5 Safety and Privacy changes in v1.0.83]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-09-04-stopping-a-timed-out-shell-command-now-lets-queued-messages-run-and-sessions-ret|Stopping a timed-out shell command now lets queued messages run and sessions return…]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-09-04-add-recent-created-name-and-classic-none-sorting-to-the-split-sessions-sidebar-w|Add Recent, Created, Name, and classic None sorting to the split Sessions sidebar…]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-09-04-3-account-and-access-changes-in-v1-0-83|3 Account and Access changes in v1.0.83]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-09-04-11-other-changes-in-v1-0-83|11 other changes in v1.0.83]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-04 · Claude Code · [[Changes/Claude Code/2026-09-04-vscode-added-an-add-server-form-and-a-remove-action-to-the-mcp-servers-dialog-so|VSCode Added an Add server form and a Remove action to the MCP servers dialog…]]
- Later: 2026-09-05 · OpenClaw · [[Changes/OpenClaw/2026-09-05-35-apps-and-integrations-changes-in-v2026-9-2|35 Apps and Integrations changes in v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-04-2f3d14&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-04-7-apps-and-integrations-changes-in-v1-0-83.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-04-2f3d14%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.83%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->