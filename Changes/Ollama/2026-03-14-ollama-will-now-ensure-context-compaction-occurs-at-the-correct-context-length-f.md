---
card_id: ollama-2026-03-14-647c43
date: '2026-03-14'
description: 'Ollama · 2026-03-14 · Context Window: Ollama will now ensure context
  compaction occurs at the correct context length for each model when using `ollama
  launch…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1045
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 4aa013a443de779e172c332662bf9c1c1c3cfee2a039e34b8849eefc67858901
product: ollama
product_name: Ollama
record:
  ai_generated: true
  card_id: ollama-2026-03-14-647c43
  comparison: ''
  confidence: low
  date: '2026-03-14'
  description: 'Ollama — v0.18.0: Ollama will now ensure context compaction occurs
    at the correct context length for each model when using `ollama launch claude`'
  evidence:
  - quote: Ollama will now ensure context compaction occurs at the correct context
      length for each model when using `ollama launch claude`
    source_release: https://github.com/ollama/ollama/releases/tag/v0.18.0
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: ollama
  product_name: Ollama
  slug: ollama-will-now-ensure-context-compaction-occurs-at-the-correct-context-length-f
  source_release: ollama-2026-03-14-v0-18-0-github-296861801-d01e9dff
  source_type: github_releases
  theme: context-window
  theme_matches:
  - matched_terms:
    - context
    - context length
    score: 110
    theme: context-window
  - matched_terms:
    - model
    score: 50
    theme: model-support
  title: Ollama will now ensure context compaction occurs at the correct context length…
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-03-11-status-line-context-window-percentage-no-longer-inflates-across-turns-by-using-t|Status
  line context window percentage no longer inflates across turns by using…]]'
- '[[Changes/GitHub Copilot CLI/2026-03-13-add-precompact-hook-to-run-commands-before-context-compaction-starts|Add
  preCompact hook to run commands before context compaction starts]]'
- '[[Changes/Claude Code/2026-03-14-added-postcompact-hook-that-fires-after-compaction-completes|Added
  PostCompact hook that fires after compaction completes]]'
source_release: '[[Releases/Ollama/ollama-2026-03-14-v0-18-0-github-296861801-d01e9dff|ollama-2026-03-14-v0-18-0-github-296861801-d01e9dff]]'
source_type: github_releases
theme: context-window
title: Ollama will now ensure context compaction occurs at the correct context length…
type: change
---

<!-- chronolog:begin region="header" -->
# Ollama will now ensure context compaction occurs at the correct context length…

**Ollama** · 2026-03-14 · [[Themes/context-window|Context Window]] · [Official source](https://github.com/ollama/ollama/releases/tag/v0.18.0) · from [[Releases/Ollama/ollama-2026-03-14-v0-18-0-github-296861801-d01e9dff|v0.18.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Ollama will now ensure context compaction occurs at the correct context length for each model when using `ollama launch claude`
>
> Source: https://github.com/ollama/ollama/releases/tag/v0.18.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2026-03-14-3-model-support-changes-in-v0-18-0|3 Model Support changes in v0.18.0]] · Model Support
- [[Changes/Ollama/2026-03-14-ollama-can-now-be-selected-as-an-authentication-and-model-provider-during-opencl|Ollama can now be selected as an authentication and model provider during OpenClaw…]] · Account and Access
- [[Changes/Ollama/2026-03-14-or-using-openclaw-s-onboarding|Or using OpenClaw’s onboarding]] · Interface Experience
- [[Changes/Ollama/2026-03-14-4-reliability-and-performance-changes-in-v0-18-0|4 Reliability and Performance changes in v0.18.0]] · Reliability and Performance
- [[Changes/Ollama/2026-03-14-7-other-changes-in-v0-18-0|7 other changes in v0.18.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-03-14 · Claude Code · [[Changes/Claude Code/2026-03-14-added-postcompact-hook-that-fires-after-compaction-completes|Added PostCompact hook that fires after compaction completes]]
- Later: 2026-03-16 · Codex CLI · [[Changes/Codex CLI/2026-03-16-2-context-window-changes-in-rust-v0-115-0|2 Context Window changes in rust-v0.115.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2026-03-14-647c43&body=Card%3A%20Changes%2FOllama%2F2026-03-14-ollama-will-now-ensure-context-compaction-occurs-at-the-correct-context-length-f.md%0ACard%20ID%3A%20ollama-2026-03-14-647c43%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.18.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->