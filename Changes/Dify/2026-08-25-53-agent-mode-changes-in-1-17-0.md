---
card_id: dify-2026-08-25-7de2d4
date: '2026-08-25'
description: 'Dify · 2026-08-25 · Agent Mode: 53 changes in v1.17.0 — New GenAI spans
  surface LLM TTFT, agent ReAct steps, tool calls, and failed LLM nodes for deeper…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1146
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 74d729b34293eaa9634d7ea64b135baf7596d8e752c2b9f2ea4a79d068b31615
product: dify
product_name: Dify
record:
  card_id: dify-2026-08-25-7de2d4
  comparison: ''
  date: '2026-08-25'
  description: 'Dify — v1.17.0: 53 Agent Mode changes'
  evidence:
  - quote: New GenAI spans surface LLM TTFT, agent ReAct steps, tool calls, and failed
      LLM nodes for deeper observability (#39339).
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '**SSRF & outbound hardening**: outbound HTTP connect phases are bounded
      (5s), agent/binding download and run timeouts are configurable, and the SSRF-blocked
      error message now points to the correct issue (#40807, #41027, #40605).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'Prevent cross-tab chat conversation switching and stop dropping non-vision
      attachments in agent chat (#40709, #40179).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '`DIFY_AGENT_RUNTIME_BACKEND`, `DIFY_AGENT_RUN_TIMEOUT_SECONDS`, `DIFY_AGENT_SANDBOX_FILES_BASE_URL`,
      `DIFY_AGENT_STUB_UPLOAD_FILE_SIZE_LIMIT`, `DIFY_AGENT_BINDING_FILE_DOWNLOAD_COMMAND_TIMEOUT_SECONDS`'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'E2B: `DIFY_AGENT_E2B_API_KEY`, `DIFY_AGENT_E2B_TEMPLATE`, `DIFY_AGENT_E2B_SHELLCTL_PORT`,
      `DIFY_AGENT_E2B_ACTIVE_TIMEOUT_SECONDS`'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'Outbound HTTP tuning: `DIFY_AGENT_OUTBOUND_HTTP_CONNECT_TIMEOUT`, `DIFY_AGENT_OUTBOUND_HTTP_READ_TIMEOUT`,
      `DIFY_AGENT_OUTBOUND_HTTP_WRITE_TIMEOUT`, `DIFY_AGENT_OUTBOUND_HTTP_POOL_TIMEOUT`,
      `DIFY_AGENT_OUTBOUND_HTTP_KEEPALIVE_EXPIRY`, `DIFY_AGENT_OUTBOUND_HTTP_MAX_CONNECTIONS`,
      `DIFY_AGENT_OUTBOUND_HTTP_MAX_KEEPALIVE_CONNECTIONS`'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '`AGENT_BACKEND_BINDING_FILE_DOWNLOAD_TIMEOUT_SECONDS`, `AGENT_BACKEND_HOME_SNAPSHOT_TIMEOUT_SECONDS`
      (`api/.env.example`)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '`AGENT_BACKEND_RUN_TIMEOUT_SECONDS` → replaced by `DIFY_AGENT_RUN_TIMEOUT_SECONDS`'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '`DIFY_AGENT_SHELLCTL_AUTH_TOKEN`, `DIFY_AGENT_SHELLCTL_ENTRYPOINT` (agent
      runtime reworked)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '`add_agent_home_snapshot_ledger`, `make_home_snapshot_references_nullable`
      — agent build-time Home Snapshot ledger and nullable snapshot references'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '`replace_agent_runtime_sessions_with_*`, `remove_agent_drive`, `clean_legacy_agent_soul_files`,
      `simplify_agent_v2_output_contract` — new agent runtime'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: use sqlite3 session in test_agent_app_feature_service by @asukaminato0721
      in https://github.com/langgenius/dify/pull/38724'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat: label agent conversation reset action on hover by @iamjoel in https://github.com/langgenius/dify/pull/39691'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor: introduce agent working environment architecture by @BeautyyuYanli
      in https://github.com/langgenius/dify/pull/39480'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test(e2e): align Agent tool credential states by @lyzno1 in https://github.com/langgenius/dify/pull/39698'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat(agent): make home snapshots optional and use backend defaults by
      @BeautyyuYanli in https://github.com/langgenius/dify/pull/39702'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat: add upload size guidance and validation for agent files and skills
      by @iamjoel in https://github.com/langgenius/dify/pull/39798'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: use SQLite sessions in services agent by @asukaminato0721 in https://github.com/langgenius/dify/pull/39054'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore: keep dify-agent env same with dify by @fatelei in https://github.com/langgenius/dify/pull/39918'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore(deps): bump cryptography from 49.0.0 to 50.0.0 in /dify-agent by
      @dependabot[bot] in https://github.com/langgenius/dify/pull/39958'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat(agent): separate CLI file URL audiences by @BeautyyuYanli in https://github.com/langgenius/dify/pull/39952'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: use sqlite3 session in test_agent_config_service by @asukaminato0721
      in https://github.com/langgenius/dify/pull/38764'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat(trace-aliyun): GenAI spans for LLM TTFT, agent ReAct, tools, and
      failed LLM nodes by @123liuziming in https://github.com/langgenius/dify/pull/39339'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test(e2e): align duplicate Agent publish state by @lyzno1 in https://github.com/langgenius/dify/pull/40108'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor(dify-agent): make config pulls direct and remove gRPC by @BeautyyuYanli
      in https://github.com/langgenius/dify/pull/40044'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat(dify-agent): propagate run limit error types by @BeautyyuYanli in
      https://github.com/langgenius/dify/pull/40116'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor(dify-agent): download Binding files through Agent Stub by @BeautyyuYanli
      in https://github.com/langgenius/dify/pull/40143'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor: replace manual model_validate with @model_validate in agent
      controllers by @likalikali in https://github.com/langgenius/dify/pull/40233'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore(deps): bump pymdown-extensions from 11.0 to 11.0.1 in /dify-agent
      by @dependabot[bot] in https://github.com/langgenius/dify/pull/40183'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'docs(web): add Next.js agent rules by @lyzno1 in https://github.com/langgenius/dify/pull/40398'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate agent drive end-user ORM models to real entities by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40654'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore(deps): bump pydantic-ai-slim from 1.102.0 to 1.106.0 in /dify-agent
      by @dependabot[bot] in https://github.com/langgenius/dify/pull/40736'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat(dify-agent): expand and enforce agent run limits by @BeautyyuYanli
      in https://github.com/langgenius/dify/pull/40641'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate agent surface sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40602'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate agent controller sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40600'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test(e2e): align agent model selector locators by @lyzno1 in https://github.com/langgenius/dify/pull/40862'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat: dispatch New Agent Beta eligibility checks by @hjlarry in https://github.com/langgenius/dify/pull/40725'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat(dify-agent): enforce signed upload size limits by @BeautyyuYanli
      in https://github.com/langgenius/dify/pull/40883'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore(dify-agent): disable Landlock for E2B templates by @BeautyyuYanli
      in https://github.com/langgenius/dify/pull/40892'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate agent runtime sessions and ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40587'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor(agent): remove Agent Drive by @BeautyyuYanli in https://github.com/langgenius/dify/pull/40887'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'perf(dify-agent): parallelize Agent Stub config pulls by @BeautyyuYanli
      in https://github.com/langgenius/dify/pull/40973'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor(dify-agent): use Workspace as shell temp space by @BeautyyuYanli
      in https://github.com/langgenius/dify/pull/41023'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate Agent App session store to SQLite ORM by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40638'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate console agent skill ORM models to SQLite by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40570'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat: Enterprise Home Snapshot — runtime endpoints and dify-agent adapter
      by @GareArc in https://github.com/langgenius/dify/pull/40996'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'refactor(agent): simplify Agent v2 output contract by @BeautyyuYanli in
      https://github.com/langgenius/dify/pull/41062'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat: support agent skill by @fatelei in https://github.com/langgenius/dify/pull/39675'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore: show full agent save time on hover by @iamjoel in https://github.com/langgenius/dify/pull/41148'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'perf(agent): polling interval tuning by @wylswz in https://github.com/langgenius/dify/pull/41221'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'perf(agent): exponential backoff in polling to prevent forking storm by
      @wylswz in https://github.com/langgenius/dify/pull/41222'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat(api): support New Agent Beta for inline Workflow agents by @hjlarry
      in https://github.com/langgenius/dify/pull/41215'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'feat: hide add library skill in agent ui by @fatelei in https://github.com/langgenius/dify/pull/41250'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 53-agent-mode-changes-in-1-17-0
  source_release: dify-2026-08-25-1-17-0-github-376348099-66c16161
  source_type: github_releases
  theme: agent-mode
  title: 53 Agent Mode changes in 1.17.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-08-24-elevenagents|ElevenAgents]]'
- '[[Changes/ElevenLabs/2026-08-24-procedures|Procedures]]'
- '[[Changes/Claude Code/2026-08-25-improved-subagent-results-a-subagent-that-stops-at-its-maxturns-limit-now-return|Improved
  subagent results]]'
source_release: '[[Releases/Dify/dify-2026-08-25-1-17-0-github-376348099-66c16161|dify-2026-08-25-1-17-0-github-376348099-66c16161]]'
source_type: github_releases
theme: agent-mode
title: 53 Agent Mode changes in 1.17.0
type: change
---

<!-- chronolog:begin region="header" -->
# 53 Agent Mode changes in 1.17.0

**Dify** · 2026-08-25 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.0) · from [[Releases/Dify/dify-2026-08-25-1-17-0-github-376348099-66c16161|v1.17.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> New GenAI spans surface LLM TTFT, agent ReAct steps, tool calls, and failed LLM nodes for deeper observability (#39339).

> **SSRF & outbound hardening**: outbound HTTP connect phases are bounded (5s), agent/binding download and run timeouts are configurable, and the SSRF-blocked error message now points to the correct issue (#40807, #41027, #40605).

> Prevent cross-tab chat conversation switching and stop dropping non-vision attachments in agent chat (#40709, #40179).

> `DIFY_AGENT_RUNTIME_BACKEND`, `DIFY_AGENT_RUN_TIMEOUT_SECONDS`, `DIFY_AGENT_SANDBOX_FILES_BASE_URL`, `DIFY_AGENT_STUB_UPLOAD_FILE_SIZE_LIMIT`, `DIFY_AGENT_BINDING_FILE_DOWNLOAD_COMMAND_TIMEOUT_SECONDS`

> E2B: `DIFY_AGENT_E2B_API_KEY`, `DIFY_AGENT_E2B_TEMPLATE`, `DIFY_AGENT_E2B_SHELLCTL_PORT`, `DIFY_AGENT_E2B_ACTIVE_TIMEOUT_SECONDS`

> Outbound HTTP tuning: `DIFY_AGENT_OUTBOUND_HTTP_CONNECT_TIMEOUT`, `DIFY_AGENT_OUTBOUND_HTTP_READ_TIMEOUT`, `DIFY_AGENT_OUTBOUND_HTTP_WRITE_TIMEOUT`, `DIFY_AGENT_OUTBOUND_HTTP_POOL_TIMEOUT`, `DIFY_AGENT_OUTBOUND_HTTP_KEEPALIVE_EXPIRY`, `DIFY_AGENT_OUTBOUND_HTTP_MAX_CONNECTIONS`, `DIFY_AGENT_OUTBOUND_HTTP_MAX_KEEPALIVE_CONNECTIONS`

> `AGENT_BACKEND_BINDING_FILE_DOWNLOAD_TIMEOUT_SECONDS`, `AGENT_BACKEND_HOME_SNAPSHOT_TIMEOUT_SECONDS` (`api/.env.example`)

> `AGENT_BACKEND_RUN_TIMEOUT_SECONDS` → replaced by `DIFY_AGENT_RUN_TIMEOUT_SECONDS`

> `DIFY_AGENT_SHELLCTL_AUTH_TOKEN`, `DIFY_AGENT_SHELLCTL_ENTRYPOINT` (agent runtime reworked)

> `add_agent_home_snapshot_ledger`, `make_home_snapshot_references_nullable` — agent build-time Home Snapshot ledger and nullable snapshot references

> `replace_agent_runtime_sessions_with_*`, `remove_agent_drive`, `clean_legacy_agent_soul_files`, `simplify_agent_v2_output_contract` — new agent runtime

> test: use sqlite3 session in test_agent_app_feature_service by @asukaminato0721 in https://github.com/langgenius/dify/pull/38724

> feat: label agent conversation reset action on hover by @iamjoel in https://github.com/langgenius/dify/pull/39691

> refactor: introduce agent working environment architecture by @BeautyyuYanli in https://github.com/langgenius/dify/pull/39480

> test(e2e): align Agent tool credential states by @lyzno1 in https://github.com/langgenius/dify/pull/39698

> feat(agent): make home snapshots optional and use backend defaults by @BeautyyuYanli in https://github.com/langgenius/dify/pull/39702

> feat: add upload size guidance and validation for agent files and skills by @iamjoel in https://github.com/langgenius/dify/pull/39798

> test: use SQLite sessions in services agent by @asukaminato0721 in https://github.com/langgenius/dify/pull/39054

> chore: keep dify-agent env same with dify by @fatelei in https://github.com/langgenius/dify/pull/39918

> chore(deps): bump cryptography from 49.0.0 to 50.0.0 in /dify-agent by @dependabot[bot] in https://github.com/langgenius/dify/pull/39958

> feat(agent): separate CLI file URL audiences by @BeautyyuYanli in https://github.com/langgenius/dify/pull/39952

> test: use sqlite3 session in test_agent_config_service by @asukaminato0721 in https://github.com/langgenius/dify/pull/38764

> feat(trace-aliyun): GenAI spans for LLM TTFT, agent ReAct, tools, and failed LLM nodes by @123liuziming in https://github.com/langgenius/dify/pull/39339

> test(e2e): align duplicate Agent publish state by @lyzno1 in https://github.com/langgenius/dify/pull/40108

> refactor(dify-agent): make config pulls direct and remove gRPC by @BeautyyuYanli in https://github.com/langgenius/dify/pull/40044

> feat(dify-agent): propagate run limit error types by @BeautyyuYanli in https://github.com/langgenius/dify/pull/40116

> refactor(dify-agent): download Binding files through Agent Stub by @BeautyyuYanli in https://github.com/langgenius/dify/pull/40143

> refactor: replace manual model_validate with @model_validate in agent controllers by @likalikali in https://github.com/langgenius/dify/pull/40233

> chore(deps): bump pymdown-extensions from 11.0 to 11.0.1 in /dify-agent by @dependabot[bot] in https://github.com/langgenius/dify/pull/40183

> docs(web): add Next.js agent rules by @lyzno1 in https://github.com/langgenius/dify/pull/40398

> test: migrate agent drive end-user ORM models to real entities by @asukaminato0721 in https://github.com/langgenius/dify/pull/40654

> chore(deps): bump pydantic-ai-slim from 1.102.0 to 1.106.0 in /dify-agent by @dependabot[bot] in https://github.com/langgenius/dify/pull/40736

> feat(dify-agent): expand and enforce agent run limits by @BeautyyuYanli in https://github.com/langgenius/dify/pull/40641

> test: migrate agent surface sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40602

> test: migrate agent controller sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40600

> test(e2e): align agent model selector locators by @lyzno1 in https://github.com/langgenius/dify/pull/40862

> feat: dispatch New Agent Beta eligibility checks by @hjlarry in https://github.com/langgenius/dify/pull/40725

> feat(dify-agent): enforce signed upload size limits by @BeautyyuYanli in https://github.com/langgenius/dify/pull/40883

> chore(dify-agent): disable Landlock for E2B templates by @BeautyyuYanli in https://github.com/langgenius/dify/pull/40892

> test: migrate agent runtime sessions and ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40587

> refactor(agent): remove Agent Drive by @BeautyyuYanli in https://github.com/langgenius/dify/pull/40887

> perf(dify-agent): parallelize Agent Stub config pulls by @BeautyyuYanli in https://github.com/langgenius/dify/pull/40973

> refactor(dify-agent): use Workspace as shell temp space by @BeautyyuYanli in https://github.com/langgenius/dify/pull/41023

> test: migrate Agent App session store to SQLite ORM by @asukaminato0721 in https://github.com/langgenius/dify/pull/40638

> test: migrate console agent skill ORM models to SQLite by @asukaminato0721 in https://github.com/langgenius/dify/pull/40570

> feat: Enterprise Home Snapshot — runtime endpoints and dify-agent adapter by @GareArc in https://github.com/langgenius/dify/pull/40996

> refactor(agent): simplify Agent v2 output contract by @BeautyyuYanli in https://github.com/langgenius/dify/pull/41062

> feat: support agent skill by @fatelei in https://github.com/langgenius/dify/pull/39675

> chore: show full agent save time on hover by @iamjoel in https://github.com/langgenius/dify/pull/41148

> perf(agent): polling interval tuning by @wylswz in https://github.com/langgenius/dify/pull/41221

> perf(agent): exponential backoff in polling to prevent forking storm by @wylswz in https://github.com/langgenius/dify/pull/41222

> feat(api): support New Agent Beta for inline Workflow agents by @hjlarry in https://github.com/langgenius/dify/pull/41215

> feat: hide add library skill in agent ui by @fatelei in https://github.com/langgenius/dify/pull/41250

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
- [[Changes/Dify/2026-08-25-4-developer-workflow-changes-in-1-17-0|4 Developer Workflow changes in 1.17.0]] · Developer Workflow
- [[Changes/Dify/2026-08-25-93-model-support-changes-in-1-17-0|93 Model Support changes in 1.17.0]] · Model Support
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
## Nearby in Agent Mode

- Earlier: 2026-08-25 · Claude Code · [[Changes/Claude Code/2026-08-25-improved-subagent-results-a-subagent-that-stops-at-its-maxturns-limit-now-return|Improved subagent results]]
- Later: 2026-08-25 · Gemini CLI · [[Changes/Gemini CLI/2026-08-25-8-agent-mode-changes-in-v0-57-0|8 Agent Mode changes in v0.57.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-08-25-7de2d4&body=Card%3A%20Changes%2FDify%2F2026-08-25-53-agent-mode-changes-in-1-17-0.md%0ACard%20ID%3A%20dify-2026-08-25-7de2d4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->