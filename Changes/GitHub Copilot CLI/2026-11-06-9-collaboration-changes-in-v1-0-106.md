---
card_id: github-copilot-cli-2026-11-06-5f6f5f
date: '2026-11-06'
description: 'GitHub Copilot CLI · 2026-11-06 · Collaboration: 9 changes in 1.0.106
  — Ctrl+Y and /share research skip research folder entries that are not readable
  files…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create
    a team here: (source link)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2856
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6f24a975b038e6d15ec09d6e016858833cd775b250a6ac3aaaa2839a205353af
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-11-06-5f6f5f
  comparison: ''
  date: '2026-11-06'
  description: 'GitHub Copilot CLI — 1.0.106: 9 Collaboration changes'
  evidence:
  - quote: Ctrl+Y and /share research skip research folder entries that are not readable
      files, such as a broken link or a folder named like a report, instead of failing
      or offering them.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: /share html exports now keep a numbered list's first number and the checkbox
      and state of task-list items, and both these exports and rich-text copies keep
      the text inside a raw HTML block such as <details> instead of dropping it.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Searching a `/share html` export or an exported research report now highlights
      the text you searched for, instead of a shifted span or a broken emoji, when
      the conversation contains a capital dotted I (İ).
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: HTML exports (`/export html`, `/share html`, research reports) and rich
      text copied with `/copy` keep inline `<br>` line breaks, including in table
      cells, instead of joining the lines
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '/share file and /share html list a message''s images as [Image: name]
      instead of leaving an image-only message blank, and the HTML page title comes
      from the first message with text'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: /share file and /share html no longer keep the quotes around a pasted output
      path in the file name
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: /share research and /share html research add .md or .html to a file path
      given without an extension, as /share file and /share html already do, and the
      saved HTML report now carries a link to open it.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Resumed renamed sessions now show the correct /share heading instead of
      New session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Shared session pages preserve emoji in long titles without replacement
      characters.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 9-collaboration-changes-in-v1-0-106
  source_release: github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4
  source_type: github_releases
  theme: collaboration
  title: 9 Collaboration changes in v1.0.106
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-11-05-allows-authorized-native-commands-to-restore-archived-source-sessions-and-report|Allows
  authorized native commands to restore archived source sessions, and reports…]]'
- '[[Changes/Qoder/2026-11-05-2-collaboration-changes-in-qoder-0-5-5|2 Collaboration
  changes in Qoder 0.5.5]]'
- '[[Changes/Descript/2026-11-06-import-from-other-projects-now-shows-every-project-in-your-drive-not-just-ones-s|Import
  from other projects now shows every project in your drive, not just ones…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4]]'
source_type: github_releases
theme: collaboration
title: 9 Collaboration changes in v1.0.106
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Collaboration changes in v1.0.106

**GitHub Copilot CLI** · 2026-11-06 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.106) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Ctrl+Y and /share research skip research folder entries that are not readable files, such as a broken link or a folder named like a report, instead of failing or offering them.

> /share html exports now keep a numbered list's first number and the checkbox and state of task-list items, and both these exports and rich-text copies keep the text inside a raw HTML block such as \<details> instead of dropping it.

> Searching a `/share html` export or an exported research report now highlights the text you searched for, instead of a shifted span or a broken emoji, when the conversation contains a capital dotted I (İ).

> HTML exports (`/export html`, `/share html`, research reports) and rich text copied with `/copy` keep inline `<br>` line breaks, including in table cells, instead of joining the lines

> /share file and /share html list a message's images as [Image: name] instead of leaving an image-only message blank, and the HTML page title comes from the first message with text

> /share file and /share html no longer keep the quotes around a pasted output path in the file name

> /share research and /share html research add .md or .html to a file path given without an extension, as /share file and /share html already do, and the saved HTML report now carries a link to open it.

> Resumed renamed sessions now show the correct /share heading instead of New session

> Shared session pages preserve emoji in long titles without replacement characters.

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
- [[Changes/GitHub Copilot CLI/2026-11-06-8-mobile-and-desktop-changes-in-v1-0-106|8 Mobile and Desktop changes in v1.0.106]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-11-06-4-projects-and-workspaces-changes-in-v1-0-106|4 Projects and Workspaces changes in v1.0.106]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-11-06-8-accessibility-and-localization-changes-in-v1-0-106|8 Accessibility and Localization changes in v1.0.106]] · Accessibility and Localization
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
## Nearby in Collaboration

- Earlier: 2026-11-06 · Descript · [[Changes/Descript/2026-11-06-import-from-other-projects-now-shows-every-project-in-your-drive-not-just-ones-s|Import from other projects now shows every project in your drive, not just ones…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-01-11 · Descript · [[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create a team here: (source link)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-11-06-5f6f5f&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-11-06-9-collaboration-changes-in-v1-0-106.md%0ACard%20ID%3A%20github-copilot-cli-2026-11-06-5f6f5f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.106%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->