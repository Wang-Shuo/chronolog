---
card_id: claude-code-2026-03-26-d5e71a
date: '2026-03-26'
description: 'Claude Code · 2026-03-26 · Apps and Integrations: 4 changes in v2.1.85
  — Added `CLAUDE_CODE_MCP_SERVER_NAME` and `CLAUDE_CODE_MCP_SERVER_URL` environment…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1099
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: da1f885627d960bce52bbe41510f8253baa7cab645f05e2cc1a965dd80eadbb7
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-26-d5e71a
  comparison: ''
  date: '2026-03-26'
  description: 'Claude Code — v2.1.85: 4 Apps and Integrations changes'
  evidence:
  - quote: Added `CLAUDE_CODE_MCP_SERVER_NAME` and `CLAUDE_CODE_MCP_SERVER_URL` environment
      variables to MCP `headersHelper` scripts, allowing one helper to serve multiple
      servers
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.85
  - quote: Deep link queries (`claude-cli://open?q=…`) now support up to 5,000 characters,
      with a "scroll to review" warning for long pre-filled prompts
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.85
  - quote: Plugins blocked by organization policy (`managed-settings.json`) can no
      longer be installed or enabled, and are hidden from marketplace views
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.85
  - quote: 'PreToolUse hooks can now satisfy `AskUserQuestion` by returning `updatedInput`
      alongside `permissionDecision: "allow"`, enabling headless integrations that
      collect answers via their own UI'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.85
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-apps-and-integrations-changes-in-v2-1-85
  source_release: claude-code-2026-03-26-v2-1-85-github-302129484-6eb9dcd7
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v2.1.85
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-03-25-google-s-file-connectors-in-chatgpt-are-now-unified-under-google-drive-providing|Google
  Drive app unification]]'
- '[[Changes/Claude Code/2026-03-25-6-apps-and-integrations-changes-in-v2-1-83|6 Apps
  and Integrations changes in v2.1.83]]'
- '[[Changes/Claude Code/2026-03-26-5-apps-and-integrations-changes-in-v2-1-84|5 Apps
  and Integrations changes in v2.1.84]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-26-v2-1-85-github-302129484-6eb9dcd7|claude-code-2026-03-26-v2-1-85-github-302129484-6eb9dcd7]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v2.1.85
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v2.1.85

**Claude Code** · 2026-03-26 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.85) · from [[Releases/Claude Code/claude-code-2026-03-26-v2-1-85-github-302129484-6eb9dcd7|v2.1.85]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `CLAUDE_CODE_MCP_SERVER_NAME` and `CLAUDE_CODE_MCP_SERVER_URL` environment variables to MCP `headersHelper` scripts, allowing one helper to serve multiple servers

> Deep link queries (`claude-cli://open?q=…`) now support up to 5,000 characters, with a "scroll to review" warning for long pre-filled prompts

> Plugins blocked by organization policy (`managed-settings.json`) can no longer be installed or enabled, and are hidden from marketplace views

> PreToolUse hooks can now satisfy `AskUserQuestion` by returning `updatedInput` alongside `permissionDecision: "allow"`, enabling headless integrations that collect answers via their own UI

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.85
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-26-mcp-oauth-now-follows-rfc-9728-protected-resource-metadata-discovery-to-find-the|MCP OAuth now follows RFC 9728 Protected Resource Metadata discovery to find…]] · Account and Access
- [[Changes/Claude Code/2026-03-26-improved-scroll-performance-with-large-transcripts-by-replacing-wasm-yoga-layout|Improved scroll performance with large transcripts by replacing WASM yoga-layout…]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-26-added-timestamp-markers-in-transcripts-when-scheduled-tasks-loop-croncreate-fire|Added timestamp markers in transcripts when scheduled tasks (/loop, CronCreate) fire]] · Automation and Scheduling
- [[Changes/Claude Code/2026-03-26-2-safety-and-privacy-changes-in-v2-1-85|2 Safety and Privacy changes in v2.1.85]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-26-improved-mention-file-autocomplete-performance-on-large-repositories|Improved @-mention file autocomplete performance on large repositories]] · Interface Experience
- [[Changes/Claude Code/2026-03-26-reduced-ui-stutter-when-compaction-triggers-on-large-sessions|Reduced UI stutter when compaction triggers on large sessions]] · Context Window
- [[Changes/Claude Code/2026-03-26-improved-powershell-dangerous-command-detection|Improved PowerShell dangerous command detection]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-5-apps-and-integrations-changes-in-v2-1-84|5 Apps and Integrations changes in v2.1.84]]
- Later: 2026-03-27 · ChatGPT · [[Changes/ChatGPT/2026-03-27-we-re-rolling-out-updated-box-notion-linear-and-dropbox-apps-in-chatgpt-these-up-9f6ee9|Updated Box, Notion, Linear, and Dropbox apps]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-26-d5e71a&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-26-4-apps-and-integrations-changes-in-v2-1-85.md%0ACard%20ID%3A%20claude-code-2026-03-26-d5e71a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.85%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->