---
card_id: claude-code-2026-10-14-0e9e30
date: '2026-10-14'
description: 'Claude Code · 2026-10-14 · Context Window: Added `cache_creation_5m_tokens`
  and `cache_creation_1h_tokens` to the OpenTelemetry `api_request` event, splitting…'
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
kind: change
machine_hash: fc1e8cf11fab0b4db92e2d1da1c6ef66e1a573e062ec0b9291faa76aad86bd7a
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-14-0e9e30
  comparison: ''
  date: '2026-10-14'
  description: 'Claude Code — v2.1.300: Added `cache_creation_5m_tokens` and `cache_creation_1h_tokens`
    to the OpenTelemetry `api_request` event, splitting cache writes by lifetime'
  evidence:
  - quote: Added `cache_creation_5m_tokens` and `cache_creation_1h_tokens` to the
      OpenTelemetry `api_request` event, splitting cache writes by lifetime
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-cache-creation-5m-tokens-and-cache-creation-1h-tokens-to-the-opentelemetry
  source_release: claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0
  source_type: github_releases
  theme: context-window
  title: Added `cache_creation_5m_tokens` and `cache_creation_1h_tokens` to the OpenTelemetry…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-02-changed-autocompact-to-save-the-auto-compact-window-per-model-so-each-model-keep|Changed
  /autocompact to save the auto-compact window per model, so each model…]]'
- '[[Changes/Claude Code/2026-10-08-improved-token-counts-behind-a-claude-apps-gateway-on-amazon-bedrock-which-conte|Improved
  token counts behind a Claude apps gateway on Amazon Bedrock…]]'
- '[[Changes/Claude Code/2026-10-09-2-context-window-changes-in-v2-1-296|2 Context
  Window changes in v2.1.296]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0|claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0]]'
source_type: github_releases
theme: context-window
title: Added cache_creation_5m_tokens and cache_creation_1h_tokens to the OpenTelemetry…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `cache_creation_5m_tokens` and `cache_creation_1h_tokens` to the OpenTelemetry…

**Claude Code** · 2026-10-14 · [[Themes/context-window|Context Window]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.300) · from [[Releases/Claude Code/claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0|v2.1.300]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `cache_creation_5m_tokens` and `cache_creation_1h_tokens` to the OpenTelemetry `api_request` event, splitting cache writes by lifetime
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

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
- [[Changes/Claude Code/2026-10-14-5-other-changes-in-v2-1-300|5 other changes in v2.1.300]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-10-09 · Claude Code · [[Changes/Claude Code/2026-10-09-2-context-window-changes-in-v2-1-296|2 Context Window changes in v2.1.296]]
- Later: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-2-context-window-changes-in-v2-1-299|2 Context Window changes in v2.1.299]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-14-0e9e30&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-14-added-cache-creation-5m-tokens-and-cache-creation-1h-tokens-to-the-opentelemetry.md%0ACard%20ID%3A%20claude-code-2026-10-14-0e9e30%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.300%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->