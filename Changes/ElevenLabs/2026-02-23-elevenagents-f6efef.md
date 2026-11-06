---
card_id: elevenlabs-2026-02-23-f6efef
date: '2026-02-23'
description: 'ElevenLabs · 2026-02-23 · Account and Access: **OAuth and advanced authentication
  for MCP servers**: MCP servers now support workspace auth connections…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1061
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: 6d46f45a61832e4b9067a9edbbcebfa6189ca73cf4f2e96f688a9cdb34fe8403
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-02-23-f6efef
  comparison: ''
  confidence: low
  date: '2026-02-23'
  description: 'ElevenLabs — ElevenLabs updates — 2026-02-23: **OAuth and advanced
    authentication for MCP servers**: MCP servers now support workspace auth connections,
    enabling OAuth2 Client Credentials, Basic Auth, Bearer Auth, JWT, and custom header
    authentication. Select an auth connection when creating or editing an MCP server
    to automatically handle token refresh and authentication headers. See the [MCP
    server documentation](https://elevenlabs.io/docs/eleven-agents/customization/tools/mcp)
    for more details.'
  evidence:
  - quote: '**OAuth and advanced authentication for MCP servers**: MCP servers now
      support workspace auth connections, enabling OAuth2 Client Credentials, Basic
      Auth, Bearer Auth, JWT, and custom header authentication. Select an auth connection
      when creating or editing an MCP server to automatically handle token refresh
      and authentication headers. See the [MCP server documentation](https://elevenlabs.io/docs/eleven-agents/customization/tools/mcp)
      for more details.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '**LLM information endpoint**: Added a new endpoint to list available LLMs
      with deprecation status, capabilities, and context limits. This enables clients
      to programmatically discover which models are available and which are being
      deprecated. See [List Available LLMs](https://elevenlabs.io/docs/api-reference/llm/list)
      for details.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '**Conversation history redaction**: Added support for redacting sensitive
      information from conversation transcripts, audio, and analysis before being
      stored. Configure specific entity types to redact (such as names, email addresses,
      etc.) using the new `conversation_history_redaction` setting in agent privacy
      configuration. See the [docs page](https://elevenlabs.io/docs/eleven-agents/customization/privacy/conversation-history-redaction)
      for more details.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '**Enhanced guardrails**: Introduced two new guardrail types for agents:'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '`focus`: Helps keep conversations on-topic'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '`prompt_injection`: Detects and prevents prompt injection attempts'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: 'Note: The `alignment` guardrail has been removed'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '**Conversation search endpoints**: Added two new endpoints for searching
      conversation messages:'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '[Text search](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search)
      - Full-text and fuzzy search over transcript messages'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '[Smart search](https://elevenlabs.io/docs/api-reference/conversations/messages/search)
      - Semantic search using embeddings'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '**File uploads in conversations**: Added endpoints to upload and manage
      files within conversations:'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '[Upload file](https://elevenlabs.io/docs/api-reference/conversations/upload-file)
      - Upload files to a conversation'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '[Delete file](https://elevenlabs.io/docs/api-reference/conversations/delete-file)
      - Remove uploaded files'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '**New embedding model**: Added support for `qwen3_embedding_4b` embedding
      model in knowledge base RAG indexing.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-02-23-2026-02-23-19067983
  source_type: elevenlabs_changelog
  theme: account-access
  theme_matches:
  - matched_terms:
    - authentication
    - oauth
    score: 100
    theme: account-access
  - matched_terms:
    - agents
    score: 50
    theme: agent-mode
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-13-added-claude-auth-login-claude-auth-status-and-claude-auth-logout-cli-subcommand|Added
  claude auth login, claude auth status, and claude auth logout CLI subcommands]]'
- "[[Changes/Open WebUI/2026-02-16-oauth-session-error-handling-corrupted-oauth-sessions-are-now-gracefully-handled|\U0001F510
  OAuth session error handling. Corrupted OAuth sessions are now gracefully…]]"
- '[[Changes/Claude Code/2026-02-19-improved-performance-by-caching-authentication-failures-for-http-and-sse-mcp-ser|Improved
  performance by caching authentication failures for HTTP and SSE MCP…]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-02-23-2026-02-23-19067983|elevenlabs-2026-02-23-2026-02-23-19067983]]'
source_type: elevenlabs_changelog
theme: account-access
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-02-23 · [[Themes/account-access|Account and Access]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/2/23) · from [[Releases/ElevenLabs/elevenlabs-2026-02-23-2026-02-23-19067983|ElevenLabs updates — 2026-02-23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **OAuth and advanced authentication for MCP servers**: MCP servers now support workspace auth connections, enabling OAuth2 Client Credentials, Basic Auth, Bearer Auth, JWT, and custom header authentication. Select an auth connection when creating or editing an MCP server to automatically handle token refresh and authentication headers. See the [MCP server documentation](https://elevenlabs.io/docs/eleven-agents/customization/tools/mcp) for more details.
>
> **LLM information endpoint**: Added a new endpoint to list available LLMs with deprecation status, capabilities, and context limits. This enables clients to programmatically discover which models are available and which are being deprecated. See [List Available LLMs](https://elevenlabs.io/docs/api-reference/llm/list) for details.
>
> **Conversation history redaction**: Added support for redacting sensitive information from conversation transcripts, audio, and analysis before being stored. Configure specific entity types to redact (such as names, email addresses, etc.) using the new `conversation_history_redaction` setting in agent privacy configuration. See the [docs page](https://elevenlabs.io/docs/eleven-agents/customization/privacy/conversation-history-redaction) for more details.
>
> **Enhanced guardrails**: Introduced two new guardrail types for agents:
>
> `focus`: Helps keep conversations on-topic
>
> `prompt_injection`: Detects and prevents prompt injection attempts
>
> Note: The `alignment` guardrail has been removed
>
> **Conversation search endpoints**: Added two new endpoints for searching conversation messages:
>
> [Text search](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search) - Full-text and fuzzy search over transcript messages
>
> [Smart search](https://elevenlabs.io/docs/api-reference/conversations/messages/search) - Semantic search using embeddings
>
> **File uploads in conversations**: Added endpoints to upload and manage files within conversations:
>
> [Upload file](https://elevenlabs.io/docs/api-reference/conversations/upload-file) - Upload files to a conversation
>
> [Delete file](https://elevenlabs.io/docs/api-reference/conversations/delete-file) - Remove uploaded files
>
> **New embedding model**: Added support for `qwen3_embedding_4b` embedding model in knowledge base RAG indexing.
>
> Source: https://elevenlabs.io/docs/changelog/2026/2/23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-02-23-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-02-23-text-to-voice|Text to Voice]] · Voice and Audio
- [[Changes/ElevenLabs/2026-02-23-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-02-23-workspaces|Workspaces]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-02-23-python-sdk|Python SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-02-23-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-02-23-music|Music]] · Collaboration
- [[Changes/ElevenLabs/2026-02-23-removed-endpoints|Removed Endpoints]] · Voice and Audio
- [[Changes/ElevenLabs/2026-02-23-voices|Voices]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-02-19 · Claude Code · [[Changes/Claude Code/2026-02-19-improved-performance-by-caching-authentication-failures-for-http-and-sse-mcp-ser|Improved performance by caching authentication failures for HTTP and SSE MCP…]]
- Later: 2026-02-23 · Open WebUI · [[Changes/Open WebUI/2026-02-23-3-account-and-access-changes-in-v0-8-4|3 Account and Access changes in v0.8.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-02-23-f6efef&body=Card%3A%20Changes%2FElevenLabs%2F2026-02-23-elevenagents-f6efef.md%0ACard%20ID%3A%20elevenlabs-2026-02-23-f6efef%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F2%2F23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->