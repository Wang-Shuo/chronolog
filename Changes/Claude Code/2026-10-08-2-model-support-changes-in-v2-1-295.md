---
card_id: claude-code-2026-10-08-8504df
date: '2026-10-08'
description: 'Claude Code · 2026-10-08 · Model Support: 2 changes in v2.1.295 — Improved
  background requests behind a Claude apps gateway to use Haiku 4.5 instead of the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1368
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 99e5cba554be72a87e4b1bbb2a727a8cd4be0fa4c6b7a188bebcc69999005e1f
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-08-8504df
  comparison: ''
  date: '2026-10-08'
  description: 'Claude Code — v2.1.295: 2 Model Support changes'
  evidence:
  - quote: Improved background requests behind a Claude apps gateway to use Haiku
      4.5 instead of the session's model, falling back to the session's model where
      the gateway does not serve Haiku 4.5
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: Improved how the Claude apps gateway handles models not listed under `models:`
      in Amazon Bedrock regions outside AWS's US geography. AWS always refused those
      requests; the gateway now tries the model in your own region, and a refusal
      names the model to add
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-model-support-changes-in-v2-1-295
  source_release: claude-code-2026-10-08-v2-1-295-github-407134589-d5c87510
  source_type: github_releases
  theme: model-support
  title: 2 Model Support changes in v2.1.295
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-06-added-prompt-caching-to-model-complete-for-mods-prompt-and-system-take-blocks-of|Added
  prompt caching to $.model.complete for mods]]'
- '[[Changes/ChatGPT/2026-10-07-we-re-introducing-gpt-6-with-intelligent-ui-in-chatgpt-chatgpt-can-now-combine-t|GPT-6
  and Intelligent UI in ChatGPT]]'
- '[[Changes/Claude Code/2026-10-07-added-claude-haiku-5-5-claude-haiku-5-5-now-the-default-haiku-model-on-the-anthr|Added
  Claude Haiku 5.5 (claude-haiku-5-5), now the default Haiku model…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-08-v2-1-295-github-407134589-d5c87510|claude-code-2026-10-08-v2-1-295-github-407134589-d5c87510]]'
source_type: github_releases
theme: model-support
title: 2 Model Support changes in v2.1.295
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Model Support changes in v2.1.295

**Claude Code** · 2026-10-08 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.295) · from [[Releases/Claude Code/claude-code-2026-10-08-v2-1-295-github-407134589-d5c87510|v2.1.295]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved background requests behind a Claude apps gateway to use Haiku 4.5 instead of the session's model, falling back to the session's model where the gateway does not serve Haiku 4.5

> Improved how the Claude apps gateway handles models not listed under `models:` in Amazon Bedrock regions outside AWS's US geography. AWS always refused those requests; the gateway now tries the model in your own region, and a refusal names the model to add

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-08-3-agent-mode-changes-in-v2-1-295|3 Agent Mode changes in v2.1.295]] · Agent Mode
- [[Changes/Claude Code/2026-10-08-added-a-line-on-stderr-when-it-is-a-terminal-that-says-what-a-claude-p-run-is-wa|Added a line on stderr, when it is a terminal, that says what a claude -p run…]] · Developer Workflow
- [[Changes/Claude Code/2026-10-08-improved-token-counts-behind-a-claude-apps-gateway-on-amazon-bedrock-which-conte|Improved token counts behind a Claude apps gateway on Amazon Bedrock…]] · Context Window
- [[Changes/Claude Code/2026-10-08-changed-ctrl-c-at-the-idle-prompt-of-an-attached-background-session-to-leave-a-p|Changed Ctrl+C at the idle prompt of an attached background session to leave…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-10-08-14-apps-and-integrations-changes-in-v2-1-295|14 Apps and Integrations changes in v2.1.295]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-08-added-support-for-forceloginmethod-gateway-and-forcelogingatewayurl-in-your-own|Added support for forceLoginMethod: "gateway" and forceLoginGatewayUrl…]] · Account and Access
- [[Changes/Claude Code/2026-10-08-changed-tab-stops-to-count-from-where-a-text-starts-instead-of-from-the-screen-s|Changed tab stops to count from where a text starts instead of from the screen's left edge]] · Editor Experience
- [[Changes/Claude Code/2026-10-08-2-interface-experience-changes-in-v2-1-295|2 Interface Experience changes in v2.1.295]] · Interface Experience
- [[Changes/Claude Code/2026-10-08-2-mobile-and-desktop-changes-in-v2-1-295|2 Mobile and Desktop changes in v2.1.295]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-08-5-safety-and-privacy-changes-in-v2-1-295|5 Safety and Privacy changes in v2.1.295]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-08-claude-tag-changed-claude-s-notice-that-a-channel-shared-across-enterprise-grid|Claude Tag Changed Claude's notice that a channel shared across Enterprise Grid…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-08-15-other-changes-in-v2-1-295|15 other changes in v2.1.295]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-07 · Claude Code · [[Changes/Claude Code/2026-10-07-added-claude-haiku-5-5-claude-haiku-5-5-now-the-default-haiku-model-on-the-anthr|Added Claude Haiku 5.5 (claude-haiku-5-5), now the default Haiku model…]]
- Later: 2026-10-09 · Claude Code · [[Changes/Claude Code/2026-10-09-claude-tag-changed-claude-in-slack-to-show-the-footer-with-the-session-link-mode|Claude Tag Changed Claude in Slack to show the footer with the session link, model…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-08-8504df&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-08-2-model-support-changes-in-v2-1-295.md%0ACard%20ID%3A%20claude-code-2026-10-08-8504df%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.295%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->