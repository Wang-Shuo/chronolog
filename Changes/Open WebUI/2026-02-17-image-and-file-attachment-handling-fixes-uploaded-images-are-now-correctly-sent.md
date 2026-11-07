---
card_id: open-webui-2026-02-17-f24d92
date: '2026-02-17'
description: "Open WebUI · 2026-02-17 · Context Window: \U0001F5BC️ **Image and file
  attachment handling fixes.** Uploaded images are now correctly sent to vision-enabled
  models, and…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1020
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 35fb5cf07b3f8171c69b678733ec8fc5ed4196898553b9eccb7cc4bdbc940033
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-17-f24d92
  comparison: ''
  date: '2026-02-17'
  description: "Open WebUI — v0.8.3: \U0001F5BC️ **Image and file attachment handling
    fixes.** Uploaded images are now correctly sent to vision-enabled models, and
    file attachments now work even when no user text is entered alongside a system
    prompt. This fixes two issues where the backend was not properly processing file
    attachments: images weren't converted to the expected format for API requests,
    and file context was dropped when the user sent only a file without accompanying
    text. [Commit](https://github.com/open-webui/open-webui/commit/f1053d94c7ef7b8b78682dd73586b65a84d202a1),
    [#21477](https://github.com/open-webui/open-webui/issues/21477), [#21457](https://github.com/open-webui/open-webui/issues/21457)"
  evidence:
  - quote: "\U0001F5BC️ **Image and file attachment handling fixes.** Uploaded images
      are now correctly sent to vision-enabled models, and file attachments now work
      even when no user text is entered alongside a system prompt. This fixes two
      issues where the backend was not properly processing file attachments: images
      weren't converted to the expected format for API requests, and file context
      was dropped when the user sent only a file without accompanying text. [Commit](https://github.com/open-webui/open-webui/commit/f1053d94c7ef7b8b78682dd73586b65a84d202a1),
      [#21477](https://github.com/open-webui/open-webui/issues/21477), [#21457](https://github.com/open-webui/open-webui/issues/21457)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.3
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: open-webui
  product_name: Open WebUI
  slug: image-and-file-attachment-handling-fixes-uploaded-images-are-now-correctly-sent
  source_release: open-webui-2026-02-17-v0-8-3-github-287117379-ddae610a
  source_type: github_releases
  theme: context-window
  theme_matches:
  - matched_terms:
    - context
    score: 50
    theme: context-window
  - matched_terms:
    - models
    score: 50
    theme: model-support
  - matched_terms:
    - vision
    score: 50
    theme: multimodal
  theme_resolution: manual-semantic-rule-v1
  title: "\U0001F5BC️ **Image and file attachment handling fixes.** Uploaded images
    are now correctly…"
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-02-14-shell-mode-pastes-raw-text-instead-of-paste-tokens|Shell
  mode pastes raw text instead of paste tokens]]'
- '[[Changes/Codex CLI/2026-02-17-4-context-window-changes-in-rust-v0-102-0|4 Context
  Window changes in rust-v0.102.0]]'
- '[[Changes/Cursor/2026-02-17-agents-can-now-search-past-conversations-and-use-chat-history-as-context|Agents
  can now search past conversations and use chat history as context]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-17-v0-8-3-github-287117379-ddae610a|open-webui-2026-02-17-v0-8-3-github-287117379-ddae610a]]'
source_type: github_releases
theme: context-window
title: "\U0001F5BC️ Image and file attachment handling fixes. Uploaded images are
  now correctly…"
type: change
---

<!-- chronolog:begin region="header" -->
# 🖼️ **Image and file attachment handling fixes.** Uploaded images are now correctly…

**Open WebUI** · 2026-02-17 · [[Themes/context-window|Context Window]] · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.3) · from [[Releases/Open WebUI/open-webui-2026-02-17-v0-8-3-github-287117379-ddae610a|v0.8.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> 🖼️ **Image and file attachment handling fixes.** Uploaded images are now correctly sent to vision-enabled models, and file attachments now work even when no user text is entered alongside a system prompt. This fixes two issues where the backend was not properly processing file attachments: images weren't converted to the expected format for API requests, and file context was dropped when the user sent only a file without accompanying text. [Commit](https://github.com/open-webui/open-webui/commit/f1053d94c7ef7b8b78682dd73586b65a84d202a1), [#21477](https://github.com/open-webui/open-webui/issues/21477), [#21457](https://github.com/open-webui/open-webui/issues/21457)
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-17-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-17-image-edit-api-background-support-the-image-edit-api-now-supports-the-background|🎨 Image edit API background support. The image edit API now supports…]] · Editor Experience
- [[Changes/Open WebUI/2026-02-17-faster-model-filtering-model-access-control-filtering-no-longer-makes-a-redundan|⚡ Faster model filtering. Model access control filtering no longer makes…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-02-17-4-model-support-changes-in-v0-8-3|4 Model Support changes in v0.8.3]] · Model Support
- [[Changes/Open WebUI/2026-02-17-tool-call-display-improvements-tool-call-results-now-display-arguments-in-a-clea|🔧 Tool call display improvements. Tool call results now display arguments…]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-17-3-other-changes-in-v0-8-3|3 other changes in v0.8.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-02-17 · Cursor · [[Changes/Cursor/2026-02-17-agents-can-now-search-past-conversations-and-use-chat-history-as-context|Agents can now search past conversations and use chat history as context]]
- Later: 2026-02-18 · Codex CLI · [[Changes/Codex CLI/2026-02-18-2-context-window-changes-in-rust-v0-104-0|2 Context Window changes in rust-v0.104.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-17-f24d92&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-17-image-and-file-attachment-handling-fixes-uploaded-images-are-now-correctly-sent.md%0ACard%20ID%3A%20open-webui-2026-02-17-f24d92%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->