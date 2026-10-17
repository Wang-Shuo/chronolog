---
card_id: claude-code-2026-10-14-72821b
date: '2026-10-14'
description: 'Claude Code · 2026-10-14 · Mobile and Desktop: 3 changes in v2.1.300
  — Changed `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` sessions to ignore CA-bundle, tool-proxy…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support 🥳]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1310
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2de55c0dd0411877f0b986f74ea1f6bff4e4057b21c1927e90d7d93b626d182c
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-14-72821b
  comparison: ''
  date: '2026-10-14'
  description: 'Claude Code — v2.1.300: 3 Mobile and Desktop changes'
  evidence:
  - quote: Changed `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` sessions to ignore CA-bundle,
      tool-proxy, git TLS and git config variables like `SSL_CERT_FILE` in settings;
      under Claude Desktop, only in project settings
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  - quote: Changed Claude Desktop's Code tab to apply managed settings when `forceLoginGatewayUrl`
      names an Anthropic-operated gateway that serves the session's hostname; that
      gateway must be reachable at start
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  - quote: Changed `claude gateway` to stop at start, naming the key, on a `desktop:`
      policy key that Claude Desktop cannot use from a gateway, where it earlier started
      with a warning
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-mobile-and-desktop-changes-in-v2-1-300
  source_release: claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0
  source_type: github_releases
  theme: mobile-desktop
  title: 3 Mobile and Desktop changes in v2.1.300
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-08-2-mobile-and-desktop-changes-in-v2-1-295|2 Mobile
  and Desktop changes in v2.1.295]]'
- '[[Changes/Claude Code/2026-10-09-2-mobile-and-desktop-changes-in-v2-1-296|2 Mobile
  and Desktop changes in v2.1.296]]'
- '[[Changes/Claude Code/2026-10-14-added-support-for-turning-off-the-attribution-block-in-claude-desktop-s-code-tab|Added
  support for turning off the attribution block in Claude Desktop''s Code tab]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0|claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0]]'
source_type: github_releases
theme: mobile-desktop
title: 3 Mobile and Desktop changes in v2.1.300
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Mobile and Desktop changes in v2.1.300

**Claude Code** · 2026-10-14 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.300) · from [[Releases/Claude Code/claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0|v2.1.300]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changed `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` sessions to ignore CA-bundle, tool-proxy, git TLS and git config variables like `SSL_CERT_FILE` in settings; under Claude Desktop, only in project settings

> Changed Claude Desktop's Code tab to apply managed settings when `forceLoginGatewayUrl` names an Anthropic-operated gateway that serves the session's hostname; that gateway must be reachable at start

> Changed `claude gateway` to stop at start, naming the key, on a `desktop:` policy key that Claude Desktop cannot use from a gateway, where it earlier started with a warning

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-14-added-cache-creation-5m-tokens-and-cache-creation-1h-tokens-to-the-opentelemetry|Added cache_creation_5m_tokens and cache_creation_1h_tokens to the OpenTelemetry…]] · Context Window
- [[Changes/Claude Code/2026-10-14-7-apps-and-integrations-changes-in-v2-1-300|7 Apps and Integrations changes in v2.1.300]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-14-added-a-dir-prop-on-a-mod-s-text-for-right-to-left-text-on-windows-and-in-vs-cod|Added a dir prop on a mod's Text for right-to-left text]] · Developer Workflow
- [[Changes/Claude Code/2026-10-14-2-safety-and-privacy-changes-in-v2-1-300|2 Safety and Privacy changes in v2.1.300]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-14-improved-the-note-claude-3-models-get-about-an-mentioned-pdf-so-they-less-often|Improved the note Claude 3 models get about an @-mentioned PDF, so they less often…]] · Model Support
- [[Changes/Claude Code/2026-10-14-2-editor-experience-changes-in-v2-1-300|2 Editor Experience changes in v2.1.300]] · Editor Experience
- [[Changes/Claude Code/2026-10-14-changed-exit-to-force-kill-background-commands-still-running-1-5-seconds-after-b|Changed exit to force-kill background commands still running 1.5 seconds after being…]] · Interface Experience
- [[Changes/Claude Code/2026-10-14-claude-tag-added-support-for-slack-voice-clips-in-claude-in-slack-claude-reads-s|Claude Tag Added support for Slack voice clips in Claude in Slack]] · Voice and Audio
- [[Changes/Claude Code/2026-10-14-3-agent-mode-changes-in-v2-1-300|3 Agent Mode changes in v2.1.300]] · Agent Mode
- [[Changes/Claude Code/2026-10-14-changed-local-session-transcripts-to-also-record-each-api-request-s-system-promp|Changed local session transcripts to also record each API request's system prompt…]] · Collaboration
- [[Changes/Claude Code/2026-10-14-added-advisor-on-claude-platform-on-aws-no-advisor-runs-until-you-pick-one-with|Added /advisor on Claude Platform on AWS]] · Other changes
- [[Changes/Claude Code/2026-10-14-5-other-changes-in-v2-1-300|5 other changes in v2.1.300]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-added-support-for-turning-off-the-attribution-block-in-claude-desktop-s-code-tab|Added support for turning off the attribution block in Claude Desktop's Code tab]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-14-72821b&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-14-3-mobile-and-desktop-changes-in-v2-1-300.md%0ACard%20ID%3A%20claude-code-2026-10-14-72821b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.300%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->