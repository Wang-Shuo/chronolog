---
card_id: claude-code-2026-09-10-1bffc8
date: '2026-09-10'
description: 'Claude Code · 2026-09-10 · Other changes: 9 changes in v2.1.268 — Added
  a startup warning for gateways when `access_control.allow_cidrs` is empty, and a…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: eff5ff735b237279a9b6c2e23e25eb3c3c4f9551dab6a4d4732a7dc44221880f
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-10-1bffc8
  comparison: ''
  date: '2026-09-10'
  description: 'Claude Code — v2.1.268: 9 other changes'
  evidence:
  - quote: Added a startup warning for gateways when `access_control.allow_cidrs`
      is empty, and a one-time warning the first time a request arrives from a public
      address
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: 'Added `claude self-hosted-runner --remove-session-state` (default off):
      delete each session''s per-session directories under `<base-dir>/_sessions/`
      when the session ends'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: Added `configDirectory` to the output of `claude auth status --json`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: 'Improved startup time in projects with `.claude/workflows/` scripts: listing
      them no longer parses each script'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: 'Improved Claude in Chrome: long page reads now stay inline instead of
      being saved to a file and read back'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: Changed Bedrock, Vertex and Foundry sessions to keep the tool list byte-stable
      across a conversation (late-connecting tools load deferred instead of rewriting
      it), matching first-party sessions
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: 'Changed local Cowork sessions set to skip all approvals: the Artifact
      tool now refuses a local file outside the session''s folders, or behind a symlink,
      instead of reading it without asking'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: Changed plain `WebFetch` deny and ask rules to no longer apply to Artifact
      tool reads and updates; use an `Artifact` rule (or `WebFetch(domain:claude.ai)`)
      to block or gate them
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: '[Claude Tag] Improved formatting of comparisons: sentence-length comparisons
      now come as lists instead of wide tables that scroll sideways, and long table
      cells wrap'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 9-other-changes-in-v2-1-268
  source_release: claude-code-2026-09-10-v2-1-268-github-386532237-baa1a848
  source_type: github_releases
  theme: uncategorized
  title: 9 other changes in v2.1.268
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-09-10-v2-1-268-github-386532237-baa1a848|claude-code-2026-09-10-v2-1-268-github-386532237-baa1a848]]'
source_type: github_releases
theme: uncategorized
title: 9 other changes in v2.1.268
type: change
---

<!-- chronolog:begin region="header" -->
# 9 other changes in v2.1.268

**Claude Code** · 2026-09-10 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.268) · from [[Releases/Claude Code/claude-code-2026-09-10-v2-1-268-github-386532237-baa1a848|v2.1.268]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a startup warning for gateways when `access_control.allow_cidrs` is empty, and a one-time warning the first time a request arrives from a public address

> Added `claude self-hosted-runner --remove-session-state` (default off): delete each session's per-session directories under `<base-dir>/_sessions/` when the session ends

> Added `configDirectory` to the output of `claude auth status --json`

> Improved startup time in projects with `.claude/workflows/` scripts: listing them no longer parses each script

> Improved Claude in Chrome: long page reads now stay inline instead of being saved to a file and read back

> Changed Bedrock, Vertex and Foundry sessions to keep the tool list byte-stable across a conversation (late-connecting tools load deferred instead of rewriting it), matching first-party sessions

> Changed local Cowork sessions set to skip all approvals: the Artifact tool now refuses a local file outside the session's folders, or behind a symlink, instead of reading it without asking

> Changed plain `WebFetch` deny and ask rules to no longer apply to Artifact tool reads and updates; use an `Artifact` rule (or `WebFetch(domain:claude.ai)`) to block or gate them

> [Claude Tag] Improved formatting of comparisons: sentence-length comparisons now come as lists instead of wide tables that scroll sideways, and long table cells wrap

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-10-2-account-and-access-changes-in-v2-1-268|2 Account and Access changes in v2.1.268]] · Account and Access
- [[Changes/Claude Code/2026-09-10-2-interface-experience-changes-in-v2-1-268|2 Interface Experience changes in v2.1.268]] · Interface Experience
- [[Changes/Claude Code/2026-09-10-2-pricing-model-changes-in-v2-1-268|2 Pricing Model changes in v2.1.268]] · Pricing Model
- [[Changes/Claude Code/2026-09-10-added-browser-tab-icons-for-published-artifacts-chosen-by-claude-to-match-each-p|Added browser-tab icons for published artifacts, chosen by Claude to match each page]] · Editor Experience
- [[Changes/Claude Code/2026-09-10-2-memory-and-personalization-changes-in-v2-1-268|2 Memory and Personalization changes in v2.1.268]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-10-2-reliability-and-performance-changes-in-v2-1-268|2 Reliability and Performance changes in v2.1.268]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-10-code-review-added-a-note-under-the-still-open-findings-list-in-follow-up-reviews|Code Review Added a note under the still-open findings list in follow-up reviews]] · Developer Workflow
- [[Changes/Claude Code/2026-09-10-improved-auto-mode-denials-the-message-claude-receives-now-names-the-rule-that-b|Improved auto mode denials]] · Agent Mode
- [[Changes/Claude Code/2026-09-10-vscode-added-a-claude-code-focus-last-message-command-that-moves-keyboard-focus|VSCode Added a "Claude Code]] · Accessibility and Localization
- [[Changes/Claude Code/2026-09-10-8-safety-and-privacy-changes-in-v2-1-268|8 Safety and Privacy changes in v2.1.268]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-10-7-apps-and-integrations-changes-in-v2-1-268|7 Apps and Integrations changes in v2.1.268]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-10-2-model-support-changes-in-v2-1-268|2 Model Support changes in v2.1.268]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-10-1bffc8&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-10-9-other-changes-in-v2-1-268.md%0ACard%20ID%3A%20claude-code-2026-09-10-1bffc8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.268%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->