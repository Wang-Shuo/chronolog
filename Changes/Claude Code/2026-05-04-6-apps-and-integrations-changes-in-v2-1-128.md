---
card_id: claude-code-2026-05-04-b3ecd9
date: '2026-05-04'
description: 'Claude Code · 2026-05-04 · Apps and Integrations: 6 changes in v2.1.128
  — `/mcp` now shows the tool count for connected servers and flags servers that…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2698
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d3800aa44d4b04c958fe11b66a36a5594461e820ae8403570ea8dcfd25578ee9
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-04-b3ecd9
  comparison: ''
  date: '2026-05-04'
  description: 'Claude Code — v2.1.128: 6 Apps and Integrations changes'
  evidence:
  - quote: '`/mcp` now shows the tool count for connected servers and flags servers
      that connected with 0 tools'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.128
  - quote: '`--plugin-dir` now accepts `.zip` plugin archives in addition to directories'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.128
  - quote: Subprocesses (Bash, hooks, MCP, LSP) no longer inherit `OTEL_*` environment
      variables, so OTEL-instrumented apps run via the Bash tool no longer pick up
      the CLI's own OTLP endpoint
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.128
  - quote: 'MCP: `workspace` is now a reserved server name — existing servers with
      that name will be skipped with a warning'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.128
  - quote: Reconnecting MCP servers no longer flood the conversation with full tool-name
      lists on every reconnect — re-announced tools are summarized by server prefix
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.128
  - quote: 'Headless `--output-format stream-json`: `init.plugin_errors` now includes
      `--plugin-dir` load failures in addition to dependency demotions'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.128
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-apps-and-integrations-changes-in-v2-1-128
  source_release: claude-code-2026-05-04-v2-1-128-github-317391175-a20e13a2
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in v2.1.128
  type: change
related_changes:
- '[[Changes/OpenCode/2026-05-01-core-invalid-remote-mcp-urls-now-fail-with-a-clear-error-instead-of-breaking-set|Core
  Invalid remote MCP URLs now fail with a clear error instead of breaking setup]]'
- '[[Changes/OpenHands/2026-05-01-2-apps-and-integrations-changes-in-1-7-0|2 Apps
  and Integrations changes in 1.7.0]]'
- '[[Changes/Replit/2026-05-01-replit-app-monitoring-keeps-an-eye-on-your-published-apps|Replit
  App Monitoring keeps an eye on your published apps]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-04-v2-1-128-github-317391175-a20e13a2|claude-code-2026-05-04-v2-1-128-github-317391175-a20e13a2]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in v2.1.128
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in v2.1.128

**Claude Code** · 2026-05-04 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.128) · from [[Releases/Claude Code/claude-code-2026-05-04-v2-1-128-github-317391175-a20e13a2|v2.1.128]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `/mcp` now shows the tool count for connected servers and flags servers that connected with 0 tools

> `--plugin-dir` now accepts `.zip` plugin archives in addition to directories

> Subprocesses (Bash, hooks, MCP, LSP) no longer inherit `OTEL_*` environment variables, so OTEL-instrumented apps run via the Bash tool no longer pick up the CLI's own OTLP endpoint

> MCP: `workspace` is now a reserved server name — existing servers with that name will be skipped with a warning

> Reconnecting MCP servers no longer flood the conversation with full tool-name lists on every reconnect — re-announced tools are summarized by server prefix

> Headless `--output-format stream-json`: `init.plugin_errors` now includes `--plugin-dir` load failures in addition to dependency demotions

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.128
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-04-auto-mode-when-the-classifier-can-t-evaluate-an-action-the-error-now-includes-a|Auto mode: when the classifier can't evaluate an action, the error now includes…]] · Agent Mode
- [[Changes/Claude Code/2026-05-04-bare-color-no-args-now-picks-a-random-session-color|Bare /color (no args) now picks a random session color]] · Interface Experience
- [[Changes/Claude Code/2026-05-04-sdk-hosts-now-receive-a-persistent-localsettings-suggestion-for-bash-permission|SDK hosts now receive a persistent localSettings suggestion for Bash permission…]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-04-updated-model-picker-collapsed-duplicate-opus-4-7-entries-and-current-opus-now-s|Updated /model picker]] · Model Support
- [[Changes/Claude Code/2026-05-04-channels-now-works-with-console-api-key-authentication-console-orgs-with-managed|--channels now works with console (API key) authentication]] · Account and Access
- [[Changes/Claude Code/2026-05-04-enterworktree-now-creates-the-new-branch-from-local-head-as-documented-instead-o|EnterWorktree now creates the new branch from local HEAD as documented, instead…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-01 · Replit · [[Changes/Replit/2026-05-01-replit-app-monitoring-keeps-an-eye-on-your-published-apps|Replit App Monitoring keeps an eye on your published apps]]
- Later: 2026-05-04 · ElevenLabs · [[Changes/ElevenLabs/2026-05-04-sdk-releases|SDK Releases]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-04-b3ecd9&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-04-6-apps-and-integrations-changes-in-v2-1-128.md%0ACard%20ID%3A%20claude-code-2026-05-04-b3ecd9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.128%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->