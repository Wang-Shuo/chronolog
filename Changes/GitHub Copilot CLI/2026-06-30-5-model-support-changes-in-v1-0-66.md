---
card_id: github-copilot-cli-2026-06-30-fcbe82
date: '2026-06-30'
description: 'GitHub Copilot CLI · 2026-06-30 · Model Support: 5 changes in 1.0.66
  — Add support for Claude Opus 4.8 Fast and deprecate Claude Opus 4.6 Fast'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1268
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ee3fc20c7b8f9e8aecd3d571299895e2664ea1c9f6cce56eea48972a4f205c97
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-30-fcbe82
  comparison: ''
  date: '2026-06-30'
  description: 'GitHub Copilot CLI — 1.0.66: 5 Model Support changes'
  evidence:
  - quote: Add support for Claude Opus 4.8 Fast and deprecate Claude Opus 4.6 Fast
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Render the timeline as a compact "highlight reel" with single-line tool
      and reasoning rows for all users
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Prevent duplicate final assistant messages for GPT models
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Show accurate Anthropic reasoning token counts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: BYOK sessions using Anthropic models no longer hit HTTP 400 errors from
      adaptive-thinking mismatches — neither from injecting adaptive thinking on models
      that don't support it, nor from sending standard thinking to models that require
      adaptive. Thinking-mode selection for dual-mode models is unchanged.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 5-model-support-changes-in-v1-0-66
  source_release: github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in v1.0.66
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-30-introducing-claude-sonnet-5-now-the-default-model-in-claude-code-with-a-native-1|Introducing
  Claude Sonnet 5]]'
- '[[Changes/Cline/2026-06-30-add-support-for-claude-sonnet-5-across-the-anthropic-bedrock-vertex-claude-code|Add
  support for Claude Sonnet 5 across the Anthropic, Bedrock, Vertex, Claude Code…]]'
- '[[Changes/GitHub Copilot CLI/2026-06-30-add-claude-sonnet-5-as-a-supported-model|Add
  Claude Sonnet 5 as a supported model]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740|github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in v1.0.66
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in v1.0.66

**GitHub Copilot CLI** · 2026-06-30 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.66) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740|1.0.66]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add support for Claude Opus 4.8 Fast and deprecate Claude Opus 4.6 Fast

> Render the timeline as a compact "highlight reel" with single-line tool and reasoning rows for all users

> Prevent duplicate final assistant messages for GPT models

> Show accurate Anthropic reasoning token counts

> BYOK sessions using Anthropic models no longer hit HTTP 400 errors from adaptive-thinking mismatches — neither from injecting adaptive thinking on models that don't support it, nor from sending standard thinking to models that require adaptive. Thinking-mode selection for dual-mode models is unchanged.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.66
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-30-2-editor-experience-changes-in-v1-0-66|2 Editor Experience changes in v1.0.66]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-30-voice-mode-turns-itself-off-when-the-engine-fails-to-start-at-boot|Voice mode turns itself off when the engine fails to start at boot]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-06-30-perform-tokenizer-warmup-in-parallel-on-a-background-thread-for-better-startup-p|Perform tokenizer warmup in parallel on a background thread for better startup performance]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-30-2-collaboration-changes-in-v1-0-66|2 Collaboration changes in v1.0.66]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-06-30-pr-auto-now-starts-a-self-paced-loop-that-fixes-one-thing-per-run-and-paces-itse|/pr auto now starts a self-paced loop that fixes one thing per run and paces itself…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-30-3-interface-experience-changes-in-v1-0-66|3 Interface Experience changes in v1.0.66]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-30-9-apps-and-integrations-changes-in-v1-0-66|9 Apps and Integrations changes in v1.0.66]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-30-match-the-terminal-text-color-to-the-github-theme-canvas|Match the terminal text color to the GitHub theme canvas]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-06-30-21-developer-workflow-changes-in-v1-0-66|21 Developer Workflow changes in v1.0.66]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-30-6-account-and-access-changes-in-v1-0-66|6 Account and Access changes in v1.0.66]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-30-configure-subagent-concurrency-and-depth-limits-in-settings-usage-based-billing|Configure subagent concurrency and depth limits in /settings (usage-based billing users)]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-06-30-2-mobile-and-desktop-changes-in-v1-0-66|2 Mobile and Desktop changes in v1.0.66]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-06-30-3-safety-and-privacy-changes-in-v1-0-66|3 Safety and Privacy changes in v1.0.66]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-30-recover-corrupted-session-history-on-load|Recover corrupted session history on load]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-06-30-8-agent-mode-changes-in-v1-0-66|8 Agent Mode changes in v1.0.66]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-30-keep-session-store-searches-and-context-lookups-responsive|Keep session-store searches and context lookups responsive]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-06-30-33-other-changes-in-v1-0-66|33 other changes in v1.0.66]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-add-claude-sonnet-5-as-a-supported-model|Add Claude Sonnet 5 as a supported model]]
- Later: 2026-06-30 · Ollama · [[Changes/Ollama/2026-06-30-tightened-gemma-4-moe-model-loading-in-the-mlx-engine|Tightened Gemma 4 MoE model loading in the MLX engine]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-30-fcbe82&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-30-5-model-support-changes-in-v1-0-66.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-30-fcbe82%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.66%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->