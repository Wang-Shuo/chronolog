---
card_id: open-webui-2026-11-03-1edd48
date: '2026-11-03'
description: "Open WebUI · 2026-11-03 · Pricing Model: \U0001F9E0 **Context compaction
  and prompt caching.** When the same model handles the conversation and its compaction
  summary…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily
    limit: To ensure a high-quality experience for all ChatGPT users, we…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1419
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: pricing
machine_hash: f8d8645b3c4057238c16b5f3bb7df71d9896a1e8e476ef1f879c3e2eaeef2834
product: open-webui
product_name: Open WebUI
record:
  ai_generated: true
  card_id: open-webui-2026-11-03-1edd48
  comparison: ''
  confidence: low
  date: '2026-11-03'
  description: "Open WebUI — v0.13.0: \U0001F9E0 **Context compaction and prompt caching.**
    When the same model handles the conversation and its compaction summary, eligible
    requests now reuse the conversation’s prompt structure so the provider can use
    its prompt cache. This can reduce the cost of summarizing long conversations and
    agent workflows; other requests retain the separate summary path. [Commit](https://github.com/open-webui/open-webui/commit/a8b478ed7b8d22fe5b8f96be3c4cfd08cd30affb)"
  evidence:
  - quote: "\U0001F9E0 **Context compaction and prompt caching.** When the same model
      handles the conversation and its compaction summary, eligible requests now reuse
      the conversation’s prompt structure so the provider can use its prompt cache.
      This can reduce the cost of summarizing long conversations and agent workflows;
      other requests retain the separate summary path. [Commit](https://github.com/open-webui/open-webui/commit/a8b478ed7b8d22fe5b8f96be3c4cfd08cd30affb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: pricing
  product: open-webui
  product_name: Open WebUI
  slug: context-compaction-and-prompt-caching-when-the-same-model-handles-the-conversati
  source_release: open-webui-2026-11-03-v0-13-0-github-432661497-44290c10
  source_type: github_releases
  theme: pricing-model
  theme_matches:
  - matched_terms:
    - agent
    score: 50
    theme: agent-mode
  - matched_terms:
    - context
    score: 50
    theme: context-window
  - matched_terms:
    - model
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: "\U0001F9E0 **Context compaction and prompt caching.** When the same model
    handles…"
  type: change
related_changes:
- '[[Changes/Lovable/2026-10-28-get-an-email-before-your-credits-run-out|Get an email
  before your credits run out]]'
- '[[Changes/Codex CLI/2026-10-29-56495-add-paginated-channel-subscription-queries-to-the-local-message-board-feli|♯56495
  Add paginated channel subscription queries to the local message board @felixxia-oai]]'
- '[[Changes/ElevenLabs/2026-11-02-3-pricing-model-changes-in-elevenlabs-updates-2026-11-02|3
  Pricing Model changes in ElevenLabs updates — 2026-11-02]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-11-03-v0-13-0-github-432661497-44290c10|open-webui-2026-11-03-v0-13-0-github-432661497-44290c10]]'
source_type: github_releases
theme: pricing-model
title: "\U0001F9E0 Context compaction and prompt caching. When the same model handles…"
type: change
---

<!-- chronolog:begin region="header" -->
# 🧠 **Context compaction and prompt caching.** When the same model handles…

**Open WebUI** · 2026-11-03 · [[Themes/pricing-model|Pricing Model]] · Pricing · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.13.0) · from [[Releases/Open WebUI/open-webui-2026-11-03-v0-13-0-github-432661497-44290c10|v0.13.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> 🧠 **Context compaction and prompt caching.** When the same model handles the conversation and its compaction summary, eligible requests now reuse the conversation’s prompt structure so the provider can use its prompt cache. This can reduce the cost of summarizing long conversations and agent workflows; other requests retain the separate summary path. [Commit](https://github.com/open-webui/open-webui/commit/a8b478ed7b8d22fe5b8f96be3c4cfd08cd30affb)
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-11-03-mcp-apps-in-chat-tools-from-mcp-servers-that-come-with-an-interactive-app-now-sh|🧩 MCP Apps in chat. Tools from MCP servers that come with an interactive app now…]] · Apps and Integrations
- [[Changes/Open WebUI/2026-11-03-4-model-support-changes-in-v0-13-0|4 Model Support changes in v0.13.0]] · Model Support
- [[Changes/Open WebUI/2026-11-03-new-chats-stay-in-sync-a-chat-started-from-the-home-page-keeps-syncing-with-the|🔃 New chats stay in sync. A chat started from the home page keeps syncing…]] · Collaboration
- [[Changes/Open WebUI/2026-11-03-4-voice-and-audio-changes-in-v0-13-0|4 Voice and Audio changes in v0.13.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-11-03-4-editor-experience-changes-in-v0-13-0|4 Editor Experience changes in v0.13.0]] · Editor Experience
- [[Changes/Open WebUI/2026-11-03-nested-code-previews-preview-now-opens-code-blocks-inside-lists-quotes-and-detai|🧩 Nested code previews. Preview now opens code blocks inside lists, quotes…]] · Artifact Creation
- [[Changes/Open WebUI/2026-11-03-live-context-usage-estimates-the-context-indicator-now-accounts-for-output-arriv|📏 Live context usage estimates. The context indicator now accounts for output…]] · Context Window
- [[Changes/Open WebUI/2026-11-03-2-automation-and-scheduling-changes-in-v0-13-0|2 Automation and Scheduling changes in v0.13.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-11-03-2-search-and-browsing-changes-in-v0-13-0|2 Search and Browsing changes in v0.13.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-11-03-image-drops-from-photo-apps-images-dropped-into-chats-and-channels-are-now-recog|🖼️ Image drops from photo apps. Images dropped into chats and channels are now…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-11-03-saved-oauth-provider-settings-oauth-providers-now-load-their-saved-connection-se|🔑 Saved OAuth provider settings. OAuth providers now load their saved connection…]] · Account and Access
- [[Changes/Open WebUI/2026-11-03-15-developer-workflow-changes-in-v0-13-0|15 Developer Workflow changes in v0.13.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-11-03-4-interface-experience-changes-in-v0-13-0|4 Interface Experience changes in v0.13.0]] · Interface Experience
- [[Changes/Open WebUI/2026-11-03-accessibility-improvements-screen-reader-users-now-hear-a-name-for-every-window|♿ Accessibility improvements. Screen reader users now hear a name for every…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-11-03-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-11-03-2-safety-and-privacy-changes-in-v0-13-0|2 Safety and Privacy changes in v0.13.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-11-03-no-sub-agent-limits-by-default-the-sub-agent-limits-in-admin-settings-and-throug|🔓 No sub-agent limits by default. The sub-agent limits in Admin Settings…]] · Agent Mode
- [[Changes/Open WebUI/2026-11-03-5-other-changes-in-v0-13-0|5 other changes in v0.13.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-11-02 · ElevenLabs · [[Changes/ElevenLabs/2026-11-02-3-pricing-model-changes-in-elevenlabs-updates-2026-11-02|3 Pricing Model changes in ElevenLabs updates — 2026-11-02]]
- Later: 2026-11-04 · Dify · [[Changes/Dify/2026-11-04-3-pricing-model-changes-in-1-19-0|3 Pricing Model changes in 1.19.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily limit: To ensure a high-quality experience for all ChatGPT users, we…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-11-03-1edd48&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-11-03-context-compaction-and-prompt-caching-when-the-same-model-handles-the-conversati.md%0ACard%20ID%3A%20open-webui-2026-11-03-1edd48%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.13.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->