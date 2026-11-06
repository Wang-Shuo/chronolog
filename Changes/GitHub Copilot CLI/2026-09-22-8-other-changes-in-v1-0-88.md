---
card_id: github-copilot-cli-2026-09-22-f00b06
date: '2026-09-22'
description: 'GitHub Copilot CLI · 2026-09-22 · Other changes: 8 changes in 1.0.88
  — Preserve /allow-all during managed-settings refresh failures, and remember exact
  session…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e55f48a195d106b17ab7a664c8cf17132987c160777c4ef51e5317798dcb3140
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-22-f00b06
  comparison: ''
  date: '2026-09-22'
  description: 'GitHub Copilot CLI — 1.0.88: 8 other changes'
  evidence:
  - quote: Preserve /allow-all during managed-settings refresh failures, and remember
      exact session approvals for missing paths without granting their parent directory;
      exact grants are visible in /list-dirs and cleared by /reset-allowed-tools
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.88
  - quote: Sandboxed network denials from proxy tunnel failures now show bypass guidance
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.88
  - quote: Pressing Enter in freeform ask_user prompts adds a new line; submit with
      Ctrl+Enter or Ctrl+S as a fallback
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.88
  - quote: Prompt mode now warns when it stops waiting for background tasks and explains
      how to change the timeout limit.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.88
  - quote: Hook commands without an explicit `cwd` again run in the project root instead
      of the session's current directory, so repo-relative hook scripts still resolve
      from a subdirectory.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.88
  - quote: Support namespaced custom skills and ignored skill directories during skill
      discovery
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.88
  - quote: Indexed search supports glob filtering and --files listings with accurate
      ripgrep fallback behavior.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.88
  - quote: Run /fork during active turns to branch work without waiting.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.88
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 8-other-changes-in-v1-0-88
  source_release: github-copilot-cli-2026-09-22-v1-0-88-github-394076851-2894d283
  source_type: github_releases
  theme: uncategorized
  title: 8 other changes in v1.0.88
  type: change
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-22-v1-0-88-github-394076851-2894d283|github-copilot-cli-2026-09-22-v1-0-88-github-394076851-2894d283]]'
source_type: github_releases
theme: uncategorized
title: 8 other changes in v1.0.88
type: change
---

<!-- chronolog:begin region="header" -->
# 8 other changes in v1.0.88

**GitHub Copilot CLI** · 2026-09-22 · Other changes · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.88) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-22-v1-0-88-github-394076851-2894d283|1.0.88]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Preserve /allow-all during managed-settings refresh failures, and remember exact session approvals for missing paths without granting their parent directory; exact grants are visible in /list-dirs and cleared by /reset-allowed-tools

> Sandboxed network denials from proxy tunnel failures now show bypass guidance

> Pressing Enter in freeform ask_user prompts adds a new line; submit with Ctrl+Enter or Ctrl+S as a fallback

> Prompt mode now warns when it stops waiting for background tasks and explains how to change the timeout limit.

> Hook commands without an explicit `cwd` again run in the project root instead of the session's current directory, so repo-relative hook scripts still resolve from a subdirectory.

> Support namespaced custom skills and ignored skill directories during skill discovery

> Indexed search supports glob filtering and --files listings with accurate ripgrep fallback behavior.

> Run /fork during active turns to branch work without waiting.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.88
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-09-22-in-the-sessions-tab-rows-you-can-dismiss-now-take-x-then-x-again-to-confirm-a-lo|In the Sessions tab, rows you can dismiss now take x then x again to confirm]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-09-22-2-agent-mode-changes-in-v1-0-88|2 Agent Mode changes in v1.0.88]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-09-22-add-optional-osc-777-terminal-notifications-for-direct-ghostty-and-wezterm-sessi|Add optional OSC 777 terminal notifications for direct Ghostty and WezTerm sessions]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-09-22-resuming-large-local-sessions-keeps-transcript-memory-bounded-for-smoother-cli-p|Resuming large local sessions keeps transcript memory bounded for smoother CLI performance]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-09-22-3-account-and-access-changes-in-v1-0-88|3 Account and Access changes in v1.0.88]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-09-22-session-resume-preserves-pending-conversation-events-when-saving-fails-and-expla|Session resume preserves pending conversation events when saving fails and explains…]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-09-22-2-safety-and-privacy-changes-in-v1-0-88|2 Safety and Privacy changes in v1.0.88]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-09-22-6-apps-and-integrations-changes-in-v1-0-88|6 Apps and Integrations changes in v1.0.88]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-22-f00b06&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-22-8-other-changes-in-v1-0-88.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-22-f00b06%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.88%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->