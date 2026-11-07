---
card_id: opencode-2026-10-27-57ce0b
date: '2026-10-27'
description: 'OpenCode · 2026-10-27 · Apps and Integrations: @opencode/plugin now
  requires @opentui/core and @opentui/solid 0.7.0, up from 0.6.8 or later. Plugins
  that…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2874
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 8fa12209ce142a7e27ead42f43c0f538ff1926e13e829a2b56597b7149f09f5d
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-10-27-57ce0b
  comparison: ''
  date: '2026-10-27'
  description: 'OpenCode — v2.2.0: @opencode/plugin now requires @opentui/core and
    @opentui/solid 0.7.0, up from 0.6.8 or later. Plugins that depend on OpenTUI 0.6
    fail to install until they upgrade. In OpenTUI 0.7, custom renderables read their
    hooks from their class at construction: assign renderBefore , renderAfter , and
    onLifecyclePass in the constructor instead of as class fields, call refreshHooks()
    after adding a hook by reflection, and replace defineNativeIntegration() with
    a static nativeIntegration declaration. See the OpenTUI 0.7.0 release notes .'
  evidence:
  - quote: '@opencode/plugin now requires @opentui/core and @opentui/solid 0.7.0,
      up from 0.6.8 or later. Plugins that depend on OpenTUI 0.6 fail to install until
      they upgrade. In OpenTUI 0.7, custom renderables read their hooks from their
      class at construction: assign renderBefore , renderAfter , and onLifecyclePass
      in the constructor instead of as class fields, call refreshHooks() after adding
      a hook by reflection, and replace defineNativeIntegration() with a static nativeIntegration
      declaration. See the OpenTUI 0.7.0 release notes .'
    source_release: https://opencode.ai/changelog/v2.2.0
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: opencode
  product_name: OpenCode
  slug: tui-plugins-require-opentui-0-7
  source_release: opencode-2026-10-27-v2-2-0-f60b51f1
  source_type: opencode_changelog
  theme: apps-integrations
  title: TUI plugins require OpenTUI 0.7
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-27-9-apps-and-integrations-changes-in-v2026-10-8|9 Apps
  and Integrations changes in v2026.10.8]]'
- '[[Changes/OpenCode/2026-10-27-add-experimental-image-and-decision-generation-apis-to-plugins-and-sdk|Add
  experimental image and decision generation APIs to plugins and sdk]]'
- '[[Changes/OpenCode/2026-10-27-create-install-and-share-desktop-plugins-experimental|Create,
  install and share Desktop plugins (experimental)]]'
source_release: '[[Releases/OpenCode/opencode-2026-10-27-v2-2-0-f60b51f1|opencode-2026-10-27-v2-2-0-f60b51f1]]'
source_type: opencode_changelog
theme: apps-integrations
title: TUI plugins require OpenTUI 0.7
type: change
---

<!-- chronolog:begin region="header" -->
# TUI plugins require OpenTUI 0.7

**OpenCode** · 2026-10-27 · [[Themes/apps-integrations|Apps and Integrations]] · Launch · [Official source](https://opencode.ai/changelog/v2.2.0) · from [[Releases/OpenCode/opencode-2026-10-27-v2-2-0-f60b51f1|v2.2.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> @opencode/plugin now requires @opentui/core and @opentui/solid 0.7.0, up from 0.6.8 or later. Plugins that depend on OpenTUI 0.6 fail to install until they upgrade. In OpenTUI 0.7, custom renderables read their hooks from their class at construction: assign renderBefore , renderAfter , and onLifecyclePass in the constructor instead of as class fields, call refreshHooks() after adding a hook by reflection, and replace defineNativeIntegration() with a static nativeIntegration declaration. See the OpenTUI 0.7.0 release notes .
>
> Source: https://opencode.ai/changelog/v2.2.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-10-27-73-mobile-and-desktop-changes-in-v2-2-0|73 Mobile and Desktop changes in v2.2.0]] · Mobile and Desktop
- [[Changes/OpenCode/2026-10-27-13-model-support-changes-in-v2-2-0|13 Model Support changes in v2.2.0]] · Model Support
- [[Changes/OpenCode/2026-10-27-core-preserve-literal-0-and-arguments-text-in-custom-command-input|Core Preserve literal $0 and $ARGUMENTS text in custom command input]] · Pricing Model
- [[Changes/OpenCode/2026-10-27-add-experimental-image-and-decision-generation-apis-to-plugins-and-sdk|Add experimental image and decision generation APIs to plugins and sdk]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-2-search-and-browsing-changes-in-v2-2-0|2 Search and Browsing changes in v2.2.0]] · Search and Browsing
- [[Changes/OpenCode/2026-10-27-create-install-and-share-desktop-plugins-experimental|Create, install and share Desktop plugins (experimental)]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-10-interface-experience-changes-in-v2-2-0|10 Interface Experience changes in v2.2.0]] · Interface Experience
- [[Changes/OpenCode/2026-10-27-3-context-window-changes-in-v2-2-0|3 Context Window changes in v2.2.0]] · Context Window
- [[Changes/OpenCode/2026-10-27-restored-the-todo-tool-in-desktop-via-opt-in|Restored the Todo tool in desktop via opt-in]] · Mobile and Desktop
- [[Changes/OpenCode/2026-10-27-8-memory-and-personalization-changes-in-v2-2-0|8 Memory and Personalization changes in v2.2.0]] · Memory and Personalization
- [[Changes/OpenCode/2026-10-27-14-apps-and-integrations-changes-in-v2-2-0|14 Apps and Integrations changes in v2.2.0]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-core-honor-shared-parallel-tool-call-and-service-tier-settings-for-groq|Core Honor shared parallel tool-call and service-tier settings for Groq]] · Collaboration
- [[Changes/OpenCode/2026-10-27-2-voice-and-audio-changes-in-v2-2-0|2 Voice and Audio changes in v2.2.0]] · Voice and Audio
- [[Changes/OpenCode/2026-10-27-refreshed-the-desktop-app-experience|Refreshed the desktop app experience]] · Mobile and Desktop
- [[Changes/OpenCode/2026-10-27-2-safety-and-privacy-changes-in-v2-2-0|2 Safety and Privacy changes in v2.2.0]] · Safety and Privacy
- [[Changes/OpenCode/2026-10-27-core-coordinate-oauth-credential-refreshes-across-locations-and-processes|Core Coordinate OAuth credential refreshes across locations and processes]] · Account and Access
- [[Changes/OpenCode/2026-10-27-5-editor-experience-changes-in-v2-2-0|5 Editor Experience changes in v2.2.0]] · Editor Experience
- [[Changes/OpenCode/2026-10-27-plugins-can-now-attach-and-update-keyed-session-instructions-with-ctx-session-in|Plugins can now attach and update keyed session instructions…]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-add-configurable-prompt-cache-ttls-per-provider-model|Add configurable prompt cache TTLs per provider/model]] · Model Support
- [[Changes/OpenCode/2026-10-27-2-agent-mode-changes-in-v2-2-0|2 Agent Mode changes in v2.2.0]] · Agent Mode
- [[Changes/OpenCode/2026-10-27-3-projects-and-workspaces-changes-in-v2-2-0|3 Projects and Workspaces changes in v2.2.0]] · Projects and Workspaces
- [[Changes/OpenCode/2026-10-27-opencode-ai-root-is-now-the-promise-api|opencode/ai root is now the Promise API]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-13-developer-workflow-changes-in-v2-2-0|13 Developer Workflow changes in v2.2.0]] · Developer Workflow
- [[Changes/OpenCode/2026-10-27-6-reliability-and-performance-changes-in-v2-2-0|6 Reliability and Performance changes in v2.2.0]] · Reliability and Performance
- [[Changes/OpenCode/2026-10-27-31-other-changes-in-v2-2-0|31 other changes in v2.2.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-27 · OpenClaw · [[Changes/OpenClaw/2026-10-27-9-apps-and-integrations-changes-in-v2026-10-8|9 Apps and Integrations changes in v2026.10.8]]
- Later: 2026-10-27 · OpenHands · [[Changes/OpenHands/2026-10-27-refactor-extensions-name-dialog-viewport-limits-by-enyst-in-https-github-com-ope|refactor(extensions): name dialog viewport limits]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-10-27-57ce0b&body=Card%3A%20Changes%2FOpenCode%2F2026-10-27-tui-plugins-require-opentui-0-7.md%0ACard%20ID%3A%20opencode-2026-10-27-57ce0b%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv2.2.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->