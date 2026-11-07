---
card_id: elevenlabs-2026-11-02-757ef7
date: '2026-11-02'
description: 'ElevenLabs · 2026-11-02 · Agent Mode: 8 changes in ElevenLabs updates
  — 2026-11-02 — **Analysis items API**: Evaluation criteria and data collection items
  can…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1215
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8a9e1fc009413985a9cb8a612eab4bce664132323ceafae5e8e3d4e11491b8c7
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-11-02-757ef7
  comparison: ''
  date: '2026-11-02'
  description: 'ElevenLabs — ElevenLabs updates — 2026-11-02: 8 Agent Mode changes'
  evidence:
  - quote: '**Analysis items API**: Evaluation criteria and data collection items
      can be managed as reusable [analysis items](https://elevenlabs.io/docs/eleven-agents/customization/agent-analysis/analysis-library)
      under `/v1/convai/analysis-items`, with endpoints to list, create, get, update,
      copy and delete items, list versions, list dependent agents and update attachments
      in bulk.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Conversation message counts**: [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
      and [Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get)
      return `user_message_count` and `agent_message_count`. `message_count` on the
      conversation list now counts only turns with text, so tool-only turns are no
      longer counted. Conversations with no messages get a `call_successful` value
      of `unknown`, and the dashboard shows them as "No conversation".'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Agent testing**: Tool call tests accept `guardrail_trigger` to assert
      that a guardrail should or should not trigger on the generated turn, with **Should
      trigger** and **Should not trigger** options in the dashboard. Tests whose turn
      is blocked by a guardrail now fail with "Agent response blocked by guardrail"
      instead of returning an inconclusive result. [List test invocations](https://elevenlabs.io/docs/api-reference/tests/test-invocations/list)
      accepts `created_by_user_id`, and the test history adds a creator filter. Test
      runs are returned in creation order. See [Agent testing](https://elevenlabs.io/docs/eleven-agents/customization/agent-testing).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Branches and merges**: Branches can have a default environment, set
      when creating or publishing to a branch and changed from the branch menu. Conversations
      on the branch use that environment unless the caller requests another one, and
      such branches cannot receive live traffic. Merge and rebase conflicts can be
      resolved with Architect, and procedure conflicts can be edited and combined
      like prompt conflicts. A single procedure''s unpublished changes can be discarded
      without discarding the whole draft. Branches whose only version was created
      with changes can be merged, and branch responses report a `current_live_percentage`
      of 100 for the main branch when the agent has no live deployment.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Issues**: Issue descriptions can be edited from the issue details sheet,
      and [Update triage ticket](https://elevenlabs.io/docs/api-reference/triage-tickets/update)
      accepts `qa_comment`. See [Triage](https://elevenlabs.io/docs/eleven-agents/operate/triage).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Widget**: Widget configuration adds `transcript_speech_sync_enabled`
      (default `true`), with a **Reveal transcript as the agent speaks** switch; set
      it to `false` to show each message in full at once. `show_rich_content` carousel
      cards accept `rating` (0 to 5) and `review_count`, shown as stars. Resumed persistent
      text conversations replay rich content in their history. See [Widget](https://elevenlabs.io/docs/eleven-agents/customization/widget).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Environment variables**: Deleting an [environment variable](https://elevenlabs.io/docs/eleven-agents/integrate/environment-variables)
      that the tip of a live branch references fails with `409` and lists the affected
      agents and branches. The environment variables table adds **Remove value** and
      **Delete** row actions.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Fixes**: Files that the LLM provider cannot process are dropped instead
      of failing later turns. Deleting an agent removes its trigger connections, so
      the integration connection can be deleted afterwards. The prompt editor saves
      `&` and `>` as typed instead of encoding them. Say nodes no longer duplicate
      messages, merge proposals that add a node group no longer fail, and node groups
      show their configured titles. The structured procedure editor opens procedures
      authored through the API, and dynamic variables in If step expressions are included
      in `referenced_dynamic_variables`. Agents whose data collection item uses a
      dynamic variable can be published again. Knowledge base rediscovery adds pages
      to older crawl jobs. The concurrency chart no longer overstates peaks when grouped
      by agent or branch. Garbled characters in LLM tool call arguments are repaired,
      and WhatsApp webhooks with resent interactive replies or contacts without a
      name are accepted instead of failing with `422`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: elevenlabs
  product_name: ElevenLabs
  slug: 8-agent-mode-changes-in-elevenlabs-updates-2026-11-02
  source_release: elevenlabs-2026-11-02-2026-11-02-7efe9660
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: 8 Agent Mode changes in ElevenLabs updates — 2026-11-02
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-11-02-elevenlabs-cli|ElevenLabs CLI]]'
- '[[Changes/ElevenLabs/2026-11-02-analysis-items-api|Analysis items API]]'
- '[[Changes/ElevenLabs/2026-11-02-elevenagents|ElevenAgents]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-11-02-2026-11-02-7efe9660|elevenlabs-2026-11-02-2026-11-02-7efe9660]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: 8 Agent Mode changes in ElevenLabs updates — 2026-11-02
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Agent Mode changes in ElevenLabs updates — 2026-11-02

**ElevenLabs** · 2026-11-02 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://elevenlabs.io/docs/changelog/2026/11/2) · from [[Releases/ElevenLabs/elevenlabs-2026-11-02-2026-11-02-7efe9660|ElevenLabs updates — 2026-11-02]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Analysis items API**: Evaluation criteria and data collection items can be managed as reusable [analysis items](https://elevenlabs.io/docs/eleven-agents/customization/agent-analysis/analysis-library) under `/v1/convai/analysis-items`, with endpoints to list, create, get, update, copy and delete items, list versions, list dependent agents and update attachments in bulk.

> **Conversation message counts**: [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list) and [Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get) return `user_message_count` and `agent_message_count`. `message_count` on the conversation list now counts only turns with text, so tool-only turns are no longer counted. Conversations with no messages get a `call_successful` value of `unknown`, and the dashboard shows them as "No conversation".

> **Agent testing**: Tool call tests accept `guardrail_trigger` to assert that a guardrail should or should not trigger on the generated turn, with **Should trigger** and **Should not trigger** options in the dashboard. Tests whose turn is blocked by a guardrail now fail with "Agent response blocked by guardrail" instead of returning an inconclusive result. [List test invocations](https://elevenlabs.io/docs/api-reference/tests/test-invocations/list) accepts `created_by_user_id`, and the test history adds a creator filter. Test runs are returned in creation order. See [Agent testing](https://elevenlabs.io/docs/eleven-agents/customization/agent-testing).

> **Branches and merges**: Branches can have a default environment, set when creating or publishing to a branch and changed from the branch menu. Conversations on the branch use that environment unless the caller requests another one, and such branches cannot receive live traffic. Merge and rebase conflicts can be resolved with Architect, and procedure conflicts can be edited and combined like prompt conflicts. A single procedure's unpublished changes can be discarded without discarding the whole draft. Branches whose only version was created with changes can be merged, and branch responses report a `current_live_percentage` of 100 for the main branch when the agent has no live deployment.

> **Issues**: Issue descriptions can be edited from the issue details sheet, and [Update triage ticket](https://elevenlabs.io/docs/api-reference/triage-tickets/update) accepts `qa_comment`. See [Triage](https://elevenlabs.io/docs/eleven-agents/operate/triage).

> **Widget**: Widget configuration adds `transcript_speech_sync_enabled` (default `true`), with a **Reveal transcript as the agent speaks** switch; set it to `false` to show each message in full at once. `show_rich_content` carousel cards accept `rating` (0 to 5) and `review_count`, shown as stars. Resumed persistent text conversations replay rich content in their history. See [Widget](https://elevenlabs.io/docs/eleven-agents/customization/widget).

> **Environment variables**: Deleting an [environment variable](https://elevenlabs.io/docs/eleven-agents/integrate/environment-variables) that the tip of a live branch references fails with `409` and lists the affected agents and branches. The environment variables table adds **Remove value** and **Delete** row actions.

> **Fixes**: Files that the LLM provider cannot process are dropped instead of failing later turns. Deleting an agent removes its trigger connections, so the integration connection can be deleted afterwards. The prompt editor saves `&` and `>` as typed instead of encoding them. Say nodes no longer duplicate messages, merge proposals that add a node group no longer fail, and node groups show their configured titles. The structured procedure editor opens procedures authored through the API, and dynamic variables in If step expressions are included in `referenced_dynamic_variables`. Agents whose data collection item uses a dynamic variable can be published again. Knowledge base rediscovery adds pages to older crawl jobs. The concurrency chart no longer overstates peaks when grouped by agent or branch. Garbled characters in LLM tool call arguments are repaired, and WhatsApp webhooks with resent interactive replies or contacts without a name are accepted instead of failing with `422`.

Source: https://elevenlabs.io/docs/changelog/2026/11/2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-11-02-elevenlabs-cli|ElevenLabs CLI]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-4-safety-and-privacy-changes-in-elevenlabs-updates-2026-11-02|4 Safety and Privacy changes in ElevenLabs updates — 2026-11-02]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-11-02-3-pricing-model-changes-in-elevenlabs-updates-2026-11-02|3 Pricing Model changes in ElevenLabs updates — 2026-11-02]] · Pricing Model
- [[Changes/ElevenLabs/2026-11-02-analysis-items-api|Analysis items API]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-sfx-v3|SFX v3]] · Model Support
- [[Changes/ElevenLabs/2026-11-02-7-model-support-changes-in-elevenlabs-updates-2026-11-02|7 Model Support changes in ElevenLabs updates — 2026-11-02]] · Model Support
- [[Changes/ElevenLabs/2026-11-02-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-2-interface-experience-changes-in-elevenlabs-updates-2026-11-02|2 Interface Experience changes in ElevenLabs updates — 2026-11-02]] · Interface Experience
- [[Changes/ElevenLabs/2026-11-02-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-workspaces|Workspaces]] · Agent Mode
- [[Changes/ElevenLabs/2026-11-02-2-files-and-data-changes-in-elevenlabs-updates-2026-11-02|2 Files and Data changes in ElevenLabs updates — 2026-11-02]] · Files and Data
- [[Changes/ElevenLabs/2026-11-02-android-sdk|Android SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-11-02-eleven-realtime-for-every-workspace|Eleven Realtime for every workspace]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-noisy-environment-detection-in-the-api|Noisy environment detection in the API]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-unity-sdk|Unity SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-video-clip-background-removal-video-clips-have-a-remove-background-action-and-ri|Video clip background removal]] · Multimodal Input
- [[Changes/ElevenLabs/2026-11-02-svg-assets-svg-uploads-to-assets-stay-svg-and-render-as-vectors-including-in-the|SVG assets: SVG uploads to Assets stay SVG and render as vectors, including…]] · Editor Experience
- [[Changes/ElevenLabs/2026-11-02-channel-integrations-asynchronous-channels-such-as-slack-telegram-intercom-gmail|Channel integrations: Asynchronous channels such as Slack, Telegram, Intercom…]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-11-02-fixes-oauth-discovery-names-the-host-the-client-connected-to-so-mcp-clients-such|Fixes: OAuth discovery names the host the client connected to, so MCP clients…]] · Account and Access
- [[Changes/ElevenLabs/2026-11-02-16-voice-and-audio-changes-in-elevenlabs-updates-2026-11-02|16 Voice and Audio changes in ElevenLabs updates — 2026-11-02]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-fixes-history-items-for-v4-generations-keep-clone-strength-and-speed-in-their-sa|Fixes: History items for v4 generations keep clone_strength and speed…]] · Reliability and Performance
- [[Changes/ElevenLabs/2026-11-02-professional-voice-clones-on-eleven-v4|Professional Voice Clones on Eleven v4]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-realtime-entity-redaction|Realtime entity redaction]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-7-other-changes-in-elevenlabs-updates-2026-11-02|7 other changes in ElevenLabs updates — 2026-11-02]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-31 · Claude Code · [[Changes/Claude Code/2026-10-31-2-agent-mode-changes-in-v2-1-316|2 Agent Mode changes in v2.1.316]]
- Later: 2026-11-03 · Google Antigravity · [[Changes/Google Antigravity/2026-11-03-remote-agents-are-starting-to-roll-out-to-google-ai-ultra-and-pro-subscribers-co|Remote agents are starting to roll out to Google AI Ultra and Pro subscribers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-11-02-757ef7&body=Card%3A%20Changes%2FElevenLabs%2F2026-11-02-8-agent-mode-changes-in-elevenlabs-updates-2026-11-02.md%0ACard%20ID%3A%20elevenlabs-2026-11-02-757ef7%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F11%2F2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->