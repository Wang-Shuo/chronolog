---
card_id: github-copilot-cli-2026-10-20-71996e
date: '2026-10-20'
description: 'GitHub Copilot CLI · 2026-10-20 · Model Support: 8 changes in 1.0.101
  — Local models and loopback providers in providers.json no longer block Auto, your
  saved…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1380
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6c47485a1787269433f1dbae76c4a7595083a58f9af8c58a42425018339d52ac
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-10-20-71996e
  comparison: ''
  date: '2026-10-20'
  description: 'GitHub Copilot CLI — 1.0.101: 8 Model Support changes'
  evidence:
  - quote: Local models and loopback providers in providers.json no longer block Auto,
      your saved model or the default model when signed in to Copilot
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.101
  - quote: Google models now avoid repeated request rewrites when screenshot-heavy
      sessions exceed image limits, reducing extra token usage.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.101
  - quote: Switching from GPT models to Gemini no longer fails when earlier turns
      include custom tool calls
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.101
  - quote: Google model requests now respect registry image limits to avoid image-count
      request failures
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.101
  - quote: The first prompt no longer hangs silently when no model is selected at
      startup; the CLI now asks you to pick one with /model and keeps your prompt
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.101
  - quote: /usage now shows just the model name for BYOK and other rows without a
      provider label instead of "Unknown provider"
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.101
  - quote: Switching to HydraFusion compacts only when the routed model actually needs
      it
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.101
  - quote: CLI model lists refresh after endpoint updates instead of staying stale
      or empty
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.101
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 8-model-support-changes-in-v1-0-101
  source_release: github-copilot-cli-2026-10-20-v1-0-101-github-418747415-a1bf6298
  source_type: github_releases
  theme: model-support
  title: 8 Model Support changes in v1.0.101
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-19-2-model-support-changes-in-v2-1-304|2 Model Support
  changes in v2.1.304]]'
- '[[Changes/GitHub Copilot CLI/2026-10-19-3-model-support-changes-in-v1-0-100|3 Model
  Support changes in v1.0.100]]'
- "[[Changes/Notion/2026-10-19-meet-auto-our-upgraded-model-router|Meet Auto, our
  upgraded model router \U0001F500]]"
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-10-20-v1-0-101-github-418747415-a1bf6298|github-copilot-cli-2026-10-20-v1-0-101-github-418747415-a1bf6298]]'
source_type: github_releases
theme: model-support
title: 8 Model Support changes in v1.0.101
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Model Support changes in v1.0.101

**GitHub Copilot CLI** · 2026-10-20 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.101) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-10-20-v1-0-101-github-418747415-a1bf6298|1.0.101]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Local models and loopback providers in providers.json no longer block Auto, your saved model or the default model when signed in to Copilot

> Google models now avoid repeated request rewrites when screenshot-heavy sessions exceed image limits, reducing extra token usage.

> Switching from GPT models to Gemini no longer fails when earlier turns include custom tool calls

> Google model requests now respect registry image limits to avoid image-count request failures

> The first prompt no longer hangs silently when no model is selected at startup; the CLI now asks you to pick one with /model and keeps your prompt

> /usage now shows just the model name for BYOK and other rows without a provider label instead of "Unknown provider"

> Switching to HydraFusion compacts only when the routed model actually needs it

> CLI model lists refresh after endpoint updates instead of staying stale or empty

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.101
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-10-20-4-account-and-access-changes-in-v1-0-101|4 Account and Access changes in v1.0.101]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-10-20-2-developer-workflow-changes-in-v1-0-101|2 Developer Workflow changes in v1.0.101]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-10-20-model-picker-marks-your-administrator-managed-model-as-the-default-when-it-is-av|Model picker marks your administrator-managed model as the default when it is available]] · Enterprise and Administration
- [[Changes/GitHub Copilot CLI/2026-10-20-switching-only-reasoning-effort-no-longer-forces-compaction-in-over-budget-sessi|Switching only reasoning effort no longer forces compaction in over-budget sessions]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-10-20-macos-sandboxed-commands-can-connect-directly-to-localhost-tcp-services-when-loc|macOS sandboxed commands can connect directly to localhost TCP services when local…]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-10-20-4-apps-and-integrations-changes-in-v1-0-101|4 Apps and Integrations changes in v1.0.101]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-10-20-permission-approval-prompts-explain-escalation-causes-and-show-a-request-specifi|Permission approval prompts explain escalation causes and show a request-specific…]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-10-20-8-other-changes-in-v1-0-101|8 other changes in v1.0.101]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-19 · Notion · [[Changes/Notion/2026-10-19-meet-auto-our-upgraded-model-router|Meet Auto, our upgraded model router 🔀]]
- Later: 2026-10-20 · Lovable · [[Changes/Lovable/2026-10-20-seedream-5-pro-and-seedance-2-5-for-your-app-s-ai-features|Seedream 5 Pro and Seedance 2.5 for your app's AI features]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-10-20-71996e&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-10-20-8-model-support-changes-in-v1-0-101.md%0ACard%20ID%3A%20github-copilot-cli-2026-10-20-71996e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.101%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->