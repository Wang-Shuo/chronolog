---
card_id: openclaw-2026-09-01-d184fc
date: '2026-09-01'
description: 'OpenClaw · 2026-09-01 · Account and Access: 2 changes in v2026.8.2 —
  When a model needs a runtime plugin, macOS onboarding and the Control UI can show
  where…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1251
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0d1c1c2beaf7fb57586d4329cac91d06ce70a19b62d736ee6e1ac017b8b4435c
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-01-d184fc
  comparison: ''
  date: '2026-09-01'
  description: 'OpenClaw — v2026.8.2: 2 Account and Access changes'
  evidence:
  - quote: When a model needs a runtime plugin, macOS onboarding and the Control UI
      can show where the plugin comes from and which capabilities it requests, ask
      for explicit approval, install it, and verify the model in the same flow. Declining
      or cancelling leaves the configured model unchanged and stops the attempt. Mac
      users can also finish ChatGPT Login after a same-route reconnect when the original
      callback was proven unsent, cancel a stalled provider sign-in, or quit onboarding
      without a late result taking over a replacement attempt.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Model and speech-provider setup now stays more closely aligned with the
      provider, login, voice, and transport that actually own the request. Catalog
      failures retain the last healthy information, pinned models use their intended
      retry budget, configured private speech endpoints stay scoped to their origin,
      and automatic language detection no longer inserts an English instruction when
      no language was chosen.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 2-account-and-access-changes-in-v2026-8-2
  source_release: openclaw-2026-09-01-v2026-8-2-cca64187
  source_type: openclaw_changelog
  theme: account-access
  title: 2 Account and Access changes in v2026.8.2
  type: change
related_changes:
- "[[Changes/Open WebUI/2026-08-31-disconnect-oauth-only-where-there-is-oauth-the-disconnect-control-on-a-tool-serv|\U0001F50C
  Disconnect OAuth only where there is OAuth. The disconnect control on a tool…]]"
- '[[Changes/Claude Code/2026-09-01-2-account-and-access-changes-in-v2-1-257|2 Account
  and Access changes in v2.1.257]]'
- '[[Changes/Codex CLI/2026-09-01-2-account-and-access-changes-in-rust-v0-152-0|2
  Account and Access changes in rust-v0.152.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|openclaw-2026-09-01-v2026-8-2-cca64187]]'
source_type: openclaw_changelog
theme: account-access
title: 2 Account and Access changes in v2026.8.2
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Account and Access changes in v2026.8.2

**OpenClaw** · 2026-09-01 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.8.2) · from [[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|v2026.8.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> When a model needs a runtime plugin, macOS onboarding and the Control UI can show where the plugin comes from and which capabilities it requests, ask for explicit approval, install it, and verify the model in the same flow. Declining or cancelling leaves the configured model unchanged and stops the attempt. Mac users can also finish ChatGPT Login after a same-route reconnect when the original callback was proven unsent, cancel a stalled provider sign-in, or quit onboarding without a late result taking over a replacement attempt.

> Model and speech-provider setup now stays more closely aligned with the provider, login, voice, and transport that actually own the request. Catalog failures retain the last healthy information, pinned models use their intended retry budget, configured private speech endpoints stay scoped to their origin, and automatic language detection no longer inserts an English instruction when no language was chosen.

Source: https://docs.openclaw.ai/releases/2026.8.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-01-4-model-support-changes-in-v2026-8-2|4 Model Support changes in v2026.8.2]] · Model Support
- [[Changes/OpenClaw/2026-09-01-11-agent-mode-changes-in-v2026-8-2|11 Agent Mode changes in v2026.8.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-01-9-voice-and-audio-changes-in-v2026-8-2|9 Voice and Audio changes in v2026.8.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-01-3-context-window-changes-in-v2026-8-2|3 Context Window changes in v2026.8.2]] · Context Window
- [[Changes/OpenClaw/2026-09-01-4-collaboration-changes-in-v2026-8-2|4 Collaboration changes in v2026.8.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-01-5-editor-experience-changes-in-v2026-8-2|5 Editor Experience changes in v2026.8.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-01-7-safety-and-privacy-changes-in-v2026-8-2|7 Safety and Privacy changes in v2026.8.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-01-3-mobile-and-desktop-changes-in-v2026-8-2|3 Mobile and Desktop changes in v2026.8.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-01-another-382-changes-in-v2026-8-2-primarily-affect-the-people-who-build-test-docu|Another 382 changes in v2026.8.2 primarily affect the people who build, test…]] · Files and Data
- [[Changes/OpenClaw/2026-09-01-usage-and-status-views-now-carry-cumulative-output-token-totals-through-tool-cal|Usage and status views now carry cumulative output-token totals through tool calls…]] · Pricing Model
- [[Changes/OpenClaw/2026-09-01-2-automation-and-scheduling-changes-in-v2026-8-2|2 Automation and Scheduling changes in v2026.8.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-01-9-apps-and-integrations-changes-in-v2026-8-2|9 Apps and Integrations changes in v2026.8.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-01-4-memory-and-personalization-changes-in-v2026-8-2|4 Memory and Personalization changes in v2026.8.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-01-3-interface-experience-changes-in-v2026-8-2|3 Interface Experience changes in v2026.8.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-01-importing-or-returning-to-a-large-retained-history-also-requires-less-local-work|Importing or returning to a large retained history also requires less local work…]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-01-20-other-changes-in-v2026-8-2|20 other changes in v2026.8.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-09-01 · Codex CLI · [[Changes/Codex CLI/2026-09-01-2-account-and-access-changes-in-rust-v0-152-0|2 Account and Access changes in rust-v0.152.0]]
- Later: 2026-09-01 · OpenCode · [[Changes/OpenCode/2026-09-01-azure-cli-sign-in-now-asks-for-the-resource-name-directly-instead-of-querying-az|Azure CLI sign-in now asks for the resource name directly instead of querying Azure…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-01-d184fc&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-01-2-account-and-access-changes-in-v2026-8-2.md%0ACard%20ID%3A%20openclaw-2026-09-01-d184fc%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.8.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->