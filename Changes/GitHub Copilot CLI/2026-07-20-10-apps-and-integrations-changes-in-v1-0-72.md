---
card_id: github-copilot-cli-2026-07-20-d1e741
date: '2026-07-20'
description: 'GitHub Copilot CLI · 2026-07-20 · Apps and Integrations: 10 changes
  in 1.0.72 — An `agentStop` hook that always blocks no longer loops indefinitely:
  the CLI…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2775
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f35a8e480c1de1ef78a4cb3147c44a55cef2f8646481cd13ee8161ba05b9fafa
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-07-20-d1e741
  comparison: ''
  date: '2026-07-20'
  description: 'GitHub Copilot CLI — 1.0.72: 10 Apps and Integrations changes'
  evidence:
  - quote: 'An `agentStop` hook that always blocks no longer loops indefinitely: the
      CLI now ends the turn after 8 consecutive blocks, and `agentStop` hooks receive
      a `stop_hook_active` flag so they can detect a forced continuation and self-limit'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Deleting an MCP server with /mcp delete stops its running background process
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Show a connected message after a slow MCP server eventually connects
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Add `update`/`uninstall` verbs to `/plugins`, let `enable`/`disable`/`remove`
      target plugins, MCP servers, or skills via `--plugin`/`--mcp`/`--skill` flags
      or a positional kind, and support installing skills with `/plugins install --skill`
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Add a /plugins help command plus skill, MCP, and marketplace management
      for full /plugin parity
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Show MCP server status correctly for names like constructor and **proto**
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Install skills from the CLI with `copilot plugins install --skill <file,
      URL, or directory>` (add `--scope project` to a file or URL install to install
      into the repository)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Require SSO for remote control when managed settings demand it
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Add --plugin, --mcp, and --skill flags for plugin mutations
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Add skill removal support to `copilot plugins remove --skill`
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 10-apps-and-integrations-changes-in-v1-0-72
  source_release: github-copilot-cli-2026-07-20-v1-0-72-github-356903706-84b07b91
  source_type: github_releases
  theme: apps-integrations
  title: 10 Apps and Integrations changes in v1.0.72
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-18-changed-sessionstart-hooks-to-report-source-fork-when-a-session-begins-as-a-fork|Changed
  SessionStart hooks to report source "fork" when a session begins as a fork…]]'
- '[[Changes/Claude Code/2026-07-20-background-sessions-mcp-and-install-github-app-now-park-a-needs-input-request-in|Background
  sessions: /mcp and /install-github-app now park…]]'
- '[[Changes/ElevenLabs/2026-07-20-sdk-releases|SDK Releases]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-20-v1-0-72-github-356903706-84b07b91|github-copilot-cli-2026-07-20-v1-0-72-github-356903706-84b07b91]]'
source_type: github_releases
theme: apps-integrations
title: 10 Apps and Integrations changes in v1.0.72
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Apps and Integrations changes in v1.0.72

**GitHub Copilot CLI** · 2026-07-20 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.72) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-20-v1-0-72-github-356903706-84b07b91|1.0.72]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> An `agentStop` hook that always blocks no longer loops indefinitely: the CLI now ends the turn after 8 consecutive blocks, and `agentStop` hooks receive a `stop_hook_active` flag so they can detect a forced continuation and self-limit

> Deleting an MCP server with /mcp delete stops its running background process

> Show a connected message after a slow MCP server eventually connects

> Add `update`/`uninstall` verbs to `/plugins`, let `enable`/`disable`/`remove` target plugins, MCP servers, or skills via `--plugin`/`--mcp`/`--skill` flags or a positional kind, and support installing skills with `/plugins install --skill`

> Add a /plugins help command plus skill, MCP, and marketplace management for full /plugin parity

> Show MCP server status correctly for names like constructor and **proto**

> Install skills from the CLI with `copilot plugins install --skill <file, URL, or directory>` (add `--scope project` to a file or URL install to install into the repository)

> Require SSO for remote control when managed settings demand it

> Add --plugin, --mcp, and --skill flags for plugin mutations

> Add skill removal support to `copilot plugins remove --skill`

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.72
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-07-20-the-sessions-sidebar-is-now-navigable-with-the-keyboard-and-mouse-arrows-open-an|The Sessions sidebar is now navigable with the keyboard and mouse…]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-07-20-8-developer-workflow-changes-in-v1-0-72|8 Developer Workflow changes in v1.0.72]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-07-20-2-context-window-changes-in-v1-0-72|2 Context Window changes in v1.0.72]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-07-20-4-safety-and-privacy-changes-in-v1-0-72|4 Safety and Privacy changes in v1.0.72]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-07-20-preserve-pasted-prompt-content-when-changing-models-through-ctrl-x-model|Preserve pasted prompt content when changing models through Ctrl+X /model]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-07-20-3-agent-mode-changes-in-v1-0-72|3 Agent Mode changes in v1.0.72]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-07-20-2-editor-experience-changes-in-v1-0-72|2 Editor Experience changes in v1.0.72]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-07-20-13-other-changes-in-v1-0-72|13 other changes in v1.0.72]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-07-20 · ElevenLabs · [[Changes/ElevenLabs/2026-07-20-sdk-releases|SDK Releases]]
- Later: 2026-07-21 · Claude Code · [[Changes/Claude Code/2026-07-21-capped-the-frontend-design-plugin-suggestion-tip-at-3-lifetime-impressions-inste|Capped the frontend-design plugin suggestion tip at 3 lifetime impressions instead…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-07-20-d1e741&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-07-20-10-apps-and-integrations-changes-in-v1-0-72.md%0ACard%20ID%3A%20github-copilot-cli-2026-07-20-d1e741%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.72%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->