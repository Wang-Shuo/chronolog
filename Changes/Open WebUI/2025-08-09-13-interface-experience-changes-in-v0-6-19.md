---
card_id: open-webui-2025-08-09-f36b7f
date: '2025-08-09'
description: 'Open WebUI · 2025-08-09 · Interface Experience: 13 changes in v0.6.19
  — ✨ **Modernized Sidebar and Major UI Refinements**: The main navigation sidebar
  has been…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2309
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cfbc20fe541678c012f9e3789b720d0185778f247093118b786795fbc40efca2
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-09-f36b7f
  comparison: ''
  date: '2025-08-09'
  description: 'Open WebUI — v0.6.19: 13 Interface Experience changes'
  evidence:
  - quote: '✨ **Modernized Sidebar and Major UI Refinements**: The main navigation
      sidebar has been completely redesigned with a modern, cleaner aesthetic, featuring
      a sticky header and footer to keep key controls accessible. Core sidebar logic,
      like the pinned models list, was also refactored into dedicated components for
      better performance and maintainability.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001FA84 **Guided Response Regeneration**: The \"Regenerate\" button
      has been transformed into a powerful new menu. You can now guide the AI's next
      attempt by suggesting changes in a text prompt, or use one-click options like
      \"Try Again,\" \"Add Details,\" or \"More Concise\" to instantly refine and
      reshape the response to better fit your needs."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F50E **Advanced Chat Search with Status Filters**: Quickly find
      any conversation with powerful new search filters. You can now instantly narrow
      down your chats using prefixes like 'pinned:true', 'shared:true', and 'archived:true'
      directly in the search bar. An intelligent dropdown menu assists you by suggesting
      available filter options as you type, streamlining your workflow and making
      chat management more efficient than ever."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '↕️ **Reorder Pinned Models via Drag-and-Drop**: You can now organize your
      pinned models in the sidebar by simply dragging and dropping them into your
      preferred order. This custom layout is saved automatically, giving you more
      flexible control over your workspace.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F4C1 **Enhanced Folder Chat Management with Sorting and Time Blocks**:
      The chat list within folders now supports comprehensive sorting options by title
      and updated time, along with intelligent time-based grouping (e.g., \"Today,\"
      \"Yesterday\") similar to the main chat view, making navigation and organization
      of project-specific conversations significantly easier."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F6E0️ **Resilient Model Loading**: Fixed an issue where a failure
      in loading the model list (e.g., from a misconfigured provider) would prevent
      the entire user interface, including the admin panel, from loading. The application
      now gracefully handles these errors, ensuring the UI remains accessible."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F3A8 **'Her' Theme Rendering Fixed**: Corrected a bug that caused
      the \"Her\" theme to incorrectly render as a dark theme in some situations.
      The theme now reliably applies its intended light appearance across all sessions."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F4DC **Corrected Markdown Table Line Break Rendering**: Fixed an
      issue where line breaks ('<br>') within Markdown tables were displayed as raw
      HTML instead of being rendered correctly. This ensures that tables with multi-line
      cell content are now displayed as intended."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F6A6 **Corrected App Configuration for Pending Users**: Fixed an
      issue where users awaiting approval could incorrectly load the full application
      interface, leading to a confusing or broken UI. This ensures that only fully
      approved users receive the standard app 'config', resulting in a smoother and
      more reliable onboarding experience."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F4F1 **Mobile User Menu Closing Behavior Fixed**: Resolved an issue
      where the user menu would remain open on mobile devices after selecting an option,
      ensuring the menu correctly closes and returns focus to the main interface for
      a smoother mobile experience."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F4DC **Markdown Line Break Rendering Refinement**: Improved handling
      of line breaks within Markdown rendering for better visual consistency."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '✂️ **Datalab Marker API Language Selection Removed**: The separate language
      selection option for the Datalab Marker API has been removed, as its functionality
      is now integrated and superseded by the more comprehensive ''additional_config''
      parameter. Users should transition to using ''additional_config'' for relevant
      language and processing settings.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F4C4 **Documentation and Releases Links Visibility**: The \"Documentation\"
      and \"Releases\" links in the user menu are now visible only to admin users,
      streamlining the user interface for non-admin roles."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 13-interface-experience-changes-in-v0-6-19
  source_release: open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243
  source_type: github_releases
  theme: interface-experience
  title: 13 Interface Experience changes in v0.6.19
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-08-05-2-interface-experience-changes-in-v0-1-17|2 Interface
  Experience changes in v0.1.17]]'
- '[[Changes/Gemini CLI/2025-08-06-2-interface-experience-changes-in-v0-1-18|2 Interface
  Experience changes in v0.1.18]]'
- '[[Changes/Aider/2025-08-09-clear-now-prints-all-chat-history-cleared-so-you-know-it-worked-by-zexin-yuan|/clear
  now prints “All chat history cleared.” so you know it worked, by Zexin Yuan]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243|open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243]]'
source_type: github_releases
theme: interface-experience
title: 13 Interface Experience changes in v0.6.19
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Interface Experience changes in v0.6.19

**Open WebUI** · 2025-08-09 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.19) · from [[Releases/Open WebUI/open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243|v0.6.19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ✨ **Modernized Sidebar and Major UI Refinements**: The main navigation sidebar has been completely redesigned with a modern, cleaner aesthetic, featuring a sticky header and footer to keep key controls accessible. Core sidebar logic, like the pinned models list, was also refactored into dedicated components for better performance and maintainability.

> 🪄 **Guided Response Regeneration**: The "Regenerate" button has been transformed into a powerful new menu. You can now guide the AI's next attempt by suggesting changes in a text prompt, or use one-click options like "Try Again," "Add Details," or "More Concise" to instantly refine and reshape the response to better fit your needs.

> 🔎 **Advanced Chat Search with Status Filters**: Quickly find any conversation with powerful new search filters. You can now instantly narrow down your chats using prefixes like 'pinned:true', 'shared:true', and 'archived:true' directly in the search bar. An intelligent dropdown menu assists you by suggesting available filter options as you type, streamlining your workflow and making chat management more efficient than ever.

> ↕️ **Reorder Pinned Models via Drag-and-Drop**: You can now organize your pinned models in the sidebar by simply dragging and dropping them into your preferred order. This custom layout is saved automatically, giving you more flexible control over your workspace.

> 📁 **Enhanced Folder Chat Management with Sorting and Time Blocks**: The chat list within folders now supports comprehensive sorting options by title and updated time, along with intelligent time-based grouping (e.g., "Today," "Yesterday") similar to the main chat view, making navigation and organization of project-specific conversations significantly easier.

> 🛠️ **Resilient Model Loading**: Fixed an issue where a failure in loading the model list (e.g., from a misconfigured provider) would prevent the entire user interface, including the admin panel, from loading. The application now gracefully handles these errors, ensuring the UI remains accessible.

> 🎨 **'Her' Theme Rendering Fixed**: Corrected a bug that caused the "Her" theme to incorrectly render as a dark theme in some situations. The theme now reliably applies its intended light appearance across all sessions.

> 📜 **Corrected Markdown Table Line Break Rendering**: Fixed an issue where line breaks ('\<br>') within Markdown tables were displayed as raw HTML instead of being rendered correctly. This ensures that tables with multi-line cell content are now displayed as intended.

> 🚦 **Corrected App Configuration for Pending Users**: Fixed an issue where users awaiting approval could incorrectly load the full application interface, leading to a confusing or broken UI. This ensures that only fully approved users receive the standard app 'config', resulting in a smoother and more reliable onboarding experience.

> 📱 **Mobile User Menu Closing Behavior Fixed**: Resolved an issue where the user menu would remain open on mobile devices after selecting an option, ensuring the menu correctly closes and returns focus to the main interface for a smoother mobile experience.

> 📜 **Markdown Line Break Rendering Refinement**: Improved handling of line breaks within Markdown rendering for better visual consistency.

> ✂️ **Datalab Marker API Language Selection Removed**: The separate language selection option for the Datalab Marker API has been removed, as its functionality is now integrated and superseded by the more comprehensive 'additional_config' parameter. Users should transition to using 'additional_config' for relevant language and processing settings.

> 📄 **Documentation and Releases Links Visibility**: The "Documentation" and "Releases" links in the user menu are now visible only to admin users, streamlining the user interface for non-admin roles.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-09-7-apps-and-integrations-changes-in-v0-6-19|7 Apps and Integrations changes in v0.6.19]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-09-2-editor-experience-changes-in-v0-6-19|2 Editor Experience changes in v0.6.19]] · Editor Experience
- [[Changes/Open WebUI/2025-08-09-3-enterprise-and-administration-changes-in-v0-6-19|3 Enterprise and Administration changes in v0.6.19]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-08-09-2-mobile-and-desktop-changes-in-v0-6-19|2 Mobile and Desktop changes in v0.6.19]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-08-09-2-search-and-browsing-changes-in-v0-6-19|2 Search and Browsing changes in v0.6.19]] · Search and Browsing
- [[Changes/Open WebUI/2025-08-09-customizable-floating-quick-actions-with-tool-support-take-full-control-of-your|✍️ Customizable Floating Quick Actions with Tool Support]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-08-09-15-reliability-and-performance-changes-in-v0-6-19|15 Reliability and Performance changes in v0.6.19]] · Reliability and Performance
- [[Changes/Open WebUI/2025-08-09-2-files-and-data-changes-in-v0-6-19|2 Files and Data changes in v0.6.19]] · Files and Data
- [[Changes/Open WebUI/2025-08-09-folder-system-prompt-variables-restored-fixed-a-bug-where-prompt-variables-e-g-c|📁 Folder System Prompt Variables Restored]] · Context Window
- [[Changes/Open WebUI/2025-08-09-admin-first-whisper-language-priority-the-global-whisper-language-setting-now-ac|🗣️ Admin-First Whisper Language Priority]] · Voice and Audio
- [[Changes/Open WebUI/2025-08-09-2-developer-workflow-changes-in-v0-6-19|2 Developer Workflow changes in v0.6.19]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-09-enhanced-memory-stability-and-security-refactored-memory-update-and-delete-opera|🧠 Enhanced Memory Stability and Security]] · Memory and Personalization
- [[Changes/Open WebUI/2025-08-09-11-model-support-changes-in-v0-6-19|11 Model Support changes in v0.6.19]] · Model Support
- [[Changes/Open WebUI/2025-08-09-4-account-and-access-changes-in-v0-6-19|4 Account and Access changes in v0.6.19]] · Account and Access
- [[Changes/Open WebUI/2025-08-09-10-safety-and-privacy-changes-in-v0-6-19|10 Safety and Privacy changes in v0.6.19]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-09-3-collaboration-changes-in-v0-6-19|3 Collaboration changes in v0.6.19]] · Collaboration
- [[Changes/Open WebUI/2025-08-09-3-accessibility-and-localization-changes-in-v0-6-19|3 Accessibility and Localization changes in v0.6.19]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-09-29-other-changes-in-v0-6-19|29 other changes in v0.6.19]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2025-08-09 · Aider · [[Changes/Aider/2025-08-09-clear-now-prints-all-chat-history-cleared-so-you-know-it-worked-by-zexin-yuan|/clear now prints “All chat history cleared.” so you know it worked, by Zexin Yuan]]
- Later: 2025-08-11 · Dify · [[Changes/Dify/2025-08-11-4-interface-experience-changes-in-1-7-2|4 Interface Experience changes in 1.7.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-09-f36b7f&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-09-13-interface-experience-changes-in-v0-6-19.md%0ACard%20ID%3A%20open-webui-2025-08-09-f36b7f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->