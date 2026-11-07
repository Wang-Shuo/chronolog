---
card_id: github-copilot-cli-2026-06-23-c97417
date: '2026-06-23'
description: 'GitHub Copilot CLI · 2026-06-23 · Agent Mode: 6 changes in 1.0.64 —
  Configure the rubber-duck subagent in /subagents, including a complementary model
  strategy…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1083
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e96eeec79437911325bd0497a83a5ed2c7d29614e0ee4afcd797476c524c8053
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-23-c97417
  comparison: ''
  date: '2026-06-23'
  description: 'GitHub Copilot CLI — 1.0.64: 6 Agent Mode changes'
  evidence:
  - quote: Configure the rubber-duck subagent in /subagents, including a complementary
      model strategy that picks an opposite-family model
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Autopilot mode now returns to interactive mode after the agent calls task_complete,
      so you aren't left in autopilot for your next prompt
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Keep task companion tools available to custom agents that use the task
      or agent alias
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Custom agents using a tools wildcard '\*' now respect deferredToolLoading
      opt-in switch
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Run queued ! shell commands locally instead of sending them to the agent
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Allow disabling task and explore built-in subagents
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 6-agent-mode-changes-in-v1-0-64
  source_release: github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd
  source_type: github_releases
  theme: agent-mode
  title: 6 Agent Mode changes in v1.0.64
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-06-22-elevenagents-ee09f3|ElevenAgents]]'
- '[[Changes/Google Antigravity/2026-06-22-new-entries-in-the-sensitive-paths-list-vscode-and-cache-are-now-recognized-as-s|New
  entries in the sensitive paths list]]'
- '[[Changes/Kimi Code/2026-06-22-allow-long-running-foreground-commands-and-subagents-to-be-moved-into-background|Allow
  long-running foreground commands and subagents to be moved into background…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd|github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd]]'
source_type: github_releases
theme: agent-mode
title: 6 Agent Mode changes in v1.0.64
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Agent Mode changes in v1.0.64

**GitHub Copilot CLI** · 2026-06-23 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.64) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd|1.0.64]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Configure the rubber-duck subagent in /subagents, including a complementary model strategy that picks an opposite-family model

> Autopilot mode now returns to interactive mode after the agent calls task_complete, so you aren't left in autopilot for your next prompt

> Keep task companion tools available to custom agents that use the task or agent alias

> Custom agents using a tools wildcard '\*' now respect deferredToolLoading opt-in switch

> Run queued ! shell commands locally instead of sending them to the agent

> Allow disabling task and explore built-in subagents

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.64
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-23-clear-queued-tool-images-when-vision-is-disabled|Clear queued tool images when vision is disabled]] · Multimodal Input
- [[Changes/GitHub Copilot CLI/2026-06-23-9-editor-experience-changes-in-v1-0-64|9 Editor Experience changes in v1.0.64]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-23-2-account-and-access-changes-in-v1-0-64|2 Account and Access changes in v1.0.64]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-23-preserve-open-canvas-instances-across-reconnects-and-restarts|Preserve open canvas instances across reconnects and restarts]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-06-23-6-safety-and-privacy-changes-in-v1-0-64|6 Safety and Privacy changes in v1.0.64]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-23-preserve-markdown-blockquotes-in-share-exports|Preserve Markdown blockquotes in /share exports]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-06-23-show-per-model-token-totals-in-usage-and-speed-up-large-history-scans|Show per-model token totals in /usage and speed up large history scans]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-23-add-loop-alias-for-the-every-command|Add /loop alias for the /every command]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-23-add-mcp-registry-installation-for-browsing-and-installing-mcp-servers|Add /mcp registry installation for browsing and installing MCP servers]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-06-23-8-apps-and-integrations-changes-in-v1-0-64|8 Apps and Integrations changes in v1.0.64]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-23-7-model-support-changes-in-v1-0-64|7 Model Support changes in v1.0.64]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-23-11-interface-experience-changes-in-v1-0-64|11 Interface Experience changes in v1.0.64]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-23-15-developer-workflow-changes-in-v1-0-64|15 Developer Workflow changes in v1.0.64]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-23-4-projects-and-workspaces-changes-in-v1-0-64|4 Projects and Workspaces changes in v1.0.64]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-06-23-display-cache-write-pricing-for-models-that-omit-it|Display cache-write pricing for models that omit it]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-06-23-3-context-window-changes-in-v1-0-64|3 Context Window changes in v1.0.64]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-06-23-42-other-changes-in-v1-0-64|42 other changes in v1.0.64]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-06-22 · Kimi Code · [[Changes/Kimi Code/2026-06-22-allow-long-running-foreground-commands-and-subagents-to-be-moved-into-background|Allow long-running foreground commands and subagents to be moved into background…]]
- Later: 2026-06-24 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-24-4-agent-mode-changes-in-v1-0-65|4 Agent Mode changes in v1.0.65]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-23-c97417&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-23-6-agent-mode-changes-in-v1-0-64.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-23-c97417%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.64%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->