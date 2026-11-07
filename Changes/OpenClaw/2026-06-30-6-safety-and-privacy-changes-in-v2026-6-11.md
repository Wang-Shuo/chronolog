---
card_id: openclaw-2026-06-30-c4ced3
date: '2026-06-30'
description: 'OpenClaw · 2026-06-30 · Safety and Privacy: 6 changes in v2026.6.11
  — Control UI users now get the patched DOMPurify release, reducing exposure to the…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2163
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 08b0fccec0922accd7bbbef42d59ec43ea6df8f7fc23737be435251c30989ce6
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-06-30-c4ced3
  comparison: ''
  date: '2026-06-30'
  description: 'OpenClaw — v2026.6.11: 6 Safety and Privacy changes'
  evidence:
  - quote: 'Control UI users now get the patched DOMPurify release, reducing exposure
      to the GHSA-cmwh-pvxp-8882 sanitizer vulnerability without changing how the
      interface behaves. #95691 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'iOS users now avoid surprise notification prompts and get clear guidance
      when approval alerts are unavailable, with permission managed from one predictable
      Settings screen. #95640 Thanks @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: iOS devices are now enrolled for push notifications only after users accept
      the hosted relay disclosure and allow notifications, preventing registration
      data from being published before consent. 8efed50 Thanks @joshavant.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'After upgrading from older sandbox storage, operators now get a clear
      openclaw doctor warning about leftover registry files and can use openclaw doctor
      --fix to migrate or clean them up. #84326 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'ClawHub skill updates now honor your configured install safety policy,
      and openclaw skills update --all updates only tracked ClawHub skills instead
      of unexpectedly installing other configured skills. #95684 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Improves iOS push sandbox and release-validation coverage. #95893 Thanks
      @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 6-safety-and-privacy-changes-in-v2026-6-11
  source_release: openclaw-2026-06-30-v2026-6-11-23cb95a9
  source_type: openclaw_changelog
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v2026.6.11
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-06-29-16-safety-and-privacy-changes-in-v0-10-0|16 Safety
  and Privacy changes in v0.10.0]]'
- '[[Changes/GitHub Copilot CLI/2026-06-30-disabling-the-sandbox-for-the-rest-of-the-session-now-takes-effect-immediately-s|Disabling
  the sandbox for the rest of the session now takes effect immediately…]]'
- '[[Changes/GitHub Copilot CLI/2026-06-30-3-safety-and-privacy-changes-in-v1-0-66|3
  Safety and Privacy changes in v1.0.66]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|openclaw-2026-06-30-v2026-6-11-23cb95a9]]'
source_type: openclaw_changelog
theme: safety-privacy
title: 6 Safety and Privacy changes in v2026.6.11
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v2026.6.11

**OpenClaw** · 2026-06-30 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.6.11) · from [[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|v2026.6.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Control UI users now get the patched DOMPurify release, reducing exposure to the GHSA-cmwh-pvxp-8882 sanitizer vulnerability without changing how the interface behaves. #95691 Thanks @vincentkoc.

> iOS users now avoid surprise notification prompts and get clear guidance when approval alerts are unavailable, with permission managed from one predictable Settings screen. #95640 Thanks @joshavant.

> iOS devices are now enrolled for push notifications only after users accept the hosted relay disclosure and allow notifications, preventing registration data from being published before consent. 8efed50 Thanks @joshavant.

> After upgrading from older sandbox storage, operators now get a clear openclaw doctor warning about leftover registry files and can use openclaw doctor --fix to migrate or clean them up. #84326 Thanks @giodl73-repo.

> ClawHub skill updates now honor your configured install safety policy, and openclaw skills update --all updates only tracked ClawHub skills instead of unexpectedly installing other configured skills. #95684 Thanks @vincentkoc.

> Improves iOS push sandbox and release-validation coverage. #95893 Thanks @joshavant.

Source: https://docs.openclaw.ai/releases/2026.6.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-06-30-7-editor-experience-changes-in-v2026-6-11|7 Editor Experience changes in v2026.6.11]] · Editor Experience
- [[Changes/OpenClaw/2026-06-30-canvas-a2ui-now-serves-only-the-current-app-assets-after-each-build-so-outdated|Canvas A2UI now serves only the current app assets after each build, so outdated…]] · Files and Data
- [[Changes/OpenClaw/2026-06-30-word-powerpoint-and-excel-document-reads-and-writes-now-use-the-intended-docx-pp|Word, PowerPoint, and Excel document reads and writes now use the intended .docx…]] · Presentation Creation
- [[Changes/OpenClaw/2026-06-30-20-context-window-changes-in-v2026-6-11|20 Context Window changes in v2026.6.11]] · Context Window
- [[Changes/OpenClaw/2026-06-30-32-agent-mode-changes-in-v2026-6-11|32 Agent Mode changes in v2026.6.11]] · Agent Mode
- [[Changes/OpenClaw/2026-06-30-15-mobile-and-desktop-changes-in-v2026-6-11|15 Mobile and Desktop changes in v2026.6.11]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-06-30-5-collaboration-changes-in-v2026-6-11|5 Collaboration changes in v2026.6.11]] · Collaboration
- [[Changes/OpenClaw/2026-06-30-26-memory-and-personalization-changes-in-v2026-6-11|26 Memory and Personalization changes in v2026.6.11]] · Memory and Personalization
- [[Changes/OpenClaw/2026-06-30-34-apps-and-integrations-changes-in-v2026-6-11|34 Apps and Integrations changes in v2026.6.11]] · Apps and Integrations
- [[Changes/OpenClaw/2026-06-30-6-voice-and-audio-changes-in-v2026-6-11|6 Voice and Audio changes in v2026.6.11]] · Voice and Audio
- [[Changes/OpenClaw/2026-06-30-32-model-support-changes-in-v2026-6-11|32 Model Support changes in v2026.6.11]] · Model Support
- [[Changes/OpenClaw/2026-06-30-qqbot-group-admins-can-choose-how-broadly-slash-commands-are-available-and-priva|QQBot group admins can choose how broadly slash commands are available…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-06-30-4-reliability-and-performance-changes-in-v2026-6-11|4 Reliability and Performance changes in v2026.6.11]] · Reliability and Performance
- [[Changes/OpenClaw/2026-06-30-3-interface-experience-changes-in-v2026-6-11|3 Interface Experience changes in v2026.6.11]] · Interface Experience
- [[Changes/OpenClaw/2026-06-30-15-automation-and-scheduling-changes-in-v2026-6-11|15 Automation and Scheduling changes in v2026.6.11]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-06-30-when-a-codex-subscription-reaches-its-usage-limit-openclaw-now-moves-to-configur|When a Codex subscription reaches its usage limit, OpenClaw now moves to configured…]] · Pricing Model
- [[Changes/OpenClaw/2026-06-30-9-developer-workflow-changes-in-v2026-6-11|9 Developer Workflow changes in v2026.6.11]] · Developer Workflow
- [[Changes/OpenClaw/2026-06-30-more-official-channel-provider-and-web-search-plugins-can-now-be-installed-or-re|More official channel, provider, and web-search plugins can now be installed…]] · Search and Browsing
- [[Changes/OpenClaw/2026-06-30-generated-images-from-a-remote-codex-app-server-now-arrive-as-attachments-instea|Generated images from a remote Codex app-server now arrive as attachments instead…]] · Image Generation
- [[Changes/OpenClaw/2026-06-30-background-image-video-and-music-results-now-return-to-the-chat-that-requested-t|Background image, video, and music results now return to the chat that requested…]] · Music Generation
- [[Changes/OpenClaw/2026-06-30-2-account-and-access-changes-in-v2026-6-11|2 Account and Access changes in v2026.6.11]] · Account and Access
- [[Changes/OpenClaw/2026-06-30-96-other-changes-in-v2026-6-11|96 other changes in v2026.6.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-3-safety-and-privacy-changes-in-v1-0-66|3 Safety and Privacy changes in v1.0.66]]
- Later: 2026-06-30 · OpenCode · [[Changes/OpenCode/2026-06-30-sdk-add-session-permission-request-create-and-fetch-endpoints|SDK Add session permission request create and fetch endpoints]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-06-30-c4ced3&body=Card%3A%20Changes%2FOpenClaw%2F2026-06-30-6-safety-and-privacy-changes-in-v2026-6-11.md%0ACard%20ID%3A%20openclaw-2026-06-30-c4ced3%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.6.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->