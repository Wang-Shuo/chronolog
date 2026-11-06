---
card_id: elevenlabs-2026-07-27-9c1cea
date: '2026-07-27'
description: 'ElevenLabs · 2026-07-27 · Agent Mode: `POST /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures`'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1117
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 0ac68107efaac1b27133251be96acc8dc1da740e918dd1d0df74c123d1f50e2a
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-07-27-9c1cea
  comparison: ''
  confidence: low
  date: '2026-07-27'
  description: 'ElevenLabs — ElevenLabs updates — 2026-07-27: `POST /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures`'
  evidence:
  - quote: '`POST /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures`'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Creates a procedure and returns its `procedure_id` (string)
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Accepts optional `name` (string, maximum 200 characters), `content` (string),
      `type` (`ProcedureType`, default `free_form`) and `trigger` (nullable string)
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '`GET /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures`'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Lists branch procedures with `procedure_id`, `version_id`, `name`, `type`,
      `trigger` and `has_draft`
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Excludes procedure content; retrieve an individual procedure to read its
      content
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '`GET /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}`'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Accepts optional `version_id` (string); otherwise returns the version at
      the branch head
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Returns `name`, `content`, `type` and `trigger`
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '`DELETE /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}`'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Removes the procedure from the branch's draft working set
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '`GET /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}/draft`'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Returns the current procedure draft
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '`PATCH /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}/draft`'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Creates or updates a draft
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Requires `name` (string, maximum 200 characters), `content` (string, maximum
      50,000 characters) and `type` (`ProcedureType`); accepts optional `trigger`
      (nullable string)
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '`DELETE /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}/draft`'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Discards draft changes and resets the procedure to its committed version
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '`POST /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/compile`'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Compiles procedure drafts into an `AgentWorkflowResponseModel`
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '[Create crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/create-crawl-job)
      - `POST /v1/convai/knowledge-base/crawl`'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Requires `url` (string)
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Accepts optional `max_depth` (integer, 1–5, default `3`), `max_pages` (integer,
      1–10,000, default `1000`), `pattern` (string), `sitemap_urls` (string array),
      `parent_folder_id` (string), `enable_auto_sync` (boolean, default `false`) and
      `auto_remove` (boolean, default `false`)
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '[List crawl jobs](https://elevenlabs.io/docs/api-reference/knowledge-base/list-crawl-jobs)
      - `GET /v1/convai/knowledge-base/crawl`'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Accepts optional `include_job_ids` (string array), `page_size` (integer,
      1–100, default `30`) and `cursor` (string)
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '[Get crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/get-crawl-job)
      - `GET /v1/convai/knowledge-base/crawl/{crawl_job_id}`'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '[Cancel crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/cancel-crawl-job)
      - `POST /v1/convai/knowledge-base/crawl/{crawl_job_id}/cancel`'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '[Get dependent agents for multiple documents](https://elevenlabs.io/docs/api-reference/knowledge-base/dependent-agents-multiple)
      - `POST /v1/convai/knowledge-base/dependent-agents`'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Requires `document_ids` (array of 1–20 unique strings)
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Accepts optional `dependent_type` (`KnowledgeBaseDependentType`, default
      `all`), `page_size` (integer, 1–100, default `30`) and `cursor` (string)
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '[Bulk delete knowledge base documents](https://elevenlabs.io/docs/api-reference/knowledge-base/bulk-delete)
      - `POST /v1/convai/knowledge-base/bulk-delete`'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Accepts optional `force` (boolean, default `false`)
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Returns a success or failure result for each document ID
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '[Export batch call results](https://elevenlabs.io/docs/api-reference/batch-calling/export)
      - `GET /v1/convai/batch-calling/{batch_id}/export`'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: Returns terminal batch recipients and conversation results as CSV
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-07-27-2026-07-27-29809f38
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-07-23-3-agent-mode-changes-in-v1-0-74|3 Agent
  Mode changes in v1.0.74]]'
- '[[Changes/Claude Code/2026-07-24-4-agent-mode-changes-in-v2-1-219|4 Agent Mode
  changes in v2.1.219]]'
- '[[Changes/ElevenLabs/2026-07-27-elevenagents|ElevenAgents]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-07-27-2026-07-27-29809f38|elevenlabs-2026-07-27-2026-07-27-29809f38]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-07-27 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/7/27) · from [[Releases/ElevenLabs/elevenlabs-2026-07-27-2026-07-27-29809f38|ElevenLabs updates — 2026-07-27]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `POST /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures`
>
> Creates a procedure and returns its `procedure_id` (string)
>
> Accepts optional `name` (string, maximum 200 characters), `content` (string), `type` (`ProcedureType`, default `free_form`) and `trigger` (nullable string)
>
> `GET /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures`
>
> Lists branch procedures with `procedure_id`, `version_id`, `name`, `type`, `trigger` and `has_draft`
>
> Excludes procedure content; retrieve an individual procedure to read its content
>
> `GET /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}`
>
> Accepts optional `version_id` (string); otherwise returns the version at the branch head
>
> Returns `name`, `content`, `type` and `trigger`
>
> `DELETE /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}`
>
> Removes the procedure from the branch's draft working set
>
> `GET /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}/draft`
>
> Returns the current procedure draft
>
> `PATCH /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}/draft`
>
> Creates or updates a draft
>
> Requires `name` (string, maximum 200 characters), `content` (string, maximum 50,000 characters) and `type` (`ProcedureType`); accepts optional `trigger` (nullable string)
>
> `DELETE /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}/draft`
>
> Discards draft changes and resets the procedure to its committed version
>
> `POST /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/compile`
>
> Compiles procedure drafts into an `AgentWorkflowResponseModel`
>
> [Create crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/create-crawl-job) - `POST /v1/convai/knowledge-base/crawl`
>
> Requires `url` (string)
>
> Accepts optional `max_depth` (integer, 1–5, default `3`), `max_pages` (integer, 1–10,000, default `1000`), `pattern` (string), `sitemap_urls` (string array), `parent_folder_id` (string), `enable_auto_sync` (boolean, default `false`) and `auto_remove` (boolean, default `false`)
>
> [List crawl jobs](https://elevenlabs.io/docs/api-reference/knowledge-base/list-crawl-jobs) - `GET /v1/convai/knowledge-base/crawl`
>
> Accepts optional `include_job_ids` (string array), `page_size` (integer, 1–100, default `30`) and `cursor` (string)
>
> [Get crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/get-crawl-job) - `GET /v1/convai/knowledge-base/crawl/{crawl_job_id}`
>
> [Cancel crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/cancel-crawl-job) - `POST /v1/convai/knowledge-base/crawl/{crawl_job_id}/cancel`
>
> [Get dependent agents for multiple documents](https://elevenlabs.io/docs/api-reference/knowledge-base/dependent-agents-multiple) - `POST /v1/convai/knowledge-base/dependent-agents`
>
> Requires `document_ids` (array of 1–20 unique strings)
>
> Accepts optional `dependent_type` (`KnowledgeBaseDependentType`, default `all`), `page_size` (integer, 1–100, default `30`) and `cursor` (string)
>
> [Bulk delete knowledge base documents](https://elevenlabs.io/docs/api-reference/knowledge-base/bulk-delete) - `POST /v1/convai/knowledge-base/bulk-delete`
>
> Accepts optional `force` (boolean, default `false`)
>
> Returns a success or failure result for each document ID
>
> [Export batch call results](https://elevenlabs.io/docs/api-reference/batch-calling/export) - `GET /v1/convai/batch-calling/{batch_id}/export`
>
> Returns terminal batch recipients and conversation results as CSV
>
> Source: https://elevenlabs.io/docs/changelog/2026/7/27
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-07-27-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-27-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-07-27-studio|Studio]] · Collaboration
- [[Changes/ElevenLabs/2026-07-27-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-07-27-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-27-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-27-voices|Voices]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-07-24 · Claude Code · [[Changes/Claude Code/2026-07-24-4-agent-mode-changes-in-v2-1-219|4 Agent Mode changes in v2.1.219]]
- Later: 2026-07-27 · Open WebUI · [[Changes/Open WebUI/2026-07-27-sub-agents-administrators-can-now-enable-sub-agents-which-let-a-model-hand-parts|🤖 Sub-agents. Administrators can now enable sub-agents, which let a model hand…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-07-27-9c1cea&body=Card%3A%20Changes%2FElevenLabs%2F2026-07-27-elevenagents-9c1cea.md%0ACard%20ID%3A%20elevenlabs-2026-07-27-9c1cea%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F7%2F27%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->