---
card_id: github-copilot-cli-2026-06-01-f944d8
date: '2026-06-01'
description: 'GitHub Copilot CLI · 2026-06-01 · Editor Experience: 9 changes in 1.0.57
  — Actionable error message shown when GitHub API rate limit is hit during `copilot…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2759
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c1e4e83987b46e5099bd61f633649c653465357585e5faf212a05ab7b8d9cfc7
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-01-f944d8
  comparison: ''
  date: '2026-06-01'
  description: 'GitHub Copilot CLI — 1.0.57: 9 Editor Experience changes'
  evidence:
  - quote: Actionable error message shown when GitHub API rate limit is hit during
      `copilot update`
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.57
  - quote: Symlinked directories appear in /cwd completion suggestions
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.57
  - quote: Running `copilot` with an unquoted multi-word prompt now shows a helpful
      "quote your prompt" hint instead of a raw commander error
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.57
  - quote: Default networking transport is now HTTP/1.1, improving reliability on
      some network paths. Opt into HTTP/2 with COPILOT_ENABLE_HTTP2=1.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.57
  - quote: COPILOT_HOME is honored for the server discovery registry directory
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.57
  - quote: Click a diff line with the mouse to select it in diff mode
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.57
  - quote: Pasting text copied from a browser, editor, or terminal no longer leaves
      a stray empty line, broken box-drawing lines, or a misplaced cursor in the prompt
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.57
  - quote: High-contrast diff backgrounds use darker colors to improve text readability
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.57
  - quote: /diff defaults to branch diff when there are no unstaged changes
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.57
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 9-editor-experience-changes-in-v1-0-57
  source_release: github-copilot-cli-2026-06-01-v1-0-57-github-332702409-1dd8346d
  source_type: github_releases
  theme: editor-experience
  title: 9 Editor Experience changes in v1.0.57
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-29-removed-the-ide-for-startup-hint-toast|Removed
  the "/ide for …" startup hint toast]]'
- '[[Changes/GitHub Copilot CLI/2026-05-29-2-editor-experience-changes-in-v1-0-56|2
  Editor Experience changes in v1.0.56]]'
- '[[Changes/Codex CLI/2026-06-01-2-editor-experience-changes-in-rust-v0-136-0|2 Editor
  Experience changes in rust-v0.136.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-01-v1-0-57-github-332702409-1dd8346d|github-copilot-cli-2026-06-01-v1-0-57-github-332702409-1dd8346d]]'
source_type: github_releases
theme: editor-experience
title: 9 Editor Experience changes in v1.0.57
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Editor Experience changes in v1.0.57

**GitHub Copilot CLI** · 2026-06-01 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.57) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-01-v1-0-57-github-332702409-1dd8346d|1.0.57]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Actionable error message shown when GitHub API rate limit is hit during `copilot update`

> Symlinked directories appear in /cwd completion suggestions

> Running `copilot` with an unquoted multi-word prompt now shows a helpful "quote your prompt" hint instead of a raw commander error

> Default networking transport is now HTTP/1.1, improving reliability on some network paths. Opt into HTTP/2 with COPILOT_ENABLE_HTTP2=1.

> COPILOT_HOME is honored for the server discovery registry directory

> Click a diff line with the mouse to select it in diff mode

> Pasting text copied from a browser, editor, or terminal no longer leaves a stray empty line, broken box-drawing lines, or a misplaced cursor in the prompt

> High-contrast diff backgrounds use darker colors to improve text readability

> /diff defaults to branch diff when there are no unstaged changes

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.57
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-01-new-reasoning-after-tool-calls-appears-at-the-bottom-of-the-timeline-instead-of|New reasoning after tool calls appears at the bottom of the timeline instead…]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-01-surface-the-underlying-reason-e-g-github-api-rate-limit-when-sdk-auth-token-vali|Surface the underlying reason (e.g. GitHub API rate limit) when SDK auth-token…]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-01-canvas-providers-can-return-file-urls-in-open-results-for-local-file-previews|Canvas providers can return file:// URLs in open results for local file previews]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-06-01-2-search-and-browsing-changes-in-v1-0-57|2 Search and Browsing changes in v1.0.57]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-06-01-session-resume-works-correctly-after-a-crash-that-left-partial-data-in-the-sessi|Session resume works correctly after a crash that left partial data in the session log]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-06-01-5-apps-and-integrations-changes-in-v1-0-57|5 Apps and Integrations changes in v1.0.57]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-01-canceling-a-running-shell-command-ctrl-c-on-a-command-or-aborting-an-agent-comma|Canceling a running shell command (Ctrl+C on a !command, or aborting an agent command]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-01-lsp-show-lsp-test-and-lsp-reload-correctly-discover-project-lsp-config-when-the|/lsp show, /lsp test, and /lsp reload correctly discover project LSP config…]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-01-9-other-changes-in-v1-0-57|9 other changes in v1.0.57]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-06-01 · Codex CLI · [[Changes/Codex CLI/2026-06-01-2-editor-experience-changes-in-rust-v0-136-0|2 Editor Experience changes in rust-v0.136.0]]
- Later: 2026-06-01 · Open WebUI · [[Changes/Open WebUI/2026-06-01-4-editor-experience-changes-in-v0-9-6|4 Editor Experience changes in v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-01-f944d8&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-01-9-editor-experience-changes-in-v1-0-57.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-01-f944d8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.57%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->