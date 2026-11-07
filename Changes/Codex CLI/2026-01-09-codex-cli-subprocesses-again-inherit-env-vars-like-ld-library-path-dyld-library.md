---
card_id: codex-cli-2026-01-09-630661
date: '2026-01-09'
description: 'Codex CLI · 2026-01-09 · Reliability and Performance: Codex CLI subprocesses
  again inherit env vars like `LD_LIBRARY_PATH`/`DYLD_LIBRARY_PATH` to avoid runtime…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2608
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: aa4ced1de1da81f28f0bf273bd3425af339e93eb495df8459b94af0511e8f2d9
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-09-630661
  comparison: ''
  date: '2026-01-09'
  description: 'Codex CLI — 0.80.0: Codex CLI subprocesses again inherit env vars
    like `LD_LIBRARY_PATH`/`DYLD_LIBRARY_PATH` to avoid runtime issues. As explained
    in #8945, failure to pass along these environment variables to subprocesses that
    expect them (notably GPU-related ones), was causing 10x+ performance regressions!
    Special thanks to @johnzfitch for the detailed investigation and write-up in #8945.
    (#8951)'
  evidence:
  - quote: 'Codex CLI subprocesses again inherit env vars like `LD_LIBRARY_PATH`/`DYLD_LIBRARY_PATH`
      to avoid runtime issues. As explained in #8945, failure to pass along these
      environment variables to subprocesses that expect them (notably GPU-related
      ones), was causing 10x+ performance regressions! Special thanks to @johnzfitch
      for the detailed investigation and write-up in #8945. (#8951)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: codex-cli
  product_name: Codex CLI
  slug: codex-cli-subprocesses-again-inherit-env-vars-like-ld-library-path-dyld-library
  source_release: codex-cli-2026-01-09-rust-v0-80-0-github-275597320-df7b3faf
  source_type: github_releases
  theme: reliability-performance
  title: Codex CLI subprocesses again inherit env vars like…
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-01-06-performance-tuning-for-tuis-cap-redraw-scheduling-and-reduce-unnecessary-rerende|Performance
  tuning for TUIs]]'
- '[[Changes/OpenCode/2026-01-06-3-reliability-and-performance-changes-in-v1-1-4|3
  Reliability and Performance changes in v1.1.4]]'
- '[[Changes/Cursor/2026-01-08-2-reliability-and-performance-changes-in-new-cli-features-and-improved-cli|2
  Reliability and Performance changes in New CLI Features and Improved CLI…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-09-rust-v0-80-0-github-275597320-df7b3faf|codex-cli-2026-01-09-rust-v0-80-0-github-275597320-df7b3faf]]'
source_type: github_releases
theme: reliability-performance
title: Codex CLI subprocesses again inherit env vars like…
type: change
---

<!-- chronolog:begin region="header" -->
# Codex CLI subprocesses again inherit env vars like…

**Codex CLI** · 2026-01-09 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.80.0) · from [[Releases/Codex CLI/codex-cli-2026-01-09-rust-v0-80-0-github-275597320-df7b3faf|0.80.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Codex CLI subprocesses again inherit env vars like `LD_LIBRARY_PATH`/`DYLD_LIBRARY_PATH` to avoid runtime issues. As explained in #8945, failure to pass along these environment variables to subprocesses that expect them (notably GPU-related ones), was causing 10x+ performance regressions! Special thanks to @johnzfitch for the detailed investigation and write-up in #8945. (#8951)
>
> Source: https://github.com/openai/codex/releases/tag/rust-v0.80.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-09-2-apps-and-integrations-changes-in-rust-v0-80-0|2 Apps and Integrations changes in rust-v0.80.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-09-2-agent-mode-changes-in-rust-v0-80-0|2 Agent Mode changes in rust-v0.80.0]] · Agent Mode
- [[Changes/Codex CLI/2026-01-09-8939-chore-move-app-server-tests-from-chat-completion-to-responses-celia-oai|♯8939 chore move app server tests from chat completion to responses @celia-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-01-09-app-server-readme-now-documents-skills-support-and-usage-8853|App-server README now documents skills support and usage]] · Files and Data
- [[Changes/Codex CLI/2026-01-09-4-developer-workflow-changes-in-rust-v0-80-0|4 Developer Workflow changes in rust-v0.80.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-09-2-mobile-and-desktop-changes-in-rust-v0-80-0|2 Mobile and Desktop changes in rust-v0.80.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-09-4-model-support-changes-in-rust-v0-80-0|4 Model Support changes in rust-v0.80.0]] · Model Support
- [[Changes/Codex CLI/2026-01-09-3-interface-experience-changes-in-rust-v0-80-0|3 Interface Experience changes in rust-v0.80.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-09-2-safety-and-privacy-changes-in-rust-v0-80-0|2 Safety and Privacy changes in rust-v0.80.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-09-62-other-changes-in-rust-v0-80-0|62 other changes in rust-v0.80.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-01-08 · Cursor · [[Changes/Cursor/2026-01-08-2-reliability-and-performance-changes-in-new-cli-features-and-improved-cli|2 Reliability and Performance changes in New CLI Features and Improved CLI…]]
- Later: 2026-01-09 · Midjourney · [[Changes/Midjourney/2026-01-09-niji-v7-features-improved-anime-coherence-prompt-understanding-text-rendering-an|Niji V7 features improved anime coherence, prompt understanding, text rendering…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-09-630661&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-09-codex-cli-subprocesses-again-inherit-env-vars-like-ld-library-path-dyld-library.md%0ACard%20ID%3A%20codex-cli-2026-01-09-630661%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.80.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->