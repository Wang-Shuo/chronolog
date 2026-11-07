---
card_id: ollama-2024-01-20-b3fa91
date: '2024-01-20'
description: 'Ollama · 2024-01-20 · Reliability and Performance: 2 changes in v0.1.21
  — Ollama now supports CPUs without AVX. This means Ollama will now run on older
  CPUs…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1888
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 13ebf8d6ea005ebbc25fcd2db21c6a58eebdd0d27bb93280c96d77ad16d543f6
product: ollama
product_name: Ollama
record:
  card_id: ollama-2024-01-20-b3fa91
  comparison: ''
  date: '2024-01-20'
  description: 'Ollama — v0.1.21: 2 Reliability and Performance changes'
  evidence:
  - quote: Ollama now supports CPUs without AVX. This means Ollama will now run on
      older CPUs and in environments (such as virtual machines, Rosetta, GitHub actions)
      that don't provide support for AVX instructions. For newer CPUs that support
      AVX2, Ollama will receive a small performance boost, running models about 10%
      faster.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.21
  - quote: Ollama will now use AVX2 for faster performance if available
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.21
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 2-reliability-and-performance-changes-in-v0-1-21
  source_release: ollama-2024-01-20-v0-1-21-github-137801319-d665d0af
  source_type: github_releases
  theme: reliability-performance
  title: 2 Reliability and Performance changes in v0.1.21
  type: change
related_changes:
- '[[Changes/Superwhisper/2024-01-12-2-reliability-and-performance-changes-in-superwhisper-macos-1-22-1|2
  Reliability and Performance changes in Superwhisper macOS 1.22.1]]'
- '[[Changes/Superwhisper/2024-01-12-performance-improvements-to-ui-and-model-running|Performance
  improvements to UI and model running]]'
- '[[Changes/Superwhisper/2024-01-13-2-reliability-and-performance-changes-in-superwhisper-macos-1-22-2|2
  Reliability and Performance changes in Superwhisper macOS 1.22.2]]'
source_release: '[[Releases/Ollama/ollama-2024-01-20-v0-1-21-github-137801319-d665d0af|ollama-2024-01-20-v0-1-21-github-137801319-d665d0af]]'
source_type: github_releases
theme: reliability-performance
title: 2 Reliability and Performance changes in v0.1.21
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Reliability and Performance changes in v0.1.21

**Ollama** · 2024-01-20 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.1.21) · from [[Releases/Ollama/ollama-2024-01-20-v0-1-21-github-137801319-d665d0af|v0.1.21]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Ollama now supports CPUs without AVX. This means Ollama will now run on older CPUs and in environments (such as virtual machines, Rosetta, GitHub actions) that don't provide support for AVX instructions. For newer CPUs that support AVX2, Ollama will receive a small performance boost, running models about 10% faster.

> Ollama will now use AVX2 for faster performance if available

Source: https://github.com/ollama/ollama/releases/tag/v0.1.21
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2024-01-20-2-developer-workflow-changes-in-v0-1-21|2 Developer Workflow changes in v0.1.21]] · Developer Workflow
- [[Changes/Ollama/2024-01-20-8-model-support-changes-in-v0-1-21|8 Model Support changes in v0.1.21]] · Model Support
- [[Changes/Ollama/2024-01-20-2-other-changes-in-v0-1-21|2 other changes in v0.1.21]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2024-01-13 · Superwhisper · [[Changes/Superwhisper/2024-01-13-2-reliability-and-performance-changes-in-superwhisper-macos-1-22-2|2 Reliability and Performance changes in Superwhisper macOS 1.22.2]]
- Later: 2024-01-24 · Raycast · [[Changes/Raycast/2024-01-24-application-uninstaller-uninstalling-big-applications-is-now-much-faster-and-you|Application Uninstaller: Uninstalling big applications is now much faster and you…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2024-01-20-b3fa91&body=Card%3A%20Changes%2FOllama%2F2024-01-20-2-reliability-and-performance-changes-in-v0-1-21.md%0ACard%20ID%3A%20ollama-2024-01-20-b3fa91%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.1.21%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->