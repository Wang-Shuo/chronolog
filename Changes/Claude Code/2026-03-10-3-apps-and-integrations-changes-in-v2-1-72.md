---
card_id: claude-code-2026-03-10-f1f60f
date: '2026-03-10'
description: 'Claude Code · 2026-03-10 · Apps and Integrations: 3 changes in v2.1.72
  — Changed tool search to bypass the third-party proxy gate when the environment
  variable…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1083
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 55506e613a39b2d7f8c22f8ceaa99ca0b4493a53f9b0df011b23a0ed68c0201a
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
- '[[Changes/Claude Code/2026-03-05-7-apps-and-integrations-changes-in-v2-1-69|7 Apps
  and Integrations changes in v2.1.69]]'
- '[[Changes/Claude Code/2026-03-06-reduced-remote-control-poll-rate-to-once-per-10-minutes-while-connected-was-1-2s|Reduced
  Remote Control /poll rate to once per 10 minutes while connected…]]'
- '[[Changes/Claude Code/2026-03-07-3-apps-and-integrations-changes-in-v2-1-71|3 Apps
  and Integrations changes in v2.1.71]]'
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

- Earlier: 2026-03-07 · Claude Code · [[Changes/Claude Code/2026-03-07-3-apps-and-integrations-changes-in-v2-1-71|3 Apps and Integrations changes in v2.1.71]]
- Later: 2026-03-11 · Cursor · [[Changes/Cursor/2026-03-11-we-ve-added-more-than-30-new-plugins-from-partners-such-as-atlassian-datadog-git-901313|New Plugins on the Cursor Marketplace]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-10-f1f60f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-10-3-apps-and-integrations-changes-in-v2-1-72.md%0ACard%20ID%3A%20claude-code-2026-03-10-f1f60f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.72%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->