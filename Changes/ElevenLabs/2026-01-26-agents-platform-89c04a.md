---
card_id: elevenlabs-2026-01-26-89c04a
date: '2026-01-26'
description: 'ElevenLabs · 2026-01-26 · Agent Mode: **Agent branching and deployments**:
  Added a complete version control system for agents, enabling teams to create…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 935
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: d644c6ab7b46a047c34d6b2db21527f2f291172f09cb60243f5414fd7c308d2e
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-01-26-89c04a
  comparison: ''
  confidence: low
  date: '2026-01-26'
  description: 'ElevenLabs — ElevenLabs updates — 2026-01-26: **Agent branching and
    deployments**: Added a complete version control system for agents, enabling teams
    to create branches, iterate on agent configurations in isolation, and merge changes
    when ready. New endpoints include `POST /v1/convai/agents/{agent_id}/branches`
    for creating branches, `POST /v1/convai/agents/{agent_id}/branches/{source_branch_id}/merge`
    for merging, and `POST /v1/convai/agents/{agent_id}/deployments` for creating
    deployments. Drafts can also be created and deleted via the new drafts endpoints.
    See the [Branches](https://elevenlabs.io/docs/api-reference/agents/branches/list)
    and [Deployments](https://elevenlabs.io/docs/api-reference/agents/deployments/create)
    documentation for details.'
  evidence:
  - quote: '**Agent branching and deployments**: Added a complete version control
      system for agents, enabling teams to create branches, iterate on agent configurations
      in isolation, and merge changes when ready. New endpoints include `POST /v1/convai/agents/{agent_id}/branches`
      for creating branches, `POST /v1/convai/agents/{agent_id}/branches/{source_branch_id}/merge`
      for merging, and `POST /v1/convai/agents/{agent_id}/deployments` for creating
      deployments. Drafts can also be created and deleted via the new drafts endpoints.
      See the [Branches](https://elevenlabs.io/docs/api-reference/agents/branches/list)
      and [Deployments](https://elevenlabs.io/docs/api-reference/agents/deployments/create)
      documentation for details.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: '**WhatsApp account management**: Added `PATCH` and `DELETE` endpoints
      for WhatsApp Business accounts, allowing you to update and remove connected
      WhatsApp accounts from agents.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: '**Conversation agent name**: The [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)
      endpoint now returns `agent_name` in the response for easier identification
      of which agent handled a conversation.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: '**Error type tracking**: Added `error_type` field to conversation event
      models for improved debugging and error categorization.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2026-01-26-2026-01-26-f7dcd336
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-01-26-agents-platform|Agents Platform]]'
- '[[Changes/ElevenLabs/2026-01-26-javascript-sdk|JavaScript SDK]]'
- '[[Changes/ElevenLabs/2026-01-26-new-endpoints|New Endpoints]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-01-26-2026-01-26-f7dcd336|elevenlabs-2026-01-26-2026-01-26-f7dcd336]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2026-01-26 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/1/26) · from [[Releases/ElevenLabs/elevenlabs-2026-01-26-2026-01-26-f7dcd336|ElevenLabs updates — 2026-01-26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Agent branching and deployments**: Added a complete version control system for agents, enabling teams to create branches, iterate on agent configurations in isolation, and merge changes when ready. New endpoints include `POST /v1/convai/agents/{agent_id}/branches` for creating branches, `POST /v1/convai/agents/{agent_id}/branches/{source_branch_id}/merge` for merging, and `POST /v1/convai/agents/{agent_id}/deployments` for creating deployments. Drafts can also be created and deleted via the new drafts endpoints. See the [Branches](https://elevenlabs.io/docs/api-reference/agents/branches/list) and [Deployments](https://elevenlabs.io/docs/api-reference/agents/deployments/create) documentation for details.
>
> **WhatsApp account management**: Added `PATCH` and `DELETE` endpoints for WhatsApp Business accounts, allowing you to update and remove connected WhatsApp accounts from agents.
>
> **Conversation agent name**: The [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get) endpoint now returns `agent_name` in the response for easier identification of which agent handled a conversation.
>
> **Error type tracking**: Added `error_type` field to conversation event models for improved debugging and error categorization.
>
> Source: https://elevenlabs.io/docs/changelog/2026/1/26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-01-26-python-sdk|Python SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-01-26-workspaces|Workspaces]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-01-26-agents-platform|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2026-01-26-javascript-sdk|JavaScript SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-01-26-new-endpoints|New Endpoints]] · Agent Mode
- [[Changes/ElevenLabs/2026-01-26-knowledge-base|Knowledge Base]] · Files and Data
- [[Changes/ElevenLabs/2026-01-26-music|Music]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-26-elevencreative-studio|ElevenCreative Studio]] · Model Support
- [[Changes/ElevenLabs/2026-01-26-new-schemas|New Schemas]] · Agent Mode
- [[Changes/ElevenLabs/2026-01-26-sdk-releases|SDK Releases]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-01-25 · OpenCode · [[Changes/OpenCode/2026-01-25-2-agent-mode-changes-in-v1-1-35|2 Agent Mode changes in v1.1.35]]
- Later: 2026-01-26 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-01-26-load-local-shell-configuration-in-agent-sessions|Load local shell configuration in agent sessions]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-01-26-89c04a&body=Card%3A%20Changes%2FElevenLabs%2F2026-01-26-agents-platform-89c04a.md%0ACard%20ID%3A%20elevenlabs-2026-01-26-89c04a%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F1%2F26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->