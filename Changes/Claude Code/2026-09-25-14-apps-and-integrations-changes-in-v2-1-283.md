---
card_id: claude-code-2026-09-25-1e0680
date: '2026-09-25'
description: 'Claude Code · 2026-09-25 · Apps and Integrations: 14 changes in v2.1.283
  — Added MCP tool, WebFetch and WebSearch outputs to the `tool.output` OpenTelemetry…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1282
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e9efed8556dd474593e74582ff22795c95a78616e780fbc5c83c9e92944e9217
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-25-1e0680
  comparison: ''
  date: '2026-09-25'
  description: 'Claude Code — v2.1.283: 14 Apps and Integrations changes'
  evidence:
  - quote: Added MCP tool, WebFetch and WebSearch outputs to the `tool.output` OpenTelemetry
      span event when `OTEL_LOG_TOOL_CONTENT=1`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: Added `path` to `--plugin-dir` load-failure entries in the stream-json
      `system/init` `plugin_errors`, naming the directory that did not load
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: 'Added an opt-in `load_test_mode` block to the Claude apps gateway config:
      requests are built and signed but not sent upstream, and clients get a canned
      reply, so a deployment can be load tested'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: Added a `mantle` upstream provider to the Claude apps gateway for Amazon
      Bedrock's Mantle endpoint
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: 'Improved the `/mcp` tool list: it shows more tools at once, scrolls with
      the page keys and mouse, and marks tools your organization blocked with a warning
      icon'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: 'Improved MCP tool results: images returned by MCP tools are now also saved
      to a file, so Bash, Read and other tools can open them'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: 'Improved the browser page shown after signing in to an MCP server: centered
      layout, dark mode, and new artwork'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: Improved the Skill tool's reply when a skill belongs to a plugin that failed
      to load, so Claude tells you the plugin could not be loaded instead of calling
      the skill uninstalled
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: 'Improved recovery from an `installed_plugins.json` that cannot be read
      at all: its contents are kept in a file beside it before it is rebuilt, and
      `claude plugin list` names that file'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: Changed `Skill(anthropic-skills:<name>)` deny rules to also block that
      skill when Claude Desktop delivers it as a plugin, and `Skill(skill:<name>)`
      denies to match the skill's alias and display name
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: Changed `claude plugin eval` to require git 2.31 or later when git is installed;
      a run on an older git is refused with a message naming the version
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: 'Self-hosted runner: Changed lifecycle hooks'' git to skip a repository''s
      Git LFS `pre-push` hook, ignore a writable system `core.hooksPath`, and not
      sign commits without `--configure-git`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: '[Claude Tag] Added a "Channels Claude can search" admin setting that limits
      Claude''s Slack search to public channels it has been added to, set per organization,
      workspace or channel'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: '[Claude Tag] Added a Back to Slack button on the page shown after connecting
      your Claude account, returning you to the thread you started from'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 14-apps-and-integrations-changes-in-v2-1-283
  source_release: claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8
  source_type: github_releases
  theme: apps-integrations
  title: 14 Apps and Integrations changes in v2.1.283
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-23-18-apps-and-integrations-changes-in-v2-1-281|18
  Apps and Integrations changes in v2.1.281]]'
- '[[Changes/Cursor/2026-09-23-integrations|Integrations]]'
- '[[Changes/Claude Code/2026-09-24-8-apps-and-integrations-changes-in-v2-1-282|8
  Apps and Integrations changes in v2.1.282]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8|claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8]]'
source_type: github_releases
theme: apps-integrations
title: 14 Apps and Integrations changes in v2.1.283
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Apps and Integrations changes in v2.1.283

**Claude Code** · 2026-09-25 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.283) · from [[Releases/Claude Code/claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8|v2.1.283]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added MCP tool, WebFetch and WebSearch outputs to the `tool.output` OpenTelemetry span event when `OTEL_LOG_TOOL_CONTENT=1`

> Added `path` to `--plugin-dir` load-failure entries in the stream-json `system/init` `plugin_errors`, naming the directory that did not load

> Added an opt-in `load_test_mode` block to the Claude apps gateway config: requests are built and signed but not sent upstream, and clients get a canned reply, so a deployment can be load tested

> Added a `mantle` upstream provider to the Claude apps gateway for Amazon Bedrock's Mantle endpoint

> Improved the `/mcp` tool list: it shows more tools at once, scrolls with the page keys and mouse, and marks tools your organization blocked with a warning icon

> Improved MCP tool results: images returned by MCP tools are now also saved to a file, so Bash, Read and other tools can open them

> Improved the browser page shown after signing in to an MCP server: centered layout, dark mode, and new artwork

> Improved the Skill tool's reply when a skill belongs to a plugin that failed to load, so Claude tells you the plugin could not be loaded instead of calling the skill uninstalled

> Improved recovery from an `installed_plugins.json` that cannot be read at all: its contents are kept in a file beside it before it is rebuilt, and `claude plugin list` names that file

> Changed `Skill(anthropic-skills:<name>)` deny rules to also block that skill when Claude Desktop delivers it as a plugin, and `Skill(skill:<name>)` denies to match the skill's alias and display name

> Changed `claude plugin eval` to require git 2.31 or later when git is installed; a run on an older git is refused with a message naming the version

> Self-hosted runner: Changed lifecycle hooks' git to skip a repository's Git LFS `pre-push` hook, ignore a writable system `core.hooksPath`, and not sign commits without `--configure-git`

> [Claude Tag] Added a "Channels Claude can search" admin setting that limits Claude's Slack search to public channels it has been added to, set per organization, workspace or channel

> [Claude Tag] Added a Back to Slack button on the page shown after connecting your Claude account, returning you to the thread you started from

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-25-3-developer-workflow-changes-in-v2-1-283|3 Developer Workflow changes in v2.1.283]] · Developer Workflow
- [[Changes/Claude Code/2026-09-25-improved-startup-claude-p-and-claude-code-remote-no-longer-load-the-interactive|Improved startup: claude -p and Claude Code Remote no longer load the interactive…]] · Agent Mode
- [[Changes/Claude Code/2026-09-25-3-safety-and-privacy-changes-in-v2-1-283|3 Safety and Privacy changes in v2.1.283]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-25-improved-prompt-audit-on-claude-code-configuration-stale-paths-stale-commands-an|Improved prompt-audit on Claude Code configuration]] · Files and Data
- [[Changes/Claude Code/2026-09-25-2-context-window-changes-in-v2-1-283|2 Context Window changes in v2.1.283]] · Context Window
- [[Changes/Claude Code/2026-09-25-2-reliability-and-performance-changes-in-v2-1-283|2 Reliability and Performance changes in v2.1.283]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-25-improved-lists-in-help-hooks-copy-chrome-memory-ide-release-notes-rewind-diff-re|Improved lists in /help, /hooks, /copy, /chrome, /memory, /ide…]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-25-2-interface-experience-changes-in-v2-1-283|2 Interface Experience changes in v2.1.283]] · Interface Experience
- [[Changes/Claude Code/2026-09-25-3-model-support-changes-in-v2-1-283|3 Model Support changes in v2.1.283]] · Model Support
- [[Changes/Claude Code/2026-09-25-9-other-changes-in-v2-1-283|9 other changes in v2.1.283]] · Other changes
- [[Changes/Claude Code/2026-09-25-added-doctor-prompt-audit-also-checkup-prompt-audit-to-audit-your-claude-md-file|Added /doctor prompt-audit (also /checkup prompt-audit) to audit your CLAUDE.md…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-24 · Claude Code · [[Changes/Claude Code/2026-09-24-8-apps-and-integrations-changes-in-v2-1-282|8 Apps and Integrations changes in v2.1.282]]
- Later: 2026-09-28 · Claude Code · [[Changes/Claude Code/2026-09-28-9-apps-and-integrations-changes-in-v2-1-284|9 Apps and Integrations changes in v2.1.284]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-25-1e0680&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-25-14-apps-and-integrations-changes-in-v2-1-283.md%0ACard%20ID%3A%20claude-code-2026-09-25-1e0680%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.283%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->