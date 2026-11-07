---
card_id: elevenlabs-2026-09-28-255ca5
date: '2026-09-28'
description: 'ElevenLabs · 2026-09-28 · Agent Mode: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
  [Get…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1180
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 812ad5ba668c1f62c595ee838756ade764ff83b3361242afcc3b6f2af53efe73
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-09-28-255ca5
  comparison: ''
  confidence: low
  date: '2026-09-28'
  description: 'ElevenLabs — ElevenLabs updates — 2026-09-28: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
    [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
  evidence:
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update
      agent](https://elevenlabs.io/docs/api-reference/agents/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: Added `gpt-6-sol`, `gpt-6-luna`, `glm-52`, `deepseek-v41-flash`, `claude-opus-5`
      and `claude-opus-5-5` to the `LLM` enum.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: Alerting monitors add optional nullable `enabled` (boolean) to control
      whether a monitor can send notifications.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: '[List conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
      and [Text search](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search)'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: '`data_collection_params` and `dynamic_variable_params` add `neq` and `in`
      operators. Values for `in` use a pipe delimiter.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: '`evaluation_params` accepts `success`, `failure` or `unknown` as the result
      value.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: '[Smart search](https://elevenlabs.io/docs/api-reference/conversations/messages/search)
      - `GET /v1/convai/conversations/messages/smart-search`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: Added optional nullable `branch_id` (string).
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: '[List test invocations](https://elevenlabs.io/docs/api-reference/tests/test-invocations/list)
      - `GET /v1/convai/test-invocations`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: Test invocation summaries add optional nullable `credits_used` (integer)
      and `total_price` (number).
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: '[Get test invocation](https://elevenlabs.io/docs/api-reference/tests/test-invocations/get)
      - `GET /v1/convai/test-invocations/{test_invocation_id}`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: Individual test runs add optional nullable `credits_used` (integer) and
      `charging` (`ConversationChargingCommonModel`).
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: '[Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation)
      and [Simulate conversation stream](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation-stream)'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: Changed the optional `new_turns_limit` default from `10,000` to `100` and
      set its maximum to `100`.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: '[Create crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/create-crawl-job)
      and [Get crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/get-crawl-job)'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: 'Added optional `auto_discover` (boolean, default `false`) to follow links
      and add newly discovered pages during auto-sync. This requires `enable_auto_sync:
      true`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: '[Refresh knowledge base document](https://elevenlabs.io/docs/api-reference/knowledge-base/refresh)
      - `POST /v1/convai/knowledge-base/{documentation_id}/refresh`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: '`AutoSyncInfo` adds optional `auto_discover` (boolean, default `false`)
      to indicate whether refreshes crawl and add newly discovered pages.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: '[List MCP server tools](https://elevenlabs.io/docs/api-reference/mcp/list-tools)
      - `GET /v1/convai/mcp-servers/{mcp_server_id}/tools`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: Responses add optional `tool_approval_statuses` (array). Each item contains
      required `tool_id` (string) and `state` (`up_to_date`, `needs_review` or `not_approved`),
      with optional approval policy and approved-definition fields.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-09-28-2026-09-28-7fc35a6b
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/OpenHands/2026-09-25-docs-correct-outdated-cloud-proxy-rule-2-in-agents-md-by-juanmichelini-in-https|docs:
  correct outdated cloud-proxy Rule 2 in AGENTS.md]]'
- '[[Changes/Claude Code/2026-09-28-added-a-yes-but-ask-again-next-time-answer-to-auto-mode-s-prompt-before-a-read-o|Added
  a "Yes, but ask again next time" answer to auto mode''s prompt before a read…]]'
- '[[Changes/Codex CLI/2026-09-28-11-agent-mode-changes-in-rust-v0-158-0|11 Agent
  Mode changes in rust-v0.158.0]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-09-28-2026-09-28-7fc35a6b|elevenlabs-2026-09-28-2026-09-28-7fc35a6b]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-09-28 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/9/28) · from [[Releases/ElevenLabs/elevenlabs-2026-09-28-2026-09-28-7fc35a6b|ElevenLabs updates — 2026-09-28]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
>
> Added `gpt-6-sol`, `gpt-6-luna`, `glm-52`, `deepseek-v41-flash`, `claude-opus-5` and `claude-opus-5-5` to the `LLM` enum.
>
> Alerting monitors add optional nullable `enabled` (boolean) to control whether a monitor can send notifications.
>
> [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list) and [Text search](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search)
>
> `data_collection_params` and `dynamic_variable_params` add `neq` and `in` operators. Values for `in` use a pipe delimiter.
>
> `evaluation_params` accepts `success`, `failure` or `unknown` as the result value.
>
> [Smart search](https://elevenlabs.io/docs/api-reference/conversations/messages/search) - `GET /v1/convai/conversations/messages/smart-search`
>
> Added optional nullable `branch_id` (string).
>
> [List test invocations](https://elevenlabs.io/docs/api-reference/tests/test-invocations/list) - `GET /v1/convai/test-invocations`
>
> Test invocation summaries add optional nullable `credits_used` (integer) and `total_price` (number).
>
> [Get test invocation](https://elevenlabs.io/docs/api-reference/tests/test-invocations/get) - `GET /v1/convai/test-invocations/{test_invocation_id}`
>
> Individual test runs add optional nullable `credits_used` (integer) and `charging` (`ConversationChargingCommonModel`).
>
> [Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation) and [Simulate conversation stream](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation-stream)
>
> Changed the optional `new_turns_limit` default from `10,000` to `100` and set its maximum to `100`.
>
> [Create crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/create-crawl-job) and [Get crawl job](https://elevenlabs.io/docs/api-reference/knowledge-base/get-crawl-job)
>
> Added optional `auto_discover` (boolean, default `false`) to follow links and add newly discovered pages during auto-sync. This requires `enable_auto_sync: true`.
>
> [Refresh knowledge base document](https://elevenlabs.io/docs/api-reference/knowledge-base/refresh) - `POST /v1/convai/knowledge-base/{documentation_id}/refresh`
>
> `AutoSyncInfo` adds optional `auto_discover` (boolean, default `false`) to indicate whether refreshes crawl and add newly discovered pages.
>
> [List MCP server tools](https://elevenlabs.io/docs/api-reference/mcp/list-tools) - `GET /v1/convai/mcp-servers/{mcp_server_id}/tools`
>
> Responses add optional `tool_approval_statuses` (array). Each item contains required `tool_id` (string) and `state` (`up_to_date`, `needs_review` or `not_approved`), with optional approval policy and approved-definition fields.
>
> Source: https://elevenlabs.io/docs/changelog/2026/9/28
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-09-28-python-sdk|Python SDK]] · Pricing Model
- [[Changes/ElevenLabs/2026-09-28-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-09-28-elevenagents-4d99c8|ElevenAgents]] · Model Support
- [[Changes/ElevenLabs/2026-09-28-models|Models]] · Model Support
- [[Changes/ElevenLabs/2026-09-28-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-28-javascript-sdk|JavaScript SDK]] · Pricing Model
- [[Changes/ElevenLabs/2026-09-28-flows|Flows]] · Image Generation
- [[Changes/ElevenLabs/2026-09-28-elevenlabs-cli|ElevenLabs CLI]] · Account and Access
- [[Changes/ElevenLabs/2026-09-28-voice-design|Voice Design]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-28-eleven-v4-and-eleven-v4-turbo|Eleven v4 and Eleven v4 Turbo]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-28-speech-to-text-d0afb0|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-28-flows-ffc074|Flows]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-28 · Codex CLI · [[Changes/Codex CLI/2026-09-28-11-agent-mode-changes-in-rust-v0-158-0|11 Agent Mode changes in rust-v0.158.0]]
- Later: 2026-09-28 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-28-queue-exit-commands-while-an-agent-response-is-still-running|Queue exit commands while an agent response is still running]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-09-28-255ca5&body=Card%3A%20Changes%2FElevenLabs%2F2026-09-28-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-09-28-255ca5%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F9%2F28%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->