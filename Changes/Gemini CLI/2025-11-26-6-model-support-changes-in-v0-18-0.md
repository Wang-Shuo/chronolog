---
card_id: gemini-cli-2025-11-26-fa45ef
date: '2025-11-26'
description: 'Gemini CLI · 2025-11-26 · Model Support: 6 changes in Release v0.18.0
  — feat: update thinking mode support to exclude gemini-2.0 models and simplify logic.
  by…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1052
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ecf6d6b1d642e0ab0dd343c0fe65a43c6354002811046520430876f8aae83f3c
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2025-11-26-fa45ef
  comparison: ''
  date: '2025-11-26'
  description: 'Gemini CLI — Release v0.18.0: 6 Model Support changes'
  evidence:
  - quote: 'feat: update thinking mode support to exclude gemini-2.0 models and simplify
      logic. by @kevin-ramdass in https://github.com/google-gemini/gemini-cli/pull/13454'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.18.0
  - quote: 'feat(core): Wire up chat code path for model configs. by @joshualitt in
      https://github.com/google-gemini/gemini-cli/pull/12850'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.18.0
  - quote: 'feat(core): Fix bug with incorrect model overriding. by @joshualitt in
      https://github.com/google-gemini/gemini-cli/pull/13477'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.18.0
  - quote: 'Revert "feat(core): Fix bug with incorrect model overriding." by @adamfweidman
      in https://github.com/google-gemini/gemini-cli/pull/13483'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.18.0
  - quote: 'feat(core): Use thinking level for Gemini 3 by @joshualitt in https://github.com/google-gemini/gemini-cli/pull/13445'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.18.0
  - quote: 'feat(core): Incorporate Gemini 3 into model config hierarchy. by @joshualitt
      in https://github.com/google-gemini/gemini-cli/pull/13447'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.18.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 6-model-support-changes-in-v0-18-0
  source_release: gemini-cli-2025-11-26-v0-18-0-github-265323405-bd13d891
  source_type: github_releases
  theme: model-support
  title: 6 Model Support changes in v0.18.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2025-11-24-opus-4-5-gpt-4-1-and-gpt-5-mini-are-now-available-in-github-copilot-cli|Opus
  4.5, GPT-4.1 and GPT-5-Mini are now available in GitHub Copilot CLI]]'
- '[[Changes/Windsurf/2025-11-24-1-12-36-claude-opus-4-5-changelog-banner|1.12.36
  Claude Opus 4.5 changelog banner]]'
- '[[Changes/Windsurf/2025-11-24-claude-opus-4-5|Claude Opus 4.5]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2025-11-26-v0-18-0-github-265323405-bd13d891|gemini-cli-2025-11-26-v0-18-0-github-265323405-bd13d891]]'
source_type: github_releases
theme: model-support
title: 6 Model Support changes in v0.18.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in v0.18.0

**Gemini CLI** · 2025-11-26 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.18.0) · from [[Releases/Gemini CLI/gemini-cli-2025-11-26-v0-18-0-github-265323405-bd13d891|Release v0.18.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> feat: update thinking mode support to exclude gemini-2.0 models and simplify logic. by @kevin-ramdass in https://github.com/google-gemini/gemini-cli/pull/13454

> feat(core): Wire up chat code path for model configs. by @joshualitt in https://github.com/google-gemini/gemini-cli/pull/12850

> feat(core): Fix bug with incorrect model overriding. by @joshualitt in https://github.com/google-gemini/gemini-cli/pull/13477

> Revert "feat(core): Fix bug with incorrect model overriding." by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/13483

> feat(core): Use thinking level for Gemini 3 by @joshualitt in https://github.com/google-gemini/gemini-cli/pull/13445

> feat(core): Incorporate Gemini 3 into model config hierarchy. by @joshualitt in https://github.com/google-gemini/gemini-cli/pull/13447

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.18.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2025-11-26-feat-add-click-to-focus-support-for-interactive-shell-by-galz10-in-https-github|feat: add click-to-focus support for interactive shell]] · Developer Workflow
- [[Changes/Gemini CLI/2025-11-26-feat-zed-integration-use-default-model-routing-for-zed-integration-by-benbrandt|feat(zed-integration): Use default model routing for Zed integration]] · Apps and Integrations
- [[Changes/Gemini CLI/2025-11-26-restore-keyboard-mode-when-exiting-the-editor-by-scidomino-in-https-github-com-g|Restore keyboard mode when exiting the editor]] · Editor Experience
- [[Changes/Gemini CLI/2025-11-26-improve-pty-resize-error-handling-for-windows-by-galz10-in-https-github-com-goog|Improve pty resize error handling for Windows]] · Mobile and Desktop
- [[Changes/Gemini CLI/2025-11-26-protect-stdout-and-stderr-so-javascript-code-can-t-accidentally-write-to-stdout|Protect stdout and stderr so JavaScript code can't accidentally write to stdout…]] · Interface Experience
- [[Changes/Gemini CLI/2025-11-26-22-other-changes-in-v0-18-0|22 other changes in v0.18.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-11-24 · Windsurf · [[Changes/Windsurf/2025-11-24-claude-opus-4-5|Claude Opus 4.5]]
- Later: 2025-11-27 · Cline · [[Changes/Cline/2025-11-27-12-model-support-changes-in-v3-38-3|12 Model Support changes in v3.38.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2025-11-26-fa45ef&body=Card%3A%20Changes%2FGemini%20CLI%2F2025-11-26-6-model-support-changes-in-v0-18-0.md%0ACard%20ID%3A%20gemini-cli-2025-11-26-fa45ef%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.18.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->