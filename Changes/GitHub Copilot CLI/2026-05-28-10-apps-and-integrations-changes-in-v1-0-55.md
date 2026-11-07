---
card_id: github-copilot-cli-2026-05-28-30fb30
date: '2026-05-28'
description: 'GitHub Copilot CLI · 2026-05-28 · Apps and Integrations: 10 changes
  in 1.0.55 — MCP server configuration form saves the latest typed value when pressing
  Ctrl+S'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2722
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a9cba5a7c2edcc0756828d49621e3432f5b454b90292825dda80baacb8f6f91b
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-05-28-30fb30
  comparison: ''
  date: '2026-05-28'
  description: 'GitHub Copilot CLI — 1.0.55: 10 Apps and Integrations changes'
  evidence:
  - quote: MCP server configuration form saves the latest typed value when pressing
      Ctrl+S
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.55
  - quote: Extension log files are now captured per extension and surfaced in the
      extensions_manage tool to help diagnose failures
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.55
  - quote: Project extensions in .github/extensions are now discovered in non-git
      (folder-backed) workspaces
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.55
  - quote: MCP configuration now opens in its own dedicated screen, with scrollable
      server and tool lists when content exceeds the visible area
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.55
  - quote: Hook progress streaming shows real-time status messages from long-running
      hooks in the timeline
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.55
  - quote: 'pluginDirectories on session.create and session.resume RPC: SDK clients
      can mount Open Plugins-format directories per session.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.55
  - quote: Support owner/repo#ref syntax when adding plugins from the marketplace
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.55
  - quote: --plugin-dir skills now take precedence over personal-home (~/.copilot,
      ~/.agents) skills with the same name. Order is now project > plugin-dir > personal
      > custom.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.55
  - quote: /env now shows loaded extensions with their status and source
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.55
  - quote: Extensions launch correctly when the CLI runs as a single-executable application
      (SEA)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.55
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 10-apps-and-integrations-changes-in-v1-0-55
  source_release: github-copilot-cli-2026-05-28-v1-0-55-github-331104258-cce42856
  source_type: github_releases
  theme: apps-integrations
  title: 10 Apps and Integrations changes in v1.0.55
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-28-4-apps-and-integrations-changes-in-v2-1-154|4
  Apps and Integrations changes in v2.1.154]]'
- '[[Changes/Cline/2026-05-28-move-the-vs-code-extension-project-into-apps-vscode|Move
  the VS Code extension project into apps/vscode]]'
- '[[Changes/Codex CLI/2026-05-28-14-apps-and-integrations-changes-in-rust-v0-135-0|14
  Apps and Integrations changes in rust-v0.135.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-28-v1-0-55-github-331104258-cce42856|github-copilot-cli-2026-05-28-v1-0-55-github-331104258-cce42856]]'
source_type: github_releases
theme: apps-integrations
title: 10 Apps and Integrations changes in v1.0.55
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Apps and Integrations changes in v1.0.55

**GitHub Copilot CLI** · 2026-05-28 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.55) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-28-v1-0-55-github-331104258-cce42856|1.0.55]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> MCP server configuration form saves the latest typed value when pressing Ctrl+S

> Extension log files are now captured per extension and surfaced in the extensions_manage tool to help diagnose failures

> Project extensions in .github/extensions are now discovered in non-git (folder-backed) workspaces

> MCP configuration now opens in its own dedicated screen, with scrollable server and tool lists when content exceeds the visible area

> Hook progress streaming shows real-time status messages from long-running hooks in the timeline

> pluginDirectories on session.create and session.resume RPC: SDK clients can mount Open Plugins-format directories per session.

> Support owner/repo#ref syntax when adding plugins from the marketplace

> --plugin-dir skills now take precedence over personal-home (~/.copilot, ~/.agents) skills with the same name. Order is now project > plugin-dir > personal > custom.

> /env now shows loaded extensions with their status and source

> Extensions launch correctly when the CLI runs as a single-executable application (SEA)

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.55
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-05-28-clipboard-correctly-copies-cjk-and-supplementary-plane-unicode-characters-on-win|Clipboard correctly copies CJK and supplementary-plane Unicode characters on Windows]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-05-28-vote-memory-tool-calls-are-throttled-per-response-and-per-interaction-to-prevent|vote_memory tool calls are throttled per response and per interaction to prevent…]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-05-28-7-interface-experience-changes-in-v1-0-55|7 Interface Experience changes in v1.0.55]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-05-28-3-agent-mode-changes-in-v1-0-55|3 Agent Mode changes in v1.0.55]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-05-28-3-pricing-model-changes-in-v1-0-55|3 Pricing Model changes in v1.0.55]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-05-28-3-developer-workflow-changes-in-v1-0-55|3 Developer Workflow changes in v1.0.55]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-05-28-schedule-manager-hint-bar-text-no-longer-wraps-over-dialog-borders-when-entries|Schedule manager hint bar text no longer wraps over dialog borders when entries are added]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-05-28-2-editor-experience-changes-in-v1-0-55|2 Editor Experience changes in v1.0.55]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-05-28-2-context-window-changes-in-v1-0-55|2 Context Window changes in v1.0.55]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-05-28-3-model-support-changes-in-v1-0-55|3 Model Support changes in v1.0.55]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-05-28-canvas-tools-with-optional-object-input-schemas-open-correctly-without-validatio|Canvas tools with optional object input schemas open correctly without validation errors]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-05-28-8-other-changes-in-v1-0-55|8 other changes in v1.0.55]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-28 · Codex CLI · [[Changes/Codex CLI/2026-05-28-14-apps-and-integrations-changes-in-rust-v0-135-0|14 Apps and Integrations changes in rust-v0.135.0]]
- Later: 2026-05-28 · Kimi Code · [[Changes/Kimi Code/2026-05-28-2-apps-and-integrations-changes-in-kimi-code-0-5-0|2 Apps and Integrations changes in Kimi Code 0.5.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-05-28-30fb30&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-05-28-10-apps-and-integrations-changes-in-v1-0-55.md%0ACard%20ID%3A%20github-copilot-cli-2026-05-28-30fb30%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.55%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->