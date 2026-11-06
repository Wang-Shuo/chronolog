---
card_id: github-copilot-cli-2026-10-13-315f6b
date: '2026-10-13'
description: 'GitHub Copilot CLI · 2026-10-13 · Other changes: 8 changes in 1.0.97
  — Streamed responses behind TLS-intercepting proxies complete when close_notify
  is omitted'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9e92142a32239624f5f225572447023946b6516575534ebf2ac7f3e3095b5716
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-10-13-315f6b
  comparison: ''
  date: '2026-10-13'
  description: 'GitHub Copilot CLI — 1.0.97: 8 other changes'
  evidence:
  - quote: Streamed responses behind TLS-intercepting proxies complete when close_notify
      is omitted
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.97
  - quote: Keep saved settings such as dismissed prompts, trusted folders and sign-ins
      when one entry in config.json is invalid, instead of resetting them on every
      launch
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.97
  - quote: File reads using a view_range that is not exactly two elements, such as
      a lone start line, now show their line range and line count in the timeline,
      and session exports no longer contain the literal text undefined
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.97
  - quote: Dragging to select text in the transcript no longer occasionally highlights
      and copies the row below the pointer.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.97
  - quote: Redact secrets safely in --output-format json output while preserving valid
      variable references
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.97
  - quote: Resuming suspended sessions now reports interrupted tool calls and avoids
      replaying canceled writes.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.97
  - quote: Keep /user switch new-session choices visible after account checks in short
      terminals
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.97
  - quote: Inline images render by default on supported terminals without enabling
      experimental mode. Use `/settings inlineImages false` to turn them off
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.97
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 8-other-changes-in-v1-0-97
  source_release: github-copilot-cli-2026-10-13-v1-0-97-github-411990782-ee7b7038
  source_type: github_releases
  theme: uncategorized
  title: 8 other changes in v1.0.97
  type: change
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-10-13-v1-0-97-github-411990782-ee7b7038|github-copilot-cli-2026-10-13-v1-0-97-github-411990782-ee7b7038]]'
source_type: github_releases
theme: uncategorized
title: 8 other changes in v1.0.97
type: change
---

<!-- chronolog:begin region="header" -->
# 8 other changes in v1.0.97

**GitHub Copilot CLI** · 2026-10-13 · Other changes · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.97) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-10-13-v1-0-97-github-411990782-ee7b7038|1.0.97]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Streamed responses behind TLS-intercepting proxies complete when close_notify is omitted

> Keep saved settings such as dismissed prompts, trusted folders and sign-ins when one entry in config.json is invalid, instead of resetting them on every launch

> File reads using a view_range that is not exactly two elements, such as a lone start line, now show their line range and line count in the timeline, and session exports no longer contain the literal text undefined

> Dragging to select text in the transcript no longer occasionally highlights and copies the row below the pointer.

> Redact secrets safely in --output-format json output while preserving valid variable references

> Resuming suspended sessions now reports interrupted tool calls and avoids replaying canceled writes.

> Keep /user switch new-session choices visible after account checks in short terminals

> Inline images render by default on supported terminals without enabling experimental mode. Use `/settings inlineImages false` to turn them off

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.97
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-10-13-background-shell-wait-status-no-longer-animates-when-no-foreground-work-is-runni|Background-shell wait status no longer animates when no foreground work is running]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-10-13-3-safety-and-privacy-changes-in-v1-0-97|3 Safety and Privacy changes in v1.0.97]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-10-13-show-billed-ai-credits-in-usage-for-token-billed-sessions-including-after-resume|Show billed AI Credits in /usage for token-billed sessions, including after resume]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-10-13-emergency-memory-relief-in-long-sessions-can-now-bypass-its-cooldown-before-v8-a|Emergency memory relief in long sessions can now bypass its cooldown before V8…]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-10-13-synchronous-task-json-output-now-includes-failed-child-error-and-lifecycle-event|Synchronous /task JSON output now includes failed child error and lifecycle events…]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-10-13-3-agent-mode-changes-in-v1-0-97|3 Agent Mode changes in v1.0.97]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-10-13-4-apps-and-integrations-changes-in-v1-0-97|4 Apps and Integrations changes in v1.0.97]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-10-13-power-bi-and-bluebird-mcp-servers-accept-their-published-resource-scopes-during|Power BI and Bluebird MCP servers accept their published resource scopes during sign-in]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-10-13-315f6b&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-10-13-8-other-changes-in-v1-0-97.md%0ACard%20ID%3A%20github-copilot-cli-2026-10-13-315f6b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.97%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->