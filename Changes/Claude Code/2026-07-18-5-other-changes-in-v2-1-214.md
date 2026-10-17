---
card_id: claude-code-2026-07-18-7f71f2
date: '2026-07-18'
description: 'Claude Code · 2026-07-18 · Other changes: 5 changes in v2.1.214 — Added
  the EndConversation tool: Claude can end sessions with highly abusive users or…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8098e04e1505b7ac88f10f2305e6858eb635aaf43fe8b7485232cda17f401452
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-18-7f71f2
  comparison: ''
  date: '2026-07-18'
  description: 'Claude Code — v2.1.214: 5 other changes'
  evidence:
  - quote: 'Added the EndConversation tool: Claude can end sessions with highly abusive
      users or jailbreak attempts, as on claude.ai since 2025 — see https://www.anthropic.com/research/end-subset-conversations'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
  - quote: Added `message.uuid`, `client_request_id`, and `tool_source` attributes
      to OpenTelemetry log events for message-level correlation and tool provenance
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
  - quote: Added `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH` to configure the 60 KB truncation
      limit on OpenTelemetry content attributes
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
  - quote: Improved the `claude rc` workspace-trust error in the home directory to
      say trust there is never saved and to suggest running from a project directory
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
  - quote: Changed keep-alive connection pooling to disable after a stale-connection
      error, so retries open a fresh socket
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-other-changes-in-v2-1-214
  source_release: claude-code-2026-07-18-v2-1-214-github-355973317-478680c5
  source_type: github_releases
  theme: uncategorized
  title: 5 other changes in v2.1.214
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-07-18-v2-1-214-github-355973317-478680c5|claude-code-2026-07-18-v2-1-214-github-355973317-478680c5]]'
source_type: github_releases
theme: uncategorized
title: 5 other changes in v2.1.214
type: change
---

<!-- chronolog:begin region="header" -->
# 5 other changes in v2.1.214

**Claude Code** · 2026-07-18 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.214) · from [[Releases/Claude Code/claude-code-2026-07-18-v2-1-214-github-355973317-478680c5|v2.1.214]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added the EndConversation tool: Claude can end sessions with highly abusive users or jailbreak attempts, as on claude.ai since 2025 — see https://www.anthropic.com/research/end-subset-conversations

> Added `message.uuid`, `client_request_id`, and `tool_source` attributes to OpenTelemetry log events for message-level correlation and tool provenance

> Added `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH` to configure the 60 KB truncation limit on OpenTelemetry content attributes

> Improved the `claude rc` workspace-trust error in the home directory to say trust there is never saved and to suggest running from a project directory

> Changed keep-alive connection pooling to disable after a stale-connection error, so retries open a fresh socket

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-18-added-an-iso-modified-timestamp-to-memory-file-frontmatter|Added an ISO modified timestamp to memory file frontmatter]] · Memory and Personalization
- [[Changes/Claude Code/2026-07-18-added-reasoning-effort-to-the-subagentstatusline-payload-so-custom-agent-rows-ca|Added reasoning effort to the subagentStatusLine payload, so custom agent rows can…]] · Agent Mode
- [[Changes/Claude Code/2026-07-18-added-a-periodic-progress-heartbeat-for-long-running-tool-calls-that-previously|Added a periodic progress heartbeat for long-running tool calls that previously went…]] · Reliability and Performance
- [[Changes/Claude Code/2026-07-18-9-safety-and-privacy-changes-in-v2-1-214|9 Safety and Privacy changes in v2.1.214]] · Safety and Privacy
- [[Changes/Claude Code/2026-07-18-changed-sessionstart-hooks-to-report-source-fork-when-a-session-begins-as-a-fork|Changed SessionStart hooks to report source "fork" when a session begins as a fork…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-18-7f71f2&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-18-5-other-changes-in-v2-1-214.md%0ACard%20ID%3A%20claude-code-2026-07-18-7f71f2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.214%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->