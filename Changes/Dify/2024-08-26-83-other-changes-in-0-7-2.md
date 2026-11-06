---
card_id: dify-2024-08-26-53cc2e
date: '2024-08-26'
description: 'Dify · 2024-08-26 · Other changes: 83 changes in v0.7.2 — Hey everyone,
  we’re excited to bring you version 0.7.2 of our platform. This release is packed
  with…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b12a7a40a6e4a7823cbfe949fd1c6e13dd409321f6f57bd251dd16651f18b870
product: dify
product_name: Dify
record:
  card_id: dify-2024-08-26-53cc2e
  comparison: ''
  date: '2024-08-26'
  description: 'Dify — v0.7.2: 83 other changes'
  evidence:
  - quote: 'Hey everyone, we’re excited to bring you version 0.7.2 of our platform.
      This release is packed with new features, enhancements, and bug fixes to make
      your experience even better. Here’s a quick rundown:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Added support for dialogue count in chatflow by @iamjoel in #7440.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Added support for Qwen text-embedding-v3 by @droxer in #7567.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Added support for the siliconflow text2img tool by @hjlarry in #7612.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Added support for the OneBot protocol tool by @RockChinQ in #7583.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: '**UI/UX Improvements**:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Improved the copywrite of the assigner node append mode description by
      @iamjoel in #7467.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Updated theme-related CSS variables values by @iamjoel in #7442.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Added Langfuse view button by @charli117 in #7578.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Updated the "tag delete" confirm modal by @YIXIAO0 in #7522.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: '**Backend Improvements**:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Applied Ruff reformatting across various API components by @bowenliang123
      in #7590, #7591, #7594, #7599, and @laipz8200 in #7645.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Support for CODE_MAX_PRECISION by @ZuzooVn in #7484.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Increased max steps to 50 in workflows by @takatost in #4252.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Added support for pgvector full-text search setting by @JohnJyong in #7427.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Added support for sorting conversations by updated_at desc by @KinWang130
      in #7348.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Create S3 bucket if it doesn''t exist by @moyueheng in #7514.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Added storage type and Google Storage settings to worker by @KiyotakaMatsushita
      in #4266.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Updated certbot/README.md by @eltociear in #7528.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Added CONTRIBUTING_VI i18n by @ZuzooVn in #7532.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: "That’s all for this release! As always, thank you for your contributions
      and feedback. Keep them coming, and happy coding! \U0001F680"
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: '> [!WARNING]'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: '> The `docker-compose.yaml` has been refactored. If you''ve made any changes
      to the file, make sure to check out the "Upgrade to new docker compose deployment"
      section above for usage and migration tips.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Back up your customized docker-compose YAML file (optional)
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Get the latest code from the main branch
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Back up data
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Upgrade services
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Stop API server, Worker and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Finally, run API server, Worker and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Web app support sending message using numpad enter by @xuzuodong in https://github.com/langgenius/dify/pull/7414
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore: correct _tts_invoke_streaming max length by @ZuzooVn in https://github.com/langgenius/dify/pull/7423'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore: #7196 i18n by @ZuzooVn in https://github.com/langgenius/dify/pull/7416'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'feat: add pgvector full_text_search by @jasonkang14 in https://github.com/langgenius/dify/pull/7396'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: add pgvector full text search settting by @JohnJyong in https://github.com/langgenius/dify/pull/7427
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore(database): Rename table name from `workflow__conversation_variables`
      to `workflow_conversation_variables`. by @laipz8200 in https://github.com/langgenius/dify/pull/7432'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore: remove .idea and .vscode from root path by @Yeuoly in https://github.com/langgenius/dify/pull/7437'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'refactor(api/core/workflow/nodes/variable_assigner): Split into multi
      files. by @laipz8200 in https://github.com/langgenius/dify/pull/7434'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore: add and update theme related css variables values by @iamjoel in
      https://github.com/langgenius/dify/pull/7442'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'refactor(api/core/app/app_config/entities.py): Move Type to outside and
      add EXTERNAL_DATA_TOOL. by @laipz8200 in https://github.com/langgenius/dify/pull/7444'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'refactor(api/core/workflow/enums.py): Rename SystemVariable to SystemVariableKey.
      by @laipz8200 in https://github.com/langgenius/dify/pull/7445'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'feat: Sort conversations by updated_at desc by @KinWang130 in https://github.com/langgenius/dify/pull/7348'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'feat: support dialogue count in chatflow by @iamjoel in https://github.com/langgenius/dify/pull/7440'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore: #7348 i18n by @ZuzooVn in https://github.com/langgenius/dify/pull/7451'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore: improve the copywrite of the assigner node append mode description
      by @iamjoel in https://github.com/langgenius/dify/pull/7467'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Separate CODE_MAX_DEPTH and set it as an environment variable by @Hisir0909
      in https://github.com/langgenius/dify/pull/7474
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'feat: support CODE_MAX_PRECISION by @ZuzooVn in https://github.com/langgenius/dify/pull/7484'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Chore/remove python dependencies selector by @Yeuoly in https://github.com/langgenius/dify/pull/7494
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: "feat(storage): \U0001F41B Create S3 bucket if it doesn't exist by @moyueheng
      in https://github.com/langgenius/dify/pull/7514"
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'feat: update the "tag delete" confirm modal by @YIXIAO0 in https://github.com/langgenius/dify/pull/7522'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'docs: update certbot/README.md by @eltociear in https://github.com/langgenius/dify/pull/7528'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'docs: CONTRIBUTING_VI i18n by @ZuzooVn in https://github.com/langgenius/dify/pull/7532'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: update nltk version to 3.8.1 by @JohnJyong in https://github.com/langgenius/dify/pull/7544
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Added Space between Chinese and English within tools' description by @AllenWriter
      in https://github.com/langgenius/dify/pull/7545
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Add N-to-1 warning translation for JP by @HanqingZ in https://github.com/langgenius/dify/pull/7553
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'feat: forward zhipu finish_reason by @orangeclk in https://github.com/langgenius/dify/pull/7560'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore: #6554 i18n by @ZuzooVn in https://github.com/langgenius/dify/pull/7562'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'feat: set workflow zoom range for shortcut by @YIXIAO0 in https://github.com/langgenius/dify/pull/7563'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore: improve the check time of variable name by @iamjoel in https://github.com/langgenius/dify/pull/7569'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore: improve the check time of variable name in conversation and env
      var by @iamjoel in https://github.com/langgenius/dify/pull/7572'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: add qwen text-embedding-v3 support. by @droxer in https://github.com/langgenius/dify/pull/7567
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: langfuser add view button by @charli117 in https://github.com/langgenius/dify/pull/7571
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Langfuse view button by @charli117 in https://github.com/langgenius/dify/pull/7578
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Do not pass query parameter when the value is empty by @AmosZhu in https://github.com/langgenius/dify/pull/7585
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Update stable_diffusion.py by @flingjie in https://github.com/langgenius/dify/pull/7536
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'Feat: add OneBot protocol tool by @RockChinQ in https://github.com/langgenius/dify/pull/7583'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore: cleanup and rearrange unclassified configs into feature config
      groups by @bowenliang123 in https://github.com/langgenius/dify/pull/7586'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore(api/configs): apply ruff reformat by @bowenliang123 in https://github.com/langgenius/dify/pull/7590'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore(api/tests): apply ruff reformat #7590 by @bowenliang123 in https://github.com/langgenius/dify/pull/7591'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Improve MIME type detection for image URLs by @Seayon in https://github.com/langgenius/dify/pull/6531
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'feat: add siliconflow text2img tool by @hjlarry in https://github.com/langgenius/dify/pull/7612'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'feat: web sso by @ZhouhaoJiang in https://github.com/langgenius/dify/pull/7135'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Web app now supports SSO config by @douxc in https://github.com/langgenius/dify/pull/7137
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'feat: replace show/hide workflow_steps with switch by @crazywoola in https://github.com/langgenius/dify/pull/7627'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore(api/tasks): apply ruff reformatting by @bowenliang123 in https://github.com/langgenius/dify/pull/7594'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore(api/services): apply ruff reformatting by @bowenliang123 in https://github.com/langgenius/dify/pull/7599'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore(api/controllers): Apply Ruff Formatter. by @laipz8200 in https://github.com/langgenius/dify/pull/7645'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: '[fix] openai''s tool role dose not support name parameter. by @sydnash
      in https://github.com/langgenius/dify/pull/7659'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: Proposal to revise Japanese expressions by @snickerjp in https://github.com/langgenius/dify/pull/7664
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: catch openai rate limit error by @JohnJyong in https://github.com/langgenius/dify/pull/7658
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'refactor: Add @staticmethod decorator in `api/core` by @totsukash in https://github.com/langgenius/dify/pull/7652'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  - quote: 'chore: Update version to 0.7.2 by @laipz8200 in https://github.com/langgenius/dify/pull/7646'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 83-other-changes-in-0-7-2
  source_release: dify-2024-08-26-0-7-2-github-171932546-d3609102
  source_type: github_releases
  theme: uncategorized
  title: 83 other changes in 0.7.2
  type: change
source_release: '[[Releases/Dify/dify-2024-08-26-0-7-2-github-171932546-d3609102|dify-2024-08-26-0-7-2-github-171932546-d3609102]]'
source_type: github_releases
theme: uncategorized
title: 83 other changes in 0.7.2
type: change
---

<!-- chronolog:begin region="header" -->
# 83 other changes in 0.7.2

**Dify** · 2024-08-26 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.7.2) · from [[Releases/Dify/dify-2024-08-26-0-7-2-github-171932546-d3609102|v0.7.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hey everyone, we’re excited to bring you version 0.7.2 of our platform. This release is packed with new features, enhancements, and bug fixes to make your experience even better. Here’s a quick rundown:

> Added support for dialogue count in chatflow by @iamjoel in #7440.

> Added support for Qwen text-embedding-v3 by @droxer in #7567.

> Added support for the siliconflow text2img tool by @hjlarry in #7612.

> Added support for the OneBot protocol tool by @RockChinQ in #7583.

> **UI/UX Improvements**:

> Improved the copywrite of the assigner node append mode description by @iamjoel in #7467.

> Updated theme-related CSS variables values by @iamjoel in #7442.

> Added Langfuse view button by @charli117 in #7578.

> Updated the "tag delete" confirm modal by @YIXIAO0 in #7522.

> **Backend Improvements**:

> Applied Ruff reformatting across various API components by @bowenliang123 in #7590, #7591, #7594, #7599, and @laipz8200 in #7645.

> Support for CODE_MAX_PRECISION by @ZuzooVn in #7484.

> Increased max steps to 50 in workflows by @takatost in #4252.

> Added support for pgvector full-text search setting by @JohnJyong in #7427.

> Added support for sorting conversations by updated_at desc by @KinWang130 in #7348.

> Create S3 bucket if it doesn't exist by @moyueheng in #7514.

> Added storage type and Google Storage settings to worker by @KiyotakaMatsushita in #4266.

> Updated certbot/README.md by @eltociear in #7528.

> Added CONTRIBUTING_VI i18n by @ZuzooVn in #7532.

> That’s all for this release! As always, thank you for your contributions and feedback. Keep them coming, and happy coding! 🚀

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

> Web app support sending message using numpad enter by @xuzuodong in https://github.com/langgenius/dify/pull/7414

> chore: correct _tts_invoke_streaming max length by @ZuzooVn in https://github.com/langgenius/dify/pull/7423

> chore: #7196 i18n by @ZuzooVn in https://github.com/langgenius/dify/pull/7416

> feat: add pgvector full_text_search by @jasonkang14 in https://github.com/langgenius/dify/pull/7396

> add pgvector full text search settting by @JohnJyong in https://github.com/langgenius/dify/pull/7427

> chore(database): Rename table name from `workflow__conversation_variables` to `workflow_conversation_variables`. by @laipz8200 in https://github.com/langgenius/dify/pull/7432

> chore: remove .idea and .vscode from root path by @Yeuoly in https://github.com/langgenius/dify/pull/7437

> refactor(api/core/workflow/nodes/variable_assigner): Split into multi files. by @laipz8200 in https://github.com/langgenius/dify/pull/7434

> chore: add and update theme related css variables values by @iamjoel in https://github.com/langgenius/dify/pull/7442

> refactor(api/core/app/app_config/entities.py): Move Type to outside and add EXTERNAL_DATA_TOOL. by @laipz8200 in https://github.com/langgenius/dify/pull/7444

> refactor(api/core/workflow/enums.py): Rename SystemVariable to SystemVariableKey. by @laipz8200 in https://github.com/langgenius/dify/pull/7445

> feat: Sort conversations by updated_at desc by @KinWang130 in https://github.com/langgenius/dify/pull/7348

> feat: support dialogue count in chatflow by @iamjoel in https://github.com/langgenius/dify/pull/7440

> chore: #7348 i18n by @ZuzooVn in https://github.com/langgenius/dify/pull/7451

> chore: improve the copywrite of the assigner node append mode description by @iamjoel in https://github.com/langgenius/dify/pull/7467

> Separate CODE_MAX_DEPTH and set it as an environment variable by @Hisir0909 in https://github.com/langgenius/dify/pull/7474

> feat: support CODE_MAX_PRECISION by @ZuzooVn in https://github.com/langgenius/dify/pull/7484

> Chore/remove python dependencies selector by @Yeuoly in https://github.com/langgenius/dify/pull/7494

> feat(storage): 🐛 Create S3 bucket if it doesn't exist by @moyueheng in https://github.com/langgenius/dify/pull/7514

> feat: update the "tag delete" confirm modal by @YIXIAO0 in https://github.com/langgenius/dify/pull/7522

> docs: update certbot/README.md by @eltociear in https://github.com/langgenius/dify/pull/7528

> docs: CONTRIBUTING_VI i18n by @ZuzooVn in https://github.com/langgenius/dify/pull/7532

> update nltk version to 3.8.1 by @JohnJyong in https://github.com/langgenius/dify/pull/7544

> Added Space between Chinese and English within tools' description by @AllenWriter in https://github.com/langgenius/dify/pull/7545

> Add N-to-1 warning translation for JP by @HanqingZ in https://github.com/langgenius/dify/pull/7553

> feat: forward zhipu finish_reason by @orangeclk in https://github.com/langgenius/dify/pull/7560

> chore: #6554 i18n by @ZuzooVn in https://github.com/langgenius/dify/pull/7562

> feat: set workflow zoom range for shortcut by @YIXIAO0 in https://github.com/langgenius/dify/pull/7563

> chore: improve the check time of variable name by @iamjoel in https://github.com/langgenius/dify/pull/7569

> chore: improve the check time of variable name in conversation and env var by @iamjoel in https://github.com/langgenius/dify/pull/7572

> add qwen text-embedding-v3 support. by @droxer in https://github.com/langgenius/dify/pull/7567

> langfuser add view button by @charli117 in https://github.com/langgenius/dify/pull/7571

> Langfuse view button by @charli117 in https://github.com/langgenius/dify/pull/7578

> Do not pass query parameter when the value is empty by @AmosZhu in https://github.com/langgenius/dify/pull/7585

> Update stable_diffusion.py by @flingjie in https://github.com/langgenius/dify/pull/7536

> Feat: add OneBot protocol tool by @RockChinQ in https://github.com/langgenius/dify/pull/7583

> chore: cleanup and rearrange unclassified configs into feature config groups by @bowenliang123 in https://github.com/langgenius/dify/pull/7586

> chore(api/configs): apply ruff reformat by @bowenliang123 in https://github.com/langgenius/dify/pull/7590

> chore(api/tests): apply ruff reformat #7590 by @bowenliang123 in https://github.com/langgenius/dify/pull/7591

> Improve MIME type detection for image URLs by @Seayon in https://github.com/langgenius/dify/pull/6531

> feat: add siliconflow text2img tool by @hjlarry in https://github.com/langgenius/dify/pull/7612

> feat: web sso by @ZhouhaoJiang in https://github.com/langgenius/dify/pull/7135

> Web app now supports SSO config by @douxc in https://github.com/langgenius/dify/pull/7137

> feat: replace show/hide workflow_steps with switch by @crazywoola in https://github.com/langgenius/dify/pull/7627

> chore(api/tasks): apply ruff reformatting by @bowenliang123 in https://github.com/langgenius/dify/pull/7594

> chore(api/services): apply ruff reformatting by @bowenliang123 in https://github.com/langgenius/dify/pull/7599

> chore(api/controllers): Apply Ruff Formatter. by @laipz8200 in https://github.com/langgenius/dify/pull/7645

> [fix] openai's tool role dose not support name parameter. by @sydnash in https://github.com/langgenius/dify/pull/7659

> Proposal to revise Japanese expressions by @snickerjp in https://github.com/langgenius/dify/pull/7664

> catch openai rate limit error by @JohnJyong in https://github.com/langgenius/dify/pull/7658

> refactor: Add @staticmethod decorator in `api/core` by @totsukash in https://github.com/langgenius/dify/pull/7652

> chore: Update version to 0.7.2 by @laipz8200 in https://github.com/langgenius/dify/pull/7646

Source: https://github.com/langgenius/dify/releases/tag/0.7.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-08-26-stop-the-service-command-please-execute-in-the-docker-directory|Stop the service，Command, please execute in the docker directory]] · Developer Workflow
- [[Changes/Dify/2024-08-26-4-interface-experience-changes-in-0-7-2|4 Interface Experience changes in 0.7.2]] · Interface Experience
- [[Changes/Dify/2024-08-26-feat-7134-use-dataset-api-create-a-dataset-with-permission-by-crazywoola-in-http|Feat/7134 use dataset api create a dataset with permission]] · Safety and Privacy
- [[Changes/Dify/2024-08-26-11-model-support-changes-in-0-7-2|11 Model Support changes in 0.7.2]] · Model Support
- [[Changes/Dify/2024-08-26-feat-speed-up-the-docker-build-for-dify-api-for-chinese-developers-by-erigo-in-h|feat: speed up the Docker build for dify-api for Chinese developers]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-08-26-53cc2e&body=Card%3A%20Changes%2FDify%2F2024-08-26-83-other-changes-in-0-7-2.md%0ACard%20ID%3A%20dify-2024-08-26-53cc2e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.7.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->