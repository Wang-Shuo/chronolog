---
card_id: elevenlabs-2026-10-19-9fea0d
date: '2026-10-19'
description: 'ElevenLabs · 2026-10-19 · Enterprise and Administration: Realtime Translation
  turns speech in one language into speech in another while the speaker is still…'
diffusion:
  first_in_tracked: '[[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export
    members as CSV (for Enterprise Plans) Quickly download a list of the people…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2470
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: b77b958985c15354cb43b66a623900a529a984665dcaa442eb9da329131cd4ab
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-10-19-9fea0d
  comparison: ''
  date: '2026-10-19'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-19: Realtime Translation
    turns speech in one language into speech in another while the speaker is still
    talking. It''s a [WebSocket API](https://elevenlabs.io/docs/api-reference/realtime-translation/v-1-translation-realtime),
    available now for enterprise workspaces.'
  evidence:
  - quote: Realtime Translation turns speech in one language into speech in another
      while the speaker is still talking. It's a [WebSocket API](https://elevenlabs.io/docs/api-reference/realtime-translation/v-1-translation-realtime),
      available now for enterprise workspaces.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: You open a connection with a `target_language` and a `voice_id`, then stream
      audio in. You get translated speech back in that voice. You don't have to say
      which language the speaker is using, because it's detected automatically, but
      you can set `source_language` if you know it. Along the way, the server also
      sends live transcripts of the original speech and the translated text, for example
      to show captions.
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '`eagerness` controls the tradeoff between speed and quality. `high` starts
      translating soonest, and `low` waits for more of the sentence. The translated
      voice uses Eleven v4 Turbo by default, and you can switch to `eleven_v3` or
      `eleven_flash_v2_5` with `tts_model_id`. For sensitive conversations, set `enable_zrm=true`
      to use [Zero Retention Mode](https://elevenlabs.io/docs/eleven-api/resources/zero-retention-mode).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: realtime-translation
  source_release: elevenlabs-2026-10-19-2026-10-19-dd219c14
  source_type: elevenlabs_changelog
  theme: enterprise-admin
  title: Realtime Translation
  type: change
related_changes:
- '[[Changes/Replit/2026-10-16-bring-your-own-cloud-to-replit|Bring Your Own Cloud
  to Replit]]'
- '[[Changes/Lovable/2026-10-18-request-edit-access-to-a-project-you-can-only-view|Request
  edit access to a project you can only view]]'
- '[[Changes/ElevenLabs/2026-10-19-music-and-sound-effects|Music and Sound Effects]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-19-2026-10-19-dd219c14|elevenlabs-2026-10-19-2026-10-19-dd219c14]]'
source_type: elevenlabs_changelog
theme: enterprise-admin
title: Realtime Translation
type: change
---

<!-- chronolog:begin region="header" -->
# Realtime Translation

**ElevenLabs** · 2026-10-19 · [[Themes/enterprise-admin|Enterprise and Administration]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/10/19) · from [[Releases/ElevenLabs/elevenlabs-2026-10-19-2026-10-19-dd219c14|ElevenLabs updates — 2026-10-19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Realtime Translation turns speech in one language into speech in another while the speaker is still talking. It's a [WebSocket API](https://elevenlabs.io/docs/api-reference/realtime-translation/v-1-translation-realtime), available now for enterprise workspaces.
>
> You open a connection with a `target_language` and a `voice_id`, then stream audio in. You get translated speech back in that voice. You don't have to say which language the speaker is using, because it's detected automatically, but you can set `source_language` if you know it. Along the way, the server also sends live transcripts of the original speech and the translated text, for example to show captions.
>
> `eagerness` controls the tradeoff between speed and quality. `high` starts translating soonest, and `low` waits for more of the sentence. The translated voice uses Eleven v4 Turbo by default, and you can switch to `eleven_v3` or `eleven_flash_v2_5` with `tts_model_id`. For sensitive conversations, set `enable_zrm=true` to use [Zero Retention Mode](https://elevenlabs.io/docs/eleven-api/resources/zero-retention-mode).
>
> Source: https://elevenlabs.io/docs/changelog/2026/10/19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-19-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-19-music-and-sound-effects|Music and Sound Effects]] · Enterprise and Administration
- [[Changes/ElevenLabs/2026-10-19-eleven-realtime|Eleven Realtime]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-elevenagents|ElevenAgents]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-video-to-music|Video to Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-19-javascript-sdk|JavaScript SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-elevenagents-b18b24|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-music|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-19-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-python-sdk|Python SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-19-elevenagents-ee74ab|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-voices-f9aa8c|Voices]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2026-10-18 · Lovable · [[Changes/Lovable/2026-10-18-request-edit-access-to-a-project-you-can-only-view|Request edit access to a project you can only view]]
- Later: 2026-10-19 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-19-2-enterprise-and-administration-changes-in-v1-0-100|2 Enterprise and Administration changes in v1.0.100]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-01-14 · Notion · [[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export members as CSV (for Enterprise Plans) Quickly download a list of the people…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-19-9fea0d&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-19-realtime-translation.md%0ACard%20ID%3A%20elevenlabs-2026-10-19-9fea0d%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->