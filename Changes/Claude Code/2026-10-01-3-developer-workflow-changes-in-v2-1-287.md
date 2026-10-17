---
card_id: claude-code-2026-10-01-517ac2
date: '2026-10-01'
description: 'Claude Code · 2026-10-01 · Developer Workflow: 3 changes in v2.1.287
  — Windows: Added a startup warning when denying the Bash tool also turns off the…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1293
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c7ae5889349d6de8de3c097e04f1c374d77b47f831d03e72fbc921b9aeaf88f1
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-01-517ac2
  comparison: ''
  date: '2026-10-01'
  description: 'Claude Code — v2.1.287: 3 Developer Workflow changes'
  evidence:
  - quote: 'Windows: Added a startup warning when denying the Bash tool also turns
      off the PowerShell tool, so Claude has no shell tool'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: Changed a shell write through a repo-committed symlink onto a sensitive
      file or out of the working tree to name where it lands and wait for a person,
      on lines with a `~` target too
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: '[Code Review] Improved the failed-review card on a pull request whose
      conversation is locked: it now says the lock blocked the review and that nothing
      was posted or charged'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-developer-workflow-changes-in-v2-1-287
  source_release: claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87
  source_type: github_releases
  theme: developer-workflow
  title: 3 Developer Workflow changes in v2.1.287
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-25-3-developer-workflow-changes-in-v2-1-283|3 Developer
  Workflow changes in v2.1.283]]'
- '[[Changes/Claude Code/2026-09-29-3-developer-workflow-changes-in-v2-1-285|3 Developer
  Workflow changes in v2.1.285]]'
- '[[Changes/Claude Code/2026-09-30-3-developer-workflow-changes-in-v2-1-286|3 Developer
  Workflow changes in v2.1.286]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87|claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87]]'
source_type: github_releases
theme: developer-workflow
title: 3 Developer Workflow changes in v2.1.287
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Developer Workflow changes in v2.1.287

**Claude Code** · 2026-10-01 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.287) · from [[Releases/Claude Code/claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87|v2.1.287]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Windows: Added a startup warning when denying the Bash tool also turns off the PowerShell tool, so Claude has no shell tool

> Changed a shell write through a repo-committed symlink onto a sensitive file or out of the working tree to name where it lands and wait for a person, on lines with a `~` target too

> [Code Review] Improved the failed-review card on a pull request whose conversation is locked: it now says the lock blocked the review and that nothing was posted or charged

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-01-4-model-support-changes-in-v2-1-287|4 Model Support changes in v2.1.287]] · Model Support
- [[Changes/Claude Code/2026-10-01-changed-opus-4-7-and-fable-to-use-a-1m-context-window-by-default-on-bedrock-vert|Changed Opus 4.7+ and Fable to use a 1M context window by default on Bedrock…]] · Context Window
- [[Changes/Claude Code/2026-10-01-2-mobile-and-desktop-changes-in-v2-1-287|2 Mobile and Desktop changes in v2.1.287]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-01-vscode-changed-the-claude-in-chrome-enabled-by-default-switch-to-also-connect-th|VSCode Changed the Claude in Chrome "Enabled by default" switch to also connect…]] · Editor Experience
- [[Changes/Claude Code/2026-10-01-6-safety-and-privacy-changes-in-v2-1-287|6 Safety and Privacy changes in v2.1.287]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-01-11-apps-and-integrations-changes-in-v2-1-287|11 Apps and Integrations changes in v2.1.287]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-01-2-reliability-and-performance-changes-in-v2-1-287|2 Reliability and Performance changes in v2.1.287]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-01-changed-screen-reader-mode-to-write-new-or-changed-lines-without-first-pausing-w|Changed screen reader mode to write new or changed lines without first pausing…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-01-4-agent-mode-changes-in-v2-1-287|4 Agent Mode changes in v2.1.287]] · Agent Mode
- [[Changes/Claude Code/2026-10-01-added-url-prompts-from-mcp-servers-on-the-2025-11-25-protocol-for-example-to-sig|Added URL prompts from MCP servers on the 2025-11-25 protocol, for example to sign in]] · Account and Access
- [[Changes/Claude Code/2026-10-01-improved-sdk-sessions-so-a-message-sent-with-priority-now-no-longer-cancels-a-ru|Improved SDK sessions so a message sent with priority "now" no longer cancels…]] · Search and Browsing
- [[Changes/Claude Code/2026-10-01-2-memory-and-personalization-changes-in-v2-1-287|2 Memory and Personalization changes in v2.1.287]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-01-4-other-changes-in-v2-1-287|4 other changes in v2.1.287]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-30 · Claude Code · [[Changes/Claude Code/2026-09-30-3-developer-workflow-changes-in-v2-1-286|3 Developer Workflow changes in v2.1.286]]
- Later: 2026-10-02 · Claude Code · [[Changes/Claude Code/2026-10-02-3-developer-workflow-changes-in-v2-1-288|3 Developer Workflow changes in v2.1.288]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-01-517ac2&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-01-3-developer-workflow-changes-in-v2-1-287.md%0ACard%20ID%3A%20claude-code-2026-10-01-517ac2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.287%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->