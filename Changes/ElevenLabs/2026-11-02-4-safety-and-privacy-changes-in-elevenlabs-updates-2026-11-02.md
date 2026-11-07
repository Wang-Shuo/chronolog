---
card_id: elevenlabs-2026-11-02-15e864
date: '2026-11-02'
description: 'ElevenLabs · 2026-11-02 · Safety and Privacy: 4 changes in ElevenLabs
  updates — 2026-11-02 — **WhatsApp**: WhatsApp conversations record `call_result`…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2288
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d9f106cdffbd0b800d9f309e95e99ba05b6da788d3d0b87e260fa2f3141ded3b
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-11-02-15e864
  comparison: ''
  date: '2026-11-02'
  description: 'ElevenLabs — ElevenLabs updates — 2026-11-02: 4 Safety and Privacy
    changes'
  evidence:
  - quote: '**WhatsApp**: WhatsApp conversations record `call_result` (`answered`,
      `voicemail`, `busy`, `no_answer` or `failed`), and conversations opened with
      a template record `opening_message` with the template name, delivery timestamps,
      error code and pricing category. Call permission requests record `responded_at_unix`,
      `permanent` and `granted_by_user_call`. WhatsApp batch calls that are declined,
      missed or cannot be placed mark the recipient `failed` instead of leaving it
      `initiated`. See [WhatsApp](https://elevenlabs.io/docs/eleven-agents/whatsapp).'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Realtime authentication**: Bearer tokens passed to the realtime WebSocket
      in `Sec-WebSocket-Protocol` require the Speech to Text permission, as the other
      authentication methods do.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**Architect permission**: Architect access is controlled by its own workspace
      permission. `PermissionType` adds `agents_architect` and group permissions add
      `architect`, so admins can turn off Architect without removing Agents access,
      and API keys have a separate Architect scope.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  - quote: '**History download permission**: [Download history items](https://elevenlabs.io/docs/api-reference/history/download)
      requires the `speech_history_read` API key permission.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: elevenlabs
  product_name: ElevenLabs
  slug: 4-safety-and-privacy-changes-in-elevenlabs-updates-2026-11-02
  source_release: elevenlabs-2026-11-02-2026-11-02-7efe9660
  source_type: elevenlabs_changelog
  theme: safety-privacy
  title: 4 Safety and Privacy changes in ElevenLabs updates — 2026-11-02
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-30-10-safety-and-privacy-changes-in-v2-1-314|10 Safety
  and Privacy changes in v2.1.314]]'
- '[[Changes/OpenCode/2026-10-30-core-preserved-permission-reasons-and-feedback-in-mcp-failures-and-made-code-mod|Core
  Preserved permission reasons and feedback in MCP failures, and made Code Mode…]]'
- '[[Changes/Lovable/2026-11-01-download-an-sbom-for-your-project|Download an SBOM
  for your project]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-11-02-2026-11-02-7efe9660|elevenlabs-2026-11-02-2026-11-02-7efe9660]]'
source_type: elevenlabs_changelog
theme: safety-privacy
title: 4 Safety and Privacy changes in ElevenLabs updates — 2026-11-02
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in ElevenLabs updates — 2026-11-02

**ElevenLabs** · 2026-11-02 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://elevenlabs.io/docs/changelog/2026/11/2) · from [[Releases/ElevenLabs/elevenlabs-2026-11-02-2026-11-02-7efe9660|ElevenLabs updates — 2026-11-02]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **WhatsApp**: WhatsApp conversations record `call_result` (`answered`, `voicemail`, `busy`, `no_answer` or `failed`), and conversations opened with a template record `opening_message` with the template name, delivery timestamps, error code and pricing category. Call permission requests record `responded_at_unix`, `permanent` and `granted_by_user_call`. WhatsApp batch calls that are declined, missed or cannot be placed mark the recipient `failed` instead of leaving it `initiated`. See [WhatsApp](https://elevenlabs.io/docs/eleven-agents/whatsapp).

> **Realtime authentication**: Bearer tokens passed to the realtime WebSocket in `Sec-WebSocket-Protocol` require the Speech to Text permission, as the other authentication methods do.

> **Architect permission**: Architect access is controlled by its own workspace permission. `PermissionType` adds `agents_architect` and group permissions add `architect`, so admins can turn off Architect without removing Agents access, and API keys have a separate Architect scope.

> **History download permission**: [Download history items](https://elevenlabs.io/docs/api-reference/history/download) requires the `speech_history_read` API key permission.

Source: https://elevenlabs.io/docs/changelog/2026/11/2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-11-02-elevenlabs-cli|ElevenLabs CLI]] · Agent Mode
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
- [[Changes/ElevenLabs/2026-11-02-16-voice-and-audio-changes-in-elevenlabs-updates-2026-11-02|16 Voice and Audio changes in ElevenLabs updates — 2026-11-02]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-fixes-history-items-for-v4-generations-keep-clone-strength-and-speed-in-their-sa|Fixes: History items for v4 generations keep clone_strength and speed…]] · Reliability and Performance
- [[Changes/ElevenLabs/2026-11-02-professional-voice-clones-on-eleven-v4|Professional Voice Clones on Eleven v4]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-realtime-entity-redaction|Realtime entity redaction]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-7-other-changes-in-elevenlabs-updates-2026-11-02|7 other changes in ElevenLabs updates — 2026-11-02]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-11-01 · Lovable · [[Changes/Lovable/2026-11-01-download-an-sbom-for-your-project|Download an SBOM for your project]]
- Later: 2026-11-02 · Lovable · [[Changes/Lovable/2026-11-02-redesigned-action-center-reviews|Redesigned Action center reviews]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-11-02-15e864&body=Card%3A%20Changes%2FElevenLabs%2F2026-11-02-4-safety-and-privacy-changes-in-elevenlabs-updates-2026-11-02.md%0ACard%20ID%3A%20elevenlabs-2026-11-02-15e864%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F11%2F2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->