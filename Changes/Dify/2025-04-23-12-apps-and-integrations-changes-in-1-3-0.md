---
card_id: dify-2025-04-23-c12a7d
date: '2025-04-23'
description: 'Dify · 2025-04-23 · Apps and Integrations: 12 changes in v1.3.0 — **Never
  Miss a Plugin Update**: Our new feature ensures you''re always in the loop. When
  a new…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2322
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 10698cd83f04d4c5c31097e20c4a06373eff6178b577150eb7243184945cf9d5
product: dify
product_name: Dify
record:
  card_id: dify-2025-04-23-c12a7d
  comparison: ''
  date: '2025-04-23'
  description: 'Dify — v1.3.0: 12 Apps and Integrations changes'
  evidence:
  - quote: '**Never Miss a Plugin Update**: Our new feature ensures you''re always
      in the loop. When a new version of a plugin drops, you''ll see a clear indicator
      right in the UI. This keeps your environment up-to-date and running smoothly,
      thanks to @Yeuoly in #17695.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.3.0
  - quote: '**Token Counting Made Easy**: We''ve tweaked the default token counting
      rules. Now, if your provider doesn''t return token usage, we''ll default to
      using 0. However, if you''d like to estimate using the tokenizer, you can set
      `PLUGIN_BASED_TOKEN_COUNTING_ENABLED=true`. Heads up, this might impact performance,
      detailed by @laipz8200 in #17706.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.3.0
  - quote: '**Japanese Touch-Ups**: Some timely translation updates and locale param
      support by @t-daisuke for plugins. Quick ‘Yoro-shiku’ to our Japanese community!'
    source_release: https://github.com/langgenius/dify/releases/tag/1.3.0
  - quote: 'refactor: add API endpoint to list latest plugin versions and query it
      in asynchronous way by @Yeuoly in https://github.com/langgenius/dify/pull/17695'
    source_release: https://github.com/langgenius/dify/releases/tag/1.3.0
  - quote: 'feat(large_language_model): Adds plugin-based token counting configuration
      option by @laipz8200 in https://github.com/langgenius/dify/pull/17706'
    source_release: https://github.com/langgenius/dify/releases/tag/1.3.0
  - quote: 'enhance(plugin): replace json.loads with Pydantic model_validate_json
      by @Yeuoly in https://github.com/langgenius/dify/pull/17867'
    source_release: https://github.com/langgenius/dify/releases/tag/1.3.0
  - quote: 'feat: plugin tool selector add tool default description by @junjiem in
      https://github.com/langgenius/dify/pull/18018'
    source_release: https://github.com/langgenius/dify/releases/tag/1.3.0
  - quote: 'feat: add minimum dify version requirement to plugins by @Yeuoly in https://github.com/langgenius/dify/pull/18022'
    source_release: https://github.com/langgenius/dify/releases/tag/1.3.0
  - quote: 'feat: implement blob chunk handling in plugin manager by @Yeuoly in https://github.com/langgenius/dify/pull/18101'
    source_release: https://github.com/langgenius/dify/releases/tag/1.3.0
  - quote: 'feat: add red corner mark to Badge component for marketplace plugins by
      @Yeuoly in https://github.com/langgenius/dify/pull/18162'
    source_release: https://github.com/langgenius/dify/releases/tag/1.3.0
  - quote: 'feat: fetch app info in plugins by @Yeuoly in https://github.com/langgenius/dify/pull/18202'
    source_release: https://github.com/langgenius/dify/releases/tag/1.3.0
  - quote: feat[plugin]:The plugin upload file change to be stored as a toolfile…
      by @Gevtolev in https://github.com/langgenius/dify/pull/18277
    source_release: https://github.com/langgenius/dify/releases/tag/1.3.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 12-apps-and-integrations-changes-in-1-3-0
  source_release: dify-2025-04-23-1-3-0-github-214141766-8d4f18a3
  source_type: github_releases
  theme: apps-integrations
  title: 12 Apps and Integrations changes in 1.3.0
  type: change
related_changes:
- '[[Changes/AnythingLLM/2025-04-18-3-apps-and-integrations-changes-in-v1-8-0|3 Apps
  and Integrations changes in v1.8.0]]'
- '[[Changes/Replit/2025-04-18-smarter-integrations-matching|Smarter integrations
  matching]]'
- '[[Changes/Cline/2025-04-19-add-ability-for-models-that-support-it-to-receive-image-responses-from-mcp-serve|Add
  ability for models that support it to receive image responses from MCP servers…]]'
source_release: '[[Releases/Dify/dify-2025-04-23-1-3-0-github-214141766-8d4f18a3|dify-2025-04-23-1-3-0-github-214141766-8d4f18a3]]'
source_type: github_releases
theme: apps-integrations
title: 12 Apps and Integrations changes in 1.3.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Apps and Integrations changes in 1.3.0

**Dify** · 2025-04-23 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.3.0) · from [[Releases/Dify/dify-2025-04-23-1-3-0-github-214141766-8d4f18a3|v1.3.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Never Miss a Plugin Update**: Our new feature ensures you're always in the loop. When a new version of a plugin drops, you'll see a clear indicator right in the UI. This keeps your environment up-to-date and running smoothly, thanks to @Yeuoly in #17695.

> **Token Counting Made Easy**: We've tweaked the default token counting rules. Now, if your provider doesn't return token usage, we'll default to using 0. However, if you'd like to estimate using the tokenizer, you can set `PLUGIN_BASED_TOKEN_COUNTING_ENABLED=true`. Heads up, this might impact performance, detailed by @laipz8200 in #17706.

> **Japanese Touch-Ups**: Some timely translation updates and locale param support by @t-daisuke for plugins. Quick ‘Yoro-shiku’ to our Japanese community!

> refactor: add API endpoint to list latest plugin versions and query it in asynchronous way by @Yeuoly in https://github.com/langgenius/dify/pull/17695

> feat(large_language_model): Adds plugin-based token counting configuration option by @laipz8200 in https://github.com/langgenius/dify/pull/17706

> enhance(plugin): replace json.loads with Pydantic model_validate_json by @Yeuoly in https://github.com/langgenius/dify/pull/17867

> feat: plugin tool selector add tool default description by @junjiem in https://github.com/langgenius/dify/pull/18018

> feat: add minimum dify version requirement to plugins by @Yeuoly in https://github.com/langgenius/dify/pull/18022

> feat: implement blob chunk handling in plugin manager by @Yeuoly in https://github.com/langgenius/dify/pull/18101

> feat: add red corner mark to Badge component for marketplace plugins by @Yeuoly in https://github.com/langgenius/dify/pull/18162

> feat: fetch app info in plugins by @Yeuoly in https://github.com/langgenius/dify/pull/18202

> feat[plugin]:The plugin upload file change to be stored as a toolfile… by @Gevtolev in https://github.com/langgenius/dify/pull/18277

Source: https://github.com/langgenius/dify/releases/tag/1.3.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-04-23-2-interface-experience-changes-in-1-3-0|2 Interface Experience changes in 1.3.0]] · Interface Experience
- [[Changes/Dify/2025-04-23-3-agent-mode-changes-in-1-3-0|3 Agent Mode changes in 1.3.0]] · Agent Mode
- [[Changes/Dify/2025-04-23-chore-speed-up-git-checkout-by-removing-fetch-depth-0-to-avoid-pulling-all-tags|chore: speed up git checkout by removing fetch-depth 0 to avoid pulling all tags…]] · Reliability and Performance
- [[Changes/Dify/2025-04-23-workflow-export-delight-ever-wanted-to-share-your-workflow-effortlessly-you-can|Workflow Export Delight: Ever wanted to share your workflow effortlessly?]] · Collaboration
- [[Changes/Dify/2025-04-23-chore-skip-document-segments-fetching-with-non-existed-dataset-of-datasetdocumen|chore: skip document segments fetching with non-existed dataset of DatasetDocument…]] · Files and Data
- [[Changes/Dify/2025-04-23-4-model-support-changes-in-1-3-0|4 Model Support changes in 1.3.0]] · Model Support
- [[Changes/Dify/2025-04-23-2-editor-experience-changes-in-1-3-0|2 Editor Experience changes in 1.3.0]] · Editor Experience
- [[Changes/Dify/2025-04-23-5-safety-and-privacy-changes-in-1-3-0|5 Safety and Privacy changes in 1.3.0]] · Safety and Privacy
- [[Changes/Dify/2025-04-23-2-developer-workflow-changes-in-1-3-0|2 Developer Workflow changes in 1.3.0]] · Developer Workflow
- [[Changes/Dify/2025-04-23-2-enterprise-and-administration-changes-in-1-3-0|2 Enterprise and Administration changes in 1.3.0]] · Enterprise and Administration
- [[Changes/Dify/2025-04-23-80-other-changes-in-1-3-0|80 other changes in 1.3.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-04-19 · Cline · [[Changes/Cline/2025-04-19-add-ability-for-models-that-support-it-to-receive-image-responses-from-mcp-serve|Add ability for models that support it to receive image responses from MCP servers…]]
- Later: 2025-04-25 · Cline · [[Changes/Cline/2025-04-25-add-download-counts-to-mcp-marketplace-items|Add download counts to MCP marketplace items]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-04-23-c12a7d&body=Card%3A%20Changes%2FDify%2F2025-04-23-12-apps-and-integrations-changes-in-1-3-0.md%0ACard%20ID%3A%20dify-2025-04-23-c12a7d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.3.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->