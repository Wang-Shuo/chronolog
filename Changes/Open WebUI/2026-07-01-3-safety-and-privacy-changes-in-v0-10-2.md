---
card_id: open-webui-2026-07-01-d2615e
date: '2026-07-01'
description: "Open WebUI · 2026-07-01 · Safety and Privacy: 3 changes in v0.10.2 —
  \U0001F6E1️ **Security Advisory**: This release includes security and access-control
  fixes. We…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1172
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 58557969f402b633f4f99944b2b86a2e03e43243f4dd8b62dbafba873764c238
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-01-d2615e
  comparison: ''
  date: '2026-07-01'
  description: 'Open WebUI — v0.10.2: 3 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F6E1️ **Security Advisory**: This release includes security and
      access-control fixes. We recommend updating production deployments at your earliest
      convenience. Not all security fixes in this version may be enumerated in the
      fixed section — some may be withheld for a short time to give administrators
      time to upgrade. [Advisories](https://github.com/open-webui/open-webui/security)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
  - quote: "\U0001F575️ **Image prompt log privacy.** Image generation workflows are
      no longer written to server logs at the default log level, keeping user-authored
      prompt content out of operator-visible logs. [#26400](https://github.com/open-webui/open-webui/issues/26400),
      [Commit](https://github.com/open-webui/open-webui/commit/64b92ff08a09b1bf338d5d95b7bf6f9db0d7e857)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
  - quote: "\U0001F40D **Reliable code execution loading.** Running Python code in
      chat now loads its runtime reliably, fixing sandbox startup failures that broke
      code execution and the Pyodide file viewer in recent releases. [#26625](https://github.com/open-webui/open-webui/pull/26625),
      [#26390](https://github.com/open-webui/open-webui/issues/26390)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-safety-and-privacy-changes-in-v0-10-2
  source_release: open-webui-2026-07-01-v0-10-2-github-347327188-9065e44f
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v0.10.2
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-06-30-disabling-the-sandbox-for-the-rest-of-the-session-now-takes-effect-immediately-s|Disabling
  the sandbox for the rest of the session now takes effect immediately…]]'
- '[[Changes/GitHub Copilot CLI/2026-06-30-3-safety-and-privacy-changes-in-v1-0-66|3
  Safety and Privacy changes in v1.0.66]]'
- '[[Changes/GitHub Copilot CLI/2026-07-01-4-safety-and-privacy-changes-in-v1-0-68|4
  Safety and Privacy changes in v1.0.68]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-01-v0-10-2-github-347327188-9065e44f|open-webui-2026-07-01-v0-10-2-github-347327188-9065e44f]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v0.10.2
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v0.10.2

**Open WebUI** · 2026-07-01 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.2) · from [[Releases/Open WebUI/open-webui-2026-07-01-v0-10-2-github-347327188-9065e44f|v0.10.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🛡️ **Security Advisory**: This release includes security and access-control fixes. We recommend updating production deployments at your earliest convenience. Not all security fixes in this version may be enumerated in the fixed section — some may be withheld for a short time to give administrators time to upgrade. [Advisories](https://github.com/open-webui/open-webui/security)

> 🕵️ **Image prompt log privacy.** Image generation workflows are no longer written to server logs at the default log level, keeping user-authored prompt content out of operator-visible logs. [#26400](https://github.com/open-webui/open-webui/issues/26400), [Commit](https://github.com/open-webui/open-webui/commit/64b92ff08a09b1bf338d5d95b7bf6f9db0d7e857)

> 🐍 **Reliable code execution loading.** Running Python code in chat now loads its runtime reliably, fixing sandbox startup failures that broke code execution and the Pyodide file viewer in recent releases. [#26625](https://github.com/open-webui/open-webui/pull/26625), [#26390](https://github.com/open-webui/open-webui/issues/26390)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-01-speech-to-text-request-format-openai-compatible-speech-to-text-can-now-send-audi|🎙️ Speech-to-text request format. OpenAI-compatible speech-to-text can now send…]] · Voice and Audio
- [[Changes/Open WebUI/2026-07-01-web-search-domain-filtering-domain-allow-and-block-rules-for-web-search-results|🔒 Web search domain filtering. Domain allow and block rules for web search…]] · Search and Browsing
- [[Changes/Open WebUI/2026-07-01-2-interface-experience-changes-in-v0-10-2|2 Interface Experience changes in v0.10.2]] · Interface Experience
- [[Changes/Open WebUI/2026-07-01-5-model-support-changes-in-v0-10-2|5 Model Support changes in v0.10.2]] · Model Support
- [[Changes/Open WebUI/2026-07-01-2-memory-and-personalization-changes-in-v0-10-2|2 Memory and Personalization changes in v0.10.2]] · Memory and Personalization
- [[Changes/Open WebUI/2026-07-01-models-with-null-capabilities-chatting-with-a-model-whose-capabilities-are-unset|🤖 Models with null capabilities. Chatting with a model whose capabilities…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-01-5-developer-workflow-changes-in-v0-10-2|5 Developer Workflow changes in v0.10.2]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-01-2-editor-experience-changes-in-v0-10-2|2 Editor Experience changes in v0.10.2]] · Editor Experience
- [[Changes/Open WebUI/2026-07-01-2-account-and-access-changes-in-v0-10-2|2 Account and Access changes in v0.10.2]] · Account and Access
- [[Changes/Open WebUI/2026-07-01-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-07-01-2-other-changes-in-v0-10-2|2 other changes in v0.10.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-01 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-01-4-safety-and-privacy-changes-in-v1-0-68|4 Safety and Privacy changes in v1.0.68]]
- Later: 2026-07-03 · Claude Code · [[Changes/Claude Code/2026-07-03-changed-the-default-permission-mode-to-manual-across-the-cli-help-vs-code-and-je|Changed the "default" permission mode to "Manual" across the CLI, --help, VS Code…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-01-d2615e&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-01-3-safety-and-privacy-changes-in-v0-10-2.md%0ACard%20ID%3A%20open-webui-2026-07-01-d2615e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->