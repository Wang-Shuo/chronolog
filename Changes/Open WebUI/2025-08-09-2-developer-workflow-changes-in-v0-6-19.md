---
card_id: open-webui-2025-08-09-8083ee
date: '2025-08-09'
description: "Open WebUI · 2025-08-09 · Developer Workflow: 2 changes in v0.6.19 —
  \U0001F4E6 **Comprehensive Redis Key Prefixing**: Corrected hardcoded prefixes to
  ensure the…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 875
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bb26eb312e798507a70a981d7b9751fbf4445f877893f65687b085d7d2a1e3ad
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-09-8083ee
  comparison: ''
  date: '2025-08-09'
  description: 'Open WebUI — v0.6.19: 2 Developer Workflow changes'
  evidence:
  - quote: "\U0001F4E6 **Comprehensive Redis Key Prefixing**: Corrected hardcoded
      prefixes to ensure the REDIS_KEY_PREFIX is now respected across all WebSocket
      and task management keys. This prevents data collisions in multi-instance deployments
      and improves compatibility with Redis cluster mode."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '✏️ **Manual Code Block Creation in Chat Restored**: Fixed an issue where
      typing three backticks and then pressing Shift+Enter would incorrectly remove
      the backticks when "Enter to Send" mode was active. This ensures users can reliably
      create multi-line code blocks manually.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-developer-workflow-changes-in-v0-6-19
  source_release: open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243
  source_type: github_releases
  theme: developer-workflow
  title: 2 Developer Workflow changes in v0.6.19
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-08-06-31-developer-workflow-changes-in-v0-1-18|31 Developer
  Workflow changes in v0.1.18]]'
- '[[Changes/Aider/2025-08-09-undo-output-now-shows-only-the-first-line-of-each-commit-message-making-it-easie|/undo
  output now shows only the first line of each commit message, making…]]'
- '[[Changes/Cline/2025-08-09-revert-unnecessary-terminal-command-issue-workarounds-by-saoudrizwan-in-https-gi|Revert
  unnecessary terminal command issue workarounds]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243|open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243]]'
source_type: github_releases
theme: developer-workflow
title: 2 Developer Workflow changes in v0.6.19
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Developer Workflow changes in v0.6.19

**Open WebUI** · 2025-08-09 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.19) · from [[Releases/Open WebUI/open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243|v0.6.19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📦 **Comprehensive Redis Key Prefixing**: Corrected hardcoded prefixes to ensure the REDIS_KEY_PREFIX is now respected across all WebSocket and task management keys. This prevents data collisions in multi-instance deployments and improves compatibility with Redis cluster mode.

> ✏️ **Manual Code Block Creation in Chat Restored**: Fixed an issue where typing three backticks and then pressing Shift+Enter would incorrectly remove the backticks when "Enter to Send" mode was active. This ensures users can reliably create multi-line code blocks manually.

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
- [[Changes/Open WebUI/2025-08-09-enhanced-memory-stability-and-security-refactored-memory-update-and-delete-opera|🧠 Enhanced Memory Stability and Security]] · Memory and Personalization
- [[Changes/Open WebUI/2025-08-09-11-model-support-changes-in-v0-6-19|11 Model Support changes in v0.6.19]] · Model Support
- [[Changes/Open WebUI/2025-08-09-4-account-and-access-changes-in-v0-6-19|4 Account and Access changes in v0.6.19]] · Account and Access
- [[Changes/Open WebUI/2025-08-09-10-safety-and-privacy-changes-in-v0-6-19|10 Safety and Privacy changes in v0.6.19]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-09-3-collaboration-changes-in-v0-6-19|3 Collaboration changes in v0.6.19]] · Collaboration
- [[Changes/Open WebUI/2025-08-09-3-accessibility-and-localization-changes-in-v0-6-19|3 Accessibility and Localization changes in v0.6.19]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-09-13-interface-experience-changes-in-v0-6-19|13 Interface Experience changes in v0.6.19]] · Interface Experience
- [[Changes/Open WebUI/2025-08-09-29-other-changes-in-v0-6-19|29 other changes in v0.6.19]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2025-08-09 · Cline · [[Changes/Cline/2025-08-09-revert-unnecessary-terminal-command-issue-workarounds-by-saoudrizwan-in-https-gi|Revert unnecessary terminal command issue workarounds]]
- Later: 2025-08-11 · Dify · [[Changes/Dify/2025-08-11-4-developer-workflow-changes-in-1-7-2|4 Developer Workflow changes in 1.7.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-09-8083ee&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-09-2-developer-workflow-changes-in-v0-6-19.md%0ACard%20ID%3A%20open-webui-2025-08-09-8083ee%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->