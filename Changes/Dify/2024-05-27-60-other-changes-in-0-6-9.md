---
card_id: dify-2024-05-27-f27caf
date: '2024-05-27'
description: 'Dify · 2024-05-27 · Other changes: 60 changes in v0.6.9 Workflow as
  Tool — We’ve been working on enhancing our workflow capabilities lately. Today we’ve
  got…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9117c58196aca5cb3316f2c2b5816f06a6c0509328aa78d4e0e78905d40987b2
product: dify
product_name: Dify
record:
  card_id: dify-2024-05-27-f27caf
  comparison: ''
  date: '2024-05-27'
  description: 'Dify — v0.6.9 Workflow as Tool: 60 other changes'
  evidence:
  - quote: 'We’ve been working on enhancing our workflow capabilities lately. Today
      we’ve got some news:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: https://github.com/langgenius/dify/assets/5485478/3e9a237a-2340-4cb1-a4a6-0b7a396a810c
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: Make sure the input is an array. Each item in the array will be processed
      sequentially by the iteration node until all items are addressed. For instance,
      if you require a lengthy article, simply input several headlines. This will
      result in an article containing a paragraph for each headline, freeing you from
      the need for complex prompt orchestration.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: We’ve updated our UI to be more intuitive and easier to use, with improved
      classification.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: '**Vertex AI Support**: Added support for Vertex AI by @patryk20120 in
      #4586 and @miendinh in #4641.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: '**Claude Stream Tool Call**: Enhanced Claude stream tool call by @Yeuoly
      in #4469.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: '**Chat Custom Disclaimer**: You can add custom disclaimers in WebApp by
      @patryk20120 in #4306.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: '**MiniMax Mode Sensitive Info Masking**: Added parameter config for masking
      sensitive info in MiniMax mode by @zhangever in #4294.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: '**Jina Search & Reader CSS Selectors**: Added CSS selectors for Jina Search
      & Reader by @rennokki in #4523.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: '**Images and Tables Extraction from DOCX**: Now supports extracting images
      and tables from DOCX files by @JohnJyong in #4619.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: '**WORKFLOW_MAX_EXECUTION_TIME**: Added environment variable for max workflow
      execution time by @majian159 in #4632.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: '**Image Preview URL expire Env Variable**: Added environment variable
      for time signature of image preview url by @patryk20120 in #4650.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: For additional enhancements and updates, refer to the What's Changed section
      below.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'Get the latest code from the main branch:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: Stop API server, Worker and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: Finally, run API server, Worker and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: Create README_KR.md by @leejoo0 in https://github.com/langgenius/dify/pull/4364
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: improve the code readability of http_executor node by @hjlarry in https://github.com/langgenius/dify/pull/4360
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'feat: Use Romanian & other langs in QA by @rennokki in https://github.com/langgenius/dify/pull/4205'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'docs: Add CONTRIBUTING_JA.md by @shutootaki in https://github.com/langgenius/dify/pull/4383'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: Optimize webscraper by @charli117 in https://github.com/langgenius/dify/pull/4392
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'chore: remove useless code in knowledge_retrieval_node by @VoidIsVoid
      in https://github.com/langgenius/dify/pull/4412'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: Custom sqlalchemy database uri scheme is supported by @xtuhcy in https://github.com/langgenius/dify/pull/4367
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: Remove useless code by @GarfieldDai in https://github.com/langgenius/dify/pull/4416
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'feat: add pre ping for sqlalchemy configuration by @takatost in https://github.com/langgenius/dify/pull/4454'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'improve: exract Code Node provider for each supported scripting language
      by @bowenliang123 in https://github.com/langgenius/dify/pull/4164'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'enhance: claude stream tool call by @Yeuoly in https://github.com/langgenius/dify/pull/4469'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'chore: update docker-compose.yaml by @eltociear in https://github.com/langgenius/dify/pull/4492'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: Feat/chat custom disclaimer by @patryk20120 in https://github.com/langgenius/dify/pull/4306
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'chore: skip unnecessary key checks prior to accessing a dictionary by
      @bowenliang123 in https://github.com/langgenius/dify/pull/4497'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'chore: sort categories in recommended app service response by @BenjaminX
      in https://github.com/langgenius/dify/pull/4498'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: feat:Provide parameter config for mask_sensitive_info of MiniMax mode…
      by @zhangever in https://github.com/langgenius/dify/pull/4294
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: Add UNSTRUCTURED_API_KEY env support by @majian159 in https://github.com/langgenius/dify/pull/4369
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'improve: generalize transformations and scripts of runner and preloads
      into TemplateTransformer by @bowenliang123 in https://github.com/langgenius/dify/pull/4487'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'chore: apply and fix flake8-bugbear lint rules by @bowenliang123 in https://github.com/langgenius/dify/pull/4496'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'feat: Jina Search & Jina Reader CSS selectors by @rennokki in https://github.com/langgenius/dify/pull/4523'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'chore: update yfinance dependency to version 0.2.40 by @BenjaminX in https://github.com/langgenius/dify/pull/4517'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: Bump oss2 to 2.18.5 for AuthV4 support by @denverdino in https://github.com/langgenius/dify/pull/4425
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: oauth2 supports. by @GarfieldDai in https://github.com/langgenius/dify/pull/4551
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: add qdrant metadata.doc_id index by @JohnJyong in https://github.com/langgenius/dify/pull/4559
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'chore: Hide the copy button when there is no content to copy by @hjlarry
      in https://github.com/langgenius/dify/pull/4546'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: Refactor part of the ProviderManager code to improve readability by @hjlarry
      in https://github.com/langgenius/dify/pull/4524
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'chore(api): Use channel from UI as API query parameter by @naporin0624
      in https://github.com/langgenius/dify/pull/4562'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'chore: add https://api.openai.com placeholder in OpenAI api base by @takatost
      in https://github.com/langgenius/dify/pull/4604'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: support images and tables extract from docx by @JohnJyong in https://github.com/langgenius/dify/pull/4619
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: add qdrant metadata.doc_id index when create qdrant collection by @JohnJyong
      in https://github.com/langgenius/dify/pull/4570
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'feat: add confirm ui by @crazywoola in https://github.com/langgenius/dify/pull/4625'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: Support for Vertex AI by @patryk20120 in https://github.com/langgenius/dify/pull/4586
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'improve: extract method for safe loading yaml file and avoid using PyYaml''s
      FullLoader by @bowenliang123 in https://github.com/langgenius/dify/pull/4031'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'feat: Add WORKFLOW_MAX_EXECUTION_TIME env var by @majian159 in https://github.com/langgenius/dify/pull/4632'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: update lite8k/speed8k/128k max_token to newest by @lingfengchencn in https://github.com/langgenius/dify/pull/4636
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'feat: update notion extractor by @badbye in https://github.com/langgenius/dify/pull/3898'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'feat: Support for Vertex AI - load Default Application Configuration by
      @miendinh in https://github.com/langgenius/dify/pull/4641'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: Feat/upgrade check i18n scripts by @crazywoola in https://github.com/langgenius/dify/pull/4671
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: 'feat: workflow new nodes by @zxhlyh in https://github.com/langgenius/dify/pull/4683'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: Feat/workflow phase2 by @Yeuoly in https://github.com/langgenius/dify/pull/4687
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: ':wrench: Add env variable for time signature by @patryk20120 in https://github.com/langgenius/dify/pull/4650'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  - quote: version to 0.6.9 by @takatost in https://github.com/langgenius/dify/pull/4692
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.9
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 60-other-changes-in-0-6-9
  source_release: dify-2024-05-27-0-6-9-github-157655872-c2725bb5
  source_type: github_releases
  theme: uncategorized
  title: 60 other changes in 0.6.9
  type: change
source_release: '[[Releases/Dify/dify-2024-05-27-0-6-9-github-157655872-c2725bb5|dify-2024-05-27-0-6-9-github-157655872-c2725bb5]]'
source_type: github_releases
theme: uncategorized
title: 60 other changes in 0.6.9
type: change
---

<!-- chronolog:begin region="header" -->
# 60 other changes in 0.6.9

**Dify** · 2024-05-27 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.6.9) · from [[Releases/Dify/dify-2024-05-27-0-6-9-github-157655872-c2725bb5|v0.6.9 Workflow as Tool]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> We’ve been working on enhancing our workflow capabilities lately. Today we’ve got some news:

> https://github.com/langgenius/dify/assets/5485478/3e9a237a-2340-4cb1-a4a6-0b7a396a810c

> Make sure the input is an array. Each item in the array will be processed sequentially by the iteration node until all items are addressed. For instance, if you require a lengthy article, simply input several headlines. This will result in an article containing a paragraph for each headline, freeing you from the need for complex prompt orchestration.

> We’ve updated our UI to be more intuitive and easier to use, with improved classification.

> **Vertex AI Support**: Added support for Vertex AI by @patryk20120 in #4586 and @miendinh in #4641.

> **Claude Stream Tool Call**: Enhanced Claude stream tool call by @Yeuoly in #4469.

> **Chat Custom Disclaimer**: You can add custom disclaimers in WebApp by @patryk20120 in #4306.

> **MiniMax Mode Sensitive Info Masking**: Added parameter config for masking sensitive info in MiniMax mode by @zhangever in #4294.

> **Jina Search & Reader CSS Selectors**: Added CSS selectors for Jina Search & Reader by @rennokki in #4523.

> **Images and Tables Extraction from DOCX**: Now supports extracting images and tables from DOCX files by @JohnJyong in #4619.

> **WORKFLOW_MAX_EXECUTION_TIME**: Added environment variable for max workflow execution time by @majian159 in #4632.

> **Image Preview URL expire Env Variable**: Added environment variable for time signature of image preview url by @patryk20120 in #4650.

> For additional enhancements and updates, refer to the What's Changed section below.

> Get the latest code from the main branch:

> Stop API server, Worker and Web frontend Server.

> Update Python dependencies:

> Then, let's run the migration script:

> Finally, run API server, Worker and Web frontend Server again.

> Create README_KR.md by @leejoo0 in https://github.com/langgenius/dify/pull/4364

> improve the code readability of http_executor node by @hjlarry in https://github.com/langgenius/dify/pull/4360

> feat: Use Romanian & other langs in QA by @rennokki in https://github.com/langgenius/dify/pull/4205

> docs: Add CONTRIBUTING_JA.md by @shutootaki in https://github.com/langgenius/dify/pull/4383

> Optimize webscraper by @charli117 in https://github.com/langgenius/dify/pull/4392

> chore: remove useless code in knowledge_retrieval_node by @VoidIsVoid in https://github.com/langgenius/dify/pull/4412

> Custom sqlalchemy database uri scheme is supported by @xtuhcy in https://github.com/langgenius/dify/pull/4367

> Remove useless code by @GarfieldDai in https://github.com/langgenius/dify/pull/4416

> feat: add pre ping for sqlalchemy configuration by @takatost in https://github.com/langgenius/dify/pull/4454

> improve: exract Code Node provider for each supported scripting language by @bowenliang123 in https://github.com/langgenius/dify/pull/4164

> enhance: claude stream tool call by @Yeuoly in https://github.com/langgenius/dify/pull/4469

> chore: update docker-compose.yaml by @eltociear in https://github.com/langgenius/dify/pull/4492

> Feat/chat custom disclaimer by @patryk20120 in https://github.com/langgenius/dify/pull/4306

> chore: skip unnecessary key checks prior to accessing a dictionary by @bowenliang123 in https://github.com/langgenius/dify/pull/4497

> chore: sort categories in recommended app service response by @BenjaminX in https://github.com/langgenius/dify/pull/4498

> feat:Provide parameter config for mask_sensitive_info of MiniMax mode… by @zhangever in https://github.com/langgenius/dify/pull/4294

> Add UNSTRUCTURED_API_KEY env support by @majian159 in https://github.com/langgenius/dify/pull/4369

> improve: generalize transformations and scripts of runner and preloads into TemplateTransformer by @bowenliang123 in https://github.com/langgenius/dify/pull/4487

> chore: apply and fix flake8-bugbear lint rules by @bowenliang123 in https://github.com/langgenius/dify/pull/4496

> feat: Jina Search & Jina Reader CSS selectors by @rennokki in https://github.com/langgenius/dify/pull/4523

> chore: update yfinance dependency to version 0.2.40 by @BenjaminX in https://github.com/langgenius/dify/pull/4517

> Bump oss2 to 2.18.5 for AuthV4 support by @denverdino in https://github.com/langgenius/dify/pull/4425

> oauth2 supports. by @GarfieldDai in https://github.com/langgenius/dify/pull/4551

> add qdrant metadata.doc_id index by @JohnJyong in https://github.com/langgenius/dify/pull/4559

> chore: Hide the copy button when there is no content to copy by @hjlarry in https://github.com/langgenius/dify/pull/4546

> Refactor part of the ProviderManager code to improve readability by @hjlarry in https://github.com/langgenius/dify/pull/4524

> chore(api): Use channel from UI as API query parameter by @naporin0624 in https://github.com/langgenius/dify/pull/4562

> chore: add https://api.openai.com placeholder in OpenAI api base by @takatost in https://github.com/langgenius/dify/pull/4604

> support images and tables extract from docx by @JohnJyong in https://github.com/langgenius/dify/pull/4619

> add qdrant metadata.doc_id index when create qdrant collection by @JohnJyong in https://github.com/langgenius/dify/pull/4570

> feat: add confirm ui by @crazywoola in https://github.com/langgenius/dify/pull/4625

> Support for Vertex AI by @patryk20120 in https://github.com/langgenius/dify/pull/4586

> improve: extract method for safe loading yaml file and avoid using PyYaml's FullLoader by @bowenliang123 in https://github.com/langgenius/dify/pull/4031

> feat: Add WORKFLOW_MAX_EXECUTION_TIME env var by @majian159 in https://github.com/langgenius/dify/pull/4632

> update lite8k/speed8k/128k max_token to newest by @lingfengchencn in https://github.com/langgenius/dify/pull/4636

> feat: update notion extractor by @badbye in https://github.com/langgenius/dify/pull/3898

> feat: Support for Vertex AI - load Default Application Configuration by @miendinh in https://github.com/langgenius/dify/pull/4641

> Feat/upgrade check i18n scripts by @crazywoola in https://github.com/langgenius/dify/pull/4671

> feat: workflow new nodes by @zxhlyh in https://github.com/langgenius/dify/pull/4683

> Feat/workflow phase2 by @Yeuoly in https://github.com/langgenius/dify/pull/4687

> :wrench: Add env variable for time signature by @patryk20120 in https://github.com/langgenius/dify/pull/4650

> version to 0.6.9 by @takatost in https://github.com/langgenius/dify/pull/4692

Source: https://github.com/langgenius/dify/releases/tag/0.6.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-05-27-allow-to-config-max-segmentation-tokens-length-for-rag-document-using-environmen|allow to config max segmentation tokens length for RAG document using environment variable]] · Context Window
- [[Changes/Dify/2024-05-27-rag-document-segmentation-configurable-max-segmentation-tokens-length-for-rag-do|RAG Document Segmentation]] · Files and Data
- [[Changes/Dify/2024-05-27-improved-variable-assigner-supports-more-flexible-variable-selection-additionall|Improved Variable Assigner supports more flexible variable selection]] · Interface Experience
- [[Changes/Dify/2024-05-27-update-docker-compose-yaml-new-debug-variable-by-theysua-in-https-github-com-lan|Update docker-compose.yaml- New DEBUG variable]] · Developer Workflow
- [[Changes/Dify/2024-05-27-general-fixes-various-bug-fixes-and-improvements-to-enhance-stability-and-perfor|General Fixes: Various bug fixes and improvements to enhance stability and performance]] · Reliability and Performance
- [[Changes/Dify/2024-05-27-2-pricing-model-changes-in-0-6-9|2 Pricing Model changes in 0.6.9]] · Pricing Model
- [[Changes/Dify/2024-05-27-13-model-support-changes-in-0-6-9|13 Model Support changes in 0.6.9]] · Model Support
- [[Changes/Dify/2024-05-27-you-can-now-publish-your-ai-workflow-in-dify-as-a-reusable-tool-this-allows-for|Publish your AI workflow in Dify as a reusable tool]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-05-27-f27caf&body=Card%3A%20Changes%2FDify%2F2024-05-27-60-other-changes-in-0-6-9.md%0ACard%20ID%3A%20dify-2024-05-27-f27caf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.6.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->