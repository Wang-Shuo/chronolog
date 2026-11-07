---
card_id: dify-2026-08-25-8a8551
date: '2026-08-25'
description: 'Dify · 2026-08-25 · Model Support: 93 changes in v1.17.0 — **Reusable
  LLM Environment Variables in Workflows**'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1324
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6c25ca2082a3b69bd0872b9ea5ca8a437080d33521dd619c7ab103d4240277c9
product: dify
product_name: Dify
record:
  card_id: dify-2026-08-25-8a8551
  comparison: ''
  date: '2026-08-25'
  description: 'Dify — v1.17.0: 93 Model Support changes'
  evidence:
  - quote: '**Reusable LLM Environment Variables in Workflows**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: Define a shared provider/model/mode/parameter configuration once (e.g.
      `for_summarize`, `for_research`) and reference it from any LLM node. Coordinated
      model changes now happen in one place instead of drifting node-by-node, and
      the references survive DSL import/export, snippets, RAG pipelines, and collaborative
      editing (#39125).
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '**Broader Model & File Handling**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'Large migration of unit tests to real ORM models / SQLite sessions for
      more reliable coverage, plus stronger typing across migrated tests (many #38xxx–#39xxx).
      No user-facing behavior change.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '> **One-time legacy model type migration for self-hosted upgrades**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '> This migration is **not included in `flask db upgrade`**. Without it,
      legacy model records can cause model-related API requests to fail with errors,
      preventing affected models from being loaded or used.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: After applying the migration, run the dry-run command again. If it reports
      no additional row updates or deletions, restart the relevant services and verify
      that existing models can be loaded and invoked successfully.
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor(web): localize model load balancing modal state by @lyzno1 in
      https://github.com/langgenius/dify/pull/39789'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: use SQLite sessions in core llm_generator by @asukaminato0721 in
      https://github.com/langgenius/dify/pull/39070'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat: pass image file to llm by @fatelei in https://github.com/langgenius/dify/pull/39848'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat(workflow): support LLM environment variables by @laipz8200 in https://github.com/langgenius/dify/pull/39125'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: use real ORM models in RAG indexing tests by @asukaminato0721 in
      https://github.com/langgenius/dify/pull/40017'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: use real ORM models in workflow repository tests by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40019'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: use real ORM models in dataset service tests by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40018'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: use real ORM models in app and API tests by @asukaminato0721 in
      https://github.com/langgenius/dify/pull/40020'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore: dep inject for model in notification dismiss by @likalikali in
      https://github.com/langgenius/dify/pull/40146'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore: dep inject for model in datasets document and web human input …
      by @likalikali in https://github.com/langgenius/dify/pull/40151'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore: dep inject for model in api based extension by @likalikali in https://github.com/langgenius/dify/pull/40154'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore: dep inject for model in website crawl api by @likalikali in https://github.com/langgenius/dify/pull/40156'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore: dep inject for model in workflow run archive download by @likalikali
      in https://github.com/langgenius/dify/pull/40157'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore: dep inject for model in onboarding step by step tour by @likalikali
      in https://github.com/langgenius/dify/pull/40155'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore: dep inject for model in workspace snippets, load balancing, and
      endpoint by @likalikali in https://github.com/langgenius/dify/pull/40161'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore: dep inject for model in explore apis by @likalikali in https://github.com/langgenius/dify/pull/40160'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore: dep inject for model in explore workflow run by @likalikali in
      https://github.com/langgenius/dify/pull/40158'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor: replace manual model_validate with @model_validate decorator
      in app controllers by @likalikali in https://github.com/langgenius/dify/pull/40170'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor: replace manual model_validate with @model_validate in explore/snippets
      controllers by @likalikali in https://github.com/langgenius/dify/pull/40241'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor: replace manual model_validate with @model_validate in app core
      controllers by @likalikali in https://github.com/langgenius/dify/pull/40234'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor: replace manual model_validate with @model_validate in app workflow
      controllers by @likalikali in https://github.com/langgenius/dify/pull/40235'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor: replace manual model_validate with @model_validate in rag_pipeline
      controllers by @likalikali in https://github.com/langgenius/dify/pull/40237'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor: replace manual model_validate with @model_validate in workspace
      remaining controllers by @likalikali in https://github.com/langgenius/dify/pull/40239'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor: replace manual model_validate with @model_validate in datasets
      controllers by @likalikali in https://github.com/langgenius/dify/pull/40236'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate API workflow pause ORM models to real entities by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40669'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate residual ORM model stand-ins to real mappings by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40666'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate residual dataset and archive ORM models by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40668'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate workflow variable ORM model to real entity by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40664'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate OpenTelemetry ORM identities to real models by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40663'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate RAG dataset ORM contracts to real models by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40662'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate residual controller ORM identities to real models by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40661'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate reranker upload-file sessions and ORM models to SQLite by
      @asukaminato0721 in https://github.com/langgenius/dify/pull/40659'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate app runner transaction sessions and ORM models to SQLite
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/40660'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate workflow tool-file ORM model to real entity by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40658'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate workflow node trace ORM models to real entities by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40657'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate conversation lifecycle sessions and ORM models to SQLite
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/40656'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor: resolve summary models through manager by @linw1995 in https://github.com/langgenius/dify/pull/40696'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor: generalize hosted model quota lifecycle by @linw1995 in https://github.com/langgenius/dify/pull/40722'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor(web): clarify model selector trigger ownership by @lyzno1 in
      https://github.com/langgenius/dify/pull/40732'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate annotation controller ORM models to real entities by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40643'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate load balancing account ORM model to real entity by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40644'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate expired log workflow ORM models to real entities by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40645'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate trace workflow run ORM model to real entity by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40642'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate web controller identity ORM models to real entities by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40639'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate workflow event ORM models to real entities by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40634'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate residual namespace ORM entities to real models by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40633'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate controller identity ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40626'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate workflow tool users to SQLite ORM models by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40628'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate RAG residual entities to real ORM models by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40629'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore: dep inject for model in dataset document actions by @ddddajie in
      https://github.com/langgenius/dify/pull/40787'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor: add Mapped type annotations to model fields (#40373) by @mahbubsouad
      in https://github.com/langgenius/dify/pull/40380'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor(controllers/web): dep-inject payloads with @model_validate by
      @a-yeyang in https://github.com/langgenius/dify/pull/40796'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate residual user ORM stand-ins to real models by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40625'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate file controller ORM models to real entities by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40632'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate RAG processor residuals to SQLite ORM models by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40608'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate residual controller sessions and ORM models to SQLite by
      @asukaminato0721 in https://github.com/langgenius/dify/pull/40606'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate console conversation sessions and ORM models to SQLite by
      @asukaminato0721 in https://github.com/langgenius/dify/pull/40528'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate controller auth wrapper sessions and ORM models to SQLite
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/40529'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate console workflow controller sessions and ORM models to SQLite
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/40527'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate Service API dataset document sessions and ORM models to
      SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40519'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate Service API dataset metadata sessions and ORM models to
      SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40518'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate RAG pipeline sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40511'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate RAG indexing sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40513'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor(models): dep-inject Session on remaining @property accessors
      by @a-yeyang in https://github.com/langgenius/dify/pull/40797'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate app model sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40530'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate residual model sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40531'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate service boundary sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40533'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate telemetry and core entity ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40574'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate residual service and task ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40576'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate residual controller sessions and ORM models to SQLite by
      @asukaminato0721 in https://github.com/langgenius/dify/pull/40579'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate app runtime sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40590'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate dataset service sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40534'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate document service sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40536'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate Explore controller sessions and ORM models to SQLite by
      @asukaminato0721 in https://github.com/langgenius/dify/pull/40537'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate media and execution service sessions and ORM models to SQLite
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/40552'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate snippet service ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40567'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate annotation sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40504'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate vector space admission sessions and ORM models to SQLite
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/40640'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate remaining controller sessions and ORM models to SQLite by
      @asukaminato0721 in https://github.com/langgenius/dify/pull/40538'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate console app sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40559'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate auth and access controller ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40572'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate console dataset segment sessions and ORM models to SQLite
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/40515'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate residual app generator ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40580'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate trigger and webhook sessions and ORM models to SQLite by
      @asukaminato0721 in https://github.com/langgenius/dify/pull/40594'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test(vdb): use real ORM models in provider tests by @asukaminato0721 in
      https://github.com/langgenius/dify/pull/40687'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate RAG variable controller sessions and ORM models to SQLite
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/40609'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 93-model-support-changes-in-1-17-0
  source_release: dify-2026-08-25-1-17-0-github-376348099-66c16161
  source_type: github_releases
  theme: model-support
  title: 93 Model Support changes in 1.17.0
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-08-24-added-support-for-attaching-audio-files-mp3-wav-m4a-aac-ogg-flac-opus-up-to-20mb|Added
  support for attaching audio files (MP3, WAV, M4A, AAC, OGG, FLAC, OPUS) up…]]'
- '[[Changes/Lovable/2026-08-24-chat-latest-for-your-app-s-ai-features|Chat Latest
  for your app''s AI features]]'
- '[[Changes/Recraft/2026-08-24-take-total-control-over-your-output-before-you-hit-generate-choose-your-batch-si|Multi-Generation
  & Model Comparison]]'
source_release: '[[Releases/Dify/dify-2026-08-25-1-17-0-github-376348099-66c16161|dify-2026-08-25-1-17-0-github-376348099-66c16161]]'
source_type: github_releases
theme: model-support
title: 93 Model Support changes in 1.17.0
type: change
---

<!-- chronolog:begin region="header" -->
# 93 Model Support changes in 1.17.0

**Dify** · 2026-08-25 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.0) · from [[Releases/Dify/dify-2026-08-25-1-17-0-github-376348099-66c16161|v1.17.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Reusable LLM Environment Variables in Workflows**

> Define a shared provider/model/mode/parameter configuration once (e.g. `for_summarize`, `for_research`) and reference it from any LLM node. Coordinated model changes now happen in one place instead of drifting node-by-node, and the references survive DSL import/export, snippets, RAG pipelines, and collaborative editing (#39125).

> **Broader Model & File Handling**

> Large migration of unit tests to real ORM models / SQLite sessions for more reliable coverage, plus stronger typing across migrated tests (many #38xxx–#39xxx). No user-facing behavior change.

> > **One-time legacy model type migration for self-hosted upgrades**

> > This migration is **not included in `flask db upgrade`**. Without it, legacy model records can cause model-related API requests to fail with errors, preventing affected models from being loaded or used.

> After applying the migration, run the dry-run command again. If it reports no additional row updates or deletions, restart the relevant services and verify that existing models can be loaded and invoked successfully.

> refactor(web): localize model load balancing modal state by @lyzno1 in https://github.com/langgenius/dify/pull/39789

> test: use SQLite sessions in core llm_generator by @asukaminato0721 in https://github.com/langgenius/dify/pull/39070

> feat: pass image file to llm by @fatelei in https://github.com/langgenius/dify/pull/39848

> feat(workflow): support LLM environment variables by @laipz8200 in https://github.com/langgenius/dify/pull/39125

> test: use real ORM models in RAG indexing tests by @asukaminato0721 in https://github.com/langgenius/dify/pull/40017

> test: use real ORM models in workflow repository tests by @asukaminato0721 in https://github.com/langgenius/dify/pull/40019

> test: use real ORM models in dataset service tests by @asukaminato0721 in https://github.com/langgenius/dify/pull/40018

> test: use real ORM models in app and API tests by @asukaminato0721 in https://github.com/langgenius/dify/pull/40020

> chore: dep inject for model in notification dismiss by @likalikali in https://github.com/langgenius/dify/pull/40146

> chore: dep inject for model in datasets document and web human input … by @likalikali in https://github.com/langgenius/dify/pull/40151

> chore: dep inject for model in api based extension by @likalikali in https://github.com/langgenius/dify/pull/40154

> chore: dep inject for model in website crawl api by @likalikali in https://github.com/langgenius/dify/pull/40156

> chore: dep inject for model in workflow run archive download by @likalikali in https://github.com/langgenius/dify/pull/40157

> chore: dep inject for model in onboarding step by step tour by @likalikali in https://github.com/langgenius/dify/pull/40155

> chore: dep inject for model in workspace snippets, load balancing, and endpoint by @likalikali in https://github.com/langgenius/dify/pull/40161

> chore: dep inject for model in explore apis by @likalikali in https://github.com/langgenius/dify/pull/40160

> chore: dep inject for model in explore workflow run by @likalikali in https://github.com/langgenius/dify/pull/40158

> refactor: replace manual model_validate with @model_validate decorator in app controllers by @likalikali in https://github.com/langgenius/dify/pull/40170

> refactor: replace manual model_validate with @model_validate in explore/snippets controllers by @likalikali in https://github.com/langgenius/dify/pull/40241

> refactor: replace manual model_validate with @model_validate in app core controllers by @likalikali in https://github.com/langgenius/dify/pull/40234

> refactor: replace manual model_validate with @model_validate in app workflow controllers by @likalikali in https://github.com/langgenius/dify/pull/40235

> refactor: replace manual model_validate with @model_validate in rag_pipeline controllers by @likalikali in https://github.com/langgenius/dify/pull/40237

> refactor: replace manual model_validate with @model_validate in workspace remaining controllers by @likalikali in https://github.com/langgenius/dify/pull/40239

> refactor: replace manual model_validate with @model_validate in datasets controllers by @likalikali in https://github.com/langgenius/dify/pull/40236

> test: migrate API workflow pause ORM models to real entities by @asukaminato0721 in https://github.com/langgenius/dify/pull/40669

> test: migrate residual ORM model stand-ins to real mappings by @asukaminato0721 in https://github.com/langgenius/dify/pull/40666

> test: migrate residual dataset and archive ORM models by @asukaminato0721 in https://github.com/langgenius/dify/pull/40668

> test: migrate workflow variable ORM model to real entity by @asukaminato0721 in https://github.com/langgenius/dify/pull/40664

> test: migrate OpenTelemetry ORM identities to real models by @asukaminato0721 in https://github.com/langgenius/dify/pull/40663

> test: migrate RAG dataset ORM contracts to real models by @asukaminato0721 in https://github.com/langgenius/dify/pull/40662

> test: migrate residual controller ORM identities to real models by @asukaminato0721 in https://github.com/langgenius/dify/pull/40661

> test: migrate reranker upload-file sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40659

> test: migrate app runner transaction sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40660

> test: migrate workflow tool-file ORM model to real entity by @asukaminato0721 in https://github.com/langgenius/dify/pull/40658

> test: migrate workflow node trace ORM models to real entities by @asukaminato0721 in https://github.com/langgenius/dify/pull/40657

> test: migrate conversation lifecycle sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40656

> refactor: resolve summary models through manager by @linw1995 in https://github.com/langgenius/dify/pull/40696

> refactor: generalize hosted model quota lifecycle by @linw1995 in https://github.com/langgenius/dify/pull/40722

> refactor(web): clarify model selector trigger ownership by @lyzno1 in https://github.com/langgenius/dify/pull/40732

> test: migrate annotation controller ORM models to real entities by @asukaminato0721 in https://github.com/langgenius/dify/pull/40643

> test: migrate load balancing account ORM model to real entity by @asukaminato0721 in https://github.com/langgenius/dify/pull/40644

> test: migrate expired log workflow ORM models to real entities by @asukaminato0721 in https://github.com/langgenius/dify/pull/40645

> test: migrate trace workflow run ORM model to real entity by @asukaminato0721 in https://github.com/langgenius/dify/pull/40642

> test: migrate web controller identity ORM models to real entities by @asukaminato0721 in https://github.com/langgenius/dify/pull/40639

> test: migrate workflow event ORM models to real entities by @asukaminato0721 in https://github.com/langgenius/dify/pull/40634

> test: migrate residual namespace ORM entities to real models by @asukaminato0721 in https://github.com/langgenius/dify/pull/40633

> test: migrate controller identity ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40626

> test: migrate workflow tool users to SQLite ORM models by @asukaminato0721 in https://github.com/langgenius/dify/pull/40628

> test: migrate RAG residual entities to real ORM models by @asukaminato0721 in https://github.com/langgenius/dify/pull/40629

> chore: dep inject for model in dataset document actions by @ddddajie in https://github.com/langgenius/dify/pull/40787

> refactor: add Mapped type annotations to model fields (#40373) by @mahbubsouad in https://github.com/langgenius/dify/pull/40380

> refactor(controllers/web): dep-inject payloads with @model_validate by @a-yeyang in https://github.com/langgenius/dify/pull/40796

> test: migrate residual user ORM stand-ins to real models by @asukaminato0721 in https://github.com/langgenius/dify/pull/40625

> test: migrate file controller ORM models to real entities by @asukaminato0721 in https://github.com/langgenius/dify/pull/40632

> test: migrate RAG processor residuals to SQLite ORM models by @asukaminato0721 in https://github.com/langgenius/dify/pull/40608

> test: migrate residual controller sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40606

> test: migrate console conversation sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40528

> test: migrate controller auth wrapper sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40529

> test: migrate console workflow controller sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40527

> test: migrate Service API dataset document sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40519

> test: migrate Service API dataset metadata sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40518

> test: migrate RAG pipeline sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40511

> test: migrate RAG indexing sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40513

> refactor(models): dep-inject Session on remaining @property accessors by @a-yeyang in https://github.com/langgenius/dify/pull/40797

> test: migrate app model sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40530

> test: migrate residual model sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40531

> test: migrate service boundary sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40533

> test: migrate telemetry and core entity ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40574

> test: migrate residual service and task ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40576

> test: migrate residual controller sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40579

> test: migrate app runtime sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40590

> test: migrate dataset service sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40534

> test: migrate document service sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40536

> test: migrate Explore controller sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40537

> test: migrate media and execution service sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40552

> test: migrate snippet service ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40567

> test: migrate annotation sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40504

> test: migrate vector space admission sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40640

> test: migrate remaining controller sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40538

> test: migrate console app sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40559

> test: migrate auth and access controller ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40572

> test: migrate console dataset segment sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40515

> test: migrate residual app generator ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40580

> test: migrate trigger and webhook sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40594

> test(vdb): use real ORM models in provider tests by @asukaminato0721 in https://github.com/langgenius/dify/pull/40687

> test: migrate RAG variable controller sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40609

Source: https://github.com/langgenius/dify/releases/tag/1.17.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-08-25-2-enterprise-and-administration-changes-in-1-17-0|2 Enterprise and Administration changes in 1.17.0]] · Enterprise and Administration
- [[Changes/Dify/2026-08-25-audio-asr-now-accepts-audio-x-m4a-and-audio-mime-types-are-validated-more-accura|Audio ASR now accepts audio/x-m4a, and audio MIME types are validated more…]] · Voice and Audio
- [[Changes/Dify/2026-08-25-5-collaboration-changes-in-1-17-0|5 Collaboration changes in 1.17.0]] · Collaboration
- [[Changes/Dify/2026-08-25-16-safety-and-privacy-changes-in-1-17-0|16 Safety and Privacy changes in 1.17.0]] · Safety and Privacy
- [[Changes/Dify/2026-08-25-feat-workflow-support-human-input-in-loop-and-iteration-by-laipz8200-in-https-gi|feat(workflow): support human input in loop and iteration]] · Automation and Scheduling
- [[Changes/Dify/2026-08-25-4-editor-experience-changes-in-1-17-0|4 Editor Experience changes in 1.17.0]] · Editor Experience
- [[Changes/Dify/2026-08-25-3-multimodal-input-changes-in-1-17-0|3 Multimodal Input changes in 1.17.0]] · Multimodal Input
- [[Changes/Dify/2026-08-25-53-agent-mode-changes-in-1-17-0|53 Agent Mode changes in 1.17.0]] · Agent Mode
- [[Changes/Dify/2026-08-25-4-developer-workflow-changes-in-1-17-0|4 Developer Workflow changes in 1.17.0]] · Developer Workflow
- [[Changes/Dify/2026-08-25-13-account-and-access-changes-in-1-17-0|13 Account and Access changes in 1.17.0]] · Account and Access
- [[Changes/Dify/2026-08-25-28-apps-and-integrations-changes-in-1-17-0|28 Apps and Integrations changes in 1.17.0]] · Apps and Integrations
- [[Changes/Dify/2026-08-25-7-pricing-model-changes-in-1-17-0|7 Pricing Model changes in 1.17.0]] · Pricing Model
- [[Changes/Dify/2026-08-25-5-files-and-data-changes-in-1-17-0|5 Files and Data changes in 1.17.0]] · Files and Data
- [[Changes/Dify/2026-08-25-workflow-runtime-stability|Workflow & Runtime Stability]] · Reliability and Performance
- [[Changes/Dify/2026-08-25-8-context-window-changes-in-1-17-0|8 Context Window changes in 1.17.0]] · Context Window
- [[Changes/Dify/2026-08-25-9-interface-experience-changes-in-1-17-0|9 Interface Experience changes in 1.17.0]] · Interface Experience
- [[Changes/Dify/2026-08-25-3-accessibility-and-localization-changes-in-1-17-0|3 Accessibility and Localization changes in 1.17.0]] · Accessibility and Localization
- [[Changes/Dify/2026-08-25-351-other-changes-in-1-17-0|351 other changes in 1.17.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-08-24 · Recraft · [[Changes/Recraft/2026-08-24-take-total-control-over-your-output-before-you-hit-generate-choose-your-batch-si|Multi-Generation & Model Comparison]]
- Later: 2026-08-25 · Microsoft 365 Copilot · [[Changes/Microsoft 365 Copilot/2026-08-25-select-models-when-using-researcher-in-copilot-chat-windows-web-microsoft-365-co|Select models when using Researcher in Copilot Chat Windows…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-08-25-8a8551&body=Card%3A%20Changes%2FDify%2F2026-08-25-93-model-support-changes-in-1-17-0.md%0ACard%20ID%3A%20dify-2026-08-25-8a8551%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->