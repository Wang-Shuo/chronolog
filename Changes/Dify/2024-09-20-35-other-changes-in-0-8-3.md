---
card_id: dify-2024-09-20-e64468
date: '2024-09-20'
description: 'Dify · 2024-09-20 · Other changes: 35 changes in v0.8.3 — Hey everyone!
  We’re thrilled to announce the release of version 0.8.3, and it brings something
  truly…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8b5a60208248b6c327b2e3bc543717740c4aaece92c7130f94e55e65d59cb214
product: dify
product_name: Dify
record:
  card_id: dify-2024-09-20-e64468
  comparison: ''
  date: '2024-09-20'
  description: 'Dify — v0.8.3: 35 other changes'
  evidence:
  - quote: 'Hey everyone! We’re thrilled to announce the release of version 0.8.3,
      and it brings something truly game-changing:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: '**New Tools**:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: '**Siliconflow Image-Gen Tool**: Part of the flux dev suite, this tool,
      introduced by @hjlarry in #8450, further expands your creative toolkit.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: '**Timeout Configuration**: Thanks to @kurokobo in #8395, you now have
      full control over text generation and workflow timeouts via environment variables,
      giving you more flexibility in managing process execution times.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: '**Workflow Improvements**: Including better result handling and improved
      multi-retrieval for datasets.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: '**Bug Fixes**: Numerous fixes across authorization, token usage, and vector
      search methods to ensure smoother operations.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: '> [!WARNING]'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: '> The `docker-compose.yaml` has been refactored. If you''ve made any changes
      to the file, make sure to check out the "Upgrade to new docker compose deployment"
      section above for usage and migration tips.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: Back up your customized docker-compose YAML file (optional)
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: Get the latest code from the main branch
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: Back up data
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: Upgrade services
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: Stop API server, Worker and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: Finally, run API server, Worker and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: 'chore: update firecrawl scrape to V1 api by @hjlarry in https://github.com/langgenius/dify/pull/8367'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: support hunyuan-turbo by @xiandan-erizo in https://github.com/langgenius/dify/pull/8372
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: 'chore: improve usage of striping prefix or suffix of string with Ruff
      0.6.5 by @bowenliang123 in https://github.com/langgenius/dify/pull/8392'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: 'feat: allow users to specify timeout for text generations and workflows
      by environment variable by @kurokobo in https://github.com/langgenius/dify/pull/8395'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: 'chore(workflow): Optimize the iteration when selecting a variable from
      a branch in the output variable causes iteration index err by @takatost in https://github.com/langgenius/dify/pull/8440'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: add WorkflowClient.get_result, increase version number by @twisker in https://github.com/langgenius/dify/pull/8435
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: add svg render & Image preview optimization by @charli117 in https://github.com/langgenius/dify/pull/8387
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: multi-retrival use dataset's top-k by @JohnJyong in https://github.com/langgenius/dify/pull/8416
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: 'chore: workflow BRANCH, PARALLEL i18n by @ZuzooVn in https://github.com/langgenius/dify/pull/8452'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: 'feat: add flux dev of siliconflow image-gen tool by @hjlarry in https://github.com/langgenius/dify/pull/8450'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: 'feat: Add base URL settings and secure_ascii options to the Brave search
      tool by @XiaoLey in https://github.com/langgenius/dify/pull/8463'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: 'chore: update the .gitignore file to include opensearch,pgvector,and myscale
      by @hwzhuhao in https://github.com/langgenius/dify/pull/8470'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: 'feat: Add ComfyUI tool for Stable Diffusion by @QunBB in https://github.com/langgenius/dify/pull/8160'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: 'refactor: rename task_type to task for jina embeddings v3 by @bwanglzu
      in https://github.com/langgenius/dify/pull/8488'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: 'feat: sync Qwen API with Aliyun Bailian by @soulteary in https://github.com/langgenius/dify/pull/8538'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: add storage error log by @JohnJyong in https://github.com/langgenius/dify/pull/8556
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: 'chore: improve delimiter by @iamjoel in https://github.com/langgenius/dify/pull/8552'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: ComfyUI tool use the new internal enumeration class "VariableKey" by @QunBB
      in https://github.com/langgenius/dify/pull/8533
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  - quote: Update version to 0.8.3 in packaging and docker-compose files by @laipz8200
      in https://github.com/langgenius/dify/pull/8590
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 35-other-changes-in-0-8-3
  source_release: dify-2024-09-20-0-8-3-github-176083684-f9381a70
  source_type: github_releases
  theme: uncategorized
  title: 35 other changes in 0.8.3
  type: change
source_release: '[[Releases/Dify/dify-2024-09-20-0-8-3-github-176083684-f9381a70|dify-2024-09-20-0-8-3-github-176083684-f9381a70]]'
source_type: github_releases
theme: uncategorized
title: 35 other changes in 0.8.3
type: change
---

<!-- chronolog:begin region="header" -->
# 35 other changes in 0.8.3

**Dify** · 2024-09-20 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.8.3) · from [[Releases/Dify/dify-2024-09-20-0-8-3-github-176083684-f9381a70|v0.8.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hey everyone! We’re thrilled to announce the release of version 0.8.3, and it brings something truly game-changing:

> **New Tools**:

> **Siliconflow Image-Gen Tool**: Part of the flux dev suite, this tool, introduced by @hjlarry in #8450, further expands your creative toolkit.

> **Timeout Configuration**: Thanks to @kurokobo in #8395, you now have full control over text generation and workflow timeouts via environment variables, giving you more flexibility in managing process execution times.

> **Workflow Improvements**: Including better result handling and improved multi-retrieval for datasets.

> **Bug Fixes**: Numerous fixes across authorization, token usage, and vector search methods to ensure smoother operations.

> > [!WARNING]

> > The `docker-compose.yaml` has been refactored. If you've made any changes to the file, make sure to check out the "Upgrade to new docker compose deployment" section above for usage and migration tips.

> Back up your customized docker-compose YAML file (optional)

> Get the latest code from the main branch

> Back up data

> Upgrade services

> Stop API server, Worker and Web frontend Server.

> Update Python dependencies:

> Then, let's run the migration script:

> Finally, run API server, Worker and Web frontend Server again.

> chore: update firecrawl scrape to V1 api by @hjlarry in https://github.com/langgenius/dify/pull/8367

> support hunyuan-turbo by @xiandan-erizo in https://github.com/langgenius/dify/pull/8372

> chore: improve usage of striping prefix or suffix of string with Ruff 0.6.5 by @bowenliang123 in https://github.com/langgenius/dify/pull/8392

> feat: allow users to specify timeout for text generations and workflows by environment variable by @kurokobo in https://github.com/langgenius/dify/pull/8395

> chore(workflow): Optimize the iteration when selecting a variable from a branch in the output variable causes iteration index err by @takatost in https://github.com/langgenius/dify/pull/8440

> add WorkflowClient.get_result, increase version number by @twisker in https://github.com/langgenius/dify/pull/8435

> add svg render & Image preview optimization by @charli117 in https://github.com/langgenius/dify/pull/8387

> multi-retrival use dataset's top-k by @JohnJyong in https://github.com/langgenius/dify/pull/8416

> chore: workflow BRANCH, PARALLEL i18n by @ZuzooVn in https://github.com/langgenius/dify/pull/8452

> feat: add flux dev of siliconflow image-gen tool by @hjlarry in https://github.com/langgenius/dify/pull/8450

> feat: Add base URL settings and secure_ascii options to the Brave search tool by @XiaoLey in https://github.com/langgenius/dify/pull/8463

> chore: update the .gitignore file to include opensearch,pgvector,and myscale by @hwzhuhao in https://github.com/langgenius/dify/pull/8470

> feat: Add ComfyUI tool for Stable Diffusion by @QunBB in https://github.com/langgenius/dify/pull/8160

> refactor: rename task_type to task for jina embeddings v3 by @bwanglzu in https://github.com/langgenius/dify/pull/8488

> feat: sync Qwen API with Aliyun Bailian by @soulteary in https://github.com/langgenius/dify/pull/8538

> add storage error log by @JohnJyong in https://github.com/langgenius/dify/pull/8556

> chore: improve delimiter by @iamjoel in https://github.com/langgenius/dify/pull/8552

> ComfyUI tool use the new internal enumeration class "VariableKey" by @QunBB in https://github.com/langgenius/dify/pull/8533

> Update version to 0.8.3 in packaging and docker-compose files by @laipz8200 in https://github.com/langgenius/dify/pull/8590

Source: https://github.com/langgenius/dify/releases/tag/0.8.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-09-20-comfyui-for-stable-diffusion-enhanced-image-generation-capabilities-with-the-int|ComfyUI for Stable Diffusion]] · Image Generation
- [[Changes/Dify/2024-09-20-python-sdk-add-knowledgebaseclient-and-the-corresponding-test-cases-by-twisker-i|Python SDK Add KnowledgeBaseClient and the corresponding test cases]] · Apps and Integrations
- [[Changes/Dify/2024-09-20-we-ve-also-worked-on-various-optimizations-and-bug-fixes-to-improve-overall-stab|We've also worked on various optimizations and bug fixes to improve overall stability]] · Reliability and Performance
- [[Changes/Dify/2024-09-20-3-developer-workflow-changes-in-0-8-3|3 Developer Workflow changes in 0.8.3]] · Developer Workflow
- [[Changes/Dify/2024-09-20-feat-add-hunyuan-vision-by-muzea-in-https-github-com-langgenius-dify-pull-8529|feat: add hunyuan-vision]] · Multimodal Input
- [[Changes/Dify/2024-09-20-5-model-support-changes-in-0-8-3|5 Model Support changes in 0.8.3]] · Model Support
- [[Changes/Dify/2024-09-20-validate-user-permission-before-enter-app-detail-page-by-douxc-in-https-github-c|validate user permission before enter app detail page]] · Safety and Privacy
- [[Changes/Dify/2024-09-20-image-preview-optimization-enhanced-svg-rendering-and-image-previews-for-a-smoot|Image Preview Optimization]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-09-20-e64468&body=Card%3A%20Changes%2FDify%2F2024-09-20-35-other-changes-in-0-8-3.md%0ACard%20ID%3A%20dify-2024-09-20-e64468%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.8.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->