---
card_id: claude-code-2026-09-03-c1c224
date: '2026-09-03'
description: 'Claude Code · 2026-09-03 · Other changes: 4 changes in v2.1.260 — Improved
  the Claude apps gateway on Amazon Bedrock: input tokens for an aborted request are…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b40ad28e7734340e8cc22d556d71c127560f0fdecdb908e02944ee8881e122e6
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-03-c1c224
  comparison: ''
  date: '2026-09-03'
  description: 'Claude Code — v2.1.260: 4 other changes'
  evidence:
  - quote: 'Improved the Claude apps gateway on Amazon Bedrock: input tokens for an
      aborted request are now counted with AWS''s free CountTokens API (grant `bedrock:CountTokens`)
      instead of a one-token request'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  - quote: Improved `/ultrareview` and `claude ultrareview` to wait up to 45 minutes
      (previously 30) for long-running cloud reviews
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  - quote: Changed Claude in Chrome to follow your organization's Claude in Chrome
      admin setting; when an admin turns it off, `--chrome`, `/chrome` and the browser
      tools are unavailable
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  - quote: Changed self-hosted runner `--kill-session-after-min` to release a session
      that is only waiting on its user (paused, resumable on the next message) instead
      of killing it and reporting a failure
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-other-changes-in-v2-1-260
  source_release: claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc
  source_type: github_releases
  theme: uncategorized
  title: 4 other changes in v2.1.260
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc|claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc]]'
source_type: github_releases
superseded: true
theme: uncategorized
title: 4 other changes in v2.1.260
type: change
---

<!-- chronolog:begin region="header" -->
# 4 other changes in v2.1.260

**Claude Code** · 2026-09-03 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.260) · from [[Releases/Claude Code/claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc|v2.1.260]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved the Claude apps gateway on Amazon Bedrock: input tokens for an aborted request are now counted with AWS's free CountTokens API (grant `bedrock:CountTokens`) instead of a one-token request

> Improved `/ultrareview` and `claude ultrareview` to wait up to 45 minutes (previously 30) for long-running cloud reviews

> Changed Claude in Chrome to follow your organization's Claude in Chrome admin setting; when an admin turns it off, `--chrome`, `/chrome` and the browser tools are unavailable

> Changed self-hosted runner `--kill-session-after-min` to release a session that is only waiting on its user (paused, resumable on the next message) instead of killing it and reporting a failure

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-03-2-model-support-changes-in-v2-1-260|2 Model Support changes in v2.1.260]] · Model Support
- [[Changes/Claude Code/2026-09-03-2-context-window-changes-in-v2-1-260|2 Context Window changes in v2.1.260]] · Context Window
- [[Changes/Claude Code/2026-09-03-improved-the-settings-error-for-rules-such-as-edit-c-dir-name-where-is-read-as-a|Improved the settings error for rules such as Edit(C:\dir\(name)\), where…]] · Editor Experience
- [[Changes/Claude Code/2026-09-03-improved-deleting-a-background-session-whose-worktree-has-unpushed-commits-the-m|Improved deleting a background session whose worktree has unpushed commits]] · Developer Workflow
- [[Changes/Claude Code/2026-09-03-4-interface-experience-changes-in-v2-1-260|4 Interface Experience changes in v2.1.260]] · Interface Experience
- [[Changes/Claude Code/2026-09-03-3-mobile-and-desktop-changes-in-v2-1-260|3 Mobile and Desktop changes in v2.1.260]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-03-2-agent-mode-changes-in-v2-1-260|2 Agent Mode changes in v2.1.260]] · Agent Mode
- [[Changes/Claude Code/2026-09-03-4-apps-and-integrations-changes-in-v2-1-260|4 Apps and Integrations changes in v2.1.260]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-03-7-safety-and-privacy-changes-in-v2-1-260|7 Safety and Privacy changes in v2.1.260]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-03-added-reload-plugins-to-headless-sessions-so-it-appears-in-the-claude-code-deskt|Added /reload-plugins to headless sessions, so it appears in the Claude Code…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-03-c1c224&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-03-4-other-changes-in-v2-1-260.md%0ACard%20ID%3A%20claude-code-2026-09-03-c1c224%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.260%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->