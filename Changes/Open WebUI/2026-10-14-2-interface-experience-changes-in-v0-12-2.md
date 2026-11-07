---
card_id: open-webui-2026-10-14-da873f
date: '2026-10-14'
description: "Open WebUI · 2026-10-14 · Interface Experience: 2 changes in v0.12.2
  — \U0001F9FE **Requested model in the audit log.** Audit log entries for chat and
  completion…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1374
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 62d38447225aa00718cb877b752832a1289e2a9629abad32d6d6fda303efd1eb
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-14-da873f
  comparison: ''
  date: '2026-10-14'
  description: 'Open WebUI — v0.12.2: 2 Interface Experience changes'
  evidence:
  - quote: "\U0001F9FE **Requested model in the audit log.** Audit log entries for
      chat and completion requests, including the OpenAI, Ollama and Anthropic compatible
      endpoints, now carry a model_id field with the model the client asked for at
      every AUDIT_LOG_LEVEL, where the model only appeared in the request body and
      went missing when MAX_BODY_LOG_SIZE cut a long prompt; other requests log it
      as null. [#32429](https://github.com/open-webui/open-webui/pull/32429), [Commit](https://github.com/open-webui/open-webui/commit/fb3d92a6ef56b5a8a6820f615f6e6294c44eaad7),
      [#30097](https://github.com/open-webui/open-webui/issues/30097)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
  - quote: "\U0001F5C2️ **Sidebar hover previews.** Moving the pointer from one sidebar
      folder to the next no longer leaves the first folder's preview open or keeps
      the next one from opening, and folder and chat previews now also open when the
      pointer rests on the padding around a name. [#32438](https://github.com/open-webui/open-webui/pull/32438),
      [Commit](https://github.com/open-webui/open-webui/commit/5e2748a03edd2459d07fcfea168daf740092bf94),
      [#32437](https://github.com/open-webui/open-webui/issues/32437)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-interface-experience-changes-in-v0-12-2
  source_release: open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d
  source_type: github_releases
  theme: interface-experience
  title: 2 Interface Experience changes in v0.12.2
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-14-vscode-improved-startup-the-model-picker-and-slash-command-menu-now-fill-in-righ|VSCode
  Improved startup]]'
- '[[Changes/Lovable/2026-10-14-restore-a-deleted-project-yourself|Restore a deleted
  project yourself]]'
- '[[Changes/Open WebUI/2026-10-14-7-interface-experience-changes-in-v0-12-1|7 Interface
  Experience changes in v0.12.1]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d|open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d]]'
source_type: github_releases
theme: interface-experience
title: 2 Interface Experience changes in v0.12.2
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Interface Experience changes in v0.12.2

**Open WebUI** · 2026-10-14 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.2) · from [[Releases/Open WebUI/open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d|v0.12.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧾 **Requested model in the audit log.** Audit log entries for chat and completion requests, including the OpenAI, Ollama and Anthropic compatible endpoints, now carry a model_id field with the model the client asked for at every AUDIT_LOG_LEVEL, where the model only appeared in the request body and went missing when MAX_BODY_LOG_SIZE cut a long prompt; other requests log it as null. [#32429](https://github.com/open-webui/open-webui/pull/32429), [Commit](https://github.com/open-webui/open-webui/commit/fb3d92a6ef56b5a8a6820f615f6e6294c44eaad7), [#30097](https://github.com/open-webui/open-webui/issues/30097)

> 🗂️ **Sidebar hover previews.** Moving the pointer from one sidebar folder to the next no longer leaves the first folder's preview open or keeps the next one from opening, and folder and chat previews now also open when the pointer rests on the padding around a name. [#32438](https://github.com/open-webui/open-webui/pull/32438), [Commit](https://github.com/open-webui/open-webui/commit/5e2748a03edd2459d07fcfea168daf740092bf94), [#32437](https://github.com/open-webui/open-webui/issues/32437)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-14-open-attached-knowledge-from-its-preview-clicking-the-name-in-the-preview-of-an|📚 Open attached knowledge from its preview. Clicking the name in the preview…]] · Editor Experience
- [[Changes/Open WebUI/2026-10-14-6-developer-workflow-changes-in-v0-12-2|6 Developer Workflow changes in v0.12.2]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-14-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-14-automation-run-results-an-automation-run-is-now-recorded-as-successful-only-afte|⏰ Automation run results. An automation run is now recorded as successful only…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-14-voice-on-android-chrome-voice-calls-and-dictation-on-android-chrome-no-longer-go|📱 Voice on Android Chrome. Voice calls and dictation on Android Chrome no longer…]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-14-per-chat-terminal-file-actions-with-the-open-terminal-chat-context-set-to-per-ch|🖥️ Per chat terminal file actions. With the Open Terminal chat context set…]] · Context Window
- [[Changes/Open WebUI/2026-10-14-4-model-support-changes-in-v0-12-2|4 Model Support changes in v0.12.2]] · Model Support
- [[Changes/Open WebUI/2026-10-14-scim-cannot-delete-admins-an-identity-provider-can-no-longer-delete-administrato|👮 SCIM cannot delete admins. An identity provider can no longer delete…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-14-memory-reindex-rate-limits-reindexing-memories-from-the-admin-reindex-knowledge|🧮 Memory reindex rate limits. Reindexing memories, from the admin Reindex…]] · Memory and Personalization
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-10-14 · Open WebUI · [[Changes/Open WebUI/2026-10-14-7-interface-experience-changes-in-v0-12-1|7 Interface Experience changes in v0.12.1]]
- Later: 2026-10-15 · Claude Code · [[Changes/Claude Code/2026-10-15-2-interface-experience-changes-in-v2-1-301|2 Interface Experience changes in v2.1.301]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-14-da873f&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-14-2-interface-experience-changes-in-v0-12-2.md%0ACard%20ID%3A%20open-webui-2026-10-14-da873f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->