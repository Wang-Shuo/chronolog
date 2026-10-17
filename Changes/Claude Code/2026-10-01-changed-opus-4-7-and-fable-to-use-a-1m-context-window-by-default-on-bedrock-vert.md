---
card_id: claude-code-2026-10-01-1aaa0a
date: '2026-10-01'
description: 'Claude Code · 2026-10-01 · Context Window: Changed Opus 4.7+ and Fable
  to use a 1M context window by default on Bedrock, Vertex, Foundry and the Claude
  apps…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1246
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: change
machine_hash: 59dcd3cf444d096bf3f799146cf53d5ca675927d16f9e67174ca73b402a5ae39
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-10-01-1aaa0a
  comparison: ''
  confidence: low
  date: '2026-10-01'
  description: 'Claude Code — v2.1.287: Changed Opus 4.7+ and Fable to use a 1M context
    window by default on Bedrock, Vertex, Foundry and the Claude apps gateway, with
    no `[1m]` suffix (`CLAUDE_CODE_DISABLE_1M_CONTEXT=1` keeps 200K)'
  evidence:
  - quote: Changed Opus 4.7+ and Fable to use a 1M context window by default on Bedrock,
      Vertex, Foundry and the Claude apps gateway, with no `[1m]` suffix (`CLAUDE_CODE_DISABLE_1M_CONTEXT=1`
      keeps 200K)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: changed-opus-4-7-and-fable-to-use-a-1m-context-window-by-default-on-bedrock-vert
  source_release: claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87
  source_type: github_releases
  theme: context-window
  theme_matches:
  - matched_terms:
    - context window
    - context
    score: 170
    theme: context-window
  - matched_terms:
    - apps
    score: 50
    theme: apps-integrations
  - matched_terms:
    - opus
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v2
  title: Changed Opus 4.7+ and Fable to use a 1M context window by default on Bedrock…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-25-2-context-window-changes-in-v2-1-283|2 Context
  Window changes in v2.1.283]]'
- '[[Changes/Claude Code/2026-09-29-2-context-window-changes-in-v2-1-285|2 Context
  Window changes in v2.1.285]]'
- '[[Changes/Claude Code/2026-09-30-improved-the-model-fallback-notice-and-the-autocompact-thrashing-error-to-say-wh|Improved
  the model fallback notice and the autocompact-thrashing error to say…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87|claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87]]'
source_type: github_releases
theme: context-window
title: Changed Opus 4.7+ and Fable to use a 1M context window by default on Bedrock…
type: change
---

<!-- chronolog:begin region="header" -->
# Changed Opus 4.7+ and Fable to use a 1M context window by default on Bedrock…

**Claude Code** · 2026-10-01 · [[Themes/context-window|Context Window]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.287) · from [[Releases/Claude Code/claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87|v2.1.287]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Changed Opus 4.7+ and Fable to use a 1M context window by default on Bedrock, Vertex, Foundry and the Claude apps gateway, with no `[1m]` suffix (`CLAUDE_CODE_DISABLE_1M_CONTEXT=1` keeps 200K)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-01-4-model-support-changes-in-v2-1-287|4 Model Support changes in v2.1.287]] · Model Support
- [[Changes/Claude Code/2026-10-01-2-mobile-and-desktop-changes-in-v2-1-287|2 Mobile and Desktop changes in v2.1.287]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-01-vscode-changed-the-claude-in-chrome-enabled-by-default-switch-to-also-connect-th|VSCode Changed the Claude in Chrome "Enabled by default" switch to also connect…]] · Editor Experience
- [[Changes/Claude Code/2026-10-01-6-safety-and-privacy-changes-in-v2-1-287|6 Safety and Privacy changes in v2.1.287]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-01-3-developer-workflow-changes-in-v2-1-287|3 Developer Workflow changes in v2.1.287]] · Developer Workflow
- [[Changes/Claude Code/2026-10-01-11-apps-and-integrations-changes-in-v2-1-287|11 Apps and Integrations changes in v2.1.287]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-01-2-reliability-and-performance-changes-in-v2-1-287|2 Reliability and Performance changes in v2.1.287]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-01-changed-screen-reader-mode-to-write-new-or-changed-lines-without-first-pausing-w|Changed screen reader mode to write new or changed lines without first pausing…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-01-4-agent-mode-changes-in-v2-1-287|4 Agent Mode changes in v2.1.287]] · Agent Mode
- [[Changes/Claude Code/2026-10-01-added-url-prompts-from-mcp-servers-on-the-2025-11-25-protocol-for-example-to-sig|Added URL prompts from MCP servers on the 2025-11-25 protocol, for example to sign in]] · Account and Access
- [[Changes/Claude Code/2026-10-01-improved-sdk-sessions-so-a-message-sent-with-priority-now-no-longer-cancels-a-ru|Improved SDK sessions so a message sent with priority "now" no longer cancels…]] · Search and Browsing
- [[Changes/Claude Code/2026-10-01-2-memory-and-personalization-changes-in-v2-1-287|2 Memory and Personalization changes in v2.1.287]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-01-4-other-changes-in-v2-1-287|4 other changes in v2.1.287]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-30 · Claude Code · [[Changes/Claude Code/2026-09-30-improved-the-model-fallback-notice-and-the-autocompact-thrashing-error-to-say-wh|Improved the model fallback notice and the autocompact-thrashing error to say…]]
- Later: 2026-10-02 · Claude Code · [[Changes/Claude Code/2026-10-02-changed-autocompact-to-save-the-auto-compact-window-per-model-so-each-model-keep|Changed /autocompact to save the auto-compact window per model, so each model…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-01-1aaa0a&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-01-changed-opus-4-7-and-fable-to-use-a-1m-context-window-by-default-on-bedrock-vert.md%0ACard%20ID%3A%20claude-code-2026-10-01-1aaa0a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.287%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->