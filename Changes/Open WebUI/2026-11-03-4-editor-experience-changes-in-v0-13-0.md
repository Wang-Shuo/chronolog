---
card_id: open-webui-2026-11-03-6fc16b
date: '2026-11-03'
description: 'Open WebUI · 2026-11-03 · Editor Experience: 4 changes in v0.13.0 —
  ↔️ **Full-width tabs.** On larger screens, expand the tabbed workspace to fill the
  chat…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1330
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a27b82ec33a8867e613f30aa772f98234ae6d091680f95f55f085fa1e172aaf4
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-11-03-6fc16b
  comparison: ''
  date: '2026-11-03'
  description: 'Open WebUI — v0.13.0: 4 Editor Experience changes'
  evidence:
  - quote: ↔️ **Full-width tabs.** On larger screens, expand the tabbed workspace
      to fill the chat area, with the main conversation kept as its own tab. Switch
      between the chat, code, browser and desktop with more room to work, or return
      to the side-by-side layout; your layout choice is remembered. [Commit](https://github.com/open-webui/open-webui/commit/09030d5dd2def4324d98c25f92cf54b1ec1844f1),
      [Commit](https://github.com/open-webui/open-webui/commit/1ce8616ab9587ca717015d5af9cb26ee4296311f)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F518 **Switch tools on and off.** Tools in Workspace > Tools now
      have an on and off switch for everyone who can edit them, and a tool that is
      switched off can no longer be picked or run in any chat, including chats where
      it was already selected. [Commit](https://github.com/open-webui/open-webui/commit/9d1b4ef362f103f2dda05760a44c96df82c064fd)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: "\U0001F91D **Multi-model sub-agents.** The model editor now lets you choose
      other models for a model to delegate work to, enabling multi-agent workflows
      such as assigning research, coding and review to different models. The parent
      model chooses among the configured models the user can access; previously, sub-agents
      always used the same model as the parent. [Commit](https://github.com/open-webui/open-webui/commit/789a0f402abe05e028bc8e0a8824d58b94e26d8f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  - quote: ✍️ **Restored chat drafts.** Saved draft text now returns to the message
      input after the new-chat editor mounts, instead of disappearing during initialization.
      [Commit](https://github.com/open-webui/open-webui/commit/4ea29c0d6198e44a84aae01475b003c8bc192e5b)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-editor-experience-changes-in-v0-13-0
  source_release: open-webui-2026-11-03-v0-13-0-github-432661497-44290c10
  source_type: github_releases
  theme: editor-experience
  title: 4 Editor Experience changes in v0.13.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-31-2-editor-experience-changes-in-v2-1-316|2 Editor
  Experience changes in v2.1.316]]'
- '[[Changes/ElevenLabs/2026-11-02-svg-assets-svg-uploads-to-assets-stay-svg-and-render-as-vectors-including-in-the|SVG
  assets: SVG uploads to Assets stay SVG and render as vectors, including…]]'
- '[[Changes/Lovable/2026-11-02-project-monitoring-catches-errors-in-your-visitors-browsers|Project
  monitoring catches errors in your visitors'' browsers]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-11-03-v0-13-0-github-432661497-44290c10|open-webui-2026-11-03-v0-13-0-github-432661497-44290c10]]'
source_type: github_releases
theme: editor-experience
title: 4 Editor Experience changes in v0.13.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Editor Experience changes in v0.13.0

**Open WebUI** · 2026-11-03 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.13.0) · from [[Releases/Open WebUI/open-webui-2026-11-03-v0-13-0-github-432661497-44290c10|v0.13.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ↔️ **Full-width tabs.** On larger screens, expand the tabbed workspace to fill the chat area, with the main conversation kept as its own tab. Switch between the chat, code, browser and desktop with more room to work, or return to the side-by-side layout; your layout choice is remembered. [Commit](https://github.com/open-webui/open-webui/commit/09030d5dd2def4324d98c25f92cf54b1ec1844f1), [Commit](https://github.com/open-webui/open-webui/commit/1ce8616ab9587ca717015d5af9cb26ee4296311f)

> 🔘 **Switch tools on and off.** Tools in Workspace > Tools now have an on and off switch for everyone who can edit them, and a tool that is switched off can no longer be picked or run in any chat, including chats where it was already selected. [Commit](https://github.com/open-webui/open-webui/commit/9d1b4ef362f103f2dda05760a44c96df82c064fd)

> 🤝 **Multi-model sub-agents.** The model editor now lets you choose other models for a model to delegate work to, enabling multi-agent workflows such as assigning research, coding and review to different models. The parent model chooses among the configured models the user can access; previously, sub-agents always used the same model as the parent. [Commit](https://github.com/open-webui/open-webui/commit/789a0f402abe05e028bc8e0a8824d58b94e26d8f)

> ✍️ **Restored chat drafts.** Saved draft text now returns to the message input after the new-chat editor mounts, instead of disappearing during initialization. [Commit](https://github.com/open-webui/open-webui/commit/4ea29c0d6198e44a84aae01475b003c8bc192e5b)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.13.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-11-03-context-compaction-and-prompt-caching-when-the-same-model-handles-the-conversati|🧠 Context compaction and prompt caching. When the same model handles…]] · Pricing Model
- [[Changes/Open WebUI/2026-11-03-mcp-apps-in-chat-tools-from-mcp-servers-that-come-with-an-interactive-app-now-sh|🧩 MCP Apps in chat. Tools from MCP servers that come with an interactive app now…]] · Apps and Integrations
- [[Changes/Open WebUI/2026-11-03-4-model-support-changes-in-v0-13-0|4 Model Support changes in v0.13.0]] · Model Support
- [[Changes/Open WebUI/2026-11-03-new-chats-stay-in-sync-a-chat-started-from-the-home-page-keeps-syncing-with-the|🔃 New chats stay in sync. A chat started from the home page keeps syncing…]] · Collaboration
- [[Changes/Open WebUI/2026-11-03-4-voice-and-audio-changes-in-v0-13-0|4 Voice and Audio changes in v0.13.0]] · Voice and Audio
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
## Nearby in Editor Experience

- Earlier: 2026-11-02 · Lovable · [[Changes/Lovable/2026-11-02-project-monitoring-catches-errors-in-your-visitors-browsers|Project monitoring catches errors in your visitors' browsers]]
- Later: 2026-11-03 · OpenHands · [[Changes/OpenHands/2026-11-03-feat-files-add-a-download-button-to-the-files-tab-ohe-3834-by-hieptl-in-https-gi|feat(files): add a Download button to the Files tab (OHE-3834)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-11-03-6fc16b&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-11-03-4-editor-experience-changes-in-v0-13-0.md%0ACard%20ID%3A%20open-webui-2026-11-03-6fc16b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.13.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->