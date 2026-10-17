---
card_id: claude-code-2026-03-26-1ded81
date: '2026-03-26'
description: 'Claude Code · 2026-03-26 · Reliability and Performance: 2 changes in
  v2.1.84 — Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming
  idle…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1197
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a2c2b3fb51c69012eb8bba4096c474d7e2a495ea1586fcfb55278ba564f86679
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-26-1ded81
  comparison: ''
  date: '2026-03-26'
  description: 'Claude Code — v2.1.84: 2 Reliability and Performance changes'
  evidence:
  - quote: Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming
      idle watchdog threshold (default 90s)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  - quote: Stats screenshot (Ctrl+S in /stats) now works in all builds and is 16×
      faster
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-reliability-and-performance-changes-in-v2-1-84
  source_release: claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa
  source_type: github_releases
  theme: reliability-performance
  title: 2 Reliability and Performance changes in v2.1.84
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-19-reduced-memory-usage-on-startup-in-large-repositories-80-mb-saved-on-250k-file-r|Reduced
  memory usage on startup in large repositories (~80 MB saved on 250k-file repos)]]'
- '[[Changes/Cursor/2026-03-19-composer-2-is-now-available-in-cursor-frontier-level-coding-performance-with-str|Composer
  2 is now available in Cursor]]'
- '[[Changes/Claude Code/2026-03-25-3-reliability-and-performance-changes-in-v2-1-83|3
  Reliability and Performance changes in v2.1.83]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa]]'
source_type: github_releases
theme: reliability-performance
title: 2 Reliability and Performance changes in v2.1.84
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Reliability and Performance changes in v2.1.84

**Claude Code** · 2026-03-26 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.84) · from [[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|v2.1.84]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming idle watchdog threshold (default 90s)

> Stats screenshot (Ctrl+S in /stats) now works in all builds and is 16× faster

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-26-fixed-the-allow-claude-to-edit-its-own-settings-for-this-session-permission-opti|Fixed the "allow Claude to edit its own settings for this session" permission option…]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-26-added-allowedchannelplugins-managed-setting-for-team-enterprise-admins-to-define|Added allowedChannelPlugins managed setting for team/enterprise admins to define…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-03-26-5-apps-and-integrations-changes-in-v2-1-84|5 Apps and Integrations changes in v2.1.84]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-26-added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef|Added ANTHROPIC_DEFAULT{OPUS,SONNET,HAIKU}MODEL_SUPPORTS env vars to override…]] · Model Support
- [[Changes/Claude Code/2026-03-26-slash-commands-unavailable-for-the-current-auth-setup-voice-mobile-chrome-upgrad|Slash commands unavailable for the current auth setup…]] · Voice and Audio
- [[Changes/Claude Code/2026-03-26-added-powershell-tool-for-windows-as-an-opt-in-preview-learn-more-at-https-code|Added PowerShell tool for Windows as an opt-in preview]] · Mobile and Desktop
- [[Changes/Claude Code/2026-03-26-2-agent-mode-changes-in-v2-1-84|2 Agent Mode changes in v2.1.84]] · Agent Mode
- [[Changes/Claude Code/2026-03-26-2-context-window-changes-in-v2-1-84|2 Context Window changes in v2.1.84]] · Context Window
- [[Changes/Claude Code/2026-03-26-5-developer-workflow-changes-in-v2-1-84|5 Developer Workflow changes in v2.1.84]] · Developer Workflow
- [[Changes/Claude Code/2026-03-26-6-other-changes-in-v2-1-84|6 other changes in v2.1.84]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-03-25 · Claude Code · [[Changes/Claude Code/2026-03-25-3-reliability-and-performance-changes-in-v2-1-83|3 Reliability and Performance changes in v2.1.83]]
- Later: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-improved-scroll-performance-with-large-transcripts-by-replacing-wasm-yoga-layout|Improved scroll performance with large transcripts by replacing WASM yoga-layout…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-26-1ded81&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-26-2-reliability-and-performance-changes-in-v2-1-84.md%0ACard%20ID%3A%20claude-code-2026-03-26-1ded81%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.84%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->