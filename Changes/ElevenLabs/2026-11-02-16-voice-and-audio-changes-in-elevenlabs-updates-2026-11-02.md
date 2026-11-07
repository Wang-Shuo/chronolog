---
card_id: elevenlabs-2026-11-02-dc19a1
date: '2026-11-02'
description: 'ElevenLabs · 2026-11-02 · Voice and Audio: 16 changes in ElevenLabs
  updates — 2026-11-02 — **Noisy environment detection**: `turn.noisy_environment_detection`…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1211
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8bad3dd46a046912bc7562796f19c2ba048f61936abe9c84751de0dc6fb5dc11
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-11-02-dc19a1
  comparison: ''
  date: '2026-11-02'
  description: 'ElevenLabs — ElevenLabs updates — 2026-11-02: 16 Voice and Audio changes'
  evidence:
  - quote: '**Noisy environment detection**: `turn.noisy_environment_detection` (default
      `false`) and `turn.noisy_environment_message` are available in the API, along
      with `noisy_environment_message_translation` on language presets and `noisy_environment_message`
      in conversation and workflow overrides. Available for voice agents in Enterprise
      workspaces. See [Noisy environment detection](https://elevenlabs.io/docs/eleven-agents/customization/conversation-flow#noisy-environment-detection).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Eleven Realtime available to all workspaces**: [Realtime voice mode](https://elevenlabs.io/docs/eleven-agents/customization/realtime-models),
      the Realtime WebSocket and the Realtime Conversations page are available to
      every workspace, completing the gradual rollout announced on October 19. Realtime
      conversation groups can now be managed through the API, under `/v1/convai/realtime/conversation-groups`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Realtime API behavior**: Each manual `input_audio_buffer.commit` transcribes
      only the speech since the previous commit, and `input_audio_buffer.clear` drops
      buffered audio. `response.metadata` from `response.create` is echoed on `response.created`
      and `response.done`, with at most 16 string pairs. `input_audio_buffer.speech_started`
      and `speech_stopped` are sent once per committed user turn instead of on every
      pause. Idle audio sessions close after 3 minutes instead of 60 seconds, after
      a `session_idle_timeout` error.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Dashboard**: The conversation view shows human agent replies captured
      after an escalation in a separate post-escalation section. The system prompt
      editor''s wand opens an **Ask Architect** menu to review and improve the prompt
      or write a new one. Filtered conversation exports include evaluation criteria
      and data collection results. Turns where the agent speaks after a silence timeout
      no longer report end-to-end latency. The agent voice settings show the **Clone
      strength** slider for every voice fine-tuned for a v4 model.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Realtime entity redaction**: The realtime WebSocket accepts `entity_redaction`
      (`all`, a category such as `pii`, `phi` or `pci`, or a list of entity types)
      and `entity_redaction_mode` (`redacted`, `entity_type` or `enumerated_entity_type`,
      the default). Each committed transcript is followed by a `redacted_transcript`
      event, and the settings are echoed in `session_started`. `entity_redaction`
      cannot be combined with `transcript_edit`. See [Entity detection](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/entity-detection#entity-redaction).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Usage on empty responses**: Empty and silent responses from [Create
      transcript](https://elevenlabs.io/docs/api-reference/speech-to-text/convert)
      include `audio_duration_secs`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Fixes**: Webhook transcription requests, with a file upload or `cloud_storage_url`,
      now apply `diarization_threshold` and `seed`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Professional Voice Clones on Eleven v4**: Professional Voice Clone fine-tuning
      for Eleven v4 and Eleven v4 Turbo is available to every workspace. See [Eleven
      v4](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4#voice-cloning).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Saved clone strength**: Eleven v4 requests for a fine-tuned Professional
      Voice Clone use the voice''s saved `clone_strength` when the request sets neither
      `clone_strength` nor `use_pvc_as_ivc`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Larger media uploads**: Pro and higher plans can upload audio and video
      assets of up to 3 GB, up from 1 GB.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Fixes**: The import speech endpoints for external audio and video clips
      return `429` `system_busy` and refund the transcription charge when transcription
      capacity is unavailable, instead of returning `500`. Duplicating a project no
      longer fails when an image clip points at a source image that is not copied.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Close codes**: The WebSocket always closes with a code: `1000` for a
      normal end, `1008` for a rejected request such as an unknown `voice_id` or an
      authentication failure, and `1011` for a server error.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Fixes**: Translated audio is encoded in the requested `output_format`,
      so μ-law and A-law output plays correctly. Repeated utterances are no longer
      dropped, Chinese, Japanese and Korean clauses are no longer spoken twice or
      skipped, and Korean word order is improved.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Clearer reference errors**: Generations whose reference file was refused
      on upload, or is not decodable audio, fail as a validation error with a clear
      message instead of an unexpected error.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Larger voice selections**: Manual voice selection is no longer limited
      to 10 voices, and link-shared voice collections offer **Select all**. Shared
      collection links open in the EU, India and Singapore data residency environments.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Fixes**: The voice verification captcha accepts Serbian readings in
      Latin or mixed script.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: elevenlabs
  product_name: ElevenLabs
  slug: 16-voice-and-audio-changes-in-elevenlabs-updates-2026-11-02
  source_release: elevenlabs-2026-11-02-2026-11-02-7efe9660
  source_type: elevenlabs_changelog
  theme: voice
  title: 16 Voice and Audio changes in ElevenLabs updates — 2026-11-02
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-11-02-noisy-environment-detection-in-the-api|Noisy environment
  detection in the API]]'
- '[[Changes/ElevenLabs/2026-11-02-unity-sdk|Unity SDK]]'
- '[[Changes/ElevenLabs/2026-11-02-javascript-sdk|JavaScript SDK]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-11-02-2026-11-02-7efe9660|elevenlabs-2026-11-02-2026-11-02-7efe9660]]'
source_type: elevenlabs_changelog
theme: voice
title: 16 Voice and Audio changes in ElevenLabs updates — 2026-11-02
type: change
---

<!-- chronolog:begin region="header" -->
# 16 Voice and Audio changes in ElevenLabs updates — 2026-11-02

**ElevenLabs** · 2026-11-02 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://elevenlabs.io/docs/changelog/2026/11/2) · from [[Releases/ElevenLabs/elevenlabs-2026-11-02-2026-11-02-7efe9660|ElevenLabs updates — 2026-11-02]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Noisy environment detection**: `turn.noisy_environment_detection` (default `false`) and `turn.noisy_environment_message` are available in the API, along with `noisy_environment_message_translation` on language presets and `noisy_environment_message` in conversation and workflow overrides. Available for voice agents in Enterprise workspaces. See [Noisy environment detection](https://elevenlabs.io/docs/eleven-agents/customization/conversation-flow#noisy-environment-detection).

> **Eleven Realtime available to all workspaces**: [Realtime voice mode](https://elevenlabs.io/docs/eleven-agents/customization/realtime-models), the Realtime WebSocket and the Realtime Conversations page are available to every workspace, completing the gradual rollout announced on October 19. Realtime conversation groups can now be managed through the API, under `/v1/convai/realtime/conversation-groups`.

> **Realtime API behavior**: Each manual `input_audio_buffer.commit` transcribes only the speech since the previous commit, and `input_audio_buffer.clear` drops buffered audio. `response.metadata` from `response.create` is echoed on `response.created` and `response.done`, with at most 16 string pairs. `input_audio_buffer.speech_started` and `speech_stopped` are sent once per committed user turn instead of on every pause. Idle audio sessions close after 3 minutes instead of 60 seconds, after a `session_idle_timeout` error.

> **Dashboard**: The conversation view shows human agent replies captured after an escalation in a separate post-escalation section. The system prompt editor's wand opens an **Ask Architect** menu to review and improve the prompt or write a new one. Filtered conversation exports include evaluation criteria and data collection results. Turns where the agent speaks after a silence timeout no longer report end-to-end latency. The agent voice settings show the **Clone strength** slider for every voice fine-tuned for a v4 model.

> **Realtime entity redaction**: The realtime WebSocket accepts `entity_redaction` (`all`, a category such as `pii`, `phi` or `pci`, or a list of entity types) and `entity_redaction_mode` (`redacted`, `entity_type` or `enumerated_entity_type`, the default). Each committed transcript is followed by a `redacted_transcript` event, and the settings are echoed in `session_started`. `entity_redaction` cannot be combined with `transcript_edit`. See [Entity detection](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/entity-detection#entity-redaction).

> **Usage on empty responses**: Empty and silent responses from [Create transcript](https://elevenlabs.io/docs/api-reference/speech-to-text/convert) include `audio_duration_secs`.

> **Fixes**: Webhook transcription requests, with a file upload or `cloud_storage_url`, now apply `diarization_threshold` and `seed`.

> **Professional Voice Clones on Eleven v4**: Professional Voice Clone fine-tuning for Eleven v4 and Eleven v4 Turbo is available to every workspace. See [Eleven v4](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4#voice-cloning).

> **Saved clone strength**: Eleven v4 requests for a fine-tuned Professional Voice Clone use the voice's saved `clone_strength` when the request sets neither `clone_strength` nor `use_pvc_as_ivc`.

> **Larger media uploads**: Pro and higher plans can upload audio and video assets of up to 3 GB, up from 1 GB.

> **Fixes**: The import speech endpoints for external audio and video clips return `429` `system_busy` and refund the transcription charge when transcription capacity is unavailable, instead of returning `500`. Duplicating a project no longer fails when an image clip points at a source image that is not copied.

> **Close codes**: The WebSocket always closes with a code: `1000` for a normal end, `1008` for a rejected request such as an unknown `voice_id` or an authentication failure, and `1011` for a server error.

> **Fixes**: Translated audio is encoded in the requested `output_format`, so μ-law and A-law output plays correctly. Repeated utterances are no longer dropped, Chinese, Japanese and Korean clauses are no longer spoken twice or skipped, and Korean word order is improved.

> **Clearer reference errors**: Generations whose reference file was refused on upload, or is not decodable audio, fail as a validation error with a clear message instead of an unexpected error.

> **Larger voice selections**: Manual voice selection is no longer limited to 10 voices, and link-shared voice collections offer **Select all**. Shared collection links open in the EU, India and Singapore data residency environments.

> **Fixes**: The voice verification captcha accepts Serbian readings in Latin or mixed script.

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
- [[Changes/ElevenLabs/2026-11-02-8-agent-mode-changes-in-elevenlabs-updates-2026-11-02|8 Agent Mode changes in ElevenLabs updates — 2026-11-02]] · Agent Mode
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
- [[Changes/ElevenLabs/2026-11-02-fixes-history-items-for-v4-generations-keep-clone-strength-and-speed-in-their-sa|Fixes: History items for v4 generations keep clone_strength and speed…]] · Reliability and Performance
- [[Changes/ElevenLabs/2026-11-02-professional-voice-clones-on-eleven-v4|Professional Voice Clones on Eleven v4]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-realtime-entity-redaction|Realtime entity redaction]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-7-other-changes-in-elevenlabs-updates-2026-11-02|7 other changes in ElevenLabs updates — 2026-11-02]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-10-29 · Suno · [[Changes/Suno/2026-10-29-auto-stretch-for-added-audio|Auto-stretch for Added Audio]]
- Later: 2026-11-03 · Google Antigravity · [[Changes/Google Antigravity/2026-11-03-voice-mode-remote-agents-redesigned-automations-and-jupyter-notebook-viewer|Voice mode, remote agents, redesigned Automations, and Jupyter notebook viewer]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-11-02-dc19a1&body=Card%3A%20Changes%2FElevenLabs%2F2026-11-02-16-voice-and-audio-changes-in-elevenlabs-updates-2026-11-02.md%0ACard%20ID%3A%20elevenlabs-2026-11-02-dc19a1%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F11%2F2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->