---
card_id: cursor-2025-09-12-8c0b1d
date: '2025-09-12'
description: 'Cursor · 2025-09-12 · Developer Workflow: When Agent decides to create
  a terminal to run shell commands, we''ve dramatically improved the stability and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 909
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: change
machine_hash: 453406a4f72f495a7a8cab0a93b01f3968d7d3c2e5e9c22961cf6bb4342ff634
product: cursor
product_name: Cursor
record:
  ai_generated: true
  card_id: cursor-2025-09-12-8c0b1d
  comparison: ''
  confidence: low
  date: '2025-09-12'
  description: 'Cursor — Slash commands, summarization, and improved Agent terminal:
    When Agent decides to create a terminal to run shell commands, we''ve dramatically
    improved the stability and reliability of the environment.'
  evidence:
  - quote: When Agent decides to create a terminal to run shell commands, we've dramatically
      improved the stability and reliability of the environment.
    source_release: https://cursor.com/changelog/1-6
  - quote: This solves known issues around terminal commands hanging and not properly
      exiting when completing tasks, as well as improving the SSH experience.
    source_release: https://cursor.com/changelog/1-6
  - quote: We've also polished the terminal UI, made it faster to run, and added OS
      notifications when shell commands require user approval.
    source_release: https://cursor.com/changelog/1-6
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: change
  product: cursor
  product_name: Cursor
  slug: improved-terminal-for-agent
  source_release: cursor-2025-09-12-1-6-https-cursor-com-changelog-1-6-f33fb3ea
  source_type: cursor_changelog
  theme: developer-workflow
  theme_matches:
  - matched_terms:
    - agent
    score: 50
    theme: agent-mode
  - matched_terms:
    - terminal
    score: 50
    theme: developer-workflow
  - matched_terms:
    - stability
    score: 50
    theme: reliability-performance
  theme_resolution: manual-semantic-rule-v1
  title: Improved terminal for Agent
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-09-08-2-developer-workflow-changes-in-rust-v0-31-0|2 Developer
  Workflow changes in rust-v0.31.0]]'
- '[[Changes/Gemini CLI/2025-09-09-3-developer-workflow-changes-in-v0-4-0|3 Developer
  Workflow changes in v0.4.0]]'
- '[[Changes/Codex CLI/2025-09-10-2-developer-workflow-changes-in-rust-v0-32-0|2 Developer
  Workflow changes in rust-v0.32.0]]'
source_release: '[[Releases/Cursor/cursor-2025-09-12-1-6-https-cursor-com-changelog-1-6-f33fb3ea|cursor-2025-09-12-1-6-https-cursor-com-changelog-1-6-f33fb3ea]]'
source_type: cursor_changelog
theme: developer-workflow
title: Improved terminal for Agent
type: change
---

<!-- chronolog:begin region="header" -->
# Improved terminal for Agent

**Cursor** · 2025-09-12 · [[Themes/developer-workflow|Developer Workflow]] · [Official source](https://cursor.com/changelog/1-6) · from [[Releases/Cursor/cursor-2025-09-12-1-6-https-cursor-com-changelog-1-6-f33fb3ea|Slash commands, summarization, and improved Agent terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> When Agent decides to create a terminal to run shell commands, we've dramatically improved the stability and reliability of the environment.
>
> This solves known issues around terminal commands hanging and not properly exiting when completing tasks, as well as improving the SSH experience.
>
> We've also polished the terminal UI, made it faster to run, and added OS notifications when shell commands require user approval.
>
> Source: https://cursor.com/changelog/1-6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cursor/2025-09-12-1-6-7-enhanced-git-diff-parsing|1.6.7: Enhanced git diff parsing]] · Editor Experience
- [[Changes/Cursor/2025-09-12-3-agent-mode-changes-in-1-6|3 Agent Mode changes in 1.6]] · Agent Mode
- [[Changes/Cursor/2025-09-12-cursor-automatically-summarizes-long-conversation-for-you-when-reaching-the-cont|Summarization triggers]] · Context Window
- [[Changes/Cursor/2025-09-12-5-developer-workflow-changes-in-1-6|5 Developer Workflow changes in 1.6]] · Developer Workflow
- [[Changes/Cursor/2025-09-12-1-6-27-native-menu-notification-badge|1.6.27: Native menu notification badge]] · Interface Experience
- [[Changes/Cursor/2025-09-12-2-apps-and-integrations-changes-in-1-6|2 Apps and Integrations changes in 1.6]] · Apps and Integrations
- [[Changes/Cursor/2025-09-12-custom-slash-commands-b79c4b|Custom slash commands]] · Developer Workflow
- [[Changes/Cursor/2025-09-12-5-reliability-and-performance-changes-in-1-6|5 Reliability and Performance changes in 1.6]] · Reliability and Performance
- [[Changes/Cursor/2025-09-12-mcp-resources-support|MCP Resources support]] · Apps and Integrations
- [[Changes/Cursor/2025-09-12-1-6-26-summarization-and-extension-improvements|1.6.26: Summarization and extension improvements]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2025-09-10 · Codex CLI · [[Changes/Codex CLI/2025-09-10-2-developer-workflow-changes-in-rust-v0-32-0|2 Developer Workflow changes in rust-v0.32.0]]
- Later: 2025-09-13 · Cline · [[Changes/Cline/2025-09-13-feature-to-generate-commit-message-for-staged-changes-with-unstaged-as-fallback|Feature to generate commit message for staged changes, with unstaged as fallback]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cursor-2025-09-12-8c0b1d&body=Card%3A%20Changes%2FCursor%2F2025-09-12-improved-terminal-for-agent.md%0ACard%20ID%3A%20cursor-2025-09-12-8c0b1d%0ASource%3A%20https%3A%2F%2Fcursor.com%2Fchangelog%2F1-6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->