---
card_id: github-copilot-cli-2026-06-09-9dbdad
date: '2026-06-09'
description: 'GitHub Copilot CLI · 2026-06-09 · Editor Experience: 4 changes in 1.0.61
  — Configure home tab bar visibility, order, and hidden tabs via the `tabs` setting
  in…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1183
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: db2aedd6f3f768bedf3a1f3eabd42af1219d55434be4519bb1f7264dc5c6ac30
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-09-9dbdad
  comparison: ''
  date: '2026-06-09'
  description: 'GitHub Copilot CLI — 1.0.61: 4 Editor Experience changes'
  evidence:
  - quote: Configure home tab bar visibility, order, and hidden tabs via the `tabs`
      setting in settings.json
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.61
  - quote: '`/sessions` now navigates to the Sessions tab instead of opening an overlay'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.61
  - quote: '`/help` now lists `$HOME/.copilot/instructions/**/*.instructions.md` alongside
      the other user-level instruction locations'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.61
  - quote: Add `beepOnSchedule` setting to disable completion beeps for scheduled
      `/every` and `/after` runs
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.61
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 4-editor-experience-changes-in-v1-0-61
  source_release: github-copilot-cli-2026-06-09-v1-0-61-github-336905979-4d0a69f2
  source_type: github_releases
  theme: editor-experience
  title: 4 Editor Experience changes in v1.0.61
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-08-background-sessions-now-preserve-ide-chrome-bare-remote-control-and-other-flags|Background
  sessions now preserve --ide, --chrome, --bare, --remote-control…]]'
- '[[Changes/Codex CLI/2026-06-08-3-editor-experience-changes-in-rust-v0-138-0|3 Editor
  Experience changes in rust-v0.138.0]]'
- '[[Changes/Codex CLI/2026-06-09-4-editor-experience-changes-in-rust-v0-139-0|4 Editor
  Experience changes in rust-v0.139.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-09-v1-0-61-github-336905979-4d0a69f2|github-copilot-cli-2026-06-09-v1-0-61-github-336905979-4d0a69f2]]'
source_type: github_releases
theme: editor-experience
title: 4 Editor Experience changes in v1.0.61
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Editor Experience changes in v1.0.61

**GitHub Copilot CLI** · 2026-06-09 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.61) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-09-v1-0-61-github-336905979-4d0a69f2|1.0.61]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Configure home tab bar visibility, order, and hidden tabs via the `tabs` setting in settings.json

> `/sessions` now navigates to the Sessions tab instead of opening an overlay

> `/help` now lists `$HOME/.copilot/instructions/**/*.instructions.md` alongside the other user-level instruction locations

> Add `beepOnSchedule` setting to disable completion beeps for scheduled `/every` and `/after` runs

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.61
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-09-2-interface-experience-changes-in-v1-0-61|2 Interface Experience changes in v1.0.61]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-09-grep-searches-in-large-monorepos-use-an-indexed-search-engine-for-significantly|Grep searches in large monorepos use an indexed search engine for significantly…]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-09-6-developer-workflow-changes-in-v1-0-61|6 Developer Workflow changes in v1.0.61]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-09-3-model-support-changes-in-v1-0-61|3 Model Support changes in v1.0.61]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-09-mcp-oauth-re-authentication-correctly-uses-the-saved-oauth-client-id-for-remote|MCP OAuth re-authentication correctly uses the saved OAuth client ID for remote servers]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-09-3-agent-mode-changes-in-v1-0-61|3 Agent Mode changes in v1.0.61]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-09-2-search-and-browsing-changes-in-v1-0-61|2 Search and Browsing changes in v1.0.61]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-06-09-use-natural-language-with-every-and-after-to-schedule-tasks-using-cron-expressio|Use natural language with /every and /after to schedule tasks using cron…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-09-resuming-a-local-session-with-memory-disabled-no-longer-crashes-the-ui-to-a-blan|Resuming a local session with memory disabled no longer crashes the UI to a blank screen]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-06-09-pasted-images-no-longer-leak-into-the-main-prompt-after-a-permission-dialog-clos|Pasted images no longer leak into the main prompt after a permission dialog closes]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-09-4-apps-and-integrations-changes-in-v1-0-61|4 Apps and Integrations changes in v1.0.61]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-09-8-other-changes-in-v1-0-61|8 other changes in v1.0.61]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-06-09 · Codex CLI · [[Changes/Codex CLI/2026-06-09-4-editor-experience-changes-in-rust-v0-139-0|4 Editor Experience changes in rust-v0.139.0]]
- Later: 2026-06-10 · OpenHands · [[Changes/OpenHands/2026-06-10-removed-app-tab-from-conversation-by-neubig-in-https-github-com-openhands-openha|Removed App tab from conversation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-09-9dbdad&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-09-4-editor-experience-changes-in-v1-0-61.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-09-9dbdad%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.61%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->