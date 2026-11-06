---
card_id: open-webui-2026-04-24-4da418
date: '2026-04-24'
description: "Open WebUI · 2026-04-24 · Context Window: 3 changes in v0.9.2 — \U0001F510
  **Session token resolution.** Session user endpoints now gracefully handle missing…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1086
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5369e4099153377271ddceb2c1456a5327c4d2349395adc5eb61698a0e0bad05
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-24-4da418
  comparison: ''
  date: '2026-04-24'
  description: 'Open WebUI — v0.9.2: 3 Context Window changes'
  evidence:
  - quote: "\U0001F510 **Session token resolution.** Session user endpoints now gracefully
      handle missing `Authorization` headers by falling back to cookie and request
      state tokens, preventing errors when used behind forward-auth proxies."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F4CA **RAG template validation UI.** The Documents settings page
      now displays a warning when RAG templates contain multiple `[context]` or `{{CONTEXT}}`
      placeholders, helping administrators avoid accidental redundant context injection."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F504 **Ollama and OpenAI metadata forwarding.** Ollama and OpenAI
      proxy routes now forward request metadata to downstream handlers, ensuring consistent
      context propagation."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-context-window-changes-in-v0-9-2
  source_release: open-webui-2026-04-24-v0-9-2-github-313142735-f0842502
  source_type: github_releases
  theme: context-window
  title: 3 Context Window changes in v0.9.2
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-04-23-2-context-window-changes-in-v1-0-35|2 Context
  Window changes in v1.0.35]]'
- '[[Changes/Codex CLI/2026-04-24-2-context-window-changes-in-rust-v0-125-0|2 Context
  Window changes in rust-v0.125.0]]'
- '[[Changes/Lovable/2026-04-24-chat-history-search|Chat history search]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-24-v0-9-2-github-313142735-f0842502|open-webui-2026-04-24-v0-9-2-github-313142735-f0842502]]'
source_type: github_releases
theme: context-window
title: 3 Context Window changes in v0.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Context Window changes in v0.9.2

**Open WebUI** · 2026-04-24 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.2) · from [[Releases/Open WebUI/open-webui-2026-04-24-v0-9-2-github-313142735-f0842502|v0.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔐 **Session token resolution.** Session user endpoints now gracefully handle missing `Authorization` headers by falling back to cookie and request state tokens, preventing errors when used behind forward-auth proxies.

> 📊 **RAG template validation UI.** The Documents settings page now displays a warning when RAG templates contain multiple `[context]` or `{{CONTEXT}}` placeholders, helping administrators avoid accidental redundant context injection.

> 🔄 **Ollama and OpenAI metadata forwarding.** Ollama and OpenAI proxy routes now forward request metadata to downstream handlers, ensuring consistent context propagation.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-24-2-memory-and-personalization-changes-in-v0-9-2|2 Memory and Personalization changes in v0.9.2]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-24-4-model-support-changes-in-v0-9-2|4 Model Support changes in v0.9.2]] · Model Support
- [[Changes/Open WebUI/2026-04-24-automation-model-detection-the-create-automation-tool-now-correctly-detects-the|🧩 Automation model detection. The create_automation tool now correctly detects…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-24-3-reliability-and-performance-changes-in-v0-9-2|3 Reliability and Performance changes in v0.9.2]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-24-2-apps-and-integrations-changes-in-v0-9-2|2 Apps and Integrations changes in v0.9.2]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-24-2-editor-experience-changes-in-v0-9-2|2 Editor Experience changes in v0.9.2]] · Editor Experience
- [[Changes/Open WebUI/2026-04-24-3-account-and-access-changes-in-v0-9-2|3 Account and Access changes in v0.9.2]] · Account and Access
- [[Changes/Open WebUI/2026-04-24-paddleocr-vl-document-extraction-administrators-can-now-use-paddleocr-vl-as-a-co|🧠 PaddleOCR-vl document extraction. Administrators can now use PaddleOCR-vl…]] · Files and Data
- [[Changes/Open WebUI/2026-04-24-13-other-changes-in-v0-9-2|13 other changes in v0.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-04-24 · Lovable · [[Changes/Lovable/2026-04-24-chat-history-search|Chat history search]]
- Later: 2026-04-28 · Claude Code · [[Changes/Claude Code/2026-04-28-vscode-context-now-opens-a-native-token-usage-dialog|VSCode /context now opens a native token usage dialog]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-24-4da418&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-24-3-context-window-changes-in-v0-9-2.md%0ACard%20ID%3A%20open-webui-2026-04-24-4da418%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->