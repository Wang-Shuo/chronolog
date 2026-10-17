---
card_id: claude-code-2026-03-26-3c8e42
date: '2026-03-26'
description: 'Claude Code · 2026-03-26 · Model Support: Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS`
  env vars to override effort/thinking capability…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1172
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 2c7414e8841a9949af6405c952fcb552789ce8a3b56e38e758f53e7cab47a50a
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-03-26-3c8e42
  comparison: ''
  confidence: low
  date: '2026-03-26'
  description: 'Claude Code — v2.1.84: Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS`
    env vars to override effort/thinking capability detection for pinned default models
    for 3p (Bedrock, Vertex, Foundry), and `_MODEL_NAME`/`_DESCRIPTION` to customize
    the `/model` picker label'
  evidence:
  - quote: Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS` env vars to
      override effort/thinking capability detection for pinned default models for
      3p (Bedrock, Vertex, Foundry), and `_MODEL_NAME`/`_DESCRIPTION` to customize
      the `/model` picker label
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef
  source_release: claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa
  source_type: github_releases
  theme: model-support
  theme_matches:
  - matched_terms:
    - model
    - models
    - opus
    - sonnet
    score: 200
    theme: model-support
  - matched_terms:
    - picker
    score: 50
    theme: interface-experience
  theme_resolution: manual-semantic-rule-v2
  title: Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS` env vars to
    override…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-17-increased-default-maximum-output-token-limits-for-claude-opus-4-6-to-64k-tokens|Increased
  default maximum output token limits for Claude Opus 4.6 to 64k tokens…]]'
- '[[Changes/ChatGPT/2026-03-18-we-re-rolling-out-gpt-5-4-mini-in-chatgpt-gpt-5-4-mini-is-available-to-free-and|GPT-5.4
  mini in ChatGPT]]'
- '[[Changes/Claude Code/2026-03-19-added-effort-frontmatter-support-for-skills-and-slash-commands-to-override-the-m|Added
  effort frontmatter support for skills and slash commands to override…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa]]'
source_type: github_releases
theme: model-support
title: Added ANTHROPIC_DEFAULT{OPUS,SONNET,HAIKU}MODEL_SUPPORTS env vars to override…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS` env vars to override…

**Claude Code** · 2026-03-26 · [[Themes/model-support|Model Support]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.84) · from [[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|v2.1.84]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS` env vars to override effort/thinking capability detection for pinned default models for 3p (Bedrock, Vertex, Foundry), and `_MODEL_NAME`/`_DESCRIPTION` to customize the `/model` picker label
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-26-fixed-the-allow-claude-to-edit-its-own-settings-for-this-session-permission-opti|Fixed the "allow Claude to edit its own settings for this session" permission option…]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-26-2-reliability-and-performance-changes-in-v2-1-84|2 Reliability and Performance changes in v2.1.84]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-26-added-allowedchannelplugins-managed-setting-for-team-enterprise-admins-to-define|Added allowedChannelPlugins managed setting for team/enterprise admins to define…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-03-26-5-apps-and-integrations-changes-in-v2-1-84|5 Apps and Integrations changes in v2.1.84]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-26-slash-commands-unavailable-for-the-current-auth-setup-voice-mobile-chrome-upgrad|Slash commands unavailable for the current auth setup…]] · Voice and Audio
- [[Changes/Claude Code/2026-03-26-added-powershell-tool-for-windows-as-an-opt-in-preview-learn-more-at-https-code|Added PowerShell tool for Windows as an opt-in preview]] · Mobile and Desktop
- [[Changes/Claude Code/2026-03-26-2-agent-mode-changes-in-v2-1-84|2 Agent Mode changes in v2.1.84]] · Agent Mode
- [[Changes/Claude Code/2026-03-26-2-context-window-changes-in-v2-1-84|2 Context Window changes in v2.1.84]] · Context Window
- [[Changes/Claude Code/2026-03-26-5-developer-workflow-changes-in-v2-1-84|5 Developer Workflow changes in v2.1.84]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-03-19 · Claude Code · [[Changes/Claude Code/2026-03-19-added-effort-frontmatter-support-for-skills-and-slash-commands-to-override-the-m|Added effort frontmatter support for skills and slash commands to override…]]
- Later: 2026-04-01 · Claude Code · [[Changes/Claude Code/2026-04-01-usage-now-hides-redundant-current-week-sonnet-only-bar-for-pro-and-enterprise-pl|/usage now hides redundant "Current week (Sonnet only)" bar for Pro and Enterprise plans]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-26-3c8e42&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-26-added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef.md%0ACard%20ID%3A%20claude-code-2026-03-26-3c8e42%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.84%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->