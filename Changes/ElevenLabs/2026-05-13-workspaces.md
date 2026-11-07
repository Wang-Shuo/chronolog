---
card_id: elevenlabs-2026-05-13-d918ed
date: '2026-05-13'
description: 'ElevenLabs · 2026-05-13 · Editor Experience: Service account API key
  create and edit schemas'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2740
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 0832a6defcefaad3777126461c3cfeae603263cfcb0538a93fb6c51963de01ce
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-05-13-d918ed
  comparison: ''
  date: '2026-05-13'
  description: 'ElevenLabs — ElevenLabs updates — 2026-05-13: Service account API
    key create and edit schemas'
  evidence:
  - quote: Service account API key create and edit schemas
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Added `allowed_ips` as an optional array of IP addresses or CIDR ranges,
      with 1 to 100 entries
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Create requests can pass `null` to allow all IPs
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Edit requests can pass `clear` or `no_update`; the default is `no_update`
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: '`WorkspaceApiKeyResponseModel`'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Added nullable `allowed_ips`
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: '`WorkspaceGroupPermission` enum'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Added `conversational_ai_read` and `voice_design`
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Auth connection schemas
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  - quote: Added `ApiIntegrationOAuth2CustomAppResponse` for user-owned OAuth2 custom
      app connections
    source_release: https://elevenlabs.io/docs/changelog/2026/5/13
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: workspaces
  source_release: elevenlabs-2026-05-13-2026-05-13-1809b47f
  source_type: elevenlabs_changelog
  theme: editor-experience
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: Workspaces
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-12-read-only-gh-cli-commands-list-view-status-diff-etc-are-auto-approved-without-pr|Read-only
  gh CLI commands (list, view, status, diff, etc.) are auto-approved without…]]'
- '[[Changes/v0/2026-05-12-the-vs-code-editor-in-your-chats-autosaves-by-default-with-a-new-vercel-light-th|The
  VS Code editor in your chats autosaves by default, with a new Vercel Light theme…]]'
- '[[Changes/Cursor/2026-05-13-improved-pr-tabs-by-adding-clearer-review-states-better-reviewer-thread-visibili|Improved
  PR tabs by adding clearer review states, better reviewer/thread visibility…]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-05-13-2026-05-13-1809b47f|elevenlabs-2026-05-13-2026-05-13-1809b47f]]'
source_type: elevenlabs_changelog
theme: editor-experience
title: Workspaces
type: change
---

<!-- chronolog:begin region="header" -->
# Workspaces

**ElevenLabs** · 2026-05-13 · [[Themes/editor-experience|Editor Experience]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/5/13) · from [[Releases/ElevenLabs/elevenlabs-2026-05-13-2026-05-13-1809b47f|ElevenLabs updates — 2026-05-13]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Service account API key create and edit schemas
>
> Added `allowed_ips` as an optional array of IP addresses or CIDR ranges, with 1 to 100 entries
>
> Create requests can pass `null` to allow all IPs
>
> Edit requests can pass `clear` or `no_update`; the default is `no_update`
>
> `WorkspaceApiKeyResponseModel`
>
> Added nullable `allowed_ips`
>
> `WorkspaceGroupPermission` enum
>
> Added `conversational_ai_read` and `voice_design`
>
> Auth connection schemas
>
> Added `ApiIntegrationOAuth2CustomAppResponse` for user-owned OAuth2 custom app connections
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
- [[Changes/ElevenLabs/2026-05-13-elevenagents-6f8d80|ElevenAgents]] · Files and Data
- [[Changes/ElevenLabs/2026-05-13-packages|Packages]] · Agent Mode
- [[Changes/ElevenLabs/2026-05-13-voice-design-b2b3bd|Voice Design]] · Voice and Audio
- [[Changes/ElevenLabs/2026-05-13-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-05-13-voice-changer-cdfc87|Voice Changer]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-05-13 · Cursor · [[Changes/Cursor/2026-05-13-improved-pr-tabs-by-adding-clearer-review-states-better-reviewer-thread-visibili|Improved PR tabs by adding clearer review states, better reviewer/thread visibility…]]
- Later: 2026-05-13 · Krea · [[Changes/Krea/2026-05-13-recipients-can-generate-using-your-moodboard-but-not-edit-it|Recipients can generate using your moodboard, but not edit it]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-05-13-d918ed&body=Card%3A%20Changes%2FElevenLabs%2F2026-05-13-workspaces.md%0ACard%20ID%3A%20elevenlabs-2026-05-13-d918ed%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F5%2F13%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->