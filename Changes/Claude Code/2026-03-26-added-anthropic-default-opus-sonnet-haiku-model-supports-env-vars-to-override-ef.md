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
extractor_version: fallback-v4
impact: significant
machine_hash: 49f9d2d71dbc8fda524c932f3f26e54ad9441adca6c2ff913fcf478c008356bb
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
  extractor_version: fallback-v4
  impact: significant
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
- '[[Changes/ChatGPT/2026-03-18-we-re-rolling-out-gpt-5-4-mini-in-chatgpt-gpt-5-4-mini-is-available-to-free-and|ChatGPT
  rolls out GPT-5.4 mini]]'
- '[[Changes/Claude Code/2026-03-19-added-effort-frontmatter-support-for-skills-and-slash-commands-to-override-the-m|Added
  effort frontmatter support for skills and slash commands to override…]]'
- '[[Changes/Cursor/2026-03-25-self-hosted-cloud-agents-offer-the-same-capabilities-as-cursor-hosted-cloud-agen|Self-hosted
  cloud agents offer the same capabilities as Cursor-hosted cloud agents…]]'
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

- [[Changes/Claude Code/2026-03-26-added-claude-stream-idle-timeout-ms-env-var-to-configure-the-streaming-idle-watc|Added CLAUDE_STREAM_IDLE_TIMEOUT_MS env var to configure the streaming idle…]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-26-added-taskcreated-hook-that-fires-when-a-task-is-created-via-taskcreate|Added TaskCreated hook that fires when a task is created via TaskCreate]] · Agent Mode
- [[Changes/Claude Code/2026-03-26-added-powershell-tool-for-windows-as-an-opt-in-preview-learn-more-at-https-code|Added PowerShell tool for Windows as an opt-in preview]] · Mobile and Desktop
- [[Changes/Claude Code/2026-03-26-added-worktreecreate-hook-support-for-type-http-return-the-created-worktree-path|Added WorktreeCreate hook support for type: "http"]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-03-25 · Cursor · [[Changes/Cursor/2026-03-25-self-hosted-cloud-agents-offer-the-same-capabilities-as-cursor-hosted-cloud-agen|Self-hosted cloud agents offer the same capabilities as Cursor-hosted cloud agents…]]
- Later: 2026-04-09 · ChatGPT · [[Changes/ChatGPT/2026-04-09-today-we-re-releasing-gpt-5-3-instant-mini-in-chatgpt-it-replaces-gpt-5-instant|Today, we’re releasing GPT-5.3 Instant Mini in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-26-3c8e42&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-26-added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef.md%0ACard%20ID%3A%20claude-code-2026-03-26-3c8e42%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.84%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->