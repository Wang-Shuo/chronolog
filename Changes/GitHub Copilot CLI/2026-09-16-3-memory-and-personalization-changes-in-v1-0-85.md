---
card_id: github-copilot-cli-2026-09-16-84ff08
date: '2026-09-16'
description: 'GitHub Copilot CLI · 2026-09-16 · Memory and Personalization: 3 changes
  in 1.0.85 — Add session and memory import commands for the semantic JSONL interchange…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1154
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f930c212de08247835dcc18c072e584e9c1d3bea67969f2880aff6d3d0b65707
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-16-84ff08
  comparison: ''
  date: '2026-09-16'
  description: 'GitHub Copilot CLI — 1.0.85: 3 Memory and Personalization changes'
  evidence:
  - quote: Add session and memory import commands for the semantic JSONL interchange
      format
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Report in-memory MCP servers as memory instead of local in copilot mcp
      list
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Reduce metadata scanning time for large local session histories, with increased
      thread and memory use
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 3-memory-and-personalization-changes-in-v1-0-85
  source_release: github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9
  source_type: github_releases
  theme: memory
  title: 3 Memory and Personalization changes in v1.0.85
  type: change
related_changes:
- '[[Changes/Raycast/2026-09-11-projects|Projects]]'
- '[[Changes/Raycast/2026-09-11-projects-6239fd|Projects]]'
- '[[Changes/Google Antigravity/2026-09-15-conversations-with-very-long-histories-now-load-faster-and-use-less-memory|Conversations
  with very long histories now load faster and use less memory]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9]]'
source_type: github_releases
theme: memory
title: 3 Memory and Personalization changes in v1.0.85
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Memory and Personalization changes in v1.0.85

**GitHub Copilot CLI** · 2026-09-16 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.85) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|1.0.85]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add session and memory import commands for the semantic JSONL interchange format

> Report in-memory MCP servers as memory instead of local in copilot mcp list

> Reduce metadata scanning time for large local session histories, with increased thread and memory use

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
- [[Changes/GitHub Copilot CLI/2026-09-16-4-mobile-and-desktop-changes-in-v1-0-85|4 Mobile and Desktop changes in v1.0.85]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-09-16-add-json-to-copilot-plugin-list-copilot-plugin-marketplace-list-and-copilot-plug|Add --json to copilot plugin list, copilot plugin marketplace list…]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-09-16-3-context-window-changes-in-v1-0-85|3 Context Window changes in v1.0.85]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-09-16-2-agent-mode-changes-in-v1-0-85|2 Agent Mode changes in v1.0.85]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-09-16-20-apps-and-integrations-changes-in-v1-0-85|20 Apps and Integrations changes in v1.0.85]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-09-16-share-notes-md-now-writes-the-exported-session-to-your-home-directory-instead-of|--share=~/notes.md now writes the exported session to your home directory instead…]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-09-16-when-session-history-is-truncated-or-compacted-just-as-a-turn-finishes-the-worki|When session history is truncated or compacted just as a turn finishes…]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-09-16-3-interface-experience-changes-in-v1-0-85|3 Interface Experience changes in v1.0.85]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-09-16-19-other-changes-in-v1-0-85|19 other changes in v1.0.85]] · Other changes
- [[Changes/GitHub Copilot CLI/2026-09-16-vim-mode-is-now-available-to-everyone-turn-it-on-with-vim-or-by-setting-editormo|Vim mode is now available to everyone]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-09-15 · Google Antigravity · [[Changes/Google Antigravity/2026-09-15-conversations-with-very-long-histories-now-load-faster-and-use-less-memory|Conversations with very long histories now load faster and use less memory]]
- Later: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-vscode-added-viewing-editing-and-deleting-a-saved-memory-inside-the-memory-dialo|VSCode Added viewing, editing and deleting a saved memory inside the Memory dialog]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-16-84ff08&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-16-3-memory-and-personalization-changes-in-v1-0-85.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-16-84ff08%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.85%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->