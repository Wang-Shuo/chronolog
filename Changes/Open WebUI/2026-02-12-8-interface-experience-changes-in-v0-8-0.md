---
card_id: open-webui-2026-02-12-c44ac4
date: '2026-02-12'
description: "Open WebUI · 2026-02-12 · Interface Experience: 8 changes in v0.8.0
  — \U0001F4A1 **Active task sidebar indicator.** Users can now see which chats have
  active tasks…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2496
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d98f947d92c08605976d38d85bf8977a86ba024bc4299977720810bdbf7ff8f5
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-12-c44ac4
  comparison: ''
  date: '2026-02-12'
  description: 'Open WebUI — v0.8.0: 8 Interface Experience changes'
  evidence:
  - quote: "\U0001F4A1 **Active task sidebar indicator.** Users can now see which
      chats have active tasks running directly in the sidebar. [Commit](https://github.com/open-webui/open-webui/commit/48522271586a5bf24b649610f03b4ffd8afb2782)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: ⌨️ **Model selector shortcut.** The model selector can now be opened with
      Ctrl+Shift+M keyboard shortcut. [#21130](https://github.com/open-webui/open-webui/pull/21130)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4C4 **Prompts workspace pagination.** The prompts workspace now
      includes pagination for large prompt collections, loading 30 prompts at a time
      with search, filtering, and sorting capabilities for improved performance and
      navigation. [Commit](https://github.com/open-webui/open-webui/commit/36766f157d46102fd76c526b42579400ca70de50)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F3A8 **Action function HTML rendering.** Action functions can now
      render rich HTML content directly in chat as embedded iframes, matching the
      capabilities that tools already had and eliminating the need for action authors
      to inject codeblocks. [#21294](https://github.com/open-webui/open-webui/pull/21294),
      [Commit](https://github.com/open-webui/open-webui/commit/60ada21c152ed642971429fdbe88dcbf478cf83a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F524 **Alphabetical tool ordering.** Tools and Functions in the
      Chat Controls sidebar now appear in alphabetical order, making it easier to
      locate specific tools when working with multiple integrations. [#20871](https://github.com/open-webui/open-webui/pull/20871)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F680 **Status indicator GPU usage fix.** High GPU usage caused by
      the user online status indicator animation has been resolved, reducing consumption
      from 35-40% to near-zero in browsers with hardware acceleration. [#21062](https://github.com/open-webui/open-webui/issues/21062),
      [Commit](https://github.com/open-webui/open-webui/commit/938d1b0743c64f0ce513d68e57dfbb86987cb06b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4AC **Reference Chats visibility fix.** The \"Reference Chats\"
      option now appears in the message input menu even when the sidebar is collapsed,
      fixing the issue where it was hidden on mobile devices and at first load. [#20827](https://github.com/open-webui/open-webui/issues/20827),
      [Commit](https://github.com/open-webui/open-webui/commit/a3600e8b219fc4c019b95258d16bd3e2827490c6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F30D **RTL table rendering fix.** Chat markdown tables now correctly
      display right-to-left when containing RTL language content (Arabic, Hebrew,
      Farsi, etc.), matching the \"Auto\" direction setting behavior. [#21160](https://github.com/open-webui/open-webui/issues/21160),
      [Commit](https://github.com/open-webui/open-webui/commit/284b97bd84c824013ad00ea07621192ec69a5e93)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 8-interface-experience-changes-in-v0-8-0
  source_release: open-webui-2026-02-12-v0-8-0-github-285910626-490914ba
  source_type: github_releases
  theme: interface-experience
  title: 8 Interface Experience changes in v0.8.0
  type: change
related_changes:
- '[[Changes/Cline/2026-02-12-2-interface-experience-changes-in-v3-58-0|2 Interface
  Experience changes in v3.58.0]]'
- '[[Changes/GitHub Copilot CLI/2026-02-12-diff-uses-full-screen-in-alt-screen-mode|/diff
  uses full screen in alt-screen mode]]'
- '[[Changes/GitHub Copilot CLI/2026-02-12-add-mouse-text-selection-in-alt-screen-mode|Add
  mouse text selection in --alt-screen mode]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|open-webui-2026-02-12-v0-8-0-github-285910626-490914ba]]'
source_type: github_releases
theme: interface-experience
title: 8 Interface Experience changes in v0.8.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Interface Experience changes in v0.8.0

**Open WebUI** · 2026-02-12 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.0) · from [[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|v0.8.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 💡 **Active task sidebar indicator.** Users can now see which chats have active tasks running directly in the sidebar. [Commit](https://github.com/open-webui/open-webui/commit/48522271586a5bf24b649610f03b4ffd8afb2782)

> ⌨️ **Model selector shortcut.** The model selector can now be opened with Ctrl+Shift+M keyboard shortcut. [#21130](https://github.com/open-webui/open-webui/pull/21130)

> 📄 **Prompts workspace pagination.** The prompts workspace now includes pagination for large prompt collections, loading 30 prompts at a time with search, filtering, and sorting capabilities for improved performance and navigation. [Commit](https://github.com/open-webui/open-webui/commit/36766f157d46102fd76c526b42579400ca70de50)

> 🎨 **Action function HTML rendering.** Action functions can now render rich HTML content directly in chat as embedded iframes, matching the capabilities that tools already had and eliminating the need for action authors to inject codeblocks. [#21294](https://github.com/open-webui/open-webui/pull/21294), [Commit](https://github.com/open-webui/open-webui/commit/60ada21c152ed642971429fdbe88dcbf478cf83a)

> 🔤 **Alphabetical tool ordering.** Tools and Functions in the Chat Controls sidebar now appear in alphabetical order, making it easier to locate specific tools when working with multiple integrations. [#20871](https://github.com/open-webui/open-webui/pull/20871)

> 🚀 **Status indicator GPU usage fix.** High GPU usage caused by the user online status indicator animation has been resolved, reducing consumption from 35-40% to near-zero in browsers with hardware acceleration. [#21062](https://github.com/open-webui/open-webui/issues/21062), [Commit](https://github.com/open-webui/open-webui/commit/938d1b0743c64f0ce513d68e57dfbb86987cb06b)

> 💬 **Reference Chats visibility fix.** The "Reference Chats" option now appears in the message input menu even when the sidebar is collapsed, fixing the issue where it was hidden on mobile devices and at first load. [#20827](https://github.com/open-webui/open-webui/issues/20827), [Commit](https://github.com/open-webui/open-webui/commit/a3600e8b219fc4c019b95258d16bd3e2827490c6)

> 🌍 **RTL table rendering fix.** Chat markdown tables now correctly display right-to-left when containing RTL language content (Arabic, Hebrew, Farsi, etc.), matching the "Auto" direction setting behavior. [#21160](https://github.com/open-webui/open-webui/issues/21160), [Commit](https://github.com/open-webui/open-webui/commit/284b97bd84c824013ad00ea07621192ec69a5e93)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-12-16-reliability-and-performance-changes-in-v0-8-0|16 Reliability and Performance changes in v0.8.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-12-audio-service-timeout-handling-audio-transcription-and-text-to-speech-requests-n|🔌 Audio service timeout handling. Audio transcription and text-to-speech…]] · Voice and Audio
- [[Changes/Open WebUI/2026-02-12-2-editor-experience-changes-in-v0-8-0|2 Editor Experience changes in v0.8.0]] · Editor Experience
- [[Changes/Open WebUI/2026-02-12-5-safety-and-privacy-changes-in-v0-8-0|5 Safety and Privacy changes in v0.8.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-02-12-19-model-support-changes-in-v0-8-0|19 Model Support changes in v0.8.0]] · Model Support
- [[Changes/Open WebUI/2026-02-12-27-developer-workflow-changes-in-v0-8-0|27 Developer Workflow changes in v0.8.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-12-5-context-window-changes-in-v0-8-0|5 Context Window changes in v0.8.0]] · Context Window
- [[Changes/Open WebUI/2026-02-12-2-image-generation-changes-in-v0-8-0|2 Image Generation changes in v0.8.0]] · Image Generation
- [[Changes/Open WebUI/2026-02-12-2-memory-and-personalization-changes-in-v0-8-0|2 Memory and Personalization changes in v0.8.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-02-12-gboard-multi-line-paste-fix-multi-line-text-pasted-from-gboard-on-android-now-in|📱 Gboard multi-line paste fix. Multi-line text pasted from Gboard on Android now…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-02-12-2-collaboration-changes-in-v0-8-0|2 Collaboration changes in v0.8.0]] · Collaboration
- [[Changes/Open WebUI/2026-02-12-6-account-and-access-changes-in-v0-8-0|6 Account and Access changes in v0.8.0]] · Account and Access
- [[Changes/Open WebUI/2026-02-12-async-pipeline-operations-pipeline-operations-now-run-asynchronously-instead-of|🔧 Async pipeline operations. Pipeline operations now run asynchronously instead…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-02-12-5-search-and-browsing-changes-in-v0-8-0|5 Search and Browsing changes in v0.8.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-02-12-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-02-12-screen-reader-accessibility-screen-reader-users-now-hear-the-password-field-labe|♿ Screen reader accessibility. Screen reader users now hear the password field…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-02-12-10-files-and-data-changes-in-v0-8-0|10 Files and Data changes in v0.8.0]] · Files and Data
- [[Changes/Open WebUI/2026-02-12-6-apps-and-integrations-changes-in-v0-8-0|6 Apps and Integrations changes in v0.8.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-02-12-29-other-changes-in-v0-8-0|29 other changes in v0.8.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-02-12 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-12-add-mouse-text-selection-in-alt-screen-mode|Add mouse text selection in --alt-screen mode]]
- Later: 2026-02-12 · OpenCode · [[Changes/OpenCode/2026-02-12-core-windows-selection-behavior-and-manual-ctrl-c-handling|Core Windows selection behavior and manual Ctrl+C handling]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-12-c44ac4&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-12-8-interface-experience-changes-in-v0-8-0.md%0ACard%20ID%3A%20open-webui-2026-02-12-c44ac4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->