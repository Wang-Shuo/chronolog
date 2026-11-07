---
card_id: openclaw-2026-09-03-dfafc5
date: '2026-09-03'
description: 'OpenClaw · 2026-09-03 · Model Support: 12 changes in v2026.9.1 — Getting
  OpenClaw running now takes a shorter path when the machine already has usable AI…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1333
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2cf5a95a2d556a6d1c090a5dddf99c9f26ec68b367144d4a248bc4f08dbc105e
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-03-dfafc5
  comparison: ''
  date: '2026-09-03'
  description: 'OpenClaw — v2026.9.1: 12 Model Support changes'
  evidence:
  - quote: Getting OpenClaw running now takes a shorter path when the machine already
      has usable AI access, while longer setup paths leave existing choices and files
      alone when a check fails or a different route is selected. This release also
      tightens Windows installation, macOS AI setup, shell configuration, Connect
      handoffs, and managed local-model downloads.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The renderer is lazy-loaded and isolated from the rest of the page, and
      model-authored output is reduced to passive SVG before display. Incomplete fences
      remain code, while invalid, oversized, or externally dependent diagrams fall
      back to readable source with an error instead of being treated as a successful
      render.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The Android app now brings the pieces people reach for during a normal
      conversation into one more complete native experience. The composer has a full-width
      writing area with compact actions, model names remain readable, and searchable
      controls expose models, effort, Fast Mode, and permissions without crowding
      the transcript. Sessions can be browsed or created from the native catalog,
      the sidebar can be arranged around the places you use, and theme families and
      accents stay with the correct profile through offline changes, reconnects, and
      app recreation.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: That work also keeps the app usable on narrow screens and with larger text,
      and it gives an actionable Providers and Models route before sending with an
      explicitly selected model whose authentication is unavailable. That check still
      follows the availability reported by the connected Gateway and is scoped to
      explicitly selected models.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Reasoning choices now stay attached to the runtime that actually owns them.
      Eligible Sol and Terra turns keep Ultra through supported child-session boundaries,
      configured native Codex models show the effort levels their account advertises,
      and Luna remains capped at Max. Anthropic Fable 5.1 joins the shared API and
      Claude CLI catalogs, supported local Ollama routes remain selectable, and status
      views keep an authored context cap when a model runs through a provider alias.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Model, utility model, fallback, thinking, and Fast Mode share the Defaults
      card. Published 2026.9.1 interface with fictional Harbor data; no live task
      execution.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Provider state is now much closer to what you actually configured. Model
      Provider settings stop counting unrelated web-search and extraction credentials
      as model accounts, externally authenticated OpenAI models remain visible without
      a second login, and compatible catalog updates survive both credential changes
      and hot reloads. A new provider login, a settings edit, or a compatible model
      change can refresh the inventory when it is next requested instead of leaving
      the old list in place until a restart.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Ordinary model inventory browsing now reuses a prepared catalog unless
      authentication is stale or a refresh was explicitly requested, so lists and
      pickers keep discovered models through temporary discovery failures without
      repeating full provider discovery.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Temporary provider failures now have one bounded retry owner, so a brief
      outage can recover quietly while a persistent one reaches the normal profile
      or model fallback path, or gives you an actionable error, within the retry window.
      A busy session stops after the first model candidate instead of making every
      fallback look broken, while hard Anthropic and Bedrock refusals stop immediately
      with revise-and-retry guidance rather than resending the request. Doctor can
      also remove a stale automatic OpenAI route without disturbing an intentional
      model choice.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Self-hosted model routes now behave more like services OpenClaw can actually
      live with. Existing llama.cpp-compatible web apps can fall back to /v1/models
      when their root models endpoint serves HTML or unusable data, managed diagnostics
      stop reading oversized response bodies without a bound, and OpenClaw waits for
      managed local model processes to stop before finishing shutdown. The shutdown
      proof is scoped to Linux and systemd, and the discovery fallback was exercised
      at the provider boundary rather than as a complete Unsloth inference run.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Newly recorded Codex dashboard turns now keep reasoning as typed thinking
      instead of mirroring it into ordinary answer text. Saved reasoning appears under
      Worked only when the session explicitly uses /reasoning on and the local View
      → Reasoning control is enabled, while off and stream keep it hidden after reload
      without hiding the final answer.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Previously malformed transcript rows are not rewritten. This change is
      also limited to saved Codex reasoning in the Control UI and does not resolve
      separate provider or channel-streaming leakage reports.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 12-model-support-changes-in-v2026-9-1
  source_release: openclaw-2026-09-03-v2026-9-1-281124fc
  source_type: openclaw_changelog
  theme: model-support
  title: 12 Model Support changes in v2026.9.1
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-09-03-gemini-3-8-flash-using-adc-in-agy-enterprise|Gemini
  3.8 Flash using ADC in AGY Enterprise]]'
- '[[Changes/Lovable/2026-09-03-gemini-omni-1-1-flash-for-your-app-s-ai-features|Gemini
  Omni 1.1 Flash for your app''s AI features]]'
- '[[Changes/Midjourney/2026-09-03-thank-you-for-all-of-your-dedicated-testing-feedback-and-bug-reports-over-the-la|Thank
  you for all of your dedicated testing, feedback, and bug reports over the last…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|openclaw-2026-09-03-v2026-9-1-281124fc]]'
source_type: openclaw_changelog
theme: model-support
title: 12 Model Support changes in v2026.9.1
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Model Support changes in v2026.9.1

**OpenClaw** · 2026-09-03 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.1) · from [[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|v2026.9.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Getting OpenClaw running now takes a shorter path when the machine already has usable AI access, while longer setup paths leave existing choices and files alone when a check fails or a different route is selected. This release also tightens Windows installation, macOS AI setup, shell configuration, Connect handoffs, and managed local-model downloads.

> The renderer is lazy-loaded and isolated from the rest of the page, and model-authored output is reduced to passive SVG before display. Incomplete fences remain code, while invalid, oversized, or externally dependent diagrams fall back to readable source with an error instead of being treated as a successful render.

> The Android app now brings the pieces people reach for during a normal conversation into one more complete native experience. The composer has a full-width writing area with compact actions, model names remain readable, and searchable controls expose models, effort, Fast Mode, and permissions without crowding the transcript. Sessions can be browsed or created from the native catalog, the sidebar can be arranged around the places you use, and theme families and accents stay with the correct profile through offline changes, reconnects, and app recreation.

> That work also keeps the app usable on narrow screens and with larger text, and it gives an actionable Providers and Models route before sending with an explicitly selected model whose authentication is unavailable. That check still follows the availability reported by the connected Gateway and is scoped to explicitly selected models.

> Reasoning choices now stay attached to the runtime that actually owns them. Eligible Sol and Terra turns keep Ultra through supported child-session boundaries, configured native Codex models show the effort levels their account advertises, and Luna remains capped at Max. Anthropic Fable 5.1 joins the shared API and Claude CLI catalogs, supported local Ollama routes remain selectable, and status views keep an authored context cap when a model runs through a provider alias.

> Model, utility model, fallback, thinking, and Fast Mode share the Defaults card. Published 2026.9.1 interface with fictional Harbor data; no live task execution.

> Provider state is now much closer to what you actually configured. Model Provider settings stop counting unrelated web-search and extraction credentials as model accounts, externally authenticated OpenAI models remain visible without a second login, and compatible catalog updates survive both credential changes and hot reloads. A new provider login, a settings edit, or a compatible model change can refresh the inventory when it is next requested instead of leaving the old list in place until a restart.

> Ordinary model inventory browsing now reuses a prepared catalog unless authentication is stale or a refresh was explicitly requested, so lists and pickers keep discovered models through temporary discovery failures without repeating full provider discovery.

> Temporary provider failures now have one bounded retry owner, so a brief outage can recover quietly while a persistent one reaches the normal profile or model fallback path, or gives you an actionable error, within the retry window. A busy session stops after the first model candidate instead of making every fallback look broken, while hard Anthropic and Bedrock refusals stop immediately with revise-and-retry guidance rather than resending the request. Doctor can also remove a stale automatic OpenAI route without disturbing an intentional model choice.

> Self-hosted model routes now behave more like services OpenClaw can actually live with. Existing llama.cpp-compatible web apps can fall back to /v1/models when their root models endpoint serves HTML or unusable data, managed diagnostics stop reading oversized response bodies without a bound, and OpenClaw waits for managed local model processes to stop before finishing shutdown. The shutdown proof is scoped to Linux and systemd, and the discovery fallback was exercised at the provider boundary rather than as a complete Unsloth inference run.

> Newly recorded Codex dashboard turns now keep reasoning as typed thinking instead of mirroring it into ordinary answer text. Saved reasoning appears under Worked only when the session explicitly uses /reasoning on and the local View → Reasoning control is enabled, while off and stream keep it hidden after reload without hiding the final answer.

> Previously malformed transcript rows are not rewritten. This change is also limited to saved Codex reasoning in the Control UI and does not resolve separate provider or channel-streaming leakage reports.

Source: https://docs.openclaw.ai/releases/2026.9.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-03-14-agent-mode-changes-in-v2026-9-1|14 Agent Mode changes in v2026.9.1]] · Agent Mode
- [[Changes/OpenClaw/2026-09-03-12-voice-and-audio-changes-in-v2026-9-1|12 Voice and Audio changes in v2026.9.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-03-2-files-and-data-changes-in-v2026-9-1|2 Files and Data changes in v2026.9.1]] · Files and Data
- [[Changes/OpenClaw/2026-09-03-7-collaboration-changes-in-v2026-9-1|7 Collaboration changes in v2026.9.1]] · Collaboration
- [[Changes/OpenClaw/2026-09-03-10-mobile-and-desktop-changes-in-v2026-9-1|10 Mobile and Desktop changes in v2026.9.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-03-19-memory-and-personalization-changes-in-v2026-9-1|19 Memory and Personalization changes in v2026.9.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-03-3-editor-experience-changes-in-v2026-9-1|3 Editor Experience changes in v2026.9.1]] · Editor Experience
- [[Changes/OpenClaw/2026-09-03-2-search-and-browsing-changes-in-v2026-9-1|2 Search and Browsing changes in v2026.9.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-03-12-account-and-access-changes-in-v2026-9-1|12 Account and Access changes in v2026.9.1]] · Account and Access
- [[Changes/OpenClaw/2026-09-03-several-less-visible-repairs-keep-the-apps-from-failing-around-dependencies-and|Several less visible repairs keep the apps from failing around dependencies…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-03-13-automation-and-scheduling-changes-in-v2026-9-1|13 Automation and Scheduling changes in v2026.9.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-03-an-update-or-doctor-repair-now-does-more-to-preserve-the-setup-you-already-autho|An update or Doctor repair now does more to preserve the setup you already authored…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-03-11-developer-workflow-changes-in-v2026-9-1|11 Developer Workflow changes in v2026.9.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-03-3-accessibility-and-localization-changes-in-v2026-9-1|3 Accessibility and Localization changes in v2026.9.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-03-26-apps-and-integrations-changes-in-v2026-9-1|26 Apps and Integrations changes in v2026.9.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-03-10-safety-and-privacy-changes-in-v2026-9-1|10 Safety and Privacy changes in v2026.9.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-03-11-context-window-changes-in-v2026-9-1|11 Context Window changes in v2026.9.1]] · Context Window
- [[Changes/OpenClaw/2026-09-03-14-interface-experience-changes-in-v2026-9-1|14 Interface Experience changes in v2026.9.1]] · Interface Experience
- [[Changes/OpenClaw/2026-09-03-on-linux-managed-local-model-and-embedding-services-are-preferred-as-the-out-of|On Linux, managed local model and embedding services are preferred…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-03-32-other-changes-in-v2026-9-1|32 other changes in v2026.9.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-03 · Midjourney · [[Changes/Midjourney/2026-09-03-thank-you-for-all-of-your-dedicated-testing-feedback-and-bug-reports-over-the-la|Thank you for all of your dedicated testing, feedback, and bug reports over the last…]]
- Later: 2026-09-04 · Claude Code · [[Changes/Claude Code/2026-09-04-improved-the-model-picker-and-the-vs-code-model-pill-to-show-a-model-s-name-inst|Improved the /model picker and the VS Code model pill to show a model's name…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-03-dfafc5&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-03-12-model-support-changes-in-v2026-9-1.md%0ACard%20ID%3A%20openclaw-2026-09-03-dfafc5%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->