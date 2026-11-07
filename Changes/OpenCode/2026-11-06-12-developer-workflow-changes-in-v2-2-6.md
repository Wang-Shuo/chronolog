---
card_id: opencode-2026-11-06-48a6e7
date: '2026-11-06'
description: 'OpenCode · 2026-11-06 · Developer Workflow: 12 changes in v2.2.6 — Terminal
  Added Scroll on send in Settings. Choose Keep ( session.submit_scroll: "keep" )
  to…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2978
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3d58ff3a1b81529b8da365399d2ff8fc3717bcebfae8bcad7f64bdcd73788540
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-11-06-48a6e7
  comparison: ''
  date: '2026-11-06'
  description: 'OpenCode — v2.2.6: 12 Developer Workflow changes'
  evidence:
  - quote: 'Terminal Added Scroll on send in Settings. Choose Keep ( session.submit_scroll:
      "keep" ) to retain your reading position after submitting a prompt.'
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: 'Core opencode run now waits for the background shell commands, subagents,
      and image jobs that its prompt started, then lets the model respond to their
      results before it exits. While it waits, it prints waiting for N background
      job(s) (a background_wait event with --format json ). There is no time limit:
      a job that never exits, such as a dev server or file watcher, keeps the run
      open until you press Ctrl+C or send SIGTERM, so set a timeout on CI jobs.'
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Terminal Allow Ctrl+Z to suspend OpenCode while a form or dialog is open.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Terminal Show an error when Ctrl+V cannot read the clipboard. Thanks @jimmyallinai.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Terminal Prevent session titles containing newlines from crashing the TUI.
      Thanks @vishalshekhar.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Terminal Improved message spacing and prevented older history from flashing
      while scrolling.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Terminal Jump to the first or last message with Home, End, and Ctrl+G in
      subagent sessions. Thanks @ricky9408.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Terminal Keypad Home, End, Page Up, and Page Down now navigate the transcript
      like the main keys in terminals that use the kitty keyboard protocol. Thanks
      @argszero.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Terminal opencode mini now uses the agent colors from your config. Thanks
      @ferdinandyb.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Terminal Allow favoriting models with Ctrl+F in /models when they come
      from a provider declared in config or an add-on instead of a saved connection.
      Thanks @Tarquinen.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Desktop Preserve drafts, focus, caret position, queued prompts, and selected
      terminal tabs across failed or concurrent transitions.
    source_release: https://opencode.ai/changelog/v2.2.6
  - quote: Desktop Fixed padding in the WSL distribution picker, the position of worktree
      and branch labels in Home search results, and the selected ring on the Interface
      layout setting. Thanks @inuyume.
    source_release: https://opencode.ai/changelog/v2.2.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: opencode
  product_name: OpenCode
  slug: 12-developer-workflow-changes-in-v2-2-6
  source_release: opencode-2026-11-06-v2-2-6-b1ac172e
  source_type: opencode_changelog
  theme: developer-workflow
  title: 12 Developer Workflow changes in v2.2.6
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-11-06-6-developer-workflow-changes-in-rust-v0-167-0|6
  Developer Workflow changes in rust-v0.167.0]]'
- '[[Changes/GitHub Copilot CLI/2026-11-06-64-developer-workflow-changes-in-v1-0-106|64
  Developer Workflow changes in v1.0.106]]'
- '[[Changes/OpenCode/2026-11-06-scripted-runs-in-worktrees|Scripted Runs in Worktrees]]'
source_release: '[[Releases/OpenCode/opencode-2026-11-06-v2-2-6-b1ac172e|opencode-2026-11-06-v2-2-6-b1ac172e]]'
source_type: opencode_changelog
theme: developer-workflow
title: 12 Developer Workflow changes in v2.2.6
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Developer Workflow changes in v2.2.6

**OpenCode** · 2026-11-06 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://opencode.ai/changelog/v2.2.6) · from [[Releases/OpenCode/opencode-2026-11-06-v2-2-6-b1ac172e|v2.2.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Terminal Added Scroll on send in Settings. Choose Keep ( session.submit_scroll: "keep" ) to retain your reading position after submitting a prompt.

> Core opencode run now waits for the background shell commands, subagents, and image jobs that its prompt started, then lets the model respond to their results before it exits. While it waits, it prints waiting for N background job(s) (a background_wait event with --format json ). There is no time limit: a job that never exits, such as a dev server or file watcher, keeps the run open until you press Ctrl+C or send SIGTERM, so set a timeout on CI jobs.

> Terminal Allow Ctrl+Z to suspend OpenCode while a form or dialog is open.

> Terminal Show an error when Ctrl+V cannot read the clipboard. Thanks @jimmyallinai.

> Terminal Prevent session titles containing newlines from crashing the TUI. Thanks @vishalshekhar.

> Terminal Improved message spacing and prevented older history from flashing while scrolling.

> Terminal Jump to the first or last message with Home, End, and Ctrl+G in subagent sessions. Thanks @ricky9408.

> Terminal Keypad Home, End, Page Up, and Page Down now navigate the transcript like the main keys in terminals that use the kitty keyboard protocol. Thanks @argszero.

> Terminal opencode mini now uses the agent colors from your config. Thanks @ferdinandyb.

> Terminal Allow favoriting models with Ctrl+F in /models when they come from a provider declared in config or an add-on instead of a saved connection. Thanks @Tarquinen.

> Desktop Preserve drafts, focus, caret position, queued prompts, and selected terminal tabs across failed or concurrent transitions.

> Desktop Fixed padding in the WSL distribution picker, the position of worktree and branch labels in Home search results, and the selected ring on the Interface layout setting. Thanks @inuyume.

Source: https://opencode.ai/changelog/v2.2.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-11-06-scripted-runs-in-worktrees|Scripted Runs in Worktrees]] · Developer Workflow
- [[Changes/OpenCode/2026-11-06-shared-mcp-connections|Shared MCP Connections]] · Apps and Integrations
- [[Changes/OpenCode/2026-11-06-mobile-composer-dock|Mobile Composer Dock]] · Mobile and Desktop
- [[Changes/OpenCode/2026-11-06-gui-plugin-themes-and-new-slots|GUI Plugin Themes and New Slots]] · Apps and Integrations
- [[Changes/OpenCode/2026-11-06-desktop-mcp-sign-in-now-accepts-a-pasted-redirect-url-when-automatic-redirection|Desktop MCP sign-in now accepts a pasted redirect URL when automatic redirection…]] · Account and Access
- [[Changes/OpenCode/2026-11-06-3-safety-and-privacy-changes-in-v2-2-6|3 Safety and Privacy changes in v2.2.6]] · Safety and Privacy
- [[Changes/OpenCode/2026-11-06-12-mobile-and-desktop-changes-in-v2-2-6|12 Mobile and Desktop changes in v2.2.6]] · Mobile and Desktop
- [[Changes/OpenCode/2026-11-06-core-added-azure-messages-support-for-foundry-claude-models|Core Added Azure Messages support for Foundry Claude models]] · Model Support
- [[Changes/OpenCode/2026-11-06-7-apps-and-integrations-changes-in-v2-2-6|7 Apps and Integrations changes in v2.2.6]] · Apps and Integrations
- [[Changes/OpenCode/2026-11-06-2-agent-mode-changes-in-v2-2-6|2 Agent Mode changes in v2.2.6]] · Agent Mode
- [[Changes/OpenCode/2026-11-06-core-keep-legacy-custom-providers-whose-models-set-only-part-of-limit-such-as-on|Core Keep legacy custom providers whose models set only part of limit , such as only…]] · Context Window
- [[Changes/OpenCode/2026-11-06-8-other-changes-in-v2-2-6|8 other changes in v2.2.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-11-06 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-11-06-64-developer-workflow-changes-in-v1-0-106|64 Developer Workflow changes in v1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-11-06-48a6e7&body=Card%3A%20Changes%2FOpenCode%2F2026-11-06-12-developer-workflow-changes-in-v2-2-6.md%0ACard%20ID%3A%20opencode-2026-11-06-48a6e7%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv2.2.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->