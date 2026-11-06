---
card_id: elevenlabs-2026-05-13-6f8d80
date: '2026-05-13'
description: 'ElevenLabs · 2026-05-13 · Files and Data: [Update knowledge base document](https://elevenlabs.io/docs/api-reference/knowledge-base/update)
  - `PATCH…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2
    Files and Data changes in 0.2.2]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1084
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 05a53d56b62a2ef942cfe5d0960bf293ac3afc2d9249a518b54862a3de67c5d3
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-05-13-6f8d80
  comparison: ''
  date: '2026-05-13'
  description: 'ElevenLabs — ElevenLabs updates — 2026-05-13: [Update knowledge base
    document](https://elevenlabs.io/docs/api-reference/knowledge-base/update) - `PATCH
    /v1/convai/knowledge-base/{documentation_id}`'
  evidence:
  - quote: '[Update knowledge base document](https://elevenlabs.io/docs/api-reference/knowledge-base/update)
      - `PATCH /v1/convai/knowledge-base/{documentation_id}`'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Added JSON request body fields `name` (optional nullable string) and `content`
      (optional nullable string)
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create)
      - `POST /v1/convai/agents/create`'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Changed `enable_versioning` default from `false` to `true`
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: '[Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
      - `PATCH /v1/convai/agents/{agent_id}`'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Changed `enable_versioning_if_not_enabled` default from `false` to `true`
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: '[Update phone number](https://elevenlabs.io/docs/api-reference/phone-numbers/update)
      - `PATCH /v1/convai/phone-numbers/{phone_number_id}`'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Added `environment` and `branch_id` to phone number agent configuration
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: '`store_sip_messages` now defaults to `true`'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: '[Get widget](https://elevenlabs.io/docs/api-reference/widget/get) - `GET
      /v1/convai/agents/{agent_id}/widget`'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Added `file_input_config` for widget file uploads
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Added `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.4-mini-2026-03-17` and `gpt-5.4-nano-2026-03-17`
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: '`AuthorizationMethod` enum'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: '`ConversationInitiationSource` enum'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Added `twilio_sms`
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: '`AgentTopicResponseModel`'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Added optional nullable `parent_topic_id`, `x_2d` and `y_2d`
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: '`BackgroundMusicConfig` and `BackgroundMusicConfigWorkflowOverride`'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Added `source_type`, `source_id`, `volume` and `crossfade_loop`
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Added `BackgroundMusicPresetId` enum values `city`, `elevator1`, `elevator2`,
      `elevator3`, `elevator4`, `office1`, `office2`, `restaurant` and `typing`
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: '`AgentPlatformSettingsResponseModel`'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Added `alerting` with `Monitor` enum values `elevated_conversation_failure_rate`
      and `elevated_tool_failure_rate`
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: '`ProcedureCompilerMode` enum'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Removed `deterministic`
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-05-13-2026-05-13-1809b47f
  source_type: elevenlabs_changelog
  theme: file-data
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-07-21379-document-codex-git-commit-attribution-config-henzelmann-oai|♯21379
  Document Codex git commit attribution config @henzelmann-oai]]'
- "[[Changes/Open WebUI/2026-05-09-sanitized-spreadsheet-html-previews-spreadsheet-previews-now-sanitize-generated|\U0001F6E1️
  Sanitized spreadsheet HTML previews. Spreadsheet previews now sanitize…]]"
- '[[Changes/Dify/2026-05-12-document-indexing-skip-empty-documents-before-vector-embedding-and-validate-miss|Document
  indexing — skip empty documents before vector embedding and validate…]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-05-13-2026-05-13-1809b47f|elevenlabs-2026-05-13-2026-05-13-1809b47f]]'
source_type: elevenlabs_changelog
theme: file-data
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-05-13 · [[Themes/file-data|Files and Data]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/5/13) · from [[Releases/ElevenLabs/elevenlabs-2026-05-13-2026-05-13-1809b47f|ElevenLabs updates — 2026-05-13]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Update knowledge base document](https://elevenlabs.io/docs/api-reference/knowledge-base/update) - `PATCH /v1/convai/knowledge-base/{documentation_id}`
>
> Added JSON request body fields `name` (optional nullable string) and `content` (optional nullable string)
>
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create) - `POST /v1/convai/agents/create`
>
> Changed `enable_versioning` default from `false` to `true`
>
> [Update agent](https://elevenlabs.io/docs/api-reference/agents/update) - `PATCH /v1/convai/agents/{agent_id}`
>
> Changed `enable_versioning_if_not_enabled` default from `false` to `true`
>
> [Update phone number](https://elevenlabs.io/docs/api-reference/phone-numbers/update) - `PATCH /v1/convai/phone-numbers/{phone_number_id}`
>
> Added `environment` and `branch_id` to phone number agent configuration
>
> `store_sip_messages` now defaults to `true`
>
> [Get widget](https://elevenlabs.io/docs/api-reference/widget/get) - `GET /v1/convai/agents/{agent_id}/widget`
>
> Added `file_input_config` for widget file uploads
>
> Added `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.4-mini-2026-03-17` and `gpt-5.4-nano-2026-03-17`
>
> `AuthorizationMethod` enum
>
> `ConversationInitiationSource` enum
>
> Added `twilio_sms`
>
> `AgentTopicResponseModel`
>
> Added optional nullable `parent_topic_id`, `x_2d` and `y_2d`
>
> `BackgroundMusicConfig` and `BackgroundMusicConfigWorkflowOverride`
>
> Added `source_type`, `source_id`, `volume` and `crossfade_loop`
>
> Added `BackgroundMusicPresetId` enum values `city`, `elevator1`, `elevator2`, `elevator3`, `elevator4`, `office1`, `office2`, `restaurant` and `typing`
>
> `AgentPlatformSettingsResponseModel`
>
> Added `alerting` with `Monitor` enum values `elevated_conversation_failure_rate` and `elevated_tool_failure_rate`
>
> `ProcedureCompilerMode` enum
>
> Removed `deterministic`
>
> Source: https://elevenlabs.io/docs/changelog/2026/5/13
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-05-13-elevenagents|ElevenAgents]] · Developer Workflow
- [[Changes/ElevenLabs/2026-05-13-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-05-13-voice-design|Voice Design]] · Voice and Audio
- [[Changes/ElevenLabs/2026-05-13-voice-changer|Voice Changer]] · Voice and Audio
- [[Changes/ElevenLabs/2026-05-13-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-05-13-packages|Packages]] · Agent Mode
- [[Changes/ElevenLabs/2026-05-13-voice-design-b2b3bd|Voice Design]] · Voice and Audio
- [[Changes/ElevenLabs/2026-05-13-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-05-13-voice-changer-cdfc87|Voice Changer]] · Voice and Audio
- [[Changes/ElevenLabs/2026-05-13-workspaces|Workspaces]] · Editor Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-05-12 · Dify · [[Changes/Dify/2026-05-12-document-indexing-skip-empty-documents-before-vector-embedding-and-validate-miss|Document indexing — skip empty documents before vector embedding and validate…]]
- Later: 2026-05-14 · ChatGPT · [[Changes/ChatGPT/2026-05-14-file-library-is-expanding-to-free-and-go-users-including-to-users-in-the-europea-141640|File library is expanding to Free and Go users, including to users in the European…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-25 · Dify · [[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2 Files and Data changes in 0.2.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-05-13-6f8d80&body=Card%3A%20Changes%2FElevenLabs%2F2026-05-13-elevenagents-6f8d80.md%0ACard%20ID%3A%20elevenlabs-2026-05-13-6f8d80%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F5%2F13%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->