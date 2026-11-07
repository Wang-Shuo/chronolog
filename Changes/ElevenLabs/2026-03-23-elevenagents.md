---
card_id: elevenlabs-2026-03-23-8f830e
date: '2026-03-23'
description: 'ElevenLabs · 2026-03-23 · Agent Mode: **Environment Variables API**:
  New [environment…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 991
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: 914640a2bed7cc9893d236199043ab02ab943c05854fcfce65cb4bda7b673281
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-03-23-8f830e
  comparison: ''
  confidence: low
  date: '2026-03-23'
  description: 'ElevenLabs — ElevenLabs updates — 2026-03-23: **Environment Variables
    API**: New [environment variables](https://elevenlabs.io/docs/eleven-agents/integrate/environment-variables)
    endpoints for managing workspace-level configuration that agents can reference
    at runtime via `{{system_env__}}` templating. Supports string, secret, and auth-connection
    variable types with per-environment value overrides. Endpoints include [create](https://elevenlabs.io/docs/api-reference/environment-variables/create),
    [list](https://elevenlabs.io/docs/api-reference/environment-variables/list), [get](https://elevenlabs.io/docs/api-reference/environment-variables/get),
    and [update](https://elevenlabs.io/docs/api-reference/environment-variables/update).'
  evidence:
  - quote: '**Environment Variables API**: New [environment variables](https://elevenlabs.io/docs/eleven-agents/integrate/environment-variables)
      endpoints for managing workspace-level configuration that agents can reference
      at runtime via `{{system_env__}}` templating. Supports string, secret, and auth-connection
      variable types with per-environment value overrides. Endpoints include [create](https://elevenlabs.io/docs/api-reference/environment-variables/create),
      [list](https://elevenlabs.io/docs/api-reference/environment-variables/list),
      [get](https://elevenlabs.io/docs/api-reference/environment-variables/get), and
      [update](https://elevenlabs.io/docs/api-reference/environment-variables/update).'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '**Auth Connections management**: New workspace-level auth connections
      API for managing authentication credentials used by agent tools and integrations.
      Supports multiple auth methods including OAuth2 client credentials, JWT, basic
      auth, bearer tokens, custom headers, and integration-managed OAuth2 authorization
      code flows. Endpoints include create, list, and delete operations.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '**Knowledge Base URL refresh**: New [refresh](https://elevenlabs.io/docs/api-reference/knowledge-base/refresh)
      endpoint (`POST /v1/convai/knowledge-base/{documentation_id}/refresh`) to re-fetch
      and update content for URL-sourced knowledge base documents. Knowledge base
      documents also now support auto-sync configuration with `enable_auto_sync`,
      `auto_remove`, and `auto_sync_info` fields.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '**Guardrail retry with feedback**: Custom and content guardrails now support
      configurable [trigger actions](https://elevenlabs.io/docs/eleven-agents/best-practices/guardrails)
      with `EndCallTriggerAction` and `RetryTriggerAction` options. When set to retry,
      the agent re-generates its response with injected system feedback up to 3 attempts.
      Available placeholders include `{{trigger_reason}}` and `{{agent_message}}`
      for contextual retry guidance.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '**Conversation History system variable**: Added a new `system__conversation_history`
      dynamic variable that provides a lazily-evaluated, JSON-serialized conversation
      history at runtime. This is useful for passing full conversation context to
      tools, webhooks, or sub-agent handoffs.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '**Webhook tool content type**: Server tools now support a configurable
      [content type](https://elevenlabs.io/docs/eleven-agents/customization/tools/server-tools)
      for webhook body parameters, allowing you to choose between `application/json`
      and `application/x-www-form-urlencoded` formats. The URL-encoded format is useful
      for integrating with legacy systems, OAuth token endpoints, and payment processors.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '**WhatsApp outbound messages**: Updated the WhatsApp integration with
      a new [outbound message dialog](https://elevenlabs.io/docs/eleven-agents/whatsapp)
      in the dashboard, enabling agents to send outbound messages in addition to calls
      through the WhatsApp channel.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '**Agent and resource listing filters**: The [list agents](https://elevenlabs.io/docs/api-reference/agents/list),
      [list knowledge base documents](https://elevenlabs.io/docs/api-reference/knowledge-base/list),
      and [list tools](https://elevenlabs.io/docs/api-reference/tools/list) endpoints
      now support a `created_by_user_id` query parameter (use `@me` for the current
      user). The previous `show_only_owned_agents` and `show_only_owned_documents`
      parameters are deprecated.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  - quote: '**Workflow conditional expressions**: Added a new `conditional_operator`
      AST node to the workflow expression schema, enabling branching logic within
      agent workflow definitions.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/23
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-03-23-2026-03-23-c7dac693
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/HeyGen/2026-03-19-video-agent|Video Agent]]'
- '[[Changes/Replit/2026-03-20-empty-project-creation|Empty project creation]]'
- '[[Changes/OpenCode/2026-03-22-ui-ux-improvements-agent-skill-ordering-more-consistent-ai-responses-with-improv|UI/UX
  Improvements Agent & Skill Ordering]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-03-23-2026-03-23-c7dac693|elevenlabs-2026-03-23-2026-03-23-c7dac693]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-03-23 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/3/23) · from [[Releases/ElevenLabs/elevenlabs-2026-03-23-2026-03-23-c7dac693|ElevenLabs updates — 2026-03-23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Environment Variables API**: New [environment variables](https://elevenlabs.io/docs/eleven-agents/integrate/environment-variables) endpoints for managing workspace-level configuration that agents can reference at runtime via `{{system_env__}}` templating. Supports string, secret, and auth-connection variable types with per-environment value overrides. Endpoints include [create](https://elevenlabs.io/docs/api-reference/environment-variables/create), [list](https://elevenlabs.io/docs/api-reference/environment-variables/list), [get](https://elevenlabs.io/docs/api-reference/environment-variables/get), and [update](https://elevenlabs.io/docs/api-reference/environment-variables/update).
>
> **Auth Connections management**: New workspace-level auth connections API for managing authentication credentials used by agent tools and integrations. Supports multiple auth methods including OAuth2 client credentials, JWT, basic auth, bearer tokens, custom headers, and integration-managed OAuth2 authorization code flows. Endpoints include create, list, and delete operations.
>
> **Knowledge Base URL refresh**: New [refresh](https://elevenlabs.io/docs/api-reference/knowledge-base/refresh) endpoint (`POST /v1/convai/knowledge-base/{documentation_id}/refresh`) to re-fetch and update content for URL-sourced knowledge base documents. Knowledge base documents also now support auto-sync configuration with `enable_auto_sync`, `auto_remove`, and `auto_sync_info` fields.
>
> **Guardrail retry with feedback**: Custom and content guardrails now support configurable [trigger actions](https://elevenlabs.io/docs/eleven-agents/best-practices/guardrails) with `EndCallTriggerAction` and `RetryTriggerAction` options. When set to retry, the agent re-generates its response with injected system feedback up to 3 attempts. Available placeholders include `{{trigger_reason}}` and `{{agent_message}}` for contextual retry guidance.
>
> **Conversation History system variable**: Added a new `system__conversation_history` dynamic variable that provides a lazily-evaluated, JSON-serialized conversation history at runtime. This is useful for passing full conversation context to tools, webhooks, or sub-agent handoffs.
>
> **Webhook tool content type**: Server tools now support a configurable [content type](https://elevenlabs.io/docs/eleven-agents/customization/tools/server-tools) for webhook body parameters, allowing you to choose between `application/json` and `application/x-www-form-urlencoded` formats. The URL-encoded format is useful for integrating with legacy systems, OAuth token endpoints, and payment processors.
>
> **WhatsApp outbound messages**: Updated the WhatsApp integration with a new [outbound message dialog](https://elevenlabs.io/docs/eleven-agents/whatsapp) in the dashboard, enabling agents to send outbound messages in addition to calls through the WhatsApp channel.
>
> **Agent and resource listing filters**: The [list agents](https://elevenlabs.io/docs/api-reference/agents/list), [list knowledge base documents](https://elevenlabs.io/docs/api-reference/knowledge-base/list), and [list tools](https://elevenlabs.io/docs/api-reference/tools/list) endpoints now support a `created_by_user_id` query parameter (use `@me` for the current user). The previous `show_only_owned_agents` and `show_only_owned_documents` parameters are deprecated.
>
> **Workflow conditional expressions**: Added a new `conditional_operator` AST node to the workflow expression schema, enabling branching logic within agent workflow definitions.
>
> Source: https://elevenlabs.io/docs/changelog/2026/3/23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-03-23-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-03-23-packages|Packages]] · Multimodal Input
- [[Changes/ElevenLabs/2026-03-23-ios-sdk|iOS SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-03-23-workspaces|Workspaces]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-23-new-schemas|New Schemas]] · Model Support
- [[Changes/ElevenLabs/2026-03-23-packages-v1-0-0-release-candidate|Packages v1.0.0 Release Candidate]] · Reliability and Performance
- [[Changes/ElevenLabs/2026-03-23-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-23-javascript-sdk|JavaScript SDK]] · Multimodal Input
- [[Changes/ElevenLabs/2026-03-23-python-sdk|Python SDK]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-03-22 · OpenCode · [[Changes/OpenCode/2026-03-22-ui-ux-improvements-agent-skill-ordering-more-consistent-ai-responses-with-improv|UI/UX Improvements Agent & Skill Ordering]]
- Later: 2026-03-23 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-23-2-agent-mode-changes-in-v1-0-11|2 Agent Mode changes in v1.0.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-03-23-8f830e&body=Card%3A%20Changes%2FElevenLabs%2F2026-03-23-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-03-23-8f830e%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F3%2F23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->