---
card_id: dify-2024-04-25-f61cd5
date: '2024-04-25'
description: 'Dify · 2024-04-25 · Other changes: 32 changes in v0.6.5 — Added support
  for Groq Llama3 by @guchenhe in #3673.'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fcbdf4435a933e5a7887a92dd68c99b177a24b12ab15e2b49ac47afa59d7f33e
product: dify
product_name: Dify
record:
  card_id: dify-2024-04-25-f61cd5
  comparison: ''
  date: '2024-04-25'
  description: 'Dify — v0.6.5: 32 other changes'
  evidence:
  - quote: 'Added support for Groq Llama3 by @guchenhe in #3673.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'Introduced a new tool, Judge0 CE, by @richards199999 in #3684.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'Added `conversation_id` and `user_id` to the chatflow/workflow system
      variables by @takatost in #3771.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: This is particularly valuable when you need to interact with internal systems.
      You can pass these two parameters when using the HTTP Request node, allowing
      the internal system to understand the current user and the corresponding conversation
      to establish a connection.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'Enabled the addition of custom tags for Knowledge and App categories by
      @JohnJyong in #3755.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'Addressed an upgrading issue where gmpy2 could cause the error "Worker
      (pid:67) was sent code 132!" on some CPUs by @bowenliang123 in #3745.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: For additional enhancements and updates, refer to the What's Changed section
      below.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'Get the latest code from the main branch:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: Stop API server, Worker and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: Finally, run API server, Worker and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: add groq llama3 by @guchenhe in https://github.com/langgenius/dify/pull/3673
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'Add new tool: Judge0 CE by @richards199999 in https://github.com/langgenius/dify/pull/3684'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'refactor: tool parameter cache by @Yeuoly in https://github.com/langgenius/dify/pull/3703'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: Update README_JA.md by @eltociear in https://github.com/langgenius/dify/pull/3727
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: Update "@formatjs/intl-localematcher" to version 0.5.4 in package.json
      by @LeoQuote in https://github.com/langgenius/dify/pull/3726
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'feat: add copy button to code by @crazywoola in https://github.com/langgenius/dify/pull/3719'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'chore: add selector for use app store by @JzoNgKVO in https://github.com/langgenius/dify/pull/3746'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: Knowledge optimization by @JohnJyong in https://github.com/langgenius/dify/pull/3755
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'feat: support prompt messages sorting by @iamjoel in https://github.com/langgenius/dify/pull/3757'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'test: add test for PKCS1OAEP_Cipher with gmpy2 by @bowenliang123 in https://github.com/langgenius/dify/pull/3760'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'feat: add conversation_id and user_id in chatflow/workflow system vars
      by @takatost in https://github.com/langgenius/dify/pull/3771'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'feat: test all unit tests by @takatost in https://github.com/langgenius/dify/pull/3787'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: use pymilvus 2.3.7 by @bowenliang123 in https://github.com/langgenius/dify/pull/3790
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'test: add unit tests for vector stores of Milvus, Qdrant and Weaviate
      by @bowenliang123 in https://github.com/langgenius/dify/pull/3688'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'feat: add log_file environment variable by @YidaHu in https://github.com/langgenius/dify/pull/3793'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'chore: remove anthropic pay entrance by @iamjoel in https://github.com/langgenius/dify/pull/3822'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: version to 0.6.5 by @takatost in https://github.com/langgenius/dify/pull/3834
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'feat: add aliyun oss storage by @henrybit in https://github.com/langgenius/dify/pull/3690'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: 'feat: query prompt template support in chatflow by @takatost in https://github.com/langgenius/dify/pull/3791'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  - quote: extract enum type for tenant account role by @bowenliang123 in https://github.com/langgenius/dify/pull/3788
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 32-other-changes-in-0-6-5
  source_release: dify-2024-04-25-0-6-5-github-152778461-0e2655b1
  source_type: github_releases
  theme: uncategorized
  title: 32 other changes in 0.6.5
  type: change
source_release: '[[Releases/Dify/dify-2024-04-25-0-6-5-github-152778461-0e2655b1|dify-2024-04-25-0-6-5-github-152778461-0e2655b1]]'
source_type: github_releases
theme: uncategorized
title: 32 other changes in 0.6.5
type: change
---

<!-- chronolog:begin region="header" -->
# 32 other changes in 0.6.5

**Dify** · 2024-04-25 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.6.5) · from [[Releases/Dify/dify-2024-04-25-0-6-5-github-152778461-0e2655b1|v0.6.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added support for Groq Llama3 by @guchenhe in #3673.

> Introduced a new tool, Judge0 CE, by @richards199999 in #3684.

> Added `conversation_id` and `user_id` to the chatflow/workflow system variables by @takatost in #3771.

> This is particularly valuable when you need to interact with internal systems. You can pass these two parameters when using the HTTP Request node, allowing the internal system to understand the current user and the corresponding conversation to establish a connection.

> Enabled the addition of custom tags for Knowledge and App categories by @JohnJyong in #3755.

> Addressed an upgrading issue where gmpy2 could cause the error "Worker (pid:67) was sent code 132!" on some CPUs by @bowenliang123 in #3745.

> For additional enhancements and updates, refer to the What's Changed section below.

> Get the latest code from the main branch:

> Stop API server, Worker and Web frontend Server.

> Update Python dependencies:

> Then, let's run the migration script:

> Finally, run API server, Worker and Web frontend Server again.

> add groq llama3 by @guchenhe in https://github.com/langgenius/dify/pull/3673

> Add new tool: Judge0 CE by @richards199999 in https://github.com/langgenius/dify/pull/3684

> refactor: tool parameter cache by @Yeuoly in https://github.com/langgenius/dify/pull/3703

> Update README_JA.md by @eltociear in https://github.com/langgenius/dify/pull/3727

> Update "@formatjs/intl-localematcher" to version 0.5.4 in package.json by @LeoQuote in https://github.com/langgenius/dify/pull/3726

> feat: add copy button to code by @crazywoola in https://github.com/langgenius/dify/pull/3719

> chore: add selector for use app store by @JzoNgKVO in https://github.com/langgenius/dify/pull/3746

> Knowledge optimization by @JohnJyong in https://github.com/langgenius/dify/pull/3755

> feat: support prompt messages sorting by @iamjoel in https://github.com/langgenius/dify/pull/3757

> test: add test for PKCS1OAEP_Cipher with gmpy2 by @bowenliang123 in https://github.com/langgenius/dify/pull/3760

> feat: add conversation_id and user_id in chatflow/workflow system vars by @takatost in https://github.com/langgenius/dify/pull/3771

> feat: test all unit tests by @takatost in https://github.com/langgenius/dify/pull/3787

> use pymilvus 2.3.7 by @bowenliang123 in https://github.com/langgenius/dify/pull/3790

> test: add unit tests for vector stores of Milvus, Qdrant and Weaviate by @bowenliang123 in https://github.com/langgenius/dify/pull/3688

> feat: add log_file environment variable by @YidaHu in https://github.com/langgenius/dify/pull/3793

> chore: remove anthropic pay entrance by @iamjoel in https://github.com/langgenius/dify/pull/3822

> version to 0.6.5 by @takatost in https://github.com/langgenius/dify/pull/3834

> feat: add aliyun oss storage by @henrybit in https://github.com/langgenius/dify/pull/3690

> feat: query prompt template support in chatflow by @takatost in https://github.com/langgenius/dify/pull/3791

> extract enum type for tenant account role by @bowenliang123 in https://github.com/langgenius/dify/pull/3788

Source: https://github.com/langgenius/dify/releases/tag/0.6.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-04-25-you-can-now-enable-memory-in-the-llm-node-within-your-chatflow-and-customize-the|Enable memory in the LLM node within your chatflow, and customize the query prompt…]] · Memory and Personalization
- [[Changes/Dify/2024-04-25-feat-prompt-editor-support-auto-height-by-content-height-and-fix-some-bugs-by-ia|feat: prompt editor support auto height by content height and fix some bugs]] · Editor Experience
- [[Changes/Dify/2024-04-25-this-update-primarily-focuses-on-enhancing-system-stability-and-improving-user-e|This update primarily focuses on enhancing system stability and improving user experience]] · Reliability and Performance
- [[Changes/Dify/2024-04-25-2-voice-and-audio-changes-in-0-6-5|2 Voice and Audio changes in 0.6.5]] · Voice and Audio
- [[Changes/Dify/2024-04-25-localize-links-to-localized-readmes-by-carsonkahn-external-in-https-github-com-l|Localize links to localized READMEs]] · Accessibility and Localization
- [[Changes/Dify/2024-04-25-6-model-support-changes-in-0-6-5|6 Model Support changes in 0.6.5]] · Model Support
- [[Changes/Dify/2024-04-25-2-files-and-data-changes-in-0-6-5|2 Files and Data changes in 0.6.5]] · Files and Data
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-04-25-f61cd5&body=Card%3A%20Changes%2FDify%2F2024-04-25-32-other-changes-in-0-6-5.md%0ACard%20ID%3A%20dify-2024-04-25-f61cd5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.6.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->