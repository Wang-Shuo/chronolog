---
draft: true
machine_hash: 03f5bbe77a86dd3ae8ae24e656d51a2498dd13b7a102b5eaf9a049e6cace1fd3
product: elevenlabs
record:
  card_id: elevenlabs-2026-07-27-cfb41f
  comparison: ''
  date: '2026-07-27'
  description: 'ElevenLabs — ElevenLabs updates — 2026-07-27: **WhatsApp branch and
    environment overrides**: [Outbound WhatsApp messages](https://elevenlabs.io/docs/api-reference/whats-app/outbound-message)
    and [outbound calls](https://elevenlabs.io/docs/api-reference/whats-app/outbound-call)
    now honor `branch_id` and `environment` passed in `conversation_initiation_client_data`.
    Overrides are validated before anything is sent — an unknown branch or environment
    is rejected with an error — and persist for the conversation, so a customer''s
    reply resumes on the requested [branch](https://elevenlabs.io/docs/eleven-agents/operate/versioning)
    and [environment](https://elevenlabs.io/docs/eleven-agents/integrate/environment-variables).
    See the [WhatsApp guide](https://elevenlabs.io/docs/eleven-agents/whatsapp) for
    examples.'
  evidence:
  - quote: '**WhatsApp branch and environment overrides**: [Outbound WhatsApp messages](https://elevenlabs.io/docs/api-reference/whats-app/outbound-message)
      and [outbound calls](https://elevenlabs.io/docs/api-reference/whats-app/outbound-call)
      now honor `branch_id` and `environment` passed in `conversation_initiation_client_data`.
      Overrides are validated before anything is sent — an unknown branch or environment
      is rejected with an error — and persist for the conversation, so a customer''s
      reply resumes on the requested [branch](https://elevenlabs.io/docs/eleven-agents/operate/versioning)
      and [environment](https://elevenlabs.io/docs/eleven-agents/integrate/environment-variables).
      See the [WhatsApp guide](https://elevenlabs.io/docs/eleven-agents/whatsapp)
      for examples.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '**Procedure APIs**: Added eight public, branch-scoped operations for managing
      [procedures](https://elevenlabs.io/docs/eleven-agents/customization/procedures).
      You can create, list, retrieve and remove procedures; create, retrieve or discard
      draft changes; and compile procedure drafts into an agent workflow. Procedure
      creation accepts `name`, `content`, `type` and `trigger`. An empty `trigger`
      creates a sub-procedure, while an omitted or `null` trigger is derived from
      the procedure content.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '**Knowledge base crawl jobs**: Added APIs to create, list, inspect and
      cancel crawl jobs. Create requests require `url` (string) and support crawl
      depth, page limits, URL patterns, sitemap URLs, folder placement, automatic
      synchronization and removal of unavailable documents.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '**Bulk knowledge base management**: Added [bulk dependency checks](https://elevenlabs.io/docs/api-reference/knowledge-base/dependent-agents-multiple)
      and [bulk deletion](https://elevenlabs.io/docs/api-reference/knowledge-base/bulk-delete)
      for 1–20 unique document or folder IDs. Dependency checks support pagination
      and `dependent_type`; deletion returns an independent success or failure for
      each ID. Setting `force: true` also removes dependencies and recursively deletes
      non-empty folders.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '**Batch call result export**: Added [Export batch call results](https://elevenlabs.io/docs/api-reference/batch-calling/export)
      to download recipients and conversation results from a terminal batch as CSV.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '**Conversation filters and analysis data**: [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
      and [Text search conversation messages](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search)
      add optional `visited_agent_ids` and `visited_agent_branch_ids` array filters,
      each limited to 50 values. List requests also accept `data_collection_ids` and
      `evaluation_criteria_ids` to include corresponding results in each conversation
      summary. Summaries add optional `data_collection_results`, `evaluation_criteria_results`
      and `tag_ids`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '**Referenced analysis configuration**: Agent platform settings add the
      optional, nullable `analysis_items` field, typed as `AgentAnalysisItems`, to
      attach evaluation and data-collection items by reference. A `null` value indicates
      that the agent still uses the legacy inline fields; an empty value indicates
      a migrated agent with no attached items.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '**Procedure dependency metadata**: Procedure references add `trigger`
      (string) and arrays for `referenced_tool_ids`, `referenced_kb_ids`, `referenced_procedure_ids`
      and `referenced_dynamic_variables`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '**WebRTC token response**: [Get WebRTC token](https://elevenlabs.io/docs/api-reference/conversations/get-webrtc-token)
      responses now require `conversation_id` (string) in addition to `token`. This
      is a breaking schema change for clients that validate or deserialize the response
      shape.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  - quote: '**Knowledge base RAG results**: `KnowledgeBaseRagToolResultModel` adds
      `chunks` (`KnowledgeBaseRagChunkModel[]`) for RAG-result-in-tool-result mode.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/27
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-07-27-2026-07-27-29809f38
  source_type: elevenlabs_changelog
  theme: __candidate__
  theme_matches:
  - matched_terms:
    - agents
    score: 50
    theme: agent-mode
  - matched_terms:
    - whatsapp
    score: 50
    theme: mobile-desktop
  theme_review_reason: ambiguous_match
  theme_suggestion: agent-mode-or-mobile-desktop
  title: ElevenAgents
  type: change
---

Pending theme review. Resolve via the theme vocabulary or review decisions.