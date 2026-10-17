---
card_id: claude-code-2026-05-04-b3ecd9
date: '2026-05-04'
description: 'Claude Code · 2026-05-04 · Apps and Integrations: 6 changes in v2.1.128
  — `/mcp` now shows the tool count for connected servers and flags servers that…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1138
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3ae364b4b123dc36273b939d841d97d248e9b219395ccb79a1ca60fe31c2f6f0
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
- '[[Changes/Claude Code/2026-04-28-6-apps-and-integrations-changes-in-v2-1-121|6
  Apps and Integrations changes in v2.1.121]]'
- '[[Changes/Cursor/2026-04-29-we-re-introducing-the-cursor-sdk-so-you-can-build-agents-with-the-same-runtime-h|Cursor
  introduces the Cursor SDK so you can build agents with the same runtime…]]'
- '[[Changes/Cursor/2026-04-29-run-npm-install-cursor-sdk-to-get-started-you-can-also-use-cursor-s-native-sdk-s-76fb76|Run
  npm install @cursor/sdk to get started]]'
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
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-29 · Cursor · [[Changes/Cursor/2026-04-29-run-npm-install-cursor-sdk-to-get-started-you-can-also-use-cursor-s-native-sdk-s-76fb76|Run npm install @cursor/sdk to get started]]
- Later: 2026-05-06 · Claude Code · [[Changes/Claude Code/2026-05-06-added-claude-code-session-id-environment-variable-to-the-bash-tool-subprocess-en|Added CLAUDE_CODE_SESSION_ID environment variable to the Bash tool subprocess…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-04-b3ecd9&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-04-6-apps-and-integrations-changes-in-v2-1-128.md%0ACard%20ID%3A%20claude-code-2026-05-04-b3ecd9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.128%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->