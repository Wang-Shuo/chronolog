---
card_id: dify-2024-08-19-7a908e
date: '2024-08-19'
description: 'Dify · 2024-08-19 · Other changes: 56 changes in v0.7.1 — Hey everyone,
  we’re excited to bring you version 0.7.1 of our platform! This release is packed
  with…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a9f3ec2bdca825b113057864376f5761de17c2614a43b709371a56925f4ca9ed
product: dify
product_name: Dify
record:
  card_id: dify-2024-08-19-7a908e
  comparison: ''
  date: '2024-08-19'
  description: 'Dify — v0.7.1: 56 other changes'
  evidence:
  - quote: 'Hey everyone, we’re excited to bring you version 0.7.1 of our platform!
      This release is packed with new features, enhancements, and crucial fixes. Let’s
      dive in:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: <img width="769" alt="Screenshot 2024-08-19 at 2 36 27 PM" src="https://github.com/user-attachments/assets/56fb1dd5-2580-4cde-ac6e-01ca036093fd">
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**OpenAI Structured Outputs Support**: Now supporting OpenAI''s Structured
      Outputs by @hjlarry in [#7258](https://github.com/langgenius/dify/pull/7258).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**Jina Tokenizer Tool**: Added a new tokenizer tool by @hjlarry in [#7375](https://github.com/langgenius/dify/pull/7375).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**GitLab Tool**: Integrated GitLab tool by @wlrnet in [#7329](https://github.com/langgenius/dify/pull/7329).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**Ruff Formatter**: Introduced Ruff Formatter for better code formatting
      by @laipz8200 in [#7291](https://github.com/langgenius/dify/pull/7291).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**Ruff Update**: Updated Ruff from 0.5.x to 0.6.x by @bowenliang123 in
      [#7384](https://github.com/langgenius/dify/pull/7384).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**Rearranged API Python Dependencies** by @bowenliang123 in [#7391](https://github.com/langgenius/dify/pull/7391)'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**Rerank Mode Fix**: Fixed missing rerank_mode when converting to DatasetEntity
      by @optionals in [#7269](https://github.com/langgenius/dify/pull/7269).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**Tool Test Modal**: Fixed issue where parameters couldn’t be input in
      tool test modal by @wellCh4n in [#7281](https://github.com/langgenius/dify/pull/7281).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**Markdown Conversion**: Fixed file to markdown conversion issue by @laipz8200
      in [#7293](https://github.com/langgenius/dify/pull/7293).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**Conversation Variables**: Added conversation variables in app DSL service
      by @laipz8200 in [#7304](https://github.com/langgenius/dify/pull/7304).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**Node and Edge Issues**: Fixed inability to add node and change the edge
      by @aixgeek in [#7303](https://github.com/langgenius/dify/pull/7303).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**Default Values**: Fixed missing default value of type array object in
      conversation variable modal by @JzoNgKVO in [#7309](https://github.com/langgenius/dify/pull/7309).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**Elasticsearch Docker Env**: Fixed docker environment for Elasticsearch
      by @QIN2DIM in [#7270](https://github.com/langgenius/dify/pull/7270).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**Run History**: Corrected iteration times number in run history by @iamjoel
      in [#7318](https://github.com/langgenius/dify/pull/7318).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**Keywords Fix**: Fixed keywords issue by @crazywoola in [#7357](https://github.com/langgenius/dify/pull/7357).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**Workflow Variables**: Added conversation variable to workflow by @laipz8200
      in [#7257](https://github.com/langgenius/dify/pull/7257).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**Japanese Translation**: Added JP translation for variable aggregator
      by @HanqingZ in [#7277](https://github.com/langgenius/dify/pull/7277).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '**Fixes in Japanese Translations**: Corrected translations of secret values
      by @yukyu30 in [#7279](https://github.com/langgenius/dify/pull/7279).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: That’s all for this release! As always, thank you for your contributions
      and feedback. Keep building and innovating!
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '> [!WARNING]'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: '> The `docker-compose.yaml` has been refactored. If you''ve made any changes
      to the file, make sure to check out the "Upgrade to new docker compose deployment"
      section above for usage and migration tips.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: Back up your customized docker-compose YAML file (optional)
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: Get the latest code from the main branch
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: Back up data
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: Upgrade services
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: Stop API server, Worker and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: Finally, run API server, Worker and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: Add jp translation for variable aggregator by @HanqingZ in https://github.com/langgenius/dify/pull/7277
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'feat(api/workflow): Add `Conversation.dialogue_count` by @laipz8200 in
      https://github.com/langgenius/dify/pull/7275'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'feat: add chatgpt-4o-latest by @hjlarry in https://github.com/langgenius/dify/pull/7289'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'feat: support OPENAI json_schema by @hjlarry in https://github.com/langgenius/dify/pull/7258'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'chore(api/core): Improve FileVar''s type hint and imports. by @laipz8200
      in https://github.com/langgenius/dify/pull/7290'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'chore(api): Introduce Ruff Formatter. by @laipz8200 in https://github.com/langgenius/dify/pull/7291'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'chore(api/libs): Apply ruff format. by @laipz8200 in https://github.com/langgenius/dify/pull/7301'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'chore: #7222 i18n by @ZuzooVn in https://github.com/langgenius/dify/pull/7312'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: add some api to DifyClient by @lingfengchencn in https://github.com/langgenius/dify/pull/7314
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'chore: delete unused resources POSTGRES_MAX_CONNECTIONS by @ZuzooVn in
      https://github.com/langgenius/dify/pull/7315'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'chore(api/libs/bearer_data_source.py): Remove expired fie. by @laipz8200
      in https://github.com/langgenius/dify/pull/7300'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'chore: update docstrings by @ZuzooVn in https://github.com/langgenius/dify/pull/7343'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'feat: tools/gitlab by @wlrnet in https://github.com/langgenius/dify/pull/7329'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: add workflowClient ,fix rename bug by @lingfengchencn in https://github.com/langgenius/dify/pull/7352
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'feat: support siliconflow rerank by @Weaxs in https://github.com/langgenius/dify/pull/7337'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'chore: add LOG_FILE to docker-compose by @ZuzooVn in https://github.com/langgenius/dify/pull/7372'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'feat(api): support wenxin text embedding by @CheneyYin in https://github.com/langgenius/dify/pull/7377'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'feat: add jina tokenizer tool by @hjlarry in https://github.com/langgenius/dify/pull/7375'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'feat: custom app icon by @xuzuodong in https://github.com/langgenius/dify/pull/7196'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'chore: update ruff from 0.5.x to 0.6.x by @bowenliang123 in https://github.com/langgenius/dify/pull/7384'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'feat: support xinference''s auth system by @ethan-fly in https://github.com/langgenius/dify/pull/7369'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'chore: rearrange api python dependencies by @bowenliang123 in https://github.com/langgenius/dify/pull/7391'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'Feat: shortcut hook by @YIXIAO0 in https://github.com/langgenius/dify/pull/7385'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'add CrossRef builtin tool: doi query and title query by @Sakura4036 in
      https://github.com/langgenius/dify/pull/7406'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  - quote: 'chore(*): Bump version 0.7.1 by @laipz8200 in https://github.com/langgenius/dify/pull/7389'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 56-other-changes-in-0-7-1
  source_release: dify-2024-08-19-0-7-1-github-170870367-4677435e
  source_type: github_releases
  theme: uncategorized
  title: 56 other changes in 0.7.1
  type: change
source_release: '[[Releases/Dify/dify-2024-08-19-0-7-1-github-170870367-4677435e|dify-2024-08-19-0-7-1-github-170870367-4677435e]]'
source_type: github_releases
theme: uncategorized
title: 56 other changes in 0.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 56 other changes in 0.7.1

**Dify** · 2024-08-19 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.7.1) · from [[Releases/Dify/dify-2024-08-19-0-7-1-github-170870367-4677435e|v0.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hey everyone, we’re excited to bring you version 0.7.1 of our platform! This release is packed with new features, enhancements, and crucial fixes. Let’s dive in:

> \<img width="769" alt="Screenshot 2024-08-19 at 2 36 27 PM" src="https://github.com/user-attachments/assets/56fb1dd5-2580-4cde-ac6e-01ca036093fd">

> **OpenAI Structured Outputs Support**: Now supporting OpenAI's Structured Outputs by @hjlarry in [#7258](https://github.com/langgenius/dify/pull/7258).

> **Jina Tokenizer Tool**: Added a new tokenizer tool by @hjlarry in [#7375](https://github.com/langgenius/dify/pull/7375).

> **GitLab Tool**: Integrated GitLab tool by @wlrnet in [#7329](https://github.com/langgenius/dify/pull/7329).

> **Ruff Formatter**: Introduced Ruff Formatter for better code formatting by @laipz8200 in [#7291](https://github.com/langgenius/dify/pull/7291).

> **Ruff Update**: Updated Ruff from 0.5.x to 0.6.x by @bowenliang123 in [#7384](https://github.com/langgenius/dify/pull/7384).

> **Rearranged API Python Dependencies** by @bowenliang123 in [#7391](https://github.com/langgenius/dify/pull/7391)

> **Rerank Mode Fix**: Fixed missing rerank_mode when converting to DatasetEntity by @optionals in [#7269](https://github.com/langgenius/dify/pull/7269).

> **Tool Test Modal**: Fixed issue where parameters couldn’t be input in tool test modal by @wellCh4n in [#7281](https://github.com/langgenius/dify/pull/7281).

> **Markdown Conversion**: Fixed file to markdown conversion issue by @laipz8200 in [#7293](https://github.com/langgenius/dify/pull/7293).

> **Conversation Variables**: Added conversation variables in app DSL service by @laipz8200 in [#7304](https://github.com/langgenius/dify/pull/7304).

> **Node and Edge Issues**: Fixed inability to add node and change the edge by @aixgeek in [#7303](https://github.com/langgenius/dify/pull/7303).

> **Default Values**: Fixed missing default value of type array object in conversation variable modal by @JzoNgKVO in [#7309](https://github.com/langgenius/dify/pull/7309).

> **Elasticsearch Docker Env**: Fixed docker environment for Elasticsearch by @QIN2DIM in [#7270](https://github.com/langgenius/dify/pull/7270).

> **Run History**: Corrected iteration times number in run history by @iamjoel in [#7318](https://github.com/langgenius/dify/pull/7318).

> **Keywords Fix**: Fixed keywords issue by @crazywoola in [#7357](https://github.com/langgenius/dify/pull/7357).

> **Workflow Variables**: Added conversation variable to workflow by @laipz8200 in [#7257](https://github.com/langgenius/dify/pull/7257).

> **Japanese Translation**: Added JP translation for variable aggregator by @HanqingZ in [#7277](https://github.com/langgenius/dify/pull/7277).

> **Fixes in Japanese Translations**: Corrected translations of secret values by @yukyu30 in [#7279](https://github.com/langgenius/dify/pull/7279).

> That’s all for this release! As always, thank you for your contributions and feedback. Keep building and innovating!

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

> Add jp translation for variable aggregator by @HanqingZ in https://github.com/langgenius/dify/pull/7277

> feat(api/workflow): Add `Conversation.dialogue_count` by @laipz8200 in https://github.com/langgenius/dify/pull/7275

> feat: add chatgpt-4o-latest by @hjlarry in https://github.com/langgenius/dify/pull/7289

> feat: support OPENAI json_schema by @hjlarry in https://github.com/langgenius/dify/pull/7258

> chore(api/core): Improve FileVar's type hint and imports. by @laipz8200 in https://github.com/langgenius/dify/pull/7290

> chore(api): Introduce Ruff Formatter. by @laipz8200 in https://github.com/langgenius/dify/pull/7291

> chore(api/libs): Apply ruff format. by @laipz8200 in https://github.com/langgenius/dify/pull/7301

> chore: #7222 i18n by @ZuzooVn in https://github.com/langgenius/dify/pull/7312

> add some api to DifyClient by @lingfengchencn in https://github.com/langgenius/dify/pull/7314

> chore: delete unused resources POSTGRES_MAX_CONNECTIONS by @ZuzooVn in https://github.com/langgenius/dify/pull/7315

> chore(api/libs/bearer_data_source.py): Remove expired fie. by @laipz8200 in https://github.com/langgenius/dify/pull/7300

> chore: update docstrings by @ZuzooVn in https://github.com/langgenius/dify/pull/7343

> feat: tools/gitlab by @wlrnet in https://github.com/langgenius/dify/pull/7329

> add workflowClient ,fix rename bug by @lingfengchencn in https://github.com/langgenius/dify/pull/7352

> feat: support siliconflow rerank by @Weaxs in https://github.com/langgenius/dify/pull/7337

> chore: add LOG_FILE to docker-compose by @ZuzooVn in https://github.com/langgenius/dify/pull/7372

> feat(api): support wenxin text embedding by @CheneyYin in https://github.com/langgenius/dify/pull/7377

> feat: add jina tokenizer tool by @hjlarry in https://github.com/langgenius/dify/pull/7375

> feat: custom app icon by @xuzuodong in https://github.com/langgenius/dify/pull/7196

> chore: update ruff from 0.5.x to 0.6.x by @bowenliang123 in https://github.com/langgenius/dify/pull/7384

> feat: support xinference's auth system by @ethan-fly in https://github.com/langgenius/dify/pull/7369

> chore: rearrange api python dependencies by @bowenliang123 in https://github.com/langgenius/dify/pull/7391

> Feat: shortcut hook by @YIXIAO0 in https://github.com/langgenius/dify/pull/7385

> add CrossRef builtin tool: doi query and title query by @Sakura4036 in https://github.com/langgenius/dify/pull/7406

> chore(*): Bump version 0.7.1 by @laipz8200 in https://github.com/langgenius/dify/pull/7389

Source: https://github.com/langgenius/dify/releases/tag/0.7.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-08-19-3-editor-experience-changes-in-0-7-1|3 Editor Experience changes in 0.7.1]] · Editor Experience
- [[Changes/Dify/2024-08-19-7-model-support-changes-in-0-7-1|7 Model Support changes in 0.7.1]] · Model Support
- [[Changes/Dify/2024-08-19-general-i18n-updates-various-internationalization-updates-by-zuzoovn-in-7312-htt|General i18n Updates]] · Accessibility and Localization
- [[Changes/Dify/2024-08-19-stop-the-service-command-please-execute-in-the-docker-directory|Stop the service，Command, please execute in the docker directory]] · Developer Workflow
- [[Changes/Dify/2024-08-19-custom-app-icons-personalize-your-apps-with-custom-icons-by-xuzuodong-in-7196-ht|Custom App Icons]] · Apps and Integrations
- [[Changes/Dify/2024-08-19-enh-setfocus-after-voice-input-by-leslie2046-in-https-github-com-langgenius-dify|enh:setfocus after voice input]] · Voice and Audio
- [[Changes/Dify/2024-08-19-xinference-auth-system-enhanced-support-for-xinference-s-authentication-system-b|Xinference Auth System]] · Account and Access
- [[Changes/Dify/2024-08-19-2-safety-and-privacy-changes-in-0-7-1|2 Safety and Privacy changes in 0.7.1]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-08-19-7a908e&body=Card%3A%20Changes%2FDify%2F2024-08-19-56-other-changes-in-0-7-1.md%0ACard%20ID%3A%20dify-2024-08-19-7a908e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->