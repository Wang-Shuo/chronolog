---
card_id: open-webui-2026-10-14-c193f5
date: '2026-10-14'
description: "Open WebUI · 2026-10-14 · Model Support: 4 changes in v0.12.2 — \U0001F4D1
  **MinerU 4.x servers.** The MinerU document engine now works with self-hosted MinerU
  4.x…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1374
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fe8bc16dc64f2e1ae5b833da6564bf58ac71f0f85eb444acbadd643f93190da6
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-14-c193f5
  comparison: ''
  date: '2026-10-14'
  description: 'Open WebUI — v0.12.2: 4 Model Support changes'
  evidence:
  - quote: "\U0001F4D1 **MinerU 4.x servers.** The MinerU document engine now works
      with self-hosted MinerU 4.x servers, where every document failed with a 404
      because 4.x removed the old parsing interface; 3.x servers work as before, 4.x
      servers take a tier (flash, basic, standard or advanced) and enable_ocr in the
      MinerU parameters while language and model_version stay 3.x only, and images
      that 4.x returns inside the document text are left out of the indexed content.
      [#32422](https://github.com/open-webui/open-webui/pull/32422), [Commit](https://github.com/open-webui/open-webui/commit/81f5b8adf80e49bd2213390b59dc867074c3738e),
      [#31516](https://github.com/open-webui/open-webui/issues/31516)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
  - quote: "\U0001F3F7️ **Model ID in custom headers.** Custom headers on connections
      and tool servers can now use {{MODEL_ID}}, which holds the ID of the model handling
      the chat request, the workspace model's own ID for a workspace model and each
      model's own ID in a multi-model chat, so downstream services can route or log
      usage per model. [#32426](https://github.com/open-webui/open-webui/pull/32426),
      [Commit](https://github.com/open-webui/open-webui/commit/bae22752d3995f573a373ee1ae4735b746d952a9),
      [#30006](https://github.com/open-webui/open-webui/issues/30006)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
  - quote: "\U0001F9ED **call_tool for Tool Search.** With Tool Search on, the model
      now gets a new call_tool tool and runs a tool it found with search_tools through
      it, passing the tool's name and its arguments, instead of calling the deferred
      tool directly by a name that is not in the request's tool list, which strict
      providers rejected; approvals and other tool behavior stay the same. [Commit](https://github.com/open-webui/open-webui/commit/7b47c3b22ce983d57f4a13073748a935c4614889),
      [#32243](https://github.com/open-webui/open-webui/issues/32243)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
  - quote: "\U0001F50F **Channel message metadata kept server side.** Channel messages
      posted or edited through the API no longer take their metadata from the request,
      so a user can no longer make a message appear to come from a channel webhook
      or a model. [#32421](https://github.com/open-webui/open-webui/pull/32421), [Commit](https://github.com/open-webui/open-webui/commit/44953df70ed758a6321f7a2e139c93aca29129f1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-model-support-changes-in-v0-12-2
  source_release: open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in v0.12.2
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-14-add-support-for-gemini-4-argon|Add support
  for Gemini 4 Argon]]'
- '[[Changes/Ollama/2026-10-14-decision-models-are-now-available-on-cloud-use-clef-cloud-and-clef-flash-cloud-t|Decision
  models are now available on cloud]]'
- '[[Changes/Open WebUI/2026-10-14-9-model-support-changes-in-v0-12-1|9 Model Support
  changes in v0.12.1]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d|open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in v0.12.2
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v0.12.2

**Open WebUI** · 2026-10-14 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.2) · from [[Releases/Open WebUI/open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d|v0.12.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📑 **MinerU 4.x servers.** The MinerU document engine now works with self-hosted MinerU 4.x servers, where every document failed with a 404 because 4.x removed the old parsing interface; 3.x servers work as before, 4.x servers take a tier (flash, basic, standard or advanced) and enable_ocr in the MinerU parameters while language and model_version stay 3.x only, and images that 4.x returns inside the document text are left out of the indexed content. [#32422](https://github.com/open-webui/open-webui/pull/32422), [Commit](https://github.com/open-webui/open-webui/commit/81f5b8adf80e49bd2213390b59dc867074c3738e), [#31516](https://github.com/open-webui/open-webui/issues/31516)

> 🏷️ **Model ID in custom headers.** Custom headers on connections and tool servers can now use {{MODEL_ID}}, which holds the ID of the model handling the chat request, the workspace model's own ID for a workspace model and each model's own ID in a multi-model chat, so downstream services can route or log usage per model. [#32426](https://github.com/open-webui/open-webui/pull/32426), [Commit](https://github.com/open-webui/open-webui/commit/bae22752d3995f573a373ee1ae4735b746d952a9), [#30006](https://github.com/open-webui/open-webui/issues/30006)

> 🧭 **call_tool for Tool Search.** With Tool Search on, the model now gets a new call_tool tool and runs a tool it found with search_tools through it, passing the tool's name and its arguments, instead of calling the deferred tool directly by a name that is not in the request's tool list, which strict providers rejected; approvals and other tool behavior stay the same. [Commit](https://github.com/open-webui/open-webui/commit/7b47c3b22ce983d57f4a13073748a935c4614889), [#32243](https://github.com/open-webui/open-webui/issues/32243)

> 🔏 **Channel message metadata kept server side.** Channel messages posted or edited through the API no longer take their metadata from the request, so a user can no longer make a message appear to come from a channel webhook or a model. [#32421](https://github.com/open-webui/open-webui/pull/32421), [Commit](https://github.com/open-webui/open-webui/commit/44953df70ed758a6321f7a2e139c93aca29129f1)

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
- [[Changes/Open WebUI/2026-10-14-scim-cannot-delete-admins-an-identity-provider-can-no-longer-delete-administrato|👮 SCIM cannot delete admins. An identity provider can no longer delete…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-14-2-interface-experience-changes-in-v0-12-2|2 Interface Experience changes in v0.12.2]] · Interface Experience
- [[Changes/Open WebUI/2026-10-14-memory-reindex-rate-limits-reindexing-memories-from-the-admin-reindex-knowledge|🧮 Memory reindex rate limits. Reindexing memories, from the admin Reindex…]] · Memory and Personalization
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-14 · Open WebUI · [[Changes/Open WebUI/2026-10-14-9-model-support-changes-in-v0-12-1|9 Model Support changes in v0.12.1]]
- Later: 2026-10-15 · Codex CLI · [[Changes/Codex CLI/2026-10-15-6-model-support-changes-in-rust-v0-163-0|6 Model Support changes in rust-v0.163.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-14-c193f5&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-14-4-model-support-changes-in-v0-12-2.md%0ACard%20ID%3A%20open-webui-2026-10-14-c193f5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->