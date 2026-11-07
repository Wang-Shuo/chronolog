---
card_id: open-webui-2026-04-24-06d175
date: '2026-04-24'
description: "Open WebUI · 2026-04-24 · Memory and Personalization: 2 changes in v0.9.2
  — \U0001F9F5 **Streaming markdown performance stability.** Streaming responses now
  stay more…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1009
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f98df34dd304aba6871c87e74e955934bd433ead1f12d29d638185c8b1fb08fc
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-24-06d175
  comparison: ''
  date: '2026-04-24'
  description: 'Open WebUI — v0.9.2: 2 Memory and Personalization changes'
  evidence:
  - quote: "\U0001F9F5 **Streaming markdown performance stability.** Streaming responses
      now stay more memory-efficient by preventing repeated cleanup callback registration
      during markdown updates. [#24048](https://github.com/open-webui/open-webui/pull/24048)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F9F9 **Browser-native message virtualization.** The custom JavaScript-based
      message culling system (spacers, height caching, scroll listeners) was replaced
      with CSS `content-visibility: auto`, letting the browser natively skip rendering
      of off-screen messages without destroying component trees. This eliminates scroll
      jump artifacts and mount/destroy thrashing while preserving memory efficiency
      in long conversations."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-memory-and-personalization-changes-in-v0-9-2
  source_release: open-webui-2026-04-24-v0-9-2-github-313142735-f0842502
  source_type: github_releases
  theme: memory
  title: 2 Memory and Personalization changes in v0.9.2
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-04-23-4-memory-and-personalization-changes-in-v0-39-0|4
  Memory and Personalization changes in v0.39.0]]'
- '[[Changes/Cline/2026-04-24-improve-cline-core-memory-diagnostics-used-by-the-extension-runtime|Improve
  cline-core memory diagnostics used by the extension runtime]]'
- '[[Changes/GitHub Copilot CLI/2026-04-24-custom-instruction-files-in-gitignored-directories-e-g-github-instructions-now-l|Custom
  instruction files in .gitignored directories (e.g., .github/instructions/)…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-24-v0-9-2-github-313142735-f0842502|open-webui-2026-04-24-v0-9-2-github-313142735-f0842502]]'
source_type: github_releases
theme: memory
title: 2 Memory and Personalization changes in v0.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Memory and Personalization changes in v0.9.2

**Open WebUI** · 2026-04-24 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.2) · from [[Releases/Open WebUI/open-webui-2026-04-24-v0-9-2-github-313142735-f0842502|v0.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧵 **Streaming markdown performance stability.** Streaming responses now stay more memory-efficient by preventing repeated cleanup callback registration during markdown updates. [#24048](https://github.com/open-webui/open-webui/pull/24048)

> 🧹 **Browser-native message virtualization.** The custom JavaScript-based message culling system (spacers, height caching, scroll listeners) was replaced with CSS `content-visibility: auto`, letting the browser natively skip rendering of off-screen messages without destroying component trees. This eliminates scroll jump artifacts and mount/destroy thrashing while preserving memory efficiency in long conversations.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-24-4-model-support-changes-in-v0-9-2|4 Model Support changes in v0.9.2]] · Model Support
- [[Changes/Open WebUI/2026-04-24-automation-model-detection-the-create-automation-tool-now-correctly-detects-the|🧩 Automation model detection. The create_automation tool now correctly detects…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-24-3-reliability-and-performance-changes-in-v0-9-2|3 Reliability and Performance changes in v0.9.2]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-24-3-context-window-changes-in-v0-9-2|3 Context Window changes in v0.9.2]] · Context Window
- [[Changes/Open WebUI/2026-04-24-2-apps-and-integrations-changes-in-v0-9-2|2 Apps and Integrations changes in v0.9.2]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-24-2-editor-experience-changes-in-v0-9-2|2 Editor Experience changes in v0.9.2]] · Editor Experience
- [[Changes/Open WebUI/2026-04-24-3-account-and-access-changes-in-v0-9-2|3 Account and Access changes in v0.9.2]] · Account and Access
- [[Changes/Open WebUI/2026-04-24-paddleocr-vl-document-extraction-administrators-can-now-use-paddleocr-vl-as-a-co|🧠 PaddleOCR-vl document extraction. Administrators can now use PaddleOCR-vl…]] · Files and Data
- [[Changes/Open WebUI/2026-04-24-13-other-changes-in-v0-9-2|13 other changes in v0.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-04-24 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-24-custom-instruction-files-in-gitignored-directories-e-g-github-instructions-now-l|Custom instruction files in .gitignored directories (e.g., .github/instructions/)…]]
- Later: 2026-04-28 · Gemini CLI · [[Changes/Gemini CLI/2026-04-28-refactor-memory-replace-memorymanageragent-with-prompt-driven-memory-editing-acr|refactor(memory): replace MemoryManagerAgent with prompt-driven memory editing…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-24-06d175&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-24-2-memory-and-personalization-changes-in-v0-9-2.md%0ACard%20ID%3A%20open-webui-2026-04-24-06d175%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->