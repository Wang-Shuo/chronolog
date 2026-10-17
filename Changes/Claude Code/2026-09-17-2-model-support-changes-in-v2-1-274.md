---
card_id: claude-code-2026-09-17-73dd77
date: '2026-09-17'
description: 'Claude Code · 2026-09-17 · Model Support: 2 changes in v2.1.274 — Added
  `effort` attribute to the `claude_code.llm_request` OpenTelemetry trace span, matching…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1347
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7f019195a2facad940c088fcb7db3ea0116236f133289055ef1ca5b2ac3a034b
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-17-73dd77
  comparison: ''
  date: '2026-09-17'
  description: 'Claude Code — v2.1.274: 2 Model Support changes'
  evidence:
  - quote: Added `effort` attribute to the `claude_code.llm_request` OpenTelemetry
      trace span, matching the `api_request` event
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: 'Improved Monitor tool notifications: a script''s final output and its
      exit now arrive as one notification instead of two, saving a model turn'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-model-support-changes-in-v2-1-274
  source_release: claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d
  source_type: github_releases
  theme: model-support
  title: 2 Model Support changes in v2.1.274
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-14-we-re-retiring-automatic-switching-from-instant-to-thinking-reasoning-for-chatgp|Changes
  to automatic switching to thinking in ChatGPT (Plus and Pro)]]'
- '[[Changes/Claude Code/2026-09-14-improved-startup-time-slightly-by-skipping-a-redundant-validation-of-built-in-mo|Improved
  startup time slightly by skipping a redundant validation of built-in model…]]'
- '[[Changes/Claude Code/2026-09-15-changed-bug-and-feedback-reports-to-include-only-model-behavior-params-model-sys|Changed
  /bug and /feedback reports to include only model-behavior params…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d|claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d]]'
source_type: github_releases
theme: model-support
title: 2 Model Support changes in v2.1.274
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Model Support changes in v2.1.274

**Claude Code** · 2026-09-17 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.274) · from [[Releases/Claude Code/claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d|v2.1.274]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `effort` attribute to the `claude_code.llm_request` OpenTelemetry trace span, matching the `api_request` event

> Improved Monitor tool notifications: a script's final output and its exit now arrive as one notification instead of two, saving a model turn

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-17-10-apps-and-integrations-changes-in-v2-1-274|10 Apps and Integrations changes in v2.1.274]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-17-improved-claude-apps-gateway-sign-in-rate-limit-errors-login-now-explains-the-re|Improved Claude apps gateway sign-in rate limit errors]] · Account and Access
- [[Changes/Claude Code/2026-09-17-claude-code-on-the-web-changed-a-routine-s-on-hold-notice-when-your-subscription|Claude Code on the web Changed a routine's on-hold notice]] · Pricing Model
- [[Changes/Claude Code/2026-09-17-added-enduser-sub-the-idp-subject-to-the-telemetry-claude-desktop-and-cowork-sen|Added enduser.sub, the IdP subject, to the telemetry Claude Desktop and Cowork…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-17-vscode-improved-screen-reader-navigation-of-the-conversation-each-message-is-ann|VSCode Improved screen reader navigation of the conversation]] · Accessibility and Localization
- [[Changes/Claude Code/2026-09-17-7-developer-workflow-changes-in-v2-1-274|7 Developer Workflow changes in v2.1.274]] · Developer Workflow
- [[Changes/Claude Code/2026-09-17-vscode-added-a-claudecode-lockeditorgroups-setting-to-stop-claude-from-locking-t|VSCode Added a claudeCode.lockEditorGroups setting to stop Claude from locking…]] · Editor Experience
- [[Changes/Claude Code/2026-09-17-vscode-added-memory-and-instructions-entries-to-the-customize-menu-memory-shows|VSCode Added Memory and Instructions entries to the Customize menu]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-17-claude-tag-removed-the-repeated-guest-attribution-note-claude-appended-to-a-slac|Claude Tag Removed the repeated guest-attribution note Claude appended to a Slack…]] · Files and Data
- [[Changes/Claude Code/2026-09-17-2-interface-experience-changes-in-v2-1-274|2 Interface Experience changes in v2.1.274]] · Interface Experience
- [[Changes/Claude Code/2026-09-17-3-safety-and-privacy-changes-in-v2-1-274|3 Safety and Privacy changes in v2.1.274]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-17-added-a-visible-warning-when-memory-usage-is-critical-with-steps-to-free-memory|Added a visible warning when memory usage is critical, with steps to free memory…]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-17-8-other-changes-in-v2-1-274|8 other changes in v2.1.274]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-15 · Claude Code · [[Changes/Claude Code/2026-09-15-changed-bug-and-feedback-reports-to-include-only-model-behavior-params-model-sys|Changed /bug and /feedback reports to include only model-behavior params…]]
- Later: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-added-a-send-now-key-ctrl-enter-or-ctrl-x-ctrl-s-that-interrupts-the-current-tur|Added a send-now key (ctrl+enter, or ctrl+x ctrl+s) that interrupts the current turn…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-17-73dd77&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-17-2-model-support-changes-in-v2-1-274.md%0ACard%20ID%3A%20claude-code-2026-09-17-73dd77%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.274%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->