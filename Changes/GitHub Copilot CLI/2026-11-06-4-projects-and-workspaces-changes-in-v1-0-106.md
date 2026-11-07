---
card_id: github-copilot-cli-2026-11-06-69afe3
date: '2026-11-06'
description: 'GitHub Copilot CLI · 2026-11-06 · Projects and Workspaces: 4 changes
  in 1.0.106 — ACP sessions now appear in session history, /chronicle, and session_store_sql…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-conversation-history-you-ll-soon-be-able-to-view-past-conversations-with-chatgpt|Conversation
    history: You’ll soon be able to view past conversations with ChatGPT…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1422
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: projects-workspaces
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 732daa67a05291e30548fe18494f113049ea46e28e6f1c1e4b1115c2e833ad12
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-11-06-69afe3
  comparison: ''
  date: '2026-11-06'
  description: 'GitHub Copilot CLI — 1.0.106: 4 Projects and Workspaces changes'
  evidence:
  - quote: ACP sessions now appear in session history, /chronicle, and session_store_sql
      results.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A telemetry-disabled warning raised while resuming a session is saved to
      the session history, so later events no longer reference a missing parent.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: With context management tools on, session_history search now matches the
      conversation text, so a query that contains a line break, a quote or a backslash
      finds the message it was copied from, and read_item returns the message text
      instead of its JSON encoding.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A session.resume request whose params are not a JSON object now fails with
      an error instead of crashing the copilot --server process
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 4-projects-and-workspaces-changes-in-v1-0-106
  source_release: github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4
  source_type: github_releases
  theme: projects-workspaces
  title: 4 Projects and Workspaces changes in v1.0.106
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-13-claude-cli-session-tools-later-turns-keep-their-authorized-session-history-and-a|Claude
  CLI session tools]]'
- '[[Changes/OpenCode/2026-10-27-3-projects-and-workspaces-changes-in-v2-2-0|3 Projects
  and Workspaces changes in v2.2.0]]'
- '[[Changes/Codex CLI/2026-10-29-57342-separate-tui-session-resume-preparation-from-activation-bc-openai|♯57342
  Separate TUI session resume preparation from activation @bc-openai]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4]]'
source_type: github_releases
theme: projects-workspaces
title: 4 Projects and Workspaces changes in v1.0.106
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Projects and Workspaces changes in v1.0.106

**GitHub Copilot CLI** · 2026-11-06 · [[Themes/projects-workspaces|Projects and Workspaces]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.106) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ACP sessions now appear in session history, /chronicle, and session_store_sql results.

> A telemetry-disabled warning raised while resuming a session is saved to the session history, so later events no longer reference a missing parent.

> With context management tools on, session_history search now matches the conversation text, so a query that contains a line break, a quote or a backslash finds the message it was copied from, and read_item returns the message text instead of its JSON encoding.

> A session.resume request whose params are not a JSON object now fails with an error instead of crashing the copilot --server process

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
## Nearby in Projects and Workspaces

- Earlier: 2026-10-29 · Codex CLI · [[Changes/Codex CLI/2026-10-29-57342-separate-tui-session-resume-preparation-from-activation-bc-openai|♯57342 Separate TUI session resume preparation from activation @bc-openai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-conversation-history-you-ll-soon-be-able-to-view-past-conversations-with-chatgpt|Conversation history: You’ll soon be able to view past conversations with ChatGPT…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-11-06-69afe3&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-11-06-4-projects-and-workspaces-changes-in-v1-0-106.md%0ACard%20ID%3A%20github-copilot-cli-2026-11-06-69afe3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.106%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->