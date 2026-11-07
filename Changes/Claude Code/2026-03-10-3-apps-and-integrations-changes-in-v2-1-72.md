---
card_id: claude-code-2026-03-10-f1f60f
date: '2026-03-10'
description: 'Claude Code · 2026-03-10 · Apps and Integrations: 3 changes in v2.1.72
  — Changed tool search to bypass the third-party proxy gate when the environment
  variable…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2643
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2a6f2e8d4158bec22f6b9261dfbe5cdba6cbbe57939c3bc996ca6442d62ca2e3
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-10-f1f60f
  comparison: ''
  date: '2026-03-10'
  description: 'Claude Code — v2.1.72: 3 Apps and Integrations changes'
  evidence:
  - quote: Changed tool search to bypass the third-party proxy gate when the environment
      variable is set (replaces `CLAUDE_CODE_PROXY_SUPPORTS_TOOL_REFERENCE`, now removed)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.72
  - quote: Added `claude plugins` as an alias for `claude plugin`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.72
  - quote: Improved `claude plugin validate` to explain that marketplace.json source
      paths are relative to the repo root when rejecting `../` paths
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.72
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-apps-and-integrations-changes-in-v2-1-72
  source_release: claude-code-2026-03-10-v2-1-72-github-294951528-18ee0f48
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v2.1.72
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-03-09-extensions-are-now-available-as-an-experimental-feature-ask-copilot-to-write-cus|Extensions
  are now available as an experimental feature]]'
- '[[Changes/GitHub Copilot CLI/2026-03-09-4-apps-and-integrations-changes-in-v1-0-3|4
  Apps and Integrations changes in v1.0.3]]'
- '[[Changes/Windsurf/2026-03-09-mcp|MCP]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-10-v2-1-72-github-294951528-18ee0f48|claude-code-2026-03-10-v2-1-72-github-294951528-18ee0f48]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v2.1.72
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v2.1.72

**Claude Code** · 2026-03-10 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.72) · from [[Releases/Claude Code/claude-code-2026-03-10-v2-1-72-github-294951528-18ee0f48|v2.1.72]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changed tool search to bypass the third-party proxy gate when the environment variable is set (replaces `CLAUDE_CODE_PROXY_SUPPORTS_TOOL_REFERENCE`, now removed)

> Added `claude plugins` as an alias for `claude plugin`

> Improved `claude plugin validate` to explain that marketplace.json source paths are relative to the repo root when rejecting `../` paths

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.72
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-10-improved-bash-command-parsing-by-switching-to-a-native-module-faster-initializat|Improved bash command parsing by switching to a native module]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-10-2-agent-mode-changes-in-v2-1-72|2 Agent Mode changes in v2.1.72]] · Agent Mode
- [[Changes/Claude Code/2026-03-10-3-developer-workflow-changes-in-v2-1-72|3 Developer Workflow changes in v2.1.72]] · Developer Workflow
- [[Changes/Claude Code/2026-03-10-added-claude-code-disable-cron-environment-variable-to-immediately-stop-schedule|Added CLAUDE_CODE_DISABLE_CRON environment variable to immediately stop scheduled…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-03-10-added-w-key-in-copy-to-write-the-focused-selection-directly-to-a-file-bypassing|Added w key in /copy to write the focused selection directly to a file…]] · Interface Experience
- [[Changes/Claude Code/2026-03-10-6-safety-and-privacy-changes-in-v2-1-72|6 Safety and Privacy changes in v2.1.72]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-10-improved-voice-input-transcription-accuracy-for-repo-names-and-common-dev-terms|Improved voice input transcription accuracy for repo names and common dev terms…]] · Voice and Audio
- [[Changes/Claude Code/2026-03-10-vscode-added-vscode-anthropic-claude-code-open-uri-handler-to-open-a-new-claude|VSCode: Added vscode://anthropic.claude-code/open URI handler to open a new Claude…]] · Editor Experience
- [[Changes/Claude Code/2026-03-10-7-other-changes-in-v2-1-72|7 other changes in v2.1.72]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-09 · Windsurf · [[Changes/Windsurf/2026-03-09-mcp|MCP]]
- Later: 2026-03-10 · Codex CLI · [[Changes/Codex CLI/2026-03-10-11-apps-and-integrations-changes-in-rust-v0-113-0|11 Apps and Integrations changes in rust-v0.113.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-10-f1f60f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-10-3-apps-and-integrations-changes-in-v2-1-72.md%0ACard%20ID%3A%20claude-code-2026-03-10-f1f60f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.72%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->