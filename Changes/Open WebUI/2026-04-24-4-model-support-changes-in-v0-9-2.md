---
card_id: open-webui-2026-04-24-0c5a5c
date: '2026-04-24'
description: 'Open WebUI · 2026-04-24 · Model Support: 4 changes in v0.9.2 — ⏰ **Calendar
  event reminder customization.** Calendar events now support a configurable…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1201
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cf99fdeee1c7b85772228600e4c383263d34db8de8d066a0f20cfd0b63673e69
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-24-0c5a5c
  comparison: ''
  date: '2026-04-24'
  description: 'Open WebUI — v0.9.2: 4 Model Support changes'
  evidence:
  - quote: ⏰ **Calendar event reminder customization.** Calendar events now support
      a configurable `reminder_minutes` parameter, allowing models to set custom reminder
      durations instead of the default 10-minute notification.
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: ⚡ **Model avatar cache reuse.** Default model profile images now redirect
      to a shared static path instead of reading files from disk per-request, reducing
      repeated I/O and improving loading efficiency when multiple models use the fallback
      icon. [#24015](https://github.com/open-webui/open-webui/pull/24015)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F9E0 **Persistent chat skill injection.** Skills mentioned in persisted
      chats now inject into the system prompt reliably. Skill ID extraction from `<$skillId|label>`
      message tags is now handled server-side, and tags are stripped before messages
      reach the model."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F512 **Model profile image path safety.** Model profile image endpoints
      now validate and sanitize static asset redirect paths, preventing path traversal
      through encoded dots or malicious URL patterns."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-model-support-changes-in-v0-9-2
  source_release: open-webui-2026-04-24-v0-9-2-github-313142735-f0842502
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in v0.9.2
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-04-24-claude-opus-4-6-now-uses-medium-reasoning-effort-by-default|Claude
  Opus 4.6 now uses medium reasoning effort by default]]'
- '[[Changes/Lovable/2026-04-24-opus-4-7|Opus 4.7]]'
- '[[Changes/Lovable/2026-04-24-knowledge-and-content-app-connectors-fireflies-gemini-enterprise-wordpress|Knowledge
  and content app connectors: Fireflies, Gemini Enterprise, WordPress]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-24-v0-9-2-github-313142735-f0842502|open-webui-2026-04-24-v0-9-2-github-313142735-f0842502]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in v0.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v0.9.2

**Open WebUI** · 2026-04-24 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.2) · from [[Releases/Open WebUI/open-webui-2026-04-24-v0-9-2-github-313142735-f0842502|v0.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ⏰ **Calendar event reminder customization.** Calendar events now support a configurable `reminder_minutes` parameter, allowing models to set custom reminder durations instead of the default 10-minute notification.

> ⚡ **Model avatar cache reuse.** Default model profile images now redirect to a shared static path instead of reading files from disk per-request, reducing repeated I/O and improving loading efficiency when multiple models use the fallback icon. [#24015](https://github.com/open-webui/open-webui/pull/24015)

> 🧠 **Persistent chat skill injection.** Skills mentioned in persisted chats now inject into the system prompt reliably. Skill ID extraction from `<$skillId|label>` message tags is now handled server-side, and tags are stripped before messages reach the model.

> 🔒 **Model profile image path safety.** Model profile image endpoints now validate and sanitize static asset redirect paths, preventing path traversal through encoded dots or malicious URL patterns.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-24-2-memory-and-personalization-changes-in-v0-9-2|2 Memory and Personalization changes in v0.9.2]] · Memory and Personalization
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
## Nearby in Model Support

- Earlier: 2026-04-24 · Lovable · [[Changes/Lovable/2026-04-24-knowledge-and-content-app-connectors-fireflies-gemini-enterprise-wordpress|Knowledge and content app connectors: Fireflies, Gemini Enterprise, WordPress]]
- Later: 2026-04-24 · OpenCode · [[Changes/OpenCode/2026-04-24-2-model-support-changes-in-v1-14-24-1|2 Model Support changes in v1.14.24 + 1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-24-0c5a5c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-24-4-model-support-changes-in-v0-9-2.md%0ACard%20ID%3A%20open-webui-2026-04-24-0c5a5c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->