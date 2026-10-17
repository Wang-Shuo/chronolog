---
card_id: claude-code-2026-04-16-0e5221
date: '2026-04-16'
description: 'Claude Code · 2026-04-16 · Model Support: 3 changes in v2.1.111 — Claude
  Opus 4.7 xhigh is now available! Use /effort to tune speed vs. intelligence'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1193
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 57f2ddf52188120598c660855d022185bb70b606d17cb41fb7d27f79afe7b165
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-16-0e5221
  comparison: ''
  date: '2026-04-16'
  description: 'Claude Code — v2.1.111: 3 Model Support changes'
  evidence:
  - quote: Claude Opus 4.7 xhigh is now available! Use /effort to tune speed vs. intelligence
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.111
  - quote: Added `xhigh` effort level for Opus 4.7, sitting between `high` and `max`.
      Available via `/effort`, `--effort`, and the model picker; other models fall
      back to `high`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.111
  - quote: Improved `/setup-vertex` and `/setup-bedrock` to show the actual `settings.json`
      path when `CLAUDE_CONFIG_DIR` is set, seed model candidates from existing pins
      on re-run, and offer a "with 1M context" option for supported models
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.111
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-model-support-changes-in-v2-1-111
  source_release: claude-code-2026-04-16-v2-1-111-github-309911692-a3025e78
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v2.1.111
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-04-09-today-we-re-releasing-gpt-5-3-instant-mini-in-chatgpt-it-replaces-gpt-5-instant|GPT-5.3
  Instant mini in ChatGPT]]'
- '[[Changes/Claude Code/2026-04-14-improved-model-to-warn-before-switching-models-mid-conversation-since-the-next-r|Improved
  /model to warn before switching models mid-conversation, since the next…]]'
- '[[Changes/Cursor/2026-04-14-trigger-the-model-picker-from-anywhere-to-switch-models-without-clearing-your-pr|Trigger
  the model picker from anywhere to switch models without clearing your prompt first]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-16-v2-1-111-github-309911692-a3025e78|claude-code-2026-04-16-v2-1-111-github-309911692-a3025e78]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v2.1.111
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v2.1.111

**Claude Code** · 2026-04-16 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.111) · from [[Releases/Claude Code/claude-code-2026-04-16-v2-1-111-github-309911692-a3025e78|v2.1.111]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Claude Opus 4.7 xhigh is now available! Use /effort to tune speed vs. intelligence

> Added `xhigh` effort level for Opus 4.7, sitting between `high` and `max`. Available via `/effort`, `--effort`, and the model picker; other models fall back to `high`

> Improved `/setup-vertex` and `/setup-bedrock` to show the actual `settings.json` path when `CLAUDE_CONFIG_DIR` is set, seed model candidates from existing pins on re-run, and offer a "with 1M context" option for supported models

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.111
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-16-transcript-view-footer-now-shows-dump-to-scrollback-and-v-open-in-editor-shortcu|Transcript view footer now shows  (dump to scrollback) and v (open in editor)…]] · Editor Experience
- [[Changes/Claude Code/2026-04-16-2-apps-and-integrations-changes-in-v2-1-111|2 Apps and Integrations changes in v2.1.111]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-16-auto-mode-is-now-available-for-max-subscribers-when-using-opus-4-7|Auto mode is now available for Max subscribers when using Opus 4.7]] · Model Support
- [[Changes/Claude Code/2026-04-16-windows-powershell-tool-is-progressively-rolling-out-opt-in-or-out-with-claude-c|Windows: PowerShell tool is progressively rolling out]] · Mobile and Desktop
- [[Changes/Claude Code/2026-04-16-3-interface-experience-changes-in-v2-1-111|3 Interface Experience changes in v2.1.111]] · Interface Experience
- [[Changes/Claude Code/2026-04-16-added-less-permission-prompts-skill-scans-transcripts-for-common-read-only-bash|Added /less-permission-prompts skill]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-16-2-developer-workflow-changes-in-v2-1-111|2 Developer Workflow changes in v2.1.111]] · Developer Workflow
- [[Changes/Claude Code/2026-04-16-added-ultrareview-for-running-comprehensive-code-review-in-the-cloud-using-paral|Added /ultrareview for running comprehensive code review in the cloud using…]] · Developer Workflow
- [[Changes/Claude Code/2026-04-16-2-safety-and-privacy-changes-in-v2-1-111|2 Safety and Privacy changes in v2.1.111]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-16-auto-mode-no-longer-requires-enable-auto-mode|Auto mode no longer requires --enable-auto-mode]] · Agent Mode
- [[Changes/Claude Code/2026-04-16-6-other-changes-in-v2-1-111|6 other changes in v2.1.111]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-04-14 · Cursor · [[Changes/Cursor/2026-04-14-trigger-the-model-picker-from-anywhere-to-switch-models-without-clearing-your-pr|Trigger the model picker from anywhere to switch models without clearing your prompt first]]
- Later: 2026-04-22 · Claude Code · [[Changes/Claude Code/2026-04-22-2-model-support-changes-in-v2-1-117|2 Model Support changes in v2.1.117]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-16-0e5221&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-16-3-model-support-changes-in-v2-1-111.md%0ACard%20ID%3A%20claude-code-2026-04-16-0e5221%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.111%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->