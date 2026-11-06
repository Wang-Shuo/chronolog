---
card_id: dify-2024-09-30-4750fc
date: '2024-09-30'
description: 'Dify · 2024-09-30 · Other changes: 58 changes in v0.9.0 — **External
  Knowledge API**: Now you can connect to third-party knowledge bases seamlessly (introduced…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d1a2e64e219ee68a31eca98289ff11a54419ac850e40c878eb73c0756812acf9
product: dify
product_name: Dify
record:
  card_id: dify-2024-09-30-4750fc
  comparison: ''
  date: '2024-09-30'
  description: 'Dify — v0.9.0: 58 other changes'
  evidence:
  - quote: '**External Knowledge API**: Now you can connect to third-party knowledge
      bases seamlessly (introduced by @JohnJyong in #8913).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: '![img_v3_02f7_b73507d9-c144-4a1d-acf4-caccec69b99g](https://github.com/user-attachments/assets/937eed02-1c8f-4635-9ba6-f3464b3a3bfe)'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Simply provide the API endpoint, API key, and external knowledge ID to
      link with the external knowledge base.
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Supports retrieval and recall of external knowledge based on user queries.
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'Introduced **InternLM 2.5-20b** and **Qwen 2.5-coder-7b** (@hwzhuhao in
      #8862).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: '**Xinference TTS Stream Mode**: Now live for a smoother text-to-speech
      experience (@leslie2046 in #8616).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'Improved **SVG output UX** for a more seamless design experience (@xuzuodong
      in #8765).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'Extended **Jina Embeddings** V3 API parameters (@DresAaron in #8657).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'Added **Min-connections and Max-connections** settings for pgvector (@hwzhuhao
      in #8841).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'Enhanced operational flexibility with fully configurable **WORKFLOW_*
      environment variables** (@fujita-h in #8644).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'Upgraded **ElasticSearch** from 8.14.x to 8.15.x to keep our infrastructure
      up-to-date (@bowenliang123 in #8197).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'Enhanced documentation to clarify the importance of **Celery Service**
      (@fchange in #8558).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'Updated configurations in **docker-compose** files and related docs (@saifeiLee
      and others in #8516 and #8691).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: '> [!WARNING]'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: '> The `docker-compose.yaml` has been refactored. If you''ve made any changes
      to the file, make sure to check out the "Upgrade to new docker compose deployment"
      section above for usage and migration tips.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Back up your customized docker-compose YAML file (optional)
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Get the latest code from the main branch
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Back up data
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Upgrade services
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Stop API server, Worker and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Finally, run API server, Worker and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'chore: translate i18n files by @github-actions in https://github.com/langgenius/dify/pull/8557'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Enhance Readme Documentation to Clarify the Importance of Celery Service
      by @fchange in https://github.com/langgenius/dify/pull/8558
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'docs: Update ssrf_proxy related doc link in docker-compose file by @saifeiLee
      in https://github.com/langgenius/dify/pull/8516'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'refactor(ops): Optimize the iteration for filter_none_values and use logging.error
      to record logs when an exception occurs by @hwzhuhao in https://github.com/langgenius/dify/pull/8461'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: update pyproject.toml by @ZhouhaoJiang in https://github.com/langgenius/dify/pull/8368'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'docs: Add Japanese documentation for tools by @totsukash in https://github.com/langgenius/dify/pull/8469'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: feat:use xinference tts stream mode by @leslie2046 in https://github.com/langgenius/dify/pull/8616
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat(tools/cogview): Updated cogview tool to support cogview-3 and the
      latest cogview-3-plus by @ox01024 in https://github.com/langgenius/dify/pull/8382'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'chore: enhance configuration descriptions by @ZuzooVn in https://github.com/langgenius/dify/pull/8624'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Make WORKFLOW_* configurable as environment variables. by @fujita-h in
      https://github.com/langgenius/dify/pull/8644
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'chore: Enable Japanese descriptions for Tools by @totsukash in https://github.com/langgenius/dify/pull/8646'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: extend api params for Jina Embeddings V3 by @DresAaron in https://github.com/langgenius/dify/pull/8657'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: add Spark Max-32K by @AAEE86 in https://github.com/langgenius/dify/pull/8676
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: add xinference sd web ui api tool by @themanforfree in https://github.com/langgenius/dify/pull/8385'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'chore: remove windows platform timezone set by @hjlarry in https://github.com/langgenius/dify/pull/8712'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: add embedding input type parameter by @JohnJyong in https://github.com/langgenius/dify/pull/8724
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'chore: make url display in the middle of http node by @hjlarry in https://github.com/langgenius/dify/pull/8741'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Add GitHub Actions Workflow for Web Tests by @xuzuodong in https://github.com/langgenius/dify/pull/8753
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'dep: bump ElasticSearch from 8.14.x to 8.15.x by @bowenliang123 in https://github.com/langgenius/dify/pull/8197'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'chore: add input_type param desc for the _invoke method of text_embedding
      by @hwzhuhao in https://github.com/langgenius/dify/pull/8778'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'refactor: update delete method as an abstract method by @hwzhuhao in https://github.com/langgenius/dify/pull/8794'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: improved SVG output UX by @xuzuodong in https://github.com/langgenius/dify/pull/8765'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: Updated the YouTube channel to Dify's by @shaiss in https://github.com/langgenius/dify/pull/8817
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: add pgvecto-rs and analyticdb in docker/.env.example by @hwzhuhao
      in https://github.com/langgenius/dify/pull/8823'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat(Tools): add feishu tools by @hgnulb in https://github.com/langgenius/dify/pull/8800'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat: add min-connection and max-connection for pgvector by @hwzhuhao
      in https://github.com/langgenius/dify/pull/8841'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'refactor: update Callback to an abstract class by @hwzhuhao in https://github.com/langgenius/dify/pull/8868'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'chore: bump ruff to 0.6.8 for fixing violation in SIM910 by @bowenliang123
      in https://github.com/langgenius/dify/pull/8869'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat(website-crawl): add jina reader as additional alternative for website
      crawling by @mapleeit in https://github.com/langgenius/dify/pull/8761'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'feat(api): add version comparison logic by @laipz8200 in https://github.com/langgenius/dify/pull/8902'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'refactor(api/variables): VariableError as a ValueError. by @laipz8200
      in https://github.com/langgenius/dify/pull/8554'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: external knowledge api by @JohnJyong in https://github.com/langgenius/dify/pull/8913
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'chore: translate i18n files by @github-actions in https://github.com/langgenius/dify/pull/8917'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'Feat: add debounce for search in logs by @JzoNgKVO in https://github.com/langgenius/dify/pull/8924'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  - quote: 'chore(versioning): bump version to 0.9.0 by @laipz8200 in https://github.com/langgenius/dify/pull/8911'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 58-other-changes-in-0-9-0
  source_release: dify-2024-09-30-0-9-0-github-177564351-208577ea
  source_type: github_releases
  theme: uncategorized
  title: 58 other changes in 0.9.0
  type: change
source_release: '[[Releases/Dify/dify-2024-09-30-0-9-0-github-177564351-208577ea|dify-2024-09-30-0-9-0-github-177564351-208577ea]]'
source_type: github_releases
theme: uncategorized
title: 58 other changes in 0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 58 other changes in 0.9.0

**Dify** · 2024-09-30 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.9.0) · from [[Releases/Dify/dify-2024-09-30-0-9-0-github-177564351-208577ea|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **External Knowledge API**: Now you can connect to third-party knowledge bases seamlessly (introduced by @JohnJyong in #8913).

> ![img_v3_02f7_b73507d9-c144-4a1d-acf4-caccec69b99g](https://github.com/user-attachments/assets/937eed02-1c8f-4635-9ba6-f3464b3a3bfe)

> Simply provide the API endpoint, API key, and external knowledge ID to link with the external knowledge base.

> Supports retrieval and recall of external knowledge based on user queries.

> Introduced **InternLM 2.5-20b** and **Qwen 2.5-coder-7b** (@hwzhuhao in #8862).

> **Xinference TTS Stream Mode**: Now live for a smoother text-to-speech experience (@leslie2046 in #8616).

> Improved **SVG output UX** for a more seamless design experience (@xuzuodong in #8765).

> Extended **Jina Embeddings** V3 API parameters (@DresAaron in #8657).

> Added **Min-connections and Max-connections** settings for pgvector (@hwzhuhao in #8841).

> Enhanced operational flexibility with fully configurable **WORKFLOW_* environment variables** (@fujita-h in #8644).

> Upgraded **ElasticSearch** from 8.14.x to 8.15.x to keep our infrastructure up-to-date (@bowenliang123 in #8197).

> Enhanced documentation to clarify the importance of **Celery Service** (@fchange in #8558).

> Updated configurations in **docker-compose** files and related docs (@saifeiLee and others in #8516 and #8691).

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

> chore: translate i18n files by @github-actions in https://github.com/langgenius/dify/pull/8557

> Enhance Readme Documentation to Clarify the Importance of Celery Service by @fchange in https://github.com/langgenius/dify/pull/8558

> docs: Update ssrf_proxy related doc link in docker-compose file by @saifeiLee in https://github.com/langgenius/dify/pull/8516

> refactor(ops): Optimize the iteration for filter_none_values and use logging.error to record logs when an exception occurs by @hwzhuhao in https://github.com/langgenius/dify/pull/8461

> feat: update pyproject.toml by @ZhouhaoJiang in https://github.com/langgenius/dify/pull/8368

> docs: Add Japanese documentation for tools by @totsukash in https://github.com/langgenius/dify/pull/8469

> feat:use xinference tts stream mode by @leslie2046 in https://github.com/langgenius/dify/pull/8616

> feat(tools/cogview): Updated cogview tool to support cogview-3 and the latest cogview-3-plus by @ox01024 in https://github.com/langgenius/dify/pull/8382

> chore: enhance configuration descriptions by @ZuzooVn in https://github.com/langgenius/dify/pull/8624

> Make WORKFLOW_* configurable as environment variables. by @fujita-h in https://github.com/langgenius/dify/pull/8644

> chore: Enable Japanese descriptions for Tools by @totsukash in https://github.com/langgenius/dify/pull/8646

> feat: extend api params for Jina Embeddings V3 by @DresAaron in https://github.com/langgenius/dify/pull/8657

> add Spark Max-32K by @AAEE86 in https://github.com/langgenius/dify/pull/8676

> feat: add xinference sd web ui api tool by @themanforfree in https://github.com/langgenius/dify/pull/8385

> chore: remove windows platform timezone set by @hjlarry in https://github.com/langgenius/dify/pull/8712

> add embedding input type parameter by @JohnJyong in https://github.com/langgenius/dify/pull/8724

> chore: make url display in the middle of http node by @hjlarry in https://github.com/langgenius/dify/pull/8741

> Add GitHub Actions Workflow for Web Tests by @xuzuodong in https://github.com/langgenius/dify/pull/8753

> dep: bump ElasticSearch from 8.14.x to 8.15.x by @bowenliang123 in https://github.com/langgenius/dify/pull/8197

> chore: add input_type param desc for the _invoke method of text_embedding by @hwzhuhao in https://github.com/langgenius/dify/pull/8778

> refactor: update delete method as an abstract method by @hwzhuhao in https://github.com/langgenius/dify/pull/8794

> feat: improved SVG output UX by @xuzuodong in https://github.com/langgenius/dify/pull/8765

> Updated the YouTube channel to Dify's by @shaiss in https://github.com/langgenius/dify/pull/8817

> feat: add pgvecto-rs and analyticdb in docker/.env.example by @hwzhuhao in https://github.com/langgenius/dify/pull/8823

> feat(Tools): add feishu tools by @hgnulb in https://github.com/langgenius/dify/pull/8800

> feat: add min-connection and max-connection for pgvector by @hwzhuhao in https://github.com/langgenius/dify/pull/8841

> refactor: update Callback to an abstract class by @hwzhuhao in https://github.com/langgenius/dify/pull/8868

> chore: bump ruff to 0.6.8 for fixing violation in SIM910 by @bowenliang123 in https://github.com/langgenius/dify/pull/8869

> feat(website-crawl): add jina reader as additional alternative for website crawling by @mapleeit in https://github.com/langgenius/dify/pull/8761

> feat(api): add version comparison logic by @laipz8200 in https://github.com/langgenius/dify/pull/8902

> refactor(api/variables): VariableError as a ValueError. by @laipz8200 in https://github.com/langgenius/dify/pull/8554

> external knowledge api by @JohnJyong in https://github.com/langgenius/dify/pull/8913

> chore: translate i18n files by @github-actions in https://github.com/langgenius/dify/pull/8917

> Feat: add debounce for search in logs by @JzoNgKVO in https://github.com/langgenius/dify/pull/8924

> chore(versioning): bump version to 0.9.0 by @laipz8200 in https://github.com/langgenius/dify/pull/8911

Source: https://github.com/langgenius/dify/releases/tag/0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-09-30-2-mobile-and-desktop-changes-in-0-9-0|2 Mobile and Desktop changes in 0.9.0]] · Mobile and Desktop
- [[Changes/Dify/2024-09-30-added-english-versions-for-customizable-model-scale-documentation-to-broaden-acc|Added English versions for customizable model scale documentation to broaden…]] · Accessibility and Localization
- [[Changes/Dify/2024-09-30-2-agent-mode-changes-in-0-9-0|2 Agent Mode changes in 0.9.0]] · Agent Mode
- [[Changes/Dify/2024-09-30-2-developer-workflow-changes-in-0-9-0|2 Developer Workflow changes in 0.9.0]] · Developer Workflow
- [[Changes/Dify/2024-09-30-corrected-a-linking-error-in-help-documents-hjlarry-in-8508|Corrected a linking error in help documents (@hjlarry in ♯8508)]] · Files and Data
- [[Changes/Dify/2024-09-30-4-reliability-and-performance-changes-in-0-9-0|4 Reliability and Performance changes in 0.9.0]] · Reliability and Performance
- [[Changes/Dify/2024-09-30-36-model-support-changes-in-0-9-0|36 Model Support changes in 0.9.0]] · Model Support
- [[Changes/Dify/2024-09-30-3-apps-and-integrations-changes-in-0-9-0|3 Apps and Integrations changes in 0.9.0]] · Apps and Integrations
- [[Changes/Dify/2024-09-30-stream-for-gemini-now-available-aaee86-in-8678-https-github-com-langgenius-dify|Stream for Gemini now available…]] · Model Support
- [[Changes/Dify/2024-09-30-add-zhipuai-web-search-by-aaee86-in-https-github-com-langgenius-dify-pull-8668|add zhipuai web search]] · Search and Browsing
- [[Changes/Dify/2024-09-30-with-this-release-we-re-truly-showcasing-the-power-of-dify-we-appreciate-your-co|With this release, we’re truly showcasing the power of Dify!]] · Collaboration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-09-30-4750fc&body=Card%3A%20Changes%2FDify%2F2024-09-30-58-other-changes-in-0-9-0.md%0ACard%20ID%3A%20dify-2024-09-30-4750fc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->