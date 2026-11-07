---
card_id: dify-2026-09-10-283af5
date: '2026-09-10'
description: 'Dify · 2026-09-10 · Model Support: 76 changes in v1.17.1 - Bug Fixes
  and Improvements — **Model Providers**'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1340
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a0bf5b972a68cfdcd9b4bb7473c695529c6bfdf791800cc62652be73565f8371
product: dify
product_name: Dify
record:
  card_id: dify-2026-09-10-283af5
  comparison: ''
  date: '2026-09-10'
  description: 'Dify — v1.17.1 - Bug Fixes and Improvements: 76 Model Support changes'
  evidence:
  - quote: '**Model Providers**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Upgrades from pre-1.15 no longer leave models unusable, and no longer
      need a manual command.** Installations older than 1.15 still carry legacy model
      type values (`text-generation`, `embeddings`, `reranking`) in their provider
      tables, which makes model-related API requests fail and prevents affected models
      from loading. Both 1.16.1 and 1.17.0 shipped this as a separate `flask data-migrate
      legacy-model-types` step that had to be run by hand. It now runs as part of
      `flask db upgrade`: legacy values are canonicalized to `llm` / `text-embedding`
      / `rerank`, legacy-versus-canonical row collisions are resolved deterministically
      while preserving credential references, and the provider cache namespace is
      rotated so stale cached credentials cannot shadow the migrated rows. (#41326,
      fixes #41294)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**A single bad LLM node took down the whole editor.** A workflow whose
      LLM node had `model_selector` persisted as `null` rather than omitted crashed
      Workflow Studio''s per-node checklist on load and tripped the page-level error
      boundary, making the entire canvas unusable rather than flagging one node. (#41707)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Replies from reasoning models rendered entirely as "thinking".** Models
      such as GLM-5.3 wrap chain-of-thought in `<think>` tags, and a tool call frequently
      interrupts generation before `</think>` is emitted, leaving the answer nested
      inside a still-open tag. The dangling tag is now closed when a tool log interrupts
      the stream, when a new `<think>` starts after real content, and at stream end
      — plus the same repair in the Markdown preprocessor so already-stored output
      renders correctly. (#41764)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**JSON extraction broke on backticks inside JSON.** `parse_json_markdown`
      picked the first code-fence-like marker anywhere in the text, so a backtick
      inside a string value — `` {"code": "use `print` function"} `` — or in surrounding
      prose made extraction start mid-string and fail. Extraction is now anchored
      on the JSON brackets themselves. This parser backs LLM output parsing for the
      rule-config generator and dataset retrieval metadata, where backticked code
      inside JSON is common. (#41959)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Explicit database sessions across the ORM layer.** The legacy `db.session`
      property wrappers were removed from `App`, `Dataset`, `Document`, `DocumentSegment`,
      `Message`, `Conversation`, `Workflow`, `InstalledApp`, `ApiToolProvider`, and
      related models, and sessions are now passed in explicitly at every call site.
      There is no API surface change, but this removes a long-standing class of `DetachedInstanceError`
      and cross-request session bleed that produced intermittent, hard-to-reproduce
      failures under load.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '`2026_08_27_1200-5578e028b2f2_migrate_legacy_model_types.py` — Data migration
      canonicalizing legacy model types across `provider_models`, `provider_model_credentials`,
      `tenant_default_models`, `provider_model_settings`, and `load_balancing_model_configs`,
      deduplicating colliding rows. This replaces the manual `flask data-migrate legacy-model-types`
      step from 1.16.1 and 1.17.0.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '> The manual `flask data-migrate legacy-model-types` step documented in
      the 1.16.1 and 1.17.0 upgrade guides is **no longer needed**. Migration `5578e028b2f2`
      performs the same canonicalization as part of `flask db upgrade` (#41326).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '> If you already ran the manual command, the migration is a no-op for
      those rows. If you never ran it — and your deployment was upgraded from a version
      earlier than `1.15.0` — this release repairs the affected rows for you. After
      upgrading, verify that your model providers list their models and that previously
      failing models can be loaded and invoked.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: Confirm your model providers still list their models (see Legacy Model
      Types above).
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate Service API dataset segment sessions and ORM models to SQLite
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/40517'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate explore installed app sessions and ORM models to SQLite
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/40525'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate knowledge file access sessions and ORM models to SQLite
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/40596'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate human input sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40597'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): pass session into PipelineCustomizedTemplate.created_user_name
      by @a-yeyang in https://github.com/langgenius/dify/pull/41394'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): pass session into ChildChunk accessors by @keith991001
      in https://github.com/langgenius/dify/pull/41370'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): pass session into WorkflowAppLog accessors by @keith991001
      in https://github.com/langgenius/dify/pull/41440'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(service_api): dep-inject payloads with @model_validate by @ShousenZHANG
      in https://github.com/langgenius/dify/pull/41374'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(controllers/console): dep-inject workflow payloads with @model_validate
      by @Terminator666666 in https://github.com/langgenius/dify/pull/41244'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate application DSL sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40554'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): pass session into Workflow accessors by @jjj-n in https://github.com/langgenius/dify/pull/41464'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(service_api): dep-inject app payloads with @model_validate by
      @ShousenZHANG in https://github.com/langgenius/dify/pull/41491'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(service_api): dep-inject dataset payloads with @model_validate
      by @ShousenZHANG in https://github.com/langgenius/dify/pull/41490'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(console): dep-inject account payloads with @model_validate by
      @ShousenZHANG in https://github.com/langgenius/dify/pull/41500'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(web): dep-inject payloads with @model_validate by @ShousenZHANG
      in https://github.com/langgenius/dify/pull/41501'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate advanced chat generator sessions and ORM models to SQLite
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/40585'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate console dataset sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40521'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate audit findings sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40551'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(console): dep-inject model provider payloads with @model_validate
      by @ShousenZHANG in https://github.com/langgenius/dify/pull/41539'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(service_api): dep-inject query params with @model_validate by
      @ShousenZHANG in https://github.com/langgenius/dify/pull/41562'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): pass session into DocumentSegment and AppDatasetJoin
      accessors by @elyar1124 in https://github.com/langgenius/dify/pull/41568'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): remove legacy db.session property wrappers on Dataset
      by @keith991001 in https://github.com/langgenius/dify/pull/41569'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate workspace member sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40523'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate dataset retrieval sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40548'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate dataset download sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40630'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(service_api): dep-inject segment payloads with @model_validate
      by @ShousenZHANG in https://github.com/langgenius/dify/pull/41571'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(inner_api): dep-inject request payloads with @model_validate
      by @ShousenZHANG in https://github.com/langgenius/dify/pull/41575'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(console,web): dep-inject query params with @model_validate by
      @ShousenZHANG in https://github.com/langgenius/dify/pull/41646'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(service_api): dep-inject the dataset create payload with @model_validate
      by @ShousenZHANG in https://github.com/langgenius/dify/pull/41651'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): remove legacy db.session property wrappers on Document
      by @keith991001 in https://github.com/langgenius/dify/pull/41721'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): use sa.false()/sa.true() for boolean server defaults
      by @Souravrajvi0 in https://github.com/langgenius/dify/pull/41762'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate application generation sessions and ORM models to SQLite
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/40509'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): pass session into tool provider accessors by @a-yeyang
      in https://github.com/langgenius/dify/pull/41830'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): pass session into AppAnnotationHitHistory accessors
      by @a-yeyang in https://github.com/langgenius/dify/pull/41832'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(web): dep-inject the passport query with @model_validate by @ShousenZHANG
      in https://github.com/langgenius/dify/pull/41845'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): remove legacy db.session properties from Conversation
      by @Kiveiru3 in https://github.com/langgenius/dify/pull/41847'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): pass session into AppAnnotationSetting.collection_binding_detail
      by @however-yir in https://github.com/langgenius/dify/pull/41885'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): remove legacy db.session wrappers on Message feedback/annotation
      accessors by @however-yir in https://github.com/langgenius/dify/pull/41883'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(inner_api): dep-inject workspace payloads with @model_validate
      by @ShousenZHANG in https://github.com/langgenius/dify/pull/41540'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(controllers): inject message request models by @Kiveiru3 in https://github.com/langgenius/dify/pull/41884'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): remove legacy db.session property wrappers on DocumentSegment
      and DatasetQuery by @keith991001 in https://github.com/langgenius/dify/pull/41794'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): remove remaining legacy db.session property wrappers
      on Dataset by @keith991001 in https://github.com/langgenius/dify/pull/41647'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): pass session into CustomizedSnippet accessors by @anneheartrecord
      in https://github.com/langgenius/dify/pull/40379'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): pass session into ApiToolProvider.user accessor by @however-yir
      in https://github.com/langgenius/dify/pull/41882'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): remove the last standalone legacy db.session properties
      on Dataset by @keith991001 in https://github.com/langgenius/dify/pull/41911'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): remove legacy db.session wrappers on Message accessors
      by @however-yir in https://github.com/langgenius/dify/pull/41886'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): pass session into InstalledApp.tenant accessor by @ShawYann
      in https://github.com/langgenius/dify/pull/41831'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): remove the legacy db.session wrappers on App by @ShousenZHANG
      in https://github.com/langgenius/dify/pull/41942'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): remove four unread legacy db.session wrappers by @ShousenZHANG
      in https://github.com/langgenius/dify/pull/41964'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): pass session into WorkflowNodeExecutionModel accessors
      by @keith991001 in https://github.com/langgenius/dify/pull/41968'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate provider core entity sessions and ORM models to SQLite by
      @asukaminato0721 in https://github.com/langgenius/dify/pull/40532'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate console dataset document sessions and ORM models to SQLite
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/40522'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate workspace snippet sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40524'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate segment service sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40535'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(models): remove the unread App.author_name db.session wrapper
      by @ShousenZHANG in https://github.com/langgenius/dify/pull/41983'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(controllers/console): inject saved-message query with @model_validate
      by @wr-Jiao in https://github.com/langgenius/dify/pull/41819'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate workflow node execution task sessions and ORM models to
      SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40571'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate console app response sessions and ORM models to SQLite by
      @asukaminato0721 in https://github.com/langgenius/dify/pull/40562'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate console workflow sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40563'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(api): migrate remaining RESTX models to Pydantic by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40399'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate summary index sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40505'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate console dataset metadata sessions and ORM models to SQLite
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/40520'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate custom tool provider ORM model to real entity by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40653'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate Service API app sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40558'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: migrate RAG retrieval sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40512'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: move mocked model and tool cases to unit tests by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40708'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 76-model-support-changes-in-1-17-1
  source_release: dify-2026-09-10-1-17-1-github-386157159-e472b6fe
  source_type: github_releases
  theme: model-support
  title: 76 Model Support changes in 1.17.1
  type: change
related_changes:
- '[[Changes/Suno/2026-09-09-the-v6-family-of-models-enables-new-possibilities|The
  v6 family of models enables new possibilities]]'
- '[[Changes/Suno/2026-09-09-introducing-the-v6-family-of-music-models|Introducing
  the v6 family of music models]]'
- '[[Changes/Claude Code/2026-09-10-2-model-support-changes-in-v2-1-268|2 Model Support
  changes in v2.1.268]]'
source_release: '[[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|dify-2026-09-10-1-17-1-github-386157159-e472b6fe]]'
source_type: github_releases
theme: model-support
title: 76 Model Support changes in 1.17.1
type: change
---

<!-- chronolog:begin region="header" -->
# 76 Model Support changes in 1.17.1

**Dify** · 2026-09-10 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.1) · from [[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|v1.17.1 - Bug Fixes and Improvements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Model Providers**

> **Upgrades from pre-1.15 no longer leave models unusable, and no longer need a manual command.** Installations older than 1.15 still carry legacy model type values (`text-generation`, `embeddings`, `reranking`) in their provider tables, which makes model-related API requests fail and prevents affected models from loading. Both 1.16.1 and 1.17.0 shipped this as a separate `flask data-migrate legacy-model-types` step that had to be run by hand. It now runs as part of `flask db upgrade`: legacy values are canonicalized to `llm` / `text-embedding` / `rerank`, legacy-versus-canonical row collisions are resolved deterministically while preserving credential references, and the provider cache namespace is rotated so stale cached credentials cannot shadow the migrated rows. (#41326, fixes #41294)

> **A single bad LLM node took down the whole editor.** A workflow whose LLM node had `model_selector` persisted as `null` rather than omitted crashed Workflow Studio's per-node checklist on load and tripped the page-level error boundary, making the entire canvas unusable rather than flagging one node. (#41707)

> **Replies from reasoning models rendered entirely as "thinking".** Models such as GLM-5.3 wrap chain-of-thought in `<think>` tags, and a tool call frequently interrupts generation before `</think>` is emitted, leaving the answer nested inside a still-open tag. The dangling tag is now closed when a tool log interrupts the stream, when a new `<think>` starts after real content, and at stream end — plus the same repair in the Markdown preprocessor so already-stored output renders correctly. (#41764)

> **JSON extraction broke on backticks inside JSON.** `parse_json_markdown` picked the first code-fence-like marker anywhere in the text, so a backtick inside a string value — `` {"code": "use `print` function"} `` — or in surrounding prose made extraction start mid-string and fail. Extraction is now anchored on the JSON brackets themselves. This parser backs LLM output parsing for the rule-config generator and dataset retrieval metadata, where backticked code inside JSON is common. (#41959)

> **Explicit database sessions across the ORM layer.** The legacy `db.session` property wrappers were removed from `App`, `Dataset`, `Document`, `DocumentSegment`, `Message`, `Conversation`, `Workflow`, `InstalledApp`, `ApiToolProvider`, and related models, and sessions are now passed in explicitly at every call site. There is no API surface change, but this removes a long-standing class of `DetachedInstanceError` and cross-request session bleed that produced intermittent, hard-to-reproduce failures under load.

> `2026_08_27_1200-5578e028b2f2_migrate_legacy_model_types.py` — Data migration canonicalizing legacy model types across `provider_models`, `provider_model_credentials`, `tenant_default_models`, `provider_model_settings`, and `load_balancing_model_configs`, deduplicating colliding rows. This replaces the manual `flask data-migrate legacy-model-types` step from 1.16.1 and 1.17.0.

> > The manual `flask data-migrate legacy-model-types` step documented in the 1.16.1 and 1.17.0 upgrade guides is **no longer needed**. Migration `5578e028b2f2` performs the same canonicalization as part of `flask db upgrade` (#41326).

> > If you already ran the manual command, the migration is a no-op for those rows. If you never ran it — and your deployment was upgraded from a version earlier than `1.15.0` — this release repairs the affected rows for you. After upgrading, verify that your model providers list their models and that previously failing models can be loaded and invoked.

> Confirm your model providers still list their models (see Legacy Model Types above).

> test: migrate Service API dataset segment sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40517

> test: migrate explore installed app sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40525

> test: migrate knowledge file access sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40596

> test: migrate human input sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40597

> refactor(models): pass session into PipelineCustomizedTemplate.created_user_name by @a-yeyang in https://github.com/langgenius/dify/pull/41394

> refactor(models): pass session into ChildChunk accessors by @keith991001 in https://github.com/langgenius/dify/pull/41370

> refactor(models): pass session into WorkflowAppLog accessors by @keith991001 in https://github.com/langgenius/dify/pull/41440

> refactor(service_api): dep-inject payloads with @model_validate by @ShousenZHANG in https://github.com/langgenius/dify/pull/41374

> refactor(controllers/console): dep-inject workflow payloads with @model_validate by @Terminator666666 in https://github.com/langgenius/dify/pull/41244

> test: migrate application DSL sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40554

> refactor(models): pass session into Workflow accessors by @jjj-n in https://github.com/langgenius/dify/pull/41464

> refactor(service_api): dep-inject app payloads with @model_validate by @ShousenZHANG in https://github.com/langgenius/dify/pull/41491

> refactor(service_api): dep-inject dataset payloads with @model_validate by @ShousenZHANG in https://github.com/langgenius/dify/pull/41490

> refactor(console): dep-inject account payloads with @model_validate by @ShousenZHANG in https://github.com/langgenius/dify/pull/41500

> refactor(web): dep-inject payloads with @model_validate by @ShousenZHANG in https://github.com/langgenius/dify/pull/41501

> test: migrate advanced chat generator sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40585

> test: migrate console dataset sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40521

> test: migrate audit findings sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40551

> refactor(console): dep-inject model provider payloads with @model_validate by @ShousenZHANG in https://github.com/langgenius/dify/pull/41539

> refactor(service_api): dep-inject query params with @model_validate by @ShousenZHANG in https://github.com/langgenius/dify/pull/41562

> refactor(models): pass session into DocumentSegment and AppDatasetJoin accessors by @elyar1124 in https://github.com/langgenius/dify/pull/41568

> refactor(models): remove legacy db.session property wrappers on Dataset by @keith991001 in https://github.com/langgenius/dify/pull/41569

> test: migrate workspace member sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40523

> test: migrate dataset retrieval sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40548

> test: migrate dataset download sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40630

> refactor(service_api): dep-inject segment payloads with @model_validate by @ShousenZHANG in https://github.com/langgenius/dify/pull/41571

> refactor(inner_api): dep-inject request payloads with @model_validate by @ShousenZHANG in https://github.com/langgenius/dify/pull/41575

> refactor(console,web): dep-inject query params with @model_validate by @ShousenZHANG in https://github.com/langgenius/dify/pull/41646

> refactor(service_api): dep-inject the dataset create payload with @model_validate by @ShousenZHANG in https://github.com/langgenius/dify/pull/41651

> refactor(models): remove legacy db.session property wrappers on Document by @keith991001 in https://github.com/langgenius/dify/pull/41721

> refactor(models): use sa.false()/sa.true() for boolean server defaults by @Souravrajvi0 in https://github.com/langgenius/dify/pull/41762

> test: migrate application generation sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40509

> refactor(models): pass session into tool provider accessors by @a-yeyang in https://github.com/langgenius/dify/pull/41830

> refactor(models): pass session into AppAnnotationHitHistory accessors by @a-yeyang in https://github.com/langgenius/dify/pull/41832

> refactor(web): dep-inject the passport query with @model_validate by @ShousenZHANG in https://github.com/langgenius/dify/pull/41845

> refactor(models): remove legacy db.session properties from Conversation by @Kiveiru3 in https://github.com/langgenius/dify/pull/41847

> refactor(models): pass session into AppAnnotationSetting.collection_binding_detail by @however-yir in https://github.com/langgenius/dify/pull/41885

> refactor(models): remove legacy db.session wrappers on Message feedback/annotation accessors by @however-yir in https://github.com/langgenius/dify/pull/41883

> refactor(inner_api): dep-inject workspace payloads with @model_validate by @ShousenZHANG in https://github.com/langgenius/dify/pull/41540

> refactor(controllers): inject message request models by @Kiveiru3 in https://github.com/langgenius/dify/pull/41884

> refactor(models): remove legacy db.session property wrappers on DocumentSegment and DatasetQuery by @keith991001 in https://github.com/langgenius/dify/pull/41794

> refactor(models): remove remaining legacy db.session property wrappers on Dataset by @keith991001 in https://github.com/langgenius/dify/pull/41647

> refactor(models): pass session into CustomizedSnippet accessors by @anneheartrecord in https://github.com/langgenius/dify/pull/40379

> refactor(models): pass session into ApiToolProvider.user accessor by @however-yir in https://github.com/langgenius/dify/pull/41882

> refactor(models): remove the last standalone legacy db.session properties on Dataset by @keith991001 in https://github.com/langgenius/dify/pull/41911

> refactor(models): remove legacy db.session wrappers on Message accessors by @however-yir in https://github.com/langgenius/dify/pull/41886

> refactor(models): pass session into InstalledApp.tenant accessor by @ShawYann in https://github.com/langgenius/dify/pull/41831

> refactor(models): remove the legacy db.session wrappers on App by @ShousenZHANG in https://github.com/langgenius/dify/pull/41942

> refactor(models): remove four unread legacy db.session wrappers by @ShousenZHANG in https://github.com/langgenius/dify/pull/41964

> refactor(models): pass session into WorkflowNodeExecutionModel accessors by @keith991001 in https://github.com/langgenius/dify/pull/41968

> test: migrate provider core entity sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40532

> test: migrate console dataset document sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40522

> test: migrate workspace snippet sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40524

> test: migrate segment service sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40535

> refactor(models): remove the unread App.author_name db.session wrapper by @ShousenZHANG in https://github.com/langgenius/dify/pull/41983

> refactor(controllers/console): inject saved-message query with @model_validate by @wr-Jiao in https://github.com/langgenius/dify/pull/41819

> test: migrate workflow node execution task sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40571

> test: migrate console app response sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40562

> test: migrate console workflow sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40563

> refactor(api): migrate remaining RESTX models to Pydantic by @asukaminato0721 in https://github.com/langgenius/dify/pull/40399

> test: migrate summary index sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40505

> test: migrate console dataset metadata sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40520

> test: migrate custom tool provider ORM model to real entity by @asukaminato0721 in https://github.com/langgenius/dify/pull/40653

> test: migrate Service API app sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40558

> test: migrate RAG retrieval sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40512

> test: move mocked model and tool cases to unit tests by @asukaminato0721 in https://github.com/langgenius/dify/pull/40708

Source: https://github.com/langgenius/dify/releases/tag/1.17.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-09-10-4-pricing-model-changes-in-1-17-1|4 Pricing Model changes in 1.17.1]] · Pricing Model
- [[Changes/Dify/2026-09-10-3-automation-and-scheduling-changes-in-1-17-1|3 Automation and Scheduling changes in 1.17.1]] · Automation and Scheduling
- [[Changes/Dify/2026-09-10-8-interface-experience-changes-in-1-17-1|8 Interface Experience changes in 1.17.1]] · Interface Experience
- [[Changes/Dify/2026-09-10-42-agent-mode-changes-in-1-17-1|42 Agent Mode changes in 1.17.1]] · Agent Mode
- [[Changes/Dify/2026-09-10-4-developer-workflow-changes-in-1-17-1|4 Developer Workflow changes in 1.17.1]] · Developer Workflow
- [[Changes/Dify/2026-09-10-3-collaboration-changes-in-1-17-1|3 Collaboration changes in 1.17.1]] · Collaboration
- [[Changes/Dify/2026-09-10-2-memory-and-personalization-changes-in-1-17-1|2 Memory and Personalization changes in 1.17.1]] · Memory and Personalization
- [[Changes/Dify/2026-09-10-16-safety-and-privacy-changes-in-1-17-1|16 Safety and Privacy changes in 1.17.1]] · Safety and Privacy
- [[Changes/Dify/2026-09-10-13-files-and-data-changes-in-1-17-1|13 Files and Data changes in 1.17.1]] · Files and Data
- [[Changes/Dify/2026-09-10-skill-packages-built-on-windows-failed-with-a-misleading-error-a-skill-md-using|Skill packages built on Windows failed with a misleading error. A SKILL.md…]] · Mobile and Desktop
- [[Changes/Dify/2026-09-10-12-apps-and-integrations-changes-in-1-17-1|12 Apps and Integrations changes in 1.17.1]] · Apps and Integrations
- [[Changes/Dify/2026-09-10-6-account-and-access-changes-in-1-17-1|6 Account and Access changes in 1.17.1]] · Account and Access
- [[Changes/Dify/2026-09-10-3-multimodal-input-changes-in-1-17-1|3 Multimodal Input changes in 1.17.1]] · Multimodal Input
- [[Changes/Dify/2026-09-10-6-editor-experience-changes-in-1-17-1|6 Editor Experience changes in 1.17.1]] · Editor Experience
- [[Changes/Dify/2026-09-10-3-accessibility-and-localization-changes-in-1-17-1|3 Accessibility and Localization changes in 1.17.1]] · Accessibility and Localization
- [[Changes/Dify/2026-09-10-a-plugin-could-exhaust-worker-memory-with-one-declared-number-the-blob-chunk-mer|A plugin could exhaust worker memory with one declared number. The blob chunk…]] · Reliability and Performance
- [[Changes/Dify/2026-09-10-6-context-window-changes-in-1-17-1|6 Context Window changes in 1.17.1]] · Context Window
- [[Changes/Dify/2026-09-10-205-other-changes-in-1-17-1|205 other changes in 1.17.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-10 · Claude Code · [[Changes/Claude Code/2026-09-10-2-model-support-changes-in-v2-1-268|2 Model Support changes in v2.1.268]]
- Later: 2026-09-10 · Raycast · [[Changes/Raycast/2026-09-10-ai-models-are-now-grouped-more-consistently-by-provider-including-models-from-ve|AI: Models are now grouped more consistently by provider, including models…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-09-10-283af5&body=Card%3A%20Changes%2FDify%2F2026-09-10-76-model-support-changes-in-1-17-1.md%0ACard%20ID%3A%20dify-2026-09-10-283af5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->