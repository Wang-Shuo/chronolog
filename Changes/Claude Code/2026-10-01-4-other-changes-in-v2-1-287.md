---
card_id: claude-code-2026-10-01-d2811f
date: '2026-10-01'
description: 'Claude Code · 2026-10-01 · Other changes: 4 changes in v2.1.287 — Added
  `prompt_text` to the OpenTelemetry `user_prompt` event, a copy of `prompt` for backends…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7040582e9f9dc06516c75ef0036dadddbd92d7fb106d4cc9b56eee029ce21ecf
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-01-d2811f
  comparison: ''
  date: '2026-10-01'
  description: 'Claude Code — v2.1.287: 4 other changes'
  evidence:
  - quote: Added `prompt_text` to the OpenTelemetry `user_prompt` event, a copy of
      `prompt` for backends that nest dotted keys; drop or mask it wherever you drop
      or mask `prompt` (anthropics/claude-code#70763)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: 'Improved `/config`: settings that cycle show ‹ › and step both ways with
      ←/→, narrow terminals stack each value under its label, and PgUp/PgDn page the
      list'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: Improved the contrast of the prompt input border in light themes and of
      the ❯ before your earlier messages
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: 'Improved what Claude says when a file cannot be sent for a reason that
      may be temporary: it now mentions that you can ask for the file again in a few
      minutes'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-other-changes-in-v2-1-287
  source_release: claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87
  source_type: github_releases
  theme: uncategorized
  title: 4 other changes in v2.1.287
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87|claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87]]'
source_type: github_releases
theme: uncategorized
title: 4 other changes in v2.1.287
type: change
---

<!-- chronolog:begin region="header" -->
# 4 other changes in v2.1.287

**Claude Code** · 2026-10-01 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.287) · from [[Releases/Claude Code/claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87|v2.1.287]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `prompt_text` to the OpenTelemetry `user_prompt` event, a copy of `prompt` for backends that nest dotted keys; drop or mask it wherever you drop or mask `prompt` (anthropics/claude-code#70763)

> Improved `/config`: settings that cycle show ‹ › and step both ways with ←/→, narrow terminals stack each value under its label, and PgUp/PgDn page the list

> Improved the contrast of the prompt input border in light themes and of the ❯ before your earlier messages

> Improved what Claude says when a file cannot be sent for a reason that may be temporary: it now mentions that you can ask for the file again in a few minutes

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-01-4-model-support-changes-in-v2-1-287|4 Model Support changes in v2.1.287]] · Model Support
- [[Changes/Claude Code/2026-10-01-changed-opus-4-7-and-fable-to-use-a-1m-context-window-by-default-on-bedrock-vert|Changed Opus 4.7+ and Fable to use a 1M context window by default on Bedrock…]] · Context Window
- [[Changes/Claude Code/2026-10-01-2-mobile-and-desktop-changes-in-v2-1-287|2 Mobile and Desktop changes in v2.1.287]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-01-vscode-changed-the-claude-in-chrome-enabled-by-default-switch-to-also-connect-th|VSCode Changed the Claude in Chrome "Enabled by default" switch to also connect…]] · Editor Experience
- [[Changes/Claude Code/2026-10-01-6-safety-and-privacy-changes-in-v2-1-287|6 Safety and Privacy changes in v2.1.287]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-01-3-developer-workflow-changes-in-v2-1-287|3 Developer Workflow changes in v2.1.287]] · Developer Workflow
- [[Changes/Claude Code/2026-10-01-11-apps-and-integrations-changes-in-v2-1-287|11 Apps and Integrations changes in v2.1.287]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-01-changed-screen-reader-mode-to-write-new-or-changed-lines-without-first-pausing-w|Changed screen reader mode to write new or changed lines without first pausing…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-01-3-reliability-and-performance-changes-in-v2-1-287|3 Reliability and Performance changes in v2.1.287]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-01-4-agent-mode-changes-in-v2-1-287|4 Agent Mode changes in v2.1.287]] · Agent Mode
- [[Changes/Claude Code/2026-10-01-improved-memory-the-left-and-right-arrow-keys-now-flip-its-on-off-settings-such|Improved /memory: the left and right arrow keys now flip its on/off settings, such…]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-01-added-url-prompts-from-mcp-servers-on-the-2025-11-25-protocol-for-example-to-sig|Added URL prompts from MCP servers on the 2025-11-25 protocol, for example to sign in]] · Account and Access
- [[Changes/Claude Code/2026-10-01-improved-sdk-sessions-so-a-message-sent-with-priority-now-no-longer-cancels-a-ru|Improved SDK sessions so a message sent with priority "now" no longer cancels…]] · Search and Browsing
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-01-d2811f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-01-4-other-changes-in-v2-1-287.md%0ACard%20ID%3A%20claude-code-2026-10-01-d2811f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.287%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->