---
card_id: dify-2024-10-14-43e895
date: '2024-10-14'
description: 'Dify · 2024-10-14 · Other changes: 66 changes in v0.9.2 — The most recent
  release brings some solid new features, enhancements, and bug fixes that should…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8de66074ea699af15ac0c8ea32a292c0b78622e13b57ff7f7b59848d6b42a1e8
product: dify
product_name: Dify
record:
  card_id: dify-2024-10-14-43e895
  comparison: ''
  date: '2024-10-14'
  description: 'Dify — v0.9.2: 66 other changes'
  evidence:
  - quote: 'The most recent release brings some solid new features, enhancements,
      and bug fixes that should enhance your experience across the platform. Check
      out what''s changed:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: '**Workflow System Parameters:** Now, you can access `sys.app_id`, `sys.workflow_id`,
      and `sys.workflow_run_id` in your workflow system variables for more dynamic
      workflows, courtesy of @ZhouhaoJiang in #9108.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: '**Tools Update:** Discord Incoming Webhook now lets you send messages
      directly, created by @yaoice. Props to @hwzhuhao for adding tags for Vanna tools
      too.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: '**Vector Provider:** Meet the new kid on the block, Volcengine VikingDB,
      integrated into the system and ready to expand your vector capabilities, brought
      to you by @yaoice in #9287.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: '**Richer Time Tool Functions:** Now you can convert and retrieve timestamps
      with the Time Tool, unlocking more precise temporal operations courtesy of @hwzhuhao.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: '**Customizeable Chatbot Embed:** Change the size to fit your needs with
      default values set for your convenience—well done, @alterxyz for this addition.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: '**Tool Descriptions:** Essential descriptions are back where they belong—visible
      and complete, thanks to @crazywoola.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: '> [!WARNING]'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: '> This version includes a migration that might update a large volume of
      messages. If you have a significant amount of message data, please review our
      changes in [#9132](https://github.com/langgenius/dify/pull/9132) before upgrading.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: Back up your customized docker-compose YAML file (optional)
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: Get the latest code from the main branch
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: Back up data
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: Upgrade services
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: Stop API server, Worker and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'Get the latest code from the release branch:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: Finally, run API server, Worker and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'refactor: remove unnecessary comment by @y-omr in https://github.com/langgenius/dify/pull/8949'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: remove unexecuted scripts to avoid ambiguity by @yaoice in https://github.com/langgenius/dify/pull/8946'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'feat: add qwen2.5-72b and llama3.2 for openrouter by @hwzhuhao in https://github.com/langgenius/dify/pull/8956'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'feat(Tools): add discord incoming webhook for sending messages by @yaoice
      in https://github.com/langgenius/dify/pull/7852'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: Update json_in_md_parser.py by @zhao85 in https://github.com/langgenius/dify/pull/8983
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'feat: Update AWS Bedrock supported regions by @Retr0-01 in https://github.com/langgenius/dify/pull/8992'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'refactor: remove the duplicate definitions across different modules by
      @hwzhuhao in https://github.com/langgenius/dify/pull/9022'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'feat: add baidu obs storage by @hwzhuhao in https://github.com/langgenius/dify/pull/9024'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: move testing env variables from pyproject.toml to pytest.ini by
      @bowenliang123 in https://github.com/langgenius/dify/pull/9019'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'feat: Improvement- use non root user for Web container by @s2oBCN in https://github.com/langgenius/dify/pull/8928'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: removing unused imports in tests by @bowenliang123 in https://github.com/langgenius/dify/pull/9049'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: refine python dependency list and check dependencies in order by
      @bowenliang123 in https://github.com/langgenius/dify/pull/9061'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'docs: Add Google Cloud Terraform to README by @sotazum in https://github.com/langgenius/dify/pull/9065'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'feat: update the xinf tool''s API key to optional by @hwzhuhao in https://github.com/langgenius/dify/pull/9073'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'feat: add timestamp conversion and timestamp retrieval for time tool by
      @hwzhuhao in https://github.com/langgenius/dify/pull/9085'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: Feat/9081 add support for llamaguard through groq provider by @crazywoola
      in https://github.com/langgenius/dify/pull/9083
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'refactor: Update countries & languages list for SearchApi engines by @SebastjanPrachovskij
      in https://github.com/langgenius/dify/pull/9090'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: add the missing tool names to the _position file by @hwzhuhao in
      https://github.com/langgenius/dify/pull/9099'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'feat: add tags for vanna tools by @hwzhuhao in https://github.com/langgenius/dify/pull/9102'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: avoid implicit optional in type annotations of method by @bowenliang123
      in https://github.com/langgenius/dify/pull/8727'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'feat: respect x-* headers for redirections by @kurokobo in https://github.com/langgenius/dify/pull/9054'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: Add customizable size for chatbot embed with default values by @alterxyz
      in https://github.com/langgenius/dify/pull/9115
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: add generate conversation name error log by @pinsily in https://github.com/langgenius/dify/pull/9117
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: avoid star imports usage by @bowenliang123 in https://github.com/langgenius/dify/pull/9123'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: Feat/add workflow sys params by @ZhouhaoJiang in https://github.com/langgenius/dify/pull/9108
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: downgrade elastic to 8.14 by @JohnJyong in https://github.com/langgenius/dify/pull/9171
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'feat: add gte rerank for tongyi by @droxer in https://github.com/langgenius/dify/pull/9153'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'feat: add NotFound error for dataset service by @crazywoola in https://github.com/langgenius/dify/pull/9215'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: Update docker-compose.yaml by @massif-01 in https://github.com/langgenius/dify/pull/9183
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: check all dependencies groups in pyproject.toml by @bowenliang123
      in https://github.com/langgenius/dify/pull/9224'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'feat: support csp by @douxc in https://github.com/langgenius/dify/pull/9111'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore(deps): bump micromatch from 4.0.5 to 4.0.8 in /web by @dependabot
      in https://github.com/langgenius/dify/pull/9234'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore(deps): bump dompurify from 3.0.5 to 3.1.7 in /web by @dependabot
      in https://github.com/langgenius/dify/pull/9232'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'feat: add supabase object storage by @hwzhuhao in https://github.com/langgenius/dify/pull/9229'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: use cache instead of re-querying node record during workflow execution
      by @takatost in https://github.com/langgenius/dify/pull/9280'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: optimize the trace ops slow queries on node executions. by @takatost
      in https://github.com/langgenius/dify/pull/9282'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: feat:support baidu vector db by @WayneCao in https://github.com/langgenius/dify/pull/9185
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: translate i18n files by @github-actions in https://github.com/langgenius/dify/pull/9284'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'feat: refresh-token by @WTW0313 in https://github.com/langgenius/dify/pull/9286'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: Feat/new account page by @douxc in https://github.com/langgenius/dify/pull/9236
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: add abstract decorator and output log when query embedding fails
      by @hwzhuhao in https://github.com/langgenius/dify/pull/9264'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: add baidu-obs and supabase for .env.example by @hwzhuhao in https://github.com/langgenius/dify/pull/9289'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: translate i18n files by @github-actions in https://github.com/langgenius/dify/pull/9288'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: Add Volcengine VikingDB as new vector provider by @yaoice in https://github.com/langgenius/dify/pull/9287
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'refactor: Refactor the service of retrieval the recommend app by @hwzhuhao
      in https://github.com/langgenius/dify/pull/9302'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: Optimize operations in Q&A mode by @Blubiubiu in https://github.com/langgenius/dify/pull/9274'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore: add reopen preview btn by @Blubiubiu in https://github.com/langgenius/dify/pull/9279'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  - quote: 'chore(release): bump version to 0.9.2 by @laipz8200 in https://github.com/langgenius/dify/pull/9314'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 66-other-changes-in-0-9-2
  source_release: dify-2024-10-14-0-9-2-github-179747449-3e58ccc7
  source_type: github_releases
  theme: uncategorized
  title: 66 other changes in 0.9.2
  type: change
source_release: '[[Releases/Dify/dify-2024-10-14-0-9-2-github-179747449-3e58ccc7|dify-2024-10-14-0-9-2-github-179747449-3e58ccc7]]'
source_type: github_releases
theme: uncategorized
title: 66 other changes in 0.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 66 other changes in 0.9.2

**Dify** · 2024-10-14 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.9.2) · from [[Releases/Dify/dify-2024-10-14-0-9-2-github-179747449-3e58ccc7|v0.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The most recent release brings some solid new features, enhancements, and bug fixes that should enhance your experience across the platform. Check out what's changed:

> **Workflow System Parameters:** Now, you can access `sys.app_id`, `sys.workflow_id`, and `sys.workflow_run_id` in your workflow system variables for more dynamic workflows, courtesy of @ZhouhaoJiang in #9108.

> **Tools Update:** Discord Incoming Webhook now lets you send messages directly, created by @yaoice. Props to @hwzhuhao for adding tags for Vanna tools too.

> **Vector Provider:** Meet the new kid on the block, Volcengine VikingDB, integrated into the system and ready to expand your vector capabilities, brought to you by @yaoice in #9287.

> **Richer Time Tool Functions:** Now you can convert and retrieve timestamps with the Time Tool, unlocking more precise temporal operations courtesy of @hwzhuhao.

> **Customizeable Chatbot Embed:** Change the size to fit your needs with default values set for your convenience—well done, @alterxyz for this addition.

> **Tool Descriptions:** Essential descriptions are back where they belong—visible and complete, thanks to @crazywoola.

> > [!WARNING]

> > This version includes a migration that might update a large volume of messages. If you have a significant amount of message data, please review our changes in [#9132](https://github.com/langgenius/dify/pull/9132) before upgrading.

> Back up your customized docker-compose YAML file (optional)

> Get the latest code from the main branch

> Back up data

> Upgrade services

> Stop API server, Worker and Web frontend Server.

> Get the latest code from the release branch:

> Update Python dependencies:

> Then, let's run the migration script:

> Finally, run API server, Worker and Web frontend Server again.

> refactor: remove unnecessary comment by @y-omr in https://github.com/langgenius/dify/pull/8949

> chore: remove unexecuted scripts to avoid ambiguity by @yaoice in https://github.com/langgenius/dify/pull/8946

> feat: add qwen2.5-72b and llama3.2 for openrouter by @hwzhuhao in https://github.com/langgenius/dify/pull/8956

> feat(Tools): add discord incoming webhook for sending messages by @yaoice in https://github.com/langgenius/dify/pull/7852

> Update json_in_md_parser.py by @zhao85 in https://github.com/langgenius/dify/pull/8983

> feat: Update AWS Bedrock supported regions by @Retr0-01 in https://github.com/langgenius/dify/pull/8992

> refactor: remove the duplicate definitions across different modules by @hwzhuhao in https://github.com/langgenius/dify/pull/9022

> feat: add baidu obs storage by @hwzhuhao in https://github.com/langgenius/dify/pull/9024

> chore: move testing env variables from pyproject.toml to pytest.ini by @bowenliang123 in https://github.com/langgenius/dify/pull/9019

> feat: Improvement- use non root user for Web container by @s2oBCN in https://github.com/langgenius/dify/pull/8928

> chore: removing unused imports in tests by @bowenliang123 in https://github.com/langgenius/dify/pull/9049

> chore: refine python dependency list and check dependencies in order by @bowenliang123 in https://github.com/langgenius/dify/pull/9061

> docs: Add Google Cloud Terraform to README by @sotazum in https://github.com/langgenius/dify/pull/9065

> feat: update the xinf tool's API key to optional by @hwzhuhao in https://github.com/langgenius/dify/pull/9073

> feat: add timestamp conversion and timestamp retrieval for time tool by @hwzhuhao in https://github.com/langgenius/dify/pull/9085

> Feat/9081 add support for llamaguard through groq provider by @crazywoola in https://github.com/langgenius/dify/pull/9083

> refactor: Update countries & languages list for SearchApi engines by @SebastjanPrachovskij in https://github.com/langgenius/dify/pull/9090

> chore: add the missing tool names to the _position file by @hwzhuhao in https://github.com/langgenius/dify/pull/9099

> feat: add tags for vanna tools by @hwzhuhao in https://github.com/langgenius/dify/pull/9102

> chore: avoid implicit optional in type annotations of method by @bowenliang123 in https://github.com/langgenius/dify/pull/8727

> feat: respect x-* headers for redirections by @kurokobo in https://github.com/langgenius/dify/pull/9054

> Add customizable size for chatbot embed with default values by @alterxyz in https://github.com/langgenius/dify/pull/9115

> add generate conversation name error log by @pinsily in https://github.com/langgenius/dify/pull/9117

> chore: avoid star imports usage by @bowenliang123 in https://github.com/langgenius/dify/pull/9123

> Feat/add workflow sys params by @ZhouhaoJiang in https://github.com/langgenius/dify/pull/9108

> downgrade elastic to 8.14 by @JohnJyong in https://github.com/langgenius/dify/pull/9171

> feat: add gte rerank for tongyi by @droxer in https://github.com/langgenius/dify/pull/9153

> feat: add NotFound error for dataset service by @crazywoola in https://github.com/langgenius/dify/pull/9215

> Update docker-compose.yaml by @massif-01 in https://github.com/langgenius/dify/pull/9183

> chore: check all dependencies groups in pyproject.toml by @bowenliang123 in https://github.com/langgenius/dify/pull/9224

> feat: support csp by @douxc in https://github.com/langgenius/dify/pull/9111

> chore(deps): bump micromatch from 4.0.5 to 4.0.8 in /web by @dependabot in https://github.com/langgenius/dify/pull/9234

> chore(deps): bump dompurify from 3.0.5 to 3.1.7 in /web by @dependabot in https://github.com/langgenius/dify/pull/9232

> feat: add supabase object storage by @hwzhuhao in https://github.com/langgenius/dify/pull/9229

> chore: use cache instead of re-querying node record during workflow execution by @takatost in https://github.com/langgenius/dify/pull/9280

> chore: optimize the trace ops slow queries on node executions. by @takatost in https://github.com/langgenius/dify/pull/9282

> feat:support baidu vector db by @WayneCao in https://github.com/langgenius/dify/pull/9185

> chore: translate i18n files by @github-actions in https://github.com/langgenius/dify/pull/9284

> feat: refresh-token by @WTW0313 in https://github.com/langgenius/dify/pull/9286

> Feat/new account page by @douxc in https://github.com/langgenius/dify/pull/9236

> chore: add abstract decorator and output log when query embedding fails by @hwzhuhao in https://github.com/langgenius/dify/pull/9264

> chore: add baidu-obs and supabase for .env.example by @hwzhuhao in https://github.com/langgenius/dify/pull/9289

> chore: translate i18n files by @github-actions in https://github.com/langgenius/dify/pull/9288

> Add Volcengine VikingDB as new vector provider by @yaoice in https://github.com/langgenius/dify/pull/9287

> refactor: Refactor the service of retrieval the recommend app by @hwzhuhao in https://github.com/langgenius/dify/pull/9302

> chore: Optimize operations in Q&A mode by @Blubiubiu in https://github.com/langgenius/dify/pull/9274

> chore: add reopen preview btn by @Blubiubiu in https://github.com/langgenius/dify/pull/9279

> chore(release): bump version to 0.9.2 by @laipz8200 in https://github.com/langgenius/dify/pull/9314

Source: https://github.com/langgenius/dify/releases/tag/0.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-10-14-miscellaneous-fixes-including-max-token-adjustments-in-openrouter-by-infinitnet|Miscellaneous Fixes: Including max-token adjustments in OpenRouter…]] · Projects and Workspaces
- [[Changes/Dify/2024-10-14-feat-implement-refresh-tokens-by-laipz8200-in-https-github-com-langgenius-dify-p|Feat/implement-refresh-tokens]] · Context Window
- [[Changes/Dify/2024-10-14-2-image-generation-changes-in-0-9-2|2 Image Generation changes in 0.9.2]] · Image Generation
- [[Changes/Dify/2024-10-14-2-reliability-and-performance-changes-in-0-9-2|2 Reliability and Performance changes in 0.9.2]] · Reliability and Performance
- [[Changes/Dify/2024-10-14-13-model-support-changes-in-0-9-2|13 Model Support changes in 0.9.2]] · Model Support
- [[Changes/Dify/2024-10-14-prompt-editor-optimization-clearer-and-more-efficient-prompt-editing-with-reset|Prompt Editor Optimization: Clearer and more efficient prompt editing with reset…]] · Editor Experience
- [[Changes/Dify/2024-10-14-2-safety-and-privacy-changes-in-0-9-2|2 Safety and Privacy changes in 0.9.2]] · Safety and Privacy
- [[Changes/Dify/2024-10-14-external-knowledge-and-retrievals-addressing-issues-in-agent-retrieval-and-entry|External Knowledge and Retrievals: Addressing issues in agent retrieval…]] · Agent Mode
- [[Changes/Dify/2024-10-14-2-developer-workflow-changes-in-0-9-2|2 Developer Workflow changes in 0.9.2]] · Developer Workflow
- [[Changes/Dify/2024-10-14-4-apps-and-integrations-changes-in-0-9-2|4 Apps and Integrations changes in 0.9.2]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-10-14-43e895&body=Card%3A%20Changes%2FDify%2F2024-10-14-66-other-changes-in-0-9-2.md%0ACard%20ID%3A%20dify-2024-10-14-43e895%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->