---
card_id: elevenlabs-2026-10-05-4c0709
date: '2026-10-05'
description: 'ElevenLabs · 2026-10-05 · Agent Mode: [Create a merge proposal](https://elevenlabs.io/docs/api-reference/agents/merge-proposals/create)
  - `POST…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1187
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 8191bd995b7d74eb582b4e88f8e28b36a48e7aab513e5aa34aabe93248568d67
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-10-05-4c0709
  comparison: ''
  confidence: low
  date: '2026-10-05'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-05: [Create a merge proposal](https://elevenlabs.io/docs/api-reference/agents/merge-proposals/create)
    - `POST /v1/convai/agents/{agent_id}/merge-proposals` - Create a proposal with
    required `source_branch_id`, `target_branch_id` and `title` fields, plus an optional
    description, reviewer IDs and triage ticket ID.'
  evidence:
  - quote: '[Create a merge proposal](https://elevenlabs.io/docs/api-reference/agents/merge-proposals/create)
      - `POST /v1/convai/agents/{agent_id}/merge-proposals` - Create a proposal with
      required `source_branch_id`, `target_branch_id` and `title` fields, plus an
      optional description, reviewer IDs and triage ticket ID.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '[List merge proposals](https://elevenlabs.io/docs/api-reference/agents/merge-proposals/list)
      - `GET /v1/convai/agents/{agent_id}/merge-proposals` - List proposals with status,
      source branch, target branch and text filters, plus cursor pagination.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '[Get a merge proposal](https://elevenlabs.io/docs/api-reference/agents/merge-proposals/get)
      - `GET /v1/convai/agents/{agent_id}/merge-proposals/{merge_proposal_id}` - Retrieve
      a proposal and its review, comment and outcome details.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '[Update a merge proposal](https://elevenlabs.io/docs/api-reference/agents/merge-proposals/update)
      - `PATCH /v1/convai/agents/{agent_id}/merge-proposals/{merge_proposal_id}` -
      Update its title, description or requested reviewers, or close it without merging.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '[Review a merge proposal](https://elevenlabs.io/docs/api-reference/agents/merge-proposals/submit-review)
      - `POST /v1/convai/agents/{agent_id}/merge-proposals/{merge_proposal_id}/reviews`
      - Submit an `approved` or `changes_requested` decision with an optional comment.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '[Comment on a merge proposal](https://elevenlabs.io/docs/api-reference/agents/merge-proposals/add-comment)
      - `POST /v1/convai/agents/{agent_id}/merge-proposals/{merge_proposal_id}/comments`
      - Add a Markdown comment of up to 4,096 characters.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '[Merge a merge proposal](https://elevenlabs.io/docs/api-reference/agents/merge-proposals/merge)
      - `POST /v1/convai/agents/{agent_id}/merge-proposals/{merge_proposal_id}/merge`
      - Merge the source branch and optionally control forced conflict resolution
      and source branch archival.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '[List agent deployments](https://elevenlabs.io/docs/api-reference/agents/deployments/list)
      - `GET /v1/convai/agents/{agent_id}/deployments` - List current and historical
      branch traffic splits with page-based pagination.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '[Cancel a test invocation](https://elevenlabs.io/docs/api-reference/tests/test-invocations/cancel)
      - `POST /v1/convai/test-invocations/{test_invocation_id}/cancel` - Cancel a
      running test invocation.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-10-05-2026-10-05-4039c076
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-url-to-set-up-the-managed-agents-pattern|Added
  /claude-api managed-agents-onboard url to set up the Managed Agents…]]'
- '[[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-quickstart-name-to-build-a-console-quick|Added
  /claude-api managed-agents-onboard quickstart-name to build a Console…]]'
- '[[Changes/Claude Code/2026-10-05-4-agent-mode-changes-in-v2-1-290|4 Agent Mode
  changes in v2.1.290]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-05-2026-10-05-4039c076|elevenlabs-2026-10-05-2026-10-05-4039c076]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-10-05 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/10/5) · from [[Releases/ElevenLabs/elevenlabs-2026-10-05-2026-10-05-4039c076|ElevenLabs updates — 2026-10-05]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Create a merge proposal](https://elevenlabs.io/docs/api-reference/agents/merge-proposals/create) - `POST /v1/convai/agents/{agent_id}/merge-proposals` - Create a proposal with required `source_branch_id`, `target_branch_id` and `title` fields, plus an optional description, reviewer IDs and triage ticket ID.
>
> [List merge proposals](https://elevenlabs.io/docs/api-reference/agents/merge-proposals/list) - `GET /v1/convai/agents/{agent_id}/merge-proposals` - List proposals with status, source branch, target branch and text filters, plus cursor pagination.
>
> [Get a merge proposal](https://elevenlabs.io/docs/api-reference/agents/merge-proposals/get) - `GET /v1/convai/agents/{agent_id}/merge-proposals/{merge_proposal_id}` - Retrieve a proposal and its review, comment and outcome details.
>
> [Update a merge proposal](https://elevenlabs.io/docs/api-reference/agents/merge-proposals/update) - `PATCH /v1/convai/agents/{agent_id}/merge-proposals/{merge_proposal_id}` - Update its title, description or requested reviewers, or close it without merging.
>
> [Review a merge proposal](https://elevenlabs.io/docs/api-reference/agents/merge-proposals/submit-review) - `POST /v1/convai/agents/{agent_id}/merge-proposals/{merge_proposal_id}/reviews` - Submit an `approved` or `changes_requested` decision with an optional comment.
>
> [Comment on a merge proposal](https://elevenlabs.io/docs/api-reference/agents/merge-proposals/add-comment) - `POST /v1/convai/agents/{agent_id}/merge-proposals/{merge_proposal_id}/comments` - Add a Markdown comment of up to 4,096 characters.
>
> [Merge a merge proposal](https://elevenlabs.io/docs/api-reference/agents/merge-proposals/merge) - `POST /v1/convai/agents/{agent_id}/merge-proposals/{merge_proposal_id}/merge` - Merge the source branch and optionally control forced conflict resolution and source branch archival.
>
> [List agent deployments](https://elevenlabs.io/docs/api-reference/agents/deployments/list) - `GET /v1/convai/agents/{agent_id}/deployments` - List current and historical branch traffic splits with page-based pagination.
>
> [Cancel a test invocation](https://elevenlabs.io/docs/api-reference/tests/test-invocations/cancel) - `POST /v1/convai/test-invocations/{test_invocation_id}/cancel` - Cancel a running test invocation.
>
> Source: https://elevenlabs.io/docs/changelog/2026/10/5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-05-swift-sdk|Swift SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-05-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-05-elevenagents-5bf5b0|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-05-python-sdk|Python SDK]] · Model Support
- [[Changes/ElevenLabs/2026-10-05-javascript-sdk|JavaScript SDK]] · Model Support
- [[Changes/ElevenLabs/2026-10-05-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-05-elevenagents-ceeb34|ElevenAgents]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-05 · Claude Code · [[Changes/Claude Code/2026-10-05-4-agent-mode-changes-in-v2-1-290|4 Agent Mode changes in v2.1.290]]
- Later: 2026-10-05 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-05-5-agent-mode-changes-in-v1-0-92|5 Agent Mode changes in v1.0.92]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-05-4c0709&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-05-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-10-05-4c0709%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->