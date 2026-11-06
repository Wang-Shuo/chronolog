---
card_id: elevenlabs-2026-11-02-cbdc28
date: '2026-11-02'
description: 'ElevenLabs · 2026-11-02 · Apps and Integrations: **Channel integrations**:
  Asynchronous channels such as Slack, Telegram, Intercom, Gmail, Salesforce and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1320
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: change
machine_hash: 5e1c55beaa509707cfcac940085d0df1d1f504d6162c1b80af0b42eff715746a
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-11-02-cbdc28
  comparison: ''
  confidence: low
  date: '2026-11-02'
  description: 'ElevenLabs — ElevenLabs updates — 2026-11-02: **Channel integrations**:
    Asynchronous channels such as Slack, Telegram, Intercom, Gmail, Salesforce and
    Custom Channel record message timestamps from the source platform and store the
    conversation''s `main_language` from the language override or the agent''s language
    instead of always `en`. Salesforce passes the customer''s email to the agent as
    `integration__salesforce_customer_email`, which is not a verified identity. Gmail
    triggers run on the agent''s current version, back off on Gmail rate limits and
    set aside threads that keep failing.'
  evidence:
  - quote: '**Channel integrations**: Asynchronous channels such as Slack, Telegram,
      Intercom, Gmail, Salesforce and Custom Channel record message timestamps from
      the source platform and store the conversation''s `main_language` from the language
      override or the agent''s language instead of always `en`. Salesforce passes
      the customer''s email to the agent as `integration__salesforce_customer_email`,
      which is not a verified identity. Gmail triggers run on the agent''s current
      version, back off on Gmail rate limits and set aside threads that keep failing.'
    source_release: https://elevenlabs.io/docs/changelog/2026/11/2
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: change
  product: elevenlabs
  product_name: ElevenLabs
  slug: channel-integrations-asynchronous-channels-such-as-slack-telegram-intercom-gmail
  source_release: elevenlabs-2026-11-02-2026-11-02-7efe9660
  source_type: elevenlabs_changelog
  theme: apps-integrations
  theme_matches:
  - matched_terms:
    - integration
    - integrations
    score: 100
    theme: apps-integrations
  - matched_terms:
    - agent
    score: 50
    theme: agent-mode
  title: '**Channel integrations**: Asynchronous channels such as Slack, Telegram,
    Intercom…'
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-10-29-2-apps-and-integrations-changes-in-v0-12-5|2 Apps
  and Integrations changes in v0.12.5]]'
- '[[Changes/Claude Code/2026-10-30-3-apps-and-integrations-changes-in-v2-1-314|3
  Apps and Integrations changes in v2.1.314]]'
- '[[Changes/Claude Code/2026-10-31-7-apps-and-integrations-changes-in-v2-1-316|7
  Apps and Integrations changes in v2.1.316]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-11-02-2026-11-02-7efe9660|elevenlabs-2026-11-02-2026-11-02-7efe9660]]'
source_type: elevenlabs_changelog
theme: apps-integrations
title: 'Channel integrations: Asynchronous channels such as Slack, Telegram, Intercom…'
type: change
---

<!-- chronolog:begin region="header" -->
# **Channel integrations**: Asynchronous channels such as Slack, Telegram, Intercom…

**ElevenLabs** · 2026-11-02 · [[Themes/apps-integrations|Apps and Integrations]] · [Official source](https://elevenlabs.io/docs/changelog/2026/11/2) · from [[Releases/ElevenLabs/elevenlabs-2026-11-02-2026-11-02-7efe9660|ElevenLabs updates — 2026-11-02]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Channel integrations**: Asynchronous channels such as Slack, Telegram, Intercom, Gmail, Salesforce and Custom Channel record message timestamps from the source platform and store the conversation's `main_language` from the language override or the agent's language instead of always `en`. Salesforce passes the customer's email to the agent as `integration__salesforce_customer_email`, which is not a verified identity. Gmail triggers run on the agent's current version, back off on Gmail rate limits and set aside threads that keep failing.
>
> Source: https://elevenlabs.io/docs/changelog/2026/11/2
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
- [[Changes/ElevenLabs/2026-11-02-fixes-oauth-discovery-names-the-host-the-client-connected-to-so-mcp-clients-such|Fixes: OAuth discovery names the host the client connected to, so MCP clients…]] · Account and Access
- [[Changes/ElevenLabs/2026-11-02-16-voice-and-audio-changes-in-elevenlabs-updates-2026-11-02|16 Voice and Audio changes in ElevenLabs updates — 2026-11-02]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-fixes-history-items-for-v4-generations-keep-clone-strength-and-speed-in-their-sa|Fixes: History items for v4 generations keep clone_strength and speed…]] · Reliability and Performance
- [[Changes/ElevenLabs/2026-11-02-professional-voice-clones-on-eleven-v4|Professional Voice Clones on Eleven v4]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-realtime-entity-redaction|Realtime entity redaction]] · Voice and Audio
- [[Changes/ElevenLabs/2026-11-02-7-other-changes-in-elevenlabs-updates-2026-11-02|7 other changes in ElevenLabs updates — 2026-11-02]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-31 · Claude Code · [[Changes/Claude Code/2026-10-31-7-apps-and-integrations-changes-in-v2-1-316|7 Apps and Integrations changes in v2.1.316]]
- Later: 2026-11-02 · Lovable · [[Changes/Lovable/2026-11-02-connect-your-app-to-bamboohr|Connect your app to BambooHR]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-11-02-cbdc28&body=Card%3A%20Changes%2FElevenLabs%2F2026-11-02-channel-integrations-asynchronous-channels-such-as-slack-telegram-intercom-gmail.md%0ACard%20ID%3A%20elevenlabs-2026-11-02-cbdc28%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F11%2F2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->