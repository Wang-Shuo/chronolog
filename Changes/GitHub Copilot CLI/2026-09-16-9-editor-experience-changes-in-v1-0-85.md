---
card_id: github-copilot-cli-2026-09-16-50e2e9
date: '2026-09-16'
description: 'GitHub Copilot CLI · 2026-09-16 · Editor Experience: 9 changes in 1.0.85
  — Add `copilot instruction list` and `copilot lsp list`, replacing `copilot plugins…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1282
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9c6ef381b6617f45115118944f9e210ff9e01e7e29dd7c610afbac68ce3c3671
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-16-50e2e9
  comparison: ''
  date: '2026-09-16'
  description: 'GitHub Copilot CLI — 1.0.85: 9 Editor Experience changes'
  evidence:
  - quote: Add `copilot instruction list` and `copilot lsp list`, replacing `copilot
      plugins list --kind instruction` and `--kind lsp`
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: End and Ctrl+E move the cursor to the true end of a wrapped line, so typing
      or Ctrl+K no longer edits one character early inside a long word or URL. On
      such a line the landing spot is the wrap boundary, so pressing End or Ctrl+E
      again advances to the end of the next visual row
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: '`copilot init` now removes the `.github` directory it created when the
      run exits without writing an instructions file.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: An editor or shell that leaves mouse tracking on no longer leaves your
      terminal reporting clicks, during the session or after the CLI exits
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Pressing Enter in the Sessions tab now foregrounds the highlighted session,
      even when a background refresh rebuilds the list at that moment, instead of
      sometimes opening a different session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: COPILOT_ALLOW_ALL no longer refuses to start the CLI on values such as
      1, 0, yes or an empty string, and falsey values now disable automatic tool approval
      instead of enabling it
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: /copy includes task completion messages when available
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Apply managed Edit and Write rules to recognized native shell redirections
      and supported in-place sed operations
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Shell completions are generated from the same grammar the CLI parses with,
      so `copilot <TAB>` offers root flags alongside subcommands and each subcommand
      offers only its own options
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 9-editor-experience-changes-in-v1-0-85
  source_release: github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9
  source_type: github_releases
  theme: editor-experience
  title: 9 Editor Experience changes in v1.0.85
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-11-5-editor-experience-changes-in-v2026-9-4|5 Editor
  Experience changes in v2026.9.4]]'
- '[[Changes/Claude Code/2026-09-14-3-editor-experience-changes-in-v2-1-271|3 Editor
  Experience changes in v2.1.271]]'
- '[[Changes/Claude Code/2026-09-15-claude-code-on-the-web-added-a-discard-unsaved-changes-confirmation-before-the-n|Claude
  Code on the web Added a "Discard unsaved changes?" confirmation before…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9]]'
source_type: github_releases
theme: editor-experience
title: 9 Editor Experience changes in v1.0.85
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Editor Experience changes in v1.0.85

**GitHub Copilot CLI** · 2026-09-16 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.85) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|1.0.85]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add `copilot instruction list` and `copilot lsp list`, replacing `copilot plugins list --kind instruction` and `--kind lsp`

> End and Ctrl+E move the cursor to the true end of a wrapped line, so typing or Ctrl+K no longer edits one character early inside a long word or URL. On such a line the landing spot is the wrap boundary, so pressing End or Ctrl+E again advances to the end of the next visual row

> `copilot init` now removes the `.github` directory it created when the run exits without writing an instructions file.

> An editor or shell that leaves mouse tracking on no longer leaves your terminal reporting clicks, during the session or after the CLI exits

> Pressing Enter in the Sessions tab now foregrounds the highlighted session, even when a background refresh rebuilds the list at that moment, instead of sometimes opening a different session

> COPILOT_ALLOW_ALL no longer refuses to start the CLI on values such as 1, 0, yes or an empty string, and falsey values now disable automatic tool approval instead of enabling it

> /copy includes task completion messages when available

> Apply managed Edit and Write rules to recognized native shell redirections and supported in-place sed operations

> Shell completions are generated from the same grammar the CLI parses with, so `copilot <TAB>` offers root flags alongside subcommands and each subcommand offers only its own options

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.85
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-09-16-4-account-and-access-changes-in-v1-0-85|4 Account and Access changes in v1.0.85]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-09-16-6-developer-workflow-changes-in-v1-0-85|6 Developer Workflow changes in v1.0.85]] · Developer Workflow
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
## Nearby in Editor Experience

- Earlier: 2026-09-15 · Claude Code · [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-added-a-discard-unsaved-changes-confirmation-before-the-n|Claude Code on the web Added a "Discard unsaved changes?" confirmation before…]]
- Later: 2026-09-16 · Midjourney · [[Changes/Midjourney/2026-09-16-lots-more-changes-on-alpha-midjourney-com-same-goal-as-before-make-the-site-easi|lots more changes on alpha.midjourney.com !]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-16-50e2e9&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-16-9-editor-experience-changes-in-v1-0-85.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-16-50e2e9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.85%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->