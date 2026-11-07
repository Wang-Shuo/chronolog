---
card_id: open-webui-2026-03-09-eb869e
date: '2026-03-09'
description: "Open WebUI · 2026-03-09 · Model Support: 3 changes in v0.8.10 — \U0001F4DD
  **Task message truncation.** Chat messages sent to task models for title and tag
  generation…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1155
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 22ce542bd82f05ed2e564acf88a6e824cc4f5e1baadd833931f8ab353973ce8b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-09-eb869e
  comparison: ''
  date: '2026-03-09'
  description: 'Open WebUI — v0.8.10: 3 Model Support changes'
  evidence:
  - quote: "\U0001F4DD **Task message truncation.** Chat messages sent to task models
      for title and tag generation can now be truncated using a filter in the prompt
      template, reducing token usage and processing time for long conversations. [#21499](https://github.com/open-webui/open-webui/issues/21499)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  - quote: "\U0001F6E0️ **Internal tool method filtering.** Tools no longer expose
      internal methods starting with underscore to the LLM, reducing clutter and improving
      accuracy. [#22408](https://github.com/open-webui/open-webui/pull/22408)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  - quote: "\U0001F504 **Custom model fallback.** Fixed custom model fallback not
      working when the base model is unavailable; the base model ID is now correctly
      retrieved from model info instead of empty params. [#22456](https://github.com/open-webui/open-webui/issues/22456)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-model-support-changes-in-v0-8-10
  source_release: open-webui-2026-03-09-v0-8-10-github-294485945-5852a771
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v0.8.10
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-03-08-9-model-support-changes-in-v0-8-9|9 Model Support
  changes in v0.8.9]]'
- '[[Changes/ElevenLabs/2026-03-09-elevenagents|ElevenAgents]]'
- '[[Changes/Google Antigravity/2026-03-09-added-support-for-reading-rules-from-agents-md-in-addition-to-gemini-md|Added
  support for reading rules from AGENTS.md in addition to GEMINI.md]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-09-v0-8-10-github-294485945-5852a771|open-webui-2026-03-09-v0-8-10-github-294485945-5852a771]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v0.8.10
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v0.8.10

**Open WebUI** · 2026-03-09 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.10) · from [[Releases/Open WebUI/open-webui-2026-03-09-v0-8-10-github-294485945-5852a771|v0.8.10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📝 **Task message truncation.** Chat messages sent to task models for title and tag generation can now be truncated using a filter in the prompt template, reducing token usage and processing time for long conversations. [#21499](https://github.com/open-webui/open-webui/issues/21499)

> 🛠️ **Internal tool method filtering.** Tools no longer expose internal methods starting with underscore to the LLM, reducing clutter and improving accuracy. [#22408](https://github.com/open-webui/open-webui/pull/22408)

> 🔄 **Custom model fallback.** Fixed custom model fallback not working when the base model is unavailable; the base model ID is now correctly retrieved from model info instead of empty params. [#22456](https://github.com/open-webui/open-webui/issues/22456)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-09-teams-webhook-crash-fixed-a-typeerror-crash-in-the-teams-webhook-handler-when-us|📨 Teams webhook crash. Fixed a TypeError crash in the Teams webhook handler…]] · Collaboration
- [[Changes/Open WebUI/2026-03-09-2-search-and-browsing-changes-in-v0-8-10|2 Search and Browsing changes in v0.8.10]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-09-2-developer-workflow-changes-in-v0-8-10|2 Developer Workflow changes in v0.8.10]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-09-2-account-and-access-changes-in-v0-8-10|2 Account and Access changes in v0.8.10]] · Account and Access
- [[Changes/Open WebUI/2026-03-09-azure-speech-transcription-errors-improved-azure-ai-speech-error-handling-to-dis|🎤 Azure speech transcription errors. Improved Azure AI Speech error handling…]] · Voice and Audio
- [[Changes/Open WebUI/2026-03-09-2-reliability-and-performance-changes-in-v0-8-10|2 Reliability and Performance changes in v0.8.10]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-09-12-other-changes-in-v0-8-10|12 other changes in v0.8.10]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-03-09 · Google Antigravity · [[Changes/Google Antigravity/2026-03-09-added-support-for-reading-rules-from-agents-md-in-addition-to-gemini-md|Added support for reading rules from AGENTS.md in addition to GEMINI.md]]
- Later: 2026-03-09 · OpenCode · [[Changes/OpenCode/2026-03-09-disable-fallback-to-free-nano-for-small-model-requests|Disable fallback to free nano for small model requests]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-09-eb869e&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-09-3-model-support-changes-in-v0-8-10.md%0ACard%20ID%3A%20open-webui-2026-03-09-eb869e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.10%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->