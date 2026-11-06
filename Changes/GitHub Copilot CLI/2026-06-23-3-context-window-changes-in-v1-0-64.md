---
card_id: github-copilot-cli-2026-06-23-f189b2
date: '2026-06-23'
description: 'GitHub Copilot CLI · 2026-06-23 · Context Window: 3 changes in 1.0.64
  — Resumed sessions reproduce the original attached-file references even if those
  files…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1146
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7265f103c7aeae2d8db7e78cbfb490e69e86c6fd4d01459f4d86f8093b6b6b9a
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-23-f189b2
  comparison: ''
  date: '2026-06-23'
  description: 'GitHub Copilot CLI — 1.0.64: 3 Context Window changes'
  evidence:
  - quote: Resumed sessions reproduce the original attached-file references even if
      those files later change on disk, avoiding prompt-cache resets
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: 'OpenTelemetry: chat spans after a successful compaction carry gen_ai.conversation.compacted=true,
      and the summary is emitted as a CompactionPart in gen_ai.input.messages'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: OpenTelemetry GenAI spans now emit `gen_ai.usage.cache_read.input_tokens`,
      `gen_ai.usage.cache_creation.input_tokens`, and `gen_ai.usage.reasoning.output_tokens`
      per the GenAI semantic conventions spec (previously used incorrect underscore-separated
      names)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 3-context-window-changes-in-v1-0-64
  source_release: github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd
  source_type: github_releases
  theme: context-window
  title: 3 Context Window changes in v1.0.64
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-06-22-starting-today-for-chatgpt-free-and-go-users-long-pastes-are-handled-differently|Large
  pastes are now handled as attachments for more plans]]'
- '[[Changes/Claude Code/2026-06-22-bash-commands-now-trigger-claude-to-respond-to-the-output-automatically-set-resp|!
  bash commands now trigger Claude to respond to the output automatically]]'
- '[[Changes/Codex CLI/2026-06-22-10-context-window-changes-in-rust-v0-142-0|10 Context
  Window changes in rust-v0.142.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd|github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd]]'
source_type: github_releases
theme: context-window
title: 3 Context Window changes in v1.0.64
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Context Window changes in v1.0.64

**GitHub Copilot CLI** · 2026-06-23 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.64) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd|1.0.64]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Resumed sessions reproduce the original attached-file references even if those files later change on disk, avoiding prompt-cache resets

> OpenTelemetry: chat spans after a successful compaction carry gen_ai.conversation.compacted=true, and the summary is emitted as a CompactionPart in gen_ai.input.messages

> OpenTelemetry GenAI spans now emit `gen_ai.usage.cache_read.input_tokens`, `gen_ai.usage.cache_creation.input_tokens`, and `gen_ai.usage.reasoning.output_tokens` per the GenAI semantic conventions spec (previously used incorrect underscore-separated names)

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
- [[Changes/GitHub Copilot CLI/2026-06-23-6-agent-mode-changes-in-v1-0-64|6 Agent Mode changes in v1.0.64]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-23-11-interface-experience-changes-in-v1-0-64|11 Interface Experience changes in v1.0.64]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-23-15-developer-workflow-changes-in-v1-0-64|15 Developer Workflow changes in v1.0.64]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-23-4-projects-and-workspaces-changes-in-v1-0-64|4 Projects and Workspaces changes in v1.0.64]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-06-23-display-cache-write-pricing-for-models-that-omit-it|Display cache-write pricing for models that omit it]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-06-23-42-other-changes-in-v1-0-64|42 other changes in v1.0.64]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-06-22 · Codex CLI · [[Changes/Codex CLI/2026-06-22-10-context-window-changes-in-rust-v0-142-0|10 Context Window changes in rust-v0.142.0]]
- Later: 2026-06-25 · Codex CLI · [[Changes/Codex CLI/2026-06-25-2-context-window-changes-in-rust-v0-142-2|2 Context Window changes in rust-v0.142.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-23-f189b2&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-23-3-context-window-changes-in-v1-0-64.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-23-f189b2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.64%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->