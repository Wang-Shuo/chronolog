---
card_id: github-copilot-cli-2026-07-30-9ec8bb
date: '2026-07-30'
description: 'GitHub Copilot CLI · 2026-07-30 · Other changes: 10 changes in 1.0.76
  — Unsent prompt text now stays with the session it was typed for (for the rest of
  the CLI…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2ee18c9033ebd0969ad5c9eb517263223e77cc58e84ff654bfdf93754a56d878
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-07-30-9ec8bb
  comparison: ''
  date: '2026-07-30'
  description: 'GitHub Copilot CLI — 1.0.76: 10 other changes'
  evidence:
  - quote: Unsent prompt text now stays with the session it was typed for (for the
      rest of the CLI session) instead of following you to the session you switch
      to
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  - quote: Resuming a session now restores its autopilot or plan mode instead of reverting
      to interactive, so the autopilot-only `task_complete` tool stays available and
      the mode matches the session you left
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  - quote: When an update is auto-downloaded, the notification suggests /restart and
      drops the warning color
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  - quote: Render inline images in Rio terminals that support Kitty graphics
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  - quote: Sandboxed searches now offer an immediate bypass prompt and avoid duplicate
      bypass prompts.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  - quote: Show the number of active scheduled prompts in the footer
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  - quote: Add /limits predict to suggest a session AI-credit limit from similar sessions.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  - quote: Queued messages list no longer shows a blank row or inflated count, and
      Ctrl+C removes your own newest queued message
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  - quote: Changing the `mouse` setting mid-session now takes effect immediately,
      from both `/settings mouse on|off` and the `/settings` dialog, instead of being
      saved but ignored until the CLI restarted
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  - quote: Autopilot stays selected after task_complete by default; set stayInAutopilot
      to false to return to interactive mode after each task
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 10-other-changes-in-v1-0-76
  source_release: github-copilot-cli-2026-07-30-v1-0-76-github-362129864-0932fe29
  source_type: github_releases
  theme: uncategorized
  title: 10 other changes in v1.0.76
  type: change
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-30-v1-0-76-github-362129864-0932fe29|github-copilot-cli-2026-07-30-v1-0-76-github-362129864-0932fe29]]'
source_type: github_releases
theme: uncategorized
title: 10 other changes in v1.0.76
type: change
---

<!-- chronolog:begin region="header" -->
# 10 other changes in v1.0.76

**GitHub Copilot CLI** · 2026-07-30 · Other changes · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.76) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-30-v1-0-76-github-362129864-0932fe29|1.0.76]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Unsent prompt text now stays with the session it was typed for (for the rest of the CLI session) instead of following you to the session you switch to

> Resuming a session now restores its autopilot or plan mode instead of reverting to interactive, so the autopilot-only `task_complete` tool stays available and the mode matches the session you left

> When an update is auto-downloaded, the notification suggests /restart and drops the warning color

> Render inline images in Rio terminals that support Kitty graphics

> Sandboxed searches now offer an immediate bypass prompt and avoid duplicate bypass prompts.

> Show the number of active scheduled prompts in the footer

> Add /limits predict to suggest a session AI-credit limit from similar sessions.

> Queued messages list no longer shows a blank row or inflated count, and Ctrl+C removes your own newest queued message

> Changing the `mouse` setting mid-session now takes effect immediately, from both `/settings mouse on|off` and the `/settings` dialog, instead of being saved but ignored until the CLI restarted

> Autopilot stays selected after task_complete by default; set stayInAutopilot to false to return to interactive mode after each task

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.76
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-07-30-5-safety-and-privacy-changes-in-v1-0-76|5 Safety and Privacy changes in v1.0.76]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-07-30-a-userpromptsubmitted-hook-returning-a-non-string-value-for-modifiedprompt-modif|A userPromptSubmitted hook returning a non-string value for modifiedPrompt…]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-07-30-diff-scrolls-and-syntax-highlights-large-multi-file-diffs-faster|/diff scrolls and syntax-highlights large multi-file diffs faster]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-07-30-2-developer-workflow-changes-in-v1-0-76|2 Developer Workflow changes in v1.0.76]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-07-30-2-apps-and-integrations-changes-in-v1-0-76|2 Apps and Integrations changes in v1.0.76]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-07-30-2-model-support-changes-in-v1-0-76|2 Model Support changes in v1.0.76]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-07-30-restore-the-early-warning-when-unreclaimable-system-and-tool-context-nears-the-l|Restore the early warning when unreclaimable system and tool context nears…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-07-30-voice-mode-pauses-playing-media-before-recording-and-resumes-it-afterward-where|Voice mode pauses playing media before recording and resumes it afterward, where…]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-07-30-2-agent-mode-changes-in-v1-0-76|2 Agent Mode changes in v1.0.76]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-07-30-2-editor-experience-changes-in-v1-0-76|2 Editor Experience changes in v1.0.76]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-07-30-4-interface-experience-changes-in-v1-0-76|4 Interface Experience changes in v1.0.76]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-07-30-9ec8bb&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-07-30-10-other-changes-in-v1-0-76.md%0ACard%20ID%3A%20github-copilot-cli-2026-07-30-9ec8bb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.76%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->