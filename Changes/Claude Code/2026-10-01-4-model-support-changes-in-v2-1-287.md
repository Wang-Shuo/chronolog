---
card_id: claude-code-2026-10-01-1a5215
date: '2026-10-01'
description: 'Claude Code · 2026-10-01 · Model Support: 4 changes in v2.1.287 — Bedrock,
  Vertex, Mantle: Fixed model availability checks under `CLAUDE_CODE_SKIP_*_AUTH`…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1361
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3ecb4dbd79c7a829550c67a30956daa0e0778729474e334ece0fd6d3ad46b8a0
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-01-1a5215
  comparison: ''
  date: '2026-10-01'
  description: 'Claude Code — v2.1.287: 4 Model Support changes'
  evidence:
  - quote: 'Bedrock, Vertex, Mantle: Fixed model availability checks under `CLAUDE_CODE_SKIP_*_AUTH`
      sending a different `Authorization` header than real requests when `ANTHROPIC_CUSTOM_HEADERS`
      repeats it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: 'Improved the Claude apps gateway''s error when Amazon Bedrock rejects
      a model ID: developers now see which model is unavailable, and the gateway log
      names the ID that was sent'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: 'Improved `/skill` names typed mid-message: Claude is now told they are
      skills, including `disable-model-invocation` ones'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  - quote: Changed automatic model switches after a flagged message to keep your current
      effort level instead of the new model's default
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-model-support-changes-in-v2-1-287
  source_release: claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in v2.1.287
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-29-eligible-plus-and-pro-users-can-authorize-participating-apps-to-use-their-chatgp|Eligible
  Plus and Pro users can authorize participating apps to use their ChatGPT…]]'
- '[[Changes/Claude Code/2026-09-29-3-model-support-changes-in-v2-1-285|3 Model Support
  changes in v2.1.285]]'
- '[[Changes/Claude Code/2026-09-30-changed-how-failed-api-requests-are-retried-one-limit-now-covers-a-whole-model-c|Changed
  how failed API requests are retried]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87|claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in v2.1.287
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v2.1.287

**Claude Code** · 2026-10-01 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.287) · from [[Releases/Claude Code/claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87|v2.1.287]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Bedrock, Vertex, Mantle: Fixed model availability checks under `CLAUDE_CODE_SKIP_*_AUTH` sending a different `Authorization` header than real requests when `ANTHROPIC_CUSTOM_HEADERS` repeats it

> Improved the Claude apps gateway's error when Amazon Bedrock rejects a model ID: developers now see which model is unavailable, and the gateway log names the ID that was sent

> Improved `/skill` names typed mid-message: Claude is now told they are skills, including `disable-model-invocation` ones

> Changed automatic model switches after a flagged message to keep your current effort level instead of the new model's default

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

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
- [[Changes/Claude Code/2026-10-01-4-other-changes-in-v2-1-287|4 other changes in v2.1.287]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-30 · Claude Code · [[Changes/Claude Code/2026-09-30-changed-how-failed-api-requests-are-retried-one-limit-now-covers-a-whole-model-c|Changed how failed API requests are retried]]
- Later: 2026-10-02 · Claude Code · [[Changes/Claude Code/2026-10-02-changed-the-client-side-auto-mode-classifier-to-ignore-an-anthropic-default-sonn|Changed the client-side auto mode classifier to ignore…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-01-1a5215&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-01-4-model-support-changes-in-v2-1-287.md%0ACard%20ID%3A%20claude-code-2026-10-01-1a5215%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.287%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->