---
card_id: open-webui-2026-07-01-a5517a
date: '2026-07-01'
description: "Open WebUI · 2026-07-01 · Developer Workflow: 5 changes in v0.10.2 —
  \U0001F5C2️ **Folder uploads to knowledge bases.** Dragging a folder into a knowledge
  base, or…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1201
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: be169f378aa40f8a2215f5962e13ebe9a1b6ecd98f783ae7c2569f0f4907f70b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-01-a5517a
  comparison: ''
  date: '2026-07-01'
  description: 'Open WebUI — v0.10.2: 5 Developer Workflow changes'
  evidence:
  - quote: "\U0001F5C2️ **Folder uploads to knowledge bases.** Dragging a folder into
      a knowledge base, or syncing one, now recreates its subfolder structure instead
      of flattening everything into loose files. [#26130](https://github.com/open-webui/open-webui/issues/26130),
      [Commit](https://github.com/open-webui/open-webui/commit/2ed8934f5b2bc8a11c74ef2f34cdb62ef024809e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
  - quote: "\U0001F9F0 **API configs via environment.** Administrators can now set
      per-connection Ollama and OpenAI API configurations through the \"OLLAMA_API_CONFIGS\"
      and \"OPENAI_API_CONFIGS\" environment variables. [Commit](https://github.com/open-webui/open-webui/commit/19d8f03bd2c64013b510f2a0eeb3513d452814a3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
  - quote: "\U0001F4E1 **Provider failure events.** Failed Ollama and OpenAI-compatible
      provider requests now emit a structured event describing the error type, provider,
      and status, giving administrators clearer visibility into upstream failures.
      [Commit](https://github.com/open-webui/open-webui/commit/4351c78b1e45bb0c5824f9d9eb911b395e343646)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
  - quote: ⏳ **Tool dialogs no longer hang.** Dismissing a tool or function input
      dialog by clicking outside it now cancels the pending request instead of leaving
      the chat spinning indefinitely. [#26417](https://github.com/open-webui/open-webui/issues/26417),
      [Commit](https://github.com/open-webui/open-webui/commit/0016266c0652757e32aa44f2e1fb7311ac08db51)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
  - quote: "\U0001F4BE **Banner and config startup.** Setting configuration such as
      \"WEBUI_BANNERS\" no longer causes a startup failure, since admin configuration
      values are now stored correctly regardless of their data type. [#26431](https://github.com/open-webui/open-webui/issues/26431),
      [Commit](https://github.com/open-webui/open-webui/commit/ab22fe64bdd10ba86845dcd46dfd7f619b22366f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-developer-workflow-changes-in-v0-10-2
  source_release: open-webui-2026-07-01-v0-10-2-github-347327188-9065e44f
  source_type: github_releases
  theme: developer-workflow
  title: 5 Developer Workflow changes in v0.10.2
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-06-30-21-developer-workflow-changes-in-v1-0-66|21
  Developer Workflow changes in v1.0.66]]'
- '[[Changes/Claude Code/2026-07-01-background-agents-launched-from-claude-agents-now-commit-push-and-open-a-draft-p|Background
  agents launched from claude agents now commit, push, and open a draft…]]'
- '[[Changes/GitHub Copilot CLI/2026-07-01-6-developer-workflow-changes-in-v1-0-68|6
  Developer Workflow changes in v1.0.68]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-01-v0-10-2-github-347327188-9065e44f|open-webui-2026-07-01-v0-10-2-github-347327188-9065e44f]]'
source_type: github_releases
theme: developer-workflow
title: 5 Developer Workflow changes in v0.10.2
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Developer Workflow changes in v0.10.2

**Open WebUI** · 2026-07-01 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.2) · from [[Releases/Open WebUI/open-webui-2026-07-01-v0-10-2-github-347327188-9065e44f|v0.10.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗂️ **Folder uploads to knowledge bases.** Dragging a folder into a knowledge base, or syncing one, now recreates its subfolder structure instead of flattening everything into loose files. [#26130](https://github.com/open-webui/open-webui/issues/26130), [Commit](https://github.com/open-webui/open-webui/commit/2ed8934f5b2bc8a11c74ef2f34cdb62ef024809e)

> 🧰 **API configs via environment.** Administrators can now set per-connection Ollama and OpenAI API configurations through the "OLLAMA_API_CONFIGS" and "OPENAI_API_CONFIGS" environment variables. [Commit](https://github.com/open-webui/open-webui/commit/19d8f03bd2c64013b510f2a0eeb3513d452814a3)

> 📡 **Provider failure events.** Failed Ollama and OpenAI-compatible provider requests now emit a structured event describing the error type, provider, and status, giving administrators clearer visibility into upstream failures. [Commit](https://github.com/open-webui/open-webui/commit/4351c78b1e45bb0c5824f9d9eb911b395e343646)

> ⏳ **Tool dialogs no longer hang.** Dismissing a tool or function input dialog by clicking outside it now cancels the pending request instead of leaving the chat spinning indefinitely. [#26417](https://github.com/open-webui/open-webui/issues/26417), [Commit](https://github.com/open-webui/open-webui/commit/0016266c0652757e32aa44f2e1fb7311ac08db51)

> 💾 **Banner and config startup.** Setting configuration such as "WEBUI_BANNERS" no longer causes a startup failure, since admin configuration values are now stored correctly regardless of their data type. [#26431](https://github.com/open-webui/open-webui/issues/26431), [Commit](https://github.com/open-webui/open-webui/commit/ab22fe64bdd10ba86845dcd46dfd7f619b22366f)

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
- [[Changes/Open WebUI/2026-07-01-2-editor-experience-changes-in-v0-10-2|2 Editor Experience changes in v0.10.2]] · Editor Experience
- [[Changes/Open WebUI/2026-07-01-2-account-and-access-changes-in-v0-10-2|2 Account and Access changes in v0.10.2]] · Account and Access
- [[Changes/Open WebUI/2026-07-01-3-safety-and-privacy-changes-in-v0-10-2|3 Safety and Privacy changes in v0.10.2]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-01-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-07-01-2-other-changes-in-v0-10-2|2 other changes in v0.10.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-07-01 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-01-6-developer-workflow-changes-in-v1-0-68|6 Developer Workflow changes in v1.0.68]]
- Later: 2026-07-02 · Claude Code · [[Changes/Claude Code/2026-07-02-claude-agents-session-rows-now-show-pull-request-links-as-bare-n-without-the-red|claude agents session rows now show pull-request links as bare ♯N without…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-01-a5517a&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-01-5-developer-workflow-changes-in-v0-10-2.md%0ACard%20ID%3A%20open-webui-2026-07-01-a5517a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->