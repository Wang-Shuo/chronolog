---
card_id: elevenlabs-2026-10-26-b99df3
date: '2026-10-26'
description: 'ElevenLabs · 2026-10-26 · Agent Mode: 9 changes in ElevenLabs updates
  — 2026-10-26 — **Procedures analytics**: The **Procedures** tab on the agent analytics…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1208
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a8da1c18589286d0e63041da99f8469eb5a0ed722f42e300a1cce766f62ee640
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-10-26-b99df3
  comparison: ''
  date: '2026-10-26'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-26: 9 Agent Mode changes'
  evidence:
  - quote: '**Procedures analytics**: The **Procedures** tab on the agent analytics
      dashboard is available to every workspace. Its **Procedure invocations** chart
      shows how often each [procedure](https://elevenlabs.io/docs/eleven-agents/customization/procedures)
      runs over time, grouped by procedure or by agent, and its tooltip shows whether
      a procedure is structured or free-form.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Start procedures at conversation start**: Conversation initiation client
      data accepts `start_procedure_ids`, up to five free-form procedures that start
      when the conversation starts. The agent must have `enable_procedure_ids_from_client`
      enabled; structured procedures and unknown IDs fail the conversation start.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Structured procedure steps**: Structured procedures can use the `end_procedure`
      system tool as a step, and the **End** step is relabeled **End conversation**.
      Sub-procedure and end steps now compile to system tool nodes, so agents start
      and end the intended procedure more reliably.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Slack thread replies**: The Slack Channel Message trigger adds a **Respond
      to** setting (`response_mode`), so an agent can keep replying in a thread after
      a single mention. Mentioning the agent with only `stop`, `mute` or `quiet` silences
      it in that thread until it is mentioned again, and events that Slack delivers
      twice get one reply.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Branch descriptions**: Branch descriptions can be edited from the branches
      table with [Update branch](https://elevenlabs.io/docs/api-reference/agents/branches/update)
      (`description`, up to 4,096 characters) and appear in the version tooltip and
      version graph.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Agent duplication keeps traffic splits**: Duplicating an agent copies
      its live traffic split across the copied branches. The resulting deployment
      records `duplicate` as its deployment source.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Delete environment variables**: `DELETE /v1/convai/environment-variables/{env_var_id}`
      deletes an [environment variable](https://elevenlabs.io/docs/eleven-agents/integrate/environment-variables).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Issues**: Triage is renamed **Issues** in the agents dashboard, and
      triage tickets are now called issues. Every QA comment and `flag_issue_for_review`
      call opens its own issue, and an issue can be reopened while the conversation
      has another open issue. The API endpoints keep their `triage-tickets` paths.
      See [Triage](https://elevenlabs.io/docs/eleven-agents/operate/triage).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Observability**: OpenTelemetry post-call webhook agent turn spans add
      `elevenlabs.rag.chunks` and `elevenlabs.rag.used_chunk_ids`, matching the JSON
      [post-call webhook](https://elevenlabs.io/docs/eleven-agents/workflows/post-call-webhooks).
      See [OpenTelemetry traces](https://elevenlabs.io/docs/eleven-agents/customization/opentelemetry-traces).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: elevenlabs
  product_name: ElevenLabs
  slug: 9-agent-mode-changes-in-elevenlabs-updates-2026-10-26
  source_release: elevenlabs-2026-10-26-2026-10-26-ca7c552d
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: 9 Agent Mode changes in ElevenLabs updates — 2026-10-26
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-26-2-agent-mode-changes-in-v2-1-311|2 Agent Mode
  changes in v2.1.311]]'
- '[[Changes/ElevenLabs/2026-10-26-knowledge-base-crawl-exclusions|Knowledge base
  crawl exclusions]]'
- '[[Changes/ElevenLabs/2026-10-26-elevenagents|ElevenAgents]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-26-2026-10-26-ca7c552d|elevenlabs-2026-10-26-2026-10-26-ca7c552d]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: 9 Agent Mode changes in ElevenLabs updates — 2026-10-26
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Agent Mode changes in ElevenLabs updates — 2026-10-26

**ElevenLabs** · 2026-10-26 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://elevenlabs.io/docs/changelog/2026/10/26) · from [[Releases/ElevenLabs/elevenlabs-2026-10-26-2026-10-26-ca7c552d|ElevenLabs updates — 2026-10-26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Procedures analytics**: The **Procedures** tab on the agent analytics dashboard is available to every workspace. Its **Procedure invocations** chart shows how often each [procedure](https://elevenlabs.io/docs/eleven-agents/customization/procedures) runs over time, grouped by procedure or by agent, and its tooltip shows whether a procedure is structured or free-form.

> **Start procedures at conversation start**: Conversation initiation client data accepts `start_procedure_ids`, up to five free-form procedures that start when the conversation starts. The agent must have `enable_procedure_ids_from_client` enabled; structured procedures and unknown IDs fail the conversation start.

> **Structured procedure steps**: Structured procedures can use the `end_procedure` system tool as a step, and the **End** step is relabeled **End conversation**. Sub-procedure and end steps now compile to system tool nodes, so agents start and end the intended procedure more reliably.

> **Slack thread replies**: The Slack Channel Message trigger adds a **Respond to** setting (`response_mode`), so an agent can keep replying in a thread after a single mention. Mentioning the agent with only `stop`, `mute` or `quiet` silences it in that thread until it is mentioned again, and events that Slack delivers twice get one reply.

> **Branch descriptions**: Branch descriptions can be edited from the branches table with [Update branch](https://elevenlabs.io/docs/api-reference/agents/branches/update) (`description`, up to 4,096 characters) and appear in the version tooltip and version graph.

> **Agent duplication keeps traffic splits**: Duplicating an agent copies its live traffic split across the copied branches. The resulting deployment records `duplicate` as its deployment source.

> **Delete environment variables**: `DELETE /v1/convai/environment-variables/{env_var_id}` deletes an [environment variable](https://elevenlabs.io/docs/eleven-agents/integrate/environment-variables).

> **Issues**: Triage is renamed **Issues** in the agents dashboard, and triage tickets are now called issues. Every QA comment and `flag_issue_for_review` call opens its own issue, and an issue can be reopened while the conversation has another open issue. The API endpoints keep their `triage-tickets` paths. See [Triage](https://elevenlabs.io/docs/eleven-agents/operate/triage).

> **Observability**: OpenTelemetry post-call webhook agent turn spans add `elevenlabs.rag.chunks` and `elevenlabs.rag.used_chunk_ids`, matching the JSON [post-call webhook](https://elevenlabs.io/docs/eleven-agents/workflows/post-call-webhooks). See [OpenTelemetry traces](https://elevenlabs.io/docs/eleven-agents/customization/opentelemetry-traces).

Source: https://elevenlabs.io/docs/changelog/2026/10/26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-26-2-apps-and-integrations-changes-in-elevenlabs-updates-2026-10-26|2 Apps and Integrations changes in ElevenLabs updates — 2026-10-26]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-26-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-knowledge-base-crawl-exclusions|Knowledge base crawl exclusions]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-26-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-26-clone-strength-for-v4-voices|Clone strength for v4 voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-android-sdk|Android SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-10-26-2-pricing-model-changes-in-elevenlabs-updates-2026-10-26|2 Pricing Model changes in ElevenLabs updates — 2026-10-26]] · Pricing Model
- [[Changes/ElevenLabs/2026-10-26-transcript-downloads-the-dubbing-project-menu-can-download-target-language-trans|Transcript downloads: The dubbing project menu can download target language…]] · Interface Experience
- [[Changes/ElevenLabs/2026-10-26-video-to-music-studio-s-video-to-music-workflow-uses-music-v2-5-by-default|Video to music: Studio's video to music workflow uses Music v2.5 by default]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-26-2-editor-experience-changes-in-elevenlabs-updates-2026-10-26|2 Editor Experience changes in ElevenLabs updates — 2026-10-26]] · Editor Experience
- [[Changes/ElevenLabs/2026-10-26-dubbing|Dubbing]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-voice-changer|Voice Changer]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-2-mobile-and-desktop-changes-in-elevenlabs-updates-2026-10-26|2 Mobile and Desktop changes in ElevenLabs updates — 2026-10-26]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-10-26-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-14-voice-and-audio-changes-in-elevenlabs-updates-2026-10-26|14 Voice and Audio changes in ElevenLabs updates — 2026-10-26]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-voice-cloning-permissions-members-without-the-create-instant-voice-clone-or-crea|Voice cloning permissions]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-10-26-fast-llm-service-tier|Fast LLM service tier]] · Model Support
- [[Changes/ElevenLabs/2026-10-26-3-model-support-changes-in-elevenlabs-updates-2026-10-26|3 Model Support changes in ElevenLabs updates — 2026-10-26]] · Model Support
- [[Changes/ElevenLabs/2026-10-26-elevenlabs-cli|ElevenLabs CLI]] · Account and Access
- [[Changes/ElevenLabs/2026-10-26-oauth-scope-oauth-clients-can-request-the-realtime-translation-scope|OAuth scope: OAuth clients can request the realtime_translation scope]] · Account and Access
- [[Changes/ElevenLabs/2026-10-26-9-other-changes-in-elevenlabs-updates-2026-10-26|9 other changes in ElevenLabs updates — 2026-10-26]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-26 · Claude Code · [[Changes/Claude Code/2026-10-26-2-agent-mode-changes-in-v2-1-311|2 Agent Mode changes in v2.1.311]]
- Later: 2026-10-26 · Windsurf · [[Changes/Windsurf/2026-10-26-the-status-bar-no-longer-disappears-after-you-switch-from-agent-mode-to-ide-mode|The status bar no longer disappears after you switch from Agent mode to IDE mode]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-26-b99df3&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-26-9-agent-mode-changes-in-elevenlabs-updates-2026-10-26.md%0ACard%20ID%3A%20elevenlabs-2026-10-26-b99df3%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->