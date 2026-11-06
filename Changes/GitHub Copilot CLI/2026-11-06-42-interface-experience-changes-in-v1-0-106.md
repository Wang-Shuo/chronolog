---
card_id: github-copilot-cli-2026-11-06-c6844c
date: '2026-11-06'
description: 'GitHub Copilot CLI · 2026-11-06 · Interface Experience: 42 changes in
  1.0.106 — The @ file picker now underlines a name with a capital dotted I, such
  as…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1397
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c68cef9cf9b669579f70498ffbb70bd617926764bf802cb629b5ea711320d6fc
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-11-06-c6844c
  comparison: ''
  date: '2026-11-06'
  description: 'GitHub Copilot CLI — 1.0.106: 42 Interface Experience changes'
  evidence:
  - quote: The @ file picker now underlines a name with a capital dotted I, such as
      İstanbul.txt, when the query is typed without the dot, and no longer shortens
      that row's matched folder.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The @ file picker now underlines matches in names stored with decomposed
      accents or found by a query typed without accents, and no longer shortens such
      a row's matched folder.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Model picker leaves more room for choices by budgeting each model's details
      separately
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Show the footer's copy shortcut hint only when copyOnSelect is disabled
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Dismiss the model picker cleanly after resizing the terminal, without leaving
      stale picker text behind
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Command approval prompts and completion notices no longer pass escape sequences
      from a model-written description to the terminal, so that text cannot be hidden,
      recolored or made a link.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Changing a setting through `/experimental`, the status line picker, the
      subagent or extension pickers and similar commands no longer replaces a `settings.json`
      the CLI cannot read with just that one setting. The change is refused with an
      error and the file is left untouched.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Footer text selection highlighting stays aligned while transcript lines
      change
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep /diff comment boxes closed beside the scrollbar, and shorten wide
      or astral file names in their titles without drawing a replacement character.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: In /diff, a mouse click selects the line under the pointer after the view
      scrolls past wrapped lines, and the scrollbar shows when wrapped lines overflow
      the view.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Open extension picker updates failed extensions from "starting" to "failed".
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Empty sessions no longer flash into the session picker before disappearing
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Pressing Enter on a search with no matches in the session browser or the
      custom agent picker, or Tab in the agent picker, no longer adds a space to the
      search text.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: When signed out, the Issues and Pull requests tabs no longer offer a `/`
      search that could only fail with "Search failed."; `/` there now opens the slash-command
      picker, as on the Gists tab.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep the /statusline dialog's preview and toggle descriptions inside its
      border when the sessions sidebar is open.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: On the colorblind theme, unread sessions in the Sessions sidebar and its
      legend are marked with \* instead of the same blue dot as finished sessions.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The terminal cursor no longer stays in an unfocused pane, such as the /config
      right pane after returning to the sidebar
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A directory name containing escape sequences no longer restyles the session
      picker Location column, the footer working directory or the /session info Directory
      row; the path is drawn as plain text
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Escape sequences in a session name, branch or working directory no longer
      restyle rows in the Sessions tab and session pickers, or show up as stray text
      such as [31m on the Sessions sidebar cards; the text is drawn plain
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: In /settings list editors, an item that wraps onto a second line no longer
      pulls its text one column left of the other items and against the selection
      marker
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The /settings value picker no longer draws its options over each other
      or over its border in short terminals, and keeps the highlighted choice on screen.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The /theme picker keeps the highlighted choice visible in short terminals
      by hiding the sample preview and scrolling the list.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Session picker closes immediately after a /resume switch commits
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Shell completion for --model suggests the fusion alias
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep Auto tier details current when provider labels repeat in the model
      picker.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The restore interrupted sessions picker no longer lets keystrokes reach
      the Sessions sidebar or app shortcuts underneath it, so typing in it cannot
      spawn sessions and Ctrl+D no longer quits the CLI.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The selected card in the Sessions sidebar now shows its working spinner,
      plan-mode dot and unread dot on 256-colour and light terminals with the GitHub
      theme, instead of drawing them in the card's own blue
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep resumed transcript position stable while older entries finish rendering.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep /settings search results, selected values, and navigation visible
      when descriptions are long
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Mouse text selection in local tmux sessions also updates the host clipboard
      backend
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep the /theme picker layout within the visible pane in split views
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Issue mention picker preserves Unicode titles and highlights matching text
      correctly
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep /chronicle command names and the active selection visible in narrow
      and short terminals
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Slash-command picker preserves command suffixes and highlights visible
      description matches
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Bare `copilot -r` returns to Sessions after folder trust so saved session
      selection continues correctly
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep the /share research report picker selection visible in short terminals
      while navigating.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Opening /diff now keeps an immediate Down-arrow keypress so selection moves
      on first input
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Status line waits for folder trust before running Git branch and change
      checks.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Autopilot resumes background task and subagent completion notifications
      after a /goal finishes
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Finished background sub-agents in /tasks show how long they ran instead
      of the time until their completion was logged.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Resume picker no longer shows a temporary startup session above saved conversations
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Make /exit close the current session instead of the CLI when the Sessions
      sidebar is open (sidebar.exitClosesSession, on by default), plus opt-in Ctrl+C
      session closing (sidebar.ctrlCClosesSession, off by default, applies to the
      confirming second Ctrl+C on an idle empty prompt)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 42-interface-experience-changes-in-v1-0-106
  source_release: github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4
  source_type: github_releases
  theme: interface-experience
  title: 42 Interface Experience changes in v1.0.106
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-10-29-12-interface-experience-changes-in-rust-v0-166-0|12
  Interface Experience changes in rust-v0.166.0]]'
- '[[Changes/OpenHands/2026-11-03-12-interface-experience-changes-in-v1-35-0|12 Interface
  Experience changes in v1.35.0]]'
- '[[Changes/Codex CLI/2026-11-06-13-interface-experience-changes-in-rust-v0-167-0|13
  Interface Experience changes in rust-v0.167.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4]]'
source_type: github_releases
theme: interface-experience
title: 42 Interface Experience changes in v1.0.106
type: change
---

<!-- chronolog:begin region="header" -->
# 42 Interface Experience changes in v1.0.106

**GitHub Copilot CLI** · 2026-11-06 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.106) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The @ file picker now underlines a name with a capital dotted I, such as İstanbul.txt, when the query is typed without the dot, and no longer shortens that row's matched folder.

> The @ file picker now underlines matches in names stored with decomposed accents or found by a query typed without accents, and no longer shortens such a row's matched folder.

> Model picker leaves more room for choices by budgeting each model's details separately

> Show the footer's copy shortcut hint only when copyOnSelect is disabled

> Dismiss the model picker cleanly after resizing the terminal, without leaving stale picker text behind

> Command approval prompts and completion notices no longer pass escape sequences from a model-written description to the terminal, so that text cannot be hidden, recolored or made a link.

> Changing a setting through `/experimental`, the status line picker, the subagent or extension pickers and similar commands no longer replaces a `settings.json` the CLI cannot read with just that one setting. The change is refused with an error and the file is left untouched.

> Footer text selection highlighting stays aligned while transcript lines change

> Keep /diff comment boxes closed beside the scrollbar, and shorten wide or astral file names in their titles without drawing a replacement character.

> In /diff, a mouse click selects the line under the pointer after the view scrolls past wrapped lines, and the scrollbar shows when wrapped lines overflow the view.

> Open extension picker updates failed extensions from "starting" to "failed".

> Empty sessions no longer flash into the session picker before disappearing

> Pressing Enter on a search with no matches in the session browser or the custom agent picker, or Tab in the agent picker, no longer adds a space to the search text.

> When signed out, the Issues and Pull requests tabs no longer offer a `/` search that could only fail with "Search failed."; `/` there now opens the slash-command picker, as on the Gists tab.

> Keep the /statusline dialog's preview and toggle descriptions inside its border when the sessions sidebar is open.

> On the colorblind theme, unread sessions in the Sessions sidebar and its legend are marked with \* instead of the same blue dot as finished sessions.

> The terminal cursor no longer stays in an unfocused pane, such as the /config right pane after returning to the sidebar

> A directory name containing escape sequences no longer restyles the session picker Location column, the footer working directory or the /session info Directory row; the path is drawn as plain text

> Escape sequences in a session name, branch or working directory no longer restyle rows in the Sessions tab and session pickers, or show up as stray text such as [31m on the Sessions sidebar cards; the text is drawn plain

> In /settings list editors, an item that wraps onto a second line no longer pulls its text one column left of the other items and against the selection marker

> The /settings value picker no longer draws its options over each other or over its border in short terminals, and keeps the highlighted choice on screen.

> The /theme picker keeps the highlighted choice visible in short terminals by hiding the sample preview and scrolling the list.

> Session picker closes immediately after a /resume switch commits

> Shell completion for --model suggests the fusion alias

> Keep Auto tier details current when provider labels repeat in the model picker.

> The restore interrupted sessions picker no longer lets keystrokes reach the Sessions sidebar or app shortcuts underneath it, so typing in it cannot spawn sessions and Ctrl+D no longer quits the CLI.

> The selected card in the Sessions sidebar now shows its working spinner, plan-mode dot and unread dot on 256-colour and light terminals with the GitHub theme, instead of drawing them in the card's own blue

> Keep resumed transcript position stable while older entries finish rendering.

> Keep /settings search results, selected values, and navigation visible when descriptions are long

> Mouse text selection in local tmux sessions also updates the host clipboard backend

> Keep the /theme picker layout within the visible pane in split views

> Issue mention picker preserves Unicode titles and highlights matching text correctly

> Keep /chronicle command names and the active selection visible in narrow and short terminals

> Slash-command picker preserves command suffixes and highlights visible description matches

> Bare `copilot -r` returns to Sessions after folder trust so saved session selection continues correctly

> Keep the /share research report picker selection visible in short terminals while navigating.

> Opening /diff now keeps an immediate Down-arrow keypress so selection moves on first input

> Status line waits for folder trust before running Git branch and change checks.

> Autopilot resumes background task and subagent completion notifications after a /goal finishes

> Finished background sub-agents in /tasks show how long they ran instead of the time until their completion was logged.

> Resume picker no longer shows a temporary startup session above saved conversations

> Make /exit close the current session instead of the CLI when the Sessions sidebar is open (sidebar.exitClosesSession, on by default), plus opt-in Ctrl+C session closing (sidebar.ctrlCClosesSession, off by default, applies to the confirming second Ctrl+C on an idle empty prompt)

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
- [[Changes/GitHub Copilot CLI/2026-11-06-8-accessibility-and-localization-changes-in-v1-0-106|8 Accessibility and Localization changes in v1.0.106]] · Accessibility and Localization
- [[Changes/GitHub Copilot CLI/2026-11-06-17-context-window-changes-in-v1-0-106|17 Context Window changes in v1.0.106]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-11-06-57-editor-experience-changes-in-v1-0-106|57 Editor Experience changes in v1.0.106]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-33-model-support-changes-in-v1-0-106|33 Model Support changes in v1.0.106]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-11-06-89-apps-and-integrations-changes-in-v1-0-106|89 Apps and Integrations changes in v1.0.106]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-11-06-2-image-generation-changes-in-v1-0-106|2 Image Generation changes in v1.0.106]] · Image Generation
- [[Changes/GitHub Copilot CLI/2026-11-06-5-pricing-model-changes-in-v1-0-106|5 Pricing Model changes in v1.0.106]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-11-06-in-the-every-schedule-manager-x-now-removes-the-highlighted-schedule-even-after|In the /every schedule manager, x now removes the highlighted schedule even after…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-11-06-23-account-and-access-changes-in-v1-0-106|23 Account and Access changes in v1.0.106]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-11-06-172-other-changes-in-v1-0-106|172 other changes in v1.0.106]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-11-06 · Codex CLI · [[Changes/Codex CLI/2026-11-06-13-interface-experience-changes-in-rust-v0-167-0|13 Interface Experience changes in rust-v0.167.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-11-06-c6844c&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-11-06-42-interface-experience-changes-in-v1-0-106.md%0ACard%20ID%3A%20github-copilot-cli-2026-11-06-c6844c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.106%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->