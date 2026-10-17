---
card_id: claude-code-2026-05-28-982dcf
date: '2026-05-28'
description: 'Claude Code · 2026-05-28 · Model Support: 5 changes in v2.1.154 — Opus
  4.8 is here! Now defaults to high effort · /effort xhigh for your hardest tasks'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1235
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6d4a00fd008cc32e321fc31981a01b01f9b1c0f1f74e3989fe9b1822e04681d2
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-28-982dcf
  comparison: ''
  date: '2026-05-28'
  description: 'Claude Code — v2.1.154: 5 Model Support changes'
  evidence:
  - quote: Opus 4.8 is here! Now defaults to high effort · /effort xhigh for your
      hardest tasks
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
  - quote: 'Fast mode on Opus 4.8 is now available at a fraction of its previous cost:
      2x the standard rate for 2.5x the speed'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
  - quote: The lean system prompt is now the default for all models except Haiku,
      Sonnet, and Opus 4.7 and earlier
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
  - quote: Added Claude Opus 4.8 support and 4.7 → 4.8 migration guidance to the `/claude-api`
      skill
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
  - quote: Deprecated `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE` (will be removed on
      06/01). To use fast mode on Opus 4.6, switch with `/model claude-opus-4-6[1m]`
      and then `/fast on`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-model-support-changes-in-v2-1-154
  source_release: claude-code-2026-05-28-v2-1-154-github-330944050-782cdfc9
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in v2.1.154
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-27-2-model-support-changes-in-v2-1-152|2 Model Support
  changes in v2.1.152]]'
- '[[Changes/ChatGPT/2026-05-28-today-we-re-continuing-to-retire-older-models-with-limited-usage-in-chatgpt-so-w|Retiring
  OpenAI o3 and GPT-4.5]]'
- '[[Changes/ChatGPT/2026-05-28-we-re-updating-gpt-5-5-instant-in-chatgpt-and-the-api-to-improve-response-style|GPT-5.5
  Instant Update]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-28-v2-1-154-github-330944050-782cdfc9|claude-code-2026-05-28-v2-1-154-github-330944050-782cdfc9]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in v2.1.154
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in v2.1.154

**Claude Code** · 2026-05-28 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.154) · from [[Releases/Claude Code/claude-code-2026-05-28-v2-1-154-github-330944050-782cdfc9|v2.1.154]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Opus 4.8 is here! Now defaults to high effort · /effort xhigh for your hardest tasks

> Fast mode on Opus 4.8 is now available at a fraction of its previous cost: 2x the standard rate for 2.5x the speed

> The lean system prompt is now the default for all models except Haiku, Sonnet, and Opus 4.7 and earlier

> Added Claude Opus 4.8 support and 4.7 → 4.8 migration guidance to the `/claude-api` skill

> Deprecated `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE` (will be removed on 06/01). To use fast mode on Opus 4.6, switch with `/model claude-opus-4-6[1m]` and then `/fast on`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-28-remote-control-autocomplete-now-shows-disconnect-remote-control-when-remote-cont|/remote-control autocomplete now shows "Disconnect Remote Control" when Remote…]] · Editor Experience
- [[Changes/Claude Code/2026-05-28-vscode-auto-mode-no-longer-requires-the-bypass-permissions-setting-to-appear-in|VSCode Auto mode no longer requires the bypass-permissions setting to appear…]] · Interface Experience
- [[Changes/Claude Code/2026-05-28-4-agent-mode-changes-in-v2-1-154|4 Agent Mode changes in v2.1.154]] · Agent Mode
- [[Changes/Claude Code/2026-05-28-4-apps-and-integrations-changes-in-v2-1-154|4 Apps and Integrations changes in v2.1.154]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-28-simplify-now-runs-a-cleanup-only-review-reuse-simplification-efficiency-altitude|/simplify now runs a cleanup-only review…]] · Developer Workflow
- [[Changes/Claude Code/2026-05-28-introducing-dynamic-workflows-ask-claude-to-create-a-workflow-and-it-orchestrate|Introducing dynamic workflows]] · Agent Mode
- [[Changes/Claude Code/2026-05-28-claude-now-reserves-the-multiple-choice-question-prompt-for-decisions-it-genuine|Claude now reserves the multiple-choice question prompt for decisions it genuinely…]] · Context Window
- [[Changes/Claude Code/2026-05-28-renamed-the-effort-slider-labels-from-speed-intelligence-to-faster-smarter-for-c|Renamed the /effort slider labels…]] · Reliability and Performance
- [[Changes/Claude Code/2026-05-28-3-other-changes-in-v2-1-154|3 other changes in v2.1.154]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-05-28 · ChatGPT · [[Changes/ChatGPT/2026-05-28-we-re-updating-gpt-5-5-instant-in-chatgpt-and-the-api-to-improve-response-style|GPT-5.5 Instant Update]]
- Later: 2026-05-28 · Claude Code · [[Changes/Claude Code/2026-05-28-model-now-saves-your-selection-as-the-default-for-new-sessions-matching-the-ide|/model now saves your selection as the default for new sessions (matching the IDE)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-28-982dcf&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-28-5-model-support-changes-in-v2-1-154.md%0ACard%20ID%3A%20claude-code-2026-05-28-982dcf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.154%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->