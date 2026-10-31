---
card_id: claude-code-2026-10-14-f47036
date: '2026-10-14'
description: 'Claude Code · 2026-10-14 · Other changes: 5 changes in v2.1.300 — Added
  `virtualText` to a mod''s prompt decorations: text drawn in the prompt box that
  never…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5e5ff9d76581a05265b46470ab17f538a3218daa9f477d88482cacb51ce3e4e7
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-14-f47036
  comparison: ''
  date: '2026-10-14'
  description: 'Claude Code — v2.1.300: 5 other changes'
  evidence:
  - quote: 'Added `virtualText` to a mod''s prompt decorations: text drawn in the
      prompt box that never enters the draft or the submitted prompt'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  - quote: Added OpenTelemetry GenAI semantic-convention attributes to trace spans,
      such as `gen_ai.provider.name`, `gen_ai.conversation.id`, `gen_ai.tool.name`
      and `error.type`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  - quote: Improved WebFetch in Cowork cloud sessions to tell Claude that a page failed
      moments ago instead of fetching it again
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  - quote: Changed large requests to api.anthropic.com to use gzip compression even
      when telemetry is disabled; set `CLAUDE_CODE_GZIP_REQUEST_BODIES=0` to turn
      it off
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  - quote: Changed background sessions to resume a carried workflow through the Workflow
      tool's approval instead of running it from the handoff file
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-other-changes-in-v2-1-300
  source_release: claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0
  source_type: github_releases
  theme: uncategorized
  title: 5 other changes in v2.1.300
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0|claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0]]'
source_type: github_releases
theme: uncategorized
title: 5 other changes in v2.1.300
type: change
---

<!-- chronolog:begin region="header" -->
# 5 other changes in v2.1.300

**Claude Code** · 2026-10-14 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.300) · from [[Releases/Claude Code/claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0|v2.1.300]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `virtualText` to a mod's prompt decorations: text drawn in the prompt box that never enters the draft or the submitted prompt

> Added OpenTelemetry GenAI semantic-convention attributes to trace spans, such as `gen_ai.provider.name`, `gen_ai.conversation.id`, `gen_ai.tool.name` and `error.type`

> Improved WebFetch in Cowork cloud sessions to tell Claude that a page failed moments ago instead of fetching it again

> Changed large requests to api.anthropic.com to use gzip compression even when telemetry is disabled; set `CLAUDE_CODE_GZIP_REQUEST_BODIES=0` to turn it off

> Changed background sessions to resume a carried workflow through the Workflow tool's approval instead of running it from the handoff file

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-14-added-cache-creation-5m-tokens-and-cache-creation-1h-tokens-to-the-opentelemetry|Added cache_creation_5m_tokens and cache_creation_1h_tokens to the OpenTelemetry…]] · Context Window
- [[Changes/Claude Code/2026-10-14-7-apps-and-integrations-changes-in-v2-1-300|7 Apps and Integrations changes in v2.1.300]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-14-added-a-dir-prop-on-a-mod-s-text-for-right-to-left-text-on-windows-and-in-vs-cod|Added a dir prop on a mod's Text for right-to-left text]] · Developer Workflow
- [[Changes/Claude Code/2026-10-14-2-safety-and-privacy-changes-in-v2-1-300|2 Safety and Privacy changes in v2.1.300]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-14-3-editor-experience-changes-in-v2-1-300|3 Editor Experience changes in v2.1.300]] · Editor Experience
- [[Changes/Claude Code/2026-10-14-2-mobile-and-desktop-changes-in-v2-1-300|2 Mobile and Desktop changes in v2.1.300]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-14-improved-the-note-claude-3-models-get-about-an-mentioned-pdf-so-they-less-often|Improved the note Claude 3 models get about an @-mentioned PDF, so they less often…]] · Model Support
- [[Changes/Claude Code/2026-10-14-changed-exit-to-force-kill-background-commands-still-running-1-5-seconds-after-b|Changed exit to force-kill background commands still running 1.5 seconds after being…]] · Interface Experience
- [[Changes/Claude Code/2026-10-14-claude-tag-added-support-for-slack-voice-clips-in-claude-in-slack-claude-reads-s|Claude Tag Added support for Slack voice clips in Claude in Slack]] · Voice and Audio
- [[Changes/Claude Code/2026-10-14-3-agent-mode-changes-in-v2-1-300|3 Agent Mode changes in v2.1.300]] · Agent Mode
- [[Changes/Claude Code/2026-10-14-changed-local-session-transcripts-to-also-record-each-api-request-s-system-promp|Changed local session transcripts to also record each API request's system prompt…]] · Collaboration
- [[Changes/Claude Code/2026-10-14-added-advisor-on-claude-platform-on-aws-no-advisor-runs-until-you-pick-one-with|Added /advisor on Claude Platform on AWS]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-14-f47036&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-14-5-other-changes-in-v2-1-300.md%0ACard%20ID%3A%20claude-code-2026-10-14-f47036%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.300%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->