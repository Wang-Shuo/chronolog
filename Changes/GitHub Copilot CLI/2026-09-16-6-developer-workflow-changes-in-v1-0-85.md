---
card_id: github-copilot-cli-2026-09-16-2de076
date: '2026-09-16'
description: 'GitHub Copilot CLI · 2026-09-16 · Developer Workflow: 6 changes in 1.0.85
  — Respect terminal color themes even when palettes are incomplete'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2927
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fe182fa6503695460c5ca1a0b70f848667f2424c2046851bc0c1b706cb26ef95
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-16-2de076
  comparison: ''
  date: '2026-09-16'
  description: 'GitHub Copilot CLI — 1.0.85: 6 Developer Workflow changes'
  evidence:
  - quote: Respect terminal color themes even when palettes are incomplete
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Keep terminal theme colors consistent at startup and during live appearance
      changes
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: '`ctrl+h` no longer deletes a whole word in tmux, screen, and remote sessions
      that carry a Windows Terminal `WT_SESSION` from elsewhere. As an accepted tradeoff,
      `ctrl+backspace` now deletes a single character in those sessions — including
      a genuinely local Windows tmux or screen pane — where `ctrl+w` still deletes
      a word'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: When you have more than one GitHub account in your credential store, a
      sandboxed gh command now acts as the account gh is logged in as instead of an
      arbitrary one.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Use /worktree, /move, and --worktree without enabling experimental mode
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Make /collect-debug-logs and --collect-debug-logs available to all users
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 6-developer-workflow-changes-in-v1-0-85
  source_release: github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9
  source_type: github_releases
  theme: developer-workflow
  title: 6 Developer Workflow changes in v1.0.85
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-09-15-the-command-palette-now-opens-over-a-dimmed-backdrop-with-enter-and-exit-animati|The
  command palette now opens over a dimmed backdrop with enter and exit animations…]]'
- '[[Changes/Kimi Code/2026-09-15-add-native-clipboard-support-on-linux-x11-so-copying-from-the-tui-no-longer-depe|Add
  native clipboard support on Linux X11, so copying from the TUI no longer depends…]]'
- '[[Changes/Devin/2026-09-16-blueprint-source-in-the-v3-api|Blueprint Source in the
  v3 API]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9]]'
source_type: github_releases
theme: developer-workflow
title: 6 Developer Workflow changes in v1.0.85
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Developer Workflow changes in v1.0.85

**GitHub Copilot CLI** · 2026-09-16 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.85) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|1.0.85]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Respect terminal color themes even when palettes are incomplete

> Keep terminal theme colors consistent at startup and during live appearance changes

> `ctrl+h` no longer deletes a whole word in tmux, screen, and remote sessions that carry a Windows Terminal `WT_SESSION` from elsewhere. As an accepted tradeoff, `ctrl+backspace` now deletes a single character in those sessions — including a genuinely local Windows tmux or screen pane — where `ctrl+w` still deletes a word

> When you have more than one GitHub account in your credential store, a sandboxed gh command now acts as the account gh is logged in as instead of an arbitrary one.

> Use /worktree, /move, and --worktree without enabling experimental mode

> Make /collect-debug-logs and --collect-debug-logs available to all users

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.85
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-09-16-4-account-and-access-changes-in-v1-0-85|4 Account and Access changes in v1.0.85]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-09-16-9-editor-experience-changes-in-v1-0-85|9 Editor Experience changes in v1.0.85]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-09-16-speed-up-startup-when-resuming-an-existing-local-session-by-its-exact-uuid-with|Speed up startup when resuming an existing local session by its exact UUID with --resume]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-09-16-17-safety-and-privacy-changes-in-v1-0-85|17 Safety and Privacy changes in v1.0.85]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-09-16-13-model-support-changes-in-v1-0-85|13 Model Support changes in v1.0.85]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-09-16-usage-shows-per-model-ai-credit-consumption-in-usage-breakdowns|/usage shows per-model AI Credit consumption in usage breakdowns]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-09-16-3-memory-and-personalization-changes-in-v1-0-85|3 Memory and Personalization changes in v1.0.85]] · Memory and Personalization
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
## Nearby in Developer Workflow

- Earlier: 2026-09-16 · Devin · [[Changes/Devin/2026-09-16-blueprint-source-in-the-v3-api|Blueprint Source in the v3 API]]
- Later: 2026-09-16 · OpenHands · [[Changes/OpenHands/2026-09-16-5-developer-workflow-changes-in-v1-19-0|5 Developer Workflow changes in v1.19.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-16-2de076&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-16-6-developer-workflow-changes-in-v1-0-85.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-16-2de076%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.85%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->