---
card_id: ollama-2026-02-03-477ad0
date: '2026-02-03'
description: 'Ollama · 2026-02-03 · Context Window: 5 changes in v0.15.5 — Ollama
  will now set context limits for a set of models when using `ollama launch opencode`'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2330
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 44f22fb7a0f1fa42f602313f54a3e4c624cf8772869a9c7745a38f500751c1be
product: ollama
product_name: Ollama
record:
  card_id: ollama-2026-02-03-477ad0
  comparison: ''
  date: '2026-02-03'
  description: 'Ollama — v0.15.5: 5 Context Window changes'
  evidence:
  - quote: Ollama will now set context limits for a set of models when using `ollama
      launch opencode`
    source_release: https://github.com/ollama/ollama/releases/tag/v0.15.5
  - quote: 'Ollama will now default to the following context lengths based on VRAM:'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.15.5
  - quote: '< 24 GiB VRAM: 4,096 context'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.15.5
  - quote: '24-48 GiB VRAM: 32,768 context'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.15.5
  - quote: '&gt;= 48 GiB VRAM: 262,144 context'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.15.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 5-context-window-changes-in-v0-15-5
  source_release: ollama-2026-02-03-v0-15-5-github-282367253-12a5b812
  source_type: github_releases
  theme: context-window
  title: 5 Context Window changes in v0.15.5
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-02-02-2-context-window-changes-in-rust-v0-94-0|2 Context
  Window changes in rust-v0.94.0]]'
- '[[Changes/Claude Code/2026-02-03-added-pages-parameter-to-the-read-tool-for-pdfs-allowing-specific-page-ranges-to|Added
  pages parameter to the Read tool for PDFs, allowing specific page ranges…]]'
- '[[Changes/Dify/2026-02-03-5-context-window-changes-in-1-12-0|5 Context Window changes
  in 1.12.0]]'
source_release: '[[Releases/Ollama/ollama-2026-02-03-v0-15-5-github-282367253-12a5b812|ollama-2026-02-03-v0-15-5-github-282367253-12a5b812]]'
source_type: github_releases
theme: context-window
title: 5 Context Window changes in v0.15.5
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Context Window changes in v0.15.5

**Ollama** · 2026-02-03 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.15.5) · from [[Releases/Ollama/ollama-2026-02-03-v0-15-5-github-282367253-12a5b812|v0.15.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Ollama will now set context limits for a set of models when using `ollama launch opencode`

> Ollama will now default to the following context lengths based on VRAM:

> < 24 GiB VRAM: 4,096 context

> 24-48 GiB VRAM: 32,768 context

> &gt;= 48 GiB VRAM: 262,144 context

Source: https://github.com/ollama/ollama/releases/tag/v0.15.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2026-02-03-sub-agent-support-for-ollama-launch-for-planning-deep-research-and-similar-tasks|Sub-agent support for ollama launch for planning, deep research, and similar tasks]] · Search and Browsing
- [[Changes/Ollama/2026-02-03-qwen3-coder-next-https-ollama-com-library-qwen3-coder-next-a-coding-focused-lang|Qwen3-Coder-Next((source link) a coding-focused…]] · Collaboration
- [[Changes/Ollama/2026-02-03-glm-ocr-https-ollama-com-library-glm-ocr-glm-ocr-is-a-multimodal-ocr-model-for-c|GLM-OCR((source link) GLM-OCR is a multimodal OCR model…]] · Multimodal Input
- [[Changes/Ollama/2026-02-03-ollama-launch-will-now-work-run-subagents-when-using-ollama-launch-claude|ollama launch will now work run subagents when using ollama launch claude]] · Agent Mode
- [[Changes/Ollama/2026-02-03-4-other-changes-in-v0-15-5|4 other changes in v0.15.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-02-03 · Dify · [[Changes/Dify/2026-02-03-5-context-window-changes-in-1-12-0|5 Context Window changes in 1.12.0]]
- Later: 2026-02-04 · Codex CLI · [[Changes/Codex CLI/2026-02-04-2-context-window-changes-in-rust-v0-95-0|2 Context Window changes in rust-v0.95.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2026-02-03-477ad0&body=Card%3A%20Changes%2FOllama%2F2026-02-03-5-context-window-changes-in-v0-15-5.md%0ACard%20ID%3A%20ollama-2026-02-03-477ad0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.15.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->