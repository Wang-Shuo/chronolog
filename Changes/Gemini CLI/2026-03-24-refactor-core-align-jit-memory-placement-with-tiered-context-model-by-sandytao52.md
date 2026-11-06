---
card_id: gemini-cli-2026-03-24-119a21
date: '2026-03-24'
description: 'Gemini CLI · 2026-03-24 · Memory and Personalization: refactor(core):
  align JIT memory placement with tiered context model by @SandyTao520 in…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 978
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: cf34b5d5ce88bd0018870f62bfffa116a509353717191822dc30eaba814b872e
product: gemini-cli
product_name: Gemini CLI
record:
  ai_generated: true
  card_id: gemini-cli-2026-03-24-119a21
  comparison: ''
  confidence: low
  date: '2026-03-24'
  description: 'Gemini CLI — Release v0.35.0: refactor(core): align JIT memory placement
    with tiered context model by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/22766'
  evidence:
  - quote: 'refactor(core): align JIT memory placement with tiered context model by
      @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/22766'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: gemini-cli
  product_name: Gemini CLI
  slug: refactor-core-align-jit-memory-placement-with-tiered-context-model-by-sandytao52
  source_release: gemini-cli-2026-03-24-v0-35-0-github-300868580-f6f9b621
  source_type: github_releases
  theme: memory
  theme_matches:
  - matched_terms:
    - memory
    score: 110
    theme: memory
  - matched_terms:
    - context
    score: 50
    theme: context-window
  - matched_terms:
    - model
    score: 50
    theme: model-support
  title: 'refactor(core): align JIT memory placement with tiered context model'
  type: change
related_changes:
- '[[Changes/Dify/2026-03-17-4-memory-and-personalization-changes-in-1-13-1|4 Memory
  and Personalization changes in 1.13.1]]'
- '[[Changes/Gemini CLI/2026-03-17-docs-document-tool-exclusion-from-memory-via-deny-policy-by-abhijit-2592-in-http|docs:
  document tool exclusion from memory via deny policy]]'
- '[[Changes/Codex CLI/2026-03-19-4-memory-and-personalization-changes-in-rust-v0-116-0|4
  Memory and Personalization changes in rust-v0.116.0]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-03-24-v0-35-0-github-300868580-f6f9b621|gemini-cli-2026-03-24-v0-35-0-github-300868580-f6f9b621]]'
source_type: github_releases
theme: memory
title: 'refactor(core): align JIT memory placement with tiered context model'
type: change
---

<!-- chronolog:begin region="header" -->
# refactor(core): align JIT memory placement with tiered context model

**Gemini CLI** · 2026-03-24 · [[Themes/memory|Memory and Personalization]] · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0) · from [[Releases/Gemini CLI/gemini-cli-2026-03-24-v0-35-0-github-300868580-f6f9b621|Release v0.35.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> refactor(core): align JIT memory placement with tiered context model by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/22766
>
> Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-03-24-docs-cli-add-custom-keybinding-documentation-by-scidomino-in-https-github-com-go|docs(cli): add custom keybinding documentation]] · Interface Experience
- [[Changes/Gemini CLI/2026-03-24-docs-document-npm-deprecation-warnings-as-safe-to-ignore-by-h30s-in-https-github|docs: document npm deprecation warnings as safe to ignore]] · Files and Data
- [[Changes/Gemini CLI/2026-03-24-2-context-window-changes-in-v0-35-0|2 Context Window changes in v0.35.0]] · Context Window
- [[Changes/Gemini CLI/2026-03-24-10-agent-mode-changes-in-v0-35-0|10 Agent Mode changes in v0.35.0]] · Agent Mode
- [[Changes/Gemini CLI/2026-03-24-feat-skills-improve-async-pr-review-workflow-and-logging-by-mattkorwel-in-https|feat(skills): improve async-pr-review workflow and logging]] · Developer Workflow
- [[Changes/Gemini CLI/2026-03-24-5-apps-and-integrations-changes-in-v0-35-0|5 Apps and Integrations changes in v0.35.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-03-24-docs-core-add-authentication-guide-for-remote-subagents-by-adamfweidman-in-https|docs(core): add authentication guide for remote subagents]] · Account and Access
- [[Changes/Gemini CLI/2026-03-24-7-model-support-changes-in-v0-35-0|7 Model Support changes in v0.35.0]] · Model Support
- [[Changes/Gemini CLI/2026-03-24-feat-telemetry-add-clearcut-instrumentation-for-ai-credits-billing-events-by-gsq|feat(telemetry): add Clearcut instrumentation for AI credits billing events]] · Pricing Model
- [[Changes/Gemini CLI/2026-03-24-2-automation-and-scheduling-changes-in-v0-35-0|2 Automation and Scheduling changes in v0.35.0]] · Automation and Scheduling
- [[Changes/Gemini CLI/2026-03-24-5-safety-and-privacy-changes-in-v0-35-0|5 Safety and Privacy changes in v0.35.0]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-03-24-58-other-changes-in-v0-35-0|58 other changes in v0.35.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-03-19 · Codex CLI · [[Changes/Codex CLI/2026-03-19-4-memory-and-personalization-changes-in-rust-v0-116-0|4 Memory and Personalization changes in rust-v0.116.0]]
- Later: 2026-03-25 · Open WebUI · [[Changes/Open WebUI/2026-03-25-4-memory-and-personalization-changes-in-v0-8-11|4 Memory and Personalization changes in v0.8.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-03-24-119a21&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-03-24-refactor-core-align-jit-memory-placement-with-tiered-context-model-by-sandytao52.md%0ACard%20ID%3A%20gemini-cli-2026-03-24-119a21%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.35.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->