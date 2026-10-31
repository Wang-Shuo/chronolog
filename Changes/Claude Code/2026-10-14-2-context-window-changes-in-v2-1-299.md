---
card_id: claude-code-2026-10-14-2c904a
date: '2026-10-14'
description: 'Claude Code · 2026-10-14 · Context Window: 2 changes in v2.1.299 — Added
  `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` to change idle compaction''s 200K-token minimum…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1259
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 630bdc507eeec9db3f69933c79a895584ca6cbc7b2683cd00cac786fdc10f23e
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-14-2c904a
  comparison: ''
  date: '2026-10-14'
  description: 'Claude Code — v2.1.299: 2 Context Window changes'
  evidence:
  - quote: 'Added `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` to change idle compaction''s
      200K-token minimum; `"idleCompaction": false` in settings.json turns it off.
      Both need v2.1.290 or later'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Improved `/reload-skills` to say it re-sends the full skill list to Claude,
      which is how to get skills back after compaction
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-context-window-changes-in-v2-1-299
  source_release: claude-code-2026-10-14-v2-1-299-github-412217284-623d9162
  source_type: github_releases
  theme: context-window
  title: 2 Context Window changes in v2.1.299
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-08-improved-token-counts-behind-a-claude-apps-gateway-on-amazon-bedrock-which-conte|Improved
  token counts behind a Claude apps gateway on Amazon Bedrock…]]'
- '[[Changes/Claude Code/2026-10-09-2-context-window-changes-in-v2-1-296|2 Context
  Window changes in v2.1.296]]'
- '[[Changes/Claude Code/2026-10-14-added-cache-creation-5m-tokens-and-cache-creation-1h-tokens-to-the-opentelemetry|Added
  cache_creation_5m_tokens and cache_creation_1h_tokens to the OpenTelemetry…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-14-v2-1-299-github-412217284-623d9162|claude-code-2026-10-14-v2-1-299-github-412217284-623d9162]]'
source_type: github_releases
theme: context-window
title: 2 Context Window changes in v2.1.299
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Context Window changes in v2.1.299

**Claude Code** · 2026-10-14 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.299) · from [[Releases/Claude Code/claude-code-2026-10-14-v2-1-299-github-412217284-623d9162|v2.1.299]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` to change idle compaction's 200K-token minimum; `"idleCompaction": false` in settings.json turns it off. Both need v2.1.290 or later

> Improved `/reload-skills` to say it re-sends the full skill list to Claude, which is how to get skills back after compaction

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-14-19-apps-and-integrations-changes-in-v2-1-299|19 Apps and Integrations changes in v2.1.299]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-14-10-developer-workflow-changes-in-v2-1-299|10 Developer Workflow changes in v2.1.299]] · Developer Workflow
- [[Changes/Claude Code/2026-10-14-2-model-support-changes-in-v2-1-299|2 Model Support changes in v2.1.299]] · Model Support
- [[Changes/Claude Code/2026-10-14-2-files-and-data-changes-in-v2-1-299|2 Files and Data changes in v2.1.299]] · Files and Data
- [[Changes/Claude Code/2026-10-14-2-editor-experience-changes-in-v2-1-299|2 Editor Experience changes in v2.1.299]] · Editor Experience
- [[Changes/Claude Code/2026-10-14-5-agent-mode-changes-in-v2-1-299|5 Agent Mode changes in v2.1.299]] · Agent Mode
- [[Changes/Claude Code/2026-10-14-added-effort-and-fast-in-agent-view-to-set-what-new-sessions-start-with-a-bare-m|Added /effort and /fast in agent view to set what new sessions start with]] · Interface Experience
- [[Changes/Claude Code/2026-10-14-improved-memory-and-disk-use-when-pdfs-are-mentioned-their-bytes-are-no-longer-k|Improved memory and disk use when PDFs are @-mentioned]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-14-added-usage-warnings-for-max-effort-workflows-always-on-context-and-large-tool-r|Added /usage warnings for max effort, workflows, always-on context and large tool…]] · Context Window
- [[Changes/Claude Code/2026-10-14-improved-the-error-shown-when-a-cloud-session-is-refused-because-your-claude-ai|Improved the error shown when a cloud session is refused because your claude.ai…]] · Account and Access
- [[Changes/Claude Code/2026-10-14-vscode-improved-startup-the-model-picker-and-slash-command-menu-now-fill-in-righ|VSCode Improved startup]] · Interface Experience
- [[Changes/Claude Code/2026-10-14-6-safety-and-privacy-changes-in-v2-1-299|6 Safety and Privacy changes in v2.1.299]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-14-11-other-changes-in-v2-1-299|11 other changes in v2.1.299]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-added-cache-creation-5m-tokens-and-cache-creation-1h-tokens-to-the-opentelemetry|Added cache_creation_5m_tokens and cache_creation_1h_tokens to the OpenTelemetry…]]
- Later: 2026-10-15 · Claude Code · [[Changes/Claude Code/2026-10-15-improved-switching-to-a-model-with-a-smaller-context-window-a-conversation-too-l|Improved switching to a model with a smaller context window]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-14-2c904a&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-14-2-context-window-changes-in-v2-1-299.md%0ACard%20ID%3A%20claude-code-2026-10-14-2c904a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.299%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->