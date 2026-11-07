---
card_id: openclaw-2026-09-01-017a4e
date: '2026-09-01'
description: 'OpenClaw · 2026-09-01 · Model Support: 4 changes in v2026.8.2 — When
  a turn has already finished its tool work, OpenClaw now makes another attempt to
  produce…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1331
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a557046b0ce0f8fdf1f8c36ea8335ae3a73a8ad271e62bd08dab3e63e6e9496f
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-01-017a4e
  comparison: ''
  date: '2026-09-01'
  description: 'OpenClaw — v2026.8.2: 4 Model Support changes'
  evidence:
  - quote: When a turn has already finished its tool work, OpenClaw now makes another
      attempt to produce the final answer and, if the model still gives it nothing
      usable, leaves one clear fallback without rerunning completed actions. Accepted
      channel turns that fail before an answer also end with one compact error instead
      of a progress marker followed by silence.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: The model list and the request it starts now agree more often about which
      provider and login own the work. Authenticated Claude CLI models found in the
      full catalog can be selected before the first turn, native Claude login remains
      in charge when an unrelated Anthropic credential is stored, and simple completions
      retain the provider transport chosen during preparation instead of borrowing
      a different connection at dispatch.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: When a provider fails, OpenClaw keeps more of the useful context needed
      to recover. Chat, the terminal UI, and Gateway history can use guidance for
      the provider that actually handled the run, malformed catalog responses no longer
      replace the last healthy OpenRouter capability data, and pinned models use their
      full same-model retry and profile-rotation budget without quietly switching
      models. Chutes and Cerebras catalog estimates can refresh without overwriting
      operator-set rates, but catalog entries and estimated prices are not proof of
      account entitlement, paid inference, or a provider invoice.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Automatic shares keep the conversation readable while leaving out reasoning
      and tool details, masking known credentials, and showing when part of the transcript
      was left out. Changing the receiver starts fresh delivery to the new destination
      without carrying unfinished updates across, and readable links can use the session
      title while old links still open the same transcript.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-model-support-changes-in-v2026-8-2
  source_release: openclaw-2026-09-01-v2026-8-2-cca64187
  source_type: openclaw_changelog
  theme: model-support
  title: 4 Model Support changes in v2026.8.2
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-01-6-model-support-changes-in-v2-1-257|6 Model Support
  changes in v2.1.257]]'
- '[[Changes/Codex CLI/2026-09-01-6-model-support-changes-in-rust-v0-152-0|6 Model
  Support changes in rust-v0.152.0]]'
- '[[Changes/Codex CLI/2026-09-01-guardian-approval-review-now-honors-node-repl-policies-provided-through-model-me|Guardian
  approval review now honors Node REPL policies provided through model metadata]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|openclaw-2026-09-01-v2026-8-2-cca64187]]'
source_type: openclaw_changelog
theme: model-support
title: 4 Model Support changes in v2026.8.2
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v2026.8.2

**OpenClaw** · 2026-09-01 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.8.2) · from [[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|v2026.8.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> When a turn has already finished its tool work, OpenClaw now makes another attempt to produce the final answer and, if the model still gives it nothing usable, leaves one clear fallback without rerunning completed actions. Accepted channel turns that fail before an answer also end with one compact error instead of a progress marker followed by silence.

> The model list and the request it starts now agree more often about which provider and login own the work. Authenticated Claude CLI models found in the full catalog can be selected before the first turn, native Claude login remains in charge when an unrelated Anthropic credential is stored, and simple completions retain the provider transport chosen during preparation instead of borrowing a different connection at dispatch.

> When a provider fails, OpenClaw keeps more of the useful context needed to recover. Chat, the terminal UI, and Gateway history can use guidance for the provider that actually handled the run, malformed catalog responses no longer replace the last healthy OpenRouter capability data, and pinned models use their full same-model retry and profile-rotation budget without quietly switching models. Chutes and Cerebras catalog estimates can refresh without overwriting operator-set rates, but catalog entries and estimated prices are not proof of account entitlement, paid inference, or a provider invoice.

> Automatic shares keep the conversation readable while leaving out reasoning and tool details, masking known credentials, and showing when part of the transcript was left out. Changing the receiver starts fresh delivery to the new destination without carrying unfinished updates across, and readable links can use the session title while old links still open the same transcript.

Source: https://docs.openclaw.ai/releases/2026.8.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

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
- [[Changes/OpenClaw/2026-09-01-2-account-and-access-changes-in-v2026-8-2|2 Account and Access changes in v2026.8.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-01-importing-or-returning-to-a-large-retained-history-also-requires-less-local-work|Importing or returning to a large retained history also requires less local work…]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-01-20-other-changes-in-v2026-8-2|20 other changes in v2026.8.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-01 · Codex CLI · [[Changes/Codex CLI/2026-09-01-guardian-approval-review-now-honors-node-repl-policies-provided-through-model-me|Guardian approval review now honors Node REPL policies provided through model metadata]]
- Later: 2026-09-01 · OpenCode · [[Changes/OpenCode/2026-09-01-2-model-support-changes-in-v1-18-26|2 Model Support changes in v1.18.26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-01-017a4e&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-01-4-model-support-changes-in-v2026-8-2.md%0ACard%20ID%3A%20openclaw-2026-09-01-017a4e%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.8.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->