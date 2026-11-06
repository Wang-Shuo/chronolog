---
card_id: cline-2026-09-24-e1a905
date: '2026-09-24'
description: 'Cline · 2026-09-24 · Context Window: Long replies on local models (llama.cpp,
  Ollama, LM Studio) that hit the output-token limit now compact the conversation…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1239
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 5fc364546f891c49c30d6d1901cdc6d63b625e1c38fe1a92b7b80f906688eee3
product: cline
product_name: Cline
record:
  card_id: cline-2026-09-24-e1a905
  comparison: ''
  date: '2026-09-24'
  description: 'Cline — v4.1.21: Long replies on local models (llama.cpp, Ollama,
    LM Studio) that hit the output-token limit now compact the conversation and retry
    once instead of ending the task. These servers cap generation at whatever context
    is left, regardless of the output budget you set. If compaction cannot help, the
    existing concise-retry recovery still runs, and the partial answer is kept.'
  evidence:
  - quote: Long replies on local models (llama.cpp, Ollama, LM Studio) that hit the
      output-token limit now compact the conversation and retry once instead of ending
      the task. These servers cap generation at whatever context is left, regardless
      of the output budget you set. If compaction cannot help, the existing concise-retry
      recovery still runs, and the partial answer is kept.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.21
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: cline
  product_name: Cline
  slug: long-replies-on-local-models-llama-cpp-ollama-lm-studio-that-hit-the-output-toke
  source_release: cline-2026-09-24-v4-1-21-github-395862160-2e42664e
  source_type: github_releases
  theme: context-window
  theme_matches:
  - matched_terms:
    - context
    score: 50
    theme: context-window
  - matched_terms:
    - models
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: Long replies on local models (llama.cpp, Ollama, LM Studio) that hit…
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-09-21-3-context-window-changes-in-v0-11-4|3 Context Window
  changes in v0.11.4]]'
- '[[Changes/Cline/2026-09-22-2-context-window-changes-in-v4-1-20|2 Context Window
  changes in v4.1.20]]'
- '[[Changes/Codex CLI/2026-09-22-17-context-window-changes-in-rust-v0-156-0|17 Context
  Window changes in rust-v0.156.0]]'
source_release: '[[Releases/Cline/cline-2026-09-24-v4-1-21-github-395862160-2e42664e|cline-2026-09-24-v4-1-21-github-395862160-2e42664e]]'
source_type: github_releases
theme: context-window
title: Long replies on local models (llama.cpp, Ollama, LM Studio) that hit…
type: change
---

<!-- chronolog:begin region="header" -->
# Long replies on local models (llama.cpp, Ollama, LM Studio) that hit…

**Cline** · 2026-09-24 · [[Themes/context-window|Context Window]] · [Official source](https://github.com/cline/cline/releases/tag/v4.1.21) · from [[Releases/Cline/cline-2026-09-24-v4-1-21-github-395862160-2e42664e|v4.1.21]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Long replies on local models (llama.cpp, Ollama, LM Studio) that hit the output-token limit now compact the conversation and retry once instead of ending the task. These servers cap generation at whatever context is left, regardless of the output budget you set. If compaction cannot help, the existing concise-retry recovery still runs, and the partial answer is kept.
>
> Source: https://github.com/cline/cline/releases/tag/v4.1.21
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-09-24-a-command-that-prints-nothing-no-longer-shows-a-raw-json-blob-like-query-git-add|A command that prints nothing no longer shows a raw JSON blob like…]] · Developer Workflow
- [[Changes/Cline/2026-09-24-3-model-support-changes-in-v4-1-21|3 Model Support changes in v4.1.21]] · Model Support
- [[Changes/Cline/2026-09-24-on-windows-mention-search-results-now-show-the-right-file-names-nested-files-suc|On Windows, @-mention search results now show the right file names]] · Search and Browsing
- [[Changes/Cline/2026-09-24-raised-the-minimum-js-yaml-version-to-4-3-2-to-pick-up-a-security-fix-in-the-par|Raised the minimum js-yaml version to 4.3.2 to pick up a security fix in the parser…]] · Safety and Privacy
- [[Changes/Cline/2026-09-24-reopening-a-task-that-failed-now-shows-the-error-with-the-retry-option-instead-o|Reopening a task that failed now shows the error with the retry option, instead…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-22 · Codex CLI · [[Changes/Codex CLI/2026-09-22-17-context-window-changes-in-rust-v0-156-0|17 Context Window changes in rust-v0.156.0]]
- Later: 2026-09-25 · Claude Code · [[Changes/Claude Code/2026-09-25-2-context-window-changes-in-v2-1-283|2 Context Window changes in v2.1.283]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-09-24-e1a905&body=Card%3A%20Changes%2FCline%2F2026-09-24-long-replies-on-local-models-llama-cpp-ollama-lm-studio-that-hit-the-output-toke.md%0ACard%20ID%3A%20cline-2026-09-24-e1a905%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.21%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->