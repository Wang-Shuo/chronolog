---
card_id: open-webui-2026-01-09-b98a48
date: '2026-01-09'
description: "Open WebUI · 2026-01-09 · Model Support: 11 changes in v0.7.0 — \U0001F4AD
  Users with models that support interleaved thinking now get more refined results
  from…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1096
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3e84c385d11d912ac52ed8b56a6885dfdf14f729ccfc9116b0f329231688033f
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-01-09-b98a48
  comparison: ''
  date: '2026-01-09'
  description: 'Open WebUI — v0.7.0: 11 Model Support changes'
  evidence:
  - quote: "\U0001F4AD Users with models that support interleaved thinking now get
      more refined results from multi-step workflows, as the model can analyze each
      tool's output before deciding what to do next."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F39B️ Users can now view read-only models in the workspace models
      list, with clear \"Read Only\" badges indicating when editing is restricted.
      [#20243](https://github.com/open-webui/open-webui/issues/20243), [#20369](https://github.com/open-webui/open-webui/pull/20369)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4CA The Evaluations leaderboard now includes a per-model activity
      chart displaying daily wins and losses as a diverging bar chart, with 30-day,
      1-year, and all-time views using weekly aggregation for longer timeframes."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F39E️ Users can now upload animated GIF and WebP formats as model
      profile images, with animation preserved by skipping resize processing for these
      file types. [Commit](https://github.com/open-webui/open-webui/commit/00af37bb4ed1ea0957c7c84a6a8def3a7998b8ca)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F50D Administrators can now control sigmoid normalization for CrossEncoder
      reranking models using the \"SENTENCE_TRANSFORMERS_CROSS_ENCODER_SIGMOID_ACTIVATION_FUNCTION\"
      environment variable, enabled by default for proper relevance threshold behavior
      with MS MARCO models. [#19999](https://github.com/open-webui/open-webui/discussions/19999)
      [#20228](https://github.com/open-webui/open-webui/pull/20228)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4CA [Users can now sync their anonymous usage statistics](https://openwebui.com/leaderboard)
      to the Open WebUI Community platform to power community leaderboards, drive
      model evaluations, and contribute to open-source AI research that benefits everyone,
      all while keeping conversations completely private (only metadata like model
      names, message counts, and ratings are shared). By sharing your stats, you're
      helping the community identify which models perform best, contributing to transparent
      AI benchmarking, and supporting the collective effort to make AI better for
      all. You can also download your stats as JSON for personal analysis."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F916 Users can now successfully @ mention models in Channels instead
      of experiencing silent failures. [Commit](https://github.com/open-webui/open-webui/commit/59957715836acb635f4b1c4ddbfb4ba7b82b3281)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F39B️ Users can now successfully use workspace models in chat, fixing
      \"Model not found\" errors that occurred when using custom model presets. [#20340](https://github.com/open-webui/open-webui/issues/20340),
      [#20344](https://github.com/open-webui/open-webui/pull/20344), [Commit](https://github.com/open-webui/open-webui/commit/b55a46ae99c32068ed306a5ecdaafa9f75504cd7),
      [Commit](https://github.com/open-webui/open-webui/commit/2bb13d5dbc6e233856e8aa26143222ceda8f6c11)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F50D Administrators using local CrossEncoder reranking models now
      see proper relevance threshold behavior through MS MARCO model score normalization
      to the 0-1 range via sigmoid activation. [#19999](https://github.com/open-webui/open-webui/issues/19999),
      [#20228](https://github.com/open-webui/open-webui/pull/20228)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4E5 Administrators no longer encounter TypeError crashes during
      SHA256 verification when uploading GGUF models via URL, fixing 500 Internal
      Server Error crashes. [#20263](https://github.com/open-webui/open-webui/issues/20263)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F517 Users now experience more reliable citations from AI models,
      especially when using smaller or weaker models that may not format citation
      references perfectly. [Commit](https://github.com/open-webui/open-webui/commit/c0ec04935b4eea3d334bfdec2fc41278f1085a49)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 11-model-support-changes-in-v0-7-0
  source_release: open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c
  source_type: github_releases
  theme: model-support
  title: 11 Model Support changes in v0.7.0
  type: change
related_changes:
- '[[Changes/Cline/2026-01-09-2-model-support-changes-in-v3-48-0|2 Model Support changes
  in v3.48.0]]'
- '[[Changes/Codex CLI/2026-01-09-4-model-support-changes-in-rust-v0-80-0|4 Model
  Support changes in rust-v0.80.0]]'
- '[[Changes/Midjourney/2026-01-09-niji-v7-is-now-live-for-those-who-don-t-know-this-is-our-version-of-our-image-mo|Niji
  V7 is now live!]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c]]'
source_type: github_releases
theme: model-support
title: 11 Model Support changes in v0.7.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Model Support changes in v0.7.0

**Open WebUI** · 2026-01-09 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.7.0) · from [[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|v0.7.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 💭 Users with models that support interleaved thinking now get more refined results from multi-step workflows, as the model can analyze each tool's output before deciding what to do next.

> 🎛️ Users can now view read-only models in the workspace models list, with clear "Read Only" badges indicating when editing is restricted. [#20243](https://github.com/open-webui/open-webui/issues/20243), [#20369](https://github.com/open-webui/open-webui/pull/20369)

> 📊 The Evaluations leaderboard now includes a per-model activity chart displaying daily wins and losses as a diverging bar chart, with 30-day, 1-year, and all-time views using weekly aggregation for longer timeframes.

> 🎞️ Users can now upload animated GIF and WebP formats as model profile images, with animation preserved by skipping resize processing for these file types. [Commit](https://github.com/open-webui/open-webui/commit/00af37bb4ed1ea0957c7c84a6a8def3a7998b8ca)

> 🔍 Administrators can now control sigmoid normalization for CrossEncoder reranking models using the "SENTENCE_TRANSFORMERS_CROSS_ENCODER_SIGMOID_ACTIVATION_FUNCTION" environment variable, enabled by default for proper relevance threshold behavior with MS MARCO models. [#19999](https://github.com/open-webui/open-webui/discussions/19999) [#20228](https://github.com/open-webui/open-webui/pull/20228)

> 📊 [Users can now sync their anonymous usage statistics](https://openwebui.com/leaderboard) to the Open WebUI Community platform to power community leaderboards, drive model evaluations, and contribute to open-source AI research that benefits everyone, all while keeping conversations completely private (only metadata like model names, message counts, and ratings are shared). By sharing your stats, you're helping the community identify which models perform best, contributing to transparent AI benchmarking, and supporting the collective effort to make AI better for all. You can also download your stats as JSON for personal analysis.

> 🤖 Users can now successfully @ mention models in Channels instead of experiencing silent failures. [Commit](https://github.com/open-webui/open-webui/commit/59957715836acb635f4b1c4ddbfb4ba7b82b3281)

> 🎛️ Users can now successfully use workspace models in chat, fixing "Model not found" errors that occurred when using custom model presets. [#20340](https://github.com/open-webui/open-webui/issues/20340), [#20344](https://github.com/open-webui/open-webui/pull/20344), [Commit](https://github.com/open-webui/open-webui/commit/b55a46ae99c32068ed306a5ecdaafa9f75504cd7), [Commit](https://github.com/open-webui/open-webui/commit/2bb13d5dbc6e233856e8aa26143222ceda8f6c11)

> 🔍 Administrators using local CrossEncoder reranking models now see proper relevance threshold behavior through MS MARCO model score normalization to the 0-1 range via sigmoid activation. [#19999](https://github.com/open-webui/open-webui/issues/19999), [#20228](https://github.com/open-webui/open-webui/pull/20228)

> 📥 Administrators no longer encounter TypeError crashes during SHA256 verification when uploading GGUF models via URL, fixing 500 Internal Server Error crashes. [#20263](https://github.com/open-webui/open-webui/issues/20263)

> 🔗 Users now experience more reliable citations from AI models, especially when using smaller or weaker models that may not format citation references perfectly. [Commit](https://github.com/open-webui/open-webui/commit/c0ec04935b4eea3d334bfdec2fc41278f1085a49)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-01-09-3-editor-experience-changes-in-v0-7-0|3 Editor Experience changes in v0.7.0]] · Editor Experience
- [[Changes/Open WebUI/2026-01-09-users-on-windows-now-see-correctly-preserved-line-breaks-when-using-the-clipboar|📋 Users on Windows now see correctly preserved line breaks when using…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-01-09-2-memory-and-personalization-changes-in-v0-7-0|2 Memory and Personalization changes in v0.7.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-01-09-4-search-and-browsing-changes-in-v0-7-0|4 Search and Browsing changes in v0.7.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-01-09-3-apps-and-integrations-changes-in-v0-7-0|3 Apps and Integrations changes in v0.7.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-01-09-5-files-and-data-changes-in-v0-7-0|5 Files and Data changes in v0.7.0]] · Files and Data
- [[Changes/Open WebUI/2026-01-09-3-context-window-changes-in-v0-7-0|3 Context Window changes in v0.7.0]] · Context Window
- [[Changes/Open WebUI/2026-01-09-9-reliability-and-performance-changes-in-v0-7-0|9 Reliability and Performance changes in v0.7.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-01-09-6-safety-and-privacy-changes-in-v0-7-0|6 Safety and Privacy changes in v0.7.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-01-09-3-account-and-access-changes-in-v0-7-0|3 Account and Access changes in v0.7.0]] · Account and Access
- [[Changes/Open WebUI/2026-01-09-4-image-generation-changes-in-v0-7-0|4 Image Generation changes in v0.7.0]] · Image Generation
- [[Changes/Open WebUI/2026-01-09-5-interface-experience-changes-in-v0-7-0|5 Interface Experience changes in v0.7.0]] · Interface Experience
- [[Changes/Open WebUI/2026-01-09-24-developer-workflow-changes-in-v0-7-0|24 Developer Workflow changes in v0.7.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-01-09-3-voice-and-audio-changes-in-v0-7-0|3 Voice and Audio changes in v0.7.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-01-09-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-01-09-26-other-changes-in-v0-7-0|26 other changes in v0.7.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-01-09 · Midjourney · [[Changes/Midjourney/2026-01-09-niji-v7-is-now-live-for-those-who-don-t-know-this-is-our-version-of-our-image-mo|Niji V7 is now live!]]
- Later: 2026-01-09 · OpenCode · [[Changes/OpenCode/2026-01-09-core-fix-model-dialog-search-issues-in-favorites-recents-list-and-prevent-deprec|Core Fix model dialog search issues in favorites/recents list and prevent deprecated…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-01-09-b98a48&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-01-09-11-model-support-changes-in-v0-7-0.md%0ACard%20ID%3A%20open-webui-2026-01-09-b98a48%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.7.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->