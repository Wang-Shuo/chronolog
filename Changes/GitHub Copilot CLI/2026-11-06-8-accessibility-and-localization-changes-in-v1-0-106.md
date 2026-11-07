---
card_id: github-copilot-cli-2026-11-06-78d687
date: '2026-11-06'
description: 'GitHub Copilot CLI · 2026-11-06 · Accessibility and Localization: 8
  changes in 1.0.106 — Keep the Selected marker readable in /settings when screen
  reader mode…'
diffusion:
  first_in_tracked: '[[Changes/Raycast/2020-11-19-improved-searching-for-localized-application-and-preference-names|Improved
    searching for localized application and preference names]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2178
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: accessibility-localization
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c3c2536b70970dec00664072c21b307299cae1b310d361bf0d10c6d5baeeb07f
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-11-06-78d687
  comparison: ''
  date: '2026-11-06'
  description: 'GitHub Copilot CLI — 1.0.106: 8 Accessibility and Localization changes'
  evidence:
  - quote: Keep the Selected marker readable in /settings when screen reader mode
      is enabled
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: With --screen-reader, /plugin, /skills and other labelled lists read their
      rows and their empty message instead of only the list name
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Under `--screen-reader`, the "User message" label on a sent message stays
      on one row beside the message instead of breaking into a column of two-letter
      pieces, and the "Search" label in `/search` and the model picker is now separated
      from the text you type.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: 'With `--screen-reader`, the session browser no longer reads the label
      of its Source tabs twice ("Source: source: current tab").'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: With --screen-reader, the home screen no longer goes blank and stops responding
      in a very small terminal, such as 15 columns by 8 rows.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Text cut to fit the terminal, such as a setting value in `/settings`, a
      cell in the subagent table, or a long objective in the pinned goal panel under
      `--screen-reader`, now ends in an ellipsis instead of stopping mid-word, so
      a cut value no longer reads as a complete one.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: With --screen-reader, failed and rejected tool calls, errors such as an
      unknown command, and warnings now begin with "Error:" or "Warning:" instead
      of reading like any other message.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: In --screen-reader mode, sidebar header buttons click correctly and no
      longer shift layout on focus.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 8-accessibility-and-localization-changes-in-v1-0-106
  source_release: github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4
  source_type: github_releases
  theme: accessibility-localization
  title: 8 Accessibility and Localization changes in v1.0.106
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-10-29-improved-ui-accessibility-screen-reader-and-keyboard-users-can-now-move-through|♿
  Improved UI accessibility. Screen reader and keyboard users can now move…]]'
- '[[Changes/Open WebUI/2026-11-03-accessibility-improvements-screen-reader-users-now-hear-a-name-for-every-window|♿
  Accessibility improvements. Screen reader users now hear a name for every…]]'
- '[[Changes/Dify/2026-11-04-summary-strong-improvements-editing-accessibility-performance-and-operations-str|summarystrongImprovements
  · editing, accessibility, performance…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4]]'
source_type: github_releases
theme: accessibility-localization
title: 8 Accessibility and Localization changes in v1.0.106
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Accessibility and Localization changes in v1.0.106

**GitHub Copilot CLI** · 2026-11-06 · [[Themes/accessibility-localization|Accessibility and Localization]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.106) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Keep the Selected marker readable in /settings when screen reader mode is enabled

> With --screen-reader, /plugin, /skills and other labelled lists read their rows and their empty message instead of only the list name

> Under `--screen-reader`, the "User message" label on a sent message stays on one row beside the message instead of breaking into a column of two-letter pieces, and the "Search" label in `/search` and the model picker is now separated from the text you type.

> With `--screen-reader`, the session browser no longer reads the label of its Source tabs twice ("Source: source: current tab").

> With --screen-reader, the home screen no longer goes blank and stops responding in a very small terminal, such as 15 columns by 8 rows.

> Text cut to fit the terminal, such as a setting value in `/settings`, a cell in the subagent table, or a long objective in the pinned goal panel under `--screen-reader`, now ends in an ellipsis instead of stopping mid-word, so a cut value no longer reads as a complete one.

> With --screen-reader, failed and rejected tool calls, errors such as an unknown command, and warnings now begin with "Error:" or "Warning:" instead of reading like any other message.

> In --screen-reader mode, sidebar header buttons click correctly and no longer shift layout on focus.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.106
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-11-06-4-voice-and-audio-changes-in-v1-0-106|4 Voice and Audio changes in v1.0.106]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-11-06-2-files-and-data-changes-in-v1-0-106|2 Files and Data changes in v1.0.106]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-11-06-3-reliability-and-performance-changes-in-v1-0-106|3 Reliability and Performance changes in v1.0.106]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-11-06-34-agent-mode-changes-in-v1-0-106|34 Agent Mode changes in v1.0.106]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-11-06-10-memory-and-personalization-changes-in-v1-0-106|10 Memory and Personalization changes in v1.0.106]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-11-06-64-developer-workflow-changes-in-v1-0-106|64 Developer Workflow changes in v1.0.106]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-11-06-34-safety-and-privacy-changes-in-v1-0-106|34 Safety and Privacy changes in v1.0.106]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-11-06-9-collaboration-changes-in-v1-0-106|9 Collaboration changes in v1.0.106]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-11-06-8-mobile-and-desktop-changes-in-v1-0-106|8 Mobile and Desktop changes in v1.0.106]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-11-06-4-projects-and-workspaces-changes-in-v1-0-106|4 Projects and Workspaces changes in v1.0.106]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-11-06-17-context-window-changes-in-v1-0-106|17 Context Window changes in v1.0.106]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-11-06-57-editor-experience-changes-in-v1-0-106|57 Editor Experience changes in v1.0.106]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-33-model-support-changes-in-v1-0-106|33 Model Support changes in v1.0.106]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-11-06-89-apps-and-integrations-changes-in-v1-0-106|89 Apps and Integrations changes in v1.0.106]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-11-06-2-image-generation-changes-in-v1-0-106|2 Image Generation changes in v1.0.106]] · Image Generation
- [[Changes/GitHub Copilot CLI/2026-11-06-42-interface-experience-changes-in-v1-0-106|42 Interface Experience changes in v1.0.106]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-5-pricing-model-changes-in-v1-0-106|5 Pricing Model changes in v1.0.106]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-11-06-in-the-every-schedule-manager-x-now-removes-the-highlighted-schedule-even-after|In the /every schedule manager, x now removes the highlighted schedule even after…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-11-06-23-account-and-access-changes-in-v1-0-106|23 Account and Access changes in v1.0.106]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-11-06-172-other-changes-in-v1-0-106|172 other changes in v1.0.106]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Accessibility and Localization

- Earlier: 2026-11-04 · Dify · [[Changes/Dify/2026-11-04-summary-strong-improvements-editing-accessibility-performance-and-operations-str|summarystrongImprovements · editing, accessibility, performance…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-11-19 · Raycast · [[Changes/Raycast/2020-11-19-improved-searching-for-localized-application-and-preference-names|Improved searching for localized application and preference names]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-11-06-78d687&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-11-06-8-accessibility-and-localization-changes-in-v1-0-106.md%0ACard%20ID%3A%20github-copilot-cli-2026-11-06-78d687%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.106%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->